---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/time-range/"
title: "Time Range"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Two <input type=\"time\"> paired with a typographic `→` divider. Single visual unit while remaining two independent fields for keyboard nav and form submission."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Time Range
Source: https://codefronts.com/components/css-input-fields/time-range/

Two <input type="time"> paired with a typographic `→` divider. Single visual unit while remaining two independent fields for keyboard nav and form submission.
## HTML
```html
<fieldset class="if-18">
  <legend class="if-18-legend">Quiet hours</legend>
  <span class="if-18-row">
    <label
      ><span class="if-18-cap">From</span><input type="time" name="from" value="22:00"
    /></label>
    <span class="if-18-sep" aria-hidden="true">→</span>
    <label><span class="if-18-cap">To</span><input type="time" name="to" value="07:00" /></label>
  </span>
</fieldset>
```
## CSS
```css
.if-18 {
  width: 100%;
  max-width: 320px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 12px 14px;
  background: #1a1a22;
}

.if-18-legend {
  padding: 0 6px;
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-18-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.if-18 label {
  flex: 1;
  display: grid;
  gap: 4px;
}

.if-18-cap {
  font-size: 10px;
  color: #b8b6d4;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.if-18 input {
  width: 100%;
  box-sizing: border-box;
  padding: 8px 10px;
  background: #0c0c12;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: #f0eeff;
  font: 600 13px/1 "JetBrains Mono", monospace;
  outline: none;
  color-scheme: dark;
}

.if-18 input:focus {
  border-color: #a78bfa;
}

.if-18-sep {
  color: #a78bfa;
  font-size: 14px;
  align-self: end;
  padding-bottom: 9px;
}
```
