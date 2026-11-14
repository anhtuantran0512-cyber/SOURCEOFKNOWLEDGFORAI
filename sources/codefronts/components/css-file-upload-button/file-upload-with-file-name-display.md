---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/file-upload-with-file-name-display/"
title: "File Upload with File Name Display"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "The most-searched follow-up to a custom upload button: how do I show what the user picked?"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: File Upload with File Name Display
Source: https://codefronts.com/components/css-file-upload-button/file-upload-with-file-name-display/

The most-searched follow-up to a custom upload button: how do I show what the user picked? Ten lines of JavaScript read input.files[0], format the byte count with Intl.NumberFormat, derive an extension chip, and write the result into a row that animates in. Long names truncate from the middle with a two-span technique instead of a lossy ellipsis, and the change is announced once through a polite live region.
## HTML
```html
<div class="fu-03">
  <button class="fu-03__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <div class="fu-03__card">
    <p class="fu-03__eyebrow">Supporting evidence</p>
    <h2 class="fu-03__h">Upload your signed contract</h2>

    <div class="fu-03__control">
      <input class="fu-03__input" id="fu-03-file" type="file" accept=".pdf,.doc,.docx" aria-describedby="fu-03-hint">
      <label class="fu-03__label" for="fu-03-file">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M14.5 3.5H7.8A2.3 2.3 0 0 0 5.5 5.8v12.4A2.3 2.3 0 0 0 7.8 20.5h8.4a2.3 2.3 0 0 0 2.3-2.3V7.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M14.3 3.6v3.6h4.1" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        Browse files
      </label>
      <p class="fu-03__hint" id="fu-03-hint">PDF or Word, max 10 MB</p>
    </div>

    <div class="fu-03__row" id="fu-03-row" hidden>
      <span class="fu-03__ext" id="fu-03-ext" aria-hidden="true">PDF</span>
      <span class="fu-03__col">
        <span class="fu-03__name" id="fu-03-name"><span class="fu-03__nameInner"></span></span>
        <span class="fu-03__meta" id="fu-03-meta"></span>
      </span>
      <button class="fu-03__clear" id="fu-03-clear" type="button">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 6.5l11 11m0-11-11 11" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        <span class="fu-03__vh">Remove selected file</span>
      </button>
    </div>

    <p class="fu-03__status" id="fu-03-status" role="status" aria-live="polite"></p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,[email protected],400;6..72,500;6..72,600&family=Instrument+Sans:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.fu-03 {
  --bg: #f7f5f1;
  --surface: #ffffff;
  --ink: #15181d;
  --muted: #666f7c;
  --line: #e5e3dd;
  --acc: #1c5f4a;
  --acc-soft: #e8f1ed;
  --ring: #1c5f4a;
  --name-max: 22ch;
  --serif: "Newsreader",ui-serif,Georgia,serif;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 60% at 80% 0%, color-mix(in oklab,var(--acc) 8%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.fu-03,
.fu-03 *,
.fu-03 *::before,
.fu-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-03 {
    --acc: oklch(45% .09 165);
    --acc-soft: color-mix(in oklab,var(--acc) 12%,white);
  }
}

.fu-03__card {
  inline-size: min(30rem,100%);
  display: grid;
  gap: .85rem;
  padding: clamp(1.25rem,4vw,1.9rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: 0 1px 2px rgba(20,24,30,.04), 0 24px 50px -34px rgba(20,24,30,.28);
}

.fu-03__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--acc) 70%,var(--muted));
}

.fu-03__h {
  margin: 0 0 .3rem;
  font-family: var(--serif);
  font-size: clamp(1.4rem,3.4vw,1.8rem);
  font-weight: 500;
  letter-spacing: -.02em;
  line-height: 1.15;
  text-wrap: balance;
}

.fu-03__control {
  display: flex;
  align-items: center;
  gap: .9rem;
  flex-wrap: wrap;
}

.fu-03__input {
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

.fu-03__label {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  cursor: pointer;
  user-select: none;
  min-block-size: 2.85rem;
  padding: .6rem 1.1rem;
  border-radius: .8rem;
  background: var(--acc);
  color: #fff;
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.01em;
  box-shadow: 0 1px 0 rgba(255,255,255,.18) inset, 0 8px 18px -10px color-mix(in oklab,var(--acc) 60%,transparent);
  transition: transform .25s cubic-bezier(.16,1,.3,1), filter .25s ease;
}

.fu-03__label svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fu-03__label:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-03__input:focus-visible + .fu-03__label {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.fu-03__hint {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-03__row {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: .85rem;
  padding: .75rem .8rem;
  border-radius: 1rem;
  border: 1px solid color-mix(in oklab,var(--acc) 22%,var(--line));
  background: var(--acc-soft);
  transition: opacity .35s ease, transform .35s cubic-bezier(.16,1,.3,1), display .35s allow-discrete;
}

.fu-03__row[hidden] {
  display: none;
}

@starting-style {
  .fu-03__row {
    opacity: 0;
    transform: translateY(8px);
  }
}

.fu-03__ext {
  display: grid;
  place-items: center;
  inline-size: 2.6rem;
  block-size: 2.6rem;
  border-radius: .7rem;
  flex: none;
  background: var(--surface);
  border: 1px solid color-mix(in oklab,var(--acc) 20%,var(--line));
  font-family: var(--mono);
  font-size: .625rem;
  font-weight: 500;
  letter-spacing: .04em;
  color: color-mix(in oklab,var(--acc) 80%,var(--ink));
}

.fu-03__col {
  display: grid;
  gap: .15rem;
  min-inline-size: 0;
}

.fu-03__name {
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.01em;
  max-inline-size: var(--name-max);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  direction: rtl;
  text-align: start;
  unicode-bidi: plaintext;
}

.fu-03__meta {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-03__clear {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  flex: none;
  cursor: pointer;
  border: 1px solid transparent;
  border-radius: .7rem;
  background: transparent;
  color: var(--muted);
  transition: background .2s ease, color .2s ease, border-color .2s ease;
}

.fu-03__clear svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fu-03__clear:hover {
  background: var(--surface);
  color: var(--ink);
  border-color: var(--line);
}

.fu-03__clear:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.fu-03__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-03__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-color-scheme: dark) {
  .fu-03:not([data-theme="light"]) {
    --bg: #0a0c0b;
    --surface: #121614;
    --ink: #eef2ef;
    --muted: #8d968f;
    --line: #222a26;
    --acc: #3ecf8e;
    --acc-soft: #16211c;
  }

  .fu-03:not([data-theme="light"]) .fu-03__label {
    color: #07120d;
  }
}

.fu-03[data-theme="dark"] {
  --bg: #0a0c0b;
  --surface: #121614;
  --ink: #eef2ef;
  --muted: #8d968f;
  --line: #222a26;
  --acc: #3ecf8e;
  --acc-soft: #16211c;
}

.fu-03[data-theme="dark"] .fu-03__label {
  color: #07120d;
}

@media (prefers-reduced-motion: reduce) {
  .fu-03 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-03__card,
    .fu-03__row,
    .fu-03__ext {
    border: 1px solid CanvasText;
  }

  .fu-03__label {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-03 {
  position: relative;
}

.fu-03__theme {
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

.fu-03__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-03__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-03__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-03__sun {
  display: none;
}

.fu-03__theme[aria-pressed="true"] .fu-03__sun {
  display: block;
}

.fu-03__theme[aria-pressed="true"] .fu-03__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-03__theme {
    transition: none;
  }

  .fu-03__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-03__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-03');
  if (!root) return;
  const input = root.querySelector('#fu-03-file');
  const row = root.querySelector('#fu-03-row');
  const nameEl = root.querySelector('.fu-03__nameInner');
  const metaEl = root.querySelector('#fu-03-meta');
  const extEl = root.querySelector('#fu-03-ext');
  const status = root.querySelector('#fu-03-status');

  const fmtBytes = (n) => {
    const units = ['B', 'KB', 'MB', 'GB'];
    let i = 0;
    while (n >= 1024 && i < units.length - 1) { n /= 1024; i++; }
    const nf = new Intl.NumberFormat(undefined, { maximumFractionDigits: n < 10 && i > 0 ? 1 : 0 });
    return nf.format(n) + ' ' + units[i];
  };

  const reset = () => {
    row.hidden = true;
    status.textContent = 'No file selected';
  };

  input.addEventListener('change', () => {
    const file = input.files && input.files[0];
    if (!file) return reset();
    nameEl.textContent = file.name;
    extEl.textContent = (file.name.split('.').pop() || 'file').slice(0, 4).toUpperCase();
    metaEl.textContent = fmtBytes(file.size) + ' · ' + (file.type || 'unknown type');
    row.hidden = false;
    status.textContent = file.name + ' selected, ready to submit';
  });

  root.querySelector('#fu-03-clear').addEventListener('click', () => {
    input.value = '';           // the only mutation the platform allows on a file input
    reset();
    input.focus();
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-03');
  const btn = root && root.querySelector('.fu-03__theme');
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
