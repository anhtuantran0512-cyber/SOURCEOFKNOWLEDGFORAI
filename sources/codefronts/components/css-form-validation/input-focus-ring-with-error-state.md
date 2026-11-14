---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/input-focus-ring-with-error-state/"
title: "Input Focus Ring with Error State"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "Focus and error have to coexist."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Input Focus Ring with Error State
Source: https://codefronts.com/components/css-form-validation/input-focus-ring-with-error-state/

Focus and error have to coexist. An invalid field that gains focus must show both signals, and the usual failure is a red border swallowing the focus ring so keyboard users lose their place. This demo lays out the full three-state matrix — valid and focused, invalid and blurred, invalid and focused — using outline rather than box-shadow so Windows High Contrast Mode keeps the ring.
## HTML
```html
<section class="fv-10" aria-labelledby="fv-10-h">
  <fieldset class="fv-10__theme">
    <legend class="fv-10__themelegend">Theme</legend>
    <input class="fv-10__themeinput" type="radio" name="fv-10-theme" id="fv-10-theme-auto" checked>
    <label class="fv-10__themeopt" for="fv-10-theme-auto">Auto</label>
    <input class="fv-10__themeinput" type="radio" name="fv-10-theme" id="fv-10-theme-light">
    <label class="fv-10__themeopt" for="fv-10-theme-light">Light</label>
    <input class="fv-10__themeinput" type="radio" name="fv-10-theme" id="fv-10-theme-dark">
    <label class="fv-10__themeopt" for="fv-10-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-10__stage">
    <header class="fv-10__head">
      <h2 class="fv-10__h" id="fv-10-h">The focus ring and the error border are two different messages</h2>
      <p class="fv-10__sub">Tab through the row. The ring never disappears into the red, because it is an <code>outline</code> with an offset — not a shadow.</p>
    </header>

    <form class="fv-10__matrix" aria-label="Focus and error state matrix">
      <div class="fv-10__cell">
        <p class="fv-10__tag">Valid · focused</p>
        <label class="fv-10__label" for="fv-10-a">Invoice email</label>
        <input class="fv-10__input" id="fv-10-a" name="fv-10-a" type="email" required placeholder="[email protected]" value="[email protected]" autocomplete="email" autofocus>
        <p class="fv-10__note">Blue ring, neutral border. The user knows where they are and that nothing is wrong.</p>
      </div>

      <div class="fv-10__cell">
        <p class="fv-10__tag">Invalid · blurred</p>
        <label class="fv-10__label" for="fv-10-b">Purchase order</label>
        <input class="fv-10__input" id="fv-10-b" name="fv-10-b" type="text" required pattern="PO-[0-9]{5}" placeholder="PO-40221" value="PO 40221" aria-describedby="fv-10-b-msg">
        <p class="fv-10__msg" id="fv-10-b-msg">
          <svg class="fv-10__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.8"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Purchase orders look like PO-40221 — letters, hyphen, five digits</span>
        </p>
      </div>

      <div class="fv-10__cell">
        <p class="fv-10__tag">Invalid · focused</p>
        <label class="fv-10__label" for="fv-10-c">VAT number</label>
        <input class="fv-10__input" id="fv-10-c" name="fv-10-c" type="text" required minlength="9" placeholder="GB421889007" value="GB42" aria-describedby="fv-10-c-msg">
        <p class="fv-10__msg" id="fv-10-c-msg">
          <svg class="fv-10__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.8"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>VAT numbers are at least 9 characters including the country prefix</span>
        </p>
        <p class="fv-10__note">Both signals visible at once: vermilion edge, blue ring, gap between them.</p>
      </div>
    </form>

    <ul class="fv-10__rules">
      <li><strong>outline, never box-shadow</strong> — forced-colors mode throws shadows away</li>
      <li><strong>outline-offset ≥ 2px</strong> — so ring and border never read as one edge</li>
      <li><strong>ring hue ≠ error hue</strong> — two signals need two colours</li>
      <li><strong>never <code>outline: none</code> on invalid</strong> — that is the field they are looking for</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.fv-10 {
  --page: #fafafa;
  --surface: #ffffff;
  --ink: #18181b;
  --muted: #5c5c66;
  --rule: #cfcfd6;
  --ring: #1f62e0;
  --ring-w: 2px;
  --ring-offset: 3px;
  --error: #d93a1f;
  --error-ink: #a82c15;
  --field-radius: 0.375rem;
  --font-display: system-ui, "Segoe UI", sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-10 {
    --ring: oklch(0.5 0.2 262);
    --error: oklch(0.55 0.2 32);
    --error-ink: oklch(0.45 0.19 32);
  }
}

.fv-10 *,
.fv-10 *::before,
.fv-10 *::after {
  box-sizing: border-box;
}

.fv-10__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 4.5vw, 3.5rem) clamp(1rem, 4vw, 3rem);
}

.fv-10__head {
  inline-size: min(100%, 56rem);
  min-inline-size: 0;
  margin-block-end: clamp(1.25rem, 3.5vw, 2rem);
}

.fv-10__h {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 3.6vw, 1.95rem);
  font-weight: 640;
  line-height: 1.15;
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.fv-10__sub {
  margin: 0;
  max-inline-size: 42rem;
  font-size: 0.9375rem;
  line-height: 1.55;
  color: var(--muted);
}

.fv-10__sub code,
.fv-10__rules code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.86em;
  padding: 0.08em 0.3em;
  border-radius: 0.25rem;
  background: #eeeef2;
}

.fv-10__matrix {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: clamp(0.875rem, 2.5vw, 1.25rem);
  inline-size: min(100%, 56rem);
}

.fv-10__cell {
  display: grid;
  gap: 0.4375rem;
  align-content: start;
  min-inline-size: 0;
  padding: 1.125rem;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
}

.fv-10__tag {
  margin: 0 0 0.25rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-10__label {
  font-size: 0.8125rem;
  font-weight: 600;
}

.fv-10__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.75rem;
  padding: 0 0.8125rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: var(--surface);
  border: 1.5px solid var(--rule);
  border-radius: var(--field-radius);
}

.fv-10__input::placeholder {
  color: #9d9da8;
}

.fv-10__input:focus-visible {
  outline: var(--ring-w) solid var(--ring);
  outline-offset: var(--ring-offset);
}

.fv-10__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
}

.fv-10__input:user-invalid {
  border-color: var(--error);
  border-width: 2px;
}

.fv-10__input:user-invalid:focus-visible {
  outline: var(--ring-w) solid var(--ring);
  outline-offset: var(--ring-offset);
}

.fv-10__input:user-valid {
  border-color: #2b7a4b;
}

.fv-10__msg {
  display: flex;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  font-weight: 500;
  color: var(--error-ink);
}

.fv-10__msg span {
  min-inline-size: 0;
}

.fv-10__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-10__note {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-10__rules {
  inline-size: min(100%, 56rem);
  min-inline-size: 0;
  margin: clamp(1.25rem, 3.5vw, 2rem) 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
  gap: 0.5rem;
}

.fv-10__rules li {
  min-inline-size: 0;
  padding: 0.6875rem 0.8125rem;
  border-inline-start: 2px solid var(--ring);
  background: var(--surface);
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-10__rules strong {
  display: block;
  color: var(--ink);
  font-weight: 650;
}

@media (forced-colors: active) {
  .fv-10__input:focus-visible {
    outline: 2px solid Highlight;
    outline-offset: 3px;
  }

  .fv-10__input:user-invalid {
    border-color: Mark;
  }

  .fv-10__msg {
    color: MarkText;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-10:not(:has(#fv-10-theme-light:checked)) {
    --page: #0c0c0e;
    --surface: #151518;
    --ink: #f0f0f2;
    --muted: #9a9aa4;
    --rule: #33333a;
    --ring: #6d9dff;
    --error: #ff7a5c;
    --error-ink: #ff9c85;
  }

  .fv-10:not(:has(#fv-10-theme-light:checked)) .fv-10__sub code,
    .fv-10:not(:has(#fv-10-theme-light:checked)) .fv-10__rules code {
    background: #22222a;
  }

  .fv-10:not(:has(#fv-10-theme-light:checked)) .fv-10__input::placeholder {
    color: #6a6a74;
  }

  .fv-10:not(:has(#fv-10-theme-light:checked)) .fv-10__input:user-valid {
    border-color: #4fb37a;
  }
}

[data-theme="dark"] .fv-10:not(:has(#fv-10-theme-light:checked)) {
  --page: #0c0c0e;
  --surface: #151518;
  --ink: #f0f0f2;
  --muted: #9a9aa4;
  --rule: #33333a;
  --ring: #6d9dff;
  --error: #ff7a5c;
  --error-ink: #ff9c85;
}

[data-theme="dark"] .fv-10:not(:has(#fv-10-theme-light:checked)) .fv-10__input::placeholder {
  color: #6a6a74;
}

.fv-10 {
  position: relative;
}

.fv-10__stage {
  padding-block-start: 4.75rem;
}

.fv-10__theme {
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

.fv-10__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-10__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-10__themeopt {
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

.fv-10__themeopt:hover {
  opacity: 0.85;
}

.fv-10__themeinput:checked + .fv-10__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-10__themeinput:focus-visible + .fv-10__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-10__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-10__themeinput:checked + .fv-10__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-10:has(#fv-10-theme-dark:checked) {
  --page: #0c0c0e;
  --surface: #151518;
  --ink: #f0f0f2;
  --muted: #9a9aa4;
  --rule: #33333a;
  --ring: #6d9dff;
  --error: #ff7a5c;
  --error-ink: #ff9c85;
}

.fv-10:has(#fv-10-theme-dark:checked) .fv-10__sub code,
.fv-10:has(#fv-10-theme-dark:checked) .fv-10__rules code {
  background: #22222a;
}

.fv-10:has(#fv-10-theme-dark:checked) .fv-10__input::placeholder {
  color: #6a6a74;
}

.fv-10:has(#fv-10-theme-dark:checked) .fv-10__input:user-valid {
  border-color: #4fb37a;
}
```
