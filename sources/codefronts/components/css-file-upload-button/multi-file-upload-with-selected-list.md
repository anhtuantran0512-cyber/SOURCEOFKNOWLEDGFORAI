---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/multi-file-upload-with-selected-list/"
title: "Multi-File Upload with Selected List"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "A real multi-file queue, including the part almost every tutorial skips: removing a single file."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-File Upload with Selected List
Source: https://codefronts.com/components/css-file-upload-button/multi-file-upload-with-selected-list/

A real multi-file queue, including the part almost every tutorial skips: removing a single file. A FileList is read-only, so the only supported way to drop one entry is to rebuild the list through a DataTransfer object and assign it back to input.files. Rows are cloned from a <template>, the running total is formatted with Intl.NumberFormat, and the whole list is a real <ul> so screen readers announce "list, 3 items".
## HTML
```html
<div class="fu-04">
  <button class="fu-04__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-04__panel" aria-labelledby="fu-04-h">
    <header class="fu-04__head">
      <div>
        <h2 class="fu-04__h" id="fu-04-h">Attachments</h2>
        <p class="fu-04__sub" id="fu-04-hint">Up to 8 files <span aria-hidden="true">·</span> 50 MB total</p>
      </div>
      <span class="fu-04__count" id="fu-04-count">0</span>
    </header>

    <div class="fu-04__pick">
      <input class="fu-04__input" id="fu-04-file" type="file" multiple accept=".pdf,.png,.jpg,.jpeg,.zip,.csv" aria-describedby="fu-04-hint">
      <label class="fu-04__label" for="fu-04-file">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 5.5v13M5.5 12h13" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        Add files
      </label>
    </div>

    <ul class="fu-04__list" id="fu-04-list"></ul>
    <p class="fu-04__empty">Nothing attached yet</p>

    <footer class="fu-04__foot">
      <span class="fu-04__total" id="fu-04-total">0 B of 50 MB</span>
      <button class="fu-04__send" id="fu-04-send" type="button" disabled>Upload</button>
    </footer>
    <p class="fu-04__status" id="fu-04-status" role="status" aria-live="polite"></p>
  </section>

  <template id="fu-04-row">
    <li class="fu-04__item">
      <span class="fu-04__chip" data-ext aria-hidden="true"></span>
      <span class="fu-04__meta">
        <span class="fu-04__name" data-name></span>
        <span class="fu-04__size" data-size></span>
      </span>
      <button class="fu-04__rm" type="button" data-rm>
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 6.5l11 11m0-11-11 11" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        <span class="fu-04__vh" data-rmlabel>Remove file</span>
      </button>
    </li>
  </template>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-04 {
  --bg: #0a0b10;
  --surface: #12141c;
  --raise: #181b25;
  --ink: #f0f2f7;
  --muted: #8b93a5;
  --line: #242938;
  --acc: #5ce1b9;
  --acc-ink: #04150f;
  --danger: #ff6b6b;
  --rows: 14rem;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(80% 50% at 15% 0%, color-mix(in oklab,var(--acc) 12%,transparent), transparent 60%), radial-gradient(70% 50% at 100% 100%, color-mix(in oklab,#6c8cff 14%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-04,
.fu-04 *,
.fu-04 *::before,
.fu-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-04 {
    --acc: oklch(84% .13 168);
  }
}

.fu-04__panel {
  inline-size: min(30rem,100%);
  display: grid;
  gap: 1rem;
  padding: clamp(1.1rem,3.5vw,1.5rem);
  background: color-mix(in oklab,var(--surface) 88%,transparent);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 80px -50px #000;
}

.fu-04__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.fu-04__h {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.fu-04__sub {
  margin: .25rem 0 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-04__count {
  display: grid;
  place-items: center;
  min-inline-size: 2rem;
  block-size: 2rem;
  padding-inline: .5rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--acc) 18%,transparent);
  border: 1px solid color-mix(in oklab,var(--acc) 35%,transparent);
  font-family: var(--mono);
  font-size: .8125rem;
  font-variant-numeric: tabular-nums;
  color: var(--acc);
}

.fu-04__input {
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

.fu-04__label {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  cursor: pointer;
  user-select: none;
  min-block-size: 3rem;
  border-radius: .9rem;
  border: 1px dashed color-mix(in oklab,var(--acc) 45%,var(--line));
  background: color-mix(in oklab,var(--acc) 7%,transparent);
  color: var(--acc);
  font-size: .9375rem;
  font-weight: 600;
  transition: background .25s ease, border-color .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.fu-04__label svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fu-04__label:hover {
  background: color-mix(in oklab,var(--acc) 14%,transparent);
  border-style: solid;
  transform: translateY(-1px);
}

.fu-04__input:focus-visible + .fu-04__label {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-04__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .5rem;
  max-block-size: var(--rows);
  overflow-y: auto;
  scrollbar-width: thin;
}

.fu-04__list:empty {
  display: none;
}

.fu-04__empty {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
  text-align: center;
  padding-block: .5rem;
}

.fu-04__panel:has(.fu-04__item) .fu-04__empty {
  display: none;
}

.fu-04__item {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: .75rem;
  padding: .55rem .6rem;
  border-radius: .85rem;
  background: var(--raise);
  border: 1px solid var(--line);
  transition: opacity .3s ease, transform .3s cubic-bezier(.16,1,.3,1), border-color .2s ease;
}

.fu-04__item:hover {
  border-color: color-mix(in oklab,var(--acc) 30%,var(--line));
}

@starting-style {
  .fu-04__item {
    opacity: 0;
    transform: translateY(-6px);
  }
}

.fu-04__chip {
  display: grid;
  place-items: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: .6rem;
  flex: none;
  background: color-mix(in oklab,var(--acc) 12%,transparent);
  color: var(--acc);
  font-family: var(--mono);
  font-size: .5625rem;
  letter-spacing: .06em;
}

.fu-04__meta {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.fu-04__name {
  font-size: .875rem;
  font-weight: 600;
  letter-spacing: -.01em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-04__size {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-04__rm {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  flex: none;
  cursor: pointer;
  border: 0;
  border-radius: .6rem;
  background: transparent;
  color: var(--muted);
  transition: background .2s ease, color .2s ease;
}

.fu-04__rm svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.fu-04__rm:hover {
  background: color-mix(in oklab,var(--danger) 18%,transparent);
  color: var(--danger);
}

.fu-04__rm:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-04__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-block-start: .15rem;
}

.fu-04__total {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-04__send {
  min-block-size: 2.75rem;
  padding: .6rem 1.3rem;
  border: 0;
  border-radius: .8rem;
  cursor: pointer;
  background: var(--acc);
  color: var(--acc-ink);
  font-family: var(--sans);
  font-size: .9375rem;
  font-weight: 700;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1), opacity .2s ease;
}

.fu-04__send:hover:not(:disabled) {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-04__send:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.fu-04__send:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-04__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-04__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-color-scheme: light) {
  .fu-04:not([data-theme="dark"]) {
    --bg: #eef1f6;
    --surface: #ffffff;
    --raise: #f6f8fb;
    --ink: #0d1018;
    --muted: #5d6678;
    --line: #e1e6ee;
    --acc: #0f8f6c;
    --acc-ink: #ffffff;
  }
}

.fu-04[data-theme="light"] {
  --bg: #eef1f6;
  --surface: #ffffff;
  --raise: #f6f8fb;
  --ink: #0d1018;
  --muted: #5d6678;
  --line: #e1e6ee;
  --acc: #0f8f6c;
  --acc-ink: #ffffff;
}

@media (prefers-reduced-motion: reduce) {
  .fu-04 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-04__panel,
    .fu-04__item,
    .fu-04__label {
    border: 1px solid CanvasText;
  }

  .fu-04__send {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-04 {
  position: relative;
}

.fu-04__theme {
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

.fu-04__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-04__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-04__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-04__sun {
  display: none;
}

.fu-04__theme[aria-pressed="true"] .fu-04__sun {
  display: block;
}

.fu-04__theme[aria-pressed="true"] .fu-04__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-04__theme {
    transition: none;
  }

  .fu-04__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-04__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-04');
  if (!root) return;
  const input = root.querySelector('#fu-04-file');
  const list = root.querySelector('#fu-04-list');
  const tpl = root.querySelector('#fu-04-row');
  const countEl = root.querySelector('#fu-04-count');
  const totalEl = root.querySelector('#fu-04-total');
  const send = root.querySelector('#fu-04-send');
  const status = root.querySelector('#fu-04-status');
  const LIMIT = 8, picked = [];

  const fmt = (n) => {
    const u = ['B','KB','MB','GB']; let i = 0;
    while (n >= 1024 && i < u.length - 1) { n /= 1024; i++; }
    return new Intl.NumberFormat(undefined, { maximumFractionDigits: n < 10 && i ? 1 : 0 }).format(n) + ' ' + u[i];
  };
  const sync = () => { const dt = new DataTransfer(); picked.forEach(f => dt.items.add(f)); input.files = dt.files; };

  function render() {
    list.replaceChildren(...picked.map((f, i) => {
      const row = tpl.content.firstElementChild.cloneNode(true);
      row.querySelector('[data-ext]').textContent = (f.name.split('.').pop() || '?').slice(0, 4).toUpperCase();
      row.querySelector('[data-name]').textContent = f.name;
      row.querySelector('[data-size]').textContent = fmt(f.size);
      row.querySelector('[data-rmlabel]').textContent = 'Remove ' + f.name;
      row.querySelector('[data-rm]').dataset.rm = i;
      return row;
    }));
    countEl.textContent = picked.length;
    totalEl.textContent = fmt(picked.reduce((s, f) => s + f.size, 0)) + ' of 50 MB';
    send.disabled = !picked.length;
  }

  input.addEventListener('change', () => {
    for (const f of input.files) {
      if (picked.length >= LIMIT) break;
      if (!picked.some(p => p.name === f.name && p.size === f.size && p.lastModified === f.lastModified)) picked.push(f);
    }
    sync(); render();
    status.textContent = picked.length + ' file' + (picked.length === 1 ? '' : 's') + ' attached';
  });

  list.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-rm]');
    if (!btn) return;
    const [gone] = picked.splice(Number(btn.dataset.rm), 1);
    if (!picked.length) input.value = '';
    sync(); render();
    status.textContent = gone.name + ' removed, ' + picked.length + ' remaining';
    (list.querySelector('[data-rm]') || root.querySelector('.fu-04__label')).focus();
  });

  send.addEventListener('click', () => {           // simulated — nothing leaves the page
    send.disabled = true; status.textContent = 'Uploading ' + picked.length + ' files…';
    setTimeout(() => { status.textContent = 'All ' + picked.length + ' files uploaded'; send.disabled = false; }, 1600);
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-04');
  const btn = root && root.querySelector('.fu-04__theme');
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
