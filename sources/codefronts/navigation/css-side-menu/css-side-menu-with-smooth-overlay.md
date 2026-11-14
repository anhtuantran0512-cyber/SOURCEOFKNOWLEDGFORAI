---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/css-side-menu-with-smooth-overlay/"
title: "CSS Side Menu with Smooth Overlay"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A sliding drawer that reveals a frosted-glass backdrop blur overlay over the main content area, using backdrop-filter and a second label element as the…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Side Menu with Smooth Overlay
Source: https://codefronts.com/navigation/css-side-menu/css-side-menu-with-smooth-overlay/

A sliding drawer that reveals a frosted-glass backdrop blur overlay over the main content area, using backdrop-filter and a second label element as the click-to-close target.
## HTML
```html
<div class="sm-02">
  <input type="checkbox" class="sm-02__toggle" id="sm-02-toggle">
  <label class="sm-02__burger" for="sm-02-toggle" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </label>
  <label class="sm-02__backdrop" for="sm-02-toggle"></label>
  <nav class="sm-02__nav">
    <div class="sm-02__section-label">Navigation</div>
    <div class="sm-02__links">
      <a class="sm-02__link sm-02__link--active" href="#">
        <span class="sm-02__link-dot"></span> Overview
      </a>
      <a class="sm-02__link" href="#">
        <span class="sm-02__link-dot"></span> Deployments
        <span class="sm-02__badge">12</span>
      </a>
      <a class="sm-02__link" href="#">
        <span class="sm-02__link-dot"></span> Integrations
      </a>
      <a class="sm-02__link" href="#">
        <span class="sm-02__link-dot"></span> Logs
        <span class="sm-02__badge">3</span>
      </a>
      <a class="sm-02__link" href="#">
        <span class="sm-02__link-dot"></span> Settings
      </a>
    </div>
    <div class="sm-02__footer">
      <div class="sm-02__avatar">AK</div>
      <div>
        <div class="sm-02__uname">Alex Kim</div>
        <div class="sm-02__urole">Admin</div>
      </div>
    </div>
  </nav>
  <div class="sm-02__content">
    <div class="sm-02__page-title">Overview</div>
    <div class="sm-02__body">
      <p>Open the drawer to see a frosted backdrop blur overlay appear behind the menu. Clicking the backdrop also closes it.</p>
      <div class="sm-02__grid">
        <div class="sm-02__tile"><div class="sm-02__tile-num">99.9%</div><div class="sm-02__tile-lbl">Uptime SLA</div></div>
        <div class="sm-02__tile"><div class="sm-02__tile-num">4.2ms</div><div class="sm-02__tile-lbl">Avg Latency</div></div>
        <div class="sm-02__tile"><div class="sm-02__tile-num">18k</div><div class="sm-02__tile-lbl">Requests / hr</div></div>
        <div class="sm-02__tile"><div class="sm-02__tile-num">0</div><div class="sm-02__tile-lbl">Open Incidents</div></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-02,
.sm-02 *,
.sm-02 *::before,
.sm-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-02 ::selection {
  background: #0ea5e9;
  color: #000;
}

.sm-02 {
  --bg: #030712;
  --surface: #111827;
  --drawer-bg: #060e1e;
  --accent: #0ea5e9;
  --accent2: #38bdf8;
  --text: #f1f5f9;
  --muted: #64748b;
  --border: rgba(14,165,233,0.15);
  --font: 'Syne', system-ui, sans-serif;
  --w: 300px;
  --ease: cubic-bezier(0.25, 0, 0.1, 1);
  --dur: 0.45s;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}

.sm-02__toggle {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
/* Overlay backdrop */

.sm-02__backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0);
  backdrop-filter: blur(0px);
  -webkit-backdrop-filter: blur(0px);
  transition: background var(--dur) var(--ease), backdrop-filter var(--dur) var(--ease);
  z-index: 30;
  pointer-events: none;
}

.sm-02__toggle:checked ~ .sm-02__backdrop {
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  pointer-events: all;
}
/* Burger */

.sm-02__burger {
  position: absolute;
  top: 18px;
  left: 18px;
  z-index: 50;
  display: flex;
  flex-direction: column;
  gap: 5px;
  width: 40px;
  height: 40px;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  background: rgba(14,165,233,0.1);
  border: 1px solid var(--border);
  border-radius: 10px;
  transition: background 0.2s;
}

.sm-02__burger:hover {
  background: rgba(14,165,233,0.25);
}

.sm-02__burger span {
  width: 18px;
  height: 2px;
  background: var(--accent2);
  border-radius: 2px;
  transition: transform var(--dur), opacity var(--dur);
  transform-origin: center;
}

.sm-02__toggle:checked ~ .sm-02__burger {
  z-index: 50;
}

.sm-02__toggle:checked ~ .sm-02__burger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.sm-02__toggle:checked ~ .sm-02__burger span:nth-child(2) {
  opacity: 0;
}

.sm-02__toggle:checked ~ .sm-02__burger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
/* Drawer */

.sm-02__nav {
  position: absolute;
  top: 0;
  left: 0;
  width: var(--w);
  height: 100%;
  background: var(--drawer-bg);
  border-right: 1px solid var(--border);
  transform: translateX(-100%);
  transition: transform var(--dur) var(--ease), box-shadow var(--dur);
  z-index: 40;
  display: flex;
  flex-direction: column;
  padding: 72px 0 20px;
}

.sm-02__toggle:checked ~ .sm-02__nav {
  transform: translateX(0);
  box-shadow: 0 0 60px rgba(14,165,233,0.12), 8px 0 40px rgba(0,0,0,0.6);
}
/* Top glow strip */

.sm-02__nav::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent), var(--accent2), transparent);
}

.sm-02__section-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 0 20px 8px;
  margin-top: 4px;
}

.sm-02__links {
  padding: 0 12px;
  flex: 1;
}

.sm-02__link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 14px;
  border-radius: 9px;
  color: var(--muted);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
  margin-bottom: 2px;
}

.sm-02__link::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 0;
  background: var(--accent);
  border-radius: 3px;
  transition: height 0.2s;
}

.sm-02__link:hover,
.sm-02__link--active {
  color: var(--text);
  background: rgba(14,165,233,0.1);
}

.sm-02__link--active::before,
.sm-02__link:hover::before {
  height: 70%;
}

.sm-02__link-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--muted);
  transition: background 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.sm-02__link--active .sm-02__link-dot,
.sm-02__link:hover .sm-02__link-dot {
  background: var(--accent);
  box-shadow: 0 0 8px var(--accent);
}

.sm-02__badge {
  margin-left: auto;
  background: rgba(14,165,233,0.2);
  color: var(--accent2);
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
}
/* User footer */

.sm-02__footer {
  padding: 16px 20px 0;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-02__avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg, #0ea5e9, #6366f1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  flex-shrink: 0;
}

.sm-02__uname {
  font-size: 13px;
  font-weight: 700;
}

.sm-02__urole {
  font-size: 11px;
  color: var(--muted);
}
/* Main content */

.sm-02__content {
  padding: 20px;
}

.sm-02__topbar {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 28px;
  padding-top: 6px;
}

.sm-02__page-title {
  font-size: 20px;
  font-weight: 800;
  margin-left: 50px;
}

.sm-02__body p {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 20px;
}

.sm-02__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.sm-02__tile {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 18px;
}

.sm-02__tile-num {
  font-size: 26px;
  font-weight: 800;
  color: var(--accent2);
}

.sm-02__tile-lbl {
  font-size: 12px;
  color: var(--muted);
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-02__nav,
    .sm-02__backdrop,
    .sm-02__burger span,
    .sm-02__link::before {
    transition: none;
  }
}
```
