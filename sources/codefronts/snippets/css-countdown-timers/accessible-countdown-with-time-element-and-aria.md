---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/accessible-countdown-with-time-element-and-aria/"
title: "Accessible Countdown with Time Element and ARIA"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "The reference accessible countdown: a semantic time element carries the machine-readable deadline, role=timer marks the display, and a polite live region…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Countdown with Time Element and ARIA
Source: https://codefronts.com/snippets/css-countdown-timers/accessible-countdown-with-time-element-and-aria/

The reference accessible countdown: a semantic time element carries the machine-readable deadline, role=timer marks the display, and a polite live region announces only at the hour, ten-minute, one-minute and expiry boundaries instead of shouting every second. An annotation panel labels each attribute so you can see why the quiet version is the usable one.
## HTML
```html
<section class="cdt-01" aria-labelledby="cdt-01-title">
  <input class="cdt-01__tgl" type="checkbox" id="cdt-01-theme">
  <label class="cdt-01__tglbtn" for="cdt-01-theme">
    <svg class="cdt-01__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-01__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-01__darktext">Dark mode</span><span class="cdt-01__lighttext">Light mode</span>
  </label>
  <div class="cdt-01__stage">
    <article class="cdt-01__card">
      <p class="cdt-01__eyebrow">Reference implementation</p>
      <h2 class="cdt-01__title" id="cdt-01-title">Enrollment for Cohort 12 closes</h2>
      <p class="cdt-01__lede">Meridian reviews applications in the order they arrive. The window below is the real cut-off, not a rolling banner.</p>

      <div class="cdt-01__timer" role="timer" aria-describedby="cdt-01-hint">
        <time class="cdt-01__digits" id="cdt-01-time" datetime="" aria-hidden="true">
          <span class="cdt-01__unit"><b data-h>02</b><i>hours</i></span>
          <span class="cdt-01__sep">:</span>
          <span class="cdt-01__unit"><b data-m>14</b><i>minutes</i></span>
          <span class="cdt-01__sep">:</span>
          <span class="cdt-01__unit"><b data-s>09</b><i>seconds</i></span>
        </time>
        <span class="cdt-01__sr" data-sentence>2 hours 14 minutes remaining</span>
      </div>

      <p class="cdt-01__hint" id="cdt-01-hint">Closes <span data-local>tonight</span> · applications reviewed within two working days</p>
      <output class="cdt-01__live" aria-live="polite" data-live></output>

      <div class="cdt-01__actions">
        <button class="cdt-01__btn" type="button">Start application</button>
        <button class="cdt-01__btn cdt-01__btn--ghost" type="button">Email me the deadline</button>
      </div>
    </article>

    <aside class="cdt-01__notes" aria-label="How this markup is annotated">
      <h3 class="cdt-01__ntitle">What each attribute is doing</h3>
      <dl class="cdt-01__nlist">
        <div class="cdt-01__note"><dt>&lt;time datetime&gt;</dt><dd>Machine-readable target in the DOM. Written from a real Date at load so a copied demo never renders expired.</dd></div>
        <div class="cdt-01__note"><dt>role="timer"</dt><dd>Names the region as a live countdown so assistive tech can expose it as one thing, not three numbers.</dd></div>
        <div class="cdt-01__note"><dt>aria-hidden on digits</dt><dd>"02:14:09" read aloud is noise. The compact group is hidden and a sentence is provided instead.</dd></div>
        <div class="cdt-01__note"><dt>aria-live="polite"</dt><dd>Fires at 60 min, 10 min, 1 min and expiry only. A per-second region floods the speech queue and the page becomes unnavigable.</dd></div>
      </dl>
    </aside>
  </div>
</section>
```
## CSS
```css
.cdt-01 {
  --page: #f7f5f0;
  --card: #ffffff;
  --ink: #16150f;
  --muted: #6b675c;
  --rule: #e2ded3;
  --accent: #8a2b1f;
  --chip: #f1ece1;
  --font-display: Georgia, "Iowan Old Style", "Times New Roman", serif;
  --digit-size: 64px;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-01 {
    --page: oklch(97% 0.008 85);
    --card: oklch(100% 0 0);
    --ink: oklch(19% 0.012 70);
    --muted: oklch(50% 0.014 75);
    --rule: oklch(90% 0.012 80);
    --accent: oklch(43% 0.14 30);
    --chip: oklch(94% 0.014 82);
  }
}

.cdt-01 *,
.cdt-01 *::before,
.cdt-01 *::after {
  box-sizing: border-box;
}

.cdt-01__stage {
  display: grid;
  gap: 26px;
  align-content: center;
  min-height: 100vh;
  max-inline-size: 1000px;
  margin-inline: auto;
  padding: clamp(20px, 5vw, 56px);
  padding-block-end: clamp(84px, 12vw, 96px);
  grid-template-columns: minmax(0, 1fr);
}

@media (min-width: 900px) {
  .cdt-01__stage {
    grid-template-columns: minmax(0, 1.35fr) minmax(0, 1fr);
    align-items: start;
  }
}

.cdt-01__card {
  min-inline-size: 0;
  padding: clamp(22px, 4vw, 38px);
  background: var(--card);
  border-block-start: 3px solid var(--accent);
  border-inline: 1px solid var(--rule);
  border-block-end: 1px solid var(--rule);
}

.cdt-01__eyebrow {
  margin: 0 0 14px;
  font: 500 11px/1 system-ui, sans-serif;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.cdt-01__title {
  margin: 0 0 10px;
  font: 400 clamp(26px, 4.4vw, 40px)/1.12 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.cdt-01__lede {
  margin: 0 0 26px;
  max-inline-size: 46ch;
  font-size: 14.5px;
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-01__timer {
  padding-block: 18px;
  border-block: 1px solid var(--rule);
}

.cdt-01__digits {
  display: flex;
  align-items: flex-start;
  gap: clamp(4px, 1.6vw, 12px);
  font-variant-numeric: tabular-nums;
}

.cdt-01__unit {
  display: grid;
  gap: 6px;
  justify-items: center;
  min-inline-size: 0;
}

.cdt-01__unit b {
  font: 400 clamp(38px, 11vw, var(--digit-size))/0.92 var(--font-display);
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
}

.cdt-01__unit i {
  font: 500 10px/1 system-ui, sans-serif;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-style: normal;
  color: var(--muted);
}

.cdt-01__sep {
  padding-block-start: 2px;
  font: 400 clamp(28px, 8vw, 46px)/1 var(--font-display);
  color: var(--rule);
}

.cdt-01__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cdt-01__hint {
  margin: 14px 0 0;
  font-size: 13px;
  color: var(--muted);
}

.cdt-01__live {
  display: block;
  margin-block-start: 10px;
  min-block-size: 1.2em;
  font: 500 13px/1.3 system-ui, sans-serif;
  color: var(--accent);
}

.cdt-01__live[data-expired] {
  padding: 4px 10px;
  background: var(--chip);
  border-radius: 2px;
}

.cdt-01__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-block-start: 22px;
}

.cdt-01__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 12px 20px;
  border: 1px solid var(--ink);
  border-radius: 2px;
  background: var(--ink);
  color: var(--card);
  font: 500 14px/1 system-ui, sans-serif;
  cursor: pointer;
}

.cdt-01__btn--ghost {
  background: transparent;
  color: var(--ink);
  border-color: var(--rule);
}

.cdt-01__btn:hover {
  opacity: 0.88;
}

.cdt-01__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-01__notes {
  min-inline-size: 0;
  padding: clamp(18px, 3vw, 26px);
  background: var(--chip);
  border: 1px solid var(--rule);
}

.cdt-01__ntitle {
  margin: 0 0 16px;
  font: 600 13px/1.3 system-ui, sans-serif;
  letter-spacing: 0.02em;
}

.cdt-01__nlist {
  display: grid;
  gap: 14px;
  margin: 0;
}

.cdt-01__note {
  display: grid;
  gap: 4px;
  padding-block-end: 14px;
  border-block-end: 1px solid var(--rule);
}

.cdt-01__note:last-child {
  padding-block-end: 0;
  border-block-end: 0;
}

.cdt-01__note dt {
  font: 600 12px/1.3 ui-monospace, "SFMono-Regular", Menlo, monospace;
  color: var(--accent);
  word-break: break-word;
}

.cdt-01__note dd {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-01 {
  position: relative;
}

.cdt-01__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-01__tglbtn {
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

.cdt-01__tglbtn:hover {
  opacity: 1;
}

.cdt-01__tgl:focus-visible + .cdt-01__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-01__tglbtn svg {
  flex: none;
}

.cdt-01__sun,
.cdt-01__lighttext {
  display: none;
}

.cdt-01:has(.cdt-01__tgl:checked) .cdt-01__moon,
.cdt-01:has(.cdt-01__tgl:checked) .cdt-01__darktext {
  display: none;
}

.cdt-01:has(.cdt-01__tgl:checked) .cdt-01__sun {
  display: block;
}

.cdt-01:has(.cdt-01__tgl:checked) .cdt-01__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-01__tglbtn {
    padding: 12px;
  }

  .cdt-01__darktext,
    .cdt-01__lighttext,
    .cdt-01:has(.cdt-01__tgl:checked) .cdt-01__darktext,
    .cdt-01:has(.cdt-01__tgl:checked) .cdt-01__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-01:has(.cdt-01__tgl:checked) {
    --page: #131211;
    --card: #1b1a18;
    --ink: #f2efe8;
    --muted: #a09b8f;
    --rule: #2c2a26;
    --accent: #e88a6d;
    --chip: #221f1c;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-01 {
    --page: #131211;
    --card: #1b1a18;
    --ink: #f2efe8;
    --muted: #a09b8f;
    --rule: #2c2a26;
    --accent: #e88a6d;
    --chip: #221f1c;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-01:has(.cdt-01__tgl:checked) {
    --page: oklch(97% 0.008 85);
    --card: oklch(100% 0 0);
    --ink: oklch(19% 0.012 70);
    --muted: oklch(50% 0.014 75);
    --rule: oklch(90% 0.012 80);
    --accent: oklch(43% 0.14 30);
    --chip: oklch(94% 0.014 82);
  }
}

@supports (color: oklch(50% 0.1 20)) {
  @media (prefers-color-scheme: dark) {
    .cdt-01 {
      --page: oklch(17% 0.008 70);
      --card: oklch(22% 0.01 70);
      --ink: oklch(95% 0.01 85);
      --muted: oklch(70% 0.02 78);
      --rule: oklch(29% 0.012 70);
      --accent: oklch(75% 0.12 45);
      --chip: oklch(25% 0.012 70);
    }
  }
}

[data-theme="dark"] .cdt-01 {
  --page: #131211;
  --card: #1b1a18;
  --ink: #f2efe8;
  --muted: #a09b8f;
  --rule: #2c2a26;
  --accent: #e88a6d;
  --chip: #221f1c;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-01');
if (root) {
  const el = (s) => root.querySelector(s);
  const time = el('#cdt-01-time'), live = el('[data-live]'), sentence = el('[data-sentence]');
  const target = new Date(Date.now() + 2 * 3600e3 + 14 * 60e3 + 9e3);
  const pad = (n) => String(n).padStart(2, '0');
  time.dateTime = target.toISOString();
  el('[data-local]').textContent = target.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
  const band = (ms) => ms <= 0 ? 'end' : ms < 60e3 ? 'm1' : ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : 'far';
  let seen = null, id = 0;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.floor(ms / 1000);
    el('[data-h]').textContent = pad(Math.floor(s / 3600));
    el('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    el('[data-s]').textContent = pad(s % 60);
    const h = Math.floor(s / 3600), m = Math.floor(s / 60) % 60;
    sentence.textContent = ms > 0 ? h + ' hours ' + m + ' minutes remaining' : 'Enrollment closed';
    const b = band(ms);
    if (b !== seen) {
      seen = b;
      live.toggleAttribute('data-expired', b === 'end');
      live.textContent = { far: '', h1: 'Less than one hour left to apply.', m10: 'Ten minutes left to apply.', m1: 'One minute left to apply.', end: 'Enrollment for Cohort 12 is closed.' }[b];
    }
    if (ms > 0) id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
