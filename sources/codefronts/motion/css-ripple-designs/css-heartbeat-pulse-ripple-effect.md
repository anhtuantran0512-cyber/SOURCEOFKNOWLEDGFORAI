---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-heartbeat-pulse-ripple-effect/"
title: "Heartbeat Pulse Ripple"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "A heartbeat is not an even throb, it is lub-dub: two beats close together, then a longer gap."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Heartbeat Pulse Ripple
Source: https://codefronts.com/motion/css-ripple-designs/css-heartbeat-pulse-ripple-effect/

A heartbeat is not an even throb, it is lub-dub: two beats close together, then a longer gap. That asymmetry lives entirely in the keyframe percentages. Rings leave the sensor point in the same two-beat envelope, laid over a clinical trace panel where the beat interval is stated in numbers as well as motion.
## HTML
```html
<section class="rpl-15" aria-labelledby="rpl-15-title">
  <input class="rpl-15__theme-input" type="checkbox" id="rpl-15-theme">
  <label class="rpl-15__theme" for="rpl-15-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-15__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-15__card">
    <header class="rpl-15__top">
      <p class="rpl-15__eyebrow">Continuous monitor</p>
      <h1 class="rpl-15__h1" id="rpl-15-title">Resting heart rate</h1>
    </header>
    <div class="rpl-15__read">
      <div class="rpl-15__pulse" aria-hidden="true">
        <span class="rpl-15__beat"></span>
        <span class="rpl-15__beat rpl-15__beat--two"></span>
        <span class="rpl-15__heart"></span>
      </div>
      <div class="rpl-15__figure">
        <span class="rpl-15__bpm">58</span>
        <span class="rpl-15__unit">bpm</span>
        <span class="rpl-15__delta">4 below your 7-day average</span>
      </div>
    </div>
    <div class="rpl-15__trace" aria-hidden="true">
      <svg viewBox="0 0 320 60" preserveAspectRatio="none"><path d="M0 42h34l7-6 6 18 8-38 7 26h30l7-6 6 18 8-38 7 26h30l7-6 6 18 8-38 7 26h30l7-6 6 18 8-38 7 26h44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
    </div>
    <div class="rpl-15__grid">
      <div class="rpl-15__cell"><span class="rpl-15__cn">41</span><span class="rpl-15__cl">ms HRV</span></div>
      <div class="rpl-15__cell"><span class="rpl-15__cn">96%</span><span class="rpl-15__cl">SpO₂</span></div>
      <div class="rpl-15__cell"><span class="rpl-15__cn">7h 12m</span><span class="rpl-15__cl">sleep</span></div>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-15 {
  --rpl-15-bg: #fbf7f5;
  --rpl-15-bg: oklch(0.978 0.006 30);
  --rpl-15-card: #ffffff;
  --rpl-15-card: oklch(1 0 0);
  --rpl-15-line: #ece3e0;
  --rpl-15-line: oklch(0.918 0.010 30);
  --rpl-15-fg: #1b1414;
  --rpl-15-fg: oklch(0.22 0.014 25);
  --rpl-15-muted: #665a5a;
  --rpl-15-muted: oklch(0.505 0.016 25);
  --rpl-15-accent: #c92841;
  --rpl-15-accent: oklch(0.54 0.20 20);
  --rpl-15-cycle: 1.4s;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-15-bg);
  color: var(--rpl-15-fg);
  font-family: "Helvetica Neue", -apple-system, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-15 *,
.rpl-15 *::before,
.rpl-15 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-15:not(:has(#rpl-15-theme:checked)) {
    --rpl-15-bg: #120e0e;
    --rpl-15-bg: oklch(0.185 0.010 25);
    --rpl-15-card: #1c1616;
    --rpl-15-card: oklch(0.24 0.012 25);
    --rpl-15-line: #2e2626;
    --rpl-15-line: oklch(0.315 0.012 25);
    --rpl-15-fg: #f7f0ef;
    --rpl-15-fg: oklch(0.965 0.008 30);
    --rpl-15-muted: #a4938f;
    --rpl-15-muted: oklch(0.725 0.016 30);
    --rpl-15-accent: #ff6b7d;
    --rpl-15-accent: oklch(0.74 0.16 18);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-15:has(#rpl-15-theme:checked) {
    --rpl-15-bg: #120e0e;
    --rpl-15-bg: oklch(0.185 0.010 25);
    --rpl-15-card: #1c1616;
    --rpl-15-card: oklch(0.24 0.012 25);
    --rpl-15-line: #2e2626;
    --rpl-15-line: oklch(0.315 0.012 25);
    --rpl-15-fg: #f7f0ef;
    --rpl-15-fg: oklch(0.965 0.008 30);
    --rpl-15-muted: #a4938f;
    --rpl-15-muted: oklch(0.725 0.016 30);
    --rpl-15-accent: #ff6b7d;
    --rpl-15-accent: oklch(0.74 0.16 18);
  }
}

.rpl-15__card {
  inline-size: 100%;
  max-inline-size: 460px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding: clamp(24px, 4vw, 34px);
  border: 1px solid var(--rpl-15-line);
  border-radius: 28px;
  background: var(--rpl-15-card);
}

.rpl-15__top {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.rpl-15__eyebrow {
  margin: 0;
  font-size: 10.5px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--rpl-15-accent);
  font-weight: 600;
}

.rpl-15__h1 {
  margin: 0;
  font-size: clamp(21px, 3.2vw, 26px);
  font-weight: 600;
  letter-spacing: -0.022em;
}

.rpl-15__read {
  display: flex;
  align-items: center;
  gap: clamp(18px, 4vw, 30px);
}

.rpl-15__pulse {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 104px;
  block-size: 104px;
  flex: none;
}

.rpl-15__heart {
  inline-size: 34%;
  aspect-ratio: 1;
  rotate: -45deg;
  background: var(--rpl-15-accent);
}

.rpl-15__heart::before,
.rpl-15__heart::after {
  content: "";
  position: absolute;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  background: var(--rpl-15-accent);
}

.rpl-15__heart::before {
  inset-block-start: -50%;
  inset-inline-start: 0;
}

.rpl-15__heart::after {
  inset-block-start: 0;
  inset-inline-start: 50%;
}
/* lub-dub: two rings from one cycle, the second fired at 26% with a shorter reach */

.rpl-15__beat {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 104px;
  aspect-ratio: 1;
  border: 2px solid var(--rpl-15-accent);
  border-radius: 50%;
  animation: rpl-15-lub var(--rpl-15-cycle) cubic-bezier(0.12, 0.7, 0.3, 1) infinite;
}

.rpl-15__beat--two {
  animation-name: rpl-15-dub;
}

@keyframes rpl-15-lub {
  0% {
    transform: translate(-50%, -50%) scale(0.24);
    opacity: 0.7;
  }

  70% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }

  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

@keyframes rpl-15-dub {
  0%,
    24% {
    transform: translate(-50%, -50%) scale(0.24);
    opacity: 0;
  }

  26% {
    transform: translate(-50%, -50%) scale(0.24);
    opacity: 0.45;
  }

  80% {
    transform: translate(-50%, -50%) scale(0.78);
    opacity: 0;
  }

  100% {
    transform: translate(-50%, -50%) scale(0.78);
    opacity: 0;
  }
}

.rpl-15__figure {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px;
  min-inline-size: 0;
}

.rpl-15__bpm {
  font-size: clamp(52px, 11vw, 74px);
  font-weight: 300;
  letter-spacing: -0.05em;
  line-height: 0.9;
  font-variant-numeric: tabular-nums;
}

.rpl-15__unit {
  font-size: 15px;
  color: var(--rpl-15-muted);
}

.rpl-15__delta {
  inline-size: 100%;
  font-size: 12.5px;
  color: var(--rpl-15-muted);
}

.rpl-15__trace {
  color: var(--rpl-15-accent);
  opacity: 0.55;
}

.rpl-15__trace svg {
  inline-size: 100%;
  block-size: 56px;
  display: block;
}

.rpl-15__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.rpl-15__cell {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 14px;
  border: 1px solid var(--rpl-15-line);
  border-radius: 16px;
}

.rpl-15__cn {
  font-size: 17px;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
}

.rpl-15__cl {
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--rpl-15-muted);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-15__beat,
    .rpl-15__beat--two {
    animation: none;
    opacity: 0.2;
    transform: translate(-50%, -50%) scale(0.55);
  }
}

.rpl-15 {
  position: relative;
}

.rpl-15__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-15__theme {
  position: absolute;
  z-index: 60;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
}

.rpl-15__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-15__theme:active {
  transform: scale(0.94);
}

.rpl-15__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-15__theme-input:checked + .rpl-15__theme svg {
  transform: rotate(180deg);
}

.rpl-15__theme-input:focus-visible + .rpl-15__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-15__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-15__theme,
    .rpl-15__theme svg {
    transition: none;
  }
}
```
