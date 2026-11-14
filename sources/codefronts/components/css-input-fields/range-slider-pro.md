---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/range-slider-pro/"
title: "Range Slider Pro"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "A native <input type=\"range\"> with custom track/thumb styling and a live value bubble that follows the thumb."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Range Slider Pro
Source: https://codefronts.com/components/css-input-fields/range-slider-pro/

A native <input type="range"> with custom track/thumb styling and a live value bubble that follows the thumb. Honest accessibility — keyboard arrows, screen-reader announcement, real form value.
## HTML
```html
<label class="if-24" for="if-24-input">
  <span class="if-24-label">Volume <span class="if-24-bubble" data-if-bubble>50</span></span>
  <input
    id="if-24-input"
    type="range"
    name="volume"
    min="0"
    max="100"
    value="50"
    data-if-24
  />
</label>
```
## CSS
```css
.if-24 {
  display: grid;
  gap: 8px;
  width: 100%;
  max-width: 280px;
}

.if-24-label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-24-bubble {
  font: 700 11px/1 "JetBrains Mono", monospace;
  color: #f0eeff;
  background: #7c6cff;
  padding: 3px 7px;
  border-radius: 999px;
  letter-spacing: 0;
}

.if-24 input {
  width: 100%;
  height: 6px;
  -webkit-appearance: none;
  appearance: none;
  background: linear-gradient(
      90deg,
      #7c6cff 0%,
      #7c6cff var(--if-24-fill, 50%),
      rgba(255, 255, 255, 0.08) var(--if-24-fill, 50%),
      rgba(255, 255, 255, 0.08) 100%
    );
  border-radius: 999px;
  outline: none;
  cursor: pointer;
}

.if-24 input::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px;
  height: 18px;
  background: #fff;
  border: 0;
  border-radius: 50%;
  box-shadow: 0 2px 6px rgba(124, 108, 255, 0.5);
  cursor: pointer;
  transition: transform 0.15s;
}

.if-24 input::-webkit-slider-thumb:hover {
  transform: scale(1.12);
}

.if-24 input::-moz-range-thumb {
  width: 18px;
  height: 18px;
  background: #fff;
  border: 0;
  border-radius: 50%;
  box-shadow: 0 2px 6px rgba(124, 108, 255, 0.5);
  cursor: pointer;
}
```

## JavaScript
```js
// Range Slider Pro — sync the live value bubble + paint the gradient fill via custom property
document.querySelectorAll("[data-if-24]").forEach(function (input) {
  var bubble = input.closest(".if-24").querySelector("[data-if-bubble]");
  function update() {
    var min = Number(input.min) || 0;
    var max = Number(input.max) || 100;
    var pct = ((Number(input.value) - min) / (max - min)) * 100;
    input.style.setProperty("--if-24-fill", pct + "%");
    if (bubble) bubble.textContent = String(input.value);
  }
  input.addEventListener("input", update);
  update();
});
```
