---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/full-page-drag-and-drop-overlay/"
title: "Full-Page Drag and Drop Overlay"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "The pattern every modern file app uses: you can drop anywhere."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Page Drag and Drop Overlay
Source: https://codefronts.com/components/css-file-upload-button/full-page-drag-and-drop-overlay/

The pattern every modern file app uses: you can drop anywhere. Listeners live on window, so the overlay appears the instant a file crosses the viewport edge and disappears when the drag leaves — detected reliably with a depth counter rather than the notoriously unreliable relatedTarget. The overlay is a <dialog>-free layer with backdrop-filter, inert content behind it, and both hidden and display:none so no stylesheet can accidentally reveal it.
## HTML
```html
<div class="fu-09">
  <button class="fu-09__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <div class="fu-09__shell" id="fu-09-shell">
    <header class="fu-09__bar">
      <span class="fu-09__brand">Depot</span>
      <span class="fu-09__crumb">Workspace <span aria-hidden="true">/</span> Q3 assets</span>
      <label class="fu-09__pick" for="fu-09-file">Upload</label>
      <input class="fu-09__input" id="fu-09-file" type="file" multiple>
    </header>

    <table class="fu-09__table">
      <caption class="fu-09__vh">Files in Q3 assets</caption>
      <thead>
        <tr><th scope="col">Name</th><th scope="col">Size</th><th scope="col">Modified</th></tr>
      </thead>
      <tbody id="fu-09-body">
        <tr><td><span class="fu-09__dot" aria-hidden="true"></span>brand-guidelines-v9.pdf</td><td>4.1 MB</td><td><time datetime="2026-08-04">4 Aug</time></td></tr>
        <tr><td><span class="fu-09__dot" aria-hidden="true"></span>launch-keynote.key</td><td>62.8 MB</td><td><time datetime="2026-08-02">2 Aug</time></td></tr>
        <tr><td><span class="fu-09__dot" aria-hidden="true"></span>press-photos.zip</td><td>211 MB</td><td><time datetime="2026-07-28">28 Jul</time></td></tr>
      </tbody>
    </table>
  </div>

  <div class="fu-09__overlay" id="fu-09-overlay" role="region" aria-label="Drop files to upload" hidden>
    <div class="fu-09__well">
      <span class="fu-09__ring" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 16.5V5.5m0 0L7.8 9.7M12 5.5l4.2 4.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path d="M4.5 15v3.2A2.3 2.3 0 0 0 6.8 20.5h10.4a2.3 2.3 0 0 0 2.3-2.3V15" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </span>
      <p class="fu-09__ot">Drop anywhere to upload</p>
      <p class="fu-09__os">Files land in Workspace / Q3 assets</p>
    </div>
  </div>

  <p class="fu-09__status" id="fu-09-status" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-09 {
  --bg: #0b0d13;
  --surface: #12151d;
  --raise: #171b25;
  --ink: #eef1f7;
  --muted: #8790a3;
  --line: #242a38;
  --acc: #4de3ff;
  --acc2: #a78bfa;
  --blur: 16px;
  --sans: "Outfit",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(80% 50% at 20% 0%, color-mix(in oklab,var(--acc2) 14%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-09,
.fu-09 *,
.fu-09 *::before,
.fu-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-09 {
    --acc: oklch(85% .13 205);
    --acc2: oklch(72% .17 295);
  }
}

.fu-09__shell {
  inline-size: min(40rem,100%);
  border-radius: 1.4rem;
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 40px 90px -60px #000;
}

.fu-09__bar {
  display: flex;
  align-items: center;
  gap: .85rem;
  padding: .85rem 1rem;
  border-block-end: 1px solid var(--line);
  background: color-mix(in oklab,var(--raise) 70%,transparent);
}

.fu-09__brand {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.fu-09__crumb {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-09__crumb span {
  margin-inline: .3rem;
  opacity: .5;
}

.fu-09__input {
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

.fu-09__pick {
  margin-inline-start: auto;
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  min-block-size: 2.5rem;
  padding: .5rem 1rem;
  border-radius: .7rem;
  background: var(--acc);
  color: #04141a;
  font-size: .875rem;
  font-weight: 600;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1);
}

.fu-09__pick:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-09__input:focus-visible + .fu-09__pick,
.fu-09__input:focus-visible ~ .fu-09__pick {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-09__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: .875rem;
}

.fu-09__table th {
  text-align: start;
  padding: .6rem 1rem;
  font-family: var(--mono);
  font-size: .5625rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 500;
  border-block-end: 1px solid var(--line);
}

.fu-09__table td {
  padding: .75rem 1rem;
  border-block-end: 1px solid color-mix(in oklab,var(--line) 60%,transparent);
  color: var(--ink);
}

.fu-09__table td:nth-child(n+2) {
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.fu-09__table tbody tr {
  transition: background .2s ease;
}

.fu-09__table tbody tr:hover {
  background: var(--raise);
}

.fu-09__table tbody tr:first-child td {
  color: var(--ink);
}

.fu-09__dot {
  display: inline-block;
  inline-size: .5rem;
  block-size: .5rem;
  margin-inline-end: .6rem;
  border-radius: 999px;
  background: var(--acc2);
}

.fu-09__table tbody tr.is-new td:first-child {
  font-weight: 600;
}

.fu-09__table tbody tr.is-new .fu-09__dot {
  background: var(--acc);
}

.fu-09__overlay {
  position: absolute;
  inset: 0;
  z-index: 5;
  display: grid;
  place-items: center;
  padding: 1.5rem;
  background: color-mix(in oklab,var(--bg) 70%,transparent);
  backdrop-filter: blur(var(--blur)) saturate(1.2);
  -webkit-backdrop-filter: blur(var(--blur)) saturate(1.2);
  transition: opacity .3s ease, display .3s allow-discrete;
}

.fu-09__overlay[hidden] {
  display: none;
}

@starting-style {
  .fu-09__overlay {
    opacity: 0;
  }

  .fu-09__well {
    transform: scale(.94);
  }
}

.fu-09__well {
  display: grid;
  justify-items: center;
  gap: .55rem;
  text-align: center;
  inline-size: min(28rem,100%);
  padding: clamp(1.75rem,6vw,3rem);
  border-radius: 1.5rem;
  border: 2px dashed color-mix(in oklab,var(--acc) 55%,transparent);
  background: color-mix(in oklab,var(--acc) 8%,transparent);
  transition: transform .35s cubic-bezier(.16,1,.3,1);
}

.fu-09__ring {
  display: grid;
  place-items: center;
  inline-size: 3.5rem;
  block-size: 3.5rem;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--acc) 45%,transparent);
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 14%,transparent);
  animation: fu-09-pulse 2s ease-in-out infinite;
}

.fu-09__ring svg {
  inline-size: 1.6rem;
  block-size: 1.6rem;
}

@keyframes fu-09-pulse {
  50% {
    transform: translateY(-4px);
    box-shadow: 0 0 0 10px color-mix(in oklab,var(--acc) 10%,transparent);
  }
}

.fu-09__ot {
  margin: .3rem 0 0;
  font-size: clamp(1.1rem,2.6vw,1.35rem);
  font-weight: 700;
  letter-spacing: -.025em;
}

.fu-09__os {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-09__status {
  position: absolute;
  inset-block-end: 1rem;
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-09__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-color-scheme: light) {
  .fu-09:not([data-theme="dark"]) {
    --bg: #eff2f7;
    --surface: #ffffff;
    --raise: #f6f8fb;
    --ink: #0c0f16;
    --muted: #5b6478;
    --line: #e2e6ee;
    --acc: #0aa2c0;
    --acc2: #7c3aed;
  }

  .fu-09:not([data-theme="dark"]) .fu-09__pick {
    color: #fff;
  }
}

.fu-09[data-theme="light"] {
  --bg: #eff2f7;
  --surface: #ffffff;
  --raise: #f6f8fb;
  --ink: #0c0f16;
  --muted: #5b6478;
  --line: #e2e6ee;
  --acc: #0aa2c0;
  --acc2: #7c3aed;
}

.fu-09[data-theme="light"] .fu-09__pick {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .fu-09 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-09__shell,
    .fu-09__well {
    border: 1px solid CanvasText;
  }

  .fu-09__overlay {
    background: Canvas;
  }

  .fu-09__pick {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-09 {
  position: relative;
}

.fu-09__theme {
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

.fu-09__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-09__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-09__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-09__sun {
  display: none;
}

.fu-09__theme[aria-pressed="true"] .fu-09__sun {
  display: block;
}

.fu-09__theme[aria-pressed="true"] .fu-09__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-09__theme {
    transition: none;
  }

  .fu-09__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-09__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-09');
  if (!root) return;
  const shell = root.querySelector('#fu-09-shell');
  const overlay = root.querySelector('#fu-09-overlay');
  const body = root.querySelector('#fu-09-body');
  const input = root.querySelector('#fu-09-file');
  const status = root.querySelector('#fu-09-status');
  let depth = 0;

  const open = () => { overlay.hidden = false; shell.inert = true; };
  const close = () => { overlay.hidden = true; shell.inert = false; };

  const fmt = (n) => {
    const u = ['B','KB','MB','GB']; let i = 0;
    while (n >= 1024 && i < u.length - 1) { n /= 1024; i++; }
    return new Intl.NumberFormat(undefined, { maximumFractionDigits: n < 10 && i ? 1 : 0 }).format(n) + ' ' + u[i];
  };

  const accept = (files) => {
    const list = [...files];
    if (!list.length) return;
    list.forEach(f => {
      const tr = document.createElement('tr');
      tr.className = 'is-new';
      tr.innerHTML = '<td><span class="fu-09__dot"></span></td><td></td><td>Just now</td>';
      tr.children[0].append(f.name);
      tr.children[1].textContent = fmt(f.size);
      body.prepend(tr);
    });
    status.textContent = list.length + ' file' + (list.length === 1 ? '' : 's') + ' added to Q3 assets';
  };

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(t =>
    window.addEventListener(t, e => e.preventDefault())
  );
  window.addEventListener('dragenter', () => { if (++depth === 1) open(); });
  window.addEventListener('dragleave', () => { if (--depth <= 0) { depth = 0; close(); } });
  window.addEventListener('drop', e => { depth = 0; close(); accept(e.dataTransfer.files); });
  window.addEventListener('dragend', () => { depth = 0; close(); });
  window.addEventListener('blur', () => { depth = 0; close(); });
  window.addEventListener('keydown', e => { if (e.key === 'Escape' && !overlay.hidden) { depth = 0; close(); } });

  input.addEventListener('change', () => { accept(input.files); input.value = ''; });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-09');
  const btn = root && root.querySelector('.fu-09__theme');
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
