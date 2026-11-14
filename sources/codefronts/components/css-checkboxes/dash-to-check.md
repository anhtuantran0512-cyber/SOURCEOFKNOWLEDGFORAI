---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/dash-to-check/"
title: "Dash to Check"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A refined state change: the box starts showing a flat dash (a neutral / partial marker) that appears to transform into a checkmark on selection."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dash to Check
Source: https://codefronts.com/components/css-checkboxes/dash-to-check/

A refined state change: the box starts showing a flat dash (a neutral / partial marker) that appears to transform into a checkmark on selection. Two SVG strokes — one retracts as the other draws — read as a single morphing line.
## HTML
```html
<section class="cb-24" aria-label="Dash to check morph checkboxes">
  <div class="cb-24__panel">
    <label class="cb-24__row"><input type="checkbox" class="cb-24__input" checked><span class="cb-24__box" aria-hidden="true"><svg viewBox="0 0 24 24"><path class="cb-24__dash" d="M6 12 H18"/><path class="cb-24__chk" d="M5 12.5 10 18 20 6"/></svg></span><span class="cb-24__label">Review approved</span></label>
    <label class="cb-24__row"><input type="checkbox" class="cb-24__input"><span class="cb-24__box" aria-hidden="true"><svg viewBox="0 0 24 24"><path class="cb-24__dash" d="M6 12 H18"/><path class="cb-24__chk" d="M5 12.5 10 18 20 6"/></svg></span><span class="cb-24__label">Awaiting sign-off</span></label>
    <label class="cb-24__row"><input type="checkbox" class="cb-24__input"><span class="cb-24__box" aria-hidden="true"><svg viewBox="0 0 24 24"><path class="cb-24__dash" d="M6 12 H18"/><path class="cb-24__chk" d="M5 12.5 10 18 20 6"/></svg></span><span class="cb-24__label">Pending checks</span></label>
  </div>
</section>
```
## CSS
```css
.cb-24,
.cb-24 *,
.cb-24 *::before,
.cb-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-24 ::selection {
  background: oklch(0.6 0.15 240);
  color: #fff;
}

.cb-24 {
  --accent: oklch(0.56 0.15 240);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #eef2f8;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-24__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #dde5f0;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-24__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-24__input {
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

.cb-24__box {
  flex: none;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  border: 2px solid #b7c4d8;
  background: #fff;
  display: grid;
  place-items: center;
  transition: background .3s,border-color .3s;
}

.cb-24__box svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: #8b98ac;
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
  transform: rotate(0deg);
  transition: stroke .3s,transform .4s;
}

.cb-24__dash {
  stroke-dasharray: 12;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset .3s ease;
}

.cb-24__chk {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  transition: stroke-dashoffset .4s .12s cubic-bezier(.6,.1,.3,1);
}

.cb-24__input:checked ~ .cb-24__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-24__input:checked ~ .cb-24__box svg {
  stroke: #fff;
  transform: rotate(-8deg);
}

.cb-24__input:checked ~ .cb-24__box .cb-24__dash {
  stroke-dashoffset: 12;
}

.cb-24__input:checked ~ .cb-24__box .cb-24__chk {
  stroke-dashoffset: 0;
}

.cb-24__input:focus-visible ~ .cb-24__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-24__label {
  font-size: 14.5px;
  color: #2c3540;
}

@media (prefers-reduced-motion: reduce) {
  .cb-24__box,
    .cb-24__box svg,
    .cb-24__dash,
    .cb-24__chk {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the dash retracts as the check draws in, reading as a morph. */
```
