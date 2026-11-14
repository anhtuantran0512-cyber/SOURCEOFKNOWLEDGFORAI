---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/promo-bar-with-countdown-timer/"
title: "Promo Bar with Countdown Timer"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A sale bar where the digits are rendered by CSS counters, not text nodes: JavaScript writes a single integer into a custom property and CSS prints it with…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Promo Bar with Countdown Timer
Source: https://codefronts.com/snippets/css-banners-alerts/promo-bar-with-countdown-timer/

A sale bar where the digits are rendered by CSS counters, not text nodes: JavaScript writes a single integer into a custom property and CSS prints it with counter(v, decimal-leading-zero). That makes the flip animation a registered-property transition, keeps the DOM untouched sixty times a minute, and gives you a countdown that never reflows because every cell is tabular-nums in a fixed ch box.
## HTML
```html
<div class="ba-02">
  <div class="ba-02__bar" role="region" aria-labelledby="ba-02-h">
    <p class="ba-02__lead">
      <span class="ba-02__flag">Mid-season</span>
      <span id="ba-02-h" class="ba-02__msg"><strong>Up to 40% off</strong> outerwear &amp; knitwear</span>
    </p>

    <div class="ba-02__clock" data-clock>
      <span class="ba-02__cell"><b></b><span>days</span></span>
      <span class="ba-02__sep" aria-hidden="true">:</span>
      <span class="ba-02__cell"><b></b><span>hrs</span></span>
      <span class="ba-02__sep" aria-hidden="true">:</span>
      <span class="ba-02__cell"><b></b><span>min</span></span>
      <span class="ba-02__sep" aria-hidden="true">:</span>
      <span class="ba-02__cell ba-02__cell--sec"><b></b><span>sec</span></span>
    </div>

    <div class="ba-02__cta">
      <button class="ba-02__code" type="button" data-copy="MIDSEASON40">
        <span class="ba-02__codeLabel">Code</span>
        <span class="ba-02__codeVal">MIDSEASON40</span>
        <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><rect x="7" y="7" width="9" height="9" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M13 7V5.5A1.5 1.5 0 0 0 11.5 4H5.5A1.5 1.5 0 0 0 4 5.5v6A1.5 1.5 0 0 0 5.5 13H7" stroke="currentColor" stroke-width="1.5"/></svg>
        <span class="ba-02__vh">Copy discount code MIDSEASON40</span>
      </button>
      <a class="ba-02__shop" href="#ba-02-h">Shop the sale<svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      <button class="ba-02__x" type="button" data-close aria-label="Dismiss offer bar">
        <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m6 6 8 8m0-8-8 8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>

  <p class="ba-02__live" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=DM+Sans:opsz,[email protected],400;9..40,500;9..40,700&display=swap');

@property --ba-02-v {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --ba-02-sweep {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.ba-02 {
  --bg: #faf7f2;
  --ink: #12100e;
  --bar: #12100e;
  --bar-ink: #fdfbf7;
  --muted: #8a8378;
  --line: #e6e0d6;
  --acc: #e8ff45;
  --urgent: #ff5a3c;
  --bar-radius: 1.15rem;
  --display: "Space Grotesk",ui-sans-serif,system-ui,sans-serif;
  --sans: "DM Sans",ui-sans-serif,system-ui,-apple-system,sans-serif;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  align-content: center;
  box-sizing: border-box;
  overflow-x: clip;
  padding: clamp(1rem,4vw,3rem) 0;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-02 *,
.ba-02 *::before,
.ba-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-02 {
    --bg: oklch(97.5% .01 85);
    --ink: oklch(17% .012 60);
    --bar: oklch(17% .012 60);
    --muted: oklch(60% .015 70);
    --line: oklch(91% .012 80);
    --acc: oklch(93% .19 108);
    --urgent: oklch(66% .21 32);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-02:not([data-theme="light"]) {
    --bg: #0c0b0a;
    --ink: #f6f3ee;
    --bar: #191614;
    --bar-ink: #f6f3ee;
    --muted: #9c948a;
    --line: #282320;
  }
}

.ba-02[data-theme="dark"] {
  --bg: #0c0b0a;
  --ink: #f6f3ee;
  --bar: #191614;
  --bar-ink: #f6f3ee;
  --muted: #9c948a;
  --line: #282320;
}

.ba-02__bar {
  position: relative;
  z-index: 4;
  width: min(72rem,100% - clamp(1.5rem,6vw,3rem));
  margin-inline: auto;
  padding: .7rem .8rem .7rem 1rem;
  display: grid;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: clamp(.75rem,2.5cqw,2rem);
  border-radius: var(--bar-radius);
  background: var(--bar);
  color: var(--bar-ink);
  box-shadow: 0 1.25rem 2.5rem -1.5rem rgb(0 0 0 / .45);
  overflow: hidden;
}

.ba-02__bar::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(100deg,transparent 20%,color-mix(in oklab,var(--acc) 22%,transparent) 46%,transparent 72%);
  translate: -120% 0;
  animation: ba-02-sheen 7s cubic-bezier(.5,0,.5,1) infinite;
}

@keyframes ba-02-sheen {
  0%,
    72% {
    translate: -120% 0;
  }

  100% {
    translate: 120% 0;
  }
}

.ba-02__bar[hidden] {
  display: none;
}

.ba-02__lead {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .65rem;
  min-width: 0;
  flex-wrap: wrap;
}

.ba-02__flag {
  flex: none;
  font-family: var(--display);
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  padding: .3rem .5rem;
  border-radius: .4rem;
  background: var(--acc);
  color: #12100e;
}

.ba-02__msg {
  font-size: clamp(.8125rem,1.6cqw,.9375rem);
  line-height: 1.35;
  letter-spacing: -.01em;
  min-width: 0;
}

.ba-02__msg strong {
  font-family: var(--display);
  font-weight: 700;
}

.ba-02__clock {
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .3rem;
  font-variant-numeric: tabular-nums;
}

.ba-02__cell {
  position: relative;
  display: grid;
  justify-items: center;
  gap: .1rem;
  min-width: 2.9ch;
  padding: .35rem .45rem;
  border-radius: .6rem;
  background: color-mix(in oklab,var(--bar-ink) 9%,transparent);
}

.ba-02__cell b {
  counter-reset: v var(--ba-02-v);
  font-family: var(--display);
  font-size: clamp(.9375rem,2cqw,1.25rem);
  font-weight: 700;
  letter-spacing: .01em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.ba-02__cell b::after {
  content: counter(v,decimal-leading-zero);
}

.ba-02__cell > span {
  font-size: .5625rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--bar-ink) 62%,transparent);
}

.ba-02__sep {
  opacity: .35;
  font-weight: 700;
  translate: 0 -.35rem;
}

.ba-02__cell--sec {
  background: conic-gradient(from -90deg, var(--acc) var(--ba-02-sweep), color-mix(in oklab,var(--bar-ink) 9%,transparent) 0) border-box;
  padding: 2px;
  transition: --ba-02-sweep 1s linear;
}

.ba-02__cell--sec > * {
  position: relative;
  z-index: 1;
}

.ba-02__cell--sec::before {
  content: "";
  position: absolute;
  inset: 2px;
  border-radius: .5rem;
  background: var(--bar);
  z-index: 0;
}

.ba-02__cell--sec b {
  animation: ba-02-flip .5s cubic-bezier(.16,1,.3,1);
}

@keyframes ba-02-flip {
  from {
    translate: 0 -.35rem;
    opacity: .2;
  }

  to {
    translate: 0 0;
    opacity: 1;
  }
}

.ba-02__bar[data-urgent] .ba-02__flag {
  background: var(--urgent);
  color: #fff;
}

.ba-02__bar[data-urgent] .ba-02__cell--sec {
  --acc: var(--urgent);
}

.ba-02__cta {
  display: flex;
  align-items: center;
  gap: .45rem;
}

.ba-02__code {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  padding: .5rem .7rem;
  font: inherit;
  font-size: .75rem;
  cursor: pointer;
  border-radius: .7rem;
  color: var(--bar-ink);
  border: 1px dashed color-mix(in oklab,var(--bar-ink) 38%,transparent);
  background: transparent;
  transition: border-color .2s ease, background .2s ease;
}

.ba-02__code:hover {
  border-color: var(--acc);
  background: color-mix(in oklab,var(--acc) 12%,transparent);
}

.ba-02__codeLabel {
  letter-spacing: .1em;
  text-transform: uppercase;
  font-size: .5625rem;
  color: color-mix(in oklab,var(--bar-ink) 60%,transparent);
}

.ba-02__codeVal {
  font-family: var(--display);
  font-weight: 700;
  letter-spacing: .04em;
}

.ba-02__code svg {
  width: 1rem;
  height: 1rem;
}

.ba-02__code[data-copied] {
  border-style: solid;
  border-color: var(--acc);
}

.ba-02__code[data-copied] .ba-02__codeVal::after {
  content: " ✓";
}

.ba-02__shop {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-height: 2.5rem;
  padding: .55rem .9rem;
  border-radius: .7rem;
  background: var(--acc);
  color: #12100e;
  text-decoration: none;
  font-size: .8125rem;
  font-weight: 700;
  font-family: var(--display);
  letter-spacing: -.01em;
  transition: translate .22s cubic-bezier(.16,1,.3,1), box-shadow .22s ease;
}

.ba-02__shop svg {
  width: 1.0625rem;
  height: 1.0625rem;
  transition: translate .25s cubic-bezier(.16,1,.3,1);
}

.ba-02__shop:hover {
  translate: 0 -1px;
  box-shadow: 0 .6rem 1.4rem -.6rem color-mix(in oklab,var(--acc) 70%,transparent);
}

.ba-02__shop:hover svg {
  translate: .2rem 0;
}

.ba-02__x {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .7rem;
  cursor: pointer;
  background: transparent;
  border: 1px solid transparent;
  color: color-mix(in oklab,var(--bar-ink) 60%,transparent);
}

.ba-02__x:hover {
  color: var(--bar-ink);
  background: color-mix(in oklab,var(--bar-ink) 10%,transparent);
}

.ba-02__x svg {
  width: 1.125rem;
  height: 1.125rem;
}

.ba-02 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-02__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 62rem) {
  .ba-02__bar {
    grid-template-columns: 1fr auto;
    row-gap: .6rem;
  }

  .ba-02__lead {
    grid-column: 1 / -1;
  }

  .ba-02__shop span {
    display: none;
  }
}

@container (max-width: 30rem) {
  .ba-02__shop {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-02 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-02__bar {
    border: 1px solid CanvasText;
  }

  .ba-02__flag,
    .ba-02__shop {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-02');
  if (!root) return;
  const bar = root.querySelector('.ba-02__bar');
  const cells = [...root.querySelectorAll('[data-clock] .ba-02__cell')];
  const live = root.querySelector('.ba-02__live');
  const DEADLINE = Date.now() + 1000 * 60 * 60 * 26 + 42000; // swap for a real ISO date

  const tick = () => {
    const left = Math.max(0, DEADLINE - Date.now());
    const s = Math.floor(left / 1000);
    const v = [Math.floor(s / 86400), Math.floor(s / 3600) % 24, Math.floor(s / 60) % 60, s % 60];
    cells.forEach((c, i) => c.style.setProperty('--ba-02-v', v[i]));
    cells[3].style.setProperty('--ba-02-sweep', (v[3] / 60) * 100 + '%');
    bar.toggleAttribute('data-urgent', left < 3600000);
    if (!left) { live.textContent = 'This offer has ended.'; root.querySelectorAll('.ba-02__shop,.ba-02__code').forEach((n) => n.setAttribute('aria-disabled', 'true')); return; }
    requestAnimationFrame(() => setTimeout(tick, 1000 - (Date.now() % 1000)));
  };
  tick();

  root.addEventListener('click', async (e) => {
    const copy = e.target.closest('[data-copy]');
    if (copy) {
      try { await navigator.clipboard.writeText(copy.dataset.copy); } catch (_) {}
      copy.dataset.copied = '1';
      live.textContent = 'Code ' + copy.dataset.copy + ' copied to clipboard.';
      setTimeout(() => delete copy.dataset.copied, 2200);
    }
    if (e.target.closest('[data-close]')) { bar.hidden = true; live.textContent = 'Offer bar dismissed.'; }
  });
})();
```
