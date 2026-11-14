---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/liquid-border/"
title: "Liquid Border"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Animated stroke that draws around the field on focus. A small flourish that makes a single text input feel deliberate and premium."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Border
Source: https://codefronts.com/components/css-input-fields/liquid-border/

Animated stroke that draws around the field on focus. A small flourish that makes a single text input feel deliberate and premium.
## HTML
```html
<label class="if-06">
  <span class="if-06-label">Project name</span>
  <input type="text" name="project" placeholder="My next big idea…" required />
</label>
```
## CSS
```css
.if-06 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
  font-size: 11px;
  color: #b8b6d4;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.if-06 input {
  width: 100%;
  box-sizing: border-box;
  padding: 11px 14px;
  background: #1a1a22;
  border: 1px solid #2a2a36;
  border-radius: 8px;
  color: #f0eeff;
  font-size: 14px;
  letter-spacing: 0;
  text-transform: none;
  outline: none;
  background-image: linear-gradient(90deg, #fbbf24, #fbbf24), linear-gradient(0deg, #fbbf24, #fbbf24), linear-gradient(90deg, #fbbf24, #fbbf24), linear-gradient(0deg, #fbbf24, #fbbf24);
  background-repeat: no-repeat;
  background-size: 0 2px, 2px 0, 0 2px, 2px 0;
  background-position: 0 0, 100% 0, 100% 100%, 0 100%;
  transition: background-size 0.35s linear, border-color 0.2s;
}

.if-06 input::placeholder {
  color: #b8b6d4;
}

.if-06 input:focus {
  border-color: transparent;
  background-size: 100% 2px, 2px 100%, 100% 2px, 2px 100%;
  transition-delay: 0s, 0.35s, 0.7s, 1.05s;
  transition-duration: 0.35s;
}
```
