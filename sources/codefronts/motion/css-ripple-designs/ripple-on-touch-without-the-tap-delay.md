---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/ripple-on-touch-without-the-tap-delay/"
title: "Ripple on Touch Without the Tap Delay"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Bind a ripple to click and on touch it can arrive hundreds of milliseconds after the finger, long after the user decided the tap did not register."
has_js: "true"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple on Touch Without the Tap Delay
Source: https://codefronts.com/motion/css-ripple-designs/ripple-on-touch-without-the-tap-delay/

Bind a ripple to click and on touch it can arrive hundreds of milliseconds after the finger, long after the user decided the tap did not register. The fix is to split feedback from action: pointerdown draws the ring, click still performs the work. The two traps come with it — pointerdown also fires when a scroll begins, and a ring that started must still finish.
## HTML
```html
<section class="rpl-07" aria-labelledby="rpl-07-title">
  <input class="rpl-07__theme-input" type="checkbox" id="rpl-07-theme">
  <label class="rpl-07__theme" for="rpl-07-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-07__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-07__phone">
    <div class="rpl-07__status" aria-hidden="true"><span>9:41</span><span class="rpl-07__status-r"><span class="rpl-07__bars"></span><span class="rpl-07__batt"></span></span></div>
    <div class="rpl-07__body">
      <h1 class="rpl-07__h1" id="rpl-07-title">Nearby</h1>
      <p class="rpl-07__sub">Delivering to Riverside Ave</p>
      <div class="rpl-07__hero">
        <span class="rpl-07__hero-tag">25 min</span>
      </div>
      <div class="rpl-07__cards">
        <div class="rpl-07__mini"><span class="rpl-07__mini-img" data-t="1"></span><span class="rpl-07__mini-n">Ozu Ramen</span><span class="rpl-07__mini-m">4.8 &middot; $$</span></div>
        <div class="rpl-07__mini"><span class="rpl-07__mini-img" data-t="2"></span><span class="rpl-07__mini-n">Fig &amp; Ash</span><span class="rpl-07__mini-m">4.6 &middot; $$$</span></div>
      </div>
    </div>
    <nav class="rpl-07__tabs" id="rpl-07-tabs" aria-label="Primary">
      <button class="rpl-07__tab rpl-07__tab--on" type="button" aria-current="page">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 11 12 4l8 7v8a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1Z"/></svg>
        <span>Home</span>
      </button>
      <button class="rpl-07__tab" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <span>Search</span>
      </button>
      <button class="rpl-07__tab" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M6 6h15l-2 9H8Z"/><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/><path d="M6 6 5 3H2"/></svg>
        <span>Orders</span>
      </button>
      <button class="rpl-07__tab" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 20c1.4-3.6 4-5.4 7-5.4s5.6 1.8 7 5.4"/></svg>
        <span>Account</span>
      </button>
    </nav>
  </div>
</section>
```
## CSS
```css
.rpl-07 {
  --rpl-07-bg: #070d18;
  --rpl-07-bg: oklch(0.17 0.030 262);
  --rpl-07-phone: #0d1526;
  --rpl-07-phone: oklch(0.215 0.032 262);
  --rpl-07-line: #1c2740;
  --rpl-07-line: oklch(0.29 0.035 262);
  --rpl-07-fg: #eef2fb;
  --rpl-07-fg: oklch(0.965 0.008 262);
  --rpl-07-muted: #8894ad;
  --rpl-07-muted: oklch(0.675 0.028 262);
  --rpl-07-accent: #ff7a4d;
  --rpl-07-accent: oklch(0.74 0.17 42);
  --rpl-07-ink: rgba(255, 122, 77, 0.28);
  --rpl-07-ink: oklch(0.74 0.17 42 / 0.28);
  --rpl-07-dur: 480ms;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(12px, 3vw, 40px);
  background: radial-gradient(90% 60% at 50% 100%, oklch(0.30 0.09 40 / 0.35), transparent 70%), var(--rpl-07-bg);
  color: var(--rpl-07-fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-07 *,
.rpl-07 *::before,
.rpl-07 *::after {
  box-sizing: border-box;
}

.rpl-07__phone {
  inline-size: min(390px, 100%);
  block-size: min(800px, 92svh);
  display: flex;
  flex-direction: column;
  border: 1px solid var(--rpl-07-line);
  border-radius: 40px;
  background: var(--rpl-07-phone);
  overflow: hidden;
  box-shadow: 0 40px 100px -50px oklch(0 0 0 / 0.95);
}

.rpl-07__status {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 26px 6px;
  font-size: 13px;
  font-weight: 600;
}

.rpl-07__status-r {
  display: flex;
  align-items: center;
  gap: 6px;
}

.rpl-07__bars {
  inline-size: 17px;
  block-size: 11px;
  background: linear-gradient(to right, currentColor 0 3px, transparent 3px 5px, currentColor 5px 8px, transparent 8px 10px, currentColor 10px 13px, transparent 13px 15px, currentColor 15px 17px);
  clip-path: polygon(0 60%, 3px 60%, 3px 40%, 8px 40%, 8px 20%, 13px 20%, 13px 0, 17px 0, 17px 100%, 0 100%);
}

.rpl-07__batt {
  inline-size: 22px;
  block-size: 11px;
  border: 1.4px solid currentColor;
  border-radius: 3px;
  position: relative;
}

.rpl-07__batt::after {
  content: "";
  position: absolute;
  inset: 2px;
  inline-size: 60%;
  background: currentColor;
  border-radius: 1px;
}

.rpl-07__body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 16px 20px 8px;
  min-block-size: 0;
  overflow: hidden;
}

.rpl-07__h1 {
  margin: 6px 0 0;
  font-size: 30px;
  font-weight: 650;
  letter-spacing: -0.03em;
}

.rpl-07__sub {
  margin: 0;
  font-size: 13px;
  color: var(--rpl-07-muted);
}

.rpl-07__hero {
  position: relative;
  block-size: clamp(140px, 26vh, 200px);
  border-radius: 20px;
  background: linear-gradient(150deg, oklch(0.55 0.14 42), oklch(0.42 0.12 300));
}

.rpl-07__hero-tag {
  position: absolute;
  inset-block-end: 12px;
  inset-inline-start: 12px;
  padding: 6px 11px;
  border-radius: 999px;
  background: oklch(0.15 0.02 262 / 0.7);
  font-size: 12px;
  font-weight: 600;
  backdrop-filter: blur(6px);
}

.rpl-07__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.rpl-07__mini {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.rpl-07__mini-img {
  block-size: 84px;
  border-radius: 14px;
  background: linear-gradient(140deg, oklch(0.48 0.10 200), oklch(0.36 0.06 250));
}

.rpl-07__mini-img[data-t="2"] {
  background: linear-gradient(140deg, oklch(0.52 0.11 130), oklch(0.36 0.06 190));
}

.rpl-07__mini-n {
  font-size: 13.5px;
  font-weight: 600;
}

.rpl-07__mini-m {
  font-size: 12px;
  color: var(--rpl-07-muted);
}

.rpl-07__tabs {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 4px;
  padding: 8px 10px calc(8px + env(safe-area-inset-bottom, 10px));
  border-block-start: 1px solid var(--rpl-07-line);
  background: oklch(0.19 0.030 262 / 0.9);
  backdrop-filter: blur(12px);
}

.rpl-07__tab {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  min-block-size: 56px;
  border: 0;
  border-radius: 16px;
  background: transparent;
  color: var(--rpl-07-muted);
  font: inherit;
  font-size: 10.5px;
  font-weight: 550;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  /* no 300ms wait: pointerdown fires immediately, and the tap highlight is suppressed */
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.rpl-07__tab svg {
  inline-size: 22px;
  block-size: 22px;
}

.rpl-07__tab--on {
  color: var(--rpl-07-accent);
}

.rpl-07__tab:focus-visible {
  outline: 2px solid var(--rpl-07-accent);
  outline-offset: -2px;
}

.rpl-07__ring {
  position: absolute;
  left: var(--rpl-07-x, 50%);
  top: var(--rpl-07-y, 50%);
  inline-size: calc(var(--rpl-07-r, 60px) * 2);
  block-size: calc(var(--rpl-07-r, 60px) * 2);
  border-radius: 50%;
  background: var(--rpl-07-ink);
  pointer-events: none;
  z-index: -1;
  animation: rpl-07-expand var(--rpl-07-dur) cubic-bezier(0.16, 0.72, 0.3, 1) forwards;
}

@keyframes rpl-07-expand {
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
  .rpl-07__ring {
    display: none;
  }

  .rpl-07__tab:active {
    background: color-mix(in oklab, var(--rpl-07-accent) 18%, transparent);
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-07:has(#rpl-07-theme:checked) {
  --rpl-07-bg: oklch(0.827 0.030 262);
  --rpl-07-phone: oklch(0.785 0.032 262);
  --rpl-07-line: oklch(0.715 0.035 262);
  --rpl-07-fg: oklch(0.140 0.008 262);
  --rpl-07-muted: oklch(0.357 0.028 262);
  --rpl-07-accent: oklch(0.297 0.17 42);
  --rpl-07-ink: oklch(0.297 0.17 42 / 0.28);
  background: radial-gradient(90% 60% at 50% 100%, oklch(0.706 0.09 40 / 0.35), transparent 70%), var(--rpl-07-bg);
  color: var(--rpl-07-fg);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__phone {
  border: 1px solid var(--rpl-07-line);
  background: var(--rpl-07-phone);
  box-shadow: 0 40px 100px -50px oklch(0.985 0 0 / 0.95);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__bars {
  background: linear-gradient(to right, currentColor 0 3px, transparent 3px 5px, currentColor 5px 8px, transparent 8px 10px, currentColor 10px 13px, transparent 13px 15px, currentColor 15px 17px);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__batt {
  border: 1.4px solid currentColor;
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__batt::after {
  background: currentColor;
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__sub {
  color: var(--rpl-07-muted);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__hero {
  background: linear-gradient(150deg, oklch(0.473 0.14 42), oklch(0.594 0.12 300));
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__hero-tag {
  background: oklch(0.845 0.02 262 / 0.7);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__mini-img {
  background: linear-gradient(140deg, oklch(0.539 0.10 200), oklch(0.650 0.06 250));
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__mini-img[data-t="2"] {
  background: linear-gradient(140deg, oklch(0.501 0.11 130), oklch(0.650 0.06 190));
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__mini-m {
  color: var(--rpl-07-muted);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__tabs {
  background: oklch(0.808 0.030 262 / 0.9);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__tab {
  color: var(--rpl-07-muted);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__tab--on {
  color: var(--rpl-07-accent);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__tab:focus-visible {
  outline: 2px solid var(--rpl-07-accent);
}

.rpl-07:has(#rpl-07-theme:checked) .rpl-07__ring {
  background: var(--rpl-07-ink);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-07:has(#rpl-07-theme:checked) .rpl-07__tab:active {
    background: color-mix(in oklab, var(--rpl-07-accent) 18%, transparent);
  }
}

.rpl-07 {
  position: relative;
}

.rpl-07__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-07__theme {
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

.rpl-07__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-07__theme:active {
  transform: scale(0.94);
}

.rpl-07__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-07__theme-input:checked + .rpl-07__theme svg {
  transform: rotate(180deg);
}

.rpl-07__theme-input:focus-visible + .rpl-07__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-07__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-07__theme,
    .rpl-07__theme svg {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.rpl-07');
const tabs = root.querySelector('#rpl-07-tabs');
const timers = new Set();

const drop = (event) => {
  const tab = event.target.closest('.rpl-07__tab');
  if (!tab) return;
  tabs.querySelectorAll('.rpl-07__tab').forEach((t) => { t.classList.remove('rpl-07__tab--on'); t.removeAttribute('aria-current'); });
  tab.classList.add('rpl-07__tab--on');
  tab.setAttribute('aria-current', 'page');
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = tab.getBoundingClientRect();
  const x = (event.clientX || box.left + box.width / 2) - box.left;
  const y = (event.clientY || box.top + box.height / 2) - box.top;
  const r = Math.max(Math.hypot(x, y), Math.hypot(box.width - x, y), Math.hypot(x, box.height - y), Math.hypot(box.width - x, box.height - y));
  const ring = document.createElement('span');
  ring.className = 'rpl-07__ring';
  ring.setAttribute('aria-hidden', 'true');
  ring.style.setProperty('--rpl-07-x', x + 'px');
  ring.style.setProperty('--rpl-07-y', y + 'px');
  ring.style.setProperty('--rpl-07-r', r + 'px');
  ring.addEventListener('animationend', () => ring.remove(), { once: true });
  const t = setTimeout(() => { timers.delete(t); ring.remove(); }, 1200);
  timers.add(t);
  tab.append(ring);
};

tabs.addEventListener('pointerdown', drop);
root.__rplCleanup = () => { tabs.removeEventListener('pointerdown', drop); timers.forEach(clearTimeout); timers.clear(); };
```
