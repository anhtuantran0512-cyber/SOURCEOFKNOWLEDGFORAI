---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/continuous-spin-loading-indicator/"
title: "Continuous Spin Loading Indicator"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A timing bench rather than a loading indicator: the same rotating mark shown at four durations — 0.6s, 1.2s, 2.4s and 4.8s — with a linear and an eased pair…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Continuous Spin Loading Indicator
Source: https://codefronts.com/motion/css-rotate-animation/continuous-spin-loading-indicator/

A timing bench rather than a loading indicator: the same rotating mark shown at four durations — 0.6s, 1.2s, 2.4s and 4.8s — with a linear and an eased pair underneath. Seeing them side by side is the only reliable way to pick a speed, because duration changes what a rotation means: urgent, working, ambient or idle.
## HTML
```html
<section class="rot-05" aria-labelledby="rot-05-h">
  <fieldset class="rot-05__theme">
    <legend class="rot-05__themelegend">Theme</legend>
    <input class="rot-05__themeinput" type="radio" name="rot-05-theme" id="rot-05-theme-auto" checked>
    <label class="rot-05__themeopt" for="rot-05-theme-auto">Auto</label>
    <input class="rot-05__themeinput" type="radio" name="rot-05-theme" id="rot-05-theme-light">
    <label class="rot-05__themeopt" for="rot-05-theme-light">Light</label>
    <input class="rot-05__themeinput" type="radio" name="rot-05-theme" id="rot-05-theme-dark">
    <label class="rot-05__themeopt" for="rot-05-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-05__pause">
    <input class="rot-05__pausebox" type="checkbox" id="rot-05-pause">
    <span class="rot-05__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-05__pausetext">Pause</span>
  </label>

  <div class="rot-05__stage">
    <header class="rot-05__head">
      <p class="rot-05__eyebrow">Timing bench</p>
      <h2 class="rot-05__h" id="rot-05-h">Same rotation. Four speeds. Four meanings.</h2>
      <p class="rot-05__sub">One keyframe drives every mark below. Only <span class="rot-05__code">animation-duration</span> changes — and with it, what the motion says.</p>
    </header>

    <div class="rot-05__row">
      <article class="rot-05__col" style="--d: 0.6s">
        <div class="rot-05__well"><span class="rot-05__mark rot-05__spin" aria-hidden="true"></span></div>
        <p class="rot-05__dur">0.6s</p>
        <p class="rot-05__read">Urgent</p>
      </article>
      <article class="rot-05__col" style="--d: 1.2s">
        <div class="rot-05__well"><span class="rot-05__mark rot-05__spin" aria-hidden="true"></span></div>
        <p class="rot-05__dur">1.2s</p>
        <p class="rot-05__read">Working</p>
      </article>
      <article class="rot-05__col" style="--d: 2.4s">
        <div class="rot-05__well"><span class="rot-05__mark rot-05__spin" aria-hidden="true"></span></div>
        <p class="rot-05__dur">2.4s</p>
        <p class="rot-05__read">Ambient</p>
      </article>
      <article class="rot-05__col" style="--d: 4.8s">
        <div class="rot-05__well"><span class="rot-05__mark rot-05__spin" aria-hidden="true"></span></div>
        <p class="rot-05__dur">4.8s</p>
        <p class="rot-05__read">Idle</p>
      </article>
    </div>

    <div class="rot-05__curves">
      <p class="rot-05__curvesh">Now hold the duration at 1.6s and change only the curve</p>
      <div class="rot-05__curverow">
        <article class="rot-05__curve">
          <div class="rot-05__well rot-05__well--sm"><span class="rot-05__mark rot-05__spin rot-05__spin--linear" aria-hidden="true"></span></div>
          <p class="rot-05__curvelabel">linear</p>
          <p class="rot-05__curvenote">Constant velocity. What a rotating object actually does.</p>
        </article>
        <article class="rot-05__curve">
          <div class="rot-05__well rot-05__well--sm"><span class="rot-05__mark rot-05__spin rot-05__spin--eased" aria-hidden="true"></span></div>
          <p class="rot-05__curvelabel">ease-in-out</p>
          <p class="rot-05__curvenote">Stalls at every cycle boundary. A pulse, not a spin.</p>
        </article>
        <article class="rot-05__curve">
          <div class="rot-05__well rot-05__well--sm"><span class="rot-05__mark rot-05__spin rot-05__spin--stepped" aria-hidden="true"></span></div>
          <p class="rot-05__curvelabel">steps(8)</p>
          <p class="rot-05__curvenote">Eight discrete positions. A mechanical detent.</p>
        </article>
      </div>
    </div>

    <p class="rot-05__fine">Not a loading indicator. A real one needs a status role, a delay before it appears and a determinate replacement once progress is known — this is a bench for choosing how fast a thing should turn.</p>
  </div>
</section>
```
## CSS
```css
.rot-05 {
  --page: #000000;
  --surface: #0a0c0a;
  --ink: #f2f7f2;
  --muted: #8a968c;
  --rule: #1a1f1b;
  --accent: #9dff4f;
  --glow: 0 0 18px;
  --mark-w: 0.375rem;
  --mark-h: 44%;
  --font-display: "Avenir Next", "Segoe UI", ui-rounded, "Nunito", system-ui, sans-serif;
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
  .rot-05 {
    --accent: oklch(0.88 0.22 130);
  }
}

.rot-05 *,
.rot-05 *::before,
.rot-05 *::after {
  box-sizing: border-box;
}

.rot-05__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.25rem, 3.5vw, 2rem);
  padding: clamp(1rem, 3vw, 2.25rem);
  padding-block-start: 5.25rem;
}

.rot-05__head {
  max-inline-size: 38rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-05__eyebrow {
  margin: 0 0 0.5rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-05__h {
  margin: 0 0 0.5rem;
  font-size: clamp(1.375rem, 4.6vw, 2.125rem);
  font-weight: 600;
  letter-spacing: -0.015em;
  line-height: 1.15;
}

.rot-05__sub {
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-05__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.rot-05__row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(6.5rem, 1fr));
  gap: 0.5rem;
  inline-size: min(100%, 44rem);
  padding: 0.75rem;
  border: 1px solid var(--rule);
  border-radius: 0.875rem;
  background: var(--surface);
}

.rot-05__col {
  min-inline-size: 0;
  display: grid;
  justify-items: center;
  gap: 0.35rem;
  padding: 0.75rem 0.25rem;
  border-radius: 0.625rem;
}

.rot-05__well {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: clamp(3.5rem, 12vw, 4.75rem);
  aspect-ratio: 1;
}

.rot-05__well--sm {
  inline-size: clamp(3rem, 10vw, 3.75rem);
}

.rot-05__well::before {
  content: "";
  position: absolute;
  inset: 12%;
  border: 1px solid var(--rule);
  border-radius: 50%;
}

.rot-05__mark {
  position: relative;
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
}

.rot-05__mark::before {
  content: "";
  position: absolute;
  inset-block-start: 6%;
  inset-inline-start: 50%;
  inline-size: var(--mark-w);
  block-size: var(--mark-h);
  translate: -50% 0;
  border-radius: 999px;
  background: var(--accent);
  box-shadow: var(--glow) color-mix(in srgb, var(--accent) 55%, transparent);
}

.rot-05__mark::after {
  content: "";
  position: absolute;
  inset: 44%;
  border-radius: 50%;
  background: color-mix(in srgb, var(--accent) 40%, transparent);
}

.rot-05__spin {
  animation: rot-05-turn var(--d, 1.6s) linear infinite;
}

.rot-05__spin--linear {
  animation-duration: 1.6s;
  animation-timing-function: linear;
}

.rot-05__spin--eased {
  animation-duration: 1.6s;
  animation-timing-function: ease-in-out;
}

.rot-05__spin--stepped {
  animation-duration: 1.6s;
  animation-timing-function: steps(8);
}

@keyframes rot-05-turn {
  to {
    transform: rotate(360deg);
  }
}

.rot-05__dur {
  margin: 0.2rem 0 0;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.9375rem;
  font-weight: 600;
  color: var(--ink);
}

.rot-05__read {
  margin: 0;
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.rot-05__curves {
  inline-size: min(100%, 44rem);
  display: grid;
  gap: 0.75rem;
  padding: 1rem 0.75rem;
  border: 1px solid var(--rule);
  border-radius: 0.875rem;
  background: var(--surface);
}

.rot-05__curvesh {
  margin: 0;
  text-align: center;
  font-size: 0.8125rem;
  letter-spacing: 0.02em;
  color: var(--muted);
}

.rot-05__curverow {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(9rem, 1fr));
  gap: 0.75rem;
}

.rot-05__curve {
  min-inline-size: 0;
  display: grid;
  justify-items: center;
  gap: 0.3rem;
}

.rot-05__curvelabel {
  margin: 0.15rem 0 0;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.8125rem;
  color: var(--accent);
}

.rot-05__curvenote {
  margin: 0;
  max-inline-size: 13rem;
  font-size: 0.75rem;
  line-height: 1.5;
  text-align: center;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-05__fine {
  inline-size: min(100%, 40rem);
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .rot-05__spin {
    animation: none;
  }

  .rot-05__col:nth-child(1) .rot-05__mark {
    transform: rotate(20deg);
  }

  .rot-05__col:nth-child(2) .rot-05__mark {
    transform: rotate(110deg);
  }

  .rot-05__col:nth-child(3) .rot-05__mark {
    transform: rotate(200deg);
  }

  .rot-05__col:nth-child(4) .rot-05__mark {
    transform: rotate(290deg);
  }

  .rot-05__curve:nth-child(1) .rot-05__mark {
    transform: rotate(45deg);
  }

  .rot-05__curve:nth-child(2) .rot-05__mark {
    transform: rotate(135deg);
  }

  .rot-05__curve:nth-child(3) .rot-05__mark {
    transform: rotate(225deg);
  }
}

.rot-05:has(.rot-05__pausebox:checked) .rot-05__spin {
  animation-play-state: paused;
}

.rot-05__theme {
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

.rot-05__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-05__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-05__themeopt {
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

.rot-05__themeopt:hover {
  opacity: 0.85;
}

.rot-05__themeinput:checked + .rot-05__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-05__themeinput:focus-visible + .rot-05__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-05__pause {
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

.rot-05__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-05__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-05__pause:has(.rot-05__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-05:has(.rot-05__pausebox:checked) .rot-05__pausedot {
  background: var(--accent);
  color: #06120a;
}

@media (forced-colors: active) {
  .rot-05__theme,
    .rot-05__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-05__themeinput:checked + .rot-05__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-05:not(:has(#rot-05-theme-dark:checked)) {
    --page: #f2f4f1;
    --surface: #ffffff;
    --ink: #12160f;
    --muted: #5b6357;
    --rule: #dfe4da;
    --accent: #3f7d16;
    --glow: 0 0 0;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-05:has(#rot-05-theme-light:checked) {
    --page: #f2f4f1;
    --surface: #ffffff;
    --ink: #12160f;
    --muted: #5b6357;
    --rule: #dfe4da;
    --accent: #3f7d16;
    --glow: 0 0 0;
  }
}

[data-theme="light"] .rot-05:not(:has(#rot-05-theme-dark:checked)) {
  --page: #f2f4f1;
  --surface: #ffffff;
  --ink: #12160f;
  --muted: #5b6357;
  --rule: #dfe4da;
  --accent: #3f7d16;
  --glow: 0 0 0;
}

.rot-05:has(#rot-05-theme-light:checked) {
  --page: #f2f4f1;
  --surface: #ffffff;
  --ink: #12160f;
  --muted: #5b6357;
  --rule: #dfe4da;
  --accent: #3f7d16;
  --glow: 0 0 0;
}

.rot-05:has(#rot-05-theme-light:checked) .rot-05__pausedot {
  color: #ffffff;
}

.rot-05:has(#rot-05-theme-dark:checked) {
  --page: #000000;
  --surface: #0a0c0a;
  --ink: #f2f7f2;
  --muted: #8a968c;
  --rule: #1a1f1b;
  --accent: #9dff4f;
  --glow: 0 0 18px;
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-05:not(:has(#rot-05-theme-light:checked)) {
  --page: #000000;
  --surface: #0a0c0a;
  --ink: #f2f7f2;
  --muted: #8a968c;
  --rule: #1a1f1b;
  --accent: #9dff4f;
  --glow: 0 0 18px;
}
```
