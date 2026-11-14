---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/outline/"
title: "Outline"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A pure-stroke toggle — track and thumb are outlines only, no fills."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Outline
Source: https://codefronts.com/components/css-toggles-switches/outline/

A pure-stroke toggle — track and thumb are outlines only, no fills. When toggled on, the thumb fills with brand color. Minimalist; pairs with the brutalist demo.
## HTML
```html
<label class="tgl-45">
  <input class="tgl-45__input" type="checkbox" checked>
  <span class="tgl-45__track" aria-hidden="true">
    <span class="tgl-45__thumb"></span>
  </span>
  <span class="tgl-45__label">Sync</span>
</label>
```
## CSS
```css
.tgl-45 {
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

.tgl-45__input {
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

.tgl-45__track {
  position: relative;
  width: 56px;
  height: 28px;
  background: transparent;
  border: 1px solid #6a6a7a;
  border-radius: 999px;
  transition: border-color 0.2s ease;
  box-sizing: border-box;
}

.tgl-45__thumb {
  position: absolute;
  top: 50%;
  left: 3px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: transparent;
  border: 1px solid #6a6a7a;
  transform: translateY(-50%);
  transition: left 0.2s cubic-bezier(0.4, 0, 0.2, 1), background 0.2s ease, border-color 0.2s ease;
}

.tgl-45__input:checked ~ .tgl-45__track {
  border-color: #7c6cff;
}

.tgl-45__input:checked ~ .tgl-45__track .tgl-45__thumb {
  /* Inner width: 56 - 2 = 54. Thumb 20. Max left: 54-20-3 = 31. */
  left: 31px;
  background: #7c6cff;
  border-color: #7c6cff;
}

.tgl-45__input:focus-visible ~ .tgl-45__track {
  outline: 2px solid #7c6cff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-45__track,
    .tgl-45__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hollow 1px-stroke track and thumb; :checked fills the thumb solid and recolors both strokes. */
```
