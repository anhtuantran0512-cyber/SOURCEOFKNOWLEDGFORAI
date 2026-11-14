---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/the-safe-triangle-diagonal-pointer-problem/"
title: "The Safe Triangle Diagonal Pointer Problem"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Moving diagonally from a nav item to the far corner of its panel passes over sibling triggers, and a naive handler closes the panel mid-journey."
has_js: "true"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: The Safe Triangle Diagonal Pointer Problem
Source: https://codefronts.com/navigation/css-mega-menus/the-safe-triangle-diagonal-pointer-problem/

Moving diagonally from a nav item to the far corner of its panel passes over sibling triggers, and a naive handler closes the panel mid-journey. This fleet console tracks the pointer's trajectory and keeps the panel open while movement stays inside the triangle between the cursor and the panel's two near corners. Aim for the bottom-right link and the panel holds.
## HTML
```html
<section class="mm-03" aria-labelledby="mm-03-title">
  <h2 class="mm-03__sr" id="mm-03-title">Vale Logistics operations console</h2>

  <div class="mm-03__theme">
    <input class="mm-03__theme-input" type="checkbox" id="mm-03-theme">
    <label class="mm-03__theme-label" for="mm-03-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-03__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-03__header" data-mm03-mode="safe" data-mm03-guard="320">
    <svg class="mm-03__viz" aria-hidden="true" focusable="false"><polygon class="mm-03__tri" points=""></polygon></svg>

    <div class="mm-03__bar">
      <a class="mm-03__brand" href="#mm-03-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M2 16V8h11v8Zm11-5h4l3 3.2V16h-7Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="7" cy="18" r="1.8" fill="currentColor"/><circle cx="17" cy="18" r="1.8" fill="currentColor"/></svg>
        Vale <span>Logistics</span>
      </a>

      <nav class="mm-03__nav" aria-label="Primary">
        <ul class="mm-03__list">
          <li class="mm-03__item">
            <button class="mm-03__trigger" type="button" aria-expanded="false" aria-controls="mm-03-panel-fleet">Fleet</button>
            <div class="mm-03__panel" id="mm-03-panel-fleet" aria-label="Fleet">
              <p class="mm-03__panel-head">Fleet operations <span>14 tools &middot; 212 depots</span></p>
              <ul class="mm-03__links">
                <li><a href="#mm-03-title"><b>Live vehicle map</b><span>realtime</span></a></li>
                <li><a href="#mm-03-title"><b>Route planner</b><span>beta</span></a></li>
                <li><a href="#mm-03-title"><b>Driver hours</b><span>compliance</span></a></li>
                <li><a href="#mm-03-title"><b>Maintenance queue</b><span>32 open</span></a></li>
                <li><a href="#mm-03-title"><b>Fuel and charging</b><span>daily</span></a></li>
                <li><a href="#mm-03-title"><b>Depot capacity</b><span>weekly</span></a></li>
                <li><a href="#mm-03-title"><b>Incident reports</b><span>archive</span></a></li>
                <li><a href="#mm-03-title"><b>Cost per mile</b><span>finance</span></a></li>
              </ul>
            </div>
          </li>

          <li class="mm-03__item">
            <button class="mm-03__trigger" type="button" aria-expanded="false" aria-controls="mm-03-panel-network">Network</button>
            <div class="mm-03__panel" id="mm-03-panel-network" aria-label="Network">
              <p class="mm-03__panel-head">Network <span>6 tools</span></p>
              <ul class="mm-03__links">
                <li><a href="#mm-03-title"><b>Depot directory</b><span>212 sites</span></a></li>
                <li><a href="#mm-03-title"><b>Partner carriers</b><span>contracts</span></a></li>
                <li><a href="#mm-03-title"><b>Coverage gaps</b><span>planning</span></a></li>
                <li><a href="#mm-03-title"><b>Service levels</b><span>SLA</span></a></li>
              </ul>
            </div>
          </li>

          <li class="mm-03__item">
            <button class="mm-03__trigger" type="button" aria-expanded="false" aria-controls="mm-03-panel-reports">Reports</button>
            <div class="mm-03__panel" id="mm-03-panel-reports" aria-label="Reports">
              <p class="mm-03__panel-head">Reports <span>9 tools</span></p>
              <ul class="mm-03__links">
                <li><a href="#mm-03-title"><b>Weekly summary</b><span>PDF</span></a></li>
                <li><a href="#mm-03-title"><b>Utilisation</b><span>dashboard</span></a></li>
                <li><a href="#mm-03-title"><b>Emissions</b><span>export</span></a></li>
                <li><a href="#mm-03-title"><b>Custom query</b><span>SQL</span></a></li>
              </ul>
            </div>
          </li>

          <li class="mm-03__item"><a class="mm-03__plain" href="#mm-03-title">Settings</a></li>
        </ul>
      </nav>

      <div class="mm-03__utils">
        <span class="mm-03__shift">Shift B &middot; 06:00&ndash;14:00</span>
        <span class="mm-03__avatar" aria-hidden="true">JL</span>
      </div>
    </div>
  </header>

  <main class="mm-03__page">
    <div class="mm-03__kpis">
      <div class="mm-03__kpi"><dt>Vehicles moving</dt><dd>1,284</dd><span>+3.1% vs yesterday</span></div>
      <div class="mm-03__kpi"><dt>On-time rate</dt><dd>96.4%</dd><span>target 95%</span></div>
      <div class="mm-03__kpi mm-03__kpi--warn"><dt>Late at depot</dt><dd>37</dd><span>18 flagged for review</span></div>
      <div class="mm-03__kpi"><dt>Cost per mile</dt><dd>&pound;1.06</dd><span>&minus;2p this week</span></div>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-03 {
  --mm-03-bg: #17140f;
  --mm-03-surf: #211c15;
  --mm-03-panel: #f7f2e8;
  --mm-03-onpanel: #1c1710;
  --mm-03-line: #362e22;
  --mm-03-ink: #f3ede1;
  --mm-03-mut: #a3947c;
  --mm-03-acc: #f2a63b;
  --mm-03-acc: oklch(77% 0.15 70);
  --mm-03-on-acc: #12100e;
  --mm-03-panel-w: 34rem;
  --mm-03-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--mm-03-bg);
  background-image: radial-gradient(60rem 28rem at 82% -10%, rgba(242, 166, 59, 0.16), transparent 62%);
  color: var(--mm-03-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.mm-03 *,
.mm-03 *::before,
.mm-03 *::after {
  box-sizing: border-box;
}

.mm-03 :focus-visible {
  outline: 2px solid var(--mm-03-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.mm-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mm-03:has(.mm-03__theme-input:checked) {
  --mm-03-bg: #f6f3ec;
  --mm-03-surf: #ffffff;
  --mm-03-panel: #1c1710;
  --mm-03-onpanel: #f7f2e8;
  --mm-03-line: #ddd4c2;
  --mm-03-ink: #1c1710;
  --mm-03-mut: #6f6455;
  --mm-03-acc: #a1560a;
  --mm-03-acc: oklch(52% 0.14 60);
  --mm-03-on-acc: #ffffff;
}

@media (prefers-color-scheme: light) {
  .mm-03 {
    --mm-03-bg: #f6f3ec;
    --mm-03-surf: #ffffff;
    --mm-03-panel: #1c1710;
    --mm-03-onpanel: #f7f2e8;
    --mm-03-line: #ddd4c2;
    --mm-03-ink: #1c1710;
    --mm-03-mut: #6f6455;
    --mm-03-acc: #a1560a;
    --mm-03-acc: oklch(52% 0.14 60);
    --mm-03-on-acc: #ffffff;
  }

  .mm-03:has(.mm-03__theme-input:checked) {
    --mm-03-bg: #17140f;
    --mm-03-surf: #211c15;
    --mm-03-panel: #f7f2e8;
    --mm-03-onpanel: #1c1710;
    --mm-03-line: #362e22;
    --mm-03-ink: #f3ede1;
    --mm-03-mut: #a3947c;
    --mm-03-acc: #f2a63b;
    --mm-03-acc: oklch(77% 0.15 70);
    --mm-03-on-acc: #12100e;
  }
}

@media (prefers-color-scheme: dark) {
  .mm-03:has(.mm-03__theme-input:checked) {
    --mm-03-bg: #f6f3ec;
    --mm-03-surf: #ffffff;
    --mm-03-panel: #1c1710;
    --mm-03-onpanel: #f7f2e8;
    --mm-03-line: #ddd4c2;
    --mm-03-ink: #1c1710;
    --mm-03-mut: #6f6455;
    --mm-03-acc: #a1560a;
    --mm-03-acc: oklch(52% 0.14 60);
    --mm-03-on-acc: #ffffff;
  }
}

.mm-03__theme {
  position: absolute;
  inset-block-start: 12px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-03__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-03__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-03-line);
  border-radius: 4px;
  background: var(--mm-03-surf);
  color: var(--mm-03-ink);
  cursor: pointer;
}

.mm-03__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-03__theme-input:focus-visible + .mm-03__theme-label {
  outline: 2px solid var(--mm-03-acc);
  outline-offset: 3px;
}

.mm-03__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-03-surf);
  border-block-end: 1px solid var(--mm-03-line);
  padding-block-end: clamp(11rem, 26vw, 14rem);
}

.mm-03__viz {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  pointer-events: none;
  z-index: 40;
}

.mm-03__tri {
  fill: color-mix(in oklab, var(--mm-03-acc) 20%, transparent);
  stroke: var(--mm-03-acc);
  stroke-width: 1.5;
  stroke-dasharray: 5 4;
  opacity: 0;
}

.mm-03__bar {
  inline-size: min(84rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 2rem);
  flex-wrap: wrap;
  min-block-size: 60px;
  padding-inline-end: 60px;
}

.mm-03__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--mm-03-ink);
  text-decoration: none;
  font: 700 0.95rem/1 var(--mm-03-font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.mm-03__brand span {
  color: var(--mm-03-mut);
  font-weight: 400;
}

.mm-03__brand svg {
  inline-size: 22px;
  block-size: 22px;
  color: var(--mm-03-acc);
}

.mm-03__nav {
  min-inline-size: 0;
}

.mm-03__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-03__item {
  position: relative;
}

.mm-03__trigger,
.mm-03__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.9rem;
  border: 0;
  border-radius: 3px;
  background: transparent;
  color: var(--mm-03-ink);
  font: 600 0.88rem/1 system-ui, sans-serif;
  text-decoration: none;
  cursor: pointer;
}

.mm-03__item--open > .mm-03__trigger,
.mm-03__item:hover > .mm-03__trigger,
.mm-03__item:focus-within > .mm-03__trigger {
  background: var(--mm-03-acc);
  color: var(--mm-03-on-acc);
}

.mm-03__plain:hover,
.mm-03__trigger:hover {
  color: var(--mm-03-acc);
}

.mm-03__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.mm-03__shift {
  font: 500 0.72rem/1 var(--mm-03-font-display);
  letter-spacing: 0.06em;
  color: var(--mm-03-mut);
}

.mm-03__avatar {
  display: grid;
  place-items: center;
  inline-size: 32px;
  block-size: 32px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--mm-03-acc) 24%, transparent);
  color: var(--mm-03-acc);
  font: 700 0.72rem/1 var(--mm-03-font-display);
}

.mm-03__panel {
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: 0;
  z-index: 30;
  inline-size: min(var(--mm-03-panel-w), calc(100vw - 3rem));
  padding: clamp(0.85rem, 2.4vw, 1.15rem);
  background: var(--mm-03-panel);
  color: var(--mm-03-onpanel);
  border-radius: 4px;
  box-shadow: 0 30px 60px -30px rgba(0, 0, 0, 0.7);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(-6px);
  transition: opacity 150ms ease, transform 150ms ease, visibility 0s linear 150ms;
}

.mm-03__item--open > .mm-03__panel,
.mm-03__item:focus-within > .mm-03__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateY(0);
  transition-delay: 0s;
}

.mm-03__panel-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.75rem;
  margin: 0 0 0.6rem;
  font: 700 0.7rem/1 var(--mm-03-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.mm-03__panel-head span {
  font-weight: 400;
  opacity: 0.6;
}

.mm-03__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 2px;
}

.mm-03__links a {
  display: grid;
  align-content: center;
  gap: 1px;
  min-block-size: 46px;
  padding: 0.3rem 0.55rem;
  border-radius: 3px;
  color: var(--mm-03-onpanel);
  text-decoration: none;
  min-inline-size: 0;
}

.mm-03__links b {
  font: 600 0.88rem/1.2 system-ui, sans-serif;
}

.mm-03__links span {
  font: 500 0.62rem/1 var(--mm-03-font-display);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  opacity: 0.55;
}

.mm-03__links a:hover {
  background: color-mix(in oklab, var(--mm-03-acc) 34%, transparent);
}

.mm-03__page {
  inline-size: min(84rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(1.5rem, 5vw, 3rem);
}
/* Dividers are per-cell borders, not a 1px gap revealing the grid
   background: auto-fit leaves empty tracks at some widths and the bleed
   trick paints those as solid grey blocks. A transparent grid makes any
   item count safe. */

.mm-03__kpis {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
  gap: 0;
  background: transparent;
  border: 1px solid var(--mm-03-line);
  border-block-end: 0;
  border-inline-end: 0;
  border-radius: 4px;
  overflow: hidden;
}

.mm-03__kpi {
  border-inline-end: 1px solid var(--mm-03-line);
  border-block-end: 1px solid var(--mm-03-line);
  display: grid;
  gap: 2px;
  padding: 1rem 1.1rem;
  background: var(--mm-03-surf);
  min-inline-size: 0;
}

.mm-03__kpi dt {
  font: 600 0.64rem/1 var(--mm-03-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-03-mut);
}

.mm-03__kpi dd {
  margin: 0;
  font: 700 clamp(1.5rem, 4vw, 2rem)/1 var(--mm-03-font-display);
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
}

.mm-03__kpi span {
  font-size: 0.74rem;
  color: var(--mm-03-mut);
}

.mm-03__kpi--warn dd {
  color: var(--mm-03-acc);
}

@media (max-width: 52rem) {
  .mm-03__header {
    padding-block-end: 0;
  }

  .mm-03__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-03__list {
    flex-direction: column;
  }

  .mm-03__utils {
    margin-inline-start: 0;
  }

  .mm-03__panel {
    position: static;
    inline-size: 100%;
    opacity: 1;
    visibility: visible;
    transform: none;
    display: none;
    margin-block-start: 0.5rem;
  }

  .mm-03__item--open > .mm-03__panel,
    .mm-03__item:focus-within > .mm-03__panel {
    display: block;
  }

  .mm-03__links {
    grid-template-columns: minmax(0, 1fr);
  }

  .mm-03__viz {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-03__panel {
    transition-duration: 1ms;
  }
}
/* Panel alignment — start-aligned to its own trigger and clamped, with the panel narrowed below 60rem
   so item-left + panel-width can never exceed the bar. No ordinal flip (it pushes left-hand panels off
   the opposite edge) and no anchor position-try (the item is the containing block here, so no fallback
   can ever score better than the first). */

.mm-03__panel {
  inset-inline-start: 0;
  inset-inline-end: auto;
  max-inline-size: min(var(--mm-03-panel-w), calc(100vw - 3rem));
}

@media (max-width: 60rem) {
  .mm-03 {
    --mm-03-panel-w: 21rem;
  }
}
/* Entry signature — telemetry rows wipe open left to right on a hard linear clock */

.mm-03__links li {
  clip-path: inset(0 100% 0 0);
  opacity: 0;
  transition: clip-path 240ms linear, opacity 100ms linear;
}

.mm-03__item:hover > .mm-03__panel .mm-03__links li,
.mm-03__item:focus-within > .mm-03__panel .mm-03__links li,
.mm-03__item--open > .mm-03__panel .mm-03__links li {
  clip-path: inset(-8px);
  opacity: 1;
}

.mm-03__links li:nth-child(1) {
  transition-delay: 20ms;
}

.mm-03__links li:nth-child(2) {
  transition-delay: 60ms;
}

.mm-03__links li:nth-child(3) {
  transition-delay: 100ms;
}

.mm-03__links li:nth-child(4) {
  transition-delay: 140ms;
}

.mm-03__links li:nth-child(5) {
  transition-delay: 180ms;
}

.mm-03__links li:nth-child(6) {
  transition-delay: 220ms;
}

.mm-03__links li:nth-child(7) {
  transition-delay: 260ms;
}

.mm-03__links li:nth-child(8) {
  transition-delay: 300ms;
}

.mm-03__links li:nth-child(n+9) {
  transition-delay: 300ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-03__links li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-03__links li {
    clip-path: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.mm-03');
const header = root.querySelector('.mm-03__header');
const nav = root.querySelector('.mm-03__nav');
const tri = root.querySelector('.mm-03__tri');
let last = null, corners = null, guardT = 0, armed = false;
const guardMs = Number(header.dataset.mm03Guard || 320);

const setOpen = (item, on) => { item.classList.toggle('mm-03__item--open', on); item.querySelector('.mm-03__trigger').setAttribute('aria-expanded', String(on)); };
const openItem = (item) => {
  nav.querySelectorAll('.mm-03__item--open').forEach((i) => { if (i !== item) setOpen(i, false); });
  setOpen(item, true);
  const r = item.querySelector('.mm-03__panel').getBoundingClientRect();
  const h = header.getBoundingClientRect();
  corners = [[r.left - h.left, r.top - h.top], [r.right - h.left, r.top - h.top]];
};
const sign = (a, b, c) => (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1]);
const inside = (p) => {
  const d1 = sign(p, last, corners[0]), d2 = sign(p, corners[0], corners[1]), d3 = sign(p, corners[1], last);
  return !((d1 < 0 || d2 < 0 || d3 < 0) && (d1 > 0 || d2 > 0 || d3 > 0));
};

const onMove = (e) => {
  const h = header.getBoundingClientRect();
  const p = [e.clientX - h.left, e.clientY - h.top];
  if (header.dataset.mm03Mode === 'safe' && last && corners) {
    armed = inside(p);
    tri.setAttribute('points', last[0] + ',' + last[1] + ' ' + corners[0].join(',') + ' ' + corners[1].join(','));
    tri.style.opacity = armed ? '1' : '0';
    clearTimeout(guardT);
    guardT = setTimeout(() => { armed = false; tri.style.opacity = '0'; }, guardMs);
  }
  const item = e.target.closest('.mm-03__item');
  if (item && item.querySelector('.mm-03__panel') && !armed && !item.classList.contains('mm-03__item--open')) openItem(item);
  last = p;
};
const onKey = (e) => {
  if (e.key !== 'Escape') return;
  const open = nav.querySelector('.mm-03__item--open');
  if (!open) return;
  setOpen(open, false); open.querySelector('.mm-03__trigger').focus();
};
const onResize = () => { const open = nav.querySelector('.mm-03__item--open'); if (open) openItem(open); };

// Nothing closed the panel on the way out — only Escape did — so leaving
// the header left it open indefinitely. Close when the pointer genuinely
// leaves the header, keeping it open while focus is still inside.
const onLeave = (e) => {
  if (e.relatedTarget && header.contains(e.relatedTarget)) return;
  if (header.contains(document.activeElement)) return;
  clearTimeout(guardT); armed = false; last = null; tri.style.opacity = '0';
  nav.querySelectorAll('.mm-03__item--open').forEach((i) => setOpen(i, false));
};

header.addEventListener('pointermove', onMove);
header.addEventListener('pointerleave', onLeave);
nav.addEventListener('keydown', onKey);
window.addEventListener('resize', onResize);

root.__mmCleanup = () => {
  header.removeEventListener('pointermove', onMove);
  header.removeEventListener('pointerleave', onLeave);
  nav.removeEventListener('keydown', onKey);
  window.removeEventListener('resize', onResize);
  clearTimeout(guardT);
};
```
