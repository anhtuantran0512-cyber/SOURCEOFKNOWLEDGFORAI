---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/form-elements/"
title: "Brutalist Form Controls"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A full form rendered with its structure showing: 3px black field borders, uppercase monospace labels, a select that keeps a plain default arrow, and a submit…"
has_js: "true"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Form Controls
Source: https://codefronts.com/design-styles/css-brutalist/form-elements/

A full form rendered with its structure showing: 3px black field borders, uppercase monospace labels, a select that keeps a plain default arrow, and a submit that looks like an unstyled HTML button. Focus inverts the field to white-on-black rather than glowing, and validation is reported through a live region — with no submit handler anywhere.
## HTML
```html
<div class="brt-16">
  <button class="brt-16__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="brt-16__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-16__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
  </button>

  <div class="brt-16__stage">
    <section class="brt-16__sheet" id="brt-16-sheet" aria-labelledby="brt-16-h">
      <h1 class="brt-16__h" id="brt-16-h">EQUIPMENT REQUEST</h1>
      <p class="brt-16__note">Internal form 04-B. Submitted requests are reviewed on Thursdays.</p>

      <div class="brt-16__row">
        <label class="brt-16__label" for="brt-16-name">01 / Requester name</label>
        <input class="brt-16__input" id="brt-16-name" type="text" autocomplete="name" placeholder="SURNAME, FIRST NAME" aria-describedby="brt-16-name-err">
        <p class="brt-16__err" id="brt-16-name-err"></p>
      </div>

      <div class="brt-16__row">
        <label class="brt-16__label" for="brt-16-mail">02 / Work email</label>
        <input class="brt-16__input" id="brt-16-mail" type="email" autocomplete="email" placeholder="[email protected]" aria-describedby="brt-16-mail-hint brt-16-mail-err">
        <p class="brt-16__hint" id="brt-16-mail-hint">Use your department address. Personal addresses are rejected.</p>
        <p class="brt-16__err" id="brt-16-mail-err"></p>
      </div>

      <div class="brt-16__two">
        <div class="brt-16__row">
          <label class="brt-16__label" for="brt-16-dept">03 / Department</label>
          <select class="brt-16__select" id="brt-16-dept">
            <option value="">SELECT ONE</option>
            <option>Fabrication</option>
            <option>Field survey</option>
            <option>Records office</option>
            <option>Print room</option>
          </select>
        </div>
        <div class="brt-16__row">
          <label class="brt-16__label" for="brt-16-qty">04 / Units</label>
          <input class="brt-16__input" id="brt-16-qty" type="number" min="1" max="40" value="2" inputmode="numeric">
        </div>
      </div>

      <div class="brt-16__row">
        <label class="brt-16__label" for="brt-16-why">05 / Justification</label>
        <textarea class="brt-16__area" id="brt-16-why" rows="3" placeholder="STATE THE TASK AND THE DEADLINE." aria-describedby="brt-16-why-err"></textarea>
        <p class="brt-16__err" id="brt-16-why-err"></p>
      </div>

      <fieldset class="brt-16__set">
        <legend class="brt-16__legend">06 / Collection</legend>
        <label class="brt-16__opt"><input class="brt-16__radio" type="radio" name="brt-16-pick" checked><span>Collect from store, ground floor</span></label>
        <label class="brt-16__opt"><input class="brt-16__radio" type="radio" name="brt-16-pick"><span>Internal post, 3 working days</span></label>
      </fieldset>

      <label class="brt-16__opt brt-16__opt--single"><input class="brt-16__check" type="checkbox" id="brt-16-ack" aria-describedby="brt-16-ack-err"><span>I accept responsibility for the listed equipment.</span></label>
      <p class="brt-16__err" id="brt-16-ack-err"></p>

      <div class="brt-16__actions">
        <button class="brt-16__submit" id="brt-16-go" type="button">SUBMIT REQUEST</button>
        <button class="brt-16__reset" id="brt-16-clear" type="button">CLEAR</button>
      </div>
      <p class="brt-16__status" id="brt-16-status" role="status" aria-live="polite"></p>
    </section>
  </div>
</div>
```
## CSS
```css
.brt-16 {
  --page: #f4f3ee;
  --panel: #ffffff;
  --ink: #000000;
  --muted: #3a3a3a;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --mono: ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
  font-size: 16px;
}

.brt-16 *,
.brt-16 *::before,
.brt-16 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-16 {
    --page: oklch(0.962 0.006 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0 0 0);
    --muted: oklch(0.34 0 0);
  }
}

.brt-16__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding: 0;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
}

.brt-16__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-16__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-16__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-16__theme:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-16__sun {
  display: none;
}

.brt-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(1rem,3vw,2.5rem);
}

.brt-16__sheet {
  inline-size: min(44rem,100%);
  padding: clamp(1.1rem,3vw,2rem);
  background: var(--panel);
  border: 5px solid var(--edge);
  box-shadow: 8px 8px 0 var(--sh);
}

.brt-16__h {
  margin: 0;
  padding-inline-end: 3rem;
  font-size: clamp(1.5rem,4.6vw,2.4rem);
  font-weight: 700;
  letter-spacing: -.02em;
  text-transform: uppercase;
}

.brt-16__note {
  margin: .4rem 0 1.6rem;
  padding-block-end: .8rem;
  border-block-end: var(--bw) solid var(--edge);
  font-family: var(--mono);
  font-size: .82rem;
  line-height: 1.5;
  color: var(--muted);
}

.brt-16__row {
  margin-block-end: 1.35rem;
}

.brt-16__two {
  display: grid;
  gap: 0 1.25rem;
  grid-template-columns: repeat(auto-fit,minmax(min(12rem,100%),1fr));
}

.brt-16__label {
  display: block;
  margin-block-end: .35rem;
  font-family: var(--mono);
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.brt-16__input,
.brt-16__area,
.brt-16__select {
  inline-size: 100%;
  min-block-size: 2.9rem;
  padding: .7rem .8rem;
  font-family: var(--mono);
  font-size: .95rem;
  color: var(--ink);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
}

.brt-16__area {
  min-block-size: 5.5rem;
  resize: vertical;
  line-height: 1.5;
}

@supports (field-sizing: content) {
  .brt-16__area {
    field-sizing: content;
    max-block-size: 12rem;
  }
}

.brt-16__input::placeholder,
.brt-16__area::placeholder {
  color: var(--muted);
  opacity: .65;
  letter-spacing: .06em;
}

.brt-16__input:focus,
.brt-16__area:focus,
.brt-16__select:focus {
  outline: 3px solid var(--edge);
  outline-offset: -3px;
  background: var(--ink);
  color: var(--page);
  caret-color: var(--page);
}

.brt-16__input:focus::placeholder,
.brt-16__area:focus::placeholder {
  color: var(--page);
  opacity: .55;
}

.brt-16__select {
  appearance: none;
  -webkit-appearance: none;
  padding-inline-end: 2.6rem;
  cursor: pointer;
  background-image: linear-gradient(45deg,transparent 50%,var(--ink) 50%),linear-gradient(135deg,var(--ink) 50%,transparent 50%);
  background-size: 9px 9px,9px 9px;
  background-repeat: no-repeat;
  background-position: right 1.25rem top 55%, right .8rem top 55%;
}

.brt-16__select:focus {
  background-image: linear-gradient(45deg,transparent 50%,var(--page) 50%),linear-gradient(135deg,var(--page) 50%,transparent 50%);
}

.brt-16__hint {
  margin: .35rem 0 0;
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--muted);
}

.brt-16__err {
  margin: 0;
  font-family: var(--mono);
  font-size: .78rem;
  font-weight: 700;
}

.brt-16__err:not(:empty) {
  margin-block-start: .4rem;
  padding: .3rem .45rem;
  background: var(--ink);
  color: var(--page);
  text-transform: uppercase;
  letter-spacing: .08em;
}

.brt-16__input[data-invalid],
.brt-16__area[data-invalid],
.brt-16__input:user-invalid {
  border-width: 5px;
}

.brt-16__set {
  margin: 0 0 1.35rem;
  padding: .9rem;
  border: var(--bw) solid var(--edge);
}

.brt-16__legend {
  padding: 0 .4rem;
  font-family: var(--mono);
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.brt-16__opt {
  display: grid;
  grid-template-columns: 1.5rem 1fr;
  gap: .7rem;
  align-items: center;
  min-block-size: 2.75rem;
  font-size: .95rem;
  cursor: pointer;
}

.brt-16__opt--single {
  margin-block-end: .25rem;
}

.brt-16__radio,
.brt-16__check {
  appearance: none;
  -webkit-appearance: none;
  margin: 0;
  inline-size: 1.5rem;
  block-size: 1.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  cursor: pointer;
}

.brt-16__radio::after,
.brt-16__check::after {
  content: '';
  inline-size: .7rem;
  block-size: .7rem;
  background: var(--ink);
  opacity: 0;
}

.brt-16__radio:checked::after,
.brt-16__check:checked::after {
  opacity: 1;
}

.brt-16__radio:focus-visible,
.brt-16__check:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-16__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem;
  margin-block-start: 1.5rem;
  padding-block-start: 1.1rem;
  border-block-start: var(--bw) solid var(--edge);
}

.brt-16__submit,
.brt-16__reset {
  min-block-size: 2.9rem;
  padding: .7rem 1.1rem;
  font-family: var(--mono);
  font-size: .88rem;
  font-weight: 700;
  letter-spacing: .1em;
  cursor: pointer;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  box-shadow: 4px 4px 0 var(--sh);
}

.brt-16__submit {
  background: var(--ink);
  color: var(--page);
}

.brt-16__submit:active,
.brt-16__reset:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-16__submit:focus-visible,
.brt-16__reset:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-16__submit[aria-busy="true"] {
  cursor: progress;
}

.brt-16__status {
  margin: 1rem 0 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.brt-16__status:not(:empty) {
  padding: .35rem .5rem;
  border: var(--bw) solid var(--edge);
}

.brt-16[data-theme="dark"] {
  --page: #000000;
  --panel: #0a0a0a;
  --ink: #ffffff;
  --muted: #c2c2c2;
  --edge: #ffffff;
  --sh: #ffffff;
}

.brt-16[data-theme="dark"] .brt-16__moon {
  display: none;
}

.brt-16[data-theme="dark"] .brt-16__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-16:not([data-theme="light"]) {
    --page: #000000;
    --panel: #0a0a0a;
    --ink: #ffffff;
    --muted: #c2c2c2;
    --edge: #ffffff;
    --sh: #ffffff;
  }

  .brt-16:not([data-theme="light"]) .brt-16__moon {
    display: none;
  }

  .brt-16:not([data-theme="light"]) .brt-16__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-16 *,
    .brt-16 *::before,
    .brt-16 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-16__sheet,
    .brt-16__input,
    .brt-16__area,
    .brt-16__select,
    .brt-16__submit,
    .brt-16__reset,
    .brt-16__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-16__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.brt-16');
  if (!root) return;
  const sheet = root.querySelector('#brt-16-sheet');
  const status = root.querySelector('#brt-16-status');
  const go = root.querySelector('#brt-16-go');
  const rules = [
    ['#brt-16-name', '#brt-16-name-err', (v) => v.trim().length > 2 || 'Name required'],
    ['#brt-16-mail', '#brt-16-mail-err', (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) || 'Department address required'],
    ['#brt-16-why', '#brt-16-why-err', (v) => v.trim().length > 9 || 'State the task and the deadline'],
  ];

  const check = () => {
    let bad = 0;
    for (const [sel, errSel, test] of rules) {
      const el = root.querySelector(sel), err = root.querySelector(errSel);
      const res = test(el.value), ok = res === true;
      err.textContent = ok ? '' : res;
      el.toggleAttribute('data-invalid', !ok);
      el.setAttribute('aria-invalid', String(!ok));
      if (!ok && ++bad === 1) el.focus();
    }
    const ack = root.querySelector('#brt-16-ack');
    const ackErr = root.querySelector('#brt-16-ack-err');
    ackErr.textContent = ack.checked ? '' : 'Accept responsibility to continue';
    if (!ack.checked) bad++;
    return bad;
  };

  const submit = () => {
    const bad = check();
    if (bad) { status.textContent = bad + ' field(s) rejected'; return; }
    go.setAttribute('aria-busy', 'true');
    status.textContent = 'Filing request…';
    setTimeout(() => { go.removeAttribute('aria-busy'); status.textContent = 'Request 04-B-2291 filed'; }, 800);
  };

  go.addEventListener('click', submit);
  sheet.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.target.matches('input:not([type="checkbox"]):not([type="radio"])')) { e.preventDefault(); submit(); }
  });
  root.querySelector('#brt-16-clear').addEventListener('click', () => {
    root.querySelectorAll('input:not([type="radio"]), textarea, select').forEach((el) => {
      if (el.type === 'checkbox') el.checked = false; else el.value = el.type === 'number' ? '2' : '';
      el.removeAttribute('data-invalid'); el.removeAttribute('aria-invalid');
    });
    root.querySelectorAll('.brt-16__err').forEach((p) => (p.textContent = ''));
    status.textContent = 'Form cleared';
  });
})();

(() => {                                     /* theme toggle */
  const root = document.querySelector('.brt-16');
  const btn = root && root.querySelector('.brt-16__theme');
  if (!btn) return;
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(dark()));
    btn.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  sync();
})();
```
