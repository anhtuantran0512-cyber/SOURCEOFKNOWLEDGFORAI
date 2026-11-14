---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/no-js-form-submit-blocked-visuals/"
title: "No JS Form Submit Blocked Visuals"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "What the browser does on its own when a required field is empty and submit is pressed: it blocks the submission, focuses the first invalid field and shows…"
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: No JS Form Submit Blocked Visuals
Source: https://codefronts.com/components/css-form-validation/no-js-form-submit-blocked-visuals/

What the browser does on its own when a required field is empty and submit is pressed: it blocks the submission, focuses the first invalid field and shows its bubble. This demo styles the surrounding experience with :has() so the form visibly reacts before any of that happens, and spells out what novalidate actually turns off — the blocking and the bubbles, but never the CSS pseudo-classes, which keep matching.
## HTML
```html
<section class="fv-20" aria-labelledby="fv-20-h">
  <fieldset class="fv-20__theme">
    <legend class="fv-20__themelegend">Theme</legend>
    <input class="fv-20__themeinput" type="radio" name="fv-20-theme" id="fv-20-theme-auto" checked>
    <label class="fv-20__themeopt" for="fv-20-theme-auto">Auto</label>
    <input class="fv-20__themeinput" type="radio" name="fv-20-theme" id="fv-20-theme-light">
    <label class="fv-20__themeopt" for="fv-20-theme-light">Light</label>
    <input class="fv-20__themeinput" type="radio" name="fv-20-theme" id="fv-20-theme-dark">
    <label class="fv-20__themeopt" for="fv-20-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-20__stage">
    <header class="fv-20__head">
      <p class="fv-20__eyebrow">Orbit · request a demo</p>
      <h2 class="fv-20__h" id="fv-20-h">The browser was already doing this for you</h2>
      <p class="fv-20__sub">Left: validation on, the platform blocks the send. Right: <code>novalidate</code>, which turns off the blocking and the bubble — and nothing else.</p>
    </header>

    <div class="fv-20__cols">
      <div class="fv-20__side">
        <p class="fv-20__sidetag">Validation on</p>
        <form class="fv-20__form" aria-label="Request a demo with native validation">
          <div class="fv-20__field">
            <label class="fv-20__label" for="fv-20-a-name">Your name</label>
            <input class="fv-20__input" id="fv-20-a-name" name="fv-20-a-name" type="text" required autocomplete="name" placeholder="Alex Chen" value="Alex Chen">
          </div>
          <div class="fv-20__field">
            <label class="fv-20__label" for="fv-20-a-email">Work email</label>
            <input class="fv-20__input" id="fv-20-a-email" name="fv-20-a-email" type="email" required autocomplete="email" placeholder="[email protected]" value="alex.chen.orbit.dev" aria-describedby="fv-20-a-email-msg">
            <p class="fv-20__msg" id="fv-20-a-email-msg">
              <svg class="fv-20__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
              <span>Enter a valid email address, like [email protected]</span>
            </p>
          </div>

          <div class="fv-20__bubblewrap">
            <div class="fv-20__bubble" role="img" aria-label="Illustration of the browser's native validation bubble reading: Please enter an email address.">
              <svg class="fv-20__bubbleicon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8.4" fill="currentColor"></circle><path d="M10 5.6v5.2" stroke="#ffffff" stroke-width="1.9" stroke-linecap="round"></path><circle cx="10" cy="14.3" r="1.15" fill="#ffffff"></circle></svg>
              <span>Please enter an email address.</span>
            </div>
            <p class="fv-20__bubblenote">An illustration of the native bubble. The real one is drawn by the browser and cannot be restyled.</p>
          </div>

          <button class="fv-20__btn" type="submit">Request demo</button>
          <p class="fv-20__count">1 field is stopping this from being sent.</p>
        </form>
      </div>

      <div class="fv-20__side">
        <p class="fv-20__sidetag">novalidate</p>
        <form class="fv-20__form fv-20__form--novalidate" novalidate aria-label="Request a demo with novalidate">
          <div class="fv-20__field">
            <label class="fv-20__label" for="fv-20-b-name">Your name</label>
            <input class="fv-20__input" id="fv-20-b-name" name="fv-20-b-name" type="text" required autocomplete="name" placeholder="Alex Chen" value="Alex Chen">
          </div>
          <div class="fv-20__field">
            <label class="fv-20__label" for="fv-20-b-email">Work email</label>
            <input class="fv-20__input" id="fv-20-b-email" name="fv-20-b-email" type="email" required autocomplete="email" placeholder="[email protected]" value="alex.chen.orbit.dev" aria-describedby="fv-20-b-email-msg">
            <p class="fv-20__msg" id="fv-20-b-email-msg">
              <svg class="fv-20__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
              <span>Enter a valid email address, like [email protected]</span>
            </p>
          </div>
          <ul class="fv-20__facts">
            <li>No bubble, no blocking</li>
            <li><code>:user-invalid</code> still matches — the border above proves it</li>
            <li><code>checkValidity()</code> still returns false</li>
          </ul>
          <button class="fv-20__btn fv-20__btn--ghost" type="submit">Request demo</button>
        </form>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-20 {
  --page: #ffffff;
  --surface: #ffffff;
  --field: #fcfcfd;
  --ink: #101114;
  --muted: #5a5d68;
  --rule: #e0e2e8;
  --accent: #101114;
  --error: #e8471f;
  --error-ink: #b2320f;
  --bloom: 0 18px 48px -26px rgba(232, 71, 31, 0.55);
  --font-display: "Inter Tight", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-20 {
    --error: oklch(0.6 0.21 34);
    --error-ink: oklch(0.48 0.2 34);
  }
}

.fv-20 *,
.fv-20 *::before,
.fv-20 *::after {
  box-sizing: border-box;
}

.fv-20__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 3.5rem) clamp(1rem, 4vw, 3rem);
}

.fv-20__head {
  inline-size: min(100%, 52rem);
  min-inline-size: 0;
  margin-block-end: clamp(1.25rem, 4vw, 2rem);
}

.fv-20__eyebrow {
  margin: 0 0 0.625rem;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--error-ink);
}

.fv-20__h {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 3.8vw, 2.05rem);
  font-weight: 640;
  letter-spacing: -0.03em;
  line-height: 1.12;
  text-wrap: balance;
}

.fv-20__sub {
  margin: 0;
  max-inline-size: 40rem;
  font-size: 0.9375rem;
  line-height: 1.55;
  color: var(--muted);
}

.fv-20__sub code,
.fv-20__facts code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.86em;
  padding: 0.08em 0.3em;
  border-radius: 0.25rem;
  background: #f1f2f5;
}

.fv-20__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: clamp(1rem, 3vw, 1.5rem);
  inline-size: min(100%, 52rem);
}

.fv-20__side {
  display: grid;
  gap: 0.5rem;
  align-content: start;
  min-inline-size: 0;
}

.fv-20__sidetag {
  margin: 0;
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-20__form {
  display: grid;
  gap: 0.875rem;
  align-content: start;
  min-inline-size: 0;
  padding: 1.25rem;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
}

.fv-20__form:has(.fv-20__input:invalid:not(:placeholder-shown)) {
  border-color: var(--error);
  box-shadow: var(--bloom);
}

.fv-20__form:has(.fv-20__input:user-invalid) {
  border-color: var(--error);
  box-shadow: var(--bloom);
}

.fv-20__field {
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
}

.fv-20__label {
  font-size: 0.75rem;
  font-weight: 650;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.fv-20__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.75rem;
  padding: 0 0.8125rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: var(--field);
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
}

.fv-20__input::placeholder {
  color: #9b9ea8;
}

.fv-20__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-20__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
}

.fv-20__input:invalid:not(:placeholder-shown):not(:focus) + .fv-20__msg {
  display: flex;
}

.fv-20__input:user-invalid {
  border-color: var(--error);
  border-width: 1.5px;
}

.fv-20__input:user-invalid + .fv-20__msg {
  display: flex;
}

.fv-20__input:user-valid {
  border-color: #2c7d55;
}

.fv-20__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--error-ink);
}

.fv-20__msg span {
  min-inline-size: 0;
}

.fv-20__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-20__bubblewrap {
  display: grid;
  gap: 0.4375rem;
  min-inline-size: 0;
}

.fv-20__bubble {
  position: relative;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: 0.5rem;
  min-inline-size: 0;
  padding: 0.5625rem 0.75rem;
  border: 1px solid var(--rule);
  border-radius: 0.375rem;
  background: #ffffff;
  box-shadow: 0 6px 16px -8px rgba(16, 17, 20, 0.35);
  font-size: 0.8125rem;
  line-height: 1.35;
}

.fv-20__bubble::before {
  content: "";
  position: absolute;
  inset-block-start: -5px;
  inset-inline-start: 1.25rem;
  inline-size: 9px;
  block-size: 9px;
  rotate: 45deg;
  background: #ffffff;
  border-block-start: 1px solid var(--rule);
  border-inline-start: 1px solid var(--rule);
}

.fv-20__bubble span {
  min-inline-size: 0;
}

.fv-20__bubbleicon {
  flex: none;
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
  color: var(--error);
}

.fv-20__bubblenote {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.6875rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-20__facts {
  margin: 0;
  padding-inline-start: 1.1rem;
  display: grid;
  gap: 0.3125rem;
  min-inline-size: 0;
}

.fv-20__facts li {
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-20__btn {
  justify-self: start;
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  padding: 0.6875rem 1.25rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 620;
  color: #ffffff;
  background: var(--accent);
  border: 1px solid var(--accent);
  border-radius: 0.5rem;
  cursor: pointer;
}

.fv-20__btn--ghost {
  color: var(--ink);
  background: transparent;
}

.fv-20__btn:focus-visible {
  outline: 2px solid var(--error);
  outline-offset: 3px;
}

.fv-20__form:has(.fv-20__input:user-invalid) .fv-20__btn {
  background: var(--error-ink);
  border-color: var(--error-ink);
}

.fv-20__form--novalidate:has(.fv-20__input:user-invalid) .fv-20__btn--ghost {
  background: transparent;
  border-color: var(--error);
  color: var(--error-ink);
}

.fv-20__count {
  display: none;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  font-weight: 600;
  color: var(--error-ink);
}

.fv-20__form:has(.fv-20__input:invalid:not(:placeholder-shown)) .fv-20__count {
  display: block;
}

.fv-20__form:has(.fv-20__input:user-invalid) .fv-20__count {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .fv-20:not(:has(#fv-20-theme-light:checked)) {
    --page: #0a0b0d;
    --surface: #121317;
    --field: #0e0f12;
    --ink: #f0f1f4;
    --muted: #9a9daa;
    --rule: #262932;
    --accent: #f0f1f4;
    --error: #ff7a52;
    --error-ink: #ff9c7c;
    --bloom: 0 18px 48px -26px rgba(255, 122, 82, 0.5);
  }

  .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__sub code,
    .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__facts code {
    background: #1c1f26;
  }

  .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__input::placeholder {
    color: #6a6d79;
  }

  .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__btn {
    color: #0a0b0d;
  }

  .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__btn--ghost {
    color: #f0f1f4;
  }

  .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__bubble {
    background: #1a1c22;
    border-color: #2c303a;
  }

  .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__bubble::before {
    background: #1a1c22;
    border-color: #2c303a;
  }

  .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__form:has(.fv-20__input:user-invalid) .fv-20__btn {
    color: #1a0a05;
  }
}

[data-theme="dark"] .fv-20:not(:has(#fv-20-theme-light:checked)) {
  --page: #0a0b0d;
  --surface: #121317;
  --field: #0e0f12;
  --ink: #f0f1f4;
  --muted: #9a9daa;
  --rule: #262932;
  --accent: #f0f1f4;
  --error: #ff7a52;
  --error-ink: #ff9c7c;
}

[data-theme="dark"] .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__btn {
  color: #0a0b0d;
}

[data-theme="dark"] .fv-20:not(:has(#fv-20-theme-light:checked)) .fv-20__bubble {
  background: #1a1c22;
  border-color: #2c303a;
}

.fv-20 {
  position: relative;
}

.fv-20__stage {
  padding-block-start: 4.75rem;
}

.fv-20__theme {
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

.fv-20__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-20__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-20__themeopt {
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

.fv-20__themeopt:hover {
  opacity: 0.85;
}

.fv-20__themeinput:checked + .fv-20__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-20__themeinput:focus-visible + .fv-20__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-20__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-20__themeinput:checked + .fv-20__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-20:has(#fv-20-theme-dark:checked) {
  --page: #0a0b0d;
  --surface: #121317;
  --field: #0e0f12;
  --ink: #f0f1f4;
  --muted: #9a9daa;
  --rule: #262932;
  --accent: #f0f1f4;
  --error: #ff7a52;
  --error-ink: #ff9c7c;
  --bloom: 0 18px 48px -26px rgba(255, 122, 82, 0.5);
}

.fv-20:has(#fv-20-theme-dark:checked) .fv-20__sub code,
.fv-20:has(#fv-20-theme-dark:checked) .fv-20__facts code {
  background: #1c1f26;
}

.fv-20:has(#fv-20-theme-dark:checked) .fv-20__input::placeholder {
  color: #6a6d79;
}

.fv-20:has(#fv-20-theme-dark:checked) .fv-20__btn {
  color: #0a0b0d;
}

.fv-20:has(#fv-20-theme-dark:checked) .fv-20__btn--ghost {
  color: #f0f1f4;
}

.fv-20:has(#fv-20-theme-dark:checked) .fv-20__bubble {
  background: #1a1c22;
  border-color: #2c303a;
}

.fv-20:has(#fv-20-theme-dark:checked) .fv-20__bubble::before {
  background: #1a1c22;
  border-color: #2c303a;
}

.fv-20:has(#fv-20-theme-dark:checked) .fv-20__form:has(.fv-20__input:user-invalid) .fv-20__btn {
  color: #1a0a05;
}
```
