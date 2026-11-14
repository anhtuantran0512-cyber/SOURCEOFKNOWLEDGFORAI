---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/audio-control-suite/"
title: "Soft UI Media Player with Layered Controls"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The showcase piece: a player where every control is a physical object."
has_js: "true"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Soft UI Media Player with Layered Controls
Source: https://codefronts.com/design-styles/css-neumorphism/audio-control-suite/

The showcase piece: a player where every control is a physical object. Album art sunk into a recess, a scrubber running in a carved channel, transport buttons as convex pucks, and a play button that visibly stays pressed while playing. Eighteen lines of script drive play state and the scrubber; everything else is the depth system from the earlier demos, applied at once.
## HTML
```html
<section class="nm-17" aria-labelledby="nm-17-heading">
      <input type="checkbox" id="nm-17-theme" class="nm-17__themeinput">
      <label for="nm-17-theme" class="nm-17__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-17__stage">
    <header class="nm-17__head">
      <p class="nm-17__kicker">Showcase</p>
      <h2 class="nm-17__heading" id="nm-17-heading">Every control is an object</h2>
      <p class="nm-17__sub">Four depth levels, alternating direction — the most a soft-UI layout can carry, and the domain that earns it.</p>
    </header>

    <div class="nm-17__player">
      <div class="nm-17__slot">
        <div class="nm-17__art">
          <svg viewBox="0 0 120 120" width="100%" height="100%" aria-hidden="true">
            <rect width="120" height="120" fill="currentColor" opacity="0.14"/>
            <circle cx="60" cy="60" r="34" fill="none" stroke="currentColor" stroke-width="1.6" opacity="0.5"/>
            <circle cx="60" cy="60" r="20" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
            <circle cx="60" cy="60" r="6" fill="currentColor" opacity="0.55"/>
          </svg>
        </div>
      </div>

      <div class="nm-17__body">
        <div class="nm-17__meta">
          <p class="nm-17__track">Coastal Road, Late</p>
          <p class="nm-17__artist">Halden Rivers · Nightlines</p>
        </div>

        <div class="nm-17__scrub">
          <div class="nm-17__channel"><span class="nm-17__fill"></span><span class="nm-17__puck"></span></div>
          <div class="nm-17__times"><span class="nm-17__elapsed">0:00</span><span class="nm-17__total">4:12</span></div>
        </div>

        <div class="nm-17__transport">
          <button class="nm-17__btn" type="button" aria-label="Previous">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M17 5 8 12l9 7V5zM7 5v14" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
          </button>
          <button class="nm-17__btn nm-17__btn--play" type="button" aria-pressed="false" aria-label="Play">
            <svg class="nm-17__play" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M8 5.5 19 12 8 18.5v-13z" fill="currentColor"/></svg>
            <svg class="nm-17__pause" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M9 5v14M15 5v14" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>
          </button>
          <button class="nm-17__btn" type="button" aria-label="Next">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M7 5l9 7-9 7V5zM17 5v14" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
    </div>

    <p class="nm-17__foot">The play button latches — it stays inset while playing, and <code>aria-pressed</code> carries the same fact to assistive technology.</p>
  </div>
</section>
```
## CSS
```css
.nm-17 {
  position: relative;
  --nm-17-surface: #e5e1da;
  --nm-17-hi: #efece7;
  --nm-17-lo: #dbd6ce;
  --nm-17-dark: rgba(175,168,157,0.66);
  --nm-17-light: rgba(255,255,255,0.93);
  --nm-17-ink: #2b2823;
  --nm-17-muted: #5f594f;
  --nm-17-border: #a29a8e;
  --nm-17-accent: #a55b34;
  --nm-17-angle: 145deg;
  --nm-17-progress: 34%;
  --nm-17-font-display: "Instrument Serif", "Iowan Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-17-surface);
  color: var(--nm-17-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 70)) {
  .nm-17 {
    --nm-17-surface: oklch(0.902 0.011 78);
    --nm-17-ink: oklch(0.27 0.012 66);
    --nm-17-muted: oklch(0.45 0.016 68);
    --nm-17-accent: oklch(0.53 0.12 46);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-17 {
    --nm-17-dark: color-mix(in oklab, var(--nm-17-surface), #000 21%);
    --nm-17-light: color-mix(in oklab, var(--nm-17-surface), #fff 90%);
    --nm-17-hi: color-mix(in oklab, var(--nm-17-surface), #fff 25%);
    --nm-17-lo: color-mix(in oklab, var(--nm-17-surface), #000 6%);
    --nm-17-border: color-mix(in oklab, var(--nm-17-surface), var(--nm-17-ink) 34%);
  }
}

.nm-17 *,
.nm-17 *::before,
.nm-17 *::after {
  box-sizing: border-box;
}

.nm-17__stage {
  max-width: 860px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 34px);
}

.nm-17__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-17__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--nm-17-muted);
}

.nm-17__heading {
  margin: 0;
  font-family: var(--nm-17-font-display);
  font-size: clamp(1.7rem, 4.8vw, 2.6rem);
  font-weight: 400;
  letter-spacing: -0.01em;
  line-height: 1.08;
  text-wrap: balance;
}

.nm-17__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-17-muted);
  text-wrap: pretty;
}

.nm-17__player {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(20px, 3.4vw, 30px);
  align-items: center;
  border-radius: 28px;
  padding: clamp(20px, 3.6vw, 32px);
  background: linear-gradient(var(--nm-17-angle), var(--nm-17-hi), var(--nm-17-lo));
  border: 1px solid var(--nm-17-border);
  box-shadow: 14px 14px 30px var(--nm-17-dark), -14px -14px 30px var(--nm-17-light);
}

@media (min-width: 620px) {
  .nm-17__player {
    grid-template-columns: minmax(0, 200px) minmax(0, 1fr);
  }
}

.nm-17__slot {
  border-radius: 20px;
  padding: 10px;
  background: var(--nm-17-surface);
  box-shadow: inset 8px 8px 16px var(--nm-17-dark), inset -8px -8px 16px var(--nm-17-light);
}

.nm-17__art {
  aspect-ratio: 1;
  border-radius: 14px;
  overflow: hidden;
  color: var(--nm-17-accent);
  background: linear-gradient(var(--nm-17-angle), var(--nm-17-lo), var(--nm-17-hi));
  box-shadow: inset 0 0 0 1px var(--nm-17-border);
  display: grid;
  place-items: center;
}

.nm-17__body {
  display: flex;
  flex-direction: column;
  gap: 20px;
  min-inline-size: 0;
}

.nm-17__meta {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-inline-size: 0;
}

.nm-17__track {
  margin: 0;
  font-family: var(--nm-17-font-display);
  font-size: clamp(1.3rem, 4vw, 1.7rem);
  line-height: 1.15;
}

.nm-17__artist {
  margin: 0;
  font-size: 0.82rem;
  color: var(--nm-17-muted);
}

.nm-17__scrub {
  display: flex;
  flex-direction: column;
  gap: 9px;
  min-inline-size: 0;
}

.nm-17__channel {
  position: relative;
  height: 14px;
  border-radius: 999px;
  background: var(--nm-17-surface);
  box-shadow: inset 4px 4px 9px var(--nm-17-dark), inset -4px -4px 9px var(--nm-17-light);
}

.nm-17__fill {
  position: absolute;
  inset: 3px auto 3px 3px;
  width: calc(var(--nm-17-progress) - 6px);
  min-width: 0;
  border-radius: 999px;
  background: var(--nm-17-accent);
}

.nm-17__puck {
  position: absolute;
  top: 50%;
  left: var(--nm-17-progress);
  width: 20px;
  height: 20px;
  margin: -10px 0 0 -10px;
  border-radius: 50%;
  background: linear-gradient(var(--nm-17-angle), var(--nm-17-hi), var(--nm-17-lo));
  border: 1px solid var(--nm-17-border);
  box-shadow: 3px 3px 7px var(--nm-17-dark), -3px -3px 7px var(--nm-17-light);
}

.nm-17__times {
  display: flex;
  justify-content: space-between;
  font-size: 0.74rem;
  color: var(--nm-17-muted);
  font-variant-numeric: tabular-nums;
}

.nm-17__transport {
  display: flex;
  align-items: center;
  gap: 16px;
}

.nm-17__btn {
  width: 50px;
  height: 50px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 1px solid var(--nm-17-border);
  color: var(--nm-17-ink);
  cursor: pointer;
  background: linear-gradient(var(--nm-17-angle), var(--nm-17-hi), var(--nm-17-lo));
  box-shadow: 7px 7px 14px var(--nm-17-dark), -7px -7px 14px var(--nm-17-light);
  transition: box-shadow 150ms ease, color 150ms ease;
}

.nm-17__btn:active {
  box-shadow: inset 5px 5px 11px var(--nm-17-dark), inset -5px -5px 11px var(--nm-17-light);
}

.nm-17__btn:focus-visible {
  outline: 2px solid var(--nm-17-accent);
  outline-offset: 3px;
}

.nm-17__btn--play {
  width: 64px;
  height: 64px;
  color: var(--nm-17-accent);
}

.nm-17__btn--play[aria-pressed="true"] {
  background: linear-gradient(var(--nm-17-angle), var(--nm-17-lo), var(--nm-17-hi));
  box-shadow: inset 6px 6px 13px var(--nm-17-dark), inset -6px -6px 13px var(--nm-17-light);
}

.nm-17__pause,
.nm-17__btn--play[aria-pressed="true"] .nm-17__play {
  display: none;
}

.nm-17__btn--play[aria-pressed="true"] .nm-17__pause {
  display: block;
}

.nm-17__foot {
  margin: 0;
  max-width: 66ch;
  font-size: 0.82rem;
  line-height: 1.6;
  color: var(--nm-17-muted);
  text-wrap: pretty;
}

.nm-17__foot code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.9em;
  color: var(--nm-17-ink);
}

@media (prefers-reduced-motion: reduce) {
  .nm-17__btn {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-17 {
    --nm-17-surface: #2c2924;
    --nm-17-hi: #37332d;
    --nm-17-lo: #262320;
    --nm-17-dark: rgba(12,11,9,0.72);
    --nm-17-light: rgba(92,87,79,0.44);
    --nm-17-ink: #ece7df;
    --nm-17-muted: #a79f93;
    --nm-17-border: #857d71;
    --nm-17-accent: #e0916a;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-17 {
      --nm-17-dark: color-mix(in oklab, var(--nm-17-surface), #000 55%);
      --nm-17-light: color-mix(in oklab, var(--nm-17-surface), #fff 14%);
      --nm-17-hi: color-mix(in oklab, var(--nm-17-surface), #fff 8%);
      --nm-17-lo: color-mix(in oklab, var(--nm-17-surface), #000 12%);
    }
  }
}

.nm-17[data-theme="dark"] {
  --nm-17-surface: #2c2924;
  --nm-17-hi: #37332d;
  --nm-17-lo: #262320;
  --nm-17-dark: rgba(12,11,9,0.72);
  --nm-17-light: rgba(92,87,79,0.44);
  --nm-17-ink: #ece7df;
  --nm-17-muted: #a79f93;
  --nm-17-border: #857d71;
  --nm-17-accent: #e0916a;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-17[data-theme="dark"] {
    --nm-17-dark: color-mix(in oklab, var(--nm-17-surface), #000 55%);
    --nm-17-light: color-mix(in oklab, var(--nm-17-surface), #fff 14%);
    --nm-17-hi: color-mix(in oklab, var(--nm-17-surface), #fff 8%);
    --nm-17-lo: color-mix(in oklab, var(--nm-17-surface), #000 12%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-17__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-17__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-17-surface);
  color: var(--nm-17-ink);
  border: 1px solid var(--nm-17-line);
  font: 600 11px/1 var(--nm-17-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-17-distance, 6px) var(--nm-17-distance, 6px) var(--nm-17-blur, 14px) var(--nm-17-dark), calc(-1 * var(--nm-17-distance, 6px)) calc(-1 * var(--nm-17-distance, 6px)) var(--nm-17-blur, 14px) var(--nm-17-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-17__themebtn:hover {
  color: var(--nm-17-ink);
}

.nm-17__themeinput:focus-visible + .nm-17__themebtn {
  outline: 2px solid var(--nm-17-ink);
  outline-offset: 3px;
}

.nm-17:has(#nm-17-theme:checked) .nm-17__themebtn {
  box-shadow: inset var(--nm-17-distance, 6px) var(--nm-17-distance, 6px) var(--nm-17-blur, 14px) var(--nm-17-dark), inset calc(-1 * var(--nm-17-distance, 6px)) calc(-1 * var(--nm-17-distance, 6px)) var(--nm-17-blur, 14px) var(--nm-17-light);
}

.nm-17__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-17:has(#nm-17-theme:checked) {
  --nm-17-surface: #2c2924;
  --nm-17-hi: #37332d;
  --nm-17-lo: #262320;
  --nm-17-dark: rgba(12,11,9,0.72);
  --nm-17-light: rgba(92,87,79,0.44);
  --nm-17-ink: #ece7df;
  --nm-17-muted: #a79f93;
  --nm-17-border: #857d71;
  --nm-17-accent: #e0916a;
}

@media (prefers-color-scheme: light) {
  .nm-17:has(#nm-17-theme:checked) {
    --nm-17-surface: #2c2924;
    --nm-17-hi: #37332d;
    --nm-17-lo: #262320;
    --nm-17-dark: rgba(12,11,9,0.72);
    --nm-17-light: rgba(92,87,79,0.44);
    --nm-17-ink: #ece7df;
    --nm-17-muted: #a79f93;
    --nm-17-border: #857d71;
    --nm-17-accent: #e0916a;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-17:has(#nm-17-theme:checked) {
    --nm-17-surface: #e5e1da;
    --nm-17-hi: #efece7;
    --nm-17-lo: #dbd6ce;
    --nm-17-dark: rgba(175,168,157,0.66);
    --nm-17-light: rgba(255,255,255,0.93);
    --nm-17-ink: #2b2823;
    --nm-17-muted: #5f594f;
    --nm-17-border: #a29a8e;
    --nm-17-accent: #a55b34;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-17__themebtn {
    transition: none;
  }
}
```

## JavaScript
```js
const p = document.querySelector('.nm-17');
if (p) {
  const play = p.querySelector('.nm-17__btn--play');
  const el = p.querySelector('.nm-17__elapsed');
  const total = 252;
  let t = 0, timer = null;
  const fmt = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
  const paint = () => { el.textContent = fmt(t); p.style.setProperty('--nm-17-progress', (t / total * 100).toFixed(1) + '%'); };
  play.addEventListener('click', () => {
    const on = play.getAttribute('aria-pressed') === 'true';
    play.setAttribute('aria-pressed', String(!on));
    play.setAttribute('aria-label', on ? 'Play' : 'Pause');
    clearInterval(timer);
    if (!on) timer = setInterval(() => { t = (t + 1) % total; paint(); }, 1000);
  });
  paint();
}
```
