---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/smooth-animated-collapsible-sidebar-menu-with-icon-only-mode/"
title: "Smooth Animated Collapsible Sidebar Menu with Icon-Only Mode"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The polished shrink-to-rail collapse: 248px of labeled navigation eases down to a 68px icon rail in one motion — the grid track, the fading labels, and a…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smooth Animated Collapsible Sidebar Menu with Icon-Only Mode
Source: https://codefronts.com/layouts/css-sidebar-layouts/smooth-animated-collapsible-sidebar-menu-with-icon-only-mode/

The polished shrink-to-rail collapse: 248px of labeled navigation eases down to a 68px icon rail in one motion — the grid track, the fading labels, and a rotating fold chevron all sharing a single 300ms curve. Labels fade BEFORE the track finishes (staggered transitions), which is the micro-detail that makes it feel engineered instead of animated.
## HTML
```html
<section class="sbl-09">
  <input type="checkbox" id="sbl09-c" class="sbl-09__state">
  <aside class="sbl-09__rail">
    <div class="sbl-09__brand"><span class="sbl-09__mark" aria-hidden="true"></span><span class="sbl-09__word">Northwind</span></div>
    <nav class="sbl-09__nav" aria-label="Main">
      <a href="#" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg><span class="sbl-09__txt">Dashboard</span></a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12a9 9 0 1 1-9-9"/><path d="M12 3a9 9 0 0 1 9 9h-9z"/></svg><span class="sbl-09__txt">Insights</span></a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 7 12 3 4 7m16 0v10l-8 4-8-4V7m16 0-8 4M4 7l8 4m0 0v10"/></svg><span class="sbl-09__txt">Inventory</span></a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg><span class="sbl-09__txt">Team</span></a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="sbl-09__txt">Settings</span></a>
    </nav>
    <label for="sbl09-c" class="sbl-09__fold"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m14 6-6 6 6 6"/></svg><span class="sbl-09__txt">Collapse</span></label>
  </aside>
  <main class="sbl-09__main"><h1>Dashboard</h1><p>Watch the choreography: on collapse the labels fade first, then the rail narrows. On expand, the reverse.</p></main>
</section>
```
## CSS
```css
.sbl-09,
.sbl-09 *,
.sbl-09 *::before,
.sbl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-09 {
  --panel: oklch(0.965 0.006 250);
  --ink: oklch(0.25 0.02 250);
  --mut: oklch(0.5 0.015 250);
  --line: oklch(0.89 0.008 250);
  --accent: oklch(0.52 0.16 250);
  display: grid;
  grid-template-columns: 248px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.99 0.002 250);
  color: var(--ink);
  transition: grid-template-columns .3s cubic-bezier(.4,0,.2,1);
}

.sbl-09:has(#sbl09-c:checked) {
  grid-template-columns: 68px 1fr;
}

.sbl-09__state {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.sbl-09__rail {
  display: flex;
  flex-direction: column;
  gap: 2px;
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 16px 10px;
  overflow: hidden;
}

.sbl-09__brand {
  display: grid;
  grid-template-columns: 28px 1fr;
  align-items: center;
  gap: 10px;
  padding: 4px 10px 18px;
  white-space: nowrap;
}

.sbl-09__mark {
  width: 28px;
  height: 28px;
  border-radius: 9px;
  background: conic-gradient(from 120deg,var(--accent),oklch(0.65 0.14 300));
}

.sbl-09__word {
  font: 700 15px/1 system-ui,sans-serif;
}

.sbl-09__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-09__nav a,
.sbl-09__fold {
  display: grid;
  grid-template-columns: 20px 1fr;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  cursor: pointer;
  white-space: nowrap;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-09__nav svg,
.sbl-09__fold svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-09__fold svg {
  transition: rotate .3s cubic-bezier(.4,0,.2,1);
}

.sbl-09__txt,
.sbl-09__word {
  opacity: 1;
  transition: opacity .18s ease .12s;
}

.sbl-09:has(#sbl09-c:checked) .sbl-09__txt,
.sbl-09:has(#sbl09-c:checked) .sbl-09__word {
  opacity: 0;
  transition: opacity .18s ease;
}

.sbl-09:has(#sbl09-c:checked) .sbl-09__fold svg {
  rotate: 180deg;
}

.sbl-09__nav a:hover,
.sbl-09__fold:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-09__nav a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 12%,transparent);
}

.sbl-09__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-09:has(#sbl09-c:focus-visible) .sbl-09__fold {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-09__fold {
  margin-top: auto;
}

.sbl-09__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-09__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-09__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 46ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-09,
    .sbl-09 .sbl-09__txt,
    .sbl-09 .sbl-09__word,
    .sbl-09 .sbl-09__fold svg {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the grid track animates 248px→68px; labels fade on a faster, asymmetrically-delayed transition for native-feeling choreography. */
```
