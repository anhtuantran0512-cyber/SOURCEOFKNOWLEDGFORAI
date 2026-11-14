---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/smooth-gradient-hue-shift-border-button/"
title: "Smooth Gradient Hue-Shift Border Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The 'Most Popular' plan highlighter: the button's border and halo drift continuously through the color wheel — violet to cyan to rose and back — by animating…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smooth Gradient Hue-Shift Border Button
Source: https://codefronts.com/components/css-glowing-border-buttons/smooth-gradient-hue-shift-border-button/

The 'Most Popular' plan highlighter: the button's border and halo drift continuously through the color wheel — violet to cyan to rose and back — by animating a single registered hue number through oklch(). Because only hue moves (lightness and chroma pinned), every frame is equally vivid and the label never loses contrast.
## HTML
```html
<section class="gbb-14" aria-label="Hue shifting gradient border button demo">
  <div class="gbb-14__plan">
    <span class="gbb-14__badge"><span class="gbb-14__dot" aria-hidden="true"></span>Most Popular</span>
    <button class="gbb-14__btn" type="button">Choose Pro &mdash; $19/mo</button>
  </div>
</section>
```
## CSS
```css
.gbb-14,
.gbb-14 *,
.gbb-14 *::before,
.gbb-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --gbb-h {
  syntax: '<number>';
  inherits: true;
  initial-value: 280;
}

.gbb-14 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.14 0.015 280);
  animation: gbb14-drift 6s linear infinite;
}

.gbb-14 .gbb-14__plan {
  display: grid;
  justify-items: center;
  gap: 14px;
}

.gbb-14 .gbb-14__badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font: 700 11px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: rgba(255,255,255,.85);
  border: 1px solid oklch(0.7 0.19 calc(var(--gbb-h) * 1deg) / .4);
  border-radius: 999px;
  padding: 6px 13px;
}

.gbb-14 .gbb-14__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: oklch(0.75 0.19 calc(var(--gbb-h) * 1deg));
  box-shadow: 0 0 8px oklch(0.75 0.19 calc(var(--gbb-h) * 1deg));
}

.gbb-14 .gbb-14__btn {
  cursor: pointer;
  border: 2px solid transparent;
  border-radius: 14px;
  padding: 16px 32px;
  font: 700 15px/1 'Segoe UI',system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(oklch(0.18 0.02 280),oklch(0.18 0.02 280)) padding-box,linear-gradient(120deg,oklch(0.7 0.19 calc(var(--gbb-h) * 1deg)),oklch(0.7 0.19 calc((var(--gbb-h) + 60) * 1deg))) border-box;
  box-shadow: 0 0 22px oklch(0.7 0.19 calc(var(--gbb-h) * 1deg) / .3);
  transition: box-shadow .3s ease,transform .25s ease;
}

.gbb-14 .gbb-14__btn:hover,
.gbb-14 .gbb-14__btn:focus-visible {
  transform: translateY(-2px);
  box-shadow: 0 0 38px oklch(0.7 0.19 calc(var(--gbb-h) * 1deg) / .5),0 0 0 4px oklch(0.7 0.19 calc(var(--gbb-h) * 1deg) / .18);
}

.gbb-14:has(.gbb-14__btn:hover),
.gbb-14:has(.gbb-14__btn:focus-visible) {
  animation-duration: 2.5s;
}

.gbb-14 .gbb-14__btn:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 4px;
}

.gbb-14 .gbb-14__btn:active {
  transform: translateY(0) scale(.98);
}

@keyframes gbb14-drift {
  from {
    --gbb-h: 0;
  }

  to {
    --gbb-h: 360;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-14 {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one registered number (--gbb-h) animates 0→360; every oklch() color on the button derives its hue from it via calc(). */
```
