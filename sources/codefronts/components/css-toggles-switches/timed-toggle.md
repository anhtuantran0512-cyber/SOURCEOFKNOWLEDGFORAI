---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/timed-toggle/"
title: "Timed Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "An SVG arc fills around a circle when the toggle activates, visualising session time."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Timed Toggle
Source: https://codefronts.com/components/css-toggles-switches/timed-toggle/

An SVG arc fills around a circle when the toggle activates, visualising session time. Temporal UI for progress-aware states — users see state over time, not just on/off. The ember glow signals an active countdown.
## HTML
```html
<label class="tgl-30">
  <input class="tgl-30__input" type="checkbox" checked>
  <span class="tgl-30__body" aria-hidden="true">
    <span class="tgl-30__arc">
      <svg viewBox="0 0 28 28">
        <circle class="tgl-30__bg" cx="14" cy="14" r="11"/>
        <circle class="tgl-30__prog" cx="14" cy="14" r="11"/>
      </svg>
      <span class="tgl-30__dot"></span>
    </span>
    <span class="tgl-30__text">15 min · active</span>
  </span>
</label>
```
## CSS
```css
.tgl-30 {
  --tgl-30-rim: #14141e;
  --tgl-30-wire: #1e1e2e;
  --tgl-30-fog: #3a3a52;
  --tgl-30-ash: #7a7a98;
  --tgl-30-ember: #ff6b35;
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

.tgl-30__input {
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

.tgl-30__body {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  padding: 10px 16px;
  border-radius: 100px;
  background: var(--tgl-30-rim);
  border: 1px solid var(--tgl-30-wire);
  transition: border-color 0.3s ease, background 0.3s ease;
}

.tgl-30__arc {
  position: relative;
  width: 32px;
  height: 32px;
  flex-shrink: 0;
}

.tgl-30__arc svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.tgl-30__bg {
  fill: none;
  stroke: var(--tgl-30-wire);
  stroke-width: 3;
}
/* circumference at r=11 is 2*pi*11 ~= 69. We use 82 as the dasharray
   so the fill animates from "empty" (offset 82) to "nearly full" (offset
   20) — leaving a small gap signals it's still counting down, not done. */

.tgl-30__prog {
  fill: none;
  stroke: var(--tgl-30-ember);
  stroke-width: 3;
  stroke-linecap: round;
  stroke-dasharray: 82;
  stroke-dashoffset: 82;
  transition: stroke-dashoffset 0.4s ease;
}

.tgl-30__dot {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 8px;
  height: 8px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  background: var(--tgl-30-fog);
  transition: background 0.3s ease, box-shadow 0.3s ease;
}

.tgl-30__text {
  font-size: 13px;
  letter-spacing: 0.04em;
  color: var(--tgl-30-ash);
  transition: color 0.3s ease;
}

.tgl-30__input:checked ~ .tgl-30__body {
  border-color: rgba(255,107,53,0.4);
  background: rgba(255,107,53,0.05);
}

.tgl-30__input:checked ~ .tgl-30__body .tgl-30__prog {
  stroke-dashoffset: 20;
}

.tgl-30__input:checked ~ .tgl-30__body .tgl-30__dot {
  background: var(--tgl-30-ember);
  box-shadow: 0 0 6px var(--tgl-30-ember);
}

.tgl-30__input:checked ~ .tgl-30__body .tgl-30__text {
  color: var(--tgl-30-ember);
}

.tgl-30__input:focus-visible ~ .tgl-30__body {
  outline: 2px solid var(--tgl-30-ember);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-30__body,
    .tgl-30__prog,
    .tgl-30__dot,
    .tgl-30__text {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an SVG stroke-dashoffset transition sweeps the ember arc from empty (82) to nearly-full (20) on :checked. */
```
