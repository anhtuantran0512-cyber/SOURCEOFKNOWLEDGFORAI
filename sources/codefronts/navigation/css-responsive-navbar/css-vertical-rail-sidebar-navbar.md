---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-vertical-rail-sidebar-navbar/"
title: "CSS Vertical Rail Sidebar Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Persistent left-rail sidebar with icon + label vertical links, section dividers, and a collapsible bottom profile area."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vertical Rail Sidebar Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-vertical-rail-sidebar-navbar/

Persistent left-rail sidebar with icon + label vertical links, section dividers, and a collapsible bottom profile area.
## HTML
```html
<div class="nav-18">
  <input type="checkbox" id="nav-18-toggle">
  <div class="nav-18__layout">
    <nav class="nav-18__rail">
      <div class="nav-18__rail-top">
        <label for="nav-18-toggle" class="nav-18__expand-btn" aria-label="Expand sidebar">⇥</label>
        <a href="#" class="nav-18__brand">Code<span>Lab</span></a>
      </div>
      <div class="nav-18__nav">
        <div class="nav-18__section-label">Main</div>
        <a href="#" class="nav-18__item is-active">
          <span class="nav-18__icon">⬡</span>
          <span class="nav-18__item-label">Overview</span>
        </a>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">📊</span>
          <span class="nav-18__item-label">Analytics</span>
          <span class="nav-18__item-badge">New</span>
        </a>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">🚀</span>
          <span class="nav-18__item-label">Deployments</span>
        </a>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">⚙️</span>
          <span class="nav-18__item-label">Functions</span>
        </a>
        <div class="nav-18__section-label">Resources</div>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">🗄️</span>
          <span class="nav-18__item-label">Storage</span>
        </a>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">🔐</span>
          <span class="nav-18__item-label">Auth</span>
        </a>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">📋</span>
          <span class="nav-18__item-label">Logs</span>
          <span class="nav-18__item-badge">24</span>
        </a>
        <div class="nav-18__section-label">Account</div>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">💳</span>
          <span class="nav-18__item-label">Billing</span>
        </a>
        <a href="#" class="nav-18__item">
          <span class="nav-18__icon">🔧</span>
          <span class="nav-18__item-label">Settings</span>
        </a>
      </div>
      <div class="nav-18__rail-bottom">
        <div class="nav-18__avatar-wrap">
          <div class="nav-18__avatar">
            <div class="nav-18__avatar-img">VR</div>
          </div>
          <div class="nav-18__user-info">
            <div class="nav-18__user-name">Vimal Raj</div>
            <div class="nav-18__user-role">Pro plan</div>
          </div>
        </div>
      </div>
    </nav>
    <div class="nav-18__content">
      <h1 style="font-size:2rem; font-weight:700; letter-spacing:-0.03em; margin-bottom:1rem; color:#f59e0b;">Vertical Rail Navbar</h1>
      <p style="color:rgba(232,234,242,0.55); font-size:1rem; line-height:1.75; max-width:560px;">Click the ⇥ icon to expand the sidebar from icon-only 64px to full 220px. Labels, badges, section headers, and user info all transition in using <code>opacity</code> and <code>width</code>. Pure CSS checkbox toggle.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.nav-18,
.nav-18 *,
.nav-18 *::before,
.nav-18 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-18 {
  --bg: #16181f;
  --text: #e8eaf2;
  --muted: rgba(232,234,242,0.4);
  --accent: #f59e0b;
  --border: rgba(255,255,255,0.07);
  --collapsed-w: 64px;
  --expanded-w: 220px;
  font-family: 'Inter', sans-serif;
}

#nav-18-toggle {
  display: none;
}

.nav-18__rail {
  width: var(--collapsed-w);
  min-height: 100vh;
  background: var(--bg);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  transition: width 0.3s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
  flex-shrink: 0;
  position: sticky;
  top: 0;
  height: 100vh;
}

#nav-18-toggle:checked ~ .nav-18__layout .nav-18__rail {
  width: var(--expanded-w);
}

.nav-18__rail-top {
  height: 56px;
  display: flex;
  align-items: center;
  padding: 0 0 0 0;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}

.nav-18__expand-btn {
  width: 64px;
  height: 56px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border: none;
  background: transparent;
  color: var(--muted);
  font-size: 1.1rem;
  transition: color 0.2s, background 0.2s;
}

.nav-18__expand-btn:hover {
  color: var(--text);
  background: rgba(255,255,255,0.04);
}

.nav-18__brand {
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.02em;
  white-space: nowrap;
  overflow: hidden;
  opacity: 0;
  width: 0;
  transition: opacity 0.2s, width 0.3s;
}

.nav-18__brand span {
  color: var(--accent);
}

#nav-18-toggle:checked ~ .nav-18__layout .nav-18__brand {
  opacity: 1;
  width: auto;
}

.nav-18__nav {
  flex: 1;
  padding: 0.75rem 0;
  overflow-y: auto;
  scrollbar-width: none;
}

.nav-18__nav::-webkit-scrollbar {
  display: none;
}

.nav-18__section-label {
  font-size: 0.6rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--muted);
  padding: 0.75rem 0 0.35rem;
  white-space: nowrap;
  overflow: hidden;
  opacity: 0;
  transition: opacity 0.2s;
  padding-left: 1.25rem;
}

#nav-18-toggle:checked ~ .nav-18__layout .nav-18__section-label {
  opacity: 1;
}

.nav-18__item {
  display: flex;
  align-items: center;
  gap: 0;
  text-decoration: none;
  height: 44px;
  padding: 0;
  color: var(--muted);
  border-radius: 0;
  position: relative;
  transition: color 0.2s;
  overflow: hidden;
}

.nav-18__item:hover {
  color: var(--text);
}

.nav-18__item.is-active {
  color: var(--accent);
}

.nav-18__item.is-active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 60%;
  background: var(--accent);
  border-radius: 0 2px 2px 0;
}

.nav-18__item:hover {
  background: rgba(255,255,255,0.03);
}

.nav-18__icon {
  width: 64px;
  height: 44px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
}

.nav-18__item-label {
  font-size: 0.875rem;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  opacity: 0;
  width: 0;
  transition: opacity 0.2s, width 0.3s;
}

#nav-18-toggle:checked ~ .nav-18__layout .nav-18__item-label {
  opacity: 1;
  width: auto;
}

.nav-18__item-badge {
  margin-left: auto;
  margin-right: 1rem;
  background: var(--accent);
  color: #1a1206;
  font-size: 0.6rem;
  font-weight: 800;
  padding: 1px 5px;
  border-radius: 10px;
  opacity: 0;
  transition: opacity 0.2s;
  white-space: nowrap;
}

#nav-18-toggle:checked ~ .nav-18__layout .nav-18__item-badge {
  opacity: 1;
}

.nav-18__rail-bottom {
  padding: 0.75rem 0;
  border-top: 1px solid var(--border);
  flex-shrink: 0;
}

.nav-18__avatar-wrap {
  display: flex;
  align-items: center;
  gap: 0;
  padding: 0.5rem 0;
  height: 52px;
  overflow: hidden;
}

.nav-18__avatar {
  width: 64px;
  height: 52px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-18__avatar-img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f59e0b, #ef4444);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  color: #fff;
}

.nav-18__user-info {
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.2s;
}

#nav-18-toggle:checked ~ .nav-18__layout .nav-18__user-info {
  opacity: 1;
}

.nav-18__user-name {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text);
}

.nav-18__user-role {
  font-size: 0.7rem;
  color: var(--muted);
}
/* Content */

.nav-18__layout {
  display: flex;
  flex: 1;
  min-width: 0;
}

.nav-18__content {
  flex: 1;
  padding: 2rem;
  color: var(--text);
  min-width: 0;
}

@media (prefers-reduced-motion: reduce) {
  .nav-18__rail,
    .nav-18__brand,
    .nav-18__item-label,
    .nav-18__item-badge,
    .nav-18__section-label,
    .nav-18__user-info {
    transition: none;
  }
}
```
