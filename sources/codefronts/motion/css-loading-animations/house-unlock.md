---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/house-unlock/"
title: "Real Estate House Unlock Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Smart-lock and property-access flows have a perfect metaphor built in."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real Estate House Unlock Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/house-unlock/

Smart-lock and property-access flows have a perfect metaphor built in. A padlock's shackle lifts, the front door swings open on a real 3D hinge, and warm interior light spills out as the address is verified — the exact beat a viewing-access or digital-key app needs while it checks a booking.
## HTML
```html
<div class="la-14" data-state="loading">
  <div class="la-14__chrome">
    <button class="la-14__btn la-14__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-14__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-14__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-14__btn la-14__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-14__card" role="status" aria-live="polite" aria-label="Verifying access to 412 Bryant Street">
    <div class="la-14__house" aria-hidden="true">
      <span class="la-14__roof"></span>
      <span class="la-14__wall">
        <span class="la-14__win"></span>
        <span class="la-14__frame">
          <span class="la-14__light"></span>
          <span class="la-14__door"><i class="la-14__knob"></i></span>
        </span>
      </span>
      <span class="la-14__lock">
        <i class="la-14__shackle"></i>
        <i class="la-14__body"></i>
      </span>
    </div>

    <div class="la-14__copy">
      <p class="la-14__label">
        <span class="la-14__load">Verifying access</span>
        <span class="la-14__ready">Access granted</span>
      </p>
      <p class="la-14__addr">412 Bryant St <span aria-hidden="true">·</span> Unit 3 <span aria-hidden="true">·</span> Jordan Lee</p>
    </div>

    <div class="la-14__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="70" aria-valuetext="Verifying digital key">
      <span class="la-14__fill"></span>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-14-open {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.la-14 {
  --bg: #f0f2f6;
  --surface: #ffffff;
  --ink: #0f1420;
  --muted: #606c80;
  --line: #e1e6ee;
  --house: #dbe2ec;
  --house-2: #c3ccd9;
  --roof: #2b3546;
  --door: #b4491f;
  --warm: #ffc978;
  --acc: #0f766e;
  --ok: #0f9d63;
  --ring: #0f766e;
  --shadow: rgba(15,20,32,.18);
  --dur: 5.2s;
  --serif: "Instrument Serif",ui-serif,Georgia,serif;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 65% at 50% -10%, color-mix(in oklab,var(--acc) 15%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-14,
.la-14 *,
.la-14 *::before,
.la-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-14 {
    --acc: oklch(48% .1 180);
    --door: oklch(48% .15 40);
    --warm: oklch(86% .13 78);
  }
}

.la-14__card {
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

.la-14__house {
  position: relative;
  inline-size: 9.5rem;
  block-size: 8rem;
  display: grid;
  place-items: end center;
}

.la-14__roof {
  position: absolute;
  inset-block-start: .4rem;
  inline-size: 8.4rem;
  block-size: 2.6rem;
  background: var(--roof);
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
}

.la-14__wall {
  position: relative;
  inline-size: 6.6rem;
  block-size: 4.4rem;
  border-radius: .3rem .3rem .5rem .5rem;
  background: linear-gradient(180deg,var(--house),var(--house-2));
  box-shadow: inset 0 1px 0 #fff, 0 14px 24px -16px var(--shadow);
  display: grid;
  place-items: end center;
}

.la-14__win {
  position: absolute;
  inset-block-start: .5rem;
  inset-inline-start: .55rem;
  inline-size: 1.5rem;
  block-size: 1.2rem;
  border-radius: .15rem;
  background: color-mix(in oklab,var(--warm) 55%,var(--house-2));
  box-shadow: inset 0 0 0 2px color-mix(in oklab,var(--roof) 60%,transparent);
  animation: la-14-win var(--dur) ease-in-out infinite;
}

@keyframes la-14-win {
  0%,
    40% {
    background: color-mix(in oklab,var(--warm) 25%,var(--house-2));
  }

  66%,
    88% {
    background: var(--warm);
  }

  100% {
    background: color-mix(in oklab,var(--warm) 25%,var(--house-2));
  }
}

.la-14__frame {
  position: relative;
  inline-size: 2rem;
  block-size: 2.9rem;
  margin-inline-end: .6rem;
  perspective: 520px;
  transform-style: preserve-3d;
  background: linear-gradient(180deg,#2a1f18,#100b08);
  border-radius: .9rem .9rem 0 0;
}

.la-14__light {
  position: absolute;
  inset: 0;
  border-radius: .9rem .9rem 0 0;
  background: radial-gradient(120% 90% at 50% 100%, var(--warm), color-mix(in oklab,var(--warm) 30%,transparent) 70%, transparent);
  opacity: 0;
  animation: la-14-glow var(--dur) ease-in-out infinite;
}

@keyframes la-14-glow {
  0%,
    34% {
    opacity: 0;
  }

  62%,
    86% {
    opacity: .95;
  }

  100% {
    opacity: 0;
  }
}

.la-14__door {
  position: absolute;
  inset: 0;
  border-radius: .9rem .9rem 0 0;
  transform-origin: 0 center;
  background: linear-gradient(100deg, color-mix(in oklab,var(--door) 78%,black), var(--door));
  box-shadow: inset -2px 0 0 rgba(0,0,0,.25);
  animation: la-14-open var(--dur) cubic-bezier(.16,1,.3,1) infinite;
}

@keyframes la-14-open {
  0%,
    30% {
    rotate: y 0deg;
  }

  60%,
    86% {
    rotate: y -74deg;
  }

  100% {
    rotate: y 0deg;
  }
}

.la-14__knob {
  position: absolute;
  inset-inline-end: .22rem;
  inset-block-start: 50%;
  inline-size: .24rem;
  block-size: .24rem;
  border-radius: 999px;
  background: var(--warm);
}

.la-14__lock {
  position: absolute;
  inset-block-end: .15rem;
  inset-inline-end: .15rem;
  inline-size: 1.9rem;
  block-size: 2.2rem;
  display: grid;
  justify-items: center;
  align-content: end;
}

.la-14__shackle {
  inline-size: 1rem;
  block-size: .9rem;
  border: .22rem solid var(--roof);
  border-block-end: 0;
  border-start-start-radius: 999px;
  border-start-end-radius: 999px;
  animation: la-14-shackle var(--dur) cubic-bezier(.16,1,.3,1) infinite;
}

@keyframes la-14-shackle {
  0%,
    22% {
    translate: 0 0;
    rotate: 0deg;
  }

  42%,
    86% {
    translate: .12rem -.34rem;
    rotate: 8deg;
  }

  100% {
    translate: 0 0;
    rotate: 0deg;
  }
}

.la-14__body {
  inline-size: 1.6rem;
  block-size: 1.25rem;
  border-radius: .3rem;
  background: linear-gradient(180deg,var(--acc), color-mix(in oklab,var(--acc) 70%,black));
  box-shadow: 0 6px 12px -8px var(--shadow);
  position: relative;
}

.la-14__body::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  inline-size: .26rem;
  block-size: .4rem;
  border-radius: 999px 999px .1rem .1rem;
  background: rgba(0,0,0,.45);
}

.la-14__copy {
  display: grid;
  gap: .25rem;
}

.la-14__label {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.5rem;
  line-height: 1.1;
}

.la-14__ready {
  display: none;
}

.la-14__addr {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
}

.la-14__track {
  inline-size: 100%;
  block-size: .35rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  overflow: hidden;
}

.la-14__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg,color-mix(in oklab,var(--acc) 55%,white),var(--acc));
  animation: la-14-bar var(--dur) linear infinite;
}

@keyframes la-14-bar {
  from {
    inline-size: 10%;
  }

  to {
    inline-size: 100%;
  }
}

.la-14.is-ready .la-14__door,
.la-14.is-ready .la-14__shackle,
.la-14.is-ready .la-14__light,
.la-14.is-ready .la-14__win,
.la-14.is-ready .la-14__fill {
  animation: none;
}

.la-14.is-ready .la-14__door {
  rotate: y -74deg;
}

.la-14.is-ready .la-14__shackle {
  translate: .12rem -.34rem;
  rotate: 8deg;
}

.la-14.is-ready .la-14__light {
  opacity: .95;
}

.la-14.is-ready .la-14__win {
  background: var(--warm);
}

.la-14.is-ready .la-14__body {
  background: linear-gradient(180deg,var(--ok), color-mix(in oklab,var(--ok) 70%,black));
}

.la-14.is-ready .la-14__fill {
  inline-size: 100%;
  background: var(--ok);
}

.la-14.is-ready .la-14__load {
  display: none;
}

.la-14.is-ready .la-14__ready {
  display: inline;
}

.la-14__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-14__btn {
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

.la-14__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-14__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-14__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-14__sun {
  display: none;
}

.la-14__theme[aria-pressed="true"] .la-14__sun {
  display: block;
}

.la-14__theme[aria-pressed="true"] .la-14__moon {
  display: none;
}

.la-14__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-14:not([data-theme="light"]) {
    --bg: #070910;
    --surface: #111620;
    --ink: #eef2f8;
    --muted: #8f9bb0;
    --line: #212936;
    --house: #2b3444;
    --house-2: #1d2530;
    --roof: #101620;
    --door: #8e3a18;
    --warm: #ffcf8a;
    --acc: #2dd4bf;
    --ok: #31d68f;
    --ring: #2dd4bf;
    --shadow: rgba(0,0,0,.7);
  }

  .la-14:not([data-theme="light"]) .la-14__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-14:not([data-theme="light"]) .la-14__done[aria-pressed="true"] {
    color: #04231a;
  }
}

.la-14[data-theme="dark"] {
  --bg: #070910;
  --surface: #111620;
  --ink: #eef2f8;
  --muted: #8f9bb0;
  --line: #212936;
  --house: #2b3444;
  --house-2: #1d2530;
  --roof: #101620;
  --door: #8e3a18;
  --warm: #ffcf8a;
  --acc: #2dd4bf;
  --ok: #31d68f;
  --ring: #2dd4bf;
  --shadow: rgba(0,0,0,.7);
}

.la-14[data-theme="dark"] .la-14__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-14[data-theme="dark"] .la-14__done[aria-pressed="true"] {
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .la-14 * {
    animation: none !important;
    transition: none !important;
  }

  .la-14__door {
    rotate: y -40deg;
  }

  .la-14__light {
    opacity: .7;
  }

  .la-14__fill {
    inline-size: 70%;
  }
}

@media (forced-colors: active) {
  .la-14__card,
    .la-14__wall {
    border: 1px solid CanvasText;
  }

  .la-14__fill {
    background: Highlight;
  }

  .la-14__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-14');
  if (!root) return;
  const theme = root.querySelector('.la-14__theme');
  const done = root.querySelector('.la-14__done');
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
    bar.setAttribute('aria-valuenow', ready ? 100 : 70);
    bar.setAttribute('aria-valuetext', ready ? 'Access granted' : 'Verifying digital key');
    region.setAttribute('aria-label', ready ? 'Access granted for 412 Bryant Street' : 'Verifying access to 412 Bryant Street');
  });
  sync();
})();
```
