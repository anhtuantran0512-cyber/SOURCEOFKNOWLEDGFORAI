---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-subscribe-confetti-button/"
title: "CSS Subscribe Confetti Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Subscribe once and eighteen paper shards fan out on individual trajectories, the bell rings, and the label flips to \"Subscribed\" — with every particle's…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Subscribe Confetti Button
Source: https://codefronts.com/components/css-buttons/css-subscribe-confetti-button/

Subscribe once and eighteen paper shards fan out on individual trajectories, the bell rings, and the label flips to "Subscribed" — with every particle's angle, distance, spin, colour and delay coming from per-child custom properties on one shared keyframe. Pure CSS, zero libraries, no canvas.
## HTML
```html
<div class="cb-14">
  <div class="cb-14__stage">
    <label class="cb-14__btn">
      <input type="checkbox" aria-label="Subscribe to the newsletter">
      <span class="cb-14__bits" aria-hidden="true">
        <span class="cb-14__bit" style="--x:-.95;--y:-.65;--r:180deg;--d:0ms"></span>
        <span class="cb-14__bit" style="--x:-.6;--y:-1;--r:-140deg;--d:20ms"></span>
        <span class="cb-14__bit" style="--x:-.25;--y:-1.1;--r:220deg;--d:40ms"></span>
        <span class="cb-14__bit" style="--x:.1;--y:-1.15;--r:-90deg;--d:10ms"></span>
        <span class="cb-14__bit" style="--x:.45;--y:-1;--r:160deg;--d:50ms"></span>
        <span class="cb-14__bit" style="--x:.8;--y:-.75;--r:-200deg;--d:30ms"></span>
        <span class="cb-14__bit" style="--x:1.05;--y:-.4;--r:120deg;--d:60ms"></span>
        <span class="cb-14__bit" style="--x:-1.1;--y:-.3;--r:-160deg;--d:70ms"></span>
        <span class="cb-14__bit" style="--x:-1.15;--y:.1;--r:200deg;--d:90ms"></span>
        <span class="cb-14__bit" style="--x:1.15;--y:.05;--r:-240deg;--d:80ms"></span>
        <span class="cb-14__bit" style="--x:-.9;--y:.5;--r:140deg;--d:120ms"></span>
        <span class="cb-14__bit" style="--x:.95;--y:.45;--r:-120deg;--d:110ms"></span>
        <span class="cb-14__bit" style="--x:-.5;--y:.85;--r:260deg;--d:150ms"></span>
        <span class="cb-14__bit" style="--x:.55;--y:.8;--r:-180deg;--d:140ms"></span>
        <span class="cb-14__bit" style="--x:0;--y:1;--r:90deg;--d:170ms"></span>
        <span class="cb-14__bit" style="--x:-.3;--y:-.5;--r:-60deg;--d:0ms"></span>
        <span class="cb-14__bit" style="--x:.3;--y:-.55;--r:60deg;--d:15ms"></span>
        <span class="cb-14__bit" style="--x:.7;--y:.2;--r:-300deg;--d:100ms"></span>
      </span>
      <span class="cb-14__face">
        <span class="cb-14__bell" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15.5V11a6 6 0 1 0-12 0v4.5L4.5 18h15L18 15.5z"/><path d="M10 20.5a2.2 2.2 0 0 0 4 0"/></svg>
        </span>
        <span class="cb-14__words">
          <span class="cb-14__word cb-14__word--off">Subscribe</span>
          <span class="cb-14__word cb-14__word--on">Subscribed</span>
        </span>
      </span>
    </label>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

.cb-14 {
  --bg: #100c1a;
  --surface: #1d1730;
  --ink: #f8f5ff;
  --accent: #f43f5e;
  --c1: #fbbf24;
  --c2: #34d399;
  --c3: #60a5fa;
  --radius: 999px;
  --spring: linear(0,.42 8%,.86 17%,1.12 25%,1.06 36%,1 50%,1);
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(46rem 28rem at 50% 40%, color-mix(in oklab,var(--accent) 14%,transparent), transparent 70%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-14 {
    --accent: oklch(64% .21 12);
    --c1: oklch(84% .16 82);
    --c2: oklch(80% .14 165);
    --c3: oklch(76% .13 253);
    --surface: oklch(25% .05 295);
  }
}

@media (prefers-color-scheme: light) {
  .cb-14:not([data-theme="dark"]) {
    --bg: #f6f3fb;
    --surface: #ffffff;
    --ink: #180f24;
  }
}

.cb-14[data-theme="light"] {
  --bg: #f6f3fb;
  --surface: #ffffff;
  --ink: #180f24;
}

.cb-14,
.cb-14 *,
.cb-14 *::before,
.cb-14 *::after {
  box-sizing: border-box;
}

.cb-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-14__btn {
  position: relative;
  z-index: 1;
  cursor: pointer;
  display: inline-grid;
  place-items: center;
  min-height: 3.5rem;
  padding: 0 1.9rem;
  border-radius: var(--radius);
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 88%,white),var(--accent));
  color: var(--ink);
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: -.01em;
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 30%,transparent), 0 16px 34px -16px color-mix(in oklab,var(--accent) 85%,transparent);
  transition: scale .35s var(--spring), background .4s ease, box-shadow .4s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-14__btn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-14__face {
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .55rem;
}

.cb-14__bell {
  display: grid;
  place-items: center;
  width: 1.25rem;
  height: 1.25rem;
  transform-origin: 50% 15%;
}

.cb-14__bell svg {
  width: 1.25rem;
  height: 1.25rem;
}

.cb-14__words {
  display: grid;
}

.cb-14__word {
  grid-area: 1/1;
  opacity: 0;
  translate: 0 .4rem;
  transition: opacity .25s ease, translate .35s cubic-bezier(.16,1,.3,1);
}

.cb-14__word--off {
  opacity: 1;
  translate: 0 0;
}

.cb-14__btn:hover {
  scale: 1.03;
}

.cb-14__btn:active {
  scale: .97;
}

.cb-14__btn:has(input:focus-visible) {
  outline: 2px solid var(--c1);
  outline-offset: 4px;
}

.cb-14__btn:has(input:checked) {
  background: linear-gradient(180deg,color-mix(in oklab,var(--surface) 70%,white 5%),var(--surface));
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--ink) 18%,transparent);
}

.cb-14__btn:has(input:checked) .cb-14__word--off {
  opacity: 0;
  translate: 0 -.4rem;
}

.cb-14__btn:has(input:checked) .cb-14__word--on {
  opacity: 1;
  translate: 0 0;
}

.cb-14__btn:has(input:checked) .cb-14__bell {
  animation: cb-14-ring .8s cubic-bezier(.36,.07,.19,.97);
}

@keyframes cb-14-ring {
  0%,
    100% {
    rotate: 0deg;
  }

  15% {
    rotate: 16deg;
  }

  32% {
    rotate: -13deg;
  }

  50% {
    rotate: 9deg;
  }

  68% {
    rotate: -6deg;
  }

  85% {
    rotate: 3deg;
  }
}

.cb-14__bits {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cb-14__bit {
  position: absolute;
  top: 50%;
  left: 50%;
  width: .5rem;
  height: .32rem;
  margin: -.16rem 0 0 -.25rem;
  border-radius: .06rem;
  background: var(--c1);
  opacity: 0;
}

.cb-14__bit:nth-child(3n) {
  background: var(--c2);
  border-radius: 999px;
  width: .34rem;
  height: .34rem;
}

.cb-14__bit:nth-child(3n+1) {
  background: var(--c3);
}

.cb-14__bit:nth-child(4n) {
  width: .28rem;
  height: .6rem;
}

.cb-14__btn:has(input:checked) .cb-14__bit {
  animation: cb-14-burst .95s cubic-bezier(.2,.7,.3,1) var(--d) forwards;
}

@keyframes cb-14-burst {
  0% {
    opacity: 0;
    translate: 0 0;
    scale: .3;
    rotate: 0deg;
  }

  12% {
    opacity: 1;
  }

  100% {
    opacity: 0;
    translate: calc(var(--x) * 5.5rem) calc(var(--y) * 5.5rem);
    rotate: var(--r);
    scale: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-14__btn,
    .cb-14__word {
    transition: none;
  }

  .cb-14__bit {
    display: none;
  }

  .cb-14__btn:has(input:checked) .cb-14__bell {
    animation: none;
  }
}

@media (forced-colors: active) {
  .cb-14__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .cb-14__bit {
    display: none;
  }
}
```
