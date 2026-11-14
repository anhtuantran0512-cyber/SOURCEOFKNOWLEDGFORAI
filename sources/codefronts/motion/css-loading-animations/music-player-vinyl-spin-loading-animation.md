---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/music-player-vinyl-spin-loading-animation/"
title: "Music Player Vinyl Spin Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "A turntable loader with real record physics: grooves cut as a repeating-radial-gradient, a specular sheen that sweeps as the disc turns, and a tonearm that…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Music Player Vinyl Spin Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/music-player-vinyl-spin-loading-animation/

A turntable loader with real record physics: grooves cut as a repeating-radial-gradient, a specular sheen that sweeps as the disc turns, and a tonearm that lowers onto the platter at the top of every cycle. An equalizer strip below moves with the beat, and the track line reads like a real now-playing row.
## HTML
```html
<div class="la-09" data-state="loading">
  <div class="la-09__chrome">
    <button class="la-09__btn la-09__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-09__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-09__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-09__btn la-09__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-09__card" role="status" aria-live="polite" aria-label="Loading track Nightdrive by Sam Rivera">
    <div class="la-09__deck" aria-hidden="true">
      <span class="la-09__disc"><span class="la-09__spindle"></span></span>
      <span class="la-09__gloss"></span>
      <span class="la-09__arm"><i class="la-09__post"></i><i class="la-09__head"></i></span>
    </div>

    <div class="la-09__copy">
      <p class="la-09__title">Nightdrive</p>
      <p class="la-09__artist">Sam Rivera <span aria-hidden="true">·</span> Neon Atlas</p>
      <p class="la-09__state">
        <span class="la-09__load">Loading track</span>
        <span class="la-09__ready">Now playing <span aria-hidden="true">·</span> 3:48</span>
      </p>
    </div>

    <p class="la-09__eq" aria-hidden="true">
      <i style="--i:0"></i><i style="--i:1"></i><i style="--i:2"></i><i style="--i:3"></i>
      <i style="--i:4"></i><i style="--i:5"></i><i style="--i:6"></i><i style="--i:7"></i>
      <i style="--i:8"></i><i style="--i:9"></i><i style="--i:10"></i><i style="--i:11"></i>
    </p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.la-09 {
  --bg: #0b0910;
  --surface: #16121d;
  --ink: #f6f1fb;
  --muted: #a396b3;
  --line: #2a2233;
  --acc: #ff2d95;
  --acc-2: #7b5cff;
  --label: #ff2d95;
  --ring: #ff2d95;
  --disc: 10rem;
  --rpm: 1.8s;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(70% 55% at 20% 10%, color-mix(in oklab,var(--acc-2) 30%,transparent), transparent 60%), radial-gradient(60% 50% at 85% 90%, color-mix(in oklab,var(--acc) 26%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-09,
.la-09 *,
.la-09 *::before,
.la-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-09 {
    --acc: oklch(66% .27 350);
    --acc-2: oklch(60% .24 285);
    --label: oklch(66% .27 350);
  }
}

.la-09__card {
  position: relative;
  inline-size: min(22rem,100%);
  padding: 1.8rem 1.5rem 1.4rem;
  display: grid;
  justify-items: center;
  gap: 1.15rem;
  text-align: center;
  border-radius: 1.5rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--surface) 90%,var(--acc-2)), var(--surface));
  border: 1px solid var(--line);
  box-shadow: 0 50px 90px -55px #000, 0 0 0 1px rgba(255,255,255,.04) inset;
}

@supports (corner-shape: squircle) {
  .la-09__card {
    corner-shape: squircle;
    border-radius: 2rem;
  }
}

.la-09__deck {
  position: relative;
  inline-size: var(--disc);
  block-size: var(--disc);
  isolation: isolate;
}

.la-09__disc {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: radial-gradient(circle, var(--label) 0 20%, transparent 20.5%), radial-gradient(circle, #08080c 0 7%, transparent 7.5%), repeating-radial-gradient(circle, #1c1c22 0 2px, #101015 2px 4px), conic-gradient(from 0deg, #0c0c11, #26262f 25%, #0c0c11 50%, #26262f 75%, #0c0c11);
  box-shadow: 0 18px 34px -20px #000, 0 0 0 1px rgba(255,255,255,.06) inset;
  animation: la-09-spin var(--rpm) linear infinite;
}

@keyframes la-09-spin {
  to {
    rotate: 360deg;
  }
}

.la-09__spindle {
  position: absolute;
  inset: 0;
  margin: auto;
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 999px;
  background: #e8e6ef;
  box-shadow: 0 0 0 2px rgba(0,0,0,.5);
}

.la-09__gloss {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  pointer-events: none;
  mix-blend-mode: overlay;
  background: linear-gradient(115deg, transparent 38%, rgba(255,255,255,.22) 50%, transparent 62%);
}

.la-09__arm {
  position: absolute;
  inset-block-start: -.6rem;
  inset-inline-end: -1.1rem;
  inline-size: 1rem;
  block-size: 6.4rem;
  transform-origin: 50% 8%;
  rotate: -20deg;
  animation: la-09-drop 5.4s cubic-bezier(.16,1,.3,1) infinite;
}

.la-09__arm::before {
  content: "";
  position: absolute;
  inset-block: .5rem 1rem;
  inset-inline-start: .36rem;
  inline-size: .28rem;
  border-radius: 999px;
  background: linear-gradient(180deg,#d8d5e2,#8f8a9d);
}

.la-09__post {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 1rem;
  block-size: 1rem;
  border-radius: 999px;
  background: linear-gradient(160deg,#3a3446,#1b1823);
  box-shadow: 0 0 0 1px rgba(255,255,255,.08) inset;
}

.la-09__head {
  position: absolute;
  inset-block-end: .4rem;
  inset-inline-start: .1rem;
  inline-size: .8rem;
  block-size: 1.1rem;
  border-radius: .2rem;
  background: linear-gradient(180deg,#c9c5d6,#6d6879);
  rotate: 6deg;
}

@keyframes la-09-drop {
  0%,
    12% {
    rotate: -20deg;
  }

  32%,
    78% {
    rotate: 1deg;
  }

  92%,
    100% {
    rotate: -20deg;
  }
}

.la-09__copy {
  display: grid;
  gap: .2rem;
}

.la-09__title {
  margin: 0;
  font-size: 1.28rem;
  font-weight: 700;
  letter-spacing: -.03em;
}

.la-09__artist {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.la-09__state {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--acc);
}

.la-09__ready {
  display: none;
}

.la-09__eq {
  margin: 0;
  display: flex;
  align-items: flex-end;
  gap: .22rem;
  block-size: 1.6rem;
}

.la-09__eq i {
  inline-size: .22rem;
  block-size: 100%;
  border-radius: 999px;
  transform-origin: 50% 100%;
  background: linear-gradient(180deg,var(--acc),var(--acc-2));
  scale: 1 .3;
  animation: la-09-eq 1.05s ease-in-out infinite alternate;
  animation-delay: calc(var(--i) * -.09s);
}

@keyframes la-09-eq {
  from {
    scale: 1 .22;
  }

  to {
    scale: 1 1;
  }
}

.la-09.is-ready .la-09__disc {
  animation-duration: calc(var(--rpm) * 1);
}

.la-09.is-ready .la-09__arm {
  animation: none;
  rotate: 1deg;
}

.la-09.is-ready .la-09__load {
  display: none;
}

.la-09.is-ready .la-09__ready {
  display: inline;
}

.la-09.is-ready .la-09__state {
  color: var(--acc-2);
}

.la-09.is-ready .la-09__eq i {
  animation-duration: .62s;
}

.la-09__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-09__btn {
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

.la-09__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-09__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-09__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-09__sun {
  display: none;
}

.la-09__theme[aria-pressed="true"] .la-09__sun {
  display: block;
}

.la-09__theme[aria-pressed="true"] .la-09__moon {
  display: none;
}

.la-09__done[aria-pressed="true"] {
  background: var(--acc);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .la-09:not([data-theme="dark"]) {
    --bg: #f3f0f7;
    --surface: #ffffff;
    --ink: #140f1b;
    --muted: #655a73;
    --line: #e5dfec;
    --acc: #d6197a;
    --acc-2: #5b3ff0;
    --label: #d6197a;
  }

  .la-09:not([data-theme="dark"]) .la-09__card {
    box-shadow: 0 1px 0 #fff inset, 0 36px 64px -42px rgba(20,15,27,.2);
  }
}

.la-09[data-theme="light"] {
  --bg: #f3f0f7;
  --surface: #ffffff;
  --ink: #140f1b;
  --muted: #655a73;
  --line: #e5dfec;
  --acc: #d6197a;
  --acc-2: #5b3ff0;
  --label: #d6197a;
}

.la-09[data-theme="light"] .la-09__card {
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -42px rgba(20,15,27,.2);
}

@media (prefers-reduced-motion: reduce) {
  .la-09 * {
    animation: none !important;
    transition: none !important;
  }

  .la-09__arm {
    rotate: 1deg;
  }

  .la-09__eq i {
    scale: 1 .55;
  }

  .la-09__eq i:nth-child(odd) {
    scale: 1 .85;
  }
}

@media (forced-colors: active) {
  .la-09__card {
    border: 1px solid CanvasText;
  }

  .la-09__disc {
    background: CanvasText;
  }

  .la-09__eq i {
    background: Highlight;
  }

  .la-09__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-09');
  if (!root) return;
  const theme = root.querySelector('.la-09__theme');
  const done = root.querySelector('.la-09__done');
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
    region.setAttribute('aria-label', ready ? 'Now playing Nightdrive by Sam Rivera' : 'Loading track Nightdrive by Sam Rivera');
  });
  sync();
})();
```
