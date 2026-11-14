---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/bootstrap-5-custom-file-input/"
title: "Bootstrap 5 Custom File Input"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "Bootstrap 5 dropped the old .custom-file wrapper: a file input is now just .form-control, and its native button is styled through the ::file-selector-button…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Custom File Input
Source: https://codefronts.com/components/css-file-upload-button/bootstrap-5-custom-file-input/

Bootstrap 5 dropped the old .custom-file wrapper: a file input is now just .form-control, and its native button is styled through the ::file-selector-button pseudo-element. This demo shows both routes side by side — the native styled input (best accessibility, zero JS) and the classic .btn-label pattern with a visually hidden input — plus validation feedback and a progress bar, all as scoped CSS with no Bootstrap CDN dependency.
## HTML
```html
<div class="fu-21">
  <button class="fu-21__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-21__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-21__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <div class="card">
    <div class="card-body">
      <h2 class="h5">Submit your entry</h2>
      <p class="text-body-secondary">Two Bootstrap 5 routes to the same control.</p>

      <div class="mb-3">
        <label class="form-label" for="fu-21-native">Native input, styled button</label>
        <input class="form-control" type="file" id="fu-21-native" accept=".zip,.pdf" aria-describedby="fu-21-help fu-21-bad">
        <div class="form-text" id="fu-21-help">ZIP or PDF, up to 20 MB.</div>
        <div class="invalid-feedback" id="fu-21-bad">Only ZIP and PDF files are accepted.</div>
      </div>

      <div class="mb-3">
        <label class="form-label" for="fu-21-btn">Button label, hidden input</label>
        <div class="input-group">
          <input class="visually-hidden" type="file" id="fu-21-btn" accept=".zip,.pdf">
          <label class="btn btn-primary" for="fu-21-btn">Choose file</label>
          <span class="input-group-text" id="fu-21-chosen">No file chosen</span>
        </div>
      </div>

      <div class="progress" id="fu-21-track" hidden>
        <div class="progress-bar" id="fu-21-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Upload progress">0%</div>
      </div>

      <div class="d-flex">
        <button class="btn btn-primary" id="fu-21-send" type="button" disabled>Upload entry</button>
        <button class="btn btn-outline" id="fu-21-clear" type="button">Clear</button>
      </div>

      <p class="form-text" id="fu-21-status" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');
/* ── Bootstrap-5-compatible tokens. In a real Bootstrap page these already exist. ── */

.fu-21 {
  --bs-body-bg: #f8f9fa;
  --bs-body-color: #212529;
  --bs-card-bg: #ffffff;
  --bs-border-color: #dee2e6;
  --bs-secondary-bg: #e9ecef;
  --bs-tertiary-bg: #f1f3f5;
  --bs-secondary-color: #6c757d;
  --bs-primary: #4f46e5;
  --bs-primary-hover: #4338ca;
  --bs-danger: #dc3545;
  --bs-success: #198754;
  --bs-border-radius: .5rem;
  --sans: "Public Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: var(--bs-body-bg);
  color: var(--bs-body-color);
  font-family: var(--sans);
}

.fu-21,
.fu-21 *,
.fu-21 *::before,
.fu-21 *::after {
  box-sizing: border-box;
}
/* ══════ scoped Bootstrap 5 component styles — delete inside a real Bootstrap build ══════ */

.fu-21 .card {
  inline-size: min(30rem,100%);
  background: var(--bs-card-bg);
  border: 1px solid var(--bs-border-color);
  border-radius: calc(var(--bs-border-radius) * 1.6);
  box-shadow: 0 .5rem 1.5rem rgba(33,37,41,.08);
}

.fu-21 .card-body {
  padding: clamp(1.15rem,4vw,1.75rem);
  display: grid;
  gap: .35rem;
}

.fu-21 .h5 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.fu-21 .text-body-secondary {
  margin: 0 0 .6rem;
  color: var(--bs-secondary-color);
  font-size: .9375rem;
}

.fu-21 .mb-3 {
  margin-block-end: 1rem;
  display: grid;
  gap: .4rem;
}

.fu-21 .form-label {
  font-size: .875rem;
  font-weight: 500;
}

.fu-21 .form-text {
  margin: 0;
  font-size: .8125rem;
  color: var(--bs-secondary-color);
}

.fu-21 .visually-hidden {
  position: absolute !important;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.fu-21 .form-control {
  inline-size: 100%;
  min-block-size: 2.75rem;
  padding: .5rem .75rem;
  font-family: inherit;
  font-size: .9375rem;
  color: var(--bs-body-color);
  background: var(--bs-card-bg);
  border: 1px solid var(--bs-border-color);
  border-radius: var(--bs-border-radius);
  transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
}

.fu-21 .form-control:focus-visible {
  outline: 2px solid var(--bs-primary);
  outline-offset: 1px;
  border-color: var(--bs-primary);
}
/* the Bootstrap 5 way: style the native button, hide nothing */

.fu-21 .form-control[type="file"]::file-selector-button {
  padding: .5rem .75rem;
  margin: -.5rem .75rem -.5rem -.75rem;
  cursor: pointer;
  block-size: calc(100% + 1rem);
  box-sizing: border-box;
  border-start-start-radius: calc(var(--bs-border-radius) - 1px);
  border-end-start-radius: calc(var(--bs-border-radius) - 1px);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  color: var(--bs-body-color);
  background: var(--bs-secondary-bg);
  border: 0;
  border-inline-end: 1px solid var(--bs-border-color);
  border-start-start-radius: var(--bs-border-radius);
  border-end-start-radius: var(--bs-border-radius);
  transition: background .15s ease-in-out;
}

.fu-21 .form-control[type="file"]:hover::file-selector-button {
  background: var(--bs-tertiary-bg);
}

.fu-21 .form-control[type="file"]::-webkit-file-upload-button {
  padding: .5rem .75rem;
  margin: -.5rem .75rem -.5rem -.75rem;
  cursor: pointer;
  block-size: calc(100% + 1rem);
  box-sizing: border-box;
  border-start-start-radius: calc(var(--bs-border-radius) - 1px);
  border-end-start-radius: calc(var(--bs-border-radius) - 1px);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  color: var(--bs-body-color);
  background: var(--bs-secondary-bg);
  border: 0;
  border-inline-end: 1px solid var(--bs-border-color);
}

.fu-21 .form-control.is-invalid {
  border-color: var(--bs-danger);
}

.fu-21 .invalid-feedback {
  display: none;
  font-size: .8125rem;
  color: var(--bs-danger);
}

.fu-21 .form-control.is-invalid ~ .invalid-feedback {
  display: block;
}

.fu-21 .form-control.is-invalid ~ .form-text {
  display: none;
}

.fu-21 .input-group {
  display: flex;
  align-items: stretch;
  flex-wrap: wrap;
}

.fu-21 .input-group-text {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .5rem .75rem;
  font-family: var(--mono);
  font-size: .8125rem;
  color: var(--bs-secondary-color);
  background: var(--bs-secondary-bg);
  border: 1px solid var(--bs-border-color);
  border-inline-start: 0;
  border-start-end-radius: var(--bs-border-radius);
  border-end-end-radius: var(--bs-border-radius);
  flex: 1;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-21 .btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  min-block-size: 2.75rem;
  padding: .5rem 1rem;
  border-radius: var(--bs-border-radius);
  font-family: inherit;
  font-size: .9375rem;
  font-weight: 600;
  border: 1px solid transparent;
  transition: background .15s ease-in-out, border-color .15s ease-in-out, transform .15s ease;
}

.fu-21 .input-group .btn {
  border-start-end-radius: 0;
  border-end-end-radius: 0;
}

.fu-21 .btn-primary {
  background: var(--bs-primary);
  color: #fff;
}

.fu-21 .btn-primary:hover {
  background: var(--bs-primary-hover);
}

.fu-21 .btn-outline {
  background: transparent;
  border-color: var(--bs-border-color);
  color: var(--bs-body-color);
}

.fu-21 .btn-outline:hover {
  background: var(--bs-secondary-bg);
}

.fu-21 .btn:disabled {
  opacity: .55;
  cursor: not-allowed;
}

.fu-21 .btn:focus-visible {
  outline: 2px solid var(--bs-primary);
  outline-offset: 2px;
}

.fu-21 .visually-hidden:focus-visible + .btn {
  outline: 2px solid var(--bs-primary);
  outline-offset: 2px;
}

.fu-21 .progress {
  block-size: .75rem;
  margin-block: .35rem .75rem;
  border-radius: 999px;
  overflow: hidden;
  background: var(--bs-secondary-bg);
}

.fu-21 .progress[hidden] {
  display: none;
}

.fu-21 .progress-bar {
  block-size: 100%;
  inline-size: 0%;
  display: grid;
  place-items: center;
  background: var(--bs-primary);
  color: #fff;
  font-size: .5625rem;
  font-family: var(--mono);
  transition: inline-size .2s linear;
}

.fu-21 .d-flex {
  display: flex;
  gap: .5rem;
  margin-block-start: .35rem;
}
/* ═════════════════════════ end scoped block ═════════════════════════ */

@media (prefers-color-scheme: dark) {
  .fu-21:not([data-theme="light"]) {
    --bs-body-bg: #0d0f14;
    --bs-body-color: #e9ecef;
    --bs-card-bg: #151920;
    --bs-border-color: #2b313c;
    --bs-secondary-bg: #1e232c;
    --bs-tertiary-bg: #252b36;
    --bs-secondary-color: #9aa3af;
    --bs-primary: #7c83ff;
    --bs-primary-hover: #6b73f5;
  }

  .fu-21:not([data-theme="light"]) .btn-primary {
    color: #0d0f14;
  }
}

.fu-21[data-theme="dark"] {
  --bs-body-bg: #0d0f14;
  --bs-body-color: #e9ecef;
  --bs-card-bg: #151920;
  --bs-border-color: #2b313c;
  --bs-secondary-bg: #1e232c;
  --bs-tertiary-bg: #252b36;
  --bs-secondary-color: #9aa3af;
  --bs-primary: #7c83ff;
  --bs-primary-hover: #6b73f5;
}

.fu-21[data-theme="dark"] .btn-primary {
  color: #0d0f14;
}

@media (prefers-reduced-motion: reduce) {
  .fu-21 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-21 .card,
    .fu-21 .form-control,
    .fu-21 .btn {
    border: 1px solid CanvasText;
  }

  .fu-21 .progress-bar {
    background: Highlight;
  }
}
/* ── in-demo theme toggle ── */

.fu-21 {
  position: relative;
}

.fu-21__theme {
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

.fu-21__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-21__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-21__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-21__sun {
  display: none;
}

.fu-21__theme[aria-pressed="true"] .fu-21__sun {
  display: block;
}

.fu-21__theme[aria-pressed="true"] .fu-21__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-21__theme {
    transition: none;
  }

  .fu-21__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-21__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-21');
  if (!root) return;
  const native = root.querySelector('#fu-21-native');
  const hidden = root.querySelector('#fu-21-btn');
  const chosen = root.querySelector('#fu-21-chosen');
  const track = root.querySelector('#fu-21-track');
  const bar = root.querySelector('#fu-21-bar');
  const send = root.querySelector('#fu-21-send');
  const clear = root.querySelector('#fu-21-clear');
  const status = root.querySelector('#fu-21-status');
  const OK = ['zip', 'pdf'];
  let picked = null, timer = null;

  const check = (input, file) => {
    const ext = (file.name.split('.').pop() || '').toLowerCase();
    const bad = !OK.includes(ext);
    input.classList.toggle('is-invalid', bad);              // Bootstrap's validation contract
    input.setAttribute('aria-invalid', String(bad));
    return !bad;
  };

  native.addEventListener('change', () => {
    const f = native.files[0];
    if (!f) return;
    if (!check(native, f)) { picked = null; send.disabled = true; status.textContent = ''; return; }
    picked = f; send.disabled = false;
    status.textContent = f.name + ' selected';
  });

  hidden.addEventListener('change', () => {
    const f = hidden.files[0];
    if (!f) return;
    chosen.textContent = f.name;
    picked = f; send.disabled = false;
    status.textContent = f.name + ' selected';
  });

  send.addEventListener('click', () => {                     // simulated upload
    if (!picked) return;
    let p = 0;
    track.hidden = false; send.disabled = true;
    status.textContent = 'Uploading ' + picked.name + '…';
    clearInterval(timer);
    timer = setInterval(() => {
      p = Math.min(100, p + 4 + Math.random() * 6);
      bar.style.inlineSize = p + '%';
      bar.textContent = Math.round(p) + '%';
      bar.setAttribute('aria-valuenow', Math.round(p));
      if (p >= 100) { clearInterval(timer); status.textContent = picked.name + ' uploaded successfully'; }
    }, 150);
  });

  clear.addEventListener('click', () => {
    clearInterval(timer);
    native.value = ''; hidden.value = '';
    native.classList.remove('is-invalid'); native.setAttribute('aria-invalid', 'false');
    chosen.textContent = 'No file chosen';
    bar.style.inlineSize = '0%'; bar.textContent = '0%'; bar.setAttribute('aria-valuenow', 0);
    track.hidden = true; picked = null; send.disabled = true;
    status.textContent = 'Cleared';
    native.focus();
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-21');
  const btn = root && root.querySelector('.fu-21__theme');
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
