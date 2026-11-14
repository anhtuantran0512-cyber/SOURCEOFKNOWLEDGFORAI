---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/password-strength-meter-with-live-feedback/"
title: "Password Strength Meter with Live Feedback"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "A four-segment strength meter that grades as you type, with a live requirement checklist beside it and a status line linked to the input through…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Password Strength Meter with Live Feedback
Source: https://codefronts.com/components/css-progress-bars/password-strength-meter-with-live-feedback/

A four-segment strength meter that grades as you type, with a live requirement checklist beside it and a status line linked to the input through aria-describedby. Colour carries the grade, but so does the word — never colour alone.
## HTML
```html
<div class="pb-06">
  <button class="pb-06__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-06__stage">
    <div class="pb-06__card">
      <header class="pb-06__head">
        <p class="pb-06__eyebrow"><span class="pb-06__step pb-06__mono">Step 2 of 3</span>Create your account</p>
        <h2 class="pb-06__title">Choose a password</h2>
        <p class="pb-06__lead">Signing up as <strong>[email protected]</strong></p>
      </header>

      <div class="pb-06__field">
        <label class="pb-06__label" for="pb-06-pw">Password</label>
        <span class="pb-06__inputWrap">
          <input class="pb-06__input" id="pb-06-pw" type="password" value="Migration2027" autocomplete="new-password" spellcheck="false" aria-describedby="pb-06-status pb-06-rules" placeholder="At least 8 characters">
          <button class="pb-06__eye" type="button" id="pb-06-eye" aria-pressed="false" aria-label="Show password">
            <svg class="pb-06__eyeOn" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M2.8 12S6.4 5.8 12 5.8 21.2 12 21.2 12 17.6 18.2 12 18.2 2.8 12 2.8 12Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="12" cy="12" r="2.9" stroke="currentColor" stroke-width="1.7"/></svg>
            <svg class="pb-06__eyeOff" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.2 4.2l15.6 15.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M9.6 6.3A8.6 8.6 0 0 1 12 6c5.6 0 9.2 6 9.2 6a17 17 0 0 1-2.6 3.4M6.8 8A17 17 0 0 0 2.8 12s3.6 6 9.2 6a8.7 8.7 0 0 0 3.1-.55" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </button>
        </span>
      </div>

      <div class="pb-06__grid">
        <div class="pb-06__meterBox">
          <div class="pb-06__meter" id="pb-06-meter" data-score="2" role="progressbar" aria-valuenow="2" aria-valuemin="0" aria-valuemax="4" aria-valuetext="Fair" aria-label="Password strength">
            <span class="pb-06__seg"></span><span class="pb-06__seg"></span><span class="pb-06__seg"></span><span class="pb-06__seg"></span>
          </div>
          <p class="pb-06__status" id="pb-06-status" role="status" aria-live="polite"><span class="pb-06__grade" id="pb-06-grade">Fair</span><span class="pb-06__advice" id="pb-06-advice">Add a number and a symbol</span></p>
        </div>

        <ul class="pb-06__rules" id="pb-06-rules">
          <li data-rule="len" data-pass="true"><span class="pb-06__glyph" aria-hidden="true"><svg class="pb-06__yes" viewBox="0 0 24 24" fill="none"><path d="M5.5 12.6l4 4L18.5 7.6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><svg class="pb-06__no" viewBox="0 0 24 24" fill="none"><path d="M7 7l10 10M17 7L7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></span>8+ characters</li>
          <li data-rule="case" data-pass="true"><span class="pb-06__glyph" aria-hidden="true"><svg class="pb-06__yes" viewBox="0 0 24 24" fill="none"><path d="M5.5 12.6l4 4L18.5 7.6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><svg class="pb-06__no" viewBox="0 0 24 24" fill="none"><path d="M7 7l10 10M17 7L7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></span>Upper and lower case</li>
          <li data-rule="digit" data-pass="false"><span class="pb-06__glyph" aria-hidden="true"><svg class="pb-06__yes" viewBox="0 0 24 24" fill="none"><path d="M5.5 12.6l4 4L18.5 7.6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><svg class="pb-06__no" viewBox="0 0 24 24" fill="none"><path d="M7 7l10 10M17 7L7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></span>A number</li>
          <li data-rule="sym" data-pass="false"><span class="pb-06__glyph" aria-hidden="true"><svg class="pb-06__yes" viewBox="0 0 24 24" fill="none"><path d="M5.5 12.6l4 4L18.5 7.6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><svg class="pb-06__no" viewBox="0 0 24 24" fill="none"><path d="M7 7l10 10M17 7L7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></span>A symbol</li>
        </ul>
      </div>

      <button class="pb-06__submit" type="button" id="pb-06-submit">Continue to payment</button>
      <p class="pb-06__foot">Press <kbd>Enter</kbd> in the field to continue. Nothing is sent anywhere.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-06 {
  --bg: #f4f5f9;
  --card: #ffffff;
  --card2: #f8f9fc;
  --ink: #0b1020;
  --muted: rgba(11,16,32,.6);
  --line: rgba(11,16,32,.1);
  --track: rgba(11,16,32,.08);
  --accent: #2563eb;
  --weak: #ef4444;
  --fair: #f59e0b;
  --good: #eab308;
  --strong: #10b981;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(70% .18 260)) {
  .pb-06 {
    --accent: oklch(58% .19 258);
    --weak: oklch(63% .21 25);
    --fair: oklch(75% .16 65);
    --good: oklch(82% .16 92);
    --strong: oklch(70% .16 162);
  }
}

.pb-06 *,
.pb-06 *::before,
.pb-06 *::after {
  box-sizing: border-box;
}

.pb-06__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(80% 60% at 10% 0%,color-mix(in srgb,var(--accent) 12%,transparent),transparent 58%), radial-gradient(70% 60% at 95% 100%,color-mix(in srgb,var(--strong) 10%,transparent),transparent 60%);
}

.pb-06__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(11,16,32,.05);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-06__theme:hover {
  transform: translateY(-1px);
}

.pb-06__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-06__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-06__sun {
  display: block;
}

.pb-06__moon {
  display: none;
}

.pb-06__card {
  inline-size: min(40rem,100%);
  display: grid;
  gap: clamp(1rem,2.3vw,1.5rem);
  padding: clamp(1.4rem,3.4vw,2.4rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: var(--card);
  box-shadow: 0 1px 2px rgba(11,16,32,.05),0 30px 60px -40px rgba(11,16,32,.45);
}

.pb-06__head {
  display: grid;
  gap: .4rem;
}

.pb-06__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .6rem;
  font-size: .85rem;
  color: var(--muted);
}

.pb-06__step {
  padding: .25rem .5rem;
  border-radius: .4rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 10%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 26%,transparent);
}

.pb-06__mono {
  font-family: var(--mono);
  font-size: .72rem;
  font-variant-numeric: tabular-nums;
}

.pb-06__title {
  margin: 0;
  font-size: clamp(1.4rem,3.3vw,2rem);
  line-height: 1.14;
  letter-spacing: -.022em;
  font-weight: 650;
}

.pb-06__lead {
  margin: 0;
  font-size: .9rem;
  color: var(--muted);
}

.pb-06__lead strong {
  color: var(--ink);
  font-weight: 600;
}

.pb-06__field {
  display: grid;
  gap: .4rem;
}

.pb-06__label {
  font-size: .82rem;
  font-weight: 600;
}

.pb-06__inputWrap {
  position: relative;
  display: block;
}

.pb-06__input {
  inline-size: 100%;
  min-block-size: 3rem;
  padding: .85rem 3.2rem .85rem 1rem;
  border-radius: .9rem;
  border: 1px solid var(--line);
  background: var(--card2);
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  letter-spacing: .02em;
  transition: border-color .18s,box-shadow .18s;
}

.pb-06__input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in srgb,var(--accent) 22%,transparent);
}

.pb-06__eye {
  position: absolute;
  inset-block: .3rem;
  inset-inline-end: .35rem;
  inline-size: 2.4rem;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: .7rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s,color .18s;
}

.pb-06__eye:hover {
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
}

.pb-06__eye:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.pb-06__eye svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.pb-06__eyeOff {
  display: none;
}

.pb-06__eye[aria-pressed="true"] .pb-06__eyeOn {
  display: none;
}

.pb-06__eye[aria-pressed="true"] .pb-06__eyeOff {
  display: block;
}

.pb-06__grid {
  display: grid;
  grid-template-columns: minmax(12rem,1fr) auto;
  gap: clamp(.9rem,2.4vw,1.6rem);
  align-items: start;
}

.pb-06__meterBox {
  display: grid;
  gap: .55rem;
}

.pb-06__meter {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .35rem;
}

.pb-06__seg {
  block-size: .55rem;
  border-radius: 99px;
  background: var(--track);
  transition: background .3s cubic-bezier(.4,0,.2,1);
}

.pb-06__meter[data-score="1"] {
  --fill: var(--weak);
}

.pb-06__meter[data-score="2"] {
  --fill: var(--fair);
}

.pb-06__meter[data-score="3"] {
  --fill: var(--good);
}

.pb-06__meter[data-score="4"] {
  --fill: var(--strong);
}

.pb-06__meter[data-score="1"] .pb-06__seg:nth-child(-n+1),
.pb-06__meter[data-score="2"] .pb-06__seg:nth-child(-n+2),
.pb-06__meter[data-score="3"] .pb-06__seg:nth-child(-n+3),
.pb-06__meter[data-score="4"] .pb-06__seg:nth-child(-n+4) {
  background: var(--fill);
}

.pb-06__meter[data-score="4"] .pb-06__seg {
  box-shadow: 0 0 0 1px color-mix(in srgb,var(--strong) 30%,transparent);
}

.pb-06__status {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: baseline;
  font-size: .85rem;
}

.pb-06__grade {
  font-weight: 650;
}

.pb-06__meter[data-score="0"] ~ .pb-06__status .pb-06__grade,
.pb-06__meter[data-score="1"] ~ .pb-06__status .pb-06__grade {
  color: var(--weak);
}

.pb-06__meter[data-score="2"] ~ .pb-06__status .pb-06__grade {
  color: var(--fair);
}

.pb-06__meter[data-score="3"] ~ .pb-06__status .pb-06__grade {
  color: color-mix(in srgb,var(--good) 78%,var(--ink));
}

.pb-06__meter[data-score="4"] ~ .pb-06__status .pb-06__grade {
  color: var(--strong);
}

.pb-06__advice {
  color: var(--muted);
}

.pb-06__rules {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .35rem;
}

.pb-06__rules li {
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .85rem;
  color: var(--muted);
}

.pb-06__rules li[data-pass="true"] {
  color: var(--ink);
}

.pb-06__glyph {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  display: grid;
  place-items: center;
  flex: none;
}

.pb-06__glyph svg {
  inline-size: .95rem;
  block-size: .95rem;
  grid-area: 1/1;
}

.pb-06__yes {
  color: var(--strong);
  display: none;
}

.pb-06__no {
  color: color-mix(in srgb,var(--ink) 35%,transparent);
}

.pb-06__rules li[data-pass="true"] .pb-06__yes {
  display: block;
}

.pb-06__rules li[data-pass="true"] .pb-06__no {
  display: none;
}

.pb-06__submit {
  min-block-size: 3rem;
  padding: .85rem 1.2rem;
  border-radius: .9rem;
  border: 1px solid transparent;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: .95rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform .18s,background .18s;
  box-shadow: 0 14px 30px -18px var(--accent);
}

.pb-06__submit:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--accent) 88%,black);
}

.pb-06__submit:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.pb-06__foot {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
}

.pb-06__foot kbd {
  font-family: var(--mono);
  font-size: .72rem;
  padding: .1rem .35rem;
  border-radius: .3rem;
  border: 1px solid var(--line);
  background: var(--card2);
}

.pb-06[data-theme="dark"] {
  --bg: #080b12;
  --card: #0d121d;
  --card2: #111825;
  --ink: #e9eefa;
  --muted: rgba(233,238,250,.6);
  --line: rgba(233,238,250,.12);
  --track: rgba(233,238,250,.09);
  --accent: #60a5fa;
}

.pb-06[data-theme="dark"] .pb-06__theme {
  background: rgba(255,255,255,.07);
}

.pb-06[data-theme="dark"] .pb-06__sun {
  display: none;
}

.pb-06[data-theme="dark"] .pb-06__moon {
  display: block;
}

.pb-06[data-theme="dark"] .pb-06__submit {
  color: #08111f;
}

@media (prefers-color-scheme: dark) {
  .pb-06:not([data-theme="light"]) {
    --bg: #080b12;
    --card: #0d121d;
    --card2: #111825;
    --ink: #e9eefa;
    --muted: rgba(233,238,250,.6);
    --line: rgba(233,238,250,.12);
    --track: rgba(233,238,250,.09);
    --accent: #60a5fa;
  }

  .pb-06:not([data-theme="light"]) .pb-06__theme {
    background: rgba(255,255,255,.07);
  }

  .pb-06:not([data-theme="light"]) .pb-06__sun {
    display: none;
  }

  .pb-06:not([data-theme="light"]) .pb-06__moon {
    display: block;
  }

  .pb-06:not([data-theme="light"]) .pb-06__submit {
    color: #08111f;
  }
}

@media (max-width: 34rem) {
  .pb-06__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-06 *,
    .pb-06 *::before,
    .pb-06 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-06__card,
    .pb-06__input,
    .pb-06__submit,
    .pb-06__theme,
    .pb-06__seg {
    border: 1px solid CanvasText;
    box-shadow: none;
  }

  .pb-06__meter[data-score] .pb-06__seg {
    background: Canvas;
  }

  .pb-06__meter[data-score="1"] .pb-06__seg:nth-child(-n+1),
    .pb-06__meter[data-score="2"] .pb-06__seg:nth-child(-n+2),
    .pb-06__meter[data-score="3"] .pb-06__seg:nth-child(-n+3),
    .pb-06__meter[data-score="4"] .pb-06__seg:nth-child(-n+4) {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb06 = document.querySelector('.pb-06');
if (pb06) {
  const q = (s) => pb06.querySelector(s);
  const [input, meter, grade, advice, submit] = ['#pb-06-pw','#pb-06-meter','#pb-06-grade','#pb-06-advice','#pb-06-submit'].map(q);
  const rules = { len: (v) => v.length >= 8, case: (v) => /[a-z]/.test(v) && /[A-Z]/.test(v), digit: (v) => /\d/.test(v), sym: (v) => /[^A-Za-z0-9]/.test(v) };
  const LABEL = ['Too short', 'Weak', 'Fair', 'Good', 'Strong'];
  const NEED = { len: 'at least 8 characters', case: 'upper and lower case', digit: 'a number', sym: 'a symbol' };
  const grade_ = () => {
    const v = input.value, missing = [];
    let score = 0;
    for (const [key, fn] of Object.entries(rules)) {
      const pass = fn(v); if (pass) score += 1; else missing.push(NEED[key]);
      pb06.querySelector('[data-rule="' + key + '"]').dataset.pass = String(pass);
    }
    meter.dataset.score = score;
    meter.setAttribute('aria-valuenow', score);
    meter.setAttribute('aria-valuetext', LABEL[score]);
    grade.textContent = LABEL[score];
    advice.textContent = missing.length ? 'Add ' + missing.slice(0, 2).join(' and ') : 'Ready to continue';
  };
  input.addEventListener('input', grade_);
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); submit.click(); } });
  submit.addEventListener('click', () => { advice.textContent = Number(meter.dataset.score) >= 3 ? 'Saved — continuing to payment' : 'Strengthen the password first'; });
  q('#pb-06-eye').addEventListener('click', (e) => {
    const show = e.currentTarget.getAttribute('aria-pressed') === 'false';
    e.currentTarget.setAttribute('aria-pressed', String(show));
    e.currentTarget.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
    input.type = show ? 'text' : 'password';
  });
  q('.pb-06__theme').addEventListener('click', (e) => {
    const dark = pb06.dataset.theme !== 'dark';
    pb06.dataset.theme = dark ? 'dark' : 'light';
    e.currentTarget.setAttribute('aria-pressed', String(dark));
  });
  grade_();
}
```
