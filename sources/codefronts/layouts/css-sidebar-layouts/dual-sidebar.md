---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/dual-sidebar/"
title: "Dual Sidebar App Shell Layout with Left Nav and Right Context Panel"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The Notion/Discord-class shell: primary navigation on the left, a contextual detail panel on the right, content in the middle — a 3-column grid where the…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dual Sidebar App Shell Layout with Left Nav and Right Context Panel
Source: https://codefronts.com/layouts/css-sidebar-layouts/dual-sidebar/

The Notion/Discord-class shell: primary navigation on the left, a contextual detail panel on the right, content in the middle — a 3-column grid where the right panel collapses away on narrower viewports (media query) while left nav survives, encoding the real information hierarchy of these products.
## HTML
```html
<section class="sbl-13">
  <aside class="sbl-13__nav" aria-label="Workspace">
    <div class="sbl-13__ws"><span class="sbl-13__mark" aria-hidden="true">L</span>Loomcraft</div>
    <div class="sbl-13__grp">Projects</div>
    <nav>
      <a href="#" aria-current="page"># brand-refresh <span class="sbl-13__badge">3</span></a>
      <a href="#"># website-v4</a>
      <a href="#"># mobile-app <span class="sbl-13__badge">12</span></a>
    </nav>
    <div class="sbl-13__grp">Team</div>
    <nav><a href="#"># design-crit</a><a href="#"># announcements</a></nav>
  </aside>
  <main class="sbl-13__feed">
    <h1># brand-refresh</h1>
    <p>The center track is <code>minmax(0,1fr)</code> — wide content shrinks and scrolls instead of crushing the context panel. Resize under 1100px: the right panel yields first, the nav survives.</p>
  </main>
  <aside class="sbl-13__ctx" aria-label="Activity">
    <h2>Activity</h2>
    <ol class="sbl-13__timeline">
      <li><span class="sbl-13__avatar" aria-hidden="true">PR</span><div><strong>Priya</strong> shipped the new wordmark<time>2h ago</time></div></li>
      <li><span class="sbl-13__avatar" aria-hidden="true">MW</span><div><strong>Marcus</strong> commented on palette v3<time>4h ago</time></div></li>
      <li><span class="sbl-13__avatar" aria-hidden="true">AO</span><div><strong>Amara</strong> uploaded 6 explorations<time>Yesterday</time></div></li>
    </ol>
  </aside>
</section>
```
## CSS
```css
.sbl-13,
.sbl-13 *,
.sbl-13 *::before,
.sbl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-13 {
  --panel: oklch(0.17 0.018 290);
  --ink: oklch(0.93 0.005 290);
  --mut: oklch(0.63 0.012 290);
  --line: oklch(0.28 0.018 290);
  --accent: oklch(0.7 0.16 300);
  display: grid;
  grid-template-columns: 232px minmax(0,1fr) 280px;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.14 0.014 290);
  color: var(--ink);
}

.sbl-13__nav {
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 16px 10px;
  overflow-y: auto;
}

.sbl-13__ws {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 14.5px/1 system-ui,sans-serif;
  padding: 2px 10px 16px;
}

.sbl-13__mark {
  display: grid;
  place-items: center;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  font: 700 12px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(135deg,var(--accent),oklch(0.6 0.18 260));
}

.sbl-13__grp {
  font: 600 10.5px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .09em;
  color: var(--mut);
  padding: 14px 10px 6px;
}

.sbl-13__nav nav {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.sbl-13__nav nav a {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 8px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.sbl-13__nav nav a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-13__nav nav a[aria-current="page"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 17%,transparent);
}

.sbl-13__nav nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-13__badge {
  margin-left: auto;
  font: 700 10.5px/1 system-ui,sans-serif;
  color: #fff;
  background: var(--accent);
  border-radius: 999px;
  padding: 3px 7px;
}

.sbl-13__feed {
  overflow-y: auto;
  padding: 30px 34px;
}

.sbl-13__feed h1 {
  font: 650 20px/1.2 system-ui,sans-serif;
  margin-bottom: 12px;
}

.sbl-13__feed p {
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
  text-wrap: pretty;
}

.sbl-13__feed code {
  font: 500 12.5px ui-monospace,Menlo,monospace;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.sbl-13__ctx {
  border-left: 1px solid var(--line);
  background: var(--panel);
  padding: 20px 16px;
  overflow-y: auto;
}

.sbl-13__ctx h2 {
  font: 600 12px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: var(--mut);
  margin-bottom: 16px;
}

.sbl-13__timeline {
  list-style: none;
  display: grid;
  gap: 0;
}

.sbl-13__timeline li {
  position: relative;
  display: grid;
  grid-template-columns: 28px 1fr;
  gap: 12px;
  padding-bottom: 20px;
}

.sbl-13__timeline li:not(:last-child)::before {
  content: "";
  position: absolute;
  left: 13.5px;
  top: 32px;
  bottom: 2px;
  width: 1px;
  background: var(--line);
}

.sbl-13__avatar {
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  font: 700 9.5px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(135deg,oklch(0.6 0.15 300),oklch(0.55 0.15 240));
}

.sbl-13__timeline strong {
  font-weight: 600;
}

.sbl-13__timeline div {
  font: 400 12.5px/1.5 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-13__timeline time {
  display: block;
  font-size: 11px;
  margin-top: 2px;
  color: color-mix(in oklab,var(--mut) 70%,transparent);
}

@media (max-width: 1100px) {
  .sbl-13 {
    grid-template-columns: 232px minmax(0,1fr);
  }

  .sbl-13__ctx {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sbl-13__nav nav a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a 3-column grid whose center track is minmax(0,1fr) so wide content can't crush the panels; the context panel yields first at 1100px. */
```
