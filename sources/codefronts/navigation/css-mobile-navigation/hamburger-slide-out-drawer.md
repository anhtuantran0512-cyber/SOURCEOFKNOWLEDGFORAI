---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/hamburger-slide-out-drawer/"
title: "Hamburger Slide-Out Drawer"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A dark slide-out nav drawer toggled by a Pure CSS checkbox."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hamburger Slide-Out Drawer
Source: https://codefronts.com/navigation/css-mobile-navigation/hamburger-slide-out-drawer/

A dark slide-out nav drawer toggled by a Pure CSS checkbox. The hamburger icon morphs into an X via CSS transforms, while the drawer slides in over a click-to-close overlay.
## HTML
```html
<div class="mn-01">
  <input type="checkbox" id="mn-01-toggle">
  <label class="mn-01__hamburger" for="mn-01-toggle">
    <span></span><span></span><span></span>
  </label>
  <label class="mn-01__overlay" for="mn-01-toggle"></label>
  <nav class="mn-01__drawer">
    <div class="mn-01__drawer-header">
      <div class="mn-01__avatar">👤</div>
      <h3>Alex Mercer</h3>
      <p>[email protected]</p>
    </div>
    <div class="mn-01__nav">
      <div class="mn-01__section-label">Main</div>
      <a href="#" class="is-active"><span class="mn-01__nav-icon">🏠</span> Dashboard</a>
      <a href="#"><span class="mn-01__nav-icon">📊</span> Analytics</a>
      <a href="#"><span class="mn-01__nav-icon">💬</span> Messages</a>
      <a href="#"><span class="mn-01__nav-icon">📁</span> Projects</a>
      <div class="mn-01__section-label">Account</div>
      <a href="#"><span class="mn-01__nav-icon">⚙️</span> Settings</a>
      <a href="#"><span class="mn-01__nav-icon">🔔</span> Notifications</a>
      <a href="#"><span class="mn-01__nav-icon">🚪</span> Sign Out</a>
    </div>
  </nav>
  <div class="mn-01__page">
    <div class="mn-01__topbar">
      <span class="mn-01__topbar-title">Dashboard</span>
    </div>
    <div class="mn-01__content">
      <div class="mn-01__card">
        <div class="mn-01__pill">New</div>
        <h4>Q4 Revenue Report</h4>
        <p>Your analytics are up 24% this quarter. Tap to view the full breakdown.</p>
      </div>
      <div class="mn-01__card">
        <h4>Recent Activity</h4>
        <p>3 new messages and 2 pending approvals waiting for your review.</p>
      </div>
      <div class="mn-01__card">
        <h4>Active Projects</h4>
        <p>5 projects in progress — 2 due this week.</p>
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

.mn-01 {
  --bg: #1a1a2e;
  --drawer: #16213e;
  --accent: #e94560;
  --text: #eaeaea;
  --muted: #8892a4;
  --overlay: rgba(0,0,0,0.6);
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.6);
}
/* Hidden checkbox toggle */

.mn-01 #mn-01-toggle {
  display: none;
}
/* Overlay */

.mn-01__overlay {
  position: absolute;
  inset: 0;
  background: var(--overlay);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.35s ease;
  z-index: 10;
}

.mn-01 #mn-01-toggle:checked ~ .mn-01__overlay {
  opacity: 1;
  pointer-events: all;
}
/* Drawer */

.mn-01__drawer {
  position: absolute;
  top: 0;
  left: 0;
  width: 280px;
  height: 100%;
  background: var(--drawer);
  transform: translateX(-100%);
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 20;
  display: flex;
  flex-direction: column;
  padding: 0;
}

.mn-01 #mn-01-toggle:checked ~ .mn-01__overlay ~ .mn-01__drawer {
  transform: translateX(0);
}

.mn-01__drawer-header {
  padding: 48px 24px 24px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}

.mn-01__avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), #f5a623);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  margin-bottom: 12px;
}

.mn-01__drawer-header h3 {
  color: var(--text);
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 2px;
}

.mn-01__drawer-header p {
  color: var(--muted);
  font-size: 13px;
}

.mn-01__nav {
  flex: 1;
  padding: 16px 0;
  overflow-y: auto;
}

.mn-01__nav a {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 24px;
  color: var(--muted);
  text-decoration: none;
  font-size: 15px;
  font-weight: 500;
  transition: all 0.2s;
  position: relative;
}

.mn-01__nav a:hover,
.mn-01__nav a.is-active {
  color: var(--text);
  background: rgba(233,69,96,0.08);
}

.mn-01__nav a.is-active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 60%;
  background: var(--accent);
  border-radius: 0 4px 4px 0;
}

.mn-01__nav-icon {
  width: 20px;
  text-align: center;
  font-size: 17px;
}

.mn-01__section-label {
  padding: 16px 24px 6px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: rgba(136,146,164,0.5);
}
/* Hamburger button */

.mn-01__hamburger {
  position: absolute;
  top: 16px;
  left: 16px;
  z-index: 30;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: rgba(255,255,255,0.06);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  transition: background 0.2s;
}

.mn-01__hamburger:hover {
  background: rgba(255,255,255,0.1);
}

.mn-01__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: center;
}

.mn-01 #mn-01-toggle:checked ~ .mn-01__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.mn-01 #mn-01-toggle:checked ~ .mn-01__hamburger span:nth-child(2) {
  opacity: 0;
  transform: scaleX(0);
}

.mn-01 #mn-01-toggle:checked ~ .mn-01__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
/* Main page content */

.mn-01__page {
  position: absolute;
  inset: 0;
  padding: 72px 20px 20px;
}

.mn-01__topbar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 60px;
}

.mn-01__topbar-title {
  color: var(--text);
  font-size: 17px;
  font-weight: 600;
}

.mn-01__content {
  margin-top: 16px;
}

.mn-01__card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 12px;
}

.mn-01__card h4 {
  color: var(--text);
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 6px;
}

.mn-01__card p {
  color: var(--muted);
  font-size: 12px;
  line-height: 1.6;
}

.mn-01__pill {
  display: inline-block;
  background: rgba(233,69,96,0.15);
  color: var(--accent);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 20px;
  margin-bottom: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .mn-01__drawer,
    .mn-01__overlay,
    .mn-01__hamburger span {
    transition: none;
  }
}
```
