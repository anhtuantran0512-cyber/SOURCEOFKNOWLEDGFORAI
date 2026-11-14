---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/package-delivery-truck-route-loading-animation/"
title: "Package Delivery Truck Route Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Package tracking is a waiting state people refresh on purpose, so it deserves the best loader in the set."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Package Delivery Truck Route Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/package-delivery-truck-route-loading-animation/

Package tracking is a waiting state people refresh on purpose, so it deserves the best loader in the set. A van drives a curved dotted route on a stylised street grid using offset-path — real CSS motion-path, not a keyframed translate approximation — the route dashes flow toward the destination pin, the pin pulses, and a live ETA ticks down next to the courier's name.
## HTML
```html
<div class="la-07" data-state="loading">
  <div class="la-07__chrome">
    <button class="la-07__btn la-07__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-07__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-07__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-07__btn la-07__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-07__card" role="status" aria-live="polite" aria-label="Package out for delivery">
    <div class="la-07__map" aria-hidden="true">
      <div class="la-07__scene">
        <svg class="la-07__route" viewBox="0 0 300 130" width="300" height="130" focusable="false">
          <path class="la-07__road-bed" d="M14 96 C 74 96, 74 34, 150 34 S 226 96, 286 96"/>
          <path class="la-07__road" d="M14 96 C 74 96, 74 34, 150 34 S 226 96, 286 96"/>
        </svg>
        <span class="la-07__origin"></span>
        <span class="la-07__pin">
          <svg viewBox="0 0 24 24" focusable="false"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>
        </span>
        <span class="la-07__van">
          <svg viewBox="0 0 44 26" focusable="false">
            <path class="la-07__body" d="M2 6h22v13H2z"/>
            <path class="la-07__cab" d="M24 10h8l6 5v4H24z"/>
            <circle class="la-07__wheel" cx="10" cy="21" r="3.4"/><circle class="la-07__wheel" cx="31" cy="21" r="3.4"/>
          </svg>
        </span>
      </div>
    </div>

    <div class="la-07__copy">
      <p class="la-07__label">
        <span class="la-07__load">Out for delivery</span>
        <span class="la-07__ready">Delivered</span>
      </p>
      <p class="la-07__meta">Courier Jordan Lee <span aria-hidden="true">·</span> 2 stops away</p>
    </div>

    <p class="la-07__eta" aria-hidden="true"><span id="la-07-eta">Arriving in 14 min</span> <span class="la-07__sep">·</span> Updated just now</p>
    <div class="la-07__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="76" aria-valuetext="2 stops away">
      <span class="la-07__fill"></span>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.la-07 {
  --bg: #f5f6f9;
  --surface: #ffffff;
  --ink: #12151b;
  --muted: #646d7b;
  --line: #e3e7ee;
  --road: #c8cfdb;
  --acc: #ff6a13;
  --ok: #12a05f;
  --ring: #ff6a13;
  --shadow: rgba(18,21,27,.16);
  --dur: 5.6s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 70% at 50% -10%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-07,
.la-07 *,
.la-07 *::before,
.la-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-07 {
    --acc: oklch(68% .2 44);
    --ok: oklch(60% .15 155);
  }
}

.la-07__card {
  position: relative;
  inline-size: min(26rem,100%);
  padding: 1.1rem 1.1rem 1.3rem;
  display: grid;
  gap: 1rem;
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -40px var(--shadow);
}

.la-07__map {
  position: relative;
  aspect-ratio: 300 / 130;
  container-type: inline-size;
  border-radius: 1.1rem;
  overflow: hidden;
  background: repeating-linear-gradient(0deg, color-mix(in oklab,var(--ink) 5%,transparent) 0 1px, transparent 1px 26px), repeating-linear-gradient(90deg, color-mix(in oklab,var(--ink) 5%,transparent) 0 1px, transparent 1px 26px), linear-gradient(160deg, color-mix(in oklab,var(--ink) 4%,transparent), transparent);
  border: 1px solid var(--line);
}

.la-07__scene {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 300px;
  block-size: 130px;
  transform-origin: 0 0;
  scale: 1;
}

@supports (width: 1cqw) {
  .la-07__scene {
    scale: calc(100cqw / 300);
  }
}

.la-07__route {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 300px;
  block-size: 130px;
  fill: none;
}

.la-07__road-bed {
  stroke: var(--road);
  stroke-width: 7;
  stroke-linecap: round;
}

.la-07__road {
  stroke: var(--acc);
  stroke-width: 2.6;
  stroke-linecap: round;
  stroke-dasharray: 8 10;
  animation: la-07-flow 1.1s linear infinite;
}

@keyframes la-07-flow {
  to {
    stroke-dashoffset: -18;
  }
}

.la-07__origin {
  position: absolute;
  inset-inline-start: 9.5px;
  inset-block-start: 91.5px;
  inline-size: 9px;
  block-size: 9px;
  border-radius: 999px;
  background: var(--surface);
  border: 2.5px solid var(--ink);
}

.la-07__pin {
  position: absolute;
  inset-inline-start: 272px;
  inset-block-start: 70px;
  inline-size: 28px;
  block-size: 28px;
  display: grid;
  place-items: center;
}

.la-07__pin svg {
  inline-size: 26px;
  block-size: 26px;
  fill: none;
  stroke: var(--ok);
  stroke-width: 1.8;
  stroke-linejoin: round;
  position: relative;
  z-index: 2;
}

.la-07__pin::before,
.la-07__pin::after {
  content: "";
  position: absolute;
  inset-block-end: 2px;
  inline-size: 22px;
  block-size: 22px;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ok) 40%,transparent);
  animation: la-07-pulse 2.2s ease-out infinite;
}

.la-07__pin::after {
  animation-delay: 1.1s;
}

@keyframes la-07-pulse {
  0% {
    scale: .3;
    opacity: .7;
  }

  100% {
    scale: 1.6;
    opacity: 0;
  }
}

.la-07__van {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 38px;
  block-size: 23px;
  animation: la-07-slide var(--dur) cubic-bezier(.45,0,.55,1) infinite;
}

.la-07__van svg {
  inline-size: 100%;
  block-size: 100%;
  fill: none;
  stroke-linejoin: round;
  stroke-linecap: round;
  stroke-width: 2;
}

.la-07__body {
  fill: var(--acc);
  stroke: none;
}

.la-07__cab {
  fill: color-mix(in oklab,var(--acc) 70%,black);
  stroke: none;
}

.la-07__wheel {
  fill: #15181e;
  stroke: none;
}

@keyframes la-07-slide {
  0% {
    translate: 0 82px;
  }

  100% {
    translate: 262px 82px;
  }
}

@supports not (offset-path: path("M0 0 L 1 1")) {
  /* no motion path: plain slide across */

  .la-07.is-ready .la-07__van {
    translate: 262px 82px;
  }

  @media (prefers-reduced-motion: reduce) {
    .la-07__van {
      translate: 150px 82px;
    }
  }
}

@supports (offset-path: path("M0 0 L 1 1")) {
  .la-07__van {
    /* never combine with translate: it stacks */
    offset-path: path("M14 96 C 74 96, 74 34, 150 34 S 226 96, 286 96");
    offset-rotate: auto 0deg;
    offset-anchor: 50% 88%;
    animation: la-07-drive var(--dur) cubic-bezier(.45,0,.55,1) infinite;
  }

  @keyframes la-07-drive {
    from {
      offset-distance: 0%;
    }

    to {
      offset-distance: 100%;
    }
  }
}

.la-07__copy {
  display: grid;
  gap: .25rem;
  padding-inline: .35rem;
}

.la-07__label {
  margin: 0;
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-07__ready {
  display: none;
}

.la-07__meta {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
}

.la-07__eta {
  margin: 0;
  padding-inline: .35rem;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-07__sep {
  opacity: .5;
}

.la-07__track {
  margin-inline: .35rem;
  block-size: .4rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  overflow: hidden;
}

.la-07__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg, color-mix(in oklab,var(--acc) 70%,white), var(--acc));
  animation: la-07-fill var(--dur) linear infinite;
}

@keyframes la-07-fill {
  from {
    inline-size: 12%;
  }

  to {
    inline-size: 100%;
  }
}

.la-07.is-ready .la-07__van,
.la-07.is-ready .la-07__road,
.la-07.is-ready .la-07__fill,
.la-07.is-ready .la-07__pin::before,
.la-07.is-ready .la-07__pin::after {
  animation: none;
}

.la-07.is-ready .la-07__road {
  stroke: var(--ok);
  stroke-dasharray: none;
}

.la-07.is-ready .la-07__van {
  offset-distance: 93%;
}
/* parked just short of the pin */

.la-07.is-ready .la-07__fill {
  inline-size: 100%;
  background: var(--ok);
}

.la-07.is-ready .la-07__pin svg {
  stroke: var(--ok);
  stroke-width: 2.4;
}

.la-07.is-ready .la-07__load {
  display: none;
}

.la-07.is-ready .la-07__ready {
  display: inline;
}

.la-07__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-07__btn {
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

.la-07__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-07__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-07__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-07__sun {
  display: none;
}

.la-07__theme[aria-pressed="true"] .la-07__sun {
  display: block;
}

.la-07__theme[aria-pressed="true"] .la-07__moon {
  display: none;
}

.la-07__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-07:not([data-theme="light"]) {
    --bg: #080a0e;
    --surface: #12161d;
    --ink: #eef1f6;
    --muted: #95a0b0;
    --line: #212833;
    --road: #2b3340;
    --acc: #ff8845;
    --ok: #2ed08a;
    --ring: #ff8845;
    --shadow: rgba(0,0,0,.7);
  }

  .la-07:not([data-theme="light"]) .la-07__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }
}

.la-07[data-theme="dark"] {
  --bg: #080a0e;
  --surface: #12161d;
  --ink: #eef1f6;
  --muted: #95a0b0;
  --line: #212833;
  --road: #2b3340;
  --acc: #ff8845;
  --ok: #2ed08a;
  --ring: #ff8845;
  --shadow: rgba(0,0,0,.7);
}

.la-07[data-theme="dark"] .la-07__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

@media (prefers-reduced-motion: reduce) {
  .la-07 * {
    animation: none !important;
    transition: none !important;
  }

  .la-07__van {
    offset-distance: 62%;
  }

  .la-07__fill {
    inline-size: 76%;
  }
}

@media (forced-colors: active) {
  .la-07__card,
    .la-07__map {
    border: 1px solid CanvasText;
  }

  .la-07__road {
    stroke: Highlight;
  }

  .la-07__fill {
    background: Highlight;
  }

  .la-07__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-07');
  if (!root) return;
  const theme = root.querySelector('.la-07__theme');
  const done = root.querySelector('.la-07__done');
  const eta = root.querySelector('#la-07-eta');
  const region = root.querySelector('[role="status"]');
  let mins = 14;
  const tick = setInterval(() => {                          // visible ETA only — not announced every minute
    if (root.classList.contains('is-ready')) return;
    mins = mins > 1 ? mins - 1 : 14; eta.textContent = 'Arriving in ' + mins + ' min';
  }, 4000);
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => { theme.setAttribute('aria-pressed', String(dark())); theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme'); };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    eta.textContent = ready ? 'Left at front door 4:12 PM' : 'Arriving in ' + mins + ' min';
    region.setAttribute('aria-label', ready ? 'Package delivered to Jordan Lee' : 'Package out for delivery');
    if (ready) clearInterval(tick);
  });
  sync();
})();
```
