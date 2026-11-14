---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/character-counter-limit-warning/"
title: "Character Counter Limit Warning"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "A live count under a <textarea> with maxlength, moving through three bands: normal, approaching in the last ten percent, and at the limit."
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Character Counter Limit Warning
Source: https://codefronts.com/components/css-form-validation/character-counter-limit-warning/

A live count under a <textarea> with maxlength, moving through three bands: normal, approaching in the last ten percent, and at the limit. The count lives in an <output> with tabular-nums so the digits do not jitter, and the announcement fires once when a band is crossed — never on every keystroke, which is how counters become unusable with a screen reader.
## HTML
```html
<section class="fv-08" aria-labelledby="fv-08-h">
  <fieldset class="fv-08__theme">
    <legend class="fv-08__themelegend">Theme</legend>
    <input class="fv-08__themeinput" type="radio" name="fv-08-theme" id="fv-08-theme-auto" checked>
    <label class="fv-08__themeopt" for="fv-08-theme-auto">Auto</label>
    <input class="fv-08__themeinput" type="radio" name="fv-08-theme" id="fv-08-theme-light">
    <label class="fv-08__themeopt" for="fv-08-theme-light">Light</label>
    <input class="fv-08__themeinput" type="radio" name="fv-08-theme" id="fv-08-theme-dark">
    <label class="fv-08__themeopt" for="fv-08-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-08__stage">
    <div class="fv-08__box" data-band="near">
      <header class="fv-08__head">
        <p class="fv-08__eyebrow">Talon · incident note</p>
        <h2 class="fv-08__h" id="fv-08-h">Warn before the typing stops</h2>
      </header>

      <div class="fv-08__field">
        <div class="fv-08__labelrow">
          <label class="fv-08__label" for="fv-08-note">Public status update</label>
          <span class="fv-08__cap">Max 180</span>
        </div>
        <textarea class="fv-08__area" id="fv-08-note" name="fv-08-note" rows="4" maxlength="180" required placeholder="What are customers seeing right now?" aria-describedby="fv-08-help">API latency in eu-west is elevated for dashboard queries. Writes are unaffected. We are failing over the read replicas now and will post an update within 30 minutes.</textarea>

        <div class="fv-08__meter">
          <span class="fv-08__ring" aria-hidden="true"></span>
          <output class="fv-08__count" for="fv-08-note">165 / 180</output>
          <p class="fv-08__help" id="fv-08-help">
            <svg class="fv-08__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 2.8 18.2 17H1.8Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"></path><path d="M10 8.2v3.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.3" r="1" fill="currentColor"></circle></svg>
            <span class="fv-08__helptext" data-ok>Keep it short — this posts to the public status page.</span>
            <span class="fv-08__helptext" data-near>Approaching the limit. 15 characters left before typing stops.</span>
            <span class="fv-08__helptext" data-limit>Limit reached. Trim the note — the field will not accept more characters.</span>
          </p>
        </div>
        <p class="fv-08__live" role="status" aria-live="polite"></p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-08 {
  --page: #17140f;
  --surface: #201c15;
  --well: #14110c;
  --ink: #f5eee0;
  --muted: #a2957f;
  --rule: #332c21;
  --ok: #8b9a7b;
  --warn: #e8a33c;
  --limit-hue: #ff6b4a;
  --pad: 0.875rem;
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
  .fv-08 {
    --warn: oklch(0.78 0.15 72);
    --limit-hue: oklch(0.68 0.2 32);
    --ok: oklch(0.7 0.05 130);
  }
}

.fv-08 *,
.fv-08 *::before,
.fv-08 *::after {
  box-sizing: border-box;
}

.fv-08__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(0.875rem, 4vw, 2.5rem);
}

.fv-08__box {
  inline-size: min(100%, 30rem);
  min-inline-size: 0;
  display: grid;
  gap: 0.875rem;
  padding: clamp(1rem, 3vw, 1.375rem);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  box-shadow: 0 0 0 1px rgba(232, 163, 60, 0.06), 0 0 44px -12px rgba(232, 163, 60, 0.18);
}

.fv-08__head {
  min-inline-size: 0;
}

.fv-08__eyebrow {
  margin: 0 0 0.375rem;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--warn);
}

.fv-08__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.125rem, 3.2vw, 1.4rem);
  font-weight: 500;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.fv-08__field {
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
}

.fv-08__labelrow {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.5rem;
  min-inline-size: 0;
}

.fv-08__label {
  font-size: 0.8125rem;
  font-weight: 600;
}

.fv-08__cap {
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  color: var(--muted);
}

.fv-08__area {
  min-inline-size: 0;
  inline-size: 100%;
  padding: var(--pad);
  font: inherit;
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--ink);
  background: var(--well);
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  resize: vertical;
  transition: border-color 0.16s ease;
}

.fv-08__area::placeholder {
  color: #6d6252;
}

.fv-08__area:focus-visible {
  outline: 2px solid var(--warn);
  outline-offset: 2px;
}

@supports (field-sizing: content) {
  .fv-08__area {
    field-sizing: content;
    min-block-size: 5.5rem;
    max-block-size: 14rem;
  }
}

.fv-08__meter {
  display: grid;
  grid-template-columns: auto auto minmax(0, 1fr);
  align-items: center;
  gap: 0.5rem 0.625rem;
  min-inline-size: 0;
}

.fv-08__ring {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  border-radius: 50%;
  background: conic-gradient(var(--band, var(--ok)) 0 var(--fill, 0%), #2e2720 var(--fill, 0%) 100%);
  mask: radial-gradient(circle, transparent 56%, #000 58%);
  -webkit-mask: radial-gradient(circle, transparent 56%, #000 58%);
}

.fv-08__count {
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.02em;
  color: var(--band, var(--muted));
}

.fv-08__help {
  grid-column: 1 / -1;
  display: flex;
  gap: 0.4375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-08__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
  opacity: 0;
}

.fv-08__helptext {
  display: none;
  min-inline-size: 0;
}

.fv-08__box[data-band="ok"] {
  --band: var(--ok);
}

.fv-08__box[data-band="ok"] .fv-08__helptext[data-ok] {
  display: block;
}

.fv-08__box[data-band="near"] {
  --band: var(--warn);
}

.fv-08__box[data-band="near"] .fv-08__helptext[data-near] {
  display: block;
}

.fv-08__box[data-band="near"] .fv-08__icon {
  opacity: 1;
  color: var(--warn);
}

.fv-08__box[data-band="near"] .fv-08__help {
  color: var(--warn);
}

.fv-08__box[data-band="near"] .fv-08__area {
  border-color: var(--warn);
}

.fv-08__box[data-band="limit"] {
  --band: var(--limit-hue);
}

.fv-08__box[data-band="limit"] .fv-08__helptext[data-limit] {
  display: block;
}

.fv-08__box[data-band="limit"] .fv-08__icon {
  opacity: 1;
  color: var(--limit-hue);
}

.fv-08__box[data-band="limit"] .fv-08__help {
  color: var(--limit-hue);
  font-weight: 550;
}

.fv-08__box[data-band="limit"] .fv-08__area {
  border-color: var(--limit-hue);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .fv-08__box[data-band="near"] .fv-08__area {
    background: color-mix(in oklab, var(--well) 88%, var(--warn));
  }

  .fv-08__box[data-band="limit"] .fv-08__area {
    background: color-mix(in oklab, var(--well) 84%, var(--limit-hue));
  }
}

.fv-08__area:user-invalid {
  border-color: var(--limit-hue);
}

.fv-08__live {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .fv-08__area {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .fv-08:not(:has(#fv-08-theme-dark:checked)) {
    --page: #f6f3ec;
    --surface: #ffffff;
    --well: #fbf9f4;
    --ink: #221d15;
    --muted: #6f6555;
    --rule: #e3ddd0;
    --warn: #a56a09;
    --limit-hue: #bf3618;
    --ok: #5f6f4f;
  }

  .fv-08:not(:has(#fv-08-theme-dark:checked)) .fv-08__box {
    box-shadow: 0 1px 2px rgba(34, 29, 21, 0.06), 0 20px 40px -34px rgba(34, 29, 21, 0.5);
  }

  .fv-08:not(:has(#fv-08-theme-dark:checked)) .fv-08__area::placeholder {
    color: #a89c88;
  }

  .fv-08:not(:has(#fv-08-theme-dark:checked)) .fv-08__ring {
    background: conic-gradient(var(--band, var(--ok)) 0 var(--fill, 0%), #e6e0d4 var(--fill, 0%) 100%);
  }
}

[data-theme="dark"] .fv-08:not(:has(#fv-08-theme-light:checked)) {
  --page: #17140f;
  --surface: #201c15;
  --well: #14110c;
  --ink: #f5eee0;
  --muted: #a2957f;
  --rule: #332c21;
  --warn: #e8a33c;
  --limit-hue: #ff6b4a;
  --ok: #8b9a7b;
}

[data-theme="dark"] .fv-08:not(:has(#fv-08-theme-light:checked)) .fv-08__ring {
  background: conic-gradient(var(--band, var(--ok)) 0 var(--fill, 0%), #2e2720 var(--fill, 0%) 100%);
}

.fv-08 {
  position: relative;
}

.fv-08__stage {
  padding-block-start: 4.75rem;
}

.fv-08__theme {
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

.fv-08__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-08__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-08__themeopt {
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

.fv-08__themeopt:hover {
  opacity: 0.85;
}

.fv-08__themeinput:checked + .fv-08__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-08__themeinput:focus-visible + .fv-08__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-08__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-08__themeinput:checked + .fv-08__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-08:has(#fv-08-theme-light:checked) {
  --page: #f6f3ec;
  --surface: #ffffff;
  --well: #fbf9f4;
  --ink: #221d15;
  --muted: #6f6555;
  --rule: #e3ddd0;
  --warn: #a56a09;
  --limit-hue: #bf3618;
  --ok: #5f6f4f;
}

.fv-08:has(#fv-08-theme-light:checked) .fv-08__box {
  box-shadow: 0 1px 2px rgba(34, 29, 21, 0.06), 0 20px 40px -34px rgba(34, 29, 21, 0.5);
}

.fv-08:has(#fv-08-theme-light:checked) .fv-08__area::placeholder {
  color: #a89c88;
}

.fv-08:has(#fv-08-theme-light:checked) .fv-08__ring {
  background: conic-gradient(var(--band, var(--ok)) 0 var(--fill, 0%), #e6e0d4 var(--fill, 0%) 100%);
}
```

## JavaScript
```js
(() => {
  const box = document.querySelector('.fv-08__box');
  if (!box || box.dataset.fv08) return;
  box.dataset.fv08 = '1';
  const area = box.querySelector('.fv-08__area');
  const out = box.querySelector('.fv-08__count');
  const live = box.querySelector('.fv-08__live');
  const max = Number(area.getAttribute('maxlength'));
  const near = Math.ceil(max * 0.9);
  let band = '';
  const render = () => {
    const n = area.value.length;
    const next = n >= max ? 'limit' : n >= near ? 'near' : 'ok';
    out.value = n + ' / ' + max;
    box.style.setProperty('--fill', Math.round((n / max) * 100) + '%');
    if (next === band) return;
    band = next;
    box.dataset.band = band;
    live.textContent = band === 'limit' ? 'Character limit reached. Trim the note to continue.'
      : band === 'near' ? (max - n) + ' characters remaining.' : '';
  };
  area.addEventListener('input', render);
  render();
})();
```
