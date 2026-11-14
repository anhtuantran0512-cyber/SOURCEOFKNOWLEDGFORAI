---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/e-commerce-flash-sales-product-pages/"
title: "Flash Sale Countdown for Product Pages"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A product-page urgency block: sale price against a struck original, a savings chip, the countdown to the sale ending and a stock-remaining bar in the same…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flash Sale Countdown for Product Pages
Source: https://codefronts.com/snippets/css-countdown-timers/e-commerce-flash-sales-product-pages/

A product-page urgency block: sale price against a struck original, a savings chip, the countdown to the sale ending and a stock-remaining bar in the same frame. At zero it does not vanish or freeze — it switches to a Sale ended state with the full price restored, which is the honest version of this pattern.
## HTML
```html
<section class="cdt-17" aria-labelledby="cdt-17-title">
  <input class="cdt-17__tgl" type="checkbox" id="cdt-17-theme">
  <label class="cdt-17__tglbtn" for="cdt-17-theme">
    <svg class="cdt-17__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-17__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-17__darktext">Dark mode</span><span class="cdt-17__lighttext">Light mode</span>
  </label>
  <div class="cdt-17__stage">
    <article class="cdt-17__card">
      <div class="cdt-17__shot" aria-hidden="true">
        <span class="cdt-17__badge">Flash</span>
        <div class="cdt-17__shotart"></div>
      </div>

      <div class="cdt-17__body">
        <p class="cdt-17__crumb">Nova Audio · monitors</p>
        <h2 class="cdt-17__title" id="cdt-17-title">Basalt M2 studio monitor, pair</h2>

        <div class="cdt-17__prices">
          <strong class="cdt-17__now" data-now>$479</strong>
          <s class="cdt-17__was" data-was>$690</s>
          <span class="cdt-17__save" data-save>Save $211 · 31%</span>
        </div>

        <div class="cdt-17__timer" role="timer" data-timer>
          <p class="cdt-17__tlabel" data-tlabel>Spring Sale ends in</p>
          <time class="cdt-17__digits" datetime="" data-clock aria-hidden="true">
            <span><b data-h>05</b><i>hrs</i></span><span class="cdt-17__c">:</span>
            <span><b data-m>12</b><i>min</i></span><span class="cdt-17__c">:</span>
            <span><b data-s>44</b><i>sec</i></span>
          </time>
        </div>

        <div class="cdt-17__stock" style="--stock: 22%">
          <div class="cdt-17__stockbar" aria-hidden="true"><span></span></div>
          <p class="cdt-17__stocktext"><strong>7 pairs left</strong> of the 32 allocated to this sale</p>
        </div>

        <button class="cdt-17__buy" type="button" data-buy>Add to cart · $479</button>
        <p class="cdt-17__cut">Order before 4pm for dispatch today · free returns for 30 days</p>
        <output class="cdt-17__live" aria-live="polite" data-live></output>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
.cdt-17 {
  --page: #f3f1ea;
  --card: #ffffff;
  --ink: #0c0c0c;
  --muted: #63615c;
  --rule: #0c0c0c;
  --accent: #ffcc00;
  --danger: #d92b1f;
  --offset: 8px;
  --font-display: "Archivo Black", "Archivo", "Helvetica Neue", ui-sans-serif, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-17 {
    --page: oklch(95.5% 0.01 90);
    --card: oklch(100% 0 0);
    --ink: oklch(10% 0 0);
    --muted: oklch(48% 0.006 80);
    --accent: oklch(88% 0.17 96);
    --danger: oklch(53% 0.22 28);
  }
}

.cdt-17 *,
.cdt-17 *::before,
.cdt-17 *::after {
  box-sizing: border-box;
}

.cdt-17__stage {
  display: grid;
  place-content: center;
  justify-items: center;
  min-height: 100vh;
  padding: clamp(16px, 4vw, 48px);
}

.cdt-17__card {
  inline-size: min(780px, 100%);
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  background: var(--card);
  border: 3px solid var(--rule);
  box-shadow: var(--offset) var(--offset) 0 0 var(--rule);
}

@media (min-width: 740px) {
  .cdt-17__card {
    grid-template-columns: 268px minmax(0, 1fr);
  }
}

.cdt-17__shot {
  position: relative;
  min-block-size: 200px;
  padding: 12px;
  background: var(--accent);
  border-block-end: 3px solid var(--rule);
  overflow: hidden;
}

@media (min-width: 740px) {
  .cdt-17__shot {
    border-block-end: 0;
    border-inline-end: 3px solid var(--rule);
  }
}

.cdt-17__badge {
  position: relative;
  z-index: 1;
  display: inline-block;
  padding: 4px 9px;
  background: var(--ink);
  color: var(--accent);
  font: 400 11px/1 var(--font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.cdt-17__shotart {
  position: absolute;
  inset: 44px 30px 22px;
  border: 3px solid var(--rule);
  background: repeating-linear-gradient(180deg, rgba(0, 0, 0, 0.06) 0 8px, transparent 8px 16px);
}

.cdt-17__shotart::after {
  content: "";
  position: absolute;
  inset-inline: 22%;
  inset-block-start: 26%;
  aspect-ratio: 1;
  border-radius: 50%;
  border: 3px solid var(--rule);
  background: var(--card);
}

.cdt-17__body {
  min-inline-size: 0;
  padding: clamp(16px, 3.4vw, 26px);
}

.cdt-17__crumb {
  margin: 0 0 8px;
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-17__title {
  margin: 0 0 16px;
  font: 400 clamp(21px, 4vw, 30px)/1.08 var(--font-display);
  letter-spacing: -0.02em;
  text-transform: uppercase;
  text-wrap: balance;
}

.cdt-17__prices {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 6px 12px;
}

.cdt-17__now {
  font: 400 clamp(28px, 6vw, 38px)/1 var(--font-display);
  font-variant-numeric: tabular-nums;
}

.cdt-17__was {
  font-size: 16px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cdt-17__save {
  padding: 4px 9px;
  background: rgba(217, 43, 31, 0.12);
  color: var(--danger);
  font: 600 11.5px/1 system-ui, sans-serif;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-17__save {
    background: color-mix(in oklab, var(--danger) 14%, var(--card));
  }
}

.cdt-17__timer {
  margin-block-start: 18px;
  padding: 13px 15px;
  border: 3px solid var(--rule);
  background: var(--page);
}

.cdt-17__tlabel {
  margin: 0 0 8px;
  font: 600 10.5px/1 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-17__digits {
  display: flex;
  align-items: flex-start;
  gap: 6px;
  font-variant-numeric: tabular-nums;
}

.cdt-17__digits > span {
  display: grid;
  gap: 3px;
  justify-items: center;
  min-inline-size: 0;
}

.cdt-17__digits b {
  font: 400 clamp(26px, 7vw, 40px)/1 var(--font-display);
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
}

.cdt-17__digits i {
  font: 600 9px/1 system-ui, sans-serif;
  font-style: normal;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-17__c {
  font: 400 clamp(20px, 5vw, 30px)/1.2 var(--font-display);
  color: var(--muted);
}

.cdt-17__timer[data-urgent] {
  border-color: var(--danger);
  color: var(--danger);
}

.cdt-17__timer[data-urgent] .cdt-17__tlabel {
  color: var(--danger);
}

.cdt-17__timer[data-ended] {
  border-color: var(--muted);
}

.cdt-17__stock {
  margin-block-start: 16px;
}

.cdt-17__stockbar {
  block-size: 10px;
  border: 2px solid var(--rule);
}

.cdt-17__stockbar span {
  display: block;
  block-size: 100%;
  inline-size: var(--stock, 30%);
  background: var(--danger);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-17__stockbar span {
    background: color-mix(in oklab, var(--danger) 88%, var(--ink));
  }
}

.cdt-17__stocktext {
  margin: 7px 0 0;
  font-size: 12.5px;
  color: var(--muted);
}

.cdt-17__stocktext strong {
  color: var(--ink);
}

.cdt-17__buy {
  inline-size: 100%;
  min-block-size: 52px;
  margin-block-start: 18px;
  padding: 15px 18px;
  border: 3px solid var(--rule);
  background: var(--ink);
  color: var(--card);
  font: 400 15px/1 var(--font-display);
  letter-spacing: 0.04em;
  text-transform: uppercase;
  cursor: pointer;
}

.cdt-17__buy:hover {
  background: var(--accent);
  color: var(--ink);
}

.cdt-17__buy:focus-visible {
  outline: 3px solid var(--danger);
  outline-offset: 2px;
}

.cdt-17__cut {
  margin: 10px 0 0;
  font-size: 11.5px;
  line-height: 1.55;
  color: var(--muted);
}

.cdt-17__live {
  display: block;
  min-block-size: 1.1em;
  margin-block-start: 6px;
  font: 600 12px/1.3 system-ui, sans-serif;
  color: var(--danger);
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-17 {
  position: relative;
}

.cdt-17__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-17__tglbtn {
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

.cdt-17__tglbtn:hover {
  opacity: 1;
}

.cdt-17__tgl:focus-visible + .cdt-17__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-17__tglbtn svg {
  flex: none;
}

.cdt-17__sun,
.cdt-17__lighttext {
  display: none;
}

.cdt-17:has(.cdt-17__tgl:checked) .cdt-17__moon,
.cdt-17:has(.cdt-17__tgl:checked) .cdt-17__darktext {
  display: none;
}

.cdt-17:has(.cdt-17__tgl:checked) .cdt-17__sun {
  display: block;
}

.cdt-17:has(.cdt-17__tgl:checked) .cdt-17__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-17__tglbtn {
    padding: 12px;
  }

  .cdt-17__darktext,
    .cdt-17__lighttext,
    .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__darktext,
    .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-17:has(.cdt-17__tgl:checked) {
    --page: #111110;
    --card: #1a1a18;
    --ink: #f7f6f1;
    --muted: #a3a19a;
    --rule: #f7f6f1;
    --accent: #ffd93b;
    --danger: #ff6a5c;
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__badge {
    color: #111110;
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__buy {
    background: var(--accent);
    color: #111110;
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__buy:hover {
    background: var(--card);
    color: var(--ink);
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__shotart::after {
    background: #1a1a18;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-17 {
    --page: #111110;
    --card: #1a1a18;
    --ink: #f7f6f1;
    --muted: #a3a19a;
    --rule: #f7f6f1;
    --accent: #ffd93b;
    --danger: #ff6a5c;
  }

  .cdt-17__badge {
    color: #111110;
  }

  .cdt-17__buy {
    background: var(--accent);
    color: #111110;
  }

  .cdt-17__buy:hover {
    background: var(--card);
    color: var(--ink);
  }

  .cdt-17__shotart::after {
    background: #1a1a18;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-17:has(.cdt-17__tgl:checked) {
    --page: oklch(95.5% 0.01 90);
    --card: oklch(100% 0 0);
    --ink: oklch(10% 0 0);
    --muted: oklch(48% 0.006 80);
    --rule: #0c0c0c;
    --accent: oklch(88% 0.17 96);
    --danger: oklch(53% 0.22 28);
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__badge {
    color: var(--accent);
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__buy {
    background: var(--ink);
    color: var(--card);
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__buy:hover {
    background: var(--accent);
    color: var(--ink);
  }

  .cdt-17:has(.cdt-17__tgl:checked) .cdt-17__shotart::after {
    background: var(--card);
  }
}

[data-theme="dark"] .cdt-17 {
  --page: #111110;
  --card: #1a1a18;
  --ink: #f7f6f1;
  --muted: #a3a19a;
  --rule: #f7f6f1;
  --accent: #ffd93b;
  --danger: #ff6a5c;
}

[data-theme="dark"] .cdt-17 .cdt-17__buy {
  background: var(--accent);
  color: #111110;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-17');
if (root) {
  const q = (s) => root.querySelector(s);
  const clock = q('[data-clock]'), box = q('[data-timer]'), live = q('[data-live]'), pad = (n) => String(n).padStart(2, '0');
  const target = new Date(Date.now() + 5 * 3600e3 + 12 * 60e3 + 44e3);
  let id = 0, seen = null;
  clock.dateTime = target.toISOString();
  const end = () => {
    box.setAttribute('data-ended', ''); box.removeAttribute('data-urgent');
    q('[data-tlabel]').textContent = 'Spring Sale ended';
    clock.innerHTML = '<span><b>00</b><i>hrs</i></span>';
    q('[data-now]').textContent = '$690'; q('[data-was]').remove();
    q('[data-save]').textContent = 'Sale ended · full price';
    q('[data-buy]').textContent = 'Add to cart · $690';
    live.textContent = 'The Spring Sale has ended. The price shown is now the full price.';
  };
  const tick = () => {
    const ms = target - Date.now();
    if (ms <= 0) return end();
    const s = Math.floor(ms / 1000);
    q('[data-h]').textContent = pad(Math.floor(s / 3600));
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    box.toggleAttribute('data-urgent', ms <= 3600e3);
    const b = ms < 60e3 ? 'm1' : ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', h1: 'Less than one hour left in the Spring Sale.', m10: 'Ten minutes left in the Spring Sale.', m1: 'One minute left in the Spring Sale.' }[b]; }
    id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
