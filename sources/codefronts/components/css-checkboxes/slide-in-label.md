---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/slide-in-label/"
title: "Slide-In Label"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "Spatial hierarchy on check: the label shifts aside and a confirmation tag glides in from the left, adding an elegant extra layer of feedback without a single…"
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide-In Label
Source: https://codefronts.com/components/css-checkboxes/slide-in-label/

Spatial hierarchy on check: the label shifts aside and a confirmation tag glides in from the left, adding an elegant extra layer of feedback without a single reflow. Great for save states, applied filters and 'added to X' confirmations.
## HTML
```html
<section class="cb-28" aria-label="Slide-in label checkboxes">
  <div class="cb-28__panel">
    <label class="cb-28__row"><input type="checkbox" class="cb-28__input" checked><span class="cb-28__box" aria-hidden="true"></span><span class="cb-28__labels"><span class="cb-28__tag">Saved</span><span class="cb-28__label">Keep in library</span></span></label>
    <label class="cb-28__row"><input type="checkbox" class="cb-28__input"><span class="cb-28__box" aria-hidden="true"></span><span class="cb-28__labels"><span class="cb-28__tag">Saved</span><span class="cb-28__label">Pin to sidebar</span></span></label>
    <label class="cb-28__row"><input type="checkbox" class="cb-28__input"><span class="cb-28__box" aria-hidden="true"></span><span class="cb-28__labels"><span class="cb-28__tag">Saved</span><span class="cb-28__label">Add to watchlist</span></span></label>
  </div>
</section>
```
## CSS
```css
.cb-28,
.cb-28 *,
.cb-28 *::before,
.cb-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-28 ::selection {
  background: oklch(0.6 0.14 195);
  color: #fff;
}

.cb-28 {
  --accent: oklch(0.55 0.12 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #eef5f6;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-28__panel {
  width: min(420px,100%);
  background: #fff;
  border: 1px solid #daeaeb;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-28__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 14px 8px;
}

.cb-28__input {
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

.cb-28__box {
  position: relative;
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 7px;
  border: 2px solid #b3ccce;
  background: #fff;
  transition: background .2s,border-color .2s;
}

.cb-28__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .2s,transform .2s cubic-bezier(.2,.9,.3,1.2);
  -webkit-mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-28__labels {
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.cb-28__tag {
  flex: none;
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #fff;
  background: var(--accent);
  padding: 3px 8px;
  border-radius: 6px;
  transform: translateX(-120%);
  opacity: 0;
  transition: transform .35s cubic-bezier(.3,.9,.3,1),opacity .3s;
}

.cb-28__label {
  font-size: 14.5px;
  color: #2a3a3b;
  transform: translateX(-30px);
  transition: transform .35s cubic-bezier(.3,.9,.3,1);
}

.cb-28__input:checked ~ .cb-28__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-28__input:checked ~ .cb-28__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-28__input:checked ~ .cb-28__labels .cb-28__tag {
  transform: translateX(0);
  opacity: 1;
  margin-right: 8px;
}

.cb-28__input:checked ~ .cb-28__labels .cb-28__label {
  transform: translateX(0);
}

.cb-28__input:focus-visible ~ .cb-28__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-28__box,
    .cb-28__box::after,
    .cb-28__tag,
    .cb-28__label {
    transition: opacity .2s;
  }

  .cb-28__tag,
    .cb-28__label {
    transform: none;
  }

  .cb-28__input:checked ~ .cb-28__labels .cb-28__tag {
    margin-right: 8px;
  }
}
```

## JavaScript
```js
/* No JavaScript — the confirmation tag slides in via translateX as the label nudges over. */
```
