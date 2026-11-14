---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/rotating-placeholder/"
title: "Rotating Placeholder"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "The native placeholder attribute itself rotates through four sample queries every 2.5 seconds — \"Search products…\" → \"Search docs…\" → \"Search people…\" →…"
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotating Placeholder
Source: https://codefronts.com/components/css-input-fields/rotating-placeholder/

The native placeholder attribute itself rotates through four sample queries every 2.5 seconds — "Search products…" → "Search docs…" → "Search people…" → "Search settings…". Light JS swaps the attribute; the browser does the rest. Stops the moment the user focuses or starts typing.
## HTML
```html
<label class="if-11">
  <span class="if-11-cap">Search</span>
  <input
    type="search"
    name="q"
    inputmode="search"
    placeholder="Search products…"
    aria-label="Search"
    data-if-rotate='["Search products…","Search docs…","Search people…","Search settings…"]'
  />
</label>
```
## CSS
```css
.if-11 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-11-cap {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-11 input {
  width: 100%;
  box-sizing: border-box;
  padding: 12px 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  color: #f0eeff;
  font: 500 14px/1 system-ui, sans-serif;
  outline: none;
  transition: border-color 0.25s, background 0.2s;
}

.if-11 input:focus {
  border-color: #c084fc;
  background: #1f1f2a;
}

.if-11 input::placeholder {
  color: #b8b6d4;
  transition: opacity 0.25s ease;
}

.if-11 input.is-fading::placeholder {
  opacity: 0;
}
```

## JavaScript
```js
// Rotating Placeholder — swap the input's placeholder attribute on a 2.5s loop
document.querySelectorAll("[data-if-rotate]").forEach(function (input) {
  var phrases;
  try {
    phrases = JSON.parse(input.getAttribute("data-if-rotate") || "[]");
  } catch (e) {
    phrases = [];
  }
  if (!phrases.length) return;
  var i = 0,
    paused = false;
  function tick() {
    if (paused || document.activeElement === input || input.value) return;
    input.classList.add("is-fading");
    setTimeout(function () {
      i = (i + 1) % phrases.length;
      input.setAttribute("placeholder", phrases[i]);
      input.classList.remove("is-fading");
    }, 250);
  }
  setInterval(tick, 2500);
  input.addEventListener("focus", function () {
    paused = true;
  });
  input.addEventListener("blur", function () {
    paused = !!input.value;
  });
});
```
