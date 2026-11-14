---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/required-field-indicator-and-legend/"
title: "Required Field Indicator and Legend"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "Required and optional marking done properly."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Required Field Indicator and Legend
Source: https://codefronts.com/components/css-form-validation/required-field-indicator-and-legend/

Required and optional marking done properly. The asterisk is decorative and carries aria-hidden="true", the real signal lives in the field's accessible name, and a legend explains the convention once at the top instead of leaving users to guess. A second panel shows the inverse convention — marking the optional fields — which reads better when nearly every field is mandatory.
## HTML
```html
<section class="fv-02" aria-labelledby="fv-02-h">
  <fieldset class="fv-02__theme">
    <legend class="fv-02__themelegend">Theme</legend>
    <input class="fv-02__themeinput" type="radio" name="fv-02-theme" id="fv-02-theme-auto" checked>
    <label class="fv-02__themeopt" for="fv-02-theme-auto">Auto</label>
    <input class="fv-02__themeinput" type="radio" name="fv-02-theme" id="fv-02-theme-light">
    <label class="fv-02__themeopt" for="fv-02-theme-light">Light</label>
    <input class="fv-02__themeinput" type="radio" name="fv-02-theme" id="fv-02-theme-dark">
    <label class="fv-02__themeopt" for="fv-02-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-02__stage">
    <header class="fv-02__head">
      <h2 class="fv-02__h" id="fv-02-h">Mark the exception, explain the key</h2>
      <p class="fv-02__sub">Two conventions, one rule: whichever you choose, say so once at the top and let the markup generate the markers.</p>
    </header>

    <div class="fv-02__grid">
      <form class="fv-02__card" data-convention="required" aria-labelledby="fv-02-lg-a">
        <fieldset class="fv-02__set">
          <legend class="fv-02__legend" id="fv-02-lg-a">
            <span class="fv-02__legendtitle">Vale account request</span>
            <span class="fv-02__key"><span class="fv-02__keymark" aria-hidden="true">*</span> marks a required field</span>
          </legend>

          <div class="fv-02__field">
            <label class="fv-02__label" for="fv-02-name">Full name<span class="fv-02__sr"> (required)</span></label>
            <input class="fv-02__input" id="fv-02-name" name="fv-02-name" type="text" required autocomplete="name" placeholder="Priya Sharma" aria-describedby="fv-02-name-msg">
            <p class="fv-02__msg" id="fv-02-name-msg">
              <svg class="fv-02__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
              <span>Enter the name as it appears on your Vale invoice</span>
            </p>
          </div>

          <div class="fv-02__field">
            <label class="fv-02__label" for="fv-02-email">Work email<span class="fv-02__sr"> (required)</span></label>
            <input class="fv-02__input" id="fv-02-email" name="fv-02-email" type="email" required autocomplete="email" placeholder="[email protected]" aria-describedby="fv-02-email-msg">
            <p class="fv-02__msg" id="fv-02-email-msg">
              <svg class="fv-02__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
              <span>Enter a valid email address, like [email protected]</span>
            </p>
          </div>

          <div class="fv-02__field">
            <label class="fv-02__label" for="fv-02-phone">Phone</label>
            <input class="fv-02__input" id="fv-02-phone" name="fv-02-phone" type="tel" autocomplete="tel" placeholder="+44 20 7946 0102">
            <p class="fv-02__hint">Only used if we need to confirm a billing change.</p>
          </div>

          <button class="fv-02__btn" type="button">Request access</button>
        </fieldset>
      </form>

      <form class="fv-02__card fv-02__card--alt" data-convention="optional" aria-labelledby="fv-02-lg-b">
        <fieldset class="fv-02__set">
          <legend class="fv-02__legend" id="fv-02-lg-b">
            <span class="fv-02__legendtitle">Vale payout details</span>
            <span class="fv-02__key">All fields are required unless tagged <span class="fv-02__keypill">Optional</span></span>
          </legend>

          <div class="fv-02__field">
            <label class="fv-02__label" for="fv-02-legal">Legal entity<span class="fv-02__sr"> (required)</span></label>
            <input class="fv-02__input" id="fv-02-legal" name="fv-02-legal" type="text" required autocomplete="organization" placeholder="Vale Instruments Ltd" aria-describedby="fv-02-legal-msg">
            <p class="fv-02__msg" id="fv-02-legal-msg">
              <svg class="fv-02__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
              <span>Enter the registered company name, not a trading name</span>
            </p>
          </div>

          <div class="fv-02__field">
            <label class="fv-02__label" for="fv-02-tax">Tax reference<span class="fv-02__sr"> (required)</span></label>
            <input class="fv-02__input" id="fv-02-tax" name="fv-02-tax" type="text" required minlength="6" placeholder="GB 421 8890 07" aria-describedby="fv-02-tax-msg">
            <p class="fv-02__msg" id="fv-02-tax-msg">
              <svg class="fv-02__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
              <span>Tax reference must be at least 6 characters</span>
            </p>
          </div>

          <div class="fv-02__field">
            <label class="fv-02__label" for="fv-02-ref">Internal cost centre</label>
            <input class="fv-02__input" id="fv-02-ref" name="fv-02-ref" type="text" placeholder="ENG-4471">
            <p class="fv-02__hint">Appears on your remittance advice.</p>
          </div>

          <button class="fv-02__btn" type="button">Save payout details</button>
        </fieldset>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-02 {
  --page: #f6f2ea;
  --surface: #fffdf8;
  --ink: #23201b;
  --muted: #6d6659;
  --rule: #e0d8c9;
  --accent: #7a5b2c;
  --marker: #a8442c;
  --error: #a8442c;
  --error-ink: #8d3421;
  --error-bg: #fbeee9;
  --field-gap: 1.75rem;
  --font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-02 {
    --marker: oklch(0.5 0.15 32);
    --error: oklch(0.5 0.15 32);
    --error-ink: oklch(0.43 0.15 32);
    --error-bg: oklch(0.96 0.02 32);
    --accent: oklch(0.45 0.08 70);
  }
}

.fv-02 *,
.fv-02 *::before,
.fv-02 *::after {
  box-sizing: border-box;
}

.fv-02__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 4rem) clamp(1rem, 4vw, 3rem);
}

.fv-02__head {
  inline-size: min(100%, 52rem);
  min-inline-size: 0;
  margin-block-end: clamp(1.5rem, 4vw, 2.5rem);
}

.fv-02__h {
  margin: 0 0 0.625rem;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4vw, 2.4rem);
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fv-02__sub {
  margin: 0;
  max-inline-size: 40rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
}

.fv-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 19rem), 1fr));
  gap: clamp(1rem, 3vw, 1.75rem);
  inline-size: min(100%, 52rem);
}

.fv-02__card {
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  box-shadow: 0 1px 2px rgba(35, 32, 27, 0.05), 0 10px 26px -18px rgba(35, 32, 27, 0.35);
}

.fv-02__card--alt {
  background: #fbf7ef;
}

.fv-02__set {
  display: grid;
  gap: var(--field-gap);
  margin: 0;
  padding: clamp(1.25rem, 3vw, 1.875rem);
  border: 0;
  min-inline-size: 0;
}

.fv-02__legend {
  display: grid;
  gap: 0.5rem;
  padding: 0;
  margin-block-end: 0.25rem;
  min-inline-size: 0;
}

.fv-02__legendtitle {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
}

.fv-02__key {
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-02__keymark {
  color: var(--marker);
  font-weight: 700;
}

.fv-02__keypill {
  display: inline-block;
  padding: 0.1rem 0.4rem;
  border: 1px solid var(--rule);
  border-radius: 999px;
  background: #f1ebdf;
  font-size: 0.6875rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-02__field {
  display: grid;
  gap: 0.4375rem;
  min-inline-size: 0;
}

.fv-02__label {
  display: flex;
  align-items: baseline;
  gap: 0.375rem;
  flex-wrap: wrap;
  min-inline-size: 0;
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 0.005em;
}

.fv-02__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fv-02__card[data-convention="required"] .fv-02__field:has(:required) .fv-02__label::after {
  content: "*";
  color: var(--marker);
  font-size: 1.05em;
  line-height: 1;
}

.fv-02__card[data-convention="optional"] .fv-02__field:not(:has(:required)) .fv-02__label::after {
  content: "Optional";
  padding: 0.1rem 0.4rem;
  border: 1px solid var(--rule);
  border-radius: 999px;
  background: #f1ebdf;
  font-size: 0.625rem;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-02__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.875rem;
  padding: 0 0.875rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: #fffefb;
  border: 1px solid var(--rule);
  border-radius: 0.375rem;
  transition: border-color 0.16s ease, box-shadow 0.16s ease;
}

.fv-02__input::placeholder {
  color: #b3a894;
}

.fv-02__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-02__hint {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--muted);
  min-inline-size: 0;
}

.fv-02__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--error-ink);
}

.fv-02__msg span {
  min-inline-size: 0;
}

.fv-02__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.05rem;
}

.fv-02__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  background: var(--error-bg);
}

.fv-02__input:invalid:not(:placeholder-shown):not(:focus) + .fv-02__msg {
  display: flex;
}

.fv-02__input:user-invalid {
  border-color: var(--error);
  background: var(--error-bg);
  box-shadow: inset 2px 0 0 var(--error);
}

.fv-02__input:user-invalid + .fv-02__msg {
  display: flex;
}

.fv-02__btn {
  justify-self: start;
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  padding: 0.6875rem 1.25rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #fffdf8;
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.16s ease;
}

.fv-02__btn:hover {
  background: #3a352c;
}

.fv-02__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .fv-02__input,
    .fv-02__btn {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-02:not(:has(#fv-02-theme-light:checked)) {
    --page: #17150f;
    --surface: #201d16;
    --ink: #f2ece0;
    --muted: #a89e8b;
    --rule: #362f24;
    --accent: #d9b877;
    --marker: #ff9a80;
    --error: #ff9a80;
    --error-ink: #ffb3a0;
    --error-bg: #2a1a14;
  }

  .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__card--alt {
    background: #1c1a13;
  }

  .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__input {
    background: #191710;
  }

  .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__input::placeholder {
    color: #6f6656;
  }

  .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__keypill,
    .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__card[data-convention="optional"] .fv-02__field:not(:has(:required)) .fv-02__label::after {
    background: #262218;
  }

  .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__btn {
    color: #17150f;
    background: #f2ece0;
    border-color: #f2ece0;
  }

  .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__btn:hover {
    background: #ffffff;
  }
}

[data-theme="dark"] .fv-02:not(:has(#fv-02-theme-light:checked)) {
  --page: #17150f;
  --surface: #201d16;
  --ink: #f2ece0;
  --muted: #a89e8b;
  --rule: #362f24;
  --accent: #d9b877;
  --marker: #ff9a80;
  --error: #ff9a80;
  --error-ink: #ffb3a0;
  --error-bg: #2a1a14;
}

[data-theme="dark"] .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__input {
  background: #191710;
}

[data-theme="dark"] .fv-02:not(:has(#fv-02-theme-light:checked)) .fv-02__btn {
  color: #17150f;
  background: #f2ece0;
  border-color: #f2ece0;
}

.fv-02 {
  position: relative;
}

.fv-02__stage {
  padding-block-start: 4.75rem;
}

.fv-02__theme {
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

.fv-02__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-02__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-02__themeopt {
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

.fv-02__themeopt:hover {
  opacity: 0.85;
}

.fv-02__themeinput:checked + .fv-02__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-02__themeinput:focus-visible + .fv-02__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-02__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-02__themeinput:checked + .fv-02__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-02:has(#fv-02-theme-dark:checked) {
  --page: #17150f;
  --surface: #201d16;
  --ink: #f2ece0;
  --muted: #a89e8b;
  --rule: #362f24;
  --accent: #d9b877;
  --marker: #ff9a80;
  --error: #ff9a80;
  --error-ink: #ffb3a0;
  --error-bg: #2a1a14;
}

.fv-02:has(#fv-02-theme-dark:checked) .fv-02__card--alt {
  background: #1c1a13;
}

.fv-02:has(#fv-02-theme-dark:checked) .fv-02__input {
  background: #191710;
}

.fv-02:has(#fv-02-theme-dark:checked) .fv-02__input::placeholder {
  color: #6f6656;
}

.fv-02:has(#fv-02-theme-dark:checked) .fv-02__keypill,
.fv-02:has(#fv-02-theme-dark:checked) .fv-02__card[data-convention="optional"] .fv-02__field:not(:has(:required)) .fv-02__label::after {
  background: #262218;
}

.fv-02:has(#fv-02-theme-dark:checked) .fv-02__btn {
  color: #17150f;
  background: #f2ece0;
  border-color: #f2ece0;
}

.fv-02:has(#fv-02-theme-dark:checked) .fv-02__btn:hover {
  background: #ffffff;
}
```
