---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/triangle-shatter/"
title: "Shatter Page Transition with Clip Path Tiles"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "The overlay is a grid of triangular shards rather than one panel."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shatter Page Transition with Clip Path Tiles
Source: https://codefronts.com/motion/css-page-transitions/triangle-shatter/

The overlay is a grid of triangular shards rather than one panel. Each shard is clipped with a polygon and animated on its own delay, so the cover assembles and the reveal breaks apart in sequence. It is the most decorative effect in the collection and also the most expensive per frame &mdash; the shard count is the cost, and the demo lets you feel where the limit is.
## HTML
```html
<section class="pt-17" aria-labelledby="pt-17-h">
  <div class="pt-17__theme">
    <input class="pt-17__theme-input" type="checkbox" id="pt-17-theme">
    <label class="pt-17__theme-label" for="pt-17-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-17__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-17__stage">
    <header class="pt-17__head">
      <p class="pt-17__kicker">Page transitions / 17</p>
      <h2 class="pt-17__h" id="pt-17-h">Shards, staggered</h2>
      <p class="pt-17__lede">Collections are DOM sections swapped by this demo&rsquo;s script once the grid has closed. Raise the shard count until your hardware complains &mdash; that number is the real limit.</p>
      <div class="pt-17__counts" role="group" aria-label="Shard count">
        <button class="pt-17__count pt-17__count--on" type="button" data-pt-17-tiles="24">24 shards</button>
        <button class="pt-17__count" type="button" data-pt-17-tiles="48">48</button>
        <button class="pt-17__count" type="button" data-pt-17-tiles="96">96</button>
      </div>
    </header>

    <div class="pt-17__view">
      <div class="pt-17__shatter" data-pt-17-grid aria-hidden="true"></div>
      <main class="pt-17__route" id="pt-17-route" tabindex="-1">
        <h3 class="pt-17__title">Sable / Objects</h3>
        <ul class="pt-17__grid">
          <li class="pt-17__card"><span class="pt-17__swatch pt-17__swatch--a"></span><b>Ceramic no.4</b><span>stoneware, 2026</span></li>
          <li class="pt-17__card"><span class="pt-17__swatch pt-17__swatch--b"></span><b>Bent ash stool</b><span>ash, brass</span></li>
          <li class="pt-17__card"><span class="pt-17__swatch pt-17__swatch--c"></span><b>Paper weight</b><span>cast iron</span></li>
          <li class="pt-17__card"><span class="pt-17__swatch pt-17__swatch--d"></span><b>Wall clock</b><span>steel, glass</span></li>
        </ul>
      </main>
    </div>

    <nav class="pt-17__tabs" aria-label="Collections">
      <button class="pt-17__tab pt-17__tab--current" type="button" data-pt-17-route="objects">Objects</button>
      <button class="pt-17__tab" type="button" data-pt-17-route="textiles">Textiles</button>
      <button class="pt-17__tab" type="button" data-pt-17-route="lighting">Lighting</button>
    </nav>
  </div>
</section>
```
## CSS
```css
.pt-17 {
  --pt-17-bg: #1c1a17;
  --pt-17-s1: #24211d;
  --pt-17-s2: #2e2a24;
  --pt-17-line: #3d372e;
  --pt-17-ink: #f0ebe1;
  --pt-17-mut: #a49a89;
  --pt-17-acc: #e8a13c;
  --pt-17-acc2: #7d8f6a;
  --pt-17-font-display: "Helvetica Neue", "Arial", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-17-bg);
  background-image: repeating-linear-gradient(45deg, rgba(255, 255, 255, 0.014) 0 2px, transparent 2px 4px);
  color: var(--pt-17-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-17 *,
.pt-17 *::before,
.pt-17 *::after {
  box-sizing: border-box;
}

.pt-17:has(.pt-17__theme-input:checked) {
  --pt-17-bg: #f5f2ec;
  --pt-17-s1: #ffffff;
  --pt-17-s2: #ebe6dc;
  --pt-17-line: #d8d1c2;
  --pt-17-ink: #1b1915;
  --pt-17-mut: #6b6354;
  --pt-17-acc: #99621a;
  --pt-17-acc2: #4d5c3c;
  background-image: repeating-linear-gradient(45deg, rgba(0, 0, 0, 0.014) 0 2px, transparent 2px 4px);
}

@media (prefers-color-scheme: light) {
  .pt-17 {
    background-image: repeating-linear-gradient(45deg, rgba(255, 255, 255, 0.014) 0 2px, transparent 2px 4px);
  }

  .pt-17:has(.pt-17__theme-input:checked) {
    --pt-17-bg: #f5f2ec;
    --pt-17-s1: #ffffff;
    --pt-17-s2: #ebe6dc;
    --pt-17-line: #d8d1c2;
    --pt-17-ink: #1b1915;
    --pt-17-mut: #6b6354;
    --pt-17-acc: #99621a;
    --pt-17-acc2: #4d5c3c;
  }
}

@media (prefers-color-scheme: dark) {
  .pt-17:has(.pt-17__theme-input:checked) {
    --pt-17-bg: #f5f2ec;
    --pt-17-s1: #ffffff;
    --pt-17-s2: #ebe6dc;
    --pt-17-line: #d8d1c2;
    --pt-17-ink: #1b1915;
    --pt-17-mut: #6b6354;
    --pt-17-acc: #99621a;
    --pt-17-acc2: #4d5c3c;
  }
}

@supports (color: oklch(0.75 0.13 70)) {
  .pt-17 {
    --pt-17-acc: oklch(0.77 0.13 68);
  }

  .pt-17:has(.pt-17__theme-input:checked) {
    --pt-17-acc: oklch(0.53 0.11 68);
  }

  @media (prefers-color-scheme: dark) {
    .pt-17:has(.pt-17__theme-input:checked) {
      --pt-17-acc: oklch(0.53 0.11 68);
    }
  }
}

.pt-17__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-17__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-17__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-17__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-17-line);
  background: var(--pt-17-s1);
  color: var(--pt-17-acc);
  cursor: pointer;
}

.pt-17__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-17__theme-input:focus-visible + .pt-17__theme-label {
  outline: 2px solid var(--pt-17-acc);
  outline-offset: 2px;
}

.pt-17__stage {
  max-inline-size: 66rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.2rem;
}

.pt-17__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-17-font-display);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--pt-17-acc);
}

.pt-17__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-17-font-display);
  font-size: clamp(1.4rem, 4.4vw, 2.1rem);
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.pt-17__lede {
  margin: 0 0 0.9rem;
  max-inline-size: 42rem;
  color: var(--pt-17-mut);
  font-size: 0.92rem;
  text-wrap: pretty;
}

.pt-17__counts {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pt-17__count {
  min-block-size: 2.75rem;
  padding: 0.4rem 0.9rem;
  border: 1px solid var(--pt-17-line);
  background: transparent;
  color: var(--pt-17-mut);
  font-family: var(--pt-17-font-display);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
}

.pt-17__count--on {
  background: var(--pt-17-acc);
  border-color: var(--pt-17-acc);
  color: var(--pt-17-bg);
}

.pt-17__count:focus-visible {
  outline: 2px solid var(--pt-17-acc);
  outline-offset: 2px;
}

.pt-17__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 17rem;
  background: var(--pt-17-s1);
  border: 1px solid var(--pt-17-line);
}

.pt-17__shatter {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
}

.pt-17__shard {
  position: absolute;
  background: var(--pt-17-acc);
  opacity: 0;
  transform: scale(0.4);
}

.pt-17__shard:nth-child(even) {
  background: var(--pt-17-ink);
}

.pt-17[data-pt-17-phase="cover"] .pt-17__shard {
  animation: pt-17-close 260ms ease-out both;
  animation-delay: var(--pt-17-d);
}

.pt-17[data-pt-17-phase="open"] .pt-17__shard {
  animation: pt-17-open 300ms ease-in both;
  animation-delay: var(--pt-17-d);
}

@keyframes pt-17-close {
  from {
    opacity: 0;
    transform: scale(0.4);
  }

  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes pt-17-open {
  from {
    opacity: 1;
    transform: scale(1);
  }

  to {
    opacity: 0;
    transform: scale(0.4) rotate(8deg);
  }
}

.pt-17__route {
  display: block;
  padding: clamp(1rem, 3vw, 1.6rem);
}

.pt-17__route:focus-visible {
  outline: 2px solid var(--pt-17-acc);
  outline-offset: -3px;
}

.pt-17__title {
  margin: 0 0 1rem;
  font-family: var(--pt-17-font-display);
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--pt-17-mut);
}

.pt-17__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.75rem;
}

@media (min-width: 34rem) {
  .pt-17__grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

.pt-17__card {
  min-inline-size: 0;
  display: grid;
  gap: 0.3rem;
}

.pt-17__swatch {
  display: block;
  block-size: 5rem;
  background: var(--pt-17-s2);
}

.pt-17__swatch--a {
  background: linear-gradient(140deg, #c9a227, #5a4a1f);
}

.pt-17__swatch--b {
  background: linear-gradient(140deg, #9c8060, #4a3a2a);
}

.pt-17__swatch--c {
  background: linear-gradient(140deg, #6f7a6a, #2c332a);
}

.pt-17__swatch--d {
  background: linear-gradient(140deg, #8f9298, #3a3d42);
}

.pt-17__card b {
  font-family: var(--pt-17-font-display);
  font-size: 0.86rem;
  font-weight: 700;
  letter-spacing: 0.04em;
}

.pt-17__card span:last-child {
  font-size: 0.74rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--pt-17-mut);
}

.pt-17__tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pt-17__tab {
  flex: 1 1 8rem;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  border: 1px solid var(--pt-17-line);
  background: transparent;
  color: var(--pt-17-mut);
  font-family: var(--pt-17-font-display);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  cursor: pointer;
}

.pt-17__tab--current {
  background: var(--pt-17-s2);
  color: var(--pt-17-ink);
}

.pt-17__tab:focus-visible {
  outline: 2px solid var(--pt-17-acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .pt-17[data-pt-17-phase="cover"] .pt-17__shard,
    .pt-17[data-pt-17-phase="open"] .pt-17__shard {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-17');
const grid = root.querySelector('[data-pt-17-grid]');
const view = root.querySelector('#pt-17-route');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = []; let cols = 8, rows = 3, busy = false;
const pages = { objects: ['Sable / Objects', [['a', 'Ceramic no.4', 'stoneware, 2026'], ['b', 'Bent ash stool', 'ash, brass'], ['c', 'Paper weight', 'cast iron'], ['d', 'Wall clock', 'steel, glass']]],
  textiles: ['Sable / Textiles', [['c', 'Flax throw', 'undyed linen'], ['b', 'Wool runner', 'hand loomed'], ['d', 'Cotton sheet', 'stone washed'], ['a', 'Silk square', 'screen printed']]],
  lighting: ['Sable / Lighting', [['d', 'Disc sconce', 'brushed steel'], ['a', 'Paper lantern', 'washi, ash'], ['b', 'Table lamp', 'walnut base'], ['c', 'Track spot', 'matte black']]] };
function build(total) {
  cols = total === 24 ? 8 : total === 48 ? 12 : 16;
  rows = total / cols;
  grid.innerHTML = '';
  const w = 100 / cols, h = 100 / rows;
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
    const s = document.createElement('span');
    s.className = 'pt-17__shard';
    s.style.cssText = 'left:' + (c * w - 0.1) + '%;top:' + (r * h - 0.1) + '%;width:' + (w + 0.2) + '%;height:' + (h + 0.2) + '%;' +
      'clip-path:polygon(' + ((r + c) % 2 ? '0 0, 100% 0, 0 100%' : '100% 0, 100% 100%, 0 100%') + ');--pt-17-d:' + ((c + r) * 14) + 'ms';
    grid.appendChild(s);
  }
}
function go(key, btn) {
  if (busy || btn.classList.contains('pt-17__tab--current')) return;
  busy = true;
  const last = (cols + rows - 2) * 14 + 260;
  root.setAttribute('data-pt-17-phase', 'cover');
  timers.push(setTimeout(() => {
    const [title, cards] = pages[key];
    view.innerHTML = '<h3 class="pt-17__title">' + title + '</h3><ul class="pt-17__grid">' + cards.map((c) => '<li class="pt-17__card"><span class="pt-17__swatch pt-17__swatch--' + c[0] + '"></span><b>' + c[1] + '</b><span>' + c[2] + '</span></li>').join('') + '</ul>';
    root.querySelectorAll('[data-pt-17-route]').forEach((t) => t.classList.toggle('pt-17__tab--current', t === btn));
    view.focus({ preventScroll: true });
    root.setAttribute('data-pt-17-phase', 'open');
    timers.push(setTimeout(() => { root.setAttribute('data-pt-17-phase', 'idle'); busy = false; }, reduce.matches ? 40 : last));
  }, reduce.matches ? 40 : last));
}
root.querySelectorAll('[data-pt-17-tiles]').forEach((b) => b.addEventListener('click', () => {
  build(Number(b.getAttribute('data-pt-17-tiles')));
  root.querySelectorAll('[data-pt-17-tiles]').forEach((x) => x.classList.toggle('pt-17__count--on', x === b));
}));
root.querySelectorAll('[data-pt-17-route]').forEach((b) => b.addEventListener('click', () => go(b.getAttribute('data-pt-17-route'), b)));
build(24);
root.__ptCleanup = () => { timers.forEach(clearTimeout); grid.innerHTML = ''; };
```
