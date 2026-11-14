---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/underline-sweep/"
title: "Underline Sweep"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Minimal underline-style input. The bottom border draws outward from the centre on focus — a subtle, premium touch driven by `:focus-within`."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Underline Sweep
Source: https://codefronts.com/components/css-input-fields/underline-sweep/

Minimal underline-style input. The bottom border draws outward from the centre on focus — a subtle, premium touch driven by `:focus-within`.
## HTML
```html
<label class="if-02">
  <span class="if-02-label">Username</span>
  <span class="if-02-wrap">
    <input type="text" name="username" autocomplete="username" placeholder="@codefronts" required />
  </span>
</label>
```
## CSS
```css
.if-02 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
  font-size: 11px;
  color: #b8b6d4;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.if-02-wrap {
  position: relative;
  display: block;
  border-bottom: 1px solid rgba(255, 255, 255, 0.14);
}

.if-02-wrap::after {
  content: "";
  position: absolute;
  left: 50%;
  right: 50%;
  bottom: -1px;
  height: 2px;
  background: linear-gradient(90deg, #ff6c8a, #ff9a76);
  transition: left 0.3s ease, right 0.3s ease;
}

.if-02-wrap:focus-within::after {
  left: 0;
  right: 0;
}

.if-02 input {
  width: 100%;
  box-sizing: border-box;
  padding: 8px 0 9px;
  background: transparent;
  border: 0;
  outline: none;
  color: #f0eeff;
  font-size: 14px;
  letter-spacing: 0;
  text-transform: none;
}

.if-02 input::placeholder {
  color: #b8b6d4;
}
```
