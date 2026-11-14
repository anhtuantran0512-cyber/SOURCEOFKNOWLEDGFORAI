---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/trash-compactor/"
title: "Trash Compactor Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "An industrial squeeze: the × sits between two heavy press plates that slam vertically inward on hover, crushing the glyph — bars compress via scaleY, bow…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Trash Compactor Close Button
Source: https://codefronts.com/components/css-close-buttons/trash-compactor/

An industrial squeeze: the × sits between two heavy press plates that slam vertically inward on hover, crushing the glyph — bars compress via scaleY, bow outward via scaleX, and the whole assembly settles into a flattened bar with a satisfying clunk bezier. Great for delete-flavored dismissals.
## HTML
```html
<section class="ccb-17" aria-label="Trash compactor close button demo">
  <button class="ccb-17__close" type="button" aria-label="Close">
    <span class="ccb-17__plate ccb-17__plate--top" aria-hidden="true"></span>
    <span class="ccb-17__x" aria-hidden="true"></span>
    <span class="ccb-17__plate ccb-17__plate--bot" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
.ccb-17,
.ccb-17 *,
.ccb-17 *::before,
.ccb-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-17 {
  --crush: .22;
  --steel: oklch(0.75 0.02 250);
  --ease: cubic-bezier(.6,-.28,.55,1.32);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.32 0.02 255),oklch(0.22 0.015 250));
}

.ccb-17 .ccb-17__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 76px;
  height: 76px;
  border: 1px solid oklch(0.5 0.02 250 / .6);
  border-radius: 14px;
  background: linear-gradient(180deg,oklch(0.4 0.02 250),oklch(0.3 0.02 250));
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 16px 36px -18px rgba(0,0,0,.85),inset 0 1px 0 oklch(0.55 0.02 250 / .5);
}

.ccb-17 .ccb-17__plate {
  position: absolute;
  inset-inline: 10px;
  height: 8px;
  border-radius: 3px;
  background: linear-gradient(180deg,var(--steel),oklch(0.55 0.02 250));
  box-shadow: 0 2px 4px rgba(0,0,0,.5);
  transition: transform .34s var(--ease);
}

.ccb-17 .ccb-17__plate--top {
  top: 8px;
}

.ccb-17 .ccb-17__plate--bot {
  bottom: 8px;
}

.ccb-17 .ccb-17__x {
  position: relative;
  width: 24px;
  height: 24px;
  transform-origin: center;
  transition: transform .34s var(--ease);
}

.ccb-17 .ccb-17__x::before,
.ccb-17 .ccb-17__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 24px;
  height: 3px;
  border-radius: 2px;
  background: oklch(0.92 0.01 250);
  transition: border-radius .34s var(--ease);
}

.ccb-17 .ccb-17__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-17 .ccb-17__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-17 .ccb-17__close:hover .ccb-17__plate--top {
  transform: translateY(15px);
}

.ccb-17 .ccb-17__close:hover .ccb-17__plate--bot {
  transform: translateY(-15px);
}

.ccb-17 .ccb-17__close:hover .ccb-17__x {
  transform: scaleY(var(--crush)) scaleX(1.25);
}

.ccb-17 .ccb-17__close:hover .ccb-17__x::before,
.ccb-17 .ccb-17__close:hover .ccb-17__x::after {
  border-radius: 4px;
}

.ccb-17 .ccb-17__close:active {
  transform: scale(.95);
}

.ccb-17 .ccb-17__close:focus-visible {
  outline: 3px solid oklch(0.8 0.1 250);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-17 .ccb-17__plate,
    .ccb-17 .ccb-17__x {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — plates translate inward while the × scaleY-crushes and scaleX-bows; one anticipation bezier unifies the machine. */
```
