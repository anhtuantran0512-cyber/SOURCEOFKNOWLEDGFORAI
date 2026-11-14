---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/grain-paint-cost-and-byte-size-measured/"
title: "Grain Paint Cost and Byte Size Measured"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Everyone repeats that SVG filters are expensive."
has_js: "true"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Grain Paint Cost and Byte Size Measured
Source: https://codefronts.com/design-styles/css-grain-texture/grain-paint-cost-and-byte-size-measured/

Everyone repeats that SVG filters are expensive. Nobody says how expensive. This demo measures it live in your own browser: frame time for a grained surface versus a plain one, the cost curve across numOctaves, the cost of six blended layers, and the real byte size of each texture definition read straight out of the computed styles.
## HTML
```html
<section class="grn-06" aria-labelledby="grn-06-title">
  <svg class="grn-06__defs" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="grn-06-oct5" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="5" seed="17" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </svg>

  <div class="grn-06__theme">
    <input class="grn-06__theme-input" type="checkbox" id="grn-06-theme">
    <label class="grn-06__theme-label" for="grn-06-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-06__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-06__shell">
    <header class="grn-06__head">
      <p class="grn-06__kicker">Measured, not guessed · 06</p>
      <h1 class="grn-06__h1" id="grn-06-title">What grain actually costs on this machine</h1>
      <p class="grn-06__lede">Four surfaces, one animated property, median frame time across a real sample. Then the byte size of each texture definition, read out of the computed styles rather than estimated.</p>
    </header>

    <section class="grn-06__panel" aria-labelledby="grn-06-h-paint">
      <div class="grn-06__panel-head">
        <h2 class="grn-06__h2" id="grn-06-h-paint">Paint cost</h2>
        <div class="grn-06__controls">
          <p class="grn-06__status" role="status" data-grn-06-status>Ready</p>
          <button class="grn-06__run" type="button" data-grn-06-run data-grn06-frames="48">Run measurement</button>
        </div>
      </div>

      <ul class="grn-06__rows" data-grn-06-rows>
        <li class="grn-06__row" data-grn06-row="control">
          <span class="grn-06__stage grn-06__stage--plain" data-grn-06-stage="control"></span>
          <span class="grn-06__row-name">No grain <em>control</em></span>
          <span class="grn-06__bar"><span class="grn-06__fill" data-grn-06-fill style="--grn-06-pct: 0"></span></span>
          <span class="grn-06__ms" data-grn-06-ms>—</span>
        </li>
        <li class="grn-06__row" data-grn06-row="datauri">
          <span class="grn-06__stage grn-06__stage--datauri" data-grn-06-stage="datauri"></span>
          <span class="grn-06__row-name">Data URI grain <em>3 octaves, cached</em></span>
          <span class="grn-06__bar"><span class="grn-06__fill" data-grn-06-fill style="--grn-06-pct: 0"></span></span>
          <span class="grn-06__ms" data-grn-06-ms>—</span>
        </li>
        <li class="grn-06__row" data-grn06-row="filter">
          <span class="grn-06__stage grn-06__stage--filter" data-grn-06-stage="filter"></span>
          <span class="grn-06__row-name">Live SVG filter <em>5 octaves, re-evaluated</em></span>
          <span class="grn-06__bar"><span class="grn-06__fill" data-grn-06-fill style="--grn-06-pct: 0"></span></span>
          <span class="grn-06__ms" data-grn-06-ms>—</span>
        </li>
        <li class="grn-06__row" data-grn06-row="stack">
          <span class="grn-06__stage grn-06__stage--stack" data-grn-06-stage="stack"></span>
          <span class="grn-06__row-name">Six blended layers <em>the expensive case</em></span>
          <span class="grn-06__bar"><span class="grn-06__fill" data-grn-06-fill style="--grn-06-pct: 0"></span></span>
          <span class="grn-06__ms" data-grn-06-ms>—</span>
        </li>
      </ul>
      <p class="grn-06__caveat">Median milliseconds per frame while a sub-pixel translate forces a repaint. Lower is better. Close devtools and keep the tab focused for a number worth quoting.</p>
    </section>

    <section class="grn-06__panel" aria-labelledby="grn-06-h-bytes">
      <div class="grn-06__panel-head">
        <h2 class="grn-06__h2" id="grn-06-h-bytes">Byte size</h2>
        <p class="grn-06__note">Read from computed styles, percent-encoding included.</p>
      </div>
      <dl class="grn-06__bytes" data-grn-06-bytes>
        <div><dt>Fine grain token</dt><dd data-grn-06-byte="fine">—</dd></div>
        <div><dt>Coarse grain token</dt><dd data-grn-06-byte="coarse">—</dd></div>
        <div><dt>Both, gzip-ish estimate</dt><dd data-grn-06-byte="gz">—</dd></div>
        <div><dt>Typical seamless PNG</dt><dd>148 KB · 1 request</dd></div>
      </dl>
    </section>
  </main>
</section>
```
## CSS
```css
.grn-06 {
  --grn-06-noise-fine: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150'%3E%3Cfilter id='grn06a'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='150' height='150' filter='url(%23grn06a)' opacity='0.6'/%3E%3C/svg%3E");
  --grn-06-noise-coarse: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='grn06b'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.28' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23grn06b)' opacity='0.5'/%3E%3C/svg%3E");
  --grn-06-bg: #131313;
  --grn-06-surf: #1c1c1c;
  --grn-06-line: #2e2e2e;
  --grn-06-ink: #f3f1ee;
  --grn-06-mut: #9c968e;
  --grn-06-acc: #fbbf24;
  --grn-06-acc: oklch(83% 0.15 80);
  --grn-06-on-acc: #1c1400;
  --grn-06-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-06-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-06-bg);
  color: var(--grn-06-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-06 *,
.grn-06 *::before,
.grn-06 *::after {
  box-sizing: border-box;
}

.grn-06 :focus-visible {
  outline: 2px solid var(--grn-06-acc);
  outline-offset: 3px;
}

.grn-06 code {
  font-family: var(--grn-06-font-mono);
  font-size: 0.9em;
}

.grn-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.grn-06__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.grn-06:has(.grn-06__theme-input:checked) {
  --grn-06-bg: #f4f2ef;
  --grn-06-surf: #ffffff;
  --grn-06-line: #dedad4;
  --grn-06-ink: #131313;
  --grn-06-mut: #625d55;
  --grn-06-acc: #b45309;
  --grn-06-acc: oklch(52% 0.14 62);
  --grn-06-on-acc: #fffbeb;
}

@media (prefers-color-scheme: light) {
  .grn-06 {
    --grn-06-bg: #f4f2ef;
    --grn-06-surf: #ffffff;
    --grn-06-line: #dedad4;
    --grn-06-ink: #131313;
    --grn-06-mut: #625d55;
    --grn-06-acc: #b45309;
    --grn-06-acc: oklch(52% 0.14 62);
    --grn-06-on-acc: #fffbeb;
  }

  .grn-06:has(.grn-06__theme-input:checked) {
    --grn-06-bg: #131313;
    --grn-06-surf: #1c1c1c;
    --grn-06-line: #2e2e2e;
    --grn-06-ink: #f3f1ee;
    --grn-06-mut: #9c968e;
    --grn-06-acc: #fbbf24;
    --grn-06-acc: oklch(83% 0.15 80);
    --grn-06-on-acc: #1c1400;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-06:has(.grn-06__theme-input:checked) {
    --grn-06-bg: #f4f2ef;
    --grn-06-surf: #ffffff;
    --grn-06-line: #dedad4;
    --grn-06-ink: #131313;
    --grn-06-mut: #625d55;
    --grn-06-acc: #b45309;
    --grn-06-acc: oklch(52% 0.14 62);
    --grn-06-on-acc: #fffbeb;
  }
}

.grn-06__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-06__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-06__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-06-line);
  border-radius: 999px;
  background: var(--grn-06-surf);
  color: var(--grn-06-ink);
  cursor: pointer;
}

.grn-06__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-06__theme-input:focus-visible + .grn-06__theme-label {
  outline: 2px solid var(--grn-06-acc);
  outline-offset: 3px;
}

.grn-06__shell {
  inline-size: min(70rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(1.8rem, 4.5vw, 2.8rem);
}

.grn-06__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.7rem;
}

.grn-06__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-06-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-06-acc);
}

.grn-06__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.2vw, 3.3rem)/1.04 var(--grn-06-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-06__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-06-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.08rem);
  text-wrap: pretty;
}

.grn-06__panel {
  display: grid;
  gap: 1rem;
  padding: clamp(1.1rem, 3vw, 1.8rem);
  border: 1px solid var(--grn-06-line);
  border-radius: 16px;
  background: var(--grn-06-surf);
}

.grn-06__panel-head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 0.6rem 1rem;
  padding-block-end: 0.7rem;
  border-block-end: 1px solid var(--grn-06-line);
}

.grn-06__h2 {
  margin: 0;
  font: 600 clamp(1.1rem, 2.6vw, 1.35rem)/1.2 var(--grn-06-font-display);
}

.grn-06__note {
  margin: 0;
  color: var(--grn-06-mut);
  font-size: 0.85rem;
}

.grn-06__controls {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  flex-wrap: wrap;
}

.grn-06__status {
  margin: 0;
  font: 400 0.8rem/1 var(--grn-06-font-mono);
  color: var(--grn-06-mut);
}

.grn-06__run {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1.1rem;
  border: 0;
  border-radius: 10px;
  background: var(--grn-06-acc);
  color: var(--grn-06-on-acc);
  font: 600 0.85rem/1 var(--grn-06-font-display);
  cursor: pointer;
}

.grn-06__run:hover {
  filter: brightness(1.07);
}

.grn-06__run[disabled] {
  opacity: 0.55;
  cursor: progress;
}

.grn-06__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.55rem;
}

.grn-06__row {
  display: grid;
  align-items: center;
  gap: 0.5rem 0.85rem;
  grid-template-columns: 44px minmax(0, 1fr) auto;
}

@media (min-width: 46rem) {
  .grn-06__row {
    grid-template-columns: 52px minmax(9rem, 15rem) minmax(0, 1fr) 5.5rem;
  }
}

.grn-06__stage {
  position: relative;
  block-size: 44px;
  border-radius: 8px;
  overflow: hidden;
  isolation: isolate;
  background: linear-gradient(135deg, var(--grn-06-acc), color-mix(in oklab, var(--grn-06-acc) 25%, var(--grn-06-surf)));
}

.grn-06__stage--datauri::after {
  content: "";
  position: absolute;
  inset: -2px;
  background-image: var(--grn-06-noise-fine);
  opacity: 0.5;
  mix-blend-mode: overlay;
}

.grn-06__stage--filter::after {
  content: "";
  position: absolute;
  inset: -2px;
  filter: url(#grn-06-oct5);
  opacity: 0.5;
  mix-blend-mode: overlay;
}

.grn-06__stage--stack::after,
.grn-06__stage--stack::before {
  content: "";
  position: absolute;
  inset: -2px;
  background-image: var(--grn-06-noise-fine), var(--grn-06-noise-coarse), var(--grn-06-noise-fine);
  opacity: 0.45;
  mix-blend-mode: overlay;
}

.grn-06__stage--stack::before {
  background-image: var(--grn-06-noise-coarse), var(--grn-06-noise-fine), var(--grn-06-noise-coarse);
  mix-blend-mode: soft-light;
}

.grn-06__row-name {
  font-size: 0.9rem;
  grid-column: 2 / -1;
}

@media (min-width: 46rem) {
  .grn-06__row-name {
    grid-column: auto;
  }
}

.grn-06__row-name em {
  display: block;
  font-style: normal;
  font-size: 0.76rem;
  color: var(--grn-06-mut);
}

.grn-06__bar {
  position: relative;
  display: block;
  block-size: 10px;
  border-radius: 999px;
  overflow: hidden;
  background: color-mix(in oklab, var(--grn-06-ink) 10%, transparent);
  grid-column: 1 / 3;
}

@media (min-width: 46rem) {
  .grn-06__bar {
    grid-column: auto;
  }
}

.grn-06__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--grn-06-pct, 0) * 1%);
  border-radius: 999px;
  background: var(--grn-06-acc);
  transition: inline-size 420ms cubic-bezier(0.22, 1, 0.36, 1);
}

.grn-06__ms {
  justify-self: end;
  font: 500 0.92rem/1 var(--grn-06-font-mono);
  font-variant-numeric: tabular-nums;
}

.grn-06__caveat {
  margin: 0;
  color: var(--grn-06-mut);
  font-size: 0.83rem;
  text-wrap: pretty;
}

.grn-06__bytes {
  display: grid;
  gap: 0.6rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  margin: 0;
}

.grn-06__bytes > div {
  display: grid;
  gap: 0.2rem;
  padding: 0.8rem 0.9rem;
  border: 1px solid var(--grn-06-line);
  border-radius: 12px;
  background: color-mix(in oklab, var(--grn-06-acc) 7%, transparent);
}

.grn-06__bytes dt {
  margin: 0;
  font-size: 0.78rem;
  color: var(--grn-06-mut);
}

.grn-06__bytes dd {
  margin: 0;
  font: 600 1.05rem/1.2 var(--grn-06-font-mono);
  font-variant-numeric: tabular-nums;
}

@media (prefers-reduced-motion: reduce) {
  .grn-06__fill {
    transition-duration: 1ms;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.grn-06');
const runBtn = root.querySelector('[data-grn-06-run]');
const statusEl = root.querySelector('[data-grn-06-status]');
const rows = Array.from(root.querySelectorAll('[data-grn06-row]'));
const frames = Number(runBtn.dataset.grn06Frames || 48);
let rafId = 0;
let cancelled = false;

function bytes(str) {
  return new TextEncoder().encode(str).length;
}

function fmt(n) {
  return n >= 1024 ? (n / 1024).toFixed(1) + ' KB' : n + ' B';
}

function reportBytes() {
  const cs = getComputedStyle(root);
  const fine = cs.getPropertyValue('--grn-06-noise-fine').trim();
  const coarse = cs.getPropertyValue('--grn-06-noise-coarse').trim();
  const bf = bytes(fine);
  const bc = bytes(coarse);
  const set = (key, val) => {
    const el = root.querySelector('[data-grn-06-byte="' + key + '"]');
    if (el) el.textContent = val;
  };
  set('fine', fmt(bf));
  set('coarse', fmt(bc));
  set('gz', '~' + fmt(Math.round((bf + bc) * 0.42)) + ' over the wire');
}

function median(list) {
  const s = list.slice().sort((a, b) => a - b);
  const mid = s.length >> 1;
  return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
}

function measure(stage) {
  return new Promise((resolve) => {
    const deltas = [];
    let last = performance.now();
    let i = 0;
    stage.style.willChange = 'transform';
    const tick = (now) => {
      if (cancelled) { stage.style.willChange = ''; resolve(0); return; }
      deltas.push(now - last);
      last = now;
      stage.style.transform = 'translate3d(' + ((i % 2) * 0.5) + 'px,0,0)';
      i += 1;
      if (i < frames) { rafId = requestAnimationFrame(tick); }
      else {
        stage.style.willChange = '';
        stage.style.transform = '';
        resolve(median(deltas.slice(4)));
      }
    };
    rafId = requestAnimationFrame(tick);
  });
}

async function run() {
  runBtn.disabled = true;
  const results = [];
  for (const row of rows) {
    if (cancelled) break;
    const key = row.dataset.grn06Row;
    statusEl.textContent = 'Measuring ' + key + '…';
    const stage = row.querySelector('[data-grn-06-stage]');
    const ms = await measure(stage);
    results.push({ row: row, ms: ms });
  }
  if (cancelled) return;
  const peak = Math.max.apply(null, results.map((r) => r.ms)) || 1;
  results.forEach((r) => {
    row_paint(r, peak);
  });
  statusEl.textContent = 'Median of ' + frames + ' frames · run again for variance';
  runBtn.disabled = false;
}

function row_paint(r, peak) {
  const msEl = r.row.querySelector('[data-grn-06-ms]');
  const fill = r.row.querySelector('[data-grn-06-fill]');
  if (msEl) msEl.textContent = r.ms.toFixed(2) + ' ms';
  if (fill) fill.style.setProperty('--grn-06-pct', String(Math.max(4, Math.round((r.ms / peak) * 100))));
}

reportBytes();
runBtn.addEventListener('click', run);

root.__grnCleanup = () => {
  cancelled = true;
  cancelAnimationFrame(rafId);
  runBtn.removeEventListener('click', run);
};
```
