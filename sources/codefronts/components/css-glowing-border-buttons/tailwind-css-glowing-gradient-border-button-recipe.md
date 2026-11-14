---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/tailwind-css-glowing-gradient-border-button-recipe/"
title: "Tailwind CSS Glowing Gradient Border Button (Recipe)"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The exact glowing-border pattern that ships in modern React/Next.js apps — an absolutely-positioned gradient layer, nudged out with -inset-0.5, blurred, and…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Glowing Gradient Border Button (Recipe)
Source: https://codefronts.com/components/css-glowing-border-buttons/tailwind-css-glowing-gradient-border-button-recipe/

The exact glowing-border pattern that ships in modern React/Next.js apps — an absolutely-positioned gradient layer, nudged out with -inset-0.5, blurred, and revealed on group-hover — implemented here in plain CSS line-for-line, with the equivalent Tailwind utility string documented so you can paste either version.
## HTML
```html
<section class="gbb-06" aria-label="Tailwind-style gradient blur glow button demo">
  <div class="gbb-06__group">
    <div class="gbb-06__glow" aria-hidden="true"></div><!-- absolute -inset-0.5 blur -->
    <button class="gbb-06__btn" type="button">Deploy Now</button><!-- relative, on top -->
  </div>
</section>
```
## CSS
```css
.gbb-06,
.gbb-06 *,
.gbb-06 *::before,
.gbb-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-06 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.13 0.02 270);
}

.gbb-06 .gbb-06__group {
  position: relative;
  display: inline-block;
}
/* .relative.group */

.gbb-06 .gbb-06__glow {
  position: absolute;
  inset: -2px;
  border-radius: 14px;
  background: linear-gradient(90deg,oklch(0.65 0.26 328),oklch(0.75 0.15 195));
  filter: blur(14px);
  opacity: .6;
  pointer-events: none;
  transition: opacity .3s ease,scale .3s ease;
  pointer-events: none;
}
/* .absolute.-inset-0.5.blur.opacity-60 */

.gbb-06 .gbb-06__group:hover .gbb-06__glow,
.gbb-06 .gbb-06__group:focus-within .gbb-06__glow {
  opacity: 1;
  scale: 1.02;
  pointer-events: none;
}
/* .group-hover:opacity-100 */

.gbb-06 .gbb-06__btn {
  position: relative;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 12px;
  padding: 16px 34px;
  font: 600 15px/1 'Segoe UI',system-ui,sans-serif;
  color: #fff;
  background: oklch(0.15 0.02 270);
  transition: transform .2s ease;
}
/* .relative.bg-slate-950 */

.gbb-06 .gbb-06__btn:hover {
  transform: translateY(-1px);
}

.gbb-06 .gbb-06__btn:focus-visible {
  outline: 2px solid oklch(0.75 0.15 195);
  outline-offset: 4px;
}

.gbb-06 .gbb-06__btn:active {
  transform: translateY(0) scale(.98);
}

@media (prefers-reduced-motion: reduce) {
  .gbb-06 .gbb-06__glow,
    .gbb-06 .gbb-06__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the canonical Tailwind two-layer pattern (relative group / absolute -inset blur layer / relative button) in plain CSS. */
```
