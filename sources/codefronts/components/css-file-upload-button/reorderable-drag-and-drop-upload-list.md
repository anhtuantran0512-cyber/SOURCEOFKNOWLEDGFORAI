---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/reorderable-drag-and-drop-upload-list/"
title: "Reorderable Drag and Drop Upload List"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "When upload order is the output — carousels, PDF page order, photo albums — the queue has to be sortable."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reorderable Drag and Drop Upload List
Source: https://codefronts.com/components/css-file-upload-button/reorderable-drag-and-drop-upload-list/

When upload order is the output — carousels, PDF page order, photo albums — the queue has to be sortable. This list is reorderable by pointer drag and by keyboard: with a row focused, Alt + ↑/↓ moves it and the new position is announced. Position numbers come from a CSS counter, so nothing has to be renumbered in JavaScript.
## HTML
```html
<div class="fu-08">
  <button class="fu-08__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-08__card" aria-labelledby="fu-08-h">
    <header class="fu-08__head">
      <h2 class="fu-08__h" id="fu-08-h">Page order</h2>
      <p class="fu-08__sub">Drag rows, or focus one and press Alt + arrow keys</p>
    </header>

    <ol class="fu-08__list" id="fu-08-list">
      <li class="fu-08__row" draggable="true" tabindex="0" data-name="01-cover-spread.pdf">
        <span class="fu-08__grip" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></span>
        <span class="fu-08__pos" aria-hidden="true"></span>
        <span class="fu-08__meta"><span class="fu-08__name">01-cover-spread.pdf</span><span class="fu-08__size">2.4 MB</span></span>
        <span class="fu-08__kind">PDF</span>
      </li>
      <li class="fu-08__row" draggable="true" tabindex="0" data-name="editorial-notes-v3.docx">
        <span class="fu-08__grip" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></span>
        <span class="fu-08__pos" aria-hidden="true"></span>
        <span class="fu-08__meta"><span class="fu-08__name">editorial-notes-v3.docx</span><span class="fu-08__size">88 KB</span></span>
        <span class="fu-08__kind">DOCX</span>
      </li>
      <li class="fu-08__row" draggable="true" tabindex="0" data-name="spread-04-final.tiff">
        <span class="fu-08__grip" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></span>
        <span class="fu-08__pos" aria-hidden="true"></span>
        <span class="fu-08__meta"><span class="fu-08__name">spread-04-final.tiff</span><span class="fu-08__size">18.7 MB</span></span>
        <span class="fu-08__kind">TIFF</span>
      </li>
      <li class="fu-08__row" draggable="true" tabindex="0" data-name="colophon.indd">
        <span class="fu-08__grip" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></span>
        <span class="fu-08__pos" aria-hidden="true"></span>
        <span class="fu-08__meta"><span class="fu-08__name">colophon.indd</span><span class="fu-08__size">640 KB</span></span>
        <span class="fu-08__kind">INDD</span>
      </li>
    </ol>

    <div class="fu-08__foot">
      <input class="fu-08__input" id="fu-08-file" type="file" multiple>
      <label class="fu-08__add" for="fu-08-file">Add to queue</label>
      <button class="fu-08__go" id="fu-08-go" type="button">Upload in this order</button>
    </div>
    <p class="fu-08__status" id="fu-08-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-08 {
  --bg: #f5f6f8;
  --surface: #ffffff;
  --raise: #fafbfc;
  --ink: #101319;
  --muted: #5d6575;
  --line: #e4e7ed;
  --acc: #3b49df;
  --acc-soft: #eef0ff;
  --grip: #c3c8d4;
  --sans: "Figtree",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
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

.fu-08,
.fu-08 *,
.fu-08 *::before,
.fu-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-08 {
    --acc: oklch(48% .22 268);
    --acc-soft: color-mix(in oklab,var(--acc) 9%,white);
  }
}

.fu-08__card {
  inline-size: min(34rem,100%);
  display: grid;
  gap: 1rem;
  padding: clamp(1.15rem,3.5vw,1.6rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.35rem;
  box-shadow: 0 24px 60px -45px rgba(16,19,25,.5);
}

.fu-08__head {
  display: grid;
  gap: .25rem;
}

.fu-08__h {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -.025em;
}

.fu-08__sub {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-08__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .45rem;
  counter-reset: fu08 0;
}

.fu-08__row {
  counter-increment: fu08;
  display: grid;
  grid-template-columns: auto auto minmax(0,1fr) auto;
  align-items: center;
  gap: .75rem;
  padding: .6rem .75rem;
  border-radius: .9rem;
  background: var(--raise);
  border: 1px solid var(--line);
  cursor: grab;
  min-block-size: 3.25rem;
  transition: background .2s ease, border-color .2s ease, transform .25s cubic-bezier(.16,1,.3,1), box-shadow .2s ease;
}

.fu-08__row:hover {
  background: var(--surface);
  border-color: color-mix(in oklab,var(--acc) 30%,var(--line));
  box-shadow: 0 8px 18px -14px rgba(16,19,25,.5);
}

.fu-08__row:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-08__row.is-dragging {
  opacity: .45;
  cursor: grabbing;
}

.fu-08__row.is-target {
  border-color: var(--acc);
  box-shadow: 0 0 0 3px var(--acc-soft);
}

.fu-08__grip {
  display: grid;
  grid-template-columns: repeat(2,3px);
  gap: 3px;
  flex: none;
}

.fu-08__grip i {
  inline-size: 3px;
  block-size: 3px;
  border-radius: 999px;
  background: var(--grip);
}

.fu-08__row:hover .fu-08__grip i {
  background: var(--acc);
}

.fu-08__pos {
  display: grid;
  place-items: center;
  inline-size: 1.65rem;
  block-size: 1.65rem;
  border-radius: .5rem;
  flex: none;
  background: var(--acc-soft);
  color: color-mix(in oklab,var(--acc) 80%,var(--ink));
  font-family: var(--mono);
  font-size: .6875rem;
  font-variant-numeric: tabular-nums;
}

.fu-08__pos::before {
  content: counter(fu08,decimal-leading-zero);
}

.fu-08__meta {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.fu-08__name {
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.01em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-08__size {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-08__kind {
  font-family: var(--mono);
  font-size: .5625rem;
  letter-spacing: .08em;
  padding: .25rem .45rem;
  border-radius: .4rem;
  border: 1px solid var(--line);
  color: var(--muted);
  flex: none;
}

.fu-08__list:has(.is-dragging) .fu-08__row:not(.is-dragging):hover {
  background: var(--acc-soft);
}

.fu-08__foot {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
}

.fu-08__input {
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

.fu-08__add {
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  min-block-size: 2.75rem;
  padding: .6rem 1rem;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: var(--surface);
  font-size: .875rem;
  font-weight: 600;
  transition: border-color .2s ease, background .2s ease;
}

.fu-08__add:hover {
  border-color: var(--acc);
  background: var(--acc-soft);
}

.fu-08__input:focus-visible + .fu-08__add {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-08__go {
  margin-inline-start: auto;
  min-block-size: 2.75rem;
  padding: .6rem 1.1rem;
  cursor: pointer;
  border: 0;
  border-radius: .75rem;
  background: var(--acc);
  color: #fff;
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 600;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1);
}

.fu-08__go:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-08__go:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-08__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

@media (prefers-color-scheme: dark) {
  .fu-08:not([data-theme="light"]) {
    --bg: #0a0b10;
    --surface: #12141b;
    --raise: #171a22;
    --ink: #f0f2f7;
    --muted: #8b93a5;
    --line: #252a37;
    --acc: #8b96ff;
    --acc-soft: #1c2035;
    --grip: #4a5266;
  }

  .fu-08:not([data-theme="light"]) .fu-08__go {
    color: #0b0d17;
  }
}

.fu-08[data-theme="dark"] {
  --bg: #0a0b10;
  --surface: #12141b;
  --raise: #171a22;
  --ink: #f0f2f7;
  --muted: #8b93a5;
  --line: #252a37;
  --acc: #8b96ff;
  --acc-soft: #1c2035;
  --grip: #4a5266;
}

.fu-08[data-theme="dark"] .fu-08__go {
  color: #0b0d17;
}

@media (prefers-reduced-motion: reduce) {
  .fu-08 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-08__row,
    .fu-08__add,
    .fu-08__kind {
    border: 1px solid CanvasText;
  }

  .fu-08__row.is-target {
    outline: 2px solid Highlight;
  }

  .fu-08__go {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-08 {
  position: relative;
}

.fu-08__theme {
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

.fu-08__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-08__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-08__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-08__sun {
  display: none;
}

.fu-08__theme[aria-pressed="true"] .fu-08__sun {
  display: block;
}

.fu-08__theme[aria-pressed="true"] .fu-08__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-08__theme {
    transition: none;
  }

  .fu-08__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-08__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-08');
  if (!root) return;
  const list = root.querySelector('#fu-08-list');
  const input = root.querySelector('#fu-08-file');
  const status = root.querySelector('#fu-08-status');
  let dragged = null;

  const announce = (row) =>
    status.textContent = row.dataset.name + ' moved to position ' +
      ([...list.children].indexOf(row) + 1) + ' of ' + list.children.length;

  list.addEventListener('dragstart', e => {
    dragged = e.target.closest('.fu-08__row');
    if (!dragged) return;
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/plain', dragged.dataset.name);  // Firefox needs payload
    dragged.classList.add('is-dragging');
  });
  list.addEventListener('dragover', e => {
    e.preventDefault();
    const row = e.target.closest('.fu-08__row');
    if (!row || !dragged || row === dragged) return;
    const box = row.getBoundingClientRect();
    list.insertBefore(dragged, e.clientY > box.top + box.height / 2 ? row.nextSibling : row);
  });
  list.addEventListener('drop', e => e.preventDefault());
  list.addEventListener('dragend', () => {
    if (!dragged) return;
    dragged.classList.remove('is-dragging');
    announce(dragged); dragged = null;
  });

  list.addEventListener('keydown', e => {                       // WCAG 2.5.7 alternative to dragging
    const row = e.target.closest('.fu-08__row');
    if (!row || !e.altKey || (e.key !== 'ArrowUp' && e.key !== 'ArrowDown')) return;
    e.preventDefault();
    const up = e.key === 'ArrowUp';
    const sib = up ? row.previousElementSibling : row.nextElementSibling;
    if (!sib) return;
    up ? list.insertBefore(row, sib) : list.insertBefore(sib, row);
    row.focus(); announce(row);
  });

  input.addEventListener('change', () => {
    for (const f of input.files) {
      const li = list.firstElementChild.cloneNode(true);
      li.dataset.name = f.name;
      li.querySelector('.fu-08__name').textContent = f.name;
      li.querySelector('.fu-08__size').textContent = Math.max(1, Math.round(f.size / 1024)) + ' KB';
      li.querySelector('.fu-08__kind').textContent = (f.name.split('.').pop() || 'file').slice(0, 4).toUpperCase();
      list.append(li);
    }
    status.textContent = list.children.length + ' files queued';
    input.value = '';
  });

  root.querySelector('#fu-08-go').addEventListener('click', () => {
    status.textContent = 'Uploading in order: ' + [...list.children].map(li => li.dataset.name).join(' → ');
    setTimeout(() => { status.textContent = 'Queue uploaded in the order shown'; }, 1800);
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-08');
  const btn = root && root.querySelector('.fu-08__theme');
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
