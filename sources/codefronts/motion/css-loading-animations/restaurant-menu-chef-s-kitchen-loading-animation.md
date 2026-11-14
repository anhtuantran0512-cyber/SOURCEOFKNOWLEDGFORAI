---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/restaurant-menu-chef-s-kitchen-loading-animation/"
title: "Restaurant Menu Chef's Kitchen Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Food delivery apps buy patience with narrative: you are not waiting, the kitchen is cooking."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Restaurant Menu Chef's Kitchen Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/restaurant-menu-chef-s-kitchen-loading-animation/

Food delivery apps buy patience with narrative: you are not waiting, the kitchen is cooking. A pan tosses on a staggered rhythm, three ingredients arc through the air, steam curls drift and dissipate, and a heat bloom flickers underneath — all drawn with gradients and radii, no sprite sheet, no Lottie. The order line names a real restaurant, courier and item count the way DoorDash or Uber Eats would.
## HTML
```html
<div class="la-03" data-state="loading">
  <div class="la-03__chrome">
    <button class="la-03__btn la-03__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-03__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-03__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-03__btn la-03__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-03__card" role="status" aria-live="polite" aria-label="Preparing your order, estimated 18 minutes">
    <div class="la-03__stage" aria-hidden="true">
      <span class="la-03__steam" style="--dx:-.5rem; --d:0s"></span>
      <span class="la-03__steam" style="--dx:.35rem; --d:.9s"></span>
      <span class="la-03__steam" style="--dx:-.1rem; --d:1.8s"></span>
      <span class="la-03__bit" style="--dx:-1.4rem; --d:0s"></span>
      <span class="la-03__bit" style="--dx:.2rem; --d:.35s"></span>
      <span class="la-03__bit" style="--dx:1.5rem; --d:.7s"></span>
      <div class="la-03__pan"><span class="la-03__food"></span><span class="la-03__handle"></span></div>
      <span class="la-03__heat"></span>
      <svg class="la-03__cloche" viewBox="0 0 64 64" focusable="false">
        <path d="M6 44h52M10 44a22 22 0 0 1 44 0M32 22v-5" />
      </svg>
    </div>

    <div class="la-03__copy">
      <p class="la-03__label">
        <span class="la-03__load">Preparing your order</span>
        <span class="la-03__ready">Order ready for pickup</span>
      </p>
      <p class="la-03__meta">Marlowe Kitchen <span aria-hidden="true">·</span> 3 items <span aria-hidden="true">·</span> Courier Jordan Lee</p>
    </div>

    <p class="la-03__dots" aria-hidden="true"><i></i><i></i><i></i></p>
    <p class="la-03__eta"><span class="la-03__load">Ready in 18 min</span><span class="la-03__ready">Picked up 12:41 PM</span></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400;12..96,600;12..96,700&family=Geist+Mono:wght@400;500&display=swap');

.la-03 {
  --bg: #fdf6ec;
  --surface: #fffdf9;
  --ink: #231a12;
  --muted: #7c6a58;
  --line: #eadfd0;
  --acc: #f4761f;
  --acc-2: #d63b1f;
  --ok: #1f8f5f;
  --ring: #f4761f;
  --shadow: rgba(60,38,16,.2);
  --pan-r: 48% 48% 46% 46% / 22% 22% 60% 60%;
  --dur: 1.9s;
  --sans: "Bricolage Grotesque",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(90% 60% at 50% 0%, color-mix(in oklab,var(--acc) 20%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-03,
.la-03 *,
.la-03 *::before,
.la-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-03 {
    --acc: oklch(70% .17 55);
    --acc-2: oklch(58% .2 32);
    --ok: oklch(58% .14 155);
  }
}

.la-03__card {
  position: relative;
  inline-size: min(23rem,100%);
  padding: 2rem 1.5rem 1.4rem;
  display: grid;
  justify-items: center;
  gap: 1.1rem;
  text-align: center;
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 60px -38px var(--shadow);
}

.la-03__stage {
  position: relative;
  inline-size: 8.5rem;
  block-size: 7.5rem;
  display: grid;
  place-items: end center;
}

.la-03__pan {
  position: relative;
  inline-size: 5.2rem;
  block-size: 2.1rem;
  margin-block-end: 1.4rem;
  border-radius: var(--pan-r);
  rotate: -6deg;
  transform-origin: 75% 40%;
  background: linear-gradient(180deg,#4a4f5a,#20242c 60%,#14171d);
  box-shadow: 0 6px 14px -8px rgba(0,0,0,.7), inset 0 2px 0 rgba(255,255,255,.18);
  animation: la-03-toss var(--dur) cubic-bezier(.3,-.35,.5,1.45) infinite;
}

@keyframes la-03-toss {
  0%,
    100% {
    rotate: -6deg;
    translate: 0 0;
  }

  35% {
    rotate: -20deg;
    translate: 0 -.4rem;
  }

  55% {
    rotate: 1deg;
    translate: 0 -.1rem;
  }

  75% {
    rotate: -4deg;
    translate: 0 .05rem;
  }
}

.la-03__food {
  position: absolute;
  inset-inline: .7rem;
  inset-block-start: .28rem;
  block-size: .5rem;
  border-radius: 999px;
  background: linear-gradient(90deg,var(--acc),var(--acc-2),color-mix(in oklab,var(--acc) 70%,white));
  filter: saturate(1.15);
}

.la-03__handle {
  position: absolute;
  inset-inline-end: -3.1rem;
  inset-block-start: .45rem;
  inline-size: 3.2rem;
  block-size: .5rem;
  border-radius: 999px;
  background: linear-gradient(90deg,#2a2f38,#171a20);
  rotate: -8deg;
}

.la-03__bit {
  position: absolute;
  inset-block-end: 3.1rem;
  inline-size: .6rem;
  block-size: .6rem;
  border-radius: .2rem;
  background: var(--acc);
  animation: la-03-bit var(--dur) cubic-bezier(.32,0,.5,1) infinite;
  animation-delay: var(--d);
}

.la-03__bit:nth-of-type(5) {
  background: var(--acc-2);
  border-radius: 999px;
}

.la-03__bit:nth-of-type(6) {
  background: color-mix(in oklab,var(--ok) 70%,var(--acc));
  border-radius: .15rem;
}

@keyframes la-03-bit {
  0% {
    translate: 0 0;
    opacity: 0;
    rotate: 0deg;
  }

  15% {
    opacity: 1;
  }

  50% {
    translate: var(--dx) -2.6rem;
    rotate: 180deg;
    opacity: 1;
  }

  85% {
    translate: calc(var(--dx) * .3) -.1rem;
    rotate: 330deg;
    opacity: 1;
  }

  100% {
    translate: 0 0;
    opacity: 0;
    rotate: 360deg;
  }
}

.la-03__steam {
  position: absolute;
  inset-block-end: 4.4rem;
  inline-size: .75rem;
  block-size: 1.1rem;
  border-radius: 999px;
  background: linear-gradient(180deg, color-mix(in oklab,var(--ink) 30%,transparent), transparent);
  filter: blur(5px);
  opacity: 0;
  animation: la-03-steam 2.7s ease-out infinite;
  animation-delay: var(--d);
}

@keyframes la-03-steam {
  0% {
    opacity: 0;
    translate: 0 0;
    scale: .6 .5;
  }

  28% {
    opacity: .6;
  }

  100% {
    opacity: 0;
    translate: var(--dx) -3.6rem;
    scale: 1.5 2.3;
  }
}

.la-03__heat {
  position: absolute;
  inset-block-end: .6rem;
  inline-size: 4.6rem;
  block-size: 1.2rem;
  border-radius: 999px;
  background: radial-gradient(closest-side, color-mix(in oklab,var(--acc) 60%,transparent), transparent);
  filter: blur(4px);
  animation: la-03-heat .9s ease-in-out infinite alternate;
}

@keyframes la-03-heat {
  from {
    opacity: .5;
    scale: .94 1;
  }

  to {
    opacity: .68;
    scale: 1.06 1.1;
  }
}

.la-03__cloche {
  position: absolute;
  inset-block-end: 1.2rem;
  inline-size: 4.6rem;
  block-size: 4.6rem;
  fill: none;
  stroke: var(--ok);
  stroke-width: 3.2;
  stroke-linecap: round;
  opacity: 0;
  scale: .8;
  transition: opacity .3s ease, scale .45s cubic-bezier(.16,1,.3,1);
}

.la-03__copy {
  display: grid;
  gap: .28rem;
}

.la-03__label {
  margin: 0;
  font-size: 1.18rem;
  font-weight: 600;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.la-03__meta {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
}

.la-03__ready {
  display: none;
}

.la-03__dots {
  margin: 0;
  display: flex;
  gap: .4rem;
}

.la-03__dots i {
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 999px;
  background: var(--acc);
  opacity: .3;
  animation: la-03-dot 1.35s ease-in-out infinite;
}

.la-03__dots i:nth-child(2) {
  animation-delay: .18s;
}

.la-03__dots i:nth-child(3) {
  animation-delay: .36s;
}

@keyframes la-03-dot {
  0%,
    100% {
    opacity: .25;
    scale: 1;
  }

  45% {
    opacity: 1;
    scale: 1.35;
  }
}

.la-03__eta {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-03.is-ready .la-03__pan,
.la-03.is-ready .la-03__bit,
.la-03.is-ready .la-03__steam,
.la-03.is-ready .la-03__heat,
.la-03.is-ready .la-03__dots i {
  animation: none;
}

.la-03.is-ready .la-03__pan,
.la-03.is-ready .la-03__bit,
.la-03.is-ready .la-03__heat {
  opacity: 0;
}

.la-03.is-ready .la-03__steam {
  opacity: .28;
  translate: var(--dx) -2rem;
  scale: 1.2 1.8;
}

.la-03.is-ready .la-03__cloche {
  opacity: 1;
  scale: 1;
}

.la-03.is-ready .la-03__dots i {
  opacity: 1;
  background: var(--ok);
}

.la-03.is-ready .la-03__load {
  display: none;
}

.la-03.is-ready .la-03__ready {
  display: inline;
}

.la-03__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-03__btn {
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

.la-03__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-03__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-03__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-03__sun {
  display: none;
}

.la-03__theme[aria-pressed="true"] .la-03__sun {
  display: block;
}

.la-03__theme[aria-pressed="true"] .la-03__moon {
  display: none;
}

.la-03__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-03:not([data-theme="light"]) {
    --bg: #120d09;
    --surface: #1c1611;
    --ink: #f7efe6;
    --muted: #a89683;
    --line: #2e251d;
    --acc: #ff8f3c;
    --acc-2: #ff5a35;
    --ok: #3ad693;
    --shadow: rgba(0,0,0,.7);
  }

  .la-03:not([data-theme="light"]) .la-03__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-03:not([data-theme="light"]) .la-03__steam {
    background: linear-gradient(180deg,rgba(255,255,255,.5),transparent);
  }
}

.la-03[data-theme="dark"] {
  --bg: #120d09;
  --surface: #1c1611;
  --ink: #f7efe6;
  --muted: #a89683;
  --line: #2e251d;
  --acc: #ff8f3c;
  --acc-2: #ff5a35;
  --ok: #3ad693;
  --shadow: rgba(0,0,0,.7);
}

.la-03[data-theme="dark"] .la-03__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-03[data-theme="dark"] .la-03__steam {
  background: linear-gradient(180deg,rgba(255,255,255,.5),transparent);
}

@media (prefers-reduced-motion: reduce) {
  .la-03 * {
    animation: none !important;
    transition: none !important;
  }

  .la-03__bit {
    opacity: 0;
  }

  .la-03__steam {
    opacity: .35;
    translate: var(--dx) -1.6rem;
    scale: 1.2 1.7;
  }

  .la-03__dots i:first-child {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .la-03__card {
    border: 1px solid CanvasText;
  }

  .la-03__pan {
    background: CanvasText;
  }

  .la-03__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-03');
  if (!root) return;
  const theme = root.querySelector('.la-03__theme');
  const done = root.querySelector('.la-03__done');
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
    region.setAttribute('aria-label', ready ? 'Order ready for pickup' : 'Preparing your order, estimated 18 minutes');
  });
  sync();
})();
```
