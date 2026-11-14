---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/error-announcement-with-live-region/"
title: "Error Announcement with Live Region"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "role=\"alert\" and aria-live=\"polite\" are not interchangeable."
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Error Announcement with Live Region
Source: https://codefronts.com/components/css-form-validation/error-announcement-with-live-region/

role="alert" and aria-live="polite" are not interchangeable. A submit-time summary interrupts, because the user has just asked for something and needs the answer; a per-field error on blur waits its turn. This demo runs both, side by side, and prints every announcement into a visible transcript so you can inspect the behaviour without turning a screen reader on.
## HTML
```html
<section class="fv-13" aria-labelledby="fv-13-h">
  <fieldset class="fv-13__theme">
    <legend class="fv-13__themelegend">Theme</legend>
    <input class="fv-13__themeinput" type="radio" name="fv-13-theme" id="fv-13-theme-auto" checked>
    <label class="fv-13__themeopt" for="fv-13-theme-auto">Auto</label>
    <input class="fv-13__themeinput" type="radio" name="fv-13-theme" id="fv-13-theme-light">
    <label class="fv-13__themeopt" for="fv-13-theme-light">Light</label>
    <input class="fv-13__themeinput" type="radio" name="fv-13-theme" id="fv-13-theme-dark">
    <label class="fv-13__themeopt" for="fv-13-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-13__stage">
    <header class="fv-13__head">
      <p class="fv-13__eyebrow">Fern · volunteer signup</p>
      <h2 class="fv-13__h" id="fv-13-h">Assertive when they asked. Polite when they didn't.</h2>
    </header>

    <div class="fv-13__split">
      <form class="fv-13__form" aria-labelledby="fv-13-h">
        <p class="fv-13__alert" role="alert"></p>

        <div class="fv-13__field">
          <label class="fv-13__label" for="fv-13-name">Your name</label>
          <input class="fv-13__input" id="fv-13-name" name="fv-13-name" type="text" required autocomplete="name" placeholder="Sam Rivera" aria-describedby="fv-13-name-msg">
          <p class="fv-13__msg" id="fv-13-name-msg" hidden>
            <svg class="fv-13__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Enter the name you would like on your volunteer badge</span>
          </p>
        </div>

        <div class="fv-13__field">
          <label class="fv-13__label" for="fv-13-email">Email</label>
          <input class="fv-13__input" id="fv-13-email" name="fv-13-email" type="email" required autocomplete="email" placeholder="[email protected]" value="sam.rivera.example.org" aria-describedby="fv-13-email-msg">
          <p class="fv-13__msg" id="fv-13-email-msg" hidden>
            <svg class="fv-13__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Enter a valid email address so we can send the rota</span>
          </p>
        </div>

        <div class="fv-13__field">
          <label class="fv-13__label" for="fv-13-shift">Shifts per month</label>
          <input class="fv-13__input" id="fv-13-shift" name="fv-13-shift" type="number" required min="1" max="12" placeholder="2" aria-describedby="fv-13-shift-msg">
          <p class="fv-13__msg" id="fv-13-shift-msg" hidden>
            <svg class="fv-13__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Choose between 1 and 12 shifts a month</span>
          </p>
        </div>

        <p class="fv-13__polite" aria-live="polite"></p>
        <button class="fv-13__btn" type="button">Sign me up</button>
      </form>

      <aside class="fv-13__transcript" aria-label="Announcement transcript">
        <div class="fv-13__thead">
          <h3 class="fv-13__ttitle">What a screen reader hears</h3>
          <p class="fv-13__tsub">Newest first. Politeness level shown per line.</p>
        </div>
        <ol class="fv-13__log"><li class="fv-13__empty">Nothing announced yet. Blur a field, or press Sign me up.</li></ol>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-13 {
  --page: #f2f0f9;
  --surface-1: #ffffff;
  --surface-2: #f7f5fd;
  --surface-3: #eeeafb;
  --ink: #1c1830;
  --muted: #5f5980;
  --rule: #ded8f2;
  --accent: #5b3fd6;
  --error: #c02a5c;
  --error-ink: #9d1f4b;
  --pad: 1.75rem;
  --font-display: "SF Pro Rounded", ui-rounded, "Segoe UI Variable Display", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-13 {
    --accent: oklch(0.48 0.2 288);
    --error: oklch(0.49 0.19 2);
    --error-ink: oklch(0.42 0.19 2);
  }
}

.fv-13 *,
.fv-13 *::before,
.fv-13 *::after {
  box-sizing: border-box;
}

.fv-13 [hidden] {
  display: none;
}

.fv-13__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 4rem) clamp(1rem, 4vw, 3rem);
}

.fv-13__head {
  inline-size: min(100%, 56rem);
  min-inline-size: 0;
  margin-block-end: clamp(1.25rem, 4vw, 2rem);
}

.fv-13__eyebrow {
  margin: 0 0 0.5rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-13__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 3.8vw, 2.05rem);
  font-weight: 640;
  line-height: 1.14;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fv-13__split {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: clamp(1rem, 3vw, 1.5rem);
  inline-size: min(100%, 56rem);
}

.fv-13__form {
  display: grid;
  gap: 1.375rem;
  align-content: start;
  min-inline-size: 0;
  padding: var(--pad);
  background: var(--surface-1);
  border-radius: 1rem;
}

.fv-13__alert {
  display: none;
  margin: 0;
  min-inline-size: 0;
  padding: 0.75rem 0.875rem;
  border-radius: 0.625rem;
  background: #fdeef3;
  color: var(--error-ink);
  font-size: 0.875rem;
  font-weight: 600;
  line-height: 1.45;
}

.fv-13__alert:not(:empty) {
  display: block;
}

.fv-13__field {
  display: grid;
  gap: 0.4375rem;
  min-inline-size: 0;
}

.fv-13__label {
  font-size: 0.8125rem;
  font-weight: 600;
}

.fv-13__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.875rem;
  padding: 0 0.875rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: var(--surface-2);
  border: 1px solid var(--rule);
  border-radius: 0.625rem;
}

.fv-13__input::placeholder {
  color: #9d97ba;
}

.fv-13__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-13__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
}

.fv-13__input:user-invalid {
  border-color: var(--error);
  background: #fdf1f5;
}

.fv-13__input[aria-invalid="true"] {
  border-color: var(--error);
  background: #fdf1f5;
}

.fv-13__input:user-valid {
  border-color: #2f8a63;
}

.fv-13__msg {
  display: flex;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--error-ink);
}

.fv-13__msg span {
  min-inline-size: 0;
}

.fv-13__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-13__polite {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fv-13__btn {
  justify-self: start;
  min-block-size: 2.875rem;
  min-inline-size: 44px;
  padding: 0.75rem 1.375rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 650;
  color: #ffffff;
  background: var(--accent);
  border: 0;
  border-radius: 0.625rem;
  cursor: pointer;
}

.fv-13__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.fv-13__transcript {
  min-inline-size: 0;
  align-self: start;
  padding: var(--pad);
  background: var(--surface-3);
  border-radius: 1rem;
}

.fv-13__thead {
  margin-block-end: 1rem;
  min-inline-size: 0;
}

.fv-13__ttitle {
  margin: 0 0 0.25rem;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 640;
}

.fv-13__tsub {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-13__log {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
}

.fv-13__log li {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: start;
  gap: 0.5rem;
  min-inline-size: 0;
  padding: 0.5625rem 0.6875rem;
  background: var(--surface-1);
  border-radius: 0.5rem;
  font-size: 0.8125rem;
  line-height: 1.45;
}

.fv-13__empty {
  display: block;
  color: var(--muted);
  font-style: italic;
}

.fv-13__level {
  flex: none;
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.fv-13__level[data-level="assertive"] {
  background: #fadfe8;
  color: var(--error-ink);
}

.fv-13__level[data-level="polite"] {
  background: #e3ddf9;
  color: var(--accent);
}

.fv-13__say {
  min-inline-size: 0;
}

@media (prefers-color-scheme: dark) {
  .fv-13:not(:has(#fv-13-theme-light:checked)) {
    --page: #100d1c;
    --surface-1: #181330;
    --surface-2: #140f28;
    --surface-3: #1d1738;
    --ink: #ece8fa;
    --muted: #a49bc9;
    --rule: #2c2450;
    --accent: #a48bff;
    --error: #ff6f9c;
    --error-ink: #ff93b4;
  }

  .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__alert {
    background: #2c1220;
  }

  .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__input::placeholder {
    color: #6b6390;
  }

  .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__input:user-invalid,
    .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__input[aria-invalid="true"] {
    background: #26101c;
  }

  .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__btn {
    color: #100d1c;
  }

  .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__level[data-level="assertive"] {
    background: #34131f;
    color: #ff93b4;
  }

  .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__level[data-level="polite"] {
    background: #241d44;
    color: #b7a4ff;
  }
}

[data-theme="dark"] .fv-13:not(:has(#fv-13-theme-light:checked)) {
  --page: #100d1c;
  --surface-1: #181330;
  --surface-2: #140f28;
  --surface-3: #1d1738;
  --ink: #ece8fa;
  --muted: #a49bc9;
  --rule: #2c2450;
  --accent: #a48bff;
  --error: #ff6f9c;
  --error-ink: #ff93b4;
}

[data-theme="dark"] .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__btn {
  color: #100d1c;
}

[data-theme="dark"] .fv-13:not(:has(#fv-13-theme-light:checked)) .fv-13__alert {
  background: #2c1220;
}

.fv-13 {
  position: relative;
}

.fv-13__stage {
  padding-block-start: 4.75rem;
}

.fv-13__theme {
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

.fv-13__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-13__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-13__themeopt {
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

.fv-13__themeopt:hover {
  opacity: 0.85;
}

.fv-13__themeinput:checked + .fv-13__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-13__themeinput:focus-visible + .fv-13__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-13__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-13__themeinput:checked + .fv-13__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-13:has(#fv-13-theme-dark:checked) {
  --page: #100d1c;
  --surface-1: #181330;
  --surface-2: #140f28;
  --surface-3: #1d1738;
  --ink: #ece8fa;
  --muted: #a49bc9;
  --rule: #2c2450;
  --accent: #a48bff;
  --error: #ff6f9c;
  --error-ink: #ff93b4;
}

.fv-13:has(#fv-13-theme-dark:checked) .fv-13__alert {
  background: #2c1220;
}

.fv-13:has(#fv-13-theme-dark:checked) .fv-13__input::placeholder {
  color: #6b6390;
}

.fv-13:has(#fv-13-theme-dark:checked) .fv-13__input:user-invalid,
.fv-13:has(#fv-13-theme-dark:checked) .fv-13__input[aria-invalid="true"] {
  background: #26101c;
}

.fv-13:has(#fv-13-theme-dark:checked) .fv-13__btn {
  color: #100d1c;
}

.fv-13:has(#fv-13-theme-dark:checked) .fv-13__level[data-level="assertive"] {
  background: #34131f;
  color: #ff93b4;
}

.fv-13:has(#fv-13-theme-dark:checked) .fv-13__level[data-level="polite"] {
  background: #241d44;
  color: #b7a4ff;
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-13__form');
  if (!form || form.dataset.fv13) return;
  form.dataset.fv13 = '1';
  const alertBox = form.querySelector('.fv-13__alert');
  const polite = form.querySelector('.fv-13__polite');
  const log = document.querySelector('.fv-13__log');
  const fields = [...form.querySelectorAll('.fv-13__input')];
  const label = (f) => form.querySelector('label[for="' + f.id + '"]').textContent;
  const write = (region, text, level) => {
    region.textContent = '';
    requestAnimationFrame(() => { region.textContent = text; });
    const li = document.createElement('li');
    const tag = document.createElement('span');
    tag.className = 'fv-13__level';
    tag.dataset.level = level;
    tag.textContent = level;
    const say = document.createElement('span');
    say.className = 'fv-13__say';
    say.textContent = text;
    li.append(tag, say);
    log.querySelector('.fv-13__empty')?.remove();
    log.prepend(li);
  };
  fields.forEach((f) => f.addEventListener('blur', () => {
    const bad = !f.checkValidity();
    f.toggleAttribute('aria-invalid', bad);
    if (bad) f.setAttribute('aria-invalid', 'true');
    document.getElementById(f.getAttribute('aria-describedby')).hidden = !bad;
    if (bad) write(polite, label(f) + ': ' + f.validationMessage, 'polite');
  }));
  form.querySelector('.fv-13__btn').addEventListener('click', () => {
    const bad = fields.filter((f) => !f.checkValidity());
    if (!bad.length) return write(alertBox, 'Thanks — your volunteer signup was received.', 'assertive');
    write(alertBox, bad.length + ' field(s) need attention before signing up. First: ' + label(bad[0]) + '.', 'assertive');
    bad[0].focus();
  });
})();
```
