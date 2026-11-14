---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/tailwind-file-upload-dropzone/"
title: "Tailwind File Upload Dropzone"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "A dropzone written the way you would write it in a Tailwind project — utility classes on every element, sr-only hiding the input, peer-focus-visible…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind File Upload Dropzone
Source: https://codefronts.com/components/css-file-upload-button/tailwind-file-upload-dropzone/

A dropzone written the way you would write it in a Tailwind project — utility classes on every element, sr-only hiding the input, peer-focus-visible projecting focus onto the label — but with no Tailwind runtime required. The same style block ships a scoped vanilla implementation of every utility used, so it renders identically in a plain HTML page and you can delete that block the moment you paste it into a real Tailwind build.
## HTML
```html
<div class="fu-20">
  <button class="fu-20__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-20__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-20__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="mx-auto w-full max-w-md grid gap-4 rounded-2xl border border-slate-200 bg-white p-6 shadow-lg" aria-labelledby="fu-20-h">
    <header class="flex items-center justify-between gap-4">
      <div>
        <h2 class="text-base font-semibold text-slate-900" id="fu-20-h">Upload assets</h2>
        <p class="text-xs text-slate-500">SVG, PNG or PDF · max 20 MB</p>
      </div>
      <span class="rounded-full bg-indigo-50 px-3 py-1 text-xs font-medium text-indigo-600" id="fu-20-count">0 files</span>
    </header>

    <div class="group grid gap-2 place-items-center rounded-xl border-2 border-dashed border-slate-200 bg-slate-50 py-10 text-center cursor-pointer transition" id="fu-20-zone" role="button" tabindex="0" aria-label="Drop files here or press Enter to browse">
      <span class="grid place-items-center size-10 rounded-full bg-indigo-600 text-white transition" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" class="size-5" focusable="false"><path d="M12 16V5.5m0 0L8 9.5M12 5.5l4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M4.5 15v3.2A2.3 2.3 0 0 0 6.8 20.5h10.4a2.3 2.3 0 0 0 2.3-2.3V15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </span>
      <p class="text-sm font-medium text-slate-900">Drag files here</p>
      <input id="fu-20-file" type="file" multiple class="sr-only peer" accept=".svg,.png,.pdf">
      <label for="fu-20-file" class="cursor-pointer rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white transition hover-indigo-500">Browse files</label>
    </div>

    <ul class="grid gap-2" id="fu-20-list"></ul>

    <button class="rounded-lg bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition" id="fu-20-go" type="button" disabled>Upload</button>
    <p class="text-xs text-slate-500" id="fu-20-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');
/* ── tokens (in a Tailwind v4 project these live in @theme) ── */

.fu-20 {
  --white: #ffffff;
  --slate-50: #f8fafc;
  --slate-100: #f1f5f9;
  --slate-200: #e2e8f0;
  --slate-500: #64748b;
  --slate-900: #0f172a;
  --indigo-50: #eef2ff;
  --indigo-500: #6366f1;
  --indigo-600: #4f46e5;
  --sans: "Inter Tight",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: var(--slate-100);
  font-family: var(--sans);
  color: var(--slate-900);
}

.fu-20,
.fu-20 *,
.fu-20 *::before,
.fu-20 *::after {
  box-sizing: border-box;
}
/* ══════════════════════════════════════════════════════════════════════
   VANILLA FALLBACK — scoped implementations of every Tailwind utility
   used above. DELETE THIS ENTIRE BLOCK inside a real Tailwind project.
   ══════════════════════════════════════════════════════════════════════ */

.fu-20 .sr-only {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  overflow: hidden;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
  opacity: 0;
}

.fu-20 .mx-auto {
  margin-inline: auto;
}

.fu-20 .w-full {
  inline-size: 100%;
}

.fu-20 .max-w-md {
  max-inline-size: 28rem;
}

.fu-20 .grid {
  display: grid;
}

.fu-20 .flex {
  display: flex;
}

.fu-20 .place-items-center {
  place-items: center;
}

.fu-20 .items-center {
  align-items: center;
}

.fu-20 .justify-between {
  justify-content: space-between;
}

.fu-20 .gap-2 {
  gap: .5rem;
}

.fu-20 .gap-4 {
  gap: 1rem;
}

.fu-20 .text-center {
  text-align: center;
}

.fu-20 .p-6 {
  padding: 1.5rem;
}

.fu-20 .py-10 {
  padding-block: 2.5rem;
}

.fu-20 .px-3 {
  padding-inline: .75rem;
}

.fu-20 .px-4 {
  padding-inline: 1rem;
}

.fu-20 .py-1 {
  padding-block: .25rem;
}

.fu-20 .py-2 {
  padding-block: .5rem;
}

.fu-20 .rounded-2xl {
  border-radius: 1rem;
}

.fu-20 .rounded-xl {
  border-radius: .75rem;
}

.fu-20 .rounded-lg {
  border-radius: .5rem;
}

.fu-20 .rounded-full {
  border-radius: 9999px;
}

.fu-20 .border {
  border: 1px solid var(--slate-200);
}

.fu-20 .border-2 {
  border: 2px solid var(--slate-200);
}

.fu-20 .border-dashed {
  border-style: dashed;
}

.fu-20 .border-slate-200 {
  border-color: var(--slate-200);
}

.fu-20 .bg-white {
  background: var(--white);
}

.fu-20 .bg-slate-50 {
  background: var(--slate-50);
}

.fu-20 .bg-slate-900 {
  background: var(--slate-900);
}

.fu-20 .bg-indigo-600 {
  background: var(--indigo-600);
}

.fu-20 .bg-indigo-50 {
  background: var(--indigo-50);
}

.fu-20 .text-white {
  color: #fff;
}

.fu-20 .text-slate-900 {
  color: var(--slate-900);
}

.fu-20 .text-slate-500 {
  color: var(--slate-500);
}

.fu-20 .text-indigo-600 {
  color: var(--indigo-600);
}

.fu-20 .text-xs {
  font-size: .75rem;
  line-height: 1.4;
}

.fu-20 .text-sm {
  font-size: .875rem;
  line-height: 1.45;
}

.fu-20 .text-base {
  font-size: 1rem;
  line-height: 1.4;
}

.fu-20 .font-medium {
  font-weight: 500;
}

.fu-20 .font-semibold {
  font-weight: 600;
}

.fu-20 .size-5 {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.fu-20 .size-10 {
  inline-size: 2.5rem;
  block-size: 2.5rem;
}

.fu-20 .shadow-lg {
  box-shadow: 0 10px 15px -3px rgb(15 23 42 / .08), 0 4px 6px -4px rgb(15 23 42 / .08);
}

.fu-20 .cursor-pointer {
  cursor: pointer;
}

.fu-20 .transition {
  transition: background .2s ease, border-color .2s ease, color .2s ease, transform .2s cubic-bezier(.16,1,.3,1), opacity .2s ease;
}

.fu-20 .fu-20 .min-w-0 {
  min-inline-size: 0;
}
/* truncate cannot shrink in a flex row without min-width:0 — flex items
   default to min-width:auto, so long filenames force the row open */

.fu-20 li {
  min-inline-size: 0;
}

.fu-20 li > .truncate {
  min-inline-size: 0;
}

.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-20 .hover-indigo-500:hover {
  background: var(--indigo-500);
}

.fu-20 .group:hover .size-10 {
  transform: translateY(-2px);
}

.fu-20 .peer:focus-visible + label {
  outline: 2px solid var(--indigo-600);
  outline-offset: 2px;
}
/* ═══════════════════ end of fallback block ═══════════════════ */

.fu-20 h2,
.fu-20 p {
  margin: 0;
}

.fu-20 button {
  font-family: inherit;
  border: 0;
}

.fu-20 label,
.fu-20 button,
.fu-20 [role="button"] {
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.fu-20 #fu-20-zone {
  min-block-size: auto;
  display: grid;
}

.fu-20 #fu-20-zone:hover {
  border-color: var(--indigo-500);
  background: var(--indigo-50);
}

.fu-20 #fu-20-zone:focus-visible {
  outline: 2px solid var(--indigo-600);
  outline-offset: 3px;
}

.fu-20 #fu-20-zone.is-over {
  border-color: var(--indigo-600);
  border-style: solid;
  background: var(--indigo-50);
  transform: scale(1.005);
}

.fu-20 #fu-20-go:disabled {
  opacity: .45;
  cursor: not-allowed;
}

.fu-20 #fu-20-go:hover:not(:disabled) {
  background: var(--indigo-600);
}

.fu-20 #fu-20-go:focus-visible,
.fu-20 #fu-20-zone label:focus-visible {
  outline: 2px solid var(--indigo-600);
  outline-offset: 3px;
}

.fu-20 #fu-20-list:empty {
  display: none;
}

.fu-20 #fu-20-list li {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .55rem .7rem;
  border-radius: .5rem;
  border: 1px solid var(--slate-200);
  background: var(--slate-50);
  font-size: .8125rem;
}

.fu-20 #fu-20-list li span:first-child {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-20 #fu-20-list li em {
  margin-inline-start: auto;
  font-style: normal;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--slate-500);
}

.fu-20 #fu-20-list button {
  inline-size: 2rem;
  min-block-size: 2rem;
  block-size: 2rem;
  border-radius: .4rem;
  background: transparent;
  color: var(--slate-500);
  cursor: pointer;
  font-size: 1rem;
  line-height: 1;
}

.fu-20 #fu-20-list button:hover {
  background: var(--slate-200);
  color: var(--slate-900);
}

.fu-20 #fu-20-list button:focus-visible {
  outline: 2px solid var(--indigo-600);
  outline-offset: 2px;
}
/* dark: variants, reproduced with the token block */

@media (prefers-color-scheme: dark) {
  .fu-20:not([data-theme="light"]) {
    --white: #0f1420;
    --slate-50: #141a28;
    --slate-100: #080b12;
    --slate-200: #242c3d;
    --slate-500: #94a3b8;
    --slate-900: #f1f5f9;
    --indigo-50: #1c2036;
    --indigo-500: #818cf8;
    --indigo-600: #6366f1;
  }

  .fu-20:not([data-theme="light"]) .bg-slate-900 {
    background: var(--indigo-600);
  }
}

.fu-20[data-theme="dark"] {
  --white: #0f1420;
  --slate-50: #141a28;
  --slate-100: #080b12;
  --slate-200: #242c3d;
  --slate-500: #94a3b8;
  --slate-900: #f1f5f9;
  --indigo-50: #1c2036;
  --indigo-500: #818cf8;
  --indigo-600: #6366f1;
}

.fu-20[data-theme="dark"] .bg-slate-900 {
  background: var(--indigo-600);
}

@media (prefers-reduced-motion: reduce) {
  .fu-20 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-20 .border,
    .fu-20 .border-2 {
    border-color: CanvasText;
  }

  .fu-20 .bg-indigo-600,
    .fu-20 .bg-slate-900 {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-20 {
  position: relative;
}

.fu-20__theme {
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

.fu-20__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-20__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-20__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-20__sun {
  display: none;
}

.fu-20__theme[aria-pressed="true"] .fu-20__sun {
  display: block;
}

.fu-20__theme[aria-pressed="true"] .fu-20__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-20__theme {
    transition: none;
  }

  .fu-20__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-20__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-20');
  if (!root) return;
  const zone = root.querySelector('#fu-20-zone');
  const input = root.querySelector('#fu-20-file');
  const list = root.querySelector('#fu-20-list');
  const count = root.querySelector('#fu-20-count');
  const go = root.querySelector('#fu-20-go');
  const status = root.querySelector('#fu-20-status');
  const files = [];
  let depth = 0;

  const kb = (n) => n < 1048576 ? Math.max(1, Math.round(n / 1024)) + ' KB' : (n / 1048576).toFixed(1) + ' MB';

  const render = () => {
    list.replaceChildren(...files.map((f, i) => {
      const li = document.createElement('li');
      li.innerHTML = '<span class="truncate min-w-0"></span><em></em><button type="button" aria-label="Remove file">×</button>';
      li.children[0].textContent = f.name;
      li.children[1].textContent = kb(f.size);
      li.children[2].dataset.i = i;
      li.children[2].setAttribute('aria-label', 'Remove ' + f.name);
      return li;
    }));
    count.textContent = files.length + (files.length === 1 ? ' file' : ' files');
    go.disabled = !files.length;
  };

  const add = (fl) => {
    for (const f of fl) if (!files.some(x => x.name === f.name && x.size === f.size)) files.push(f);
    render();
    status.textContent = files.length + ' file(s) ready to upload';
  };

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(t =>
    zone.addEventListener(t, e => { e.preventDefault(); e.stopPropagation(); })
  );
  zone.addEventListener('dragenter', () => { depth++; zone.classList.add('is-over'); });
  zone.addEventListener('dragleave', () => { if (--depth <= 0) { depth = 0; zone.classList.remove('is-over'); } });
  zone.addEventListener('drop', e => { depth = 0; zone.classList.remove('is-over'); add(e.dataTransfer.files); });
  zone.addEventListener('click', e => { if (!e.target.closest('label')) input.click(); });
  zone.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); } });
  input.addEventListener('change', () => { add(input.files); input.value = ''; });

  list.addEventListener('click', e => {
    const btn = e.target.closest('button[data-i]');
    if (!btn) return;
    const [gone] = files.splice(Number(btn.dataset.i), 1);
    render();
    status.textContent = gone.name + ' removed';
  });

  go.addEventListener('click', () => {         // simulated
    go.disabled = true; status.textContent = 'Uploading…';
    setTimeout(() => { status.textContent = files.length + ' file(s) uploaded'; go.disabled = false; }, 1500);
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-20');
  const btn = root && root.querySelector('.fu-20__theme');
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
