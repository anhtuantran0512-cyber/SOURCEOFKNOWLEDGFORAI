---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/date-picker-native/"
title: "Date Picker Native"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "A styled <input type=\"date\"> keeps every native picker behaviour (keyboard, accessibility, browser/OS calendars) while the chrome matches the rest of your form."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Date Picker Native
Source: https://codefronts.com/components/css-input-fields/date-picker-native/

A styled <input type="date"> keeps every native picker behaviour (keyboard, accessibility, browser/OS calendars) while the chrome matches the rest of your form. `::-webkit-calendar-picker-indicator` is recoloured to match the accent.
## HTML
```html
<label class="if-17">
  <span class="if-17-label">Start date</span>
  <input type="date" name="start" />
</label>
```
## CSS
```css
.if-17 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-17-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-17 input {
  width: 100%;
  box-sizing: border-box;
  padding: 12px 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  color: #f0eeff;
  font: 500 14px/1 system-ui, sans-serif;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
  color-scheme: dark;
}

.if-17 input:focus {
  border-color: #06b6d4;
  background: #1f1f2a;
}

.if-17 input::-webkit-calendar-picker-indicator {
  filter: invert(0.7) sepia(1) saturate(5) hue-rotate(150deg);
  cursor: pointer;
  opacity: 0.8;
}

.if-17 input::-webkit-calendar-picker-indicator:hover {
  opacity: 1;
}
```
