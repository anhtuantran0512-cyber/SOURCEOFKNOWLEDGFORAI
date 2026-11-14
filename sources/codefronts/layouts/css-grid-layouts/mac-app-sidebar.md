---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/mac-app-sidebar/"
title: "Mac App Sidebar"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The desktop-app frame macOS made canonical: a translucent source-list sidebar with grouped sections, a unified toolbar, and a content pane that scrolls alone."
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mac App Sidebar
Source: https://codefronts.com/layouts/css-grid-layouts/mac-app-sidebar/

The desktop-app frame macOS made canonical: a translucent source-list sidebar with grouped sections, a unified toolbar, and a content pane that scrolls alone. Vibrancy via backdrop-filter, hairline separators at true 1px, and the grid discipline that keeps 'app chrome' rock-still while documents fly.
## HTML
```html
<section class="cgl-26" aria-label="Mac app sidebar demo">
  <div class="cgl-26__window">
    <header class="cgl-26__toolbar">
      <span class="cgl-26__lights" aria-hidden="true"><i></i><i></i><i></i></span>
      <strong>Notes</strong>
      <button type="button" class="cgl-26__tbtn">＋ New</button>
    </header>
    <nav class="cgl-26__sidebar" aria-label="Folders">
      <p class="cgl-26__group">iCloud</p>
      <a href="#0" class="is-selected"><span>📝</span>All Notes<em>128</em></a>
      <a href="#0"><span>📌</span>Pinned<em>6</em></a>
      <a href="#0"><span>🗂️</span>Work<em>34</em></a>
      <p class="cgl-26__group">Tags</p>
      <a href="#0"><span>#</span>css-grid<em>12</em></a>
      <a href="#0"><span>#</span>codefronts<em>30</em></a>
    </nav>
    <main class="cgl-26__content">
      <h4>Grid keeps the chrome still</h4>
      <p>This pane owns the only document scrollbar. The toolbar spans both columns with grid-column: 1/-1; the sidebar scrolls its groups independently.</p>
      <p>Vibrancy = translucent fill + backdrop-filter: blur(24px) saturate(160%) over the window's backdrop.</p>
    </main>
  </div>
</section>
```
## CSS
```css
.cgl-26,
.cgl-26 *,
.cgl-26 *::before,
.cgl-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-26 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.65 0.17 260);
  --txt: oklch(0.22 0.01 260);
  --dim: oklch(0.5 0.015 260);
  font-family: system-ui,-apple-system,sans-serif;
  background: linear-gradient(140deg,oklch(0.75 0.08 300),oklch(0.7 0.09 220) 50%,oklch(0.78 0.07 170));
  padding: 1.6rem;
}

.cgl-26 .cgl-26__window {
  display: grid;
  grid-template-columns: 224px minmax(0,1fr);
  grid-template-rows: auto minmax(0,1fr);
  block-size: 360px;
  max-inline-size: 640px;
  margin-inline: auto;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 30px 70px -30px oklch(0.2 0.05 260/.7);
  border: 1px solid oklch(1 0 0/.4);
}

.cgl-26 .cgl-26__toolbar {
  grid-column: 1/-1;
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: .6rem .9rem;
  background: oklch(0.97 0.005 260/.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-block-end: 1px solid oklch(0.2 0.01 260/.12);
}

.cgl-26 .cgl-26__lights {
  display: flex;
  gap: 7px;
}

.cgl-26 .cgl-26__lights i {
  inline-size: 11px;
  aspect-ratio: 1;
  border-radius: 50%;
}

.cgl-26 .cgl-26__lights i:nth-child(1) {
  background: oklch(0.68 0.19 25);
}

.cgl-26 .cgl-26__lights i:nth-child(2) {
  background: oklch(0.8 0.15 85);
}

.cgl-26 .cgl-26__lights i:nth-child(3) {
  background: oklch(0.75 0.17 145);
}

.cgl-26 .cgl-26__toolbar strong {
  font-size: .82rem;
  color: var(--txt);
}

.cgl-26 .cgl-26__tbtn {
  margin-inline-start: auto;
  font-size: .75rem;
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 10%,white);
  border: 1px solid color-mix(in oklab,var(--accent) 30%,white);
  border-radius: 7px;
  padding: .35rem .7rem;
  cursor: pointer;
  min-block-size: 2rem;
}

.cgl-26 .cgl-26__tbtn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cgl-26 .cgl-26__sidebar {
  overflow-y: auto;
  background: oklch(0.96 0.008 260/.62);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border-inline-end: 1px solid oklch(0.2 0.01 260/.12);
  padding: .7rem .55rem;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.cgl-26 .cgl-26__group {
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--dim);
  padding: .7rem .55rem .25rem;
}

.cgl-26 .cgl-26__sidebar a {
  display: grid;
  grid-template-columns: 1.3em minmax(0,1fr) auto;
  align-items: center;
  column-gap: .5rem;
  font-size: .8rem;
  color: var(--txt);
  text-decoration: none;
  padding: .3rem .55rem;
  min-block-size: 28px;
  border-radius: 7px;
}

.cgl-26 .cgl-26__sidebar a em {
  font-style: normal;
  font-size: .68rem;
  font-variant-numeric: tabular-nums;
  color: var(--dim);
}

.cgl-26 .cgl-26__sidebar a:hover {
  background: oklch(0.2 0.01 260/.07);
}

.cgl-26 .cgl-26__sidebar a.is-selected {
  background: color-mix(in oklab,var(--accent) 20%,transparent);
  color: color-mix(in oklab,var(--accent) 70%,var(--txt));
  font-weight: 600;
}

.cgl-26 .cgl-26__sidebar a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.cgl-26 .cgl-26__content {
  overflow-y: auto;
  background: white;
  padding: 1.3rem;
}

.cgl-26 h4 {
  font-size: 1rem;
  color: var(--txt);
  margin-block-end: .6rem;
}

.cgl-26 .cgl-26__content p {
  font-size: .82rem;
  line-height: 1.65;
  color: var(--dim);
  margin-block-end: .7rem;
}

@media (max-width: 560px) {
  .cgl-26 .cgl-26__window {
    grid-template-columns: minmax(0,1fr);
  }

  .cgl-26 .cgl-26__sidebar {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a toolbar-spanning app grid; vibrancy from backdrop-filter blur + saturate over the window backdrop. */
```
