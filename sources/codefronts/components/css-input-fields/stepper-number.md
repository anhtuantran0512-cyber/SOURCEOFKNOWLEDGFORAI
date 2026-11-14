---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/stepper-number/"
title: "Stepper Number"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Quantity input with custom −/+ controls. Native <input type=\"number\"> underneath keeps keyboard arrows, validation, and screen-reader semantics intact."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stepper Number
Source: https://codefronts.com/components/css-input-fields/stepper-number/

Quantity input with custom −/+ controls. Native <input type="number"> underneath keeps keyboard arrows, validation, and screen-reader semantics intact.
## HTML
```html
<label class="if-14">
  <span class="if-14-label">Quantity</span>
  <span class="if-14-wrap">
    <button type="button" class="if-14-btn" data-if-14="-1" aria-label="Decrease">−</button>
    <input type="number" name="qty" min="0" max="99" value="1" aria-label="Quantity" />
    <button type="button" class="if-14-btn" data-if-14="1" aria-label="Increase">+</button>
  </span>
</label>
```
## CSS
```css
.if-14 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 220px;
  font-size: 11px;
  color: #b8b6d4;
}

.if-14-label {
  font-weight: 600;
}

.if-14-wrap {
  display: grid;
  grid-template-columns: 36px 1fr 36px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  overflow: hidden;
  transition: border-color 0.2s;
}

.if-14-wrap:focus-within {
  border-color: #14b8a6;
}

.if-14-btn {
  background: rgba(20, 184, 166, 0.06);
  border: 0;
  color: #5eead4;
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
}

.if-14-btn:hover {
  background: rgba(20, 184, 166, 0.18);
  color: #fff;
}

.if-14-btn:active {
  background: rgba(20, 184, 166, 0.28);
}

.if-14 input {
  background: transparent;
  border: 0;
  outline: none;
  color: #f0eeff;
  font-size: 16px;
  font-weight: 600;
  text-align: center;
  padding: 10px 0;
  -moz-appearance: textfield;
}

.if-14 input::-webkit-outer-spin-button,
.if-14 input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
```

## JavaScript
```js
// Stepper +/- buttons — clamp to min/max
document.querySelectorAll(".if-14-wrap").forEach(function (wrap) {
  var input = wrap.querySelector('input[type="number"]');
  if (!input) return;
  wrap.querySelectorAll("[data-if-14]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var dir = parseInt(btn.dataset.ifStep, 10) || 0;
      var min = input.min !== "" ? Number(input.min) : -Infinity;
      var max = input.max !== "" ? Number(input.max) : Infinity;
      var val = (Number(input.value) || 0) + dir;
      if (val < min) val = min;
      if (val > max) val = max;
      input.value = String(val);
    });
  });
});
```
