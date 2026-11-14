---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/chunked-upload-progress-list/"
title: "Chunked Upload Progress List"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "What a resumable, chunked uploader actually looks like: each file is a row of discrete chunk segments that fill one by one, one chunk fails on purpose and…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chunked Upload Progress List
Source: https://codefronts.com/components/css-file-upload-button/chunked-upload-progress-list/

What a resumable, chunked uploader actually looks like: each file is a row of discrete chunk segments that fill one by one, one chunk fails on purpose and turns red with a retry, and an aggregate bar sums the whole queue. Chunk state lives in data-* attributes so all the visual logic is CSS attribute selectors — the script only ever flips a value.
## HTML
```html
<div class="fu-15">
  <button class="fu-15__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-15__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-15__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-15__panel" aria-labelledby="fu-15-h">
    <header class="fu-15__head">
      <div>
        <h2 class="fu-15__h" id="fu-15-h">Uploading 3 files</h2>
        <p class="fu-15__sub" id="fu-15-sub">8 MB chunks <span aria-hidden="true">·</span> resumable</p>
      </div>
      <span class="fu-15__all" id="fu-15-allpct">0%</span>
    </header>

    <div class="fu-15__allbar" role="progressbar" id="fu-15-allbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Overall upload progress">
      <span id="fu-15-allfill"></span>
    </div>

    <ul class="fu-15__list" id="fu-15-list">
      <li class="fu-15__row" data-chunks="8" data-fail="-1">
        <span class="fu-15__name" id="fu-15-n1">dataset-export-2026.csv</span>
        <span class="fu-15__size">64 MB</span>
        <span class="fu-15__chunks" role="progressbar" aria-labelledby="fu-15-n1" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></span>
        <span class="fu-15__pct">0%</span>
        <button class="fu-15__retry" type="button">Retry</button>
      </li>
      <li class="fu-15__row" data-chunks="12" data-fail="7">
        <span class="fu-15__name" id="fu-15-n2">field-recordings.zip</span>
        <span class="fu-15__size">96 MB</span>
        <span class="fu-15__chunks" role="progressbar" aria-labelledby="fu-15-n2" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></span>
        <span class="fu-15__pct">0%</span>
        <button class="fu-15__retry" type="button">Retry</button>
      </li>
      <li class="fu-15__row" data-chunks="6" data-fail="-1">
        <span class="fu-15__name" id="fu-15-n3">site-survey.geojson</span>
        <span class="fu-15__size">48 MB</span>
        <span class="fu-15__chunks" role="progressbar" aria-labelledby="fu-15-n3" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></span>
        <span class="fu-15__pct">0%</span>
        <button class="fu-15__retry" type="button">Retry</button>
      </li>
    </ul>

    <div class="fu-15__foot">
      <input class="fu-15__input" id="fu-15-file" type="file" multiple>
      <label class="fu-15__add" for="fu-15-file">Add file</label>
      <button class="fu-15__start" id="fu-15-start" type="button">Start queue</button>
    </div>
    <p class="fu-15__status" id="fu-15-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600&family=Instrument+Sans:wght@400;500;600;700&display=swap');

.fu-15 {
  --bg: #06070a;
  --surface: #0e1016;
  --raise: #141821;
  --ink: #e9edf4;
  --muted: #7d8698;
  --line: #1e2430;
  --acc: #00e0b8;
  --ok: #00e0b8;
  --danger: #ff5470;
  --idle: #232a38;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(60% 40% at 100% 0%, color-mix(in oklab,var(--acc) 12%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-15,
.fu-15 *,
.fu-15 *::before,
.fu-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-15 {
    --acc: oklch(82% .15 175);
    --ok: oklch(82% .15 175);
    --danger: oklch(66% .22 12);
  }
}

.fu-15__panel {
  inline-size: min(40rem,100%);
  display: grid;
  gap: .9rem;
  padding: clamp(1.1rem,3.5vw,1.5rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: 0 40px 90px -60px #000;
}

.fu-15__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.fu-15__h {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 700;
  letter-spacing: -.025em;
}

.fu-15__sub {
  margin: .2rem 0 0;
  font-family: var(--mono);
  font-size: .625rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.fu-15__all {
  font-family: var(--mono);
  font-size: 1.0625rem;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
}

.fu-15__allbar {
  block-size: .4rem;
  border-radius: 999px;
  background: var(--idle);
  overflow: hidden;
}

.fu-15__allbar span {
  display: block;
  block-size: 100%;
  inline-size: 0%;
  border-radius: 999px;
  background: var(--acc);
  transition: inline-size .3s linear;
}

.fu-15__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .5rem;
}

.fu-15__row {
  display: grid;
  gap: .15rem .8rem;
  align-items: center;
  grid-template-columns: minmax(0,1fr) auto auto;
  grid-template-areas: "name size pct" "chunks chunks chunks";
  padding: .7rem .8rem;
  border-radius: .9rem;
  background: var(--raise);
  border: 1px solid var(--line);
  transition: border-color .25s ease, background .25s ease;
}

.fu-15__name {
  grid-area: name;
  font-size: .875rem;
  font-weight: 600;
  letter-spacing: -.01em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-15__size {
  grid-area: size;
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-15__pct {
  grid-area: pct;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-inline-size: 2.6rem;
  text-align: end;
}

.fu-15__chunks {
  grid-area: chunks;
  display: flex;
  gap: 3px;
  margin-block-start: .45rem;
}

.fu-15__chunks i {
  flex: 1;
  block-size: .4rem;
  border-radius: 2px;
  background: var(--idle);
  transition: background .28s ease, transform .28s cubic-bezier(.16,1,.3,1);
}

.fu-15__chunks i[data-state="done"] {
  background: var(--ok);
}

.fu-15__chunks i[data-state="active"] {
  background: color-mix(in oklab,var(--acc) 55%,var(--idle));
  animation: fu-15-pulse .9s ease-in-out infinite;
}

.fu-15__chunks i[data-state="error"] {
  background: var(--danger);
  transform: scaleY(1.6);
}

@keyframes fu-15-pulse {
  50% {
    background: var(--acc);
    transform: scaleY(1.5);
  }
}

.fu-15__retry {
  grid-area: pct;
  display: none;
  align-items: center;
  justify-self: end;
  cursor: pointer;
  min-block-size: 2rem;
  padding: .35rem .7rem;
  border-radius: .5rem;
  border: 1px solid color-mix(in oklab,var(--danger) 45%,transparent);
  background: color-mix(in oklab,var(--danger) 14%,transparent);
  color: var(--danger);
  font-family: var(--mono);
  font-size: .625rem;
  font-weight: 500;
  letter-spacing: .04em;
  transition: background .2s ease;
}

.fu-15__retry:hover {
  background: color-mix(in oklab,var(--danger) 26%,transparent);
}

.fu-15__retry:focus-visible {
  outline: 2px solid var(--danger);
  outline-offset: 2px;
}

.fu-15__row:has(i[data-state="error"]),
.fu-15__row.has-error {
  border-color: color-mix(in oklab,var(--danger) 45%,var(--line));
  background: color-mix(in oklab,var(--danger) 7%,var(--raise));
}

.fu-15__row:has(i[data-state="error"]) .fu-15__retry,
.fu-15__row.has-error .fu-15__retry {
  display: inline-flex;
}

.fu-15__row:has(i[data-state="error"]) .fu-15__pct,
.fu-15__row.has-error .fu-15__pct {
  display: none;
}

.fu-15__foot {
  display: flex;
  align-items: center;
  gap: .6rem;
}

.fu-15__input {
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

.fu-15__add {
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  min-block-size: 2.75rem;
  padding: .6rem 1rem;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: transparent;
  color: var(--ink);
  font-size: .875rem;
  font-weight: 600;
  transition: border-color .2s ease, background .2s ease;
}

.fu-15__add:hover {
  border-color: var(--acc);
  background: color-mix(in oklab,var(--acc) 8%,transparent);
}

.fu-15__input:focus-visible + .fu-15__add {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-15__start {
  margin-inline-start: auto;
  min-block-size: 2.75rem;
  padding: .6rem 1.2rem;
  cursor: pointer;
  border: 0;
  border-radius: .75rem;
  background: var(--acc);
  color: #03130f;
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 700;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1), opacity .2s ease;
}

.fu-15__start:hover:not(:disabled) {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-15__start:disabled {
  opacity: .45;
  cursor: not-allowed;
}

.fu-15__start:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-15__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

@media (prefers-color-scheme: light) {
  .fu-15:not([data-theme="dark"]) {
    --bg: #f0f2f6;
    --surface: #ffffff;
    --raise: #f7f8fb;
    --ink: #0a0d14;
    --muted: #5a6274;
    --line: #e2e6ee;
    --acc: #0f9d8c;
    --ok: #0f9d8c;
    --danger: #d92548;
    --idle: #e6eaf1;
  }

  .fu-15:not([data-theme="dark"]) .fu-15__start {
    color: #fff;
  }
}

.fu-15[data-theme="light"] {
  --bg: #f0f2f6;
  --surface: #ffffff;
  --raise: #f7f8fb;
  --ink: #0a0d14;
  --muted: #5a6274;
  --line: #e2e6ee;
  --acc: #0f9d8c;
  --ok: #0f9d8c;
  --danger: #d92548;
  --idle: #e6eaf1;
}

.fu-15[data-theme="light"] .fu-15__start {
  color: #fff;
}

@media (max-width: 30rem) {
  .fu-15__row {
    grid-template-columns: minmax(0,1fr) auto;
    grid-template-areas: "name pct" "size size" "chunks chunks";
  }
}

@media (prefers-reduced-motion: reduce) {
  .fu-15 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-15__panel,
    .fu-15__row {
    border: 1px solid CanvasText;
  }

  .fu-15__chunks i[data-state="done"] {
    background: Highlight;
  }

  .fu-15__chunks i[data-state="error"] {
    background: CanvasText;
  }
}
/* ── in-demo theme toggle ── */

.fu-15 {
  position: relative;
}

.fu-15__theme {
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

.fu-15__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-15__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-15__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-15__sun {
  display: none;
}

.fu-15__theme[aria-pressed="true"] .fu-15__sun {
  display: block;
}

.fu-15__theme[aria-pressed="true"] .fu-15__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-15__theme {
    transition: none;
  }

  .fu-15__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-15__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-15');
  if (!root) return;
  const rows = [...root.querySelectorAll('.fu-15__row')];
  const allFill = root.querySelector('#fu-15-allfill');
  const allPct = root.querySelector('#fu-15-allpct');
  const allBar = root.querySelector('#fu-15-allbar');
  const start = root.querySelector('#fu-15-start');
  const input = root.querySelector('#fu-15-file');
  const status = root.querySelector('#fu-15-status');

  const build = (row) => {
    const box = row.querySelector('.fu-15__chunks');
    box.replaceChildren(...Array.from({ length: Number(row.dataset.chunks) }, () => {
      const i = document.createElement('i'); i.dataset.state = 'idle'; return i;
    }));
  };
  rows.forEach(build);

  const total = () => rows.reduce((s, r) => s + Number(r.dataset.chunks), 0);
  const done = () => rows.reduce((s, r) => s + r.querySelectorAll('i[data-state="done"]').length, 0);
  const refreshAll = () => {
    const p = Math.round((done() / total()) * 100);
    allFill.style.inlineSize = p + '%'; allPct.textContent = p + '%';
    allBar.setAttribute('aria-valuenow', p);
  };

  const run = (row, from = 0) => new Promise(res => {
    const segs = [...row.querySelectorAll('i')];
    const fail = Number(row.dataset.fail);
    const bar = row.querySelector('.fu-15__chunks');
    let i = from;
    row.classList.remove('has-error');
    const tick = () => {
      if (i >= segs.length) return res(true);
      if (i === fail && row.dataset.failed !== 'yes') {
        segs[i].dataset.state = 'error';
        row.dataset.failed = 'yes'; row.classList.add('has-error');
        status.textContent = row.querySelector('.fu-15__name').textContent + ' failed at chunk ' + (i + 1) + ' — retry available';
        return res(false);
      }
      segs[i].dataset.state = 'active';
      setTimeout(() => {
        segs[i].dataset.state = 'done';
        const p = Math.round(((i + 1) / segs.length) * 100);
        row.querySelector('.fu-15__pct').textContent = p + '%';
        bar.setAttribute('aria-valuenow', p);
        refreshAll(); i++; tick();
      }, 180 + Math.random() * 220);
    };
    tick();
  });

  start.addEventListener('click', async () => {
    start.disabled = true;
    status.textContent = 'Uploading queue…';
    for (const row of rows) await run(row);
    start.disabled = false;
    status.textContent = done() === total() ? 'All chunks uploaded' : 'Queue finished with errors — retry the failed file';
  });

  root.addEventListener('click', (e) => {
    const btn = e.target.closest('.fu-15__retry');
    if (!btn) return;
    const row = btn.closest('.fu-15__row');
    const segs = [...row.querySelectorAll('i')];
    const from = segs.findIndex(s => s.dataset.state === 'error');
    segs[from].dataset.state = 'idle';
    status.textContent = 'Resuming from chunk ' + (from + 1) + '…';
    run(row, from).then(() => refreshAll());
  });

  input.addEventListener('change', () => {
    for (const f of input.files) {
      const row = rows[0].cloneNode(true);
      const id = 'fu-15-n' + (rows.length + 1);
      row.dataset.chunks = Math.min(16, Math.ceil(f.size / 8388608) || 3);
      row.dataset.fail = '-1'; row.removeAttribute('data-failed');
      row.classList.remove('has-error');
      Object.assign(row.querySelector('.fu-15__name'), { textContent: f.name, id });
      row.querySelector('.fu-15__chunks').setAttribute('aria-labelledby', id);
      row.querySelector('.fu-15__size').textContent = Math.max(1, Math.round(f.size / 1048576)) + ' MB';
      row.querySelector('.fu-15__pct').textContent = '0%';
      build(row);
      root.querySelector('#fu-15-list').append(row);
      rows.push(row);
    }
    root.querySelector('#fu-15-h').textContent = 'Uploading ' + rows.length + ' files';
    input.value = ''; refreshAll();
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-15');
  const btn = root && root.querySelector('.fu-15__theme');
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
