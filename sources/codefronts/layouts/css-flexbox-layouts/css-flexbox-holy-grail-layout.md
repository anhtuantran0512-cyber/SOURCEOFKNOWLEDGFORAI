---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-holy-grail-layout/"
title: "CSS Flexbox Holy Grail Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A classic holy grail layout — fixed header, footer, left sidebar, right aside, and expanding main column — built entirely with nested flex containers and no…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Holy Grail Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-holy-grail-layout/

A classic holy grail layout — fixed header, footer, left sidebar, right aside, and expanding main column — built entirely with nested flex containers and no CSS Grid.
## HTML
```html
<div class="fl-01">
  <div class="fl-01__wrapper">

    <!-- Header -->
    <header class="fl-01__header">
      <div class="fl-01__logo">Holy<span>Grail</span></div>
      <ul class="fl-01__nav">
        <li><a href="#">Docs</a></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </header>

    <!-- Body Row -->
    <div class="fl-01__body">

      <!-- Left Sidebar -->
      <nav class="fl-01__sidebar">
        <div class="fl-01__sidebar-label">Navigation</div>
        <div class="fl-01__sidebar-item is-active">
          <div class="fl-01__sidebar-icon"></div> Dashboard
        </div>
        <div class="fl-01__sidebar-item">
          <div class="fl-01__sidebar-icon"></div> Analytics
        </div>
        <div class="fl-01__sidebar-item">
          <div class="fl-01__sidebar-icon"></div> Content
        </div>
        <div class="fl-01__sidebar-item">
          <div class="fl-01__sidebar-icon"></div> Settings
        </div>
        <div class="fl-01__sidebar-label" style="margin-top:8px">Library</div>
        <div class="fl-01__sidebar-item">
          <div class="fl-01__sidebar-icon"></div> Media
        </div>
        <div class="fl-01__sidebar-item">
          <div class="fl-01__sidebar-icon"></div> Files
        </div>
      </nav>

      <!-- Main Content -->
      <main class="fl-01__main">
        <div class="fl-01__breadcrumb">Home › Dashboard › <span>Overview</span></div>
        <h1 class="fl-01__main-title">Holy Grail Layout<br>with CSS Flexbox</h1>
        <div class="fl-01__meta">
          <div class="fl-01__tag">Pure CSS</div>
          <span>Header · Sidebar · Content · Aside · Footer</span>
        </div>
        <div class="fl-01__content-body">
          <p>The Holy Grail layout — a full-height page with a header, sticky footer, left sidebar, right aside, and fluid centre — solved the hardest layout problem of the float era. Flexbox reduces it to two nested flex containers: an outer <code>column</code> wrapper and an inner <code>row</code> middle section.</p>
          <p>The outer wrapper uses <code>flex-direction: column</code> and <code>min-height: 100%</code>. The middle row gets <code>flex: 1</code> to fill remaining space, while sidebars use a fixed <code>width</code> with <code>flex-shrink: 0</code> to resist compression.</p>
        </div>
        <div class="fl-01__divider"></div>
        <div class="fl-01__cards">
          <div class="fl-01__card">
            <div class="fl-01__card-label">flex: 1</div>
            <div class="fl-01__card-value">Main</div>
            <div class="fl-01__card-delta">Fills remaining width</div>
          </div>
          <div class="fl-01__card">
            <div class="fl-01__card-label">flex-shrink: 0</div>
            <div class="fl-01__card-value">Sides</div>
            <div class="fl-01__card-delta">Fixed at 180px each</div>
          </div>
          <div class="fl-01__card">
            <div class="fl-01__card-label">flex-direction</div>
            <div class="fl-01__card-value">Column</div>
            <div class="fl-01__card-delta">Header stacks on footer</div>
          </div>
        </div>
      </main>

      <!-- Right Aside -->
      <aside class="fl-01__aside">
        <div class="fl-01__aside-title">Flex Properties</div>
        <div class="fl-01__aside-item">
          <div class="fl-01__aside-name">flex-grow</div>
          <div class="fl-01__aside-sub">Fills free space</div>
          <div class="fl-01__aside-bar-wrap">
            <div class="fl-01__aside-bar" style="width:90%"></div>
          </div>
        </div>
        <div class="fl-01__aside-item">
          <div class="fl-01__aside-name">flex-shrink</div>
          <div class="fl-01__aside-sub">Resists squish</div>
          <div class="fl-01__aside-bar-wrap">
            <div class="fl-01__aside-bar" style="width:60%"></div>
          </div>
        </div>
        <div class="fl-01__aside-item">
          <div class="fl-01__aside-name">flex-basis</div>
          <div class="fl-01__aside-sub">Starting size</div>
          <div class="fl-01__aside-bar-wrap">
            <div class="fl-01__aside-bar" style="width:75%"></div>
          </div>
        </div>
        <div class="fl-01__aside-item">
          <div class="fl-01__aside-name">align-items</div>
          <div class="fl-01__aside-sub">Cross-axis align</div>
          <div class="fl-01__aside-bar-wrap">
            <div class="fl-01__aside-bar" style="width:50%"></div>
          </div>
        </div>
      </aside>

    </div><!-- /.fl-01__body -->

    <!-- Footer -->
    <footer class="fl-01__footer">
      <span>© 2025 HolyGrail Demo · Flexbox</span>
      <ul class="fl-01__footer-links">
        <li><a href="#">Privacy</a></li>
        <li><a href="#">Terms</a></li>
        <li><a href="#">Sitemap</a></li>
      </ul>
    </footer>

  </div>
</div>
```
## CSS
```css
.fl-01,
.fl-01 *,
.fl-01 *::before,
.fl-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-01 ::selection {
  background: #6c63ff;
  color: #fff;
}

.fl-01 {
  --ink: #1a1a2e;
  --muted: #6b7280;
  --accent: #6c63ff;
  --accent2: #f59e0b;
  --surface: #f8f7ff;
  --border: #e5e3ff;
  --header-bg: #1a1a2e;
  --sidebar-bg: #f0eeff;
  --aside-bg: #fff8ed;
  --content-bg: #ffffff;
  --footer-bg: #1a1a2e;
  font-family: 'Inter', sans-serif;
  background: var(--surface);
  min-height: 500px;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--border);
}
/* Holy Grail: column flex on outer, row flex on middle */

.fl-01__wrapper {
  display: flex;
  flex-direction: column;
  min-height: 500px;
}
/* ── Header ── */

.fl-01__header {
  background: var(--header-bg);
  color: #fff;
  padding: 14px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
}

.fl-01__logo {
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
  letter-spacing: -0.02em;
}

.fl-01__logo span {
  color: var(--accent2);
}

.fl-01__nav {
  display: flex;
  gap: 20px;
  list-style: none;
}

.fl-01__nav li a {
  color: rgba(255,255,255,0.7);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transition: color 0.2s;
}

.fl-01__nav li a:hover {
  color: #fff;
}
/* ── Middle row: sidebar + main + aside ── */

.fl-01__body {
  display: flex;
  flex: 1;
  min-height: 0;
}
/* ── Left Sidebar ── */

.fl-01__sidebar {
  background: var(--sidebar-bg);
  width: 180px;
  flex-shrink: 0;
  padding: 20px 16px;
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.fl-01__sidebar-label {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 8px 8px 4px;
}

.fl-01__sidebar-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--ink);
  cursor: pointer;
  transition: background 0.15s;
}

.fl-01__sidebar-item:hover {
  background: rgba(108,99,255,0.1);
}

.fl-01__sidebar-item.is-active {
  background: var(--accent);
  color: #fff;
}

.fl-01__sidebar-icon {
  width: 18px;
  height: 18px;
  border-radius: 4px;
  background: currentColor;
  opacity: 0.25;
}

.fl-01__sidebar-item.is-active .fl-01__sidebar-icon {
  opacity: 0.6;
  background: #fff;
}
/* ── Main Content ── */

.fl-01__main {
  flex: 1;
  background: var(--content-bg);
  padding: 24px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.fl-01__breadcrumb {
  font-size: 0.72rem;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 6px;
}

.fl-01__breadcrumb span {
  color: var(--ink);
  font-weight: 600;
}

.fl-01__main-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem;
  color: var(--ink);
  line-height: 1.3;
}

.fl-01__meta {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.75rem;
  color: var(--muted);
}

.fl-01__tag {
  background: rgba(108,99,255,0.1);
  color: var(--accent);
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 20px;
  font-size: 0.7rem;
}

.fl-01__content-body {
  font-size: 0.85rem;
  color: var(--muted);
  line-height: 1.7;
}

.fl-01__content-body p + p {
  margin-top: 10px;
}

.fl-01__divider {
  height: 1px;
  background: var(--border);
}

.fl-01__cards {
  display: flex;
  gap: 12px;
}

.fl-01__card {
  flex: 1;
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
}

.fl-01__card-label {
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 6px;
}

.fl-01__card-value {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--ink);
}

.fl-01__card-delta {
  font-size: 0.72rem;
  color: #10b981;
  font-weight: 600;
  margin-top: 2px;
}
/* ── Right Aside ── */

.fl-01__aside {
  background: var(--aside-bg);
  width: 180px;
  flex-shrink: 0;
  padding: 20px 16px;
  border-left: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.fl-01__aside-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
}

.fl-01__aside-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 10px;
  background: #fff;
  border-radius: 8px;
  border: 1px solid #fde68a;
}

.fl-01__aside-name {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--ink);
}

.fl-01__aside-sub {
  font-size: 0.7rem;
  color: var(--muted);
}

.fl-01__aside-bar-wrap {
  height: 4px;
  background: #fde68a;
  border-radius: 4px;
  overflow: hidden;
  margin-top: 2px;
}

.fl-01__aside-bar {
  height: 100%;
  background: var(--accent2);
  border-radius: 4px;
  animation: fl-01-bar-grow 1.2s ease both;
}

@keyframes fl-01-bar-grow {
  from {
    width: 0;
  }
}
/* ── Footer ── */

.fl-01__footer {
  background: var(--footer-bg);
  color: rgba(255,255,255,0.5);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.72rem;
  flex-shrink: 0;
}

.fl-01__footer-links {
  display: flex;
  gap: 16px;
  list-style: none;
}

.fl-01__footer-links a {
  color: rgba(255,255,255,0.4);
  text-decoration: none;
}

.fl-01__footer-links a:hover {
  color: #fff;
}
/* Label overlay */

.fl-01__zone-label {
  display: inline-block;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: rgba(108,99,255,0.12);
  color: var(--accent);
  padding: 2px 7px;
  border-radius: 4px;
  margin-bottom: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .fl-01__aside-bar {
    animation: none;
  }
}
```
