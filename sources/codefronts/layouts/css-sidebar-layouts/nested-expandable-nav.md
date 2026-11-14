---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/nested-expandable-nav/"
title: "Multi-Level Nested Tree Sidebar Navigation Layout"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "A file-explorer-grade tree: three levels of nested <details> disclosure with rotating chevrons, indent guides drawn as borders so hierarchy stays legible at…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Level Nested Tree Sidebar Navigation Layout
Source: https://codefronts.com/layouts/css-sidebar-layouts/nested-expandable-nav/

A file-explorer-grade tree: three levels of nested <details> disclosure with rotating chevrons, indent guides drawn as borders so hierarchy stays legible at any depth, folder/file iconography, and progressive padding from a single --indent variable — the whole tree keyboard-operable out of the box because disclosure is native.
## HTML
```html
<section class="sbl-24">
  <aside class="sbl-24__rail" aria-label="Project files">
    <h2 class="sbl-24__title">explorer</h2>
    <details class="sbl-24__branch" open>
      <summary><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>src</summary>
      <div class="sbl-24__kids" style="--indent:1">
        <details class="sbl-24__branch" open>
          <summary><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>components</summary>
          <div class="sbl-24__kids" style="--indent:2">
            <a class="sbl-24__leaf" href="#" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>Sidebar.css</a>
            <a class="sbl-24__leaf" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>Sidebar.html</a>
          </div>
        </details>
        <details class="sbl-24__branch">
          <summary><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>tokens</summary>
          <div class="sbl-24__kids" style="--indent:2">
            <a class="sbl-24__leaf" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>colors.css</a>
            <a class="sbl-24__leaf" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>spacing.css</a>
          </div>
        </details>
        <a class="sbl-24__leaf" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>index.html</a>
      </div>
    </details>
    <details class="sbl-24__branch">
      <summary><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>docs</summary>
      <div class="sbl-24__kids" style="--indent:1">
        <a class="sbl-24__leaf" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>README.md</a>
      </div>
    </details>
  </aside>
  <main class="sbl-24__main"><h1>Sidebar.css</h1><p>Every branch is a native &lt;details&gt; — keyboard toggling and state come free. Indent guides keep level 3 legible.</p></main>
</section>
```
## CSS
```css
.sbl-24,
.sbl-24 *,
.sbl-24 *::before,
.sbl-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-24 {
  --panel: oklch(0.16 0.012 250);
  --ink: oklch(0.92 0.005 250);
  --mut: oklch(0.62 0.012 250);
  --line: oklch(0.27 0.014 250);
  --accent: oklch(0.75 0.12 210);
  display: grid;
  grid-template-columns: 264px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.01 250);
  color: var(--ink);
}

.sbl-24__rail {
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 16px 10px;
  overflow-y: auto;
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
}

.sbl-24__title {
  font: 600 10.5px/1 ui-monospace,Menlo,monospace;
  text-transform: uppercase;
  letter-spacing: .12em;
  color: var(--mut);
  padding: 2px 12px 12px;
}

.sbl-24__branch summary {
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 34px;
  padding: 0 10px;
  padding-inline-start: calc(10px + (var(--indent,0)) * 18px);
  border-radius: 8px;
  font: 500 13px/1 ui-monospace,Menlo,monospace;
  color: var(--ink);
  cursor: pointer;
  list-style: none;
  transition: background-color .15s ease;
}

.sbl-24__branch summary::-webkit-details-marker {
  display: none;
}

.sbl-24__branch summary:hover {
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-24__branch summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-24__branch summary svg {
  width: 14px;
  height: 14px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: rotate .2s ease;
}

.sbl-24__branch[open] > summary svg {
  rotate: 90deg;
}

.sbl-24__kids {
  display: flex;
  flex-direction: column;
  border-inline-start: 1px solid var(--line);
  margin-inline-start: calc(16px + (var(--indent) - 1) * 18px);
}

.sbl-24__kids .sbl-24__branch summary,
.sbl-24__kids .sbl-24__leaf {
  padding-inline-start: 12px;
}

.sbl-24__leaf {
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 34px;
  padding: 0 10px;
  border-radius: 8px;
  font: 400 13px/1 ui-monospace,Menlo,monospace;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.sbl-24__leaf svg {
  width: 14px;
  height: 14px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linejoin: round;
}

.sbl-24__leaf:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-24__leaf[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 12%,transparent);
}

.sbl-24__leaf:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-24__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-24__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-24__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 48ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-24__branch summary svg,
    .sbl-24__leaf,
    .sbl-24__branch summary {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — nested native <details> branches; indentation and guide rails derive from one --indent variable per level. */
```
