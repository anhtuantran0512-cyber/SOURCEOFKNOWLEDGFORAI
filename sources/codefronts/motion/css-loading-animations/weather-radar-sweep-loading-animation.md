---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/weather-radar-sweep-loading-animation/"
title: "Weather Radar Sweep Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "A doppler-style radar scope: a conic sweep rotates over concentric range rings, precipitation cells fade up as the beam passes them, and range/coordinate…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Weather Radar Sweep Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/weather-radar-sweep-loading-animation/

A doppler-style radar scope: a conic sweep rotates over concentric range rings, precipitation cells fade up as the beam passes them, and range/coordinate readouts frame it like a real weather console. It is the most "instrument-panel" loader in the set and the best fit for any geospatial or scanning wait state.
## HTML
```html
<div class="la-13" data-state="loading">
  <div class="la-13__chrome">
    <button class="la-13__btn la-13__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-13__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-13__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-13__btn la-13__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-13__card" role="status" aria-live="polite" aria-label="Scanning weather radar for San Francisco">
    <div class="la-13__scope" aria-hidden="true">
      <span class="la-13__cell" style="--a:38; --r:1.9rem; --s:2.6rem; --c:var(--p1)"></span>
      <span class="la-13__cell" style="--a:104; --r:3.3rem; --s:3.4rem; --c:var(--p2)"></span>
      <span class="la-13__cell" style="--a:150; --r:2.4rem; --s:1.9rem; --c:var(--p3)"></span>
      <span class="la-13__cell" style="--a:228; --r:3.7rem; --s:2.2rem; --c:var(--p1)"></span>
      <span class="la-13__cell" style="--a:300; --r:2.7rem; --s:2.9rem; --c:var(--p2)"></span>
      <span class="la-13__beam"></span>
      <span class="la-13__hub"></span>
    </div>

    <div class="la-13__copy">
      <p class="la-13__label">
        <span class="la-13__load">Scanning radar</span>
        <span class="la-13__ready">Radar up to date</span>
      </p>
      <p class="la-13__meta">San Francisco, CA <span aria-hidden="true">·</span> 37.77° N, 122.42° W</p>
    </div>

    <dl class="la-13__read">
      <div><dt>Range</dt><dd>120 km</dd></div>
      <div><dt>Tilt</dt><dd>0.5°</dd></div>
      <div><dt>Sweep</dt><dd class="la-13__sweepv">3.2 s</dd></div>
    </dl>

    <p class="la-13__legend">
      <span class="la-13__item"><i class="la-13__sw la-13__sw--1" aria-hidden="true"></i>Light</span>
      <span class="la-13__item"><i class="la-13__sw la-13__sw--2" aria-hidden="true"></i>Moderate</span>
      <span class="la-13__item"><i class="la-13__sw la-13__sw--3" aria-hidden="true"></i>Heavy</span>
    </p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-13-deg {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.la-13 {
  --bg: #03080c;
  --surface: #081218;
  --ink: #e8f6f4;
  --muted: #7fa3a5;
  --line: #14262e;
  --grid: rgba(120,220,200,.16);
  --scope-1: #0a1b20;
  --scope-2: #040d11;
  --edge: #ffffff;
  --cell-blend: screen;
  --cell-blur: 1px;
  --acc: #37f0c2;
  --p1: #2ee88a;
  --p2: #ffc247;
  --p3: #ff5470;
  --ok: #37f0c2;
  --ring: #37f0c2;
  --dur: 3.2s;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(80% 60% at 50% 0%, #0b1c22, var(--bg));
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-13,
.la-13 *,
.la-13 *::before,
.la-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-13 {
    --acc: oklch(85% .17 175);
    --p1: oklch(78% .19 150);
    --p2: oklch(84% .16 85);
    --p3: oklch(68% .22 15);
  }
}

.la-13__card {
  position: relative;
  inline-size: min(23rem,100%);
  padding: 1.6rem 1.4rem 1.3rem;
  display: grid;
  justify-items: center;
  gap: 1rem;
  text-align: center;
  border-radius: 1.4rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--surface) 88%,var(--acc)), var(--surface));
  border: 1px solid var(--line);
  box-shadow: 0 40px 80px -50px #000, 0 0 0 1px rgba(255,255,255,.03) inset;
}

.la-13__scope {
  position: relative;
  inline-size: 11rem;
  block-size: 11rem;
  border-radius: 999px;
  overflow: hidden;
  isolation: isolate;
  background: repeating-radial-gradient(circle, transparent 0 21%, var(--grid) 21% calc(21% + 1px)), linear-gradient(var(--grid) 0 0) 50%/1px 100% no-repeat, linear-gradient(var(--grid) 0 0) 50%/100% 1px no-repeat, radial-gradient(circle, var(--scope-1), var(--scope-2));
  border: 1px solid color-mix(in oklab,var(--acc) 30%,transparent);
  box-shadow: 0 0 0 6px color-mix(in oklab,var(--acc) 6%,transparent), inset 0 0 30px rgba(0,0,0,.7);
}

.la-13__beam {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: conic-gradient(from var(--la-13-deg, 40deg),
      color-mix(in oklab,var(--acc) 65%,transparent) 0deg,
      color-mix(in oklab,var(--acc) 22%,transparent) 18deg,
      transparent 46deg);
  animation: la-13-sweep var(--dur) linear infinite;
}

@keyframes la-13-sweep {
  from {
    --la-13-deg: 0deg;
  }

  to {
    --la-13-deg: 360deg;
  }
}

.la-13__beam::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: conic-gradient(from var(--la-13-deg, 40deg), color-mix(in oklab,var(--acc) 90%,var(--edge)) 0deg 1.6deg, transparent 1.6deg);
}

.la-13__hub {
  position: absolute;
  inset: 0;
  margin: auto;
  inline-size: .42rem;
  block-size: .42rem;
  border-radius: 999px;
  background: var(--acc);
  box-shadow: 0 0 8px var(--acc);
}

.la-13__cell {
  position: absolute;
  inset: 0;
  margin: auto;
  inline-size: var(--s);
  block-size: var(--s);
  border-radius: 48% 52% 44% 56%;
  background: radial-gradient(closest-side, var(--c), color-mix(in oklab,var(--c) 25%,transparent) 70%, transparent);
  translate: calc(cos(var(--a) * 1deg) * var(--r)) calc(sin(var(--a) * 1deg) * var(--r));
  mix-blend-mode: var(--cell-blend);
  opacity: .12;
  filter: blur(var(--cell-blur));
  animation: la-13-ping var(--dur) linear infinite;
  animation-delay: calc(var(--a) / 360 * var(--dur) * -1 + var(--dur));
}

@keyframes la-13-ping {
  0%,
    5% {
    opacity: .95;
  }

  55% {
    opacity: .45;
  }

  100% {
    opacity: .12;
  }
}

.la-13__copy {
  display: grid;
  gap: .22rem;
}

.la-13__label {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-13__ready {
  display: none;
}

.la-13__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-13__read {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
  inline-size: 100%;
}

.la-13__read div {
  padding: .45rem .3rem;
  border-radius: .55rem;
  background: color-mix(in oklab,var(--acc) 7%,transparent);
  border: 1px solid var(--line);
}

.la-13__read dt {
  margin: 0 0 .1rem;
  font-family: var(--mono);
  font-size: .56rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.la-13__read dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .78rem;
  font-variant-numeric: tabular-nums;
}

.la-13__legend {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .2rem .7rem;
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .06em;
  color: var(--muted);
  flex-wrap: wrap;
  justify-content: center;
}

.la-13__item {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  white-space: nowrap;
}

.la-13__sw {
  inline-size: .55rem;
  block-size: .55rem;
  border-radius: .15rem;
  flex: none;
}

.la-13__sw--1 {
  background: var(--p1);
}

.la-13__sw--2 {
  background: var(--p2);
}

.la-13__sw--3 {
  background: var(--p3);
}

.la-13.is-ready .la-13__beam,
.la-13.is-ready .la-13__cell {
  animation: none;
}

.la-13.is-ready .la-13__beam {
  opacity: .12;
}

.la-13.is-ready .la-13__cell {
  opacity: .85;
}

.la-13.is-ready .la-13__load {
  display: none;
}

.la-13.is-ready .la-13__ready {
  display: inline;
}

.la-13.is-ready .la-13__sweepv {
  color: var(--ok);
}

.la-13__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-13__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 22%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 78%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-13__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-13__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-13__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-13__sun {
  display: none;
}

.la-13__theme[aria-pressed="true"] .la-13__sun {
  display: block;
}

.la-13__theme[aria-pressed="true"] .la-13__moon {
  display: none;
}

.la-13__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #02231c;
}

@media (prefers-color-scheme: light) {
  .la-13:not([data-theme="dark"]) {
    --bg: #e9f2f0;
    --surface: #ffffff;
    --ink: #04191c;
    --muted: #4c6b6e;
    --line: #d3e3e0;
    --grid: rgba(8,72,62,.22);
    --scope-1: #f6fcfa;
    --scope-2: #d9ebe7;
    --edge: #04191c;
    --cell-blend: multiply;
    --cell-blur: 2px;
    --acc: #00795f;
    --p1: #0f7a45;
    --p2: #a86a00;
    --p3: #b81f3f;
    --ok: #00795f;
  }

  .la-13:not([data-theme="dark"]) .la-13__scope {
    box-shadow: 0 0 0 6px color-mix(in oklab,var(--acc) 8%,transparent), inset 0 0 24px color-mix(in oklab,var(--acc) 10%,transparent);
  }

  .la-13:not([data-theme="dark"]) .la-13__hub {
    box-shadow: 0 0 0 3px color-mix(in oklab,var(--acc) 22%,transparent);
  }

  .la-13:not([data-theme="dark"]) .la-13__card {
    box-shadow: 0 1px 0 #fff inset, 0 36px 64px -42px rgba(4,25,28,.24);
  }

  .la-13:not([data-theme="dark"]) .la-13__done[aria-pressed="true"] {
    color: #fff;
  }
}

.la-13[data-theme="light"] {
  --bg: #e9f2f0;
  --surface: #ffffff;
  --ink: #04191c;
  --muted: #4c6b6e;
  --line: #d3e3e0;
  --grid: rgba(8,72,62,.22);
  --scope-1: #f6fcfa;
  --scope-2: #d9ebe7;
  --edge: #04191c;
  --cell-blend: multiply;
  --cell-blur: 2px;
  --acc: #00795f;
  --p1: #0f7a45;
  --p2: #a86a00;
  --p3: #b81f3f;
  --ok: #00795f;
}

.la-13[data-theme="light"] .la-13__scope {
  box-shadow: 0 0 0 6px color-mix(in oklab,var(--acc) 8%,transparent), inset 0 0 24px color-mix(in oklab,var(--acc) 10%,transparent);
}

.la-13[data-theme="light"] .la-13__hub {
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--acc) 22%,transparent);
}

.la-13[data-theme="light"] .la-13__card {
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -42px rgba(4,25,28,.24);
}

.la-13[data-theme="light"] .la-13__done[aria-pressed="true"] {
  color: #fff;
}

@supports (color: oklch(0 0 0)) {
  /* light ramp, declared after the hex baseline so it wins */

  @media (prefers-color-scheme: light) {
    .la-13:not([data-theme="dark"]) {
      --acc: oklch(50% .12 172);
      --p1: oklch(52% .14 150);
      --p2: oklch(60% .13 72);
      --p3: oklch(52% .2 18);
    }
  }

  .la-13[data-theme="light"] {
    --acc: oklch(50% .12 172);
    --p1: oklch(52% .14 150);
    --p2: oklch(60% .13 72);
    --p3: oklch(52% .2 18);
  }
}

@media (prefers-reduced-motion: reduce) {
  .la-13 * {
    animation: none !important;
    transition: none !important;
  }

  .la-13__beam {
    --la-13-deg: 300deg;
    opacity: .5;
  }

  .la-13__cell {
    opacity: .7;
  }
}

@media (forced-colors: active) {
  .la-13__card,
    .la-13__scope {
    border: 1px solid CanvasText;
  }

  .la-13__beam {
    background: Highlight;
    opacity: .3;
  }

  .la-13__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-13');
  if (!root) return;
  const theme = root.querySelector('.la-13__theme');
  const done = root.querySelector('.la-13__done');
  const region = root.querySelector('[role="status"]');
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    region.setAttribute('aria-label', ready ? 'Radar up to date for San Francisco' : 'Scanning weather radar for San Francisco');
  });
  sync();
})();
```
