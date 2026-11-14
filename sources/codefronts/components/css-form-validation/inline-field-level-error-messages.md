---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/inline-field-level-error-messages/"
title: "Inline Field Level Error Messages"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "The error message sits directly under its input and animates open without a magic max-height."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Field Level Error Messages
Source: https://codefronts.com/components/css-form-validation/inline-field-level-error-messages/

The error message sits directly under its input and animates open without a magic max-height. A grid-template-rows transition from 0fr to 1fr lets the message take its natural height, and the row is reserved in layout so revealing it never pushes the rest of the form down. Driven entirely by :user-invalid — no script, no class toggling.
## HTML
```html
<section class="fv-03" aria-labelledby="fv-03-h">
  <fieldset class="fv-03__theme">
    <legend class="fv-03__themelegend">Theme</legend>
    <input class="fv-03__themeinput" type="radio" name="fv-03-theme" id="fv-03-theme-auto" checked>
    <label class="fv-03__themeopt" for="fv-03-theme-auto">Auto</label>
    <input class="fv-03__themeinput" type="radio" name="fv-03-theme" id="fv-03-theme-light">
    <label class="fv-03__themeopt" for="fv-03-theme-light">Light</label>
    <input class="fv-03__themeinput" type="radio" name="fv-03-theme" id="fv-03-theme-dark">
    <label class="fv-03__themeopt" for="fv-03-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-03__stage">
    <form class="fv-03__card" aria-labelledby="fv-03-h">
      <header class="fv-03__head">
        <p class="fv-03__eyebrow">Basalt · transfer request</p>
        <h2 class="fv-03__h" id="fv-03-h">The message grows into space that was already reserved</h2>
      </header>

      <div class="fv-03__field">
        <label class="fv-03__label" for="fv-03-acct">Recipient account</label>
        <input class="fv-03__input" id="fv-03-acct" name="fv-03-acct" type="text" required pattern="[0-9]{8}" inputmode="numeric" placeholder="8 digits" aria-describedby="fv-03-acct-msg">
        <div class="fv-03__msgwrap">
          <p class="fv-03__msg" id="fv-03-acct-msg">
            <svg class="fv-03__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 2.6 18 17H2Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path><path d="M10 8v3.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.4" r="1" fill="currentColor"></circle></svg>
            <span>Account numbers are exactly 8 digits with no spaces or dashes</span>
          </p>
        </div>
      </div>

      <div class="fv-03__field">
        <label class="fv-03__label" for="fv-03-ref">Payment reference</label>
        <input class="fv-03__input" id="fv-03-ref" name="fv-03-ref" type="text" required minlength="4" maxlength="18" placeholder="INV-2026-0431" aria-describedby="fv-03-ref-msg">
        <div class="fv-03__msgwrap">
          <p class="fv-03__msg" id="fv-03-ref-msg">
            <svg class="fv-03__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 2.6 18 17H2Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path><path d="M10 8v3.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.4" r="1" fill="currentColor"></circle></svg>
            <span>Use at least 4 characters so the recipient can match the payment</span>
          </p>
        </div>
      </div>

      <div class="fv-03__field">
        <label class="fv-03__label" for="fv-03-amount">Amount</label>
        <input class="fv-03__input" id="fv-03-amount" name="fv-03-amount" type="number" required min="1" max="25000" step="0.01" placeholder="1200.00" aria-describedby="fv-03-amount-msg">
        <div class="fv-03__msgwrap">
          <p class="fv-03__msg" id="fv-03-amount-msg">
            <svg class="fv-03__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 2.6 18 17H2Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path><path d="M10 8v3.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.4" r="1" fill="currentColor"></circle></svg>
            <span>Single transfers run from 1.00 to 25,000.00 — split anything larger</span>
          </p>
        </div>
      </div>

      <div class="fv-03__foot">
        <button class="fv-03__btn" type="button">Review transfer</button>
        <p class="fv-03__footnote">Rows stay put. Only the message row changes height.</p>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-03 {
  --page: #070b18;
  --surface: #0d1329;
  --well: #080d1f;
  --ink: #e9edfa;
  --muted: #8e98bb;
  --rule: #1d2646;
  --accent: #4f7cff;
  --error: #ff5c7a;
  --error-ink: #ff92a6;
  --error-bg: #1e0f1c;
  --inset: inset 0 1px 0 rgba(0, 0, 0, 0.5);
  --font-display: "Archivo Narrow", "Avenir Next Condensed", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-03 {
    --accent: oklch(0.62 0.19 265);
    --error: oklch(0.66 0.2 12);
    --error-ink: oklch(0.76 0.16 12);
  }
}

@supports (interpolate-size: allow-keywords) {
  .fv-03 {
    interpolate-size: allow-keywords;
  }
}

.fv-03 *,
.fv-03 *::before,
.fv-03 *::after {
  box-sizing: border-box;
}

.fv-03__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2rem);
  background-image: radial-gradient(120% 80% at 50% 0%, #10193a 0%, transparent 62%);
}

.fv-03__card {
  inline-size: min(100%, 30rem);
  min-inline-size: 0;
  display: grid;
  gap: 1.125rem;
  padding: clamp(1.25rem, 4vw, 2rem);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 1rem;
}

.fv-03__head {
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
}

.fv-03__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-03__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 3.6vw, 1.6rem);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: 0.005em;
  text-wrap: balance;
}

.fv-03__field {
  display: grid;
  gap: 0.4375rem;
  min-inline-size: 0;
  min-block-size: 5.75rem;
  align-content: start;
}

.fv-03__label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-03__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.875rem;
  padding: 0 0.875rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: var(--well);
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  box-shadow: var(--inset);
  transition: border-color 0.18s ease, box-shadow 0.18s ease;
}

.fv-03__input::placeholder {
  color: #5a6588;
}

.fv-03__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-03__msgwrap {
  display: grid;
  grid-template-rows: 0fr;
  overflow: clip;
  transition: grid-template-rows 0.24s cubic-bezier(0.32, 0.72, 0, 1);
}

.fv-03__msg {
  display: flex;
  gap: 0.4375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  padding-block-start: 0.125rem;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--error-ink);
  opacity: 0;
  transition: opacity 0.2s ease 0.04s;
}

.fv-03__msg span {
  min-inline-size: 0;
}

.fv-03__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-03__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  background: var(--error-bg);
}

.fv-03__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-03__msgwrap {
  grid-template-rows: 1fr;
}

.fv-03__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-03__msgwrap .fv-03__msg {
  opacity: 1;
}

.fv-03__input:user-invalid {
  border-color: var(--error);
  background: var(--error-bg);
}

.fv-03__input:user-invalid ~ .fv-03__msgwrap {
  grid-template-rows: 1fr;
}

.fv-03__input:user-invalid ~ .fv-03__msgwrap .fv-03__msg {
  opacity: 1;
}

.fv-03__input:user-valid {
  border-color: #2f9e6f;
}

.fv-03__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1rem;
  min-inline-size: 0;
}

.fv-03__btn {
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  padding: 0.6875rem 1.375rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #06102b;
  background: var(--accent);
  border: 0;
  border-radius: 0.5rem;
  cursor: pointer;
}

.fv-03__btn:focus-visible {
  outline: 2px solid #ffffff;
  outline-offset: 3px;
}

.fv-03__footnote {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.4;
  color: var(--muted);
}

@supports (interpolate-size: allow-keywords) {
  .fv-03__msgwrap {
    grid-template-rows: none;
    block-size: 0;
    transition: block-size 0.24s cubic-bezier(0.32, 0.72, 0, 1);
  }

  .fv-03__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-03__msgwrap,
    .fv-03__input:user-invalid ~ .fv-03__msgwrap {
    block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fv-03__msgwrap,
    .fv-03__msg,
    .fv-03__input {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .fv-03:not(:has(#fv-03-theme-dark:checked)) {
    --page: #eef1f8;
    --surface: #ffffff;
    --well: #f7f8fc;
    --ink: #101736;
    --muted: #5b6484;
    --rule: #d8deee;
    --error-bg: #fdf1f3;
    --error-ink: #a81330;
    --inset: inset 0 1px 0 rgba(16, 23, 54, 0.06);
  }

  .fv-03:not(:has(#fv-03-theme-dark:checked)) .fv-03__stage {
    background-image: radial-gradient(120% 80% at 50% 0%, #e2e8f8 0%, transparent 62%);
  }

  .fv-03:not(:has(#fv-03-theme-dark:checked)) .fv-03__input::placeholder {
    color: #98a1bd;
  }

  .fv-03:not(:has(#fv-03-theme-dark:checked)) .fv-03__btn {
    color: #ffffff;
  }
}

[data-theme="dark"] .fv-03:not(:has(#fv-03-theme-light:checked)) {
  --page: #070b18;
  --surface: #0d1329;
  --well: #080d1f;
  --ink: #e9edfa;
  --muted: #8e98bb;
  --rule: #1d2646;
  --error-bg: #1e0f1c;
  --error-ink: #ff92a6;
}

[data-theme="dark"] .fv-03:not(:has(#fv-03-theme-light:checked)) .fv-03__btn {
  color: #06102b;
}

.fv-03 {
  position: relative;
}

.fv-03__stage {
  padding-block-start: 4.75rem;
}

.fv-03__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 7%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.fv-03__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-03__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-03__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 1.875rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.fv-03__themeopt:hover {
  opacity: 0.85;
}

.fv-03__themeinput:checked + .fv-03__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-03__themeinput:focus-visible + .fv-03__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-03__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-03__themeinput:checked + .fv-03__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-03:has(#fv-03-theme-light:checked) {
  --page: #eef1f8;
  --surface: #ffffff;
  --well: #f7f8fc;
  --ink: #101736;
  --muted: #5b6484;
  --rule: #d8deee;
  --error-bg: #fdf1f3;
  --error-ink: #a81330;
  --inset: inset 0 1px 0 rgba(16, 23, 54, 0.06);
}

.fv-03:has(#fv-03-theme-light:checked) .fv-03__stage {
  background-image: radial-gradient(120% 80% at 50% 0%, #e2e8f8 0%, transparent 62%);
}

.fv-03:has(#fv-03-theme-light:checked) .fv-03__input::placeholder {
  color: #98a1bd;
}

.fv-03:has(#fv-03-theme-light:checked) .fv-03__btn {
  color: #ffffff;
}
```
