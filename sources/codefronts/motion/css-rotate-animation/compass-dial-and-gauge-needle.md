---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/compass-dial-and-gauge-needle/"
title: "Compass Dial and Gauge Needle"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A compass and a speed gauge sharing one mechanism: a needle pivoting at its base, not its centre, which makes transform-origin: 50% 100% the entire trick."
has_js: "true"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compass Dial and Gauge Needle
Source: https://codefronts.com/motion/css-rotate-animation/compass-dial-and-gauge-needle/

A compass and a speed gauge sharing one mechanism: a needle pivoting at its base, not its centre, which makes transform-origin: 50% 100% the entire trick. The angle arrives as a registered <angle> custom property so it interpolates smoothly, and each instrument is a role="meter" carrying its real value.
## HTML
```html
<section class="rot-13" aria-labelledby="rot-13-h">
  <fieldset class="rot-13__theme">
    <legend class="rot-13__themelegend">Theme</legend>
    <input class="rot-13__themeinput" type="radio" name="rot-13-theme" id="rot-13-theme-auto" checked>
    <label class="rot-13__themeopt" for="rot-13-theme-auto">Auto</label>
    <input class="rot-13__themeinput" type="radio" name="rot-13-theme" id="rot-13-theme-light">
    <label class="rot-13__themeopt" for="rot-13-theme-light">Light</label>
    <input class="rot-13__themeinput" type="radio" name="rot-13-theme" id="rot-13-theme-dark">
    <label class="rot-13__themeopt" for="rot-13-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-13__stage" id="rot-13-root">
    <header class="rot-13__head">
      <p class="rot-13__eyebrow">Ranger Instruments · Bench 2</p>
      <h2 class="rot-13__h" id="rot-13-h">The pivot is at the base, not the centre</h2>
      <p class="rot-13__sub">Two instruments, one mechanism. Change the reading and watch the needle sweep — the angle is a registered custom property, so it interpolates.</p>
    </header>

    <div class="rot-13__bench">
      <figure class="rot-13__instrument">
        <div class="rot-13__dial rot-13__dial--compass" role="meter" id="rot-13-compass" aria-label="Heading" aria-valuemin="0" aria-valuemax="359" aria-valuenow="42" aria-valuetext="42 degrees, north east">
          <span class="rot-13__ring" aria-hidden="true"></span>
          <span class="rot-13__rose" aria-hidden="true">
            <span class="rot-13__cardinal rot-13__cardinal--n">N</span>
            <span class="rot-13__cardinal rot-13__cardinal--e">E</span>
            <span class="rot-13__cardinal rot-13__cardinal--s">S</span>
            <span class="rot-13__cardinal rot-13__cardinal--w">W</span>
          </span>
          <span class="rot-13__needle rot-13__needle--compass" aria-hidden="true"></span>
          <span class="rot-13__hub" aria-hidden="true"></span>
        </div>
        <figcaption class="rot-13__cap">
          <output class="rot-13__readout" id="rot-13-compassout">042°</output>
          <span class="rot-13__caplabel">Heading</span>
        </figcaption>
      </figure>

      <figure class="rot-13__instrument">
        <div class="rot-13__dial rot-13__dial--gauge" role="meter" id="rot-13-gauge" aria-label="Ground speed in kilometres per hour" aria-valuemin="0" aria-valuemax="200" aria-valuenow="86">
          <span class="rot-13__arc" aria-hidden="true"></span>
          <span class="rot-13__ticks" aria-hidden="true"></span>
          <span class="rot-13__needle rot-13__needle--gauge" aria-hidden="true"></span>
          <span class="rot-13__hub" aria-hidden="true"></span>
          <span class="rot-13__unit" aria-hidden="true">km/h</span>
        </div>
        <figcaption class="rot-13__cap">
          <output class="rot-13__readout" id="rot-13-gaugeout">86</output>
          <span class="rot-13__caplabel">Ground speed</span>
        </figcaption>
      </figure>
    </div>

    <div class="rot-13__controls">
      <button class="rot-13__btn" type="button" data-rot13="42,18">Docked</button>
      <button class="rot-13__btn" type="button" data-rot13="118,86">Transit</button>
      <button class="rot-13__btn" type="button" data-rot13="284,164">Open water</button>
      <button class="rot-13__btn" type="button" data-rot13="359,206">Over range</button>
    </div>

    <p class="rot-13__fine">The last preset hands the gauge 206 on a 200 scale. The map is clamped, so the needle parks at its end stop instead of wrapping round to point at a number it is not measuring.</p>
  </div>
</section>
```
## CSS
```css
@property --rot-13-heading {
  syntax: "<angle>";
  inherits: true;
  initial-value: 42deg;
}

@property --rot-13-speed {
  syntax: "<angle>";
  inherits: true;
  initial-value: -16.8deg;
}

.rot-13 {
  --page: #efe9dc;
  --face: #f8f4ea;
  --ink: #1d1c18;
  --muted: #6a655a;
  --rule: #cdc5b2;
  --needle: #c22b1f;
  --accent: #1f4f6b;
  --dial: clamp(9rem, 34vw, 13rem);
  --needle-len: 40%;
  --sweep: 240deg;
  --vmax: 200;
  --tick-major: 12;
  --ease-needle: cubic-bezier(0.32, 0.9, 0.24, 1);
  --font-display: Futura, "Century Gothic", "Trebuchet MS", "URW Gothic", sans-serif;
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
  .rot-13 {
    --needle: oklch(0.53 0.19 27);
    --accent: oklch(0.42 0.08 235);
  }
}

.rot-13 *,
.rot-13 *::before,
.rot-13 *::after {
  box-sizing: border-box;
}

.rot-13__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.25rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-13__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-13__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-13__h {
  margin: 0 0 0.6rem;
  font-size: clamp(1.375rem, 4.6vw, 2.125rem);
  font-weight: 500;
  letter-spacing: 0.01em;
  line-height: 1.14;
}

.rot-13__sub {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-13__bench {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
  gap: clamp(1.25rem, 4vw, 2.5rem);
  inline-size: min(100%, 40rem);
  justify-items: center;
}

.rot-13__instrument {
  margin: 0;
  display: grid;
  justify-items: center;
  gap: 0.75rem;
  min-inline-size: 0;
}

.rot-13__dial {
  position: relative;
  inline-size: var(--dial);
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle at 50% 42%, var(--face) 62%, #e6dfd0 100%);
  box-shadow: inset 0 0 0 0.35rem #d9d2c0, inset 0 3px 10px rgba(0, 0, 0, 0.18), 0 2px 0 #ffffff, 0 14px 26px -18px rgba(0, 0, 0, 0.5);
}

.rot-13__ring {
  position: absolute;
  inset: 0.75rem;
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, var(--ink) 0deg 0.7deg, transparent 0.7deg calc(360deg / var(--tick-major)));
  -webkit-mask: radial-gradient(circle, transparent 0 78%, #000 79% 100%);
  mask: radial-gradient(circle, transparent 0 78%, #000 79% 100%);
  opacity: 0.55;
}

.rot-13__rose {
  position: absolute;
  inset: 1.5rem;
}

.rot-13__cardinal {
  position: absolute;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--muted);
}

.rot-13__cardinal--n {
  inset-block-start: 0;
  inset-inline-start: 50%;
  translate: -50% 0;
  color: var(--needle);
}

.rot-13__cardinal--s {
  inset-block-end: 0;
  inset-inline-start: 50%;
  translate: -50% 0;
}

.rot-13__cardinal--e {
  inset-inline-end: 0;
  inset-block-start: 50%;
  translate: 0 -50%;
}

.rot-13__cardinal--w {
  inset-inline-start: 0;
  inset-block-start: 50%;
  translate: 0 -50%;
}

.rot-13__arc {
  position: absolute;
  inset: 0.9rem;
  border-radius: 50%;
  background: conic-gradient(from 180deg, transparent 0deg 30deg, var(--accent) 30deg 200deg, var(--needle) 200deg 270deg, transparent 270deg 360deg);
  -webkit-mask: radial-gradient(circle, transparent 0 80%, #000 81% 100%);
  mask: radial-gradient(circle, transparent 0 80%, #000 81% 100%);
  opacity: 0.85;
}

.rot-13__ticks {
  position: absolute;
  inset: 1.4rem;
  border-radius: 50%;
  background: repeating-conic-gradient(from 210deg, var(--ink) 0deg 0.6deg, transparent 0.6deg 12deg);
  -webkit-mask: radial-gradient(circle, transparent 0 74%, #000 75% 100%);
  mask: radial-gradient(circle, transparent 0 74%, #000 75% 100%);
  opacity: 0.4;
}

.rot-13__needle {
  position: absolute;
  inset-block-start: calc(50% - var(--needle-len));
  inset-inline-start: 50%;
  inline-size: 0.28rem;
  block-size: var(--needle-len);
  translate: -50% 0;
  transform-origin: 50% 100%;
  border-radius: 999px 999px 0.1rem 0.1rem;
  background: linear-gradient(var(--needle), color-mix(in srgb, var(--needle) 70%, #000000));
  transition: transform 900ms var(--ease-needle), rotate 900ms var(--ease-needle);
}

.rot-13__needle--compass {
  transform: rotate(var(--rot-13-heading, 42deg));
}

.rot-13__needle--gauge {
  transform: rotate(var(--rot-13-speed, -16.8deg));
}

.rot-13__hub {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 0.9rem;
  block-size: 0.9rem;
  translate: -50% -50%;
  border-radius: 50%;
  background: var(--ink);
  box-shadow: 0 0 0 0.18rem var(--face);
}

.rot-13__unit {
  position: absolute;
  inset-block-end: 18%;
  inset-inline: 0;
  text-align: center;
  font-size: 0.625rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.rot-13__cap {
  display: grid;
  justify-items: center;
  gap: 0.15rem;
}

.rot-13__readout {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 1.375rem;
  font-weight: 600;
  color: var(--ink);
}

.rot-13__caplabel {
  font-size: 0.6875rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.rot-13__controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
}

.rot-13__btn {
  min-block-size: 2.75rem;
  padding: 0 1rem;
  border: 1px solid var(--rule);
  border-radius: 0.4rem;
  background: var(--face);
  color: var(--ink);
  font-family: var(--font-display);
  font-size: 0.8125rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 2px 0 var(--rule);
}

.rot-13__btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.rot-13__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.rot-13__fine {
  inline-size: min(100%, 36rem);
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .rot-13__needle {
    transition: none;
  }
}

.rot-13__theme {
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

.rot-13__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-13__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-13__themeopt {
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

.rot-13__themeopt:hover {
  opacity: 0.85;
}

.rot-13__themeinput:checked + .rot-13__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-13__themeinput:focus-visible + .rot-13__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-13__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-13__themeinput:checked + .rot-13__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-13:not(:has(#rot-13-theme-light:checked)) {
    --page: #121311;
    --face: #1d1f1c;
    --ink: #efeae0;
    --muted: #9b968a;
    --rule: #32352f;
    --needle: #ff5c48;
    --accent: #66b6d8;
  }

  .rot-13:not(:has(#rot-13-theme-light:checked)) .rot-13__dial {
    background: radial-gradient(circle at 50% 42%, #23261f 62%, #14160f 100%);
    box-shadow: inset 0 0 0 0.35rem #2b2e26, inset 0 3px 10px rgba(0, 0, 0, 0.6), 0 14px 26px -18px rgba(0, 0, 0, 0.9);
  }

  .rot-13:not(:has(#rot-13-theme-light:checked)) .rot-13__btn {
    box-shadow: 0 2px 0 #24261f;
  }
}

@media (prefers-color-scheme: light) {
  .rot-13:has(#rot-13-theme-dark:checked) {
    --page: #121311;
    --face: #1d1f1c;
    --ink: #efeae0;
    --muted: #9b968a;
    --rule: #32352f;
    --needle: #ff5c48;
    --accent: #66b6d8;
  }

  .rot-13:has(#rot-13-theme-dark:checked) .rot-13__dial {
    background: radial-gradient(circle at 50% 42%, #23261f 62%, #14160f 100%);
    box-shadow: inset 0 0 0 0.35rem #2b2e26, inset 0 3px 10px rgba(0, 0, 0, 0.6), 0 14px 26px -18px rgba(0, 0, 0, 0.9);
  }
}

[data-theme="dark"] .rot-13:not(:has(#rot-13-theme-light:checked)) {
  --page: #121311;
  --face: #1d1f1c;
  --ink: #efeae0;
  --muted: #9b968a;
  --rule: #32352f;
  --needle: #ff5c48;
  --accent: #66b6d8;
}

[data-theme="dark"] .rot-13:not(:has(#rot-13-theme-light:checked)) .rot-13__dial {
  background: radial-gradient(circle at 50% 42%, #23261f 62%, #14160f 100%);
  box-shadow: inset 0 0 0 0.35rem #2b2e26, inset 0 3px 10px rgba(0, 0, 0, 0.6), 0 14px 26px -18px rgba(0, 0, 0, 0.9);
}

.rot-13:has(#rot-13-theme-dark:checked) {
  --page: #121311;
  --face: #1d1f1c;
  --ink: #efeae0;
  --muted: #9b968a;
  --rule: #32352f;
  --needle: #ff5c48;
  --accent: #66b6d8;
}

.rot-13:has(#rot-13-theme-dark:checked) .rot-13__dial {
  background: radial-gradient(circle at 50% 42%, #23261f 62%, #14160f 100%);
  box-shadow: inset 0 0 0 0.35rem #2b2e26, inset 0 3px 10px rgba(0, 0, 0, 0.6), 0 14px 26px -18px rgba(0, 0, 0, 0.9);
}

.rot-13:has(#rot-13-theme-dark:checked) .rot-13__btn {
  box-shadow: 0 2px 0 #24261f;
}

.rot-13:has(#rot-13-theme-light:checked) {
  --page: #efe9dc;
  --face: #f8f4ea;
  --ink: #1d1c18;
  --muted: #6a655a;
  --rule: #cdc5b2;
  --needle: #c22b1f;
  --accent: #1f4f6b;
}

.rot-13:has(#rot-13-theme-light:checked) .rot-13__dial {
  background: radial-gradient(circle at 50% 42%, #f8f4ea 62%, #e6dfd0 100%);
  box-shadow: inset 0 0 0 0.35rem #d9d2c0, inset 0 3px 10px rgba(0, 0, 0, 0.18), 0 2px 0 #ffffff, 0 14px 26px -18px rgba(0, 0, 0, 0.5);
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.rot-13__stage');
  if (!root || root.dataset.rot13) return;
  root.dataset.rot13 = '1';
  const compass = root.querySelector('.rot-13__dial--compass');
  const gauge = root.querySelector('.rot-13__dial--gauge');
  const cOut = root.querySelector('#rot-13-compassout');
  const gOut = root.querySelector('#rot-13-gaugeout');
  const VMAX = 200, SWEEP = 240;
  const apply = (heading, speed) => {
    const clamped = Math.min(VMAX, Math.max(0, speed));
    root.style.setProperty('--rot-13-heading', heading + 'deg');
    root.style.setProperty('--rot-13-speed', (clamped / VMAX * SWEEP - SWEEP / 2).toFixed(2) + 'deg');
    compass.setAttribute('aria-valuenow', String(heading));
    compass.setAttribute('aria-valuetext', heading + ' degrees');
    gauge.setAttribute('aria-valuenow', String(clamped));
    cOut.textContent = String(heading).padStart(3, '0') + '°';
    gOut.textContent = speed > VMAX ? clamped + ' (clamped)' : String(clamped);
  };
  root.querySelectorAll('[data-rot13]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const [h, s] = btn.dataset.rot13.split(',').map(Number);
      apply(h, s);
    });
  });
  apply(42, 18);
})();
```
