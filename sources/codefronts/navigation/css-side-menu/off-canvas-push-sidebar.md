---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/off-canvas-push-sidebar/"
title: "Off-Canvas Push Sidebar"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A side navigation that physically shifts the entire main content area horizontally when it opens rather than overlapping it, creating a genuine off-canvas…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Off-Canvas Push Sidebar
Source: https://codefronts.com/navigation/css-side-menu/off-canvas-push-sidebar/

A side navigation that physically shifts the entire main content area horizontally when it opens rather than overlapping it, creating a genuine off-canvas push effect.
## HTML
```html
<div class="sm-03">
  <input type="checkbox" class="sm-03__toggle" id="sm-03-toggle">
  <nav class="sm-03__nav">
    <div class="sm-03__nav-header">
      <div class="sm-03__logo">G</div>
      <div class="sm-03__brand">Grove App</div>
    </div>
    <div class="sm-03__links">
      <a class="sm-03__link sm-03__link--active" href="#"><span class="sm-03__link-icon">▦</span> Home</a>
      <a class="sm-03__link" href="#"><span class="sm-03__link-icon">◉</span> Analytics</a>
      <a class="sm-03__link" href="#"><span class="sm-03__link-icon">◈</span> Reports</a>
      <a class="sm-03__link" href="#"><span class="sm-03__link-icon">◬</span> Team</a>
      <a class="sm-03__link" href="#"><span class="sm-03__link-icon">⬡</span> Settings</a>
    </div>
  </nav>
  <div class="sm-03__shell">
    <div class="sm-03__main">
      <div class="sm-03__topbar">
        <label class="sm-03__burger" for="sm-03-toggle">
          <span></span><span></span><span></span>
        </label>
        <div class="sm-03__page-title">Dashboard</div>
      </div>
      <div class="sm-03__body">
        <p class="sm-03__desc">The entire content area physically slides right when the menu opens — true off-canvas push behaviour with zero JS.</p>
        <div class="sm-03__stats">
          <div class="sm-03__stat"><div class="sm-03__stat-val">7,291</div><div class="sm-03__stat-lbl">Visitors</div></div>
          <div class="sm-03__stat"><div class="sm-03__stat-val">89%</div><div class="sm-03__stat-lbl">Retention</div></div>
          <div class="sm-03__stat"><div class="sm-03__stat-val">$9.1k</div><div class="sm-03__stat-lbl">Revenue</div></div>
          <div class="sm-03__stat"><div class="sm-03__stat-val">312</div><div class="sm-03__stat-lbl">Signups</div></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-03,
.sm-03 *,
.sm-03 *::before,
.sm-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-03 ::selection {
  background: #10b981;
  color: #000;
}

.sm-03 {
  --bg: #0a0f0d;
  --surface: #131a16;
  --nav-bg: #0d1a13;
  --accent: #10b981;
  --accent2: #34d399;
  --text: #ecfdf5;
  --muted: #6b7280;
  --border: rgba(16,185,129,0.15);
  --w: 260px;
  --dur: 0.4s;
  --ease: cubic-bezier(0.4, 0, 0.2, 1);
  font-family: 'DM Sans', system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}

.sm-03__toggle {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
/* Layout shell: nav + main side by side */

.sm-03__shell {
  display: flex;
  height: 100%;
  min-height: 440px;
  transform: translateX(0);
  transition: transform var(--dur) var(--ease);
}

.sm-03__toggle:checked ~ .sm-03__shell {
  transform: translateX(var(--w));
}
/* Fixed nav (off-canvas) */

.sm-03__nav {
  position: absolute;
  left: 0;
  top: 0;
  width: var(--w);
  height: 100%;
  background: var(--nav-bg);
  border-right: 1px solid var(--border);
  transform: translateX(calc(-1 * var(--w)));
  transition: transform var(--dur) var(--ease);
  display: flex;
  flex-direction: column;
  padding: 24px 0;
  z-index: 20;
}

.sm-03__toggle:checked ~ .sm-03__nav {
  transform: translateX(0);
}

.sm-03__nav-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0 20px 20px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
}

.sm-03__logo {
  width: 32px;
  height: 32px;
  background: var(--accent);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
  color: #000;
}

.sm-03__brand {
  font-weight: 700;
  font-size: 15px;
}

.sm-03__links {
  flex: 1;
  padding: 0 10px;
}

.sm-03__link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 14px;
  border-radius: 8px;
  color: var(--muted);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 3px;
  text-decoration: none;
}

.sm-03__link:hover {
  color: var(--text);
  background: rgba(16,185,129,0.1);
}

.sm-03__link--active {
  color: var(--accent2);
  background: rgba(16,185,129,0.12);
  font-weight: 600;
}

.sm-03__link-icon {
  font-size: 16px;
}
/* Main content area */

.sm-03__main {
  flex: 1;
  min-width: 0;
  background: var(--bg);
  position: relative;
  z-index: 10;
}

.sm-03__topbar {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 20px;
  border-bottom: 1px solid var(--border);
}

.sm-03__burger {
  width: 38px;
  height: 38px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  cursor: pointer;
  flex-shrink: 0;
  transition: background 0.2s;
}

.sm-03__burger:hover {
  background: rgba(16,185,129,0.2);
}

.sm-03__burger span {
  width: 16px;
  height: 2px;
  background: var(--accent2);
  border-radius: 2px;
  transition: transform var(--dur), opacity var(--dur);
}

.sm-03__toggle:checked ~ .sm-03__shell .sm-03__burger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.sm-03__toggle:checked ~ .sm-03__shell .sm-03__burger span:nth-child(2) {
  opacity: 0;
}

.sm-03__toggle:checked ~ .sm-03__shell .sm-03__burger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.sm-03__page-title {
  font-size: 17px;
  font-weight: 700;
}

.sm-03__body {
  padding: 20px;
}

.sm-03__desc {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 20px;
}

.sm-03__stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sm-03__stat {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
}

.sm-03__stat-val {
  font-size: 22px;
  font-weight: 700;
  color: var(--accent2);
}

.sm-03__stat-lbl {
  font-size: 11px;
  color: var(--muted);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-03__shell,
    .sm-03__nav,
    .sm-03__burger span {
    transition: none;
  }
}
```
