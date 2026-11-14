---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/product-launch-waitlist-countdown-page/"
title: "Product Launch Waitlist Countdown Page"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A launch page built around the conversion surface rather than the clock: email capture first, a referral position chip that shows what moving up the queue is…"
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Launch Waitlist Countdown Page
Source: https://codefronts.com/snippets/css-countdown-timers/product-launch-waitlist-countdown-page/

A launch page built around the conversion surface rather than the clock: email capture first, a referral position chip that shows what moving up the queue is worth, and the countdown as supporting chrome under it. Glass panels over a violet-cyan field, and every number is a time-remaining value, never a counter climbing to a target.
## HTML
```html
<section class="cdt-09" aria-labelledby="cdt-09-title">
  <input class="cdt-09__tgl" type="checkbox" id="cdt-09-theme">
  <label class="cdt-09__tglbtn" for="cdt-09-theme">
    <svg class="cdt-09__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-09__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-09__darktext">Dark mode</span><span class="cdt-09__lighttext">Light mode</span>
  </label>
  <div class="cdt-09__field" aria-hidden="true"></div>
  <div class="cdt-09__stage">
    <div class="cdt-09__panel">
      <p class="cdt-09__eyebrow">Prism · early access</p>
      <h2 class="cdt-09__title" id="cdt-09-title">The waitlist opens before the product does</h2>
      <p class="cdt-09__lede">Invites go out in batches, top of the list first. Share your link and you move up.</p>

      <div class="cdt-09__form">
        <label class="cdt-09__label" for="cdt-09-email">Work email</label>
        <div class="cdt-09__inputrow">
          <input class="cdt-09__input" id="cdt-09-email" type="email" inputmode="email" autocomplete="email" placeholder="[email protected]">
          <button class="cdt-09__btn" type="button">Join the waitlist</button>
        </div>
        <p class="cdt-09__proof"><strong>3,418</strong> people already on the list · invites in batches of 250</p>
      </div>

      <dl class="cdt-09__chip">
        <div><dt>Your position</dt><dd>#1,204</dd></div>
        <div><dt>Each referral</dt><dd>−40 places</dd></div>
      </dl>
    </div>

    <aside class="cdt-09__clockwrap" role="timer" aria-label="Countdown to first invite batch">
      <p class="cdt-09__clocklabel">First batch goes out in</p>
      <p class="cdt-09__clock" aria-hidden="true">
        <span><em class="cdt-09__h"></em><i>hrs</i></span>
        <span><em class="cdt-09__mt"></em><em class="cdt-09__mu"></em><i>min</i></span>
        <span><em class="cdt-09__st"></em><em class="cdt-09__su"></em><i>sec</i></span>
      </p>
      <p class="cdt-09__clockfoot">Batch window <time datetime="PT3H">3 hours</time> · the timer is supporting chrome, the list is the point.</p>
      <div class="cdt-09__done" role="status"><strong>Invites are going out</strong><span>Check your inbox</span></div>
    </aside>
  </div>
</section>
```
## CSS
```css
@property --cdt09-h {
  syntax: '<integer>';
  inherits: false;
  initial-value: 2;
}

@property --cdt09-mt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt09-mu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --cdt09-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt09-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

.cdt-09 {
  --page: #0a0618;
  --ink: #f3eeff;
  --muted: #a99cd0;
  --glass: rgba(255, 255, 255, 0.07);
  --edge: rgba(255, 255, 255, 0.16);
  --accent: #9b6bff;
  --accent-2: #35e0e8;
  --dur: 10800s;
  --font-display: "Space Grotesk", "Archivo", ui-sans-serif, system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  overflow: hidden;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-09 {
    --page: oklch(14% 0.06 295);
    --ink: oklch(96% 0.02 300);
    --muted: oklch(74% 0.06 300);
    --accent: oklch(70% 0.2 295);
    --accent-2: oklch(84% 0.14 195);
  }
}

.cdt-09 *,
.cdt-09 *::before,
.cdt-09 *::after {
  box-sizing: border-box;
}

.cdt-09__field {
  position: absolute;
  inset: -30%;
  background: conic-gradient(from 210deg at 40% 45%, #9b6bff, #35e0e8, #2b1a5e, #9b6bff);
  filter: blur(90px);
  opacity: 0.5;
  animation: cdt09-spin 44s linear infinite;
}

@keyframes cdt09-spin {
  to {
    transform: rotate(1turn);
  }
}

.cdt-09__stage {
  position: relative;
  display: grid;
  gap: 20px;
  align-content: center;
  min-height: 100vh;
  max-inline-size: 1020px;
  margin-inline: auto;
  padding: clamp(18px, 5vw, 56px);
  grid-template-columns: minmax(0, 1fr);
}

@media (min-width: 880px) {
  .cdt-09__stage {
    grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr);
    align-items: stretch;
  }
}

.cdt-09__panel,
.cdt-09__clockwrap {
  min-inline-size: 0;
  padding: clamp(22px, 4vw, 34px);
  border: 1px solid var(--edge);
  border-radius: 20px;
  background: var(--glass);
  -webkit-backdrop-filter: blur(16px) saturate(1.3);
  backdrop-filter: blur(16px) saturate(1.3);
}

.cdt-09__eyebrow {
  margin: 0 0 14px;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent-2);
}

.cdt-09__title {
  margin: 0 0 10px;
  font: 600 clamp(25px, 4.6vw, 40px)/1.1 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.cdt-09__lede {
  margin: 0 0 24px;
  max-inline-size: 44ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-09__label {
  display: block;
  margin-block-end: 7px;
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-09__inputrow {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
}

.cdt-09__input {
  flex: 1 1 200px;
  min-inline-size: 0;
  min-block-size: 48px;
  padding: 13px 15px;
  border: 1px solid var(--edge);
  border-radius: 12px;
  background: rgba(0, 0, 0, 0.25);
  color: var(--ink);
  font-size: 14.5px;
}

.cdt-09__input::placeholder {
  color: rgba(243, 238, 255, 0.42);
}

.cdt-09__input:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 2px;
}

.cdt-09__btn {
  flex: 0 0 auto;
  min-block-size: 48px;
  min-inline-size: 44px;
  padding: 13px 22px;
  border: 0;
  border-radius: 12px;
  background: linear-gradient(120deg, var(--accent), var(--accent-2));
  color: #0a0618;
  font: 700 14px/1 var(--font-display);
  cursor: pointer;
}

.cdt-09__btn:hover {
  filter: brightness(1.08);
}

.cdt-09__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.cdt-09__proof {
  margin: 12px 0 0;
  font-size: 12.5px;
  color: var(--muted);
}

.cdt-09__proof strong {
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.cdt-09__chip {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 22px 0 0;
}

.cdt-09__chip > div {
  flex: 1 1 130px;
  min-inline-size: 0;
  padding: 12px 14px;
  border: 1px solid var(--edge);
  border-radius: 14px;
  background: rgba(0, 0, 0, 0.2);
}

.cdt-09__chip dt {
  font: 600 10px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-09__chip dd {
  margin: 6px 0 0;
  font: 700 20px/1 var(--font-display);
  font-variant-numeric: tabular-nums;
  color: var(--accent-2);
}

.cdt-09__clockwrap {
  position: relative;
  display: grid;
  align-content: center;
  gap: 12px;
  overflow: hidden;
  text-align: center;
}

.cdt-09__clocklabel {
  margin: 0;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-09__clock {
  display: flex;
  justify-content: center;
  gap: clamp(8px, 3vw, 18px);
  margin: 0;
  font-variant-numeric: tabular-nums;
}

.cdt-09__clock > span {
  display: grid;
  gap: 4px;
  justify-items: center;
  min-inline-size: 0;
}

.cdt-09__clock em {
  font-style: normal;
  font: 600 clamp(30px, 8vw, 44px)/1 var(--font-display);
  letter-spacing: -0.02em;
}

.cdt-09__clock > span {
  grid-auto-flow: column;
}

.cdt-09__clock i {
  grid-column: 1 / -1;
  font: 600 9.5px/1 var(--font-display);
  font-style: normal;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-09__h::before {
  content: counter(cdt09-h);
  counter-reset: cdt09-h var(--cdt09-h);
}

.cdt-09__mt::before {
  content: counter(cdt09-mt);
  counter-reset: cdt09-mt var(--cdt09-mt);
}

.cdt-09__mu::before {
  content: counter(cdt09-mu);
  counter-reset: cdt09-mu var(--cdt09-mu);
}

.cdt-09__st::before {
  content: counter(cdt09-st);
  counter-reset: cdt09-st var(--cdt09-st);
}

.cdt-09__su::before {
  content: counter(cdt09-su);
  counter-reset: cdt09-su var(--cdt09-su);
}

.cdt-09__h {
  animation: cdt09-h var(--dur) steps(3, end) forwards;
}

.cdt-09__mt {
  animation: cdt09-mt 3600s steps(6, end) infinite;
}

.cdt-09__mu {
  animation: cdt09-mu 600s steps(10, end) infinite;
}

.cdt-09__st {
  animation: cdt09-st 60s steps(6, end) infinite;
}

.cdt-09__su {
  animation: cdt09-su 10s steps(10, end) infinite;
}

@keyframes cdt09-h {
  from {
    --cdt09-h: 2;
  }

  to {
    --cdt09-h: -1;
  }
}

@keyframes cdt09-mt {
  from {
    --cdt09-mt: 5;
  }

  to {
    --cdt09-mt: -1;
  }
}

@keyframes cdt09-mu {
  from {
    --cdt09-mu: 9;
  }

  to {
    --cdt09-mu: 0;
  }
}

@keyframes cdt09-st {
  from {
    --cdt09-st: 5;
  }

  to {
    --cdt09-st: 0;
  }
}

@keyframes cdt09-su {
  from {
    --cdt09-su: 9;
  }

  to {
    --cdt09-su: 0;
  }
}

.cdt-09__clockfoot {
  margin: 0;
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--muted);
}

.cdt-09__done {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 6px;
  place-content: center;
  padding: 16px;
  background: rgba(10, 6, 24, 0.92);
  opacity: 0;
  visibility: hidden;
  animation: cdt09-done 0.01s linear var(--dur) forwards;
}

.cdt-09__done strong {
  font: 700 clamp(20px, 5vw, 28px)/1.15 var(--font-display);
  color: var(--accent-2);
}

.cdt-09__done span {
  font-size: 12.5px;
  color: var(--muted);
}

@keyframes cdt09-done {
  from {
    opacity: 0;
    visibility: hidden;
  }

  to {
    opacity: 1;
    visibility: visible;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdt-09__field {
    animation: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-09 {
  position: relative;
}

.cdt-09__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-09__tglbtn {
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

.cdt-09__tglbtn:hover {
  opacity: 1;
}

.cdt-09__tgl:focus-visible + .cdt-09__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-09__tglbtn svg {
  flex: none;
}

.cdt-09__moon,
.cdt-09__darktext {
  display: none;
}

.cdt-09:has(.cdt-09__tgl:checked) .cdt-09__sun,
.cdt-09:has(.cdt-09__tgl:checked) .cdt-09__lighttext {
  display: none;
}

.cdt-09:has(.cdt-09__tgl:checked) .cdt-09__moon {
  display: block;
}

.cdt-09:has(.cdt-09__tgl:checked) .cdt-09__darktext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-09__tglbtn {
    padding: 12px;
  }

  .cdt-09__darktext,
    .cdt-09__lighttext,
    .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__darktext,
    .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__lighttext {
    display: none;
  }
}
/* toggle in the system-dark case */

@media (prefers-color-scheme: dark) {
  .cdt-09:has(.cdt-09__tgl:checked) {
    --page: #f4f1fd;
    --ink: #1a1130;
    --muted: #5f5482;
    --glass: rgba(255, 255, 255, 0.6);
    --edge: rgba(26, 17, 48, 0.12);
    --accent: #6b34e0;
    --accent-2: #0b8f97;
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__field {
    opacity: 0.32;
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__input {
    background: rgba(255, 255, 255, 0.75);
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__input::placeholder {
    color: rgba(26, 17, 48, 0.42);
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__btn {
    color: #fff;
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__chip > div {
    background: rgba(255, 255, 255, 0.6);
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__done {
    background: rgba(244, 241, 253, 0.94);
  }
}

@media (prefers-color-scheme: light) {
  .cdt-09 {
    --page: #f4f1fd;
    --ink: #1a1130;
    --muted: #5f5482;
    --glass: rgba(255, 255, 255, 0.6);
    --edge: rgba(26, 17, 48, 0.12);
    --accent: #6b34e0;
    --accent-2: #0b8f97;
  }

  .cdt-09__field {
    opacity: 0.32;
  }

  .cdt-09__input {
    background: rgba(255, 255, 255, 0.75);
  }

  .cdt-09__input::placeholder {
    color: rgba(26, 17, 48, 0.42);
  }

  .cdt-09__btn {
    color: #fff;
  }

  .cdt-09__chip > div {
    background: rgba(255, 255, 255, 0.6);
  }

  .cdt-09__done {
    background: rgba(244, 241, 253, 0.94);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-09:has(.cdt-09__tgl:checked) {
    --page: oklch(14% 0.06 295);
    --ink: oklch(96% 0.02 300);
    --muted: oklch(74% 0.06 300);
    --glass: rgba(255, 255, 255, 0.07);
    --edge: rgba(255, 255, 255, 0.16);
    --accent: oklch(70% 0.2 295);
    --accent-2: oklch(84% 0.14 195);
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__field {
    opacity: 0.5;
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__input {
    background: rgba(0, 0, 0, 0.25);
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__input::placeholder {
    color: rgba(243, 238, 255, 0.42);
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__btn {
    color: #0a0618;
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__chip > div {
    background: rgba(0, 0, 0, 0.2);
  }

  .cdt-09:has(.cdt-09__tgl:checked) .cdt-09__done {
    background: rgba(10, 6, 24, 0.92);
  }
}

[data-theme="dark"] .cdt-09 {
  --page: #0a0618;
  --ink: #f3eeff;
  --muted: #a99cd0;
  --glass: rgba(255, 255, 255, 0.07);
  --edge: rgba(255, 255, 255, 0.16);
  --accent: #9b6bff;
  --accent-2: #35e0e8;
}
```
