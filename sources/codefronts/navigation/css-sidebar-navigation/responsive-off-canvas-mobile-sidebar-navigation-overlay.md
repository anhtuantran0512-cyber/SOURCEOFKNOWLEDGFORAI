---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/responsive-off-canvas-mobile-sidebar-navigation-overlay/"
title: "Off Canvas Sidebar Drawer with Focus Return"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "The full modal-drawer contract from demos 02, 03 and 08 assembled in one place: focus moves in, focus is trapped, the background goes inert, Esc closes,…"
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Off Canvas Sidebar Drawer with Focus Return
Source: https://codefronts.com/navigation/css-sidebar-navigation/responsive-off-canvas-mobile-sidebar-navigation-overlay/

The full modal-drawer contract from demos 02, 03 and 08 assembled in one place: focus moves in, focus is trapped, the background goes inert, Esc closes, focus returns to the trigger, and scroll never chains to the page behind. css-hamburger-menus owns the trigger design; this is the behaviour it must open onto.
## HTML
```html
<section class="sdb-19" aria-label="Fern Daily">
  <div class="sdb-19__theme">
    <input class="sdb-19__theme-input" type="checkbox" id="sdb-19-theme">
    <label class="sdb-19__theme-label" for="sdb-19-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-19__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-19__screen" id="sdb-19-screen">
    <div class="sdb-19__page" id="sdb-19-page">
      <div class="sdb-19__bar">
        <button class="sdb-19__trigger" type="button" id="sdb-19-open" aria-expanded="false" aria-controls="sdb-19-drawer">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-19__sr">Open sections</span>
        </button>
        <p class="sdb-19__brand">Fern Daily</p>
      </div>
      <article class="sdb-19__article">
        <p class="sdb-19__eyebrow">Infrastructure</p>
        <h2 class="sdb-19__title">Regions added in the third quarter</h2>
        <p class="sdb-19__byline">Alex Chen &middot; 6 min read</p>
        <p class="sdb-19__body">Three new regions came online this quarter, each with an independent control plane and its own certificate authority.</p>
        <p class="sdb-19__body">Promotion remains a pointer move, so rollback stays instant even across regions. The verification step is the slow part, and it is deliberately manual.</p>
        <p class="sdb-19__body">Failover drills now run monthly per region, with an observer from a second team. The runbook lives in the handbook under Operations.</p>
        <a class="sdb-19__more" href="#sdb-19-screen">Read the full report</a>
      </article>
    </div>

    <div class="sdb-19__scrim" data-sdb-19-scrim hidden></div>

    <div class="sdb-19__drawer" id="sdb-19-drawer" role="dialog" aria-modal="true" aria-labelledby="sdb-19-dh" hidden>
      <div class="sdb-19__drawer-head">
        <p class="sdb-19__drawer-h" id="sdb-19-dh">Sections</p>
        <button class="sdb-19__close" type="button" data-sdb-19-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-19__sr">Close sections</span>
        </button>
      </div>
      <nav class="sdb-19__nav" aria-label="Fern Daily sections">
        <ul class="sdb-19__list">
          <li><a class="sdb-19__link" href="#sdb-19-screen" aria-current="page">Infrastructure</a></li>
          <li><a class="sdb-19__link" href="#sdb-19-screen">Security</a></li>
          <li><a class="sdb-19__link" href="#sdb-19-screen">Billing</a></li>
          <li><a class="sdb-19__link" href="#sdb-19-screen">Field notes</a></li>
          <li><a class="sdb-19__link" href="#sdb-19-screen">Audit log</a></li>
          <li><a class="sdb-19__link" href="#sdb-19-screen">Newsletters</a></li>
          <li><a class="sdb-19__link" href="#sdb-19-screen">Archive</a></li>
        </ul>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.sdb-19 {
  --sdb-19-bg: #1c1a18;
  --sdb-19-surf: #262320;
  --sdb-19-surf2: #302c28;
  --sdb-19-line: #3d3833;
  --sdb-19-ink: #f5efe8;
  --sdb-19-mut: #ab9f93;
  --sdb-19-acc: #ef7a52;
  --sdb-19-acc: oklch(70% 0.16 40);
  --sdb-19-acc-soft: #3a251c;
  --sdb-19-font-display: "Roboto Condensed", "Archivo Narrow", "Helvetica Neue", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-19-bg);
  color: var(--sdb-19-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-19 *,
.sdb-19 *::before,
.sdb-19 *::after {
  box-sizing: border-box;
}

.sdb-19:has(.sdb-19__theme-input:checked) {
  --sdb-19-bg: #f8f4ef;
  --sdb-19-surf: #ffffff;
  --sdb-19-surf2: #efe9e2;
  --sdb-19-line: #ded5cb;
  --sdb-19-ink: #221e1a;
  --sdb-19-mut: #6a6058;
  --sdb-19-acc: #9e3d18;
  --sdb-19-acc: oklch(48% 0.14 40);
  --sdb-19-acc-soft: #f6e2d8;
}

@media (prefers-color-scheme: light) {
  .sdb-19 {
    --sdb-19-bg: #f8f4ef;
    --sdb-19-surf: #ffffff;
    --sdb-19-surf2: #efe9e2;
    --sdb-19-line: #ded5cb;
    --sdb-19-ink: #221e1a;
    --sdb-19-mut: #6a6058;
    --sdb-19-acc: #9e3d18;
    --sdb-19-acc: oklch(48% 0.14 40);
    --sdb-19-acc-soft: #f6e2d8;
  }

  .sdb-19:has(.sdb-19__theme-input:checked) {
    --sdb-19-bg: #1c1a18;
    --sdb-19-surf: #262320;
    --sdb-19-surf2: #302c28;
    --sdb-19-line: #3d3833;
    --sdb-19-ink: #f5efe8;
    --sdb-19-mut: #ab9f93;
    --sdb-19-acc: #ef7a52;
    --sdb-19-acc: oklch(70% 0.16 40);
    --sdb-19-acc-soft: #3a251c;
  }
}

@media (prefers-color-scheme: dark) {
  .sdb-19:has(.sdb-19__theme-input:checked) {
    --sdb-19-bg: #f8f4ef;
    --sdb-19-surf: #ffffff;
    --sdb-19-surf2: #efe9e2;
    --sdb-19-line: #ded5cb;
    --sdb-19-ink: #221e1a;
    --sdb-19-mut: #6a6058;
    --sdb-19-acc: #9e3d18;
    --sdb-19-acc: oklch(48% 0.14 40);
    --sdb-19-acc-soft: #f6e2d8;
  }
}

.sdb-19__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-19__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-19__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.5rem;
  border: 1px solid var(--sdb-19-line);
  background: var(--sdb-19-surf);
  color: var(--sdb-19-ink);
  cursor: pointer;
  box-shadow: 0 0.4rem 1rem rgba(0, 0, 0, 0.25);
}

.sdb-19__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-19__theme-input:focus-visible + .sdb-19__theme-label {
  outline: 2px solid var(--sdb-19-acc);
  outline-offset: 2px;
}

.sdb-19__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-19__screen {
  position: relative;
  overflow: hidden;
  block-size: 100vh;
  background: var(--sdb-19-surf);
}

.sdb-19__page {
  display: flex;
  flex-direction: column;
  block-size: 100%;
}

.sdb-19__page[inert] {
  opacity: 0.4;
}

.sdb-19__bar {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.6rem 4.2rem 0.6rem 0.7rem;
  border-block-end: 1px solid var(--sdb-19-line);
}

.sdb-19__trigger {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.5rem;
  border: 0;
  background: var(--sdb-19-surf2);
  color: var(--sdb-19-ink);
  cursor: pointer;
}

.sdb-19__trigger svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.sdb-19__brand {
  margin: 0;
  font-family: var(--sdb-19-font-display);
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--sdb-19-acc);
}

.sdb-19__article {
  flex: 1;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 1.2rem 1.25rem 2.5rem;
}

@media (min-width: 46rem) {
  .sdb-19__article {
    padding: 2rem 2.25rem 3rem;
  }
}

.sdb-19__eyebrow {
  margin: 0 0 0.25rem;
  font-family: var(--sdb-19-font-display);
  font-size: 0.74rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--sdb-19-acc);
}

.sdb-19__title {
  margin: 0 0 0.3rem;
  font-family: var(--sdb-19-font-display);
  font-size: clamp(1.5rem, 4vw, 2.2rem);
  line-height: 1.08;
  max-inline-size: 34rem;
}

.sdb-19__byline {
  margin: 0 0 1rem;
  font-size: 0.82rem;
  color: var(--sdb-19-mut);
}

.sdb-19__body {
  margin: 0 0 0.8rem;
  font-size: 0.94rem;
  color: var(--sdb-19-mut);
  max-inline-size: 38rem;
  text-wrap: pretty;
}

.sdb-19__more {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  color: var(--sdb-19-acc);
  font-size: 0.9rem;
  font-weight: 650;
}

.sdb-19__more:focus-visible,
.sdb-19__trigger:focus-visible {
  outline: 2px solid var(--sdb-19-acc);
  outline-offset: 2px;
}

.sdb-19__scrim {
  position: absolute;
  inset: 0;
  z-index: 20;
  background: rgba(10, 8, 6, 0.5);
}

.sdb-19__drawer {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  z-index: 30;
  inline-size: min(15rem, 80%);
  display: flex;
  flex-direction: column;
  background: var(--sdb-19-surf);
  border-inline-end: 1px solid var(--sdb-19-line);
  box-shadow: 0.6rem 0 2rem rgba(0, 0, 0, 0.35);
  transform: translateX(-100%);
  transition: transform 260ms cubic-bezier(0.22, 1, 0.36, 1);
}

.sdb-19__drawer[hidden] {
  display: none;
}

.sdb-19[data-sdb-19-open="true"] .sdb-19__drawer {
  transform: translateX(0);
}

.sdb-19__drawer-head {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 0.6rem;
  border-block-end: 1px solid var(--sdb-19-line);
}

.sdb-19__drawer-h {
  margin: 0 auto 0 0;
  font-family: var(--sdb-19-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--sdb-19-mut);
}

.sdb-19__close {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.5rem;
  border: 0;
  background: var(--sdb-19-surf2);
  color: var(--sdb-19-ink);
  cursor: pointer;
}

.sdb-19__close svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sdb-19__nav {
  flex: 1;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 0.3rem;
}

.sdb-19__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-19__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.45rem 0.6rem;
  border-radius: 0.4rem;
  color: var(--sdb-19-ink);
  text-decoration: none;
  font-size: 0.89rem;
  min-inline-size: 0;
}

.sdb-19__link:hover {
  background: var(--sdb-19-surf2);
}

.sdb-19__link[aria-current="page"] {
  background: var(--sdb-19-acc-soft);
  color: var(--sdb-19-acc);
  font-weight: 650;
}

.sdb-19__link:focus-visible,
.sdb-19__close:focus-visible {
  outline: 2px solid var(--sdb-19-acc);
  outline-offset: -2px;
}

@media (prefers-reduced-motion: reduce) {
  .sdb-19__drawer {
    transition: transform 1ms linear;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-19');
const drawer = root.querySelector('#sdb-19-drawer');
const page = root.querySelector('#sdb-19-page');
const scrim = root.querySelector('[data-sdb-19-scrim]');
const trigger = root.querySelector('#sdb-19-open');
const supportsInert = 'inert' in HTMLElement.prototype;
const SEL = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';
const focusables = () => [...drawer.querySelectorAll(SEL)].filter((el) => el.offsetParent !== null);
let returnTo = null;
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
  drawer.hidden = scrim.hidden = false;
  root.setAttribute('data-sdb-19-open', 'true');
  trigger.setAttribute('aria-expanded', 'true');
  if (supportsInert) page.inert = true; else page.setAttribute('aria-hidden', 'true');
  document.addEventListener('keydown', onKey);
  requestAnimationFrame(() => drawer.querySelector('[data-sdb-19-close]').focus());
}
function close() {
  document.removeEventListener('keydown', onKey);
  if (supportsInert) page.inert = false; else page.removeAttribute('aria-hidden');
  root.removeAttribute('data-sdb-19-open');
  trigger.setAttribute('aria-expanded', 'false');
  drawer.hidden = scrim.hidden = true;
  (returnTo || trigger).focus({ preventScroll: true });
  returnTo = null;
}
trigger.addEventListener('click', open);
scrim.addEventListener('click', close);
root.querySelectorAll('[data-sdb-19-close]').forEach((b) => b.addEventListener('click', close));
root.__sdbCleanup = () => { document.removeEventListener('keydown', onKey); if (supportsInert) page.inert = false; };
```
