---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/coming-soon-product-launch-landing-pages/"
title: "Coming Soon Launch Page Countdown"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "The classic pre-launch splash, rebuilt: a brand mark, one headline, four unit blocks for days, hours, minutes and seconds, and a single email field."
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Coming Soon Launch Page Countdown
Source: https://codefronts.com/snippets/css-countdown-timers/coming-soon-product-launch-landing-pages/

The classic pre-launch splash, rebuilt: a brand mark, one headline, four unit blocks for days, hours, minutes and seconds, and a single email field. Where most versions stall at zero, this one flips the whole page to a live state, because the day the countdown ends is the day the page has to still make sense.
## HTML
```html
<section class="cdt-20" aria-labelledby="cdt-20-title">
  <input class="cdt-20__tgl" type="checkbox" id="cdt-20-theme">
  <label class="cdt-20__tglbtn" for="cdt-20-theme">
    <svg class="cdt-20__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-20__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-20__darktext">Dark mode</span><span class="cdt-20__lighttext">Light mode</span>
  </label>
  <div class="cdt-20__stage">
    <p class="cdt-20__mark">Aperture</p>

    <div class="cdt-20__lead">
      <h2 class="cdt-20__title" id="cdt-20-title" data-title>The archive opens in</h2>
      <p class="cdt-20__sub" data-sub>Forty years of Meridian's print catalogue, scanned, indexed and free to read.</p>
    </div>

    <div class="cdt-20__clock" role="timer" data-clockwrap>
      <time class="cdt-20__blocks" datetime="" data-clock>
        <span class="cdt-20__block"><b data-d>04</b><i>days</i></span>
        <span class="cdt-20__block"><b data-h>11</b><i>hours</i></span>
        <span class="cdt-20__block"><b data-m>28</b><i>minutes</i></span>
        <span class="cdt-20__block"><b data-s>05</b><i>seconds</i></span>
      </time>
      <p class="cdt-20__live" data-livecopy hidden>We are live — start reading</p>
    </div>

    <div class="cdt-20__form">
      <label class="cdt-20__label" for="cdt-20-email">Email me when it opens</label>
      <div class="cdt-20__row">
        <input class="cdt-20__input" id="cdt-20-email" type="email" inputmode="email" autocomplete="email" placeholder="[email protected]">
        <button class="cdt-20__btn" type="button" data-cta>Notify me</button>
      </div>
      <p class="cdt-20__meta">No newsletter, one message on launch day. 2,140 people waiting.</p>
    </div>
    <output class="cdt-20__sr" aria-live="polite" data-live></output>
  </div>
</section>
```
## CSS
```css
.cdt-20 {
  --field-a: #e7e2ff;
  --field-b: #d9f2e6;
  --ink: #14121a;
  --muted: #5c5871;
  --edge: rgba(20, 18, 26, 0.14);
  --accent: #14121a;
  --digit: 76px;
  --font-display: "Iowan Old Style", "Playfair Display", Georgia, ui-serif, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  color: var(--ink);
  background: linear-gradient(150deg, var(--field-a), var(--field-b) 70%, #fdfbf6);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-20 {
    --field-a: oklch(91% 0.05 295);
    --field-b: oklch(93% 0.05 160);
    --ink: oklch(17% 0.02 290);
    --muted: oklch(46% 0.03 290);
  }
}

.cdt-20 *,
.cdt-20 *::before,
.cdt-20 *::after {
  box-sizing: border-box;
}

.cdt-20__stage {
  display: grid;
  gap: clamp(20px, 4vw, 34px);
  align-content: center;
  justify-items: center;
  min-height: 100vh;
  max-inline-size: 880px;
  margin-inline: auto;
  padding: clamp(20px, 5vw, 64px);
  text-align: center;
}

.cdt-20__mark {
  margin: 0;
  font: 400 13px/1 var(--font-display);
  letter-spacing: 0.42em;
  text-transform: uppercase;
}

.cdt-20__lead {
  min-inline-size: 0;
}

.cdt-20__title {
  margin: 0 0 10px;
  font: 400 clamp(30px, 7vw, 60px)/1.05 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.cdt-20__sub {
  margin: 0;
  max-inline-size: 46ch;
  font-size: clamp(13.5px, 2vw, 15.5px);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-20__clock {
  inline-size: 100%;
}

.cdt-20__blocks {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(132px, 1fr));
  gap: clamp(10px, 2vw, 18px);
  font-variant-numeric: tabular-nums;
}

.cdt-20__blocks[hidden] {
  display: none;
}

.cdt-20__block {
  display: grid;
  gap: 8px;
  justify-items: center;
  min-inline-size: 0;
  padding: clamp(14px, 2.6vw, 22px) 6px;
  border: 1px solid var(--edge);
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.42);
}

.cdt-20__block b {
  font: 400 clamp(40px, 10vw, var(--digit))/0.9 var(--font-display);
  letter-spacing: -0.04em;
  font-variant-numeric: tabular-nums;
}

.cdt-20__block i {
  font: 500 10px/1 system-ui, sans-serif;
  font-style: normal;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-20__live {
  margin: 0;
  padding: clamp(18px, 4vw, 30px) 12px;
  border: 1px solid var(--edge);
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.55);
  font: 400 clamp(26px, 6vw, 46px)/1.1 var(--font-display);
  letter-spacing: -0.03em;
}

.cdt-20__live[hidden] {
  display: none;
}

.cdt-20__form {
  inline-size: min(500px, 100%);
}

.cdt-20__label {
  display: block;
  margin-block-end: 8px;
  font: 500 10.5px/1 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-20__row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.cdt-20__input {
  flex: 1 1 200px;
  min-inline-size: 0;
  min-block-size: 50px;
  padding: 14px 16px;
  border: 1px solid var(--edge);
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.7);
  color: var(--ink);
  font-size: 15px;
}

.cdt-20__input::placeholder {
  color: rgba(20, 18, 26, 0.4);
}

.cdt-20__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-20__btn {
  flex: 0 0 auto;
  min-block-size: 50px;
  min-inline-size: 44px;
  padding: 14px 24px;
  border: 1px solid var(--accent);
  border-radius: 2px;
  background: var(--accent);
  color: #fdfbf6;
  font: 500 14.5px/1 system-ui, sans-serif;
  letter-spacing: 0.02em;
  cursor: pointer;
}

.cdt-20__btn:hover {
  background: transparent;
  color: var(--accent);
}

.cdt-20__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cdt-20__meta {
  margin: 10px 0 0;
  font-size: 12px;
  color: var(--muted);
}

.cdt-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-20 {
  position: relative;
}

.cdt-20__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-20__tglbtn {
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

.cdt-20__tglbtn:hover {
  opacity: 1;
}

.cdt-20__tgl:focus-visible + .cdt-20__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-20__tglbtn svg {
  flex: none;
}

.cdt-20__sun,
.cdt-20__lighttext {
  display: none;
}

.cdt-20:has(.cdt-20__tgl:checked) .cdt-20__moon,
.cdt-20:has(.cdt-20__tgl:checked) .cdt-20__darktext {
  display: none;
}

.cdt-20:has(.cdt-20__tgl:checked) .cdt-20__sun {
  display: block;
}

.cdt-20:has(.cdt-20__tgl:checked) .cdt-20__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-20__tglbtn {
    padding: 12px;
  }

  .cdt-20__darktext,
    .cdt-20__lighttext,
    .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__darktext,
    .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-20:has(.cdt-20__tgl:checked) {
    --field-a: #191630;
    --field-b: #12241d;
    --ink: #f5f1ff;
    --muted: #a49fbe;
    --edge: rgba(245, 241, 255, 0.16);
    --accent: #f5f1ff;
    background: linear-gradient(150deg, #191630, #12241d 70%, #0b0912);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__block,
    .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__live {
    background: rgba(255, 255, 255, 0.05);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__input {
    background: rgba(255, 255, 255, 0.07);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__input::placeholder {
    color: rgba(245, 241, 255, 0.4);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__btn {
    color: #12101c;
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__btn:hover {
    color: var(--accent);
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-20 {
    --field-a: #191630;
    --field-b: #12241d;
    --ink: #f5f1ff;
    --muted: #a49fbe;
    --edge: rgba(245, 241, 255, 0.16);
    --accent: #f5f1ff;
    background: linear-gradient(150deg, #191630, #12241d 70%, #0b0912);
  }

  .cdt-20__block,
    .cdt-20__live {
    background: rgba(255, 255, 255, 0.05);
  }

  .cdt-20__input {
    background: rgba(255, 255, 255, 0.07);
  }

  .cdt-20__input::placeholder {
    color: rgba(245, 241, 255, 0.4);
  }

  .cdt-20__btn {
    color: #12101c;
  }

  .cdt-20__btn:hover {
    color: var(--accent);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-20:has(.cdt-20__tgl:checked) {
    --field-a: oklch(91% 0.05 295);
    --field-b: oklch(93% 0.05 160);
    --ink: oklch(17% 0.02 290);
    --muted: oklch(46% 0.03 290);
    --edge: rgba(20, 18, 26, 0.14);
    --accent: #14121a;
    background: linear-gradient(150deg, var(--field-a), var(--field-b) 70%, #fdfbf6);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__block,
    .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__live {
    background: rgba(255, 255, 255, 0.42);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__input {
    background: rgba(255, 255, 255, 0.7);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__input::placeholder {
    color: rgba(20, 18, 26, 0.4);
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__btn {
    color: #fdfbf6;
  }

  .cdt-20:has(.cdt-20__tgl:checked) .cdt-20__btn:hover {
    color: var(--accent);
  }
}

[data-theme="dark"] .cdt-20 {
  --field-a: #191630;
  --field-b: #12241d;
  --ink: #f5f1ff;
  --muted: #a49fbe;
  --edge: rgba(245, 241, 255, 0.16);
  --accent: #f5f1ff;
  background: linear-gradient(150deg, #191630, #12241d 70%, #0b0912);
}

[data-theme="dark"] .cdt-20 .cdt-20__block,
[data-theme="dark"] .cdt-20 .cdt-20__live {
  background: rgba(255, 255, 255, 0.05);
}

[data-theme="dark"] .cdt-20 .cdt-20__btn {
  color: #12101c;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-20');
if (root) {
  const q = (s) => root.querySelector(s);
  const clock = q('[data-clock]'), live = q('[data-live]'), pad = (n) => String(n).padStart(2, '0');
  const target = new Date(Date.now() + 4 * 86400e3 + 11 * 3600e3 + 28 * 60e3 + 5e3);
  let id = 0, seen = null;
  clock.dateTime = target.toISOString();
  const tick = () => {
    const ms = target - Date.now();
    if (ms <= 0) {
      clock.hidden = true; q('[data-livecopy]').hidden = false;
      q('[data-title]').textContent = 'The archive is open';
      q('[data-sub]').textContent = 'Forty years of print, indexed and searchable. Start anywhere.';
      q('[data-cta]').textContent = 'Start reading';
      live.textContent = 'The archive is now open.';
      return;
    }
    const s = Math.floor(ms / 1000);
    q('[data-d]').textContent = pad(Math.floor(s / 86400));
    q('[data-h]').textContent = pad(Math.floor(s / 3600) % 24);
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    const b = ms < 60e3 ? 'm1' : ms < 3600e3 ? 'h1' : ms < 86400e3 ? 'd1' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', d1: 'The archive opens within a day.', h1: 'The archive opens within the hour.', m1: 'The archive opens in one minute.' }[b]; }
    id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
