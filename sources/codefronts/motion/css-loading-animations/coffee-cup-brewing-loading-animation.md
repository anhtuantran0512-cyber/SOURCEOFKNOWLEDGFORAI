---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/coffee-cup-brewing-loading-animation/"
title: "Coffee Cup Brewing Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "The friendliest loader in the collection and the easiest to reuse: an espresso stream pours from the group head, the cup fills with a real crema line, steam…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Coffee Cup Brewing Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/coffee-cup-brewing-loading-animation/

The friendliest loader in the collection and the easiest to reuse: an espresso stream pours from the group head, the cup fills with a real crema line, steam curls lift and dissipate, and a serif label counts the brew. Everything is CSS — one cup element, one liquid mask and three blurred pills — so it drops into any café, kitchen or lifestyle app.
## HTML
```html
<div class="la-11" data-state="loading">
  <div class="la-11__chrome">
    <button class="la-11__btn la-11__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-11__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-11__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-11__btn la-11__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-11__card" role="status" aria-live="polite" aria-label="Brewing your flat white">
    <div class="la-11__stage" aria-hidden="true">
      <span class="la-11__head"><i></i><i></i></span>
      <span class="la-11__pour"></span>
      <span class="la-11__steam" style="--dx:-.45rem; --d:0s"></span>
      <span class="la-11__steam" style="--dx:.3rem; --d:1s"></span>
      <span class="la-11__steam" style="--dx:-.05rem; --d:2s"></span>
      <span class="la-11__cup">
        <span class="la-11__liquid"></span>
        <span class="la-11__handle"></span>
      </span>
      <span class="la-11__saucer"></span>
    </div>

    <div class="la-11__copy">
      <p class="la-11__label">
        <span class="la-11__load">Brewing your flat white</span>
        <span class="la-11__ready">Ready at the bar</span>
      </p>
      <p class="la-11__meta">Alex Chen <span aria-hidden="true">·</span> Order 042 <span aria-hidden="true">·</span> Oat, extra hot</p>
    </div>

    <div class="la-11__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="62" aria-valuetext="62 percent brewed">
      <span class="la-11__fill"></span>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500&family=Geist+Mono:wght@400;500&display=swap');

@property --la-11-fill {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.la-11 {
  --bg: #f7f1e8;
  --surface: #fffdfa;
  --ink: #241a12;
  --muted: #7b6857;
  --line: #ece0d2;
  --coffee: #4a2a15;
  --crema: #c98f52;
  --cup: #ffffff;
  --saucer: #e7d8c5;
  --acc: #a35c2b;
  --ok: #2f8f5b;
  --ring: #a35c2b;
  --shadow: rgba(50,32,16,.2);
  --dur: 4.6s;
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
  background: radial-gradient(90% 60% at 50% 0%, color-mix(in oklab,var(--acc) 18%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-11,
.la-11 *,
.la-11 *::before,
.la-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-11 {
    --acc: oklch(52% .12 48);
    --coffee: oklch(32% .09 50);
    --crema: oklch(72% .11 62);
  }
}

.la-11__card {
  position: relative;
  inline-size: min(22.5rem,100%);
  padding: 1.9rem 1.5rem 1.4rem;
  display: grid;
  justify-items: center;
  gap: 1.15rem;
  text-align: center;
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 62px -40px var(--shadow);
}

.la-11__stage {
  position: relative;
  inline-size: 9rem;
  block-size: 9.5rem;
  display: grid;
  place-items: end center;
}

.la-11__head {
  position: absolute;
  inset-block-start: 0;
  inline-size: 3.4rem;
  block-size: 1.1rem;
  border-radius: .3rem .3rem .5rem .5rem;
  background: linear-gradient(180deg,#3c3f47,#22252b);
  display: flex;
  justify-content: center;
  gap: .9rem;
  align-items: flex-end;
}

.la-11__head i {
  inline-size: .3rem;
  block-size: .28rem;
  border-radius: 0 0 999px 999px;
  background: #14161a;
}

.la-11__pour {
  position: absolute;
  inset-block-start: 1.1rem;
  inline-size: .26rem;
  block-size: 2.5rem;
  border-radius: 999px;
  background: linear-gradient(180deg, color-mix(in oklab,var(--coffee) 70%,var(--crema)), var(--coffee));
  transform-origin: 50% 0;
  scale: 1 0;
  animation: la-11-pour var(--dur) cubic-bezier(.4,0,.6,1) infinite;
}

@keyframes la-11-pour {
  0% {
    scale: 1 0;
  }

  10%,
    60% {
    scale: 1 1;
  }

  72%,
    100% {
    scale: 1 0;
  }
}

.la-11__cup {
  position: relative;
  inline-size: 5rem;
  block-size: 4rem;
  margin-block-end: .75rem;
  overflow: hidden;
  border-radius: .5rem .5rem 2.2rem 2.2rem / .5rem .5rem 1.8rem 1.8rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--cup) 92%,var(--ink)), var(--cup));
  box-shadow: 0 12px 22px -14px color-mix(in oklab,var(--saucer) 80%,black), inset 0 -2px 0 rgba(0,0,0,.06);
}

.la-11__liquid {
  position: absolute;
  inset: .28rem .3rem .1rem;
  border-radius: .3rem .3rem 2rem 2rem / .3rem .3rem 1.6rem 1.6rem;
  background: linear-gradient(to top,
      var(--coffee) 0 var(--la-11-fill, 62%),
      var(--crema) var(--la-11-fill, 62%),
      transparent calc(var(--la-11-fill, 62%) + 7%));
  animation: la-11-fill var(--dur) ease-in-out infinite;
}

@keyframes la-11-fill {
  0% {
    --la-11-fill: 4%;
  }

  66%,
    88% {
    --la-11-fill: 88%;
  }

  100% {
    --la-11-fill: 4%;
  }
}

.la-11__handle {
  position: absolute;
  inset-inline-end: -1.35rem;
  inset-block-start: .7rem;
  inline-size: 1.5rem;
  block-size: 1.7rem;
  border: .34rem solid var(--cup);
  border-inline-start-color: transparent;
  border-radius: 0 999px 999px 0;
}

.la-11__saucer {
  position: absolute;
  inset-block-end: 0;
  inline-size: 6.8rem;
  block-size: .55rem;
  border-radius: 999px;
  background: linear-gradient(180deg, var(--saucer), color-mix(in oklab,var(--saucer) 70%,black));
}

.la-11__steam {
  position: absolute;
  inset-block-end: 5.1rem;
  inline-size: .7rem;
  block-size: 1rem;
  border-radius: 999px;
  background: linear-gradient(180deg, color-mix(in oklab,var(--ink) 26%,transparent), transparent);
  filter: blur(4px);
  opacity: 0;
  animation: la-11-steam 3s ease-out infinite;
  animation-delay: var(--d);
}

@keyframes la-11-steam {
  0% {
    opacity: 0;
    translate: 0 0;
    scale: .6 .5;
  }

  32% {
    opacity: .5;
  }

  100% {
    opacity: 0;
    translate: var(--dx) -3.2rem;
    scale: 1.6 2.4;
  }
}

.la-11__copy {
  display: grid;
  gap: .25rem;
}

.la-11__label {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.55rem;
  line-height: 1.1;
  letter-spacing: -.01em;
  text-wrap: balance;
}

@supports (text-box-trim: trim-both) {
  .la-11__label {
    text-box-trim: trim-both;
    text-box-edge: cap alphabetic;
  }
}

.la-11__ready {
  display: none;
}

.la-11__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
}

.la-11__track {
  inline-size: 100%;
  block-size: .35rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 8%,transparent);
  overflow: hidden;
}

.la-11__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  inline-size: var(--la-11-fill, 62%);
  background: linear-gradient(90deg,var(--crema),var(--acc));
  animation: la-11-fill var(--dur) ease-in-out infinite;
}

.la-11.is-ready .la-11__pour,
.la-11.is-ready .la-11__liquid,
.la-11.is-ready .la-11__fill {
  animation: none;
}

.la-11.is-ready .la-11__pour {
  scale: 1 0;
}

.la-11.is-ready .la-11__liquid {
  --la-11-fill: 88%;
}

.la-11.is-ready .la-11__fill {
  inline-size: 100%;
  background: var(--ok);
}

.la-11.is-ready .la-11__load {
  display: none;
}

.la-11.is-ready .la-11__ready {
  display: inline;
}

.la-11__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-11__btn {
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

.la-11__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-11__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-11__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-11__sun {
  display: none;
}

.la-11__theme[aria-pressed="true"] .la-11__sun {
  display: block;
}

.la-11__theme[aria-pressed="true"] .la-11__moon {
  display: none;
}

.la-11__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-11:not([data-theme="light"]) {
    --bg: #100c08;
    --surface: #1a1410;
    --ink: #f6ece0;
    --muted: #a8927c;
    --line: #2c2119;
    --cup: #2f2620;
    --saucer: #3a2e25;
    --crema: #e0a86a;
    --acc: #d98a4a;
    --ok: #3ecf8a;
    --shadow: rgba(0,0,0,.7);
  }

  .la-11:not([data-theme="light"]) .la-11__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-11:not([data-theme="light"]) .la-11__steam {
    background: linear-gradient(180deg,rgba(255,255,255,.5),transparent);
  }
}

.la-11[data-theme="dark"] {
  --bg: #100c08;
  --surface: #1a1410;
  --ink: #f6ece0;
  --muted: #a8927c;
  --line: #2c2119;
  --cup: #2f2620;
  --saucer: #3a2e25;
  --crema: #e0a86a;
  --acc: #d98a4a;
  --ok: #3ecf8a;
  --shadow: rgba(0,0,0,.7);
}

.la-11[data-theme="dark"] .la-11__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-11[data-theme="dark"] .la-11__steam {
  background: linear-gradient(180deg,rgba(255,255,255,.5),transparent);
}

@media (prefers-reduced-motion: reduce) {
  .la-11 * {
    animation: none !important;
    transition: none !important;
  }

  .la-11__liquid {
    --la-11-fill: 62%;
  }

  .la-11__pour {
    scale: 1 1;
  }

  .la-11__steam {
    opacity: .3;
    translate: var(--dx) -1.6rem;
    scale: 1.2 1.6;
  }
}

@media (forced-colors: active) {
  .la-11__card {
    border: 1px solid CanvasText;
  }

  .la-11__cup {
    border: 1px solid CanvasText;
  }

  .la-11__fill {
    background: Highlight;
  }

  .la-11__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-11');
  if (!root) return;
  const theme = root.querySelector('.la-11__theme');
  const done = root.querySelector('.la-11__done');
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
    bar.setAttribute('aria-valuenow', ready ? 100 : 62);
    bar.setAttribute('aria-valuetext', ready ? 'Brew complete' : '62 percent brewed');
    region.setAttribute('aria-label', ready ? 'Your flat white is ready at the bar' : 'Brewing your flat white');
  });
  sync();
})();
```
