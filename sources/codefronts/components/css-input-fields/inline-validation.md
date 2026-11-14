---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/inline-validation/"
title: "Inline Validation"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Live `:valid` / `:invalid` feedback. Green tick when correct, red cross when not — driven by `:has()` and pseudo-elements, no JavaScript required."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Validation
Source: https://codefronts.com/components/css-input-fields/inline-validation/

Live `:valid` / `:invalid` feedback. Green tick when correct, red cross when not — driven by `:has()` and pseudo-elements, no JavaScript required.
## HTML
```html
<label class="if-07">
  <span class="if-07-label">Email</span>
  <span class="if-07-wrap">
    <input type="email" name="email" autocomplete="email" placeholder="[email protected]" required />
  </span>
  <span class="if-07-help">We'll never share your address.</span>
</label>
```
## CSS
```css
.if-07 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
  font-size: 11px;
  color: #b8b6d4;
}

.if-07-label {
  font-weight: 600;
  letter-spacing: 0.04em;
}

.if-07-wrap {
  position: relative;
  display: block;
}

.if-07 input {
  width: 100%;
  box-sizing: border-box;
  padding: 11px 38px 11px 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: #f0eeff;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
}

.if-07 input:focus {
  border-color: #7c6cff;
}

.if-07-wrap::after {
  content: "";
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%) scale(0.5);
  width: 18px;
  height: 18px;
  border-radius: 50%;
  opacity: 0;
  transition: transform 0.2s, opacity 0.2s, background 0.2s;
}

.if-07:has(input:not(:placeholder-shown):invalid) input {
  border-color: rgba(239, 68, 68, 0.55);
}

.if-07:has(input:not(:placeholder-shown):invalid) .if-07-wrap::after {
  opacity: 1;
  transform: translateY(-50%) scale(1);
  background: #ef4444 url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 10 10' fill='none' stroke='white' stroke-width='1.6' stroke-linecap='round'><path d='M2 2 L8 8 M8 2 L2 8'/></svg>") center/10px no-repeat;
}

.if-07:has(input:not(:placeholder-shown):valid) input {
  border-color: rgba(34, 197, 94, 0.55);
}

.if-07:has(input:not(:placeholder-shown):valid) .if-07-wrap::after {
  opacity: 1;
  transform: translateY(-50%) scale(1);
  background: #22c55e url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 10 10' fill='none' stroke='white' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'><path d='M2 5 L4.2 7.2 L8 3'/></svg>") center/10px no-repeat;
}

.if-07-help {
  font-size: 10.5px;
  color: #b8b6d4;
}
```
