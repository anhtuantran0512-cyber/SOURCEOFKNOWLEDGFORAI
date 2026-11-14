---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/ios-light-mode/"
title: "iOS Light Mode"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The iOS toggle in its light-theme presentation — clean white card backdrop, soft gray off-state, signature green on-state. Counterpart to demo 1."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS Light Mode
Source: https://codefronts.com/components/css-toggles-switches/ios-light-mode/

The iOS toggle in its light-theme presentation — clean white card backdrop, soft gray off-state, signature green on-state. Counterpart to demo 1.
## HTML
```html
<label class="tgl-44">
  <input class="tgl-44__input" type="checkbox" checked>
  <span class="tgl-44__track" aria-hidden="true">
    <span class="tgl-44__thumb"></span>
  </span>
  <span class="tgl-44__label">Bluetooth</span>
</label>
```
## CSS
```css
.tgl-44 {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
  font-size: 15px;
  color: #1a1a1f;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  background: #f2f2f7;
  box-sizing: border-box;
}

.tgl-44__input {
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

.tgl-44__track {
  position: relative;
  width: 51px;
  height: 31px;
  background: #e5e5ea;
  border-radius: 999px;
  transition: background 0.25s ease;
}

.tgl-44__thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 27px;
  height: 27px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 1px 2px rgba(0,0,0,0.18), 0 0 1px rgba(0,0,0,0.08);
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.tgl-44__input:checked ~ .tgl-44__track {
  background: #34c759;
}

.tgl-44__input:checked ~ .tgl-44__track .tgl-44__thumb {
  transform: translateX(20px);
}

.tgl-44__input:focus-visible ~ .tgl-44__track {
  outline: 2px solid #0a84ff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-44__track,
    .tgl-44__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — iOS geometry with light-surface color tuning; the thumb slides on transform:translateX inside a white card surface. */
```
