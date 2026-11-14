---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/light-flexible-css-vertical-rail-menu-collapsible/"
title: "Icon Rail Sidebar with Accessible Labels"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "An icon-only rail where every item keeps an accessible name, and the tooltip is deliberately not that name."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Rail Sidebar with Accessible Labels
Source: https://codefronts.com/navigation/css-sidebar-navigation/light-flexible-css-vertical-rail-menu-collapsible/

An icon-only rail where every item keeps an accessible name, and the tooltip is deliberately not that name. The two jobs are separate: the name is permanent clipped text that assistive technology always reads; the tooltip is a visual affordance for anyone who does not recognise the glyph. title is wrong for either &mdash; announced inconsistently, absent on touch, and its tooltip cannot be hovered or dismissed.
## HTML
```html
<section class="sdb-13" aria-label="Aperture media library">
  <div class="sdb-13__theme">
    <input class="sdb-13__theme-input" type="checkbox" id="sdb-13-theme">
    <label class="sdb-13__theme-label" for="sdb-13-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-13__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-13__app">
    <nav class="sdb-13__rail" aria-label="Aperture library">
      <ul class="sdb-13__list">
        <li><a class="sdb-13__link" href="#sdb-13-main" aria-current="page">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="4" y="5" width="16" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M4 15l4-4 4 4 3-3 5 5" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>
          <span class="sdb-13__sr">All media</span><span class="sdb-13__tip" aria-hidden="true">All media</span></a></li>
        <li><a class="sdb-13__link" href="#sdb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h6l2 2h8v9H4Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <span class="sdb-13__sr">Collections</span><span class="sdb-13__tip" aria-hidden="true">Collections</span></a></li>
        <li><a class="sdb-13__link" href="#sdb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M15.5 15.5L20 20" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <span class="sdb-13__sr">Saved searches</span><span class="sdb-13__tip" aria-hidden="true">Saved searches</span></a></li>
        <li><a class="sdb-13__link" href="#sdb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4l7 4v8l-7 4-7-4V8Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <span class="sdb-13__sr">Renditions</span><span class="sdb-13__tip" aria-hidden="true">Renditions</span></a></li>
        <li><a class="sdb-13__link" href="#sdb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19V5h9l5 5v9Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 13h6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <span class="sdb-13__sr">Licences</span><span class="sdb-13__tip" aria-hidden="true">Licences</span></a></li>
        <li><a class="sdb-13__link" href="#sdb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 4h12v16l-6-4-6 4Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <span class="sdb-13__sr">Archive</span><span class="sdb-13__tip" aria-hidden="true">Archive</span></a></li>
      </ul>
    </nav>

    <main class="sdb-13__main" id="sdb-13-main">
      <div class="sdb-13__main-head">
        <h2 class="sdb-13__main-h">All media</h2>
        <p class="sdb-13__main-m">1,842 assets &middot; 41 GB &middot; last ingest 14:02</p>
      </div>
      <div class="sdb-13__grid" aria-hidden="true">
        <span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-13 {
  --sdb-13-bg: #f4f4f5;
  --sdb-13-surf: #ffffff;
  --sdb-13-surf2: #e9e9ec;
  --sdb-13-line: #d3d3d8;
  --sdb-13-ink: #131316;
  --sdb-13-mut: #5c5c66;
  --sdb-13-acc: #0f5c8c;
  --sdb-13-acc: oklch(45% 0.1 232);
  --sdb-13-acc-soft: #dceaf4;
  --sdb-13-w: 4rem;
  --sdb-13-font-display: "Roboto Condensed", "Archivo Narrow", "Helvetica Neue", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-13-bg);
  color: var(--sdb-13-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-13 *,
.sdb-13 *::before,
.sdb-13 *::after {
  box-sizing: border-box;
}

.sdb-13:has(.sdb-13__theme-input:checked) {
  --sdb-13-bg: #0d0d0f;
  --sdb-13-surf: #15151a;
  --sdb-13-surf2: #1d1d23;
  --sdb-13-line: #2a2a31;
  --sdb-13-ink: #eeeef1;
  --sdb-13-mut: #9a9aa4;
  --sdb-13-acc: #6fbde8;
  --sdb-13-acc: oklch(78% 0.1 232);
  --sdb-13-acc-soft: #16283a;
}

@media (prefers-color-scheme: dark) {
  .sdb-13 {
    --sdb-13-bg: #0d0d0f;
    --sdb-13-surf: #15151a;
    --sdb-13-surf2: #1d1d23;
    --sdb-13-line: #2a2a31;
    --sdb-13-ink: #eeeef1;
    --sdb-13-mut: #9a9aa4;
    --sdb-13-acc: #6fbde8;
    --sdb-13-acc: oklch(78% 0.1 232);
    --sdb-13-acc-soft: #16283a;
  }

  .sdb-13:has(.sdb-13__theme-input:checked) {
    --sdb-13-bg: #f4f4f5;
    --sdb-13-surf: #ffffff;
    --sdb-13-surf2: #e9e9ec;
    --sdb-13-line: #d3d3d8;
    --sdb-13-ink: #131316;
    --sdb-13-mut: #5c5c66;
    --sdb-13-acc: #0f5c8c;
    --sdb-13-acc: oklch(45% 0.1 232);
    --sdb-13-acc-soft: #dceaf4;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-13:has(.sdb-13__theme-input:checked) {
    --sdb-13-bg: #0d0d0f;
    --sdb-13-surf: #15151a;
    --sdb-13-surf2: #1d1d23;
    --sdb-13-line: #2a2a31;
    --sdb-13-ink: #eeeef1;
    --sdb-13-mut: #9a9aa4;
    --sdb-13-acc: #6fbde8;
    --sdb-13-acc: oklch(78% 0.1 232);
    --sdb-13-acc-soft: #16283a;
  }
}

.sdb-13__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-13__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-13__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-13-line);
  background: var(--sdb-13-surf);
  color: var(--sdb-13-ink);
  cursor: pointer;
}

.sdb-13__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-13__theme-input:focus-visible + .sdb-13__theme-label {
  outline: 2px solid var(--sdb-13-acc);
  outline-offset: 2px;
}

.sdb-13__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-13__app {
  display: flex;
  min-inline-size: 0;
  min-block-size: 100vh;
  background: var(--sdb-13-surf);
}

.sdb-13__rail {
  flex: none;
  inline-size: var(--sdb-13-w);
  min-inline-size: 0;
  border-inline-end: 1px solid var(--sdb-13-line);
  background: var(--sdb-13-surf2);
}

.sdb-13__list {
  list-style: none;
  margin: 0;
  padding: 0.3rem;
  display: grid;
  gap: 0.2rem;
}

.sdb-13__link {
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 2.75rem;
  block-size: 2.75rem;
  color: var(--sdb-13-mut);
  text-decoration: none;
}

.sdb-13__link svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
}

.sdb-13__link:hover {
  background: var(--sdb-13-surf);
  color: var(--sdb-13-ink);
}

.sdb-13__link:focus-visible {
  outline: 2px solid var(--sdb-13-acc);
  outline-offset: -2px;
}

.sdb-13__link[aria-current="page"] {
  background: var(--sdb-13-acc-soft);
  color: var(--sdb-13-acc);
  box-shadow: inset 3px 0 0 var(--sdb-13-acc);
}

.sdb-13__tip {
  position: absolute;
  inset-inline-start: calc(100% + 0.55rem);
  inset-block-start: 50%;
  transform: translateY(-50%);
  z-index: 8;
  white-space: nowrap;
  pointer-events: none;
  padding: 0.3rem 0.55rem;
  background: var(--sdb-13-ink);
  color: var(--sdb-13-bg);
  font-family: var(--sdb-13-font-display);
  font-size: 0.8rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  opacity: 0;
  visibility: hidden;
  transition: opacity 120ms ease, visibility 120ms ease;
}

.sdb-13__link:hover .sdb-13__tip,
.sdb-13__link:focus-visible .sdb-13__tip {
  opacity: 1;
  visibility: visible;
}

.sdb-13__main {
  flex: 1;
  min-inline-size: 0;
  padding: 1.4rem 1.25rem 2.5rem;
  display: grid;
  gap: 1.1rem;
  align-content: start;
}

@media (min-width: 46rem) {
  .sdb-13__main {
    padding: 2.2rem 2rem 3rem;
  }
}

.sdb-13__main-head {
  min-inline-size: 0;
}

.sdb-13__main-h {
  margin: 0 0 0.2rem;
  font-family: var(--sdb-13-font-display);
  font-size: clamp(1.5rem, 3.6vw, 2rem);
  text-transform: uppercase;
  letter-spacing: 0.02em;
}

.sdb-13__main-m {
  margin: 0;
  font-size: 0.84rem;
  color: var(--sdb-13-mut);
  font-variant-numeric: tabular-nums;
}

.sdb-13__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(7rem, 1fr));
  gap: 0.5rem;
}

.sdb-13__grid span {
  aspect-ratio: 4 / 3;
  background: var(--sdb-13-surf2);
  border: 1px solid var(--sdb-13-line);
}

.sdb-13__grid span:nth-child(3n) {
  background: var(--sdb-13-acc-soft);
}

@media (prefers-reduced-motion: reduce) {
  .sdb-13__tip {
    transition: none;
  }
}
```
