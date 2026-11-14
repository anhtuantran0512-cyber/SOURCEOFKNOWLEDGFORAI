---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/accessible-error-with-aria-describedby/"
title: "Accessible Error with ARIA Describedby"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "The full accessible-error contract in one field group: aria-invalid=\"true\" on the control, aria-describedby pointing at the message's id, and the message…"
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Error with ARIA Describedby
Source: https://codefronts.com/components/css-form-validation/accessible-error-with-aria-describedby/

The full accessible-error contract in one field group: aria-invalid="true" on the control, aria-describedby pointing at the message's id, and the message removed from the accessibility tree the moment the field becomes valid. An inspector panel beside the form shows the computed name, role, state and description for the focused field, so you can see what a screen reader would actually receive.
## HTML
```html
<section class="fv-11" aria-labelledby="fv-11-h">
  <fieldset class="fv-11__theme">
    <legend class="fv-11__themelegend">Theme</legend>
    <input class="fv-11__themeinput" type="radio" name="fv-11-theme" id="fv-11-theme-auto" checked>
    <label class="fv-11__themeopt" for="fv-11-theme-auto">Auto</label>
    <input class="fv-11__themeinput" type="radio" name="fv-11-theme" id="fv-11-theme-light">
    <label class="fv-11__themeopt" for="fv-11-theme-light">Light</label>
    <input class="fv-11__themeinput" type="radio" name="fv-11-theme" id="fv-11-theme-dark">
    <label class="fv-11__themeopt" for="fv-11-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-11__stage">
    <header class="fv-11__head">
      <p class="fv-11__eyebrow">Basalt Health · patient portal</p>
      <h2 class="fv-11__h" id="fv-11-h">What the screen reader is handed</h2>
      <p class="fv-11__sub">Name, role, state, description. Four things, and only one of them is the colour of the border.</p>
    </header>

    <div class="fv-11__split">
      <form class="fv-11__form" aria-labelledby="fv-11-h">
        <div class="fv-11__field">
          <label class="fv-11__label" for="fv-11-nhs">NHS number</label>
          <input class="fv-11__input" id="fv-11-nhs" name="fv-11-nhs" type="text" required pattern="[0-9 ]{10,12}" inputmode="numeric" placeholder="943 476 5919" value="943 476" aria-describedby="fv-11-nhs-msg">
          <p class="fv-11__msg" id="fv-11-nhs-msg" hidden>
            <svg class="fv-11__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Enter all 10 digits of your NHS number, spaces are fine</span>
          </p>
        </div>

        <div class="fv-11__field">
          <label class="fv-11__label" for="fv-11-dob">Date of birth</label>
          <input class="fv-11__input" id="fv-11-dob" name="fv-11-dob" type="date" required max="2026-08-21" value="2031-04-02" aria-describedby="fv-11-dob-msg">
          <p class="fv-11__msg" id="fv-11-dob-msg" hidden>
            <svg class="fv-11__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Date of birth cannot be in the future — check the year</span>
          </p>
        </div>

        <div class="fv-11__field">
          <label class="fv-11__label" for="fv-11-contact">Contact email</label>
          <input class="fv-11__input" id="fv-11-contact" name="fv-11-contact" type="email" required autocomplete="email" placeholder="[email protected]" value="[email protected]" aria-describedby="fv-11-contact-msg">
          <p class="fv-11__msg" id="fv-11-contact-msg" hidden>
            <svg class="fv-11__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Enter a valid email address so we can send your appointment letter</span>
          </p>
        </div>

        <button class="fv-11__btn" type="button">Check my details</button>
      </form>

      <aside class="fv-11__inspect" aria-label="Accessibility tree preview">
        <h3 class="fv-11__insphead">Accessibility tree</h3>
        <dl class="fv-11__rows">
          <div class="fv-11__row"><dt>Name</dt><dd data-slot="name">—</dd></div>
          <div class="fv-11__row"><dt>Role</dt><dd data-slot="role">—</dd></div>
          <div class="fv-11__row"><dt>State</dt><dd data-slot="state">—</dd></div>
          <div class="fv-11__row"><dt>Description</dt><dd data-slot="desc">—</dd></div>
          <div class="fv-11__row"><dt>describedby</dt><dd data-slot="db">—</dd></div>
        </dl>
        <p class="fv-11__inspnote">Focus or blur a field. The description only exists while the error does.</p>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-11 {
  --page: #ffffff;
  --surface: #ffffff;
  --panel: #f4f7fa;
  --ink: #0f1a24;
  --muted: #4e6070;
  --rule: #dfe6ec;
  --accent: #0b6ea8;
  --error: #b8264f;
  --error-ink: #971d40;
  --gap: 2rem;
  --font-display: "Seravek", "Gill Sans Nova", Optima, "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-11 {
    --accent: oklch(0.5 0.13 240);
    --error: oklch(0.47 0.17 5);
    --error-ink: oklch(0.4 0.17 5);
  }
}

.fv-11 *,
.fv-11 *::before,
.fv-11 *::after {
  box-sizing: border-box;
}

.fv-11 [hidden] {
  display: none;
}

.fv-11__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 4rem) clamp(1rem, 4vw, 3rem);
}

.fv-11__head {
  inline-size: min(100%, 58rem);
  min-inline-size: 0;
  padding-block-end: 1.5rem;
  border-block-end: 1px solid var(--rule);
  margin-block-end: var(--gap);
}

.fv-11__eyebrow {
  margin: 0 0 0.625rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-11__h {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: clamp(1.4rem, 4vw, 2.2rem);
  font-weight: 600;
  line-height: 1.12;
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fv-11__sub {
  margin: 0;
  max-inline-size: 38rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
}

.fv-11__split {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 19rem), 1fr));
  gap: var(--gap);
  inline-size: min(100%, 58rem);
}

.fv-11__form {
  display: grid;
  gap: var(--gap);
  align-content: start;
  min-inline-size: 0;
}

.fv-11__field {
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
  padding-block-end: var(--gap);
  border-block-end: 1px solid var(--rule);
}

.fv-11__field:last-of-type {
  border-block-end: 0;
  padding-block-end: 0;
}

.fv-11__label {
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 0.005em;
}

.fv-11__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 3rem;
  padding: 0 0.875rem;
  font: inherit;
  font-size: 1rem;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.25rem;
}

.fv-11__input::placeholder {
  color: #93a3b0;
}

.fv-11__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-11__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  border-inline-start-width: 4px;
}

.fv-11__input:user-invalid {
  border-color: var(--error);
  border-inline-start-width: 4px;
}

.fv-11__input[aria-invalid="true"] {
  border-color: var(--error);
  border-inline-start-width: 4px;
}

.fv-11__msg {
  display: flex;
  gap: 0.4375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.875rem;
  line-height: 1.45;
  color: var(--error-ink);
}

.fv-11__msg span {
  min-inline-size: 0;
}

.fv-11__icon {
  flex: none;
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
  margin-block-start: 0.1rem;
}

.fv-11__btn {
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
  border-radius: 0.25rem;
  cursor: pointer;
}

.fv-11__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.fv-11__inspect {
  min-inline-size: 0;
  align-self: start;
  padding: 1.25rem;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 0.25rem;
}

.fv-11__insphead {
  margin: 0 0 0.875rem;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
}

.fv-11__rows {
  margin: 0;
  display: grid;
  gap: 0;
}

.fv-11__row {
  display: grid;
  grid-template-columns: minmax(0, 8rem) minmax(0, 1fr);
  gap: 0.5rem;
  padding-block: 0.5rem;
  border-block-end: 1px solid var(--rule);
}

.fv-11__row:last-child {
  border-block-end: 0;
}

.fv-11__row dt {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  min-inline-size: 0;
}

.fv-11__row dd {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  overflow-wrap: anywhere;
}

.fv-11__row dd[data-slot="state"] {
  font-weight: 600;
}

.fv-11__inspnote {
  margin: 0.875rem 0 0;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
}

@media (prefers-color-scheme: dark) {
  .fv-11:not(:has(#fv-11-theme-light:checked)) {
    --page: #070e14;
    --surface: #0d161e;
    --panel: #101b25;
    --ink: #e7eff5;
    --muted: #93a6b6;
    --rule: #1d2b37;
    --accent: #4aa8e0;
    --error: #ff6f92;
    --error-ink: #ff92ab;
  }

  .fv-11:not(:has(#fv-11-theme-light:checked)) .fv-11__input::placeholder {
    color: #64798a;
  }

  .fv-11:not(:has(#fv-11-theme-light:checked)) .fv-11__btn {
    color: #04121c;
  }
}

[data-theme="dark"] .fv-11:not(:has(#fv-11-theme-light:checked)) {
  --page: #070e14;
  --surface: #0d161e;
  --panel: #101b25;
  --ink: #e7eff5;
  --muted: #93a6b6;
  --rule: #1d2b37;
  --accent: #4aa8e0;
  --error: #ff6f92;
  --error-ink: #ff92ab;
}

[data-theme="dark"] .fv-11:not(:has(#fv-11-theme-light:checked)) .fv-11__btn {
  color: #04121c;
}

.fv-11 {
  position: relative;
}

.fv-11__stage {
  padding-block-start: 4.75rem;
}

.fv-11__theme {
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

.fv-11__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-11__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-11__themeopt {
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

.fv-11__themeopt:hover {
  opacity: 0.85;
}

.fv-11__themeinput:checked + .fv-11__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-11__themeinput:focus-visible + .fv-11__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-11__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-11__themeinput:checked + .fv-11__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-11:has(#fv-11-theme-dark:checked) {
  --page: #070e14;
  --surface: #0d161e;
  --panel: #101b25;
  --ink: #e7eff5;
  --muted: #93a6b6;
  --rule: #1d2b37;
  --accent: #4aa8e0;
  --error: #ff6f92;
  --error-ink: #ff92ab;
}

.fv-11:has(#fv-11-theme-dark:checked) .fv-11__input::placeholder {
  color: #64798a;
}

.fv-11:has(#fv-11-theme-dark:checked) .fv-11__btn {
  color: #04121c;
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-11__form');
  if (!form || form.dataset.fv11) return;
  form.dataset.fv11 = '1';
  const slots = {};
  document.querySelectorAll('.fv-11__inspect [data-slot]').forEach((el) => { slots[el.dataset.slot] = el; });
  const fields = [...form.querySelectorAll('.fv-11__input')];
  const mark = (el) => {
    const bad = !el.checkValidity();
    const msg = document.getElementById(el.getAttribute('aria-describedby'));
    if (bad) el.setAttribute('aria-invalid', 'true');
    else el.removeAttribute('aria-invalid');
    msg.hidden = !bad;
    return bad;
  };
  const report = (el) => {
    const msg = document.getElementById(el.getAttribute('aria-describedby'));
    slots.name.textContent = form.querySelector('label[for="' + el.id + '"]').textContent;
    slots.role.textContent = el.type === 'date' ? 'date' : el.type === 'email' ? 'textbox (email)' : 'textbox';
    slots.state.textContent = el.getAttribute('aria-invalid') === 'true' ? 'invalid entry, required' : 'required';
    slots.desc.textContent = msg.hidden ? 'none' : msg.textContent.trim();
    slots.db.textContent = el.getAttribute('aria-describedby');
  };
  fields.forEach((el) => {
    el.addEventListener('blur', () => { mark(el); report(el); });
    el.addEventListener('focus', () => report(el));
    el.addEventListener('input', () => { if (el.getAttribute('aria-invalid') === 'true') { mark(el); report(el); } });
  });
  form.querySelector('.fv-11__btn').addEventListener('click', () => { fields.forEach(mark); report(fields.find((f) => !f.checkValidity()) || fields[0]); });
  fields.forEach(mark);
})();
```
