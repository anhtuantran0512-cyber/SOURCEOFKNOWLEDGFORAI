---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/compact-signup-form-validation/"
title: "Compact Signup Form Validation"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "A complete signup form in a 380px column that validates without feeling hostile: errors appear on blur, never on keystroke, and the submit button is never…"
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compact Signup Form Validation
Source: https://codefronts.com/components/css-form-validation/compact-signup-form-validation/

A complete signup form in a 380px column that validates without feeling hostile: errors appear on blur, never on keystroke, and the submit button is never disabled. A disabled button gives the user nothing to press and no explanation of why — so this one stays live, reports what is wrong, and moves focus to the first field that needs work.
## HTML
```html
<section class="fv-16" aria-labelledby="fv-16-h">
  <fieldset class="fv-16__theme">
    <legend class="fv-16__themelegend">Theme</legend>
    <input class="fv-16__themeinput" type="radio" name="fv-16-theme" id="fv-16-theme-auto" checked>
    <label class="fv-16__themeopt" for="fv-16-theme-auto">Auto</label>
    <input class="fv-16__themeinput" type="radio" name="fv-16-theme" id="fv-16-theme-light">
    <label class="fv-16__themeopt" for="fv-16-theme-light">Light</label>
    <input class="fv-16__themeinput" type="radio" name="fv-16-theme" id="fv-16-theme-dark">
    <label class="fv-16__themeopt" for="fv-16-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-16__stage">
    <form class="fv-16__form" aria-labelledby="fv-16-h">
      <header class="fv-16__head">
        <h2 class="fv-16__h" id="fv-16-h">Create your Meridian account</h2>
        <p class="fv-16__sub">Free for 14 days. No card needed.</p>
      </header>

      <div class="fv-16__field">
        <label class="fv-16__label" for="fv-16-name">Full name</label>
        <input class="fv-16__input" id="fv-16-name" name="fv-16-name" type="text" required autocomplete="name" placeholder="Priya Sharma" aria-describedby="fv-16-name-msg">
        <p class="fv-16__msg" id="fv-16-name-msg" hidden>
          <svg class="fv-16__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Enter your name so teammates can find you</span>
        </p>
      </div>

      <div class="fv-16__field">
        <label class="fv-16__label" for="fv-16-email">Work email</label>
        <input class="fv-16__input" id="fv-16-email" name="fv-16-email" type="email" required autocomplete="email" placeholder="[email protected]" aria-describedby="fv-16-email-msg">
        <p class="fv-16__msg" id="fv-16-email-msg" hidden>
          <svg class="fv-16__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Enter a valid work email address, like [email protected]</span>
        </p>
      </div>

      <div class="fv-16__field">
        <label class="fv-16__label" for="fv-16-pw">Password</label>
        <input class="fv-16__input" id="fv-16-pw" name="fv-16-pw" type="password" required minlength="10" autocomplete="new-password" placeholder="At least 10 characters" aria-describedby="fv-16-pw-msg">
        <p class="fv-16__msg" id="fv-16-pw-msg" hidden>
          <svg class="fv-16__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Password must be at least 10 characters</span>
        </p>
      </div>

      <div class="fv-16__terms">
        <input class="fv-16__check" id="fv-16-terms" name="fv-16-terms" type="checkbox" required aria-describedby="fv-16-terms-msg">
        <label class="fv-16__checklabel" for="fv-16-terms">I accept the Meridian terms and privacy notice</label>
        <p class="fv-16__msg" id="fv-16-terms-msg" hidden>
          <svg class="fv-16__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>You need to accept the terms before we can create the account</span>
        </p>
      </div>

      <button class="fv-16__btn" type="button">Create account</button>
      <p class="fv-16__status" role="status">The button is never disabled. Press it and it tells you what is missing.</p>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-16 {
  --page: #f4f4f5;
  --surface: #ffffff;
  --field: #fafafa;
  --ink: #18181b;
  --muted: #62626b;
  --rule: #dcdce1;
  --accent: #4338ca;
  --error: #be1e4f;
  --error-ink: #9d1741;
  --gap: 0.75rem;
  --radius: 0.5rem;
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
  .fv-16 {
    --accent: oklch(0.45 0.22 285);
    --error: oklch(0.48 0.2 2);
    --error-ink: oklch(0.41 0.2 2);
  }
}

.fv-16 *,
.fv-16 *::before,
.fv-16 *::after {
  box-sizing: border-box;
}

.fv-16 [hidden] {
  display: none;
}

.fv-16__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3rem) 1rem;
}

.fv-16__form {
  inline-size: min(100%, 23.75rem);
  min-inline-size: 0;
  display: grid;
  gap: var(--gap);
  padding: 1.25rem;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  box-shadow: 0 1px 2px rgba(24, 24, 27, 0.05), 0 12px 28px -22px rgba(24, 24, 27, 0.6);
}

.fv-16__head {
  min-inline-size: 0;
  margin-block-end: 0.125rem;
}

.fv-16__h {
  margin: 0 0 0.25rem;
  font-family: var(--font-display);
  font-size: 1.1875rem;
  font-weight: 620;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.fv-16__sub {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-16__field {
  display: grid;
  gap: 0.25rem;
  min-inline-size: 0;
}

.fv-16__label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.fv-16__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.75rem;
  padding: 0 0.75rem;
  font: inherit;
  font-size: 0.875rem;
  color: var(--ink);
  background: var(--field);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
}

.fv-16__input::placeholder {
  color: #a1a1aa;
}

.fv-16__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-16__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
}

.fv-16__input:user-invalid:not(:focus) {
  border-color: var(--error);
}

.fv-16__input[aria-invalid="true"] {
  border-color: var(--error);
  background: #fdf2f5;
}

.fv-16__input:user-valid {
  border-color: #2d7a53;
}

.fv-16__terms {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: 0.5rem;
  min-block-size: 2.75rem;
  min-inline-size: 0;
  margin-block-start: 0.125rem;
}

.fv-16__check {
  inline-size: 1.125rem;
  block-size: 1.125rem;
  margin: 0;
  accent-color: var(--accent);
}

.fv-16__check:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fv-16__checklabel {
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.4;
}

.fv-16__terms .fv-16__msg {
  grid-column: 1 / -1;
}

.fv-16__msg {
  display: flex;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0.0625rem 0 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.4;
  color: var(--error-ink);
}

.fv-16__msg span {
  min-inline-size: 0;
}

.fv-16__icon {
  flex: none;
  inline-size: 0.9375rem;
  block-size: 0.9375rem;
  margin-block-start: 0.08rem;
}

.fv-16__btn {
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  margin-block-start: 0.25rem;
  padding: 0.6875rem 1rem;
  font: inherit;
  font-size: 0.875rem;
  font-weight: 620;
  color: #ffffff;
  background: var(--accent);
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  transition: background-color 0.15s ease;
}

.fv-16__btn:hover {
  background: #372fb0;
}

.fv-16__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.fv-16__status {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-16__status[data-tone="bad"] {
  color: var(--error-ink);
  font-weight: 600;
}

.fv-16__status[data-tone="good"] {
  color: #2d7a53;
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .fv-16__btn {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-16:not(:has(#fv-16-theme-light:checked)) {
    --page: #09090b;
    --surface: #131316;
    --field: #0f0f12;
    --ink: #f2f2f4;
    --muted: #9c9ca6;
    --rule: #2a2a30;
    --accent: #8b83ff;
    --error: #ff6f96;
    --error-ink: #ff93af;
  }

  .fv-16:not(:has(#fv-16-theme-light:checked)) .fv-16__input::placeholder {
    color: #6b6b75;
  }

  .fv-16:not(:has(#fv-16-theme-light:checked)) .fv-16__input[aria-invalid="true"] {
    background: #22101a;
  }

  .fv-16:not(:has(#fv-16-theme-light:checked)) .fv-16__btn {
    color: #0c0b1a;
  }

  .fv-16:not(:has(#fv-16-theme-light:checked)) .fv-16__btn:hover {
    background: #a49dff;
  }

  .fv-16:not(:has(#fv-16-theme-light:checked)) .fv-16__status[data-tone="good"] {
    color: #58c48c;
  }
}

[data-theme="dark"] .fv-16:not(:has(#fv-16-theme-light:checked)) {
  --page: #09090b;
  --surface: #131316;
  --field: #0f0f12;
  --ink: #f2f2f4;
  --muted: #9c9ca6;
  --rule: #2a2a30;
  --accent: #8b83ff;
  --error: #ff6f96;
  --error-ink: #ff93af;
}

[data-theme="dark"] .fv-16:not(:has(#fv-16-theme-light:checked)) .fv-16__btn {
  color: #0c0b1a;
}

[data-theme="dark"] .fv-16:not(:has(#fv-16-theme-light:checked)) .fv-16__input[aria-invalid="true"] {
  background: #22101a;
}

.fv-16 {
  position: relative;
}

.fv-16__stage {
  padding-block-start: 4.75rem;
}

.fv-16__theme {
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

.fv-16__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-16__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-16__themeopt {
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

.fv-16__themeopt:hover {
  opacity: 0.85;
}

.fv-16__themeinput:checked + .fv-16__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-16__themeinput:focus-visible + .fv-16__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-16__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-16__themeinput:checked + .fv-16__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-16:has(#fv-16-theme-dark:checked) {
  --page: #09090b;
  --surface: #131316;
  --field: #0f0f12;
  --ink: #f2f2f4;
  --muted: #9c9ca6;
  --rule: #2a2a30;
  --accent: #8b83ff;
  --error: #ff6f96;
  --error-ink: #ff93af;
}

.fv-16:has(#fv-16-theme-dark:checked) .fv-16__input::placeholder {
  color: #6b6b75;
}

.fv-16:has(#fv-16-theme-dark:checked) .fv-16__input[aria-invalid="true"] {
  background: #22101a;
}

.fv-16:has(#fv-16-theme-dark:checked) .fv-16__btn {
  color: #0c0b1a;
}

.fv-16:has(#fv-16-theme-dark:checked) .fv-16__btn:hover {
  background: #a49dff;
}

.fv-16:has(#fv-16-theme-dark:checked) .fv-16__status[data-tone="good"] {
  color: #58c48c;
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-16__form');
  if (!form || form.dataset.fv16) return;
  form.dataset.fv16 = '1';
  const status = form.querySelector('.fv-16__status');
  const fields = [...form.querySelectorAll('.fv-16__input, .fv-16__check')];
  const mark = (el) => {
    const bad = !el.checkValidity();
    const msg = document.getElementById(el.getAttribute('aria-describedby'));
    if (bad) el.setAttribute('aria-invalid', 'true');
    else el.removeAttribute('aria-invalid');
    if (msg) msg.hidden = !bad;
    return bad;
  };
  fields.forEach((el) => {
    el.addEventListener('blur', () => mark(el));
    el.addEventListener('change', () => { if (el.type === 'checkbox') mark(el); });
    el.addEventListener('input', () => { if (el.getAttribute('aria-invalid') === 'true') mark(el); });
  });
  const submit = () => {
    const bad = fields.filter(mark);
    status.dataset.tone = bad.length ? 'bad' : 'good';
    status.textContent = bad.length
      ? bad.length + ' field(s) still need attention — starting with ' + (form.querySelector('label[for="' + bad[0].id + '"]').textContent) + '.'
      : 'Account created. Check your inbox for the confirmation link.';
    if (bad.length) bad[0].focus();
  };
  form.querySelector('.fv-16__btn').addEventListener('click', submit);
  form.addEventListener('keydown', (e) => { if (e.key === 'Enter' && e.target.tagName === 'INPUT') { e.preventDefault(); submit(); } });
})();
```
