---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/drag-and-drop-file-upload-zone/"
title: "Drag and Drop File Upload Zone"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "The canonical dropzone, done to spec."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Drag and Drop File Upload Zone
Source: https://codefronts.com/components/css-file-upload-button/drag-and-drop-file-upload-zone/

The canonical dropzone, done to spec. All four drag events call preventDefault() (miss one and the browser navigates away to the dropped file), dragleave flicker from child elements is fixed with a depth counter, and the zone is a real role="button" with tabindex="0" that opens the picker on Space or Enter. The dashed outline is an SVG stroke-dasharray that marches only while a drag is over it.
## HTML
```html
<div class="fu-06">
  <button class="fu-06__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <div class="fu-06__zone" id="fu-06-zone" role="button" tabindex="0"
       aria-label="Drop files here, or press Enter to browse your device" aria-describedby="fu-06-hint">
    <svg class="fu-06__outline" aria-hidden="true" focusable="false" preserveAspectRatio="none">
      <rect x="1" y="1" rx="22" ry="22" width="calc(100% - 2px)" height="calc(100% - 2px)"></rect>
    </svg>

    <span class="fu-06__art" aria-hidden="true">
      <span class="fu-06__sheet fu-06__sheet--a"></span>
      <span class="fu-06__sheet fu-06__sheet--b"></span>
      <span class="fu-06__sheet fu-06__sheet--c">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 16V6m0 0-3.4 3.4M12 6l3.4 3.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
    </span>

    <p class="fu-06__title">Drop files to upload</p>
    <p class="fu-06__hint" id="fu-06-hint">
      or <label class="fu-06__browse" for="fu-06-file">browse your device</label>
      <span class="fu-06__rule" aria-hidden="true"></span>
      <span class="fu-06__types">PNG, JPG, PDF, ZIP · 100 MB</span>
    </p>

    <input class="fu-06__input" id="fu-06-file" type="file" multiple accept=".png,.jpg,.jpeg,.pdf,.zip">
  </div>

  <ul class="fu-06__chips" id="fu-06-chips"></ul>
  <p class="fu-06__status" id="fu-06-status" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-06 {
  --bg: #0a0c11;
  --surface: #12151d;
  --ink: #eff2f7;
  --muted: #8a93a6;
  --line: #262c3a;
  --acc: #6d7cff;
  --acc2: #31e0c0;
  --march: 1.4s;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 1rem;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(90% 60% at 50% -10%, color-mix(in oklab,var(--acc) 16%,transparent), transparent 65%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-06,
.fu-06 *,
.fu-06 *::before,
.fu-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-06 {
    --acc: oklch(64% .19 275);
    --acc2: oklch(82% .15 178);
  }
}

.fu-06__zone {
  position: relative;
  isolation: isolate;
  cursor: pointer;
  inline-size: min(34rem,100%);
  min-block-size: clamp(16rem,42vh,22rem);
  display: grid;
  place-content: center;
  justify-items: center;
  gap: .55rem;
  text-align: center;
  padding: clamp(1.5rem,5vw,2.5rem);
  border-radius: 1.5rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--surface) 92%,transparent), var(--surface));
  transition: transform .35s cubic-bezier(.16,1,.3,1), background .35s ease, box-shadow .35s ease;
}

.fu-06__zone::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  opacity: 0;
  background: radial-gradient(70% 60% at 50% 40%, color-mix(in oklab,var(--acc) 30%,transparent), transparent 70%);
  transition: opacity .35s ease;
}

.fu-06__zone:hover {
  background: linear-gradient(180deg, color-mix(in oklab,var(--acc) 6%,var(--surface)), var(--surface));
}

.fu-06__zone:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 4px;
}

.fu-06__zone.is-over {
  transform: scale(1.015);
  box-shadow: 0 30px 70px -45px var(--acc);
}

.fu-06__zone.is-over::before {
  opacity: 1;
}

.fu-06__outline {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  z-index: -1;
  pointer-events: none;
}

.fu-06__outline rect {
  fill: none;
  stroke: var(--line);
  stroke-width: 2;
  stroke-dasharray: 14 12;
  transition: stroke .3s ease;
}

.fu-06__zone.is-over .fu-06__outline rect {
  stroke: var(--acc2);
  animation: fu-06-march var(--march) linear infinite;
}

@keyframes fu-06-march {
  to {
    stroke-dashoffset: -52;
  }
}

.fu-06__art {
  position: relative;
  inline-size: 5.5rem;
  block-size: 4rem;
  margin-block-end: .4rem;
}

.fu-06__sheet {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 50%;
  inline-size: 2.6rem;
  block-size: 3.4rem;
  border-radius: .5rem;
  border: 1px solid var(--line);
  background: color-mix(in oklab,var(--ink) 6%,var(--surface));
  translate: -50% 0;
  transition: rotate .4s cubic-bezier(.16,1,.3,1), translate .4s cubic-bezier(.16,1,.3,1);
}

.fu-06__sheet--a {
  rotate: -13deg;
  translate: -125% 6px;
}

.fu-06__sheet--b {
  rotate: 11deg;
  translate: 25% 4px;
}

.fu-06__sheet--c {
  display: grid;
  place-items: center;
  z-index: 1;
  color: var(--acc2);
  border-color: color-mix(in oklab,var(--acc2) 40%,var(--line));
  background: color-mix(in oklab,var(--acc) 16%,var(--surface));
}

.fu-06__sheet--c svg {
  inline-size: 1.4rem;
  block-size: 1.4rem;
}

.fu-06__zone:hover .fu-06__sheet--a,
.fu-06__zone.is-over .fu-06__sheet--a {
  rotate: -22deg;
  translate: -142% 2px;
}

.fu-06__zone:hover .fu-06__sheet--b,
.fu-06__zone.is-over .fu-06__sheet--b {
  rotate: 20deg;
  translate: 42% 0;
}

.fu-06__zone.is-over .fu-06__sheet--c {
  translate: -50% -8px;
}

.fu-06__title {
  margin: 0;
  font-size: clamp(1.15rem,2.6vw,1.4rem);
  font-weight: 700;
  letter-spacing: -.025em;
}

.fu-06__hint {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: .5rem;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
}

.fu-06__browse {
  cursor: pointer;
  color: var(--acc2);
  text-decoration: underline;
  text-underline-offset: 3px;
  padding: .35rem 0;
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
}

.fu-06__browse:hover {
  color: var(--ink);
}

.fu-06__rule {
  inline-size: 1px;
  block-size: .85rem;
  background: var(--line);
}

.fu-06__input {
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

.fu-06__input:focus-visible ~ .fu-06__title {
  text-decoration: underline;
}

.fu-06__chips {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: center;
  inline-size: min(34rem,100%);
}

.fu-06__chips:empty {
  display: none;
}

.fu-06__chips li {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding: .4rem .7rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--acc) 12%,var(--surface));
  border: 1px solid var(--line);
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--ink);
  transition: opacity .3s ease, transform .3s cubic-bezier(.16,1,.3,1);
}

@starting-style {
  .fu-06__chips li {
    opacity: 0;
    transform: translateY(6px);
  }
}

.fu-06__chips b {
  font-weight: 500;
  color: var(--muted);
}

.fu-06__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

@media (prefers-color-scheme: light) {
  .fu-06:not([data-theme="dark"]) {
    --bg: #f2f4f9;
    --surface: #ffffff;
    --ink: #0c0f16;
    --muted: #5b6478;
    --line: #dfe3ec;
    --acc: #4a5bff;
    --acc2: #0f9c85;
  }
}

.fu-06[data-theme="light"] {
  --bg: #f2f4f9;
  --surface: #ffffff;
  --ink: #0c0f16;
  --muted: #5b6478;
  --line: #dfe3ec;
  --acc: #4a5bff;
  --acc2: #0f9c85;
}

@media (prefers-reduced-motion: reduce) {
  .fu-06 * {
    animation: none !important;
    transition: none !important;
  }

  .fu-06__zone.is-over {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-06__outline rect {
    stroke: CanvasText;
  }

  .fu-06__zone.is-over .fu-06__outline rect {
    stroke: Highlight;
  }

  .fu-06__sheet {
    border: 1px solid CanvasText;
  }
}
/* ── in-demo theme toggle ── */

.fu-06 {
  position: relative;
}

.fu-06__theme {
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

.fu-06__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-06__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-06__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-06__sun {
  display: none;
}

.fu-06__theme[aria-pressed="true"] .fu-06__sun {
  display: block;
}

.fu-06__theme[aria-pressed="true"] .fu-06__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-06__theme {
    transition: none;
  }

  .fu-06__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-06__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-06');
  if (!root) return;
  const zone = root.querySelector('#fu-06-zone');
  const input = root.querySelector('#fu-06-file');
  const chips = root.querySelector('#fu-06-chips');
  const status = root.querySelector('#fu-06-status');
  let depth = 0;

  const fmt = (n) => {
    const u = ['B','KB','MB','GB']; let i = 0;
    while (n >= 1024 && i < u.length - 1) { n /= 1024; i++; }
    return Math.round(n) + ' ' + u[i];
  };

  const accept = (files) => {
    const list = [...files];
    if (!list.length) return;
    chips.replaceChildren(...list.map(f => {
      const li = document.createElement('li');
      li.append(f.name, Object.assign(document.createElement('b'), { textContent: fmt(f.size) }));
      return li;
    }));
    status.textContent = list.length + ' file' + (list.length === 1 ? '' : 's') + ' ready — ' + list.map(f => f.name).join(', ');
  };

  // preventDefault on ALL FOUR, or the browser opens the dropped file
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(t =>
    zone.addEventListener(t, e => { e.preventDefault(); e.stopPropagation(); })
  );
  zone.addEventListener('dragenter', () => { depth++; zone.classList.add('is-over'); });
  zone.addEventListener('dragover', e => { e.dataTransfer.dropEffect = 'copy'; });
  zone.addEventListener('dragleave', () => { if (--depth <= 0) { depth = 0; zone.classList.remove('is-over'); } });
  zone.addEventListener('drop', e => {
    depth = 0; zone.classList.remove('is-over');
    accept(e.dataTransfer.files);
  });

  zone.addEventListener('click', e => { if (!e.target.closest('label')) input.click(); });
  zone.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); }
  });
  input.addEventListener('change', () => accept(input.files));
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-06');
  const btn = root && root.querySelector('.fu-06__theme');
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
