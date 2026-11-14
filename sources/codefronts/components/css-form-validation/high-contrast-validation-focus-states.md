---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/high-contrast-validation-focus-states/"
title: "High Contrast Validation Focus States"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "Validation that survives forced-colors: active and does not lean on saturated colour to carry meaning."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: High Contrast Validation Focus States
Source: https://codefronts.com/components/css-form-validation/high-contrast-validation-focus-states/

Validation that survives forced-colors: active and does not lean on saturated colour to carry meaning. The error signal here is weight, an icon and a rule — colour is the last layer, not the first. Inside a @media (forced-colors: active) block the states switch to the Mark, MarkText and Highlight system keywords so the browser's own palette drives them.
## HTML
```html
<section class="fv-14" aria-labelledby="fv-14-h">
  <fieldset class="fv-14__theme">
    <legend class="fv-14__themelegend">Theme</legend>
    <input class="fv-14__themeinput" type="radio" name="fv-14-theme" id="fv-14-theme-auto" checked>
    <label class="fv-14__themeopt" for="fv-14-theme-auto">Auto</label>
    <input class="fv-14__themeinput" type="radio" name="fv-14-theme" id="fv-14-theme-light">
    <label class="fv-14__themeopt" for="fv-14-theme-light">Light</label>
    <input class="fv-14__themeinput" type="radio" name="fv-14-theme" id="fv-14-theme-dark">
    <label class="fv-14__themeopt" for="fv-14-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-14__stage">
    <div class="fv-14__frame">
      <header class="fv-14__head">
        <div class="fv-14__headtext">
          <p class="fv-14__eyebrow">Aperture · benefits claim</p>
          <h2 class="fv-14__h" id="fv-14-h">Weight and shape first. Colour last.</h2>
        </div>
        <div class="fv-14__toggle">
          <input class="fv-14__switch" type="checkbox" id="fv-14-hc">
          <label class="fv-14__switchlabel" for="fv-14-hc">
            <span class="fv-14__track" aria-hidden="true"><span class="fv-14__knob"></span></span>
            Preview forced colours
          </label>
        </div>
      </header>

      <form class="fv-14__form" aria-labelledby="fv-14-h">
        <div class="fv-14__field">
          <label class="fv-14__label" for="fv-14-ni">National insurance number</label>
          <input class="fv-14__input" id="fv-14-ni" name="fv-14-ni" type="text" required pattern="[A-Za-z]{2}[0-9]{6}[A-Za-z]" placeholder="QQ123456C" value="QQ12345" aria-describedby="fv-14-ni-msg">
          <p class="fv-14__msg" id="fv-14-ni-msg">
            <svg class="fv-14__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 2.4 18.6 17.2H1.4Z" fill="none" stroke="currentColor" stroke-width="2"></path><path d="M10 7.6v4.2" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path><circle cx="10" cy="14.6" r="1.1" fill="currentColor"></circle></svg>
            <span><strong>Error.</strong> Two letters, six digits, one letter — like QQ123456C</span>
          </p>
        </div>

        <div class="fv-14__field">
          <label class="fv-14__label" for="fv-14-claim">Claim reference</label>
          <input class="fv-14__input" id="fv-14-claim" name="fv-14-claim" type="text" required minlength="8" placeholder="AP-2026-88412" value="AP-2026-88412" aria-describedby="fv-14-claim-msg">
          <p class="fv-14__msg" id="fv-14-claim-msg">
            <svg class="fv-14__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 2.4 18.6 17.2H1.4Z" fill="none" stroke="currentColor" stroke-width="2"></path><path d="M10 7.6v4.2" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path><circle cx="10" cy="14.6" r="1.1" fill="currentColor"></circle></svg>
            <span><strong>Error.</strong> Claim references are at least 8 characters</span>
          </p>
        </div>

        <div class="fv-14__swatches">
          <p class="fv-14__swatchnote">These two keep their real hue via <code>forced-color-adjust: none</code> — the colour <em>is</em> the content. Nothing else in this form does.</p>
          <div class="fv-14__swatchrow">
            <span class="fv-14__swatch" data-tone="error"><span class="fv-14__chip" aria-hidden="true"></span>Error 4.7:1</span>
            <span class="fv-14__swatch" data-tone="ok"><span class="fv-14__chip" aria-hidden="true"></span>Accepted 4.9:1</span>
          </div>
        </div>

        <button class="fv-14__btn" type="button">Submit claim</button>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-14 {
  --paper: #12100e;
  --surface: #1a1714;
  --ink: #f4efe6;
  --muted: #a89f92;
  --rule: #3a342d;
  --rule-w: 2px;
  --focus: #f4efe6;
  --error-tone: #ff8f6b;
  --ok-tone: #96c48a;
  --radius: 0.125rem;
  --font-display: "Archivo Narrow", "Avenir Next Condensed", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--paper);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-14 {
    --error-tone: oklch(0.74 0.14 38);
    --ok-tone: oklch(0.79 0.1 140);
  }
}

.fv-14 *,
.fv-14 *::before,
.fv-14 *::after {
  box-sizing: border-box;
}

.fv-14__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
}

.fv-14__frame {
  inline-size: min(100%, 34rem);
  min-inline-size: 0;
  border: var(--rule-w) solid var(--ink);
  background: var(--surface);
}

.fv-14__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.875rem;
  min-inline-size: 0;
  padding: 1.125rem 1.25rem;
  border-block-end: var(--rule-w) solid var(--ink);
}

.fv-14__headtext {
  min-inline-size: 0;
}

.fv-14__eyebrow {
  margin: 0 0 0.25rem;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-14__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.2rem, 3.4vw, 1.55rem);
  font-weight: 700;
  letter-spacing: 0.01em;
  text-transform: uppercase;
  line-height: 1.1;
}

.fv-14__toggle {
  min-inline-size: 0;
}

.fv-14__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-14__switchlabel {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 2.75rem;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  cursor: pointer;
}

.fv-14__track {
  inline-size: 2.375rem;
  block-size: 1.25rem;
  padding: 2px;
  border: var(--rule-w) solid var(--ink);
  display: block;
}

.fv-14__knob {
  display: block;
  inline-size: 0.75rem;
  block-size: 0.75rem;
  background: var(--ink);
}

.fv-14__switch:checked + .fv-14__switchlabel .fv-14__knob {
  margin-inline-start: 1.0625rem;
}

.fv-14__switch:focus-visible + .fv-14__switchlabel .fv-14__track {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.fv-14__form {
  display: grid;
  gap: 1.25rem;
  min-inline-size: 0;
  padding: 1.25rem;
}

.fv-14__field {
  display: grid;
  gap: 0.4375rem;
  min-inline-size: 0;
}

.fv-14__label {
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.fv-14__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.875rem;
  padding: 0 0.75rem;
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.9375rem;
  letter-spacing: 0.04em;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--rule);
  border-radius: var(--radius);
}

.fv-14__input::placeholder {
  color: #6f665b;
}

.fv-14__input:focus-visible {
  outline: var(--rule-w) solid var(--focus);
  outline-offset: 2px;
}

.fv-14__msg {
  display: none;
  gap: 0.5rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  padding-inline-start: 0.625rem;
  border-inline-start: var(--rule-w) solid currentColor;
  font-size: 0.8125rem;
  line-height: 1.45;
  font-weight: 500;
}

.fv-14__msg strong {
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-size: 0.9em;
}

.fv-14__msg span {
  min-inline-size: 0;
}

.fv-14__icon {
  flex: none;
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
  margin-block-start: 0.1rem;
}

.fv-14__input:invalid:not(:placeholder-shown):not(:focus) {
  border-width: var(--rule-w);
  border-color: var(--ink);
}

.fv-14__input:invalid:not(:placeholder-shown):not(:focus) + .fv-14__msg {
  display: flex;
}

.fv-14__input:user-invalid {
  border-width: var(--rule-w);
  border-color: var(--ink);
}

.fv-14__input:user-invalid + .fv-14__msg {
  display: flex;
}

.fv-14__swatches {
  display: grid;
  gap: 0.625rem;
  min-inline-size: 0;
  padding-block-start: 0.25rem;
  border-block-start: 1px solid var(--rule);
}

.fv-14__swatchnote {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-14__swatchnote code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.92em;
  color: var(--ink);
}

.fv-14__swatchrow {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  min-inline-size: 0;
}

.fv-14__swatch {
  display: inline-flex;
  align-items: center;
  gap: 0.4375rem;
  min-inline-size: 0;
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  forced-color-adjust: none;
}

.fv-14__swatch .fv-14__chip {
  inline-size: 0.875rem;
  block-size: 0.875rem;
  border: 1px solid var(--ink);
}

.fv-14__swatch[data-tone="error"] .fv-14__chip {
  background: var(--error-tone);
}

.fv-14__swatch[data-tone="ok"] .fv-14__chip {
  background: var(--ok-tone);
}

.fv-14__btn {
  justify-self: start;
  min-block-size: 2.875rem;
  min-inline-size: 44px;
  padding: 0.75rem 1.375rem;
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--paper);
  background: var(--ink);
  border: var(--rule-w) solid var(--ink);
  border-radius: var(--radius);
  cursor: pointer;
}

.fv-14__btn:focus-visible {
  outline: var(--rule-w) solid var(--focus);
  outline-offset: 3px;
}

.fv-14:has(.fv-14__switch:checked) {
  --paper: #000000;
  --surface: #000000;
  --ink: #ffffff;
  --muted: #ffffff;
  --rule: #ffffff;
  --focus: #ffff00;
  --error-tone: #ffff00;
  --ok-tone: #00ff00;
}

.fv-14:has(.fv-14__switch:checked) .fv-14__msg {
  color: #ffff00;
}

.fv-14:has(.fv-14__switch:checked) .fv-14__input:user-invalid,
.fv-14:has(.fv-14__switch:checked) .fv-14__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: #ffff00;
}

@media (forced-colors: active) {
  .fv-14__frame,
    .fv-14__head {
    border-color: CanvasText;
  }

  .fv-14__input {
    border-color: CanvasText;
    color: CanvasText;
  }

  .fv-14__input:user-invalid,
    .fv-14__input:invalid:not(:placeholder-shown):not(:focus) {
    border-color: Mark;
    border-width: var(--rule-w);
  }

  .fv-14__msg {
    color: MarkText;
    background: Mark;
    border-inline-start-color: MarkText;
    padding: 0.375rem 0.5rem;
  }

  .fv-14__input:focus-visible {
    outline: var(--rule-w) solid Highlight;
    outline-offset: 2px;
  }

  .fv-14__btn {
    color: ButtonText;
    background: ButtonFace;
    border-color: ButtonText;
  }

  .fv-14__track,
    .fv-14__knob {
    border-color: CanvasText;
    background: CanvasText;
  }
}

@media (prefers-color-scheme: light) {
  .fv-14:not(:has(#fv-14-theme-dark:checked)) {
    --paper: #f5f1e8;
    --surface: #fdfbf6;
    --ink: #14120f;
    --muted: #5f584e;
    --rule: #c9c2b4;
    --focus: #14120f;
    --error-tone: #a63a12;
    --ok-tone: #2f6b34;
  }

  .fv-14:not(:has(#fv-14-theme-dark:checked)) .fv-14__input::placeholder {
    color: #9b9285;
  }

  .fv-14:not(:has(#fv-14-theme-dark:checked)):has(.fv-14__switch:checked) {
    --paper: #ffffff;
    --surface: #ffffff;
    --ink: #000000;
    --muted: #000000;
    --rule: #000000;
    --focus: #0000ff;
    --error-tone: #d40000;
    --ok-tone: #006600;
  }

  .fv-14:not(:has(#fv-14-theme-dark:checked)):has(.fv-14__switch:checked) .fv-14__msg {
    color: #d40000;
  }

  .fv-14:not(:has(#fv-14-theme-dark:checked)):has(.fv-14__switch:checked) .fv-14__input:user-invalid,
    .fv-14:not(:has(#fv-14-theme-dark:checked)):has(.fv-14__switch:checked) .fv-14__input:invalid:not(:placeholder-shown):not(:focus) {
    border-color: #d40000;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-14:not(:has(#fv-14-theme-light:checked)):has(.fv-14__switch:checked) {
    --paper: #000000;
    --surface: #000000;
    --ink: #ffffff;
    --muted: #ffffff;
    --rule: #ffffff;
    --focus: #ffff00;
    --error-tone: #ffff00;
    --ok-tone: #00ff00;
  }

  .fv-14:not(:has(#fv-14-theme-light:checked)):has(.fv-14__switch:checked) .fv-14__msg {
    color: #ffff00;
  }
}

[data-theme="dark"] .fv-14:not(:has(#fv-14-theme-light:checked)) {
  --paper: #12100e;
  --surface: #1a1714;
  --ink: #f4efe6;
  --muted: #a89f92;
  --rule: #3a342d;
  --focus: #f4efe6;
  --error-tone: #ff8f6b;
  --ok-tone: #96c48a;
}

.fv-14 {
  position: relative;
}

.fv-14__stage {
  padding-block-start: 4.75rem;
}

.fv-14__theme {
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

.fv-14__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-14__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-14__themeopt {
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

.fv-14__themeopt:hover {
  opacity: 0.85;
}

.fv-14__themeinput:checked + .fv-14__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-14__themeinput:focus-visible + .fv-14__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-14__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-14__themeinput:checked + .fv-14__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-14:has(#fv-14-theme-light:checked) {
  --paper: #f5f1e8;
  --surface: #fdfbf6;
  --ink: #14120f;
  --muted: #5f584e;
  --rule: #c9c2b4;
  --focus: #14120f;
  --error-tone: #a63a12;
  --ok-tone: #2f6b34;
}

.fv-14:has(#fv-14-theme-light:checked) .fv-14__input::placeholder {
  color: #9b9285;
}

.fv-14:has(#fv-14-theme-light:checked):has(.fv-14__switch:checked) {
  --paper: #ffffff;
  --surface: #ffffff;
  --ink: #000000;
  --muted: #000000;
  --rule: #000000;
  --focus: #0000ff;
  --error-tone: #d40000;
  --ok-tone: #006600;
}

.fv-14:has(#fv-14-theme-light:checked):has(.fv-14__switch:checked) .fv-14__msg {
  color: #d40000;
}

.fv-14:has(#fv-14-theme-light:checked):has(.fv-14__switch:checked) .fv-14__input:user-invalid,
.fv-14:has(#fv-14-theme-light:checked):has(.fv-14__switch:checked) .fv-14__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: #d40000;
}
```
