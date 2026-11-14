---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/resizable-sidebar-with-a-keyboard-accessible-handle/"
title: "Resizable Sidebar with a Keyboard Accessible Handle"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Drag-to-resize is standard in tools and almost always mouse-only."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Resizable Sidebar with a Keyboard Accessible Handle
Source: https://codefronts.com/navigation/css-sidebar-navigation/resizable-sidebar-with-a-keyboard-accessible-handle/

Drag-to-resize is standard in tools and almost always mouse-only. The accessible version gives the handle role="separator" with aria-valuenow, aria-valuemin and aria-valuemax, plus arrow-key support so it can be operated without a pointer &mdash; Home and End snap to the bounds. The width is clamped to sensible limits and remembered, with the current value shown live.
## HTML
```html
<section class="sdb-10" aria-label="Aperture editor">
  <div class="sdb-10__theme">
    <input class="sdb-10__theme-input" type="checkbox" id="sdb-10-theme">
    <label class="sdb-10__theme-label" for="sdb-10-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-10__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-10__app" id="sdb-10-app" style="--sdb-10-w: 17rem;">
    <main class="sdb-10__canvas">
      <p class="sdb-10__canvas-label">Artboard &mdash; Meridian marketing site</p>
      <div class="sdb-10__art" aria-hidden="true">
        <span class="sdb-10__block sdb-10__block--a"></span>
        <span class="sdb-10__block sdb-10__block--b"></span>
        <span class="sdb-10__block sdb-10__block--c"></span>
      </div>
    </main>

    <div class="sdb-10__handle" id="sdb-10-handle" role="separator" tabindex="0" aria-orientation="vertical"
         aria-label="Resize layers panel" aria-valuemin="200" aria-valuemax="440" aria-valuenow="272" aria-controls="sdb-10-panel">
      <span class="sdb-10__grip" aria-hidden="true"></span>
    </div>

    <aside class="sdb-10__panel" id="sdb-10-panel">
      <div class="sdb-10__panel-head">
        <p class="sdb-10__panel-h">Layers</p>
        <output class="sdb-10__value" id="sdb-10-value">272px</output>
      </div>
      <nav class="sdb-10__nav" aria-label="Layer groups">
        <ul class="sdb-10__list">
          <li><a class="sdb-10__link" href="#sdb-10-panel" aria-current="page"><span class="sdb-10__dot" aria-hidden="true"></span>Hero / masthead</a></li>
          <li><a class="sdb-10__link" href="#sdb-10-panel"><span class="sdb-10__dot" aria-hidden="true"></span>Feature grid</a></li>
          <li><a class="sdb-10__link" href="#sdb-10-panel"><span class="sdb-10__dot" aria-hidden="true"></span>Pricing table</a></li>
          <li><a class="sdb-10__link" href="#sdb-10-panel"><span class="sdb-10__dot" aria-hidden="true"></span>Footer / legal</a></li>
          <li><a class="sdb-10__link" href="#sdb-10-panel"><span class="sdb-10__dot" aria-hidden="true"></span>Annotations</a></li>
          <li><a class="sdb-10__link" href="#sdb-10-panel"><span class="sdb-10__dot" aria-hidden="true"></span>Grid guides</a></li>
        </ul>
      </nav>
    </aside>
  </div>
</section>
```
## CSS
```css
.sdb-10 {
  --sdb-10-bg: #1a1a1c;
  --sdb-10-surf: #232326;
  --sdb-10-surf2: #2c2c30;
  --sdb-10-line: #3a3a3f;
  --sdb-10-ink: #ececef;
  --sdb-10-mut: #9b9ba3;
  --sdb-10-acc: #d8d84a;
  --sdb-10-acc: oklch(86% 0.17 105);
  --sdb-10-acc-soft: #33331a;
  --sdb-10-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-10-bg);
  color: var(--sdb-10-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-10 *,
.sdb-10 *::before,
.sdb-10 *::after {
  box-sizing: border-box;
}

.sdb-10:has(.sdb-10__theme-input:checked) {
  --sdb-10-bg: #f2f2f0;
  --sdb-10-surf: #ffffff;
  --sdb-10-surf2: #e7e7e3;
  --sdb-10-line: #cfcfc9;
  --sdb-10-ink: #1a1a18;
  --sdb-10-mut: #5e5e58;
  --sdb-10-acc: #6b6b12;
  --sdb-10-acc: oklch(48% 0.13 105);
  --sdb-10-acc-soft: #eaeacb;
}

@media (prefers-color-scheme: light) {
  .sdb-10 {
    --sdb-10-bg: #f2f2f0;
    --sdb-10-surf: #ffffff;
    --sdb-10-surf2: #e7e7e3;
    --sdb-10-line: #cfcfc9;
    --sdb-10-ink: #1a1a18;
    --sdb-10-mut: #5e5e58;
    --sdb-10-acc: #6b6b12;
    --sdb-10-acc: oklch(48% 0.13 105);
    --sdb-10-acc-soft: #eaeacb;
  }

  .sdb-10:has(.sdb-10__theme-input:checked) {
    --sdb-10-bg: #1a1a1c;
    --sdb-10-surf: #232326;
    --sdb-10-surf2: #2c2c30;
    --sdb-10-line: #3a3a3f;
    --sdb-10-ink: #ececef;
    --sdb-10-mut: #9b9ba3;
    --sdb-10-acc: #d8d84a;
    --sdb-10-acc: oklch(86% 0.17 105);
    --sdb-10-acc-soft: #33331a;
  }
}

@media (prefers-color-scheme: dark) {
  .sdb-10:has(.sdb-10__theme-input:checked) {
    --sdb-10-bg: #f2f2f0;
    --sdb-10-surf: #ffffff;
    --sdb-10-surf2: #e7e7e3;
    --sdb-10-line: #cfcfc9;
    --sdb-10-ink: #1a1a18;
    --sdb-10-mut: #5e5e58;
    --sdb-10-acc: #6b6b12;
    --sdb-10-acc: oklch(48% 0.13 105);
    --sdb-10-acc-soft: #eaeacb;
  }
}

.sdb-10__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-10__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-10__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-10-line);
  background: var(--sdb-10-surf);
  color: var(--sdb-10-ink);
  cursor: pointer;
}

.sdb-10__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-10__theme-input:focus-visible + .sdb-10__theme-label {
  outline: 2px solid var(--sdb-10-acc);
  outline-offset: 2px;
}

.sdb-10__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-10__app {
  display: flex;
  min-inline-size: 0;
  block-size: 100vh;
  background: var(--sdb-10-surf);
}

.sdb-10__canvas {
  flex: 1;
  min-inline-size: 0;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  background: var(--sdb-10-bg);
}

.sdb-10__canvas-label {
  margin: 0;
  font-family: var(--sdb-10-font-display);
  font-size: 0.72rem;
  color: var(--sdb-10-mut);
}

.sdb-10__art {
  flex: 1;
  min-block-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.6rem;
}

.sdb-10__block {
  border: 1px solid var(--sdb-10-line);
  background: var(--sdb-10-surf2);
}

.sdb-10__block--a {
  border-color: var(--sdb-10-acc);
}

.sdb-10__handle {
  flex: none;
  inline-size: 0.85rem;
  margin-inline: -0.25rem;
  cursor: col-resize;
  display: grid;
  place-items: center;
  background: transparent;
  touch-action: none;
  z-index: 3;
}

.sdb-10__grip {
  display: block;
  inline-size: 2px;
  block-size: 100%;
  background: var(--sdb-10-line);
}

.sdb-10__handle:hover .sdb-10__grip,
.sdb-10__handle:focus-visible .sdb-10__grip {
  background: var(--sdb-10-acc);
  inline-size: 4px;
}

.sdb-10__handle:focus-visible {
  outline: 2px solid var(--sdb-10-acc);
  outline-offset: -1px;
}

.sdb-10__panel {
  flex: none;
  inline-size: var(--sdb-10-w);
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  border-inline-start: 1px solid var(--sdb-10-line);
}

.sdb-10__panel-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 0.7rem;
  border-block-end: 1px solid var(--sdb-10-line);
}

.sdb-10__panel-h {
  margin: 0 auto 0 0;
  font-family: var(--sdb-10-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-10-mut);
}

.sdb-10__value {
  font-family: var(--sdb-10-font-display);
  font-size: 0.78rem;
  color: var(--sdb-10-acc);
  font-variant-numeric: tabular-nums;
}

.sdb-10__nav {
  flex: 1;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 0.3rem;
}

.sdb-10__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-10__link {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-block-size: 2.75rem;
  padding: 0.45rem 0.6rem;
  color: var(--sdb-10-ink);
  text-decoration: none;
  font-size: 0.88rem;
  min-inline-size: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sdb-10__dot {
  flex: none;
  inline-size: 0.5rem;
  block-size: 0.5rem;
  background: var(--sdb-10-mut);
}

.sdb-10__link:hover {
  background: var(--sdb-10-surf2);
}

.sdb-10__link[aria-current="page"] {
  background: var(--sdb-10-acc-soft);
  color: var(--sdb-10-acc);
  font-weight: 650;
}

.sdb-10__link[aria-current="page"] .sdb-10__dot {
  background: var(--sdb-10-acc);
}

.sdb-10__link:focus-visible {
  outline: 2px solid var(--sdb-10-acc);
  outline-offset: -2px;
}

@media (max-width: 34rem) {
  .sdb-10__app {
    flex-direction: column;
    block-size: auto;
    min-block-size: 100vh;
  }

  .sdb-10__canvas {
    min-block-size: 14rem;
  }

  .sdb-10__handle {
    display: none;
  }

  .sdb-10__panel {
    inline-size: 100%;
    border-inline-start: 0;
    border-block-start: 1px solid var(--sdb-10-line);
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-10');
const app = root.querySelector('#sdb-10-app');
const handle = root.querySelector('#sdb-10-handle');
const out = root.querySelector('#sdb-10-value');
const KEY = 'sdb-10:panel-w';
const MIN = 200, MAX = 440;
const clamp = (n) => Math.min(MAX, Math.max(MIN, Math.round(n)));
let w = clamp((() => { try { return Number(localStorage.getItem(KEY)) || 272; } catch (e) { return 272; } })());
function set(next) {
  w = clamp(next);
  app.style.setProperty('--sdb-10-w', w + 'px');
  handle.setAttribute('aria-valuenow', String(w));
  out.textContent = w + 'px';
  try { localStorage.setItem(KEY, String(w)); } catch (e) { /* storage blocked: session only */ }
}
function onKey(e) {
  const step = e.shiftKey ? 64 : 16;
  const map = { ArrowLeft: w + step, ArrowRight: w - step, Home: MAX, End: MIN };
  if (!(e.key in map)) return;
  e.preventDefault();
  set(map[e.key]);
}
function onMove(e) { set(app.getBoundingClientRect().right - e.clientX); }
function onDown(e) {
  handle.setPointerCapture(e.pointerId);
  handle.addEventListener('pointermove', onMove);
  handle.addEventListener('pointerup', onUp, { once: true });
}
function onUp(e) { handle.releasePointerCapture(e.pointerId); handle.removeEventListener('pointermove', onMove); }
handle.addEventListener('keydown', onKey);
handle.addEventListener('pointerdown', onDown);
set(w);
root.__sdbCleanup = () => { handle.removeEventListener('keydown', onKey); handle.removeEventListener('pointerdown', onDown); handle.removeEventListener('pointermove', onMove); };
```
