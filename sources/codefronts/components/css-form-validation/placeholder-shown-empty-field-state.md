---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/placeholder-shown-empty-field-state/"
title: "Placeholder Shown Empty Field State"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: ":placeholder-shown answers one question well — is this field still empty — and it is the backbone of the pre-:user-invalid validation pattern."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Placeholder Shown Empty Field State
Source: https://codefronts.com/components/css-form-validation/placeholder-shown-empty-field-state/

:placeholder-shown answers one question well — is this field still empty — and it is the backbone of the pre-:user-invalid validation pattern. This demo lays out the four states side by side (empty, empty and focused, abandoned, filled), shows why :not(:focus) matters, and spells out the two limits: it needs a non-empty placeholder attribute to ever match, and empty is not the same as invalid.
## HTML
```html
<section class="fv-05" aria-labelledby="fv-05-h">
  <fieldset class="fv-05__theme">
    <legend class="fv-05__themelegend">Theme</legend>
    <input class="fv-05__themeinput" type="radio" name="fv-05-theme" id="fv-05-theme-auto" checked>
    <label class="fv-05__themeopt" for="fv-05-theme-auto">Auto</label>
    <input class="fv-05__themeinput" type="radio" name="fv-05-theme" id="fv-05-theme-light">
    <label class="fv-05__themeopt" for="fv-05-theme-light">Light</label>
    <input class="fv-05__themeinput" type="radio" name="fv-05-theme" id="fv-05-theme-dark">
    <label class="fv-05__themeopt" for="fv-05-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-05__stage">
    <header class="fv-05__head">
      <p class="fv-05__eyebrow">Orbit · field states</p>
      <h2 class="fv-05__h" id="fv-05-h">Empty, focused, abandoned, filled</h2>
      <p class="fv-05__sub">One Baseline selector separates these four. It answers "is this still empty" — nothing more.</p>
    </header>

    <form class="fv-05__matrix" aria-label="Placeholder shown state matrix">
      <div class="fv-05__cell">
        <p class="fv-05__state">Empty · not focused</p>
        <label class="fv-05__label" for="fv-05-a">Project key</label>
        <input class="fv-05__input" id="fv-05-a" name="fv-05-a" type="text" placeholder="ORB-1" aria-describedby="fv-05-a-hint">
        <p class="fv-05__hint" id="fv-05-a-hint"><code>:placeholder-shown</code> matches. Optional field, so no error.</p>
      </div>

      <div class="fv-05__cell">
        <p class="fv-05__state">Empty · required · left behind</p>
        <label class="fv-05__label" for="fv-05-b">Owner email</label>
        <input class="fv-05__input fv-05__input--watch" id="fv-05-b" name="fv-05-b" type="email" required placeholder="[email protected]" autocomplete="email" aria-describedby="fv-05-b-msg">
        <p class="fv-05__nudge" id="fv-05-b-msg">
          <svg class="fv-05__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 6.4v4.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="13.9" r="1" fill="currentColor"></circle></svg>
          <span>Still needed before this project can be created</span>
        </p>
      </div>

      <div class="fv-05__cell">
        <p class="fv-05__state">Filled · wrong</p>
        <label class="fv-05__label" for="fv-05-c">Region code</label>
        <input class="fv-05__input" id="fv-05-c" name="fv-05-c" type="text" required pattern="[a-z]{2}-[a-z]{4}-[0-9]" placeholder="eu-west-1" value="eu west 1" aria-describedby="fv-05-c-msg">
        <p class="fv-05__msg" id="fv-05-c-msg">
          <svg class="fv-05__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M7 7l6 6M13 7l-6 6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path></svg>
          <span>Use the hyphenated form, like eu-west-1</span>
        </p>
      </div>

      <div class="fv-05__cell">
        <p class="fv-05__state">Filled · valid</p>
        <label class="fv-05__label" for="fv-05-d">Retention</label>
        <input class="fv-05__input" id="fv-05-d" name="fv-05-d" type="number" required min="1" max="365" placeholder="30" value="90" aria-describedby="fv-05-d-hint">
        <p class="fv-05__hint" id="fv-05-d-hint"><code>:not(:placeholder-shown)</code> matches — the field carries a value.</p>
      </div>
    </form>

    <p class="fv-05__rule"><span class="fv-05__rulekey">Remember</span> No <code>placeholder</code> attribute means the selector never matches. And empty never means invalid.</p>
  </div>
</section>
```
## CSS
```css
.fv-05 {
  --page: #0a0a0a;
  --surface: #131313;
  --ink: #f2f2f0;
  --muted: #8d8d88;
  --rule: #2a2a28;
  --accent: #c6f24e;
  --error: #ff4d2e;
  --error-ink: #ff8368;
  --warn: #f0a53c;
  --offset: 4px;
  --matrix-min: 15rem;
  --font-display: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-05 {
    --accent: oklch(0.9 0.2 118);
    --error: oklch(0.62 0.23 30);
    --error-ink: oklch(0.72 0.18 30);
    --warn: oklch(0.78 0.15 70);
  }
}

.fv-05 *,
.fv-05 *::before,
.fv-05 *::after {
  box-sizing: border-box;
}

.fv-05__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3.25rem) clamp(0.875rem, 3.5vw, 2.5rem);
}

.fv-05__head {
  inline-size: min(100%, 54rem);
  min-inline-size: 0;
  margin-block-end: 1.5rem;
}

.fv-05__eyebrow {
  margin: 0 0 0.625rem;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-05__h {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 3.4vw, 1.9rem);
  font-weight: 500;
  letter-spacing: -0.02em;
  line-height: 1.15;
}

.fv-05__sub {
  margin: 0;
  max-inline-size: 38rem;
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--muted);
}

.fv-05__matrix {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, var(--matrix-min)), 1fr));
  gap: 0.75rem;
  inline-size: min(100%, 54rem);
}

.fv-05__cell {
  display: grid;
  gap: 0.375rem;
  align-content: start;
  min-inline-size: 0;
  padding: 0.75rem;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0;
  box-shadow: var(--offset) var(--offset) 0 0 #1e1e1c;
}

.fv-05__state {
  margin: 0 0 0.125rem;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-05__label {
  font-size: 0.8125rem;
  font-weight: 600;
}

.fv-05__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.5rem;
  padding: 0 0.625rem;
  font-family: var(--font-display);
  font-size: 0.875rem;
  color: var(--ink);
  background: #0e0e0e;
  border: 1px solid var(--rule);
  border-radius: 0;
  transition: border-color 0.14s linear, color 0.14s linear;
}

.fv-05__input::placeholder {
  color: #5c5c58;
}

.fv-05__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-05__input:placeholder-shown:not(:focus) {
  color: var(--muted);
  border-style: dashed;
}

.fv-05__input:not(:placeholder-shown) {
  border-color: #3d3d39;
}

.fv-05__input--watch:required:placeholder-shown:not(:focus) {
  border-color: var(--warn);
}

.fv-05__hint {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-05__hint code,
.fv-05__rule code {
  font-family: var(--font-display);
  font-size: 0.92em;
  color: var(--accent);
}

.fv-05__nudge,
.fv-05__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.4;
}

.fv-05__nudge span,
.fv-05__msg span {
  min-inline-size: 0;
}

.fv-05__icon {
  flex: none;
  inline-size: 0.9375rem;
  block-size: 0.9375rem;
  margin-block-start: 0.08rem;
}

.fv-05__nudge {
  color: var(--warn);
}

.fv-05__msg {
  color: var(--error-ink);
}

.fv-05__input--watch:required:placeholder-shown:not(:focus) ~ .fv-05__nudge {
  display: flex;
}

.fv-05__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  color: var(--error-ink);
}

.fv-05__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-05__msg {
  display: flex;
}

.fv-05__input:user-invalid:not(:placeholder-shown) {
  border-color: var(--error);
  color: var(--error-ink);
}

.fv-05__input:user-invalid:not(:placeholder-shown) ~ .fv-05__msg {
  display: flex;
}

.fv-05__input:user-valid:not(:placeholder-shown) {
  border-color: var(--accent);
}

.fv-05__rule {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: baseline;
  inline-size: min(100%, 54rem);
  min-inline-size: 0;
  margin: 1.25rem 0 0;
  padding: 0.75rem 0.875rem;
  border: 1px dashed var(--rule);
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-05__rulekey {
  flex: none;
  padding: 0.15rem 0.45rem;
  background: var(--accent);
  color: #0a0a0a;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

@media (prefers-reduced-motion: reduce) {
  .fv-05__input {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .fv-05:not(:has(#fv-05-theme-dark:checked)) {
    --page: #f4f4f1;
    --surface: #ffffff;
    --ink: #131311;
    --muted: #6a6a64;
    --rule: #d8d8d2;
    --accent: #4d7a00;
    --error: #c62c12;
    --error-ink: #9c2210;
    --warn: #8a5a08;
  }

  .fv-05:not(:has(#fv-05-theme-dark:checked)) .fv-05__cell {
    box-shadow: var(--offset) var(--offset) 0 0 #e2e2dc;
  }

  .fv-05:not(:has(#fv-05-theme-dark:checked)) .fv-05__input {
    background: #fbfbf9;
  }

  .fv-05:not(:has(#fv-05-theme-dark:checked)) .fv-05__input::placeholder {
    color: #a3a39c;
  }

  .fv-05:not(:has(#fv-05-theme-dark:checked)) .fv-05__rulekey {
    color: #ffffff;
  }
}

[data-theme="dark"] .fv-05:not(:has(#fv-05-theme-light:checked)) {
  --page: #0a0a0a;
  --surface: #131313;
  --ink: #f2f2f0;
  --muted: #8d8d88;
  --rule: #2a2a28;
  --accent: #c6f24e;
  --error: #ff4d2e;
  --error-ink: #ff8368;
  --warn: #f0a53c;
}

[data-theme="dark"] .fv-05:not(:has(#fv-05-theme-light:checked)) .fv-05__cell {
  box-shadow: var(--offset) var(--offset) 0 0 #1e1e1c;
}

[data-theme="dark"] .fv-05:not(:has(#fv-05-theme-light:checked)) .fv-05__input {
  background: #0e0e0e;
}

[data-theme="dark"] .fv-05:not(:has(#fv-05-theme-light:checked)) .fv-05__rulekey {
  color: #0a0a0a;
}

.fv-05 {
  position: relative;
}

.fv-05__stage {
  padding-block-start: 4.75rem;
}

.fv-05__theme {
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

.fv-05__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-05__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-05__themeopt {
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

.fv-05__themeopt:hover {
  opacity: 0.85;
}

.fv-05__themeinput:checked + .fv-05__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-05__themeinput:focus-visible + .fv-05__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-05__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-05__themeinput:checked + .fv-05__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-05:has(#fv-05-theme-light:checked) {
  --page: #f4f4f1;
  --surface: #ffffff;
  --ink: #131311;
  --muted: #6a6a64;
  --rule: #d8d8d2;
  --accent: #4d7a00;
  --error: #c62c12;
  --error-ink: #9c2210;
  --warn: #8a5a08;
}

.fv-05:has(#fv-05-theme-light:checked) .fv-05__cell {
  box-shadow: var(--offset) var(--offset) 0 0 #e2e2dc;
}

.fv-05:has(#fv-05-theme-light:checked) .fv-05__input {
  background: #fbfbf9;
}

.fv-05:has(#fv-05-theme-light:checked) .fv-05__input::placeholder {
  color: #a3a39c;
}

.fv-05:has(#fv-05-theme-light:checked) .fv-05__rulekey {
  color: #ffffff;
}
```
