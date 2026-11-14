---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/appointment-reminder-countdown-card/"
title: "Appointment Reminder Countdown Card"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "An upcoming-visit card that changes precision as the appointment approaches: days and hours while it is far off, hours and minutes inside the last day, and…"
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Appointment Reminder Countdown Card
Source: https://codefronts.com/snippets/css-countdown-timers/appointment-reminder-countdown-card/

An upcoming-visit card that changes precision as the appointment approaches: days and hours while it is far off, hours and minutes inside the last day, and the Reschedule and Cancel actions surfaced only once that switch happens. Two states are shown side by side so the transition is visible rather than described.
## HTML
```html
<section class="cdt-11" aria-labelledby="cdt-11-title">
  <input class="cdt-11__tgl" type="checkbox" id="cdt-11-theme">
  <label class="cdt-11__tglbtn" for="cdt-11-theme">
    <svg class="cdt-11__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-11__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-11__darktext">Dark mode</span><span class="cdt-11__lighttext">Light mode</span>
  </label>
  <div class="cdt-11__stage">
    <div class="cdt-11__head">
      <p class="cdt-11__brand">Vale Family Practice</p>
      <h2 class="cdt-11__title" id="cdt-11-title">Upcoming appointments</h2>
      <p class="cdt-11__sub">The card changes precision inside the last day, and surfaces the two actions that matter then.</p>
    </div>

    <article class="cdt-11__card">
      <header class="cdt-11__top">
        <span class="cdt-11__state">Scheduled</span>
        <span class="cdt-11__when"><time datetime="2026-08-24T09:20">Mon 24 Aug, 9:20 am</time></span>
      </header>
      <h3 class="cdt-11__what">Annual review with Dr Priya Sharma</h3>
      <p class="cdt-11__meta">Room 2, Ground floor · 14 Basalt Road · bring your current prescriptions</p>
      <p class="cdt-11__remain" role="timer">In <time datetime="P2DT4H">2 days 4 hours</time></p>
      <p class="cdt-11__hint">More than a day out: days and hours only. No actions surfaced.</p>
    </article>

    <article class="cdt-11__card" data-state="soon">
      <header class="cdt-11__top">
        <span class="cdt-11__state"><i aria-hidden="true"></i>Tomorrow</span>
        <span class="cdt-11__when"><time datetime="2026-08-22T14:00">Sat 22 Aug, 2:00 pm</time></span>
      </header>
      <h3 class="cdt-11__what">Blood work · fasting from midnight</h3>
      <p class="cdt-11__meta">Pathology desk, Level 1 · Jordan Lee, phlebotomist</p>
      <p class="cdt-11__remain cdt-11__remain--live" role="timer" aria-label="Time until appointment">
        In <span class="cdt-11__clock" aria-hidden="true"><em class="cdt-11__h"></em><span>:</span><em class="cdt-11__mt"></em><em class="cdt-11__mu"></em><span>:</span><em class="cdt-11__st"></em><em class="cdt-11__su"></em></span>
      </p>
      <p class="cdt-11__hint">Inside twenty-four hours: hour and minute precision, actions available.</p>
      <div class="cdt-11__actions">
        <button class="cdt-11__btn" type="button">Reschedule</button>
        <button class="cdt-11__btn cdt-11__btn--quiet" type="button">Cancel visit</button>
      </div>
      <p class="cdt-11__policy">Cancelling inside four hours is recorded as a late cancellation. Call the desk if you are running behind — the slot is held ten minutes.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@property --cdt11-h {
  syntax: '<integer>';
  inherits: false;
  initial-value: 4;
}

@property --cdt11-mt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 3;
}

@property --cdt11-mu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 2;
}

@property --cdt11-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt11-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

.cdt-11 {
  --page: #f0f4f2;
  --card: #ffffff;
  --sunk: #e7efeb;
  --ink: #1c2b28;
  --muted: #5f7370;
  --rule: #dbe6e2;
  --accent: #0f8f7a;
  --dur: 14400s;
  --font-display: "Optima", "Palatino", "Iowan Old Style", ui-serif, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-11 {
    --page: oklch(96% 0.012 170);
    --card: oklch(100% 0 0);
    --sunk: oklch(94% 0.016 170);
    --ink: oklch(26% 0.024 175);
    --muted: oklch(52% 0.022 175);
    --rule: oklch(91% 0.014 170);
    --accent: oklch(56% 0.11 172);
  }
}

.cdt-11 *,
.cdt-11 *::before,
.cdt-11 *::after {
  box-sizing: border-box;
}

.cdt-11__stage {
  display: grid;
  gap: 16px;
  align-content: center;
  min-height: 100vh;
  max-inline-size: 760px;
  margin-inline: auto;
  padding: clamp(18px, 5vw, 52px);
  padding-block-end: clamp(84px, 12vw, 96px);
}

.cdt-11__head {
  margin-block-end: 6px;
}

.cdt-11__brand {
  margin: 0 0 8px;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.cdt-11__title {
  margin: 0 0 6px;
  font: 400 clamp(24px, 4.4vw, 34px)/1.15 var(--font-display);
  letter-spacing: -0.01em;
}

.cdt-11__sub {
  margin: 0;
  max-inline-size: 52ch;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-11__card {
  min-inline-size: 0;
  padding: clamp(18px, 3.6vw, 26px);
  background: var(--card);
  border-radius: 4px;
  border-inline-start: 3px solid var(--rule);
}

.cdt-11__card[data-state="soon"] {
  border-inline-start-color: var(--accent);
  background: var(--card);
}

.cdt-11__top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 6px 14px;
  margin-block-end: 12px;
}

.cdt-11__state {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font: 600 10.5px/1 system-ui, sans-serif;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-11__card[data-state="soon"] .cdt-11__state {
  color: var(--accent);
}

.cdt-11__state i {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: var(--accent);
  animation: cdt11-pulse 2.4s ease-out infinite;
}

@keyframes cdt11-pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(15, 143, 122, 0.4);
  }

  70%,
    100% {
    box-shadow: 0 0 0 8px rgba(15, 143, 122, 0);
  }
}

.cdt-11__when {
  font: 500 12.5px/1 system-ui, sans-serif;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cdt-11__what {
  margin: 0 0 6px;
  font: 400 clamp(17px, 3vw, 21px)/1.3 var(--font-display);
  text-wrap: pretty;
}

.cdt-11__meta {
  margin: 0 0 16px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-11__remain {
  margin: 0;
  padding: 14px 16px;
  background: var(--sunk);
  border-radius: 4px;
  font: 400 clamp(19px, 3.6vw, 24px)/1.2 var(--font-display);
}

.cdt-11__remain time {
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.cdt-11__remain--live .cdt-11__clock {
  display: inline-flex;
  align-items: baseline;
  font-variant-numeric: tabular-nums;
  font-weight: 600;
  color: var(--accent);
}

.cdt-11__clock em {
  font-style: normal;
}

.cdt-11__clock > span {
  opacity: 0.45;
}

.cdt-11__h::before {
  content: counter(cdt11-h);
  counter-reset: cdt11-h var(--cdt11-h);
}

.cdt-11__mt::before {
  content: counter(cdt11-mt);
  counter-reset: cdt11-mt var(--cdt11-mt);
}

.cdt-11__mu::before {
  content: counter(cdt11-mu);
  counter-reset: cdt11-mu var(--cdt11-mu);
}

.cdt-11__st::before {
  content: counter(cdt11-st);
  counter-reset: cdt11-st var(--cdt11-st);
}

.cdt-11__su::before {
  content: counter(cdt11-su);
  counter-reset: cdt11-su var(--cdt11-su);
}

.cdt-11__h {
  animation: cdt11-h var(--dur) steps(5, end) forwards;
}

.cdt-11__mt {
  animation: cdt11-mt 3600s steps(6, end) infinite;
}

.cdt-11__mu {
  animation: cdt11-mu 600s steps(10, end) infinite;
}

.cdt-11__st {
  animation: cdt11-st 60s steps(6, end) infinite;
}

.cdt-11__su {
  animation: cdt11-su 10s steps(10, end) infinite;
}

@keyframes cdt11-h {
  from {
    --cdt11-h: 4;
  }

  to {
    --cdt11-h: -1;
  }
}

@keyframes cdt11-mt {
  from {
    --cdt11-mt: 5;
  }

  to {
    --cdt11-mt: -1;
  }
}

@keyframes cdt11-mu {
  from {
    --cdt11-mu: 9;
  }

  to {
    --cdt11-mu: 0;
  }
}

@keyframes cdt11-st {
  from {
    --cdt11-st: 5;
  }

  to {
    --cdt11-st: 0;
  }
}

@keyframes cdt11-su {
  from {
    --cdt11-su: 9;
  }

  to {
    --cdt11-su: 0;
  }
}

.cdt-11__hint {
  margin: 10px 0 0;
  font-size: 11.5px;
  line-height: 1.55;
  color: var(--muted);
}

.cdt-11__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  margin-block-start: 16px;
}

.cdt-11__btn {
  flex: 1 1 140px;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 12px 16px;
  border: 1px solid var(--accent);
  border-radius: 4px;
  background: var(--accent);
  color: #fff;
  font: 600 13.5px/1 system-ui, sans-serif;
  cursor: pointer;
}

.cdt-11__btn--quiet {
  background: transparent;
  color: var(--ink);
  border-color: var(--rule);
}

.cdt-11__btn:hover {
  filter: brightness(1.06);
}

.cdt-11__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.cdt-11__policy {
  margin: 12px 0 0;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .cdt-11__state i {
    animation: none;
    box-shadow: 0 0 0 4px rgba(15, 143, 122, 0.22);
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-11 {
  position: relative;
}

.cdt-11__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-11__tglbtn {
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

.cdt-11__tglbtn:hover {
  opacity: 1;
}

.cdt-11__tgl:focus-visible + .cdt-11__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-11__tglbtn svg {
  flex: none;
}

.cdt-11__sun,
.cdt-11__lighttext {
  display: none;
}

.cdt-11:has(.cdt-11__tgl:checked) .cdt-11__moon,
.cdt-11:has(.cdt-11__tgl:checked) .cdt-11__darktext {
  display: none;
}

.cdt-11:has(.cdt-11__tgl:checked) .cdt-11__sun {
  display: block;
}

.cdt-11:has(.cdt-11__tgl:checked) .cdt-11__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-11__tglbtn {
    padding: 12px;
  }

  .cdt-11__darktext,
    .cdt-11__lighttext,
    .cdt-11:has(.cdt-11__tgl:checked) .cdt-11__darktext,
    .cdt-11:has(.cdt-11__tgl:checked) .cdt-11__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-11:has(.cdt-11__tgl:checked) {
    --page: #101715;
    --card: #17201d;
    --sunk: #1e2a26;
    --ink: #e8f1ee;
    --muted: #92a5a0;
    --rule: #26332f;
    --accent: #4fd1b5;
  }

  .cdt-11:has(.cdt-11__tgl:checked) .cdt-11__btn {
    color: #101715;
  }

  .cdt-11:has(.cdt-11__tgl:checked) .cdt-11__btn--quiet {
    color: #e8f1ee;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-11 {
    --page: #101715;
    --card: #17201d;
    --sunk: #1e2a26;
    --ink: #e8f1ee;
    --muted: #92a5a0;
    --rule: #26332f;
    --accent: #4fd1b5;
  }

  .cdt-11__btn {
    color: #101715;
  }

  .cdt-11__btn--quiet {
    color: #e8f1ee;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-11:has(.cdt-11__tgl:checked) {
    --page: oklch(96% 0.012 170);
    --card: oklch(100% 0 0);
    --sunk: oklch(94% 0.016 170);
    --ink: oklch(26% 0.024 175);
    --muted: oklch(52% 0.022 175);
    --rule: oklch(91% 0.014 170);
    --accent: oklch(56% 0.11 172);
  }

  .cdt-11:has(.cdt-11__tgl:checked) .cdt-11__btn {
    color: #fff;
  }

  .cdt-11:has(.cdt-11__tgl:checked) .cdt-11__btn--quiet {
    color: var(--ink);
  }
}

[data-theme="dark"] .cdt-11 {
  --page: #101715;
  --card: #17201d;
  --sunk: #1e2a26;
  --ink: #e8f1ee;
  --muted: #92a5a0;
  --rule: #26332f;
  --accent: #4fd1b5;
}

[data-theme="dark"] .cdt-11 .cdt-11__btn {
  color: #101715;
}

[data-theme="dark"] .cdt-11 .cdt-11__btn--quiet {
  color: #e8f1ee;
}
```
