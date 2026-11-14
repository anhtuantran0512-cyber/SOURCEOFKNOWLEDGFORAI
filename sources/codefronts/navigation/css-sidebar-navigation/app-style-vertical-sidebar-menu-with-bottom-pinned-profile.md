---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/app-style-vertical-sidebar-menu-with-bottom-pinned-profile/"
title: "Sidebar Footer Pinning with Scrollable Nav"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "A footer pinned to the bottom of the rail while the nav list between header and footer scrolls on its own."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sidebar Footer Pinning with Scrollable Nav
Source: https://codefronts.com/navigation/css-sidebar-navigation/app-style-vertical-sidebar-menu-with-bottom-pinned-profile/

A footer pinned to the bottom of the rail while the nav list between header and footer scrolls on its own. The mechanic is a flex column with min-block-size: 0 on the scrolling child &mdash; without it the child's automatic minimum size lets it grow to its content, the whole rail gets taller, and the overflow never engages. The failure produces no error at all, which is what makes it expensive; this build is the corrected one.
## HTML
```html
<section class="sdb-20" aria-label="Orbit workspace">
  <div class="sdb-20__theme">
    <input class="sdb-20__theme-input" type="checkbox" id="sdb-20-theme">
    <label class="sdb-20__theme-label" for="sdb-20-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-20__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-20__app">
    <aside class="sdb-20__rail">
      <div class="sdb-20__rail-head"><p class="sdb-20__brand">Orbit</p></div>
      <nav class="sdb-20__nav" aria-label="Orbit workspace">
        <ul class="sdb-20__list">
          <li><a class="sdb-20__link" href="#sdb-20-main" aria-current="page">Overview</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Projects</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Deployments</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Team settings</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Audit log</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Billing</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">API keys</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Integrations</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Webhooks</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Regions</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Certificates</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Environments</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Secrets</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Usage</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Invoices</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Support</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Status</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Changelog</a></li>
          <li><a class="sdb-20__link" href="#sdb-20-main">Archive</a></li>
        </ul>
      </nav>
      <div class="sdb-20__foot">
        <span class="sdb-20__avatar" aria-hidden="true">JL</span>
        <span class="sdb-20__who"><b>Jordan Lee</b>Operations</span>
      </div>
    </aside>

    <main class="sdb-20__main" id="sdb-20-main">
      <h2 class="sdb-20__main-h">Overview</h2>
      <div class="sdb-20__cards">
        <div class="sdb-20__card"><p class="sdb-20__card-k">Open projects</p><p class="sdb-20__card-v">14</p></div>
        <div class="sdb-20__card"><p class="sdb-20__card-k">Deployments today</p><p class="sdb-20__card-v">9</p></div>
        <div class="sdb-20__card"><p class="sdb-20__card-k">Members</p><p class="sdb-20__card-v">38</p></div>
      </div>
      <ul class="sdb-20__rows">
        <li><span>northwind-api</span><em>Promoted 09:14</em></li>
        <li><span>ledger-web</span><em>Building</em></li>
        <li><span>fern-cms</span><em>Promoted 07:41</em></li>
        <li><span>talon-editor</span><em>Rolled back</em></li>
      </ul>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-20 {
  --sdb-20-bg: #f6f4ef;
  --sdb-20-surf: #fffdf9;
  --sdb-20-surf2: #ece7dd;
  --sdb-20-line: #d9d2c5;
  --sdb-20-ink: #1e1c18;
  --sdb-20-mut: #665f54;
  --sdb-20-acc: #2f4f7a;
  --sdb-20-acc: oklch(42% 0.1 250);
  --sdb-20-acc-soft: #dde5f0;
  --sdb-20-font-display: "Roboto Slab", Rockwell, "Bookman Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-20-bg);
  color: var(--sdb-20-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-20 *,
.sdb-20 *::before,
.sdb-20 *::after {
  box-sizing: border-box;
}

.sdb-20:has(.sdb-20__theme-input:checked) {
  --sdb-20-bg: #131210;
  --sdb-20-surf: #1a1916;
  --sdb-20-surf2: #221f1b;
  --sdb-20-line: #302c26;
  --sdb-20-ink: #efece5;
  --sdb-20-mut: #a29a8d;
  --sdb-20-acc: #93b4dd;
  --sdb-20-acc: oklch(78% 0.08 250);
  --sdb-20-acc-soft: #1c2635;
}

@media (prefers-color-scheme: dark) {
  .sdb-20 {
    --sdb-20-bg: #131210;
    --sdb-20-surf: #1a1916;
    --sdb-20-surf2: #221f1b;
    --sdb-20-line: #302c26;
    --sdb-20-ink: #efece5;
    --sdb-20-mut: #a29a8d;
    --sdb-20-acc: #93b4dd;
    --sdb-20-acc: oklch(78% 0.08 250);
    --sdb-20-acc-soft: #1c2635;
  }

  .sdb-20:has(.sdb-20__theme-input:checked) {
    --sdb-20-bg: #f6f4ef;
    --sdb-20-surf: #fffdf9;
    --sdb-20-surf2: #ece7dd;
    --sdb-20-line: #d9d2c5;
    --sdb-20-ink: #1e1c18;
    --sdb-20-mut: #665f54;
    --sdb-20-acc: #2f4f7a;
    --sdb-20-acc: oklch(42% 0.1 250);
    --sdb-20-acc-soft: #dde5f0;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-20:has(.sdb-20__theme-input:checked) {
    --sdb-20-bg: #131210;
    --sdb-20-surf: #1a1916;
    --sdb-20-surf2: #221f1b;
    --sdb-20-line: #302c26;
    --sdb-20-ink: #efece5;
    --sdb-20-mut: #a29a8d;
    --sdb-20-acc: #93b4dd;
    --sdb-20-acc: oklch(78% 0.08 250);
    --sdb-20-acc-soft: #1c2635;
  }
}

.sdb-20__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-20__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-20__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-20-line);
  background: var(--sdb-20-surf);
  color: var(--sdb-20-ink);
  cursor: pointer;
}

.sdb-20__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-20__theme-input:focus-visible + .sdb-20__theme-label {
  outline: 2px solid var(--sdb-20-acc);
  outline-offset: 2px;
}

.sdb-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-20__app {
  display: flex;
  min-inline-size: 0;
  block-size: 100vh;
  background: var(--sdb-20-surf);
}

.sdb-20__rail {
  flex: none;
  inline-size: 15rem;
  min-inline-size: 0;
  min-block-size: 0;
  display: flex;
  flex-direction: column;
  background: var(--sdb-20-surf2);
  border-inline-end: 1px solid var(--sdb-20-line);
}

.sdb-20__rail-head {
  padding: 0.9rem 1rem;
  border-block-end: 1px solid var(--sdb-20-line);
}

.sdb-20__brand {
  margin: 0;
  font-family: var(--sdb-20-font-display);
  font-size: 1.15rem;
  letter-spacing: -0.01em;
}
/* min-block-size: 0 is what lets flex: 1 hand this child a bounded height,
   so overflow engages and the footer below stays pinned. */

.sdb-20__nav {
  flex: 1;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  padding: 0.4rem 0.35rem;
}

.sdb-20__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-20__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.45rem 0.65rem;
  color: var(--sdb-20-ink);
  text-decoration: none;
  font-size: 0.9rem;
  min-inline-size: 0;
}

.sdb-20__link:hover {
  background: var(--sdb-20-surf);
}

.sdb-20__link[aria-current="page"] {
  background: var(--sdb-20-acc-soft);
  color: var(--sdb-20-acc);
  font-weight: 650;
  box-shadow: inset 3px 0 0 var(--sdb-20-acc);
}

.sdb-20__link:focus-visible {
  outline: 2px solid var(--sdb-20-acc);
  outline-offset: -2px;
}

.sdb-20__foot {
  flex: none;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.75rem 0.9rem;
  border-block-start: 1px solid var(--sdb-20-line);
}

.sdb-20__avatar {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 2.2rem;
  block-size: 2.2rem;
  background: var(--sdb-20-acc);
  color: var(--sdb-20-surf);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.04em;
}

.sdb-20__who {
  display: grid;
  min-inline-size: 0;
  font-size: 0.76rem;
  color: var(--sdb-20-mut);
}

.sdb-20__who b {
  font-size: 0.88rem;
  color: var(--sdb-20-ink);
  font-weight: 650;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.sdb-20__main {
  flex: 1;
  min-inline-size: 0;
  min-block-size: 0;
  overflow-y: auto;
  padding: 1.5rem 1.25rem 2.5rem;
}

@media (min-width: 46rem) {
  .sdb-20__main {
    padding: 2.4rem 2.25rem 3rem;
  }
}

.sdb-20__main-h {
  margin: 0 0 1.2rem;
  font-family: var(--sdb-20-font-display);
  font-size: clamp(1.45rem, 3.6vw, 2.1rem);
  line-height: 1.1;
}

.sdb-20__cards {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.75rem;
  margin-block-end: 1.2rem;
  max-inline-size: 46rem;
}

@media (min-width: 34rem) {
  .sdb-20__cards {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.sdb-20__card {
  min-inline-size: 0;
  padding: 0.9rem 1rem;
  border: 1px solid var(--sdb-20-line);
}

.sdb-20__card-k {
  margin: 0 0 0.2rem;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-20-mut);
}

.sdb-20__card-v {
  margin: 0;
  font-family: var(--sdb-20-font-display);
  font-size: 1.5rem;
  font-variant-numeric: tabular-nums;
}

.sdb-20__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
  background: var(--sdb-20-line);
  border: 1px solid var(--sdb-20-line);
  max-inline-size: 46rem;
}

.sdb-20__rows li {
  display: flex;
  gap: 0.7rem;
  padding: 0.7rem 0.9rem;
  background: var(--sdb-20-surf);
  font-size: 0.9rem;
  min-inline-size: 0;
}

.sdb-20__rows span {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.sdb-20__rows em {
  margin-inline-start: auto;
  font-style: normal;
  font-size: 0.82rem;
  color: var(--sdb-20-mut);
}

@media (max-width: 34rem) {
  .sdb-20__app {
    flex-direction: column;
    block-size: auto;
    min-block-size: 100vh;
  }

  .sdb-20__rail {
    inline-size: 100%;
    block-size: 60vh;
    border-inline-end: 0;
    border-block-end: 1px solid var(--sdb-20-line);
  }

  .sdb-20__main {
    overflow: visible;
  }
}
```
