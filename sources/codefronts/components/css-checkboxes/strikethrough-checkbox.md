---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/strikethrough-checkbox/"
title: "Strikethrough Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "The definitive to-do interaction: checking an item strikes a line cleanly across its label from left to right and dims the text — the universal 'done' gesture."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Strikethrough Checkbox
Source: https://codefronts.com/components/css-checkboxes/strikethrough-checkbox/

The definitive to-do interaction: checking an item strikes a line cleanly across its label from left to right and dims the text — the universal 'done' gesture. Built with a scaleX pseudo-element, not a jumpy text-decoration.
## HTML
```html
<section class="cb-20" aria-label="To-do list with strikethrough">
  <div class="cb-20__panel">
    <label class="cb-20__row"><input type="checkbox" class="cb-20__input" checked><span class="cb-20__box" aria-hidden="true"></span><span class="cb-20__label">Write the launch email</span></label>
    <label class="cb-20__row"><input type="checkbox" class="cb-20__input"><span class="cb-20__box" aria-hidden="true"></span><span class="cb-20__label">Review pull requests</span></label>
    <label class="cb-20__row"><input type="checkbox" class="cb-20__input"><span class="cb-20__box" aria-hidden="true"></span><span class="cb-20__label">Book the venue</span></label>
    <label class="cb-20__row"><input type="checkbox" class="cb-20__input" checked><span class="cb-20__box" aria-hidden="true"></span><span class="cb-20__label">Update the changelog</span></label>
  </div>
</section>
```
## CSS
```css
.cb-20,
.cb-20 *,
.cb-20 *::before,
.cb-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-20 ::selection {
  background: oklch(0.6 0.14 155);
  color: #fff;
}

.cb-20 {
  --accent: oklch(0.55 0.14 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f3f6f4;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-20__panel {
  width: min(420px,100%);
  background: #fff;
  border: 1px solid #e1e8e3;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-20__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-20__input {
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

.cb-20__box {
  position: relative;
  flex: none;
  width: 22px;
  height: 22px;
  border-radius: 6px;
  border: 2px solid #bcccc2;
  background: #fff;
  transition: background .2s,border-color .2s;
}

.cb-20__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .18s,transform .18s;
  -webkit-mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-20__input:checked ~ .cb-20__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-20__input:checked ~ .cb-20__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-20__input:focus-visible ~ .cb-20__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-20__label {
  position: relative;
  font-size: 15px;
  color: #2c3a33;
  transition: color .3s;
}

.cb-20__label::after {
  content: "";
  position: absolute;
  left: 0;
  top: 52%;
  width: 100%;
  height: 2px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .35s cubic-bezier(.5,.1,.2,1);
}

.cb-20__input:checked ~ .cb-20__label {
  color: #9bb0a4;
}

.cb-20__input:checked ~ .cb-20__label::after {
  transform: scaleX(1);
}

@media (prefers-reduced-motion: reduce) {
  .cb-20__box,
    .cb-20__box::after,
    .cb-20__label,
    .cb-20__label::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a scaleX pseudo-element strikes across the label on :checked. */
```
