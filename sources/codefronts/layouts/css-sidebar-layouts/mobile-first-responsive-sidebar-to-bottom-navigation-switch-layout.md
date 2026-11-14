---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/mobile-first-responsive-sidebar-to-bottom-navigation-switch-layout/"
title: "Mobile-First Responsive Sidebar to Bottom Navigation Switch Layout"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "One <nav>, two personalities: below 768px it's an iOS-style bottom tab bar with safe-area padding; on desktop the very same markup stands up into a full left…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile-First Responsive Sidebar to Bottom Navigation Switch Layout
Source: https://codefronts.com/layouts/css-sidebar-layouts/mobile-first-responsive-sidebar-to-bottom-navigation-switch-layout/

One <nav>, two personalities: below 768px it's an iOS-style bottom tab bar with safe-area padding; on desktop the very same markup stands up into a full left sidebar with labels beside icons. No duplicate nav trees to keep in sync, no JS resize listeners — a grid-area swap and a flex-direction flip do all of it.
## HTML
```html
<section class="sbl-05">
  <nav class="sbl-05__bar" aria-label="Primary">
    <a class="sbl-05__tab" href="#" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><span>Home</span></a>
    <a class="sbl-05__tab" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Search</span></a>
    <a class="sbl-05__tab" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 9h18M8 2v4m8-4v4"/></svg><span>Bookings</span></a>
    <a class="sbl-05__tab" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 8-3 8h18s-3-1-3-8m-4.3 11a2 2 0 0 1-3.4 0"/></svg><span>Alerts</span></a>
    <a class="sbl-05__tab" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-3.9 3.6-6.5 8-6.5s8 2.6 8 6.5"/></svg><span>Profile</span></a>
  </nav>
  <main class="sbl-05__main"><h1>Today</h1><p>Resize the viewport — under 768px this same nav element becomes a bottom tab bar with safe-area padding.</p></main>
</section>
```
## CSS
```css
.sbl-05,
.sbl-05 *,
.sbl-05 *::before,
.sbl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-05 {
  --panel: oklch(0.17 0.02 250);
  --ink: oklch(0.93 0.005 250);
  --mut: oklch(0.62 0.012 250);
  --line: oklch(0.28 0.02 250);
  --accent: oklch(0.75 0.14 200);
  display: grid;
  grid-template-areas: "main" "nav";
  grid-template-rows: 1fr auto;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.015 250);
  color: var(--ink);
}

.sbl-05__bar {
  grid-area: nav;
  display: flex;
  flex-direction: row;
  background: var(--panel);
  border-top: 1px solid var(--line);
  padding: 6px 8px calc(6px + env(safe-area-inset-bottom,0px));
}

.sbl-05__tab {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  min-height: 48px;
  border-radius: 12px;
  font: 500 10.5px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s ease,background-color .2s ease;
}

.sbl-05__tab svg {
  width: 21px;
  height: 21px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-05__tab:hover {
  color: var(--ink);
}

.sbl-05__tab[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 14%,transparent);
}

.sbl-05__tab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-05__main {
  grid-area: main;
  overflow-y: auto;
  padding: 28px;
}

.sbl-05__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-05__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 46ch;
  text-wrap: pretty;
}

@media (min-width: 768px) {
  .sbl-05 {
    grid-template-areas: "nav main";
    grid-template-columns: 248px 1fr;
    grid-template-rows: 1fr;
  }

  .sbl-05__bar {
    flex-direction: column;
    gap: 2px;
    justify-content: flex-start;
    border-top: none;
    border-right: 1px solid var(--line);
    padding: 18px 12px;
  }

  .sbl-05__tab {
    flex: 0 0 auto;
    flex-direction: row;
    justify-content: flex-start;
    gap: 12px;
    min-height: 44px;
    padding: 0 14px;
    font-size: 14px;
  }

  .sbl-05__tab[aria-current="page"] {
    box-shadow: inset 2px 0 0 var(--accent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sbl-05__tab {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one <nav> re-maps between bottom tab bar and left sidebar via grid-template-areas + a flex-direction flip at 768px. */
```
