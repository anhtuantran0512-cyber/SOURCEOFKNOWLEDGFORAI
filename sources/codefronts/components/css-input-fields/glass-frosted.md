---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/glass-frosted/"
title: "Glass Frosted"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Frosted-glass input on a soft gradient. Translucent surface with `backdrop-filter` blur and an inner highlight — an elegant fit for hero sections."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Frosted
Source: https://codefronts.com/components/css-input-fields/glass-frosted/

Frosted-glass input on a soft gradient. Translucent surface with `backdrop-filter` blur and an inner highlight — an elegant fit for hero sections.
## HTML
```html
<div class="if-04">
  <div class="if-04-bg" aria-hidden="true"></div>
  <label class="if-04-field">
    <span>Search</span>
    <input type="search" name="q" placeholder="Search anything…" />
  </label>
</div>
```
## CSS
```css
.if-04 {
  position: relative;
  width: 100%;
  max-width: 280px;
  border-radius: 14px;
  padding: 14px;
  isolation: isolate;
  overflow: hidden;
}

.if-04-bg {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: radial-gradient(40% 60% at 30% 30%, #f59e0b 0%, transparent 60%), radial-gradient(50% 60% at 80% 70%, #7c3aed 0%, transparent 60%), #0a0a14;
  filter: blur(24px);
  transform: scale(1.2);
}

.if-04-field {
  display: grid;
  gap: 6px;
  font-size: 11px;
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.if-04-field input {
  width: 100%;
  box-sizing: border-box;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border-radius: 10px;
  padding: 10px 12px;
  color: #fff;
  font-size: 14px;
  text-transform: none;
  letter-spacing: 0;
  outline: none;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.18);
  transition: border-color 0.2s, background 0.2s;
}

.if-04-field input::placeholder {
  color: rgba(255, 255, 255, 0.45);
}

.if-04-field input:focus {
  border-color: rgba(255, 255, 255, 0.5);
  background: rgba(255, 255, 255, 0.16);
}
```
