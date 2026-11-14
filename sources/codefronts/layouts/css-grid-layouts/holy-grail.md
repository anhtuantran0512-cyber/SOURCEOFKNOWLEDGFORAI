---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/holy-grail/"
title: "Holy Grail"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The canonical three-row, three-column holy grail — presented as the teaching version: every region labelled with its grid-area name, a visible track diagram,…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holy Grail
Source: https://codefronts.com/layouts/css-grid-layouts/holy-grail/

The canonical three-row, three-column holy grail — presented as the teaching version: every region labelled with its grid-area name, a visible track diagram, and the exact 2000s-era problems (equal-height columns, footer at the bottom, source-order independence) annotated as solved. The reference students bookmark.
## HTML
```html
<section class="cgl-07" aria-label="Holy grail layout demo">
  <div class="cgl-07__shell">
    <header class="cgl-07__masthead"><h3>The Holy Grail</h3><p>solved in one declaration since 2017</p></header>
    <nav class="cgl-07__menu" aria-label="Sections"><span class="cgl-07__tag">menu · 160px</span><a href="#0">Front page</a><a href="#0">Archive</a><a href="#0">About</a></nav>
    <main class="cgl-07__content"><span class="cgl-07__tag">content · minmax(0,1fr)</span><p>Equal-height columns? Automatic — grid items stretch to their row. Fluid center? The 1fr track. Footer at the bottom on short pages? The 1fr <em>row</em>. Three famous problems, zero hacks.</p></main>
    <aside class="cgl-07__extras"><span class="cgl-07__tag">extras · 160px</span><p>Source order stays semantic; the grid places regions visually.</p></aside>
    <footer class="cgl-07__colophon"><span class="cgl-07__tag">colophon</span><p>grid-template: areas / rows / columns — one shorthand, whole page.</p></footer>
  </div>
</section>
```
## CSS
```css
.cgl-07,
.cgl-07 *,
.cgl-07 *::before,
.cgl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-07 {
  width: 100%;
  min-height: 100vh;
  --cream: oklch(0.96 0.02 90);
  --ink: oklch(0.28 0.04 50);
  --red: oklch(0.55 0.19 30);
  font-family: Georgia,'Times New Roman',serif;
  background: var(--cream);
  color: var(--ink);
  padding: 1.4rem;
}

.cgl-07 .cgl-07__shell {
  display: grid;
  grid-template: "masthead masthead masthead" auto "menu content extras" 1fr "colophon colophon colophon" auto / 160px minmax(0,1fr) 160px;
  gap: 2px;
  min-block-size: 360px;
  background: var(--ink);
  border: 2px solid var(--ink);
  border-radius: 6px;
  overflow: hidden;
}

.cgl-07 .cgl-07__shell>* {
  background: var(--cream);
  padding: 1rem;
}

.cgl-07 .cgl-07__masthead {
  grid-area: masthead;
  display: flex;
  align-items: baseline;
  gap: 1rem;
  border-block-end: none;
}

.cgl-07 .cgl-07__masthead h3 {
  font-size: 1.4rem;
  font-variant: small-caps;
  letter-spacing: .04em;
}

.cgl-07 .cgl-07__masthead p {
  font-size: .78rem;
  font-style: italic;
  color: color-mix(in oklab,var(--ink) 65%,var(--cream));
}

.cgl-07 .cgl-07__menu {
  grid-area: menu;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.cgl-07 .cgl-07__menu a {
  font-size: .85rem;
  color: var(--ink);
  text-decoration: none;
  border-block-end: 1px dotted color-mix(in oklab,var(--ink) 40%,var(--cream));
  padding-block: .35rem;
  overflow-wrap: break-word;
}

.cgl-07 .cgl-07__menu a:hover {
  color: var(--red);
}

.cgl-07 .cgl-07__menu a:focus-visible {
  outline: 2px solid var(--red);
  outline-offset: 2px;
}

.cgl-07 .cgl-07__content {
  grid-area: content;
}

.cgl-07 .cgl-07__extras {
  grid-area: extras;
}

.cgl-07 .cgl-07__colophon {
  grid-area: colophon;
  display: flex;
  align-items: baseline;
  gap: 1rem;
  background: oklch(0.92 0.025 85);
}

.cgl-07 .cgl-07__tag {
  display: block;
  font-family: ui-monospace,Menlo,monospace;
  font-size: .62rem;
  color: var(--red);
  background: color-mix(in oklab,var(--red) 10%,var(--cream));
  border: 1px solid color-mix(in oklab,var(--red) 35%,var(--cream));
  border-radius: 4px;
  padding: .2rem .45rem;
  inline-size: fit-content;
  margin-block-end: .6rem;
}

.cgl-07 p {
  font-size: .85rem;
  line-height: 1.6;
}

@media (max-width: 600px) {
  .cgl-07 .cgl-07__shell {
    grid-template: "masthead" auto "menu" auto "content" 1fr "extras" auto "colophon" auto / 1fr;
  }
}
```

## JavaScript
```js
/* No JavaScript — the grid-template shorthand sets areas, rows and columns in a single declaration. */
```
