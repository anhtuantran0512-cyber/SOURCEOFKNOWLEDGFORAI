---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/floating-label/"
title: "Floating Label"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Classic floating label input. The placeholder lifts and shrinks above the field on focus — a calm, accessible pattern used across every modern product surface."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Label
Source: https://codefronts.com/components/css-input-fields/floating-label/

Classic floating label input. The placeholder lifts and shrinks above the field on focus — a calm, accessible pattern used across every modern product surface.
## HTML
```html
<label class="if-01">
  <input type="email" name="email" autocomplete="email" placeholder=" " required />
  <span class="if-01-label">Email address</span>
</label>
```
## CSS
```css
.if-01 {
  position: relative;
  display: block;
  width: 100%;
  max-width: 280px;
}

.if-01 input {
  width: 100%;
  box-sizing: border-box;
  padding: 18px 14px 8px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  color: #f0eeff;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
}

.if-01 input:focus {
  border-color: #7c6cff;
  background: #1f1f2a;
}

.if-01-label {
  position: absolute;
  left: 14px;
  top: 14px;
  font-size: 13px;
  color: #b8b6d4;
  pointer-events: none;
  transition: transform 0.2s, font-size 0.2s, color 0.2s;
}

.if-01 input:focus + .if-01-label,
.if-01 input:not(:placeholder-shown) + .if-01-label {
  transform: translateY(-9px);
  font-size: 10px;
  color: #a78bfa;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
```
