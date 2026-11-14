---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/auction-ending-countdown-with-anti-snipe/"
title: "Auction Ending Countdown with Anti Snipe"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A lot card whose countdown turns red under a minute and, when a bid lands in the closing seconds, visibly extends by two minutes with an Extended +2:00 flash."
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auction Ending Countdown with Anti Snipe
Source: https://codefronts.com/snippets/css-countdown-timers/auction-ending-countdown-with-anti-snipe/

A lot card whose countdown turns red under a minute and, when a bid lands in the closing seconds, visibly extends by two minutes with an Extended +2:00 flash. That soft-close rule is what keeps a last-second snipe from deciding the sale, and it is the one countdown where a real-time exemption to adjustable timing genuinely applies.
## HTML
```html
<section class="cdt-07" aria-labelledby="cdt-07-title">
  <input class="cdt-07__tgl" type="checkbox" id="cdt-07-theme">
  <label class="cdt-07__tglbtn" for="cdt-07-theme">
    <svg class="cdt-07__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-07__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-07__darktext">Dark mode</span><span class="cdt-07__lighttext">Light mode</span>
  </label>
  <div class="cdt-07__stage">
    <article class="cdt-07__card">
      <div class="cdt-07__thumb" aria-hidden="true">
        <span class="cdt-07__thumbmark">Lot 214</span>
        <div class="cdt-07__thumbart"></div>
      </div>

      <div class="cdt-07__body">
        <p class="cdt-07__pill">Live · soft close</p>
        <h2 class="cdt-07__title" id="cdt-07-title">Basalt No. 4 letterpress cabinet, 1948</h2>
        <p class="cdt-07__meta">Ranger Auction House · 32 bids · reserve met</p>

        <div class="cdt-07__bid">
          <span class="cdt-07__bidlabel">Current bid</span>
          <strong class="cdt-07__bidval">$4,150</strong>
        </div>

        <div class="cdt-07__timer" role="timer" data-timer>
          <span class="cdt-07__icon" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="17" height="17"><circle cx="10" cy="10" r="7.6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 6.2V10l2.6 1.7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
          </span>
          <time class="cdt-07__clock" datetime="" data-clock>00:58</time>
          <span class="cdt-07__cap" data-cap>until bidding closes</span>
        </div>

        <p class="cdt-07__flash" data-flash hidden>Extended +2:00 — a bid landed in the final minute</p>

        <div class="cdt-07__actions">
          <button class="cdt-07__btn" type="button" data-bid>Bid $4,200</button>
          <button class="cdt-07__btn cdt-07__btn--ghost" type="button">Watch lot</button>
        </div>

        <ul class="cdt-07__log" data-log aria-label="Recent bids">
          <li><b>$4,150</b> Jordan Lee · 41s ago</li>
          <li><b>$4,050</b> Sam Rivera · 2m ago</li>
        </ul>
        <p class="cdt-07__rule">Any bid in the final minute moves the close two minutes out. Auctions are a real-time event, so the clock is the same for every bidder and cannot be extended on request.</p>
        <output class="cdt-07__sr" aria-live="polite" data-live></output>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
.cdt-07 {
  --page: #f4f1ea;
  --card: #fffefb;
  --ink: #14100c;
  --muted: #6a6157;
  --rule: #1a1512;
  --accent: #14100c;
  --danger: #cc2115;
  --shadow-offset: 7px;
  --font-display: "Archivo Narrow", "Oswald", "Helvetica Neue", ui-sans-serif, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-07 {
    --page: oklch(95% 0.014 85);
    --card: oklch(99% 0.006 85);
    --ink: oklch(17% 0.014 60);
    --muted: oklch(50% 0.018 65);
    --rule: oklch(20% 0.016 60);
    --danger: oklch(52% 0.22 28);
  }
}

.cdt-07 *,
.cdt-07 *::before,
.cdt-07 *::after {
  box-sizing: border-box;
}

.cdt-07__stage {
  display: grid;
  place-content: center;
  justify-items: center;
  min-height: 100vh;
  padding: clamp(16px, 4vw, 44px);
}

.cdt-07__card {
  inline-size: min(760px, 100%);
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  background: var(--card);
  border: 2px solid var(--rule);
  box-shadow: var(--shadow-offset) var(--shadow-offset) 0 0 var(--rule);
}

@media (min-width: 720px) {
  .cdt-07__card {
    grid-template-columns: 244px minmax(0, 1fr);
  }
}

.cdt-07__thumb {
  position: relative;
  min-inline-size: 0;
  min-block-size: 190px;
  padding: 14px;
  background: #e8e2d5;
  border-block-end: 2px solid var(--rule);
  overflow: hidden;
}

@media (min-width: 720px) {
  .cdt-07__thumb {
    border-block-end: 0;
    border-inline-end: 2px solid var(--rule);
  }
}

.cdt-07__thumbmark {
  position: relative;
  z-index: 1;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
}

.cdt-07__thumbart {
  position: absolute;
  inset: 30px 22px 18px;
  background: repeating-linear-gradient(90deg, #cfc6b2 0 12px, #ded6c6 12px 24px);
  border: 2px solid var(--rule);
}

.cdt-07__thumbart::after {
  content: "";
  position: absolute;
  inset-inline: 14px;
  inset-block-start: 22%;
  block-size: 34%;
  background: var(--card);
  border: 2px solid var(--rule);
}

.cdt-07__body {
  min-inline-size: 0;
  padding: clamp(16px, 3.4vw, 26px);
}

.cdt-07__pill {
  display: inline-block;
  margin: 0 0 12px;
  padding: 4px 9px;
  background: var(--rule);
  color: var(--card);
  font: 600 10px/1 var(--font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.cdt-07__title {
  margin: 0 0 6px;
  font: 600 clamp(19px, 3.4vw, 25px)/1.18 var(--font-display);
  letter-spacing: -0.005em;
  text-wrap: balance;
}

.cdt-07__meta {
  margin: 0 0 18px;
  font-size: 12.5px;
  color: var(--muted);
}

.cdt-07__bid {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 4px 10px;
  padding-block-end: 14px;
  border-block-end: 1px solid rgba(26, 21, 18, 0.16);
}

.cdt-07__bidlabel {
  font: 500 10.5px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-07__bidval {
  font: 600 clamp(24px, 5vw, 32px)/1 var(--font-display);
  font-variant-numeric: tabular-nums;
}

.cdt-07__timer {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px 10px;
  margin-block-start: 14px;
  padding: 12px 14px;
  border: 2px solid var(--rule);
  background: var(--page);
}

.cdt-07__icon {
  display: flex;
  flex: none;
}

.cdt-07__clock {
  font: 600 clamp(28px, 7vw, 40px)/1 var(--font-display);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
  min-inline-size: 4.4ch;
}

.cdt-07__cap {
  flex: 1 1 120px;
  min-inline-size: 0;
  font-size: 12px;
  color: var(--muted);
}

.cdt-07__timer[data-urgent] {
  color: var(--danger);
  border-color: var(--danger);
  background: rgba(204, 33, 21, 0.06);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-07__timer[data-urgent] {
    background: color-mix(in oklab, var(--danger) 8%, var(--card));
  }
}

.cdt-07__timer[data-urgent] .cdt-07__cap {
  color: var(--danger);
  font-weight: 600;
}

.cdt-07__flash {
  margin: 10px 0 0;
  padding: 9px 12px;
  background: rgba(204, 33, 21, 0.1);
  border-inline-start: 4px solid var(--danger);
  font: 600 12.5px/1.4 var(--font-display);
  color: var(--danger);
  animation: cdt07-flash 0.4s ease-out;
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-07__flash {
    background: color-mix(in oklab, var(--danger) 12%, var(--card));
  }
}

.cdt-07__flash[hidden] {
  display: none;
}

@keyframes cdt07-flash {
  from {
    opacity: 0;
    transform: translateY(-6px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.cdt-07__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-block-start: 16px;
}

.cdt-07__btn {
  flex: 1 1 150px;
  min-block-size: 46px;
  min-inline-size: 44px;
  padding: 12px 16px;
  border: 2px solid var(--rule);
  background: var(--rule);
  color: var(--card);
  font: 600 14px/1 var(--font-display);
  letter-spacing: 0.02em;
  cursor: pointer;
}

.cdt-07__btn--ghost {
  background: transparent;
  color: var(--ink);
}

.cdt-07__btn:hover {
  transform: translate(-1px, -1px);
}

.cdt-07__btn:focus-visible {
  outline: 2px solid var(--danger);
  outline-offset: 2px;
}

.cdt-07__log {
  display: grid;
  gap: 6px;
  margin: 16px 0 0;
  padding: 0;
  list-style: none;
  font-size: 12px;
  color: var(--muted);
}

.cdt-07__log b {
  font-variant-numeric: tabular-nums;
  color: var(--ink);
}

.cdt-07__rule {
  margin: 14px 0 0;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-07__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (prefers-reduced-motion: reduce) {
  .cdt-07__flash {
    animation: none;
  }

  .cdt-07__btn:hover {
    transform: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-07 {
  position: relative;
}

.cdt-07__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-07__tglbtn {
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

.cdt-07__tglbtn:hover {
  opacity: 1;
}

.cdt-07__tgl:focus-visible + .cdt-07__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-07__tglbtn svg {
  flex: none;
}

.cdt-07__sun,
.cdt-07__lighttext {
  display: none;
}

.cdt-07:has(.cdt-07__tgl:checked) .cdt-07__moon,
.cdt-07:has(.cdt-07__tgl:checked) .cdt-07__darktext {
  display: none;
}

.cdt-07:has(.cdt-07__tgl:checked) .cdt-07__sun {
  display: block;
}

.cdt-07:has(.cdt-07__tgl:checked) .cdt-07__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-07__tglbtn {
    padding: 12px;
  }

  .cdt-07__darktext,
    .cdt-07__lighttext,
    .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__darktext,
    .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-07:has(.cdt-07__tgl:checked) {
    --page: #17140f;
    --card: #1f1b16;
    --ink: #f6f1e6;
    --muted: #a2988a;
    --rule: #f6f1e6;
    --danger: #ff6b5e;
  }

  .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__pill,
    .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__btn {
    color: #17140f;
  }

  .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__thumb {
    background: #2a251d;
  }

  .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__thumbart {
    background: repeating-linear-gradient(90deg, #3a3227 0 12px, #443b2e 12px 24px);
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-07 {
    --page: #17140f;
    --card: #1f1b16;
    --ink: #f6f1e6;
    --muted: #a2988a;
    --rule: #f6f1e6;
    --danger: #ff6b5e;
  }

  .cdt-07__pill,
    .cdt-07__btn {
    color: #17140f;
  }

  .cdt-07__thumb {
    background: #2a251d;
  }

  .cdt-07__thumbart {
    background: repeating-linear-gradient(90deg, #3a3227 0 12px, #443b2e 12px 24px);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-07:has(.cdt-07__tgl:checked) {
    --page: oklch(95% 0.014 85);
    --card: oklch(99% 0.006 85);
    --ink: oklch(17% 0.014 60);
    --muted: oklch(50% 0.018 65);
    --rule: oklch(20% 0.016 60);
    --danger: oklch(52% 0.22 28);
  }

  .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__pill,
    .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__btn {
    color: var(--card);
  }

  .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__thumb {
    background: #e8e2d5;
  }

  .cdt-07:has(.cdt-07__tgl:checked) .cdt-07__thumbart {
    background: repeating-linear-gradient(90deg, #cfc6b2 0 12px, #ded6c6 12px 24px);
  }
}

[data-theme="dark"] .cdt-07 {
  --page: #17140f;
  --card: #1f1b16;
  --ink: #f6f1e6;
  --muted: #a2988a;
  --rule: #f6f1e6;
  --danger: #ff6b5e;
}

[data-theme="dark"] .cdt-07 .cdt-07__pill,
[data-theme="dark"] .cdt-07 .cdt-07__btn {
  color: #17140f;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-07');
if (root) {
  const q = (s) => root.querySelector(s);
  const clock = q('[data-clock]'), cap = q('[data-cap]'), box = q('[data-timer]');
  const flash = q('[data-flash]'), live = q('[data-live]'), log = q('[data-log]');
  const SOFT = 60e3, BUMP = 120e3;
  let target = Date.now() + 58e3, id = 0, seen = null, bid = 4150;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    clock.textContent = String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
    clock.dateTime = new Date(target).toISOString();
    const urgent = ms > 0 && ms <= SOFT;
    box.toggleAttribute('data-urgent', urgent);
    if (ms > 0) cap.textContent = urgent ? 'Final minute · bids extend the close' : 'until bidding closes';
    const b = ms <= 0 ? 'end' : urgent ? 'urgent' : 'open';
    if (b !== seen) { seen = b; live.textContent = b === 'end' ? 'Bidding closed at ' + bid.toLocaleString() + ' dollars.' : b === 'urgent' ? 'Final minute of bidding.' : ''; }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); } else { clock.textContent = 'Closed'; cap.textContent = 'Bidding closed · lot sold'; q('[data-bid]').disabled = true; }
  };
  q('[data-bid]').addEventListener('click', (e) => {
    if (e.currentTarget.disabled) return;
    bid += 50; q('.cdt-07__bidval').textContent = '$' + bid.toLocaleString();
    e.currentTarget.textContent = 'Bid $' + (bid + 50).toLocaleString();
    log.insertAdjacentHTML('afterbegin', '<li><b>$' + bid.toLocaleString() + '</b> You · just now</li>');
    if (target - Date.now() <= SOFT) {
      target = Date.now() + BUMP; flash.hidden = false; seen = null;
      live.textContent = 'Bid accepted. Closing time extended by two minutes.';
    }
  });
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
