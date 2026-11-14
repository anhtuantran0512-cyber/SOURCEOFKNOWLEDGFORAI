---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/infinite-rotate-animation-with-keyframes/"
title: "Infinite Rotate Animation with Keyframes"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "The canonical continuous-rotation recipe: one keyframe block ending at rotate(360deg), one animation shorthand with linear and infinite."
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinite Rotate Animation with Keyframes
Source: https://codefronts.com/motion/css-rotate-animation/infinite-rotate-animation-with-keyframes/

The canonical continuous-rotation recipe: one keyframe block ending at rotate(360deg), one animation shorthand with linear and infinite. Two dials run the identical four-second rotation side by side, one linear and one eased, so the stutter an eased curve creates at every cycle boundary is visible rather than asserted. Reach for this whenever something needs to turn without stopping.
## HTML
```html
<section class="rot-01" aria-labelledby="rot-01-h">
  <fieldset class="rot-01__theme">
    <legend class="rot-01__themelegend">Theme</legend>
    <input class="rot-01__themeinput" type="radio" name="rot-01-theme" id="rot-01-theme-auto" checked>
    <label class="rot-01__themeopt" for="rot-01-theme-auto">Auto</label>
    <input class="rot-01__themeinput" type="radio" name="rot-01-theme" id="rot-01-theme-light">
    <label class="rot-01__themeopt" for="rot-01-theme-light">Light</label>
    <input class="rot-01__themeinput" type="radio" name="rot-01-theme" id="rot-01-theme-dark">
    <label class="rot-01__themeopt" for="rot-01-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-01__pause">
    <input class="rot-01__pausebox" type="checkbox" id="rot-01-pause">
    <span class="rot-01__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-01__pausetext">Pause</span>
  </label>

  <div class="rot-01__stage">
    <header class="rot-01__head">
      <p class="rot-01__eyebrow">Continuous rotation</p>
      <h2 class="rot-01__h" id="rot-01-h">One keyframe, four seconds, forever</h2>
      <p class="rot-01__sub">Both dials run the same <span class="rot-01__code">rot-01-spin</span> keyframe at the same duration. Only the timing function differs. Watch the fixed seam at twelve o'clock.</p>
    </header>

    <div class="rot-01__pair">
      <article class="rot-01__panel">
        <p class="rot-01__label">
          <span class="rot-01__code">linear</span>
          <span class="rot-01__labeltext">Constant angular velocity</span>
        </p>
        <div class="rot-01__well">
          <span class="rot-01__seam" aria-hidden="true"></span>
          <div class="rot-01__dial rot-01__spin rot-01__spin--linear" aria-hidden="true">
            <span class="rot-01__ticks"></span>
            <span class="rot-01__index"></span>
            <span class="rot-01__hub"></span>
          </div>
        </div>
        <p class="rot-01__verdict rot-01__verdict--good">The index mark crosses the seam at the same speed it left it. The cycle boundary is invisible.</p>
      </article>

      <article class="rot-01__panel rot-01__panel--muted">
        <p class="rot-01__label">
          <span class="rot-01__code">ease-in-out</span>
          <span class="rot-01__labeltext">Decelerates into every seam</span>
        </p>
        <div class="rot-01__well">
          <span class="rot-01__seam" aria-hidden="true"></span>
          <div class="rot-01__dial rot-01__spin rot-01__spin--eased" aria-hidden="true">
            <span class="rot-01__ticks"></span>
            <span class="rot-01__index"></span>
            <span class="rot-01__hub"></span>
          </div>
        </div>
        <p class="rot-01__verdict rot-01__verdict--bad">It slows almost to a stop at the seam, then lunges away from it. Four times a cycle, forever.</p>
      </article>
    </div>

    <dl class="rot-01__spec">
      <div class="rot-01__specrow">
        <dt class="rot-01__dt">The keyframe</dt>
        <dd class="rot-01__dd"><span class="rot-01__code">to { transform: rotate(360deg) }</span> — no <span class="rot-01__code">from</span> block. The element's current transform is the implicit start, so the same keyframe works on an element already tilted.</dd>
      </div>
      <div class="rot-01__specrow">
        <dt class="rot-01__dt">The shorthand</dt>
        <dd class="rot-01__dd"><span class="rot-01__code">animation: rot-01-spin 4s linear infinite</span> — duration, curve and count in one declaration. Drop <span class="rot-01__code">infinite</span> and it turns exactly once.</dd>
      </div>
      <div class="rot-01__specrow">
        <dt class="rot-01__dt">Degrees or turns</dt>
        <dd class="rot-01__dd"><span class="rot-01__code">360deg</span> and <span class="rot-01__code">1turn</span> are the same rotation. Readability decides; only a negative angle changes behaviour, reversing the direction.</dd>
      </div>
    </dl>
  </div>
</section>
```
## CSS
```css
.rot-01 {
  --page: #f6f7f9;
  --surface: #ffffff;
  --ink: #14161c;
  --muted: #62667a;
  --rule: #e2e4ea;
  --accent: #6b4df6;
  --warn: #b4571a;
  --dial: clamp(7rem, 26vw, 10.5rem);
  --spin: 4s;
  --font-display: system-ui, "Segoe UI", sans-serif;
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
  .rot-01 {
    --accent: oklch(0.55 0.24 288);
    --warn: oklch(0.55 0.14 55);
  }
}

.rot-01 *,
.rot-01 *::before,
.rot-01 *::after {
  box-sizing: border-box;
}

.rot-01__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.75rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-01__head {
  max-inline-size: 40rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-01__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-01__h {
  margin: 0 0 0.65rem;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 4.4vw, 2.1rem);
  font-weight: 650;
  letter-spacing: -0.02em;
  line-height: 1.15;
}

.rot-01__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-01__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  padding: 0.1em 0.35em;
  border-radius: 0.25rem;
  background: #eceef4;
  color: var(--ink);
}

.rot-01__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: clamp(1rem, 3vw, 1.75rem);
  inline-size: min(100%, 46rem);
}

.rot-01__panel {
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
  justify-items: center;
  padding: clamp(1rem, 3vw, 1.5rem);
  border: 1px solid var(--rule);
  border-radius: 1rem;
  background: var(--surface);
  box-shadow: 0 1px 2px rgba(20, 22, 28, 0.05), 0 12px 28px -22px rgba(20, 22, 28, 0.35);
}

.rot-01__label {
  display: grid;
  gap: 0.35rem;
  justify-items: center;
  margin: 0;
  text-align: center;
}

.rot-01__labeltext {
  font-size: 0.75rem;
  color: var(--muted);
}

.rot-01__well {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: calc(var(--dial) * 1.45);
  block-size: calc(var(--dial) * 1.45);
}

.rot-01__seam {
  position: absolute;
  inset-block-start: 2%;
  inset-inline-start: 50%;
  inline-size: 1px;
  block-size: calc(var(--dial) * 0.62);
  background: linear-gradient(var(--accent), transparent);
  opacity: 0.5;
}

.rot-01__dial {
  position: relative;
  inline-size: var(--dial);
  block-size: var(--dial);
  border-radius: 50%;
}

.rot-01__ticks {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, var(--rule) 0deg 1.4deg, transparent 1.4deg 15deg);
  -webkit-mask: radial-gradient(circle, transparent 0 68%, #000 69% 100%);
  mask: radial-gradient(circle, transparent 0 68%, #000 69% 100%);
}

.rot-01__index {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 50%;
  inline-size: 0.5rem;
  block-size: 42%;
  translate: -50% 0;
  border-radius: 999px;
  background: linear-gradient(var(--accent), color-mix(in srgb, var(--accent) 30%, transparent));
}

.rot-01__hub {
  position: absolute;
  inset: 38%;
  border-radius: 50%;
  background: var(--ink);
}

.rot-01__spin {
  animation: rot-01-spin var(--spin) linear infinite;
}

.rot-01__spin--eased {
  animation-timing-function: ease-in-out;
}

@keyframes rot-01-spin {
  to {
    transform: rotate(360deg);
  }
}

.rot-01__verdict {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.55;
  text-align: center;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-01__verdict--good {
  color: var(--accent);
}

.rot-01__verdict--bad {
  color: var(--warn);
}

.rot-01__spec {
  inline-size: min(100%, 46rem);
  margin: 0;
  display: grid;
  gap: 0;
  border: 1px solid var(--rule);
  border-radius: 1rem;
  background: var(--surface);
  overflow: hidden;
}

.rot-01__specrow {
  display: grid;
  grid-template-columns: minmax(0, 9rem) minmax(0, 1fr);
  gap: 0.75rem 1.25rem;
  padding: 0.9rem clamp(0.9rem, 3vw, 1.4rem);
  border-block-start: 1px solid var(--rule);
}

.rot-01__specrow:first-child {
  border-block-start: 0;
}

.rot-01__dt {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink);
  min-inline-size: 0;
}

.rot-01__dd {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  min-inline-size: 0;
}

@media (max-width: 30rem) {
  .rot-01__specrow {
    grid-template-columns: minmax(0, 1fr);
    gap: 0.3rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rot-01__spin {
    animation: none;
    transform: rotate(28deg);
  }
}

.rot-01:has(.rot-01__pausebox:checked) .rot-01__spin {
  animation-play-state: paused;
}

.rot-01__theme {
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

.rot-01__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-01__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-01__themeopt {
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

.rot-01__themeopt:hover {
  opacity: 0.85;
}

.rot-01__themeinput:checked + .rot-01__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-01__themeinput:focus-visible + .rot-01__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-01__pause {
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

.rot-01__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-01__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-01__pause:has(.rot-01__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-01:has(.rot-01__pausebox:checked) .rot-01__pausedot {
  background: var(--accent);
  color: var(--surface);
}

@media (forced-colors: active) {
  .rot-01__theme,
    .rot-01__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-01__themeinput:checked + .rot-01__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-01:not(:has(#rot-01-theme-light:checked)) {
    --page: #0b0c11;
    --surface: #14161d;
    --ink: #eceef5;
    --muted: #9298ad;
    --rule: #232733;
    --accent: #a08cff;
    --warn: #ffab63;
  }

  .rot-01:not(:has(#rot-01-theme-light:checked)) .rot-01__code {
    background: #1d212b;
    color: #eceef5;
  }

  .rot-01:not(:has(#rot-01-theme-light:checked)) .rot-01__panel {
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
  }

  .rot-01:not(:has(#rot-01-theme-light:checked)) .rot-01__hub {
    background: #eceef5;
  }
}

@media (prefers-color-scheme: light) {
  .rot-01:has(#rot-01-theme-dark:checked) {
    --page: #0b0c11;
    --surface: #14161d;
    --ink: #eceef5;
    --muted: #9298ad;
    --rule: #232733;
    --accent: #a08cff;
    --warn: #ffab63;
  }
}

[data-theme="dark"] .rot-01:not(:has(#rot-01-theme-light:checked)) {
  --page: #0b0c11;
  --surface: #14161d;
  --ink: #eceef5;
  --muted: #9298ad;
  --rule: #232733;
  --accent: #a08cff;
  --warn: #ffab63;
}

[data-theme="dark"] .rot-01:not(:has(#rot-01-theme-light:checked)) .rot-01__code {
  background: #1d212b;
  color: #eceef5;
}

[data-theme="dark"] .rot-01:not(:has(#rot-01-theme-light:checked)) .rot-01__hub {
  background: #eceef5;
}

.rot-01:has(#rot-01-theme-dark:checked) {
  --page: #0b0c11;
  --surface: #14161d;
  --ink: #eceef5;
  --muted: #9298ad;
  --rule: #232733;
  --accent: #a08cff;
  --warn: #ffab63;
}

.rot-01:has(#rot-01-theme-dark:checked) .rot-01__code {
  background: #1d212b;
  color: #eceef5;
}

.rot-01:has(#rot-01-theme-dark:checked) .rot-01__panel {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}

.rot-01:has(#rot-01-theme-dark:checked) .rot-01__hub {
  background: #eceef5;
}

.rot-01:has(#rot-01-theme-light:checked) {
  --page: #f6f7f9;
  --surface: #ffffff;
  --ink: #14161c;
  --muted: #62667a;
  --rule: #e2e4ea;
  --accent: #6b4df6;
  --warn: #b4571a;
}

.rot-01:has(#rot-01-theme-light:checked) .rot-01__code {
  background: #eceef4;
  color: #14161c;
}

.rot-01:has(#rot-01-theme-light:checked) .rot-01__hub {
  background: #14161c;
}
```
