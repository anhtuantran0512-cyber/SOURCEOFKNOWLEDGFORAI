---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/css-position-sticky-sidebar-layout-for-e-commerce-and-blogs/"
title: "CSS Position Sticky Sidebar Layout for E-Commerce and Blogs"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The long-article companion rail: a table of contents that rides along as you scroll — position:sticky with the three constraints people always miss (top…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Position Sticky Sidebar Layout for E-Commerce and Blogs
Source: https://codefronts.com/layouts/css-sidebar-layouts/css-position-sticky-sidebar-layout-for-e-commerce-and-blogs/

The long-article companion rail: a table of contents that rides along as you scroll — position:sticky with the three constraints people always miss (top offset, self-alignment, max-height) — plus a scroll-driven reading progress bar powered by CSS scroll-timeline. The page scrolls as one document; only the rail sticks.
## HTML
```html
<section class="sbl-15">
  <div class="sbl-15__progress" aria-hidden="true"></div>
  <div class="sbl-15__page">
    <aside class="sbl-15__rail" aria-label="On this page">
      <h2>On this page</h2>
      <nav><a href="#sbl15-s1" aria-current="true">Why grids beat floats</a><a href="#sbl15-s2">Track sizing deep-dive</a><a href="#sbl15-s3">Alignment properties</a><a href="#sbl15-s4">Subgrid in practice</a><a href="#sbl15-s5">Container queries</a></nav>
    </aside>
    <article class="sbl-15__article">
      <h1 id="sbl15-s1">Modern CSS layout, properly</h1>
      <p>Scroll this page — the rail sticks at 24px from the top while the article flows past. The progress bar up top is a scroll-driven animation, no JS.</p>
      <h2 id="sbl15-s2">Track sizing deep-dive</h2>
      <p>Fixed, fractional, minmax and fit-content tracks each answer a different layout question. Fractional units distribute leftover space, not total space — the distinction that explains most grid surprises.</p>
      <h2 id="sbl15-s3">Alignment properties</h2>
      <p>justify- controls the inline axis, align- the block axis. The -content properties move tracks; -items move children within their cells; -self overrides per child.</p>
      <h2 id="sbl15-s4">Subgrid in practice</h2>
      <p>Subgrid lets nested elements adopt parent rails — card grids with aligned footers, forms with aligned labels, sidebars with aligned badges (see demo 06).</p>
      <h2 id="sbl15-s5">Container queries</h2>
      <p>Components respond to their container, not the viewport. Demo 29 rebuilds this sidebar pattern on @container rules.</p>
    </article>
  </div>
</section>
```
## CSS
```css
.sbl-15,
.sbl-15 *,
.sbl-15 *::before,
.sbl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-15 {
  --ink: oklch(0.27 0.015 250);
  --mut: oklch(0.52 0.012 250);
  --line: oklch(0.9 0.007 250);
  --accent: oklch(0.55 0.16 250);
  height: 100vh;
  height: 100dvh;
  overflow-y: auto;
  scroll-timeline: --sbl15-scroll block;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.99 0.002 250);
  color: var(--ink);
}

.sbl-15__progress {
  position: sticky;
  top: 0;
  height: 3px;
  background: linear-gradient(90deg,var(--accent),oklch(0.65 0.15 300));
  width: 0;
  z-index: 5;
  animation: sbl15-grow linear;
  animation-timeline: --sbl15-scroll;
}

@keyframes sbl15-grow {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

.sbl-15__page {
  display: grid;
  grid-template-columns: 230px minmax(0,1fr);
  gap: 40px;
  max-width: 920px;
  margin: 0 auto;
  padding: 32px 24px 60px;
}

.sbl-15__rail {
  position: sticky;
  top: 24px;
  align-self: start;
  max-height: calc(100dvh - 48px);
  overflow-y: auto;
  border-right: 1px solid var(--line);
  padding-right: 20px;
}

.sbl-15__rail h2 {
  font: 600 11px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .09em;
  color: var(--mut);
  margin-bottom: 12px;
}

.sbl-15__rail nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-15__rail a {
  padding: 7px 10px;
  border-radius: 8px;
  font: 500 13px/1.4 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: color .15s ease,background-color .15s ease;
}

.sbl-15__rail a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 5%,transparent);
}

.sbl-15__rail a[aria-current="true"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 9%,transparent);
  font-weight: 600;
}

.sbl-15__rail a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-15__article h1 {
  font: 700 26px/1.2 system-ui,sans-serif;
  margin-bottom: 14px;
}

.sbl-15__article h2 {
  font: 650 18px/1.3 system-ui,sans-serif;
  margin: 30px 0 10px;
  scroll-margin-top: 20px;
}

.sbl-15__article p {
  font-size: 14.5px;
  line-height: 1.75;
  color: oklch(0.38 0.012 250);
  max-width: 62ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-15__progress {
    animation: none;
    width: 100%;
    opacity: .25;
  }
}
```

## JavaScript
```js
/* No JavaScript — sticky needs top + align-self:start + max-height (all three here); the progress bar runs on a named CSS scroll-timeline. */
```
