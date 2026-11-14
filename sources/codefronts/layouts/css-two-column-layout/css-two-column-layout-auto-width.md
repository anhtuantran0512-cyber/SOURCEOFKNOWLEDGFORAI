---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-auto-width/"
title: "CSS Two Column Layout Auto Width"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "Content-sized first column, fluid second: grid-template-columns: auto 1fr (and its stricter sibling max-content 1fr) let a badge, timestamp or keyboard…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Layout Auto Width
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-auto-width/

Content-sized first column, fluid second: grid-template-columns: auto 1fr (and its stricter sibling max-content 1fr) let a badge, timestamp or keyboard shortcut set its own width while the text takes the rest — shown as a release changelog and a shortcuts panel where every label column self-aligns to the widest item.
## HTML
```html
<section class="tcl-15" aria-label="Auto width two column layout demo">
  <div class="tcl-15__wrap">
    <div class="tcl-15__panel">
      <header class="tcl-15__phead"><h2>Changelog</h2><span class="tcl-15__spec">auto 1fr</span></header>
      <div class="tcl-15__log">
        <span class="tcl-15__ver tcl-15__ver--new">v3.2.0</span><p><b>Container query cards.</b> Card components now respond to their wrapper width — the same card works in feeds, rails and modals.</p>
        <span class="tcl-15__ver">v3.1.4</span><p><b>Fix:</b> sticky sidebars no longer unpin inside overflow-clipped sections.</p>
        <span class="tcl-15__ver">v3.1.0</span><p><b>Scroll-driven progress.</b> Reading indicators moved off JavaScript onto <code>animation-timeline</code>.</p>
        <span class="tcl-15__ver">v3.0.2</span><p><b>Fix:</b> form grids keep 44px hit targets at 200% zoom.</p>
      </div>
    </div>
    <div class="tcl-15__panel tcl-15__panel--dark">
      <header class="tcl-15__phead"><h2>Shortcuts</h2><span class="tcl-15__spec tcl-15__spec--dark">max-content 1fr</span></header>
      <div class="tcl-15__keys">
        <span class="tcl-15__kbd"><kbd>⌘</kbd><kbd>K</kbd></span><p>Open the command palette</p>
        <span class="tcl-15__kbd"><kbd>⌘</kbd><kbd>Shift</kbd><kbd>P</kbd></span><p>Publish the current draft</p>
        <span class="tcl-15__kbd"><kbd>G</kbd><kbd>then</kbd><kbd>I</kbd></span><p>Jump to inbox</p>
        <span class="tcl-15__kbd"><kbd>?</kbd></span><p>Show every shortcut</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.tcl-15,
.tcl-15 *,
.tcl-15 *::before,
.tcl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-15 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.62 0.17 250);
  --ink: oklch(0.25 0.02 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: oklch(0.965 0.008 250);
  padding: clamp(24px,4vw,52px);
}

.tcl-15__wrap {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(320px,1fr));
  gap: 20px;
  max-width: 960px;
  margin-inline: auto;
  align-items: start;
}

.tcl-15__panel {
  background: #fff;
  border: 1px solid oklch(0.89 0.012 250);
  border-radius: 18px;
  padding: clamp(18px,2.5vw,26px);
  display: grid;
  gap: 16px;
}

.tcl-15__panel--dark {
  background: oklch(0.23 0.03 260);
  border-color: oklch(0.32 0.03 260);
  color: oklch(0.92 0.01 250);
}

.tcl-15__phead {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.tcl-15__phead h2 {
  font-size: 19px;
  letter-spacing: -.015em;
}

.tcl-15__spec {
  font: 600 10.5px/1 ui-monospace,monospace;
  color: var(--accent);
  border: 1px dashed color-mix(in oklab,var(--accent) 50%,transparent);
  border-radius: 99px;
  padding: 5px 9px;
}

.tcl-15__spec--dark {
  color: oklch(0.75 0.12 250);
  border-color: oklch(0.5 0.08 250);
}

.tcl-15__log {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 14px 16px;
  align-items: start;
}

.tcl-15__ver {
  font: 700 11.5px/1 ui-monospace,monospace;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
  background: oklch(0.955 0.008 250);
  border: 1px solid oklch(0.9 0.012 250);
  border-radius: 7px;
  padding: 6px 9px;
  justify-self: start;
  white-space: nowrap;
}

.tcl-15__ver--new {
  color: #fff;
  background: var(--accent);
  border-color: var(--accent);
}

.tcl-15__log p {
  font-size: 13.5px;
  line-height: 1.6;
  color: color-mix(in oklab,var(--ink) 75%,transparent);
  text-wrap: pretty;
}

.tcl-15__log p b {
  color: var(--ink);
}

.tcl-15__log p code {
  font: 600 12px ui-monospace,monospace;
  background: color-mix(in oklab,var(--accent) 10%,transparent);
  border-radius: 4px;
  padding: 1px 5px;
}

.tcl-15__keys {
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 14px 18px;
  align-items: center;
}

.tcl-15__kbd {
  display: flex;
  gap: 4px;
}

.tcl-15__kbd kbd {
  font: 600 11.5px/1 ui-monospace,monospace;
  color: oklch(0.9 0.02 250);
  background: oklch(0.3 0.03 260);
  border: 1px solid oklch(0.42 0.03 260);
  border-bottom-width: 2.5px;
  border-radius: 6px;
  padding: 6px 8px;
  white-space: nowrap;
}

.tcl-15__keys p {
  font-size: 13.5px;
  line-height: 1.5;
  color: oklch(0.8 0.02 250);
}

@media (max-width: 420px) {
  .tcl-15__log,
    .tcl-15__keys {
    grid-template-columns: 1fr;
  }

  .tcl-15__log p,
    .tcl-15__keys p {
    margin-top: -8px;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-columns:auto 1fr (changelog) and max-content 1fr (shortcuts); one shared grid per list makes every first-column item align to the widest. */
```
