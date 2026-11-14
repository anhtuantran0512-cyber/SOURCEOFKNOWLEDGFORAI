---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/industrial-rocker/"
title: "Industrial Rocker"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A chunky industrial rocker switch with twin indicator lights, rotating \"teeth\" along the rail, and a color-shifting metallic thumb."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Industrial Rocker
Source: https://codefronts.com/components/css-toggles-switches/industrial-rocker/

A chunky industrial rocker switch with twin indicator lights, rotating "teeth" along the rail, and a color-shifting metallic thumb. The off-light glows red; the on-light glows brand purple. Inspired by heavy-duty equipment power switches.
## HTML
```html
<label class="tgl-47">
  <input class="tgl-47__input" type="checkbox" checked>
  <span class="tgl-47__body" aria-hidden="true">
    <span class="tgl-47__lights">
      <span class="tgl-47__light tgl-47__light-off"></span>
      <span class="tgl-47__light tgl-47__light-on"></span>
    </span>
    <span class="tgl-47__track-top">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </span>
    <span class="tgl-47__rail"></span>
    <span class="tgl-47__thumb"></span>
    <span class="tgl-47__track-bot">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </span>
  </span>
  <span class="tgl-47__label">Power</span>
</label>
```
## CSS
```css
@property --tgl-47-shine {
  syntax: "<color>";
  initial-value: #f50000;
  inherits: false;
}

.tgl-47 {
  --tgl-47-sz: 8px;
  --tgl-47-off: #f50000;
  --tgl-47-on: #7c6cff;
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
  font-size: 14px;
  color: #1a1a2e;
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

.tgl-47__input {
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
/* Body proportions: 28×sz wide, 18×sz tall.
   Layout regions stacked vertically:
     row 1 (top): lights row, ~3×sz tall
     row 2: top track teeth, ~1.5×sz tall
     row 3: rail + thumb, ~7×sz tall (the main switch)
     row 4: bottom track teeth, ~1.5×sz tall */

.tgl-47__body {
  position: relative;
  display: inline-block;
  width: calc(var(--tgl-47-sz) * 28);
  height: calc(var(--tgl-47-sz) * 18);
}

.tgl-47__lights {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: calc(var(--tgl-47-sz) * 2);
}

.tgl-47__light {
  width: calc(var(--tgl-47-sz) * 1.4);
  height: calc(var(--tgl-47-sz) * 1.4);
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #4a4a52, #1a1a1f);
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.6);
  transition: all 0.5s ease;
}
/* Rail spans the full body width, vertically centered. */

.tgl-47__rail {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: calc(var(--tgl-47-sz) * 7);
  transform: translateY(-50%);
  background: linear-gradient(180deg, #2a2a30, #0a0a0e);
  border-radius: calc(var(--tgl-47-sz) * 0.8);
  box-shadow: inset 0 2px 6px rgba(0,0,0,0.8), inset 0 -1px 2px rgba(255,255,255,0.05), 0 2px 4px rgba(0,0,0,0.3);
}
/* Thumb: ~12×sz wide (almost half the body), 6×sz tall, sits on the rail. */

.tgl-47__thumb {
  position: absolute;
  top: 50%;
  left: calc(var(--tgl-47-sz) * 1);
  width: calc(var(--tgl-47-sz) * 12);
  height: calc(var(--tgl-47-sz) * 5.5);
  transform: translateY(-50%);
  background: linear-gradient(180deg, #c0c0c8 0%, #8a8a92 45%, #4a4a52 100%);
  border-radius: calc(var(--tgl-47-sz) * 0.6);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), inset 0 -2px 4px rgba(0,0,0,0.5), 0 3px 6px rgba(0,0,0,0.5), 0 0 calc(var(--tgl-47-sz) * 1.8) var(--tgl-47-shine);
  transition: left 0.5s ease, --tgl-47-shine 0.5s ease;
}
/* Grip lines: three horizontal bars across the thumb face. */

.tgl-47__thumb::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 25%;
  right: 25%;
  height: 1px;
  transform: translateY(-50%);
  background: rgba(0,0,0,0.55);
  box-shadow: 0 calc(var(--tgl-47-sz) * 0.6) 0 rgba(0,0,0,0.55), 0 calc(var(--tgl-47-sz) * -0.6) 0 rgba(0,0,0,0.55);
}

.tgl-47__track-top,
.tgl-47__track-bot {
  position: absolute;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  padding: 0 calc(var(--tgl-47-sz) * 1);
}

.tgl-47__track-top {
  top: calc(var(--tgl-47-sz) * 3);
}

.tgl-47__track-bot {
  bottom: calc(var(--tgl-47-sz) * 0);
}

.tgl-47__track-top span,
.tgl-47__track-bot span {
  width: calc(var(--tgl-47-sz) * 1);
  height: calc(var(--tgl-47-sz) * 1);
  background: #3a3a42;
  border-radius: 1px;
  transition: transform 0.5s ease;
}
/* Off state — left light glows red. */

.tgl-47__light-off {
  background: radial-gradient(circle at 35% 35%, #ff7575, var(--tgl-47-off));
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.3), 0 0 calc(var(--tgl-47-sz) * 1.2) var(--tgl-47-off);
}
/* On state — left dims, right lights up purple, thumb slides right. */

.tgl-47__input:checked ~ .tgl-47__body .tgl-47__light-off {
  background: radial-gradient(circle at 35% 35%, #4a4a52, #1a1a1f);
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.6);
}

.tgl-47__input:checked ~ .tgl-47__body .tgl-47__light-on {
  background: radial-gradient(circle at 35% 35%, #b5a8ff, var(--tgl-47-on));
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.3), 0 0 calc(var(--tgl-47-sz) * 1.2) var(--tgl-47-on);
}

.tgl-47__input:checked ~ .tgl-47__body .tgl-47__thumb {
  left: calc(100% - var(--tgl-47-sz) * 13);
  --tgl-47-shine: #7c6cff;
}

.tgl-47__input:checked ~ .tgl-47__body .tgl-47__track-top span {
  transform: rotate(20deg);
}

.tgl-47__input:checked ~ .tgl-47__body .tgl-47__track-bot span {
  transform: rotate(-20deg);
}

.tgl-47__input:focus-visible ~ .tgl-47__body .tgl-47__rail {
  outline: 2px solid #7c6cff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-47__thumb,
    .tgl-47__light,
    .tgl-47__track-top span,
    .tgl-47__track-bot span {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a registered @property <color> lets the thumb's under-glow tween red→purple while lamps crossfade and rail teeth rotate. */
```
