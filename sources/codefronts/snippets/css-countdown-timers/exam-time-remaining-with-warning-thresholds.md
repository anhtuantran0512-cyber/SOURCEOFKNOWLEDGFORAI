---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/exam-time-remaining-with-warning-thresholds/"
title: "Exam Time Remaining with Warning Thresholds"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A proctored-test time chip that changes state at 50%, 10% and 2% of the window remaining — colour, weight, icon and a single announcement at each boundary."
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Exam Time Remaining with Warning Thresholds
Source: https://codefronts.com/snippets/css-countdown-timers/exam-time-remaining-with-warning-thresholds/

A proctored-test time chip that changes state at 50%, 10% and 2% of the window remaining — colour, weight, icon and a single announcement at each boundary. It also ships the affordance most exam timers omit: a documented way to add time, because a timed assessment without an extension path locks out the students who need one.
## HTML
```html
<section class="cdt-12" aria-labelledby="cdt-12-title">
  <input class="cdt-12__tgl" type="checkbox" id="cdt-12-theme">
  <label class="cdt-12__tglbtn" for="cdt-12-theme">
    <svg class="cdt-12__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-12__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-12__darktext">Dark mode</span><span class="cdt-12__lighttext">Light mode</span>
  </label>
  <div class="cdt-12__stage">
    <div class="cdt-12__paper">
      <p class="cdt-12__crumb">Basalt Certification · Section 3 of 4</p>
      <h2 class="cdt-12__title" id="cdt-12-title">Query planning and index selection</h2>
      <ol class="cdt-12__qs">
        <li><p>Which access path does the planner choose when the predicate is non-sargable?</p><div class="cdt-12__opts"><span></span><span></span><span></span></div></li>
        <li><p>Given a composite index on (tenant_id, created_at), which query cannot use it?</p><div class="cdt-12__opts"><span></span><span></span><span></span></div></li>
      </ol>
    </div>

    <div class="cdt-12__chip" role="timer" data-band="ok">
      <div class="cdt-12__chiptop">
        <span class="cdt-12__ico" aria-hidden="true">
          <svg viewBox="0 0 18 18" width="15" height="15"><circle cx="9" cy="9" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M9 5.4V9l2.6 1.6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
        </span>
        <time class="cdt-12__clock" datetime="" data-clock>44:59</time>
        <span class="cdt-12__band" data-caption>On track</span>
      </div>
      <div class="cdt-12__bar" aria-hidden="true"><span data-fill></span></div>
      <button class="cdt-12__add" type="button" data-add>+ 10 min approved time</button>
      <p class="cdt-12__policy">Accommodations are granted by the exam office before the session. This control models that flow.</p>
      <output class="cdt-12__sr" aria-live="polite" data-live></output>
    </div>
  </div>
</section>
```
## CSS
```css
.cdt-12 {
  --page: #ffffff;
  --paper: #ffffff;
  --ink: #0b0b0c;
  --muted: #6a6a70;
  --rule: #dededf;
  --accent: #3b2ee0;
  --warn: #b06a00;
  --crit: #c22b1d;
  --font-display: "Archivo Narrow", "Roboto Condensed", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-12 {
    --page: oklch(100% 0 0);
    --ink: oklch(12% 0.004 280);
    --muted: oklch(50% 0.008 280);
    --rule: oklch(89% 0.003 280);
    --accent: oklch(45% 0.24 275);
    --warn: oklch(58% 0.14 70);
    --crit: oklch(52% 0.2 27);
  }
}

.cdt-12 *,
.cdt-12 *::before,
.cdt-12 *::after {
  box-sizing: border-box;
}

.cdt-12__stage {
  display: grid;
  gap: 20px;
  align-content: start;
  min-height: 100vh;
  max-inline-size: 940px;
  margin-inline: auto;
  padding: clamp(16px, 4vw, 44px);
  grid-template-columns: minmax(0, 1fr);
}

@media (min-width: 860px) {
  .cdt-12__stage {
    grid-template-columns: minmax(0, 1fr) 268px;
    align-content: center;
  }
}

.cdt-12__paper {
  min-inline-size: 0;
  padding-block: 6px;
}

.cdt-12__crumb {
  margin: 0 0 10px;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-12__title {
  margin: 0 0 24px;
  padding-block-end: 14px;
  border-block-end: 1px solid var(--rule);
  font: 600 clamp(21px, 3.8vw, 30px)/1.2 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.cdt-12__qs {
  display: grid;
  gap: 22px;
  margin: 0;
  padding-inline-start: 22px;
}

.cdt-12__qs p {
  margin: 0 0 12px;
  font-size: 14.5px;
  line-height: 1.55;
  text-wrap: pretty;
}

.cdt-12__opts {
  display: grid;
  gap: 8px;
}

.cdt-12__opts span {
  display: block;
  block-size: 34px;
  border: 1px solid var(--rule);
  border-radius: 3px;
}

.cdt-12__chip {
  align-self: start;
  padding: 14px;
  border: 1px solid var(--rule);
  border-radius: 3px;
  background: var(--page);
}

@media (min-width: 860px) {
  .cdt-12__chip {
    position: sticky;
    inset-block-start: 20px;
  }
}

.cdt-12__chiptop {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px 8px;
}

.cdt-12__ico {
  display: flex;
  color: var(--accent);
}

.cdt-12__clock {
  font: 600 clamp(24px, 5vw, 30px)/1 var(--font-display);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
  min-inline-size: 5.2ch;
}

.cdt-12__band {
  flex: 1 1 100%;
  font: 600 10.5px/1.3 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-12__bar {
  margin-block: 12px 0;
  block-size: 3px;
  background: var(--rule);
}

.cdt-12__bar span {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  background: var(--accent);
  transition: inline-size 0.9s linear;
}

.cdt-12__chip[data-band="warn"] {
  border-color: var(--warn);
  background: rgba(176, 106, 0, 0.06);
}

.cdt-12__chip[data-band="warn"] .cdt-12__ico,
.cdt-12__chip[data-band="warn"] .cdt-12__band {
  color: var(--warn);
}

.cdt-12__chip[data-band="warn"] .cdt-12__bar span {
  background: var(--warn);
}

.cdt-12__chip[data-band="crit"] {
  border-color: var(--crit);
  background: rgba(194, 43, 29, 0.07);
}

.cdt-12__chip[data-band="crit"] .cdt-12__ico,
.cdt-12__chip[data-band="crit"] .cdt-12__band,
.cdt-12__chip[data-band="crit"] .cdt-12__clock {
  color: var(--crit);
}

.cdt-12__chip[data-band="crit"] .cdt-12__clock {
  font-weight: 700;
}

.cdt-12__chip[data-band="crit"] .cdt-12__bar span {
  background: var(--crit);
}

.cdt-12__chip[data-band="end"] {
  border-color: var(--crit);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-12__chip[data-band="warn"] {
    background: color-mix(in oklab, var(--warn) 8%, var(--page));
  }

  .cdt-12__chip[data-band="crit"] {
    background: color-mix(in oklab, var(--crit) 10%, var(--page));
  }
}

.cdt-12__add {
  inline-size: 100%;
  min-block-size: 44px;
  margin-block-start: 12px;
  padding: 11px 12px;
  border: 1px solid var(--rule);
  border-radius: 3px;
  background: transparent;
  color: var(--ink);
  font: 600 12.5px/1 var(--font-display);
  cursor: pointer;
}

.cdt-12__add:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.cdt-12__add:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-12__policy {
  margin: 10px 0 0;
  font-size: 11px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-12__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (prefers-reduced-motion: reduce) {
  .cdt-12__bar span {
    transition: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-12 {
  position: relative;
}

.cdt-12__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-12__tglbtn {
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

.cdt-12__tglbtn:hover {
  opacity: 1;
}

.cdt-12__tgl:focus-visible + .cdt-12__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-12__tglbtn svg {
  flex: none;
}

.cdt-12__sun,
.cdt-12__lighttext {
  display: none;
}

.cdt-12:has(.cdt-12__tgl:checked) .cdt-12__moon,
.cdt-12:has(.cdt-12__tgl:checked) .cdt-12__darktext {
  display: none;
}

.cdt-12:has(.cdt-12__tgl:checked) .cdt-12__sun {
  display: block;
}

.cdt-12:has(.cdt-12__tgl:checked) .cdt-12__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-12__tglbtn {
    padding: 12px;
  }

  .cdt-12__darktext,
    .cdt-12__lighttext,
    .cdt-12:has(.cdt-12__tgl:checked) .cdt-12__darktext,
    .cdt-12:has(.cdt-12__tgl:checked) .cdt-12__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-12:has(.cdt-12__tgl:checked) {
    --page: #0b0b0d;
    --ink: #f3f3f5;
    --muted: #90909a;
    --rule: #24242a;
    --accent: #9b90ff;
    --warn: #f0b04a;
    --crit: #ff6a5a;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-12 {
    --page: #0b0b0d;
    --ink: #f3f3f5;
    --muted: #90909a;
    --rule: #24242a;
    --accent: #9b90ff;
    --warn: #f0b04a;
    --crit: #ff6a5a;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-12:has(.cdt-12__tgl:checked) {
    --page: oklch(100% 0 0);
    --ink: oklch(12% 0.004 280);
    --muted: oklch(50% 0.008 280);
    --rule: oklch(89% 0.003 280);
    --accent: oklch(45% 0.24 275);
    --warn: oklch(58% 0.14 70);
    --crit: oklch(52% 0.2 27);
  }
}

[data-theme="dark"] .cdt-12 {
  --page: #0b0b0d;
  --ink: #f3f3f5;
  --muted: #90909a;
  --rule: #24242a;
  --accent: #9b90ff;
  --warn: #f0b04a;
  --crit: #ff6a5a;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-12');
if (root) {
  const q = (s) => root.querySelector(s);
  const chip = q('.cdt-12__chip'), clock = q('[data-clock]'), fill = q('[data-fill]');
  const cap = q('[data-caption]'), live = q('[data-live]');
  let total = 45 * 60e3, target = Date.now() + total, id = 0, seen = null;
  const CAPTIONS = { ok: 'On track', half: 'Half the time used', warn: 'Ten percent left', crit: 'Final moments', end: 'Time expired' };
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), f = ms / total, s = Math.ceil(ms / 1000);
    clock.textContent = String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
    clock.dateTime = new Date(target).toISOString();
    fill.style.inlineSize = (f * 100).toFixed(2) + '%';
    const b = ms <= 0 ? 'end' : f <= 0.02 ? 'crit' : f <= 0.1 ? 'warn' : f <= 0.5 ? 'half' : 'ok';
    if (b !== seen) {
      seen = b; chip.dataset.band = b === 'half' ? 'ok' : b; cap.textContent = CAPTIONS[b];
      if (b !== 'ok') live.textContent = { half: 'Half of your exam time has been used.', warn: 'Ten percent of your exam time remains.', crit: 'Two percent of your time remains. Finish and submit.', end: 'Time expired. Your answers were submitted.' }[b];
    }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); } else { clock.textContent = '00:00'; }
  };
  q('[data-add]').addEventListener('click', () => {
    total += 10 * 60e3; target += 10 * 60e3; seen = null;
    live.textContent = 'Ten minutes of approved time added. New remaining time announced.';
    clearTimeout(id); tick();
  });
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
