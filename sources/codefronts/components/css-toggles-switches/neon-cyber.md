---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/neon-cyber/"
title: "Neon Cyber"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A glowing neon outline toggle — dark track with a cyan thumb that pulses with a soft glow when active. Futuristic dashboard aesthetic."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Cyber
Source: https://codefronts.com/components/css-toggles-switches/neon-cyber/

A glowing neon outline toggle — dark track with a cyan thumb that pulses with a soft glow when active. Futuristic dashboard aesthetic.
## HTML
```html
<label class="tgl-37">
  <input class="tgl-37__input" type="checkbox" checked>
  <span class="tgl-37__track" aria-hidden="true">
    <span class="tgl-37__thumb"></span>
  </span>
  <span class="tgl-37__label">Shields</span>
</label>
```
## CSS
```css
.tgl-37 {
  font-family: "JetBrains Mono", "Fira Code", ui-monospace, monospace;
  font-size: 11px;
  color: #b8e8f0;
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

.tgl-37__input {
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

.tgl-37__track {
  position: relative;
  width: 54px;
  height: 26px;
  background: #0a1320;
  border: 1px solid rgba(0, 220, 255, 0.3);
  border-radius: 999px;
  transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

.tgl-37__thumb {
  position: absolute;
  top: 50%;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #6be8ff 0%, #0a90b8 100%);
  transform: translateY(-50%);
  box-shadow: 0 0 6px rgba(0, 220, 255, 0.4), inset 0 1px 1px rgba(255,255,255,0.4);
  transition: left 0.25s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.25s ease;
}

.tgl-37__input:checked ~ .tgl-37__track {
  border-color: rgba(0, 220, 255, 0.9);
  box-shadow: 0 0 12px rgba(0, 220, 255, 0.5), inset 0 0 8px rgba(0, 220, 255, 0.15);
}

.tgl-37__input:checked ~ .tgl-37__track .tgl-37__thumb {
  left: 33px;
  box-shadow: 0 0 14px rgba(0, 220, 255, 0.9), inset 0 1px 1px rgba(255,255,255,0.5);
}

.tgl-37__input:focus-visible ~ .tgl-37__track {
  outline: 2px solid #6be8ff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-37__track,
    .tgl-37__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — graded-alpha box-shadow layers ignite the track border and thumb orb on :checked. */
```
