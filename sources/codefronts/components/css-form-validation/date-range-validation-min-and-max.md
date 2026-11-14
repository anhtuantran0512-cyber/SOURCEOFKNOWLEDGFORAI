---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/date-range-validation-min-and-max/"
title: "Date Range Validation Min and Max"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "Start and end dates where the end must fall after the start."
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Date Range Validation Min and Max
Source: https://codefronts.com/components/css-form-validation/date-range-validation-min-and-max/

Start and end dates where the end must fall after the start. Absolute bounds come free from min and max, and :out-of-range styles a value outside them — a pseudo-class most developers never meet. The relative constraint needs about twenty lines that move the end field's min whenever the start changes, with the verdict routed through setCustomValidity().
## HTML
```html
<section class="fv-18" aria-labelledby="fv-18-h">
  <fieldset class="fv-18__theme">
    <legend class="fv-18__themelegend">Theme</legend>
    <input class="fv-18__themeinput" type="radio" name="fv-18-theme" id="fv-18-theme-auto" checked>
    <label class="fv-18__themeopt" for="fv-18-theme-auto">Auto</label>
    <input class="fv-18__themeinput" type="radio" name="fv-18-theme" id="fv-18-theme-light">
    <label class="fv-18__themeopt" for="fv-18-theme-light">Light</label>
    <input class="fv-18__themeinput" type="radio" name="fv-18-theme" id="fv-18-theme-dark">
    <label class="fv-18__themeopt" for="fv-18-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-18__stage">
    <form class="fv-18__card" data-range="bad" aria-labelledby="fv-18-h">
      <header class="fv-18__head">
        <p class="fv-18__eyebrow">Ranger Cabins · Cairngorms</p>
        <h2 class="fv-18__h" id="fv-18-h">Stay dates</h2>
        <p class="fv-18__sub">Bookable 21 Aug 2026 to 31 Mar 2027. The end date has to come after the start.</p>
      </header>

      <div class="fv-18__pair">
        <div class="fv-18__field">
          <label class="fv-18__label" for="fv-18-start">Arrive</label>
          <input class="fv-18__input" id="fv-18-start" name="fv-18-start" type="date" required min="2026-08-21" max="2027-03-31" value="2026-09-18" aria-describedby="fv-18-start-msg">
          <p class="fv-18__msg" id="fv-18-start-msg">
            <svg class="fv-18__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><rect x="2.6" y="4.2" width="14.8" height="13.2" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.6"></rect><path d="M2.6 8.4h14.8M6.6 2.6v3M13.4 2.6v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path></svg>
            <span>Arrival must fall inside the 21 Aug 2026 – 31 Mar 2027 season</span>
          </p>
        </div>

        <div class="fv-18__link" aria-hidden="true"></div>

        <div class="fv-18__field">
          <label class="fv-18__label" for="fv-18-end">Depart</label>
          <input class="fv-18__input" id="fv-18-end" name="fv-18-end" type="date" required min="2026-08-21" max="2027-03-31" value="2026-09-14" aria-describedby="fv-18-end-msg">
          <p class="fv-18__msg" id="fv-18-end-msg">
            <svg class="fv-18__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><rect x="2.6" y="4.2" width="14.8" height="13.2" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.6"></rect><path d="M2.6 8.4h14.8M6.6 2.6v3M13.4 2.6v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path></svg>
            <span>Departure must be after the arrival date — pick a later day</span>
          </p>
        </div>
      </div>

      <div class="fv-18__summary">
        <p class="fv-18__nightsrow">
          <span class="fv-18__nightslabel">Nights</span>
          <output class="fv-18__nights" for="fv-18-start fv-18-end">—</output>
        </p>
        <p class="fv-18__band">
          <span class="fv-18__bandtext" data-idle>Both dates sit inside the season window.</span>
          <span class="fv-18__bandtext" data-bad>Out of range — the departure is earlier than the arrival.</span>
          <span class="fv-18__bandtext" data-ok>Range accepted.</span>
        </p>
      </div>

      <button class="fv-18__btn" type="button">Check availability</button>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-18 {
  --page: #f2ece0;
  --surface: #fdfaf4;
  --ink: #10302e;
  --muted: #4f6b68;
  --rule: #cfc6b4;
  --accent: #0d5c56;
  --warn: #b4711a;
  --error: #b8341c;
  --error-ink: #96280f;
  --shadow-x: 6px;
  --font-display: "Space Grotesk", "Inter Tight", system-ui, sans-serif;
  --font-num: ui-monospace, "SF Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-18 {
    --accent: oklch(0.4 0.09 178);
    --warn: oklch(0.6 0.13 70);
    --error: oklch(0.5 0.18 30);
    --error-ink: oklch(0.42 0.18 30);
  }
}

.fv-18 *,
.fv-18 *::before,
.fv-18 *::after {
  box-sizing: border-box;
}

.fv-18__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
}

.fv-18__card {
  inline-size: min(100%, 32rem);
  min-inline-size: 0;
  display: grid;
  gap: 1.125rem;
  padding: clamp(1.25rem, 4vw, 1.75rem);
  background: var(--surface);
  border: 1.5px solid var(--ink);
  border-radius: 0.375rem;
  box-shadow: var(--shadow-x) var(--shadow-x) 0 0 var(--accent);
}

.fv-18__head {
  min-inline-size: 0;
  display: grid;
  gap: 0.375rem;
}

.fv-18__eyebrow {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-18__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 3.6vw, 1.65rem);
  font-weight: 650;
  letter-spacing: -0.02em;
  line-height: 1.15;
}

.fv-18__sub {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-18__pair {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);
  align-items: start;
  gap: 0.75rem;
  min-inline-size: 0;
}

.fv-18__link {
  align-self: center;
  inline-size: 1.25rem;
  block-size: 1.5px;
  margin-block-start: 1.5rem;
  background: var(--ink);
}

.fv-18__field {
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
}

.fv-18__label {
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.fv-18__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.875rem;
  padding: 0 0.75rem;
  font-family: var(--font-num);
  font-size: 0.9375rem;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
  background: #ffffff;
  border: 1.5px solid var(--rule);
  border-radius: 0.25rem;
}

.fv-18__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-18__input:in-range {
  border-color: var(--rule);
}

.fv-18__input:out-of-range {
  border-color: var(--warn);
  background: #fdf4e6;
}

.fv-18__input:invalid:not(:focus) {
  border-color: var(--error);
}

.fv-18__input:user-invalid {
  border-color: var(--error);
  background: #fdf0ec;
}

.fv-18__input:user-valid {
  border-color: var(--accent);
}

.fv-18__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  font-weight: 500;
  color: var(--error-ink);
}

.fv-18__msg span {
  min-inline-size: 0;
}

.fv-18__icon {
  flex: none;
  inline-size: 0.9375rem;
  block-size: 0.9375rem;
  margin-block-start: 0.1rem;
}

.fv-18__input:invalid:not(:focus) + .fv-18__msg,
.fv-18__input:out-of-range + .fv-18__msg,
.fv-18__input:user-invalid + .fv-18__msg {
  display: flex;
}

.fv-18__summary {
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
  padding: 0.75rem 0.875rem;
  border: 1.5px dashed var(--rule);
  border-radius: 0.25rem;
}

.fv-18__nightsrow {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.5rem;
  margin: 0;
  min-inline-size: 0;
}

.fv-18__nightslabel {
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-18__nights {
  font-family: var(--font-num);
  font-size: 1rem;
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.fv-18__band {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
}

.fv-18__bandtext {
  display: none;
}

.fv-18__card[data-range="idle"] .fv-18__bandtext[data-idle] {
  display: block;
  color: var(--muted);
}

.fv-18__card[data-range="bad"] .fv-18__bandtext[data-bad] {
  display: block;
  color: var(--error-ink);
  font-weight: 600;
}

.fv-18__card[data-range="ok"] .fv-18__bandtext[data-ok] {
  display: block;
  color: var(--accent);
  font-weight: 600;
}

.fv-18__btn {
  justify-self: start;
  min-block-size: 2.875rem;
  min-inline-size: 44px;
  padding: 0.75rem 1.375rem;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 650;
  color: var(--surface);
  background: var(--accent);
  border: 1.5px solid var(--ink);
  border-radius: 0.25rem;
  cursor: pointer;
}

.fv-18__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

@media (max-width: 26rem) {
  .fv-18__pair {
    grid-template-columns: minmax(0, 1fr);
  }

  .fv-18__link {
    inline-size: 1.5px;
    block-size: 1rem;
    margin: 0 0 0 0.75rem;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-18:not(:has(#fv-18-theme-light:checked)) {
    --page: #0b1614;
    --surface: #10201e;
    --ink: #e6f2ef;
    --muted: #8fa8a4;
    --rule: #274038;
    --accent: #52c9b4;
    --warn: #e5a54a;
    --error: #ff7f63;
    --error-ink: #ff9c85;
  }

  .fv-18:not(:has(#fv-18-theme-light:checked)) .fv-18__input {
    background: #0c1a18;
  }

  .fv-18:not(:has(#fv-18-theme-light:checked)) .fv-18__input:out-of-range {
    background: #2a1f0e;
  }

  .fv-18:not(:has(#fv-18-theme-light:checked)) .fv-18__input:user-invalid {
    background: #2a1310;
  }

  .fv-18:not(:has(#fv-18-theme-light:checked)) .fv-18__btn {
    color: #05100e;
  }

  .fv-18:not(:has(#fv-18-theme-light:checked)) .fv-18__card {
    box-shadow: var(--shadow-x) var(--shadow-x) 0 0 var(--accent);
  }
}

[data-theme="dark"] .fv-18:not(:has(#fv-18-theme-light:checked)) {
  --page: #0b1614;
  --surface: #10201e;
  --ink: #e6f2ef;
  --muted: #8fa8a4;
  --rule: #274038;
  --accent: #52c9b4;
  --warn: #e5a54a;
  --error: #ff7f63;
  --error-ink: #ff9c85;
}

[data-theme="dark"] .fv-18:not(:has(#fv-18-theme-light:checked)) .fv-18__input {
  background: #0c1a18;
}

[data-theme="dark"] .fv-18:not(:has(#fv-18-theme-light:checked)) .fv-18__btn {
  color: #05100e;
}

.fv-18 {
  position: relative;
}

.fv-18__stage {
  padding-block-start: 4.75rem;
}

.fv-18__theme {
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

.fv-18__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-18__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-18__themeopt {
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

.fv-18__themeopt:hover {
  opacity: 0.85;
}

.fv-18__themeinput:checked + .fv-18__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-18__themeinput:focus-visible + .fv-18__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-18__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-18__themeinput:checked + .fv-18__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-18:has(#fv-18-theme-dark:checked) {
  --page: #0b1614;
  --surface: #10201e;
  --ink: #e6f2ef;
  --muted: #8fa8a4;
  --rule: #274038;
  --accent: #52c9b4;
  --warn: #e5a54a;
  --error: #ff7f63;
  --error-ink: #ff9c85;
}

.fv-18:has(#fv-18-theme-dark:checked) .fv-18__input {
  background: #0c1a18;
}

.fv-18:has(#fv-18-theme-dark:checked) .fv-18__input:out-of-range {
  background: #2a1f0e;
}

.fv-18:has(#fv-18-theme-dark:checked) .fv-18__input:user-invalid {
  background: #2a1310;
}

.fv-18:has(#fv-18-theme-dark:checked) .fv-18__btn {
  color: #05100e;
}

.fv-18:has(#fv-18-theme-dark:checked) .fv-18__card {
  box-shadow: var(--shadow-x) var(--shadow-x) 0 0 var(--accent);
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-18__card');
  if (!form || form.dataset.fv18) return;
  form.dataset.fv18 = '1';
  const start = form.querySelector('#fv-18-start');
  const end = form.querySelector('#fv-18-end');
  const nights = form.querySelector('.fv-18__nights');
  const sync = () => {
    if (start.value) end.min = start.value;
    const bad = Boolean(start.value && end.value && end.value <= start.value);
    end.setCustomValidity(bad ? 'The departure date must be after the arrival date.' : '');
    const span = start.value && end.value ? Math.round((Date.parse(end.value) - Date.parse(start.value)) / 86400000) : 0;
    nights.value = span > 0 ? span + (span === 1 ? ' night' : ' nights') : '—';
    form.dataset.range = bad ? 'bad' : span > 0 ? 'ok' : 'idle';
  };
  ['input', 'change'].forEach((ev) => { start.addEventListener(ev, sync); end.addEventListener(ev, sync); });
  form.querySelector('.fv-18__btn').addEventListener('click', () => { sync(); if (!form.checkValidity()) form.reportValidity(); });
  form.addEventListener('keydown', (e) => { if (e.key === 'Enter' && e.target.tagName === 'INPUT') { e.preventDefault(); sync(); form.reportValidity(); } });
  sync();
})();
```
