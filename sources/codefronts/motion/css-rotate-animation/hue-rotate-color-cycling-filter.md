---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/hue-rotate-color-cycling-filter/"
title: "Hue Rotate Color Cycling Filter"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "The one place in this collection where rotating does not move anything: filter: hue-rotate() turns colour around the wheel while leaving lightness and…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hue Rotate Color Cycling Filter
Source: https://codefronts.com/motion/css-rotate-animation/hue-rotate-color-cycling-filter/

The one place in this collection where rotating does not move anything: filter: hue-rotate() turns colour around the wheel while leaving lightness and saturation where they were. Two panels cycle the full 360 degrees — a gradient field and a CSS-drawn plate — so you can see why identical source colours drift apart at wildly different rates.
## HTML
```html
<section class="rot-09" aria-labelledby="rot-09-h">
  <fieldset class="rot-09__theme">
    <legend class="rot-09__themelegend">Theme</legend>
    <input class="rot-09__themeinput" type="radio" name="rot-09-theme" id="rot-09-theme-auto" checked>
    <label class="rot-09__themeopt" for="rot-09-theme-auto">Auto</label>
    <input class="rot-09__themeinput" type="radio" name="rot-09-theme" id="rot-09-theme-light">
    <label class="rot-09__themeopt" for="rot-09-theme-light">Light</label>
    <input class="rot-09__themeinput" type="radio" name="rot-09-theme" id="rot-09-theme-dark">
    <label class="rot-09__themeopt" for="rot-09-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-09__pause">
    <input class="rot-09__pausebox" type="checkbox" id="rot-09-pause">
    <span class="rot-09__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-09__pausetext">Pause</span>
  </label>

  <div class="rot-09__stage">
    <header class="rot-09__head">
      <p class="rot-09__eyebrow">Nova Optics · Colour</p>
      <h2 class="rot-09__h" id="rot-09-h">Rotation without movement</h2>
      <p class="rot-09__sub">Both panels below are geometrically still. What rotates is hue — the whole wheel, once every twelve seconds.</p>
    </header>

    <div class="rot-09__pair">
      <figure class="rot-09__panel">
        <div class="rot-09__field rot-09__cycle" aria-hidden="true"></div>
        <figcaption class="rot-09__cap">Saturated gradient field · swings hard through cyan and lime</figcaption>
      </figure>
      <figure class="rot-09__panel">
        <div class="rot-09__plate rot-09__cycle" aria-hidden="true">
          <span class="rot-09__plateband"></span>
          <span class="rot-09__platedot"></span>
        </div>
        <figcaption class="rot-09__cap">Low-saturation plate · barely shifts, same filter</figcaption>
      </figure>
    </div>

    <div class="rot-09__strip">
      <p class="rot-09__striph">Fixed samples, sixty degrees apart</p>
      <div class="rot-09__strips">
        <div class="rot-09__swatch" style="--h: 0deg" aria-hidden="true"><span class="rot-09__swatchval">0</span></div>
        <div class="rot-09__swatch" style="--h: 60deg" aria-hidden="true"><span class="rot-09__swatchval">60</span></div>
        <div class="rot-09__swatch" style="--h: 120deg" aria-hidden="true"><span class="rot-09__swatchval">120</span></div>
        <div class="rot-09__swatch" style="--h: 180deg" aria-hidden="true"><span class="rot-09__swatchval">180</span></div>
        <div class="rot-09__swatch" style="--h: 240deg" aria-hidden="true"><span class="rot-09__swatchval">240</span></div>
        <div class="rot-09__swatch" style="--h: 300deg" aria-hidden="true"><span class="rot-09__swatchval">300</span></div>
      </div>
      <p class="rot-09__stripnote">Equal degree steps, unequal perceptual steps. The filter is a matrix approximation, not a perceptual rotation.</p>
    </div>

    <p class="rot-09__fine">Apply the filter to the leaf, not the wrapper. Any non-<span class="rot-09__code">none</span> filter makes its element a containing block for fixed descendants and flattens any 3D context beneath it.</p>
  </div>
</section>
```
## CSS
```css
.rot-09 {
  --page: #0a0610;
  --surface: #140c1e;
  --ink: #f4ecff;
  --muted: #a291bd;
  --rule: #2a1c3d;
  --accent: #ff4fa3;
  --cycle: 12s;
  --bloom: 0 26px 60px -30px;
  --font-display: "Helvetica Neue", Helvetica, "Nimbus Sans", Arial, sans-serif;
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
  .rot-09 {
    --accent: oklch(0.68 0.24 350);
  }
}

.rot-09 *,
.rot-09 *::before,
.rot-09 *::after {
  box-sizing: border-box;
}

.rot-09__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.5rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-09__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-09__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-09__h {
  margin: 0 0 0.6rem;
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.08;
  text-transform: uppercase;
}

.rot-09__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-09__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.rot-09__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: clamp(1rem, 3vw, 1.75rem);
  inline-size: min(100%, 46rem);
}

.rot-09__panel {
  min-inline-size: 0;
  margin: 0;
  display: grid;
  gap: 0.6rem;
}

.rot-09__field {
  aspect-ratio: 4 / 3;
  border-radius: 1rem;
  background: conic-gradient(from 210deg at 30% 25%, #ff2d78, #ffb03a 25%, #35e2b0 50%, #4f6dff 72%, #ff2d78 100%);
  box-shadow: var(--bloom) color-mix(in srgb, var(--accent) 60%, transparent);
}

.rot-09__plate {
  position: relative;
  aspect-ratio: 4 / 3;
  border-radius: 1rem;
  background: linear-gradient(160deg, #8f9aa8 0%, #6d7684 55%, #4d545e 100%);
  box-shadow: var(--bloom) rgba(0, 0, 0, 0.7);
  overflow: hidden;
}

.rot-09__plateband {
  position: absolute;
  inset-block-start: 58%;
  inset-inline: 0;
  block-size: 18%;
  background: #c46a4a;
}

.rot-09__platedot {
  position: absolute;
  inset-block-start: 18%;
  inset-inline-start: 16%;
  inline-size: 22%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: #e0d3a8;
}

.rot-09__cycle {
  animation: rot-09-hue var(--cycle) linear infinite;
}

@keyframes rot-09-hue {
  from {
    filter: hue-rotate(0deg);
  }

  to {
    filter: hue-rotate(360deg);
  }
}

.rot-09__cap {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.5;
  letter-spacing: 0.02em;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-09__strip {
  inline-size: min(100%, 46rem);
  display: grid;
  gap: 0.6rem;
  padding: 1rem;
  border: 1px solid var(--rule);
  border-radius: 1rem;
  background: var(--surface);
}

.rot-09__striph {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.rot-09__strips {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 0.35rem;
}

.rot-09__swatch {
  position: relative;
  aspect-ratio: 1;
  min-inline-size: 0;
  border-radius: 0.5rem;
  background: conic-gradient(from 210deg at 30% 25%, #ff2d78, #ffb03a 25%, #35e2b0 50%, #4f6dff 72%, #ff2d78 100%);
  filter: hue-rotate(var(--h, 0deg));
}

.rot-09__swatchval {
  position: absolute;
  inset-block-end: 0.25rem;
  inset-inline: 0;
  text-align: center;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.625rem;
  color: rgba(10, 6, 16, 0.85);
}

.rot-09__stripnote {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.55;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-09__fine {
  inline-size: min(100%, 40rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .rot-09__cycle {
    animation: none;
    filter: hue-rotate(215deg);
  }
}

.rot-09:has(.rot-09__pausebox:checked) .rot-09__cycle {
  animation-play-state: paused;
}

.rot-09__theme {
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

.rot-09__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-09__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-09__themeopt {
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

.rot-09__themeopt:hover {
  opacity: 0.85;
}

.rot-09__themeinput:checked + .rot-09__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-09__themeinput:focus-visible + .rot-09__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-09__pause {
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
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  user-select: none;
}

.rot-09__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-09__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-09__pause:has(.rot-09__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-09:has(.rot-09__pausebox:checked) .rot-09__pausedot {
  background: var(--accent);
  color: #180a12;
}

@media (forced-colors: active) {
  .rot-09__theme,
    .rot-09__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-09__themeinput:checked + .rot-09__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-09:not(:has(#rot-09-theme-dark:checked)) {
    --page: #f6f2fa;
    --surface: #ffffff;
    --ink: #190f26;
    --muted: #63527a;
    --rule: #e4dced;
    --accent: #c01f78;
    --bloom: 0 22px 44px -30px;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-09:has(#rot-09-theme-light:checked) {
    --page: #f6f2fa;
    --surface: #ffffff;
    --ink: #190f26;
    --muted: #63527a;
    --rule: #e4dced;
    --accent: #c01f78;
    --bloom: 0 22px 44px -30px;
  }
}

[data-theme="light"] .rot-09:not(:has(#rot-09-theme-dark:checked)) {
  --page: #f6f2fa;
  --surface: #ffffff;
  --ink: #190f26;
  --muted: #63527a;
  --rule: #e4dced;
  --accent: #c01f78;
  --bloom: 0 22px 44px -30px;
}

.rot-09:has(#rot-09-theme-light:checked) {
  --page: #f6f2fa;
  --surface: #ffffff;
  --ink: #190f26;
  --muted: #63527a;
  --rule: #e4dced;
  --accent: #c01f78;
  --bloom: 0 22px 44px -30px;
}

.rot-09:has(#rot-09-theme-light:checked) .rot-09__pausedot {
  color: #ffffff;
}

.rot-09:has(#rot-09-theme-dark:checked) {
  --page: #0a0610;
  --surface: #140c1e;
  --ink: #f4ecff;
  --muted: #a291bd;
  --rule: #2a1c3d;
  --accent: #ff4fa3;
  --bloom: 0 26px 60px -30px;
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-09:not(:has(#rot-09-theme-light:checked)) {
  --page: #0a0610;
  --surface: #140c1e;
  --ink: #f4ecff;
  --muted: #a291bd;
  --rule: #2a1c3d;
  --accent: #ff4fa3;
  --bloom: 0 26px 60px -30px;
}
```
