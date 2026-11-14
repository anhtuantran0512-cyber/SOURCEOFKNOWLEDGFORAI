---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/pure-css-animated-border-trace-button/"
title: "Pure CSS Animated Border Trace Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "A single comet of light sweeps the button's perimeter on hover — no SVG, no JavaScript."
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Animated Border Trace Button
Source: https://codefronts.com/components/css-glowing-border-buttons/pure-css-animated-border-trace-button/

A single comet of light sweeps the button's perimeter on hover — no SVG, no JavaScript. A rotating conic-gradient wedge is clipped to a 2px border ring with the mask-composite trick, so the beam hugs any border-radius perfectly. The go-to 'expensive detail' for portfolio and dev-tool sites.
## HTML
```html
<section class="gbb-03" aria-label="Animated border trace button demo">
  <a class="gbb-03__btn" href="#">View Case Study<span class="gbb-03__arrow" aria-hidden="true">&rarr;</span></a>
</section>
```
## CSS
```css
.gbb-03,
.gbb-03 *,
.gbb-03 *::before,
.gbb-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --gbb-a3 {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.gbb-03 {
  --beam: oklch(0.85 0.12 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.16 0.015 260),oklch(0.12 0.01 260));
}

.gbb-03 .gbb-03__btn {
  position: relative;
  isolation: isolate;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 16px 30px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.14);
  background: oklch(0.18 0.015 260);
  font: 600 15px/1 'Segoe UI',system-ui,sans-serif;
  color: #f2f5f8;
  text-decoration: none;
  transition: border-color .3s ease;
}

.gbb-03 .gbb-03__btn::before,
.gbb-03 .gbb-03__btn::after {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  padding: 2px;
  background: conic-gradient(from var(--gbb-a3),transparent 0 82%,color-mix(in oklab,var(--beam) 45%,transparent) 88%,var(--beam) 93%,transparent 97%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s ease;
}

.gbb-03 .gbb-03__btn::after {
  filter: blur(8px);
  inset: -3px;
  padding: 4px;
}

.gbb-03 .gbb-03__btn:hover,
.gbb-03 .gbb-03__btn:focus-visible {
  border-color: rgba(255,255,255,.22);
}

.gbb-03 .gbb-03__btn:hover::before,
.gbb-03 .gbb-03__btn:hover::after,
.gbb-03 .gbb-03__btn:focus-visible::before,
.gbb-03 .gbb-03__btn:focus-visible::after {
  opacity: 1;
  animation: gbb03-lap 1.4s linear infinite;
}

.gbb-03 .gbb-03__btn:focus-visible {
  outline: 2px solid var(--beam);
  outline-offset: 4px;
}

.gbb-03 .gbb-03__arrow {
  transition: translate .3s ease;
}

.gbb-03 .gbb-03__btn:hover .gbb-03__arrow {
  translate: 4px 0;
}

@keyframes gbb03-lap {
  to {
    --gbb-a3: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-03 .gbb-03__btn:hover::before,
    .gbb-03 .gbb-03__btn:hover::after,
    .gbb-03 .gbb-03__btn:focus-visible::before,
    .gbb-03 .gbb-03__btn:focus-visible::after {
    animation: none;
    opacity: .6;
  }
}
```

## JavaScript
```js
/* No JavaScript — a conic-gradient comet wedge is clipped to a 2px ring with mask-composite:exclude and spun via an @property angle. */
```
