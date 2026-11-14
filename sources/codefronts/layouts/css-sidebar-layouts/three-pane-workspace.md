---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/three-pane-workspace/"
title: "Three-Pane Productivity Workspace Shell Layout"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The Slack/IDE archetype assembled from this collection's parts: a 68px icon rail (demo 14), a 264px list pane with sticky search (demo 21), and the workspace…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Three-Pane Productivity Workspace Shell Layout
Source: https://codefronts.com/layouts/css-sidebar-layouts/three-pane-workspace/

The Slack/IDE archetype assembled from this collection's parts: a 68px icon rail (demo 14), a 264px list pane with sticky search (demo 21), and the workspace body — grid-template-columns: 72px 280px 1fr as one composed shell, with each pane owning its scroll and the whole thing collapsing progressively as space runs out.
## HTML
```html
<section class="sbl-28">
  <aside class="sbl-28__dock" aria-label="Apps">
    <span class="sbl-28__logo" aria-hidden="true"></span>
    <a href="#" class="sbl-28__app" aria-current="page" aria-label="Messages"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2.5-2.5A8 8 0 1 1 21 12z"/></svg></a>
    <a href="#" class="sbl-28__app" aria-label="Calendar"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 9h18M8 2v4m8-4v4"/></svg></a>
    <a href="#" class="sbl-28__app" aria-label="Tasks"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m4 12 4 4L20 4M4 19h16"/></svg></a>
    <span class="sbl-28__me" aria-hidden="true">JV</span>
  </aside>
  <aside class="sbl-28__list" aria-label="Conversations">
    <div class="sbl-28__search"><label><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" placeholder="Search…" aria-label="Search conversations"></label></div>
    <a href="#" class="sbl-28__convo" aria-current="true"><strong># frontend-guild</strong><em>Priya: subgrid landed in the design sys…</em></a>
    <a href="#" class="sbl-28__convo" data-unread><strong># releases</strong><em>Deploy 4.2.0 is live in production</em></a>
    <a href="#" class="sbl-28__convo"><strong>Marcus Webb</strong><em>You: sounds good, ship it</em></a>
    <a href="#" class="sbl-28__convo"><strong># design-crit</strong><em>Amara: posting Thursday's agenda</em></a>
  </aside>
  <main class="sbl-28__body">
    <header class="sbl-28__head"><strong># frontend-guild</strong><span>128 members</span></header>
    <div class="sbl-28__msgs">
      <p><b>Priya</b> subgrid landed in the design system — sidebar badges finally align. <time>09:12</time></p>
      <p><b>You</b> demo 06 energy. Shipping the workspace shell next. <time>09:15</time></p>
    </div>
    <div class="sbl-28__compose"><input type="text" placeholder="Message # frontend-guild" aria-label="Message input"><button type="button">Send</button></div>
  </main>
</section>
```
## CSS
```css
.sbl-28,
.sbl-28 *,
.sbl-28 *::before,
.sbl-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-28 {
  --dock: oklch(0.14 0.02 265);
  --panel: oklch(0.17 0.018 265);
  --ink: oklch(0.94 0.005 265);
  --mut: oklch(0.63 0.013 265);
  --line: oklch(0.28 0.018 265);
  --accent: oklch(0.7 0.15 265);
  display: grid;
  grid-template-columns: 68px 264px minmax(0,1fr);
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.014 265);
  color: var(--ink);
}

.sbl-28__dock {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 14px 0;
  background: var(--dock);
  border-right: 1px solid var(--line);
}

.sbl-28__logo {
  width: 30px;
  height: 30px;
  border-radius: 9px;
  background: conic-gradient(from 30deg,var(--accent),oklch(0.62 0.16 320));
  margin-bottom: 10px;
}

.sbl-28__app {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  color: var(--mut);
  transition: color .2s ease,background-color .2s ease;
}

.sbl-28__app svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-28__app:hover {
  color: var(--ink);
}

.sbl-28__app[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 15%,transparent);
}

.sbl-28__app:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-28__me {
  margin-top: auto;
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  font: 700 11px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(135deg,var(--accent),oklch(0.58 0.16 320));
}

.sbl-28__list {
  background: var(--panel);
  border-right: 1px solid var(--line);
  overflow-y: auto;
  overscroll-behavior: contain;
}

.sbl-28__search {
  position: sticky;
  top: 0;
  z-index: 2;
  padding: 12px;
  background: var(--panel);
  border-bottom: 1px solid var(--line);
}

.sbl-28__search label {
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 8px;
  height: 36px;
  padding: 0 11px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: oklch(0.14 0.015 265);
}

.sbl-28__search label:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 20%,transparent);
}

.sbl-28__search svg {
  width: 14px;
  height: 14px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 2;
  stroke-linecap: round;
}

.sbl-28__search input {
  min-width: 0;
  border: none;
  background: none;
  color: var(--ink);
  font: 400 13px/1 system-ui,sans-serif;
  outline: none;
}

.sbl-28__convo {
  display: grid;
  gap: 3px;
  padding: 12px 14px;
  border-bottom: 1px solid color-mix(in oklab,var(--line) 55%,transparent);
  text-decoration: none;
  color: inherit;
  transition: background-color .15s ease;
}

.sbl-28__convo:hover {
  background: color-mix(in oklab,var(--ink) 4%,transparent);
}

.sbl-28__convo[aria-current="true"] {
  background: color-mix(in oklab,var(--accent) 11%,transparent);
  box-shadow: inset 2.5px 0 0 var(--accent);
}

.sbl-28__convo:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sbl-28__convo strong {
  font: 600 13px/1.2 system-ui,sans-serif;
}

.sbl-28__convo[data-unread] strong::after {
  content: "";
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--accent);
  margin-left: 7px;
}

.sbl-28__convo em {
  font: 400 12px/1.4 system-ui,sans-serif;
  font-style: normal;
  color: var(--mut);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sbl-28__body {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-width: 0;
}

.sbl-28__head {
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 15px 20px;
  border-bottom: 1px solid var(--line);
  font: 650 14.5px/1 system-ui,sans-serif;
}

.sbl-28__head span {
  font: 400 12px/1 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-28__msgs {
  overflow-y: auto;
  padding: 18px 20px;
  display: grid;
  gap: 14px;
  align-content: start;
}

.sbl-28__msgs p {
  font: 400 13.5px/1.55 system-ui,sans-serif;
  color: var(--mut);
  max-width: 64ch;
}

.sbl-28__msgs b {
  color: var(--ink);
  font-weight: 650;
  margin-right: 6px;
}

.sbl-28__msgs time {
  margin-left: 8px;
  font-size: 11px;
  color: color-mix(in oklab,var(--mut) 65%,transparent);
}

.sbl-28__compose {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  padding: 14px 20px;
  border-top: 1px solid var(--line);
}

.sbl-28__compose input {
  height: 42px;
  padding: 0 14px;
  border-radius: 11px;
  border: 1px solid var(--line);
  background: var(--panel);
  color: var(--ink);
  font: 400 13.5px/1 system-ui,sans-serif;
  outline: none;
}

.sbl-28__compose input:focus-visible {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 20%,transparent);
}

.sbl-28__compose button {
  padding: 0 18px;
  border: none;
  border-radius: 11px;
  background: var(--accent);
  color: #fff;
  font: 600 13px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: filter .2s ease;
}

.sbl-28__compose button:hover {
  filter: brightness(1.1);
}

.sbl-28__compose button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 1000px) {
  .sbl-28 {
    grid-template-columns: 68px 220px minmax(0,1fr);
  }
}

@media (max-width: 820px) {
  .sbl-28 {
    grid-template-columns: 68px minmax(0,1fr);
  }

  .sbl-28__list {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sbl-28__app,
    .sbl-28__convo,
    .sbl-28__compose button {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — three panes composed from demos 14, 21 and 08 on one grid: 68px 264px minmax(0,1fr), collapsing progressively by pane priority. */
```
