---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/inert-background-content-behind-a-drawer/"
title: "Inert Background Content Behind a Drawer"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "A focus trap stops Tab from leaving, but the page behind an open drawer is still clickable and still reachable by a screen reader's virtual cursor."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inert Background Content Behind a Drawer
Source: https://codefronts.com/navigation/css-sidebar-navigation/inert-background-content-behind-a-drawer/

A focus trap stops Tab from leaving, but the page behind an open drawer is still clickable and still reachable by a screen reader's virtual cursor. The inert attribute removes a whole subtree from the accessibility tree and from hit-testing in one declaration &mdash; the same thing <dialog>'s showModal() does internally. It goes on with the drawer and comes off when the drawer closes, with a detected fallback for engines that do not have it.
## HTML
```html
<section class="sdb-03" aria-label="Sable order desk">
  <div class="sdb-03__theme">
    <input class="sdb-03__theme-input" type="checkbox" id="sdb-03-theme">
    <label class="sdb-03__theme-label" for="sdb-03-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-03__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-03__app">
    <div class="sdb-03__content" id="sdb-03-content">
      <div class="sdb-03__bar">
        <p class="sdb-03__brand">Sable &mdash; order desk</p>
        <a class="sdb-03__bar-link" href="#sdb-03-content">Fulfilment</a>
        <a class="sdb-03__bar-link" href="#sdb-03-content">Returns</a>
        <button class="sdb-03__btn" type="button" id="sdb-03-open" aria-expanded="false" aria-controls="sdb-03-drawer">Filters</button>
      </div>
      <table class="sdb-03__table">
        <thead><tr><th scope="col">Order</th><th scope="col">Customer</th><th scope="col">State</th><th scope="col"></th></tr></thead>
        <tbody>
          <tr><td>SB-4417</td><td>Priya Sharma</td><td>Packing</td><td><a class="sdb-03__row-link" href="#sdb-03-content">Open</a></td></tr>
          <tr><td>SB-4418</td><td>Jordan Lee</td><td>Awaiting stock</td><td><a class="sdb-03__row-link" href="#sdb-03-content">Open</a></td></tr>
          <tr><td>SB-4421</td><td>Sam Rivera</td><td>Ready to ship</td><td><a class="sdb-03__row-link" href="#sdb-03-content">Open</a></td></tr>
          <tr><td>SB-4423</td><td>Ada Okafor</td><td>Packing</td><td><a class="sdb-03__row-link" href="#sdb-03-content">Open</a></td></tr>
          <tr><td>SB-4425</td><td>Tomas Vidal</td><td>Awaiting stock</td><td><a class="sdb-03__row-link" href="#sdb-03-content">Open</a></td></tr>
        </tbody>
      </table>
    </div>

    <div class="sdb-03__scrim" data-sdb-03-scrim hidden></div>

    <aside class="sdb-03__drawer" id="sdb-03-drawer" role="dialog" aria-modal="true" aria-labelledby="sdb-03-dh" hidden>
      <header class="sdb-03__drawer-head">
        <h3 class="sdb-03__drawer-h" id="sdb-03-dh">Filters</h3>
        <button class="sdb-03__close" type="button" data-sdb-03-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-03__sr">Close filters</span>
        </button>
      </header>
      <nav class="sdb-03__nav" aria-label="Order views">
        <ul class="sdb-03__list">
          <li><a class="sdb-03__link" href="#sdb-03-content" aria-current="page">All open orders</a></li>
          <li><a class="sdb-03__link" href="#sdb-03-content">Awaiting stock</a></li>
          <li><a class="sdb-03__link" href="#sdb-03-content">Ready to ship</a></li>
          <li><a class="sdb-03__link" href="#sdb-03-content">Returns queue</a></li>
          <li><a class="sdb-03__link" href="#sdb-03-content">Archived</a></li>
        </ul>
      </nav>
    </aside>
  </div>
</section>
```
## CSS
```css
.sdb-03 {
  --sdb-03-bg: #f6f1e8;
  --sdb-03-surf: #fffdf9;
  --sdb-03-surf2: #efe7da;
  --sdb-03-line: #ddd1bd;
  --sdb-03-ink: #23201a;
  --sdb-03-mut: #6d6455;
  --sdb-03-acc: #8a4b1f;
  --sdb-03-acc: oklch(48% 0.12 52);
  --sdb-03-acc-soft: #f2e4d5;
  --sdb-03-font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-03-bg);
  color: var(--sdb-03-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-03 *,
.sdb-03 *::before,
.sdb-03 *::after {
  box-sizing: border-box;
}

.sdb-03:has(.sdb-03__theme-input:checked) {
  --sdb-03-bg: #17140f;
  --sdb-03-surf: #1f1b15;
  --sdb-03-surf2: #292319;
  --sdb-03-line: #3a3226;
  --sdb-03-ink: #f2ece1;
  --sdb-03-mut: #a89b87;
  --sdb-03-acc: #e6a06a;
  --sdb-03-acc: oklch(78% 0.11 55);
  --sdb-03-acc-soft: #35291d;
}

@media (prefers-color-scheme: dark) {
  .sdb-03 {
    --sdb-03-bg: #17140f;
    --sdb-03-surf: #1f1b15;
    --sdb-03-surf2: #292319;
    --sdb-03-line: #3a3226;
    --sdb-03-ink: #f2ece1;
    --sdb-03-mut: #a89b87;
    --sdb-03-acc: #e6a06a;
    --sdb-03-acc: oklch(78% 0.11 55);
    --sdb-03-acc-soft: #35291d;
  }

  .sdb-03:has(.sdb-03__theme-input:checked) {
    --sdb-03-bg: #f6f1e8;
    --sdb-03-surf: #fffdf9;
    --sdb-03-surf2: #efe7da;
    --sdb-03-line: #ddd1bd;
    --sdb-03-ink: #23201a;
    --sdb-03-mut: #6d6455;
    --sdb-03-acc: #8a4b1f;
    --sdb-03-acc: oklch(48% 0.12 52);
    --sdb-03-acc-soft: #f2e4d5;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-03:has(.sdb-03__theme-input:checked) {
    --sdb-03-bg: #17140f;
    --sdb-03-surf: #1f1b15;
    --sdb-03-surf2: #292319;
    --sdb-03-line: #3a3226;
    --sdb-03-ink: #f2ece1;
    --sdb-03-mut: #a89b87;
    --sdb-03-acc: #e6a06a;
    --sdb-03-acc: oklch(78% 0.11 55);
    --sdb-03-acc-soft: #35291d;
  }
}

.sdb-03__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-03__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-03__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 50%;
  border: 1px solid var(--sdb-03-line);
  background: var(--sdb-03-surf);
  color: var(--sdb-03-ink);
  cursor: pointer;
}

.sdb-03__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-03__theme-input:focus-visible + .sdb-03__theme-label {
  outline: 2px solid var(--sdb-03-acc);
  outline-offset: 2px;
}

.sdb-03__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-03__app {
  position: relative;
  overflow: hidden;
  min-block-size: 100vh;
  background: var(--sdb-03-surf);
}

.sdb-03__content {
  min-inline-size: 0;
}

.sdb-03__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem;
  padding: 0.6rem 4.2rem 0.6rem 1rem;
  border-block-end: 1px solid var(--sdb-03-line);
  background: var(--sdb-03-surf2);
}

.sdb-03__brand {
  margin: 0 auto 0 0;
  font-family: var(--sdb-03-font-display);
  font-size: 1.05rem;
}

.sdb-03__bar-link,
.sdb-03__row-link {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding-inline: 0.6rem;
  color: var(--sdb-03-acc);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 600;
}

.sdb-03__bar-link:hover,
.sdb-03__row-link:hover {
  text-decoration: underline;
}

.sdb-03__bar-link:focus-visible,
.sdb-03__row-link:focus-visible {
  outline: 2px solid var(--sdb-03-acc);
  outline-offset: 2px;
}

.sdb-03__btn {
  min-block-size: 2.75rem;
  padding-inline: 1rem;
  cursor: pointer;
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  border: 1px solid var(--sdb-03-acc);
  background: var(--sdb-03-acc);
  color: var(--sdb-03-surf);
}

.sdb-03__btn:focus-visible {
  outline: 2px solid var(--sdb-03-ink);
  outline-offset: 2px;
}

.sdb-03__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.sdb-03__table th,
.sdb-03__table td {
  padding: 0.75rem 1rem;
  text-align: start;
  border-block-end: 1px solid var(--sdb-03-line);
  min-inline-size: 0;
}

.sdb-03__table th {
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--sdb-03-mut);
  font-weight: 600;
}

.sdb-03__content[inert] {
  opacity: 0.45;
}

.sdb-03__scrim {
  position: absolute;
  inset: 0;
  z-index: 20;
  background: rgba(35, 32, 26, 0.42);
}

.sdb-03__drawer {
  position: absolute;
  inset-block: 0;
  inset-inline-end: 0;
  z-index: 30;
  inline-size: min(18rem, 84%);
  display: flex;
  flex-direction: column;
  background: var(--sdb-03-surf);
  border-inline-start: 1px solid var(--sdb-03-line);
  transform: translateX(100%);
  transition: transform 220ms ease-out;
}

.sdb-03__drawer[hidden] {
  display: none;
}

.sdb-03[data-sdb-03-open="true"] .sdb-03__drawer {
  transform: translateX(0);
}

.sdb-03__drawer-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem 0.8rem;
  border-block-end: 1px solid var(--sdb-03-line);
}

.sdb-03__drawer-h {
  margin: 0 auto 0 0;
  font-family: var(--sdb-03-font-display);
  font-size: 1.1rem;
}

.sdb-03__close {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-03-line);
  background: transparent;
  color: var(--sdb-03-ink);
  cursor: pointer;
}

.sdb-03__close svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sdb-03__nav {
  flex: 1;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
}

.sdb-03__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-03__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.8rem;
  color: var(--sdb-03-ink);
  text-decoration: none;
  font-size: 0.9rem;
  min-inline-size: 0;
  border-block-end: 1px solid var(--sdb-03-line);
}

.sdb-03__link:hover {
  background: var(--sdb-03-surf2);
}

.sdb-03__link[aria-current="page"] {
  background: var(--sdb-03-acc-soft);
  color: var(--sdb-03-acc);
  font-weight: 650;
}

.sdb-03__close:focus-visible,
.sdb-03__link:focus-visible {
  outline: 2px solid var(--sdb-03-acc);
  outline-offset: -2px;
}

@media (prefers-reduced-motion: reduce) {
  .sdb-03__drawer {
    transition: transform 1ms linear;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-03');
const drawer = root.querySelector('#sdb-03-drawer');
const scrim = root.querySelector('[data-sdb-03-scrim]');
const content = root.querySelector('#sdb-03-content');
const openBtn = root.querySelector('#sdb-03-open');
const supported = 'inert' in HTMLElement.prototype;
const behind = () => [...content.querySelectorAll('a[href], button:not([disabled])')];
let returnTo = null;
function block(on) {
  if (supported) { content.inert = on; return; }
  content.setAttribute('aria-hidden', String(on));
  behind().forEach((el) => on ? el.setAttribute('tabindex', '-1') : el.removeAttribute('tabindex'));
}
function onKey(e) { if (e.key === 'Escape') setOpen(false); }
function setOpen(next) {
  if (next) returnTo = document.activeElement;
  drawer.hidden = scrim.hidden = !next;
  root.setAttribute('data-sdb-03-open', String(next));
  openBtn.setAttribute('aria-expanded', String(next));
  block(next);
  if (next) { document.addEventListener('keydown', onKey); requestAnimationFrame(() => drawer.querySelector('[data-sdb-03-close]').focus()); }
  else { document.removeEventListener('keydown', onKey); (returnTo || openBtn).focus({ preventScroll: true }); }
}
openBtn.addEventListener('click', () => setOpen(true));
scrim.addEventListener('click', () => setOpen(false));
root.querySelectorAll('[data-sdb-03-close]').forEach((b) => b.addEventListener('click', () => setOpen(false)));
root.__sdbCleanup = () => { document.removeEventListener('keydown', onKey); };
```
