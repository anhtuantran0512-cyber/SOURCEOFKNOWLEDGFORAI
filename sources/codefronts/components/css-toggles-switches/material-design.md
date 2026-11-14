---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/material-design/"
title: "Material Design"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "Google Material Design 3 switch — track with rounded thumb that lifts and changes colour on toggle. Active state shows a filled icon-style indicator."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design
Source: https://codefronts.com/components/css-toggles-switches/material-design/

Google Material Design 3 switch — track with rounded thumb that lifts and changes colour on toggle. Active state shows a filled icon-style indicator.
## HTML
```html
<label class="tgl-35">
  <input class="tgl-35__input" type="checkbox" checked>
  <span class="tgl-35__track" aria-hidden="true">
    <span class="tgl-35__thumb"></span>
  </span>
  <span class="tgl-35__label">Notifications</span>
</label>
```
## CSS
```css
.tgl-35 {
  font-family: "Roboto", "Google Sans", sans-serif;
  font-size: 14px;
  color: #e6e0e9;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  background: #14141e;
  box-sizing: border-box;
}

.tgl-35__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.tgl-35__track {
  position: relative;
  width: 52px;
  height: 32px;
  background: #49454f;
  border: 2px solid #79747e;
  border-radius: 999px;
  transition: background 0.2s ease, border-color 0.2s ease;
  box-sizing: border-box;
}

.tgl-35__thumb {
  position: absolute;
  top: 50%;
  left: 6px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #cac4d0;
  transform: translateY(-50%);
  transition: left 0.2s cubic-bezier(0.4, 0, 0.2, 1), width 0.15s ease, height 0.15s ease, background 0.2s ease;
}

.tgl-35__input:checked ~ .tgl-35__track {
  background: #d0bcff;
  border-color: #d0bcff;
}

.tgl-35__input:checked ~ .tgl-35__track .tgl-35__thumb {
  /* Inner width is 48px (52 - 2px border × 2). Thumb grows to 24px
       on-state, so max left value that keeps the thumb fully inside the
       border is 48 - 24 = 24px, minus 2px breathing room = 22px. */
  left: 22px;
  width: 24px;
  height: 24px;
  background: #381e72;
}

.tgl-35__input:focus-visible ~ .tgl-35__track {
  outline: 2px solid #d0bcff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-35__track,
    .tgl-35__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the M3 thumb grows 16→24px and shifts left:6→22px on separate transitions while track and border merge to the tonal fill. */
```
