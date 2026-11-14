---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-breadcrumb-navigation/"
title: "CSS Breadcrumb Navigation"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A versatile breadcrumb navigation component with three style variants: classic arrow separators, rounded pill badges, and a slash-separated minimal style."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Breadcrumb Navigation
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-breadcrumb-navigation/

A versatile breadcrumb navigation component with three style variants: classic arrow separators, rounded pill badges, and a slash-separated minimal style. Breadcrumbs improve site navigation hierarchy clarity and are critical for SEO structured data markup.
## HTML
```html
<div class="nav-09">

  <div class="nav-09__section">
    <p class="nav-09__section-label">Chevron Separator (default)</p>
    <ol class="nav-09__crumb" aria-label="Breadcrumb">
      <li><a href="#">Home</a></li>
      <li>
        <svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
        <a href="#">Documentation</a>
      </li>
      <li>
        <svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
        <a href="#">CSS Guides</a>
      </li>
      <li>
        <svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
        <span aria-current="page">Navigation Patterns</span>
      </li>
    </ol>
  </div>

  <div class="nav-09__section">
    <p class="nav-09__section-label">Slash Separator</p>
    <ol class="nav-09__crumb nav-09__crumb--slash" aria-label="Breadcrumb">
      <li><a href="#">Dashboard</a></li>
      <li><a href="#">Projects</a></li>
      <li><a href="#">Website Redesign</a></li>
      <li><span aria-current="page">Assets</span></li>
    </ol>
  </div>

  <div class="nav-09__section">
    <p class="nav-09__section-label">With Icons</p>
    <ol class="nav-09__crumb" aria-label="Breadcrumb">
      <li>
        <a href="#" style="display:flex;align-items:center">
          <svg class="nav-09__crumb-icon" viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>Home
        </a>
      </li>
      <li>
        <svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
        <a href="#" style="display:flex;align-items:center">
          <svg class="nav-09__crumb-icon" viewBox="0 0 24 24"><path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/></svg>Components
        </a>
      </li>
      <li>
        <svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
        <span aria-current="page" style="display:flex;align-items:center">
          <svg class="nav-09__crumb-icon" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>Navigation
        </span>
      </li>
    </ol>
  </div>

  <div class="nav-09__section">
    <p class="nav-09__section-label">Filled Pill Style</p>
    <ol class="nav-09__crumb nav-09__crumb--filled" aria-label="Breadcrumb">
      <li><a href="#">Home</a></li>
      <li>
        <svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
        <a href="#">Products</a>
      </li>
      <li>
        <svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
        <span aria-current="page">Navigation Bars</span>
      </li>
    </ol>
  </div>

  <div class="nav-09__section">
    <p class="nav-09__section-label">Mobile Back Button</p>
    <a href="#" class="nav-09__back" aria-label="Back to CSS Guides">
      <svg viewBox="0 0 24 24"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
      CSS Guides
    </a>
  </div>

  <div class="nav-09__section">
    <p class="nav-09__section-label">In Context — Documentation Layout</p>
    <div class="nav-09__doc">
      <div class="nav-09__doc-bar">
        <ol class="nav-09__crumb" style="background:transparent;border:none;padding:0" aria-label="Breadcrumb">
          <li><a href="#">Docs</a></li>
          <li><svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg><a href="#">Navigation</a></li>
          <li><svg class="nav-09__sep" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg><span aria-current="page">Breadcrumbs</span></li>
        </ol>
      </div>
      <div class="nav-09__doc-body">
        <h2>Breadcrumb Navigation</h2>
        <p>Breadcrumbs show users where they are in the site hierarchy and let them jump up to any ancestor page. Built entirely with CSS using <code>flex</code>, pseudo-elements for separators, and <code>:hover</code> transitions — no JavaScript needed.</p>
      </div>
    </div>
  </div>

</div>
```
## CSS
```css
.nav-09,
.nav-09 *,
.nav-09 *::before,
.nav-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-09 ::selection {
  background: #0d9488;
  color: #fff;
}

.nav-09 {
  --bg: #f0fdfa;
  --surface: #fff;
  --border: #ccfbf1;
  --text: #0f172a;
  --muted: #64748b;
  --link: #0d9488;
  --link-h: #0f766e;
  font-family: 'Source Sans 3',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 60px 24px;
  gap: 48px;
}

.nav-09__section {
  width: 100%;
  max-width: 700px;
}

.nav-09__section-label {
  font-size: .7rem;
  font-weight: 700;
  color: #0d9488;
  letter-spacing: .1em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
/* base breadcrumb */

.nav-09__crumb {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0;
  list-style: none;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 12px 18px;
}

.nav-09__crumb li {
  display: flex;
  align-items: center;
}

.nav-09__crumb li a {
  color: var(--link);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 500;
  padding: 3px 6px;
  border-radius: 5px;
  transition: background .15s,color .15s;
}

.nav-09__crumb li a:hover {
  background: #ccfbf1;
  color: var(--link-h);
}

.nav-09__crumb li span {
  font-size: .9rem;
  font-weight: 600;
  color: var(--text);
  padding: 3px 6px;
}
/* separator with chevron */

.nav-09__sep {
  width: 16px;
  height: 16px;
  margin: 0 2px;
  opacity: .35;
  flex-shrink: 0;
  stroke: var(--text);
  fill: none;
  stroke-width: 2;
}
/* separator with slash */

.nav-09__crumb--slash li:not(:last-child)::after {
  content: '/';
  margin: 0 8px;
  color: rgba(0,0,0,.2);
  font-size: .9rem;
}

.nav-09__crumb--slash .nav-09__sep {
  display: none;
}
/* separator with dot */

.nav-09__crumb--dot li:not(:last-child)::after {
  content: '·';
  margin: 0 8px;
  color: rgba(0,0,0,.25);
  font-size: 1.2rem;
  line-height: 1;
}

.nav-09__crumb--dot .nav-09__sep {
  display: none;
}
/* icons in crumbs */

.nav-09__crumb-icon {
  width: 14px;
  height: 14px;
  margin-right: 5px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  flex-shrink: 0;
}
/* filled crumb style */

.nav-09__crumb--filled {
  background: transparent;
  border: none;
  padding: 0;
  gap: 4px;
}

.nav-09__crumb--filled li a {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 6px 12px;
  border-radius: 8px;
  display: flex;
  align-items: center;
}

.nav-09__crumb--filled li a:hover {
  background: #ccfbf1;
  border-color: #5eead4;
}

.nav-09__crumb--filled li span {
  background: var(--link);
  color: #fff;
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid transparent;
}

.nav-09__crumb--filled .nav-09__sep {
  stroke: var(--muted);
}
/* compact / mobile crumb with back only */

.nav-09__back {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--link);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 600;
  padding: 8px 14px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--surface);
  transition: background .15s,border-color .15s;
}

.nav-09__back:hover {
  background: #ccfbf1;
  border-color: #5eead4;
}

.nav-09__back svg {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2.5;
}
/* doc layout */

.nav-09__doc {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
}

.nav-09__doc-bar {
  padding: 16px 24px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-09__doc-body {
  padding: 28px 24px;
}

.nav-09__doc-body h2 {
  font-size: 1.375rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 10px;
}

.nav-09__doc-body p {
  font-size: .9375rem;
  color: var(--muted);
  line-height: 1.7;
}

@media (prefers-reduced-motion: reduce) {
  .nav-09__crumb li a,
    .nav-09__back {
    transition: none;
  }
}
```
