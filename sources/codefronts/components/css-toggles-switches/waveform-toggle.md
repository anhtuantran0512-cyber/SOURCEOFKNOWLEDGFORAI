---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/waveform-toggle/"
title: "Waveform Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "Static audio bars spring to life with staggered breathing animations when toggled on."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Waveform Toggle
Source: https://codefronts.com/components/css-toggles-switches/waveform-toggle/

Static audio bars spring to life with staggered breathing animations when toggled on. The track border and indicator dot pulse with an ice-cyan glow. Audio-visual data physicality — toggle = sound on/off.
## HTML
```html
<label class="tgl-29">
  <input class="tgl-29__input" type="checkbox" checked>
  <span class="tgl-29__body" aria-hidden="true">
    <span class="tgl-29__bars">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span>
    </span>
    <span class="tgl-29__text">Microphone</span>
    <span class="tgl-29__dot"></span>
  </span>
</label>
```
## CSS
```css
.tgl-29 {
  --tgl-29-rim: #14141e;
  --tgl-29-wire: #1e1e2e;
  --tgl-29-fog: #3a3a52;
  --tgl-29-ash: #7a7a98;
  --tgl-29-ice: #00e5ff;
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
  font-size: 14px;
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

.tgl-29__input {
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

.tgl-29__body {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 12px;
  background: var(--tgl-29-rim);
  border: 1px solid var(--tgl-29-wire);
  min-width: 240px;
  transition: border-color 0.3s ease, background 0.3s ease;
}

.tgl-29__bars {
  display: flex;
  align-items: center;
  gap: 2.5px;
  height: 28px;
}

.tgl-29__bars span {
  display: block;
  width: 3px;
  border-radius: 2px;
  background: var(--tgl-29-fog);
  transition: background 0.3s ease, height 0.3s ease;
}
/* Static heights (off state) — each bar has its own resting height. */

.tgl-29__bars span:nth-child(1) {
  height: 8px;
}

.tgl-29__bars span:nth-child(2) {
  height: 14px;
}

.tgl-29__bars span:nth-child(3) {
  height: 20px;
}

.tgl-29__bars span:nth-child(4) {
  height: 26px;
}

.tgl-29__bars span:nth-child(5) {
  height: 18px;
}

.tgl-29__bars span:nth-child(6) {
  height: 24px;
}

.tgl-29__bars span:nth-child(7) {
  height: 12px;
}

.tgl-29__bars span:nth-child(8) {
  height: 20px;
}

.tgl-29__bars span:nth-child(9) {
  height: 8px;
}

.tgl-29__text {
  font-size: 13px;
  color: var(--tgl-29-ash);
  transition: color 0.3s ease;
}

.tgl-29__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--tgl-29-wire);
  margin-left: auto;
  flex-shrink: 0;
  transition: background 0.3s ease, box-shadow 0.3s ease;
}
/* Each bar oscillates between its resting height and ~30% of it. The
   varied durations + delays keep the pattern from looking robotic. */

@keyframes tgl-29-breathe {
  0%,
    100% {
    height: var(--tgl-29-h);
  }

  50% {
    height: calc(var(--tgl-29-h) * 0.3 + 4px);
  }
}

.tgl-29__input:checked ~ .tgl-29__body {
  border-color: rgba(0,229,255,0.3);
  background: rgba(0,229,255,0.04);
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span {
  background: var(--tgl-29-ice);
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(1) {
  animation: tgl-29-breathe 0.9s ease-in-out infinite;
  --tgl-29-h: 8px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(2) {
  animation: tgl-29-breathe 0.7s ease-in-out 0.1s infinite;
  --tgl-29-h: 14px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(3) {
  animation: tgl-29-breathe 1.1s ease-in-out 0.2s infinite;
  --tgl-29-h: 20px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(4) {
  animation: tgl-29-breathe 0.8s ease-in-out 0.05s infinite;
  --tgl-29-h: 26px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(5) {
  animation: tgl-29-breathe 1.0s ease-in-out 0.15s infinite;
  --tgl-29-h: 18px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(6) {
  animation: tgl-29-breathe 0.6s ease-in-out 0.25s infinite;
  --tgl-29-h: 24px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(7) {
  animation: tgl-29-breathe 0.9s ease-in-out 0.08s infinite;
  --tgl-29-h: 12px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(8) {
  animation: tgl-29-breathe 1.2s ease-in-out 0.18s infinite;
  --tgl-29-h: 20px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span:nth-child(9) {
  animation: tgl-29-breathe 0.75s ease-in-out 0.3s infinite;
  --tgl-29-h: 8px;
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__text {
  color: var(--tgl-29-ice);
}

.tgl-29__input:checked ~ .tgl-29__body .tgl-29__dot {
  background: var(--tgl-29-ice);
  box-shadow: 0 0 8px var(--tgl-29-ice);
}

.tgl-29__input:focus-visible ~ .tgl-29__body {
  outline: 2px solid var(--tgl-29-ice);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-29__body,
    .tgl-29__bars span,
    .tgl-29__dot,
    .tgl-29__text {
    transition: none;
  }

  .tgl-29__input:checked ~ .tgl-29__body .tgl-29__bars span {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one keyframe block reads a per-bar --h custom property, so nine staggered durations/delays make an ever-changing equalizer. */
```
