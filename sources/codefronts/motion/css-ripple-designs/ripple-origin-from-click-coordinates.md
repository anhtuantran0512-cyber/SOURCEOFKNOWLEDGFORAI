---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/ripple-origin-from-click-coordinates/"
title: "Ripple Origin from Click Coordinates"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "A click carries two numbers and a ripple needs exactly those two."
has_js: "true"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Origin from Click Coordinates
Source: https://codefronts.com/motion/css-ripple-designs/ripple-origin-from-click-coordinates/

A click carries two numbers and a ripple needs exactly those two. This build reads the pointer position against the container box, writes it into two custom properties, and scales a ring from zero to a radius computed to reach the furthest corner. The readout prints the coordinates and the radius as you click, including the case where a too-small radius leaves a corner untouched.
## HTML
```html
<section class="rpl-01" aria-labelledby="rpl-01-title">
  <input class="rpl-01__theme-input" type="checkbox" id="rpl-01-theme">
  <label class="rpl-01__theme" for="rpl-01-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-01__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-01__shell">
    <header class="rpl-01__bar">
      <span class="rpl-01__mark" aria-hidden="true"></span>
      <span class="rpl-01__brand">Atlas</span>
      <nav class="rpl-01__nav" aria-label="Sections">
        <span class="rpl-01__nav-item rpl-01__nav-item--on">Overview</span>
        <span class="rpl-01__nav-item">Services</span>
        <span class="rpl-01__nav-item">Logs</span>
      </nav>
      <span class="rpl-01__avatar" aria-hidden="true">KM</span>
    </header>
    <div class="rpl-01__head">
      <h1 class="rpl-01__h1" id="rpl-01-title">Good afternoon, Kira</h1>
      <p class="rpl-01__sub">Six workspaces synced &middot; last check 40s ago</p>
    </div>
    <div class="rpl-01__grid" id="rpl-01-grid">
      <button class="rpl-01__tile" type="button">
        <span class="rpl-01__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 7h16M4 12h16M4 17h10"/></svg></span>
        <span class="rpl-01__label">Deployments</span>
        <span class="rpl-01__meta">12 active</span>
      </button>
      <button class="rpl-01__tile" type="button">
        <span class="rpl-01__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></span>
        <span class="rpl-01__label">Scheduler</span>
        <span class="rpl-01__meta">4 queued</span>
      </button>
      <button class="rpl-01__tile" type="button">
        <span class="rpl-01__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 18V8m5 10V5m5 13v-7m5 7V9"/></svg></span>
        <span class="rpl-01__label">Analytics</span>
        <span class="rpl-01__meta">+18.4%</span>
      </button>
      <button class="rpl-01__tile" type="button">
        <span class="rpl-01__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M9 12h6"/></svg></span>
        <span class="rpl-01__label">Storage</span>
        <span class="rpl-01__meta">2.1 TB free</span>
      </button>
      <button class="rpl-01__tile" type="button">
        <span class="rpl-01__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l8 4v5c0 5-3.4 8.2-8 9-4.6-.8-8-4-8-9V7Z"/></svg></span>
        <span class="rpl-01__label">Access</span>
        <span class="rpl-01__meta">31 members</span>
      </button>
      <button class="rpl-01__tile" type="button">
        <span class="rpl-01__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 3v3m0 12v3M3 12h3m12 0h3M5.6 5.6l2.1 2.1m8.6 8.6 2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/></svg></span>
        <span class="rpl-01__label">Settings</span>
        <span class="rpl-01__meta">Workspace</span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-01 {
  --rpl-01-bg: #0b0d12;
  --rpl-01-bg: oklch(0.16 0.014 268);
  --rpl-01-tile: #14171f;
  --rpl-01-tile: oklch(0.215 0.016 268);
  --rpl-01-line: #232833;
  --rpl-01-line: oklch(0.29 0.017 268);
  --rpl-01-fg: #eef1f6;
  --rpl-01-fg: oklch(0.96 0.006 268);
  --rpl-01-muted: #939bab;
  --rpl-01-muted: oklch(0.70 0.017 268);
  --rpl-01-accent: #8b9dff;
  --rpl-01-accent: oklch(0.75 0.145 275);
  --rpl-01-ink: rgba(139, 157, 255, 0.30);
  --rpl-01-ink: oklch(0.75 0.145 275 / 0.30);
  --rpl-01-dur: 640ms;
  --rpl-01-ease: cubic-bezier(0.12, 0.72, 0.28, 1);
  position: relative;
  display: flex;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(18px, 4vw, 56px);
  background: radial-gradient(120% 90% at 15% 0%, oklch(0.26 0.05 278 / 0.55), transparent 62%), var(--rpl-01-bg);
  color: var(--rpl-01-fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-01 *,
.rpl-01 *::before,
.rpl-01 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .rpl-01:not(:has(#rpl-01-theme:checked)) {
    --rpl-01-bg: #f4f5f9;
    --rpl-01-bg: oklch(0.965 0.005 268);
    --rpl-01-tile: #ffffff;
    --rpl-01-tile: oklch(1 0 0);
    --rpl-01-line: #e0e3ec;
    --rpl-01-line: oklch(0.905 0.008 268);
    --rpl-01-fg: #12151c;
    --rpl-01-fg: oklch(0.20 0.014 268);
    --rpl-01-muted: #676f80;
    --rpl-01-muted: oklch(0.55 0.017 268);
    --rpl-01-accent: #4a4fe0;
    --rpl-01-accent: oklch(0.50 0.20 274);
    --rpl-01-ink: rgba(74, 79, 224, 0.20);
    --rpl-01-ink: oklch(0.50 0.20 274 / 0.20);
    background: radial-gradient(120% 90% at 15% 0%, oklch(0.90 0.05 278 / 0.7), transparent 62%), var(--rpl-01-bg);
  }
}

@media (prefers-color-scheme: dark) {
  .rpl-01:has(#rpl-01-theme:checked) {
    --rpl-01-bg: #f4f5f9;
    --rpl-01-bg: oklch(0.965 0.005 268);
    --rpl-01-tile: #ffffff;
    --rpl-01-tile: oklch(1 0 0);
    --rpl-01-line: #e0e3ec;
    --rpl-01-line: oklch(0.905 0.008 268);
    --rpl-01-fg: #12151c;
    --rpl-01-fg: oklch(0.20 0.014 268);
    --rpl-01-muted: #676f80;
    --rpl-01-muted: oklch(0.55 0.017 268);
    --rpl-01-accent: #4a4fe0;
    --rpl-01-accent: oklch(0.50 0.20 274);
    --rpl-01-ink: rgba(74, 79, 224, 0.20);
    --rpl-01-ink: oklch(0.50 0.20 274 / 0.20);
    background: radial-gradient(120% 90% at 15% 0%, oklch(0.90 0.05 278 / 0.7), transparent 62%), var(--rpl-01-bg);
  }
}

.rpl-01__shell {
  inline-size: 100%;
  max-inline-size: 1180px;
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 3.5vw, 40px);
}

.rpl-01__bar {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  min-inline-size: 0;
}

.rpl-01__mark {
  inline-size: 26px;
  block-size: 26px;
  border-radius: 9px;
  background: linear-gradient(140deg, var(--rpl-01-accent), oklch(0.62 0.19 330));
  flex: none;
}

.rpl-01__brand {
  font-size: 15px;
  font-weight: 650;
  letter-spacing: -0.01em;
}

.rpl-01__nav {
  display: flex;
  gap: 4px;
  margin-inline-start: 12px;
}

.rpl-01__nav-item {
  padding: 7px 12px;
  border-radius: 999px;
  font-size: 13px;
  color: var(--rpl-01-muted);
}

.rpl-01__nav-item--on {
  background: var(--rpl-01-tile);
  color: var(--rpl-01-fg);
  border: 1px solid var(--rpl-01-line);
}

.rpl-01__avatar {
  margin-inline-start: auto;
  display: grid;
  place-items: center;
  inline-size: 34px;
  block-size: 34px;
  border-radius: 50%;
  background: var(--rpl-01-tile);
  border: 1px solid var(--rpl-01-line);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.rpl-01__head {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rpl-01__h1 {
  margin: 0;
  font-size: clamp(28px, 5vw, 46px);
  font-weight: 620;
  letter-spacing: -0.03em;
  line-height: 1.05;
}

.rpl-01__sub {
  margin: 0;
  font-size: 14px;
  color: var(--rpl-01-muted);
}

.rpl-01__grid {
  display: grid;
  gap: clamp(12px, 1.6vw, 18px);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 230px), 1fr));
}

.rpl-01__tile {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-block-size: clamp(150px, 20vh, 190px);
  padding: 20px;
  border: 1px solid var(--rpl-01-line);
  border-radius: 20px;
  background: var(--rpl-01-tile);
  color: inherit;
  font: inherit;
  text-align: start;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  transition: border-color 160ms ease, transform 160ms ease;
}

.rpl-01__tile:hover {
  border-color: color-mix(in oklab, var(--rpl-01-accent) 45%, var(--rpl-01-line));
}

.rpl-01__tile:active {
  transform: scale(0.994);
}

.rpl-01__tile:focus-visible {
  outline: 2px solid var(--rpl-01-accent);
  outline-offset: 3px;
}

.rpl-01__ico {
  display: grid;
  place-items: center;
  inline-size: 36px;
  block-size: 36px;
  border-radius: 11px;
  background: color-mix(in oklab, var(--rpl-01-accent) 16%, transparent);
  color: var(--rpl-01-accent);
  pointer-events: none;
}

.rpl-01__ico svg {
  inline-size: 19px;
  block-size: 19px;
}

.rpl-01__label {
  margin-block-start: auto;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: -0.01em;
  pointer-events: none;
}

.rpl-01__meta {
  font-size: 13px;
  color: var(--rpl-01-muted);
  font-variant-numeric: tabular-nums;
  pointer-events: none;
}

.rpl-01__ring {
  position: absolute;
  left: var(--rpl-01-x, 50%);
  top: var(--rpl-01-y, 50%);
  inline-size: calc(var(--rpl-01-r, 90px) * 2);
  block-size: calc(var(--rpl-01-r, 90px) * 2);
  border-radius: 50%;
  background: var(--rpl-01-ink);
  pointer-events: none;
  z-index: 0;
  animation: rpl-01-expand var(--rpl-01-dur) var(--rpl-01-ease) forwards;
}

@keyframes rpl-01-expand {
  from {
    transform: translate(-50%, -50%) scale(0);
    opacity: 1;
  }

  60% {
    opacity: 0.42;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rpl-01__ring {
    display: none;
  }

  .rpl-01__tile {
    transition: none;
  }

  .rpl-01__tile:active {
    background: color-mix(in oklab, var(--rpl-01-accent) 18%, var(--rpl-01-tile));
    transform: none;
  }
}

.rpl-01 {
  position: relative;
}

.rpl-01__bar {
  padding-inline-end: 52px;
}

.rpl-01__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-01__theme {
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

.rpl-01__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-01__theme:active {
  transform: scale(0.94);
}

.rpl-01__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-01__theme-input:checked + .rpl-01__theme svg {
  transform: rotate(180deg);
}

.rpl-01__theme-input:focus-visible + .rpl-01__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-01__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-01__theme,
    .rpl-01__theme svg {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.rpl-01');
const grid = root.querySelector('#rpl-01-grid');
const timers = new Set();

const drop = (event) => {
  const tile = event.target.closest('.rpl-01__tile');
  if (!tile || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = tile.getBoundingClientRect();
  const x = event.clientX - box.left;
  const y = event.clientY - box.top;
  const r = Math.max(Math.hypot(x, y), Math.hypot(box.width - x, y), Math.hypot(x, box.height - y), Math.hypot(box.width - x, box.height - y));
  const rings = tile.querySelectorAll('.rpl-01__ring');
  if (rings.length >= 4) rings[0].remove();
  const ring = document.createElement('span');
  ring.className = 'rpl-01__ring';
  ring.setAttribute('aria-hidden', 'true');
  ring.style.setProperty('--rpl-01-x', x + 'px');
  ring.style.setProperty('--rpl-01-y', y + 'px');
  ring.style.setProperty('--rpl-01-r', r + 'px');
  ring.addEventListener('animationend', () => ring.remove(), { once: true });
  const t = setTimeout(() => { timers.delete(t); ring.remove(); }, 1400);
  timers.add(t);
  tile.append(ring);
};

grid.addEventListener('pointerdown', drop);
root.__rplCleanup = () => { grid.removeEventListener('pointerdown', drop); timers.forEach(clearTimeout); timers.clear(); };
```
