---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/neumorphic-checkbox/"
title: "Neumorphic Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "Soft-UI 'clay' controls: the box appears extruded from the surface, then presses inward when checked — created entirely with paired light and dark shadows on…"
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Checkbox
Source: https://codefronts.com/components/css-checkboxes/neumorphic-checkbox/

Soft-UI 'clay' controls: the box appears extruded from the surface, then presses inward when checked — created entirely with paired light and dark shadows on a single tonal background. The signature look of calm, monochrome dashboards.
## HTML
```html
<section class="cb-12" aria-label="Neumorphic checkboxes">
  <div class="cb-12__panel">
    <label class="cb-12__row"><input type="checkbox" class="cb-12__input" checked><span class="cb-12__box" aria-hidden="true"></span><span class="cb-12__label">Silent mode</span></label>
    <label class="cb-12__row"><input type="checkbox" class="cb-12__input"><span class="cb-12__box" aria-hidden="true"></span><span class="cb-12__label">Haptic feedback</span></label>
    <label class="cb-12__row"><input type="checkbox" class="cb-12__input"><span class="cb-12__box" aria-hidden="true"></span><span class="cb-12__label">Battery saver</span></label>
  </div>
</section>
```
## CSS
```css
.cb-12,
.cb-12 *,
.cb-12 *::before,
.cb-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-12 ::selection {
  background: oklch(0.62 0.15 265);
  color: #fff;
}

.cb-12 {
  --surface: #e6e9ef;
  --accent: oklch(0.58 0.16 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: var(--surface);
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-12__panel {
  width: min(400px,100%);
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 20px;
  border-radius: 22px;
  background: var(--surface);
  box-shadow: 9px 9px 20px #c4c9d3,-9px -9px 20px #ffffff;
}

.cb-12__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 12px 10px;
}

.cb-12__input {
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

.cb-12__box {
  position: relative;
  flex: none;
  width: 30px;
  height: 30px;
  border-radius: 9px;
  background: var(--surface);
  box-shadow: 4px 4px 8px #c4c9d3,-4px -4px 8px #ffffff;
  transition: box-shadow .3s ease;
}

.cb-12__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--accent);
  opacity: 0;
  transform: scale(.5);
  transition: opacity .25s,transform .25s cubic-bezier(.2,.9,.3,1.2);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-12__input:checked ~ .cb-12__box {
  box-shadow: inset 4px 4px 8px #c4c9d3,inset -4px -4px 8px #ffffff;
}

.cb-12__input:checked ~ .cb-12__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-12__input:focus-visible ~ .cb-12__box {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

.cb-12__label {
  font-size: 14.5px;
  font-weight: 500;
  color: #59606e;
}

@media (prefers-reduced-motion: reduce) {
  .cb-12__box,
    .cb-12__box::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — raised box-shadows swap to inset on :checked for the pressed look. */
```
