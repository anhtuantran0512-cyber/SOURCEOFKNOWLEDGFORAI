---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/healthcare-appointment-confirmation-loading-animation/"
title: "Healthcare Appointment Confirmation Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Health-tech waiting states carry anxiety, so this one is calm and factual: a calendar tile scans its days, settles on the booked slot, and strokes a…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Healthcare Appointment Confirmation Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/healthcare-appointment-confirmation-loading-animation/

Health-tech waiting states carry anxiety, so this one is calm and factual: a calendar tile scans its days, settles on the booked slot, and strokes a confirmation tick while an ECG trace runs a steady 60 bpm underneath. The copy names the clinician, date and clinic — everything a patient needs to know the right appointment is being held.
## HTML
```html
<div class="la-08" data-state="loading">
  <div class="la-08__chrome">
    <button class="la-08__btn la-08__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-08__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-08__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-08__btn la-08__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-08__card" role="status" aria-live="polite" aria-label="Confirming appointment with Dr Priya Sharma, Tuesday 12 May at 9:40 AM">
    <div class="la-08__cal" aria-hidden="true">
      <span class="la-08__cal-top"><i></i><i></i></span>
      <ol class="la-08__grid">
        <li class="la-08__day" style="--i:0"></li><li class="la-08__day" style="--i:1"></li>
        <li class="la-08__day" style="--i:2"></li><li class="la-08__day" style="--i:3"></li>
        <li class="la-08__day" style="--i:4"></li><li class="la-08__day" style="--i:5"></li>
        <li class="la-08__day" style="--i:6"></li><li class="la-08__day" style="--i:7"></li>
        <li class="la-08__day la-08__day--sel" style="--i:8">12</li><li class="la-08__day" style="--i:9"></li>
        <li class="la-08__day" style="--i:10"></li><li class="la-08__day" style="--i:11"></li>
        <li class="la-08__day" style="--i:12"></li><li class="la-08__day" style="--i:13"></li>
        <li class="la-08__day" style="--i:14"></li>
      </ol>
      <svg class="la-08__seal" viewBox="0 0 48 48" focusable="false">
        <circle class="la-08__ring" cx="24" cy="24" r="15"/>
        <path class="la-08__check" d="M16.5 24.6 21.6 29.8 32 18.8"/>
      </svg>
    </div>

    <div class="la-08__copy">
      <p class="la-08__label">
        <span class="la-08__load">Confirming appointment</span>
        <span class="la-08__ready">Appointment confirmed</span>
      </p>
      <p class="la-08__meta">Dr Priya Sharma <span aria-hidden="true">·</span> Tue 12 May, 9:40 AM</p>
      <p class="la-08__clinic">Bayview Family Health <span aria-hidden="true">·</span> Suite 204</p>
    </div>

    <div class="la-08__vitals" aria-hidden="true">
      <svg class="la-08__ecg-wrap" viewBox="0 0 240 40" preserveAspectRatio="none" focusable="false">
        <path class="la-08__base" d="M0 24h240"/>
        <path class="la-08__ecg" d="M0 24h44l6-3 5 10 6-22 6 15 5-3h40l6-3 5 10 6-22 6 15 5-3h95"/>
      </svg>
      <span class="la-08__bpm">72 bpm</span>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-08-glow {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

.la-08 {
  --bg: #eef6f5;
  --surface: #ffffff;
  --ink: #0d1a1c;
  --muted: #5c7078;
  --line: #dde9e8;
  --acc: #0d9488;
  --acc-2: #e11d48;
  --ok: #0d9488;
  --ring-c: #0d9488;
  --shadow: rgba(13,26,28,.14);
  --dur: 3.6s;
  --bpm-dur: 1s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 70% at 50% -10%, color-mix(in oklab,var(--acc) 16%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-08,
.la-08 *,
.la-08 *::before,
.la-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-08 {
    --acc: oklch(58% .11 190);
    --acc-2: oklch(60% .21 15);
  }
}

.la-08__card {
  position: relative;
  inline-size: min(23.5rem,100%);
  padding: 1.9rem 1.5rem 1.4rem;
  display: grid;
  justify-items: center;
  gap: 1.15rem;
  text-align: center;
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -40px var(--shadow);
}

.la-08__cal {
  position: relative;
  inline-size: 7.2rem;
  padding: .55rem;
  border-radius: 1rem;
  background: color-mix(in oklab,var(--acc) 8%,var(--surface));
  border: 1px solid var(--line);
  display: grid;
  gap: .45rem;
  box-shadow: 0 0 0 var(--la-08-glow, 0px) color-mix(in oklab,var(--acc) 22%,transparent);
  animation: la-08-glow var(--dur) ease-in-out infinite;
}

@keyframes la-08-glow {
  0%,
    60% {
    --la-08-glow: 0px;
  }

  78% {
    --la-08-glow: 8px;
  }

  100% {
    --la-08-glow: 0px;
  }
}

.la-08__cal-top {
  display: flex;
  justify-content: center;
  gap: 1.6rem;
}

.la-08__cal-top i {
  inline-size: .32rem;
  block-size: .55rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 35%,transparent);
}

.la-08__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: .24rem;
}

.la-08__day {
  aspect-ratio: 1;
  border-radius: .35rem;
  background: color-mix(in oklab,var(--ink) 7%,transparent);
  display: grid;
  place-items: center;
  font-size: .55rem;
  font-weight: 600;
  color: transparent;
  animation: la-08-scan var(--dur) linear infinite;
  animation-delay: calc(var(--i) * .07s);
}

@keyframes la-08-scan {
  0%,
    3% {
    background: color-mix(in oklab,var(--acc) 45%,transparent);
  }

  10%,
    100% {
    background: color-mix(in oklab,var(--ink) 7%,transparent);
  }
}

.la-08__day--sel {
  color: #fff;
  animation: la-08-lock var(--dur) ease-out infinite;
}

@keyframes la-08-lock {
  0%,
    45% {
    background: color-mix(in oklab,var(--ink) 7%,transparent);
    color: transparent;
    scale: 1;
  }

  56% {
    background: var(--acc);
    color: #fff;
    scale: 1.18;
  }

  70%,
    100% {
    background: var(--acc);
    color: #fff;
    scale: 1;
  }
}

.la-08__seal {
  position: absolute;
  inset-block-end: -.9rem;
  inset-inline-end: -.9rem;
  inline-size: 2.6rem;
  block-size: 2.6rem;
  fill: none;
  stroke-width: 3.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  background: var(--surface);
  border-radius: 999px;
  padding: .1rem;
}

.la-08__ring {
  stroke: var(--ok);
  stroke-dasharray: 95;
  stroke-dashoffset: 95;
  animation: la-08-draw var(--dur) ease-in-out infinite;
}

.la-08__check {
  stroke: var(--ok);
  stroke-dasharray: 22;
  stroke-dashoffset: 22;
  animation: la-08-draw var(--dur) ease-in-out infinite;
  animation-delay: .4s;
}

@keyframes la-08-draw {
  0%,
    62% {
    stroke-dashoffset: var(--dash, 95);
  }

  84%,
    96% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: var(--dash, 95);
  }
}

.la-08__ring {
  --dash: 95;
}

.la-08__check {
  --dash: 22;
}

.la-08__copy {
  display: grid;
  gap: .22rem;
}

.la-08__label {
  margin: 0;
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.la-08__ready {
  display: none;
}

.la-08__meta {
  margin: 0;
  font-size: .84rem;
  color: var(--ink);
}

.la-08__clinic {
  margin: 0;
  font-size: .76rem;
  color: var(--muted);
}

.la-08__vitals {
  inline-size: 100%;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: .6rem;
  padding: .5rem .7rem;
  border-radius: .8rem;
  background: color-mix(in oklab,var(--acc) 7%,transparent);
}

.la-08__ecg-wrap {
  inline-size: 100%;
  block-size: 2.1rem;
  fill: none;
}

.la-08__base {
  stroke: color-mix(in oklab,var(--ink) 12%,transparent);
  stroke-width: 1;
}

.la-08__ecg {
  stroke: var(--acc-2);
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 40 300;
  stroke-dashoffset: 340;
  animation: la-08-beat var(--bpm-dur) linear infinite;
}

@keyframes la-08-beat {
  to {
    stroke-dashoffset: 0;
  }
}

.la-08__bpm {
  font-family: var(--mono);
  font-size: .66rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-08.is-ready .la-08__day,
.la-08.is-ready .la-08__cal,
.la-08.is-ready .la-08__ring,
.la-08.is-ready .la-08__check {
  animation: none;
}

.la-08.is-ready .la-08__day--sel {
  background: var(--acc);
  color: #fff;
}

.la-08.is-ready .la-08__ring,
.la-08.is-ready .la-08__check {
  stroke-dashoffset: 0;
}

.la-08.is-ready .la-08__load {
  display: none;
}

.la-08.is-ready .la-08__ready {
  display: inline;
}

.la-08.is-ready .la-08__cal {
  box-shadow: 0 0 0 6px color-mix(in oklab,var(--acc) 18%,transparent);
}

.la-08__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-08__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 16%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 72%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-08__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-08__btn:focus-visible {
  outline: 2px solid var(--ring-c);
  outline-offset: 3px;
}

.la-08__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-08__sun {
  display: none;
}

.la-08__theme[aria-pressed="true"] .la-08__sun {
  display: block;
}

.la-08__theme[aria-pressed="true"] .la-08__moon {
  display: none;
}

.la-08__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-08:not([data-theme="light"]) {
    --bg: #050d0f;
    --surface: #101a1d;
    --ink: #e9f4f4;
    --muted: #8ba3a9;
    --line: #1e2b2f;
    --acc: #2dd4bf;
    --acc-2: #fb7185;
    --ok: #2dd4bf;
    --ring-c: #2dd4bf;
    --shadow: rgba(0,0,0,.7);
  }

  .la-08:not([data-theme="light"]) .la-08__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-08:not([data-theme="light"]) .la-08__done[aria-pressed="true"] {
    color: #04201d;
  }
}

.la-08[data-theme="dark"] {
  --bg: #050d0f;
  --surface: #101a1d;
  --ink: #e9f4f4;
  --muted: #8ba3a9;
  --line: #1e2b2f;
  --acc: #2dd4bf;
  --acc-2: #fb7185;
  --ok: #2dd4bf;
  --ring-c: #2dd4bf;
  --shadow: rgba(0,0,0,.7);
}

.la-08[data-theme="dark"] .la-08__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-08[data-theme="dark"] .la-08__done[aria-pressed="true"] {
  color: #04201d;
}

@media (prefers-reduced-motion: reduce) {
  .la-08 * {
    animation: none !important;
    transition: none !important;
  }

  .la-08__day--sel {
    background: var(--acc);
    color: #fff;
  }

  .la-08__ring,
    .la-08__check {
    stroke-dashoffset: 0;
  }

  .la-08__ecg {
    stroke-dasharray: none;
    stroke-dashoffset: 0;
  }
}

@media (forced-colors: active) {
  .la-08__card,
    .la-08__cal {
    border: 1px solid CanvasText;
  }

  .la-08__day--sel {
    background: Highlight;
  }

  .la-08__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-08');
  if (!root) return;
  const theme = root.querySelector('.la-08__theme');
  const done = root.querySelector('.la-08__done');
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
    region.setAttribute('aria-label', ready
      ? 'Appointment confirmed with Dr Priya Sharma, Tuesday 12 May at 9:40 AM'
      : 'Confirming appointment with Dr Priya Sharma, Tuesday 12 May at 9:40 AM');
  });
  sync();
})();
```
