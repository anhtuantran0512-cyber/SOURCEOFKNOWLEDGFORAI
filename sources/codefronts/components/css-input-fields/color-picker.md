---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/color-picker/"
title: "Color Picker"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "A <input type=\"color\"> swatch chip paired with a hex text field — both accept the same `name` and submit value via the underlying form."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Color Picker
Source: https://codefronts.com/components/css-input-fields/color-picker/

A <input type="color"> swatch chip paired with a hex text field — both accept the same `name` and submit value via the underlying form. Sibling-`+` selectors mirror the swatch state.
## HTML
```html
<label class="if-19">
  <span class="if-19-label">Brand colour</span>
  <span class="if-19-wrap">
    <input type="color" id="if-19-c" value="#7c6cff" aria-label="Pick colour" />
    <input
      type="text"
      id="if-19-t"
      value="#7c6cff"
      aria-label="Hex value"
      pattern="^#[0-9A-Fa-f]{6}$"
    />
  </span>
</label>
```
## CSS
```css
.if-19 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-19-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-19-wrap {
  display: inline-flex;
  align-items: stretch;
  gap: 0;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  overflow: hidden;
  transition: border-color 0.2s;
}

.if-19-wrap:focus-within {
  border-color: #7c6cff;
}

.if-19 input[type="color"] {
  width: 44px;
  height: 44px;
  padding: 6px;
  border: 0;
  outline: none;
  cursor: pointer;
  background: transparent;
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.if-19 input[type="color"]::-webkit-color-swatch-wrapper {
  padding: 0;
}

.if-19 input[type="color"]::-webkit-color-swatch {
  border: 0;
  border-radius: 6px;
}

.if-19 input[type="text"] {
  flex: 1;
  min-width: 0;
  padding: 0 14px;
  border: 0;
  outline: none;
  background: transparent;
  color: #f0eeff;
  font: 600 13px/1 "JetBrains Mono", monospace;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
```
