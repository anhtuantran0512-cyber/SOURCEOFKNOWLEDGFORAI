---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/css-hover-triggered-sidebar-drawer/"
title: "CSS Hover-Triggered Sidebar Drawer"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A side navigation for wide viewports that slides open when the user hovers over a persistent thin edge trigger strip, using only CSS parent :hover to expand…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hover-Triggered Sidebar Drawer
Source: https://codefronts.com/navigation/css-side-menu/css-hover-triggered-sidebar-drawer/

A side navigation for wide viewports that slides open when the user hovers over a persistent thin edge trigger strip, using only CSS parent :hover to expand the drawer.
## HTML
```html
<div class="sm-14">
  <!-- Hover-trigger wrapper -->
  <div class="sm-14__drawer-wrap">
    <div class="sm-14__trigger">
      <div class="sm-14__trigger-inner"></div>
    </div>
    <nav class="sm-14__nav">
      <div class="sm-14__brand">
        <div class="sm-14__logo">T</div>
        <div class="sm-14__brand-name">Tidal</div>
      </div>
      <div class="sm-14__links">
        <a class="sm-14__link sm-14__link--active" href="#"><span class="sm-14__link-icon">⬡</span> Overview</a>
        <a class="sm-14__link" href="#"><span class="sm-14__link-icon">◈</span> Streams</a>
        <a class="sm-14__link" href="#"><span class="sm-14__link-icon">▦</span> Channels <span class="sm-14__badge">8</span></a>
        <a class="sm-14__link" href="#"><span class="sm-14__link-icon">◉</span> Alerts <span class="sm-14__badge">2</span></a>
        <a class="sm-14__link" href="#"><span class="sm-14__link-icon">⬙</span> Settings</a>
      </div>
      <div class="sm-14__user">
        <div class="sm-14__avatar">RJ</div>
        <div>
          <div class="sm-14__uname">R. Jensen</div>
          <div class="sm-14__urole">Operator</div>
        </div>
      </div>
    </nav>
  </div>
  <div class="sm-14__main">
    <div class="sm-14__heading">Hover Drawer</div>
    <div class="sm-14__sub">Slide-out sidebar triggered purely by hovering the thin edge rail — no checkbox, no JS. Uses CSS <code>:hover</code> on a parent wrapper.</div>
    <div class="sm-14__hint">
      ← Hover the teal edge strip to open the menu
    </div>
    <div class="sm-14__grid">
      <div class="sm-14__card"><div class="sm-14__card-val">4.1k</div><div class="sm-14__card-lbl">Events / sec</div></div>
      <div class="sm-14__card"><div class="sm-14__card-val">8</div><div class="sm-14__card-lbl">Active Streams</div></div>
      <div class="sm-14__card"><div class="sm-14__card-val">0</div><div class="sm-14__card-lbl">Alerts</div></div>
      <div class="sm-14__card"><div class="sm-14__card-val">99.8%</div><div class="sm-14__card-lbl">Uptime</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-14,
.sm-14 *,
.sm-14 *::before,
.sm-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-14 ::selection {
  background: #0f766e;
  color: #fff;
}

.sm-14 {
  --bg: #0a1628;
  --surface: #0f1f35;
  --trigger-bg: #071020;
  --accent: #14b8a6;
  --accent2: #2dd4bf;
  --text: #e2e8f0;
  --muted: #475569;
  --border: rgba(20,184,166,0.15);
  --font: 'Mulish', system-ui, sans-serif;
  --w: 240px;
  --trigger-w: 32px;
  --dur: 0.4s;
  --ease: cubic-bezier(0.4, 0, 0.2, 1);
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
}
/* Hot-zone trigger */

.sm-14__trigger {
  width: var(--trigger-w);
  min-height: 100vh;
  background: var(--trigger-bg);
  border-right: 1px solid rgba(20,184,166,0.35);
  flex-shrink: 0;
  position: relative;
  z-index: 10;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset -1px 0 0 rgba(20,184,166,0.15), 1px 0 12px rgba(20,184,166,0.08);
}
/* Hover indicator arrow */

.sm-14__trigger::before {
  content: '›';
  color: var(--accent2);
  font-size: 22px;
  font-weight: 800;
  line-height: 1;
  padding-left: 2px;
  text-shadow: 0 0 8px rgba(20,184,166,0.4);
  transition: color 0.2s, transform 0.2s, text-shadow 0.2s;
}
/* When trigger is hovered, expand the drawer */

.sm-14__trigger:hover::before {
  color: var(--accent);
  transform: scale(1.3);
}
/* Hover zone + nav — use :has or a sibling approach */
/* Use a wrapper around trigger+nav for :hover on parent */

.sm-14__drawer-wrap {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: var(--trigger-w);
  z-index: 20;
  transition: width var(--dur) var(--ease);
}

.sm-14__drawer-wrap:hover {
  width: calc(var(--trigger-w) + var(--w));
}

.sm-14__drawer-wrap:hover .sm-14__trigger::before {
  content: '‹';
  transform: scale(1.15);
  color: var(--accent2);
}

.sm-14__drawer-wrap:hover .sm-14__nav {
  transform: translateX(0);
  box-shadow: 8px 0 40px rgba(0,0,0,0.5);
}

.sm-14__trigger-inner {
  width: var(--trigger-w);
  height: 100%;
}

.sm-14__nav {
  position: absolute;
  top: 0;
  left: var(--trigger-w);
  width: var(--w);
  height: 100%;
  background: var(--surface);
  border-right: 1px solid var(--border);
  transform: translateX(calc(-1 * var(--w)));
  transition: transform var(--dur) var(--ease);
  display: flex;
  flex-direction: column;
  padding: 24px 0;
}

.sm-14__nav::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 1px;
  height: 100%;
  background: linear-gradient(180deg, transparent, var(--accent), transparent);
  opacity: 0.4;
}

.sm-14__brand {
  padding: 0 18px 18px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-14__logo {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  color: #000;
  font-size: 14px;
}

.sm-14__brand-name {
  font-size: 15px;
  font-weight: 800;
}

.sm-14__links {
  flex: 1;
  padding: 0 10px;
}

.sm-14__link {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 11px 14px;
  border-radius: 9px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
  margin-bottom: 3px;
  white-space: nowrap;
}

.sm-14__link:hover {
  color: var(--text);
  background: rgba(20,184,166,0.1);
}

.sm-14__link--active {
  color: var(--accent2);
  background: rgba(20,184,166,0.12);
}

.sm-14__link-icon {
  font-size: 15px;
  flex-shrink: 0;
}

.sm-14__badge {
  margin-left: auto;
  background: rgba(20,184,166,0.2);
  color: var(--accent2);
  font-size: 10px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 99px;
}

.sm-14__user {
  padding: 14px 18px 0;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-14__avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), #6366f1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  color: #fff;
}

.sm-14__uname {
  font-size: 12px;
  font-weight: 800;
}

.sm-14__urole {
  font-size: 10px;
  color: var(--muted);
}
/* Main */

.sm-14__main {
  flex: 1;
  padding: 24px 22px 22px 50px;
}

.sm-14__heading {
  font-size: 20px;
  font-weight: 800;
  margin-bottom: 6px;
}

.sm-14__sub {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 22px;
}
/* Tooltip hint */

.sm-14__hint {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(20,184,166,0.08);
  border: 1px solid rgba(20,184,166,0.2);
  border-radius: 9px;
  padding: 12px 14px;
  font-size: 13px;
  color: var(--accent2);
  font-weight: 600;
  margin-bottom: 20px;
}

.sm-14__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sm-14__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 9px;
  padding: 14px;
}

.sm-14__card-val {
  font-size: 20px;
  font-weight: 800;
  color: var(--accent2);
}

.sm-14__card-lbl {
  font-size: 11px;
  color: var(--muted);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-14__nav,
    .sm-14__trigger::before {
    transition: none;
  }
}
```
