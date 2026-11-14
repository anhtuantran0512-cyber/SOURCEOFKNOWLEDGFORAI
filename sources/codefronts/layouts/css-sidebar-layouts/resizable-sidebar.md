---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/resizable-sidebar/"
title: "Pure CSS Resizable Sidebar Layout Using Resize Property"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "A drag-to-resize sidebar with no mousemove listeners, no pointer capture, no drag math: the CSS resize property does the entire interaction."
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Resizable Sidebar Layout Using Resize Property
Source: https://codefronts.com/layouts/css-sidebar-layouts/resizable-sidebar/

A drag-to-resize sidebar with no mousemove listeners, no pointer capture, no drag math: the CSS resize property does the entire interaction. min/max-width fence the range, a styled grip zone signals the affordance, and the main pane reflows live because the layout is plain flex — the browser is running the drag loop for you, off the main thread.
## HTML
```html
<section class="sbl-27">
  <aside class="sbl-27__rail" aria-label="Notes">
    <div class="sbl-27__inner">
      <h2>Notebook</h2>
      <nav>
        <a href="#" aria-current="page">Container queries field guide</a><a href="#">Subgrid recipes</a><a href="#">The :has() cookbook</a><a href="#">Anchor positioning notes</a><a href="#">View transitions research</a>
      </nav>
    </div>
    <span class="sbl-27__grip" aria-hidden="true"><i></i><i></i><i></i></span>
  </aside>
  <main class="sbl-27__main"><h1>Container queries field guide</h1><p>Drag the sidebar's bottom-right corner (or along the dotted grip) — resize:horizontal + a min/max fence, zero drag JavaScript. The pane you're reading reflows live.</p></main>
</section>
```
## CSS
```css
.sbl-27,
.sbl-27 *,
.sbl-27 *::before,
.sbl-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-27 {
  --panel: oklch(0.17 0.014 85);
  --ink: oklch(0.94 0.006 85);
  --mut: oklch(0.66 0.015 85);
  --line: oklch(0.29 0.018 85);
  --accent: oklch(0.8 0.13 90);
  display: flex;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.012 85);
  color: var(--ink);
}

.sbl-27__rail {
  position: relative;
  resize: horizontal;
  overflow: auto;
  min-width: 200px;
  max-width: 440px;
  width: 280px;
  flex: none;
  background: var(--panel);
  border-right: 1px solid var(--line);
}

.sbl-27__inner {
  padding: 20px 14px;
  min-width: 186px;
}

.sbl-27__rail h2 {
  font: 700 14.5px/1 system-ui,sans-serif;
  padding: 0 10px 14px;
}

.sbl-27__rail nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-27__rail a {
  padding: 10px 12px;
  border-radius: 9px;
  font: 500 13.5px/1.35 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: background-color .15s ease,color .15s ease;
}

.sbl-27__rail a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-27__rail a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 13%,transparent);
}

.sbl-27__rail a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-27__grip {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 14px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  align-items: center;
  justify-content: center;
  cursor: col-resize;
  opacity: .5;
  transition: opacity .2s ease;
}

.sbl-27__grip:hover {
  opacity: 1;
}

.sbl-27__grip i {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: var(--mut);
}

.sbl-27__main {
  flex: 1;
  min-width: 0;
  padding: 32px;
  overflow-y: auto;
}

.sbl-27__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-27__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.65;
  max-width: 54ch;
  text-wrap: pretty;
}

@media (pointer: coarse) {
  .sbl-27__grip {
    width: 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sbl-27__grip,
    .sbl-27__rail a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — resize:horizontal + overflow:auto + a min/max-width fence; the browser runs the entire drag interaction natively. */
```
