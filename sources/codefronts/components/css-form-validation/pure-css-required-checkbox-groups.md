---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/pure-css-required-checkbox-groups/"
title: "Pure CSS Required Checkbox Groups"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "\"Select at least one\" is the one common requirement native HTML cannot express."
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Required Checkbox Groups
Source: https://codefronts.com/components/css-form-validation/pure-css-required-checkbox-groups/

"Select at least one" is the one common requirement native HTML cannot express. required on a radio applies to the whole group; on a checkbox it applies only to that single box, so ticking a different option leaves the form invalid. This demo puts both groups side by side and closes the checkbox gap with a nine-line setCustomValidity() shim, keeping the verdict inside the native constraint system.
## HTML
```html
<section class="fv-04" aria-labelledby="fv-04-h">
  <fieldset class="fv-04__theme">
    <legend class="fv-04__themelegend">Theme</legend>
    <input class="fv-04__themeinput" type="radio" name="fv-04-theme" id="fv-04-theme-auto" checked>
    <label class="fv-04__themeopt" for="fv-04-theme-auto">Auto</label>
    <input class="fv-04__themeinput" type="radio" name="fv-04-theme" id="fv-04-theme-light">
    <label class="fv-04__themeopt" for="fv-04-theme-light">Light</label>
    <input class="fv-04__themeinput" type="radio" name="fv-04-theme" id="fv-04-theme-dark">
    <label class="fv-04__themeopt" for="fv-04-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-04__stage">
    <header class="fv-04__head">
      <h2 class="fv-04__h" id="fv-04-h">Radios validate as a group. Checkboxes don't.</h2>
      <p class="fv-04__sub">Same attribute, two meanings. The left group needs nothing; the right needs nine lines.</p>
    </header>

    <form class="fv-04__form" aria-labelledby="fv-04-h">
      <div class="fv-04__cols">
        <fieldset class="fv-04__group fv-04__group--radio">
          <legend class="fv-04__legend">
            Delivery window
            <span class="fv-04__badge fv-04__badge--native">Native</span>
          </legend>
          <p class="fv-04__note">One <code>required</code> on any member covers the whole group, because the shared <code>name</code> defines it.</p>
          <label class="fv-04__opt"><input type="radio" name="fv-04-window" value="am" required><span>Weekday morning</span></label>
          <label class="fv-04__opt"><input type="radio" name="fv-04-window" value="pm"><span>Weekday afternoon</span></label>
          <label class="fv-04__opt"><input type="radio" name="fv-04-window" value="sat"><span>Saturday, 9am–1pm</span></label>
        </fieldset>

        <fieldset class="fv-04__group fv-04__group--check" aria-describedby="fv-04-check-msg">
          <legend class="fv-04__legend">
            Alert channels
            <span class="fv-04__badge fv-04__badge--shim">Needs a shim</span>
          </legend>
          <p class="fv-04__note">Here <code>required</code> would only ever mean "tick <em>this</em> box", so one anchor carries a custom validity instead.</p>
          <label class="fv-04__opt"><input type="checkbox" name="fv-04-alerts" value="email"><span>Email digest</span></label>
          <label class="fv-04__opt"><input type="checkbox" name="fv-04-alerts" value="sms"><span>SMS for outages</span></label>
          <label class="fv-04__opt"><input type="checkbox" name="fv-04-alerts" value="slack"><span>Slack channel post</span></label>
          <p class="fv-04__msg" id="fv-04-check-msg">
            <svg class="fv-04__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5.1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.3" r="1.05" fill="currentColor"></circle></svg>
            <span>Choose at least one alert channel so Fern can reach you during an incident</span>
          </p>
        </fieldset>
      </div>

      <div class="fv-04__foot">
        <button class="fv-04__btn" type="button">Save notification settings</button>
        <p class="fv-04__status" role="status"></p>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-04 {
  --page: #f2f5ee;
  --surface: #ffffff;
  --ink: #1b2620;
  --muted: #5d6b62;
  --rule: #d5e0d4;
  --accent: #2f6b4f;
  --error: #7d2230;
  --error-ink: #6b1c28;
  --error-bg: #fdf0f0;
  --card-radius: 0.875rem;
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
  .fv-04 {
    --accent: oklch(0.48 0.1 156);
    --error: oklch(0.39 0.15 18);
    --error-ink: oklch(0.35 0.15 18);
    --error-bg: oklch(0.96 0.02 18);
  }
}

.fv-04 *,
.fv-04 *::before,
.fv-04 *::after {
  box-sizing: border-box;
}

.fv-04__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.5rem, 5vw, 3.75rem) clamp(1rem, 4vw, 3rem);
}

.fv-04__head {
  inline-size: min(100%, 48rem);
  min-inline-size: 0;
  margin-block-end: clamp(1.25rem, 4vw, 2rem);
}

.fv-04__h {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 3.8vw, 2.05rem);
  font-weight: 650;
  line-height: 1.15;
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fv-04__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.55;
  color: var(--muted);
}

.fv-04__form {
  inline-size: min(100%, 48rem);
  min-inline-size: 0;
  display: grid;
  gap: 1.25rem;
}

.fv-04__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: clamp(0.875rem, 2.5vw, 1.25rem);
}

.fv-04__group {
  display: grid;
  gap: 0.6875rem;
  align-content: start;
  min-inline-size: 0;
  margin: 0;
  padding: 1.25rem;
  border: 1px solid var(--rule);
  border-radius: var(--card-radius);
  background: var(--surface);
  box-shadow: 0 14px 30px -26px rgba(27, 38, 32, 0.55);
  transition: border-color 0.18s ease, box-shadow 0.18s ease;
}

.fv-04__legend {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  padding: 0;
  min-inline-size: 0;
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 650;
}

.fv-04__badge {
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  font-family: system-ui, sans-serif;
  font-size: 0.625rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.fv-04__badge--native {
  background: #dff0e4;
  color: #1f5c3d;
}

.fv-04__badge--shim {
  background: #fbe9dd;
  color: #8a4415;
}

.fv-04__note {
  margin: 0 0 0.25rem;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-04__note code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.82em;
  padding: 0.1em 0.32em;
  border-radius: 0.25rem;
  background: #eef2ec;
}

.fv-04__opt {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  min-block-size: 2.75rem;
  min-inline-size: 0;
  padding: 0.4375rem 0.6875rem;
  border: 1px solid transparent;
  border-radius: 0.625rem;
  font-size: 0.9375rem;
  cursor: pointer;
  transition: background-color 0.14s ease;
}

.fv-04__opt:hover {
  background: #f4f7f2;
}

.fv-04__opt span {
  min-inline-size: 0;
}

.fv-04__opt input {
  flex: none;
  inline-size: 1.125rem;
  block-size: 1.125rem;
  margin: 0;
  accent-color: var(--accent);
}

.fv-04__opt input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fv-04__msg {
  display: none;
  gap: 0.4375rem;
  align-items: flex-start;
  margin: 0.125rem 0 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  font-weight: 500;
  color: var(--error-ink);
}

.fv-04__msg span {
  min-inline-size: 0;
}

.fv-04__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-04__group:has(input:user-invalid) {
  border-color: var(--error);
  background: var(--error-bg);
  box-shadow: 0 0 0 3px rgba(125, 34, 48, 0.12);
}

.fv-04__group:has(input:user-invalid) .fv-04__msg {
  display: flex;
}

.fv-04__group--radio:has(input:user-valid) {
  border-color: var(--accent);
}

.fv-04__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1rem;
  min-inline-size: 0;
}

.fv-04__btn {
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  padding: 0.6875rem 1.25rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #ffffff;
  background: var(--accent);
  border: 0;
  border-radius: 0.625rem;
  cursor: pointer;
}

.fv-04__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.fv-04__status {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.4;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fv-04__group,
    .fv-04__opt {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-04:not(:has(#fv-04-theme-light:checked)) {
    --page: #0f150f;
    --surface: #161d17;
    --ink: #e6efe6;
    --muted: #97a89b;
    --rule: #263025;
    --accent: #6bcf9a;
    --error: #ff8090;
    --error-ink: #ff9fab;
    --error-bg: #241318;
  }

  .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__badge--native {
    background: #16321f;
    color: #92e3b2;
  }

  .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__badge--shim {
    background: #33230f;
    color: #f0bd7e;
  }

  .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__note code {
    background: #1e251e;
  }

  .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__opt:hover {
    background: #1c241c;
  }

  .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__btn {
    color: #0c1410;
  }

  .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__group:has(input:user-invalid) {
    box-shadow: 0 0 0 3px rgba(255, 128, 144, 0.14);
  }
}

[data-theme="dark"] .fv-04:not(:has(#fv-04-theme-light:checked)) {
  --page: #0f150f;
  --surface: #161d17;
  --ink: #e6efe6;
  --muted: #97a89b;
  --rule: #263025;
  --accent: #6bcf9a;
  --error: #ff8090;
  --error-ink: #ff9fab;
  --error-bg: #241318;
}

[data-theme="dark"] .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__btn {
  color: #0c1410;
}

[data-theme="dark"] .fv-04:not(:has(#fv-04-theme-light:checked)) .fv-04__note code {
  background: #1e251e;
}

.fv-04 {
  position: relative;
}

.fv-04__stage {
  padding-block-start: 4.75rem;
}

.fv-04__theme {
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

.fv-04__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-04__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-04__themeopt {
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

.fv-04__themeopt:hover {
  opacity: 0.85;
}

.fv-04__themeinput:checked + .fv-04__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-04__themeinput:focus-visible + .fv-04__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-04__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-04__themeinput:checked + .fv-04__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-04:has(#fv-04-theme-dark:checked) {
  --page: #0f150f;
  --surface: #161d17;
  --ink: #e6efe6;
  --muted: #97a89b;
  --rule: #263025;
  --accent: #6bcf9a;
  --error: #ff8090;
  --error-ink: #ff9fab;
  --error-bg: #241318;
}

.fv-04:has(#fv-04-theme-dark:checked) .fv-04__badge--native {
  background: #16321f;
  color: #92e3b2;
}

.fv-04:has(#fv-04-theme-dark:checked) .fv-04__badge--shim {
  background: #33230f;
  color: #f0bd7e;
}

.fv-04:has(#fv-04-theme-dark:checked) .fv-04__note code {
  background: #1e251e;
}

.fv-04:has(#fv-04-theme-dark:checked) .fv-04__opt:hover {
  background: #1c241c;
}

.fv-04:has(#fv-04-theme-dark:checked) .fv-04__btn {
  color: #0c1410;
}

.fv-04:has(#fv-04-theme-dark:checked) .fv-04__group:has(input:user-invalid) {
  box-shadow: 0 0 0 3px rgba(255, 128, 144, 0.14);
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-04__form');
  if (!form || form.dataset.fv04) return;
  form.dataset.fv04 = '1';
  const boxes = [...form.querySelectorAll('.fv-04__group--check input[type="checkbox"]')];
  const anchor = boxes[0];
  const status = form.querySelector('.fv-04__status');
  const sync = () => {
    const chosen = boxes.filter((b) => b.checked).length;
    anchor.setCustomValidity(chosen ? '' : 'Choose at least one alert channel.');
    return chosen;
  };
  const submit = () => {
    const chosen = sync();
    const ok = form.checkValidity();
    status.textContent = ok ? 'Saved — ' + chosen + ' channel(s) active.' : '';
    if (!ok) form.reportValidity();
  };
  boxes.forEach((b) => b.addEventListener('change', () => { sync(); status.textContent = ''; }));
  form.querySelector('.fv-04__btn').addEventListener('click', submit);
  form.addEventListener('keydown', (e) => { if (e.key === 'Enter' && e.target.tagName !== 'BUTTON') { e.preventDefault(); submit(); } });
  sync();
})();
```
