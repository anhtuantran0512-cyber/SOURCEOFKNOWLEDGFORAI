---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/persisting-sidebar-collapse-state-across-reloads/"
title: "Persisting Sidebar Collapse State Across Reloads"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "A sidebar that forgets it was collapsed is a small daily annoyance that compounds."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Persisting Sidebar Collapse State Across Reloads
Source: https://codefronts.com/navigation/css-sidebar-navigation/persisting-sidebar-collapse-state-across-reloads/

A sidebar that forgets it was collapsed is a small daily annoyance that compounds. Persist the boolean, then apply it before first paint &mdash; an inline script in <head> that sets a class on the root, the same trick a theme toggle uses. Reading the value in a framework effect instead means the wide sidebar paints first and visibly snaps shut. Every read and write is wrapped, because storage throws in sandboxed and private contexts.
## HTML
```html
<section class="sdb-07" aria-label="Prism analytics">
  <div class="sdb-07__theme">
    <input class="sdb-07__theme-input" type="checkbox" id="sdb-07-theme">
    <label class="sdb-07__theme-label" for="sdb-07-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-07__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-07__app" data-sdb-07-collapsed="false" data-sdb-07-noanim>
    <aside class="sdb-07__rail" id="sdb-07-rail">
      <div class="sdb-07__rail-head">
        <span class="sdb-07__mark" aria-hidden="true">PR</span>
        <p class="sdb-07__brand"><span class="sdb-07__hideable">Prism</span></p>
        <button class="sdb-07__collapse" type="button" id="sdb-07-toggle" aria-expanded="true" aria-controls="sdb-07-rail">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h10M4 18h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-07__sr">Collapse sidebar</span>
        </button>
      </div>
      <nav class="sdb-07__nav" aria-label="Prism reports">
        <ul class="sdb-07__list">
          <li><a class="sdb-07__link" href="#sdb-07-main" aria-current="page"><span class="sdb-07__ico" aria-hidden="true">01</span><span class="sdb-07__hideable">Overview</span></a></li>
          <li><a class="sdb-07__link" href="#sdb-07-main"><span class="sdb-07__ico" aria-hidden="true">02</span><span class="sdb-07__hideable">Acquisition</span></a></li>
          <li><a class="sdb-07__link" href="#sdb-07-main"><span class="sdb-07__ico" aria-hidden="true">03</span><span class="sdb-07__hideable">Retention</span></a></li>
          <li><a class="sdb-07__link" href="#sdb-07-main"><span class="sdb-07__ico" aria-hidden="true">04</span><span class="sdb-07__hideable">Revenue</span></a></li>
          <li><a class="sdb-07__link" href="#sdb-07-main"><span class="sdb-07__ico" aria-hidden="true">05</span><span class="sdb-07__hideable">Audit log</span></a></li>
        </ul>
      </nav>
    </aside>

    <main class="sdb-07__main" id="sdb-07-main">
      <div class="sdb-07__kpis">
        <div class="sdb-07__kpi"><p class="sdb-07__kpi-k">Active workspaces</p><p class="sdb-07__kpi-v">1,284</p></div>
        <div class="sdb-07__kpi"><p class="sdb-07__kpi-k">Weekly retention</p><p class="sdb-07__kpi-v">71.4%</p></div>
        <div class="sdb-07__kpi"><p class="sdb-07__kpi-k">Net revenue</p><p class="sdb-07__kpi-v">$418k</p></div>
      </div>
      <div class="sdb-07__chart" aria-hidden="true">
        <span style="--sdb-07-h:32"></span><span style="--sdb-07-h:48"></span><span style="--sdb-07-h:41"></span>
        <span style="--sdb-07-h:66"></span><span style="--sdb-07-h:58"></span><span style="--sdb-07-h:74"></span>
        <span style="--sdb-07-h:69"></span><span style="--sdb-07-h:88"></span><span style="--sdb-07-h:79"></span>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-07 {
  --sdb-07-bg: #eef4f1;
  --sdb-07-surf: #ffffff;
  --sdb-07-surf2: #e2ebe7;
  --sdb-07-line: #cbd8d2;
  --sdb-07-ink: #16211d;
  --sdb-07-mut: #5a6a64;
  --sdb-07-acc: #0f7a63;
  --sdb-07-acc: oklch(50% 0.1 172);
  --sdb-07-acc-soft: #d5eae4;
  --sdb-07-w-open: 14.5rem;
  --sdb-07-w-rail: 4.25rem;
  --sdb-07-font-display: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-07-bg);
  color: var(--sdb-07-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-07 *,
.sdb-07 *::before,
.sdb-07 *::after {
  box-sizing: border-box;
}

.sdb-07:has(.sdb-07__theme-input:checked) {
  --sdb-07-bg: #0b1210;
  --sdb-07-surf: #121a18;
  --sdb-07-surf2: #18221f;
  --sdb-07-line: #26332f;
  --sdb-07-ink: #e9f1ee;
  --sdb-07-mut: #93a4a0;
  --sdb-07-acc: #62d9b8;
  --sdb-07-acc: oklch(82% 0.12 172);
  --sdb-07-acc-soft: #12302a;
}

@media (prefers-color-scheme: dark) {
  .sdb-07 {
    --sdb-07-bg: #0b1210;
    --sdb-07-surf: #121a18;
    --sdb-07-surf2: #18221f;
    --sdb-07-line: #26332f;
    --sdb-07-ink: #e9f1ee;
    --sdb-07-mut: #93a4a0;
    --sdb-07-acc: #62d9b8;
    --sdb-07-acc: oklch(82% 0.12 172);
    --sdb-07-acc-soft: #12302a;
  }

  .sdb-07:has(.sdb-07__theme-input:checked) {
    --sdb-07-bg: #eef4f1;
    --sdb-07-surf: #ffffff;
    --sdb-07-surf2: #e2ebe7;
    --sdb-07-line: #cbd8d2;
    --sdb-07-ink: #16211d;
    --sdb-07-mut: #5a6a64;
    --sdb-07-acc: #0f7a63;
    --sdb-07-acc: oklch(50% 0.1 172);
    --sdb-07-acc-soft: #d5eae4;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-07:has(.sdb-07__theme-input:checked) {
    --sdb-07-bg: #0b1210;
    --sdb-07-surf: #121a18;
    --sdb-07-surf2: #18221f;
    --sdb-07-line: #26332f;
    --sdb-07-ink: #e9f1ee;
    --sdb-07-mut: #93a4a0;
    --sdb-07-acc: #62d9b8;
    --sdb-07-acc: oklch(82% 0.12 172);
    --sdb-07-acc-soft: #12302a;
  }
}

.sdb-07__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-07__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-07__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-07-line);
  background: var(--sdb-07-surf);
  color: var(--sdb-07-ink);
  cursor: pointer;
}

.sdb-07__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-07__theme-input:focus-visible + .sdb-07__theme-label {
  outline: 2px solid var(--sdb-07-acc);
  outline-offset: 2px;
}

.sdb-07__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-07__app {
  display: flex;
  min-inline-size: 0;
  min-block-size: 100vh;
  background: var(--sdb-07-surf);
}

.sdb-07__rail {
  flex: none;
  inline-size: var(--sdb-07-w-open);
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  border-inline-end: 1px solid var(--sdb-07-line);
  background: var(--sdb-07-surf2);
  transition: inline-size 200ms ease;
}

.sdb-07__app[data-sdb-07-collapsed="true"] .sdb-07__rail {
  inline-size: var(--sdb-07-w-rail);
}

.sdb-07__app[data-sdb-07-noanim] .sdb-07__rail {
  transition: none;
}

.sdb-07__rail-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 0.6rem;
  border-block-end: 1px solid var(--sdb-07-line);
}

.sdb-07__mark {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  background: var(--sdb-07-acc);
  color: var(--sdb-07-surf);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.06em;
}

.sdb-07__brand {
  margin: 0 auto 0 0;
  font-family: var(--sdb-07-font-display);
  font-size: 0.82rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  min-inline-size: 0;
  overflow: hidden;
}

.sdb-07__collapse {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: transparent;
  color: var(--sdb-07-ink);
  cursor: pointer;
}

.sdb-07__collapse svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-07__nav {
  padding: 0.4rem 0.35rem;
  min-inline-size: 0;
}

.sdb-07__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-07__link {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.6rem;
  color: var(--sdb-07-ink);
  text-decoration: none;
  font-size: 0.9rem;
  white-space: nowrap;
  min-inline-size: 0;
}

.sdb-07__ico {
  flex: none;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.72rem;
  color: var(--sdb-07-mut);
  inline-size: 1.5rem;
}

.sdb-07__link:hover {
  background: var(--sdb-07-surf);
}

.sdb-07__link[aria-current="page"] {
  background: var(--sdb-07-acc-soft);
  color: var(--sdb-07-acc);
  font-weight: 650;
}

.sdb-07__link[aria-current="page"] .sdb-07__ico {
  color: var(--sdb-07-acc);
}

.sdb-07__link:focus-visible,
.sdb-07__collapse:focus-visible {
  outline: 2px solid var(--sdb-07-acc);
  outline-offset: -2px;
}

.sdb-07__hideable {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sdb-07__app[data-sdb-07-collapsed="true"] .sdb-07__hideable {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-07__app[data-sdb-07-collapsed="true"] .sdb-07__brand {
  flex: none;
}
/* Collapsed rail is 68px, but the head row needs the 30px mark + 8px gap +
   44px button + 19px padding = ~101px, and both children are flex: none, so
   the button overflowed 32px past the rail edge. Stack the row instead:
   both stay centred, the button keeps its 44px target, and the brand mark
   stays visible so the collapsed rail still carries an identity. */

.sdb-07__app[data-sdb-07-collapsed="true"] .sdb-07__rail-head {
  flex-direction: column;
  gap: 0.25rem;
  padding: 0.4rem 0;
}

.sdb-07__app[data-sdb-07-collapsed="true"] .sdb-07__collapse {
  inline-size: 2.75rem;
}

.sdb-07__main {
  flex: 1;
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
  display: grid;
  gap: 1.2rem;
  align-content: start;
}

@media (min-width: 46rem) {
  .sdb-07__main {
    padding: 2.4rem 2.25rem 3rem;
  }
}

.sdb-07__kpis {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.75rem;
}

@media (min-width: 34rem) {
  .sdb-07__kpis {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.sdb-07__kpi {
  min-inline-size: 0;
  padding: 0.9rem 1rem;
  border: 1px solid var(--sdb-07-line);
}

.sdb-07__kpi-k {
  margin: 0 0 0.2rem;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--sdb-07-mut);
}

.sdb-07__kpi-v {
  margin: 0;
  font-family: var(--sdb-07-font-display);
  font-size: 1.45rem;
  font-variant-numeric: tabular-nums;
}

.sdb-07__chart {
  display: flex;
  align-items: flex-end;
  gap: 0.4rem;
  block-size: 12rem;
  padding: 0.8rem;
  border: 1px solid var(--sdb-07-line);
}

.sdb-07__chart span {
  flex: 1;
  min-inline-size: 0;
  block-size: calc(var(--sdb-07-h) * 1%);
  background: var(--sdb-07-acc);
  opacity: 0.75;
}

@media (max-width: 30rem) {
  .sdb-07__app {
    flex-direction: column;
  }

  .sdb-07__rail,
    .sdb-07__app[data-sdb-07-collapsed="true"] .sdb-07__rail {
    inline-size: 100%;
    border-inline-end: 0;
    border-block-end: 1px solid var(--sdb-07-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sdb-07__rail {
    transition: none;
  }
}
/* The theme toggle is pinned top-right of the demo root, and on narrow
   viewports the rail head reaches under it — the toggle then intercepts
   every click meant for the collapse button. Reserve the toggle its own
   lane. Must sit at the END of the block: the base rail-head rule has
   equal specificity and would otherwise win on source order. */

@media (max-width: 30rem) {
  .sdb-07__rail-head,
    .sdb-07__head {
    padding-inline-end: 3.4rem;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-07');
const app = root.querySelector('.sdb-07__app');
const btn = root.querySelector('#sdb-07-toggle');
const KEY = 'sdb-07:rail-collapsed';
const read = () => { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
const write = (v) => { try { localStorage.setItem(KEY, v); } catch (e) {} };
function paint(collapsed) {
  app.setAttribute('data-sdb-07-collapsed', String(collapsed));
  btn.setAttribute('aria-expanded', String(!collapsed));
  btn.querySelector('.sdb-07__sr').textContent = collapsed ? 'Expand sidebar' : 'Collapse sidebar';
}
// In production this runs as an inline script in <head> so the restored width is in the first frame.
app.setAttribute('data-sdb-07-noanim', '');
paint(read() === 'true');
requestAnimationFrame(() => app.removeAttribute('data-sdb-07-noanim'));
function toggle() {
  const collapsed = app.getAttribute('data-sdb-07-collapsed') !== 'true';
  write(String(collapsed));
  paint(collapsed);
}
btn.addEventListener('click', toggle);
root.__sdbCleanup = () => { btn.removeEventListener('click', toggle); };
```
