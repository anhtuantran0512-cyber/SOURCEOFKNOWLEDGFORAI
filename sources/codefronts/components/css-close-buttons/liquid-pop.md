---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/liquid-pop/"
title: "Liquid Pop Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A gooey blob dismiss: the button sits inside an SVG feGaussianBlur + feColorMatrix \"metaball\" filter, so on hover two satellite droplets squeeze OUT of the…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Pop Close Button
Source: https://codefronts.com/components/css-close-buttons/liquid-pop/

A gooey blob dismiss: the button sits inside an SVG feGaussianBlur + feColorMatrix "metaball" filter, so on hover two satellite droplets squeeze OUT of the main circle, wobble, and merge back — real liquid physics faked entirely with the classic goo filter and elastic keyframes.
## HTML
```html
<section class="ccb-15" aria-label="Liquid goo close button demo">
  <svg class="ccb-15__defs" width="0" height="0" aria-hidden="true"><defs>
    <filter id="ccb-15-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="g"/><feComposite in="SourceGraphic" in2="g" operator="atop"/></filter>
  </defs></svg>
  <div class="ccb-15__stack">
    <div class="ccb-15__goo" aria-hidden="true">
      <span class="ccb-15__blob ccb-15__blob--main"></span>
      <span class="ccb-15__blob ccb-15__blob--sat1"></span>
      <span class="ccb-15__blob ccb-15__blob--sat2"></span>
    </div>
    <button class="ccb-15__close" type="button" aria-label="Close">
      <span class="ccb-15__x" aria-hidden="true"></span>
    </button>
  </div>
</section>
```
## CSS
```css
.ccb-15,
.ccb-15 *,
.ccb-15 *::before,
.ccb-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-15 {
  --goo: oklch(0.65 0.22 350);
  --fling: 38px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,oklch(0.96 0.012 350),oklch(0.92 0.03 340));
}

.ccb-15 .ccb-15__defs {
  position: absolute;
}

.ccb-15 .ccb-15__stack {
  position: relative;
  display: grid;
  place-items: center;
  width: 130px;
  height: 130px;
}

.ccb-15 .ccb-15__goo {
  position: absolute;
  inset: 0;
  filter: url(#ccb-15-goo);
  display: grid;
  place-items: center;
}

.ccb-15 .ccb-15__blob {
  position: absolute;
  border-radius: 50%;
  background: var(--goo);
}

.ccb-15 .ccb-15__blob--main {
  width: 64px;
  height: 64px;
}

.ccb-15 .ccb-15__blob--sat1 {
  width: 20px;
  height: 20px;
  transition: transform .55s cubic-bezier(.68,-.55,.265,1.55);
}

.ccb-15 .ccb-15__blob--sat2 {
  width: 14px;
  height: 14px;
  transition: transform .55s cubic-bezier(.68,-.55,.265,1.55) .04s;
}

.ccb-15 .ccb-15__stack:hover .ccb-15__blob--sat1 {
  transform: translate(calc(var(--fling) * 1),calc(var(--fling) * -0.7));
}

.ccb-15 .ccb-15__stack:hover .ccb-15__blob--sat2 {
  transform: translate(calc(var(--fling) * -0.9),calc(var(--fling) * 0.8));
}

.ccb-15 .ccb-15__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 64px;
  height: 64px;
  border: none;
  border-radius: 50%;
  background: transparent;
  cursor: pointer;
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.ccb-15 .ccb-15__close:hover {
  transform: scale(1.06);
}

.ccb-15 .ccb-15__close:active {
  transform: scale(.9);
}

.ccb-15 .ccb-15__close:focus-visible {
  outline: 3px solid var(--goo);
  outline-offset: 4px;
  border-radius: 50%;
}

.ccb-15 .ccb-15__x {
  position: relative;
  width: 22px;
  height: 22px;
}

.ccb-15 .ccb-15__x::before,
.ccb-15 .ccb-15__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 22px;
  height: 3px;
  border-radius: 3px;
  background: #fff;
}

.ccb-15 .ccb-15__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-15 .ccb-15__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-15 .ccb-15__blob--sat1,
    .ccb-15 .ccb-15__blob--sat2,
    .ccb-15 .ccb-15__close {
    transition: none;
  }

  .ccb-15 .ccb-15__stack:hover .ccb-15__blob--sat1,
    .ccb-15 .ccb-15__stack:hover .ccb-15__blob--sat2 {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — feGaussianBlur + feColorMatrix re-threshold overlapping blurs into liquid; elastic beziers fling the droplets. */
```
