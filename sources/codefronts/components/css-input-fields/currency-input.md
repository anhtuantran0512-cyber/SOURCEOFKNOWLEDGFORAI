---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/currency-input/"
title: "Currency Input"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Right-aligned numeric input with an inline `$` prefix."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Currency Input
Source: https://codefronts.com/components/css-input-fields/currency-input/

Right-aligned numeric input with an inline `$` prefix. `inputmode="decimal"` brings up the right mobile keyboard; `:focus-within` lights the prefix to match the field accent.
## HTML
```html
<label class="if-16">
  <span class="if-16-label">Amount</span>
  <span class="if-16-wrap">
    <span class="if-16-prefix">$</span>
    <input type="text" name="amount" inputmode="decimal" pattern="[0-9.,]*" placeholder="0.00" />
    <span class="if-16-suffix">USD</span>
  </span>
</label>
```
## CSS
```css
.if-16 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-16-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-16-wrap {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 0 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  transition: border-color 0.2s, background 0.2s;
}

.if-16-wrap:focus-within {
  border-color: #f5a84a;
  background: #1f1f2a;
}

.if-16-prefix {
  color: #b8b6d4;
  font: 600 14px/1 system-ui, sans-serif;
  transition: color 0.2s;
}

.if-16-wrap:focus-within .if-16-prefix {
  color: #f5a84a;
}

.if-16 input {
  flex: 1;
  min-width: 0;
  padding: 12px 0;
  border: 0;
  outline: none;
  background: transparent;
  color: #f0eeff;
  font: 600 14px/1 system-ui, sans-serif;
  text-align: right;
  -moz-appearance: textfield;
}

.if-16 input::-webkit-outer-spin-button,
.if-16 input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.if-16 input::placeholder {
  color: #b8b6d4;
}

.if-16-suffix {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  color: #b8b6d4;
  letter-spacing: 0.06em;
}
```
