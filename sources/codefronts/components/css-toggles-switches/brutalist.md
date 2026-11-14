---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/brutalist/"
title: "Brutalist"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "Hard edges, no shadows, monospace label, raw markup feel. The track and thumb are pure rectangles. A counterpoint to polished SaaS-style toggles."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist
Source: https://codefronts.com/components/css-toggles-switches/brutalist/

Hard edges, no shadows, monospace label, raw markup feel. The track and thumb are pure rectangles. A counterpoint to polished SaaS-style toggles.
## HTML
```html
<label class="tgl-38">
  <input class="tgl-38__input" type="checkbox" checked>
  <span class="tgl-38__track" aria-hidden="true">
    <span class="tgl-38__thumb"></span>
  </span>
  <span class="tgl-38__label">Tracking</span>
</label>
```
## CSS
```css
.tgl-38 {
  font-family: "Courier New", ui-monospace, monospace;
  font-size: 13px;
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

.tgl-38__input {
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

.tgl-38__track {
  /* Outer 60×28; with 2px border, inner space is 56×24. Thumb is a
       24×24 white block that slides inside that inner space. Track
       stays dark in both states — the thumb's position is the signal,
       not a color inversion, so the state is readable at a glance even
       in a static preview. */
  position: relative;
  width: 60px;
  height: 28px;
  background: #1a1a1a;
  border: 2px solid #f0eeff;
  border-radius: 0;
  transition: background 0.1s linear;
  box-sizing: border-box;
}

.tgl-38__thumb {
  position: absolute;
  top: 0;
  left: 0;
  width: 24px;
  height: 100%;
  background: #f0eeff;
  border-radius: 0;
  transition: left 0.1s linear;
}

.tgl-38__input:checked ~ .tgl-38__track .tgl-38__thumb {
  /* Inner width is 56px, thumb width 24px → 32px is the rightmost
       position that keeps the thumb fully inside the border. The track
       stays dark in both states — the thumb's position is the only
       state signal. Pure brutalist: stark contrast, no decoration. */
  left: 32px;
}

.tgl-38__input:focus-visible ~ .tgl-38__track {
  outline: 2px solid #ff6c8a;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-38__track,
    .tgl-38__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a light block thumb snaps 32px across a bordered dark track on a 0.1s linear transition; position IS the state. */
```
