---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/glassmorphism/"
title: "Glassmorphism"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A frosted-glass pill with a backdrop-blurred thumb. The colored backdrop tints the glass; the thumb floats above it. Modern dark-mode aesthetic."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism
Source: https://codefronts.com/components/css-toggles-switches/glassmorphism/

A frosted-glass pill with a backdrop-blurred thumb. The colored backdrop tints the glass; the thumb floats above it. Modern dark-mode aesthetic.
## HTML
```html
<label class="tgl-42">
  <input class="tgl-42__input" type="checkbox" checked>
  <span class="tgl-42__track" aria-hidden="true">
    <span class="tgl-42__thumb"></span>
  </span>
  <span class="tgl-42__label">Focus mode</span>
</label>
```
## CSS
```css
.tgl-42 {
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
  font-size: 14px;
  color: #f0eeff;
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

.tgl-42__input {
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

.tgl-42__track {
  position: relative;
  width: 56px;
  height: 30px;
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 999px;
  transition: background 0.3s ease, border-color 0.3s ease;
  box-sizing: border-box;
}

.tgl-42__thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(255,255,255,0.85);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.6), 0 2px 6px rgba(0,0,0,0.18);
  transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1), background 0.3s ease;
}

.tgl-42__input:checked ~ .tgl-42__track {
  background: rgba(124,108,255,0.32);
  border-color: rgba(124,108,255,0.55);
}

.tgl-42__input:checked ~ .tgl-42__track .tgl-42__thumb {
  /* Inner width: 56 - 2 = 54. Thumb 24. Max left to stay inside: 54-24-2 = 28. */
  left: 28px;
  background: rgba(255,255,255,0.95);
}

.tgl-42__input:focus-visible ~ .tgl-42__track {
  outline: 2px solid rgba(255,255,255,0.7);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-42__track,
    .tgl-42__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a blurred 8%-white glass track over a gradient backdrop tints violet on :checked while a denser glass puck slides across. */
```
