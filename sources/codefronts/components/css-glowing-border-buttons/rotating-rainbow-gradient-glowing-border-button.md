---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/rotating-rainbow-gradient-glowing-border-button/"
title: "Rotating Rainbow Gradient Glowing Border Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The definitive dark-theme SaaS primary CTA: a full-spectrum conic-gradient ring orbits the button forever, with a blurred twin of the same gradient breathing…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotating Rainbow Gradient Glowing Border Button
Source: https://codefronts.com/components/css-glowing-border-buttons/rotating-rainbow-gradient-glowing-border-button/

The definitive dark-theme SaaS primary CTA: a full-spectrum conic-gradient ring orbits the button forever, with a blurred twin of the same gradient breathing underneath as the glow. Built on @property so the rotation is a real, hardware-cheap CSS animation — zero JavaScript, zero libraries.
## HTML
```html
<section class="gbb-01" aria-label="Rotating rainbow gradient border button demo">
  <button class="gbb-01__btn" type="button">Get Started Free</button>
</section>
```
## CSS
```css
.gbb-01,
.gbb-01 *,
.gbb-01 *::before,
.gbb-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --gbb-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.gbb-01 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(70% 90% at 50% 0%,oklch(0.22 0.05 290 / .8),transparent 65%),oklch(0.13 0.02 280);
}

.gbb-01 .gbb-01__btn {
  position: relative;
  isolation: isolate;
  border: none;
  cursor: pointer;
  padding: 16px 34px;
  border-radius: 999px;
  font: 600 16px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .01em;
  color: #fff;
  background: oklch(0.17 0.02 280);
  transition: transform .25s ease;
}

.gbb-01 .gbb-01__btn::before,
.gbb-01 .gbb-01__btn::after {
  content: "";
  position: absolute;
  inset: -2px;
  z-index: -1;
  border-radius: inherit;
  background: conic-gradient(from var(--gbb-a),oklch(0.72 0.2 20),oklch(0.8 0.17 90),oklch(0.75 0.16 160),oklch(0.7 0.15 230),oklch(0.65 0.22 300),oklch(0.72 0.2 20));
  animation: gbb01-spin 3.5s linear infinite;
}

.gbb-01 .gbb-01__btn::after {
  filter: blur(18px);
  opacity: .55;
  transition: opacity .35s ease;
}

.gbb-01 .gbb-01__btn:hover,
.gbb-01 .gbb-01__btn:focus-visible {
  transform: translateY(-2px);
}

.gbb-01 .gbb-01__btn:hover::before,
.gbb-01 .gbb-01__btn:hover::after {
  animation-duration: 1.4s;
}

.gbb-01 .gbb-01__btn:hover::after {
  opacity: .95;
}

.gbb-01 .gbb-01__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 5px;
}

.gbb-01 .gbb-01__btn:active {
  transform: translateY(0) scale(.98);
}

@keyframes gbb01-spin {
  to {
    --gbb-a: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-01 .gbb-01__btn::before,
    .gbb-01 .gbb-01__btn::after {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — @property makes --gbb-a a typed, animatable angle, so the conic-gradient ring rotates with a plain @keyframes loop. */
```
