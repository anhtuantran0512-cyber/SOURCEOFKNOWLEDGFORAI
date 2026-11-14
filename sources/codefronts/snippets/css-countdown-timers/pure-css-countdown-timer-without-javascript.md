---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/pure-css-countdown-timer-without-javascript/"
title: "Pure CSS Countdown Timer Without JavaScript"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A countdown that runs with zero script: a registered integer custom property is animated over a wall-clock duration and printed through counter-reset plus…"
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Countdown Timer Without JavaScript
Source: https://codefronts.com/snippets/css-countdown-timers/pure-css-countdown-timer-without-javascript/

A countdown that runs with zero script: a registered integer custom property is animated over a wall-clock duration and printed through counter-reset plus content: counter(). It is honest about the one thing it cannot do — it measures a duration from render, not the distance to a timestamp, so it suits session and quiz clocks, never a dated sale.
## HTML
```html
<section class="cdt-02" aria-labelledby="cdt-02-title">
  <input class="cdt-02__tgl" type="checkbox" id="cdt-02-theme">
  <label class="cdt-02__tglbtn" for="cdt-02-theme">
    <svg class="cdt-02__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-02__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-02__darktext">Dark mode</span><span class="cdt-02__lighttext">Light mode</span>
  </label>
  <div class="cdt-02__stage">
    <div class="cdt-02__head">
      <span class="cdt-02__badge">no javascript</span>
      <h2 class="cdt-02__title" id="cdt-02-title">Practice set — Basalt certification</h2>
      <p class="cdt-02__sub"><time datetime="PT20M">Twenty minutes</time> from the moment this page rendered. The clock below is animated CSS, not a script.</p>
    </div>

    <div class="cdt-02__face" role="timer" aria-label="Twenty minute practice timer, counting down from page load">
      <div class="cdt-02__digits" aria-hidden="true">
        <span class="cdt-02__mm"><em class="cdt-02__mt"></em><em class="cdt-02__mu"></em></span>
        <span class="cdt-02__colon">:</span>
        <span class="cdt-02__ss"><em class="cdt-02__st"></em><em class="cdt-02__su"></em></span>
      </div>
      <p class="cdt-02__label">minutes · seconds remaining</p>
      <div class="cdt-02__over" role="status">
        <strong>Time up</strong>
        <span>Answers submitted automatically</span>
      </div>
    </div>

    <p class="cdt-02__caveat">
      <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M8 1.6 1.2 13.4h13.6L8 1.6Z" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M8 6v3.4M8 11.2v.9" stroke="currentColor" stroke-width="1.3"/></svg>
      A CSS-only countdown measures a duration from render, not the distance to a timestamp. It fits session and quiz clocks. For "sale ends Friday" you need the real clock, which means script.
    </p>
  </div>
</section>
```
## CSS
```css
@property --cdt02-mt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

@property --cdt02-mu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --cdt02-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt02-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

.cdt-02 {
  --page: #05070a;
  --panel: #0a0f14;
  --ink: #d8fff0;
  --muted: #5f8a7c;
  --rule: #16211d;
  --accent: #37e58f;
  --dur: 1200s;
  --font-display: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-02 {
    --page: oklch(14% 0.02 190);
    --panel: oklch(19% 0.025 185);
    --ink: oklch(94% 0.07 165);
    --muted: oklch(62% 0.05 168);
    --rule: oklch(26% 0.03 180);
    --accent: oklch(80% 0.18 155);
  }
}

.cdt-02 *,
.cdt-02 *::before,
.cdt-02 *::after {
  box-sizing: border-box;
}

.cdt-02__stage {
  display: grid;
  gap: 22px;
  align-content: center;
  justify-items: center;
  min-height: 100vh;
  max-inline-size: 760px;
  margin-inline: auto;
  padding: clamp(16px, 4vw, 40px);
}

.cdt-02__head {
  text-align: center;
  min-inline-size: 0;
}

.cdt-02__badge {
  display: inline-block;
  margin-block-end: 12px;
  padding: 5px 10px;
  border: 1px solid var(--accent);
  border-radius: 2px;
  font-size: 10.5px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.cdt-02__title {
  margin: 0 0 8px;
  font: 500 clamp(19px, 3.4vw, 26px)/1.25 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.cdt-02__sub {
  margin: 0;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-02__face {
  position: relative;
  inline-size: 100%;
  padding: clamp(22px, 6vw, 44px) clamp(14px, 4vw, 32px);
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 4px;
  overflow: hidden;
  text-align: center;
}

.cdt-02__face::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(to bottom, rgba(255, 255, 255, 0.045) 0 1px, transparent 1px 3px);
}

.cdt-02__digits {
  display: flex;
  justify-content: center;
  align-items: baseline;
  gap: 2px;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
  text-shadow: 0 0 22px rgba(55, 229, 143, 0.35);
}

.cdt-02__digits em {
  font-style: normal;
  font-size: clamp(52px, 17vw, 116px);
  font-weight: 500;
  line-height: 0.9;
  letter-spacing: -0.04em;
}

.cdt-02__colon {
  font-size: clamp(40px, 12vw, 88px);
  line-height: 0.9;
  opacity: 0.5;
  animation: cdt02-blink 2s steps(2, end) infinite;
}

.cdt-02__mt::before {
  content: counter(cdt02-mt);
  counter-reset: cdt02-mt var(--cdt02-mt);
}

.cdt-02__mu::before {
  content: counter(cdt02-mu);
  counter-reset: cdt02-mu var(--cdt02-mu);
}

.cdt-02__st::before {
  content: counter(cdt02-st);
  counter-reset: cdt02-st var(--cdt02-st);
}

.cdt-02__su::before {
  content: counter(cdt02-su);
  counter-reset: cdt02-su var(--cdt02-su);
}

.cdt-02__mt {
  animation: cdt02-mt var(--dur) steps(2, end) forwards;
}

.cdt-02__mu {
  animation: cdt02-mu 600s steps(10, end) 2;
}

.cdt-02__st {
  animation: cdt02-st 60s steps(6, end) infinite;
}

.cdt-02__su {
  animation: cdt02-su 10s steps(10, end) infinite;
}

@keyframes cdt02-mt {
  from {
    --cdt02-mt: 1;
  }

  to {
    --cdt02-mt: 0;
  }
}

@keyframes cdt02-mu {
  from {
    --cdt02-mu: 9;
  }

  to {
    --cdt02-mu: 0;
  }
}

@keyframes cdt02-st {
  from {
    --cdt02-st: 5;
  }

  to {
    --cdt02-st: 0;
  }
}

@keyframes cdt02-su {
  from {
    --cdt02-su: 9;
  }

  to {
    --cdt02-su: 0;
  }
}

@keyframes cdt02-blink {
  0%,
    50% {
    opacity: 0.5;
  }

  51%,
    100% {
    opacity: 0.12;
  }
}

@keyframes cdt02-over {
  from {
    opacity: 0;
    visibility: hidden;
  }

  to {
    opacity: 1;
    visibility: visible;
  }
}

.cdt-02__label {
  margin: 14px 0 0;
  font-size: 10.5px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-02__over {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 6px;
  place-content: center;
  background: var(--panel);
  opacity: 0;
  visibility: hidden;
  animation: cdt02-over 0.01s linear var(--dur) forwards;
}

.cdt-02__over strong {
  font-size: clamp(26px, 7vw, 44px);
  font-weight: 500;
  letter-spacing: -0.02em;
  color: var(--accent);
}

.cdt-02__over span {
  font-size: 12px;
  color: var(--muted);
}

.cdt-02__caveat {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  min-inline-size: 0;
  margin: 0;
  padding: 14px 16px;
  border: 1px dashed var(--rule);
  border-radius: 3px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-02__caveat svg {
  flex: none;
  margin-block-start: 2px;
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .cdt-02__colon {
    animation: none;
    opacity: 0.5;
  }

  .cdt-02__face::after {
    display: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-02 {
  position: relative;
}

.cdt-02__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-02__tglbtn {
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

.cdt-02__tglbtn:hover {
  opacity: 1;
}

.cdt-02__tgl:focus-visible + .cdt-02__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-02__tglbtn svg {
  flex: none;
}

.cdt-02__moon,
.cdt-02__darktext {
  display: none;
}

.cdt-02:has(.cdt-02__tgl:checked) .cdt-02__sun,
.cdt-02:has(.cdt-02__tgl:checked) .cdt-02__lighttext {
  display: none;
}

.cdt-02:has(.cdt-02__tgl:checked) .cdt-02__moon {
  display: block;
}

.cdt-02:has(.cdt-02__tgl:checked) .cdt-02__darktext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-02__tglbtn {
    padding: 12px;
  }

  .cdt-02__darktext,
    .cdt-02__lighttext,
    .cdt-02:has(.cdt-02__tgl:checked) .cdt-02__darktext,
    .cdt-02:has(.cdt-02__tgl:checked) .cdt-02__lighttext {
    display: none;
  }
}
/* toggle in the system-dark case */

@media (prefers-color-scheme: dark) {
  .cdt-02:has(.cdt-02__tgl:checked) {
    --page: #eef2ef;
    --panel: #ffffff;
    --ink: #0d1a15;
    --muted: #5c7a70;
    --rule: #d5e0da;
    --accent: #0f7a4a;
  }

  .cdt-02:has(.cdt-02__tgl:checked) .cdt-02__digits {
    text-shadow: none;
  }

  .cdt-02:has(.cdt-02__tgl:checked) .cdt-02__face::after {
    background: repeating-linear-gradient(to bottom, rgba(0, 0, 0, 0.03) 0 1px, transparent 1px 3px);
  }
}

@media (prefers-color-scheme: light) {
  .cdt-02 {
    --page: #eef2ef;
    --panel: #ffffff;
    --ink: #0d1a15;
    --muted: #5c7a70;
    --rule: #d5e0da;
    --accent: #0f7a4a;
  }

  .cdt-02__digits {
    text-shadow: none;
  }

  .cdt-02__face::after {
    background: repeating-linear-gradient(to bottom, rgba(0, 0, 0, 0.03) 0 1px, transparent 1px 3px);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-02:has(.cdt-02__tgl:checked) {
    --page: oklch(14% 0.02 190);
    --panel: oklch(19% 0.025 185);
    --ink: oklch(94% 0.07 165);
    --muted: oklch(62% 0.05 168);
    --rule: oklch(26% 0.03 180);
    --accent: oklch(80% 0.18 155);
  }

  .cdt-02:has(.cdt-02__tgl:checked) .cdt-02__digits {
    text-shadow: 0 0 22px rgba(55, 229, 143, 0.35);
  }

  .cdt-02:has(.cdt-02__tgl:checked) .cdt-02__face::after {
    background: repeating-linear-gradient(to bottom, rgba(255, 255, 255, 0.045) 0 1px, transparent 1px 3px);
  }
}

[data-theme="dark"] .cdt-02 {
  --page: #05070a;
  --panel: #0a0f14;
  --ink: #d8fff0;
  --muted: #5f8a7c;
  --rule: #16211d;
  --accent: #37e58f;
}

[data-theme="dark"] .cdt-02 .cdt-02__digits {
  text-shadow: 0 0 22px rgba(55, 229, 143, 0.35);
}
```
