---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/icon-sidebar-flyout-dropdown/"
title: "Icon Sidebar Flyout Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A compact icon-only rail navigation where hovering each icon causes a labeled flyout panel to slide in from the right — a common pattern for collapsed sidebars."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Sidebar Flyout Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/icon-sidebar-flyout-dropdown/

A compact icon-only rail navigation where hovering each icon causes a labeled flyout panel to slide in from the right — a common pattern for collapsed sidebars.
## HTML
```html
<div class="dd-12">
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <div class="dd-12__app">
    <aside class="dd-12__rail">
      <div class="dd-12__brand-icon">&#9670;</div>

      <div class="dd-12__item">
        <div class="dd-12__icon-wrap">
          <span class="dd-12__icon">&#127968;</span>
        </div>
        <div class="dd-12__flyout">
          <p class="dd-12__fly-title">Dashboard</p>
          <div class="dd-12__fly-divider"></div>
          <a href="#" class="dd-12__fly-link">Overview</a>
          <a href="#" class="dd-12__fly-link">Analytics</a>
          <a href="#" class="dd-12__fly-link">Reports</a>
        </div>
      </div>

      <div class="dd-12__item">
        <div class="dd-12__icon-wrap">
          <span class="dd-12__icon">&#128203;</span>
        </div>
        <div class="dd-12__flyout">
          <p class="dd-12__fly-title">Projects</p>
          <div class="dd-12__fly-divider"></div>
          <a href="#" class="dd-12__fly-link">All Projects</a>
          <a href="#" class="dd-12__fly-link">Active</a>
          <a href="#" class="dd-12__fly-link">Archived</a>
        </div>
      </div>

      <div class="dd-12__item">
        <div class="dd-12__icon-wrap">
          <span class="dd-12__icon">&#128172;</span>
        </div>
        <div class="dd-12__flyout">
          <p class="dd-12__fly-title">Messages</p>
          <div class="dd-12__fly-divider"></div>
          <a href="#" class="dd-12__fly-link">Inbox</a>
          <a href="#" class="dd-12__fly-link">Sent</a>
          <a href="#" class="dd-12__fly-link">Drafts</a>
        </div>
      </div>

      <div class="dd-12__item">
        <div class="dd-12__icon-wrap">
          <span class="dd-12__icon">&#9881;</span>
        </div>
        <div class="dd-12__flyout">
          <p class="dd-12__fly-title">Settings</p>
          <div class="dd-12__fly-divider"></div>
          <a href="#" class="dd-12__fly-link">Profile</a>
          <a href="#" class="dd-12__fly-link">Security</a>
          <a href="#" class="dd-12__fly-link">Billing</a>
        </div>
      </div>
    </aside>
    <main class="dd-12__main">
      <p class="dd-12__hint">Hover the icons &#8592;</p>
    </main>
  </div>
</div>
```
## CSS
```css
.dd-12,
.dd-12 *,
.dd-12 *::before,
.dd-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-12 ::selection {
  background: #7c3aed;
  color: #ede9fe;
}

.dd-12 {
  --accent: #7c3aed;
  --surface: #fff;
  --rail-bg: #fafafa;
  --text: #1e1b4b;
  --muted: #6b7280;
  --border: #ede9fe;
  --hover-icon: #f5f3ff;
  font-family: 'IBM Plex Sans', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
  padding: 40px 20px;
}

.dd-12__app {
  display: flex;
  height: 300px;
  width: 100%;
  max-width: 560px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: visible;
  box-shadow: 0 8px 32px rgba(124,58,237,.12);
}

.dd-12__rail {
  width: 60px;
  background: var(--rail-bg);
  border-right: 1px solid var(--border);
  border-radius: 16px 0 0 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 14px 0;
  gap: 4px;
  flex-shrink: 0;
  position: relative;
  z-index: 10;
  overflow: visible;
}

.dd-12__brand-icon {
  font-size: 18px;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 16px;
}

.dd-12__item {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
}
/* hover-bridge: invisible strip on the right of the icon-rail item
   covering the 8px gap to the flyout panel. Lives on .__item (not
   .__flyout, which has pointer-events:none at rest). */

.dd-12__item::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 100%;
  width: 8px;
}

.dd-12__icon-wrap {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.15s;
}

.dd-12__item:hover .dd-12__icon-wrap {
  background: var(--hover-icon);
}

.dd-12__icon {
  font-size: 18px;
}
/* flyout panel */

.dd-12__flyout {
  position: absolute;
  left: calc(100% + 8px);
  top: -4px;
  min-width: 170px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 8px 28px rgba(124,58,237,.15);
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  opacity: 0;
  pointer-events: none;
  transform: translateX(-8px);
  transition: opacity 0.2s ease, transform 0.25s cubic-bezier(0.16,1,0.3,1);
  z-index: 20;
}

.dd-12__item:hover .dd-12__flyout {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(0);
}

.dd-12__fly-title {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent);
  padding: 0 4px 4px;
}

.dd-12__fly-divider {
  height: 1px;
  background: var(--border);
  margin: 4px 0;
}

.dd-12__fly-link {
  display: block;
  padding: 7px 10px;
  border-radius: 7px;
  text-decoration: none;
  color: var(--text);
  font-size: 13px;
  font-weight: 500;
  transition: background 0.12s, color 0.12s;
}

.dd-12__fly-link:hover {
  background: var(--hover-icon);
  color: var(--accent);
}

.dd-12__main {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.dd-12__hint {
  color: var(--muted);
  font-size: 13px;
  font-style: italic;
}

@media (prefers-reduced-motion: reduce) {
  .dd-12__flyout {
    transition: none;
  }
}
```
