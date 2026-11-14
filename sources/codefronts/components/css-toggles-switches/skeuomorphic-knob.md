---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/skeuomorphic-knob/"
title: "Skeuomorphic Knob"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A brushed-metal rotary knob that physically rotates 90 degrees on toggle."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeuomorphic Knob
Source: https://codefronts.com/components/css-toggles-switches/skeuomorphic-knob/

A brushed-metal rotary knob that physically rotates 90 degrees on toggle. Different motion type from the sliding switches — rotation as the state signal. Tick marks anchor the dial.
## HTML
```html
<label class="tgl-43">
  <input class="tgl-43__input" type="checkbox" checked>
  <span class="tgl-43__stage" aria-hidden="true">
    <span class="tgl-43__tick tgl-43__t-off">OFF</span>
    <span class="tgl-43__tick tgl-43__t-on">ON</span>
    <span class="tgl-43__dial">
      <span class="tgl-43__indicator"></span>
    </span>
  </span>
  <span class="tgl-43__label">Power</span>
</label>
```
## CSS
```css
.tgl-43 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  color: #d8d4dc;
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

.tgl-43__input {
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

.tgl-43__stage {
  position: relative;
  width: 60px;
  height: 60px;
}

.tgl-43__tick {
  position: absolute;
  font-family: ui-monospace, "Fira Code", monospace;
  font-size: 8px;
  letter-spacing: 0.1em;
  color: #6a6a7a;
}

.tgl-43__t-off {
  top: 4px;
  left: 0;
}

.tgl-43__t-on {
  top: 4px;
  right: 0;
}

.tgl-43__dial {
  position: absolute;
  top: 12px;
  left: 6px;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #f0e8d8 0%, #6a5a30 90%);
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.4), inset 0 -2px 4px rgba(0,0,0,0.3), 0 2px 6px rgba(0,0,0,0.4);
  transform: rotate(-45deg);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.tgl-43__indicator {
  position: absolute;
  top: 4px;
  left: 50%;
  width: 3px;
  height: 14px;
  background: #2a1d0e;
  border-radius: 2px;
  transform: translateX(-50%);
}

.tgl-43__input:checked ~ .tgl-43__stage .tgl-43__dial {
  transform: rotate(45deg);
}

.tgl-43__input:checked ~ .tgl-43__stage .tgl-43__t-on {
  color: #d8b66e;
}

.tgl-43__input:not(:checked) ~ .tgl-43__stage .tgl-43__t-off {
  color: #d8b66e;
}

.tgl-43__input:focus-visible ~ .tgl-43__stage .tgl-43__dial {
  outline: 2px solid #d8b66e;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-43__dial {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the brass dial rotates a 90° throw (−45°→45°) between OFF/ON ticks, its indicator riding the same transform. */
```
