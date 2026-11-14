---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/circular-depleting-ring-countdown-timer/"
title: "Circular Depleting Ring Countdown Timer"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "An SVG ring that empties as time runs out, not one that fills as a task completes."
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Depleting Ring Countdown Timer
Source: https://codefronts.com/snippets/css-countdown-timers/circular-depleting-ring-countdown-timer/

An SVG ring that empties as time runs out, not one that fills as a task completes. pathLength="100" turns the circumference into a percentage so stroke-dashoffset animates 0 to 100 with no circumference maths, and color-mix shifts the stroke through amber and red as the 50% and 20% marks pass.
## HTML
```html
<section class="cdt-04" aria-labelledby="cdt-04-title">
  <input class="cdt-04__tgl" type="checkbox" id="cdt-04-theme">
  <label class="cdt-04__tglbtn" for="cdt-04-theme">
    <svg class="cdt-04__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-04__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-04__darktext">Dark mode</span><span class="cdt-04__lighttext">Light mode</span>
  </label>
  <div class="cdt-04__stage">
    <div class="cdt-04__head">
      <h2 class="cdt-04__title" id="cdt-04-title">Hold time remaining</h2>
      <p class="cdt-04__sub">Orbit support · Priya Sharma is next · window <time datetime="PT5M">5 minutes</time></p>
    </div>

    <div class="cdt-04__dial" role="timer" aria-label="Five minute hold timer, time remaining">
      <svg class="cdt-04__ring" viewBox="0 0 120 120" aria-hidden="true">
        <circle class="cdt-04__trackring" cx="60" cy="60" r="52" pathLength="100"/>
        <circle class="cdt-04__arc" cx="60" cy="60" r="52" pathLength="100"/>
      </svg>
      <div class="cdt-04__center">
        <p class="cdt-04__clock" aria-hidden="true">
          <em class="cdt-04__m"></em><span>:</span><em class="cdt-04__st"></em><em class="cdt-04__su"></em>
        </p>
        <p class="cdt-04__word">remaining</p>
      </div>
      <div class="cdt-04__done" role="status"><strong>Connecting</strong><span>Agent picking up</span></div>
    </div>

    <ul class="cdt-04__bands">
      <li class="cdt-04__band cdt-04__band--calm"><span aria-hidden="true"></span>Plenty of time · above 50%</li>
      <li class="cdt-04__band cdt-04__band--warn"><span aria-hidden="true"></span>Wrap up · under 50%</li>
      <li class="cdt-04__band cdt-04__band--danger"><span aria-hidden="true"></span>Final seconds · under 20%</li>
    </ul>
    <p class="cdt-04__note">Time-depleting, not task-progress: the arc shrinks because the window is closing, and the caption changes with it so the state never depends on colour alone. Pure CSS, so it measures five minutes from render.</p>
  </div>
</section>
```
## CSS
```css
@property --cdt04-m {
  syntax: '<integer>';
  inherits: false;
  initial-value: 4;
}

@property --cdt04-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt04-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

.cdt-04 {
  --page: #070c1a;
  --panel: #0d1428;
  --ink: #eaf0ff;
  --muted: #8494bd;
  --rule: #1c2745;
  --calm: #38d9c8;
  --warn: #f2b23c;
  --danger: #ff5a63;
  --ring-w: 9px;
  --dur: 300s;
  --font-display: "Oswald", "Archivo Narrow", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-04 {
    --page: oklch(16% 0.04 265);
    --panel: oklch(21% 0.05 264);
    --ink: oklch(95% 0.02 265);
    --muted: oklch(68% 0.05 268);
    --rule: oklch(30% 0.05 265);
    --calm: oklch(80% 0.13 185);
    --warn: oklch(80% 0.15 78);
    --danger: oklch(68% 0.2 20);
  }
}

.cdt-04 *,
.cdt-04 *::before,
.cdt-04 *::after {
  box-sizing: border-box;
}

.cdt-04__stage {
  display: grid;
  gap: 26px;
  align-content: center;
  justify-items: center;
  min-height: 100vh;
  max-inline-size: 640px;
  margin-inline: auto;
  padding: clamp(18px, 5vw, 48px);
  text-align: center;
}

.cdt-04__head {
  min-inline-size: 0;
}

.cdt-04__title {
  margin: 0 0 6px;
  font: 500 clamp(20px, 4vw, 30px)/1.15 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.cdt-04__sub {
  margin: 0;
  font-size: 13px;
  color: var(--muted);
}

.cdt-04__dial {
  position: relative;
  inline-size: clamp(216px, 58vw, 320px);
  aspect-ratio: 1;
}

.cdt-04__ring {
  inline-size: 100%;
  block-size: 100%;
  transform: rotate(-90deg);
  filter: drop-shadow(0 0 14px rgba(56, 217, 200, 0.28));
}

.cdt-04__trackring {
  fill: none;
  stroke: var(--rule);
  stroke-width: var(--ring-w);
}

.cdt-04__arc {
  fill: none;
  stroke: rgba(56, 217, 200, 0.95);
  stroke-width: var(--ring-w);
  stroke-linecap: round;
  stroke-dasharray: 100;
  stroke-dashoffset: 0;
  animation: cdt04-arc var(--dur) linear forwards, cdt04-hue var(--dur) steps(1, end) forwards;
}

@supports (color: color-mix(in oklab, red, blue)) {
  .cdt-04__arc {
    stroke: color-mix(in oklab, var(--calm) 92%, white);
  }
}

@keyframes cdt04-arc {
  from {
    stroke-dashoffset: 0;
  }

  to {
    stroke-dashoffset: 100;
  }
}

@keyframes cdt04-hue {
  0% {
    stroke: var(--calm);
    stroke-width: var(--ring-w);
  }

  50% {
    stroke: var(--warn);
    stroke-width: var(--ring-w);
  }

  80% {
    stroke: var(--danger);
    stroke-width: calc(var(--ring-w) + 2px);
  }
}

.cdt-04__center {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 4px;
  place-content: center;
}

.cdt-04__clock {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: baseline;
  gap: 1px;
  font-variant-numeric: tabular-nums;
  font: 500 clamp(44px, 13vw, 68px)/1 var(--font-display);
  letter-spacing: -0.01em;
}

.cdt-04__clock span {
  opacity: 0.45;
}

.cdt-04__clock em {
  font-style: normal;
}

.cdt-04__m::before {
  content: counter(cdt04-m);
  counter-reset: cdt04-m var(--cdt04-m);
}

.cdt-04__st::before {
  content: counter(cdt04-st);
  counter-reset: cdt04-st var(--cdt04-st);
}

.cdt-04__su::before {
  content: counter(cdt04-su);
  counter-reset: cdt04-su var(--cdt04-su);
}

.cdt-04__m {
  animation: cdt04-m var(--dur) steps(5, end) forwards;
}

.cdt-04__st {
  animation: cdt04-st 60s steps(6, end) infinite;
}

.cdt-04__su {
  animation: cdt04-su 10s steps(10, end) infinite;
}

@keyframes cdt04-m {
  from {
    --cdt04-m: 4;
  }

  to {
    --cdt04-m: -1;
  }
}

@keyframes cdt04-st {
  from {
    --cdt04-st: 5;
  }

  to {
    --cdt04-st: 0;
  }
}

@keyframes cdt04-su {
  from {
    --cdt04-su: 9;
  }

  to {
    --cdt04-su: 0;
  }
}

.cdt-04__word {
  margin: 0;
  font-size: 10.5px;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-04__done {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 4px;
  place-content: center;
  border-radius: 50%;
  background: var(--panel);
  opacity: 0;
  visibility: hidden;
  animation: cdt04-done 0.01s linear var(--dur) forwards;
}

.cdt-04__done strong {
  font: 500 clamp(22px, 6vw, 30px)/1 var(--font-display);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--calm);
}

.cdt-04__done span {
  font-size: 12px;
  color: var(--muted);
}

@keyframes cdt04-done {
  from {
    opacity: 0;
    visibility: hidden;
  }

  to {
    opacity: 1;
    visibility: visible;
  }
}

.cdt-04__bands {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px 16px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.cdt-04__band {
  display: flex;
  align-items: center;
  gap: 7px;
  min-inline-size: 0;
  font-size: 12px;
  color: var(--muted);
}

.cdt-04__band span {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
}

.cdt-04__band--calm span {
  background: var(--calm);
}

.cdt-04__band--warn span {
  background: var(--warn);
}

.cdt-04__band--danger span {
  background: var(--danger);
}

.cdt-04__note {
  margin: 0;
  max-inline-size: 52ch;
  font-size: 12.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .cdt-04__ring {
    filter: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-04 {
  position: relative;
}

.cdt-04__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-04__tglbtn {
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

.cdt-04__tglbtn:hover {
  opacity: 1;
}

.cdt-04__tgl:focus-visible + .cdt-04__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-04__tglbtn svg {
  flex: none;
}

.cdt-04__moon,
.cdt-04__darktext {
  display: none;
}

.cdt-04:has(.cdt-04__tgl:checked) .cdt-04__sun,
.cdt-04:has(.cdt-04__tgl:checked) .cdt-04__lighttext {
  display: none;
}

.cdt-04:has(.cdt-04__tgl:checked) .cdt-04__moon {
  display: block;
}

.cdt-04:has(.cdt-04__tgl:checked) .cdt-04__darktext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-04__tglbtn {
    padding: 12px;
  }

  .cdt-04__darktext,
    .cdt-04__lighttext,
    .cdt-04:has(.cdt-04__tgl:checked) .cdt-04__darktext,
    .cdt-04:has(.cdt-04__tgl:checked) .cdt-04__lighttext {
    display: none;
  }
}
/* toggle in the system-dark case */

@media (prefers-color-scheme: dark) {
  .cdt-04:has(.cdt-04__tgl:checked) {
    --page: #f2f5fb;
    --panel: #ffffff;
    --ink: #101a2f;
    --muted: #5a6a8c;
    --rule: #dde3f0;
    --calm: #0f9c8c;
    --warn: #b8760a;
    --danger: #cf2f38;
  }

  .cdt-04:has(.cdt-04__tgl:checked) .cdt-04__ring {
    filter: none;
  }
}

@media (prefers-color-scheme: light) {
  .cdt-04 {
    --page: #f2f5fb;
    --panel: #ffffff;
    --ink: #101a2f;
    --muted: #5a6a8c;
    --rule: #dde3f0;
    --calm: #0f9c8c;
    --warn: #b8760a;
    --danger: #cf2f38;
  }

  .cdt-04__ring {
    filter: none;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-04:has(.cdt-04__tgl:checked) {
    --page: oklch(16% 0.04 265);
    --panel: oklch(21% 0.05 264);
    --ink: oklch(95% 0.02 265);
    --muted: oklch(68% 0.05 268);
    --rule: oklch(30% 0.05 265);
    --calm: oklch(80% 0.13 185);
    --warn: oklch(80% 0.15 78);
    --danger: oklch(68% 0.2 20);
  }

  .cdt-04:has(.cdt-04__tgl:checked) .cdt-04__ring {
    filter: drop-shadow(0 0 14px rgba(56, 217, 200, 0.28));
  }
}

[data-theme="dark"] .cdt-04 {
  --page: #070c1a;
  --panel: #0d1428;
  --ink: #eaf0ff;
  --muted: #8494bd;
  --rule: #1c2745;
  --calm: #38d9c8;
  --warn: #f2b23c;
  --danger: #ff5a63;
}
```
