---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/neubrutalist-signup-form/"
title: "Neubrutalist Signup Form"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A centred signup card where the inputs carry the aesthetic: a 3px black edge that thickens to 4px on :focus-visible while the offset shadow shifts, so focus…"
has_js: "true"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neubrutalist Signup Form
Source: https://codefronts.com/design-styles/css-brutalist/neubrutalist-signup-form/

A centred signup card where the inputs carry the aesthetic: a 3px black edge that thickens to 4px on :focus-visible while the offset shadow shifts, so focus is felt as movement rather than a coloured glow. Validation is announced through aria-live, the tick is a pure-CSS chunky check, and there is no submit handler — Enter and click are wired directly, which is what keeps it working inside sandboxed playground iframes.
## HTML
```html
<div class="brt-03">
  <button class="brt-03__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="brt-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
  </button>

  <div class="brt-03__stage">
    <section class="brt-03__card" id="brt-03-card" aria-labelledby="brt-03-h">
      <p class="brt-03__kicker">Free 14-day trial</p>
      <h2 class="brt-03__h" id="brt-03-h">Create your workspace</h2>
      <p class="brt-03__lede">No card needed. Invite your team once you are in.</p>

      <div class="brt-03__row">
        <label class="brt-03__label" for="brt-03-name">Full name</label>
        <input class="brt-03__input" id="brt-03-name" name="name" type="text" autocomplete="name" placeholder="Priya Sharma" required aria-describedby="brt-03-name-err">
        <p class="brt-03__err" id="brt-03-name-err"></p>
      </div>

      <div class="brt-03__row">
        <label class="brt-03__label" for="brt-03-email">Work email</label>
        <input class="brt-03__input" id="brt-03-email" name="email" type="email" autocomplete="email" placeholder="[email protected]" required aria-describedby="brt-03-email-err">
        <p class="brt-03__err" id="brt-03-email-err"></p>
      </div>

      <div class="brt-03__row">
        <label class="brt-03__label" for="brt-03-pass">Password</label>
        <input class="brt-03__input" id="brt-03-pass" name="password" type="password" autocomplete="new-password" placeholder="8 characters or more" required minlength="8" aria-describedby="brt-03-pass-hint brt-03-pass-err">
        <div class="brt-03__meter" data-strength="0">
          <span class="brt-03__meterbar" aria-hidden="true"></span>
          <p class="brt-03__hint" id="brt-03-pass-hint">Strength: <b class="brt-03__strength">add 8+ characters</b></p>
        </div>
        <p class="brt-03__err" id="brt-03-pass-err"></p>
      </div>

      <label class="brt-03__check">
        <input class="brt-03__box" type="checkbox" id="brt-03-terms" aria-describedby="brt-03-terms-err">
        <span>Email me product updates. Two a month, never more.</span>
      </label>
      <p class="brt-03__err" id="brt-03-terms-err"></p>

      <button class="brt-03__submit" id="brt-03-go" type="button">Create workspace</button>
      <p class="brt-03__status" id="brt-03-status" role="status" aria-live="polite"></p>
      <p class="brt-03__alt">Already have an account? <a href="#brt-03-card">Sign in</a></p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-03 {
  --page: #fdf6ee;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --edge: #000000;
  --sh: #000000;
  --cta-sh: #fda4af;
  --bw: 3px;
  --r: 14px;
  --gap: 1.15rem;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-03 *,
.brt-03 *::before,
.brt-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-03 {
    --page: oklch(0.972 0.022 78);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
    --cta-sh: oklch(0.83 0.10 15);
  }
}

.brt-03__theme {
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
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-03__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-03__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-03__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-03__theme:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-03__sun {
  display: none;
}

.brt-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3rem);
}

.brt-03__card {
  inline-size: min(28rem,100%);
  padding: clamp(1.5rem,4vw,2.25rem);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 8px 8px 0 var(--sh);
}

.brt-03__kicker {
  display: inline-block;
  margin: 0 0 .85rem;
  padding: .3rem .6rem;
  background: var(--mint);
  color: var(--on);
  border: 2px solid var(--edge);
  border-radius: 7px;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.brt-03__h {
  margin: 0;
  font-size: clamp(1.6rem,4.4vw,2.1rem);
  font-weight: 700;
  letter-spacing: -.025em;
  line-height: 1.05;
  text-wrap: balance;
}

.brt-03__lede {
  margin: .5rem 0 1.5rem;
  font-size: .95rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.brt-03__row {
  display: grid;
  gap: .4rem;
  margin-block-end: var(--gap);
}

.brt-03__label {
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
}

.brt-03__row:has(:focus-visible) .brt-03__label {
  text-decoration: 3px underline var(--lilac);
  text-underline-offset: 3px;
}

.brt-03__input {
  inline-size: 100%;
  min-block-size: 2.9rem;
  padding: .7rem .85rem;
  font: inherit;
  font-size: 1rem;
  color: var(--ink);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  transition: translate .14s ease, box-shadow .14s ease, border-width .1s ease;
}

.brt-03__input::placeholder {
  color: var(--muted);
  opacity: .75;
}

.brt-03__input:hover {
  translate: -1px -1px;
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-03__input:focus-visible {
  outline: none;
  border-width: 4px;
  translate: -2px -2px;
  box-shadow: 6px 6px 0 var(--sh);
}

.brt-03__input:user-invalid,
.brt-03__input[data-invalid] {
  background: var(--coral);
  color: var(--on);
}

.brt-03__err {
  margin: 0;
  min-block-size: 0;
  font-size: .82rem;
  font-weight: 700;
  color: var(--ink);
}

.brt-03__err:not(:empty) {
  margin-block-start: .35rem;
  padding: .3rem .5rem;
  background: var(--coral);
  color: var(--on);
  border: 2px solid var(--edge);
  border-radius: 7px;
}

.brt-03__meter {
  margin-block-start: .5rem;
}

.brt-03__meterbar {
  display: block;
  block-size: .75rem;
  border: 2px solid var(--edge);
  border-radius: 6px;
  background: var(--page);
  overflow: hidden;
  position: relative;
}

.brt-03__meterbar::after {
  content: '';
  position: absolute;
  inset: 0;
  inline-size: 0;
  background: var(--coral);
  border-inline-end: 2px solid var(--edge);
  transition: inline-size .18s ease, background .18s ease;
}

.brt-03__meter[data-strength="1"] .brt-03__meterbar::after {
  inline-size: 34%;
  background: var(--coral);
}

.brt-03__meter[data-strength="2"] .brt-03__meterbar::after {
  inline-size: 67%;
  background: var(--butter);
}

.brt-03__meter[data-strength="3"] .brt-03__meterbar::after {
  inline-size: 100%;
  background: var(--mint);
  border-inline-end: 0;
}

.brt-03__hint {
  margin: .35rem 0 0;
  font-size: .78rem;
  color: var(--muted);
}

.brt-03__hint b {
  color: var(--ink);
}

.brt-03__check {
  display: grid;
  grid-template-columns: 1.6rem 1fr;
  gap: .7rem;
  align-items: start;
  min-block-size: 2.75rem;
  align-content: center;
  font-size: .9rem;
  line-height: 1.4;
  cursor: pointer;
  color: var(--ink);
}

.brt-03__box {
  appearance: none;
  -webkit-appearance: none;
  margin: 0;
  inline-size: 1.6rem;
  block-size: 1.6rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  cursor: pointer;
  border: var(--bw) solid var(--edge);
  border-radius: 6px;
  box-shadow: 3px 3px 0 var(--sh);
  transition: translate .12s ease, box-shadow .12s ease, background .12s ease;
}

.brt-03__box::after {
  content: '';
  inline-size: .5rem;
  block-size: .9rem;
  border: solid var(--on);
  border-width: 0 4px 4px 0;
  rotate: 45deg;
  translate: 0 -2px;
  opacity: 0;
  transition: opacity .12s ease;
}

.brt-03__box:checked {
  background: var(--mint);
}

.brt-03__box:checked::after {
  opacity: 1;
}

.brt-03__box:active {
  translate: 2px 2px;
  box-shadow: 1px 1px 0 var(--sh);
}

.brt-03__box:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-03__submit {
  inline-size: 100%;
  margin-block-start: 1.4rem;
  min-block-size: 3rem;
  padding: .85rem 1rem;
  font: inherit;
  font-size: 1.02rem;
  font-weight: 700;
  cursor: pointer;
  background: var(--ink);
  color: var(--page);
  border: var(--bw) solid var(--edge);
  border-radius: 11px;
  box-shadow: 5px 5px 0 var(--cta-sh);
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-03__submit:hover {
  translate: -1px -1px;
  box-shadow: 7px 7px 0 var(--cta-sh);
}

.brt-03__submit:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--cta-sh);
}

.brt-03__submit:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-03__submit[aria-busy="true"] {
  opacity: .75;
  cursor: progress;
}

.brt-03__status {
  margin: .8rem 0 0;
  min-block-size: 1.2rem;
  font-size: .85rem;
  font-weight: 700;
}

.brt-03__status[data-ok="true"] {
  padding: .45rem .6rem;
  background: var(--mint);
  color: var(--on);
  border: 2px solid var(--edge);
  border-radius: 8px;
}

.brt-03__alt {
  margin: 1rem 0 0;
  font-size: .88rem;
  color: var(--muted);
  text-align: center;
}

.brt-03__alt a {
  color: var(--ink);
  font-weight: 700;
  text-decoration: 3px underline var(--lilac);
  text-underline-offset: 3px;
}

.brt-03__alt a:hover {
  background: var(--lilac);
  color: var(--on);
}

.brt-03__alt a:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 2px;
}

.brt-03[data-theme="dark"] {
  --page: #131218;
  --panel: #201e28;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-03[data-theme="dark"] .brt-03__moon {
  display: none;
}

.brt-03[data-theme="dark"] .brt-03__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-03:not([data-theme="light"]) {
    --page: #131218;
    --panel: #201e28;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-03:not([data-theme="light"]) .brt-03__moon {
    display: none;
  }

  .brt-03:not([data-theme="light"]) .brt-03__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-03 *,
    .brt-03 *::before,
    .brt-03 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-03__card,
    .brt-03__input,
    .brt-03__submit,
    .brt-03__box,
    .brt-03__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-03__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.brt-03');
  if (!root) return;
  const card = root.querySelector('#brt-03-card');
  const status = root.querySelector('#brt-03-status');
  const go = root.querySelector('#brt-03-go');
  const pass = root.querySelector('#brt-03-pass');
  const meter = root.querySelector('.brt-03__meter');
  const strength = root.querySelector('.brt-03__strength');
  const rules = [
    ['#brt-03-name', '#brt-03-name-err', (v) => v.trim().length > 1 || 'Tell us the name on the account.'],
    ['#brt-03-email', '#brt-03-email-err', (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) || 'That email address is missing something.'],
    ['#brt-03-pass', '#brt-03-pass-err', (v) => v.length >= 8 || 'Use at least 8 characters.'],
  ];

  const grade = (v) => (v.length >= 12 && /[^a-z0-9]/i.test(v) ? 3 : v.length >= 8 ? 2 : v.length ? 1 : 0);
  const words = ['add 8+ characters', 'too short', 'good', 'strong'];
  pass.addEventListener('input', () => {
    const g = grade(pass.value);
    meter.dataset.strength = String(g);
    strength.textContent = words[g];
  });

  const check = () => {
    let bad = 0;
    for (const [sel, errSel, test] of rules) {
      const el = root.querySelector(sel), err = root.querySelector(errSel);
      const res = test(el.value);
      const ok = res === true;
      err.textContent = ok ? '' : res;
      el.toggleAttribute('data-invalid', !ok);
      el.setAttribute('aria-invalid', String(!ok));
      if (!ok) { bad++; if (bad === 1) el.focus(); }
    }
    return bad;
  };

  const submit = () => {
    const bad = check();
    status.dataset.ok = String(bad === 0);
    if (bad) { status.textContent = bad + (bad === 1 ? ' field needs a fix.' : ' fields need a fix.'); return; }
    go.setAttribute('aria-busy', 'true');
    status.textContent = 'Creating your workspace…';
    setTimeout(() => { go.removeAttribute('aria-busy'); status.textContent = 'Workspace ready — check your inbox to confirm.'; }, 900);
  };

  go.addEventListener('click', submit);
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.target.matches('input:not([type="checkbox"])')) { e.preventDefault(); submit(); }
  });
})();

(() => {                                     /* theme toggle */
  const root = document.querySelector('.brt-03');
  const btn = root && root.querySelector('.brt-03__theme');
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
