---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/neon-glow/"
title: "Neon Glow"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Cyan neon-glow input. The border crisps and the box-shadow blooms on focus — perfect for dark dashboards, gaming UIs, and developer tools."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow
Source: https://codefronts.com/components/css-input-fields/neon-glow/

Cyan neon-glow input. The border crisps and the box-shadow blooms on focus — perfect for dark dashboards, gaming UIs, and developer tools.
## HTML
```html
<label class="if-03">
  <span class="if-03-label">SECURE TOKEN</span>
  <input type="text" name="token" placeholder="sk_live_••••••••••••" required />
</label>
```
## CSS
```css
.if-03 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-03-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.18em;
  color: #6cffff;
  text-shadow: 0 0 8px rgba(108, 255, 255, 0.5);
}

.if-03 input {
  width: 100%;
  box-sizing: border-box;
  background: #0a0a14;
  border: 1px solid rgba(108, 255, 255, 0.4);
  border-radius: 6px;
  padding: 11px 14px;
  color: #fff;
  font-family: "JetBrains Mono", monospace;
  font-size: 13px;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s, background 0.2s;
}

.if-03 input::placeholder {
  color: rgba(108, 255, 255, 0.45);
}

.if-03 input:focus {
  border-color: #6cffff;
  background: #0d1820;
  box-shadow: 0 0 0 1px #6cffff, 0 0 16px rgba(108, 255, 255, 0.45), inset 0 0 12px rgba(108, 255, 255, 0.12);
}
```
