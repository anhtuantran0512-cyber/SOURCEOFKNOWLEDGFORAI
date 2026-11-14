---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/fintech-transaction-processing-shield-loader/"
title: "Fintech Transaction Processing Shield Loader"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Trust is the product in fintech, so the loader has to look like verification, not decoration."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fintech Transaction Processing Shield Loader
Source: https://codefronts.com/motion/css-loading-animations/fintech-transaction-processing-shield-loader/

Trust is the product in fintech, so the loader has to look like verification, not decoration. A shield fills with a conic sweep, a scan line passes over it, the padlock's checkmark strokes itself in, and the copy states the amount and the encryption standard. The percentage under it is a pure-CSS counter — no timer repainting text while a payment is in flight.
## HTML
```html
<div class="la-06" data-state="loading">
  <div class="la-06__chrome">
    <button class="la-06__btn la-06__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-06__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-06__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-06__btn la-06__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-06__card" role="status" aria-live="polite" aria-label="Processing payment of 47 dollars 20 cents">
    <div class="la-06__badge" aria-hidden="true">
      <span class="la-06__ring"></span>
      <span class="la-06__shield">
        <span class="la-06__sweep"></span>
        <span class="la-06__scan"></span>
      </span>
      <svg class="la-06__mark" viewBox="0 0 48 48" focusable="false">
        <path class="la-06__lock" d="M18 22v-4.5a6 6 0 0 1 12 0V22"/>
        <rect class="la-06__body" x="15" y="22" width="18" height="13" rx="3"/>
        <path class="la-06__tick" d="M19.5 28.6 23 32.2 29.5 25"/>
      </svg>
    </div>

    <div class="la-06__copy">
      <p class="la-06__label">
        <span class="la-06__load">Processing payment</span>
        <span class="la-06__ready">Payment approved</span>
      </p>
      <p class="la-06__amt">$47.20 <span class="la-06__sep" aria-hidden="true">·</span> <span class="la-06__card-no">Visa •••• 4242</span></p>
    </div>

    <div class="la-06__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="64" aria-valuetext="64 percent verified">
      <span class="la-06__fill"></span>
    </div>
    <p class="la-06__foot"><span class="la-06__pct"></span> <span aria-hidden="true">·</span> 256-bit encrypted <span aria-hidden="true">·</span> Priya Sharma</p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

@property --la-06-deg {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@property --la-06-p {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.la-06 {
  --bg: #0b0f17;
  --surface: #141a25;
  --ink: #f1f5fb;
  --muted: #93a1b5;
  --line: #232c3b;
  --acc: #2ee6a8;
  --acc-2: #3b8cff;
  --ok: #2ee6a8;
  --ring-c: #2ee6a8;
  --shadow: rgba(0,0,0,.7);
  --dur: 4.2s;
  --scan-dur: 2.1s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(80% 60% at 50% 0%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 62%), radial-gradient(70% 50% at 20% 100%, color-mix(in oklab,var(--acc-2) 18%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-06,
.la-06 *,
.la-06 *::before,
.la-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-06 {
    --acc: oklch(80% .17 165);
    --acc-2: oklch(64% .18 258);
  }
}

.la-06__card {
  position: relative;
  inline-size: min(23rem,100%);
  padding: 2rem 1.5rem 1.35rem;
  display: grid;
  justify-items: center;
  gap: 1.05rem;
  text-align: center;
  border-radius: 1.5rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--surface) 92%,var(--acc)), var(--surface));
  border: 1px solid var(--line);
  box-shadow: 0 40px 80px -50px #000, 0 0 0 1px rgba(255,255,255,.03) inset;
}

.la-06__badge {
  position: relative;
  inline-size: 6.5rem;
  block-size: 6.5rem;
  display: grid;
  place-items: center;
}

.la-06__ring {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: conic-gradient(from var(--la-06-deg, 40deg), transparent, var(--acc), transparent 62%);
  mask: radial-gradient(closest-side, transparent 82%, #000 83%);
  -webkit-mask: radial-gradient(closest-side, transparent 82%, #000 83%);
  animation: la-06-spin 2.4s linear infinite;
  opacity: .9;
}

@keyframes la-06-spin {
  from {
    --la-06-deg: 0deg;
  }

  to {
    --la-06-deg: 360deg;
  }
}

.la-06__shield {
  position: relative;
  inline-size: 4.4rem;
  block-size: 5rem;
  overflow: hidden;
  clip-path: polygon(50% 0, 100% 15%, 100% 56%, 50% 100%, 0 56%, 0 15%);
  background: color-mix(in oklab,var(--acc) 14%,transparent);
  border: 0;
}

.la-06__sweep {
  position: absolute;
  inset: -30%;
  background: conic-gradient(from var(--la-06-deg, 40deg), transparent 0deg, color-mix(in oklab,var(--acc) 55%,transparent) 90deg, transparent 200deg);
  animation: la-06-spin var(--dur) linear infinite;
}

.la-06__scan {
  position: absolute;
  inset-inline: 0;
  block-size: 38%;
  background: linear-gradient(180deg, transparent, color-mix(in oklab,var(--acc) 60%,transparent), transparent);
  animation: la-06-scan var(--scan-dur) ease-in-out infinite alternate;
}

@keyframes la-06-scan {
  from {
    translate: 0 -40%;
  }

  to {
    translate: 0 175%;
  }
}

.la-06__mark {
  position: absolute;
  inline-size: 2.6rem;
  block-size: 2.6rem;
  fill: none;
  stroke: var(--ink);
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-06__body {
  fill: color-mix(in oklab,var(--surface) 70%,transparent);
}

.la-06__tick {
  stroke: var(--ok);
  stroke-dasharray: 16;
  stroke-dashoffset: 16;
  animation: la-06-tick var(--dur) ease-out infinite;
}

@keyframes la-06-tick {
  0%,
    60% {
    stroke-dashoffset: 16;
  }

  80%,
    94% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: 16;
  }
}

.la-06__copy {
  display: grid;
  gap: .3rem;
}

.la-06__label {
  margin: 0;
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-06__ready {
  display: none;
}

.la-06__amt {
  margin: 0;
  font-family: var(--mono);
  font-size: .85rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-06__card-no {
  color: color-mix(in oklab,var(--ink) 80%,transparent);
}

.la-06__track {
  inline-size: 100%;
  block-size: .4rem;
  border-radius: 999px;
  background: rgba(255,255,255,.08);
  overflow: hidden;
}

.la-06__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  inline-size: calc(var(--la-06-p, 64) * 1%);
  background: linear-gradient(90deg, var(--acc-2), var(--acc));
  animation: la-06-count var(--dur) linear infinite;
}

.la-06__foot {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .02em;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  counter-reset: la-06-p var(--la-06-p, 64);
  animation: la-06-count var(--dur) linear infinite;
}

.la-06__pct::after {
  content: counter(la-06-p) "%";
}

@keyframes la-06-count {
  from {
    --la-06-p: 0;
  }

  to {
    --la-06-p: 100;
  }
}

.la-06.is-ready .la-06__ring,
.la-06.is-ready .la-06__sweep,
.la-06.is-ready .la-06__scan {
  animation: none;
}

.la-06.is-ready .la-06__scan {
  opacity: 0;
}

.la-06.is-ready .la-06__shield {
  background: color-mix(in oklab,var(--ok) 26%,transparent);
}

.la-06.is-ready .la-06__tick {
  animation: none;
  stroke-dashoffset: 0;
}

.la-06.is-ready .la-06__load {
  display: none;
}

.la-06.is-ready .la-06__ready {
  display: inline;
}

.la-06.is-ready .la-06__fill {
  animation: none;
  inline-size: 100%;
}

.la-06.is-ready .la-06__foot {
  animation: none;
  --la-06-p: 100;
}

.la-06__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-06__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 20%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 78%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-06__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-06__btn:focus-visible {
  outline: 2px solid var(--ring-c);
  outline-offset: 3px;
}

.la-06__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-06__sun {
  display: none;
}

.la-06__theme[aria-pressed="true"] .la-06__sun {
  display: block;
}

.la-06__theme[aria-pressed="true"] .la-06__moon {
  display: none;
}

.la-06__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #04140d;
}

@media (prefers-color-scheme: light) {
  .la-06:not([data-theme="dark"]) {
    --bg: #eff3f8;
    --surface: #ffffff;
    --ink: #08111c;
    --muted: #5b6879;
    --line: #dfe5ee;
    --acc: #00a37a;
    --acc-2: #2563eb;
    --ok: #00a37a;
    --shadow: rgba(8,17,28,.16);
  }

  .la-06:not([data-theme="dark"]) .la-06__card {
    box-shadow: 0 1px 0 #fff inset, 0 36px 64px -42px var(--shadow);
  }

  .la-06:not([data-theme="dark"]) .la-06__track {
    background: rgba(8,17,28,.09);
  }

  .la-06:not([data-theme="dark"]) .la-06__done[aria-pressed="true"] {
    color: #fff;
  }
}

.la-06[data-theme="light"] {
  --bg: #eff3f8;
  --surface: #ffffff;
  --ink: #08111c;
  --muted: #5b6879;
  --line: #dfe5ee;
  --acc: #00a37a;
  --acc-2: #2563eb;
  --ok: #00a37a;
  --shadow: rgba(8,17,28,.16);
}

.la-06[data-theme="light"] .la-06__card {
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -42px var(--shadow);
}

.la-06[data-theme="light"] .la-06__track {
  background: rgba(8,17,28,.09);
}

.la-06[data-theme="light"] .la-06__done[aria-pressed="true"] {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .la-06 * {
    animation: none !important;
    transition: none !important;
  }

  .la-06__ring {
    --la-06-deg: 120deg;
    opacity: .7;
  }

  .la-06__scan {
    opacity: 0;
  }

  .la-06__fill {
    inline-size: 64%;
  }
}

@media (forced-colors: active) {
  .la-06__card {
    border: 1px solid CanvasText;
  }

  .la-06__fill {
    background: Highlight;
  }

  .la-06__shield {
    background: Canvas;
    border: 1px solid CanvasText;
  }

  .la-06__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-06');
  if (!root) return;
  const theme = root.querySelector('.la-06__theme');
  const done = root.querySelector('.la-06__done');
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
    const ready = root.classList.toggle('is-ready');        // payment_intent.succeeded
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    bar.setAttribute('aria-valuenow', ready ? 100 : 64);
    bar.setAttribute('aria-valuetext', ready ? 'Payment approved' : '64 percent verified');
    region.setAttribute('aria-label', ready ? 'Payment of 47 dollars 20 cents approved' : 'Processing payment of 47 dollars 20 cents');
  });
  sync();
})();
```
