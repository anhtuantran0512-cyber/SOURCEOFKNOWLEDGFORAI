---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/collapsible-sidebar/"
title: "Pure CSS Collapsible Sidebar Drawer Menu without JavaScript"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The zero-JS drawer, done the 2026 way: a hidden checkbox holds the open/closed state, :has() reads it from the body level, and the drawer slides on…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Collapsible Sidebar Drawer Menu without JavaScript
Source: https://codefronts.com/layouts/css-sidebar-layouts/collapsible-sidebar/

The zero-JS drawer, done the 2026 way: a hidden checkbox holds the open/closed state, :has() reads it from the body level, and the drawer slides on transform: translate3d() so the whole animation runs on the GPU compositor — 60fps even mid-page-load, nothing for Lighthouse to flag. The hamburger morphs into an X with two transforms.
## HTML
```html
<section class="sbl-07">
  <input type="checkbox" id="sbl07-t" class="sbl-07__state">
  <header class="sbl-07__topbar">
    <label for="sbl07-t" class="sbl-07__burger" aria-hidden="true"><span></span><span></span><span></span></label>
    <strong>Fieldnotes</strong>
  </header>
  <label for="sbl07-t" class="sbl-07__scrim" aria-hidden="true"></label>
  <aside class="sbl-07__drawer" aria-label="Menu">
    <nav class="sbl-07__nav">
      <a href="#" aria-current="page">All notes</a><a href="#">Notebooks</a><a href="#">Tags</a><a href="#">Archive</a><a href="#">Trash</a>
    </nav>
  </aside>
  <main class="sbl-07__main"><h1>All notes</h1><p>Open the drawer — the only animated property is transform, so the slide is fully GPU-composited. Zero JavaScript on this page.</p></main>
</section>
```
## CSS
```css
.sbl-07,
.sbl-07 *,
.sbl-07 *::before,
.sbl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-07 {
  --panel: oklch(0.18 0.02 300);
  --ink: oklch(0.93 0.005 300);
  --mut: oklch(0.64 0.012 300);
  --line: oklch(0.29 0.02 300);
  --accent: oklch(0.72 0.16 320);
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.14 0.015 300);
  color: var(--ink);
}

.sbl-07__state {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.sbl-07__topbar {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 0 16px;
  height: 54px;
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  font: 600 15px/1 system-ui,sans-serif;
}

.sbl-07__burger {
  display: grid;
  gap: 4.5px;
  padding: 12px 10px;
  margin-left: -10px;
  cursor: pointer;
  border-radius: 9px;
}

.sbl-07__burger span {
  display: block;
  width: 19px;
  height: 2px;
  border-radius: 2px;
  background: var(--ink);
  transition: rotate .3s ease,translate .3s ease,opacity .2s ease;
}

.sbl-07:has(#sbl07-t:checked) .sbl-07__burger span:nth-child(1) {
  rotate: 45deg;
  translate: 0 6.5px;
}

.sbl-07:has(#sbl07-t:checked) .sbl-07__burger span:nth-child(2) {
  opacity: 0;
}

.sbl-07:has(#sbl07-t:checked) .sbl-07__burger span:nth-child(3) {
  rotate: -45deg;
  translate: 0 -6.5px;
}

.sbl-07:has(#sbl07-t:focus-visible) .sbl-07__burger {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-07__scrim {
  position: absolute;
  inset: 54px 0 0;
  background: oklch(0 0 0 / .5);
  backdrop-filter: blur(2px);
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s ease;
  z-index: 1;
}

.sbl-07:has(#sbl07-t:checked) .sbl-07__scrim {
  opacity: 1;
  pointer-events: auto;
}

.sbl-07__drawer {
  position: absolute;
  top: 54px;
  bottom: 0;
  left: 0;
  width: min(280px,85vw);
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 16px 12px;
  transform: translate3d(-100%,0,0);
  visibility: hidden;
  transition: transform .32s cubic-bezier(.4,0,.2,1),visibility 0s .32s;
  z-index: 2;
}

.sbl-07:has(#sbl07-t:checked) .sbl-07__drawer {
  transform: translate3d(0,0,0);
  visibility: visible;
  transition: transform .32s cubic-bezier(.4,0,.2,1);
}

.sbl-07__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-07__nav a {
  padding: 11px 14px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-07__nav a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.sbl-07__nav a[aria-current="page"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 18%,transparent);
}

.sbl-07__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-07__main {
  padding: 28px;
  overflow-y: auto;
}

.sbl-07__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-07__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 46ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-07__drawer,
    .sbl-07__scrim,
    .sbl-07__burger span {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hidden checkbox holds state, :has(:checked) slides the drawer via GPU-composited translate3d, and the scrim is a second <label>. */
```
