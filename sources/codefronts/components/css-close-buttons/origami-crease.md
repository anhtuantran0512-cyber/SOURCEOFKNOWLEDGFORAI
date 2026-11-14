---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/origami-crease/"
title: "Origami Crease Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A paper-craft ×: the two strokes are flat paper strips in 3D space (preserve-3d + perspective) that fold along their long axis on hover like creased origami,…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Origami Crease Close Button
Source: https://codefronts.com/components/css-close-buttons/origami-crease/

A paper-craft ×: the two strokes are flat paper strips in 3D space (preserve-3d + perspective) that fold along their long axis on hover like creased origami, each half catching different light via a gradient that shifts mid-fold. Delicate, tactile, and entirely pseudo-element powered.
## HTML
```html
<section class="ccb-11" aria-label="Origami fold close button demo">
  <button class="ccb-11__close" type="button" aria-label="Close">
    <span class="ccb-11__rig" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
.ccb-11,
.ccb-11 *,
.ccb-11 *::before,
.ccb-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-11 {
  --fold: 58deg;
  --paper-a: oklch(0.97 0.02 85);
  --paper-b: oklch(0.78 0.05 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,oklch(0.93 0.025 80),oklch(0.87 0.04 70));
}

.ccb-11 .ccb-11__close {
  position: relative;
  width: 72px;
  height: 72px;
  border: none;
  border-radius: 20px;
  background: oklch(0.99 0.008 85);
  cursor: pointer;
  perspective: 400px;
  box-shadow: 0 16px 34px -18px oklch(0.5 0.08 70 / .55),inset 0 0 0 1px oklch(0.9 0.03 80);
}

.ccb-11 .ccb-11__rig {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
}

.ccb-11 .ccb-11__rig::before,
.ccb-11 .ccb-11__rig::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 32px;
  height: 9px;
  margin: -4.5px 0 0 -16px;
  border-radius: 2px;
  background: linear-gradient(180deg,var(--paper-a) 50%,var(--paper-b) 50%);
  box-shadow: 0 6px 10px -4px oklch(0.45 0.06 70 / .35);
  transition: transform .38s cubic-bezier(.34,1.3,.5,1),background .38s ease;
}

.ccb-11 .ccb-11__rig::before {
  transform: rotate(45deg);
}

.ccb-11 .ccb-11__rig::after {
  transform: rotate(-45deg);
}

.ccb-11 .ccb-11__close:hover .ccb-11__rig::before {
  transform: rotate(45deg) rotateX(var(--fold));
}

.ccb-11 .ccb-11__close:hover .ccb-11__rig::after {
  transform: rotate(-45deg) rotateX(var(--fold));
}

.ccb-11 .ccb-11__close:hover .ccb-11__rig::before,
.ccb-11 .ccb-11__close:hover .ccb-11__rig::after {
  background: linear-gradient(180deg,var(--paper-a) 50%,oklch(0.68 0.06 70) 50%);
}

.ccb-11 .ccb-11__close:active {
  transform: scale(.95);
}

.ccb-11 .ccb-11__close:focus-visible {
  outline: 3px solid oklch(0.6 0.12 70);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-11 .ccb-11__rig::before,
    .ccb-11 .ccb-11__rig::after {
    transition: none;
  }

  .ccb-11 .ccb-11__close:hover .ccb-11__rig::before {
    transform: rotate(45deg);
  }

  .ccb-11 .ccb-11__close:hover .ccb-11__rig::after {
    transform: rotate(-45deg);
  }
}
```

## JavaScript
```js
/* No JavaScript — perspective on the button + preserve-3d lets each bar rotateX along its own long axis, folding like creased paper. */
```
