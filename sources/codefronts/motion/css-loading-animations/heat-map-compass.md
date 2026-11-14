---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/heat-map-compass/"
title: "Real Estate Heat-Map Compass Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Map and analytics products need a loader that says \"we are computing over an area\"."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real Estate Heat-Map Compass Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/heat-map-compass/

Map and analytics products need a loader that says "we are computing over an area". A price heat-map grid pulses in diagonal waves as a compass needle hunts for north — the wave is pure nth-child delay maths, and the colour ramp is built in oklch() so intensity steps look evenly spaced instead of muddy in the middle.
## HTML
```html
<div class="la-17" data-state="loading">
  <div class="la-17__chrome">
    <button class="la-17__btn la-17__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-17__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-17__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-17__btn la-17__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-17__card" role="status" aria-live="polite" aria-label="Mapping price trends for Austin, Texas">
    <div class="la-17__map" aria-hidden="true">
      <div class="la-17__grid">
        <i style="--row:0;--col:0;--w:20"></i><i style="--row:0;--col:1;--w:35"></i><i style="--row:0;--col:2;--w:55"></i><i style="--row:0;--col:3;--w:40"></i><i style="--row:0;--col:4;--w:25"></i><i style="--row:0;--col:5;--w:15"></i>
        <i style="--row:1;--col:0;--w:30"></i><i style="--row:1;--col:1;--w:60"></i><i style="--row:1;--col:2;--w:80"></i><i style="--row:1;--col:3;--w:65"></i><i style="--row:1;--col:4;--w:40"></i><i style="--row:1;--col:5;--w:22"></i>
        <i style="--row:2;--col:0;--w:45"></i><i style="--row:2;--col:1;--w:75"></i><i style="--row:2;--col:2;--w:100"></i><i style="--row:2;--col:3;--w:85"></i><i style="--row:2;--col:4;--w:55"></i><i style="--row:2;--col:5;--w:30"></i>
        <i style="--row:3;--col:0;--w:35"></i><i style="--row:3;--col:1;--w:58"></i><i style="--row:3;--col:2;--w:82"></i><i style="--row:3;--col:3;--w:70"></i><i style="--row:3;--col:4;--w:48"></i><i style="--row:3;--col:5;--w:26"></i>
        <i style="--row:4;--col:0;--w:22"></i><i style="--row:4;--col:1;--w:38"></i><i style="--row:4;--col:2;--w:52"></i><i style="--row:4;--col:3;--w:44"></i><i style="--row:4;--col:4;--w:30"></i><i style="--row:4;--col:5;--w:18"></i>
      </div>
      <span class="la-17__compass">
        <i class="la-17__needle"></i>
        <i class="la-17__hub"></i>
      </span>
    </div>

    <div class="la-17__copy">
      <p class="la-17__label">
        <span class="la-17__load">Mapping price trends</span>
        <span class="la-17__ready">Heat map ready</span>
      </p>
      <p class="la-17__meta">Austin, TX <span aria-hidden="true">·</span> 1,284 listings <span aria-hidden="true">·</span> 12-month change</p>
    </div>

    <dl class="la-17__read">
      <div><dt>Median</dt><dd>$612k</dd></div>
      <div><dt>YoY</dt><dd>+4.8%</dd></div>
      <div><dt>Bearing</dt><dd class="la-17__bearing">N 4° E</dd></div>
    </dl>

    <p class="la-17__legend">
      <span class="la-17__item"><i aria-hidden="true" class="la-17__sw la-17__sw--c"></i>Cooling</span>
      <span class="la-17__item"><i aria-hidden="true" class="la-17__sw la-17__sw--m"></i>Steady</span>
      <span class="la-17__item"><i aria-hidden="true" class="la-17__sw la-17__sw--h"></i>Heating</span>
    </p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-17-rot {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.la-17 {
  --bg: #f2f4f7;
  --surface: #ffffff;
  --ink: #0d121a;
  --muted: #606b7c;
  --line: #e2e6ee;
  --grid: #eef1f6;
  --cool: #2f6fed;
  --hot: #ff4d3d;
  --acc: #ff4d3d;
  --ok: #0f9d63;
  --ring: #2f6fed;
  --shadow: rgba(13,18,26,.16);
  --dur: 2.8s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 60% at 50% -10%, color-mix(in oklab,var(--cool) 14%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-17,
.la-17 *,
.la-17 *::before,
.la-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-17 {
    --cool: oklch(58% .17 258);
    --hot: oklch(64% .23 30);
    --acc: oklch(64% .23 30);
  }
}

.la-17__card {
  position: relative;
  inline-size: min(24rem,100%);
  padding: 1.5rem 1.4rem 1.3rem;
  display: grid;
  justify-items: center;
  gap: 1rem;
  text-align: center;
  border-radius: 1.5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -40px var(--shadow);
}

.la-17__map {
  position: relative;
  inline-size: 100%;
  padding: .55rem;
  border-radius: 1rem;
  background: var(--grid);
  border: 1px solid var(--line);
  overflow: hidden;
}

.la-17__grid {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  gap: .3rem;
}

.la-17__grid i {
  aspect-ratio: 1;
  border-radius: .3rem;
  opacity: .28;
  scale: .9;
  background: color-mix(in oklab, var(--hot) calc(var(--w) * 1%), var(--cool));
  animation: la-17-wave var(--dur) ease-in-out infinite;
  animation-delay: calc((var(--row) + var(--col)) * .085s);
}

@keyframes la-17-wave {
  0%,
    100% {
    opacity: .22;
    scale: .88;
  }

  45% {
    opacity: 1;
    scale: 1;
  }
}

.la-17__compass {
  position: absolute;
  inset-block-end: .6rem;
  inset-inline-end: .6rem;
  inline-size: 2.9rem;
  block-size: 2.9rem;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: color-mix(in srgb, var(--surface) 88%, transparent);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border: 1px solid var(--line);
  box-shadow: 0 10px 20px -14px var(--shadow);
}

.la-17__compass::before {
  content: "N";
  position: absolute;
  inset-block-start: .1rem;
  font-family: var(--mono);
  font-size: .5rem;
  color: var(--muted);
}

.la-17__needle {
  inline-size: .28rem;
  block-size: 2.1rem;
  border-radius: 999px;
  background: linear-gradient(180deg, var(--hot) 0 50%, color-mix(in oklab,var(--ink) 55%,transparent) 50%);
  transform-origin: 50% 50%;
  rotate: -24deg;
  animation: la-17-hunt calc(var(--dur) * 2) cubic-bezier(.34,1.4,.5,1) infinite;
}

@keyframes la-17-hunt {
  0% {
    rotate: -24deg;
  }

  42% {
    rotate: 196deg;
  }

  56% {
    rotate: 172deg;
  }

  72%,
    100% {
    rotate: 184deg;
  }
}

.la-17__hub {
  position: absolute;
  inline-size: .42rem;
  block-size: .42rem;
  border-radius: 999px;
  background: var(--ink);
}

.la-17__copy {
  display: grid;
  gap: .22rem;
}

.la-17__label {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-17__ready {
  display: none;
}

.la-17__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-17__read {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
  inline-size: 100%;
}

.la-17__read div {
  padding: .45rem .3rem;
  border-radius: .55rem;
  background: color-mix(in oklab,var(--cool) 7%,transparent);
  border: 1px solid var(--line);
}

.la-17__read dt {
  margin: 0 0 .1rem;
  font-family: var(--mono);
  font-size: .55rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.la-17__read dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .78rem;
  font-variant-numeric: tabular-nums;
}

.la-17__legend {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .2rem .7rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .58rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.la-17__item {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  white-space: nowrap;
}

.la-17__sw {
  inline-size: .55rem;
  block-size: .55rem;
  border-radius: .15rem;
  flex: none;
}

.la-17__sw--c {
  background: var(--cool);
}

.la-17__sw--m {
  background: color-mix(in oklab,var(--hot) 50%,var(--cool));
}

.la-17__sw--h {
  background: var(--hot);
}

.la-17.is-ready .la-17__grid i {
  animation: none;
  opacity: 1;
  scale: 1;
}

.la-17.is-ready .la-17__needle {
  animation: none;
  rotate: 184deg;
}

.la-17.is-ready .la-17__load {
  display: none;
}

.la-17.is-ready .la-17__ready {
  display: inline;
}

.la-17.is-ready .la-17__bearing {
  color: var(--ok);
}

.la-17__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-17__btn {
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

.la-17__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-17__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-17__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-17__sun {
  display: none;
}

.la-17__theme[aria-pressed="true"] .la-17__sun {
  display: block;
}

.la-17__theme[aria-pressed="true"] .la-17__moon {
  display: none;
}

.la-17__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-17:not([data-theme="light"]) {
    --bg: #080a10;
    --surface: #111620;
    --ink: #eef1f8;
    --muted: #909cb0;
    --line: #212936;
    --grid: #0d1219;
    --cool: #4d8bff;
    --hot: #ff6a52;
    --acc: #ff6a52;
    --ok: #31d68f;
    --ring: #4d8bff;
    --shadow: rgba(0,0,0,.7);
  }

  .la-17:not([data-theme="light"]) .la-17__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-17:not([data-theme="light"]) .la-17__done[aria-pressed="true"] {
    color: #04231a;
  }
}

.la-17[data-theme="dark"] {
  --bg: #080a10;
  --surface: #111620;
  --ink: #eef1f8;
  --muted: #909cb0;
  --line: #212936;
  --grid: #0d1219;
  --cool: #4d8bff;
  --hot: #ff6a52;
  --acc: #ff6a52;
  --ok: #31d68f;
  --ring: #4d8bff;
  --shadow: rgba(0,0,0,.7);
}

.la-17[data-theme="dark"] .la-17__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-17[data-theme="dark"] .la-17__done[aria-pressed="true"] {
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .la-17 * {
    animation: none !important;
    transition: none !important;
  }

  .la-17__grid i {
    opacity: 1;
    scale: 1;
  }

  .la-17__needle {
    rotate: 184deg;
  }
}

@media (forced-colors: active) {
  .la-17__card,
    .la-17__map {
    border: 1px solid CanvasText;
  }

  .la-17__grid i {
    background: CanvasText;
  }

  .la-17__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-17');
  if (!root) return;
  const theme = root.querySelector('.la-17__theme');
  const done = root.querySelector('.la-17__done');
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
    region.setAttribute('aria-label', ready ? 'Heat map ready for Austin, Texas' : 'Mapping price trends for Austin, Texas');
  });
  sync();
})();
```
