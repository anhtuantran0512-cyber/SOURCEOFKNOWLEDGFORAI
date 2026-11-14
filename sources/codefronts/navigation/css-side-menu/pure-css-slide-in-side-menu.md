---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/pure-css-slide-in-side-menu/"
title: "Pure CSS Slide-In Side Menu"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A navigation drawer that slides in from off-screen left when a burger icon is clicked, driven entirely by a hidden checkbox and CSS sibling selectors."
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Slide-In Side Menu
Source: https://codefronts.com/navigation/css-side-menu/pure-css-slide-in-side-menu/

A navigation drawer that slides in from off-screen left when a burger icon is clicked, driven entirely by a hidden checkbox and CSS sibling selectors.
## HTML
```html
<div class="sm-01">
  <input type="checkbox" class="sm-01__toggle" id="sm-01-toggle">
  <label class="sm-01__burger" for="sm-01-toggle" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </label>
  <nav class="sm-01__nav">
    <div class="sm-01__brand">
      <div class="sm-01__logo">V</div>
      <div><div class="sm-01__brand-name">Velocity</div><div class="sm-01__brand-sub">Design System</div></div>
    </div>
    <div class="sm-01__links">
      <a class="sm-01__link sm-01__link--active" href="#">
        <span class="sm-01__link-icon">⬡</span> Dashboard
      </a>
      <a class="sm-01__link" href="#">
        <span class="sm-01__link-icon">◈</span> Analytics
      </a>
      <a class="sm-01__link" href="#">
        <span class="sm-01__link-icon">⬟</span> Projects
      </a>
      <a class="sm-01__link" href="#">
        <span class="sm-01__link-icon">◇</span> Messages
      </a>
      <a class="sm-01__link" href="#">
        <span class="sm-01__link-icon">⬙</span> Settings
      </a>
    </div>
    <div class="sm-01__nav-footer">
      <div class="sm-01__avatar">
        <div class="sm-01__avatar-img">JD</div>
        <div>
          <div class="sm-01__avatar-name">Jane Doe</div>
          <div class="sm-01__avatar-role">Pro Plan</div>
        </div>
      </div>
    </div>
  </nav>
  <div class="sm-01__content">
    <div class="sm-01__heading">Welcome back, Jane 👋</div>
    <div class="sm-01__subhead">Click the button above to slide open the menu — pure CSS only.</div>
    <div class="sm-01__cards">
      <div class="sm-01__card"><div class="sm-01__card-val">2,847</div><div class="sm-01__card-lbl">Page Views</div></div>
      <div class="sm-01__card"><div class="sm-01__card-val">94%</div><div class="sm-01__card-lbl">Uptime</div></div>
      <div class="sm-01__card"><div class="sm-01__card-val">$12.4k</div><div class="sm-01__card-lbl">Revenue</div></div>
      <div class="sm-01__card"><div class="sm-01__card-val">483</div><div class="sm-01__card-lbl">Users</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-01,
.sm-01 *,
.sm-01 *::before,
.sm-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-01 ::selection {
  background: #7c3aed;
  color: #fff;
}

.sm-01 {
  --bg: #0f172a;
  --surface: #1e293b;
  --menu-bg: #1a1033;
  --accent: #7c3aed;
  --accent2: #a78bfa;
  --text: #e2e8f0;
  --muted: #94a3b8;
  --border: rgba(124,58,237,0.2);
  --font: 'Plus Jakarta Sans', system-ui, sans-serif;
  --menu-w: 280px;
  --duration: 0.4s;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}
/* Hidden checkbox toggle */

.sm-01__toggle {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
  pointer-events: none;
}
/* Burger label */

.sm-01__burger {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 50;
  width: 42px;
  height: 42px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  transition: background 0.2s, border-color 0.2s;
}

.sm-01__burger:hover {
  background: var(--accent);
  border-color: var(--accent);
}

.sm-01__burger span {
  display: block;
  width: 20px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform var(--duration), opacity var(--duration);
  transform-origin: center;
}
/* Burger → X animation */

.sm-01__toggle:checked ~ .sm-01__burger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.sm-01__toggle:checked ~ .sm-01__burger span:nth-child(2) {
  opacity: 0;
  transform: scaleX(0);
}

.sm-01__toggle:checked ~ .sm-01__burger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
/* Slide-in panel */

.sm-01__nav {
  position: absolute;
  top: 0;
  left: 0;
  width: var(--menu-w);
  height: 100%;
  background: var(--menu-bg);
  border-right: 1px solid var(--border);
  transform: translateX(-100%);
  transition: transform var(--duration) cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 40;
  display: flex;
  flex-direction: column;
  padding: 80px 0 24px;
  box-shadow: 4px 0 32px rgba(0,0,0,0.4);
}

.sm-01__toggle:checked ~ .sm-01__nav {
  transform: translateX(0);
}
/* Brand */

.sm-01__brand {
  padding: 0 24px 24px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.sm-01__logo {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 16px;
}

.sm-01__brand-name {
  font-weight: 700;
  font-size: 16px;
}

.sm-01__brand-sub {
  font-size: 11px;
  color: var(--muted);
}
/* Nav links */

.sm-01__links {
  flex: 1;
  padding: 0 12px;
}

.sm-01__link {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 13px 16px;
  border-radius: 10px;
  color: var(--muted);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.2s;
  margin-bottom: 4px;
  cursor: pointer;
}

.sm-01__link:hover {
  color: var(--text);
  background: rgba(124,58,237,0.15);
}

.sm-01__link--active {
  color: var(--text);
  background: rgba(124,58,237,0.2);
}

.sm-01__link-icon {
  width: 36px;
  height: 36px;
  background: rgba(255,255,255,0.05);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
  transition: background 0.2s;
}

.sm-01__link:hover .sm-01__link-icon,
.sm-01__link--active .sm-01__link-icon {
  background: var(--accent);
}
/* Footer */

.sm-01__nav-footer {
  padding: 16px 24px 0;
  border-top: 1px solid var(--border);
}

.sm-01__avatar {
  display: flex;
  align-items: center;
  gap: 12px;
}

.sm-01__avatar-img {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, #f59e0b, #ef4444);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 13px;
}

.sm-01__avatar-name {
  font-size: 13px;
  font-weight: 600;
}

.sm-01__avatar-role {
  font-size: 11px;
  color: var(--muted);
}
/* Main content */

.sm-01__content {
  padding: 80px 24px 24px 24px;
  transition: transform var(--duration) cubic-bezier(0.4, 0, 0.2, 1);
}

.sm-01__heading {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 8px;
}

.sm-01__subhead {
  font-size: 14px;
  color: var(--muted);
  margin-bottom: 24px;
  line-height: 1.6;
}

.sm-01__cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.sm-01__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
}

.sm-01__card-val {
  font-size: 22px;
  font-weight: 700;
  color: var(--accent2);
}

.sm-01__card-lbl {
  font-size: 12px;
  color: var(--muted);
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-01__nav,
    .sm-01__burger span {
    transition: none;
  }
}
```
