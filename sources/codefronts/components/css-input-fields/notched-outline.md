---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/notched-outline/"
title: "Notched Outline"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Material-style notched outline. The label sits inside a gap cut into the border. Subtle, professional, and works beautifully for forms with dense fields."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notched Outline
Source: https://codefronts.com/components/css-input-fields/notched-outline/

Material-style notched outline. The label sits inside a gap cut into the border. Subtle, professional, and works beautifully for forms with dense fields.
## HTML
```html
<label class="if-05">
  <span class="if-05-label">Full name</span>
  <input type="text" name="name" autocomplete="name" placeholder=" " required />
  <span class="if-05-frame" aria-hidden="true">
    <span class="if-05-l"></span>
    <span class="if-05-cut"><span>Full name</span></span>
    <span class="if-05-r"></span>
  </span>
</label>
```
## CSS
```css
.if-05 {
  position: relative;
  display: block;
  width: 100%;
  max-width: 280px;
}

.if-05 input {
  width: 100%;
  box-sizing: border-box;
  padding: 13px 14px;
  background: transparent;
  border: 0;
  outline: none;
  color: #f0eeff;
  font-size: 14px;
  position: relative;
  z-index: 1;
}

.if-05 input::placeholder {
  color: transparent;
}

.if-05-label {
  position: absolute;
  left: 14px;
  top: 13px;
  font-size: 13px;
  color: #b8b6d4;
  pointer-events: none;
  transition: opacity 0.15s;
  z-index: 2;
}

.if-05 input:focus ~ .if-05-label,
.if-05 input:not(:placeholder-shown) ~ .if-05-label {
  opacity: 0;
}

.if-05-frame {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: 12px auto 1fr;
  pointer-events: none;
}

.if-05-l,
.if-05-cut,
.if-05-r {
  border: 1px solid rgba(46, 184, 138, 0.35);
  transition: border-color 0.2s;
}

.if-05-l {
  border-right: 0;
  border-radius: 8px 0 0 8px;
}

.if-05-r {
  border-left: 0;
  border-radius: 0 8px 8px 0;
}

.if-05-cut {
  border-left: 0;
  border-right: 0;
  position: relative;
  display: flex;
  align-items: center;
  padding: 0 6px;
}

.if-05-cut > span {
  font-size: 10px;
  color: rgba(46, 184, 138, 0.85);
  font-weight: 600;
  background: #07070f;
  padding: 0 4px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transform: translateY(-13px) scale(0);
  transform-origin: left center;
  transition: transform 0.2s ease;
}

.if-05 input:focus ~ .if-05-frame .if-05-cut > span,
.if-05 input:not(:placeholder-shown) ~ .if-05-frame .if-05-cut > span {
  transform: translateY(-13px) scale(1);
}

.if-05:focus-within .if-05-l,
.if-05:focus-within .if-05-cut,
.if-05:focus-within .if-05-r {
  border-color: #2eb88a;
}
```
