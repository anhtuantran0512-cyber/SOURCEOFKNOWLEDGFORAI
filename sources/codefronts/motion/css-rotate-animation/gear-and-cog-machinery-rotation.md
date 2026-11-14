---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/gear-and-cog-machinery-rotation/"
title: "Gear and Cog Machinery Rotation"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A three-gear train where the ratios are real: a 36-tooth wheel drives a 24-tooth and a 12-tooth, so their durations are 12s, 8s and 4s and every second gear…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gear and Cog Machinery Rotation
Source: https://codefronts.com/motion/css-rotate-animation/gear-and-cog-machinery-rotation/

A three-gear train where the ratios are real: a 36-tooth wheel drives a 24-tooth and a 12-tooth, so their durations are 12s, 8s and 4s and every second gear turns the other way. Getting the inverse-proportion right is the difference between a convincing mechanism and three unrelated circles spinning at whatever speed looked nice.
## HTML
```html
<section class="rot-11" aria-labelledby="rot-11-h">
  <fieldset class="rot-11__theme">
    <legend class="rot-11__themelegend">Theme</legend>
    <input class="rot-11__themeinput" type="radio" name="rot-11-theme" id="rot-11-theme-auto" checked>
    <label class="rot-11__themeopt" for="rot-11-theme-auto">Auto</label>
    <input class="rot-11__themeinput" type="radio" name="rot-11-theme" id="rot-11-theme-light">
    <label class="rot-11__themeopt" for="rot-11-theme-light">Light</label>
    <input class="rot-11__themeinput" type="radio" name="rot-11-theme" id="rot-11-theme-dark">
    <label class="rot-11__themeopt" for="rot-11-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-11__pause">
    <input class="rot-11__pausebox" type="checkbox" id="rot-11-pause">
    <span class="rot-11__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-11__pausetext">Pause</span>
  </label>

  <div class="rot-11__stage">
    <header class="rot-11__head">
      <p class="rot-11__eyebrow">Basalt Works · Drive assembly</p>
      <h2 class="rot-11__h" id="rot-11-h">Three gears, one ratio rule</h2>
      <p class="rot-11__sub">36 teeth at 12 seconds drives 24 teeth at 8 and 12 teeth at 4. Every second wheel runs in reverse, because meshed gears have no other option.</p>
    </header>

    <div class="rot-11__train" aria-hidden="true">
      <div class="rot-11__gear rot-11__gear--a" style="--t: 36; --dur: 12s">
        <span class="rot-11__rim"></span>
        <span class="rot-11__hub"></span>
        <span class="rot-11__spoke"></span>
      </div>
      <div class="rot-11__gear rot-11__gear--b" style="--t: 24; --dur: 8s">
        <span class="rot-11__rim"></span>
        <span class="rot-11__hub"></span>
        <span class="rot-11__spoke"></span>
      </div>
      <div class="rot-11__gear rot-11__gear--c" style="--t: 12; --dur: 4s">
        <span class="rot-11__rim"></span>
        <span class="rot-11__hub"></span>
        <span class="rot-11__spoke"></span>
      </div>
    </div>

    <div class="rot-11__tablewrap">
    <table class="rot-11__table">
      <caption class="rot-11__caption">Drive train, as specified</caption>
      <thead>
        <tr><th scope="col">Wheel</th><th scope="col">Teeth</th><th scope="col">Per turn</th><th scope="col">Direction</th></tr>
      </thead>
      <tbody>
        <tr><th scope="row">Driver</th><td>36</td><td>12.0s</td><td>Clockwise</td></tr>
        <tr><th scope="row">Idler</th><td>24</td><td>8.0s</td><td>Anticlockwise</td></tr>
        <tr><th scope="row">Output</th><td>12</td><td>4.0s</td><td>Clockwise</td></tr>
      </tbody>
    </table>
    </div>

    <p class="rot-11__fine">Duration equals the reference duration times this wheel's tooth count over the reference tooth count. Choose speeds by eye instead and the teeth visibly slip past each other.</p>
  </div>
</section>
```
## CSS
```css
.rot-11 {
  --page: #d9dcdf;
  --surface: #eceef0;
  --steel-1: #f4f6f7;
  --steel-2: #b9bfc5;
  --steel-3: #7d858d;
  --ink: #14181c;
  --muted: #4e565f;
  --rule: #b2b8be;
  --accent: #e2560f;
  --ref: 1;
  --tooth-depth: 14%;
  --font-display: "Arial Black", "Arial Bold", Impact, system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-11 {
    --accent: oklch(0.63 0.2 42);
  }
}

.rot-11 *,
.rot-11 *::before,
.rot-11 *::after {
  box-sizing: border-box;
}

.rot-11__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.25rem, 3.5vw, 2.25rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-11__head {
  max-inline-size: 38rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-11__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-11__h {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 4.6vw, 2.25rem);
  font-weight: 900;
  letter-spacing: -0.02em;
  line-height: 1.1;
  text-transform: uppercase;
}

.rot-11__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-11__train {
  position: relative;
  inline-size: min(100%, 30rem);
  block-size: clamp(13rem, 46vw, 18rem);
}

.rot-11__gear {
  position: absolute;
  border-radius: 50%;
  animation: rot-11-mesh var(--dur, 8s) linear infinite;
}

.rot-11__gear--a {
  inline-size: clamp(9rem, 32vw, 13rem);
  aspect-ratio: 1;
  inset-block-start: 8%;
  inset-inline-start: 2%;
}

.rot-11__gear--b {
  inline-size: clamp(6rem, 21vw, 8.7rem);
  aspect-ratio: 1;
  inset-block-start: 44%;
  inset-inline-start: calc(2% + clamp(8.1rem, 29vw, 11.7rem));
  animation-direction: reverse;
}

.rot-11__gear--c {
  inline-size: clamp(3rem, 10.5vw, 4.35rem);
  aspect-ratio: 1;
  inset-block-start: 22%;
  inset-inline-start: calc(2% + clamp(10.8rem, 40vw, 15.9rem));
}

.rot-11__rim {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--steel-2);
}

@supports (background: conic-gradient(#000, #fff)) {
  .rot-11__rim {
    background: repeating-conic-gradient(from 0deg, var(--steel-1) 0deg calc(180deg / var(--t)), var(--steel-3) calc(180deg / var(--t)) calc(360deg / var(--t)));
  }
}

.rot-11__rim::after {
  content: "";
  position: absolute;
  inset: var(--tooth-depth);
  border-radius: 50%;
  background: radial-gradient(circle at 34% 28%, var(--steel-1), var(--steel-2) 62%, var(--steel-3) 100%);
  box-shadow: inset 0 2px 3px rgba(255, 255, 255, 0.75), inset 0 -3px 6px rgba(0, 0, 0, 0.35);
}

.rot-11__hub {
  position: absolute;
  inset: 38%;
  border-radius: 50%;
  background: var(--steel-3);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.55), 0 1px 0 rgba(255, 255, 255, 0.6);
}

.rot-11__spoke {
  position: absolute;
  inset-block-start: 22%;
  inset-inline-start: 50%;
  inline-size: 8%;
  block-size: 28%;
  translate: -50% 0;
  border-radius: 999px;
  background: var(--accent);
}

.rot-11__gear--b .rot-11__spoke {
  background: var(--steel-1);
}

@keyframes rot-11-mesh {
  to {
    transform: rotate(360deg);
  }
}

.rot-11__tablewrap {
  inline-size: min(100%, 30rem);
  max-inline-size: 100%;
  min-inline-size: 0;
  overflow-x: auto;
}

.rot-11__table {
  inline-size: 100%;
  table-layout: fixed;
  border-collapse: collapse;
  font-size: 0.8125rem;
  background: var(--surface);
  border: 1px solid var(--rule);
}

.rot-11__caption {
  padding-block-end: 0.5rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: start;
}

.rot-11__table th,
.rot-11__table td {
  padding: 0.55rem 0.5rem;
  text-align: start;
  border-block-start: 1px solid var(--rule);
  overflow-wrap: break-word;
}

@media (max-width: 24rem) {
  .rot-11__table {
    font-size: 0.6875rem;
  }

  .rot-11__table th,
    .rot-11__table td {
    padding: 0.45rem 0.3rem;
  }
}

.rot-11__table thead th {
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  border-block-start: 0;
}

.rot-11__table tbody th {
  font-weight: 700;
}

.rot-11__fine {
  inline-size: min(100%, 34rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .rot-11__gear {
    animation: none;
  }

  .rot-11__gear--a {
    transform: rotate(5deg);
  }

  .rot-11__gear--b {
    transform: rotate(-7.5deg);
  }

  .rot-11__gear--c {
    transform: rotate(15deg);
  }
}

.rot-11:has(.rot-11__pausebox:checked) .rot-11__gear {
  animation-play-state: paused;
}

.rot-11__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.rot-11__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-11__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-11__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.rot-11__themeopt:hover {
  opacity: 0.85;
}

.rot-11__themeinput:checked + .rot-11__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-11__themeinput:focus-visible + .rot-11__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-11__pause {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-start: 0.875rem;
  z-index: 9;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin: 0;
  padding: 0.1875rem 0.75rem 0.1875rem 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  user-select: none;
}

.rot-11__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-11__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-11__pause:has(.rot-11__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-11:has(.rot-11__pausebox:checked) .rot-11__pausedot {
  background: var(--accent);
  color: #ffffff;
}

@media (forced-colors: active) {
  .rot-11__theme,
    .rot-11__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-11__themeinput:checked + .rot-11__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-11:not(:has(#rot-11-theme-light:checked)) {
    --page: #14171a;
    --surface: #1c2024;
    --steel-1: #6f777f;
    --steel-2: #4a5057;
    --steel-3: #2b3036;
    --ink: #eceff2;
    --muted: #9aa3ac;
    --rule: #2f353b;
    --accent: #ff7a2f;
  }
}

@media (prefers-color-scheme: light) {
  .rot-11:has(#rot-11-theme-dark:checked) {
    --page: #14171a;
    --surface: #1c2024;
    --steel-1: #6f777f;
    --steel-2: #4a5057;
    --steel-3: #2b3036;
    --ink: #eceff2;
    --muted: #9aa3ac;
    --rule: #2f353b;
    --accent: #ff7a2f;
  }
}

[data-theme="dark"] .rot-11:not(:has(#rot-11-theme-light:checked)) {
  --page: #14171a;
  --surface: #1c2024;
  --steel-1: #6f777f;
  --steel-2: #4a5057;
  --steel-3: #2b3036;
  --ink: #eceff2;
  --muted: #9aa3ac;
  --rule: #2f353b;
  --accent: #ff7a2f;
}

.rot-11:has(#rot-11-theme-dark:checked) {
  --page: #14171a;
  --surface: #1c2024;
  --steel-1: #6f777f;
  --steel-2: #4a5057;
  --steel-3: #2b3036;
  --ink: #eceff2;
  --muted: #9aa3ac;
  --rule: #2f353b;
  --accent: #ff7a2f;
}

.rot-11:has(#rot-11-theme-light:checked) {
  --page: #d9dcdf;
  --surface: #eceef0;
  --steel-1: #f4f6f7;
  --steel-2: #b9bfc5;
  --steel-3: #7d858d;
  --ink: #14181c;
  --muted: #4e565f;
  --rule: #b2b8be;
  --accent: #e2560f;
}
```
