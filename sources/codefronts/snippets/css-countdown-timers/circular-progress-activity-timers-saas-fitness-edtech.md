---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/circular-progress-activity-timers-saas-fitness-edtech/"
title: "Circular Activity Timer for SaaS and Fitness"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "An interval session timer with a depleting ring, Work and Rest phase labels, and a play-pause control that runs entirely on CSS: a checkbox flips…"
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Activity Timer for SaaS and Fitness
Source: https://codefronts.com/snippets/css-countdown-timers/circular-progress-activity-timers-saas-fitness-edtech/

An interval session timer with a depleting ring, Work and Rest phase labels, and a play-pause control that runs entirely on CSS: a checkbox flips animation-play-state, so the ring, the digits and the phase label all freeze and resume together with no script holding state.
## HTML
```html
<section class="cdt-21" aria-labelledby="cdt-21-title">
  <input class="cdt-21__tgl" type="checkbox" id="cdt-21-theme">
  <label class="cdt-21__tglbtn" for="cdt-21-theme">
    <svg class="cdt-21__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-21__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-21__darktext">Dark mode</span><span class="cdt-21__lighttext">Light mode</span>
  </label>
  <div class="cdt-21__stage">
    <div class="cdt-21__head">
      <p class="cdt-21__brand">Talon Train</p>
      <h2 class="cdt-21__title" id="cdt-21-title">Interval 3 of 8 · lower body</h2>
    </div>

    <div class="cdt-21__dial">
      <input class="cdt-21__pause" type="checkbox" id="cdt-21-pause">
      <div class="cdt-21__ringwrap" role="timer" aria-label="Interval timer, work then rest">
        <span class="cdt-21__halo" aria-hidden="true"></span>
        <svg class="cdt-21__ring" viewBox="0 0 120 120" aria-hidden="true">
          <circle class="cdt-21__track" cx="60" cy="60" r="51" pathLength="100"/>
          <circle class="cdt-21__arc" cx="60" cy="60" r="51" pathLength="100"/>
        </svg>
        <div class="cdt-21__center">
          <p class="cdt-21__phase" aria-hidden="true"><span class="cdt-21__work">Work</span><span class="cdt-21__rest">Rest</span></p>
          <p class="cdt-21__clock" aria-hidden="true"><em class="cdt-21__m"></em><span>:</span><em class="cdt-21__st"></em><em class="cdt-21__su"></em></p>
          <p class="cdt-21__of">of <time datetime="PT2M">2:00</time></p>
        </div>
      </div>

      <label class="cdt-21__btn" for="cdt-21-pause">
        <span class="cdt-21__ic cdt-21__ic--pause" aria-hidden="true"><svg viewBox="0 0 20 20" width="17" height="17"><rect x="5" y="3.5" width="3.6" height="13" rx="1.2" fill="currentColor"/><rect x="11.4" y="3.5" width="3.6" height="13" rx="1.2" fill="currentColor"/></svg></span>
        <span class="cdt-21__ic cdt-21__ic--play" aria-hidden="true"><svg viewBox="0 0 20 20" width="17" height="17"><path d="M6 3.6 16 10 6 16.4V3.6Z" fill="currentColor"/></svg></span>
        <span class="cdt-21__btntext">Pause interval</span>
      </label>
    </div>

    <p class="cdt-21__note">Pause is a checkbox and a <code>:has()</code> rule setting <code>animation-play-state</code>, so the ring, digits and phase label freeze in the same frame. An interval is a duration, so measuring from render is correct here — cues and session logs would need script.</p>
  </div>
</section>
```
## CSS
```css
@property --cdt21-m {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

@property --cdt21-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt21-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

.cdt-21 {
  --page: #f6ecea;
  --card: #fdf5f3;
  --ink: #2b1620;
  --muted: #7d5d68;
  --shade: #e2cfcb;
  --work-hue: #ff6a4d;
  --rest-hue: #7a4fd6;
  --ring-w: 10px;
  --work: 120s;
  --rest: 40s;
  --font-display: ui-rounded, "SF Pro Rounded", "Nunito", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-21 {
    --page: oklch(94% 0.02 30);
    --card: oklch(97% 0.014 30);
    --ink: oklch(26% 0.05 350);
    --muted: oklch(50% 0.05 350);
    --shade: oklch(87% 0.02 30);
    --work-hue: oklch(68% 0.19 34);
    --rest-hue: oklch(55% 0.19 295);
  }
}

.cdt-21 *,
.cdt-21 *::before,
.cdt-21 *::after {
  box-sizing: border-box;
}

.cdt-21__stage {
  display: grid;
  gap: 24px;
  align-content: center;
  justify-items: center;
  min-height: 100vh;
  max-inline-size: 560px;
  margin-inline: auto;
  padding: clamp(18px, 5vw, 48px);
  text-align: center;
}

.cdt-21__brand {
  margin: 0 0 6px;
  font: 700 11px/1 var(--font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--work-hue);
}

.cdt-21__title {
  margin: 0;
  font: 700 clamp(19px, 3.6vw, 25px)/1.2 var(--font-display);
  letter-spacing: -0.02em;
}

.cdt-21__dial {
  display: grid;
  justify-items: center;
  gap: 22px;
  inline-size: 100%;
  padding: clamp(22px, 5vw, 36px);
  border-radius: 36px;
  background: var(--card);
  box-shadow: 10px 10px 26px var(--shade), -10px -10px 26px rgba(255, 255, 255, 0.9);
}

.cdt-21__pause {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__arc,
.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__m,
.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__st,
.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__su,
.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__work,
.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__rest,
.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__halo {
  animation-play-state: paused;
}

.cdt-21__ringwrap {
  position: relative;
  inline-size: clamp(212px, 56vw, 288px);
  aspect-ratio: 1;
}

.cdt-21__halo {
  position: absolute;
  inset: 8%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255, 106, 77, 0.16), rgba(255, 106, 77, 0) 70%);
  animation: cdt21-halo 4s ease-in-out infinite;
}

@keyframes cdt21-halo {
  0%,
    100% {
    transform: scale(0.96);
    opacity: 0.7;
  }

  50% {
    transform: scale(1.04);
    opacity: 1;
  }
}

.cdt-21__ring {
  inline-size: 100%;
  block-size: 100%;
  transform: rotate(-90deg);
}

.cdt-21__track {
  fill: none;
  stroke: var(--shade);
  stroke-width: var(--ring-w);
}

.cdt-21__arc {
  fill: none;
  stroke: var(--work-hue);
  stroke-width: var(--ring-w);
  stroke-linecap: round;
  stroke-dasharray: 100;
  stroke-dashoffset: 0;
  animation: cdt21-arc var(--work) linear forwards, cdt21-hue var(--work) steps(1, end) forwards;
}

@keyframes cdt21-arc {
  from {
    stroke-dashoffset: 0;
  }

  to {
    stroke-dashoffset: 100;
  }
}

@keyframes cdt21-hue {
  0% {
    stroke: var(--work-hue);
  }

  100% {
    stroke: var(--rest-hue);
  }
}

.cdt-21__center {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  gap: 2px;
}

.cdt-21__phase {
  position: relative;
  margin: 0;
  block-size: 1.1em;
  font: 700 11.5px/1.1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--work-hue);
}

.cdt-21__phase span {
  position: absolute;
  inset-inline: 0;
}

.cdt-21__work {
  animation: cdt21-out 0.01s linear var(--work) forwards;
}

.cdt-21__rest {
  opacity: 0;
  color: var(--rest-hue);
  animation: cdt21-in 0.01s linear var(--work) forwards;
}

@keyframes cdt21-out {
  to {
    opacity: 0;
  }
}

@keyframes cdt21-in {
  to {
    opacity: 1;
  }
}

.cdt-21__clock {
  display: flex;
  justify-content: center;
  align-items: baseline;
  margin: 0;
  font-variant-numeric: tabular-nums;
}

.cdt-21__clock em {
  font-style: normal;
  font: 700 clamp(46px, 13vw, 66px)/1 var(--font-display);
  letter-spacing: -0.04em;
}

.cdt-21__clock span {
  font: 700 clamp(34px, 10vw, 50px)/1 var(--font-display);
  opacity: 0.35;
}

.cdt-21__m::before {
  content: counter(cdt21-m);
  counter-reset: cdt21-m var(--cdt21-m);
}

.cdt-21__st::before {
  content: counter(cdt21-st);
  counter-reset: cdt21-st var(--cdt21-st);
}

.cdt-21__su::before {
  content: counter(cdt21-su);
  counter-reset: cdt21-su var(--cdt21-su);
}

.cdt-21__m {
  animation: cdt21-m var(--work) steps(2, end) forwards;
}

.cdt-21__st {
  animation: cdt21-st 60s steps(6, end) infinite;
}

.cdt-21__su {
  animation: cdt21-su 10s steps(10, end) infinite;
}

@keyframes cdt21-m {
  from {
    --cdt21-m: 1;
  }

  to {
    --cdt21-m: -1;
  }
}

@keyframes cdt21-st {
  from {
    --cdt21-st: 5;
  }

  to {
    --cdt21-st: 0;
  }
}

@keyframes cdt21-su {
  from {
    --cdt21-su: 9;
  }

  to {
    --cdt21-su: 0;
  }
}

.cdt-21__of {
  margin: 4px 0 0;
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-21__btn {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-block-size: 48px;
  min-inline-size: 44px;
  padding: 13px 22px;
  border-radius: 99px;
  background: var(--work-hue);
  color: #fff;
  font: 700 14px/1 var(--font-display);
  cursor: pointer;
}

.cdt-21__btn:hover {
  filter: brightness(1.06);
}

.cdt-21__pause:focus-visible + .cdt-21__ringwrap + .cdt-21__btn {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.cdt-21__ic--play,
.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__ic--pause {
  display: none;
}

.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__ic--play {
  display: inline-flex;
}

.cdt-21__ic {
  display: inline-flex;
}

.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__btntext {
  font-size: 0;
}

.cdt-21__dial:has(.cdt-21__pause:checked) .cdt-21__btntext::after {
  content: "Resume interval";
  font-size: 14px;
}

.cdt-21__note {
  margin: 0;
  max-inline-size: 52ch;
  font-size: 12px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-21__note code {
  padding: 1px 5px;
  border-radius: 5px;
  background: var(--shade);
  font: 500 11px/1.4 ui-monospace, Menlo, monospace;
}

@media (prefers-reduced-motion: reduce) {
  .cdt-21__halo {
    animation: none;
    opacity: 0.8;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-21 {
  position: relative;
}

.cdt-21__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-21__tglbtn {
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

.cdt-21__tglbtn:hover {
  opacity: 1;
}

.cdt-21__tgl:focus-visible + .cdt-21__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-21__tglbtn svg {
  flex: none;
}

.cdt-21__sun,
.cdt-21__lighttext {
  display: none;
}

.cdt-21:has(.cdt-21__tgl:checked) .cdt-21__moon,
.cdt-21:has(.cdt-21__tgl:checked) .cdt-21__darktext {
  display: none;
}

.cdt-21:has(.cdt-21__tgl:checked) .cdt-21__sun {
  display: block;
}

.cdt-21:has(.cdt-21__tgl:checked) .cdt-21__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-21__tglbtn {
    padding: 12px;
  }

  .cdt-21__darktext,
    .cdt-21__lighttext,
    .cdt-21:has(.cdt-21__tgl:checked) .cdt-21__darktext,
    .cdt-21:has(.cdt-21__tgl:checked) .cdt-21__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-21:has(.cdt-21__tgl:checked) {
    --page: #1a1216;
    --card: #22181d;
    --ink: #fbeef2;
    --muted: #b18f9c;
    --shade: #2e2027;
    --work-hue: #ff8266;
    --rest-hue: #a98cff;
  }

  .cdt-21:has(.cdt-21__tgl:checked) .cdt-21__dial {
    box-shadow: 10px 10px 26px #140e11, -10px -10px 26px #291d24;
  }

  .cdt-21:has(.cdt-21__tgl:checked) .cdt-21__btn {
    color: #1a1216;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-21 {
    --page: #1a1216;
    --card: #22181d;
    --ink: #fbeef2;
    --muted: #b18f9c;
    --shade: #2e2027;
    --work-hue: #ff8266;
    --rest-hue: #a98cff;
  }

  .cdt-21__dial {
    box-shadow: 10px 10px 26px #140e11, -10px -10px 26px #291d24;
  }

  .cdt-21__btn {
    color: #1a1216;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-21:has(.cdt-21__tgl:checked) {
    --page: oklch(94% 0.02 30);
    --card: oklch(97% 0.014 30);
    --ink: oklch(26% 0.05 350);
    --muted: oklch(50% 0.05 350);
    --shade: oklch(87% 0.02 30);
    --work-hue: oklch(68% 0.19 34);
    --rest-hue: oklch(55% 0.19 295);
  }

  .cdt-21:has(.cdt-21__tgl:checked) .cdt-21__dial {
    box-shadow: 10px 10px 26px var(--shade), -10px -10px 26px rgba(255, 255, 255, 0.9);
  }

  .cdt-21:has(.cdt-21__tgl:checked) .cdt-21__btn {
    color: #fff;
  }
}

[data-theme="dark"] .cdt-21 {
  --page: #1a1216;
  --card: #22181d;
  --ink: #fbeef2;
  --muted: #b18f9c;
  --shade: #2e2027;
  --work-hue: #ff8266;
  --rest-hue: #a98cff;
}

[data-theme="dark"] .cdt-21 .cdt-21__dial {
  box-shadow: 10px 10px 26px #140e11, -10px -10px 26px #291d24;
}

[data-theme="dark"] .cdt-21 .cdt-21__btn {
  color: #1a1216;
}
```
