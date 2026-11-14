---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-sidebar-drawer-navigation/"
title: "CSS Sidebar Drawer Navigation"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Off-canvas sidebar drawer that slides in from the left using a hidden checkbox toggle with overlay backdrop."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sidebar Drawer Navigation
Source: https://codefronts.com/navigation/css-responsive-navbar/css-sidebar-drawer-navigation/

Off-canvas sidebar drawer that slides in from the left using a hidden checkbox toggle with overlay backdrop.
## HTML
```html
<div class="nav-03">
  <input type="checkbox" id="nav-03-toggle">
  <div class="nav-03__bar">
    <label for="nav-03-toggle" class="nav-03__menu-btn" aria-label="Toggle sidebar">
      <span></span><span></span><span></span>
    </label>
    <a href="#" class="nav-03__logo">Arch<em>ive</em></a>
    <div class="nav-03__search">
      <span class="nav-03__search-icon">🔍</span>
      <input type="text" placeholder="Search...">
    </div>
    <div class="nav-03__bar-actions">
      <button class="nav-03__icon-btn">🔔</button>
      <button class="nav-03__icon-btn">⚙️</button>
      <div class="nav-03__avatar">VR</div>
    </div>
  </div>
  <label for="nav-03-toggle" class="nav-03__overlay"></label>
  <nav class="nav-03__drawer">
    <div class="nav-03__drawer-header">
      <div class="nav-03__drawer-title">Navigation</div>
    </div>
    <div class="nav-03__section">
      <div class="nav-03__section-label">Main</div>
      <a href="#" class="nav-03__link is-active"><span class="nav-03__link-icon">🏠</span> Dashboard</a>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">📊</span> Analytics <span class="nav-03__badge">New</span></a>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">📁</span> Projects</a>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">✉️</span> Messages <span class="nav-03__badge">4</span></a>
    </div>
    <div class="nav-03__section">
      <div class="nav-03__section-label">Workspace</div>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">📋</span> Tasks</a>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">📅</span> Calendar</a>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">🗂️</span> Files</a>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">👥</span> Team</a>
    </div>
    <div class="nav-03__section">
      <div class="nav-03__section-label">Account</div>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">👤</span> Profile</a>
      <a href="#" class="nav-03__link"><span class="nav-03__link-icon">⚙️</span> Settings</a>
    </div>
    <div class="nav-03__drawer-footer">
      <div class="nav-03__profile">
        <div class="nav-03__avatar">VR</div>
        <div>
          <div class="nav-03__profile-name">Vimal Raj</div>
          <div class="nav-03__profile-role">Admin</div>
        </div>
      </div>
    </div>
  </nav>
  <div class="nav-03__content">
    <h1 style="font-size:2.5rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:1rem; color:#e6edf3;">Sidebar Drawer <span style="color:#f78166;">Navigation</span></h1>
    <p style="color:#7d8590; font-size:1.1rem; line-height:1.7; max-width:600px;">On desktop the sidebar is always visible. On mobile, tap the hamburger icon to slide it in over an overlay. Pure CSS checkbox toggle — no JavaScript.</p>
  </div>
</div>
```
## CSS
```css
.nav-03,
.nav-03 *,
.nav-03 *::before,
.nav-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-03 {
  --bg: #161b22;
  --sidebar: #0d1117;
  --text: #e6edf3;
  --muted: #7d8590;
  --accent: #f78166;
  --border: rgba(240,246,252,0.1);
  --drawer-w: 280px;
  font-family: 'Syne', sans-serif;
}

#nav-03-toggle {
  display: none;
}
/* Top bar */

.nav-03__bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 300;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 1.5rem;
  gap: 1rem;
}

.nav-03__menu-btn {
  width: 36px;
  height: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  cursor: pointer;
  border: none;
  background: transparent;
  border-radius: 8px;
  transition: background 0.15s;
  flex-shrink: 0;
}

.nav-03__menu-btn:hover {
  background: rgba(255,255,255,0.07);
}

.nav-03__menu-btn span {
  display: block;
  width: 18px;
  height: 1.5px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s cubic-bezier(.4,0,.2,1), opacity 0.3s, width 0.3s;
}

#nav-03-toggle:checked ~ .nav-03__bar .nav-03__menu-btn span:nth-child(1) {
  transform: translateY(6.5px) rotate(45deg);
}

#nav-03-toggle:checked ~ .nav-03__bar .nav-03__menu-btn span:nth-child(2) {
  opacity: 0;
  width: 0;
}

#nav-03-toggle:checked ~ .nav-03__bar .nav-03__menu-btn span:nth-child(3) {
  transform: translateY(-6.5px) rotate(-45deg);
}

.nav-03__logo {
  font-weight: 800;
  font-size: 1.15rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.02em;
}

.nav-03__logo em {
  color: var(--accent);
  font-style: normal;
}

.nav-03__search {
  flex: 1;
  max-width: 340px;
  position: relative;
}

.nav-03__search input {
  width: 100%;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  font-family: inherit;
  font-size: 0.875rem;
  padding: 0.45rem 0.75rem 0.45rem 2.2rem;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
}

.nav-03__search input:focus {
  border-color: var(--accent);
  background: rgba(247,129,102,0.05);
}

.nav-03__search input::placeholder {
  color: var(--muted);
}

.nav-03__search-icon {
  position: absolute;
  left: 0.6rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  font-size: 0.875rem;
  pointer-events: none;
}

.nav-03__bar-actions {
  margin-left: auto;
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.nav-03__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f78166, #ffa657);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  color: #fff;
  cursor: pointer;
}

.nav-03__icon-btn {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--muted);
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, color 0.15s;
}

.nav-03__icon-btn:hover {
  background: rgba(255,255,255,0.07);
  color: var(--text);
}
/* Overlay */

.nav-03__overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.6);
  z-index: 200;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
}

#nav-03-toggle:checked ~ .nav-03__overlay {
  opacity: 1;
  pointer-events: all;
}
/* Drawer */

.nav-03__drawer {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: var(--drawer-w);
  background: var(--sidebar);
  border-right: 1px solid var(--border);
  z-index: 250;
  transform: translateX(-100%);
  transition: transform 0.35s cubic-bezier(.4,0,.2,1);
  overflow-y: auto;
  padding: 1rem 0;
  display: flex;
  flex-direction: column;
}

#nav-03-toggle:checked ~ .nav-03__drawer {
  transform: translateX(0);
}

.nav-03__drawer-header {
  padding: 0.75rem 1.25rem 1.25rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 0.5rem;
}

.nav-03__drawer-title {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
}

.nav-03__section {
  margin-bottom: 0.25rem;
}

.nav-03__section-label {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
  padding: 0.75rem 1.25rem 0.35rem;
}

.nav-03__link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  color: var(--muted);
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.55rem 1.25rem;
  border-radius: 6px;
  margin: 0 0.5rem;
  transition: background 0.15s, color 0.15s;
  position: relative;
}

.nav-03__link:hover {
  background: rgba(255,255,255,0.05);
  color: var(--text);
}

.nav-03__link.is-active {
  color: var(--text);
  background: rgba(247,129,102,0.1);
}

.nav-03__link.is-active::before {
  content: '';
  position: absolute;
  left: -0.5rem;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 60%;
  background: var(--accent);
  border-radius: 0 2px 2px 0;
}

.nav-03__link-icon {
  font-size: 1rem;
  width: 20px;
  text-align: center;
  flex-shrink: 0;
}

.nav-03__badge {
  margin-left: auto;
  background: var(--accent);
  color: #fff;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 10px;
}

.nav-03__drawer-footer {
  margin-top: auto;
  padding: 1rem;
  border-top: 1px solid var(--border);
}

.nav-03__profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav-03__profile-name {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text);
}

.nav-03__profile-role {
  font-size: 0.75rem;
  color: var(--muted);
}

.nav-03__content {
  padding-top: 60px;
  padding: 80px 2rem 2rem;
  color: var(--text);
}

@media (min-width: 768px) {
  .nav-03__drawer {
    transform: translateX(0) !important;
  }

  .nav-03__overlay {
    display: none !important;
  }

  .nav-03__menu-btn {
    display: none;
  }

  .nav-03__content {
    padding-left: calc(var(--drawer-w) + 2rem);
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-03__drawer {
    transition: none;
  }

  .nav-03__overlay {
    transition: none;
  }

  .nav-03__menu-btn span {
    transition: none;
  }
}
```
