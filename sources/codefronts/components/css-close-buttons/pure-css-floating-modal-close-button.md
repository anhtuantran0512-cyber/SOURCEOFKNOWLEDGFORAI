---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/pure-css-floating-modal-close-button/"
title: "Pure CSS Floating Modal Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The canonical dialog dismiss: a quiet circular button pinned to the modal's top-right corner with absolute positioning, its × drawn from two rotated…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Floating Modal Close Button
Source: https://codefronts.com/components/css-close-buttons/pure-css-floating-modal-close-button/

The canonical dialog dismiss: a quiet circular button pinned to the modal's top-right corner with absolute positioning, its × drawn from two rotated pseudo-element bars — zero icon fonts, zero SVG. Hover breathes the circle in with a soft tint; :focus-visible rings it. This is the copy-paste answer to "modal close button top right corner CSS".
## HTML
```html
<section class="ccb-01" aria-label="Floating modal close button demo">
  <div class="ccb-01__modal" role="dialog" aria-labelledby="ccb-01-title">
    <button class="ccb-01__close" type="button" aria-label="Close dialog"></button>
    <h3 class="ccb-01__title" id="ccb-01-title">Confirm your email</h3>
    <p class="ccb-01__text">We sent a verification link to your inbox. Click it to activate your account.</p>
  </div>
</section>
```
## CSS
```css
.ccb-01,
.ccb-01 *,
.ccb-01 *::before,
.ccb-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-01 {
  --accent: oklch(0.55 0.16 265);
  --offset: 1rem;
  --x-size: 16px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(160deg,oklch(0.95 0.015 265),oklch(0.9 0.03 280));
}

.ccb-01 .ccb-01__modal {
  position: relative;
  width: min(400px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 32px 28px 28px;
  box-shadow: 0 30px 70px -30px oklch(0.35 0.08 270 / .55);
}

.ccb-01 .ccb-01__title {
  font-size: 19px;
  color: oklch(0.25 0.02 270);
  margin-bottom: 10px;
}

.ccb-01 .ccb-01__text {
  font-size: 14px;
  line-height: 1.55;
  color: oklch(0.5 0.02 270);
}

.ccb-01 .ccb-01__close {
  position: absolute;
  top: var(--offset);
  inset-inline-end: var(--offset);
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 50%;
  background: transparent;
  cursor: pointer;
  transition: background .18s ease;
}

.ccb-01 .ccb-01__close::before,
.ccb-01 .ccb-01__close::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: var(--x-size);
  height: 2px;
  border-radius: 2px;
  background: oklch(0.45 0.02 270);
  transition: transform .18s ease,background .18s ease;
}

.ccb-01 .ccb-01__close::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-01 .ccb-01__close::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-01 .ccb-01__close:hover {
  background: color-mix(in oklab,var(--accent) 12%,transparent);
}

.ccb-01 .ccb-01__close:hover::before {
  transform: translate(-50%,-50%) rotate(45deg) scaleX(1.15);
  background: var(--accent);
}

.ccb-01 .ccb-01__close:hover::after {
  transform: translate(-50%,-50%) rotate(-45deg) scaleX(1.15);
  background: var(--accent);
}

.ccb-01 .ccb-01__close:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.ccb-01 .ccb-01__close:active {
  transform: scale(.94);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-01 .ccb-01__close,
    .ccb-01 .ccb-01__close::before,
    .ccb-01 .ccb-01__close::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two rotated pseudo-element bars draw the ×; custom properties position and size everything. */
```
