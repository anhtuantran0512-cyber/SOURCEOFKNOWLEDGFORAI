---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/flip-card/"
title: "Flip Card"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A 3D flip toggle — front face shows OFF, back face shows ON. Rotates around the Y axis on toggle. Showcases transform-style: preserve-3d."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flip Card
Source: https://codefronts.com/components/css-toggles-switches/flip-card/

A 3D flip toggle — front face shows OFF, back face shows ON. Rotates around the Y axis on toggle. Showcases transform-style: preserve-3d.
## HTML
```html
<label class="tgl-40">
  <input class="tgl-40__input" type="checkbox" checked>
  <span class="tgl-40__card" aria-hidden="true">
    <span class="tgl-40__face tgl-40__on">ON</span>
    <span class="tgl-40__face tgl-40__off">OFF</span>
  </span>
  <span class="tgl-40__label">Auto-save</span>
</label>
```
## CSS
```css
.tgl-40 {
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

.tgl-40__input {
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

.tgl-40__card {
  position: relative;
  width: 56px;
  height: 30px;
  transform-style: preserve-3d;
  transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
}

.tgl-40__face {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  border-radius: 6px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.tgl-40__on {
  background: linear-gradient(135deg, #2eb88a 0%, #1d9c70 100%);
  color: #fff;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.2);
}

.tgl-40__off {
  background: linear-gradient(135deg, #4a4a52 0%, #2a2a30 100%);
  color: #b8b6d4;
  transform: rotateY(180deg);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
}

.tgl-40__input:not(:checked) ~ .tgl-40__card {
  transform: rotateY(180deg);
}

.tgl-40__input:focus-visible ~ .tgl-40__card {
  outline: 2px solid #7c6cff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-40__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a preserve-3d card rotates rotateY(180°) between two backface-hidden ON/OFF faces. */
```
