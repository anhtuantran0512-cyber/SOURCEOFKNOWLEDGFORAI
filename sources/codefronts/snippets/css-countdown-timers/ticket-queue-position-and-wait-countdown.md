---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/ticket-queue-position-and-wait-countdown/"
title: "Ticket Queue Position and Wait Countdown"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A virtual waiting room: your place in line as the largest thing on the screen, an estimated wait counting down beneath it, and a reassurance line telling you…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ticket Queue Position and Wait Countdown
Source: https://codefronts.com/snippets/css-countdown-timers/ticket-queue-position-and-wait-countdown/

A virtual waiting room: your place in line as the largest thing on the screen, an estimated wait counting down beneath it, and a reassurance line telling you not to refresh — because refreshing is the one action that costs a user their place, and it is exactly what an unexplained blank wait invites.
## HTML
```html
<section class="cdt-15" aria-labelledby="cdt-15-title">
  <input class="cdt-15__tgl" type="checkbox" id="cdt-15-theme">
  <label class="cdt-15__tglbtn" for="cdt-15-theme">
    <svg class="cdt-15__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-15__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-15__darktext">Dark mode</span><span class="cdt-15__lighttext">Light mode</span>
  </label>
  <div class="cdt-15__stage">
    <p class="cdt-15__brand">Orbit Live · Sable Arena, 14 November</p>
    <h2 class="cdt-15__title" id="cdt-15-title">You are in the queue</h2>

    <div class="cdt-15__queue" role="timer">
      <p class="cdt-15__poslabel">Position in line</p>
      <p class="cdt-15__pos" data-pos>#1,247</p>
      <p class="cdt-15__wait">Estimated wait <time datetime="" data-clock>7–9 minutes</time></p>
      <div class="cdt-15__track" aria-hidden="true"><span data-fill></span></div>
    </div>

    <div class="cdt-15__reassure">
      <svg viewBox="0 0 18 18" width="16" height="16" aria-hidden="true"><path d="M9 1.8 2 4.6v4.2c0 3.4 2.9 6.3 7 7.4 4.1-1.1 7-4 7-7.4V4.6L9 1.8Z" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M6.2 8.9 8.4 11l3.6-3.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      <p><strong>Do not refresh or close this tab.</strong> Your place is held here. Refreshing sends you to the back of the line, and there is no way for us to restore it.</p>
    </div>

    <div class="cdt-15__ready" data-ready hidden role="status">
      <p class="cdt-15__readytitle">It is your turn</p>
      <p class="cdt-15__readytext">You have <strong>10 minutes</strong> to choose seats and check out. The hold releases automatically after that.</p>
      <button class="cdt-15__btn" type="button">Enter seat selection</button>
    </div>

    <p class="cdt-15__foot">A shared queue is a real-time event: one person's window cannot be extended without reordering everyone else. If this tab sits idle for 30 minutes the place is released.</p>
    <output class="cdt-15__sr" aria-live="polite" data-live></output>
  </div>
</section>
```
## CSS
```css
.cdt-15 {
  --page-a: #ff8a4c;
  --page-b: #ffd4a3;
  --ink: #33170a;
  --muted: #7d4a2d;
  --edge: rgba(51, 23, 10, 0.14);
  --accent: #e0451f;
  --digit: 132px;
  --font-display: "Archivo", "Geist", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: linear-gradient(165deg, var(--page-a), var(--page-b) 62%, #fff3e4);
  color: var(--ink);
  font-family: var(--font-display);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-15 {
    --page-a: oklch(76% 0.16 48);
    --page-b: oklch(89% 0.08 62);
    --ink: oklch(28% 0.07 44);
    --muted: oklch(48% 0.08 46);
    --accent: oklch(56% 0.19 32);
  }
}

.cdt-15 *,
.cdt-15 *::before,
.cdt-15 *::after {
  box-sizing: border-box;
}

.cdt-15__stage {
  display: grid;
  gap: 16px;
  align-content: center;
  justify-items: center;
  min-height: 100vh;
  max-inline-size: 620px;
  margin-inline: auto;
  padding: clamp(18px, 5vw, 56px);
  text-align: center;
}

.cdt-15__brand {
  margin: 0;
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-15__title {
  margin: 0;
  font: 600 clamp(21px, 4vw, 30px)/1.15 var(--font-display);
  letter-spacing: -0.02em;
}

.cdt-15__queue {
  inline-size: 100%;
}

.cdt-15__poslabel {
  margin: 0;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-15__pos {
  margin: 4px 0 0;
  font: 700 clamp(58px, 21vw, var(--digit))/0.9 var(--font-display);
  letter-spacing: -0.05em;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
}

.cdt-15__wait {
  margin: 6px 0 0;
  font: 500 clamp(15px, 3vw, 18px)/1.3 var(--font-display);
}

.cdt-15__wait time {
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cdt-15__track {
  margin-block-start: 18px;
  block-size: 8px;
  border-radius: 99px;
  background: rgba(51, 23, 10, 0.13);
  overflow: hidden;
}

.cdt-15__track span {
  display: block;
  block-size: 100%;
  inline-size: 4%;
  border-radius: 99px;
  background: var(--accent);
  transition: inline-size 1s linear;
}

.cdt-15__reassure {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  inline-size: 100%;
  padding: 14px 16px;
  border: 1px solid var(--edge);
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.5);
  text-align: start;
}

.cdt-15__reassure svg {
  flex: none;
  margin-block-start: 2px;
  color: var(--accent);
}

.cdt-15__reassure p {
  margin: 0;
  min-inline-size: 0;
  font-size: 13px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-15__reassure strong {
  color: var(--ink);
}

.cdt-15__ready {
  inline-size: 100%;
  padding: 18px;
  border: 1px solid var(--edge);
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.72);
}

.cdt-15__ready[hidden] {
  display: none;
}

.cdt-15__readytitle {
  margin: 0 0 6px;
  font: 700 clamp(19px, 4vw, 25px)/1.15 var(--font-display);
  letter-spacing: -0.02em;
}

.cdt-15__readytext {
  margin: 0 0 14px;
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--muted);
}

.cdt-15__btn {
  min-block-size: 48px;
  min-inline-size: 44px;
  padding: 13px 22px;
  border: 0;
  border-radius: 12px;
  background: var(--accent);
  color: #fff;
  font: 700 14.5px/1 var(--font-display);
  cursor: pointer;
}

.cdt-15__btn:hover {
  filter: brightness(1.06);
}

.cdt-15__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.cdt-15__foot {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (prefers-reduced-motion: reduce) {
  .cdt-15__track span {
    transition: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-15 {
  position: relative;
}

.cdt-15__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-15__tglbtn {
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

.cdt-15__tglbtn:hover {
  opacity: 1;
}

.cdt-15__tgl:focus-visible + .cdt-15__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-15__tglbtn svg {
  flex: none;
}

.cdt-15__sun,
.cdt-15__lighttext {
  display: none;
}

.cdt-15:has(.cdt-15__tgl:checked) .cdt-15__moon,
.cdt-15:has(.cdt-15__tgl:checked) .cdt-15__darktext {
  display: none;
}

.cdt-15:has(.cdt-15__tgl:checked) .cdt-15__sun {
  display: block;
}

.cdt-15:has(.cdt-15__tgl:checked) .cdt-15__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-15__tglbtn {
    padding: 12px;
  }

  .cdt-15__darktext,
    .cdt-15__lighttext,
    .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__darktext,
    .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-15:has(.cdt-15__tgl:checked) {
    --page-a: #2a1206;
    --page-b: #4a2110;
    --ink: #ffeadb;
    --muted: #d0a488;
    --edge: rgba(255, 234, 219, 0.16);
    --accent: #ff8557;
    background: linear-gradient(165deg, #2a1206, #4a2110 62%, #120804);
  }

  .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__reassure,
    .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__ready {
    background: rgba(255, 255, 255, 0.07);
  }

  .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__track {
    background: rgba(255, 234, 219, 0.16);
  }

  .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__btn {
    color: #2a1206;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-15 {
    --page-a: #2a1206;
    --page-b: #4a2110;
    --ink: #ffeadb;
    --muted: #d0a488;
    --edge: rgba(255, 234, 219, 0.16);
    --accent: #ff8557;
    background: linear-gradient(165deg, #2a1206, #4a2110 62%, #120804);
  }

  .cdt-15__reassure,
    .cdt-15__ready {
    background: rgba(255, 255, 255, 0.07);
  }

  .cdt-15__track {
    background: rgba(255, 234, 219, 0.16);
  }

  .cdt-15__btn {
    color: #2a1206;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-15:has(.cdt-15__tgl:checked) {
    --page-a: oklch(76% 0.16 48);
    --page-b: oklch(89% 0.08 62);
    --ink: oklch(28% 0.07 44);
    --muted: oklch(48% 0.08 46);
    --edge: rgba(51, 23, 10, 0.14);
    --accent: oklch(56% 0.19 32);
    background: linear-gradient(165deg, var(--page-a), var(--page-b) 62%, #fff3e4);
  }

  .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__reassure,
    .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__ready {
    background: rgba(255, 255, 255, 0.5);
  }

  .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__track {
    background: rgba(51, 23, 10, 0.13);
  }

  .cdt-15:has(.cdt-15__tgl:checked) .cdt-15__btn {
    color: #fff;
  }
}

[data-theme="dark"] .cdt-15 {
  --page-a: #2a1206;
  --page-b: #4a2110;
  --ink: #ffeadb;
  --muted: #d0a488;
  --edge: rgba(255, 234, 219, 0.16);
  --accent: #ff8557;
  background: linear-gradient(165deg, #2a1206, #4a2110 62%, #120804);
}

[data-theme="dark"] .cdt-15 .cdt-15__reassure,
[data-theme="dark"] .cdt-15 .cdt-15__ready {
  background: rgba(255, 255, 255, 0.07);
}

[data-theme="dark"] .cdt-15 .cdt-15__btn {
  color: #2a1206;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-15');
if (root) {
  const q = (s) => root.querySelector(s);
  const pos = q('[data-pos]'), clock = q('[data-clock]'), fill = q('[data-fill]');
  const ready = q('[data-ready]'), live = q('[data-live]'), queue = q('.cdt-15__queue');
  const START = 1247, RATE = 9;
  const t0 = Date.now(), target = Date.now() + Math.ceil(START / RATE) * 1000;
  let id = 0, seen = Math.ceil(START / 1000);
  const tick = () => {
    const left = Math.max(0, START - Math.floor((Date.now() - t0) / 1000) * RATE);
    const secs = Math.ceil(left / RATE), lo = Math.max(0, Math.floor(secs / 60)), hi = lo + Math.max(1, Math.round(lo * 0.25));
    pos.textContent = '#' + left.toLocaleString();
    clock.dateTime = new Date(target).toISOString();
    clock.textContent = left === 0 ? 'less than a minute' : lo < 1 ? 'under a minute' : lo + '–' + hi + ' minutes';
    fill.style.inlineSize = ((1 - left / START) * 96 + 4).toFixed(1) + '%';
    const band = Math.ceil(left / 1000);
    if (band !== seen) { seen = band; live.textContent = 'Queue position now about ' + left.toLocaleString() + '.'; }
    if (left > 0) return void (id = setTimeout(tick, 1000 - (Date.now() % 1000)));
    queue.hidden = true; ready.hidden = false;
    live.textContent = 'It is your turn. You have ten minutes to choose seats and check out.';
  };
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
