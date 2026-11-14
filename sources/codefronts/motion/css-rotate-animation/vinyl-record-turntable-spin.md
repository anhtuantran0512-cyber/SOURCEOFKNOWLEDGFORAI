---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/vinyl-record-turntable-spin/"
title: "Vinyl Record Turntable Spin"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A platter turning at a real 33⅓ rpm — 1.8s per revolution, not a round number that looked about right — with grooves from a repeating radial gradient, an…"
has_js: "true"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vinyl Record Turntable Spin
Source: https://codefronts.com/motion/css-rotate-animation/vinyl-record-turntable-spin/

A platter turning at a real 33⅓ rpm — 1.8s per revolution, not a round number that looked about right — with grooves from a repeating radial gradient, an off-centre label and a tonearm resting across the disc. Ten lines of JavaScript flip animation-play-state, so the record resumes from the angle it stopped at instead of snapping back.
## HTML
```html
<section class="rot-12" aria-labelledby="rot-12-h">
  <fieldset class="rot-12__theme">
    <legend class="rot-12__themelegend">Theme</legend>
    <input class="rot-12__themeinput" type="radio" name="rot-12-theme" id="rot-12-theme-auto" checked>
    <label class="rot-12__themeopt" for="rot-12-theme-auto">Auto</label>
    <input class="rot-12__themeinput" type="radio" name="rot-12-theme" id="rot-12-theme-light">
    <label class="rot-12__themeopt" for="rot-12-theme-light">Light</label>
    <input class="rot-12__themeinput" type="radio" name="rot-12-theme" id="rot-12-theme-dark">
    <label class="rot-12__themeopt" for="rot-12-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-12__stage">
    <header class="rot-12__head">
      <p class="rot-12__eyebrow">Fern &amp; Quill · Pressing 004</p>
      <h2 class="rot-12__h" id="rot-12-h">Thirty-three and a third is 1.8 seconds</h2>
      <p class="rot-12__sub">Sixty over 33.333 recurring, exactly. Rounding it to two seconds is the tell that separates a record from a spinning circle.</p>
    </header>

    <div class="rot-12__deck" id="rot-12-deck" data-spin="running">
      <div class="rot-12__platter" aria-hidden="true">
        <div class="rot-12__disc">
          <span class="rot-12__grooves"></span>
          <span class="rot-12__gloss"></span>
          <span class="rot-12__label">
            <span class="rot-12__labeltext">Longwave</span>
            <span class="rot-12__spindle"></span>
          </span>
        </div>
      </div>
      <div class="rot-12__arm" aria-hidden="true">
        <span class="rot-12__armpivot"></span>
        <span class="rot-12__armtube"></span>
        <span class="rot-12__armhead"></span>
      </div>
    </div>

    <div class="rot-12__transport">
      <button class="rot-12__btn" type="button" id="rot-12-toggle" aria-pressed="true">
        <span class="rot-12__btnicon" aria-hidden="true"></span>
        <span class="rot-12__btnlabel">Pause platter</span>
      </button>
      <output class="rot-12__state" id="rot-12-state" aria-live="polite">Running · 33⅓ rpm · 1.8s per turn</output>
    </div>

    <dl class="rot-12__specs">
      <div class="rot-12__specrow"><dt class="rot-12__dt">33⅓ rpm</dt><dd class="rot-12__dd">1.800s</dd></div>
      <div class="rot-12__specrow"><dt class="rot-12__dt">45 rpm</dt><dd class="rot-12__dd">1.333s</dd></div>
      <div class="rot-12__specrow"><dt class="rot-12__dt">78 rpm</dt><dd class="rot-12__dd">0.769s</dd></div>
    </dl>

    <p class="rot-12__fine">Pausing freezes the platter at its current angle and resumes from there. This is a mechanism, not a menu — the vinyl-as-navigation shape belongs somewhere else.</p>
  </div>
</section>
```
## CSS
```css
.rot-12 {
  --page: #17110b;
  --walnut-1: #3f2a1a;
  --walnut-2: #26180e;
  --brass: #d8a951;
  --ink: #f6ece0;
  --muted: #a8917a;
  --rule: #3a2a1c;
  --platter: #0d0b09;
  --label: #c8452f;
  --gloss: 0.5;
  --rpm-period: 1.8s;
  --groove-step: 2px;
  --arm-angle: -19deg;
  --disc: clamp(11rem, 44vw, 17rem);
  --font-display: Baskerville, "Hoefler Text", "Palatino Linotype", Palatino, serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: linear-gradient(165deg, var(--walnut-1) 0%, var(--page) 60%, #0d0906 100%);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-12 {
    --brass: oklch(0.78 0.12 82);
    --label: oklch(0.58 0.18 30);
  }
}

.rot-12 *,
.rot-12 *::before,
.rot-12 *::after {
  box-sizing: border-box;
}

.rot-12__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.5rem);
  padding: clamp(1.5rem, 4vw, 3.5rem);
  padding-block-start: 5.5rem;
}

.rot-12__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-12__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--brass);
}

.rot-12__h {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 400;
  line-height: 1.1;
}

.rot-12__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-12__deck {
  position: relative;
  inline-size: min(100%, 28rem);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  border: 1px solid var(--rule);
  border-radius: 1.25rem;
  background: linear-gradient(155deg, var(--walnut-1), var(--walnut-2));
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.12), 0 30px 60px -34px rgba(0, 0, 0, 0.9);
}

.rot-12__platter {
  display: grid;
  place-items: center;
  inline-size: calc(var(--disc) * 1.12);
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle, #221a13 0%, var(--platter) 70%);
  box-shadow: inset 0 0 24px rgba(0, 0, 0, 0.8);
}

.rot-12__disc {
  position: relative;
  inline-size: var(--disc);
  aspect-ratio: 1;
  border-radius: 50%;
  background: #0a0a0b;
  animation: rot-12-platter var(--rpm-period) linear infinite;
}

.rot-12__grooves {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.08) 0 1px, rgba(0, 0, 0, 0.55) 1px var(--groove-step));
  -webkit-mask: radial-gradient(circle, transparent 0 27%, #000 28% 100%);
  mask: radial-gradient(circle, transparent 0 27%, #000 28% 100%);
}

.rot-12__gloss {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: linear-gradient(118deg, transparent 34%, rgba(255, 255, 255, 0.22) 47%, transparent 56%);
  opacity: var(--gloss);
}

.rot-12__label {
  position: absolute;
  inset: 30%;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: radial-gradient(circle at 40% 34%, color-mix(in srgb, var(--label) 80%, #ffffff), var(--label) 70%);
}

.rot-12__labeltext {
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.92);
  transform: translateY(-1.15em);
}

.rot-12__spindle {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 8%;
  aspect-ratio: 1;
  translate: -50% -50%;
  border-radius: 50%;
  background: #14100c;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.9);
}

@keyframes rot-12-platter {
  to {
    transform: rotate(360deg);
  }
}

.rot-12__arm {
  position: absolute;
  inset-block-start: 8%;
  inset-inline-end: 9%;
  inline-size: 42%;
  block-size: 52%;
}

.rot-12__armpivot {
  position: absolute;
  inset-block-start: 0;
  inset-inline-end: 0;
  inline-size: 1.9rem;
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle at 38% 32%, #f0dcae, var(--brass) 65%, #7a5a1d 100%);
  box-shadow: 0 4px 10px -4px rgba(0, 0, 0, 0.8);
}

.rot-12__armtube {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.9rem;
  inline-size: 0.3rem;
  block-size: 88%;
  transform-origin: 50% 0;
  transform: rotate(var(--arm-angle));
  border-radius: 999px;
  background: linear-gradient(90deg, #8d8f95, #d7d9dd 45%, #6f7178);
}

.rot-12__armhead {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.9rem;
  inline-size: 0.85rem;
  block-size: 88%;
  transform-origin: 50% 0;
  transform: rotate(var(--arm-angle));
}

.rot-12__armhead::after {
  content: "";
  position: absolute;
  inset-block-end: -0.2rem;
  inset-inline-start: -0.15rem;
  inline-size: 0.95rem;
  block-size: 1.1rem;
  border-radius: 0.15rem;
  background: #2b2b2e;
  box-shadow: 0 3px 8px -3px rgba(0, 0, 0, 0.85);
}

.rot-12__transport {
  display: flex;
  align-items: center;
  gap: 0.875rem;
  flex-wrap: wrap;
  justify-content: center;
}

.rot-12__btn {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 2.75rem;
  padding: 0 1.1rem;
  border: 1px solid var(--brass);
  border-radius: 999px;
  background: transparent;
  color: var(--ink);
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
}

.rot-12__btn:hover {
  background: color-mix(in srgb, var(--brass) 18%, transparent);
}

.rot-12__btn:focus-visible {
  outline: 2px solid var(--brass);
  outline-offset: 3px;
}

.rot-12__btnicon {
  inline-size: 0.75rem;
  block-size: 0.75rem;
  border-inline: 0.25rem solid var(--brass);
}

.rot-12__deck[data-spin="paused"] ~ .rot-12__transport .rot-12__btnicon {
  border-inline: 0;
  border-block: 0;
  inline-size: 0;
  block-size: 0;
  border-inline-start: 0.7rem solid var(--brass);
  border-block-start: 0.4rem solid transparent;
  border-block-end: 0.4rem solid transparent;
}

.rot-12__state {
  font-size: 0.8125rem;
  color: var(--muted);
}

.rot-12__specs {
  inline-size: min(100%, 28rem);
  margin: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(7rem, 1fr));
  gap: 0.5rem;
}

.rot-12__specrow {
  display: grid;
  gap: 0.15rem;
  padding: 0.6rem 0.75rem;
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  background: rgba(0, 0, 0, 0.2);
  min-inline-size: 0;
}

.rot-12__dt {
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.rot-12__dd {
  margin: 0;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.9375rem;
  color: var(--brass);
}

.rot-12__fine {
  inline-size: min(100%, 34rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-12__deck[data-spin="paused"] .rot-12__disc {
  animation-play-state: paused;
}

@media (prefers-reduced-motion: reduce) {
  .rot-12__disc {
    animation: none;
  }
}

.rot-12__theme {
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

.rot-12__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-12__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-12__themeopt {
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

.rot-12__themeopt:hover {
  opacity: 0.85;
}

.rot-12__themeinput:checked + .rot-12__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-12__themeinput:focus-visible + .rot-12__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-12__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-12__themeinput:checked + .rot-12__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-12:not(:has(#rot-12-theme-dark:checked)) {
    --page: #efe6d9;
    --walnut-1: #c8a880;
    --walnut-2: #a8845c;
    --ink: #241a11;
    --muted: #6b5844;
    --rule: #c3a680;
    --brass: #8a5e12;
    background: linear-gradient(165deg, #f6efe4 0%, #e6d8c4 60%, #d8c7ad 100%);
  }

  .rot-12:not(:has(#rot-12-theme-dark:checked)) .rot-12__specrow {
    background: rgba(255, 255, 255, 0.5);
  }
}

@media (prefers-color-scheme: dark) {
  .rot-12:has(#rot-12-theme-light:checked) {
    --page: #efe6d9;
    --walnut-1: #c8a880;
    --walnut-2: #a8845c;
    --ink: #241a11;
    --muted: #6b5844;
    --rule: #c3a680;
    --brass: #8a5e12;
    background: linear-gradient(165deg, #f6efe4 0%, #e6d8c4 60%, #d8c7ad 100%);
  }

  .rot-12:has(#rot-12-theme-light:checked) .rot-12__specrow {
    background: rgba(255, 255, 255, 0.5);
  }
}

[data-theme="light"] .rot-12:not(:has(#rot-12-theme-dark:checked)) {
  --page: #efe6d9;
  --walnut-1: #c8a880;
  --walnut-2: #a8845c;
  --ink: #241a11;
  --muted: #6b5844;
  --rule: #c3a680;
  --brass: #8a5e12;
  background: linear-gradient(165deg, #f6efe4 0%, #e6d8c4 60%, #d8c7ad 100%);
}

.rot-12:has(#rot-12-theme-light:checked) {
  --page: #efe6d9;
  --walnut-1: #c8a880;
  --walnut-2: #a8845c;
  --ink: #241a11;
  --muted: #6b5844;
  --rule: #c3a680;
  --brass: #8a5e12;
  background: linear-gradient(165deg, #f6efe4 0%, #e6d8c4 60%, #d8c7ad 100%);
}

.rot-12:has(#rot-12-theme-light:checked) .rot-12__specrow {
  background: rgba(255, 255, 255, 0.5);
}

.rot-12:has(#rot-12-theme-dark:checked) {
  --page: #17110b;
  --walnut-1: #3f2a1a;
  --walnut-2: #26180e;
  --ink: #f6ece0;
  --muted: #a8917a;
  --rule: #3a2a1c;
  --brass: #d8a951;
  background: linear-gradient(165deg, #3f2a1a 0%, #17110b 60%, #0d0906 100%);
}

.rot-12:has(#rot-12-theme-dark:checked) .rot-12__specrow {
  background: rgba(0, 0, 0, 0.2);
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-12:not(:has(#rot-12-theme-light:checked)) {
  --page: #17110b;
  --walnut-1: #3f2a1a;
  --walnut-2: #26180e;
  --ink: #f6ece0;
  --muted: #a8917a;
  --rule: #3a2a1c;
  --brass: #d8a951;
  background: linear-gradient(165deg, #3f2a1a 0%, #17110b 60%, #0d0906 100%);
}

[data-theme="dark"] .rot-12:not(:has(#rot-12-theme-light:checked)) .rot-12__specrow {
  background: rgba(0, 0, 0, 0.2);
}
```

## JavaScript
```js
(() => {
  const deck = document.querySelector('.rot-12__deck');
  if (!deck || deck.dataset.rot12) return;
  deck.dataset.rot12 = '1';
  const btn = document.querySelector('.rot-12__btn');
  const state = document.querySelector('.rot-12__state');
  const label = btn.querySelector('.rot-12__btnlabel');
  const sync = () => {
    const running = deck.dataset.spin === 'running';
    btn.setAttribute('aria-pressed', String(running));
    label.textContent = running ? 'Pause platter' : 'Resume platter';
    state.textContent = running ? 'Running · 33⅓ rpm · 1.8s per turn' : 'Paused · frozen at the current angle';
  };
  btn.addEventListener('click', () => {
    deck.dataset.spin = deck.dataset.spin === 'running' ? 'paused' : 'running';
    sync();
  });
  sync();
})();
```
