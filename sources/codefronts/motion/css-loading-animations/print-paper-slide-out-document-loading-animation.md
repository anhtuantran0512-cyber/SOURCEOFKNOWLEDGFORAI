---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/print-paper-slide-out-document-loading-animation/"
title: "Print Paper Slide-Out Document Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Generating a PDF, exporting a contract, printing a label — anything that produces a document deserves this loader instead of a spinner."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Print Paper Slide-Out Document Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/print-paper-slide-out-document-loading-animation/

Generating a PDF, exporting a contract, printing a label — anything that produces a document deserves this loader instead of a spinner. A sheet slides out of a printer with its text lines revealing top-to-bottom under a mask, the status LED blinks between passes, and the page counter advances 1 → 5 in pure CSS with a stepped counter().
## HTML
```html
<div class="la-12" data-state="loading">
  <div class="la-12__chrome">
    <button class="la-12__btn la-12__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-12__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-12__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-12__btn la-12__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-12__card" role="status" aria-live="polite" aria-label="Printing lease-agreement.pdf">
    <div class="la-12__machine" aria-hidden="true">
      <span class="la-12__tray"></span>
      <span class="la-12__body">
        <span class="la-12__led"></span>
        <span class="la-12__vent"></span>
      </span>
      <span class="la-12__slot">
        <span class="la-12__sheet"><i></i><i></i><i></i><i></i><i></i><i></i></span>
      </span>
    </div>

    <div class="la-12__copy">
      <p class="la-12__label">
        <span class="la-12__load">Printing document</span>
        <span class="la-12__ready">Document ready</span>
      </p>
      <p class="la-12__name">lease-agreement.pdf <span aria-hidden="true">·</span> Sam Rivera</p>
    </div>

    <div class="la-12__track" role="progressbar" aria-valuemin="1" aria-valuemax="5" aria-valuenow="3" aria-valuetext="Page 3 of 5">
      <span class="la-12__fill"></span>
    </div>
    <p class="la-12__page"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-12-page {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

@property --la-12-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.la-12 {
  --bg: #f1f3f7;
  --surface: #ffffff;
  --ink: #0e1219;
  --muted: #636d7d;
  --line: #e2e6ee;
  --shell: #dfe4ec;
  --shell-2: #c3cad6;
  --paper: #ffffff;
  --lines: #c9d1de;
  --acc: #5457ff;
  --ok: #0f9d63;
  --ring: #5457ff;
  --shadow: rgba(14,18,25,.16);
  --dur: 5s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 65% at 50% -10%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-12,
.la-12 *,
.la-12 *::before,
.la-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-12 {
    --acc: oklch(56% .22 275);
    --ok: oklch(62% .15 158);
  }
}

.la-12__card {
  position: relative;
  inline-size: min(23rem,100%);
  padding: 1.9rem 1.5rem 1.4rem;
  display: grid;
  justify-items: center;
  gap: 1.1rem;
  text-align: center;
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -40px var(--shadow);
}

.la-12__machine {
  position: relative;
  inline-size: 9.5rem;
  block-size: 8rem;
  display: grid;
  place-items: start center;
}

.la-12__tray {
  position: absolute;
  inset-block-start: .2rem;
  inline-size: 5.6rem;
  block-size: .7rem;
  border-radius: .3rem .3rem 0 0;
  background: linear-gradient(180deg,var(--shell-2),var(--shell));
}

.la-12__body {
  position: absolute;
  inset-block-start: .85rem;
  inline-size: 8.2rem;
  block-size: 2.9rem;
  border-radius: .7rem;
  background: linear-gradient(180deg, var(--shell), var(--shell-2));
  box-shadow: 0 10px 20px -14px var(--shadow), inset 0 1px 0 #fff;
  display: grid;
  align-content: center;
  justify-items: start;
  padding-inline: .7rem;
  gap: .35rem;
}

.la-12__led {
  inline-size: .42rem;
  block-size: .42rem;
  border-radius: 999px;
  background: var(--acc);
  box-shadow: 0 0 6px var(--acc);
  animation: la-12-led 1.05s steps(2, jump-none) infinite;
}

@keyframes la-12-led {
  0% {
    opacity: 1;
  }

  50% {
    opacity: .25;
  }
}

.la-12__vent {
  inline-size: 3.2rem;
  block-size: .24rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 18%,transparent);
}

.la-12__slot {
  position: absolute;
  inset-block-start: 3.55rem;
  inline-size: 8.2rem;
  block-size: 4.4rem;
  clip-path: inset(0 0 -140% 0);
}

.la-12__slot::before {
  content: "";
  position: absolute;
  inset-block-start: 0;
  inset-inline: .5rem;
  block-size: .34rem;
  border-radius: 0 0 .2rem .2rem;
  background: linear-gradient(180deg,#2a2f39,#161a20);
  z-index: 3;
}

.la-12__sheet {
  position: absolute;
  inset-block-start: .2rem;
  inset-inline-start: 1.1rem;
  inline-size: 6rem;
  block-size: 4rem;
  border-radius: .15rem;
  background: var(--paper);
  box-shadow: 0 8px 16px -10px var(--shadow), 0 0 0 1px color-mix(in oklab,var(--ink) 10%,transparent);
  display: grid;
  align-content: start;
  gap: .34rem;
  padding: .5rem .55rem;
  translate: 0 -3.4rem;
  z-index: 2;
  -webkit-mask-image: linear-gradient(#000 var(--la-12-p, 70%), transparent var(--la-12-p, 70%));
  mask-image: linear-gradient(#000 var(--la-12-p, 70%), transparent var(--la-12-p, 70%));
  animation: la-12-feed var(--dur) cubic-bezier(.45,0,.55,1) infinite, la-12-reveal var(--dur) linear infinite;
}

.la-12__sheet i {
  display: block;
  block-size: .22rem;
  border-radius: 999px;
  background: var(--lines);
}

.la-12__sheet i:first-child {
  block-size: .34rem;
  inline-size: 70%;
  background: color-mix(in oklab,var(--ink) 45%,transparent);
}

.la-12__sheet i:nth-child(4) {
  inline-size: 88%;
}

.la-12__sheet i:nth-child(6) {
  inline-size: 46%;
}

@keyframes la-12-feed {
  0% {
    translate: 0 -3.4rem;
  }

  78%,
    100% {
    translate: 0 .35rem;
  }
}

@keyframes la-12-reveal {
  0% {
    --la-12-p: 0%;
  }

  74%,
    100% {
    --la-12-p: 100%;
  }
}

.la-12__copy {
  display: grid;
  gap: .25rem;
}

.la-12__label {
  margin: 0;
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-12__ready {
  display: none;
}

.la-12__name {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.la-12__track {
  inline-size: 100%;
  block-size: .4rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  overflow: hidden;
}

.la-12__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg, color-mix(in oklab,var(--acc) 60%,white), var(--acc));
  animation: la-12-bar var(--dur) steps(5, jump-none) infinite;
}

@keyframes la-12-bar {
  from {
    inline-size: 20%;
  }

  to {
    inline-size: 100%;
  }
}

.la-12__page {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  counter-reset: la-12-page var(--la-12-page, 3);
  animation: la-12-count var(--dur) steps(5, jump-none) infinite;
}

.la-12__page::after {
  content: "Page " counter(la-12-page) " of 5";
}

@keyframes la-12-count {
  from {
    --la-12-page: 1;
  }

  to {
    --la-12-page: 5;
  }
}

.la-12.is-ready .la-12__sheet,
.la-12.is-ready .la-12__led,
.la-12.is-ready .la-12__fill,
.la-12.is-ready .la-12__page {
  animation: none;
}

.la-12.is-ready .la-12__sheet {
  translate: 0 .35rem;
  --la-12-p: 100%;
}

.la-12.is-ready .la-12__led {
  background: var(--ok);
  box-shadow: 0 0 6px var(--ok);
  opacity: 1;
}

.la-12.is-ready .la-12__fill {
  inline-size: 100%;
  background: var(--ok);
}

.la-12.is-ready .la-12__page {
  --la-12-page: 5;
}

.la-12.is-ready .la-12__load {
  display: none;
}

.la-12.is-ready .la-12__ready {
  display: inline;
}

.la-12__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-12__btn {
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

.la-12__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-12__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-12__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-12__sun {
  display: none;
}

.la-12__theme[aria-pressed="true"] .la-12__sun {
  display: block;
}

.la-12__theme[aria-pressed="true"] .la-12__moon {
  display: none;
}

.la-12__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-12:not([data-theme="light"]) {
    --bg: #080a0f;
    --surface: #111620;
    --ink: #eef1f7;
    --muted: #94a0b2;
    --line: #212936;
    --shell: #2a3140;
    --shell-2: #1a202b;
    --paper: #e9edf4;
    --lines: #9fabbd;
    --acc: #8b8dff;
    --ok: #31d68f;
    --ring: #8b8dff;
    --shadow: rgba(0,0,0,.7);
  }

  .la-12:not([data-theme="light"]) .la-12__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-12:not([data-theme="light"]) .la-12__done[aria-pressed="true"] {
    color: #04231a;
  }
}

.la-12[data-theme="dark"] {
  --bg: #080a0f;
  --surface: #111620;
  --ink: #eef1f7;
  --muted: #94a0b2;
  --line: #212936;
  --shell: #2a3140;
  --shell-2: #1a202b;
  --paper: #e9edf4;
  --lines: #9fabbd;
  --acc: #8b8dff;
  --ok: #31d68f;
  --ring: #8b8dff;
  --shadow: rgba(0,0,0,.7);
}

.la-12[data-theme="dark"] .la-12__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-12[data-theme="dark"] .la-12__done[aria-pressed="true"] {
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .la-12 * {
    animation: none !important;
    transition: none !important;
  }

  .la-12__sheet {
    translate: 0 .2rem;
    --la-12-p: 100%;
  }

  .la-12__fill {
    inline-size: 60%;
  }
}

@media (forced-colors: active) {
  .la-12__card,
    .la-12__sheet {
    border: 1px solid CanvasText;
  }

  .la-12__fill {
    background: Highlight;
  }

  .la-12__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-12');
  if (!root) return;
  const theme = root.querySelector('.la-12__theme');
  const done = root.querySelector('.la-12__done');
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
    bar.setAttribute('aria-valuenow', ready ? 5 : 3);
    bar.setAttribute('aria-valuetext', ready ? 'All 5 pages printed' : 'Page 3 of 5');
    region.setAttribute('aria-label', ready ? 'lease-agreement.pdf ready, 5 pages' : 'Printing lease-agreement.pdf');
  });
  sync();
})();
```
