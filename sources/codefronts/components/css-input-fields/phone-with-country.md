---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/phone-with-country/"
title: "Phone with Country"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Phone number input with a native <select> for the country dialling code. Semantic, accessible by default, and styled to match the input seamlessly."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Phone with Country
Source: https://codefronts.com/components/css-input-fields/phone-with-country/

Phone number input with a native <select> for the country dialling code. Semantic, accessible by default, and styled to match the input seamlessly.
## HTML
```html
<label class="if-13">
  <span class="if-13-label">Phone</span>
  <span class="if-13-wrap">
    <select aria-label="Country code" name="country">
      <option value="+44">🇬🇧 +44</option>
      <option value="+1" selected>🇺🇸 +1</option>
      <option value="+91">🇮🇳 +91</option>
      <option value="+33">🇫🇷 +33</option>
      <option value="+49">🇩🇪 +49</option>
      <option value="+81">🇯🇵 +81</option>
    </select>
    <input type="tel" name="phone" autocomplete="tel" placeholder="(555) 123-4567" required />
  </span>
</label>
```
## CSS
```css
.if-13 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
  font-size: 11px;
  color: #b8b6d4;
}

.if-13-label {
  font-weight: 600;
}

.if-13-wrap {
  display: grid;
  grid-template-columns: auto 1fr;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  overflow: hidden;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.if-13-wrap:focus-within {
  border-color: #ef4444;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.15);
}

.if-13 select {
  background: rgba(255, 255, 255, 0.04);
  border: 0;
  border-right: 1px solid rgba(255, 255, 255, 0.1);
  outline: none;
  color: #f0eeff;
  font-size: 13px;
  padding: 10px 28px 10px 12px;
  cursor: pointer;
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6' fill='none' stroke='%239d9bbf' stroke-width='1.5' stroke-linecap='round'><path d='M1 1l4 4 4-4'/></svg>");
  background-repeat: no-repeat;
  background-position: right 10px center;
}

.if-13 select option {
  background: #1a1a22;
  color: #f0eeff;
}

.if-13 input {
  background: transparent;
  border: 0;
  outline: none;
  color: #f0eeff;
  font-size: 14px;
  padding: 10px 12px;
  min-width: 0;
}

.if-13 input::placeholder {
  color: #b8b6d4;
}
```
