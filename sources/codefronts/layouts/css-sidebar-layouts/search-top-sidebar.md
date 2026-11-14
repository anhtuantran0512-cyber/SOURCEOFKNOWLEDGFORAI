---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/search-top-sidebar/"
title: "App Sidebar Navigation with Integrated Sticky Search Bar"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The command-center rail: a search field pinned above a long scrolling menu — sticky INSIDE the sidebar's own scroll context — with a ⌘K keycap hint, a…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: App Sidebar Navigation with Integrated Sticky Search Bar
Source: https://codefronts.com/layouts/css-sidebar-layouts/search-top-sidebar/

The command-center rail: a search field pinned above a long scrolling menu — sticky INSIDE the sidebar's own scroll context — with a ⌘K keycap hint, a scroll-aware border that appears only once the list has scrolled beneath it, and :focus-within lighting the whole search box when the input takes focus.
## HTML
```html
<section class="sbl-21">
  <aside class="sbl-21__rail" aria-label="Channels">
    <div class="sbl-21__search">
      <label class="sbl-21__field">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input type="search" placeholder="Jump to…" aria-label="Search channels">
        <kbd>⌘K</kbd>
      </label>
    </div>
    <nav class="sbl-21__nav">
      <a href="#" aria-current="page"># general</a><a href="#"># announcements</a><a href="#"># engineering</a><a href="#"># design-systems</a><a href="#"># frontend-guild</a><a href="#"># css-wizardry</a><a href="#"># accessibility</a><a href="#"># performance</a><a href="#"># releases</a><a href="#"># random</a><a href="#"># watercooler</a><a href="#"># reading-club</a>
    </nav>
  </aside>
  <main class="sbl-21__main"><h1># general</h1><p>Scroll the channel list — the search stays pinned inside the rail's own scroll context, and channels slide beneath it.</p></main>
</section>
```
## CSS
```css
.sbl-21,
.sbl-21 *,
.sbl-21 *::before,
.sbl-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-21 {
  --panel: oklch(0.17 0.02 310);
  --ink: oklch(0.94 0.005 310);
  --mut: oklch(0.64 0.014 310);
  --line: oklch(0.28 0.02 310);
  --accent: oklch(0.72 0.15 310);
  display: grid;
  grid-template-columns: 264px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.015 310);
  color: var(--ink);
}

.sbl-21__rail {
  background: var(--panel);
  border-right: 1px solid var(--line);
  overflow-y: auto;
  overscroll-behavior: contain;
}

.sbl-21__search {
  position: sticky;
  top: 0;
  z-index: 2;
  padding: 14px 12px 10px;
  background: var(--panel);
  border-bottom: 1px solid var(--line);
}

.sbl-21__field {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 9px;
  padding: 0 12px;
  height: 40px;
  border-radius: 11px;
  border: 1px solid var(--line);
  background: oklch(0.14 0.016 310);
  transition: border-color .2s ease,box-shadow .2s ease;
}

.sbl-21__field:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 22%,transparent);
}

.sbl-21__field svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 2;
  stroke-linecap: round;
}

.sbl-21__field input {
  min-width: 0;
  border: none;
  background: none;
  color: var(--ink);
  font: 400 13.5px/1 system-ui,sans-serif;
  outline: none;
}

.sbl-21__field input::placeholder {
  color: color-mix(in oklab,var(--mut) 75%,transparent);
}

.sbl-21__field kbd {
  font: 600 10.5px/1 ui-monospace,Menlo,monospace;
  color: var(--mut);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
  border: 1px solid var(--line);
  border-radius: 5px;
  padding: 3px 5px;
}

.sbl-21__nav {
  display: flex;
  flex-direction: column;
  gap: 1px;
  padding: 10px 12px 16px;
}

.sbl-21__nav a {
  padding: 9px 12px;
  border-radius: 9px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.sbl-21__nav a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-21__nav a[aria-current="page"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 16%,transparent);
}

.sbl-21__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-21__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-21__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-21__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 47ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-21__field,
    .sbl-21__nav a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the search is position:sticky inside the rail's own scroll context; :focus-within ring-lights the whole field when the input focuses. */
```
