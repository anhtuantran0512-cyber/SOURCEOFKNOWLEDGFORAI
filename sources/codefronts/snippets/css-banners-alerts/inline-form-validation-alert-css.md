---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/inline-form-validation-alert-css/"
title: "Inline Form Validation Alert"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "Validation done to the WCAG playbook, with modern CSS doing most of the work: :user-invalid for humane timing, :has() to style the whole field group from the…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Form Validation Alert
Source: https://codefronts.com/snippets/css-banners-alerts/inline-form-validation-alert-css/

Validation done to the WCAG playbook, with modern CSS doing most of the work: :user-invalid for humane timing, :has() to style the whole field group from the input's state, a live password strength meter, field-sizing:content on the textarea, and an error summary at the top whose links move focus straight to the offending field.
## HTML
```html
<div class="ba-14">
  <section class="ba-14__card" aria-labelledby="ba-14-h">
    <header class="ba-14__head">
      <p class="ba-14__eyebrow">Step 2 of 3</p>
      <h2 class="ba-14__h" id="ba-14-h">Create your workspace account</h2>
      <p class="ba-14__sub">Fields marked with an asterisk are required. We validate as you go, not while you type your first letter.</p>
    </header>

    <div class="ba-14__summary" data-summary hidden tabindex="-1">
      <span class="ba-14__sumIcon" aria-hidden="true">
        <svg viewBox="0 0 20 20" fill="none" focusable="false"><path d="M10 3.4 17.4 16H2.6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M10 8v3.4M10 13.7h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </span>
      <div>
        <h3 class="ba-14__sumTitle" data-sumtitle>There are 2 problems with your details</h3>
        <ul class="ba-14__sumList" data-sumlist></ul>
      </div>
    </div>

    <div class="ba-14__grid">
      <div class="ba-14__f">
        <label for="ba-14-name">Full name <abbr title="required">*</abbr></label>
        <div class="ba-14__inputWrap">
          <input id="ba-14-name" type="text" required minlength="2" autocomplete="name" placeholder="Ada Okonjo"
                 aria-describedby="ba-14-name-h ba-14-name-m" data-field data-label="Full name">
          <svg class="ba-14__ok" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m5 10.4 3.2 3.2L15 6.8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <p class="ba-14__hint" id="ba-14-name-h">As it should appear on invoices.</p>
        <p class="ba-14__msg" id="ba-14-name-m" data-msg>Enter your full name, at least two characters.</p>
      </div>

      <div class="ba-14__f">
        <label for="ba-14-email">Work email <abbr title="required">*</abbr></label>
        <div class="ba-14__inputWrap">
          <input id="ba-14-email" type="email" required inputmode="email" autocomplete="email" placeholder="[email protected]"
                 aria-describedby="ba-14-email-h ba-14-email-m" data-field data-label="Work email">
          <svg class="ba-14__ok" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m5 10.4 3.2 3.2L15 6.8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <p class="ba-14__hint" id="ba-14-email-h">We send one verification link, nothing else.</p>
        <p class="ba-14__msg" id="ba-14-email-m" data-msg>Enter an address like [email protected].</p>
      </div>

      <div class="ba-14__f">
        <label for="ba-14-pw">Password <abbr title="required">*</abbr></label>
        <div class="ba-14__inputWrap">
          <input id="ba-14-pw" type="password" required minlength="12" autocomplete="new-password"
                 aria-describedby="ba-14-pw-h ba-14-pw-m ba-14-pw-s" data-field data-label="Password" data-pw>
          <button class="ba-14__peek" type="button" data-peek aria-pressed="false">
            <span class="ba-14__vh">Show password</span>
            <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M2.5 10S5.4 5.2 10 5.2 17.5 10 17.5 10 14.6 14.8 10 14.8 2.5 10 2.5 10z" stroke="currentColor" stroke-width="1.5"/><circle cx="10" cy="10" r="2.2" stroke="currentColor" stroke-width="1.5"/></svg>
          </button>
        </div>
        <div class="ba-14__meter" id="ba-14-pw-s">
          <div class="ba-14__mtrack" role="progressbar" aria-label="Password strength" aria-valuemin="0" aria-valuemax="4" aria-valuenow="0" data-mtrack>
            <span></span><span></span><span></span><span></span>
          </div>
          <p class="ba-14__mText" data-mtext>Use 12+ characters with a number and a symbol.</p>
        </div>
        <p class="ba-14__hint" id="ba-14-pw-h">A passphrase beats a clever short password.</p>
        <p class="ba-14__msg" id="ba-14-pw-m" data-msg>Use at least 12 characters.</p>
      </div>

      <div class="ba-14__f">
        <label for="ba-14-team">Team size</label>
        <div class="ba-14__inputWrap">
          <select id="ba-14-team" aria-describedby="ba-14-team-h">
            <option value="">Select a range</option>
            <option>Just me</option>
            <option>2-10</option>
            <option>11-50</option>
            <option>51-200</option>
            <option>200+</option>
          </select>
        </div>
        <p class="ba-14__hint" id="ba-14-team-h">Used to set your default plan; you can change it later.</p>
      </div>

      <div class="ba-14__f ba-14__f--wide">
        <label for="ba-14-note">What are you building? <span class="ba-14__opt">Optional</span></label>
        <div class="ba-14__inputWrap">
          <textarea id="ba-14-note" rows="2" maxlength="280" placeholder="One line is plenty." aria-describedby="ba-14-note-h" data-note></textarea>
        </div>
        <p class="ba-14__hint" id="ba-14-note-h"><span data-count>0</span>/280 · the box grows as you type.</p>
      </div>

      <div class="ba-14__f ba-14__f--wide">
        <label class="ba-14__check">
          <input type="checkbox" required data-field data-label="Terms" aria-describedby="ba-14-terms-m">
          <span class="ba-14__box" aria-hidden="true"></span>
          <span>I accept the <a href="#ba-14-h">terms of service</a> and the <a href="#ba-14-h">data processing addendum</a>. <abbr title="required">*</abbr></span>
        </label>
        <p class="ba-14__msg" id="ba-14-terms-m" data-msg>You need to accept the terms to continue.</p>
      </div>
    </div>

    <div class="ba-14__foot">
      <button class="ba-14__submit" type="button" data-submit>Create account</button>
      <p class="ba-14__footNote">Already have one? <a href="#ba-14-h">Sign in instead</a></p>
    </div>

    <div class="ba-14__done" data-done hidden>
      <span aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="m6 12.5 4 4 8.5-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <p><strong>Account created.</strong> Check your inbox for the verification link.</p>
    </div>
  </section>
  <p class="ba-14__live" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');

@property --ba-14-s {
  syntax: '<number>';
  inherits: false;
  initial-value: 0;
}

.ba-14 {
  --cols: 2;
  --bg: #f3f4f7;
  --surface: #ffffff;
  --ink: #0e1116;
  --muted: #666e7a;
  --line: #dfe3e9;
  --acc: #4338ca;
  --good: #0f9d58;
  --bad: #d92d20;
  --warn: #e0a000;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(44rem 30rem at 15% 0%, color-mix(in oklab,var(--acc) 11%,transparent), transparent 65%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-14 *,
.ba-14 *::before,
.ba-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-14 {
    --bg: oklch(96.5% .006 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(18% .014 265);
    --muted: oklch(56% .016 265);
    --line: oklch(90% .01 265);
    --acc: oklch(48% .2 285);
    --good: oklch(60% .16 150);
    --bad: oklch(57% .21 27);
    --warn: oklch(74% .15 82);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-14:not([data-theme="light"]) {
    --bg: #0a0c10;
    --surface: #12151b;
    --ink: #eef1f5;
    --muted: #98a0ac;
    --line: #232831;
  }
}

.ba-14[data-theme="dark"] {
  --bg: #0a0c10;
  --surface: #12151b;
  --ink: #eef1f5;
  --muted: #98a0ac;
  --line: #232831;
}

.ba-14__card {
  container-type: inline-size;
  width: min(44rem,100%);
  display: grid;
  gap: 1.15rem;
  padding: clamp(1.25rem,4vw,2.25rem);
  border-radius: 1.5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 2.5rem 5rem -2.5rem rgb(14 17 22 / .22);
}

.ba-14__head {
  display: grid;
  gap: .35rem;
}

.ba-14__eyebrow {
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ba-14__h {
  margin: 0;
  font-size: clamp(1.375rem,4cqw,1.875rem);
  font-weight: 700;
  letter-spacing: -.035em;
  line-height: 1.1;
  text-wrap: balance;
}

.ba-14__sub {
  margin: 0;
  font-size: .875rem;
  line-height: 1.55;
  color: var(--muted);
  max-width: 62ch;
  text-wrap: pretty;
}

.ba-14__summary {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .75rem;
  align-items: start;
  padding: .9rem 1rem;
  border-radius: 1rem;
  color: color-mix(in oklab,var(--bad) 80%,var(--ink));
  background: color-mix(in oklab,var(--bad) 10%,var(--surface));
  border: 1px solid color-mix(in oklab,var(--bad) 32%,transparent);
}

.ba-14__summary[hidden] {
  display: none;
}

@starting-style {
  .ba-14__summary {
    opacity: 0;
    translate: 0 -.4rem;
  }
}

.ba-14__sumIcon {
  display: grid;
  place-items: center;
  width: 1.5rem;
  height: 1.5rem;
  color: var(--bad);
}

.ba-14__sumIcon svg {
  width: 1.35rem;
  height: 1.35rem;
}

.ba-14__sumTitle {
  margin: 0 0 .35rem;
  font-size: .9375rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ba-14__sumList {
  margin: 0;
  padding: 0 0 0 1rem;
  display: grid;
  gap: .2rem;
  font-size: .8125rem;
}

.ba-14__sumList a {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.ba-14__sumList a:hover {
  text-decoration-thickness: 2px;
}

.ba-14__grid {
  display: grid;
  grid-template-columns: repeat(var(--cols),minmax(0,1fr));
  gap: 1rem;
}

.ba-14__f {
  --ring: var(--line);
  --iconTint: var(--good);
  display: grid;
  gap: .35rem;
  min-width: 0;
}

.ba-14__f--wide {
  grid-column: 1 / -1;
}

.ba-14__f > label {
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: -.01em;
  display: flex;
  align-items: center;
  gap: .35rem;
}

.ba-14__f abbr {
  color: var(--bad);
  text-decoration: none;
  font-weight: 700;
}

.ba-14__opt {
  font-size: .6875rem;
  font-weight: 500;
  color: var(--muted);
  padding: .1rem .35rem;
  border-radius: .3rem;
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.ba-14__inputWrap {
  position: relative;
}

.ba-14__f input:not([type="checkbox"]),
.ba-14__f select,
.ba-14__f textarea {
  width: 100%;
  min-height: 2.9rem;
  padding: .75rem 2.5rem .75rem .9rem;
  font: inherit;
  font-size: .9375rem;
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 3%,var(--surface));
  border: 1.5px solid var(--ring);
  border-radius: .85rem;
  transition: border-color .2s ease, background .2s ease, box-shadow .2s ease;
}

.ba-14__f textarea {
  min-block-size: 3.5rem;
  resize: vertical;
  line-height: 1.55;
}

@supports (field-sizing: content) {
  .ba-14__f textarea {
    field-sizing: content;
    max-block-size: 9rem;
  }
}

.ba-14__f select {
  appearance: none;
  cursor: pointer;
}

.ba-14__f input::placeholder,
.ba-14__f textarea::placeholder {
  color: color-mix(in oklab,var(--ink) 34%,transparent);
}

.ba-14__f input:focus,
.ba-14__f select:focus,
.ba-14__f textarea:focus {
  outline: 0;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--acc) 16%,transparent);
}

.ba-14__f input:autofill {
  box-shadow: 0 0 0 100px color-mix(in oklab,var(--acc) 8%,var(--surface)) inset;
  -webkit-text-fill-color: var(--ink);
}

.ba-14__f:has(input:user-invalid),
.ba-14__f:has([aria-invalid="true"]) {
  --ring: var(--bad);
}

.ba-14__f:has(input:user-valid) {
  --ring: color-mix(in oklab,var(--good) 55%,var(--line));
}

.ba-14__ok {
  position: absolute;
  inset-inline-end: .9rem;
  inset-block-start: .95rem;
  width: 1.05rem;
  height: 1.05rem;
  color: var(--good);
  scale: 0;
  transition: scale .3s cubic-bezier(.34,1.56,.64,1);
}

.ba-14__f:has(input:user-valid) .ba-14__ok {
  scale: 1;
}

.ba-14__hint {
  margin: 0;
  font-size: .75rem;
  line-height: 1.5;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-14__msg {
  display: none;
  margin: 0;
  align-items: center;
  gap: .35rem;
  font-size: .75rem;
  font-weight: 600;
  line-height: 1.45;
  color: var(--bad);
}

.ba-14__msg::before {
  content: "⚠";
  font-size: .8125rem;
}

.ba-14__f:has(input:user-invalid) .ba-14__msg,
.ba-14__f:has([aria-invalid="true"]) .ba-14__msg {
  display: flex;
}

.ba-14__peek {
  position: absolute;
  inset-inline-end: .55rem;
  inset-block-start: .5rem;
  display: grid;
  place-items: center;
  width: 1.9rem;
  height: 1.9rem;
  border: 0;
  border-radius: .5rem;
  cursor: pointer;
  background: transparent;
  color: var(--muted);
}

.ba-14__peek:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.ba-14__peek svg {
  width: 1.05rem;
  height: 1.05rem;
}

.ba-14__peek[aria-pressed="true"] {
  color: var(--acc);
}

.ba-14__meter {
  display: grid;
  gap: .3rem;
}

.ba-14__mtrack {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .25rem;
}

.ba-14__mtrack span {
  height: .3rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 12%,transparent);
  transition: background .3s ease;
}

.ba-14__mtrack[data-score="1"] span:nth-child(-n+1) {
  background: var(--bad);
}

.ba-14__mtrack[data-score="2"] span:nth-child(-n+2) {
  background: var(--warn);
}

.ba-14__mtrack[data-score="3"] span:nth-child(-n+3) {
  background: color-mix(in oklab,var(--good) 75%,var(--warn));
}

.ba-14__mtrack[data-score="4"] span {
  background: var(--good);
}

.ba-14__mText {
  margin: 0;
  font-size: .75rem;
  color: var(--muted);
}

.ba-14__check {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .6rem;
  align-items: start;
  cursor: pointer;
  font-size: .8125rem;
  line-height: 1.55;
  font-weight: 400;
}

.ba-14__check input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.ba-14__box {
  display: grid;
  place-items: center;
  width: 1.2rem;
  height: 1.2rem;
  margin-block-start: .1rem;
  border-radius: .35rem;
  border: 1.5px solid var(--line);
  transition: background .2s ease, border-color .2s ease;
}

.ba-14__check input:checked + .ba-14__box {
  background: var(--acc);
  border-color: var(--acc);
}

.ba-14__check input:checked + .ba-14__box::after {
  content: "";
  width: .3rem;
  height: .55rem;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  rotate: 45deg;
  translate: 0 -1px;
}

.ba-14__check input:focus-visible + .ba-14__box {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-14__f:has(input[type="checkbox"]:user-invalid) .ba-14__box {
  border-color: var(--bad);
}

.ba-14__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding-block-start: .35rem;
}

.ba-14__submit {
  min-height: 3rem;
  padding: .85rem 1.6rem;
  border: 0;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-size: .9375rem;
  font-weight: 700;
  letter-spacing: -.01em;
  background: var(--acc);
  color: #fff;
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .2s ease, background .2s ease;
}

.ba-14__submit:hover {
  translate: 0 -1px;
  background: color-mix(in oklab,var(--acc) 88%,white);
  box-shadow: 0 .8rem 1.8rem -.9rem color-mix(in oklab,var(--acc) 70%,transparent);
}

.ba-14__footNote {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.ba-14__done {
  display: flex;
  align-items: center;
  gap: .85rem;
  padding: .9rem 1rem;
  border-radius: 1rem;
  color: color-mix(in oklab,var(--good) 80%,var(--ink));
  background: color-mix(in oklab,var(--good) 10%,var(--surface));
  border: 1px solid color-mix(in oklab,var(--good) 30%,transparent);
}

.ba-14__done[hidden] {
  display: none;
}

.ba-14__done span {
  display: grid;
  place-items: center;
  width: 2.25rem;
  height: 2.25rem;
  flex: none;
  border-radius: 999px;
  color: var(--good);
  background: color-mix(in oklab,var(--good) 16%,transparent);
}

.ba-14__done svg {
  width: 1.3rem;
  height: 1.3rem;
}

.ba-14__done p {
  margin: 0;
  font-size: .875rem;
  line-height: 1.5;
}

.ba-14__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-14__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-14 a {
  color: var(--acc);
}

.ba-14 a:hover {
  color: color-mix(in oklab,var(--acc) 70%,var(--ink));
}

.ba-14 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@container (max-width: 34rem) {
  .ba-14 {
    --cols: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-14 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-14__card,
    .ba-14__summary {
    border: 1px solid CanvasText;
  }

  .ba-14__submit {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-14');
  if (!root) return;
  const summary = root.querySelector('[data-summary]');
  const list = root.querySelector('[data-sumlist]');
  const live = root.querySelector('.ba-14__live');
  const fields = [...root.querySelectorAll('[data-field]')];

  const MESSAGES = {
    'Full name': 'enter your full name, at least two characters',
    'Work email': 'enter an address like [email protected]',
    'Password': 'use at least 12 characters',
    'Terms': 'accept the terms to continue',
  };

  // password strength
  const pw = root.querySelector('[data-pw]');
  const RULES = [
    ['12 or more characters', (v) => v.length >= 12],
    ['a number', (v) => /\d/.test(v)],
    ['a symbol', (v) => /[^\w\s]/.test(v)],
    ['upper and lower case', (v) => /[a-z]/.test(v) && /[A-Z]/.test(v)],
  ];
  const track = root.querySelector('[data-mtrack]');
  const mtext = root.querySelector('[data-mtext]');
  pw.addEventListener('input', () => {
    const v = pw.value;
    const missing = RULES.filter(([, t]) => !t(v)).map(([label]) => label);
    const score = RULES.length - missing.length;
    track.dataset.score = v ? score : 0;
    track.setAttribute('aria-valuenow', v ? score : 0);
    track.setAttribute('aria-valuetext', ['very weak', 'weak', 'fair', 'good', 'strong'][v ? score : 0]);
    mtext.textContent = !v ? 'Use 12+ characters with a number and a symbol.'
      : missing.length ? 'Still needs ' + missing.slice(0, 2).join(' and ') + '.'
      : 'Strong password.';
  });

  root.querySelector('[data-peek]').addEventListener('click', (e) => {
    const btn = e.currentTarget;
    const on = btn.getAttribute('aria-pressed') === 'false';
    btn.setAttribute('aria-pressed', String(on));
    pw.type = on ? 'text' : 'password';
    btn.querySelector('.ba-14__vh').textContent = on ? 'Hide password' : 'Show password';
  });

  const note = root.querySelector('[data-note]');
  note.addEventListener('input', () => { root.querySelector('[data-count]').textContent = note.value.length; });

  root.querySelector('[data-submit]').addEventListener('click', () => {
    const bad = fields.filter((f) => !f.checkValidity());
    fields.forEach((f) => f.toggleAttribute('aria-invalid', bad.includes(f)));
    list.replaceChildren();
    if (!bad.length) {
      summary.hidden = true;
      root.querySelector('[data-done]').hidden = false;
      live.textContent = 'Account created. Check your inbox for the verification link.';
      return;
    }
    bad.forEach((f) => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = '#' + (f.id || '');
      a.textContent = f.dataset.label + ': ' + (MESSAGES[f.dataset.label] || 'check this field');
      a.addEventListener('click', (e) => { e.preventDefault(); f.focus(); });
      li.append(a); list.append(li);
    });
    root.querySelector('[data-sumtitle]').textContent = 'There ' + (bad.length === 1 ? 'is 1 problem' : 'are ' + bad.length + ' problems') + ' with your details';
    summary.hidden = false;
    summary.setAttribute('role', 'alert');
    summary.focus();
  });
})();
```
