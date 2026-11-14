---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/tabbed-sidebar/"
title: "Multi-Tab Sidebar UI Component with Dynamic Panel Switching"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "One sidebar, three personalities: Files, Search and Activity panels switched by a segmented tab control — hidden radio inputs drive which panel renders, a…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Tab Sidebar UI Component with Dynamic Panel Switching
Source: https://codefronts.com/layouts/css-sidebar-layouts/tabbed-sidebar/

One sidebar, three personalities: Files, Search and Activity panels switched by a segmented tab control — hidden radio inputs drive which panel renders, a sliding thumb highlights the active tab, and the panels cross-fade with a few pixels of lift. Radio semantics mean arrow-key switching works exactly like a native tab strip.
## HTML
```html
<section class="sbl-25">
  <aside class="sbl-25__rail">
    <div class="sbl-25__tabs" role="group" aria-label="Sidebar panels">
      <input type="radio" name="sbl25" id="sbl25-t1" checked><input type="radio" name="sbl25" id="sbl25-t2"><input type="radio" name="sbl25" id="sbl25-t3">
      <div class="sbl-25__strip" aria-hidden="true"></div>
      <label for="sbl25-t1">Files</label><label for="sbl25-t2">Search</label><label for="sbl25-t3">Activity</label>
    </div>
    <div class="sbl-25__panel sbl-25__panel--1">
      <a href="#" aria-current="page">proposal-v3.md</a><a href="#">budget-2027.xlsx</a><a href="#">kickoff-notes.md</a><a href="#">brand-audit.pdf</a>
    </div>
    <div class="sbl-25__panel sbl-25__panel--2">
      <label class="sbl-25__search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" placeholder="Search workspace…" aria-label="Search workspace"></label>
      <span class="sbl-25__recent">Recent</span><a href="#">container queries</a><a href="#">q3 roadmap</a>
    </div>
    <div class="sbl-25__panel sbl-25__panel--3">
      <p><strong>Priya</strong> edited proposal-v3 <time>12m</time></p><p><strong>Marcus</strong> commented <time>1h</time></p><p><strong>Amara</strong> uploaded 2 files <time>3h</time></p>
    </div>
  </aside>
  <main class="sbl-25__main"><h1>proposal-v3.md</h1><p>Switch tabs — the thumb glides, panels cross-fade. Radios give the group arrow-key switching natively.</p></main>
</section>
```
## CSS
```css
.sbl-25,
.sbl-25 *,
.sbl-25 *::before,
.sbl-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-25 {
  --panel: oklch(0.17 0.016 35);
  --ink: oklch(0.94 0.006 35);
  --mut: oklch(0.65 0.014 35);
  --line: oklch(0.28 0.018 35);
  --accent: oklch(0.72 0.15 40);
  display: grid;
  grid-template-columns: 272px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.013 35);
  color: var(--ink);
}

.sbl-25__rail {
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 14px 12px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.sbl-25__tabs {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  padding: 4px;
  border-radius: 11px;
  background: oklch(0.14 0.014 35);
  border: 1px solid var(--line);
}

.sbl-25__tabs input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.sbl-25__strip {
  position: absolute;
  top: 4px;
  bottom: 4px;
  left: 4px;
  width: calc((100% - 8px)/3);
  border-radius: 8px;
  background: color-mix(in oklab,var(--accent) 22%,transparent);
  border: 1px solid color-mix(in oklab,var(--accent) 40%,transparent);
  transition: translate .28s cubic-bezier(.5,0,.2,1.1);
}

.sbl-25:has(#sbl25-t2:checked) .sbl-25__strip {
  translate: 100% 0;
}

.sbl-25:has(#sbl25-t3:checked) .sbl-25__strip {
  translate: 200% 0;
}

.sbl-25__tabs label {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  height: 34px;
  border-radius: 8px;
  font: 600 12.5px/1 system-ui,sans-serif;
  color: var(--mut);
  cursor: pointer;
  transition: color .2s ease;
}

.sbl-25:has(#sbl25-t1:checked) label[for="sbl25-t1"],
.sbl-25:has(#sbl25-t2:checked) label[for="sbl25-t2"],
.sbl-25:has(#sbl25-t3:checked) label[for="sbl25-t3"] {
  color: var(--ink);
}

.sbl-25__tabs:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-25__panel {
  display: none;
  flex-direction: column;
  gap: 2px;
  padding-top: 14px;
  min-height: 0;
  overflow-y: auto;
}

.sbl-25:has(#sbl25-t1:checked) .sbl-25__panel--1,
.sbl-25:has(#sbl25-t2:checked) .sbl-25__panel--2,
.sbl-25:has(#sbl25-t3:checked) .sbl-25__panel--3 {
  display: flex;
  animation: sbl25-in .25s ease;
}

@keyframes sbl25-in {
  from {
    opacity: 0;
    translate: 0 4px;
  }
}

.sbl-25__panel a {
  padding: 10px 12px;
  border-radius: 9px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.sbl-25__panel a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-25__panel a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 12%,transparent);
}

.sbl-25__panel a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-25__search {
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 8px;
  padding: 0 12px;
  height: 38px;
  margin-bottom: 10px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: oklch(0.14 0.014 35);
}

.sbl-25__search:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 20%,transparent);
}

.sbl-25__search svg {
  width: 15px;
  height: 15px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 2;
  stroke-linecap: round;
}

.sbl-25__search input {
  min-width: 0;
  border: none;
  background: none;
  color: var(--ink);
  font: 400 13px/1 system-ui,sans-serif;
  outline: none;
}

.sbl-25__recent {
  font: 600 10.5px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: var(--mut);
  padding: 6px 12px 4px;
}

.sbl-25__panel--3 p {
  padding: 10px 12px;
  font: 400 13px/1.5 system-ui,sans-serif;
  color: var(--mut);
  border-bottom: 1px solid var(--line);
}

.sbl-25__panel--3 strong {
  color: var(--ink);
  font-weight: 600;
}

.sbl-25__panel--3 time {
  float: right;
  font-size: 11px;
}

.sbl-25__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-25__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-25__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 46ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-25__strip {
    transition: none;
  }

  .sbl-25__panel {
    animation: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — radio inputs drive panel display via :has(:checked); the segmented thumb translates 0/100%/200%; arrow keys switch tabs natively. */
```
