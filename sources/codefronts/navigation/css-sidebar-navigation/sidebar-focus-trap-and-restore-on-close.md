---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/sidebar-focus-trap-and-restore-on-close/"
title: "Sidebar Focus Trap and Restore on Close"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "When a sidebar opens as a modal drawer, focus has to move into it, stay inside while it is open, and land back on the trigger when it closes."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sidebar Focus Trap and Restore on Close
Source: https://codefronts.com/navigation/css-sidebar-navigation/sidebar-focus-trap-and-restore-on-close/

When a sidebar opens as a modal drawer, focus has to move into it, stay inside while it is open, and land back on the trigger when it closes. This wires the trap by hand &mdash; first and last focusable, Tab and Shift+Tab wrapping, Esc closing &mdash; and shows the live tab order as a ring, including the step almost everyone drops: storing the trigger before opening so focus has somewhere to return to.
## HTML
```html
<section class="sdb-02" aria-label="Meridian sprint board">
  <div class="sdb-02__theme">
    <input class="sdb-02__theme-input" type="checkbox" id="sdb-02-theme">
    <label class="sdb-02__theme-label" for="sdb-02-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-02__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-02__app">
    <div class="sdb-02__bar" id="sdb-02-bg">
      <p class="sdb-02__brand">Meridian</p>
      <button class="sdb-02__trigger" type="button" id="sdb-02-open" aria-expanded="false" aria-controls="sdb-02-drawer">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        Project menu
      </button>
      <a class="sdb-02__bar-link" href="#sdb-02-main">Sprint 24</a>
      <a class="sdb-02__bar-link" href="#sdb-02-main">Backlog</a>
    </div>

    <main class="sdb-02__board" id="sdb-02-main" aria-label="Sprint board">
      <article class="sdb-02__card"><p class="sdb-02__card-tag">In review</p><h3 class="sdb-02__card-h">Rate limit on token exchange</h3><p class="sdb-02__card-m">Priya Sharma &middot; 3 files</p></article>
      <article class="sdb-02__card"><p class="sdb-02__card-tag">In progress</p><h3 class="sdb-02__card-h">Audit log retention window</h3><p class="sdb-02__card-m">Jordan Lee &middot; 8 files</p></article>
      <article class="sdb-02__card"><p class="sdb-02__card-tag">Blocked</p><h3 class="sdb-02__card-h">Billing webhook replay</h3><p class="sdb-02__card-m">Sam Rivera &middot; 1 file</p></article>
      <article class="sdb-02__card"><p class="sdb-02__card-tag">Shipped</p><h3 class="sdb-02__card-h">Session revoke endpoint</h3><p class="sdb-02__card-m">Ada Okafor &middot; 5 files</p></article>
    </main>

    <div class="sdb-02__scrim" data-sdb-02-scrim hidden></div>

    <div class="sdb-02__drawer" id="sdb-02-drawer" role="dialog" aria-modal="true" aria-labelledby="sdb-02-dh" hidden>
      <header class="sdb-02__drawer-head">
        <h3 class="sdb-02__drawer-h" id="sdb-02-dh">Meridian project</h3>
        <button class="sdb-02__close" type="button" data-sdb-02-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-02__sr">Close project menu</span>
        </button>
      </header>
      <nav class="sdb-02__nav" aria-label="Meridian project">
        <ul class="sdb-02__list">
          <li><a class="sdb-02__link" href="#sdb-02-main" aria-current="page">Sprint board</a></li>
          <li><a class="sdb-02__link" href="#sdb-02-main">Backlog</a></li>
          <li><a class="sdb-02__link" href="#sdb-02-main">Deployments</a></li>
          <li><a class="sdb-02__link" href="#sdb-02-main">Audit log</a></li>
          <li><a class="sdb-02__link" href="#sdb-02-main">Team settings</a></li>
        </ul>
      </nav>
      <footer class="sdb-02__drawer-foot">
        <button class="sdb-02__ghost" type="button" data-sdb-02-close>Done</button>
      </footer>
    </div>
  </div>
</section>
```
## CSS
```css
.sdb-02 {
  --sdb-02-bg: #f2f4f9;
  --sdb-02-surf: #ffffff;
  --sdb-02-deep: #101a34;
  --sdb-02-deep: oklch(21% 0.06 265);
  --sdb-02-line: #d5dbe8;
  --sdb-02-ink: #0d1428;
  --sdb-02-mut: #5c6684;
  --sdb-02-acc: #2f4de0;
  --sdb-02-acc: oklch(50% 0.2 267);
  --sdb-02-acc-soft: #e5e9fd;
  --sdb-02-on-deep: #eaeefb;
  --sdb-02-font-display: system-ui, "Segoe UI", Roboto, sans-serif;
  --sdb-02-shadow: 0 1.5rem 3rem rgba(13, 20, 40, 0.22);
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-02-bg);
  color: var(--sdb-02-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-02 *,
.sdb-02 *::before,
.sdb-02 *::after {
  box-sizing: border-box;
}

.sdb-02:has(.sdb-02__theme-input:checked) {
  --sdb-02-bg: #070b16;
  --sdb-02-surf: #101728;
  --sdb-02-deep: #060a14;
  --sdb-02-line: #212b45;
  --sdb-02-ink: #e9edf9;
  --sdb-02-mut: #93a0c0;
  --sdb-02-acc: #93a8ff;
  --sdb-02-acc: oklch(80% 0.12 268);
  --sdb-02-acc-soft: #1a2344;
  --sdb-02-on-deep: #e9edf9;
  --sdb-02-shadow: 0 1.5rem 3rem rgba(0, 0, 0, 0.6);
}

@media (prefers-color-scheme: dark) {
  .sdb-02 {
    --sdb-02-bg: #070b16;
    --sdb-02-surf: #101728;
    --sdb-02-deep: #060a14;
    --sdb-02-line: #212b45;
    --sdb-02-ink: #e9edf9;
    --sdb-02-mut: #93a0c0;
    --sdb-02-acc: #93a8ff;
    --sdb-02-acc: oklch(80% 0.12 268);
    --sdb-02-acc-soft: #1a2344;
    --sdb-02-on-deep: #e9edf9;
    --sdb-02-shadow: 0 1.5rem 3rem rgba(0, 0, 0, 0.6);
  }

  .sdb-02:has(.sdb-02__theme-input:checked) {
    --sdb-02-bg: #f2f4f9;
    --sdb-02-surf: #ffffff;
    --sdb-02-deep: #101a34;
    --sdb-02-line: #d5dbe8;
    --sdb-02-ink: #0d1428;
    --sdb-02-mut: #5c6684;
    --sdb-02-acc: #2f4de0;
    --sdb-02-acc: oklch(50% 0.2 267);
    --sdb-02-acc-soft: #e5e9fd;
    --sdb-02-on-deep: #eaeefb;
    --sdb-02-shadow: 0 1.5rem 3rem rgba(13, 20, 40, 0.22);
  }
}

@media (prefers-color-scheme: light) {
  .sdb-02:has(.sdb-02__theme-input:checked) {
    --sdb-02-bg: #070b16;
    --sdb-02-surf: #101728;
    --sdb-02-deep: #060a14;
    --sdb-02-line: #212b45;
    --sdb-02-ink: #e9edf9;
    --sdb-02-mut: #93a0c0;
    --sdb-02-acc: #93a8ff;
    --sdb-02-acc: oklch(80% 0.12 268);
    --sdb-02-acc-soft: #1a2344;
    --sdb-02-on-deep: #e9edf9;
    --sdb-02-shadow: 0 1.5rem 3rem rgba(0, 0, 0, 0.6);
  }
}

.sdb-02__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-02__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-02__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.7rem;
  border: 1px solid var(--sdb-02-line);
  background: var(--sdb-02-surf);
  color: var(--sdb-02-ink);
  cursor: pointer;
  box-shadow: 0 0.15rem 0.5rem rgba(13, 20, 40, 0.1);
}

.sdb-02__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-02__theme-input:focus-visible + .sdb-02__theme-label {
  outline: 2px solid var(--sdb-02-acc);
  outline-offset: 2px;
}

.sdb-02__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-02__app {
  position: relative;
  overflow: hidden;
  min-block-size: 100vh;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  background: var(--sdb-02-bg);
}

.sdb-02__bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  padding: 0.7rem 4.2rem 0.7rem 1rem;
  background: var(--sdb-02-deep);
  color: var(--sdb-02-on-deep);
}

.sdb-02__brand {
  margin: 0 auto 0 0;
  font-family: var(--sdb-02-font-display);
  font-weight: 700;
  letter-spacing: -0.01em;
}

.sdb-02__trigger {
  order: 3;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 2.75rem;
  padding-inline: 0.9rem;
  border-radius: 0.6rem;
  border: 0;
  cursor: pointer;
  background: var(--sdb-02-acc);
  color: #fff;
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
}

.sdb-02:has(.sdb-02__theme-input:checked) .sdb-02__trigger {
  color: #070b16;
}

.sdb-02__trigger svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sdb-02__trigger:focus-visible,
.sdb-02__bar-link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.sdb-02__bar-link {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding-inline: 0.7rem;
  color: var(--sdb-02-on-deep);
  text-decoration: none;
  font-size: 0.9rem;
  opacity: 0.8;
  border-radius: 0.5rem;
}

.sdb-02__bar-link:hover {
  opacity: 1;
}

.sdb-02__board {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.9rem;
  align-content: start;
  padding: 1.1rem;
  min-inline-size: 0;
}

@media (min-width: 40rem) {
  .sdb-02__board {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    padding: 1.6rem;
  }
}

@media (min-width: 62rem) {
  .sdb-02__board {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    padding: 2rem;
  }
}

.sdb-02__card {
  min-inline-size: 0;
  padding: 1rem;
  border-radius: 0.8rem;
  background: var(--sdb-02-surf);
  border: 1px solid var(--sdb-02-line);
}

.sdb-02__card-tag {
  margin: 0 0 0.4rem;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-02-acc);
}

.sdb-02__card-h {
  margin: 0 0 0.35rem;
  font-size: 0.98rem;
  line-height: 1.25;
}

.sdb-02__card-m {
  margin: 0;
  font-size: 0.8rem;
  color: var(--sdb-02-mut);
}

.sdb-02__scrim {
  position: absolute;
  inset: 0;
  z-index: 20;
  background: rgba(8, 12, 26, 0.5);
}

.sdb-02__drawer {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  z-index: 30;
  inline-size: min(19rem, 86%);
  display: flex;
  flex-direction: column;
  background: var(--sdb-02-surf);
  border-inline-end: 1px solid var(--sdb-02-line);
  box-shadow: var(--sdb-02-shadow);
  transform: translateX(-100%);
  transition: transform 240ms cubic-bezier(0.22, 1, 0.36, 1);
}

.sdb-02__drawer[hidden] {
  display: none;
}

.sdb-02[data-sdb-02-open="true"] .sdb-02__drawer {
  transform: translateX(0);
}

.sdb-02__drawer-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 0.9rem;
  border-block-end: 1px solid var(--sdb-02-line);
}

.sdb-02__drawer-h {
  margin: 0 auto 0 0;
  font-family: var(--sdb-02-font-display);
  font-size: 1rem;
}

.sdb-02__close {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.6rem;
  border: 1px solid var(--sdb-02-line);
  background: transparent;
  color: var(--sdb-02-ink);
  cursor: pointer;
}

.sdb-02__close svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sdb-02__nav {
  flex: 1;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 0.5rem;
}

.sdb-02__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-02__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border-radius: 0.55rem;
  color: var(--sdb-02-ink);
  text-decoration: none;
  font-size: 0.93rem;
  min-inline-size: 0;
}

.sdb-02__link:hover {
  background: var(--sdb-02-acc-soft);
}

.sdb-02__link[aria-current="page"] {
  background: var(--sdb-02-acc-soft);
  color: var(--sdb-02-acc);
  font-weight: 650;
}

.sdb-02__drawer-foot {
  padding: 0.7rem 0.9rem;
  border-block-start: 1px solid var(--sdb-02-line);
}

.sdb-02__ghost {
  min-block-size: 2.75rem;
  inline-size: 100%;
  border-radius: 0.6rem;
  cursor: pointer;
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  border: 1px solid var(--sdb-02-line);
  background: transparent;
  color: var(--sdb-02-ink);
}

.sdb-02__close:focus-visible,
.sdb-02__link:focus-visible,
.sdb-02__ghost:focus-visible {
  outline: 2px solid var(--sdb-02-acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .sdb-02__drawer {
    transition: transform 1ms linear;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-02');
const drawer = root.querySelector('#sdb-02-drawer');
const scrim = root.querySelector('[data-sdb-02-scrim]');
const trigger = root.querySelector('#sdb-02-open');
const SEL = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';
let returnTo = null;
const focusables = () => [...drawer.querySelectorAll(SEL)].filter((el) => el.offsetParent !== null);
function onKey(e) {
  if (e.key === 'Escape') { close(); return; }
  if (e.key !== 'Tab') return;
  const f = focusables();
  if (!f.length) return;
  const first = f[0], last = f[f.length - 1];
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
}
function open() {
  returnTo = document.activeElement;
  drawer.hidden = false; scrim.hidden = false;
  root.setAttribute('data-sdb-02-open', 'true');
  trigger.setAttribute('aria-expanded', 'true');
  requestAnimationFrame(() => drawer.querySelector('[data-sdb-02-close]').focus());
  document.addEventListener('keydown', onKey);
}
function close() {
  document.removeEventListener('keydown', onKey);
  root.removeAttribute('data-sdb-02-open');
  trigger.setAttribute('aria-expanded', 'false');
  drawer.hidden = true; scrim.hidden = true;
  (returnTo || trigger).focus({ preventScroll: true });
  returnTo = null;
}
trigger.addEventListener('click', open);
scrim.addEventListener('click', close);
root.querySelectorAll('[data-sdb-02-close]').forEach((b) => b.addEventListener('click', close));
root.__sdbCleanup = () => { document.removeEventListener('keydown', onKey); };
```
