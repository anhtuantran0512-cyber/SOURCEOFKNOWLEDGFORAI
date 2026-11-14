---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/shopping-cart-expiration-timers/"
title: "Shopping Cart Expiration Countdown Timer"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A cart-page reservation timer: items held for a fixed window, a per-line list of what is reserved, a warning state inside the last two minutes and an extend…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shopping Cart Expiration Countdown Timer
Source: https://codefronts.com/snippets/css-countdown-timers/shopping-cart-expiration-timers/

A cart-page reservation timer: items held for a fixed window, a per-line list of what is reserved, a warning state inside the last two minutes and an extend control. The rule it demonstrates is the one stores get wrong — never silently empty a cart; warn, offer more time, and say what happens if the window closes.
## HTML
```html
<section class="cdt-19" aria-labelledby="cdt-19-title">
  <input class="cdt-19__tgl" type="checkbox" id="cdt-19-theme">
  <label class="cdt-19__tglbtn" for="cdt-19-theme">
    <svg class="cdt-19__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-19__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-19__darktext">Dark mode</span><span class="cdt-19__lighttext">Light mode</span>
  </label>
  <div class="cdt-19__stage">
    <article class="cdt-19__panel" data-panel>
      <header class="cdt-19__head">
        <p class="cdt-19__brand">Quill Press · checkout</p>
        <h2 class="cdt-19__title" id="cdt-19-title">Your items are reserved</h2>
      </header>

      <div class="cdt-19__timer" role="timer">
        <span class="cdt-19__ico" aria-hidden="true" data-ico>
          <svg viewBox="0 0 20 20" width="18" height="18"><circle cx="10" cy="10" r="7.6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 5.9V10l2.8 1.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
        </span>
        <p class="cdt-19__tcopy">Held for <time class="cdt-19__clock" datetime="" data-clock>9:47</time></p>
        <p class="cdt-19__tnote" data-note>Checkout completes the sale. Nothing is charged until you confirm.</p>
      </div>

      <ul class="cdt-19__lines">
        <li><span class="cdt-19__name">Basalt letterpress set, A5</span><span class="cdt-19__hold">Held firmly · 12 in stock</span><span class="cdt-19__price">$64</span></li>
        <li><span class="cdt-19__name">Meridian ink, oxide black</span><span class="cdt-19__hold">Held firmly · 40 in stock</span><span class="cdt-19__price">$18</span></li>
        <li data-low><span class="cdt-19__name">Fern cotton paper, 250gsm</span><span class="cdt-19__hold">Low stock · hold cannot be extended</span><span class="cdt-19__price">$39</span></li>
      </ul>

      <div class="cdt-19__actions">
        <button class="cdt-19__btn" type="button">Checkout · $121</button>
        <button class="cdt-19__btn cdt-19__btn--ghost" type="button" data-extend>Give me more time</button>
      </div>

      <p class="cdt-19__foot">If the hold expires the items stay in your basket — the reservation is released, so stock is no longer guaranteed. Nothing is deleted without telling you.</p>
      <output class="cdt-19__sr" aria-live="polite" data-live></output>
    </article>
  </div>
</section>
```
## CSS
```css
.cdt-19 {
  --page: #f0e9df;
  --panel: #fdfaf5;
  --ink: #2a2018;
  --muted: #746353;
  --rule: #2a2018;
  --accent: #b4531f;
  --warn: #b4531f;
  --crit: #a01f14;
  --offset: 6px;
  --font-display: "Iowan Old Style", "Palatino Linotype", Georgia, ui-serif, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-19 {
    --page: oklch(93.5% 0.018 75);
    --panel: oklch(98.5% 0.01 80);
    --ink: oklch(26% 0.02 55);
    --muted: oklch(50% 0.03 55);
    --rule: oklch(28% 0.024 55);
    --accent: oklch(53% 0.15 45);
    --warn: oklch(53% 0.15 45);
    --crit: oklch(45% 0.2 28);
  }
}

.cdt-19 *,
.cdt-19 *::before,
.cdt-19 *::after {
  box-sizing: border-box;
}

.cdt-19__stage {
  display: grid;
  place-content: center;
  justify-items: center;
  min-height: 100vh;
  padding: clamp(16px, 4vw, 48px);
}

.cdt-19__panel {
  inline-size: min(560px, 100%);
  padding: clamp(20px, 4.4vw, 32px);
  background: var(--panel);
  border: 2px solid var(--rule);
  box-shadow: var(--offset) var(--offset) 0 0 var(--rule);
}

.cdt-19__brand {
  margin: 0 0 8px;
  font: 600 10.5px/1 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-19__title {
  margin: 0 0 20px;
  font: 400 clamp(23px, 4.4vw, 32px)/1.12 var(--font-display);
  letter-spacing: -0.012em;
  text-wrap: balance;
}

.cdt-19__timer {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 4px 10px;
  padding: 14px 16px;
  border: 1px solid rgba(42, 32, 24, 0.2);
  background: rgba(180, 83, 31, 0.05);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-19__timer {
    background: color-mix(in oklab, var(--accent) 6%, var(--panel));
  }
}

.cdt-19__ico {
  display: flex;
  padding-block-start: 3px;
  color: var(--accent);
}

.cdt-19__tcopy {
  grid-column: 2;
  margin: 0;
  font: 400 clamp(17px, 3.4vw, 21px)/1.2 var(--font-display);
}

.cdt-19__clock {
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
}

.cdt-19__tnote {
  grid-column: 2;
  margin: 0;
  font-size: 12px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-19__panel[data-state="warn"] .cdt-19__timer {
  border-color: var(--crit);
  background: rgba(160, 31, 20, 0.08);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-19__panel[data-state="warn"] .cdt-19__timer {
    background: color-mix(in oklab, var(--crit) 9%, var(--panel));
  }
}

.cdt-19__panel[data-state="warn"] .cdt-19__ico,
.cdt-19__panel[data-state="warn"] .cdt-19__clock {
  color: var(--crit);
}

.cdt-19__panel[data-state="expired"] .cdt-19__timer {
  border-color: var(--muted);
  background: transparent;
}

.cdt-19__lines {
  display: grid;
  gap: 1px;
  margin: 18px 0 0;
  padding: 0;
  list-style: none;
  background: rgba(42, 32, 24, 0.14);
}

.cdt-19__lines li {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 2px 12px;
  padding: 12px 2px;
  background: var(--panel);
}

.cdt-19__name {
  min-inline-size: 0;
  font: 400 15px/1.35 var(--font-display);
}

.cdt-19__hold {
  grid-column: 1;
  min-inline-size: 0;
  font-size: 11.5px;
  color: var(--muted);
}

.cdt-19__lines li[data-low] .cdt-19__hold {
  color: var(--crit);
}

.cdt-19__price {
  grid-row: 1 / span 2;
  align-self: center;
  font: 400 16px/1 var(--font-display);
  font-variant-numeric: tabular-nums;
}

.cdt-19__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-block-start: 20px;
}

.cdt-19__btn {
  flex: 1 1 150px;
  min-block-size: 48px;
  min-inline-size: 44px;
  padding: 13px 18px;
  border: 2px solid var(--rule);
  background: var(--ink);
  color: var(--panel);
  font: 600 14px/1 system-ui, sans-serif;
  cursor: pointer;
}

.cdt-19__btn--ghost {
  background: transparent;
  color: var(--ink);
}

.cdt-19__btn:hover {
  transform: translate(-1px, -1px);
}

.cdt-19__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-19__btn[disabled] {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.cdt-19__foot {
  margin: 16px 0 0;
  font-size: 11.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-19__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (prefers-reduced-motion: reduce) {
  .cdt-19__btn:hover {
    transform: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-19 {
  position: relative;
}

.cdt-19__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-19__tglbtn {
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

.cdt-19__tglbtn:hover {
  opacity: 1;
}

.cdt-19__tgl:focus-visible + .cdt-19__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-19__tglbtn svg {
  flex: none;
}

.cdt-19__sun,
.cdt-19__lighttext {
  display: none;
}

.cdt-19:has(.cdt-19__tgl:checked) .cdt-19__moon,
.cdt-19:has(.cdt-19__tgl:checked) .cdt-19__darktext {
  display: none;
}

.cdt-19:has(.cdt-19__tgl:checked) .cdt-19__sun {
  display: block;
}

.cdt-19:has(.cdt-19__tgl:checked) .cdt-19__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-19__tglbtn {
    padding: 12px;
  }

  .cdt-19__darktext,
    .cdt-19__lighttext,
    .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__darktext,
    .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-19:has(.cdt-19__tgl:checked) {
    --page: #191410;
    --panel: #221b16;
    --ink: #f5ece1;
    --muted: #a89684;
    --rule: #f5ece1;
    --accent: #f08a4b;
    --warn: #f08a4b;
    --crit: #ff7466;
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__btn {
    background: var(--accent);
    color: #191410;
    border-color: var(--accent);
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__btn--ghost {
    background: transparent;
    color: var(--ink);
    border-color: var(--rule);
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__lines {
    background: rgba(245, 236, 225, 0.16);
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__timer {
    border-color: rgba(245, 236, 225, 0.24);
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-19 {
    --page: #191410;
    --panel: #221b16;
    --ink: #f5ece1;
    --muted: #a89684;
    --rule: #f5ece1;
    --accent: #f08a4b;
    --warn: #f08a4b;
    --crit: #ff7466;
  }

  .cdt-19__btn {
    background: var(--accent);
    color: #191410;
    border-color: var(--accent);
  }

  .cdt-19__btn--ghost {
    background: transparent;
    color: var(--ink);
    border-color: var(--rule);
  }

  .cdt-19__lines {
    background: rgba(245, 236, 225, 0.16);
  }

  .cdt-19__timer {
    border-color: rgba(245, 236, 225, 0.24);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-19:has(.cdt-19__tgl:checked) {
    --page: oklch(93.5% 0.018 75);
    --panel: oklch(98.5% 0.01 80);
    --ink: oklch(26% 0.02 55);
    --muted: oklch(50% 0.03 55);
    --rule: oklch(28% 0.024 55);
    --accent: oklch(53% 0.15 45);
    --warn: oklch(53% 0.15 45);
    --crit: oklch(45% 0.2 28);
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__btn {
    background: var(--ink);
    color: var(--panel);
    border-color: var(--rule);
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__btn--ghost {
    background: transparent;
    color: var(--ink);
    border-color: var(--rule);
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__timer {
    border-color: rgba(42, 32, 24, 0.2);
  }

  .cdt-19:has(.cdt-19__tgl:checked) .cdt-19__lines {
    background: rgba(42, 32, 24, 0.14);
  }
}

[data-theme="dark"] .cdt-19 {
  --page: #191410;
  --panel: #221b16;
  --ink: #f5ece1;
  --muted: #a89684;
  --rule: #f5ece1;
  --accent: #f08a4b;
  --warn: #f08a4b;
  --crit: #ff7466;
}

[data-theme="dark"] .cdt-19 .cdt-19__btn {
  background: var(--accent);
  color: #191410;
  border-color: var(--accent);
}

[data-theme="dark"] .cdt-19 .cdt-19__btn--ghost {
  background: transparent;
  color: var(--ink);
  border-color: var(--rule);
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-19');
if (root) {
  const q = (s) => root.querySelector(s);
  const panel = q('[data-panel]'), clock = q('[data-clock]'), note = q('[data-note]'), live = q('[data-live]');
  const HOLD = 9 * 60e3 + 47e3, MORE = 5 * 60e3;
  let target = Date.now() + HOLD, id = 0, seen = null;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    clock.textContent = Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
    clock.dateTime = new Date(target).toISOString();
    const b = ms <= 0 ? 'expired' : ms <= 120e3 ? 'warn' : ms <= 300e3 ? 'soon' : 'ok';
    if (b !== seen) {
      seen = b;
      panel.dataset.state = b === 'soon' ? 'ok' : b;
      note.textContent = { ok: 'Checkout completes the sale. Nothing is charged until you confirm.', soon: 'Five minutes left on this hold. You can extend it once.', warn: 'Under two minutes — extend the hold or complete checkout now.', expired: 'The hold was released. Your items are still listed; stock is no longer guaranteed.' }[b];
      if (b !== 'ok') live.textContent = { soon: 'Five minutes left on your cart reservation.', warn: 'Under two minutes left. Extend the hold or check out.', expired: 'Your cart reservation expired. The items are still in your basket.' }[b];
    }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); } else { clock.textContent = 'released'; }
  };
  q('[data-extend]').addEventListener('click', (e) => {
    target = Date.now() + MORE; seen = null; e.currentTarget.disabled = true;
    e.currentTarget.textContent = 'Extended once';
    live.textContent = 'Five more minutes added to your reservation.';
    clearTimeout(id); tick();
  });
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
