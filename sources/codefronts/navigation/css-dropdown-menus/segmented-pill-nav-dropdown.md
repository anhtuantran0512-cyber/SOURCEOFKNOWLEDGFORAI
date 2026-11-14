---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/segmented-pill-nav-dropdown/"
title: "Segmented Pill Nav Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A pill-shaped navigation bar with a sliding background highlight that follows focus between segments, each revealing its own dropdown panel below."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Segmented Pill Nav Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/segmented-pill-nav-dropdown/

A pill-shaped navigation bar with a sliding background highlight that follows focus between segments, each revealing its own dropdown panel below.
## HTML
```html
<div class="dd-14">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <div class="dd-14__scene">
    <nav class="dd-14__rail">
      <div class="dd-14__seg">
        <button class="dd-14__pill">&#127968; Home</button>
        <div class="dd-14__drop">
          <a href="#" class="dd-14__link">Dashboard</a>
          <a href="#" class="dd-14__link">Overview</a>
          <a href="#" class="dd-14__link">Widgets</a>
        </div>
      </div>
      <div class="dd-14__seg">
        <button class="dd-14__pill">&#128202; Analytics</button>
        <div class="dd-14__drop">
          <a href="#" class="dd-14__link">Traffic</a>
          <a href="#" class="dd-14__link">Conversions</a>
          <a href="#" class="dd-14__link">Funnels</a>
          <a href="#" class="dd-14__link">Cohorts</a>
        </div>
      </div>
      <div class="dd-14__seg">
        <button class="dd-14__pill">&#128101; Audience</button>
        <div class="dd-14__drop">
          <a href="#" class="dd-14__link">Segments</a>
          <a href="#" class="dd-14__link">Profiles</a>
          <a href="#" class="dd-14__link">Behaviour</a>
        </div>
      </div>
      <div class="dd-14__seg">
        <button class="dd-14__pill">&#9881; Settings</button>
        <div class="dd-14__drop">
          <a href="#" class="dd-14__link">General</a>
          <a href="#" class="dd-14__link">Integrations</a>
          <a href="#" class="dd-14__link">Billing</a>
        </div>
      </div>
    </nav>
  </div>
</div>
```
## CSS
```css
.dd-14,
.dd-14 *,
.dd-14 *::before,
.dd-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-14 ::selection {
  background: #0f172a;
  color: #f8fafc;
}

.dd-14 {
  --trough: #f1f5f9;
  --pill-bg: #fff;
  --text: #0f172a;
  --muted: #64748b;
  --accent: #6366f1;
  --border: #e2e8f0;
  --shadow: 0 2px 8px rgba(0,0,0,.08);
  font-family: 'DM Sans', sans-serif;
  min-height: 360px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 36px 20px;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
}

.dd-14__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: 100%;
  position: relative;
  z-index: 100;
}

.dd-14__rail {
  display: flex;
  gap: 4px;
  background: var(--trough);
  border-radius: 100px;
  padding: 4px;
  box-shadow: inset 0 1px 3px rgba(0,0,0,.08);
}

.dd-14__seg {
  position: relative;
}
/* hover-bridge: invisible strip below the pill covering the 10px gap. */

.dd-14__seg::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 10px;
}

.dd-14__pill {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 9px 18px;
  border: none;
  border-radius: 100px;
  background: transparent;
  cursor: pointer;
  font-family: inherit;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--muted);
  transition: background 0.18s, color 0.18s, box-shadow 0.18s;
  white-space: nowrap;
  position: relative;
}

.dd-14__pill:hover,
.dd-14__seg:hover .dd-14__pill {
  background: var(--pill-bg);
  color: var(--text);
  box-shadow: var(--shadow);
}
/* dropdown */

.dd-14__drop {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) translateY(-6px);
  min-width: 160px;
  background: var(--pill-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 12px 36px rgba(0,0,0,.12);
  padding: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.26s cubic-bezier(0.16,1,0.3,1);
}

.dd-14__seg:hover .dd-14__drop {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}
/* Hover bridge — keeps :hover active while cursor crosses the 10px
   visible gap between the pill trigger and the dropdown panel. */

.dd-14__drop::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -10px;
  height: 10px;
}

.dd-14__link {
  display: block;
  padding: 9px 13px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 500;
  transition: background 0.14s, color 0.14s;
}

.dd-14__link:hover {
  background: #eef2ff;
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .dd-14__drop,
    .dd-14__pill {
    transition: none;
  }
}
```
