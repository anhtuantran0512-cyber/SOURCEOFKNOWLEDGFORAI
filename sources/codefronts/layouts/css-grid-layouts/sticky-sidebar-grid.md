---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/sticky-sidebar-grid/"
title: "Sticky Sidebar Grid"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A docs-style two-column grid where the table of contents stays pinned while the article scrolls past — the pattern developers fight with for hours because…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Sidebar Grid
Source: https://codefronts.com/layouts/css-grid-layouts/sticky-sidebar-grid/

A docs-style two-column grid where the table of contents stays pinned while the article scrolls past — the pattern developers fight with for hours because one missing declaration silently kills position: sticky inside grid. This demo names the culprit (align-self: start) and ships the fix.
## HTML
```html
<section class="cgl-02" aria-label="Sticky sidebar grid demo">
  <div class="cgl-02__shell">
    <aside class="cgl-02__side">
      <nav class="cgl-02__nav" aria-label="Section navigation">
        <p class="cgl-02__navtitle">On this page</p>
        <a href="#cgl02-a" class="is-active">Getting started</a>
        <a href="#cgl02-b">Why sticky breaks</a>
        <a href="#cgl02-c">The align-self fix</a>
        <a href="#cgl02-d">Overflow traps</a>
      </nav>
    </aside>
    <main class="cgl-02__main">
      <article id="cgl02-a"><h3>Getting started</h3><p>Scroll this panel — the sidebar nav stays pinned while the article moves. Two grid columns, one sticky child, zero JavaScript.</p></article>
      <article id="cgl02-b"><h3>Why sticky breaks</h3><p>Grid stretches items to fill the row's block size. A stretched sidebar is already as tall as its track, so it has no room to travel — sticky computes but never visibly engages.</p></article>
      <article id="cgl02-c"><h3>The align-self fix</h3><p>Setting align-self: start shrinks the sidebar to its content height. Now the track is taller than the item, and sticky has the travel distance it needs.</p></article>
      <article id="cgl02-d"><h3>Overflow traps</h3><p>The second silent killer: any ancestor with overflow: hidden becomes the sticky containing block and clips the effect. Keep the chain clean.</p></article>
    </main>
  </div>
</section>
```
## CSS
```css
.cgl-02,
.cgl-02 *,
.cgl-02 *::before,
.cgl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-02 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.18 0.02 265);
  --panel: oklch(0.22 0.025 265);
  --txt: oklch(0.92 0.01 260);
  --dim: oklch(0.68 0.02 260);
  --lime: oklch(0.85 0.19 130);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  color: var(--txt);
  padding: 1.2rem;
}

.cgl-02 .cgl-02__shell {
  display: grid;
  grid-template-columns: minmax(200px,240px) minmax(0,1fr);
  gap: 1.2rem;
  block-size: 340px;
  overflow-y: auto;
  overscroll-behavior: contain;
  border: 1px solid oklch(0.32 0.03 265);
  border-radius: 14px;
  padding: 1.2rem;
  background: var(--panel);
}

.cgl-02 .cgl-02__side {
  grid-column: 1;
}

.cgl-02 .cgl-02__nav {
  position: sticky;
  inset-block-start: 0;
  align-self: start;
  display: flex;
  flex-direction: column;
  gap: 2px;
  background: oklch(0.26 0.03 265);
  border: 1px solid oklch(0.34 0.03 265);
  border-radius: 10px;
  padding: .9rem;
}

.cgl-02 .cgl-02__navtitle {
  font-size: .68rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--dim);
  margin-block-end: .5rem;
}

.cgl-02 .cgl-02__nav a {
  font-size: .85rem;
  color: var(--dim);
  text-decoration: none;
  padding: .45rem .6rem;
  border-radius: 7px;
  border-inline-start: 2px solid transparent;
}

.cgl-02 .cgl-02__nav a:hover {
  color: var(--txt);
  background: oklch(0.3 0.03 265);
}

.cgl-02 .cgl-02__nav a.is-active {
  color: var(--lime);
  border-inline-start-color: var(--lime);
  background: color-mix(in oklab,var(--lime) 10%,transparent);
}

.cgl-02 .cgl-02__nav a:focus-visible {
  outline: 2px solid var(--lime);
  outline-offset: 2px;
}

.cgl-02 .cgl-02__main {
  display: flex;
  flex-direction: column;
  gap: 1.4rem;
}

.cgl-02 .cgl-02__main article {
  scroll-margin-block-start: 1rem;
}

.cgl-02 h3 {
  font-size: 1.05rem;
  margin-block-end: .4rem;
  color: var(--lime);
}

.cgl-02 p {
  font-size: .88rem;
  line-height: 1.65;
  color: var(--dim);
}

@media (max-width: 600px) {
  .cgl-02 .cgl-02__shell {
    grid-template-columns: 1fr;
  }

  .cgl-02 .cgl-02__nav {
    position: static;
  }
}
```

## JavaScript
```js
/* No JavaScript — align-self: start un-stretches the sidebar so position: sticky can engage inside its grid track. */
```
