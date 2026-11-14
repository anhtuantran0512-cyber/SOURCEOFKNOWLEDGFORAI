---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/e-commerce-checkout-cart-loading-animation/"
title: "E-Commerce Checkout Cart Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "The waiting state that costs the most money on the internet."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Checkout Cart Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/e-commerce-checkout-cart-loading-animation/

The waiting state that costs the most money on the internet. Instead of a bare spinner, this one narrates the three things actually happening after a shopper hits Pay — processing payment → confirming order → generating receipt — while product tiles drop into an animated cart and a determinate bar fills. The percentage readout is pure CSS: an animated @property integer piped into counter(), so there is no setInterval repainting text every frame.
## HTML
```html
<div class="la-01" data-state="loading">
  <div class="la-01__chrome">
    <button class="la-01__btn la-01__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-01__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-01__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-01__btn la-01__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-01__card" role="status" aria-live="polite" aria-label="Placing your order">
    <div class="la-01__stage" aria-hidden="true">
      <span class="la-01__item la-01__item--a"></span>
      <span class="la-01__item la-01__item--b"></span>
      <span class="la-01__item la-01__item--c"></span>
      <svg class="la-01__cart" viewBox="0 0 64 64" focusable="false">
        <path d="M5 11h8l7.6 25.4A5 5 0 0 0 25.4 40h21.9a5 5 0 0 0 4.8-3.5L58 19H16.5"/>
        <circle cx="27" cy="52" r="4.2"/><circle cx="47" cy="52" r="4.2"/>
      </svg>
      <svg class="la-01__seal" viewBox="0 0 64 64" focusable="false">
        <circle cx="32" cy="32" r="21"/><path class="la-01__tick" d="M22 33 29.6 40.4 43 24.6"/>
      </svg>
    </div>

    <div class="la-01__copy">
      <p class="la-01__label">
        <span class="la-01__load">Processing payment</span>
        <span class="la-01__ready">Order confirmed</span>
      </p>
      <p class="la-01__meta"><span class="la-01__amt">$47.20</span> <span aria-hidden="true">·</span> Order #CF-48210</p>
    </div>

    <ol class="la-01__steps">
      <li class="la-01__step">Payment</li>
      <li class="la-01__step">Order</li>
      <li class="la-01__step">Receipt</li>
    </ol>

    <div class="la-01__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="68" aria-valuetext="68 percent complete">
      <span class="la-01__fill"></span>
    </div>
    <p class="la-01__pct"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

@property --la-01-p {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --la-01-spin {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.la-01 {
  --bg: #f2f3f7;
  --surface: #ffffff;
  --ink: #0b0e14;
  --muted: #646e7e;
  --line: #e4e7ee;
  --acc: #5b3df5;
  --acc-ink: #ffffff;
  --ok: #0f9d63;
  --ring: #5b3df5;
  --shadow: rgba(11,14,20,.16);
  --dur: 5.4s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(120% 80% at 50% -20%, color-mix(in oklab,var(--acc) 16%,transparent), transparent 60%), radial-gradient(80% 60% at 100% 100%, color-mix(in oklab,var(--ok) 10%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-01,
.la-01 *,
.la-01 *::before,
.la-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-01 {
    --acc: oklch(54% .25 285);
    --ok: oklch(62% .16 158);
    --ink: oklch(15% .02 265);
    --muted: oklch(52% .015 265);
  }
}

.la-01__card {
  position: relative;
  inline-size: min(24rem,100%);
  padding: 2.1rem 1.6rem 1.5rem;
  display: grid;
  justify-items: center;
  gap: 1.15rem;
  border-radius: 1.75rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--surface) 94%,var(--acc)), var(--surface));
  border: 1px solid var(--line);
  container-type: inline-size;
  box-shadow: 0 1px 0 color-mix(in oklab,white 80%,transparent) inset, 0 40px 70px -40px var(--shadow), 0 2px 8px -4px var(--shadow);
}

@supports (corner-shape: squircle) {
  .la-01__card {
    corner-shape: squircle;
    border-radius: 2.2rem;
  }
}

.la-01__stage {
  position: relative;
  inline-size: 7.5rem;
  block-size: 7.5rem;
  display: grid;
  place-items: center;
}

.la-01__stage::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: conic-gradient(from var(--la-01-spin), color-mix(in oklab,var(--acc) 70%,transparent), transparent 42%, color-mix(in oklab,var(--acc) 70%,transparent));
  mask: radial-gradient(closest-side, transparent 76%, black 77%);
  animation: la-01-spin 3.2s linear infinite;
}

@keyframes la-01-spin {
  to {
    --la-01-spin: 360deg;
  }
}

.la-01__cart,
.la-01__seal {
  position: absolute;
  inline-size: 3.5rem;
  block-size: 3.5rem;
  fill: none;
  stroke: var(--ink);
  stroke-width: 3.4;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-01__seal {
  stroke: var(--ok);
  opacity: 0;
  scale: .7;
  transition: opacity .35s ease, scale .45s cubic-bezier(.16,1,.3,1);
}

.la-01__tick {
  stroke-dasharray: 32;
  stroke-dashoffset: 32;
  transition: stroke-dashoffset .5s .12s ease;
}

.la-01__item {
  position: absolute;
  inline-size: .85rem;
  block-size: .85rem;
  border-radius: .28rem;
  background: var(--acc);
  box-shadow: 0 4px 10px -4px var(--acc);
  animation: la-01-drop 1.8s cubic-bezier(.5,0,.6,1) infinite;
}

.la-01__item--a {
  --x: -1.5rem;
  background: var(--acc);
  animation-delay: 0s;
}

.la-01__item--b {
  --x: 0rem;
  background: color-mix(in oklab,var(--acc) 55%,var(--ok));
  animation-delay: .6s;
}

.la-01__item--c {
  --x: 1.5rem;
  background: color-mix(in oklab,var(--acc) 40%,black);
  animation-delay: 1.2s;
}

@keyframes la-01-drop {
  0% {
    translate: var(--x) -3.4rem;
    opacity: 0;
    rotate: -25deg;
  }

  22% {
    opacity: 1;
  }

  60% {
    translate: var(--x) -.1rem;
    opacity: 1;
    rotate: 8deg;
  }

  74%,
    100% {
    translate: var(--x) .5rem;
    opacity: 0;
    rotate: 14deg;
  }
}

.la-01__copy {
  display: grid;
  gap: .3rem;
  justify-items: center;
  text-align: center;
}

.la-01__label {
  margin: 0;
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-01__ready {
  display: none;
}

.la-01__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-01__amt {
  color: var(--ink);
  font-weight: 500;
}

.la-01__steps {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  font-size: .75rem;
  letter-spacing: .02em;
  color: var(--muted);
}

.la-01__step {
  display: flex;
  align-items: center;
  gap: .4rem;
  opacity: .38;
  animation: la-01-step var(--dur) linear infinite;
}

.la-01__step::before {
  content: "";
  inline-size: .42rem;
  block-size: .42rem;
  border-radius: 999px;
  background: currentColor;
}

.la-01__step:nth-child(1) {
  animation-delay: 0s;
}

.la-01__step:nth-child(2) {
  animation-delay: 1.8s;
}

.la-01__step:nth-child(3) {
  animation-delay: 3.6s;
}

@keyframes la-01-step {
  0%,
    3% {
    opacity: .34;
    color: var(--muted);
  }

  8%,
    30% {
    opacity: 1;
    color: var(--acc);
  }

  35%,
    100% {
    opacity: .34;
    color: var(--muted);
  }
}

.la-01__track {
  inline-size: 100%;
  block-size: .5rem;
  border-radius: 999px;
  overflow: hidden;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
}

.la-01__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  inline-size: calc(var(--la-01-p, 68) * 1%);
  background: linear-gradient(90deg, color-mix(in oklab,var(--acc) 65%,white), var(--acc));
  animation: la-01-count var(--dur) linear infinite;
}

.la-01__pct {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  counter-reset: la-01-pct var(--la-01-p, 68);
  animation: la-01-count var(--dur) linear infinite;
}

.la-01__pct::after {
  content: counter(la-01-pct) "%";
}

@keyframes la-01-count {
  from {
    --la-01-p: 0;
  }

  to {
    --la-01-p: 100;
  }
}
/* ── completed state: what your success callback switches on ── */

.la-01.is-ready .la-01__cart {
  opacity: 0;
  scale: .8;
}

.la-01.is-ready .la-01__seal {
  opacity: 1;
  scale: 1;
}

.la-01.is-ready .la-01__tick {
  stroke-dashoffset: 0;
}

.la-01.is-ready .la-01__item,
.la-01.is-ready .la-01__stage::before {
  animation: none;
  opacity: 0;
}

.la-01.is-ready .la-01__load {
  display: none;
}

.la-01.is-ready .la-01__ready {
  display: inline;
}

.la-01.is-ready .la-01__step {
  animation: none;
  opacity: 1;
  color: var(--ok);
}

.la-01.is-ready .la-01__fill {
  animation: none;
  inline-size: 100%;
  background: var(--ok);
}

.la-01.is-ready .la-01__pct {
  animation: none;
  --la-01-p: 100;
}

.la-01:has(.la-01__done[aria-pressed="true"]) .la-01__card {
  border-color: color-mix(in oklab,var(--ok) 40%,var(--line));
}

@supports (transition-behavior: allow-discrete) {
  .la-01__seal {
    transition-behavior: allow-discrete;
  }

  @starting-style {
    .la-01.is-ready .la-01__seal {
      opacity: 0;
      scale: .7;
    }
  }
}
/* ── chrome ── */

.la-01__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-01__btn {
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
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), color .25s ease;
}

.la-01__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-01__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-01__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-01__sun {
  display: none;
}

.la-01__theme[aria-pressed="true"] .la-01__sun {
  display: block;
}

.la-01__theme[aria-pressed="true"] .la-01__moon {
  display: none;
}

.la-01__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}
/* ── dark theme ── */

@media (prefers-color-scheme: dark) {
  .la-01:not([data-theme="light"]) {
    --bg: #080a0f;
    --surface: #12151d;
    --ink: #eef1f6;
    --muted: #98a2b3;
    --line: #232936;
    --acc: #8b78ff;
    --ok: #37d39a;
    --ring: #8b78ff;
    --shadow: rgba(0,0,0,.6);
  }

  .la-01:not([data-theme="light"]) .la-01__card {
    box-shadow: 0 1px 0 color-mix(in oklab,white 8%,transparent) inset, 0 40px 80px -40px #000;
  }
}

.la-01[data-theme="dark"] {
  --bg: #080a0f;
  --surface: #12151d;
  --ink: #eef1f6;
  --muted: #98a2b3;
  --line: #232936;
  --acc: #8b78ff;
  --ok: #37d39a;
  --ring: #8b78ff;
  --shadow: rgba(0,0,0,.6);
}

.la-01[data-theme="dark"] .la-01__card {
  box-shadow: 0 1px 0 color-mix(in oklab,white 8%,transparent) inset, 0 40px 80px -40px #000;
}

@media (prefers-reduced-motion: reduce) {
  .la-01 * {
    animation: none !important;
    transition: none !important;
  }

  .la-01__item {
    opacity: 1;
    translate: var(--x) .2rem;
  }

  .la-01__stage::before {
    opacity: .5;
  }

  .la-01__fill {
    inline-size: 68%;
  }

  .la-01__step {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .la-01__card {
    border: 1px solid CanvasText;
  }

  .la-01__fill {
    background: Highlight;
  }

  .la-01__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}

@container (max-width: 19rem) {
  .la-01__steps {
    gap: .65rem;
    font-size: .7rem;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-01');
  if (!root) return;
  const theme = root.querySelector('.la-01__theme');
  const done = root.querySelector('.la-01__done');
  const bar = root.querySelector('[role="progressbar"]');
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');        // the one line your success callback needs
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    bar.setAttribute('aria-valuenow', ready ? 100 : 68);
    bar.setAttribute('aria-valuetext', ready ? 'Order confirmed' : '68 percent complete');
  });
  sync();
})();
```
