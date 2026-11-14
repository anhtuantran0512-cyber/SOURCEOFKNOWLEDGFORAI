---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/free-shipping-threshold-progress-bar/"
title: "Free Shipping Threshold Progress Bar"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "The single highest-converting bar in e-commerce, built properly: a real role=\"progressbar\" with aria-valuenow, milestone markers that light up as you cross…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Free Shipping Threshold Progress Bar
Source: https://codefronts.com/snippets/css-banners-alerts/free-shipping-threshold-progress-bar/

The single highest-converting bar in e-commerce, built properly: a real role="progressbar" with aria-valuenow, milestone markers that light up as you cross them, an animated gradient fill driven by one registered percentage, and an unlocked state that the CSS derives itself with :has() — no state class juggling in JavaScript.
## HTML
```html
<div class="ba-03">
  <section class="ba-03__cart" aria-labelledby="ba-03-h">
    <header class="ba-03__head">
      <h2 class="ba-03__h" id="ba-03-h">Your basket <span>3 items</span></h2>
      <p class="ba-03__sub">Delivered by <time datetime="2026-08-14">Fri 14 Aug</time></p>
    </header>

    <div class="ba-03__banner" data-banner>
      <p class="ba-03__msg" data-msg>
        <span class="ba-03__lockIcon" aria-hidden="true">
          <svg class="ba-03__iLock" viewBox="0 0 20 20" fill="none" focusable="false"><rect x="4.2" y="8.8" width="11.6" height="8" rx="2.2" stroke="currentColor" stroke-width="1.6"/><path d="M7.2 8.8V6.6a2.8 2.8 0 0 1 5.6 0v2.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          <svg class="ba-03__iTruck" viewBox="0 0 20 20" fill="none" focusable="false"><path d="M2.5 6.5h8.2v7.2H2.5zM10.7 9h3l2.8 2.6v2.1h-5.8z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="6.2" cy="15" r="1.5" stroke="currentColor" stroke-width="1.4"/><circle cx="13.6" cy="15" r="1.5" stroke="currentColor" stroke-width="1.4"/></svg>
        </span>
        <span class="ba-03__msgText" data-msgtext>Spend <strong data-gap>£24.00</strong> more for free next-day delivery</span>
      </p>

      <div class="ba-03__track" role="progressbar" aria-labelledby="ba-03-h" aria-valuemin="0" aria-valuemax="75" aria-valuenow="51" aria-valuetext="£51.00 of £75.00 towards free delivery" data-track>
        <span class="ba-03__fill" data-fill></span>
        <span class="ba-03__tick" style="--at:40"><span class="ba-03__tickLabel">£30</span></span>
        <span class="ba-03__tick ba-03__tick--goal" style="--at:100"><span class="ba-03__tickLabel">£75</span></span>
      </div>
      <p class="ba-03__scale"><span>£0</span><span data-total>£51.00</span></p>
    </div>

    <ul class="ba-03__items">
      <li class="ba-03__item" data-price="1800" data-qty="1">
        <div class="ba-03__itemText"><p class="ba-03__name">Cable-knit beanie</p><p class="ba-03__var">Oat · One size</p></div>
        <div class="ba-03__qty">
          <button type="button" data-step="-1" aria-label="Decrease quantity of Cable-knit beanie">−</button>
          <span data-count aria-live="off">1</span>
          <button type="button" data-step="1" aria-label="Increase quantity of Cable-knit beanie">+</button>
        </div>
        <p class="ba-03__price" data-line>£18.00</p>
      </li>
      <li class="ba-03__item" data-price="2400" data-qty="1">
        <div class="ba-03__itemText"><p class="ba-03__name">Court trainer, low</p><p class="ba-03__var">Chalk · UK 9</p></div>
        <div class="ba-03__qty">
          <button type="button" data-step="-1" aria-label="Decrease quantity of Court trainer">−</button>
          <span data-count aria-live="off">1</span>
          <button type="button" data-step="1" aria-label="Increase quantity of Court trainer">+</button>
        </div>
        <p class="ba-03__price" data-line>£24.00</p>
      </li>
      <li class="ba-03__item" data-price="900" data-qty="1">
        <div class="ba-03__itemText"><p class="ba-03__name">House blend, 250g</p><p class="ba-03__var">Whole bean</p></div>
        <div class="ba-03__qty">
          <button type="button" data-step="-1" aria-label="Decrease quantity of House blend">−</button>
          <span data-count aria-live="off">1</span>
          <button type="button" data-step="1" aria-label="Increase quantity of House blend">+</button>
        </div>
        <p class="ba-03__price" data-line>£9.00</p>
      </li>
    </ul>

    <footer class="ba-03__foot">
      <p class="ba-03__sum">Subtotal<strong data-subtotal>£51.00</strong></p>
      <button class="ba-03__checkout" type="button">Checkout</button>
    </footer>
  </section>
  <p class="ba-03__live" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

@property --ba-03-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.ba-03 {
  --threshold: 75;
  --bar-h: .75rem;
  --bg: #f6f6f4;
  --surface: #ffffff;
  --ink: #101211;
  --muted: #6a706d;
  --line: #e4e6e3;
  --acc: #1f6feb;
  --acc-2: #6ba8ff;
  --ok: #10a05a;
  --ink-inv: #ffffff;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(50rem 30rem at 50% -10%, color-mix(in oklab,var(--acc) 12%,transparent), transparent 70%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-03 *,
.ba-03 *::before,
.ba-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-03 {
    --bg: oklch(97% .004 150);
    --surface: oklch(100% 0 0);
    --ink: oklch(18% .01 160);
    --muted: oklch(55% .012 160);
    --line: oklch(92% .008 155);
    --acc: oklch(56% .19 255);
    --acc-2: oklch(74% .13 255);
    --ok: oklch(62% .16 155);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-03:not([data-theme="light"]) {
    --bg: #0a0c0b;
    --surface: #131615;
    --ink: #f0f2f1;
    --muted: #98a09d;
    --line: #242927;
  }
}

.ba-03[data-theme="dark"] {
  --bg: #0a0c0b;
  --surface: #131615;
  --ink: #f0f2f1;
  --muted: #98a09d;
  --line: #242927;
}

.ba-03__cart {
  container-type: inline-size;
  width: min(38rem,100%);
  display: grid;
  gap: 1rem;
  padding: clamp(1rem,3vw,1.5rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  box-shadow: 0 2rem 4rem -2rem rgb(16 18 17 / .18);
}

.ba-03__cart:has([data-state="unlocked"]) {
  --acc: var(--ok);
  --acc-2: color-mix(in oklab,var(--ok) 55%,white);
}

.ba-03__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.ba-03__h {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 800;
  letter-spacing: -.03em;
}

.ba-03__h span {
  font-weight: 500;
  color: var(--muted);
  font-size: .8125rem;
  margin-inline-start: .4rem;
}

.ba-03__sub {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.ba-03__banner {
  display: grid;
  gap: .6rem;
  padding: .9rem 1rem 1rem;
  border-radius: 1.125rem;
  background: color-mix(in oklab,var(--acc) 7%,var(--surface));
  border: 1px solid color-mix(in oklab,var(--acc) 22%,var(--line));
}

.ba-03__msg {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .875rem;
  letter-spacing: -.01em;
}

.ba-03__lockIcon {
  display: grid;
  place-items: center;
  width: 1.75rem;
  height: 1.75rem;
  flex: none;
  border-radius: .6rem;
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 14%,transparent);
  transition: rotate .4s cubic-bezier(.34,1.56,.64,1), scale .4s cubic-bezier(.34,1.56,.64,1);
}

.ba-03__lockIcon svg {
  width: 1.125rem;
  height: 1.125rem;
  grid-area: 1/1;
}

.ba-03__iTruck {
  display: none;
}

.ba-03__msg[data-state="unlocked"] .ba-03__iLock {
  display: none;
}

.ba-03__msg[data-state="unlocked"] .ba-03__iTruck {
  display: block;
}

.ba-03__msg[data-state="unlocked"] .ba-03__lockIcon {
  rotate: -8deg;
  scale: 1.08;
}

.ba-03__msgText strong {
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.ba-03__track {
  position: relative;
  height: var(--bar-h);
  border-radius: 999px;
  overflow: visible;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
}

.ba-03__fill {
  --ba-03-p: 0%;
  display: block;
  height: 100%;
  width: var(--ba-03-p);
  border-radius: 999px;
  position: relative;
  overflow: hidden;
  background: linear-gradient(90deg,var(--acc),var(--acc-2));
  transition: width .7s cubic-bezier(.16,1,.3,1);
  box-shadow: 0 0 1.25rem -.25rem color-mix(in oklab,var(--acc) 65%,transparent);
}

.ba-03__fill::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg,transparent 30%,rgb(255 255 255 / .55) 50%,transparent 70%);
  translate: -100% 0;
  animation: ba-03-shimmer 2.4s linear infinite;
}

.ba-03__banner:has([data-state="unlocked"]) .ba-03__fill::after {
  animation: none;
  opacity: 0;
}

@keyframes ba-03-shimmer {
  to {
    translate: 200% 0;
  }
}

.ba-03__tick {
  position: absolute;
  inset-block: -.3rem;
  inset-inline-start: calc(var(--at) * 1%);
  width: 2px;
  translate: -1px 0;
  border-radius: 2px;
  background: color-mix(in oklab,var(--ink) 22%,transparent);
}

.ba-03__tick--goal {
  background: color-mix(in oklab,var(--acc) 60%,transparent);
}

.ba-03__tickLabel {
  position: absolute;
  inset-block-start: 1.1rem;
  inset-inline-start: 50%;
  translate: -50% 0;
  font-size: .625rem;
  font-weight: 700;
  color: var(--muted);
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}

.ba-03__tick--goal .ba-03__tickLabel {
  translate: -100% 0;
}

.ba-03__scale {
  margin: 1.1rem 0 0;
  display: flex;
  justify-content: space-between;
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.ba-03__items {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
}

.ba-03__item {
  display: grid;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: .75rem;
  padding: .75rem 0;
  border-top: 1px solid var(--line);
}

.ba-03__name {
  margin: 0;
  font-size: .875rem;
  font-weight: 700;
  letter-spacing: -.015em;
}

.ba-03__var {
  margin: .15rem 0 0;
  font-size: .75rem;
  color: var(--muted);
}

.ba-03__qty {
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--line);
  border-radius: .7rem;
  overflow: hidden;
}

.ba-03__qty button {
  width: 2.25rem;
  height: 2.25rem;
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  border: 0;
  background: transparent;
  color: var(--ink);
  transition: background .18s ease, color .18s ease;
}

.ba-03__qty button:hover {
  background: color-mix(in oklab,var(--acc) 12%,transparent);
  color: var(--acc);
}

.ba-03__qty span {
  min-width: 1.75rem;
  text-align: center;
  font-size: .8125rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.ba-03__price {
  margin: 0;
  min-width: 4.25rem;
  text-align: end;
  font-size: .875rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.ba-03__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-top: .85rem;
  border-top: 1px solid var(--line);
  flex-wrap: wrap;
}

.ba-03__sum {
  margin: 0;
  display: flex;
  gap: .5rem;
  align-items: baseline;
  font-size: .8125rem;
  color: var(--muted);
  font-weight: 600;
}

.ba-03__sum strong {
  font-size: 1.25rem;
  color: var(--ink);
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.ba-03__checkout {
  min-height: 2.75rem;
  padding: .75rem 1.4rem;
  border-radius: .85rem;
  cursor: pointer;
  border: 0;
  font: inherit;
  font-size: .875rem;
  font-weight: 800;
  letter-spacing: -.01em;
  background: var(--ink);
  color: var(--surface);
  transition: translate .22s cubic-bezier(.16,1,.3,1), box-shadow .22s ease;
}

.ba-03__checkout:hover {
  translate: 0 -1px;
  box-shadow: 0 .8rem 1.6rem -.8rem rgb(16 18 17 / .5);
}

.ba-03 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-03__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 26rem) {
  .ba-03__item {
    grid-template-columns: 1fr auto;
    grid-template-areas: "text text" "qty price";
  }

  .ba-03__itemText {
    grid-area: text;
  }

  .ba-03__qty {
    grid-area: qty;
  }

  .ba-03__price {
    grid-area: price;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-03 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-03__fill {
    background: Highlight;
  }

  .ba-03__banner,
    .ba-03__cart {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-03');
  if (!root) return;
  const money = new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP' });
  const threshold = Number(getComputedStyle(root).getPropertyValue('--threshold')) * 100;
  const items = [...root.querySelectorAll('.ba-03__item')];
  const fill = root.querySelector('[data-fill]');
  const track = root.querySelector('[data-track]');
  const msg = root.querySelector('[data-msg]');
  const live = root.querySelector('.ba-03__live');
  let wasUnlocked = false;

  const render = () => {
    const total = items.reduce((sum, li) => {
      const qty = Number(li.dataset.qty), price = Number(li.dataset.price);
      li.querySelector('[data-count]').textContent = qty;
      li.querySelector('[data-line]').textContent = money.format((price * qty) / 100);
      li.querySelector('[data-step="-1"]').disabled = qty <= 1;
      return sum + price * qty;
    }, 0);
    const pct = Math.min(100, (total / threshold) * 100);
    const gap = Math.max(0, threshold - total);
    fill.style.setProperty('--ba-03-p', pct + '%');
    track.setAttribute('aria-valuenow', (total / 100).toFixed(2));
    track.setAttribute('aria-valuetext', money.format(total / 100) + ' of ' + money.format(threshold / 100) + ' towards free delivery');
    root.querySelector('[data-total]').textContent = money.format(total / 100);
    root.querySelector('[data-subtotal]').textContent = money.format(total / 100);
    root.querySelector('.ba-03__h span').textContent = items.reduce((n, li) => n + Number(li.dataset.qty), 0) + ' items';

    const unlocked = gap === 0;
    msg.dataset.state = unlocked ? 'unlocked' : 'locked';
    msg.querySelector('[data-msgtext]').innerHTML = unlocked
      ? 'Free next-day delivery unlocked'
      : 'Spend <strong data-gap>' + money.format(gap / 100) + '</strong> more for free next-day delivery';
    if (unlocked !== wasUnlocked) { live.textContent = unlocked ? 'Free delivery unlocked.' : money.format(gap / 100) + ' to free delivery.'; wasUnlocked = unlocked; }
  };

  root.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-step]');
    if (!btn) return;
    const li = btn.closest('.ba-03__item');
    li.dataset.qty = Math.max(1, Number(li.dataset.qty) + Number(btn.dataset.step));
    render();
  });
  render();
})();
```
