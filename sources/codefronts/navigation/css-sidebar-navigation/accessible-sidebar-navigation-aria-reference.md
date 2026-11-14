---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/accessible-sidebar-navigation-aria-reference/"
title: "Accessible Sidebar Navigation ARIA Reference"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "The reference build the other nineteen demos borrow from."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Sidebar Navigation ARIA Reference
Source: https://codefronts.com/navigation/css-sidebar-navigation/accessible-sidebar-navigation-aria-reference/

The reference build the other nineteen demos borrow from. A <nav> with an accessible name, a real <ul> of links, aria-current="page" on the active item, and a disclosure control that carries its expanded state. The two mistakes seen most in review are the ones this markup is built to avoid: aria-selected borrowed from tabs, and aria-expanded parked on the sidebar rather than the control.
## HTML
```html
<section class="sdb-01" aria-label="Basalt developer console">
  <div class="sdb-01__theme">
    <input class="sdb-01__theme-input" type="checkbox" id="sdb-01-theme">
    <label class="sdb-01__theme-label" for="sdb-01-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-01__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-01__app">
    <nav class="sdb-01__nav" aria-label="Basalt documentation">
      <p class="sdb-01__brand">Basalt</p>
      <ul class="sdb-01__list">
        <li class="sdb-01__li"><a class="sdb-01__link" href="#sdb-01-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          Overview</a></li>
        <li class="sdb-01__li"><a class="sdb-01__link" href="#sdb-01-main" aria-current="page">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19V9l7-5 7 5v10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          Deployments</a></li>
        <li class="sdb-01__li"><a class="sdb-01__link" href="#sdb-01-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="7.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M12 8v8M8 12h8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          API keys <span class="sdb-01__count">4</span></a></li>
        <li class="sdb-01__li"><a class="sdb-01__link" href="#sdb-01-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 17V7l8-3 8 3v10l-8 3Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
          Environments</a></li>
      </ul>

      <details class="sdb-01__group" open>
        <summary class="sdb-01__summary" aria-controls="sdb-01-sublist">
          <svg class="sdb-01__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Team settings
        </summary>
        <ul class="sdb-01__sublist" id="sdb-01-sublist">
          <li class="sdb-01__li"><a class="sdb-01__link sdb-01__link--sub" href="#sdb-01-main">Members</a></li>
          <li class="sdb-01__li"><a class="sdb-01__link sdb-01__link--sub" href="#sdb-01-main">Audit log</a></li>
          <li class="sdb-01__li"><a class="sdb-01__link sdb-01__link--sub" href="#sdb-01-main">Billing</a></li>
        </ul>
      </details>
    </nav>

    <main class="sdb-01__main" id="sdb-01-main">
      <header class="sdb-01__bar">
        <p class="sdb-01__crumb">northwind-api / production</p>
        <h2 class="sdb-01__title">Deployments</h2>
      </header>

      <div class="sdb-01__panel">
        <table class="sdb-01__table">
          <thead><tr><th scope="col">Build</th><th scope="col">Commit</th><th scope="col">Duration</th><th scope="col">State</th></tr></thead>
          <tbody>
            <tr><td>#2481</td><td>a17f0c9</td><td>1m 42s</td><td><span class="sdb-01__pill">Live</span></td></tr>
            <tr><td>#2480</td><td>7b3d114</td><td>1m 39s</td><td>Rolled back</td></tr>
            <tr><td>#2479</td><td>0c92ae4</td><td>2m 04s</td><td>Superseded</td></tr>
            <tr><td>#2478</td><td>d4418f2</td><td>1m 51s</td><td>Superseded</td></tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-01 {
  --sdb-01-bg: #f3f5f8;
  --sdb-01-surf: #ffffff;
  --sdb-01-surf2: #e8ecf1;
  --sdb-01-line: #d2d8e0;
  --sdb-01-ink: #101419;
  --sdb-01-mut: #5a6472;
  --sdb-01-acc: #1b56d6;
  --sdb-01-acc: oklch(48% 0.19 264);
  --sdb-01-acc-soft: #e3eafd;
  --sdb-01-acc-soft: oklch(94% 0.03 264);
  --sdb-01-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-01-bg);
  color: var(--sdb-01-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-01 *,
.sdb-01 *::before,
.sdb-01 *::after {
  box-sizing: border-box;
}

.sdb-01:has(.sdb-01__theme-input:checked) {
  --sdb-01-bg: #0c1015;
  --sdb-01-surf: #141a21;
  --sdb-01-surf2: #1b222c;
  --sdb-01-line: #29323d;
  --sdb-01-ink: #eef1f5;
  --sdb-01-mut: #97a2b2;
  --sdb-01-acc: #8fa8ff;
  --sdb-01-acc: oklch(78% 0.13 267);
  --sdb-01-acc-soft: #1a2340;
  --sdb-01-acc-soft: oklch(30% 0.07 267);
}

@media (prefers-color-scheme: dark) {
  .sdb-01 {
    --sdb-01-bg: #0c1015;
    --sdb-01-surf: #141a21;
    --sdb-01-surf2: #1b222c;
    --sdb-01-line: #29323d;
    --sdb-01-ink: #eef1f5;
    --sdb-01-mut: #97a2b2;
    --sdb-01-acc: #8fa8ff;
    --sdb-01-acc: oklch(78% 0.13 267);
    --sdb-01-acc-soft: #1a2340;
    --sdb-01-acc-soft: oklch(30% 0.07 267);
  }

  .sdb-01:has(.sdb-01__theme-input:checked) {
    --sdb-01-bg: #f3f5f8;
    --sdb-01-surf: #ffffff;
    --sdb-01-surf2: #e8ecf1;
    --sdb-01-line: #d2d8e0;
    --sdb-01-ink: #101419;
    --sdb-01-mut: #5a6472;
    --sdb-01-acc: #1b56d6;
    --sdb-01-acc: oklch(48% 0.19 264);
    --sdb-01-acc-soft: #e3eafd;
    --sdb-01-acc-soft: oklch(94% 0.03 264);
  }
}

@media (prefers-color-scheme: light) {
  .sdb-01:has(.sdb-01__theme-input:checked) {
    --sdb-01-bg: #0c1015;
    --sdb-01-surf: #141a21;
    --sdb-01-surf2: #1b222c;
    --sdb-01-line: #29323d;
    --sdb-01-ink: #eef1f5;
    --sdb-01-mut: #97a2b2;
    --sdb-01-acc: #8fa8ff;
    --sdb-01-acc: oklch(78% 0.13 267);
    --sdb-01-acc-soft: #1a2340;
    --sdb-01-acc-soft: oklch(30% 0.07 267);
  }
}

.sdb-01__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-01__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-01__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-01-line);
  background: var(--sdb-01-surf);
  color: var(--sdb-01-ink);
  cursor: pointer;
}

.sdb-01__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-01__theme-input:focus-visible + .sdb-01__theme-label {
  outline: 2px solid var(--sdb-01-acc);
  outline-offset: 2px;
}

.sdb-01__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-01__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
}

@media (min-width: 48rem) {
  .sdb-01__app {
    grid-template-columns: 16.25rem minmax(0, 1fr);
  }
}

.sdb-01__nav {
  min-inline-size: 0;
  padding: 1rem 0.75rem;
  background: var(--sdb-01-surf);
  border-block-end: 1px solid var(--sdb-01-line);
}

@media (min-width: 48rem) {
  .sdb-01__nav {
    border-block-end: 0;
    border-inline-end: 1px solid var(--sdb-01-line);
  }
}

.sdb-01__brand {
  margin: 0 0 1rem;
  padding-inline: 0.7rem;
  font-family: var(--sdb-01-font-display);
  font-size: 0.82rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--sdb-01-mut);
}

.sdb-01__list,
.sdb-01__sublist {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-01__li {
  min-inline-size: 0;
}

.sdb-01__link {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.65rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  color: var(--sdb-01-ink);
  text-decoration: none;
  font-size: 0.92rem;
  border-inline-start: 2px solid transparent;
  min-inline-size: 0;
}

.sdb-01__link svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  flex: none;
  color: var(--sdb-01-mut);
}

.sdb-01__link:hover {
  background: var(--sdb-01-surf2);
}

.sdb-01__link:focus-visible {
  outline: 2px solid var(--sdb-01-acc);
  outline-offset: -2px;
}

.sdb-01__link[aria-current="page"] {
  background: var(--sdb-01-acc-soft);
  border-inline-start-color: var(--sdb-01-acc);
  color: var(--sdb-01-acc);
  font-weight: 600;
}

.sdb-01__link[aria-current="page"] svg {
  color: var(--sdb-01-acc);
}

.sdb-01__link--sub {
  padding-inline-start: 2.4rem;
  font-size: 0.88rem;
  color: var(--sdb-01-mut);
}

.sdb-01__count {
  margin-inline-start: auto;
  font-family: var(--sdb-01-font-display);
  font-size: 0.72rem;
  padding: 0.1rem 0.4rem;
  background: var(--sdb-01-surf2);
  color: var(--sdb-01-mut);
}

.sdb-01__group {
  margin-block-start: 0.6rem;
  border-block-start: 1px solid var(--sdb-01-line);
}

.sdb-01__summary {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.65rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  cursor: pointer;
  font-size: 0.92rem;
  font-weight: 600;
  list-style: none;
}

.sdb-01__summary::-webkit-details-marker {
  display: none;
}

.sdb-01__summary:focus-visible {
  outline: 2px solid var(--sdb-01-acc);
  outline-offset: -2px;
}

.sdb-01__chev {
  inline-size: 1rem;
  block-size: 1rem;
  flex: none;
  color: var(--sdb-01-mut);
  transition: transform 160ms ease;
}

.sdb-01__group[open] .sdb-01__chev {
  transform: rotate(90deg);
}

.sdb-01__main {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  align-content: start;
}

.sdb-01__bar {
  padding: 1.5rem 1.25rem 1.1rem;
  border-block-end: 1px solid var(--sdb-01-line);
}

@media (min-width: 48rem) {
  .sdb-01__bar {
    padding: 2rem 2.25rem 1.4rem;
  }
}

.sdb-01__crumb {
  margin: 0 0 0.35rem;
  font-family: var(--sdb-01-font-display);
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  color: var(--sdb-01-mut);
}

.sdb-01__title {
  margin: 0;
  font-size: clamp(1.35rem, 3.4vw, 1.9rem);
  line-height: 1.15;
  letter-spacing: -0.02em;
}

.sdb-01__panel {
  padding: 1.25rem;
  overflow-x: auto;
}

@media (min-width: 48rem) {
  .sdb-01__panel {
    padding: 1.75rem 2.25rem 2.5rem;
  }
}

.sdb-01__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  background: var(--sdb-01-surf);
  border: 1px solid var(--sdb-01-line);
}

.sdb-01__table th,
.sdb-01__table td {
  padding: 0.7rem 0.9rem;
  text-align: start;
  border-block-end: 1px solid var(--sdb-01-line);
  min-inline-size: 0;
}

.sdb-01__table th {
  font-family: var(--sdb-01-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sdb-01-mut);
  font-weight: 600;
}

.sdb-01__table td {
  font-family: var(--sdb-01-font-display);
  font-size: 0.82rem;
  color: var(--sdb-01-mut);
}

.sdb-01__table tbody tr:last-child td {
  border-block-end: 0;
}

.sdb-01__pill {
  display: inline-block;
  padding: 0.1rem 0.45rem;
  background: var(--sdb-01-acc-soft);
  color: var(--sdb-01-acc);
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .sdb-01__chev {
    transition: none;
  }
}
```
