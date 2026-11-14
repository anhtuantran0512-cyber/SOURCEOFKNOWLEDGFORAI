---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/section-grouped-nav/"
title: "Section-Grouped Sidebar Navigation Menu with Header Labels"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "How large admin tools stay navigable: links organized under quiet uppercase group labels — the typographic system (size, tracking, color, spacing rhythm)…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Section-Grouped Sidebar Navigation Menu with Header Labels
Source: https://codefronts.com/layouts/css-sidebar-layouts/section-grouped-nav/

How large admin tools stay navigable: links organized under quiet uppercase group labels — the typographic system (size, tracking, color, spacing rhythm) that makes 25 links scan like 5 groups. The groups are semantic lists with real headings, so screen reader users get the same wayfinding the type provides visually.
## HTML
```html
<section class="sbl-22">
  <aside class="sbl-22__rail" aria-label="Admin">
    <div class="sbl-22__brand"><span aria-hidden="true"></span>Control Plane</div>
    <section class="sbl-22__grp" aria-labelledby="sbl22-g1">
      <h2 id="sbl22-g1">Provisioning</h2>
      <ul><li><a href="#" aria-current="page">Clusters <span>8</span></a></li><li><a href="#">Node pools</a></li><li><a href="#">Volumes <span>42</span></a></li><li><a href="#">Snapshots</a></li></ul>
    </section>
    <section class="sbl-22__grp" aria-labelledby="sbl22-g2">
      <h2 id="sbl22-g2">Networking</h2>
      <ul><li><a href="#">Load balancers</a></li><li><a href="#">Firewalls <span>3</span></a></li><li><a href="#">DNS zones</a></li></ul>
    </section>
    <section class="sbl-22__grp" aria-labelledby="sbl22-g3">
      <h2 id="sbl22-g3">Access</h2>
      <ul><li><a href="#">Team members</a></li><li><a href="#">API tokens</a></li><li><a href="#">Audit log</a></li></ul>
    </section>
  </aside>
  <main class="sbl-22__main"><h1>Clusters</h1><p>No divider lines anywhere — the 22px-to-2px spacing rhythm and the label typography do all the grouping.</p></main>
</section>
```
## CSS
```css
.sbl-22,
.sbl-22 *,
.sbl-22 *::before,
.sbl-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-22 {
  --panel: oklch(0.965 0.005 230);
  --ink: oklch(0.26 0.02 230);
  --mut: oklch(0.5 0.015 230);
  --line: oklch(0.89 0.008 230);
  --accent: oklch(0.5 0.15 235);
  display: grid;
  grid-template-columns: 256px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.99 0.002 230);
  color: var(--ink);
}

.sbl-22__rail {
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 20px 14px;
  overflow-y: auto;
}

.sbl-22__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 15px/1 system-ui,sans-serif;
  padding: 2px 10px 6px;
}

.sbl-22__brand span {
  width: 24px;
  height: 24px;
  border-radius: 7px;
  background: conic-gradient(from 80deg,var(--accent),oklch(0.62 0.13 190));
}

.sbl-22__grp {
  margin-block-start: 22px;
}

.sbl-22__grp h2 {
  font: 650 10.5px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .09em;
  color: color-mix(in oklab,var(--mut) 85%,transparent);
  padding: 0 12px 7px;
}

.sbl-22__grp ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-22__grp a {
  display: flex;
  align-items: center;
  padding: 9px 12px;
  border-radius: 9px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.sbl-22__grp a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 5%,transparent);
}

.sbl-22__grp a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 10%,transparent);
  font-weight: 600;
}

.sbl-22__grp a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-22__grp a span {
  margin-inline-start: auto;
  font: 600 11px/1 system-ui,sans-serif;
  color: var(--mut);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
  border-radius: 999px;
  padding: 3px 8px;
}

.sbl-22__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-22__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-22__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 48ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-22__grp a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — grouping is pure typography: 10.5px uppercase labels at 60% ink and a 22px:2px spacing rhythm; sections carry real headings for AT. */
```
