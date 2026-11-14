---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/morphing-hamburger-to-x/"
title: "Morphing Hamburger to X"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A GitHub-dark-inspired top navigation bar where the hamburger icon morphs cleanly into a close X via CSS transforms."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Morphing Hamburger to X
Source: https://codefronts.com/navigation/css-mobile-navigation/morphing-hamburger-to-x/

A GitHub-dark-inspired top navigation bar where the hamburger icon morphs cleanly into a close X via CSS transforms. The dropdown menu slides down from beneath the nav with a smooth cubic-bezier easing.
## HTML
```html
<div class="mn-04">
  <input type="checkbox" id="mn-04-toggle">
  <div class="mn-04__topbar">
    <div class="mn-04__logo">
      <div class="mn-04__logo-mark">⬡</div>
      <span class="mn-04__logo-text">DevHub</span>
    </div>
    <label for="mn-04-toggle" class="mn-04__btn">
      <span class="mn-04__btn-bar"></span>
      <span class="mn-04__btn-bar"></span>
      <span class="mn-04__btn-bar"></span>
    </label>
  </div>

  <nav class="mn-04__menu">
    <div class="mn-04__menu-inner">
      <div class="mn-04__menu-section">Explore</div>
      <a href="#" class="mn-04__menu-item is-active">
        <span class="mn-04__menu-item-icon">🏠</span> Dashboard
      </a>
      <a href="#" class="mn-04__menu-item">
        <span class="mn-04__menu-item-icon">📦</span> Repositories
        <span class="mn-04__menu-item-badge">12</span>
      </a>
      <a href="#" class="mn-04__menu-item">
        <span class="mn-04__menu-item-icon">🔀</span> Pull Requests
        <span class="mn-04__menu-item-badge">3</span>
      </a>
      <a href="#" class="mn-04__menu-item">
        <span class="mn-04__menu-item-icon">🐛</span> Issues
      </a>
      <div class="mn-04__menu-divider"></div>
      <div class="mn-04__menu-section">Account</div>
      <a href="#" class="mn-04__menu-item">
        <span class="mn-04__menu-item-icon">👤</span> Profile
      </a>
      <a href="#" class="mn-04__menu-item">
        <span class="mn-04__menu-item-icon">⚙️</span> Settings
      </a>
    </div>
  </nav>

  <div class="mn-04__content">
    <div class="mn-04__greeting">
      <p>Good morning 👋</p>
      <h2>Welcome back, Dev</h2>
    </div>

    <div class="mn-04__repo">
      <div class="mn-04__repo-header">
        <div class="mn-04__repo-name">ui-components</div>
      </div>
      <div class="mn-04__repo-desc">A collection of production-ready React components built with TypeScript.</div>
      <div class="mn-04__repo-meta">
        <span><div class="mn-04__dot" style="background:#3fb950"></div> TypeScript</span>
        <span>⭐ 842</span>
        <span>🍴 124</span>
      </div>
    </div>

    <div class="mn-04__repo">
      <div class="mn-04__repo-header">
        <div class="mn-04__repo-name">api-gateway</div>
      </div>
      <div class="mn-04__repo-desc">High-performance API gateway with rate limiting and auth middleware.</div>
      <div class="mn-04__repo-meta">
        <span><div class="mn-04__dot" style="background:#58a6ff"></div> Go</span>
        <span>⭐ 231</span>
        <span>🍴 48</span>
      </div>
    </div>

    <div class="mn-04__repo">
      <div class="mn-04__repo-header">
        <div class="mn-04__repo-name">css-animations</div>
      </div>
      <div class="mn-04__repo-desc">60+ CSS animation demos with no dependencies required.</div>
      <div class="mn-04__repo-meta">
        <span><div class="mn-04__dot" style="background:#e34c26"></div> CSS</span>
        <span>⭐ 1.2k</span>
        <span>🍴 307</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: 'Segoe UI', sans-serif;
}

.mn-04 {
  --bg: #0d1117;
  --surface: #161b22;
  --border: #30363d;
  --accent: #58a6ff;
  --accent2: #3fb950;
  --text: #c9d1d9;
  --muted: #8b949e;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7);
  color: var(--text);
}

.mn-04 #mn-04-toggle {
  display: none;
}
/* Top bar */

.mn-04__topbar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  z-index: 5;
}

.mn-04__logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.mn-04__logo-mark {
  width: 28px;
  height: 28px;
  background: var(--accent);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}

.mn-04__logo-text {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.3px;
}
/* Morphing hamburger button */

.mn-04__btn {
  width: 36px;
  height: 36px;
  cursor: pointer;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mn-04__btn-bar {
  position: absolute;
  width: 24px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
  transform-origin: center;
}

.mn-04__btn-bar:nth-child(1) {
  transform: translateY(-7px);
  width: 16px;
  right: 6px;
}

.mn-04__btn-bar:nth-child(2) {
  transform: translateY(0px);
}

.mn-04__btn-bar:nth-child(3) {
  transform: translateY(7px);
  width: 20px;
  right: 6px;
}

.mn-04 #mn-04-toggle:checked ~ .mn-04__topbar .mn-04__btn-bar:nth-child(1) {
  transform: translateY(0) rotate(45deg);
  width: 24px;
  right: 6px;
}

.mn-04 #mn-04-toggle:checked ~ .mn-04__topbar .mn-04__btn-bar:nth-child(2) {
  opacity: 0;
  transform: scaleX(0) translateY(0);
}

.mn-04 #mn-04-toggle:checked ~ .mn-04__topbar .mn-04__btn-bar:nth-child(3) {
  transform: translateY(0) rotate(-45deg);
  width: 24px;
  right: 6px;
}
/* Menu panel — drops from top */

.mn-04__menu {
  position: absolute;
  top: 60px;
  left: 0;
  right: 0;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  z-index: 4;
  transform: translateY(-100%);
  opacity: 0;
  transition: transform 0.45s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.3s;
  pointer-events: none;
}

.mn-04 #mn-04-toggle:checked ~ .mn-04__menu {
  transform: translateY(0);
  opacity: 1;
  pointer-events: all;
}

.mn-04__menu-inner {
  padding: 8px 0 16px;
}

.mn-04__menu-section {
  padding: 12px 20px 4px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--muted);
}

.mn-04__menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 20px;
  font-size: 14px;
  color: var(--text);
  cursor: pointer;
  transition: background 0.15s;
  text-decoration: none;
}

.mn-04__menu-item:hover {
  background: rgba(88,166,255,0.06);
}

.mn-04__menu-item.is-active {
  color: var(--accent);
}

.mn-04__menu-item-icon {
  width: 18px;
  text-align: center;
  font-size: 15px;
}

.mn-04__menu-item-badge {
  margin-left: auto;
  background: var(--accent);
  color: var(--bg);
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 10px;
}

.mn-04__menu-divider {
  height: 1px;
  background: var(--border);
  margin: 8px 20px;
}
/* Page content */

.mn-04__content {
  position: absolute;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 24px 20px;
  overflow-y: auto;
}

.mn-04__greeting {
  margin-bottom: 24px;
}

.mn-04__greeting p {
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 4px;
}

.mn-04__greeting h2 {
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.5px;
}

.mn-04__repo {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px;
  margin-bottom: 10px;
  transition: border-color 0.2s;
}

.mn-04__repo:hover {
  border-color: var(--accent);
}

.mn-04__repo-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.mn-04__repo-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--accent);
}

.mn-04__repo-desc {
  font-size: 12px;
  color: var(--muted);
  line-height: 1.5;
  margin-bottom: 10px;
}

.mn-04__repo-meta {
  display: flex;
  gap: 14px;
}

.mn-04__repo-meta span {
  font-size: 11px;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 4px;
}

.mn-04__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

@media (prefers-reduced-motion: reduce) {
  .mn-04__btn-bar,
    .mn-04__menu {
    transition: none;
  }
}
```
