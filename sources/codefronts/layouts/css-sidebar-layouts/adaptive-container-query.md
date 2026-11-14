---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/adaptive-container-query/"
title: "Next-Gen Adaptive Sidebar Layout Using CSS Container Queries"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "A sidebar that responds to ITS OWN width, not the viewport: drag the demo's resize handle and watch the nav morph through three densities — full labels+meta,…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Next-Gen Adaptive Sidebar Layout Using CSS Container Queries
Source: https://codefronts.com/layouts/css-sidebar-layouts/adaptive-container-query/

A sidebar that responds to ITS OWN width, not the viewport: drag the demo's resize handle and watch the nav morph through three densities — full labels+meta, labels only, icon rail — driven entirely by @container rules. Drop this component into any column of any app and it self-adapts; media queries could never know.
## HTML
```html
<section class="sbl-29">
  <div class="sbl-29__frame">
    <aside class="sbl-29__rail" aria-label="Library">
      <div class="sbl-29__brand"><span class="sbl-29__mark" aria-hidden="true"></span><span class="sbl-29__name">Shelfspace</span></div>
      <nav class="sbl-29__nav">
        <a href="#" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5zM4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg><span class="sbl-29__lbl">Reading now</span><small class="sbl-29__meta">3</small></a>
        <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h12a2 2 0 0 1 2 2v18l-8-4-8 4V4a2 2 0 0 1 2-2z"/></svg><span class="sbl-29__lbl">Saved</span><small class="sbl-29__meta">47</small></a>
        <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg><span class="sbl-29__lbl">History</span><small class="sbl-29__meta">210</small></a>
        <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="sbl-29__lbl">Settings</span></a>
      </nav>
    </aside>
    <span class="sbl-29__grip" aria-hidden="true"><i></i><i></i><i></i></span>
  </div>
  <main class="sbl-29__main"><h1>Reading now</h1><p>Drag the dotted edge. Full → labels-only → icon rail: three densities from @container rules — the sidebar reads its OWN width, never the viewport's.</p></main>
</section>
```
## CSS
```css
.sbl-29,
.sbl-29 *,
.sbl-29 *::before,
.sbl-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-29 {
  --panel: oklch(0.17 0.016 155);
  --ink: oklch(0.94 0.005 155);
  --mut: oklch(0.64 0.013 155);
  --line: oklch(0.28 0.017 155);
  --accent: oklch(0.78 0.15 160);
  display: flex;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.012 155);
  color: var(--ink);
}

.sbl-29__frame {
  position: relative;
  flex: none;
  resize: horizontal;
  overflow: auto;
  width: 264px;
  min-width: 76px;
  max-width: 340px;
  container: sbl29/inline-size;
  background: var(--panel);
  border-right: 1px solid var(--line);
}

.sbl-29__rail {
  padding: 16px 10px;
  min-height: 100%;
}

.sbl-29__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 4px 10px 16px;
  overflow: hidden;
}

.sbl-29__mark {
  flex: none;
  width: 28px;
  height: 28px;
  border-radius: 9px;
  background: conic-gradient(from 250deg,var(--accent),oklch(0.6 0.14 220));
}

.sbl-29__name {
  font: 700 clamp(13px,6cqi,16px)/1 system-ui,sans-serif;
  white-space: nowrap;
}

.sbl-29__nav {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.sbl-29__nav a {
  display: flex;
  align-items: center;
  gap: 11px;
  min-height: 44px;
  padding: 0 12px;
  border-radius: 11px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  white-space: nowrap;
  transition: background-color .18s ease,color .18s ease;
}

.sbl-29__nav svg {
  flex: none;
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-29__nav a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-29__nav a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 14%,transparent);
}

.sbl-29__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-29__meta {
  margin-left: auto;
  font: 600 11px/1 system-ui,sans-serif;
  color: var(--mut);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
  border-radius: 999px;
  padding: 3px 8px;
}

@container sbl29 (max-width: 220px) {
  .sbl-29__meta {
    display: none;
  }
}

@container sbl29 (max-width: 120px) {
  .sbl-29__lbl,
    .sbl-29__name {
    display: none;
  }

  .sbl-29__nav a {
    justify-content: center;
    padding: 0;
    width: 44px;
    margin-inline: auto;
  }

  .sbl-29__brand {
    justify-content: center;
    padding-inline: 0;
  }
}

.sbl-29__grip {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 14px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  align-items: center;
  justify-content: center;
  cursor: col-resize;
  opacity: .5;
}

.sbl-29__grip:hover {
  opacity: 1;
}

.sbl-29__grip i {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: var(--mut);
}

.sbl-29 > .sbl-29__frame + .sbl-29__main,
.sbl-29__main {
  flex: 1;
  min-width: 0;
  padding: 32px;
  overflow-y: auto;
}

.sbl-29__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-29__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.65;
  max-width: 50ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-29__nav a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — container:sbl29/inline-size makes the rail's own width queryable; @container rules morph it through three densities as you drag. */
```
