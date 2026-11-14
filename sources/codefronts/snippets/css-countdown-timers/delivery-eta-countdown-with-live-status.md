---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/delivery-eta-countdown-with-live-status/"
title: "Delivery ETA Countdown with Live Status"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "An order-tracking ETA that counts down beside a four-step status rail, with the active step pulsing."
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Delivery ETA Countdown with Live Status
Source: https://codefronts.com/snippets/css-countdown-timers/delivery-eta-countdown-with-live-status/

An order-tracking ETA that counts down beside a four-step status rail, with the active step pulsing. The detail most implementations miss is the zero state: instead of drifting into negative minutes it flips to Arriving any moment, because a courier who is two minutes late should not make the interface look broken.
## HTML
```html
<section class="cdt-08" aria-labelledby="cdt-08-title">
  <input class="cdt-08__tgl" type="checkbox" id="cdt-08-theme">
  <label class="cdt-08__tglbtn" for="cdt-08-theme">
    <svg class="cdt-08__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-08__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-08__darktext">Dark mode</span><span class="cdt-08__lighttext">Light mode</span>
  </label>
  <div class="cdt-08__stage">
    <article class="cdt-08__card">
      <header class="cdt-08__head">
        <div>
          <p class="cdt-08__brand">Fern Kitchen</p>
          <h2 class="cdt-08__title" id="cdt-08-title">Order 8842 · two bowls, one flatbread</h2>
        </div>
        <span class="cdt-08__courier">Sam Rivera<br><em>Courier</em></span>
      </header>

      <div class="cdt-08__eta" role="timer" aria-label="Estimated arrival countdown">
        <p class="cdt-08__etalabel">Arriving in</p>
        <p class="cdt-08__clock" aria-hidden="true">
          <em class="cdt-08__min"></em><span>:</span><em class="cdt-08__st"></em><em class="cdt-08__su"></em>
        </p>
        <p class="cdt-08__etafoot">Estimated <time datetime="PT14M">14 minutes</time> from Vale Street</p>
        <div class="cdt-08__done" role="status">
          <strong>Arriving any moment</strong>
          <span>Sam is on your street — meet at the door</span>
        </div>
      </div>

      <ol class="cdt-08__rail">
        <li class="cdt-08__step" data-state="done"><span aria-hidden="true"></span>Order placed<em>7:02 pm</em></li>
        <li class="cdt-08__step" data-state="done"><span aria-hidden="true"></span>Preparing<em>7:09 pm</em></li>
        <li class="cdt-08__step" data-state="active" data-active><span aria-hidden="true"></span>On the way<em>now</em></li>
        <li class="cdt-08__step"><span aria-hidden="true"></span>Arriving<em>7:36 pm</em></li>
      </ol>

      <p class="cdt-08__note">At zero this ETA flips to a terminal message instead of counting into negative minutes. Written in CSS only, so it measures fourteen minutes from render rather than tracking a server timestamp.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@property --cdt08-min {
  syntax: '<integer>';
  inherits: false;
  initial-value: 13;
}

@property --cdt08-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt08-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

.cdt-08 {
  --page: #f2f5ef;
  --surface-1: #ffffff;
  --surface-2: #e8eee3;
  --ink: #17231b;
  --muted: #5f7166;
  --rule: #d5e0d0;
  --accent: #2f7d4f;
  --dur: 840s;
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
  .cdt-08 {
    --page: oklch(96% 0.015 140);
    --surface-1: oklch(100% 0 0);
    --surface-2: oklch(93% 0.022 140);
    --ink: oklch(23% 0.03 150);
    --muted: oklch(52% 0.028 155);
    --rule: oklch(88% 0.02 145);
    --accent: oklch(52% 0.12 150);
  }
}

.cdt-08 *,
.cdt-08 *::before,
.cdt-08 *::after {
  box-sizing: border-box;
}

.cdt-08__stage {
  display: grid;
  place-content: center;
  justify-items: center;
  min-height: 100vh;
  padding: clamp(16px, 4vw, 44px);
}

.cdt-08__card {
  inline-size: min(560px, 100%);
  padding: clamp(20px, 4.4vw, 32px);
  background: var(--surface-1);
  border-radius: 22px;
}

.cdt-08__head {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 16px;
  align-items: flex-start;
  justify-content: space-between;
}

.cdt-08__brand {
  margin: 0 0 4px;
  font: 700 11px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.cdt-08__title {
  margin: 0;
  min-inline-size: 0;
  font: 600 clamp(16px, 2.8vw, 19px)/1.3 var(--font-display);
  text-wrap: pretty;
}

.cdt-08__courier {
  flex: none;
  font: 600 13px/1.4 var(--font-display);
  text-align: end;
}

.cdt-08__courier em {
  font: 500 11px/1 var(--font-display);
  font-style: normal;
  color: var(--muted);
}

.cdt-08__eta {
  position: relative;
  margin-block: 22px;
  padding: clamp(20px, 5vw, 30px) 18px;
  background: var(--surface-2);
  border-radius: 18px;
  text-align: center;
  overflow: hidden;
}

.cdt-08__etalabel {
  margin: 0 0 6px;
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-08__clock {
  display: flex;
  justify-content: center;
  align-items: baseline;
  gap: 1px;
  margin: 0;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
}

.cdt-08__clock em {
  font-style: normal;
  font: 700 clamp(46px, 14vw, 76px)/0.95 var(--font-display);
  letter-spacing: -0.03em;
}

.cdt-08__clock span {
  font: 700 clamp(34px, 10vw, 58px)/1 var(--font-display);
  opacity: 0.4;
}

.cdt-08__min::before {
  content: counter(cdt08-min);
  counter-reset: cdt08-min var(--cdt08-min);
}

.cdt-08__st::before {
  content: counter(cdt08-st);
  counter-reset: cdt08-st var(--cdt08-st);
}

.cdt-08__su::before {
  content: counter(cdt08-su);
  counter-reset: cdt08-su var(--cdt08-su);
}

.cdt-08__min {
  animation: cdt08-min var(--dur) steps(14, end) forwards;
}

.cdt-08__st {
  animation: cdt08-st 60s steps(6, end) infinite;
}

.cdt-08__su {
  animation: cdt08-su 10s steps(10, end) infinite;
}

@keyframes cdt08-min {
  from {
    --cdt08-min: 13;
  }

  to {
    --cdt08-min: -1;
  }
}

@keyframes cdt08-st {
  from {
    --cdt08-st: 5;
  }

  to {
    --cdt08-st: 0;
  }
}

@keyframes cdt08-su {
  from {
    --cdt08-su: 9;
  }

  to {
    --cdt08-su: 0;
  }
}

.cdt-08__etafoot {
  margin: 10px 0 0;
  font-size: 12.5px;
  color: var(--muted);
}

.cdt-08__done {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 6px;
  place-content: center;
  padding: 16px;
  background: var(--surface-2);
  opacity: 0;
  visibility: hidden;
  animation: cdt08-done 0.01s linear var(--dur) forwards;
}

.cdt-08__done strong {
  font: 700 clamp(22px, 6vw, 32px)/1.1 var(--font-display);
  color: var(--accent);
}

.cdt-08__done span {
  font-size: 12.5px;
  color: var(--muted);
}

@keyframes cdt08-done {
  from {
    opacity: 0;
    visibility: hidden;
  }

  to {
    opacity: 1;
    visibility: visible;
  }
}

.cdt-08__rail {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(72px, 1fr));
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
  overflow: clip;
  overflow-clip-margin: 10px;
}

.cdt-08__step {
  position: relative;
  display: grid;
  gap: 6px;
  justify-items: center;
  min-inline-size: 0;
  padding-block-start: 16px;
  font: 600 12px/1.3 var(--font-display);
  color: var(--muted);
  text-align: center;
}

.cdt-08__step > span {
  position: absolute;
  inset-block-start: 0;
  inline-size: 11px;
  block-size: 11px;
  border-radius: 50%;
  background: var(--rule);
}

.cdt-08__step::before {
  content: "";
  position: absolute;
  inset-block-start: 5px;
  inset-inline: 50% -50%;
  block-size: 2px;
  background: var(--rule);
}

.cdt-08__step:last-child::before {
  display: none;
}

.cdt-08__step[data-state="done"] > span,
.cdt-08__step[data-state="done"]::before {
  background: var(--accent);
}

.cdt-08__step[data-state="done"] {
  color: var(--ink);
}

.cdt-08__step[data-active] {
  color: var(--accent);
}

.cdt-08__step[data-active] > span {
  background: var(--accent);
  animation: cdt08-pulse 1.8s ease-out infinite;
}

@keyframes cdt08-pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(47, 125, 79, 0.45);
  }

  70%,
    100% {
    box-shadow: 0 0 0 9px rgba(47, 125, 79, 0);
  }
}

.cdt-08__step em {
  font: 500 11px/1 var(--font-display);
  font-style: normal;
  color: var(--muted);
}

.cdt-08__note {
  margin: 22px 0 0;
  font-size: 12px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .cdt-08__step[data-active] > span {
    animation: none;
    box-shadow: 0 0 0 4px rgba(47, 125, 79, 0.25);
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-08 {
  position: relative;
}

.cdt-08__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-08__tglbtn {
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

.cdt-08__tglbtn:hover {
  opacity: 1;
}

.cdt-08__tgl:focus-visible + .cdt-08__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-08__tglbtn svg {
  flex: none;
}

.cdt-08__sun,
.cdt-08__lighttext {
  display: none;
}

.cdt-08:has(.cdt-08__tgl:checked) .cdt-08__moon,
.cdt-08:has(.cdt-08__tgl:checked) .cdt-08__darktext {
  display: none;
}

.cdt-08:has(.cdt-08__tgl:checked) .cdt-08__sun {
  display: block;
}

.cdt-08:has(.cdt-08__tgl:checked) .cdt-08__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-08__tglbtn {
    padding: 12px;
  }

  .cdt-08__darktext,
    .cdt-08__lighttext,
    .cdt-08:has(.cdt-08__tgl:checked) .cdt-08__darktext,
    .cdt-08:has(.cdt-08__tgl:checked) .cdt-08__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-08:has(.cdt-08__tgl:checked) {
    --page: #101410;
    --surface-1: #171d18;
    --surface-2: #1f271f;
    --ink: #e9f2e9;
    --muted: #96a99a;
    --rule: #2b352c;
    --accent: #6fcf8f;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-08 {
    --page: #101410;
    --surface-1: #171d18;
    --surface-2: #1f271f;
    --ink: #e9f2e9;
    --muted: #96a99a;
    --rule: #2b352c;
    --accent: #6fcf8f;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-08:has(.cdt-08__tgl:checked) {
    --page: oklch(96% 0.015 140);
    --surface-1: oklch(100% 0 0);
    --surface-2: oklch(93% 0.022 140);
    --ink: oklch(23% 0.03 150);
    --muted: oklch(52% 0.028 155);
    --rule: oklch(88% 0.02 145);
    --accent: oklch(52% 0.12 150);
  }
}

[data-theme="dark"] .cdt-08 {
  --page: #101410;
  --surface-1: #171d18;
  --surface-2: #1f271f;
  --ink: #e9f2e9;
  --muted: #96a99a;
  --rule: #2b352c;
  --accent: #6fcf8f;
}
```
