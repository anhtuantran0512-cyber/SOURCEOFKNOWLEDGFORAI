---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/filter-tag-pill-checkbox/"
title: "Filter Tag Pill Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A multi-select filter chip cloud — the pattern behind every e-commerce facet bar and job-board filter."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Filter Tag Pill Checkbox
Source: https://codefronts.com/components/css-checkboxes/filter-tag-pill-checkbox/

A multi-select filter chip cloud — the pattern behind every e-commerce facet bar and job-board filter. The raw checkbox is safely hidden while the label becomes a clickable pill that flips its accent and reveals a check on selection.
## HTML
```html
<section class="cb-02" aria-label="Filter tag pills">
  <fieldset class="cb-02__group">
    <legend class="cb-02__legend">Filter by category</legend>
    <label class="cb-02__pill"><input type="checkbox" class="cb-02__input" checked><span class="cb-02__ico" aria-hidden="true"></span>Design</label>
    <label class="cb-02__pill"><input type="checkbox" class="cb-02__input"><span class="cb-02__ico" aria-hidden="true"></span>Engineering</label>
    <label class="cb-02__pill"><input type="checkbox" class="cb-02__input" checked><span class="cb-02__ico" aria-hidden="true"></span>Marketing</label>
    <label class="cb-02__pill"><input type="checkbox" class="cb-02__input"><span class="cb-02__ico" aria-hidden="true"></span>Remote</label>
    <label class="cb-02__pill"><input type="checkbox" class="cb-02__input"><span class="cb-02__ico" aria-hidden="true"></span>Full-time</label>
    <label class="cb-02__pill"><input type="checkbox" class="cb-02__input" checked><span class="cb-02__ico" aria-hidden="true"></span>Contract</label>
  </fieldset>
</section>
```
## CSS
```css
.cb-02,
.cb-02 *,
.cb-02 *::before,
.cb-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-02 ::selection {
  background: oklch(0.62 0.16 160);
  color: #fff;
}

.cb-02 {
  --sel: oklch(0.55 0.13 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f6f5;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-02__group {
  width: min(480px,100%);
  border: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.cb-02__legend {
  width: 100%;
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #7c847f;
  margin-bottom: 14px;
}

.cb-02__input {
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

.cb-02__pill {
  display: inline-flex;
  align-items: center;
  gap: 0;
  cursor: pointer;
  user-select: none;
  padding: 9px 16px;
  border: 1.5px solid #d6dcd9;
  border-radius: 999px;
  background: #fff;
  font-size: 14px;
  font-weight: 600;
  color: #41474a;
  transition: background .2s,border-color .2s,color .2s;
}

.cb-02__ico {
  width: 0;
  height: 14px;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  opacity: 0;
  transform: scale(.5);
  transition: width .2s,opacity .2s,transform .2s,margin .2s;
}

.cb-02__ico::before {
  content: "";
  width: 14px;
  height: 14px;
  flex: none;
  background: currentColor;
  -webkit-mask: no-repeat center/12px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/12px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-02__input:checked ~ .cb-02__ico {
  width: 14px;
  opacity: 1;
  transform: scale(1);
  margin-right: 7px;
}

.cb-02__pill:hover {
  border-color: var(--sel);
}

.cb-02__input:checked ~ *,
.cb-02__pill:has(.cb-02__input:checked) {
}

.cb-02__pill:has(:checked) {
  background: var(--sel);
  border-color: var(--sel);
  color: #fff;
}

.cb-02__pill:has(:focus-visible) {
  outline: 3px solid var(--sel);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-02__pill,
    .cb-02__ico {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :checked (+ :has for the label paint) styles each pill. */
```
