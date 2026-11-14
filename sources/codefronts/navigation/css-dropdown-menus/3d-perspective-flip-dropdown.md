---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/3d-perspective-flip-dropdown/"
title: "3D Perspective Flip Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A dropdown panel that folds open from the top edge using rotateX perspective, simulating a physical lid being lifted."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Perspective Flip Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/3d-perspective-flip-dropdown/

A dropdown panel that folds open from the top edge using rotateX perspective, simulating a physical lid being lifted.
## HTML
```html
<div class="dd-03">
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@500;600;700&display=swap" rel="stylesheet">
  <nav class="dd-03__nav">
    <span class="dd-03__brand">NOVA</span>
    <div class="dd-03__items">
      <div class="dd-03__item">
        <a href="#" class="dd-03__trigger">Work</a>
        <div class="dd-03__perspective">
          <div class="dd-03__panel">
            <a href="#" class="dd-03__link">Case Studies</a>
            <a href="#" class="dd-03__link">Branding</a>
            <a href="#" class="dd-03__link">Motion</a>
            <a href="#" class="dd-03__link">Web Design</a>
          </div>
        </div>
      </div>
      <div class="dd-03__item">
        <a href="#" class="dd-03__trigger">Services</a>
        <div class="dd-03__perspective">
          <div class="dd-03__panel">
            <a href="#" class="dd-03__link">Strategy</a>
            <a href="#" class="dd-03__link">Design</a>
            <a href="#" class="dd-03__link">Development</a>
          </div>
        </div>
      </div>
      <div class="dd-03__item">
        <a href="#" class="dd-03__trigger">Studio</a>
        <div class="dd-03__perspective">
          <div class="dd-03__panel">
            <a href="#" class="dd-03__link">About</a>
            <a href="#" class="dd-03__link">Team</a>
            <a href="#" class="dd-03__link">Culture</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</div>
```
## CSS
```css
.dd-03,
.dd-03 *,
.dd-03 *::before,
.dd-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-03 ::selection {
  background: #0f172a;
  color: #e2e8f0;
}

.dd-03 {
  --ink: #0f172a;
  --surface: #f8fafc;
  --panel: #ffffff;
  --accent: #6366f1;
  --muted: #64748b;
  --border: #e2e8f0;
  font-family: 'Syne', sans-serif;
  min-height: 360px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 20px;
  background: linear-gradient(135deg, #f1f5f9 0%, #e0e7ff 100%);
}

.dd-03__nav {
  display: flex;
  align-items: center;
  gap: 40px;
  background: var(--ink);
  padding: 16px 32px;
  border-radius: 14px;
  box-shadow: 0 8px 32px rgba(15,23,42,.25);
  position: relative;
  z-index: 100;
}

.dd-03__brand {
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 3px;
  margin-right: auto;
}

.dd-03__items {
  display: flex;
  gap: 4px;
}

.dd-03__item {
  position: relative;
}
/* hover-bridge: invisible strip below the trigger covering the visible
   10px gap before the 3D perspective container (which has
   pointer-events:none in its closed state, so its own ::before bridge
   doesn't catch hover). */

.dd-03__item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 10px;
}

.dd-03__trigger {
  display: block;
  padding: 8px 16px;
  color: rgba(255,255,255,0.75);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.5px;
  border-radius: 8px;
  transition: color 0.15s, background 0.15s;
}

.dd-03__trigger:hover,
.dd-03__item:hover .dd-03__trigger {
  color: #fff;
  background: rgba(255,255,255,0.1);
}
/* 3D perspective container */

.dd-03__perspective {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
  perspective: 800px;
  transform-style: preserve-3d;
  pointer-events: none;
}

.dd-03__perspective::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -10px;
  height: 10px;
  /* invisible hover-bridge — keeps :hover active while
       the cursor traverses the visible gap between trigger
       and panel. */
}

.dd-03__item:hover .dd-03__perspective {
  pointer-events: auto;
}

.dd-03__panel {
  background: var(--panel);
  border-radius: 12px;
  border: 1px solid var(--border);
  box-shadow: 0 20px 60px rgba(15,23,42,.2);
  min-width: 180px;
  padding: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  transform: rotateX(-90deg);
  transform-origin: top center;
  opacity: 0;
  transition: transform 0.42s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.22s ease;
}

.dd-03__item:hover .dd-03__panel {
  transform: rotateX(0deg);
  opacity: 1;
}

.dd-03__link {
  display: block;
  padding: 10px 14px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--ink);
  font-size: 14px;
  font-weight: 500;
  transition: background 0.15s, color 0.15s;
}

.dd-03__link:hover {
  background: #eef2ff;
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .dd-03__panel {
    transition: none;
  }
}
```
