---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/preloading-routes-so-transitions-never-stall/"
title: "Preloading Routes So Transitions Never Stall"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "A transition that waits on the network is not a transition, it is a stall with an overlay on top."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Preloading Routes So Transitions Never Stall
Source: https://codefronts.com/motion/css-page-transitions/preloading-routes-so-transitions-never-stall/

A transition that waits on the network is not a transition, it is a stall with an overlay on top. Intent-based prefetch fixes it: warm the next route on hover or on pointer-down, well before the click, then start the animation only once the content is in hand. The chart shows both numbers &mdash; how long the fetch took and how long the transition ran &mdash; so you can see which one the user actually waited on.
## HTML
```html
<section class="pt-06" aria-labelledby="pt-06-h">
  <div class="pt-06__theme">
    <input class="pt-06__theme-input" type="checkbox" id="pt-06-theme">
    <label class="pt-06__theme-label" for="pt-06-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-06__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-06__stage">
    <header class="pt-06__bar">
      <p class="pt-06__brand">Meridian</p>
      <nav class="pt-06__nav" aria-label="Marketing pages">
        <button class="pt-06__link pt-06__link--current" type="button" data-pt-06-route="platform">Platform</button>
        <button class="pt-06__link" type="button" data-pt-06-route="pricing">Pricing</button>
        <button class="pt-06__link" type="button" data-pt-06-route="customers">Customers</button>
      </nav>
    </header>

    <div class="pt-06__intro">
      <p class="pt-06__kicker">Page transitions / 06</p>
      <h2 class="pt-06__h" id="pt-06-h">Warm the route before the click</h2>
      <p class="pt-06__lede">Hover a nav item to warm it, then click. The chart records the simulated fetch and the animation separately. Routes are swapped in place by this demo&rsquo;s script &mdash; the &ldquo;network&rdquo; is a timer.</p>
    </div>

    <div class="pt-06__view">
      <div class="pt-06__overlay" aria-hidden="true"><span class="pt-06__spin"></span></div>
      <main class="pt-06__route" id="pt-06-route" tabindex="-1">
        <p class="pt-06__eyebrow">Platform</p>
        <h3 class="pt-06__title">One control plane for every region</h3>
        <p class="pt-06__text">Deploy once and Meridian places the workload against live latency data. No per-region configuration and no duplicated pipelines.</p>
        <ul class="pt-06__facts">
          <li><b>18</b><span>edge regions</span></li>
          <li><b>41ms</b><span>median p50</span></li>
          <li><b>99.98%</b><span>rolling uptime</span></li>
        </ul>
      </main>
    </div>

    <figure class="pt-06__chart">
      <figcaption class="pt-06__chart-cap">Last navigation</figcaption>
      <div class="pt-06__rows">
        <p class="pt-06__row"><span class="pt-06__row-k">fetch</span><span class="pt-06__row-bar" data-pt-06-bar="fetch"></span><span class="pt-06__row-v" data-pt-06-val="fetch">&mdash;</span></p>
        <p class="pt-06__row"><span class="pt-06__row-k">transition</span><span class="pt-06__row-bar pt-06__row-bar--pt-06-t" data-pt-06-bar="anim"></span><span class="pt-06__row-v" data-pt-06-val="anim">&mdash;</span></p>
      </div>
      <p class="pt-06__state" data-pt-06-state>Warm a link by hovering it. Cold routes take 700ms of simulated network.</p>
    </figure>
  </div>
</section>
```
## CSS
```css
.pt-06 {
  --pt-06-bg: #f4f7fd;
  --pt-06-s1: #ffffff;
  --pt-06-s2: #e8eefb;
  --pt-06-line: #cdd9f2;
  --pt-06-ink: #10182b;
  --pt-06-mut: #52627f;
  --pt-06-acc: #1f5cd8;
  --pt-06-warn: #b25a06;
  --pt-06-hard: 6px 6px 0 var(--pt-06-line);
  --pt-06-font-display: "Segoe UI", "Lucida Grande", "Frutiger", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-06-bg);
  color: var(--pt-06-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.pt-06 *,
.pt-06 *::before,
.pt-06 *::after {
  box-sizing: border-box;
}

.pt-06:has(.pt-06__theme-input:checked) {
  --pt-06-bg: #080c16;
  --pt-06-s1: #101725;
  --pt-06-s2: #172033;
  --pt-06-line: #24314e;
  --pt-06-ink: #e9eefb;
  --pt-06-mut: #94a3c2;
  --pt-06-acc: #79a2ff;
  --pt-06-warn: #e8a458;
  --pt-06-hard: 6px 6px 0 var(--pt-06-line);
}

@media (prefers-color-scheme: dark) {
  .pt-06 {
    --pt-06-bg: #080c16;
    --pt-06-s1: #101725;
    --pt-06-s2: #172033;
    --pt-06-line: #24314e;
    --pt-06-ink: #e9eefb;
    --pt-06-mut: #94a3c2;
    --pt-06-acc: #79a2ff;
    --pt-06-warn: #e8a458;
  }

  .pt-06:has(.pt-06__theme-input:checked) {
    --pt-06-bg: #f4f7fd;
    --pt-06-s1: #ffffff;
    --pt-06-s2: #e8eefb;
    --pt-06-line: #cdd9f2;
    --pt-06-ink: #10182b;
    --pt-06-mut: #52627f;
    --pt-06-acc: #1f5cd8;
    --pt-06-warn: #b25a06;
  }
}

@media (prefers-color-scheme: light) {
  .pt-06:has(.pt-06__theme-input:checked) {
    --pt-06-bg: #080c16;
    --pt-06-s1: #101725;
    --pt-06-s2: #172033;
    --pt-06-line: #24314e;
    --pt-06-ink: #e9eefb;
    --pt-06-mut: #94a3c2;
    --pt-06-acc: #79a2ff;
    --pt-06-warn: #e8a458;
  }
}

@supports (color: oklch(0.5 0.2 265)) {
  .pt-06 {
    --pt-06-acc: oklch(0.5 0.19 264);
  }

  .pt-06:has(.pt-06__theme-input:checked) {
    --pt-06-acc: oklch(0.76 0.13 264);
  }

  @media (prefers-color-scheme: dark) {
    .pt-06 {
      --pt-06-acc: oklch(0.76 0.13 264);
    }

    .pt-06:has(.pt-06__theme-input:checked) {
      --pt-06-acc: oklch(0.5 0.19 264);
    }
  }
}

.pt-06__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-06__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-06__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-06__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 2px solid var(--pt-06-ink);
  border-radius: 0.4rem;
  background: var(--pt-06-s1);
  color: var(--pt-06-ink);
  cursor: pointer;
  box-shadow: 4px 4px 0 var(--pt-06-ink);
}

.pt-06__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-06__theme-input:focus-visible + .pt-06__theme-label {
  outline: 2px solid var(--pt-06-acc);
  outline-offset: 3px;
}

.pt-06__stage {
  max-inline-size: 66rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.35rem;
}

.pt-06__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1.5rem;
  padding: 0.6rem 0.9rem;
  padding-inline-end: 4rem;
  background: var(--pt-06-s1);
  border: 2px solid var(--pt-06-ink);
  border-radius: 0.5rem;
  box-shadow: var(--pt-06-hard);
}

.pt-06__brand {
  margin: 0;
  font-family: var(--pt-06-font-display);
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -0.01em;
}

.pt-06__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  min-inline-size: 0;
}

.pt-06__link {
  min-block-size: 2.75rem;
  padding: 0.4rem 0.85rem;
  border: 0;
  border-radius: 0.35rem;
  background: transparent;
  color: var(--pt-06-mut);
  font: inherit;
  font-size: 0.9rem;
  cursor: pointer;
}

.pt-06__link:hover {
  background: var(--pt-06-s2);
  color: var(--pt-06-ink);
}

.pt-06__link:focus-visible {
  outline: 2px solid var(--pt-06-acc);
  outline-offset: 2px;
}

.pt-06__link--current {
  background: var(--pt-06-acc);
  color: #fff;
  font-weight: 600;
}

.pt-06__link[data-pt-06-warm] {
  box-shadow: inset 0 -2px 0 var(--pt-06-warn);
}

.pt-06__kicker {
  margin: 0 0 0.45rem;
  font-size: 0.73rem;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--pt-06-acc);
}

.pt-06__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-06-font-display);
  font-size: clamp(1.4rem, 4.4vw, 2.1rem);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.pt-06__lede {
  margin: 0;
  max-inline-size: 44rem;
  color: var(--pt-06-mut);
  font-size: 0.94rem;
  text-wrap: pretty;
}

.pt-06__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 16rem;
  background: var(--pt-06-s1);
  border: 2px solid var(--pt-06-ink);
  border-radius: 0.5rem;
  box-shadow: var(--pt-06-hard);
}

.pt-06__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: grid;
  place-items: center;
  background: var(--pt-06-ink);
  opacity: 0;
  pointer-events: none;
  transition: opacity 180ms linear;
}

.pt-06[data-pt-06-cover="1"] .pt-06__overlay {
  opacity: 1;
}

.pt-06__spin {
  inline-size: 1.4rem;
  block-size: 1.4rem;
  border-radius: 999px;
  border: 2px solid var(--pt-06-mut);
  border-block-start-color: var(--pt-06-bg);
  animation: pt-06-spin 700ms linear infinite;
  opacity: 0;
}

.pt-06[data-pt-06-slow="1"] .pt-06__spin {
  opacity: 1;
}

@keyframes pt-06-spin {
  to {
    transform: rotate(1turn);
  }
}

.pt-06__route {
  display: block;
  padding: clamp(1rem, 3vw, 1.75rem);
}

.pt-06__route:focus-visible {
  outline: 2px solid var(--pt-06-acc);
  outline-offset: -4px;
}

.pt-06__eyebrow {
  margin: 0 0 0.4rem;
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--pt-06-warn);
}

.pt-06__title {
  margin: 0 0 0.6rem;
  font-family: var(--pt-06-font-display);
  font-size: clamp(1.15rem, 3.4vw, 1.5rem);
  font-weight: 700;
  letter-spacing: -0.015em;
}

.pt-06__text {
  margin: 0 0 1rem;
  max-inline-size: 40rem;
  font-size: 0.93rem;
  color: var(--pt-06-mut);
  text-wrap: pretty;
}

.pt-06__facts {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 2rem;
}

.pt-06__facts li {
  min-inline-size: 0;
  display: grid;
}

.pt-06__facts b {
  font-family: var(--pt-06-font-display);
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--pt-06-acc);
  font-variant-numeric: tabular-nums;
}

.pt-06__facts span {
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--pt-06-mut);
}

.pt-06__chart {
  margin: 0;
  padding: 0.9rem 1rem;
  background: var(--pt-06-s2);
  border-radius: 0.5rem;
}

.pt-06__chart-cap {
  font-size: 0.72rem;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--pt-06-mut);
  margin-block-end: 0.6rem;
}

.pt-06__rows {
  display: grid;
  gap: 0.45rem;
}

.pt-06__row {
  margin: 0;
  display: grid;
  grid-template-columns: 5.5rem minmax(0, 1fr) 4.5rem;
  gap: 0.6rem;
  align-items: center;
}

.pt-06__row-k {
  font-size: 0.76rem;
  color: var(--pt-06-mut);
}

.pt-06__row-bar {
  display: block;
  block-size: 0.5rem;
  border-radius: 999px;
  background: var(--pt-06-line);
  position: relative;
  overflow: hidden;
}

.pt-06__row-bar::after {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  inline-size: var(--pt-06-fill, 0%);
  background: var(--pt-06-warn);
  transition: inline-size 220ms ease-out;
}

.pt-06__row-bar--pt-06-t::after {
  background: var(--pt-06-acc);
}

.pt-06__row-v {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.8rem;
  text-align: end;
  font-variant-numeric: tabular-nums;
}

.pt-06__state {
  margin: 0.7rem 0 0;
  font-size: 0.82rem;
  color: var(--pt-06-mut);
}

@media (prefers-reduced-motion: reduce) {
  .pt-06__overlay {
    transition-duration: 60ms;
  }

  .pt-06__spin {
    animation-duration: 1400ms;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-06');
const view = root.querySelector('#pt-06-route');
const links = [...root.querySelectorAll('[data-pt-06-route]')];
const state = root.querySelector('[data-pt-06-state]');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const cache = new Map(); const timers = []; let dwell;
const pages = {
  platform: ['Platform', 'One control plane for every region', 'Deploy once and Meridian places the workload against live latency data.'],
  pricing: ['Pricing', 'Usage billing, no seat minimums', 'Every plan includes all regions. You pay for requests served and bytes moved, invoiced monthly.'],
  customers: ['Customers', 'Teams running on Meridian', 'Fern moved 41 services in a quarter. Vale runs its checkout path here. Talon serves 2.1B monthly requests.']
};
const bar = (k, ms, cap) => { const b = root.querySelector('[data-pt-06-bar="' + k + '"]'); b.style.setProperty('--pt-06-fill', Math.min(100, ms / cap * 100) + '%'); root.querySelector('[data-pt-06-val="' + k + '"]').textContent = Math.round(ms) + 'ms'; };
const warm = (key, el) => { if (cache.has(key) || navigator.connection && navigator.connection.saveData) return;
  cache.set(key, new Promise((res) => timers.push(setTimeout(() => res(pages[key]), 700))));
  el.setAttribute('data-pt-06-warm', '1'); state.textContent = 'Warming ' + key + ' — link rel=prefetch injected on intent.'; };
async function go(key, btn) {
  const t0 = performance.now(); const hit = cache.has(key);
  if (!hit) warm(key, btn);
  root.setAttribute('data-pt-06-cover', '1');
  timers.push(setTimeout(() => { root.setAttribute('data-pt-06-slow', '1'); }, 220));
  let page; try { page = await cache.get(key); } catch (e) { page = null; }
  const fetched = performance.now() - t0;
  root.setAttribute('data-pt-06-slow', '0');
  if (!page) { root.setAttribute('data-pt-06-cover', '0'); state.textContent = 'Fetch failed — overlay cleared and the previous route kept.'; return; }
  links.forEach((l) => l.classList.toggle('pt-06__link--current', l === btn));
  view.innerHTML = '<p class="pt-06__eyebrow">' + page[0] + '</p><h3 class="pt-06__title">' + page[1] + '</h3><p class="pt-06__text">' + page[2] + '</p>';
  view.focus({ preventScroll: true });
  const anim = reduce.matches ? 60 : 300;
  timers.push(setTimeout(() => { root.setAttribute('data-pt-06-cover', '0'); }, anim));
  bar('fetch', fetched, 900); bar('anim', anim, 900);
  state.textContent = hit ? 'Prefetched — the user only waited on the animation.' : 'Cold — the transition was gated on the network.';
}
links.forEach((btn) => {
  const key = btn.getAttribute('data-pt-06-route');
  btn.addEventListener('pointerenter', () => { dwell = setTimeout(() => warm(key, btn), 90); });
  btn.addEventListener('pointerleave', () => clearTimeout(dwell));
  btn.addEventListener('pointerdown', () => warm(key, btn));
  btn.addEventListener('click', () => go(key, btn));
});
root.__ptCleanup = () => { clearTimeout(dwell); timers.forEach(clearTimeout); };
```
