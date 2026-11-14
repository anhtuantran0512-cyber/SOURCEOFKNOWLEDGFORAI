---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/validation-summary-box-with-has-selector/"
title: "Validation Summary Box with Has Selector"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "A summary panel above the form that appears only while the form contains a field the user has left invalid — .fv-12__form:has(:user-invalid) .fv-12__summary,…"
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Validation Summary Box with Has Selector
Source: https://codefronts.com/components/css-form-validation/validation-summary-box-with-has-selector/

A summary panel above the form that appears only while the form contains a field the user has left invalid — .fv-12__form:has(:user-invalid) .fv-12__summary, and nothing else. Each line links to its field by id so clicking moves focus straight there. The script only keeps the list text current; whether the panel is on screen is decided entirely in CSS, and that split is the point.
## HTML
```html
<section class="fv-12" aria-labelledby="fv-12-h">
  <fieldset class="fv-12__theme">
    <legend class="fv-12__themelegend">Theme</legend>
    <input class="fv-12__themeinput" type="radio" name="fv-12-theme" id="fv-12-theme-auto" checked>
    <label class="fv-12__themeopt" for="fv-12-theme-auto">Auto</label>
    <input class="fv-12__themeinput" type="radio" name="fv-12-theme" id="fv-12-theme-light">
    <label class="fv-12__themeopt" for="fv-12-theme-light">Light</label>
    <input class="fv-12__themeinput" type="radio" name="fv-12-theme" id="fv-12-theme-dark">
    <label class="fv-12__themeopt" for="fv-12-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-12__stage">
    <form class="fv-12__form" aria-labelledby="fv-12-h">
      <header class="fv-12__head">
        <p class="fv-12__eyebrow">Sable · access request</p>
        <h2 class="fv-12__h" id="fv-12-h">The panel is a selector, not a state flag</h2>
      </header>

      <div class="fv-12__summary" role="group" aria-labelledby="fv-12-sum-h">
        <div class="fv-12__sumhead">
          <svg class="fv-12__sumicon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8.2" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.6v5.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path><circle cx="10" cy="14.3" r="1.1" fill="currentColor"></circle></svg>
          <h3 class="fv-12__sumtitle" id="fv-12-sum-h">Before this can be sent</h3>
          <p class="fv-12__count">2 fields need attention</p>
        </div>
        <ul class="fv-12__list">
          <li><a href="#fv-12-email">Work email — Enter a valid email address</a></li>
          <li><a href="#fv-12-seats">Seats — Enter a number from 1 to 500</a></li>
        </ul>
      </div>

      <div class="fv-12__fields">
        <div class="fv-12__field">
          <label class="fv-12__label" for="fv-12-name">Requester</label>
          <input class="fv-12__input" id="fv-12-name" name="fv-12-name" type="text" required autocomplete="name" placeholder="Jordan Lee" value="Jordan Lee">
        </div>
        <div class="fv-12__field">
          <label class="fv-12__label" for="fv-12-email">Work email</label>
          <input class="fv-12__input" id="fv-12-email" name="fv-12-email" type="email" required autocomplete="email" placeholder="[email protected]" value="jordan.sable.io">
        </div>
        <div class="fv-12__field">
          <label class="fv-12__label" for="fv-12-seats">Seats</label>
          <input class="fv-12__input" id="fv-12-seats" name="fv-12-seats" type="number" required min="1" max="500" placeholder="24" value="0">
        </div>
        <div class="fv-12__field">
          <label class="fv-12__label" for="fv-12-team">Team</label>
          <input class="fv-12__input" id="fv-12-team" name="fv-12-team" type="text" required placeholder="Platform" value="Platform">
        </div>
      </div>

      <div class="fv-12__foot">
        <button class="fv-12__btn" type="button">Send request</button>
        <p class="fv-12__hint">Visibility is pure <code>:has()</code>. The list text is the only thing script touches.</p>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-12 {
  --page: #000000;
  --surface: rgba(20, 22, 26, 0.72);
  --field: #0c0d10;
  --ink: #f4f6fa;
  --muted: #9096a4;
  --rule: #23262e;
  --accent: #22e0d0;
  --error: #ff4b5c;
  --error-ink: #ff8f9a;
  --glass-blur: 14px;
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
  .fv-12 {
    --accent: oklch(0.83 0.16 182);
    --error: oklch(0.65 0.22 18);
    --error-ink: oklch(0.76 0.16 18);
  }
}

.fv-12 *,
.fv-12 *::before,
.fv-12 *::after {
  box-sizing: border-box;
}

.fv-12 [hidden] {
  display: none;
}

.fv-12__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3.5rem) clamp(1rem, 4vw, 2.5rem);
  background-image: radial-gradient(90% 60% at 20% 0%, rgba(34, 224, 208, 0.12) 0%, transparent 60%), radial-gradient(70% 50% at 100% 100%, rgba(255, 75, 92, 0.1) 0%, transparent 60%);
}

.fv-12__form {
  inline-size: min(100%, 34rem);
  min-inline-size: 0;
  display: grid;
  gap: 1.125rem;
  padding: clamp(1.125rem, 3.5vw, 1.75rem);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 1rem;
  -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(140%);
  backdrop-filter: blur(var(--glass-blur)) saturate(140%);
}

.fv-12__head {
  min-inline-size: 0;
}

.fv-12__eyebrow {
  margin: 0 0 0.375rem;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-12__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.2rem, 3.4vw, 1.5rem);
  font-weight: 620;
  line-height: 1.2;
  letter-spacing: -0.025em;
}

.fv-12__summary {
  display: none;
  gap: 0.6875rem;
  min-inline-size: 0;
  padding: 0.9375rem 1rem;
  border: 1px solid var(--error);
  border-radius: 0.75rem;
  background: rgba(255, 75, 92, 0.1);
}

.fv-12__form:has(.fv-12__input:invalid:not(:placeholder-shown)) .fv-12__summary {
  display: grid;
}

.fv-12__form:has(.fv-12__input:user-invalid) .fv-12__summary {
  display: grid;
}

.fv-12__sumhead {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: 0.5rem 0.625rem;
  min-inline-size: 0;
}

.fv-12__sumicon {
  grid-row: span 2;
  inline-size: 1.375rem;
  block-size: 1.375rem;
  color: var(--error);
}

.fv-12__sumtitle {
  margin: 0;
  min-inline-size: 0;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 620;
  color: var(--error-ink);
}

.fv-12__count {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fv-12__list {
  margin: 0;
  padding-inline-start: 1.75rem;
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
}

.fv-12__list li {
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
}

.fv-12__list a {
  color: var(--error-ink);
  text-decoration: underline;
  text-underline-offset: 0.18em;
  text-decoration-thickness: 1px;
}

.fv-12__list a:hover {
  color: #ffffff;
}

.fv-12__list a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 0.125rem;
}

.fv-12__fields {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  gap: 0.875rem;
  min-inline-size: 0;
}

.fv-12__field {
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
}

.fv-12__label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-12__input {
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

.fv-12__input::placeholder {
  color: #5f6674;
}

.fv-12__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-12__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
}

.fv-12__input:user-invalid {
  border-color: var(--error);
  background: #170a0d;
}

.fv-12__input:user-valid {
  border-color: #2f6b62;
}

.fv-12__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1rem;
  min-inline-size: 0;
}

.fv-12__btn {
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  padding: 0.6875rem 1.375rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 650;
  color: #04100f;
  background: var(--accent);
  border: 0;
  border-radius: 0.5rem;
  cursor: pointer;
}

.fv-12__btn:focus-visible {
  outline: 2px solid #ffffff;
  outline-offset: 3px;
}

.fv-12__hint {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-12__hint code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.9em;
  color: var(--accent);
}

@media (prefers-color-scheme: light) {
  .fv-12:not(:has(#fv-12-theme-dark:checked)) {
    --page: #eef0f4;
    --surface: rgba(255, 255, 255, 0.78);
    --field: #ffffff;
    --ink: #14161c;
    --muted: #5c6472;
    --rule: #d6dae2;
    --accent: #0b8f84;
    --error: #cf2137;
    --error-ink: #a5162a;
  }

  .fv-12:not(:has(#fv-12-theme-dark:checked)) .fv-12__stage {
    background-image: radial-gradient(90% 60% at 20% 0%, rgba(11, 143, 132, 0.1) 0%, transparent 60%), radial-gradient(70% 50% at 100% 100%, rgba(207, 33, 55, 0.08) 0%, transparent 60%);
  }

  .fv-12:not(:has(#fv-12-theme-dark:checked)) .fv-12__summary {
    background: rgba(207, 33, 55, 0.07);
  }

  .fv-12:not(:has(#fv-12-theme-dark:checked)) .fv-12__input:user-invalid {
    background: #fdf2f3;
  }

  .fv-12:not(:has(#fv-12-theme-dark:checked)) .fv-12__input::placeholder {
    color: #9aa2b0;
  }

  .fv-12:not(:has(#fv-12-theme-dark:checked)) .fv-12__list a:hover {
    color: #14161c;
  }

  .fv-12:not(:has(#fv-12-theme-dark:checked)) .fv-12__btn {
    color: #ffffff;
  }
}

[data-theme="dark"] .fv-12:not(:has(#fv-12-theme-light:checked)) {
  --page: #000000;
  --surface: rgba(20, 22, 26, 0.72);
  --field: #0c0d10;
  --ink: #f4f6fa;
  --muted: #9096a4;
  --rule: #23262e;
  --accent: #22e0d0;
  --error: #ff4b5c;
  --error-ink: #ff8f9a;
}

[data-theme="dark"] .fv-12:not(:has(#fv-12-theme-light:checked)) .fv-12__btn {
  color: #04100f;
}

[data-theme="dark"] .fv-12:not(:has(#fv-12-theme-light:checked)) .fv-12__input:user-invalid {
  background: #170a0d;
}

.fv-12 {
  position: relative;
}

.fv-12__stage {
  padding-block-start: 4.75rem;
}

.fv-12__theme {
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

.fv-12__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-12__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-12__themeopt {
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

.fv-12__themeopt:hover {
  opacity: 0.85;
}

.fv-12__themeinput:checked + .fv-12__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-12__themeinput:focus-visible + .fv-12__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-12__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-12__themeinput:checked + .fv-12__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-12:has(#fv-12-theme-light:checked) {
  --page: #eef0f4;
  --surface: rgba(255, 255, 255, 0.78);
  --field: #ffffff;
  --ink: #14161c;
  --muted: #5c6472;
  --rule: #d6dae2;
  --accent: #0b8f84;
  --error: #cf2137;
  --error-ink: #a5162a;
}

.fv-12:has(#fv-12-theme-light:checked) .fv-12__stage {
  background-image: radial-gradient(90% 60% at 20% 0%, rgba(11, 143, 132, 0.1) 0%, transparent 60%), radial-gradient(70% 50% at 100% 100%, rgba(207, 33, 55, 0.08) 0%, transparent 60%);
}

.fv-12:has(#fv-12-theme-light:checked) .fv-12__summary {
  background: rgba(207, 33, 55, 0.07);
}

.fv-12:has(#fv-12-theme-light:checked) .fv-12__input:user-invalid {
  background: #fdf2f3;
}

.fv-12:has(#fv-12-theme-light:checked) .fv-12__input::placeholder {
  color: #9aa2b0;
}

.fv-12:has(#fv-12-theme-light:checked) .fv-12__list a:hover {
  color: #14161c;
}

.fv-12:has(#fv-12-theme-light:checked) .fv-12__btn {
  color: #ffffff;
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-12__form');
  if (!form || form.dataset.fv12) return;
  form.dataset.fv12 = '1';
  const list = form.querySelector('.fv-12__list');
  const count = form.querySelector('.fv-12__count');
  const fields = [...form.querySelectorAll('.fv-12__input')];
  const label = (f) => form.querySelector('label[for="' + f.id + '"]').textContent;
  const sync = () => {
    const bad = fields.filter((f) => !f.checkValidity());
    count.textContent = bad.length === 1 ? '1 field needs attention' : bad.length + ' fields need attention';
    list.replaceChildren(...bad.map((f) => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = '#' + f.id;
      a.textContent = label(f) + ' — ' + (f.validationMessage || 'Check this field');
      a.addEventListener('click', (e) => { e.preventDefault(); f.focus(); });
      li.append(a);
      return li;
    }));
  };
  fields.forEach((f) => { f.addEventListener('blur', sync); f.addEventListener('input', sync); });
  form.querySelector('.fv-12__btn').addEventListener('click', () => { sync(); if (!form.checkValidity()) form.reportValidity(); });
  fields.forEach((f) => f.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); sync(); form.reportValidity(); } }));
  sync();
})();
```
