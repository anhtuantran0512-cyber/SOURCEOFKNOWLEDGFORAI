---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/floor-by-floor/"
title: "Building Floor-by-Floor Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "For anything that loads in layers — floor plans, building data, a multi-tenant dataset — this loader lights a tower floor by floor from the ground up, with a…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Building Floor-by-Floor Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/floor-by-floor/

For anything that loads in layers — floor plans, building data, a multi-tenant dataset — this loader lights a tower floor by floor from the ground up, with a survey line rising through it and a floor counter climbing 1 → 6 in pure CSS. It looks like a city at dusk and reads instantly as "still assembling".
## HTML
```html
<div class="la-18" data-state="loading">
  <div class="la-18__chrome">
    <button class="la-18__btn la-18__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-18__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-18__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-18__btn la-18__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-18__card" role="status" aria-live="polite" aria-label="Loading floor plans">
    <div class="la-18__tower" aria-hidden="true">
      <span class="la-18__roof"></span>
      <div class="la-18__body">
        <i class="la-18__win" style="--floor:5;--col:0"></i><i class="la-18__win" style="--floor:5;--col:1"></i><i class="la-18__win" style="--floor:5;--col:2"></i><i class="la-18__win" style="--floor:5;--col:3"></i>
        <i class="la-18__win" style="--floor:4;--col:0"></i><i class="la-18__win" style="--floor:4;--col:1"></i><i class="la-18__win" style="--floor:4;--col:2"></i><i class="la-18__win" style="--floor:4;--col:3"></i>
        <i class="la-18__win" style="--floor:3;--col:0"></i><i class="la-18__win" style="--floor:3;--col:1"></i><i class="la-18__win" style="--floor:3;--col:2"></i><i class="la-18__win" style="--floor:3;--col:3"></i>
        <i class="la-18__win" style="--floor:2;--col:0"></i><i class="la-18__win" style="--floor:2;--col:1"></i><i class="la-18__win" style="--floor:2;--col:2"></i><i class="la-18__win" style="--floor:2;--col:3"></i>
        <i class="la-18__win" style="--floor:1;--col:0"></i><i class="la-18__win" style="--floor:1;--col:1"></i><i class="la-18__win" style="--floor:1;--col:2"></i><i class="la-18__win" style="--floor:1;--col:3"></i>
        <i class="la-18__win la-18__win--door" style="--floor:0;--col:0"></i><i class="la-18__win" style="--floor:0;--col:1"></i><i class="la-18__win" style="--floor:0;--col:2"></i><i class="la-18__win" style="--floor:0;--col:3"></i>
      </div>
      <span class="la-18__scan"></span>
      <span class="la-18__ground"></span>
    </div>

    <div class="la-18__copy">
      <p class="la-18__label">
        <span class="la-18__load">Loading floor plans</span>
        <span class="la-18__ready">All floors loaded</span>
      </p>
      <p class="la-18__meta">Rivermark Tower <span aria-hidden="true">·</span> 6 levels <span aria-hidden="true">·</span> 18,400 sqft</p>
    </div>

    <div class="la-18__track" role="progressbar" aria-valuemin="1" aria-valuemax="6" aria-valuenow="4" aria-valuetext="Floor 4 of 6">
      <span class="la-18__fill"></span>
    </div>
    <p class="la-18__floor"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-18-f {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

.la-18 {
  color-scheme: light dark;
  --bg: #eef1f6;
  --surface: #ffffff;
  --ink: #0c1119;
  --muted: #616c7e;
  --line: #e1e6ee;
  --tower: #cdd6e2;
  --tower-2: #aab6c6;
  --warm: #ffc861;
  --cool: #8fd8ff;
  --pane: #3b4a5f;
  --acc: #2563eb;
  --ok: #0f9d63;
  --ring: #2563eb;
  --shadow: rgba(12,17,25,.18);
  --dur: 4.8s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(90% 60% at 50% 0%, color-mix(in oklab,var(--acc) 15%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-18,
.la-18 *,
.la-18 *::before,
.la-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-18 {
    --acc: oklch(52% .2 262);
    --warm: oklch(84% .14 78);
    --cool: oklch(85% .1 220);
  }
}

.la-18__card {
  position: relative;
  inline-size: min(22.5rem,100%);
  padding: 1.8rem 1.5rem 1.35rem;
  display: grid;
  justify-items: center;
  gap: 1.05rem;
  text-align: center;
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -40px var(--shadow);
}

.la-18__tower {
  position: relative;
  inline-size: 8rem;
  block-size: 9.5rem;
  display: grid;
  place-items: end center;
}

.la-18__roof {
  position: absolute;
  inset-block-start: .35rem;
  inline-size: 5.4rem;
  block-size: .5rem;
  border-radius: .25rem .25rem 0 0;
  background: var(--tower-2);
}

.la-18__roof::after {
  content: "";
  position: absolute;
  inset-block-start: -1rem;
  inset-inline-start: 50%;
  inline-size: 2px;
  block-size: 1rem;
  background: var(--tower-2);
}

.la-18__body {
  inline-size: 5.9rem;
  block-size: 8rem;
  margin-block-end: .4rem;
  padding: .45rem;
  border-radius: .35rem .35rem 0 0;
  background: linear-gradient(180deg,var(--tower),var(--tower-2));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6), 0 16px 26px -18px var(--shadow);
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .28rem;
  align-content: end;
}

.la-18__win {
  border-radius: .12rem;
  background: var(--warm);
  opacity: .14;
  box-shadow: 0 0 6px color-mix(in srgb, var(--warm) 60%, transparent);
  animation: la-18-lamp var(--dur) ease-in-out infinite;
  animation-delay: calc(var(--floor) * .42s + var(--col) * .07s);
}

.la-18__win:nth-child(4n+2) {
  background: color-mix(in oklab,var(--warm) 65%,var(--cool));
}

.la-18__win:nth-child(6n+3) {
  background: color-mix(in oklab,var(--cool) 55%,var(--warm));
}

.la-18__win--door {
  border-radius: .12rem .12rem 0 0;
  background: color-mix(in oklab,var(--warm) 80%,white);
}

@keyframes la-18-lamp {
  0%,
    8% {
    opacity: .14;
  }

  24%,
    76% {
    opacity: 1;
  }

  92%,
    100% {
    opacity: .14;
  }
}

@supports (color: light-dark(#000,#fff)) {
  .la-18__win {
    box-shadow: 0 0 8px light-dark(rgba(255,190,90,.5), rgba(255,205,120,.75));
  }
}

.la-18__scan {
  position: absolute;
  inset-inline: .6rem;
  inset-block-end: .4rem;
  block-size: 2px;
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, var(--acc), transparent);
  box-shadow: 0 0 12px color-mix(in srgb, var(--acc) 70%, transparent);
  animation: la-18-scan var(--dur) cubic-bezier(.4,0,.6,1) infinite;
}

@keyframes la-18-scan {
  0% {
    translate: 0 0;
    opacity: 0;
  }

  12% {
    opacity: 1;
  }

  82% {
    translate: 0 -7.4rem;
    opacity: 1;
  }

  100% {
    translate: 0 -7.8rem;
    opacity: 0;
  }
}

.la-18__ground {
  position: absolute;
  inset-block-end: 0;
  inline-size: 7.4rem;
  block-size: .35rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 14%,transparent);
  filter: blur(1px);
}

.la-18__copy {
  display: grid;
  gap: .24rem;
}

.la-18__label {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-18__ready {
  display: none;
}

.la-18__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-18__track {
  inline-size: 100%;
  block-size: .4rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  overflow: hidden;
}

.la-18__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg,color-mix(in oklab,var(--acc) 55%,white),var(--acc));
  animation: la-18-bar var(--dur) steps(6, jump-none) infinite;
}

@keyframes la-18-bar {
  from {
    inline-size: 16.6%;
  }

  to {
    inline-size: 100%;
  }
}

.la-18__floor {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  counter-reset: la-18-f var(--la-18-f, 4);
  animation: la-18-count var(--dur) steps(6, jump-none) infinite;
}

.la-18__floor::after {
  content: "Floor " counter(la-18-f) " of 6";
}

@keyframes la-18-count {
  from {
    --la-18-f: 1;
  }

  to {
    --la-18-f: 6;
  }
}

.la-18.is-ready .la-18__win,
.la-18.is-ready .la-18__scan,
.la-18.is-ready .la-18__fill,
.la-18.is-ready .la-18__floor {
  animation: none;
}

.la-18.is-ready .la-18__win {
  opacity: 1;
}

.la-18.is-ready .la-18__scan {
  opacity: 0;
}

.la-18.is-ready .la-18__fill {
  inline-size: 100%;
  background: var(--ok);
}

.la-18.is-ready .la-18__floor {
  --la-18-f: 6;
}

.la-18.is-ready .la-18__load {
  display: none;
}

.la-18.is-ready .la-18__ready {
  display: inline;
}

.la-18__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-18__btn {
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

.la-18__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-18__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-18__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-18__sun {
  display: none;
}

.la-18__theme[aria-pressed="true"] .la-18__sun {
  display: block;
}

.la-18__theme[aria-pressed="true"] .la-18__moon {
  display: none;
}

.la-18__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-18:not([data-theme="light"]) {
    --bg: #06080e;
    --surface: #101620;
    --ink: #eef1f8;
    --muted: #909cb0;
    --line: #202836;
    --tower: #2a3546;
    --tower-2: #18202c;
    --acc: #6f9bff;
    --ok: #31d68f;
    --ring: #6f9bff;
    --shadow: rgba(0,0,0,.75);
  }

  .la-18:not([data-theme="light"]) .la-18__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-18:not([data-theme="light"]) .la-18__body {
    box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 20px 30px -20px #000;
  }

  .la-18:not([data-theme="light"]) .la-18__done[aria-pressed="true"] {
    color: #04231a;
  }
}

.la-18[data-theme="dark"] {
  --bg: #06080e;
  --surface: #101620;
  --ink: #eef1f8;
  --muted: #909cb0;
  --line: #202836;
  --tower: #2a3546;
  --tower-2: #18202c;
  --acc: #6f9bff;
  --ok: #31d68f;
  --ring: #6f9bff;
  --shadow: rgba(0,0,0,.75);
}

.la-18[data-theme="dark"] .la-18__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-18[data-theme="dark"] .la-18__body {
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 20px 30px -20px #000;
}

.la-18[data-theme="dark"] .la-18__done[aria-pressed="true"] {
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .la-18 * {
    animation: none !important;
    transition: none !important;
  }

  .la-18__win {
    opacity: 1;
  }

  .la-18__scan {
    opacity: 0;
  }

  .la-18__fill {
    inline-size: 66%;
  }
}

@media (forced-colors: active) {
  .la-18__card,
    .la-18__body {
    border: 1px solid CanvasText;
  }

  .la-18__win {
    background: Highlight;
  }

  .la-18__fill {
    background: Highlight;
  }

  .la-18__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-18');
  if (!root) return;
  const theme = root.querySelector('.la-18__theme');
  const done = root.querySelector('.la-18__done');
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
    bar.setAttribute('aria-valuenow', ready ? 6 : 4);
    bar.setAttribute('aria-valuetext', ready ? 'All 6 floors loaded' : 'Floor 4 of 6');
    region.setAttribute('aria-label', ready ? 'All floor plans loaded' : 'Loading floor plans');
  });
  sync();
})();
```
