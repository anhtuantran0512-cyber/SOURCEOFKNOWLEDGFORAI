---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/snap-cross/"
title: "Snap Cross Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "Motion-design fundamentals in one button: on hover the × whips 90° with a spring bezier that overshoots to ~104° before wobbling home —…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Snap Cross Close Button
Source: https://codefronts.com/components/css-close-buttons/snap-cross/

Motion-design fundamentals in one button: on hover the × whips 90° with a spring bezier that overshoots to ~104° before wobbling home — cubic-bezier(0.68,-0.55,0.265,1.55), the famous 'back' easing. The demo renders its own easing curve as a background diagram, making it a teaching tool for custom timing functions.
## HTML
```html
<section class="ccb-20" aria-label="Spring snap close button demo">
  <button class="ccb-20__close" type="button" aria-label="Close">
    <span class="ccb-20__x" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
.ccb-20,
.ccb-20 *,
.ccb-20 *::before,
.ccb-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-20 {
  --accent: oklch(0.68 0.19 35);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.96 0.01 35),oklch(0.92 0.02 40));
}

.ccb-20 .ccb-20__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 80px;
  height: 80px;
  border: 2px solid oklch(0.85 0.03 35);
  border-radius: 22px;
  cursor: pointer;
  background: radial-gradient(circle,oklch(0.85 0.02 35 / .6) 1px,transparent 1.5px) 0 0/10px 10px,linear-gradient(0deg,transparent calc(50% - .5px),oklch(0.85 0.03 35) calc(50% - .5px) calc(50% + .5px),transparent calc(50% + .5px)),linear-gradient(90deg,transparent calc(50% - .5px),oklch(0.85 0.03 35) calc(50% - .5px) calc(50% + .5px),transparent calc(50% + .5px)),#fff;
  transition: transform .5s cubic-bezier(.68,-.55,.265,1.55),border-color .2s ease;
  box-shadow: 0 16px 36px -22px oklch(0.5 0.1 35 / .6);
}

.ccb-20 .ccb-20__x {
  position: relative;
  width: 26px;
  height: 26px;
  transition: transform .5s cubic-bezier(.68,-.55,.265,1.55);
}

.ccb-20 .ccb-20__x::before,
.ccb-20 .ccb-20__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 26px;
  height: 3.5px;
  border-radius: 3px;
  background: var(--accent);
}

.ccb-20 .ccb-20__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-20 .ccb-20__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-20 .ccb-20__close:hover .ccb-20__x {
  transform: rotate(90deg);
}

.ccb-20 .ccb-20__close:hover {
  border-color: var(--accent);
}

.ccb-20 .ccb-20__close:active {
  transform: scale(.9);
}

.ccb-20 .ccb-20__close:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-20 .ccb-20__close,
    .ccb-20 .ccb-20__x {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — cubic-bezier(.68,-.55,.265,1.55): y<0 winds up, y>1 overshoots; the browser interpolates the whole spring. */
```
