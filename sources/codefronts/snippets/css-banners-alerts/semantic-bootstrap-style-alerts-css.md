---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/semantic-bootstrap-style-alerts-css/"
title: "Age Verification Gate Banner"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "An age gate that doubles as a four-variant semantic alert system."
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Age Verification Gate Banner
Source: https://codefronts.com/snippets/css-banners-alerts/semantic-bootstrap-style-alerts-css/

An age gate that doubles as a four-variant semantic alert system. One .ba-07__alert class plus data-variant="info | success | warning | danger" drives colour, icon and role — the Bootstrap idea rebuilt on custom properties and oklch(), with the roles wired correctly (role="alert" for errors, role="status" for confirmations).
## HTML
```html
<div class="ba-07" data-min-age="21">
  <div class="ba-07__site" aria-hidden="true">
    <div class="ba-07__siteNav"><span>Foxglove Distillery</span><span>Est. 1998 · Islay</span></div>
  </div>

  <div class="ba-07__gate" data-gate role="dialog" aria-modal="true" aria-labelledby="ba-07-h" aria-describedby="ba-07-d">
    <div class="ba-07__panel">
      <p class="ba-07__brand">Foxglove <span aria-hidden="true">·</span> Cask Programme</p>
      <h2 class="ba-07__h" id="ba-07-h">Confirm your date of birth</h2>
      <p class="ba-07__d" id="ba-07-d">You must be 21 or over to browse the cask programme. We check once and remember it on this device.</p>

      <div class="ba-07__dob" role="group" aria-labelledby="ba-07-dobLabel">
        <p class="ba-07__dobLabel" id="ba-07-dobLabel">Date of birth</p>
        <div class="ba-07__dobRow">
          <span class="ba-07__cell">
            <label for="ba-07-d1">Day</label>
            <input id="ba-07-d1" type="text" inputmode="numeric" maxlength="2" placeholder="DD" autocomplete="bday-day" data-dob="2">
          </span>
          <span class="ba-07__slash" aria-hidden="true">/</span>
          <span class="ba-07__cell">
            <label for="ba-07-m1">Month</label>
            <input id="ba-07-m1" type="text" inputmode="numeric" maxlength="2" placeholder="MM" autocomplete="bday-month" data-dob="2">
          </span>
          <span class="ba-07__slash" aria-hidden="true">/</span>
          <span class="ba-07__cell ba-07__cell--y">
            <label for="ba-07-y1">Year</label>
            <input id="ba-07-y1" type="text" inputmode="numeric" maxlength="4" placeholder="YYYY" autocomplete="bday-year" data-dob="4">
          </span>
        </div>
      </div>

      <div class="ba-07__alert" data-variant="info" data-slot role="status">
        <span class="ba-07__icons" aria-hidden="true">
          <svg class="ba-07__i ba-07__i--info" viewBox="0 0 20 20" fill="none" focusable="false"><circle cx="10" cy="10" r="7.4" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.4M10 6.4h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <svg class="ba-07__i ba-07__i--success" viewBox="0 0 20 20" fill="none" focusable="false"><circle cx="10" cy="10" r="7.4" stroke="currentColor" stroke-width="1.6"/><path d="m6.6 10.4 2.4 2.4 4.6-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <svg class="ba-07__i ba-07__i--warning" viewBox="0 0 20 20" fill="none" focusable="false"><path d="M10 3.4 17.4 16H2.6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M10 8.2v3.4M10 13.6h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <svg class="ba-07__i ba-07__i--danger" viewBox="0 0 20 20" fill="none" focusable="false"><circle cx="10" cy="10" r="7.4" stroke="currentColor" stroke-width="1.6"/><path d="m7.4 7.4 5.2 5.2m0-5.2-5.2 5.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </span>
        <p class="ba-07__alertText" data-alerttext><strong>Heads up.</strong> Enter the date in full — day, month and four-digit year.</p>
      </div>

      <label class="ba-07__remember"><input type="checkbox" data-remember checked><span aria-hidden="true"></span>Remember me on this device for 30 days</label>

      <div class="ba-07__actions">
        <button class="ba-07__btn ba-07__btn--primary" type="button" data-enter>Enter site</button>
        <a class="ba-07__btn ba-07__btn--ghost" href="#ba-07-h" data-leave>I'm under 21</a>
      </div>
      <p class="ba-07__legal">Please drink responsibly. By entering you accept our <a href="#ba-07-h">terms</a> and <a href="#ba-07-h">privacy notice</a>.</p>
    </div>
  </div>

  <div class="ba-07__swatch" data-swatch hidden>
    <div class="ba-07__alert" data-variant="success" role="status"><span class="ba-07__icons" aria-hidden="true"><svg class="ba-07__i ba-07__i--success" viewBox="0 0 20 20" fill="none" focusable="false"><circle cx="10" cy="10" r="7.4" stroke="currentColor" stroke-width="1.6"/><path d="m6.6 10.4 2.4 2.4 4.6-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span><p class="ba-07__alertText"><strong>Verified.</strong> Welcome to the cask programme.</p></div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Newsreader:opsz,[email protected],400;6..72,500&display=swap');

.ba-07 {
  --scrim: .72;
  --bg: #0d0b09;
  --surface: #17130f;
  --ink: #f6f1e8;
  --muted: #a89c8c;
  --line: #2b241d;
  --blue: #5b9dff;
  --green: #3fbe72;
  --amber: #f0b429;
  --red: #ff6a5a;
  --gold: #c8a45c;
  --sans: "Outfit",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  overflow: clip;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-07 *,
.ba-07 *::before,
.ba-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-07 {
    --bg: oklch(15% .012 60);
    --surface: oklch(19% .016 58);
    --ink: oklch(95% .014 85);
    --muted: oklch(70% .022 70);
    --line: oklch(28% .018 58);
    --blue: oklch(70% .15 255);
    --green: oklch(70% .16 150);
    --amber: oklch(80% .15 80);
    --red: oklch(68% .19 25);
    --gold: oklch(75% .1 85);
  }
}

@media (prefers-color-scheme: light) {
  .ba-07:not([data-theme="dark"]) {
    --bg: #f6f3ec;
    --surface: #ffffff;
    --ink: #1a150f;
    --muted: #6b6154;
    --line: #e5ded1;
    --scrim: .55;
  }
}

.ba-07[data-theme="light"] {
  --bg: #f6f3ec;
  --surface: #ffffff;
  --ink: #1a150f;
  --muted: #6b6154;
  --line: #e5ded1;
  --scrim: .55;
}

.ba-07__site {
  position: absolute;
  inset: 0;
  z-index: 0;
  background: radial-gradient(70% 55% at 50% 8%, color-mix(in oklab,var(--gold) 26%,transparent), transparent 70%), conic-gradient(from 210deg at 50% 120%, color-mix(in oklab,var(--gold) 12%,transparent), transparent 40%), repeating-linear-gradient(115deg, color-mix(in oklab,var(--ink) 4%,transparent) 0 2px, transparent 2px 22px), var(--bg);
}

.ba-07__siteNav {
  position: absolute;
  z-index: 1;
  inset: 0 0 auto;
  display: flex;
  justify-content: space-between;
  padding: clamp(1rem,3vw,2rem);
  font-size: .8125rem;
  letter-spacing: .04em;
  color: var(--ink);
  text-shadow: 0 1px 12px rgb(0 0 0 / .6);
}

.ba-07__gate {
  position: absolute;
  inset: 0;
  z-index: 2;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,2rem);
  background: color-mix(in oklab, var(--bg) calc(var(--scrim) * 100%), transparent);
}

@supports (backdrop-filter: blur(1px)) {
  .ba-07__gate {
    backdrop-filter: blur(14px) saturate(1.1);
  }
}

.ba-07__gate[hidden] {
  display: none;
}

.ba-07__panel {
  width: min(30rem,100%);
  display: grid;
  gap: .85rem;
  padding: clamp(1.35rem,4vw,2.25rem);
  border-radius: 1.5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 3rem 6rem -2rem rgb(0 0 0 / .6);
  transition: opacity .4s ease, scale .4s cubic-bezier(.16,1,.3,1);
}

@starting-style {
  .ba-07__panel {
    opacity: 0;
    scale: .96;
  }
}

.ba-07__brand {
  margin: 0;
  font-size: .625rem;
  font-weight: 600;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--gold);
}

.ba-07__h {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1.5rem,4.5vw,2rem);
  font-weight: 500;
  line-height: 1.08;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.ba-07__d {
  margin: 0;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 46ch;
  text-wrap: pretty;
}

.ba-07__dob {
  margin-block-start: .35rem;
}

.ba-07__dobLabel {
  margin: 0 0 .45rem;
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.ba-07__dobRow {
  display: flex;
  align-items: end;
  gap: .4rem;
}

.ba-07__cell {
  display: grid;
  gap: .25rem;
  flex: 1 1 4rem;
}

.ba-07__cell--y {
  flex: 1.4 1 6rem;
}

.ba-07__cell label {
  font-size: .625rem;
  color: var(--muted);
  letter-spacing: .06em;
}

.ba-07__cell input {
  width: 100%;
  min-height: 3rem;
  padding: .7rem .8rem;
  text-align: center;
  font: inherit;
  font-size: 1.125rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  letter-spacing: .08em;
  color: var(--ink);
  border-radius: .85rem;
  background: color-mix(in oklab,var(--ink) 6%,transparent);
  border: 1.5px solid var(--line);
  transition: border-color .2s ease, background .2s ease;
}

.ba-07__cell input::placeholder {
  color: color-mix(in oklab,var(--ink) 28%,transparent);
  letter-spacing: .12em;
}

.ba-07__cell input:focus {
  outline: 0;
  border-color: var(--gold);
  background: color-mix(in oklab,var(--ink) 10%,transparent);
}

.ba-07__slash {
  padding-block-end: .85rem;
  color: var(--muted);
}
/* semantic alert: one class, four variants */

.ba-07__alert {
  --v: var(--blue);
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .6rem;
  align-items: start;
  padding: .7rem .85rem;
  border-radius: .9rem;
  color: color-mix(in oklab,var(--v) 78%,var(--ink));
  background: color-mix(in oklab,var(--v) 12%,var(--surface));
  border: 1px solid color-mix(in oklab,var(--v) 30%,transparent);
  border-inline-start: 3px solid var(--v);
  transition: color .3s ease, background .3s ease, border-color .3s ease;
}

@starting-style {
  .ba-07__alert {
    opacity: 0;
    translate: 0 .35rem;
  }
}

.ba-07__alert[data-variant="success"] {
  --v: var(--green);
}

.ba-07__alert[data-variant="warning"] {
  --v: var(--amber);
}

.ba-07__alert[data-variant="danger"] {
  --v: var(--red);
}

.ba-07__icons {
  display: grid;
  place-items: center;
  width: 1.25rem;
  height: 1.25rem;
  margin-block-start: .1rem;
  color: var(--v);
}

.ba-07__i {
  grid-area: 1/1;
  width: 1.25rem;
  height: 1.25rem;
  display: none;
}

.ba-07__alert[data-variant="info"] .ba-07__i--info,
.ba-07__alert[data-variant="success"] .ba-07__i--success,
.ba-07__alert[data-variant="warning"] .ba-07__i--warning,
.ba-07__alert[data-variant="danger"] .ba-07__i--danger {
  display: block;
}

.ba-07__alertText {
  margin: 0;
  font-size: .8125rem;
  line-height: 1.55;
  text-wrap: pretty;
}

.ba-07__alertText strong {
  font-weight: 600;
}

.ba-07__remember {
  display: flex;
  align-items: center;
  gap: .5rem;
  min-height: 2.5rem;
  cursor: pointer;
  font-size: .75rem;
  color: var(--muted);
}

.ba-07__remember input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.ba-07__remember span {
  display: grid;
  place-items: center;
  width: 1.1rem;
  height: 1.1rem;
  flex: none;
  border-radius: .35rem;
  border: 1.5px solid var(--line);
  transition: background .2s ease, border-color .2s ease;
}

.ba-07__remember input:checked + span {
  background: var(--gold);
  border-color: var(--gold);
}

.ba-07__remember input:checked + span::after {
  content: "";
  width: .3rem;
  height: .55rem;
  border: solid var(--surface);
  border-width: 0 2px 2px 0;
  rotate: 45deg;
  translate: 0 -1px;
}

.ba-07__remember input:focus-visible + span {
  outline: 2px solid var(--gold);
  outline-offset: 2px;
}

.ba-07__actions {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
}

.ba-07__btn {
  flex: 1 1 9rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 3rem;
  padding: .85rem 1.2rem;
  border-radius: .9rem;
  cursor: pointer;
  text-decoration: none;
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.01em;
  border: 1px solid var(--line);
  background: transparent;
  color: var(--ink);
  transition: translate .2s ease, background .2s ease, border-color .2s ease;
}

.ba-07__btn--primary {
  background: var(--gold);
  border-color: transparent;
  color: #1a150f;
}

.ba-07__btn--primary:hover {
  translate: 0 -1px;
  background: color-mix(in oklab,var(--gold) 88%,white);
}

.ba-07__btn--ghost {
  color: var(--muted);
  flex: 0 1 auto;
}

.ba-07__btn--ghost:hover {
  color: var(--ink);
  border-color: var(--muted);
}

.ba-07__legal {
  margin: 0;
  font-size: .6875rem;
  line-height: 1.55;
  color: var(--muted);
}

.ba-07__legal a {
  color: var(--muted);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.ba-07__legal a:hover {
  color: var(--gold);
}

.ba-07 :focus-visible {
  outline: 2px solid var(--gold);
  outline-offset: 2px;
}

.ba-07__swatch {
  position: absolute;
  z-index: 3;
  inset: auto 50% 1.5rem auto;
  translate: 50% 0;
  width: min(26rem,calc(100% - 2rem));
}

.ba-07__swatch[hidden] {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .ba-07 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-07__panel,
    .ba-07__alert {
    border: 1px solid CanvasText;
  }

  .ba-07__btn--primary {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-07');
  if (!root) return;
  const minAge = Number(root.dataset.minAge);
  const gate = root.querySelector('[data-gate]');
  const alert = root.querySelector('[data-slot]');
  const text = root.querySelector('[data-alerttext]');
  const inputs = [...root.querySelectorAll('[data-dob]')];
  const swatch = root.querySelector('[data-swatch]');

  const say = (variant, html) => {
    alert.dataset.variant = variant;
    alert.setAttribute('role', variant === 'danger' ? 'alert' : 'status');
    text.innerHTML = html;
  };

  inputs.forEach((el, i) => {
    el.addEventListener('input', () => {
      el.value = el.value.replace(/\D/g, '');
      if (el.value.length >= Number(el.dataset.dob) && inputs[i + 1]) inputs[i + 1].focus();
    });
    el.addEventListener('keydown', (e) => {
      if (e.key === 'Backspace' && !el.value && inputs[i - 1]) inputs[i - 1].focus();
    });
  });

  root.querySelector('[data-enter]').addEventListener('click', () => {
    const [d, m, y] = inputs.map((el) => Number(el.value));
    if (!d || !m || !y || String(y).length < 4) return say('warning', '<strong>Almost.</strong> Fill in day, month and a four-digit year.');
    const dob = new Date(y, m - 1, d);
    if (dob.getDate() !== d || dob.getMonth() !== m - 1) return say('danger', '<strong>That date does not exist.</strong> Check the day and month and try again.');
    const now = new Date();
    let age = now.getFullYear() - y;
    if (now.getMonth() < m - 1 || (now.getMonth() === m - 1 && now.getDate() < d)) age -= 1;
    if (age < 0 || age > 120) return say('danger', '<strong>Check the year.</strong> That birth date is out of range.');
    if (age < minAge) return say('danger', '<strong>Sorry.</strong> You need to be ' + minAge + ' or over to browse the cask programme.');
    say('success', '<strong>Verified.</strong> Age ' + age + ' confirmed — opening the site.');
    swatch.hidden = false;
    setTimeout(() => { gate.hidden = true; }, 900);
  });

  root.querySelector('[data-leave]').addEventListener('click', (e) => {
    e.preventDefault();
    say('warning', '<strong>No problem.</strong> Come back when you are ' + minAge + '. Here is <a href="#ba-07-h">our alcohol-free range</a> instead.');
  });
})();
```
