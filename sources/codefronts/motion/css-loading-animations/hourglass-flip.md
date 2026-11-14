---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/hourglass-flip/"
title: "Hourglass Flip Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "The universal \"this will take a moment\" symbol, executed properly: sand actually drains from the top bulb into the bottom one through a falling stream, and…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hourglass Flip Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/hourglass-flip/

The universal "this will take a moment" symbol, executed properly: sand actually drains from the top bulb into the bottom one through a falling stream, and the whole glass flips at the end of every cycle so the loop never resets visibly. A countdown readout ticks down in pure CSS beside it.
## HTML
```html
<div class="la-20" data-state="loading">
  <div class="la-20__chrome">
    <button class="la-20__btn la-20__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-20__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-20__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-20__btn la-20__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-20__card" role="status" aria-live="polite" aria-label="Rendering export, about 12 seconds remaining">
    <div class="la-20__glass" aria-hidden="true">
      <span class="la-20__cap"></span>
      <span class="la-20__bulbs">
        <i class="la-20__bulb la-20__bulb--top"></i>
        <i class="la-20__stream"></i>
        <i class="la-20__bulb la-20__bulb--bot"></i>
      </span>
      <span class="la-20__cap la-20__cap--b"></span>
    </div>

    <div class="la-20__copy">
      <p class="la-20__label">
        <span class="la-20__load">Rendering export</span>
        <span class="la-20__ready">Export ready</span>
      </p>
      <p class="la-20__meta">
        <span class="la-20__load">quarterly-review.mp4 <span aria-hidden="true">·</span> <span class="la-20__secs"></span> left</span>
        <span class="la-20__ready">quarterly-review.mp4 <span aria-hidden="true">·</span> 148 MB</span>
      </p>
    </div>

    <div class="la-20__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="58" aria-valuetext="58 percent rendered">
      <span class="la-20__fill"></span>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-20-top {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 100%;
}

@property --la-20-bot {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

@property --la-20-s {
  syntax: '<integer>';
  inherits: false;
  initial-value: 12;
}

.la-20 {
  --bg: #0c0e14;
  --surface: #151922;
  --ink: #f3f5fa;
  --muted: #98a1b3;
  --line: #242b38;
  --sand: #ffb454;
  --glass: rgba(255,255,255,.1);
  --frame: #8a93a6;
  --acc: #ffb454;
  --ok: #3ad68f;
  --ring: #ffb454;
  --dur: 6s;
  --h: 6.5rem;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(85% 60% at 50% 0%, #1b2029, var(--bg));
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-20,
.la-20 *,
.la-20 *::before,
.la-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-20 {
    --sand: oklch(80% .15 70);
    --acc: oklch(80% .15 70);
    --ok: oklch(78% .16 160);
  }
}

.la-20__card {
  position: relative;
  inline-size: min(22rem,100%);
  padding: 1.9rem 1.5rem 1.4rem;
  display: grid;
  justify-items: center;
  gap: 1.15rem;
  text-align: center;
  border-radius: 1.5rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--surface) 92%,var(--sand)), var(--surface));
  border: 1px solid var(--line);
  box-shadow: 0 40px 80px -50px #000, 0 0 0 1px rgba(255,255,255,.03) inset;
}

.la-20__glass {
  position: relative;
  inline-size: calc(var(--h) * .72);
  block-size: var(--h);
  display: grid;
  grid-template-rows: auto 1fr auto;
  justify-items: center;
  animation: la-20-flip var(--dur) cubic-bezier(.6,0,.4,1) infinite;
  filter: drop-shadow(0 10px 18px rgba(0,0,0,.45));
}

@keyframes la-20-flip {
  0%,
    82% {
    rotate: 0deg;
  }

  95%,
    100% {
    rotate: 180deg;
  }
}

.la-20__cap {
  inline-size: 100%;
  block-size: .34rem;
  border-radius: .2rem;
  background: linear-gradient(180deg,var(--frame),color-mix(in oklab,var(--frame) 60%,black));
}

.la-20__bulbs {
  position: relative;
  inline-size: 100%;
  block-size: 100%;
  display: grid;
  grid-template-rows: 1fr 1fr;
}

.la-20__bulb {
  inline-size: 100%;
  block-size: 100%;
  background: var(--glass);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.14);
}

.la-20__bulb--top {
  clip-path: polygon(0 0, 100% 0, 54% 100%, 46% 100%);
  background: linear-gradient(to top, transparent 0 calc(100% - var(--la-20-top, 46%)), var(--sand) calc(100% - var(--la-20-top, 46%))), var(--glass);
  animation: la-20-drain var(--dur) linear infinite;
}

.la-20__bulb--bot {
  clip-path: polygon(46% 0, 54% 0, 100% 100%, 0 100%);
  background: linear-gradient(to top, var(--sand) 0 var(--la-20-bot, 54%), transparent var(--la-20-bot, 54%)), var(--glass);
  animation: la-20-heap var(--dur) linear infinite;
}

@keyframes la-20-drain {
  0% {
    --la-20-top: 96%;
  }

  78%,
    100% {
    --la-20-top: 2%;
  }
}

@keyframes la-20-heap {
  0% {
    --la-20-bot: 4%;
  }

  78%,
    100% {
    --la-20-bot: 92%;
  }
}

.la-20__stream {
  position: absolute;
  inset-block: 32% 34%;
  inset-inline-start: calc(50% - 1.5px);
  inline-size: 3px;
  background: repeating-linear-gradient(180deg, var(--sand) 0 2px, transparent 2px 5px);
  animation: la-20-fall .42s linear infinite, la-20-tap var(--dur) linear infinite;
}

@keyframes la-20-fall {
  to {
    background-position: 0 5px;
  }
}

@keyframes la-20-tap {
  0%,
    74% {
    opacity: 1;
  }

  82%,
    100% {
    opacity: 0;
  }
}

.la-20__copy {
  display: grid;
  gap: .24rem;
}

.la-20__label {
  margin: 0;
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-20__ready {
  display: none;
}

.la-20__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-20__secs {
  counter-reset: la-20-s var(--la-20-s, 12);
  animation: la-20-count var(--dur) steps(12, jump-none) infinite;
}

.la-20__secs::after {
  content: counter(la-20-s) "s";
}

@keyframes la-20-count {
  from {
    --la-20-s: 12;
  }

  to {
    --la-20-s: 1;
  }
}

.la-20__track {
  inline-size: 100%;
  block-size: .4rem;
  border-radius: 999px;
  background: rgba(255,255,255,.09);
  overflow: hidden;
}

.la-20__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg,color-mix(in oklab,var(--sand) 60%,white),var(--sand));
  animation: la-20-bar var(--dur) linear infinite;
}

@keyframes la-20-bar {
  from {
    inline-size: 8%;
  }

  to {
    inline-size: 100%;
  }
}

.la-20.is-ready .la-20__glass,
.la-20.is-ready .la-20__bulb,
.la-20.is-ready .la-20__stream,
.la-20.is-ready .la-20__fill,
.la-20.is-ready .la-20__secs {
  animation: none;
}

.la-20.is-ready .la-20__glass {
  rotate: 0deg;
}

.la-20.is-ready .la-20__bulb--top {
  --la-20-top: 0%;
}

.la-20.is-ready .la-20__bulb--bot {
  --la-20-bot: 94%;
}

.la-20.is-ready .la-20__stream {
  opacity: 0;
}

.la-20.is-ready .la-20__fill {
  inline-size: 100%;
  background: var(--ok);
}

.la-20.is-ready .la-20__load {
  display: none;
}

.la-20.is-ready .la-20__ready {
  display: inline;
}

.la-20__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-20__btn {
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

.la-20__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-20__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-20__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-20__sun {
  display: none;
}

.la-20__theme[aria-pressed="true"] .la-20__sun {
  display: block;
}

.la-20__theme[aria-pressed="true"] .la-20__moon {
  display: none;
}

.la-20__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #04231a;
}

@media (prefers-color-scheme: light) {
  .la-20:not([data-theme="dark"]) {
    --bg: #f2f3f7;
    --surface: #ffffff;
    --ink: #0d111a;
    --muted: #5f6a7c;
    --line: #e2e6ee;
    --glass: rgba(13,17,26,.06);
    --frame: #4a5262;
    --sand: #e08a1e;
    --acc: #e08a1e;
    --ok: #0f9d63;
    --ring: #e08a1e;
  }

  .la-20:not([data-theme="dark"]) .la-20__card {
    box-shadow: 0 1px 0 #fff inset, 0 34px 60px -42px rgba(13,17,26,.24);
  }

  .la-20:not([data-theme="dark"]) .la-20__track {
    background: rgba(13,17,26,.08);
  }

  .la-20:not([data-theme="dark"]) .la-20__done[aria-pressed="true"] {
    color: #fff;
  }
}

.la-20[data-theme="light"] {
  --bg: #f2f3f7;
  --surface: #ffffff;
  --ink: #0d111a;
  --muted: #5f6a7c;
  --line: #e2e6ee;
  --glass: rgba(13,17,26,.06);
  --frame: #4a5262;
  --sand: #e08a1e;
  --acc: #e08a1e;
  --ok: #0f9d63;
  --ring: #e08a1e;
}

.la-20[data-theme="light"] .la-20__card {
  box-shadow: 0 1px 0 #fff inset, 0 34px 60px -42px rgba(13,17,26,.24);
}

.la-20[data-theme="light"] .la-20__track {
  background: rgba(13,17,26,.08);
}

.la-20[data-theme="light"] .la-20__done[aria-pressed="true"] {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .la-20 * {
    animation: none !important;
    transition: none !important;
  }

  .la-20__bulb--top {
    --la-20-top: 46%;
  }

  .la-20__bulb--bot {
    --la-20-bot: 54%;
  }

  .la-20__fill {
    inline-size: 58%;
  }
}

@media (forced-colors: active) {
  .la-20__card {
    border: 1px solid CanvasText;
  }

  .la-20__bulb {
    background: Canvas;
    border: 1px solid CanvasText;
  }

  .la-20__fill {
    background: Highlight;
  }

  .la-20__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-20');
  if (!root) return;
  const theme = root.querySelector('.la-20__theme');
  const done = root.querySelector('.la-20__done');
  const bar = root.querySelector('[role="progressbar"]');
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
    bar.setAttribute('aria-valuenow', ready ? 100 : 58);
    bar.setAttribute('aria-valuetext', ready ? 'Export ready' : '58 percent rendered');
    region.setAttribute('aria-label', ready ? 'Export ready, quarterly-review.mp4' : 'Rendering export, about 12 seconds remaining');
  });
  sync();
})();
```
