---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/upload-success-error-retry-states/"
title: "Upload Success Error Retry States"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "Five states — idle, uploading, success, error, retrying — and one attribute."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Upload Success Error Retry States
Source: https://codefronts.com/components/css-file-upload-button/upload-success-error-retry-states/

Five states — idle, uploading, success, error, retrying — and one attribute. Every visual difference between them is a CSS [data-state] selector, so the script's entire job is card.dataset.state = 'error'. That is the discipline that keeps upload UIs from rotting: no orphan classes, no impossible combinations like "success and error at once", and a state you can read straight out of the DOM in DevTools.
## HTML
```html
<div class="fu-16">
  <button class="fu-16__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-16__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-16__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-16__card" id="fu-16-card" data-state="idle" aria-labelledby="fu-16-h">
    <span class="fu-16__glyph" aria-hidden="true">
      <svg class="fu-16__g fu-16__g--up" viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 16V5.5m0 0L7.8 9.7M12 5.5l4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M4.5 15v3.2A2.3 2.3 0 0 0 6.8 20.5h10.4a2.3 2.3 0 0 0 2.3-2.3V15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <svg class="fu-16__g fu-16__g--spin" viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-dasharray="40 14"/></svg>
      <svg class="fu-16__g fu-16__g--ok" viewBox="0 0 24 24" fill="none" focusable="false"><path d="m5.5 12.4 4.3 4.3 8.7-9.4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <svg class="fu-16__g fu-16__g--bad" viewBox="0 0 24 24" fill="none" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    </span>

    <h2 class="fu-16__h" id="fu-16-h">
      <span class="fu-16__t fu-16__t--idle">Attach your portfolio</span>
      <span class="fu-16__t fu-16__t--uploading">Uploading…</span>
      <span class="fu-16__t fu-16__t--retrying">Retrying…</span>
      <span class="fu-16__t fu-16__t--success">Upload complete</span>
      <span class="fu-16__t fu-16__t--error">Upload failed</span>
    </h2>

    <p class="fu-16__body">
      <span class="fu-16__t fu-16__t--idle">PDF up to 40 MB. One file per submission.</span>
      <span class="fu-16__t fu-16__t--uploading"><span id="fu-16-file">portfolio-2026.pdf</span> <span aria-hidden="true">·</span> <span id="fu-16-pct">0%</span></span>
      <span class="fu-16__t fu-16__t--retrying">Attempt <span id="fu-16-try">2</span> of 3 <span aria-hidden="true">·</span> resuming</span>
      <span class="fu-16__t fu-16__t--success">Stored securely. You can close this tab.</span>
      <span class="fu-16__t fu-16__t--error">The connection dropped at 62%. Nothing was lost — retry resumes.</span>
    </p>

    <div class="fu-16__bar" id="fu-16-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Upload progress"><span id="fu-16-fill"></span></div>

    <div class="fu-16__actions">
      <input class="fu-16__input" id="fu-16-input" type="file" accept="application/pdf">
      <label class="fu-16__pick" for="fu-16-input">Choose file</label>
      <button class="fu-16__act" id="fu-16-act" type="button">Start upload</button>
      <button class="fu-16__ghost" id="fu-16-reset" type="button">Start over</button>
    </div>

    <p class="fu-16__status" id="fu-16-status" role="status" aria-live="polite"></p>
    <p class="fu-16__alert" id="fu-16-alert" role="alert"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-16 {
  --bg: #0a0b0f;
  --surface: #12141b;
  --ink: #eff1f6;
  --muted: #858da0;
  --line: #232838;
  --acc: #7c8cff;
  --ok: #31d68f;
  --danger: #ff5f6d;
  --state: var(--acc);
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(65% 45% at 50% 0%, color-mix(in oklab,var(--state) 16%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
  transition: background .5s ease;
}

.fu-16,
.fu-16 *,
.fu-16 *::before,
.fu-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-16 {
    --acc: oklch(68% .17 275);
    --ok: oklch(78% .17 158);
    --danger: oklch(68% .2 18);
  }
}

.fu-16__card {
  inline-size: min(27rem,100%);
  display: grid;
  justify-items: center;
  gap: .75rem;
  text-align: center;
  padding: clamp(1.5rem,5vw,2.25rem);
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid color-mix(in oklab,var(--state) 30%,var(--line));
  box-shadow: 0 40px 90px -60px #000, 0 0 0 6px color-mix(in oklab,var(--state) 6%,transparent);
  transition: border-color .4s ease, box-shadow .4s ease;
}

.fu-16__card[data-state="success"] {
  --state: var(--ok);
}

.fu-16__card[data-state="error"] {
  --state: var(--danger);
}

.fu-16__glyph {
  display: grid;
  place-items: center;
  inline-size: 3.75rem;
  block-size: 3.75rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--state) 16%,transparent);
  color: var(--state);
  transition: background .35s ease, color .35s ease;
}

.fu-16__g {
  grid-area: 1/1;
  inline-size: 1.6rem;
  block-size: 1.6rem;
  display: none;
}

.fu-16__card[data-state="idle"] .fu-16__g--up {
  display: block;
}

.fu-16__card[data-state="uploading"] .fu-16__g--spin,
.fu-16__card[data-state="retrying"] .fu-16__g--spin {
  display: block;
  animation: fu-16-spin 1s linear infinite;
}

.fu-16__card[data-state="success"] .fu-16__g--ok {
  display: block;
  animation: fu-16-pop .5s cubic-bezier(.16,1,.3,1);
}

.fu-16__card[data-state="error"] .fu-16__g--bad {
  display: block;
  animation: fu-16-shake .4s ease;
}

@keyframes fu-16-spin {
  to {
    rotate: 360deg;
  }
}

@keyframes fu-16-pop {
  from {
    scale: .4;
    opacity: 0;
  }
}

@keyframes fu-16-shake {
  25% {
    translate: -4px 0;
  }

  75% {
    translate: 4px 0;
  }
}

.fu-16__h {
  margin: 0;
  font-size: clamp(1.2rem,3vw,1.45rem);
  font-weight: 700;
  letter-spacing: -.03em;
  display: grid;
}

.fu-16__body {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  line-height: 1.6;
  color: var(--muted);
  display: grid;
  min-block-size: 2.4rem;
  text-wrap: pretty;
}

.fu-16__t {
  display: none;
  grid-area: 1/1;
}

.fu-16__card[data-state="idle"] .fu-16__t--idle,
.fu-16__card[data-state="uploading"] .fu-16__t--uploading,
.fu-16__card[data-state="retrying"] .fu-16__t--retrying,
.fu-16__card[data-state="success"] .fu-16__t--success,
.fu-16__card[data-state="error"] .fu-16__t--error {
  display: block;
  transition: opacity .3s ease, transform .3s cubic-bezier(.16,1,.3,1);
}

@starting-style {
  .fu-16__t {
    opacity: 0;
    transform: translateY(6px);
  }
}

.fu-16__bar {
  inline-size: 100%;
  block-size: .4rem;
  border-radius: 999px;
  overflow: hidden;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  opacity: 0;
  transition: opacity .3s ease;
}

.fu-16__bar span {
  display: block;
  block-size: 100%;
  inline-size: 0%;
  border-radius: 999px;
  background: var(--state);
  transition: inline-size .25s linear, background .3s ease;
}

.fu-16__card[data-state="uploading"] .fu-16__bar,
.fu-16__card[data-state="retrying"] .fu-16__bar,
.fu-16__card[data-state="error"] .fu-16__bar {
  opacity: 1;
}

.fu-16__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  inline-size: 100%;
}

.fu-16__input {
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

.fu-16__pick,
.fu-16__act,
.fu-16__ghost {
  min-block-size: 2.85rem;
  padding: .65rem 1.2rem;
  border-radius: .8rem;
  cursor: pointer;
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 600;
  display: none;
  align-items: center;
  justify-content: center;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1), background .25s ease, border-color .2s ease;
}

.fu-16__pick {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--ink);
}

.fu-16__pick:hover {
  border-color: var(--state);
}

.fu-16__input:focus-visible + .fu-16__pick {
  outline: 2px solid var(--state);
  outline-offset: 3px;
}

.fu-16__act {
  border: 0;
  background: var(--state);
  color: #0a0b12;
}

.fu-16__act:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-16__ghost {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--muted);
}

.fu-16__ghost:hover {
  color: var(--ink);
  border-color: var(--muted);
}

.fu-16__act:focus-visible,
.fu-16__ghost:focus-visible {
  outline: 2px solid var(--state);
  outline-offset: 3px;
}

.fu-16__card[data-state="idle"] .fu-16__pick,
.fu-16__card[data-state="idle"] .fu-16__act,
.fu-16__card[data-state="error"] .fu-16__act,
.fu-16__card[data-state="error"] .fu-16__ghost,
.fu-16__card[data-state="success"] .fu-16__ghost {
  display: inline-flex;
}

.fu-16__status,
.fu-16__alert {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--muted);
}

.fu-16__alert {
  color: var(--danger);
}

@media (prefers-color-scheme: light) {
  .fu-16:not([data-theme="dark"]) {
    --bg: #f2f3f7;
    --surface: #ffffff;
    --ink: #0b0d14;
    --muted: #5b6376;
    --line: #e3e6ee;
    --acc: #4353ff;
    --ok: #0f9d63;
    --danger: #dc2440;
  }

  .fu-16:not([data-theme="dark"]) .fu-16__act {
    color: #fff;
  }
}

.fu-16[data-theme="light"] {
  --bg: #f2f3f7;
  --surface: #ffffff;
  --ink: #0b0d14;
  --muted: #5b6376;
  --line: #e3e6ee;
  --acc: #4353ff;
  --ok: #0f9d63;
  --danger: #dc2440;
}

.fu-16[data-theme="light"] .fu-16__act {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .fu-16 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-16__card {
    border: 1px solid CanvasText;
  }

  .fu-16__glyph {
    background: Canvas;
    border: 1px solid CanvasText;
  }

  .fu-16__act {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-16 {
  position: relative;
}

.fu-16__theme {
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

.fu-16__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-16__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-16__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-16__sun {
  display: none;
}

.fu-16__theme[aria-pressed="true"] .fu-16__sun {
  display: block;
}

.fu-16__theme[aria-pressed="true"] .fu-16__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-16__theme {
    transition: none;
  }

  .fu-16__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-16__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-16');
  if (!root) return;
  const card = root.querySelector('#fu-16-card');
  const fill = root.querySelector('#fu-16-fill');
  const bar = root.querySelector('#fu-16-bar');
  const pct = root.querySelector('#fu-16-pct');
  const act = root.querySelector('#fu-16-act');
  const reset = root.querySelector('#fu-16-reset');
  const input = root.querySelector('#fu-16-input');
  const nameEl = root.querySelector('#fu-16-file');
  const tryEl = root.querySelector('#fu-16-try');
  const status = root.querySelector('#fu-16-status');
  const alert = root.querySelector('#fu-16-alert');
  const SAY = { idle: 'Ready to upload', uploading: 'Upload in progress', retrying: 'Retrying upload', success: 'Upload complete' };
  let timer = null, attempt = 1, p = 0;

  const setP = (v) => {
    p = v; fill.style.inlineSize = v + '%';
    bar.setAttribute('aria-valuenow', Math.round(v));
    pct.textContent = Math.round(v) + '%';
  };

  const go = (state) => {                       // one attribute drives every visual
    card.dataset.state = state;
    if (state === 'error') { alert.textContent = 'Upload failed at ' + Math.round(p) + '%. Retry to resume.'; status.textContent = ''; }
    else { alert.textContent = ''; status.textContent = SAY[state] || ''; }
    act.textContent = state === 'error' ? 'Retry upload' : 'Start upload';
  };

  const run = (from = 0, failAt = null) => {
    setP(from);
    clearInterval(timer);
    timer = setInterval(() => {
      setP(Math.min(100, p + 2 + Math.random() * 3));
      if (failAt !== null && p >= failAt) { clearInterval(timer); go('error'); return; }
      if (p >= 100) { clearInterval(timer); go('success'); }
    }, 120);
  };

  act.addEventListener('click', () => {
    if (card.dataset.state === 'error') {
      attempt++; tryEl.textContent = attempt;
      go('retrying'); run(p, null);              // resume from where it broke
    } else {
      attempt = 1; go('uploading'); run(0, 62);  // first attempt fails at 62% on purpose
    }
  });

  reset.addEventListener('click', () => {
    clearInterval(timer); attempt = 1; setP(0);
    input.value = ''; go('idle'); input.focus();
  });

  input.addEventListener('change', () => {
    const f = input.files && input.files[0];
    if (!f) return;
    nameEl.textContent = f.name;
    status.textContent = f.name + ' selected';
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-16');
  const btn = root && root.querySelector('.fu-16__theme');
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
