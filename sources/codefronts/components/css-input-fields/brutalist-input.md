---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/brutalist-input/"
title: "Brutalist Input"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Bold offset-shadow stamp with hard edges and monospace type — a confident input that doesn't apologize for itself. Press collapses into the shadow on focus."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Input
Source: https://codefronts.com/components/css-input-fields/brutalist-input/

Bold offset-shadow stamp with hard edges and monospace type — a confident input that doesn't apologize for itself. Press collapses into the shadow on focus.
## HTML
```html
<label class="if-28">
  <span class="if-28-label">USERNAME_</span>
  <input type="text" name="user-brut" placeholder="enter handle..." />
</label>
```
## CSS
```css
.if-28 {
  display: grid;
  gap: 8px;
  width: 100%;
  max-width: 280px;
}

.if-28-label {
  font-family: "Courier New", monospace;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #f0eeff;
}

.if-28 input {
  width: 100%;
  box-sizing: border-box;
  padding: 12px 14px;
  background: #f0eeff;
  border: 2.5px solid #1a1a2e;
  border-radius: 0;
  color: #1a1a2e;
  font: 700 13px/1 "Courier New", monospace;
  letter-spacing: 0.06em;
  outline: none;
  box-shadow: 5px 5px 0 #ff6c8a;
  transition: transform 0.1s, box-shadow 0.1s;
}

.if-28 input::placeholder {
  color: rgba(26, 26, 46, 0.5);
}

.if-28 input:focus {
  transform: translate(2px, 2px);
  box-shadow: 3px 3px 0 #ff6c8a;
}

.if-28 input:invalid:not(:placeholder-shown) {
  box-shadow: 5px 5px 0 #ff5d6c;
}
```
