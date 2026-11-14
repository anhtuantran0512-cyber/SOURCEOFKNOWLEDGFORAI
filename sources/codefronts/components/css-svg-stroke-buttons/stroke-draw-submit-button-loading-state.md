---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-submit-button-loading-state/"
title: "Stroke Draw Submit Button Loading State"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A checkout button with three real states carried entirely by its own outline: idle draws on hover, pending sends a quarter-perimeter segment orbiting the…"
has_js: "true"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stroke Draw Submit Button Loading State
Source: https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-submit-button-loading-state/

A checkout button with three real states carried entirely by its own outline: idle draws on hover, pending sends a quarter-perimeter segment orbiting the pill, and success closes the frame in mint and draws a tick while the label swaps to the amount paid. The script only sets data-state, aria-busy and a live-region sentence — every pixel of motion is CSS.
## HTML
```html
<section class="svgb-15">
  <input class="svgb-15__ti" type="checkbox" id="svgb-15-theme">
  <label class="svgb-15__toggle" for="svgb-15-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-15__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-15__stage">
    <div class="svgb-15__checkout">
      <p class="svgb-15__store">Northlight Supply</p>
      <ul class="svgb-15__lines">
        <li class="svgb-15__line">
          <img class="svgb-15__thumb" src="https://picsum.photos/seed/svgb15lamp/200/200" alt="" width="200" height="200" loading="lazy" decoding="async">
          <span class="svgb-15__ln">Arc desk lamp <em>&times;1</em></span>
          <span class="svgb-15__lp">&euro;148.00</span>
        </li>
        <li class="svgb-15__line">
          <img class="svgb-15__thumb" src="https://picsum.photos/seed/svgb15shade/200/200" alt="" width="200" height="200" loading="lazy" decoding="async">
          <span class="svgb-15__ln">Linen shade <em>&times;2</em></span>
          <span class="svgb-15__lp">&euro;62.00</span>
        </li>
      </ul>
      <div class="svgb-15__totals">
        <span>Subtotal</span><span>&euro;210.00</span>
        <span>Shipping</span><span>&euro;9.50</span>
        <span class="svgb-15__grand">Total</span><span class="svgb-15__grand">&euro;219.50</span>
      </div>

      <div class="svgb-15__pay">
        <button class="svgb-15__btn" type="button" data-state="idle">
          <svg class="svgb-15__frame" viewBox="0 0 300 68" aria-hidden="true">
            <rect class="svgb-15__base" x="2" y="2" width="296" height="64" rx="32" pathLength="1"/>
            <rect class="svgb-15__ink" x="2" y="2" width="296" height="64" rx="32" pathLength="1"/>
            <rect class="svgb-15__spin" x="2" y="2" width="296" height="64" rx="32" pathLength="1"/>
          </svg>
          <span class="svgb-15__labels">
            <span class="svgb-15__l svgb-15__l--idle">Pay &euro;219.50</span>
            <span class="svgb-15__l svgb-15__l--busy">Authorising</span>
            <span class="svgb-15__l svgb-15__l--done">Paid</span>
          </span>
          <svg class="svgb-15__tick" viewBox="0 0 24 24" aria-hidden="true">
            <path class="svgb-15__tickline" d="M5 12.5 10 17.5 19 7.5" pathLength="1"/>
          </svg>
        </button>
        <p class="svgb-15__status" role="status" aria-live="polite">Card &bull;&bull;&bull;&bull; 4242 &middot; ready</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700&family=JetBrains+Mono:wght@400&display=swap');

.svgb-15 {
  --svgb-15-bg: #07100d;
  --svgb-15-bg: oklch(0.16 0.02 165);
  --svgb-15-fg: #eaf2ee;
  --svgb-15-fg: oklch(0.95 0.012 165);
  --svgb-15-muted: #85978f;
  --svgb-15-muted: oklch(0.655 0.018 165);
  --svgb-15-card: #0e1815;
  --svgb-15-card: oklch(0.215 0.022 165);
  --svgb-15-rest: rgba(234, 242, 238, 0.14);
  --svgb-15-rest: oklch(0.95 0.012 165 / 0.14);
  --svgb-15-stroke: #57e3a8;
  --svgb-15-stroke: oklch(0.85 0.15 160);
  --svgb-15-ok: #9dff6f;
  --svgb-15-ok: oklch(0.91 0.19 132);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-15-bg);
  position: relative;
  color: var(--svgb-15-fg);
  font-family: 'Manrope', system-ui, sans-serif;
}

.svgb-15 *,
.svgb-15 *::before,
.svgb-15 *::after {
  box-sizing: border-box;
}

.svgb-15__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px, 5vw, 68px);
}

.svgb-15__checkout {
  width: 100%;
  max-width: 460px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: clamp(22px, 4vw, 34px);
  border-radius: 26px;
  background: var(--svgb-15-card);
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.05), 0 34px 80px -50px #000;
}

.svgb-15__store {
  margin: 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--svgb-15-muted);
}

.svgb-15__lines {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.svgb-15__line {
  display: grid;
  grid-template-columns: 44px 1fr auto;
  gap: 14px;
  align-items: center;
}

.svgb-15__thumb {
  inline-size: 44px;
  block-size: 44px;
  border-radius: 12px;
  object-fit: cover;
}

.svgb-15__ln {
  font-size: 14.5px;
}

.svgb-15__ln em {
  font-style: normal;
  color: var(--svgb-15-muted);
}

.svgb-15__lp {
  font-size: 14px;
  font-variant-numeric: tabular-nums;
  color: var(--svgb-15-muted);
}

.svgb-15__totals {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 7px 16px;
  padding-block: 16px;
  border-block: 1px solid var(--svgb-15-rest);
  font-size: 13.5px;
  color: var(--svgb-15-muted);
  font-variant-numeric: tabular-nums;
}

.svgb-15__grand {
  font-size: 17px;
  font-weight: 700;
  color: var(--svgb-15-fg);
}

.svgb-15__pay {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
}

.svgb-15__btn {
  position: relative;
  inline-size: min(300px, 100%);
  block-size: 68px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 999px;
  background: color-mix(in oklab, var(--svgb-15-stroke) 14%, transparent);
  color: inherit;
  font: inherit;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.01em;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition: background 260ms ease;
}

.svgb-15__btn:focus-visible {
  outline: 2px solid var(--svgb-15-stroke);
  outline-offset: 4px;
}

.svgb-15__btn[disabled] {
  cursor: default;
}

.svgb-15__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-15__frame rect {
  fill: none;
  stroke-linecap: round;
}

.svgb-15__base {
  stroke: var(--svgb-15-rest);
  stroke-width: 1.5px;
}

.svgb-15__ink {
  stroke: var(--svgb-15-stroke);
  stroke-width: 2.2px;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 620ms cubic-bezier(0.22, 1, 0.36, 1), stroke 300ms ease;
}

.svgb-15__btn[data-state='idle']:hover .svgb-15__ink,
.svgb-15__btn[data-state='idle']:focus-visible .svgb-15__ink {
  stroke-dashoffset: 0;
}

.svgb-15__spin {
  stroke: var(--svgb-15-stroke);
  stroke-width: 2.6px;
  stroke-dasharray: 0.25 0.75;
  stroke-dashoffset: 0;
  opacity: 0;
}

@keyframes svgb-15-orbit {
  to {
    stroke-dashoffset: -1;
  }
}

.svgb-15__labels {
  position: relative;
  z-index: 1;
  display: grid;
}

.svgb-15__l {
  grid-area: 1 / 1;
  opacity: 0;
  transition: opacity 200ms ease;
}

.svgb-15__l--idle {
  opacity: 1;
}

.svgb-15__tick {
  position: absolute;
  z-index: 1;
  inset-inline-end: 22px;
  inset-block-start: 50%;
  translate: 0 -50%;
  inline-size: 22px;
  block-size: 22px;
  opacity: 0;
  transition: opacity 200ms ease;
}

.svgb-15__tickline {
  fill: none;
  stroke: var(--svgb-15-ok);
  stroke-width: 2.6px;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 420ms cubic-bezier(0.22, 1, 0.36, 1) 120ms;
}

.svgb-15__btn[data-state='busy'] {
  background: color-mix(in oklab, var(--svgb-15-stroke) 7%, transparent);
}

.svgb-15__btn[data-state='busy'] .svgb-15__spin {
  opacity: 1;
  animation: svgb-15-orbit 1.1s linear infinite;
}

.svgb-15__btn[data-state='busy'] .svgb-15__l--idle {
  opacity: 0;
}

.svgb-15__btn[data-state='busy'] .svgb-15__l--busy {
  opacity: 1;
}

.svgb-15__btn[data-state='done'] {
  background: color-mix(in oklab, var(--svgb-15-ok) 14%, transparent);
}

.svgb-15__btn[data-state='done'] .svgb-15__ink {
  stroke: var(--svgb-15-ok);
  stroke-dashoffset: 0;
  transition-duration: 300ms;
}

.svgb-15__btn[data-state='done'] .svgb-15__l--idle {
  opacity: 0;
}

.svgb-15__btn[data-state='done'] .svgb-15__l--done {
  opacity: 1;
}

.svgb-15__btn[data-state='done'] .svgb-15__tick {
  opacity: 1;
}

.svgb-15__btn[data-state='done'] .svgb-15__tickline {
  stroke-dashoffset: 0;
}

.svgb-15__btn[data-state='done'] .svgb-15__labels {
  translate: -14px 0;
  transition: translate 300ms cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-15__status {
  margin: 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  color: var(--svgb-15-muted);
}

.svgb-15__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-15__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 20%, transparent);
  background: color-mix(in oklab, currentColor 7%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-15__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-15__toggle:active {
  transform: scale(0.94);
}

.svgb-15__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-15__ti:checked + .svgb-15__toggle svg {
  transform: rotate(180deg);
}

.svgb-15__ti:focus-visible + .svgb-15__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-15:has(#svgb-15-theme:checked) {
  --svgb-15-bg: #eef3f0;
  --svgb-15-bg: oklch(0.95 0.008 165);
  --svgb-15-fg: #0f1714;
  --svgb-15-fg: oklch(0.19 0.018 165);
  --svgb-15-muted: #566159;
  --svgb-15-muted: oklch(0.49 0.016 160);
  --svgb-15-card: #ffffff;
  --svgb-15-card: oklch(1 0 0);
  --svgb-15-rest: rgba(15, 23, 20, 0.14);
  --svgb-15-rest: oklch(0.19 0.018 165 / 0.14);
  --svgb-15-stroke: #0a6b4b;
  --svgb-15-stroke: oklch(0.46 0.12 162);
  --svgb-15-ok: #2f6b12;
  --svgb-15-ok: oklch(0.48 0.15 132);
}

.svgb-15:has(#svgb-15-theme:checked) .svgb-15__checkout {
  box-shadow: 0 1px 2px oklch(0 0 0 / 0.05), 0 30px 70px -50px oklch(0 0 0 / 0.4);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-15__ink,
    .svgb-15__tickline,
    .svgb-15__labels,
    .svgb-15__btn {
    transition: none;
  }

  .svgb-15__spin {
    animation: none !important;
    stroke-dasharray: 0.5 0.5;
  }

  .svgb-15__btn[data-state='busy'] .svgb-15__spin {
    opacity: 0.7;
  }

  .svgb-15__toggle,
    .svgb-15__toggle svg {
    transition: none;
  }
}
```

## JavaScript
```js
/* State machine only: the script never animates, it just sets data-state and ARIA. */
(function () {
  var root = document.querySelector('.svgb-15');
  if (!root) return;
  var btn = root.querySelector('.svgb-15__btn');
  var status = root.querySelector('.svgb-15__status');
  var timers = new Set();

  function later(fn, ms) {
    var id = setTimeout(function () { timers.delete(id); fn(); }, ms);
    timers.add(id);
  }

  function setState(state, message) {
    btn.dataset.state = state;
    btn.setAttribute('aria-busy', state === 'busy' ? 'true' : 'false');
    btn.disabled = state === 'busy';
    status.textContent = message;
  }

  btn.addEventListener('click', function () {
    if (btn.dataset.state !== 'idle') return;
    setState('busy', 'Authorising with your bank');
    later(function () {
      setState('done', 'Paid EUR 219.50 - receipt sent');
      later(function () { setState('idle', 'Card 4242 - ready'); }, 2600);
    }, 1800);
  });

  root.__svgb15Cleanup = function () {
    timers.forEach(clearTimeout);
    timers.clear();
  };
})();
```
