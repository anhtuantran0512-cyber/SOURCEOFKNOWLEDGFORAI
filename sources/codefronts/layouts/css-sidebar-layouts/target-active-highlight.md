---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/target-active-highlight/"
title: "CSS Target Active Indicator Sidebar Menu without JavaScript"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "A sliding active-indicator bar that animates between menu items when you click — the signature 'framer-motion layoutId' effect — with zero JavaScript."
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Target Active Indicator Sidebar Menu without JavaScript
Source: https://codefronts.com/layouts/css-sidebar-layouts/target-active-highlight/

A sliding active-indicator bar that animates between menu items when you click — the signature 'framer-motion layoutId' effect — with zero JavaScript. The links target page anchors, :target identifies the active section, and the indicator is a single element whose position transitions between :has()-selected states.
## HTML
```html
<section class="sbl-23">
  <aside class="sbl-23__rail" aria-label="Sections">
    <span class="sbl-23__bar" aria-hidden="true"></span>
    <nav>
      <a href="#sbl23-inbox">Inbox</a><a href="#sbl23-today">Today</a><a href="#sbl23-upcoming">Upcoming</a><a href="#sbl23-someday">Someday</a><a href="#sbl23-logbook">Logbook</a>
    </nav>
  </aside>
  <div class="sbl-23__panes">
    <section id="sbl23-inbox"><h1>Inbox</h1><p>Click the menu — the accent bar glides between items. URL fragments + :target + :has(), no script.</p></section>
    <section id="sbl23-today"><h1>Today</h1><p>Three tasks scheduled.</p></section>
    <section id="sbl23-upcoming"><h1>Upcoming</h1><p>Planning horizon: two weeks.</p></section>
    <section id="sbl23-someday"><h1>Someday</h1><p>Ideas parked without guilt.</p></section>
    <section id="sbl23-logbook"><h1>Logbook</h1><p>Completed items, newest first.</p></section>
  </div>
</section>
```
## CSS
```css
.sbl-23,
.sbl-23 *,
.sbl-23 *::before,
.sbl-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-23 {
  --row: 46px;
  --panel: oklch(0.17 0.015 145);
  --ink: oklch(0.94 0.005 145);
  --mut: oklch(0.64 0.012 145);
  --line: oklch(0.28 0.016 145);
  --accent: oklch(0.8 0.16 150);
  display: grid;
  grid-template-columns: 224px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.012 145);
  color: var(--ink);
}

.sbl-23__rail {
  position: relative;
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 18px 12px;
}

.sbl-23__rail nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-23__rail a {
  display: flex;
  align-items: center;
  height: 44px;
  padding: 0 16px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s ease,background-color .2s ease;
}

.sbl-23__rail a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-23__rail a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-23__bar {
  position: absolute;
  left: 4px;
  top: 18px;
  width: 3px;
  height: 28px;
  margin-top: 8px;
  border-radius: 4px;
  background: var(--accent);
  box-shadow: 0 0 12px color-mix(in oklab,var(--accent) 55%,transparent);
  translate: 0 0;
  transition: translate .32s cubic-bezier(.5,0,.2,1.15);
}

.sbl-23:has(#sbl23-today:target) .sbl-23__bar {
  translate: 0 var(--row);
}

.sbl-23:has(#sbl23-upcoming:target) .sbl-23__bar {
  translate: 0 calc(var(--row) * 2);
}

.sbl-23:has(#sbl23-someday:target) .sbl-23__bar {
  translate: 0 calc(var(--row) * 3);
}

.sbl-23:has(#sbl23-logbook:target) .sbl-23__bar {
  translate: 0 calc(var(--row) * 4);
}

.sbl-23:not(:has(:target)) a[href="#sbl23-inbox"],
.sbl-23:has(#sbl23-inbox:target) a[href="#sbl23-inbox"],
.sbl-23:has(#sbl23-today:target) a[href="#sbl23-today"],
.sbl-23:has(#sbl23-upcoming:target) a[href="#sbl23-upcoming"],
.sbl-23:has(#sbl23-someday:target) a[href="#sbl23-someday"],
.sbl-23:has(#sbl23-logbook:target) a[href="#sbl23-logbook"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 12%,transparent);
}

.sbl-23__panes {
  overflow-y: auto;
  padding: 32px;
  display: grid;
  gap: 40px;
  align-content: start;
}

.sbl-23__panes section {
  scroll-margin-top: 24px;
}

.sbl-23__panes h1 {
  font: 600 21px/1.2 system-ui,sans-serif;
  margin-bottom: 8px;
}

.sbl-23__panes p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 48ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-23__bar,
    .sbl-23__rail a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :target marks the active section, :has() repositions one indicator bar via translate stops, and the transition makes it glide. */
```
