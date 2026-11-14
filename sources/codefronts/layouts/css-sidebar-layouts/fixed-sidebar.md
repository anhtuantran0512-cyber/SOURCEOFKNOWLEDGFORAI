---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/fixed-sidebar/"
title: "CSS Fixed Sidebar Layout with Independent Scrollable Main Content"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The foundational app-shell every dashboard starts from — a locked left sidebar and a main pane that scrolls on its own — built the modern way: not…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Fixed Sidebar Layout with Independent Scrollable Main Content
Source: https://codefronts.com/layouts/css-sidebar-layouts/fixed-sidebar/

The foundational app-shell every dashboard starts from — a locked left sidebar and a main pane that scrolls on its own — built the modern way: not position:fixed with magic margins, but a height-constrained grid where each pane owns its own overflow. Scrollbars stay where they belong, nothing overlaps, and the pattern nests cleanly inside any container.
## HTML
```html
<section class="sbl-08">
  <aside class="sbl-08__rail" aria-label="Workspace">
    <div class="sbl-08__brand"><span aria-hidden="true"></span>Ledgerly</div>
    <nav class="sbl-08__nav">
      <a href="#" aria-current="page">Overview</a><a href="#">Transactions</a><a href="#">Invoices</a><a href="#">Recurring</a><a href="#">Vendors</a><a href="#">Categories</a><a href="#">Receipts</a><a href="#">Tax reports</a><a href="#">Bank feeds</a><a href="#">Rules</a><a href="#">Integrations</a><a href="#">Team</a><a href="#">Settings</a>
    </nav>
  </aside>
  <main class="sbl-08__main">
    <h1>Overview</h1>
    <p>Both panes scroll independently. The sidebar nav is intentionally long — scroll it, then scroll this pane; neither moves the other.</p>
    <div class="sbl-08__stack"><div></div><div></div><div></div><div></div><div></div><div></div></div>
  </main>
</section>
```
## CSS
```css
.sbl-08,
.sbl-08 *,
.sbl-08 *::before,
.sbl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-08 {
  --panel: oklch(0.17 0.015 235);
  --ink: oklch(0.93 0.005 235);
  --mut: oklch(0.63 0.012 235);
  --line: oklch(0.28 0.015 235);
  --accent: oklch(0.72 0.13 210);
  display: grid;
  grid-template-columns: 260px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.012 235);
  color: var(--ink);
}

.sbl-08__rail {
  display: flex;
  flex-direction: column;
  background: var(--panel);
  border-right: 1px solid var(--line);
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-width: thin;
  scrollbar-color: var(--line) transparent;
  padding: 20px 12px;
}

.sbl-08__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 15px/1 system-ui,sans-serif;
  padding: 2px 10px 18px;
}

.sbl-08__brand span {
  width: 24px;
  height: 24px;
  border-radius: 7px;
  background: conic-gradient(from 45deg,var(--accent),oklch(0.6 0.15 260));
}

.sbl-08__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-08__nav a {
  padding: 10px 14px;
  border-radius: 9px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .18s ease,color .18s ease;
}

.sbl-08__nav a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-08__nav a[aria-current="page"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 17%,transparent);
  box-shadow: inset 2px 0 0 var(--accent);
}

.sbl-08__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-08__main {
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  padding: 32px;
}

.sbl-08__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-08__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 52ch;
  margin-bottom: 24px;
  text-wrap: pretty;
}

.sbl-08__stack {
  display: grid;
  gap: 16px;
}

.sbl-08__stack div {
  height: 130px;
  border-radius: 14px;
  background: var(--panel);
  border: 1px solid var(--line);
}

@media (prefers-reduced-motion: reduce) {
  .sbl-08__nav a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a height-constrained grid shell; each pane owns overflow-y:auto + overscroll-behavior:contain, so scrolling never couples. */
```
