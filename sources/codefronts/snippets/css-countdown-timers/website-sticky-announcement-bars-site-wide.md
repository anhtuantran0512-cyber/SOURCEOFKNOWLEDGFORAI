---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/website-sticky-announcement-bars-site-wide/"
title: "Sticky Announcement Bar Countdown"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A site-wide sticky bar where the timer, not the message, is the dominant element: oversized tabular digits, one short line of offer copy, a compact CTA and a…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Announcement Bar Countdown
Source: https://codefronts.com/snippets/css-countdown-timers/website-sticky-announcement-bars-site-wide/

A site-wide sticky bar where the timer, not the message, is the dominant element: oversized tabular digits, one short line of offer copy, a compact CTA and a real dismiss control. It sticks to the top of the scroll container, collapses to a two-line layout on narrow screens and states its own end condition.
## HTML
```html
<section class="cdt-18" aria-labelledby="cdt-18-title">
  <input class="cdt-18__tgl" type="checkbox" id="cdt-18-theme">
  <label class="cdt-18__tglbtn" for="cdt-18-theme">
    <svg class="cdt-18__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-18__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-18__darktext">Dark mode</span><span class="cdt-18__lighttext">Light mode</span>
  </label>
  <div class="cdt-18__scroll">
    <div class="cdt-18__bar" data-bar role="timer">
      <time class="cdt-18__digits" datetime="" data-clock aria-hidden="true">
        <b data-h>01</b><span>:</span><b data-m>59</b><span>:</span><b data-s>07</b>
      </time>
      <p class="cdt-18__copy" data-copy>Free next-day shipping on everything — ends when the clock does.</p>
      <button class="cdt-18__cta" type="button" data-cta>Shop the drop</button>
      <button class="cdt-18__x" type="button" data-close>
        <span class="cdt-18__sr">Dismiss the offer bar</span>
        <svg viewBox="0 0 14 14" width="13" height="13" aria-hidden="true"><path d="M2.5 2.5l9 9M11.5 2.5l-9 9" stroke="currentColor" stroke-width="1.8"/></svg>
      </button>
    </div>

    <div class="cdt-18__page">
      <header class="cdt-18__nav" aria-hidden="true"><strong>Fern Supply</strong><span>New</span><span>Workshop</span><span>Journal</span><span>Cart · 2</span></header>
      <h2 class="cdt-18__title" id="cdt-18-title">Scroll — the bar stays, the timer keeps counting</h2>
      <p class="cdt-18__lede">The bar is sticky inside this scroll container, which is where the pattern usually breaks: an <code>overflow: hidden</code> ancestor between the bar and the scroll root disables sticky entirely.</p>
      <div class="cdt-18__grid" aria-hidden="true">
        <div class="cdt-18__tile"></div><div class="cdt-18__tile"></div><div class="cdt-18__tile"></div>
        <div class="cdt-18__tile"></div><div class="cdt-18__tile"></div><div class="cdt-18__tile"></div>
      </div>
      <p class="cdt-18__foot">At zero the bar swaps to a closed state in place rather than disappearing and shifting the page under you.</p>
      <output class="cdt-18__srlive" aria-live="polite" data-live></output>
    </div>
  </div>
</section>
```
## CSS
```css
.cdt-18 {
  --page: #f5f5f2;
  --bar: #17181a;
  --barink: #f7f8f4;
  --ink: #17181a;
  --muted: #6b6d70;
  --rule: #e2e2dd;
  --accent: #c8f52e;
  --digit: 30px;
  --font-display: "Archivo", "Geist", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-18 {
    --page: oklch(96.5% 0.004 100);
    --bar: oklch(19% 0.006 260);
    --barink: oklch(97% 0.008 100);
    --ink: oklch(20% 0.006 260);
    --muted: oklch(52% 0.008 260);
    --rule: oklch(91% 0.006 100);
    --accent: oklch(90% 0.19 120);
  }
}

.cdt-18 *,
.cdt-18 *::before,
.cdt-18 *::after {
  box-sizing: border-box;
}

.cdt-18__scroll {
  block-size: 100vh;
  overflow-y: auto;
}

.cdt-18__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 5;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto auto;
  align-items: center;
  gap: 6px 14px;
  padding: 8px clamp(10px, 2.6vw, 18px);
  background: var(--bar);
  color: var(--barink);
}

.cdt-18__bar[hidden] {
  display: none;
}

.cdt-18__digits {
  display: flex;
  align-items: baseline;
  gap: 1px;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
}

.cdt-18__digits b {
  font: 700 clamp(21px, 5.6vw, var(--digit))/1 var(--font-display);
  letter-spacing: -0.03em;
}

.cdt-18__digits span {
  font: 700 clamp(16px, 4vw, 24px)/1 var(--font-display);
  opacity: 0.45;
}

.cdt-18__copy {
  min-inline-size: 0;
  margin: 0;
  font-size: 12.5px;
  line-height: 1.35;
  color: rgba(247, 248, 244, 0.78);
  text-wrap: pretty;
}

.cdt-18__cta {
  min-block-size: 36px;
  padding: 9px 14px;
  border: 0;
  border-radius: 4px;
  background: var(--accent);
  color: var(--bar);
  font: 700 12.5px/1 var(--font-display);
  white-space: nowrap;
  cursor: pointer;
}

.cdt-18__cta:hover {
  filter: brightness(1.07);
}

.cdt-18__cta:focus-visible {
  outline: 2px solid var(--barink);
  outline-offset: 2px;
}

.cdt-18__x {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 0;
  border-radius: 4px;
  background: transparent;
  color: var(--barink);
  cursor: pointer;
}

.cdt-18__x:hover {
  background: rgba(255, 255, 255, 0.1);
}

.cdt-18__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-18__sr,
.cdt-18__srlive {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (max-width: 560px) {
  .cdt-18__bar {
    grid-template-columns: minmax(0, 1fr) auto auto;
  }

  .cdt-18__digits {
    grid-column: 1 / -1;
  }

  .cdt-18__copy {
    grid-column: 1;
  }
}

.cdt-18__page {
  padding: clamp(16px, 4vw, 40px);
}

.cdt-18__nav {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px 16px;
  padding-block-end: 16px;
  border-block-end: 1px solid var(--rule);
  font-size: 12.5px;
  color: var(--muted);
}

.cdt-18__nav strong {
  font: 700 15px/1 var(--font-display);
  color: var(--ink);
}

.cdt-18__title {
  margin: 24px 0 8px;
  max-inline-size: 22ch;
  font: 700 clamp(24px, 5vw, 38px)/1.1 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.cdt-18__lede {
  margin: 0 0 24px;
  max-inline-size: 56ch;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-18__lede code {
  padding: 1px 5px;
  border-radius: 4px;
  background: var(--rule);
  font: 500 12px/1.4 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

.cdt-18__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 12px;
}

.cdt-18__tile {
  min-block-size: 168px;
  border: 1px solid var(--rule);
  border-radius: 8px;
  background: linear-gradient(160deg, #ffffff, #eceae3);
}

.cdt-18__foot {
  margin: 24px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-18 {
  position: relative;
}

.cdt-18__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-18__tglbtn {
  position: absolute;
  inset-block-end: 14px;
  inset-inline-end: 14px;
  z-index: 20;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 12px 14px;
  border: 1px solid currentColor;
  border-radius: 10px;
  background: transparent;
  color: inherit;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: 0.62;
}

.cdt-18__tglbtn:hover {
  opacity: 1;
}

.cdt-18__tgl:focus-visible + .cdt-18__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-18__tglbtn svg {
  flex: none;
}

.cdt-18__sun,
.cdt-18__lighttext {
  display: none;
}

.cdt-18:has(.cdt-18__tgl:checked) .cdt-18__moon,
.cdt-18:has(.cdt-18__tgl:checked) .cdt-18__darktext {
  display: none;
}

.cdt-18:has(.cdt-18__tgl:checked) .cdt-18__sun {
  display: block;
}

.cdt-18:has(.cdt-18__tgl:checked) .cdt-18__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-18__tglbtn {
    padding: 12px;
  }

  .cdt-18__darktext,
    .cdt-18__lighttext,
    .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__darktext,
    .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-18:has(.cdt-18__tgl:checked) {
    --page: #101112;
    --bar: #c8f52e;
    --barink: #14160c;
    --ink: #f2f3ee;
    --muted: #93959a;
    --rule: #26282a;
    --accent: #14160c;
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__copy {
    color: rgba(20, 22, 12, 0.78);
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__cta {
    background: #14160c;
    color: #c8f52e;
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__x:hover {
    background: rgba(0, 0, 0, 0.12);
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__tile {
    background: linear-gradient(160deg, #1a1c1e, #141517);
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-18 {
    --page: #101112;
    --bar: #c8f52e;
    --barink: #14160c;
    --ink: #f2f3ee;
    --muted: #93959a;
    --rule: #26282a;
    --accent: #14160c;
  }

  .cdt-18__copy {
    color: rgba(20, 22, 12, 0.78);
  }

  .cdt-18__cta {
    background: #14160c;
    color: #c8f52e;
  }

  .cdt-18__x:hover {
    background: rgba(0, 0, 0, 0.12);
  }

  .cdt-18__tile {
    background: linear-gradient(160deg, #1a1c1e, #141517);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-18:has(.cdt-18__tgl:checked) {
    --page: oklch(96.5% 0.004 100);
    --bar: oklch(19% 0.006 260);
    --barink: oklch(97% 0.008 100);
    --ink: oklch(20% 0.006 260);
    --muted: oklch(52% 0.008 260);
    --rule: oklch(91% 0.006 100);
    --accent: oklch(90% 0.19 120);
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__copy {
    color: rgba(247, 248, 244, 0.78);
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__cta {
    background: var(--accent);
    color: var(--bar);
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__x:hover {
    background: rgba(255, 255, 255, 0.1);
  }

  .cdt-18:has(.cdt-18__tgl:checked) .cdt-18__tile {
    background: linear-gradient(160deg, #ffffff, #eceae3);
  }
}

[data-theme="dark"] .cdt-18 {
  --page: #101112;
  --bar: #c8f52e;
  --barink: #14160c;
  --ink: #f2f3ee;
  --muted: #93959a;
  --rule: #26282a;
  --accent: #14160c;
}

[data-theme="dark"] .cdt-18 .cdt-18__cta {
  background: #14160c;
  color: #c8f52e;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-18');
if (root) {
  const q = (s) => root.querySelector(s);
  const bar = q('[data-bar]'), clock = q('[data-clock]'), live = q('[data-live]'), pad = (n) => String(n).padStart(2, '0');
  const target = new Date(Date.now() + 3600e3 + 59 * 60e3 + 7e3);
  let id = 0, seen = null;
  clock.dateTime = target.toISOString();
  const tick = () => {
    const ms = target - Date.now();
    if (ms <= 0) {
      clock.innerHTML = '<b>Closed</b>';
      q('[data-copy]').textContent = 'Free shipping has ended — standard rates apply.';
      q('[data-cta]').textContent = 'Browse the range';
      live.textContent = 'The free shipping offer has closed.';
      return;
    }
    const s = Math.floor(ms / 1000);
    q('[data-h]').textContent = pad(Math.floor(s / 3600));
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    const b = ms < 60e3 ? 'm1' : ms < 600e3 ? 'm10' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', m10: 'Ten minutes left for free next-day shipping.', m1: 'One minute left for free next-day shipping.' }[b]; }
    id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  q('[data-close]').addEventListener('click', () => { clearTimeout(id); bar.hidden = true; });
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
