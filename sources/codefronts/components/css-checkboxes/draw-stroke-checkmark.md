---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/draw-stroke-checkmark/"
title: "Draw Stroke Checkmark"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A premium, hand-drawn feel: an inline SVG checkmark that draws itself in on check using the classic stroke-dasharray / stroke-dashoffset line technique."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Draw Stroke Checkmark
Source: https://codefronts.com/components/css-checkboxes/draw-stroke-checkmark/

A premium, hand-drawn feel: an inline SVG checkmark that draws itself in on check using the classic stroke-dasharray / stroke-dashoffset line technique. Crisp at any size, no raster assets, and the animation is pure CSS.
## HTML
```html
<section class="cb-09" aria-label="Draw-stroke checkmark checkboxes">
  <div class="cb-09__panel">
    <label class="cb-09__row"><input type="checkbox" class="cb-09__input" checked><span class="cb-09__box" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4.5 12.5 10 18 20 6"/></svg></span><span class="cb-09__label">Contract signed</span></label>
    <label class="cb-09__row"><input type="checkbox" class="cb-09__input"><span class="cb-09__box" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4.5 12.5 10 18 20 6"/></svg></span><span class="cb-09__label">Payment received</span></label>
    <label class="cb-09__row"><input type="checkbox" class="cb-09__input"><span class="cb-09__box" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4.5 12.5 10 18 20 6"/></svg></span><span class="cb-09__label">Shipment dispatched</span></label>
  </div>
</section>
```
## CSS
```css
.cb-09,
.cb-09 *,
.cb-09 *::before,
.cb-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-09 ::selection {
  background: oklch(0.6 0.15 155);
  color: #fff;
}

.cb-09 {
  --accent: oklch(0.56 0.14 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f3f6f4;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-09__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #e2e8e4;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-09__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-09__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.cb-09__box {
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 7px;
  border: 2px solid #c2ccc6;
  background: #fff;
  display: grid;
  place-items: center;
  transition: background .25s,border-color .25s;
}

.cb-09__box svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #fff;
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cb-09__box svg path {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  transition: stroke-dashoffset .45s cubic-bezier(.6,.1,.3,1);
}

.cb-09__input:checked ~ .cb-09__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-09__input:checked ~ .cb-09__box svg path {
  stroke-dashoffset: 0;
}

.cb-09__input:focus-visible ~ .cb-09__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-09__label {
  font-size: 14.5px;
  color: #2c352f;
}

@media (prefers-reduced-motion: reduce) {
  .cb-09__box,
    .cb-09__box svg path {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — stroke-dashoffset animates 24→0 on :checked to draw the tick. */
```
