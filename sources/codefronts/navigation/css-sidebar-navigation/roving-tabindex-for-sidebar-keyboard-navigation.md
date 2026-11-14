---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/roving-tabindex-for-sidebar-keyboard-navigation/"
title: "Roving Tabindex for Sidebar Keyboard Navigation"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Whether arrow keys should move between sidebar items at all, and when."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Roving Tabindex for Sidebar Keyboard Navigation
Source: https://codefronts.com/navigation/css-sidebar-navigation/roving-tabindex-for-sidebar-keyboard-navigation/

Whether arrow keys should move between sidebar items at all, and when. For a plain navigation list the answer is usually no &mdash; links belong in the natural tab order and hijacking the arrows breaks what users expect from a page. For a long rail that genuinely behaves as one composite widget, roving tabindex turns fifty tab stops into one. The rail here takes the roving route: one tab stop, arrows and Home/End moving focus, activation only on Enter.
## HTML
```html
<section class="sdb-06" aria-label="Ranger file manager">
  <div class="sdb-06__theme">
    <input class="sdb-06__theme-input" type="checkbox" id="sdb-06-theme">
    <label class="sdb-06__theme-label" for="sdb-06-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-06__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-06__app">
    <nav class="sdb-06__rail" aria-label="Ranger folders">
      <p class="sdb-06__rail-title">All folders</p>
      <ul class="sdb-06__list" id="sdb-06-roving">
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="0" aria-current="page">Deployments</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Design source</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Contracts 2026</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Audit exports</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Vendor invoices</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Brand assets</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Field photos</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Board minutes</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Payroll archive</a></li>
        <li><a class="sdb-06__link" href="#sdb-06-main" tabindex="-1">Trash</a></li>
      </ul>
    </nav>

    <main class="sdb-06__main" id="sdb-06-main">
      <h2 class="sdb-06__title">Deployments</h2>
      <p class="sdb-06__sub">42 items &middot; last change 2 hours ago</p>
      <table class="sdb-06__table">
        <thead><tr><th scope="col">Name</th><th scope="col">Owner</th><th scope="col">Size</th></tr></thead>
        <tbody>
          <tr><td>release-notes.md</td><td>Priya Sharma</td><td>18 KB</td></tr>
          <tr><td>rollback-runbook.pdf</td><td>Jordan Lee</td><td>1.2 MB</td></tr>
          <tr><td>env-matrix.csv</td><td>Sam Rivera</td><td>44 KB</td></tr>
          <tr><td>token-exchange.log</td><td>Ada Okafor</td><td>7.8 MB</td></tr>
          <tr><td>staging-snapshot.zip</td><td>Tomas Vidal</td><td>212 MB</td></tr>
        </tbody>
      </table>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-06 {
  --sdb-06-bg: #eef1ea;
  --sdb-06-surf: #f8faf5;
  --sdb-06-surf2: #e3e8db;
  --sdb-06-line: #c8d1bd;
  --sdb-06-ink: #1b2118;
  --sdb-06-mut: #5b6653;
  --sdb-06-acc: #2f6b45;
  --sdb-06-acc: oklch(46% 0.1 155);
  --sdb-06-acc-soft: #d9e8dd;
  --sdb-06-font-display: Optima, "Gill Sans", "Gill Sans MT", Candara, "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-06-bg);
  color: var(--sdb-06-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-06 *,
.sdb-06 *::before,
.sdb-06 *::after {
  box-sizing: border-box;
}

.sdb-06:has(.sdb-06__theme-input:checked) {
  --sdb-06-bg: #0f1310;
  --sdb-06-surf: #161c16;
  --sdb-06-surf2: #1e251d;
  --sdb-06-line: #2d372b;
  --sdb-06-ink: #eaf0e6;
  --sdb-06-mut: #9aa694;
  --sdb-06-acc: #8fd2a8;
  --sdb-06-acc: oklch(82% 0.11 155);
  --sdb-06-acc-soft: #1d2c22;
}

@media (prefers-color-scheme: dark) {
  .sdb-06 {
    --sdb-06-bg: #0f1310;
    --sdb-06-surf: #161c16;
    --sdb-06-surf2: #1e251d;
    --sdb-06-line: #2d372b;
    --sdb-06-ink: #eaf0e6;
    --sdb-06-mut: #9aa694;
    --sdb-06-acc: #8fd2a8;
    --sdb-06-acc: oklch(82% 0.11 155);
    --sdb-06-acc-soft: #1d2c22;
  }

  .sdb-06:has(.sdb-06__theme-input:checked) {
    --sdb-06-bg: #eef1ea;
    --sdb-06-surf: #f8faf5;
    --sdb-06-surf2: #e3e8db;
    --sdb-06-line: #c8d1bd;
    --sdb-06-ink: #1b2118;
    --sdb-06-mut: #5b6653;
    --sdb-06-acc: #2f6b45;
    --sdb-06-acc: oklch(46% 0.1 155);
    --sdb-06-acc-soft: #d9e8dd;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-06:has(.sdb-06__theme-input:checked) {
    --sdb-06-bg: #0f1310;
    --sdb-06-surf: #161c16;
    --sdb-06-surf2: #1e251d;
    --sdb-06-line: #2d372b;
    --sdb-06-ink: #eaf0e6;
    --sdb-06-mut: #9aa694;
    --sdb-06-acc: #8fd2a8;
    --sdb-06-acc: oklch(82% 0.11 155);
    --sdb-06-acc-soft: #1d2c22;
  }
}

.sdb-06__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-06__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-06__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.4rem;
  border: 1px solid var(--sdb-06-line);
  background: var(--sdb-06-surf);
  box-shadow: inset 0 1px 3px rgba(27, 33, 24, 0.14);
  color: var(--sdb-06-ink);
  cursor: pointer;
}

.sdb-06__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-06__theme-input:focus-visible + .sdb-06__theme-label {
  outline: 2px solid var(--sdb-06-acc);
  outline-offset: 2px;
}

.sdb-06__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-06__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
}

@media (min-width: 46rem) {
  .sdb-06__app {
    grid-template-columns: 17rem minmax(0, 1fr);
  }
}

.sdb-06__rail {
  min-inline-size: 0;
  padding: 1rem 0.75rem;
  background: var(--sdb-06-surf);
  border-block-end: 1px solid var(--sdb-06-line);
  box-shadow: inset 0 2px 6px rgba(27, 33, 24, 0.09);
}

@media (min-width: 46rem) {
  .sdb-06__rail {
    border-block-end: 0;
    border-inline-end: 1px solid var(--sdb-06-line);
  }
}

.sdb-06__rail-title {
  margin: 0 0 0.5rem;
  padding-inline: 0.7rem;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-06-mut);
}

.sdb-06__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.sdb-06__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border-radius: 0.3rem;
  color: var(--sdb-06-ink);
  text-decoration: none;
  font-size: 0.93rem;
  min-inline-size: 0;
}

.sdb-06__link:hover {
  background: var(--sdb-06-surf2);
}

.sdb-06__link:focus-visible {
  outline: 2px solid var(--sdb-06-acc);
  outline-offset: -2px;
  background: var(--sdb-06-acc-soft);
}

.sdb-06__link[aria-current="page"] {
  background: var(--sdb-06-acc-soft);
  color: var(--sdb-06-acc);
  font-weight: 650;
}

.sdb-06__main {
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
  align-content: start;
}

@media (min-width: 46rem) {
  .sdb-06__main {
    padding: 2.4rem 2.25rem 3rem;
  }
}

.sdb-06__title {
  margin: 0 0 0.2rem;
  font-family: var(--sdb-06-font-display);
  font-size: clamp(1.4rem, 3.6vw, 2rem);
  line-height: 1.1;
}

.sdb-06__sub {
  margin: 0 0 1.3rem;
  font-size: 0.88rem;
  color: var(--sdb-06-mut);
}

.sdb-06__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  background: var(--sdb-06-surf);
  border: 1px solid var(--sdb-06-line);
  border-radius: 0.5rem;
  overflow: hidden;
}

.sdb-06__table th,
.sdb-06__table td {
  padding: 0.7rem 0.9rem;
  text-align: start;
  border-block-end: 1px solid var(--sdb-06-line);
  min-inline-size: 0;
}

.sdb-06__table th {
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-06-mut);
  font-weight: 700;
}

.sdb-06__table tbody tr:last-child td {
  border-block-end: 0;
}

.sdb-06__table td:last-child {
  color: var(--sdb-06-mut);
  font-variant-numeric: tabular-nums;
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-06');
const rail = root.querySelector('#sdb-06-roving');
const items = [...rail.querySelectorAll('.sdb-06__link')];
let index = Math.max(0, items.findIndex((a) => a.hasAttribute('aria-current')));
function move(next) {
  index = Math.min(items.length - 1, Math.max(0, next));
  items.forEach((a, i) => a.setAttribute('tabindex', i === index ? '0' : '-1'));
  items[index].focus();
}
function onKey(e) {
  const map = { ArrowDown: index + 1, ArrowUp: index - 1, Home: 0, End: items.length - 1 };
  if (!(e.key in map)) return;
  e.preventDefault();
  move(map[e.key]);
}
function onFocus(e) { const i = items.indexOf(e.target); if (i > -1) index = i; }
rail.addEventListener('keydown', onKey);
rail.addEventListener('focusin', onFocus);
root.__sdbCleanup = () => { rail.removeEventListener('keydown', onKey); rail.removeEventListener('focusin', onFocus); };
```
