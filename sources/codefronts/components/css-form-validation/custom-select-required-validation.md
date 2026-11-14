---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/custom-select-required-validation/"
title: "Custom Select Required Validation"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "required on a <select> only works when the placeholder option has an empty value — that one detail is what most implementations miss."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Select Required Validation
Source: https://codefronts.com/components/css-form-validation/custom-select-required-validation/

required on a <select> only works when the placeholder option has an empty value — that one detail is what most implementations miss. This demo pairs value="" with disabled selected so the unchosen state is genuinely invalid from first paint, then styles it with bare :invalid, which is safe here in a way it is nowhere else in this collection.
## HTML
```html
<section class="fv-09" aria-labelledby="fv-09-h">
  <fieldset class="fv-09__theme">
    <legend class="fv-09__themelegend">Theme</legend>
    <input class="fv-09__themeinput" type="radio" name="fv-09-theme" id="fv-09-theme-auto" checked>
    <label class="fv-09__themeopt" for="fv-09-theme-auto">Auto</label>
    <input class="fv-09__themeinput" type="radio" name="fv-09-theme" id="fv-09-theme-light">
    <label class="fv-09__themeopt" for="fv-09-theme-light">Light</label>
    <input class="fv-09__themeinput" type="radio" name="fv-09-theme" id="fv-09-theme-dark">
    <label class="fv-09__themeopt" for="fv-09-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-09__stage">
    <form class="fv-09__card" aria-labelledby="fv-09-h">
      <header class="fv-09__head">
        <p class="fv-09__eyebrow">Prism · workspace setup</p>
        <h2 class="fv-09__h" id="fv-09-h">The empty value is what makes required work</h2>
        <p class="fv-09__sub">Nothing is chosen yet, so both selects are genuinely invalid — the one case where styling <code>:invalid</code> on load is honest.</p>
      </header>

      <div class="fv-09__field">
        <label class="fv-09__label" for="fv-09-plan">Billing plan</label>
        <div class="fv-09__control">
          <select class="fv-09__select" id="fv-09-plan" name="fv-09-plan" required aria-describedby="fv-09-plan-msg">
            <option value="" disabled selected>Choose a plan</option>
            <option value="team">Team · 12 seats included</option>
            <option value="business">Business · SSO and audit log</option>
            <option value="enterprise">Enterprise · custom terms</option>
          </select>
          <svg class="fv-09__chev" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5.5 8l4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
        </div>
        <p class="fv-09__msg" id="fv-09-plan-msg">
          <svg class="fv-09__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Choose a billing plan to continue — you can change it later from Settings</span>
        </p>
      </div>

      <div class="fv-09__field">
        <label class="fv-09__label" for="fv-09-region">Data region</label>
        <div class="fv-09__control">
          <select class="fv-09__select" id="fv-09-region" name="fv-09-region" required aria-describedby="fv-09-region-msg">
            <option value="" disabled selected>Choose a region</option>
            <option value="eu-west-1">eu-west-1 · Ireland</option>
            <option value="us-east-2">us-east-2 · Ohio</option>
            <option value="ap-south-1">ap-south-1 · Mumbai</option>
          </select>
          <svg class="fv-09__chev" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5.5 8l4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
        </div>
        <p class="fv-09__msg" id="fv-09-region-msg">
          <svg class="fv-09__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Pick the region where Prism should store your data — this cannot be changed after setup</span>
        </p>
      </div>

      <div class="fv-09__legend">
        <p class="fv-09__legenditem"><code>value=""</code> on the placeholder — without it, <code>required</code> does nothing</p>
        <p class="fv-09__legenditem"><code>disabled selected</code> — starts empty, cannot be reselected</p>
      </div>

      <button class="fv-09__btn" type="button">Continue to billing</button>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-09 {
  --page: #f3f6fb;
  --surface: #ffffff;
  --ink: #101a2c;
  --muted: #5b6a84;
  --rule: #d5deec;
  --accent: #1f5fd8;
  --error: #c0203c;
  --error-ink: #9c1730;
  --error-bg: #fdf1f3;
  --radius: 0.5rem;
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
  .fv-09 {
    --accent: oklch(0.5 0.19 262);
    --error: oklch(0.51 0.19 16);
    --error-ink: oklch(0.43 0.19 16);
    --error-bg: oklch(0.97 0.02 16);
  }
}

.fv-09 *,
.fv-09 *::before,
.fv-09 *::after {
  box-sizing: border-box;
}

.fv-09__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 3.5rem) clamp(1rem, 4vw, 2.5rem);
}

.fv-09__card {
  inline-size: min(100%, 31rem);
  min-inline-size: 0;
  display: grid;
  gap: 1.125rem;
  padding: clamp(1.25rem, 4vw, 1.875rem);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.875rem;
  box-shadow: 0 1px 2px rgba(16, 26, 44, 0.05), 0 18px 40px -30px rgba(16, 26, 44, 0.55);
}

.fv-09__head {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
}

.fv-09__eyebrow {
  margin: 0;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-09__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.2rem, 3.4vw, 1.5rem);
  font-weight: 650;
  line-height: 1.2;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fv-09__sub {
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--muted);
}

.fv-09__sub code,
.fv-09__legenditem code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.86em;
  padding: 0.1em 0.32em;
  border-radius: 0.25rem;
  background: #eef2f9;
  color: var(--ink);
}

.fv-09__field {
  display: grid;
  gap: 0.4375rem;
  min-inline-size: 0;
}

.fv-09__label {
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.fv-09__control {
  position: relative;
  display: grid;
  min-inline-size: 0;
}

.fv-09__select {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.875rem;
  padding: 0 2.5rem 0 0.875rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: #fbfcfe;
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  appearance: none;
  cursor: pointer;
  transition: border-color 0.16s ease, background-color 0.16s ease;
}

.fv-09__select:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-09__select option {
  color: var(--ink);
}

.fv-09__select option[value=""] {
  color: #8b98ad;
}

.fv-09__chev {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-end: 0.875rem;
  translate: 0 -50%;
  inline-size: 1.125rem;
  block-size: 1.125rem;
  color: var(--muted);
  pointer-events: none;
}

.fv-09__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--error-ink);
}

.fv-09__msg span {
  min-inline-size: 0;
}

.fv-09__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-09__select:invalid {
  border-color: var(--error);
  background: var(--error-bg);
  color: #7b8698;
}

.fv-09__select:invalid ~ .fv-09__chev {
  color: var(--error);
}

.fv-09__field:has(.fv-09__select:invalid) .fv-09__msg {
  display: flex;
}

.fv-09__select:valid {
  border-color: #1f8f5f;
  background: #f2fbf6;
  color: var(--ink);
}

.fv-09__legend {
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
  padding: 0.75rem 0.875rem;
  border: 1px dashed var(--rule);
  border-radius: var(--radius);
  background: #f8fafd;
}

.fv-09__legenditem {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-09__btn {
  justify-self: start;
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  padding: 0.6875rem 1.25rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #ffffff;
  background: var(--accent);
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
}

.fv-09__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .fv-09__select {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-09:not(:has(#fv-09-theme-light:checked)) {
    --page: #080d16;
    --surface: #101724;
    --ink: #e8eef8;
    --muted: #94a3bd;
    --rule: #1f2a3d;
    --accent: #5b9bff;
    --error: #ff6d84;
    --error-ink: #ff96a6;
    --error-bg: #22111a;
  }

  .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__select {
    background: #0c121d;
  }

  .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__select:valid {
    background: #0d1d17;
    border-color: #3fae7c;
  }

  .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__sub code,
    .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__legenditem code {
    background: #17202f;
    color: #e8eef8;
  }

  .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__legend {
    background: #0c121d;
  }

  .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__btn {
    color: #05101f;
  }
}

[data-theme="dark"] .fv-09:not(:has(#fv-09-theme-light:checked)) {
  --page: #080d16;
  --surface: #101724;
  --ink: #e8eef8;
  --muted: #94a3bd;
  --rule: #1f2a3d;
  --accent: #5b9bff;
  --error: #ff6d84;
  --error-ink: #ff96a6;
  --error-bg: #22111a;
}

[data-theme="dark"] .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__select {
  background: #0c121d;
}

[data-theme="dark"] .fv-09:not(:has(#fv-09-theme-light:checked)) .fv-09__btn {
  color: #05101f;
}

.fv-09 {
  position: relative;
}

.fv-09__stage {
  padding-block-start: 4.75rem;
}

.fv-09__theme {
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

.fv-09__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-09__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-09__themeopt {
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

.fv-09__themeopt:hover {
  opacity: 0.85;
}

.fv-09__themeinput:checked + .fv-09__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-09__themeinput:focus-visible + .fv-09__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-09__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-09__themeinput:checked + .fv-09__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-09:has(#fv-09-theme-dark:checked) {
  --page: #080d16;
  --surface: #101724;
  --ink: #e8eef8;
  --muted: #94a3bd;
  --rule: #1f2a3d;
  --accent: #5b9bff;
  --error: #ff6d84;
  --error-ink: #ff96a6;
  --error-bg: #22111a;
}

.fv-09:has(#fv-09-theme-dark:checked) .fv-09__select {
  background: #0c121d;
}

.fv-09:has(#fv-09-theme-dark:checked) .fv-09__select:valid {
  background: #0d1d17;
  border-color: #3fae7c;
}

.fv-09:has(#fv-09-theme-dark:checked) .fv-09__sub code,
.fv-09:has(#fv-09-theme-dark:checked) .fv-09__legenditem code {
  background: #17202f;
  color: #e8eef8;
}

.fv-09:has(#fv-09-theme-dark:checked) .fv-09__legend {
  background: #0c121d;
}

.fv-09:has(#fv-09-theme-dark:checked) .fv-09__btn {
  color: #05101f;
}
```
