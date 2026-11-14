---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/soft-ui-calculator/"
title: "Soft UI Keypad and the Paint Cost of Shadows"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Twelve keys, twenty-four blurred shadows, and a measurable cost."
has_js: "true"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Soft UI Keypad and the Paint Cost of Shadows
Source: https://codefronts.com/design-styles/css-neumorphism/soft-ui-calculator/

Twelve keys, twenty-four blurred shadows, and a measurable cost. A working soft-UI keypad with a live toggle between three shadow strategies — full blurred pairs, a single shadow, and a pre-composited parent — so you can watch the difference in a profiler. The lesson: box-shadow is cheap once and expensive in bulk, and the fix is almost never will-change.
## HTML
```html
<section class="nm-12" aria-labelledby="nm-12-heading">
      <input type="checkbox" id="nm-12-theme" class="nm-12__themeinput">
      <label for="nm-12-theme" class="nm-12__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-12__stage">
    <header class="nm-12__head">
      <p class="nm-12__kicker">Performance</p>
      <h2 class="nm-12__heading" id="nm-12-heading">Twelve keys, twenty-four blurs</h2>
      <p class="nm-12__sub">Shadows are cheap once and expensive in bulk. Switch strategies and profile the difference.</p>
    </header>

    <div class="nm-12__switcher" role="group" aria-label="Shadow strategy">
      <button class="nm-12__strat is-active" type="button" data-strategy="full">A · full pairs</button>
      <button class="nm-12__strat" type="button" data-strategy="single">B · single shadow</button>
      <button class="nm-12__strat" type="button" data-strategy="parent">C · parent only</button>
    </div>

    <div class="nm-12__layout">
      <div class="nm-12__pad" data-strategy="full">
        <div class="nm-12__display"><span class="nm-12__readout">0</span></div>
        <div class="nm-12__keys">
          <button class="nm-12__key" type="button">1</button>
          <button class="nm-12__key" type="button">2</button>
          <button class="nm-12__key" type="button">3</button>
          <button class="nm-12__key" type="button">4</button>
          <button class="nm-12__key" type="button">5</button>
          <button class="nm-12__key" type="button">6</button>
          <button class="nm-12__key" type="button">7</button>
          <button class="nm-12__key" type="button">8</button>
          <button class="nm-12__key" type="button">9</button>
          <button class="nm-12__key nm-12__key--alt" type="button" data-action="clear">C</button>
          <button class="nm-12__key" type="button">0</button>
          <button class="nm-12__key nm-12__key--alt" type="button" data-action="back">←</button>
        </div>
      </div>

      <div class="nm-12__notes">
        <article class="nm-12__note" data-for="full">
          <h3 class="nm-12__ntitle">A · Full mirrored pairs</h3>
          <p class="nm-12__nbody">Twenty-four blurred rasters, one dark and one light per key. Correct-looking, and the most expensive thing on the screen.</p>
        </article>
        <article class="nm-12__note" data-for="single">
          <h3 class="nm-12__ntitle">B · One shadow plus inset hairline</h3>
          <p class="nm-12__nbody">Keeps the dark shadow, replaces the light one with a 1px inset highlight. Half the blur area, near-identical read.</p>
        </article>
        <article class="nm-12__note" data-for="parent">
          <h3 class="nm-12__ntitle">C · Pre-composited parent</h3>
          <p class="nm-12__nbody">One shadow on the pad, keys separated by gaps and hairlines. Twelve borders instead of twenty-four blurs — and no per-key depth.</p>
        </article>
        <p class="nm-12__tip">Press feedback stays on <code>transform</code> in all three, so the interaction never enters the paint path.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-12 {
  position: relative;
  --nm-12-surface: #e5e8ea;
  --nm-12-dark: rgba(167,175,180,0.62);
  --nm-12-light: rgba(255,255,255,0.94);
  --nm-12-ink: #232830;
  --nm-12-muted: #58606a;
  --nm-12-border: #979ea7;
  --nm-12-accent: #2f6f8f;
  --nm-12-dist: 7px;
  --nm-12-blur: 15px;
  --nm-12-font-display: ui-monospace, "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-12-surface);
  color: var(--nm-12-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 230)) {
  .nm-12 {
    --nm-12-surface: oklch(0.923 0.007 230);
    --nm-12-ink: oklch(0.27 0.018 255);
    --nm-12-muted: oklch(0.46 0.019 255);
    --nm-12-accent: oklch(0.5 0.09 232);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-12 {
    --nm-12-dark: color-mix(in oklab, var(--nm-12-surface), #000 19%);
    --nm-12-light: color-mix(in oklab, var(--nm-12-surface), #fff 92%);
    --nm-12-border: color-mix(in oklab, var(--nm-12-surface), var(--nm-12-ink) 33%);
  }
}

.nm-12 *,
.nm-12 *::before,
.nm-12 *::after {
  box-sizing: border-box;
}

.nm-12__stage {
  max-width: 980px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(20px, 3.2vw, 32px);
}

.nm-12__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-12__kicker {
  margin: 0;
  font-family: var(--nm-12-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--nm-12-muted);
}

.nm-12__heading {
  margin: 0;
  font-family: var(--nm-12-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.2rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-12__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-12-muted);
  text-wrap: pretty;
}

.nm-12__switcher {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.nm-12__strat {
  min-height: 44px;
  padding: 0 16px;
  border-radius: 12px;
  border: 1px solid var(--nm-12-border);
  background: var(--nm-12-surface);
  color: var(--nm-12-muted);
  font: inherit;
  font-family: var(--nm-12-font-display);
  font-size: 0.78rem;
  cursor: pointer;
  box-shadow: 5px 5px 11px var(--nm-12-dark), -5px -5px 11px var(--nm-12-light);
}

.nm-12__strat.is-active {
  color: var(--nm-12-accent);
  border-color: var(--nm-12-accent);
  box-shadow: inset 4px 4px 9px var(--nm-12-dark), inset -4px -4px 9px var(--nm-12-light);
}

.nm-12__strat:focus-visible {
  outline: 2px solid var(--nm-12-accent);
  outline-offset: 3px;
}

.nm-12__layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(20px, 3.4vw, 32px);
  align-items: start;
}

@media (min-width: 760px) {
  .nm-12__layout {
    grid-template-columns: minmax(0, 300px) minmax(0, 1fr);
  }
}

.nm-12__pad {
  border-radius: 26px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  min-inline-size: 0;
  background: var(--nm-12-surface);
  border: 1px solid var(--nm-12-border);
}

.nm-12__pad[data-strategy="parent"] {
  box-shadow: 12px 12px 26px var(--nm-12-dark), -12px -12px 26px var(--nm-12-light);
}

.nm-12__display {
  border-radius: 14px;
  padding: 16px 18px;
  text-align: right;
  background: var(--nm-12-surface);
  box-shadow: inset 5px 5px 10px var(--nm-12-dark), inset -5px -5px 10px var(--nm-12-light);
}

.nm-12__readout {
  font-family: var(--nm-12-font-display);
  font-size: 1.7rem;
  font-variant-numeric: tabular-nums;
  overflow-wrap: anywhere;
}

.nm-12__keys {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.nm-12__key {
  min-height: 56px;
  border-radius: 16px;
  border: 1px solid var(--nm-12-border);
  background: var(--nm-12-surface);
  color: var(--nm-12-ink);
  font: inherit;
  font-family: var(--nm-12-font-display);
  font-size: 1.05rem;
  cursor: pointer;
  transition: transform 90ms ease;
}

.nm-12__key--alt {
  color: var(--nm-12-accent);
}

.nm-12__key:active {
  transform: translateY(2px);
}

.nm-12__key:focus-visible {
  outline: 2px solid var(--nm-12-accent);
  outline-offset: 2px;
}

.nm-12__pad[data-strategy="full"] .nm-12__key {
  box-shadow: var(--nm-12-dist) var(--nm-12-dist) var(--nm-12-blur) var(--nm-12-dark), calc(var(--nm-12-dist) * -1) calc(var(--nm-12-dist) * -1) var(--nm-12-blur) var(--nm-12-light);
}

.nm-12__pad[data-strategy="single"] .nm-12__key {
  box-shadow: var(--nm-12-dist) var(--nm-12-dist) var(--nm-12-blur) var(--nm-12-dark), inset 0 1px 0 var(--nm-12-light);
}

.nm-12__pad[data-strategy="parent"] .nm-12__key {
  box-shadow: inset 0 1px 0 var(--nm-12-light);
}

.nm-12__notes {
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-inline-size: 0;
}

.nm-12__note {
  border-radius: 16px;
  padding: 16px 18px;
  min-inline-size: 0;
  background: var(--nm-12-surface);
  border: 1px solid var(--nm-12-border);
  box-shadow: 6px 6px 13px var(--nm-12-dark), -6px -6px 13px var(--nm-12-light);
  opacity: 0.55;
  transition: opacity 180ms ease;
}

.nm-12__note.is-active {
  opacity: 1;
}

.nm-12__ntitle {
  margin: 0 0 6px;
  font-family: var(--nm-12-font-display);
  font-size: 0.86rem;
  font-weight: 600;
}

.nm-12__nbody {
  margin: 0;
  font-size: 0.82rem;
  line-height: 1.6;
  color: var(--nm-12-muted);
  text-wrap: pretty;
}

.nm-12__tip {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.6;
  color: var(--nm-12-muted);
  text-wrap: pretty;
}

.nm-12__tip code {
  font-family: var(--nm-12-font-display);
  font-size: 0.9em;
  color: var(--nm-12-ink);
}

@media (prefers-reduced-motion: reduce) {
  .nm-12__key,
    .nm-12__note {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-12 {
    --nm-12-surface: #262a30;
    --nm-12-dark: rgba(11,12,15,0.72);
    --nm-12-light: rgba(88,94,104,0.44);
    --nm-12-ink: #e7eaef;
    --nm-12-muted: #9aa2ad;
    --nm-12-border: #858d98;
    --nm-12-accent: #74b4d4;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-12 {
      --nm-12-dark: color-mix(in oklab, var(--nm-12-surface), #000 55%);
      --nm-12-light: color-mix(in oklab, var(--nm-12-surface), #fff 14%);
    }
  }
}

.nm-12[data-theme="dark"] {
  --nm-12-surface: #262a30;
  --nm-12-dark: rgba(11,12,15,0.72);
  --nm-12-light: rgba(88,94,104,0.44);
  --nm-12-ink: #e7eaef;
  --nm-12-muted: #9aa2ad;
  --nm-12-border: #858d98;
  --nm-12-accent: #74b4d4;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-12[data-theme="dark"] {
    --nm-12-dark: color-mix(in oklab, var(--nm-12-surface), #000 55%);
    --nm-12-light: color-mix(in oklab, var(--nm-12-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-12__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-12__themebtn {
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
  background: var(--nm-12-surface);
  color: var(--nm-12-ink);
  border: 1px solid var(--nm-12-line);
  font: 600 11px/1 var(--nm-12-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-12-distance, 6px) var(--nm-12-distance, 6px) var(--nm-12-blur, 14px) var(--nm-12-dark), calc(-1 * var(--nm-12-distance, 6px)) calc(-1 * var(--nm-12-distance, 6px)) var(--nm-12-blur, 14px) var(--nm-12-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-12__themebtn:hover {
  color: var(--nm-12-ink);
}

.nm-12__themeinput:focus-visible + .nm-12__themebtn {
  outline: 2px solid var(--nm-12-ink);
  outline-offset: 3px;
}

.nm-12:has(#nm-12-theme:checked) .nm-12__themebtn {
  box-shadow: inset var(--nm-12-distance, 6px) var(--nm-12-distance, 6px) var(--nm-12-blur, 14px) var(--nm-12-dark), inset calc(-1 * var(--nm-12-distance, 6px)) calc(-1 * var(--nm-12-distance, 6px)) var(--nm-12-blur, 14px) var(--nm-12-light);
}

.nm-12__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-12:has(#nm-12-theme:checked) {
  --nm-12-surface: #262a30;
  --nm-12-dark: rgba(11,12,15,0.72);
  --nm-12-light: rgba(88,94,104,0.44);
  --nm-12-ink: #e7eaef;
  --nm-12-muted: #9aa2ad;
  --nm-12-border: #858d98;
  --nm-12-accent: #74b4d4;
}

@media (prefers-color-scheme: light) {
  .nm-12:has(#nm-12-theme:checked) {
    --nm-12-surface: #262a30;
    --nm-12-dark: rgba(11,12,15,0.72);
    --nm-12-light: rgba(88,94,104,0.44);
    --nm-12-ink: #e7eaef;
    --nm-12-muted: #9aa2ad;
    --nm-12-border: #858d98;
    --nm-12-accent: #74b4d4;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-12:has(#nm-12-theme:checked) {
    --nm-12-surface: #e5e8ea;
    --nm-12-dark: rgba(167,175,180,0.62);
    --nm-12-light: rgba(255,255,255,0.94);
    --nm-12-ink: #232830;
    --nm-12-muted: #58606a;
    --nm-12-border: #979ea7;
    --nm-12-accent: #2f6f8f;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-12__themebtn {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.nm-12');
if (root) {
  const pad = root.querySelector('.nm-12__pad');
  const out = root.querySelector('.nm-12__readout');
  const notes = [...root.querySelectorAll('.nm-12__note')];
  const sync = (s) => notes.forEach(n => n.classList.toggle('is-active', n.dataset.for === s));
  sync('full');
  root.querySelectorAll('.nm-12__strat').forEach(btn => btn.addEventListener('click', () => {
    root.querySelectorAll('.nm-12__strat').forEach(b => b.classList.toggle('is-active', b === btn));
    pad.dataset.strategy = btn.dataset.strategy;
    sync(btn.dataset.strategy);
  }));
  root.querySelectorAll('.nm-12__key').forEach(key => key.addEventListener('click', () => {
    const a = key.dataset.action, t = out.textContent;
    out.textContent = a === 'clear' ? '0' : a === 'back' ? (t.length > 1 ? t.slice(0, -1) : '0') : (t === '0' ? key.textContent : (t + key.textContent).slice(0, 12));
  }));
}
```
