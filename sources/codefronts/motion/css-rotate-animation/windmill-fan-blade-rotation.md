---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/windmill-fan-blade-rotation/"
title: "Windmill Fan Blade Rotation"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "Five blades built from one repeated element, each rotated to its own position around a shared origin, with the whole assembly turning as a single unit."
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Windmill Fan Blade Rotation
Source: https://codefronts.com/motion/css-rotate-animation/windmill-fan-blade-rotation/

Five blades built from one repeated element, each rotated to its own position around a shared origin, with the whole assembly turning as a single unit. It also tells the truth about speed: past a certain rate a bladed rotor reads as standing still or turning backwards, exactly as it does on camera, so the fix is to slow it or blur it rather than fight it.
## HTML
```html
<section class="rot-14" aria-labelledby="rot-14-h">
  <fieldset class="rot-14__theme">
    <legend class="rot-14__themelegend">Theme</legend>
    <input class="rot-14__themeinput" type="radio" name="rot-14-theme" id="rot-14-theme-auto" checked>
    <label class="rot-14__themeopt" for="rot-14-theme-auto">Auto</label>
    <input class="rot-14__themeinput" type="radio" name="rot-14-theme" id="rot-14-theme-light">
    <label class="rot-14__themeopt" for="rot-14-theme-light">Light</label>
    <input class="rot-14__themeinput" type="radio" name="rot-14-theme" id="rot-14-theme-dark">
    <label class="rot-14__themeopt" for="rot-14-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-14__pause">
    <input class="rot-14__pausebox" type="checkbox" id="rot-14-pause">
    <span class="rot-14__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-14__pausetext">Pause</span>
  </label>

  <div class="rot-14__stage">
    <header class="rot-14__head">
      <p class="rot-14__eyebrow">Fern Land &amp; Water · Pump house</p>
      <h2 class="rot-14__h" id="rot-14-h">Five blades, one origin, one moving part</h2>
      <p class="rot-14__sub">Each blade is the same element rotated by its index times 72 degrees. Only the hub animates, so the spacing can never drift.</p>
    </header>

    <div class="rot-14__tower">
      <div class="rot-14__rotor rot-14__rotor--main" aria-hidden="true">
        <span class="rot-14__blade" style="--n: 0"></span>
        <span class="rot-14__blade" style="--n: 1"></span>
        <span class="rot-14__blade" style="--n: 2"></span>
        <span class="rot-14__blade" style="--n: 3"></span>
        <span class="rot-14__blade" style="--n: 4"></span>
        <span class="rot-14__cap"></span>
      </div>
      <span class="rot-14__mast" aria-hidden="true"></span>
      <span class="rot-14__base" aria-hidden="true"></span>
    </div>

    <div class="rot-14__samples">
      <article class="rot-14__sample">
        <div class="rot-14__mini rot-14__rotor rot-14__rotor--slow" aria-hidden="true">
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 0"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 1"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 2"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 3"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 4"></span>
          <span class="rot-14__cap"></span>
        </div>
        <p class="rot-14__samplelabel">3.6s per turn</p>
        <p class="rot-14__samplenote">Every blade is individually trackable. This is the speed a viewer reads as turning.</p>
      </article>
      <article class="rot-14__sample">
        <div class="rot-14__mini rot-14__rotor rot-14__rotor--strobe" aria-hidden="true">
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 0"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 1"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 2"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 3"></span>
          <span class="rot-14__blade rot-14__blade--sm" style="--n: 4"></span>
          <span class="rot-14__cap"></span>
        </div>
        <p class="rot-14__samplelabel">0.28s per turn</p>
        <p class="rot-14__samplenote">Near the strobe threshold. Each blade lands close to where the last one was, so the rotor can read as frozen or reversed.</p>
      </article>
      <article class="rot-14__sample">
        <div class="rot-14__mini rot-14__disc" aria-hidden="true"></div>
        <p class="rot-14__samplelabel">Blurred rotor</p>
        <p class="rot-14__samplenote">The honest answer at high speed: stop drawing individual blades and draw the disc they sweep.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.rot-14 {
  --page: #eef1e8;
  --surface: #fbfcf8;
  --ink: #1b241c;
  --muted: #5c6a5d;
  --rule: #c9d4c6;
  --accent: #3f7d5c;
  --blade-fill: #dfe7da;
  --blades: 5;
  --blade-len: 42%;
  --blade-w: 13%;
  --blade-skew: -8deg;
  --rotor-dur: 5.2s;
  --font-display: Optima, "Gill Sans", "Gill Sans MT", Candara, system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-14 {
    --accent: oklch(0.52 0.1 155);
  }
}

.rot-14 *,
.rot-14 *::before,
.rot-14 *::after {
  box-sizing: border-box;
}

.rot-14__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.5rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-14__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-14__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-14__h {
  margin: 0 0 0.6rem;
  font-size: clamp(1.5rem, 5vw, 2.375rem);
  font-weight: 500;
  line-height: 1.12;
}

.rot-14__sub {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-14__tower {
  position: relative;
  inline-size: min(100%, 22rem);
  aspect-ratio: 4 / 5;
  display: grid;
  place-items: start center;
}

.rot-14__rotor {
  position: relative;
  inline-size: clamp(10rem, 40vw, 15rem);
  aspect-ratio: 1;
  animation: rot-14-rotor var(--rotor-dur) linear infinite;
}

.rot-14__rotor--main {
  z-index: 2;
}

.rot-14__blade {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: var(--blade-w);
  block-size: var(--blade-len);
  transform-origin: 50% 0;
  transform: translate(-50%, 0) rotate(calc(var(--n) * (360deg / var(--blades)))) skewX(var(--blade-skew));
  border-radius: 0 0 999px 999px;
  background: linear-gradient(var(--blade-fill), color-mix(in srgb, var(--blade-fill) 70%, var(--accent)));
  border: 1px solid var(--rule);
  box-shadow: 3px 3px 0 0 color-mix(in srgb, var(--ink) 14%, transparent);
}

.rot-14__blade--sm {
  inline-size: 16%;
}

.rot-14__cap {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 18%;
  aspect-ratio: 1;
  translate: -50% -50%;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 2px 2px 0 0 color-mix(in srgb, var(--ink) 30%, transparent);
}

@keyframes rot-14-rotor {
  to {
    transform: rotate(360deg);
  }
}

.rot-14__mast {
  position: absolute;
  inset-block-start: 46%;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: 8%;
  block-size: 54%;
  background: linear-gradient(90deg, var(--surface), var(--rule));
  border: 1px solid var(--rule);
  border-block-end: 0;
}

.rot-14__base {
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: 34%;
  block-size: 4%;
  background: var(--ink);
  border-radius: 0.2rem;
}

.rot-14__samples {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
  gap: clamp(0.75rem, 3vw, 1.5rem);
  inline-size: min(100%, 46rem);
}

.rot-14__sample {
  min-inline-size: 0;
  display: grid;
  justify-items: center;
  gap: 0.4rem;
  padding: 1rem 0.75rem;
  border: 1px solid var(--rule);
  background: var(--surface);
  box-shadow: 5px 5px 0 0 color-mix(in srgb, var(--ink) 10%, transparent);
}

.rot-14__mini {
  inline-size: clamp(4.5rem, 16vw, 6rem);
  aspect-ratio: 1;
}

.rot-14__rotor--slow {
  animation-duration: 3.6s;
}

.rot-14__rotor--strobe {
  animation-duration: 0.28s;
}

.rot-14__disc {
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, color-mix(in srgb, var(--accent) 30%, transparent) 0deg 3deg, transparent 3deg 6deg);
  box-shadow: inset 0 0 0 1px var(--rule);
  filter: blur(1.5px);
}

.rot-14__samplelabel {
  margin: 0.35rem 0 0;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.8125rem;
  color: var(--accent);
}

.rot-14__samplenote {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.75rem;
  line-height: 1.5;
  text-align: center;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .rot-14__rotor {
    animation: none;
    transform: rotate(14deg);
  }
}

.rot-14:has(.rot-14__pausebox:checked) .rot-14__rotor {
  animation-play-state: paused;
}

.rot-14__theme {
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

.rot-14__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-14__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-14__themeopt {
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

.rot-14__themeopt:hover {
  opacity: 0.85;
}

.rot-14__themeinput:checked + .rot-14__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-14__themeinput:focus-visible + .rot-14__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-14__pause {
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
  font-family: system-ui, sans-serif;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  user-select: none;
}

.rot-14__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-14__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-14__pause:has(.rot-14__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-14:has(.rot-14__pausebox:checked) .rot-14__pausedot {
  background: var(--accent);
  color: var(--surface);
}

@media (forced-colors: active) {
  .rot-14__theme,
    .rot-14__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-14__themeinput:checked + .rot-14__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-14:not(:has(#rot-14-theme-light:checked)) {
    --page: #0f1410;
    --surface: #161d17;
    --ink: #e8efe6;
    --muted: #94a494;
    --rule: #263026;
    --accent: #6fc396;
    --blade-fill: #232d24;
  }
}

@media (prefers-color-scheme: light) {
  .rot-14:has(#rot-14-theme-dark:checked) {
    --page: #0f1410;
    --surface: #161d17;
    --ink: #e8efe6;
    --muted: #94a494;
    --rule: #263026;
    --accent: #6fc396;
    --blade-fill: #232d24;
  }
}

[data-theme="dark"] .rot-14:not(:has(#rot-14-theme-light:checked)) {
  --page: #0f1410;
  --surface: #161d17;
  --ink: #e8efe6;
  --muted: #94a494;
  --rule: #263026;
  --accent: #6fc396;
  --blade-fill: #232d24;
}

.rot-14:has(#rot-14-theme-dark:checked) {
  --page: #0f1410;
  --surface: #161d17;
  --ink: #e8efe6;
  --muted: #94a494;
  --rule: #263026;
  --accent: #6fc396;
  --blade-fill: #232d24;
}

.rot-14:has(#rot-14-theme-light:checked) {
  --page: #eef1e8;
  --surface: #fbfcf8;
  --ink: #1b241c;
  --muted: #5c6a5d;
  --rule: #c9d4c6;
  --accent: #3f7d5c;
  --blade-fill: #dfe7da;
}
```
