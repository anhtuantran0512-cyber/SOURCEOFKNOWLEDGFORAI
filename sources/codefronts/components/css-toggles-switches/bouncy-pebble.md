---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/bouncy-pebble/"
title: "Bouncy Pebble"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A chunky outlined toggle with an organic \"pebble\" thumb shape built from 8-value border-radius syntax."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncy Pebble
Source: https://codefronts.com/components/css-toggles-switches/bouncy-pebble/

A chunky outlined toggle with an organic "pebble" thumb shape built from 8-value border-radius syntax. Bouncy springy transition with anticipation + overshoot. Track and thumb swap colors on each state. The reference for hand-crafted, designer-drawn toggles — distinctive from every other demo in the collection.
## HTML
```html
<label class="tgl-46">
  <input class="tgl-46__input" type="checkbox" checked>
  <span class="tgl-46__track" aria-hidden="true">
    <span class="tgl-46__thumb"></span>
  </span>
  <span class="tgl-46__label">Theme: butter</span>
</label>
```
## CSS
```css
.tgl-46 {
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

.tgl-46__input {
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

.tgl-46__track {
  position: relative;
  width: 150px;
  height: 74px;
  background: #f3f3f3;
  border-radius: 999px;
  box-shadow: inset 0 0 0 3px #2a2a2a, 0 10px 20px rgba(0,0,0,0.35);
  transition: background 0.35s ease;
}

.tgl-46__thumb {
  position: absolute;
  top: 50%;
  left: 10px;
  width: 48px;
  height: 48px;
  background: #f4df72;
  border: 3px solid #2b2b2b;
  box-shadow: 0 5px 10px rgba(0,0,0,0.25);
  /* 8-value border-radius (horizontal × vertical radii per corner)
       creates the organic asymmetric pebble shape: fuller left, tighter
       right, subtle diagonal tension. The -2deg tilt adds hand-crafted
       irregularity. The cubic-bezier easing has anticipation (negative
       control point) and overshoot (>1 control point) — the thumb
       pulls back slightly before sliding, then overshoots the
       destination before settling. */
  border-radius: 52% 38% 42% 58% / 52% 42% 58% 48%;
  transform: translateY(-50%) rotate(-2deg);
  transition: all 0.35s cubic-bezier(0.68, -0.4, 0.27, 1.4);
}

.tgl-46__input:checked ~ .tgl-46__track {
  background: #f4df72;
}

.tgl-46__input:checked ~ .tgl-46__track .tgl-46__thumb {
  /* Slides to right edge. Track is 150px wide, thumb is 48px + 3px×2
       border = 54px total. left: calc(100% - 64px) gives 10px from the
       right edge, mirroring the 10px from the left in the off state. */
  left: calc(100% - 64px);
  background: #f5f5f5;
  /* Mirrored border-radius — horizontal asymmetry flips. The "fuller"
       side is now the right (the direction the thumb just came from). */
  border-radius: 38% 52% 58% 42% / 42% 52% 48% 58%;
  transform: translateY(-50%) rotate(2deg);
}

.tgl-46__input:focus-visible ~ .tgl-46__track {
  outline: 3px solid #7c6cff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-46__track,
    .tgl-46__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an 8-value border-radius pebble slides on an anticipation/overshoot bezier, mirroring its radii and tilt on landing. */
```
