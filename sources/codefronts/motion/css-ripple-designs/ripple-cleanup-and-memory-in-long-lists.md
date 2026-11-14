---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/ripple-cleanup-and-memory-in-long-lists/"
title: "Ripple Cleanup and Memory in Long Lists"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Every click that appends a ring leaves a node behind unless something removes it."
has_js: "true"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Cleanup and Memory in Long Lists
Source: https://codefronts.com/motion/css-ripple-designs/ripple-cleanup-and-memory-in-long-lists/

Every click that appends a ring leaves a node behind unless something removes it. This build shows the animationend listener with once: true, the fallback timeout for when the animation never fires at all, and a live count of ripple nodes so the leak is visible. The rows share one delegated listener, because 500 rows means 500 listeners otherwise.
## HTML
```html
<section class="rpl-06" aria-labelledby="rpl-06-title">
  <input class="rpl-06__theme-input" type="checkbox" id="rpl-06-theme">
  <label class="rpl-06__theme" for="rpl-06-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-06__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-06__app">
    <header class="rpl-06__head">
      <div>
        <p class="rpl-06__eyebrow">Everyday account</p>
        <h1 class="rpl-06__balance" id="rpl-06-title">$4,182.60</h1>
      </div>
      <button class="rpl-06__filter" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 6h16M7 12h10m-7 6h4"/></svg>
        Filter
      </button>
    </header>
    <p class="rpl-06__group">Today</p>
    <ul class="rpl-06__list" id="rpl-06-list">
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="a" aria-hidden="true">GB</span><span class="rpl-06__txt"><span class="rpl-06__name">Greenbelt Market</span><span class="rpl-06__sub">Groceries &middot; 11:24</span></span><span class="rpl-06__amt">&minus;$46.20</span></button></li>
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="b" aria-hidden="true">TF</span><span class="rpl-06__txt"><span class="rpl-06__name">Transit Fare</span><span class="rpl-06__sub">Travel &middot; 09:02</span></span><span class="rpl-06__amt">&minus;$3.40</span></button></li>
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="c" aria-hidden="true">AV</span><span class="rpl-06__txt"><span class="rpl-06__name">Avery Lund</span><span class="rpl-06__sub">Transfer received &middot; 08:41</span></span><span class="rpl-06__amt rpl-06__amt--in">+$120.00</span></button></li>
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="d" aria-hidden="true">NR</span><span class="rpl-06__txt"><span class="rpl-06__name">Northline Rent</span><span class="rpl-06__sub">Housing &middot; 08:00</span></span><span class="rpl-06__amt">&minus;$1,480.00</span></button></li>
    </ul>
    <p class="rpl-06__group">Yesterday</p>
    <ul class="rpl-06__list" id="rpl-06-list-b">
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="e" aria-hidden="true">KO</span><span class="rpl-06__txt"><span class="rpl-06__name">Kōhī Roasters</span><span class="rpl-06__sub">Cafés &middot; 17:55</span></span><span class="rpl-06__amt">&minus;$8.75</span></button></li>
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="f" aria-hidden="true">SP</span><span class="rpl-06__txt"><span class="rpl-06__name">Spool Studio</span><span class="rpl-06__sub">Subscriptions &middot; 12:10</span></span><span class="rpl-06__amt">&minus;$19.00</span></button></li>
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="g" aria-hidden="true">HW</span><span class="rpl-06__txt"><span class="rpl-06__name">Harbour Works</span><span class="rpl-06__sub">Payroll &middot; 09:30</span></span><span class="rpl-06__amt rpl-06__amt--in">+$2,940.00</span></button></li>
      <li><button class="rpl-06__row" type="button"><span class="rpl-06__av" data-c="h" aria-hidden="true">MD</span><span class="rpl-06__txt"><span class="rpl-06__name">Mera Dental</span><span class="rpl-06__sub">Health &middot; 08:15</span></span><span class="rpl-06__amt">&minus;$210.00</span></button></li>
    </ul>
  </div>
</section>
```
## CSS
```css
.rpl-06 {
  --rpl-06-bg: #ffffff;
  --rpl-06-bg: oklch(1 0 0);
  --rpl-06-panel: #f7f8fa;
  --rpl-06-panel: oklch(0.978 0.003 265);
  --rpl-06-line: #e8eaef;
  --rpl-06-line: oklch(0.925 0.005 265);
  --rpl-06-fg: #0f1115;
  --rpl-06-fg: oklch(0.19 0.008 265);
  --rpl-06-muted: #5c626e;
  --rpl-06-muted: oklch(0.515 0.014 265);
  --rpl-06-accent: #3b3bd8;
  --rpl-06-accent: oklch(0.46 0.20 275);
  --rpl-06-in: #12734f;
  --rpl-06-in: oklch(0.50 0.12 160);
  --rpl-06-ink: rgba(59, 59, 216, 0.13);
  --rpl-06-ink: oklch(0.46 0.20 275 / 0.13);
  --rpl-06-dur: 560ms;
  position: relative;
  display: grid;
  place-items: start center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 44px);
  background: var(--rpl-06-bg);
  color: var(--rpl-06-fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-06 *,
.rpl-06 *::before,
.rpl-06 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-06:not(:has(#rpl-06-theme:checked)) {
    --rpl-06-bg: #0b0c0f;
    --rpl-06-bg: oklch(0.165 0.006 265);
    --rpl-06-panel: #14161b;
    --rpl-06-panel: oklch(0.215 0.008 265);
    --rpl-06-line: #23262e;
    --rpl-06-line: oklch(0.285 0.010 265);
    --rpl-06-fg: #f0f2f6;
    --rpl-06-fg: oklch(0.955 0.004 265);
    --rpl-06-muted: #949aa6;
    --rpl-06-muted: oklch(0.70 0.012 265);
    --rpl-06-accent: #9aa3ff;
    --rpl-06-accent: oklch(0.78 0.13 277);
    --rpl-06-in: #5fd6a4;
    --rpl-06-in: oklch(0.80 0.12 162);
    --rpl-06-ink: rgba(154, 163, 255, 0.16);
    --rpl-06-ink: oklch(0.78 0.13 277 / 0.16);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-06:has(#rpl-06-theme:checked) {
    --rpl-06-bg: #0b0c0f;
    --rpl-06-bg: oklch(0.165 0.006 265);
    --rpl-06-panel: #14161b;
    --rpl-06-panel: oklch(0.215 0.008 265);
    --rpl-06-line: #23262e;
    --rpl-06-line: oklch(0.285 0.010 265);
    --rpl-06-fg: #f0f2f6;
    --rpl-06-fg: oklch(0.955 0.004 265);
    --rpl-06-muted: #949aa6;
    --rpl-06-muted: oklch(0.70 0.012 265);
    --rpl-06-accent: #9aa3ff;
    --rpl-06-accent: oklch(0.78 0.13 277);
    --rpl-06-in: #5fd6a4;
    --rpl-06-in: oklch(0.80 0.12 162);
    --rpl-06-ink: rgba(154, 163, 255, 0.16);
    --rpl-06-ink: oklch(0.78 0.13 277 / 0.16);
  }
}

.rpl-06__app {
  inline-size: 100%;
  max-inline-size: 560px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.rpl-06__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  padding: clamp(12px, 3vw, 24px) 4px clamp(16px, 3vw, 26px);
}

.rpl-06__eyebrow {
  margin: 0 0 6px;
  font-size: 12px;
  color: var(--rpl-06-muted);
}

.rpl-06__balance {
  margin: 0;
  font-size: clamp(30px, 6vw, 42px);
  font-weight: 620;
  letter-spacing: -0.035em;
  font-variant-numeric: tabular-nums;
}

.rpl-06__filter {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-block-size: 40px;
  padding: 0 14px;
  border: 1px solid var(--rpl-06-line);
  border-radius: 999px;
  background: var(--rpl-06-bg);
  color: var(--rpl-06-fg);
  font: inherit;
  font-size: 13px;
  cursor: pointer;
}

.rpl-06__filter svg {
  inline-size: 16px;
  block-size: 16px;
}

.rpl-06__filter:focus-visible {
  outline: 2px solid var(--rpl-06-accent);
  outline-offset: 2px;
}

.rpl-06__group {
  margin: 14px 4px 4px;
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--rpl-06-muted);
}

.rpl-06__list {
  margin: 0;
  padding: 6px;
  list-style: none;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--rpl-06-line);
  border-radius: 18px;
  background: var(--rpl-06-panel);
}

.rpl-06__row {
  position: relative;
  inline-size: 100%;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 64px;
  padding: 12px 14px;
  border: 0;
  border-radius: 13px;
  background: transparent;
  color: inherit;
  font: inherit;
  text-align: start;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  -webkit-tap-highlight-color: transparent;
}

.rpl-06__row:focus-visible {
  outline: 2px solid var(--rpl-06-accent);
  outline-offset: -2px;
}

.rpl-06__av {
  display: grid;
  place-items: center;
  inline-size: 38px;
  block-size: 38px;
  flex: none;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--rpl-06-fg);
  background: color-mix(in oklab, var(--rpl-06-accent) 14%, transparent);
  pointer-events: none;
}

.rpl-06__av[data-c="b"] {
  background: color-mix(in oklab, oklch(0.70 0.16 40) 20%, transparent);
}

.rpl-06__av[data-c="c"] {
  background: color-mix(in oklab, var(--rpl-06-in) 20%, transparent);
}

.rpl-06__av[data-c="d"] {
  background: color-mix(in oklab, oklch(0.70 0.15 320) 20%, transparent);
}

.rpl-06__av[data-c="e"] {
  background: color-mix(in oklab, oklch(0.70 0.13 75) 22%, transparent);
}

.rpl-06__av[data-c="f"] {
  background: color-mix(in oklab, oklch(0.70 0.13 220) 20%, transparent);
}

.rpl-06__av[data-c="g"] {
  background: color-mix(in oklab, var(--rpl-06-in) 20%, transparent);
}

.rpl-06__av[data-c="h"] {
  background: color-mix(in oklab, oklch(0.72 0.12 190) 22%, transparent);
}

.rpl-06__txt {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-inline-size: 0;
  flex: 1;
  pointer-events: none;
}

.rpl-06__name {
  font-size: 14.5px;
  font-weight: 550;
  letter-spacing: -0.01em;
}

.rpl-06__sub {
  font-size: 12.5px;
  color: var(--rpl-06-muted);
}

.rpl-06__amt {
  font-size: 14.5px;
  font-weight: 550;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
  pointer-events: none;
}

.rpl-06__amt--in {
  color: var(--rpl-06-in);
}

.rpl-06__ring {
  position: absolute;
  left: var(--rpl-06-x, 50%);
  top: var(--rpl-06-y, 50%);
  inline-size: calc(var(--rpl-06-r, 120px) * 2);
  block-size: calc(var(--rpl-06-r, 120px) * 2);
  border-radius: 50%;
  background: var(--rpl-06-ink);
  pointer-events: none;
  z-index: -1;
  animation: rpl-06-expand var(--rpl-06-dur) cubic-bezier(0.14, 0.7, 0.3, 1) forwards;
}

@keyframes rpl-06-expand {
  from {
    transform: translate(-50%, -50%) scale(0);
    opacity: 1;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rpl-06__ring {
    display: none;
  }

  .rpl-06__row:active {
    background: color-mix(in oklab, var(--rpl-06-accent) 12%, transparent);
  }
}

.rpl-06 {
  position: relative;
}

.rpl-06__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-06__theme {
  position: absolute;
  z-index: 60;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
}

.rpl-06__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-06__theme:active {
  transform: scale(0.94);
}

.rpl-06__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-06__theme-input:checked + .rpl-06__theme svg {
  transform: rotate(180deg);
}

.rpl-06__theme-input:focus-visible + .rpl-06__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-06__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-06__theme,
    .rpl-06__theme svg {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.rpl-06');
const lists = [root.querySelector('#rpl-06-list'), root.querySelector('#rpl-06-list-b')];
const timers = new Set();

const drop = (event) => {
  const row = event.target.closest('.rpl-06__row');
  if (!row || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = row.getBoundingClientRect();
  const x = event.clientX - box.left;
  const y = event.clientY - box.top;
  const r = Math.max(Math.hypot(x, y), Math.hypot(box.width - x, y), Math.hypot(x, box.height - y), Math.hypot(box.width - x, box.height - y));
  const old = row.querySelectorAll('.rpl-06__ring');
  if (old.length >= 3) old[0].remove();
  const ring = document.createElement('span');
  ring.className = 'rpl-06__ring';
  ring.setAttribute('aria-hidden', 'true');
  ring.style.setProperty('--rpl-06-x', x + 'px');
  ring.style.setProperty('--rpl-06-y', y + 'px');
  ring.style.setProperty('--rpl-06-r', r + 'px');
  ring.addEventListener('animationend', () => ring.remove(), { once: true });
  const t = setTimeout(() => { timers.delete(t); ring.remove(); }, 1300);
  timers.add(t);
  row.append(ring);
};

lists.forEach((list) => list.addEventListener('pointerdown', drop));
root.__rplCleanup = () => { lists.forEach((list) => list.removeEventListener('pointerdown', drop)); timers.forEach(clearTimeout); timers.clear(); };
```
