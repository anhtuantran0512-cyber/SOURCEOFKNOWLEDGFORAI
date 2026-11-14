---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/collapsible-sidebar-menu-with-css-transitions/"
title: "Collapsible Sidebar Menu with CSS Transitions"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A sidebar that fluidly animates between full expanded width and icon-only collapsed state using transition:width, with text labels and badges fading out in…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Collapsible Sidebar Menu with CSS Transitions
Source: https://codefronts.com/navigation/css-side-menu/collapsible-sidebar-menu-with-css-transitions/

A sidebar that fluidly animates between full expanded width and icon-only collapsed state using transition:width, with text labels and badges fading out in sync.
## HTML
```html
<div class="sm-15">
  <input type="checkbox" class="sm-15__toggle" id="sm-15-toggle">
  <div class="sm-15__layout">
    <nav class="sm-15__nav">
      <div class="sm-15__brand">
        <div class="sm-15__logo">R</div>
        <span class="sm-15__brand-name">Recto</span>
      </div>
      <div class="sm-15__links">
        <a class="sm-15__link sm-15__link--active" href="#">
          <span class="sm-15__link-icon">⬡</span>
          <span class="sm-15__link-text">Dashboard</span>
        </a>
        <a class="sm-15__link" href="#">
          <span class="sm-15__link-icon">◈</span>
          <span class="sm-15__link-text">Analytics</span>
          <span class="sm-15__badge">9</span>
        </a>
        <a class="sm-15__link" href="#">
          <span class="sm-15__link-icon">▦</span>
          <span class="sm-15__link-text">Products</span>
        </a>
        <a class="sm-15__link" href="#">
          <span class="sm-15__link-icon">◉</span>
          <span class="sm-15__link-text">Orders</span>
          <span class="sm-15__badge">3</span>
        </a>
        <a class="sm-15__link" href="#">
          <span class="sm-15__link-icon">◬</span>
          <span class="sm-15__link-text">Customers</span>
        </a>
        <a class="sm-15__link" href="#">
          <span class="sm-15__link-icon">⬙</span>
          <span class="sm-15__link-text">Settings</span>
        </a>
      </div>
      <label class="sm-15__collapse-btn" for="sm-15-toggle" title="Collapse sidebar">‹</label>
      <div class="sm-15__user">
        <div class="sm-15__user-avatar">WP</div>
        <div class="sm-15__user-info">
          <div class="sm-15__user-name">W. Park</div>
          <div class="sm-15__user-role">Admin</div>
        </div>
      </div>
    </nav>
    <div class="sm-15__main">
      <div class="sm-15__heading">Dashboard</div>
      <div class="sm-15__sub">Click ‹ to collapse the sidebar from full width to icon-only. Driven by <code>transition: width</code> — zero JS.</div>
      <div class="sm-15__grid">
        <div class="sm-15__card"><div class="sm-15__card-val">$82k</div><div class="sm-15__card-lbl">Revenue</div></div>
        <div class="sm-15__card"><div class="sm-15__card-val">1,247</div><div class="sm-15__card-lbl">Orders</div></div>
        <div class="sm-15__card"><div class="sm-15__card-val">98%</div><div class="sm-15__card-lbl">Uptime</div></div>
        <div class="sm-15__card"><div class="sm-15__card-val">4.9★</div><div class="sm-15__card-lbl">Rating</div></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-15,
.sm-15 *,
.sm-15 *::before,
.sm-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-15 ::selection {
  background: #e11d48;
  color: #fff;
}

.sm-15 {
  --bg: #09090b;
  --surface: #141418;
  --nav-bg: #0f0f12;
  --accent: #e11d48;
  --accent2: #fb7185;
  --text: #f1f5f9;
  --muted: #52525b;
  --border: rgba(225,29,72,0.12);
  --font: 'Sora', system-ui, sans-serif;
  --full-w: 240px;
  --collapsed-w: 64px;
  --dur: 0.35s;
  --ease: cubic-bezier(0.4, 0, 0.2, 1);
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  border-radius: 12px;
  overflow: hidden;
}
/* Toggle */

.sm-15__toggle {
  display: none;
}
/* Sidebar */

.sm-15__nav {
  width: var(--full-w);
  background: var(--nav-bg);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  overflow: hidden;
  transition: width var(--dur) var(--ease);
  position: relative;
}

.sm-15__toggle:checked ~ .sm-15__layout .sm-15__nav {
  width: var(--collapsed-w);
}
/* Shell wrapper to allow :checked targeting */

.sm-15__layout {
  display: flex;
  flex: 1;
  min-width: 0;
}
/* Brand */

.sm-15__brand {
  display: flex;
  align-items: center;
  padding: 20px 10px 18px 10px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 12px;
  overflow: hidden;
  white-space: nowrap;
  gap: 0;
  min-width: 0;
}

.sm-15__logo {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 16px;
  color: #fff;
  flex-shrink: 0;
}

.sm-15__brand-name {
  font-size: 15px;
  font-weight: 800;
  margin-left: 10px;
  overflow: hidden;
  opacity: 1;
  transition: opacity var(--dur) var(--ease), max-width var(--dur) var(--ease);
  max-width: 160px;
}

.sm-15__toggle:checked ~ .sm-15__layout .sm-15__brand-name {
  opacity: 0;
  max-width: 0;
}
/* Collapse toggle button */

.sm-15__collapse-btn {
  align-self: flex-end;
  margin: 8px 12px;
  width: 28px;
  height: 28px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 12px;
  color: var(--muted);
  flex-shrink: 0;
  transition: transform var(--dur) var(--ease), align-self var(--dur) var(--ease), margin var(--dur) var(--ease), background 0.2s, color 0.2s;
}

.sm-15__toggle:checked ~ .sm-15__layout .sm-15__collapse-btn {
  align-self: center;
  margin: 8px 0;
  transform: rotate(180deg);
}

.sm-15__collapse-btn:hover {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}
/* Links */

.sm-15__links {
  flex: 1;
  padding: 0 6px;
}

.sm-15__link {
  display: flex;
  align-items: center;
  padding: 11px 7px;
  border-radius: 9px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
  margin-bottom: 4px;
  white-space: nowrap;
  overflow: hidden;
  gap: 0;
}

.sm-15__link:hover {
  color: var(--text);
  background: rgba(225,29,72,0.08);
}

.sm-15__link--active {
  color: var(--accent2);
  background: rgba(225,29,72,0.1);
}

.sm-15__link-icon {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 17px;
  flex-shrink: 0;
  border-radius: 8px;
  transition: background 0.2s;
}

.sm-15__link:hover .sm-15__link-icon {
  background: rgba(225,29,72,0.15);
}

.sm-15__link--active .sm-15__link-icon {
  background: rgba(225,29,72,0.18);
}

.sm-15__link-text {
  margin-left: 6px;
  opacity: 1;
  transition: opacity var(--dur) var(--ease), max-width var(--dur) var(--ease);
  max-width: 160px;
  overflow: hidden;
}

.sm-15__toggle:checked ~ .sm-15__layout .sm-15__link-text {
  opacity: 0;
  max-width: 0;
  margin-left: 0;
}

.sm-15__badge {
  margin-left: auto;
  background: rgba(225,29,72,0.2);
  color: var(--accent2);
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
  transition: opacity var(--dur);
}

.sm-15__toggle:checked ~ .sm-15__layout .sm-15__badge {
  opacity: 0;
}
/* Footer user */

.sm-15__user {
  padding: 14px 8px 18px;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  overflow: hidden;
  transition: justify-content var(--dur) var(--ease);
}

.sm-15__toggle:checked ~ .sm-15__layout .sm-15__user {
  justify-content: center;
  padding: 14px 0 18px;
}

.sm-15__user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), #8b5cf6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.sm-15__user-info {
  margin-left: 10px;
  opacity: 1;
  transition: opacity var(--dur), max-width var(--dur) var(--ease);
  max-width: 160px;
  white-space: nowrap;
  overflow: hidden;
}

.sm-15__toggle:checked ~ .sm-15__layout .sm-15__user-info {
  opacity: 0;
  max-width: 0;
  margin-left: 0;
}

.sm-15__user-name {
  font-size: 12px;
  font-weight: 700;
}

.sm-15__user-role {
  font-size: 10px;
  color: var(--muted);
}
/* Main */

.sm-15__main {
  flex: 1;
  padding: 24px;
  min-width: 0;
}

.sm-15__heading {
  font-size: 20px;
  font-weight: 800;
  margin-bottom: 6px;
}

.sm-15__sub {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 22px;
}

.sm-15__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sm-15__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 9px;
  padding: 14px;
}

.sm-15__card-val {
  font-size: 22px;
  font-weight: 800;
  color: var(--accent2);
}

.sm-15__card-lbl {
  font-size: 11px;
  color: var(--muted);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-15__nav,
    .sm-15__brand-name,
    .sm-15__link-text,
    .sm-15__badge,
    .sm-15__user-info,
    .sm-15__collapse-btn {
    transition: none;
  }
}
```
