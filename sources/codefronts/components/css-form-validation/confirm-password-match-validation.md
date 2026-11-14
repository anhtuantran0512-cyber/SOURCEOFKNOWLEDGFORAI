---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/confirm-password-match-validation/"
title: "Confirm Password Match Validation"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "Two password fields and one question: do they match."
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Confirm Password Match Validation
Source: https://codefronts.com/components/css-form-validation/confirm-password-match-validation/

Two password fields and one question: do they match. Fifteen lines call setCustomValidity() on the confirm field whenever either input changes, which hands the verdict to the browser's own constraint system — so :user-invalid styles it, checkValidity() respects it, and the native message says the right thing. The match indicator between the fields updates live; the error message waits for blur.
## HTML
```html
<section class="fv-07" aria-labelledby="fv-07-h">
  <fieldset class="fv-07__theme">
    <legend class="fv-07__themelegend">Theme</legend>
    <input class="fv-07__themeinput" type="radio" name="fv-07-theme" id="fv-07-theme-auto" checked>
    <label class="fv-07__themeopt" for="fv-07-theme-auto">Auto</label>
    <input class="fv-07__themeinput" type="radio" name="fv-07-theme" id="fv-07-theme-light">
    <label class="fv-07__themeopt" for="fv-07-theme-light">Light</label>
    <input class="fv-07__themeinput" type="radio" name="fv-07-theme" id="fv-07-theme-dark">
    <label class="fv-07__themeopt" for="fv-07-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-07__stage">
    <form class="fv-07__form" aria-labelledby="fv-07-h">
      <header class="fv-07__head">
        <p class="fv-07__eyebrow">Quill · reset your password</p>
        <h2 class="fv-07__h" id="fv-07-h">Let the browser hold the verdict</h2>
      </header>

      <div class="fv-07__field">
        <label class="fv-07__label" for="fv-07-pw">New password</label>
        <input class="fv-07__input" id="fv-07-pw" name="fv-07-pw" type="password" required minlength="8" autocomplete="new-password" placeholder="At least 8 characters" value="quill-atrium-84" aria-describedby="fv-07-pw-msg">
        <p class="fv-07__msg" id="fv-07-pw-msg">
          <svg class="fv-07__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Password must be at least 8 characters</span>
        </p>
      </div>

      <p class="fv-07__state" aria-hidden="true">
        <span class="fv-07__link"></span>
        <span class="fv-07__statetext" data-idle>Type it twice — we compare on every keystroke, quietly</span>
        <span class="fv-07__statetext" data-yes>
          <svg class="fv-07__stateicon" viewBox="0 0 20 20" focusable="false"><path d="M4 10.6l4 3.9L16 5.8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
          Both entries match
        </span>
        <span class="fv-07__statetext" data-no>
          <svg class="fv-07__stateicon" viewBox="0 0 20 20" focusable="false"><path d="M6 6l8 8M14 6l-8 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg>
          Not matching yet
        </span>
      </p>

      <div class="fv-07__field">
        <label class="fv-07__label" for="fv-07-confirm">Confirm password</label>
        <input class="fv-07__input fv-07__input--confirm" id="fv-07-confirm" name="fv-07-confirm" type="password" required autocomplete="new-password" placeholder="Repeat the password" value="quill-atrium-48" aria-describedby="fv-07-confirm-msg">
        <p class="fv-07__msg" id="fv-07-confirm-msg">
          <svg class="fv-07__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Both passwords must match exactly — check for a stray capital or trailing space</span>
        </p>
      </div>

      <div class="fv-07__foot">
        <button class="fv-07__btn" type="button">Set new password</button>
        <p class="fv-07__result" role="status"></p>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-07 {
  --page: #efe7dd;
  --surface-1: #f8f2ea;
  --surface-2: #f2e9de;
  --ink: #2c241c;
  --muted: #756455;
  --rule: #ddcfbe;
  --accent: #8a5a3b;
  --ok: #4a7350;
  --error: #a63f2b;
  --error-ink: #8b3220;
  --font-display: "Charter", "Iowan Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-07 {
    --accent: oklch(0.48 0.09 50);
    --ok: oklch(0.52 0.08 148);
    --error: oklch(0.48 0.16 32);
    --error-ink: oklch(0.41 0.16 32);
  }
}

.fv-07 *,
.fv-07 *::before,
.fv-07 *::after {
  box-sizing: border-box;
}

.fv-07__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 3.5rem) clamp(1rem, 4vw, 2.5rem);
}

.fv-07__form {
  inline-size: min(100%, 29rem);
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
  padding: clamp(1.25rem, 4vw, 1.875rem);
  background: var(--surface-1);
  border: 1px solid var(--rule);
  border-radius: 0.25rem;
}

.fv-07__head {
  min-inline-size: 0;
  margin-block-end: 0.25rem;
}

.fv-07__eyebrow {
  margin: 0 0 0.5rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-07__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 3.6vw, 1.75rem);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
}

.fv-07__field {
  display: grid;
  gap: 0.4375rem;
  min-inline-size: 0;
}

.fv-07__label {
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.fv-07__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.875rem;
  padding: 0 0.875rem;
  font: inherit;
  font-size: 0.9375rem;
  letter-spacing: 0.02em;
  color: var(--ink);
  background: #fdfaf5;
  border: 1px solid var(--rule);
  border-radius: 0.25rem;
  transition: border-color 0.16s ease;
}

.fv-07__input::placeholder {
  color: #b3a291;
}

.fv-07__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-07__state {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: 0.5rem;
  margin: 0;
  min-inline-size: 0;
  padding: 0.5rem 0.6875rem;
  background: var(--surface-2);
  border-radius: 0.25rem;
  font-size: 0.8125rem;
  line-height: 1.4;
  color: var(--muted);
}

.fv-07__link {
  inline-size: 0.5rem;
  block-size: 0.5rem;
  border-radius: 50%;
  background: var(--muted);
}

.fv-07__statetext {
  display: none;
  align-items: center;
  gap: 0.375rem;
  min-inline-size: 0;
}

.fv-07__stateicon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
}

.fv-07__form[data-match="idle"] .fv-07__statetext[data-idle] {
  display: flex;
}

.fv-07__form[data-match="yes"] .fv-07__statetext[data-yes] {
  display: flex;
  color: var(--ok);
  font-weight: 600;
}

.fv-07__form[data-match="yes"] .fv-07__link {
  background: var(--ok);
}

.fv-07__form[data-match="no"] .fv-07__statetext[data-no] {
  display: flex;
  color: var(--error-ink);
  font-weight: 600;
}

.fv-07__form[data-match="no"] .fv-07__link {
  background: var(--error);
}

.fv-07__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--error-ink);
}

.fv-07__msg span {
  min-inline-size: 0;
}

.fv-07__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-07__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  background: #fbeee9;
}

.fv-07__input:invalid:not(:placeholder-shown):not(:focus) + .fv-07__msg {
  display: flex;
}

.fv-07__input:user-invalid:not(:focus) {
  border-color: var(--error);
  background: #fbeee9;
}

.fv-07__input:user-invalid:not(:focus) + .fv-07__msg {
  display: flex;
}

.fv-07__input:user-valid {
  border-color: var(--ok);
}

.fv-07__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1rem;
  min-inline-size: 0;
  margin-block-start: 0.25rem;
}

.fv-07__btn {
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  padding: 0.6875rem 1.25rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #fdfaf5;
  background: var(--ink);
  border: 0;
  border-radius: 0.25rem;
  cursor: pointer;
}

.fv-07__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fv-07__result {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.4;
  color: var(--ok);
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .fv-07__input {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-07:not(:has(#fv-07-theme-light:checked)) {
    --page: #1a1512;
    --surface-1: #221c17;
    --surface-2: #2a221b;
    --ink: #f0e6da;
    --muted: #a89684;
    --rule: #3a2f26;
    --accent: #dba46f;
    --ok: #7fc48d;
    --error: #ff8a6d;
    --error-ink: #ffa88f;
  }

  .fv-07:not(:has(#fv-07-theme-light:checked)) .fv-07__input {
    background: #1d1814;
  }

  .fv-07:not(:has(#fv-07-theme-light:checked)) .fv-07__input::placeholder {
    color: #6f6154;
  }

  .fv-07:not(:has(#fv-07-theme-light:checked)) .fv-07__input:invalid:not(:placeholder-shown):not(:focus),
    .fv-07:not(:has(#fv-07-theme-light:checked)) .fv-07__input:user-invalid:not(:focus) {
    background: #2b1a14;
  }

  .fv-07:not(:has(#fv-07-theme-light:checked)) .fv-07__btn {
    color: #1a1512;
    background: #f0e6da;
  }
}

[data-theme="dark"] .fv-07:not(:has(#fv-07-theme-light:checked)) {
  --page: #1a1512;
  --surface-1: #221c17;
  --surface-2: #2a221b;
  --ink: #f0e6da;
  --muted: #a89684;
  --rule: #3a2f26;
  --accent: #dba46f;
  --ok: #7fc48d;
  --error: #ff8a6d;
  --error-ink: #ffa88f;
}

[data-theme="dark"] .fv-07:not(:has(#fv-07-theme-light:checked)) .fv-07__input {
  background: #1d1814;
}

[data-theme="dark"] .fv-07:not(:has(#fv-07-theme-light:checked)) .fv-07__btn {
  color: #1a1512;
  background: #f0e6da;
}

.fv-07 {
  position: relative;
}

.fv-07__stage {
  padding-block-start: 4.75rem;
}

.fv-07__theme {
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

.fv-07__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-07__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-07__themeopt {
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

.fv-07__themeopt:hover {
  opacity: 0.85;
}

.fv-07__themeinput:checked + .fv-07__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-07__themeinput:focus-visible + .fv-07__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-07__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-07__themeinput:checked + .fv-07__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-07:has(#fv-07-theme-dark:checked) {
  --page: #1a1512;
  --surface-1: #221c17;
  --surface-2: #2a221b;
  --ink: #f0e6da;
  --muted: #a89684;
  --rule: #3a2f26;
  --accent: #dba46f;
  --ok: #7fc48d;
  --error: #ff8a6d;
  --error-ink: #ffa88f;
}

.fv-07:has(#fv-07-theme-dark:checked) .fv-07__input {
  background: #1d1814;
}

.fv-07:has(#fv-07-theme-dark:checked) .fv-07__input::placeholder {
  color: #6f6154;
}

.fv-07:has(#fv-07-theme-dark:checked) .fv-07__input:invalid:not(:placeholder-shown):not(:focus),
.fv-07:has(#fv-07-theme-dark:checked) .fv-07__input:user-invalid:not(:focus) {
  background: #2b1a14;
}

.fv-07:has(#fv-07-theme-dark:checked) .fv-07__btn {
  color: #1a1512;
  background: #f0e6da;
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-07__form');
  if (!form || form.dataset.fv07) return;
  form.dataset.fv07 = '1';
  const pw = form.querySelector('#fv-07-pw');
  const confirm = form.querySelector('#fv-07-confirm');
  const result = form.querySelector('.fv-07__result');
  const sync = () => {
    const mismatch = confirm.value !== '' && confirm.value !== pw.value;
    confirm.setCustomValidity(mismatch ? 'Both passwords must match exactly.' : '');
    confirm.setAttribute('aria-invalid', mismatch ? 'true' : 'false');
    form.dataset.match = confirm.value === '' ? 'idle' : mismatch ? 'no' : 'yes';
  };
  const submit = () => {
    sync();
    const ok = form.checkValidity();
    result.textContent = ok ? 'Password updated for Quill.' : '';
    if (!ok) form.reportValidity();
  };
  [pw, confirm].forEach((el) => el.addEventListener('input', () => { sync(); result.textContent = ''; }));
  form.querySelector('.fv-07__btn').addEventListener('click', submit);
  [pw, confirm].forEach((el) => el.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); submit(); } }));
  sync();
})();
```
