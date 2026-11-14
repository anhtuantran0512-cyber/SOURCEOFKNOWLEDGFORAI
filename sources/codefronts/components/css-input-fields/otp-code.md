---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/otp-code/"
title: "OTP Code"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "One-time-passcode entry split across six boxes inside a single <fieldset>."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: OTP Code
Source: https://codefronts.com/components/css-input-fields/otp-code/

One-time-passcode entry split across six boxes inside a single <fieldset>. Auto-advance, backspace step-back, and full paste-to-fill — `autocomplete="one-time-code"` drives SMS auto-suggest.
## HTML
```html
<fieldset class="if-10">
  <legend class="if-10-legend">Verification code</legend>
  <input
    type="text"
    inputmode="numeric"
    maxlength="1"
    autocomplete="one-time-code"
    pattern="[0-9]"
    aria-label="Digit 1"
    data-if-10
  />
  <input
    type="text"
    inputmode="numeric"
    maxlength="1"
    pattern="[0-9]"
    aria-label="Digit 2"
    data-if-10
  />
  <input
    type="text"
    inputmode="numeric"
    maxlength="1"
    pattern="[0-9]"
    aria-label="Digit 3"
    data-if-10
  />
  <input
    type="text"
    inputmode="numeric"
    maxlength="1"
    pattern="[0-9]"
    aria-label="Digit 4"
    data-if-10
  />
  <input
    type="text"
    inputmode="numeric"
    maxlength="1"
    pattern="[0-9]"
    aria-label="Digit 5"
    data-if-10
  />
  <input
    type="text"
    inputmode="numeric"
    maxlength="1"
    pattern="[0-9]"
    aria-label="Digit 6"
    data-if-10
  />
</fieldset>
```
## CSS
```css
.if-10 {
  border: 0;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 8px;
  width: 100%;
  max-width: 280px;
  position: relative;
}

.if-10-legend {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.if-10 input {
  width: 100%;
  box-sizing: border-box;
  aspect-ratio: 1 / 1;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  font-size: 18px;
  font-weight: 700;
  text-align: center;
  color: #f0eeff;
  outline: none;
  caret-color: #7c6cff;
  transition: border-color 0.15s, background 0.15s, transform 0.12s;
}

.if-10 input:focus {
  border-color: #7c6cff;
  background: rgba(124, 108, 255, 0.1);
  transform: translateY(-1px);
}
```

## JavaScript
```js
// OTP — auto-advance, backspace step-back, full paste-to-fill
document.querySelectorAll(".if-10").forEach(function (row) {
  var inputs = Array.prototype.slice.call(row.querySelectorAll("[data-if-10]"));
  inputs.forEach(function (input, i) {
    input.addEventListener("input", function () {
      input.value = (input.value || "").replace(/\\D/g, "").slice(0, 1);
      if (input.value && inputs[i + 1]) inputs[i + 1].focus();
    });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Backspace" && !input.value && inputs[i - 1]) inputs[i - 1].focus();
    });
    input.addEventListener("paste", function (e) {
      var data = (e.clipboardData || window.clipboardData).getData("text");
      var digits = (data || "").replace(/\\D/g, "").slice(0, inputs.length);
      if (!digits) return;
      e.preventDefault();
      for (var j = 0; j < digits.length; j++) {
        if (inputs[i + j]) inputs[i + j].value = digits[j];
      }
      inputs[Math.min(i + digits.length, inputs.length - 1)].focus();
    });
  });
});
```
