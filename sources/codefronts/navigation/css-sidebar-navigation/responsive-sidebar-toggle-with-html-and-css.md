---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/responsive-sidebar-toggle-with-html-and-css/"
title: "Responsive Sidebar Breakpoint Behavior"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "The point where a persistent sidebar has to become a modal drawer, and what changes at that line."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Sidebar Breakpoint Behavior
Source: https://codefronts.com/navigation/css-sidebar-navigation/responsive-sidebar-toggle-with-html-and-css/

The point where a persistent sidebar has to become a modal drawer, and what changes at that line. Below the breakpoint the focus trap switches on, inert starts applying, Esc starts closing, and the toggle's aria-expanded means something different &mdash; it now describes a modal, not a layout. Most implementations change the CSS and forget the behaviour. Resize the frame across 44rem and the contract changes with it.
## HTML
```html
<section class="sdb-12" aria-label="Orbit banking">
  <div class="sdb-12__theme">
    <input class="sdb-12__theme-input" type="checkbox" id="sdb-12-theme">
    <label class="sdb-12__theme-label" for="sdb-12-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-12__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-12__app" id="sdb-12-app" data-sdb-12-mode="persistent">
    <div class="sdb-12__content" id="sdb-12-content">
      <div class="sdb-12__bar">
        <button class="sdb-12__trigger" type="button" id="sdb-12-open" aria-expanded="false" aria-controls="sdb-12-rail">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-12__sr">Open navigation</span>
        </button>
        <p class="sdb-12__brand">Orbit</p>
        <a class="sdb-12__bar-link" href="#sdb-12-content">Help</a>
      </div>
      <div class="sdb-12__cards">
        <div class="sdb-12__card"><p class="sdb-12__card-k">Current account</p><p class="sdb-12__card-v">&euro;4,182.60</p></div>
        <div class="sdb-12__card"><p class="sdb-12__card-k">Savings</p><p class="sdb-12__card-v">&euro;16,400.00</p></div>
      </div>
      <ul class="sdb-12__tx">
        <li><span>Meridian Ltd</span><em>&minus;&euro;42.00</em></li>
        <li><span>Fern Studio</span><em>+&euro;1,250.00</em></li>
        <li><span>Basalt Hosting</span><em>&minus;&euro;18.00</em></li>
        <li><span>Kestrel Rail</span><em>&minus;&euro;64.40</em></li>
        <li><span>Slack Water Co</span><em>+&euro;320.00</em></li>
      </ul>
    </div>

    <div class="sdb-12__scrim" data-sdb-12-scrim hidden></div>

    <aside class="sdb-12__rail" id="sdb-12-rail" aria-labelledby="sdb-12-rail-h">
      <div class="sdb-12__rail-head">
        <p class="sdb-12__rail-h" id="sdb-12-rail-h">Accounts</p>
        <button class="sdb-12__close" type="button" data-sdb-12-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-12__sr">Close navigation</span>
        </button>
      </div>
      <nav class="sdb-12__nav" aria-label="Orbit accounts">
        <ul class="sdb-12__list">
          <li><a class="sdb-12__link" href="#sdb-12-content" aria-current="page">Overview</a></li>
          <li><a class="sdb-12__link" href="#sdb-12-content">Payments</a></li>
          <li><a class="sdb-12__link" href="#sdb-12-content">Standing orders</a></li>
          <li><a class="sdb-12__link" href="#sdb-12-content">Statements</a></li>
          <li><a class="sdb-12__link" href="#sdb-12-content">Team settings</a></li>
        </ul>
      </nav>
    </aside>
  </div>
</section>
```
## CSS
```css
.sdb-12 {
  --sdb-12-bg: #f4f1fb;
  --sdb-12-surf: #ffffff;
  --sdb-12-surf2: #ece7f9;
  --sdb-12-line: #d9d1f0;
  --sdb-12-ink: #1d1830;
  --sdb-12-mut: #625b80;
  --sdb-12-acc: #6b3fd4;
  --sdb-12-acc: oklch(52% 0.2 292);
  --sdb-12-acc-soft: #e6dcfb;
  --sdb-12-font-display: "SF Pro Display", "Segoe UI Variable", system-ui, -apple-system, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-12-bg);
  color: var(--sdb-12-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-12 *,
.sdb-12 *::before,
.sdb-12 *::after {
  box-sizing: border-box;
}

.sdb-12:has(.sdb-12__theme-input:checked) {
  --sdb-12-bg: #0d0a17;
  --sdb-12-surf: #151020;
  --sdb-12-surf2: #1d1730;
  --sdb-12-line: #2b2342;
  --sdb-12-ink: #ece8f8;
  --sdb-12-mut: #a099c0;
  --sdb-12-acc: #b394ff;
  --sdb-12-acc: oklch(80% 0.14 292);
  --sdb-12-acc-soft: #241c3c;
}

@media (prefers-color-scheme: dark) {
  .sdb-12 {
    --sdb-12-bg: #0d0a17;
    --sdb-12-surf: #151020;
    --sdb-12-surf2: #1d1730;
    --sdb-12-line: #2b2342;
    --sdb-12-ink: #ece8f8;
    --sdb-12-mut: #a099c0;
    --sdb-12-acc: #b394ff;
    --sdb-12-acc: oklch(80% 0.14 292);
    --sdb-12-acc-soft: #241c3c;
  }

  .sdb-12:has(.sdb-12__theme-input:checked) {
    --sdb-12-bg: #f4f1fb;
    --sdb-12-surf: #ffffff;
    --sdb-12-surf2: #ece7f9;
    --sdb-12-line: #d9d1f0;
    --sdb-12-ink: #1d1830;
    --sdb-12-mut: #625b80;
    --sdb-12-acc: #6b3fd4;
    --sdb-12-acc: oklch(52% 0.2 292);
    --sdb-12-acc-soft: #e6dcfb;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-12:has(.sdb-12__theme-input:checked) {
    --sdb-12-bg: #0d0a17;
    --sdb-12-surf: #151020;
    --sdb-12-surf2: #1d1730;
    --sdb-12-line: #2b2342;
    --sdb-12-ink: #ece8f8;
    --sdb-12-mut: #a099c0;
    --sdb-12-acc: #b394ff;
    --sdb-12-acc: oklch(80% 0.14 292);
    --sdb-12-acc-soft: #241c3c;
  }
}

.sdb-12__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-12__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-12__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.9rem;
  border: 1px solid var(--sdb-12-line);
  background: var(--sdb-12-surf);
  color: var(--sdb-12-ink);
  cursor: pointer;
  box-shadow: 0 0.3rem 0.8rem rgba(29, 24, 48, 0.14);
}

.sdb-12__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-12__theme-input:focus-visible + .sdb-12__theme-label {
  outline: 2px solid var(--sdb-12-acc);
  outline-offset: 2px;
}

.sdb-12__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-12__app {
  position: relative;
  overflow: hidden;
  display: flex;
  min-inline-size: 0;
  min-block-size: 100vh;
  background: var(--sdb-12-surf);
}

.sdb-12__content {
  flex: 1;
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
}

.sdb-12__content[inert] {
  opacity: 0.5;
}

.sdb-12__bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem 4.2rem 0.7rem 0.9rem;
  border-block-end: 1px solid var(--sdb-12-line);
}

.sdb-12__trigger {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.8rem;
  border: 0;
  background: var(--sdb-12-surf2);
  color: var(--sdb-12-ink);
  cursor: pointer;
}

.sdb-12__trigger svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-12__app[data-sdb-12-mode="persistent"] .sdb-12__trigger {
  display: none;
}

.sdb-12__brand {
  margin: 0 auto 0 0;
  font-family: var(--sdb-12-font-display);
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--sdb-12-acc);
}

.sdb-12__bar-link {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding-inline: 0.6rem;
  color: var(--sdb-12-mut);
  text-decoration: none;
  font-size: 0.86rem;
}

.sdb-12__cards {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.7rem;
  padding: 1rem 1rem 0.5rem;
}

.sdb-12__card {
  min-inline-size: 0;
  padding: 0.9rem 1rem;
  border-radius: 1rem;
  background: var(--sdb-12-surf2);
}

.sdb-12__card-k {
  margin: 0 0 0.2rem;
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--sdb-12-mut);
}

.sdb-12__card-v {
  margin: 0;
  font-family: var(--sdb-12-font-display);
  font-size: 1.25rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.sdb-12__tx {
  list-style: none;
  margin: 0;
  padding: 0.5rem 1rem 1.5rem;
  display: grid;
  gap: 0.35rem;
}

.sdb-12__tx li {
  display: flex;
  gap: 0.6rem;
  padding: 0.6rem 0.8rem;
  border-radius: 0.7rem;
  background: var(--sdb-12-surf2);
  font-size: 0.88rem;
  min-inline-size: 0;
}

.sdb-12__tx span {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.sdb-12__tx em {
  margin-inline-start: auto;
  font-style: normal;
  font-variant-numeric: tabular-nums;
  color: var(--sdb-12-mut);
}

.sdb-12__scrim {
  position: absolute;
  inset: 0;
  z-index: 20;
  background: rgba(20, 14, 38, 0.45);
}

.sdb-12__rail {
  flex: none;
  inline-size: 14rem;
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  background: var(--sdb-12-surf2);
  order: -1;
  border-inline-end: 1px solid var(--sdb-12-line);
}

.sdb-12__app[data-sdb-12-mode="modal"] .sdb-12__rail {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  z-index: 30;
  inline-size: min(15rem, 82%);
  transform: translateX(-100%);
  transition: transform 220ms cubic-bezier(0.22, 1, 0.36, 1);
  box-shadow: 0 0 2rem rgba(20, 14, 38, 0.4);
}

.sdb-12__app[data-sdb-12-mode="modal"][data-sdb-12-open="true"] .sdb-12__rail {
  transform: translateX(0);
}

.sdb-12__rail[hidden] {
  display: none;
}

.sdb-12__rail-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem;
}

.sdb-12__rail-h {
  margin: 0 auto 0 0;
  font-size: 0.74rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-12-mut);
}

.sdb-12__close {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.8rem;
  border: 0;
  background: var(--sdb-12-surf);
  color: var(--sdb-12-ink);
  cursor: pointer;
}

.sdb-12__close svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sdb-12__app[data-sdb-12-mode="persistent"] .sdb-12__close {
  display: none;
}

.sdb-12__nav {
  flex: 1;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 0.2rem 0.5rem 0.7rem;
}

.sdb-12__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.15rem;
}

.sdb-12__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border-radius: 0.7rem;
  color: var(--sdb-12-ink);
  text-decoration: none;
  font-size: 0.9rem;
  min-inline-size: 0;
}

.sdb-12__link:hover {
  background: var(--sdb-12-surf);
}

.sdb-12__link[aria-current="page"] {
  background: var(--sdb-12-acc);
  color: #fff;
  font-weight: 650;
}

.sdb-12:has(.sdb-12__theme-input:checked) .sdb-12__link[aria-current="page"] {
  color: #0d0a17;
}

.sdb-12__link:focus-visible,
.sdb-12__close:focus-visible,
.sdb-12__trigger:focus-visible,
.sdb-12__bar-link:focus-visible {
  outline: 2px solid var(--sdb-12-acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .sdb-12__app[data-sdb-12-mode="modal"] .sdb-12__rail {
    transition: transform 1ms linear;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-12');
const app = root.querySelector('#sdb-12-app');
const rail = root.querySelector('#sdb-12-rail');
const content = root.querySelector('#sdb-12-content');
const scrim = root.querySelector('[data-sdb-12-scrim]');
const trigger = root.querySelector('#sdb-12-open');
const supportsInert = 'inert' in HTMLElement.prototype;
// One source of truth for the mode: the stylesheet keys off data-sdb-12-mode, never its own copy of the breakpoint.
const mq = window.matchMedia('(min-width: 44rem)');
let open = false, returnTo = null;
const modal = () => !mq.matches;
function onKey(e) { if (e.key === 'Escape' && open) setOpen(false); }
function paint() {
  app.setAttribute('data-sdb-12-mode', modal() ? 'modal' : 'persistent');
  app.setAttribute('data-sdb-12-open', String(open));
  rail.hidden = modal() && !open;
  scrim.hidden = !(modal() && open);
  rail.setAttribute('role', modal() ? 'dialog' : 'complementary');
  if (modal()) rail.setAttribute('aria-modal', 'true'); else rail.removeAttribute('aria-modal');
  trigger.setAttribute('aria-expanded', String(modal() && open));
  const block = modal() && open;
  if (supportsInert) content.inert = block;
  else content.setAttribute('aria-hidden', String(block));
}
function setOpen(next) {
  open = next;
  if (next) { returnTo = document.activeElement; document.addEventListener('keydown', onKey); }
  else document.removeEventListener('keydown', onKey);
  paint();
  if (next) requestAnimationFrame(() => rail.querySelector('[data-sdb-12-close]').focus());
  else if (returnTo) { returnTo.focus({ preventScroll: true }); returnTo = null; }
}
function onModeChange() { if (open && !modal()) setOpen(false); else paint(); }
mq.addEventListener('change', onModeChange);
// matchMedia can read stale at parse time, so settle the mode after first layout too.
requestAnimationFrame(paint);
trigger.addEventListener('click', () => setOpen(true));
scrim.addEventListener('click', () => setOpen(false));
root.querySelectorAll('[data-sdb-12-close]').forEach((b) => b.addEventListener('click', () => setOpen(false)));
paint();
root.__sdbCleanup = () => { document.removeEventListener('keydown', onKey); mq.removeEventListener('change', onModeChange); };
```
