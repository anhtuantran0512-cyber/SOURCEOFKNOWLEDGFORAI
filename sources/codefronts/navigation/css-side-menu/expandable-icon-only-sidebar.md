---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/expandable-icon-only-sidebar/"
title: "Expandable Icon-Only Sidebar"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A persistent narrow icon rail that smoothly expands on hover to reveal full text labels and notification badges, using a CSS width transition with no toggle…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Icon-Only Sidebar
Source: https://codefronts.com/navigation/css-side-menu/expandable-icon-only-sidebar/

A persistent narrow icon rail that smoothly expands on hover to reveal full text labels and notification badges, using a CSS width transition with no toggle required.
## HTML
```html
<div class="sm-04">
  <nav class="sm-04__rail">
    <div class="sm-04__logo">Z</div>
    <div class="sm-04__links">
      <a class="sm-04__link sm-04__link--active" href="#">
        <span class="sm-04__link-icon">⬡</span>
        <span class="sm-04__link-text">Dashboard</span>
      </a>
      <a class="sm-04__link" href="#">
        <span class="sm-04__link-icon">◈</span>
        <span class="sm-04__link-text">Analytics</span>
        <span class="sm-04__link-badge">5</span>
      </a>
      <a class="sm-04__link" href="#">
        <span class="sm-04__link-icon">▦</span>
        <span class="sm-04__link-text">Projects</span>
      </a>
      <a class="sm-04__link" href="#">
        <span class="sm-04__link-icon">◉</span>
        <span class="sm-04__link-text">Messages</span>
        <span class="sm-04__link-badge">9</span>
      </a>
      <div class="sm-04__divider"></div>
      <a class="sm-04__link" href="#">
        <span class="sm-04__link-icon">◬</span>
        <span class="sm-04__link-text">Help</span>
      </a>
      <a class="sm-04__link" href="#">
        <span class="sm-04__link-icon">⬙</span>
        <span class="sm-04__link-text">Settings</span>
      </a>
    </div>
    <div class="sm-04__user">
      <div class="sm-04__user-icon"><div class="sm-04__user-avatar">MK</div></div>
      <div class="sm-04__user-info">
        <div class="sm-04__user-name">M. Kowalski</div>
        <div class="sm-04__user-role">Admin</div>
      </div>
    </div>
  </nav>
  <div class="sm-04__main">
    <div class="sm-04__heading">Dashboard</div>
    <div class="sm-04__sub">Hover the icon rail on the left to expand. Labels and badges appear without any JavaScript.</div>
    <div class="sm-04__cards">
      <div class="sm-04__card"><div class="sm-04__card-val">41</div><div class="sm-04__card-lbl">Active Projects</div></div>
      <div class="sm-04__card"><div class="sm-04__card-val">98%</div><div class="sm-04__card-lbl">Health Score</div></div>
      <div class="sm-04__card"><div class="sm-04__card-val">$74k</div><div class="sm-04__card-lbl">Monthly Revenue</div></div>
      <div class="sm-04__card"><div class="sm-04__card-val">1.2k</div><div class="sm-04__card-lbl">Team Members</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-04,
.sm-04 *,
.sm-04 *::before,
.sm-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-04 ::selection {
  background: #f59e0b;
  color: #000;
}

.sm-04 {
  --bg: #09090b;
  --surface: #18181b;
  --rail-bg: #0f0f12;
  --accent: #f59e0b;
  --accent2: #fbbf24;
  --text: #fafafa;
  --muted: #71717a;
  --border: rgba(245,158,11,0.15);
  --collapsed: 60px;
  --expanded: 230px;
  --dur: 0.35s;
  --ease: cubic-bezier(0.4, 0, 0.2, 1);
  font-family: 'Inter', system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}
/* Sidebar rail */

.sm-04__rail {
  width: var(--collapsed);
  min-height: 440px;
  background: var(--rail-bg);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16px 0;
  overflow: hidden;
  transition: width var(--dur) var(--ease);
  flex-shrink: 0;
  position: relative;
  z-index: 5;
}

.sm-04__rail:hover {
  width: var(--expanded);
}
/* Logo */

.sm-04__logo {
  width: 36px;
  height: 36px;
  background: var(--accent);
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 16px;
  color: #000;
  flex-shrink: 0;
  margin-bottom: 24px;
  transition: border-radius 0.3s;
}

.sm-04__rail:hover .sm-04__logo {
  border-radius: 50%;
}
/* Nav items */

.sm-04__links {
  width: 100%;
  flex: 1;
}

.sm-04__link {
  display: flex;
  align-items: center;
  gap: 0;
  width: 100%;
  padding: 0;
  color: var(--muted);
  cursor: pointer;
  text-decoration: none;
  transition: color 0.2s, background 0.2s;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  height: 48px;
}

.sm-04__link:hover,
.sm-04__link--active {
  color: var(--text);
  background: rgba(245,158,11,0.08);
}

.sm-04__link--active::after {
  content: '';
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 60%;
  background: var(--accent);
  border-radius: 3px 0 0 3px;
  transition: opacity 0.2s;
}

.sm-04__link-icon {
  width: var(--collapsed);
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
  transition: background 0.2s;
}

.sm-04__link:hover .sm-04__link-icon {
  color: var(--accent);
}

.sm-04__link--active .sm-04__link-icon {
  color: var(--accent2);
}

.sm-04__link-text {
  font-size: 13px;
  font-weight: 600;
  opacity: 0;
  transition: opacity 0.2s 0.05s;
  pointer-events: none;
  flex: 1;
}

.sm-04__rail:hover .sm-04__link-text {
  opacity: 1;
}

.sm-04__link-badge {
  margin-right: 12px;
  background: rgba(245,158,11,0.2);
  color: var(--accent2);
  font-size: 10px;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 99px;
  opacity: 0;
  transition: opacity 0.2s 0.05s;
}

.sm-04__rail:hover .sm-04__link-badge {
  opacity: 1;
}
/* Divider */

.sm-04__divider {
  width: 80%;
  height: 1px;
  background: var(--border);
  margin: 8px auto;
  flex-shrink: 0;
}
/* Bottom user */

.sm-04__user {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 0;
  overflow: hidden;
  padding: 8px 0 0;
  border-top: 1px solid var(--border);
}

.sm-04__user-icon {
  width: var(--collapsed);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.sm-04__user-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f59e0b, #ef4444);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  color: #000;
}

.sm-04__user-info {
  opacity: 0;
  transition: opacity 0.2s 0.05s;
  white-space: nowrap;
}

.sm-04__rail:hover .sm-04__user-info {
  opacity: 1;
}

.sm-04__user-name {
  font-size: 12px;
  font-weight: 600;
}

.sm-04__user-role {
  font-size: 10px;
  color: var(--muted);
}
/* Main */

.sm-04__main {
  flex: 1;
  padding: 24px;
  min-width: 0;
}

.sm-04__heading {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
}

.sm-04__sub {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 22px;
}

.sm-04__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sm-04__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
}

.sm-04__card-val {
  font-size: 20px;
  font-weight: 700;
  color: var(--accent2);
}

.sm-04__card-lbl {
  font-size: 11px;
  color: var(--muted);
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-04__rail,
    .sm-04__link-text,
    .sm-04__link-badge,
    .sm-04__user-info {
    transition: none;
  }
}
```
