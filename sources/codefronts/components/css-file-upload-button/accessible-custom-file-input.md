---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/accessible-custom-file-input/"
title: "Accessible Custom File Input"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "The reference implementation for the whole collection: a file input that passes a keyboard-only audit, a screen-reader pass and a forced-colors check."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Custom File Input
Source: https://codefronts.com/components/css-file-upload-button/accessible-custom-file-input/

The reference implementation for the whole collection: a file input that passes a keyboard-only audit, a screen-reader pass and a forced-colors check. Help text is wired with aria-describedby, validation failures set aria-invalid and point at a role="alert" message via aria-errormessage, focus is moved deliberately after every state change, and the focus indicator meets WCAG 2.2's Focus Appearance criterion — 2px thick, 3:1 contrast, never clipped.
## HTML
```html
<div class="fu-05">
  <button class="fu-05__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-05__card" aria-labelledby="fu-05-h">
    <h2 class="fu-05__h" id="fu-05-h">Import your member list</h2>

    <div class="fu-05__field">
      <input class="fu-05__input" id="fu-05-file" type="file" accept=".csv,.xlsx"
             aria-describedby="fu-05-hint" aria-errormessage="fu-05-err" aria-invalid="false">
      <label class="fu-05__label" for="fu-05-file">
        <span class="fu-05__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 15.5V4.5m0 0L8.2 8.3M12 4.5l3.8 3.8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M4.5 14.5v3.2A2.3 2.3 0 0 0 6.8 20h10.4a2.3 2.3 0 0 0 2.3-2.3v-3.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </span>
        <span class="fu-05__labelCol">
          <span class="fu-05__labelTop">Choose a spreadsheet</span>
          <span class="fu-05__labelSub" id="fu-05-hint">CSV or XLSX <span aria-hidden="true">·</span> 5 MB maximum</span>
        </span>
      </label>
    </div>

    <p class="fu-05__err" id="fu-05-err" role="alert" hidden></p>

    <div class="fu-05__ok" id="fu-05-ok" hidden>
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m5 12.5 4.3 4.3L19 7" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <span class="fu-05__okName" id="fu-05-ok-name"></span>
      <button class="fu-05__undo" id="fu-05-undo" type="button">Remove</button>
    </div>

    <p class="fu-05__status" id="fu-05-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

.fu-05 {
  --bg: #fbfbfd;
  --surface: #ffffff;
  --ink: #0a0a0f;
  --muted: #4d5361;
  --line: #d8dce5;
  --acc: #1740ff;
  --ok: #0a7d4f;
  --danger: #c81e35;
  --ring: #1740ff;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.fu-05,
.fu-05 *,
.fu-05 *::before,
.fu-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-05 {
    --acc: oklch(48% .26 268);
    --ok: oklch(50% .13 158);
    --danger: oklch(52% .21 22);
  }
}

.fu-05__card {
  inline-size: min(31rem,100%);
  display: grid;
  gap: 1rem;
  /* grid items default to min-width:auto, so a long unbroken filename in
       the status row would otherwise force the card past its own width */
  grid-template-columns: minmax(0,1fr);
  padding: clamp(1.25rem,4vw,2rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  box-shadow: 0 20px 45px -35px rgba(10,10,15,.4);
}

.fu-05__h {
  margin: 0;
  font-size: clamp(1.25rem,3vw,1.5rem);
  font-weight: 600;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.fu-05__field {
  position: relative;
}

.fu-05__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  border: 0;
  overflow: hidden;
  opacity: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
}

.fu-05__label {
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
  user-select: none;
  min-block-size: 4.5rem;
  padding: 1rem 1.15rem;
  border-radius: 1rem;
  border: 2px solid var(--line);
  background: var(--surface);
  transition: border-color .25s ease, background .25s ease, box-shadow .25s ease;
}

.fu-05__label:hover {
  border-color: var(--acc);
  background: color-mix(in oklab,var(--acc) 5%,var(--surface));
}

.fu-05__input:focus-visible + .fu-05__label {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
  border-color: var(--acc);
}

.fu-05__icon {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  flex: none;
  border-radius: .8rem;
  background: color-mix(in oklab,var(--acc) 12%,transparent);
  color: var(--acc);
}

.fu-05__icon svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.fu-05__labelCol {
  display: grid;
  gap: .2rem;
}

.fu-05__labelTop {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.fu-05__labelSub {
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
}
/* error state derives from the same attribute assistive tech reads */

.fu-05__field:has(.fu-05__input[aria-invalid="true"]) .fu-05__label {
  border-color: var(--danger);
  background: color-mix(in oklab,var(--danger) 7%,var(--surface));
}

.fu-05__field:has(.fu-05__input[aria-invalid="true"]) .fu-05__icon {
  background: color-mix(in oklab,var(--danger) 14%,transparent);
  color: var(--danger);
}

.fu-05__err {
  margin: 0;
  display: flex;
  gap: .5rem;
  padding: .7rem .85rem;
  border-radius: .75rem;
  background: color-mix(in oklab,var(--danger) 10%,transparent);
  border: 1px solid color-mix(in oklab,var(--danger) 35%,transparent);
  color: color-mix(in oklab,var(--danger) 75%,var(--ink));
  font-size: .875rem;
  line-height: 1.5;
}

.fu-05__err[hidden] {
  display: none;
}

.fu-05__err::before {
  content: "!";
  font-weight: 700;
  font-family: var(--mono);
}

.fu-05__ok {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-inline-size: 0;
  padding: .7rem .85rem;
  border-radius: .75rem;
  background: color-mix(in oklab,var(--ok) 9%,transparent);
  border: 1px solid color-mix(in oklab,var(--ok) 32%,transparent);
  color: color-mix(in oklab,var(--ok) 78%,var(--ink));
  font-size: .875rem;
}

.fu-05__ok[hidden] {
  display: none;
}

.fu-05__ok svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.fu-05__okName {
  flex: 1;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 600;
}

.fu-05__undo {
  min-block-size: 2.75rem;
  padding: .5rem .9rem;
  cursor: pointer;
  border-radius: .6rem;
  border: 1px solid color-mix(in oklab,var(--ok) 40%,transparent);
  background: transparent;
  color: inherit;
  font-family: var(--sans);
  font-size: .8125rem;
  font-weight: 600;
  transition: background .2s ease;
}

.fu-05__undo:hover {
  background: color-mix(in oklab,var(--ok) 14%,transparent);
}

.fu-05__undo:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.fu-05__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
}

@media (prefers-color-scheme: dark) {
  .fu-05:not([data-theme="light"]) {
    --bg: #08080c;
    --surface: #101118;
    --ink: #f4f5f9;
    --muted: #98a0b2;
    --line: #272c3a;
    --acc: #8aa0ff;
    --ok: #4ade9b;
    --danger: #ff7a8a;
    --ring: #8aa0ff;
  }
}

.fu-05[data-theme="dark"] {
  --bg: #08080c;
  --surface: #101118;
  --ink: #f4f5f9;
  --muted: #98a0b2;
  --line: #272c3a;
  --acc: #8aa0ff;
  --ok: #4ade9b;
  --danger: #ff7a8a;
  --ring: #8aa0ff;
}

@media (prefers-reduced-motion: reduce) {
  .fu-05 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-05__label {
    border: 2px solid ButtonText;
  }

  .fu-05__input:focus-visible + .fu-05__label {
    outline: 2px solid Highlight;
  }

  .fu-05__icon {
    background: Highlight;
    color: HighlightText;
  }

  .fu-05__err,
    .fu-05__ok {
    border: 1px solid CanvasText;
    background: Canvas;
    color: CanvasText;
  }
}
/* ── in-demo theme toggle ── */

.fu-05 {
  position: relative;
}

.fu-05__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.4rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.4rem);
  z-index: 20;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,currentColor 30%,transparent);
  background: color-mix(in oklab,currentColor 12%,transparent);
  color: inherit;
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.fu-05__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-05__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-05__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-05__sun {
  display: none;
}

.fu-05__theme[aria-pressed="true"] .fu-05__sun {
  display: block;
}

.fu-05__theme[aria-pressed="true"] .fu-05__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-05__theme {
    transition: none;
  }

  .fu-05__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-05__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-05');
  if (!root) return;
  const input = root.querySelector('#fu-05-file');
  const err = root.querySelector('#fu-05-err');
  const ok = root.querySelector('#fu-05-ok');
  const okName = root.querySelector('#fu-05-ok-name');
  const status = root.querySelector('#fu-05-status');
  const MAX_MB = 5, ACCEPT = ['csv', 'xlsx'];

  const fail = (msg) => {
    input.setAttribute('aria-invalid', 'true');
    err.textContent = msg; err.hidden = false;
    ok.hidden = true; input.value = '';
    input.focus();                       // return focus so retry is one keystroke away
  };
  const pass = (file) => {
    input.setAttribute('aria-invalid', 'false');
    err.hidden = true; err.textContent = '';
    okName.textContent = file.name; ok.hidden = false;
    status.textContent = file.name + ' accepted and ready to import';
  };

  input.addEventListener('change', () => {
    const file = input.files && input.files[0];
    if (!file) return;
    const ext = (file.name.split('.').pop() || '').toLowerCase();
    if (!ACCEPT.includes(ext)) return fail('“' + file.name + '” is a .' + ext + ' file. Choose a CSV or XLSX file instead.');
    if (file.size > MAX_MB * 1024 * 1024) return fail('“' + file.name + '” is larger than the ' + MAX_MB + ' MB limit. Split the export and try again.');
    pass(file);
  });

  root.querySelector('#fu-05-undo').addEventListener('click', () => {
    input.value = '';
    input.setAttribute('aria-invalid', 'false');
    ok.hidden = true;
    status.textContent = 'Selection cleared';
    input.focus();
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-05');
  const btn = root && root.querySelector('.fu-05__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
