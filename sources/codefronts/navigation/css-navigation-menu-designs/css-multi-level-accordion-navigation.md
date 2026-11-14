---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-multi-level-accordion-navigation/"
title: "CSS Multi-Level Accordion Navigation"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A hierarchical accordion sidebar navigation with smooth expand/collapse animations, nested sub-menus, and visual depth indicators."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Multi-Level Accordion Navigation
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-multi-level-accordion-navigation/

A hierarchical accordion sidebar navigation with smooth expand/collapse animations, nested sub-menus, and visual depth indicators. Built with CSS `max-height` transitions and hidden checkbox inputs — ideal for documentation sites and complex application navigation trees.
## HTML
```html
<div class="nav-12">
  <input type="checkbox" id="nav-12-c1" checked>
  <input type="checkbox" id="nav-12-c2">
  <input type="checkbox" id="nav-12-c3">
  <input type="checkbox" id="nav-12-c4">
  <aside class="nav-12__sidebar" role="navigation" aria-label="Sidebar tree">
    <div class="nav-12__sidebar-head">
      <div class="nav-12__sidebar-icon">
        <svg viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg>
      </div>
      <span class="nav-12__sidebar-logo"><span>Dev</span>Docs</span>
    </div>
    <div class="nav-12__search">
      <div class="nav-12__search-inner">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <span>Search docs…</span>
      </div>
    </div>
    <nav class="nav-12__tree">
      <ul>
        <li class="nav-12__item"><a href="#" class="nav-12__active">
          <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>Introduction</a>
        </li>
        <li class="nav-12__item">
          <label for="nav-12-c1" class="nav-12__label--1">
            <svg viewBox="0 0 24 24"><path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/></svg>
            Getting Started
            <svg class="nav-12__chevron" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
          </label>
          <ul class="nav-12__sub nav-12__sub--1">
            <li><a href="#">Installation</a></li>
            <li><a href="#">Quick Start Guide</a></li>
            <li><a href="#">Project Structure</a></li>
            <li class="nav-12__item">
              <label for="nav-12-c2" class="nav-12__label--2" style="padding:7px 8px 7px 16px;font-size:.8125rem">
                Configuration
                <svg class="nav-12__chevron" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
              </label>
              <ul class="nav-12__sub nav-12__sub--2">
                <li><a href="#">Environment Variables</a></li>
                <li><a href="#">TypeScript Config</a></li>
                <li><a href="#">ESLint Setup</a></li>
              </ul>
            </li>
          </ul>
        </li>
        <li class="nav-12__item">
          <label for="nav-12-c3" class="nav-12__label--3">
            <svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
            Components
            <svg class="nav-12__chevron" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
          </label>
          <ul class="nav-12__sub nav-12__sub--3">
            <li><a href="#">Button</a></li>
            <li><a href="#">Input</a></li>
            <li><a href="#">Modal</a></li>
            <li><a href="#">Navigation</a></li>
            <li><a href="#">Table</a></li>
          </ul>
        </li>
        <li class="nav-12__item">
          <label for="nav-12-c4" class="nav-12__label--4">
            <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            API Reference
            <svg class="nav-12__chevron" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
          </label>
          <ul class="nav-12__sub nav-12__sub--4">
            <li><a href="#">Authentication</a></li>
            <li><a href="#">Endpoints</a></li>
            <li><a href="#">Webhooks</a></li>
          </ul>
        </li>
        <li class="nav-12__item"><a href="#"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>FAQ</a></li>
      </ul>
    </nav>
  </aside>
  <main class="nav-12__main">
    <h2>Multi-Level Accordion Navigation</h2>
    <p>The tree sidebar uses hidden <code>&lt;input type="checkbox"&gt;</code> elements toggled by <code>&lt;label&gt;</code> siblings. Each sub-list transitions from <code>max-height: 0</code> to a large value, creating a smooth accordion without JavaScript.</p>
    <div class="nav-12__code-block">
<span class="cmt">/* Chevron rotates when section is open */</span>
<br>#nav-12-c1:checked ~ * .nav-12__chevron {
<br>&nbsp;&nbsp;<span class="kw">transform</span>: rotate(<span class="str">90deg</span>);
<br>}
<br><span class="cmt">/* Sub-list expands */</span>
<br>#nav-12-c1:checked ~ * .nav-12__sub--1 {
<br>&nbsp;&nbsp;<span class="kw">max-height</span>: <span class="str">500px</span>;
<br>}
    </div>
  </main>
</div>
```
## CSS
```css
.nav-12,
.nav-12 *,
.nav-12 *::before,
.nav-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-12 ::selection {
  background: #0891b2;
  color: #fff;
}

.nav-12 {
  --bg: #f8fafc;
  --sidebar: #fff;
  --border: #e2e8f0;
  --text: #1e293b;
  --muted: #64748b;
  --accent: #0891b2;
  --accent-bg: #ecfeff;
  font-family: 'Rubik',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
}
/* accordion inputs */

.nav-12 input[type="checkbox"] {
  display: none;
}

.nav-12__sidebar {
  width: 260px;
  min-height: 100vh;
  background: var(--sidebar);
  border-right: 1px solid var(--border);
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
}

.nav-12__sidebar-head {
  padding: 20px 16px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-12__sidebar-logo {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
}

.nav-12__sidebar-logo span {
  color: var(--accent);
}

.nav-12__sidebar-icon {
  width: 30px;
  height: 30px;
  border-radius: 7px;
  background: var(--accent);
  display: grid;
  place-items: center;
}

.nav-12__sidebar-icon svg {
  width: 16px;
  height: 16px;
  stroke: #fff;
  fill: none;
  stroke-width: 2;
}
/* search */

.nav-12__search {
  padding: 12px 12px;
  border-bottom: 1px solid var(--border);
}

.nav-12__search-inner {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 12px;
}

.nav-12__search-inner svg {
  width: 15px;
  height: 15px;
  stroke: var(--muted);
  fill: none;
  stroke-width: 2;
  flex-shrink: 0;
}

.nav-12__search-inner span {
  font-size: .8125rem;
  color: var(--muted);
}

.nav-12__tree {
  padding: 10px 8px;
  flex: 1;
  overflow-y: auto;
}

.nav-12__tree > ul {
  list-style: none;
}
/* top-level item */

.nav-12__item {
  margin-bottom: 2px;
}

.nav-12__item > label,
.nav-12__item > a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 9px 8px;
  border-radius: 8px;
  font-size: .875rem;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  transition: background .15s,color .15s;
  user-select: none;
  text-decoration: none;
}

.nav-12__item > label:hover,
.nav-12__item > a:hover {
  background: var(--bg);
  color: var(--text);
}

.nav-12__item > label svg,
.nav-12__item > a svg {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  flex-shrink: 0;
  opacity: .7;
}

.nav-12__item > a.nav-12__active {
  background: var(--accent-bg);
  color: var(--accent);
  font-weight: 600;
}

.nav-12__item > a.nav-12__active svg {
  opacity: 1;
}
/* chevron */

.nav-12__chevron {
  margin-left: auto;
  width: 14px;
  height: 14px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  transition: transform .22s ease;
  opacity: .5;
}
/* sub list */

.nav-12__sub {
  max-height: 0;
  overflow: hidden;
  list-style: none;
  padding-left: 22px;
  transition: max-height .3s ease;
}

.nav-12__sub a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 7px 8px 7px 16px;
  border-radius: 8px;
  font-size: .8125rem;
  font-weight: 500;
  color: var(--muted);
  text-decoration: none;
  transition: background .15s,color .15s;
  position: relative;
}

.nav-12__sub a::before {
  content: '';
  position: absolute;
  left: 2px;
  top: 50%;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--border);
  transform: translateY(-50%);
  transition: background .15s;
}

.nav-12__sub a:hover {
  background: var(--bg);
  color: var(--text);
}

.nav-12__sub a:hover::before {
  background: var(--muted);
}

.nav-12__sub a.nav-12__active {
  color: var(--accent);
}

.nav-12__sub a.nav-12__active::before {
  background: var(--accent);
}
/* nested sub */

.nav-12__sub .nav-12__sub {
  padding-left: 16px;
}
/* checked open states */

#nav-12-c1:checked ~ * .nav-12__sub--1 {
  max-height: 500px;
}

#nav-12-c1:checked ~ * .nav-12__label--1 .nav-12__chevron {
  transform: rotate(90deg);
}

#nav-12-c2:checked ~ * .nav-12__sub--2 {
  max-height: 300px;
}

#nav-12-c2:checked ~ * .nav-12__label--2 .nav-12__chevron {
  transform: rotate(90deg);
}

#nav-12-c3:checked ~ * .nav-12__sub--3 {
  max-height: 300px;
}

#nav-12-c3:checked ~ * .nav-12__label--3 .nav-12__chevron {
  transform: rotate(90deg);
}

#nav-12-c4:checked ~ * .nav-12__sub--4 {
  max-height: 300px;
}

#nav-12-c4:checked ~ * .nav-12__label--4 .nav-12__chevron {
  transform: rotate(90deg);
}
/* main content */

.nav-12__main {
  flex: 1;
  padding: 32px;
  overflow-y: auto;
}

.nav-12__main h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 16px;
}

.nav-12__main p {
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 16px;
  font-size: .9375rem;
}

.nav-12__code-block {
  background: #0f172a;
  border-radius: 10px;
  padding: 20px 22px;
  font-family: 'IBM Plex Mono',monospace;
  font-size: .8rem;
  color: #94a3b8;
  line-height: 1.7;
}

.nav-12__code-block .kw {
  color: #7dd3fc;
}

.nav-12__code-block .str {
  color: #86efac;
}

.nav-12__code-block .cmt {
  color: #475569;
}

@media (max-width: 600px) {
  .nav-12__sidebar {
    width: 220px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-12__sub,
    .nav-12__chevron {
    transition: none;
  }
}
```
