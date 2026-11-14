---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/success-checkmark-on-valid-input/"
title: "Success Checkmark on Valid Input"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "A checkmark that draws itself in when the field becomes valid, driven by :user-valid and a stroke-dasharray animation."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Success Checkmark on Valid Input
Source: https://codefronts.com/components/css-form-validation/success-checkmark-on-valid-input/

A checkmark that draws itself in when the field becomes valid, driven by :user-valid and a stroke-dasharray animation. The technique is easy; the judgement is the point. Confirming every field turns a form into a scoreboard, so this demo confirms only the two fields where success is genuinely news — an available username and a verified card postcode — and leaves the rest silent.
## HTML
```html
<section class="fv-06" aria-labelledby="fv-06-h">
  <fieldset class="fv-06__theme">
    <legend class="fv-06__themelegend">Theme</legend>
    <input class="fv-06__themeinput" type="radio" name="fv-06-theme" id="fv-06-theme-auto" checked>
    <label class="fv-06__themeopt" for="fv-06-theme-auto">Auto</label>
    <input class="fv-06__themeinput" type="radio" name="fv-06-theme" id="fv-06-theme-light">
    <label class="fv-06__themeopt" for="fv-06-theme-light">Light</label>
    <input class="fv-06__themeinput" type="radio" name="fv-06-theme" id="fv-06-theme-dark">
    <label class="fv-06__themeopt" for="fv-06-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-06__stage">
    <div class="fv-06__panel">
      <header class="fv-06__head">
        <p class="fv-06__eyebrow">Nova · claim your handle</p>
        <h2 class="fv-06__h" id="fv-06-h">Confirm the fields where the answer was in doubt</h2>
        <p class="fv-06__sub">Two of these three earn a tick. The third never needed one.</p>
      </header>

      <form class="fv-06__form" aria-labelledby="fv-06-h">
        <div class="fv-06__field fv-06__field--confirm">
          <label class="fv-06__label" for="fv-06-handle">Workspace handle</label>
          <div class="fv-06__wrap">
            <input class="fv-06__input" id="fv-06-handle" name="fv-06-handle" type="text" required pattern="[a-z0-9-]{4,20}" placeholder="nova-data" value="nova-data" autocomplete="off" spellcheck="false" aria-describedby="fv-06-handle-msg">
            <svg class="fv-06__check" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4.5 12.6l4.7 4.6L19.5 6.9" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></svg>
          </div>
          <p class="fv-06__ok">nova-data is available on Nova</p>
          <p class="fv-06__msg" id="fv-06-handle-msg">
            <svg class="fv-06__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Use 4–20 lowercase letters, numbers or hyphens</span>
          </p>
        </div>

        <div class="fv-06__field fv-06__field--confirm">
          <label class="fv-06__label" for="fv-06-post">Billing postcode</label>
          <div class="fv-06__wrap">
            <input class="fv-06__input" id="fv-06-post" name="fv-06-post" type="text" required pattern="[A-Za-z0-9 ]{5,8}" placeholder="EC2A 4NE" value="EC2A 4NE" autocomplete="postal-code" aria-describedby="fv-06-post-msg">
            <svg class="fv-06__check" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4.5 12.6l4.7 4.6L19.5 6.9" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></svg>
          </div>
          <p class="fv-06__ok">Matches the postcode on file for this card</p>
          <p class="fv-06__msg" id="fv-06-post-msg">
            <svg class="fv-06__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Enter the postcode registered to your payment card</span>
          </p>
        </div>

        <div class="fv-06__field">
          <label class="fv-06__label" for="fv-06-name">Display name</label>
          <div class="fv-06__wrap">
            <input class="fv-06__input" id="fv-06-name" name="fv-06-name" type="text" required placeholder="Sam Rivera" value="Sam Rivera" autocomplete="name">
          </div>
          <p class="fv-06__quiet">No tick here on purpose — you already knew this one was right.</p>
        </div>

        <button class="fv-06__btn" type="button">Create workspace</button>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-06 {
  --page: #eef4f1;
  --surface: #ffffff;
  --ink: #16211d;
  --muted: #566a63;
  --rule: #dbe6e1;
  --accent: #0f6b57;
  --success: #10896b;
  --success-bg: #e7f6f0;
  --error: #b8323f;
  --error-ink: #97222f;
  --pad: 1.625rem;
  --lift: 0 14px 0 -8px rgba(22, 33, 29, 0.08), 0 22px 44px -30px rgba(22, 33, 29, 0.5);
  --font-display: "Geist", "Inter Tight", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-06 {
    --accent: oklch(0.44 0.1 172);
    --success: oklch(0.53 0.12 168);
    --success-bg: oklch(0.96 0.03 168);
    --error: oklch(0.5 0.17 18);
    --error-ink: oklch(0.43 0.17 18);
  }
}

.fv-06 *,
.fv-06 *::before,
.fv-06 *::after {
  box-sizing: border-box;
}

.fv-06__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 4rem) clamp(1rem, 4vw, 2.5rem);
}

.fv-06__panel {
  inline-size: min(100%, 33rem);
  min-inline-size: 0;
  padding: var(--pad);
  background: var(--surface);
  border: 0;
  border-radius: 1.25rem;
  box-shadow: var(--lift);
}

.fv-06__head {
  margin-block-end: 1.5rem;
  min-inline-size: 0;
}

.fv-06__eyebrow {
  margin: 0 0 0.625rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-06__h {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 3.4vw, 1.6rem);
  font-weight: 620;
  line-height: 1.2;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fv-06__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.55;
  color: var(--muted);
}

.fv-06__form {
  display: grid;
  gap: 1.5rem;
  min-inline-size: 0;
}

.fv-06__field {
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
}

.fv-06__label {
  font-size: 0.875rem;
  font-weight: 600;
}

.fv-06__wrap {
  position: relative;
  display: grid;
  min-inline-size: 0;
}

.fv-06__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 3rem;
  padding: 0 3rem 0 0.9375rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: #fbfdfc;
  border: 1px solid var(--rule);
  border-radius: 0.625rem;
  transition: border-color 0.18s ease;
}

.fv-06__input::placeholder {
  color: #9aaba5;
}

.fv-06__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-06__check {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-end: 0.875rem;
  translate: 0 -50%;
  inline-size: 1.375rem;
  block-size: 1.375rem;
  color: var(--success);
  opacity: 0;
  pointer-events: none;
}

.fv-06__check path {
  stroke-dasharray: 26;
  stroke-dashoffset: 26;
}

@keyframes fv-06-draw {
  from {
    stroke-dashoffset: 26;
  }

  to {
    stroke-dashoffset: 0;
  }
}

.fv-06__ok,
.fv-06__msg {
  display: none;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
}

.fv-06__ok {
  align-items: center;
  gap: 0.375rem;
  padding: 0.3125rem 0.5rem;
  border-radius: 0.375rem;
  background: var(--success-bg);
  color: #0c5f4b;
  font-weight: 550;
}

.fv-06__msg {
  gap: 0.375rem;
  align-items: flex-start;
  color: var(--error-ink);
}

.fv-06__msg span {
  min-inline-size: 0;
}

.fv-06__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-06__quiet {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-06__field--confirm .fv-06__input:valid:not(:placeholder-shown) {
  border-color: var(--success);
}

.fv-06__field--confirm .fv-06__input:valid:not(:placeholder-shown) ~ .fv-06__check {
  opacity: 1;
}

.fv-06__field--confirm .fv-06__input:valid:not(:placeholder-shown) ~ .fv-06__check path {
  animation: fv-06-draw 0.5s cubic-bezier(0.25, 1, 0.4, 1) forwards;
}

.fv-06__field--confirm .fv-06__input:valid:not(:placeholder-shown) ~ .fv-06__ok {
  display: flex;
}

.fv-06__field--confirm .fv-06__input:user-valid {
  border-color: var(--success);
}

.fv-06__field--confirm .fv-06__input:user-valid ~ .fv-06__check {
  opacity: 1;
}

.fv-06__field--confirm .fv-06__input:user-valid ~ .fv-06__check path {
  animation: fv-06-draw 0.5s cubic-bezier(0.25, 1, 0.4, 1) forwards;
}

.fv-06__field--confirm .fv-06__input:user-valid ~ .fv-06__ok {
  display: flex;
}

.fv-06__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
}

.fv-06__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-06__msg {
  display: flex;
}

.fv-06__input:user-invalid {
  border-color: var(--error);
}

.fv-06__input:user-invalid ~ .fv-06__msg {
  display: flex;
}

.fv-06__input:user-invalid ~ .fv-06__ok {
  display: none;
}

.fv-06__btn {
  justify-self: start;
  min-block-size: 2.875rem;
  min-inline-size: 44px;
  padding: 0.75rem 1.375rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #ffffff;
  background: var(--accent);
  border: 0;
  border-radius: 0.625rem;
  cursor: pointer;
  transition: background-color 0.16s ease;
}

.fv-06__btn:hover {
  background: #0b5544;
}

.fv-06__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .fv-06__input,
    .fv-06__btn {
    transition: none;
  }

  .fv-06__check path {
    animation: none;
    stroke-dashoffset: 0;
  }

  .fv-06__field--confirm .fv-06__input:user-valid ~ .fv-06__check path,
    .fv-06__field--confirm .fv-06__input:valid:not(:placeholder-shown) ~ .fv-06__check path {
    animation: none;
    stroke-dashoffset: 0;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-06:not(:has(#fv-06-theme-light:checked)) {
    --page: #0b1310;
    --surface: #121b18;
    --ink: #e6f1ec;
    --muted: #92a8a0;
    --rule: #223029;
    --accent: #4fd6ac;
    --success: #4fd6ac;
    --success-bg: #10261f;
    --error: #ff7b88;
    --error-ink: #ff9aa4;
    --lift: 0 14px 0 -8px rgba(0, 0, 0, 0.4), 0 22px 44px -30px rgba(0, 0, 0, 0.9);
  }

  .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__input {
    background: #0e1614;
  }

  .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__input::placeholder {
    color: #64786f;
  }

  .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__ok {
    color: #8ce8c6;
  }

  .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__btn {
    color: #06130f;
  }

  .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__btn:hover {
    background: #6ee5c0;
  }
}

[data-theme="dark"] .fv-06:not(:has(#fv-06-theme-light:checked)) {
  --page: #0b1310;
  --surface: #121b18;
  --ink: #e6f1ec;
  --muted: #92a8a0;
  --rule: #223029;
  --accent: #4fd6ac;
  --success: #4fd6ac;
  --success-bg: #10261f;
  --error: #ff7b88;
  --error-ink: #ff9aa4;
}

[data-theme="dark"] .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__input {
  background: #0e1614;
}

[data-theme="dark"] .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__btn {
  color: #06130f;
}

[data-theme="dark"] .fv-06:not(:has(#fv-06-theme-light:checked)) .fv-06__ok {
  color: #8ce8c6;
}

.fv-06 {
  position: relative;
}

.fv-06__stage {
  padding-block-start: 4.75rem;
}

.fv-06__theme {
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

.fv-06__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-06__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-06__themeopt {
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

.fv-06__themeopt:hover {
  opacity: 0.85;
}

.fv-06__themeinput:checked + .fv-06__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-06__themeinput:focus-visible + .fv-06__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-06__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-06__themeinput:checked + .fv-06__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-06:has(#fv-06-theme-dark:checked) {
  --page: #0b1310;
  --surface: #121b18;
  --ink: #e6f1ec;
  --muted: #92a8a0;
  --rule: #223029;
  --accent: #4fd6ac;
  --success: #4fd6ac;
  --success-bg: #10261f;
  --error: #ff7b88;
  --error-ink: #ff9aa4;
  --lift: 0 14px 0 -8px rgba(0, 0, 0, 0.4), 0 22px 44px -30px rgba(0, 0, 0, 0.9);
}

.fv-06:has(#fv-06-theme-dark:checked) .fv-06__input {
  background: #0e1614;
}

.fv-06:has(#fv-06-theme-dark:checked) .fv-06__input::placeholder {
  color: #64786f;
}

.fv-06:has(#fv-06-theme-dark:checked) .fv-06__ok {
  color: #8ce8c6;
}

.fv-06:has(#fv-06-theme-dark:checked) .fv-06__btn {
  color: #06130f;
}

.fv-06:has(#fv-06-theme-dark:checked) .fv-06__btn:hover {
  background: #6ee5c0;
}
```
