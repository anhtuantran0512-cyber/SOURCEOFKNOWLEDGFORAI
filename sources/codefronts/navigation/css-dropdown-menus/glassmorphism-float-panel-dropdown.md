---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/glassmorphism-float-panel-dropdown/"
title: "Glassmorphism Float Panel Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A frosted-glass dropdown panel that floats above a vivid gradient background using backdrop-filter blur and translucent borders."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Float Panel Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/glassmorphism-float-panel-dropdown/

A frosted-glass dropdown panel that floats above a vivid gradient background using backdrop-filter blur and translucent borders.
## HTML
```html
<div class="dd-05">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <div class="dd-05__bg">
    <div class="dd-05__orb dd-05__orb--1"></div>
    <div class="dd-05__orb dd-05__orb--2"></div>
    <div class="dd-05__orb dd-05__orb--3"></div>
    <nav class="dd-05__nav">
      <span class="dd-05__brand">Aura</span>
      <div class="dd-05__items">
        <div class="dd-05__item">
          <a href="#" class="dd-05__trigger">Features ▾</a>
          <div class="dd-05__panel">
            <a href="#" class="dd-05__link">&#127775; AI Insights</a>
            <a href="#" class="dd-05__link">&#128202; Live Dashboard</a>
            <a href="#" class="dd-05__link">&#128274; Zero Trust Security</a>
            <a href="#" class="dd-05__link">&#9889; Real-time Sync</a>
          </div>
        </div>
        <div class="dd-05__item">
          <a href="#" class="dd-05__trigger">Pricing ▾</a>
          <div class="dd-05__panel">
            <a href="#" class="dd-05__link">&#127381; Free Plan</a>
            <a href="#" class="dd-05__link">&#128640; Pro Plan</a>
            <a href="#" class="dd-05__link">&#127959; Enterprise</a>
          </div>
        </div>
        <div class="dd-05__item">
          <a href="#" class="dd-05__trigger">About ▾</a>
          <div class="dd-05__panel">
            <a href="#" class="dd-05__link">&#128101; Our Team</a>
            <a href="#" class="dd-05__link">&#127759; Mission</a>
            <a href="#" class="dd-05__link">&#128240; Press Kit</a>
          </div>
        </div>
      </div>
    </nav>
  </div>
</div>
```
## CSS
```css
.dd-05,
.dd-05 *,
.dd-05 *::before,
.dd-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-05 ::selection {
  background: rgba(255,255,255,.4);
  color: #fff;
}

.dd-05 {
  font-family: 'Outfit', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.dd-05__bg {
  position: relative;
  width: 100%;
  min-height: 380px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 40%, #f093fb 100%);
  overflow: hidden;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 20px;
}

.dd-05__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.5;
}

.dd-05__orb--1 {
  width: 300px;
  height: 300px;
  background: #f093fb;
  top: -100px;
  left: -80px;
}

.dd-05__orb--2 {
  width: 250px;
  height: 250px;
  background: #4facfe;
  bottom: -80px;
  right: 0;
}

.dd-05__orb--3 {
  width: 200px;
  height: 200px;
  background: #f5af19;
  top: 40%;
  left: 40%;
}

.dd-05__nav {
  position: relative;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,255,255,0.15);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 100px;
  padding: 8px 8px 8px 24px;
  box-shadow: 0 8px 32px rgba(0,0,0,.2), inset 0 1px 0 rgba(255,255,255,.4);
}

.dd-05__brand {
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.3px;
  margin-right: 8px;
}

.dd-05__items {
  display: flex;
  gap: 2px;
}

.dd-05__item {
  position: relative;
}

.dd-05__item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 12px;
  /* hover-bridge: invisible strip below the trigger covering
       the visible gap before the panel. Lives on .__item (not
       the panel, which has overflow:hidden / pointer-events:
       none in its closed state) so the parent :hover stays
       active while the cursor traverses the gap. */
}

.dd-05__trigger {
  display: block;
  padding: 8px 16px;
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  border-radius: 100px;
  transition: background 0.18s, color 0.18s;
}

.dd-05__trigger:hover,
.dd-05__item:hover .dd-05__trigger {
  background: rgba(255,255,255,0.2);
  color: #fff;
}
/* glassmorphism panel */

.dd-05__panel {
  position: absolute;
  top: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%) translateY(-12px);
  min-width: 210px;
  background: rgba(255,255,255,0.18);
  -webkit-backdrop-filter: blur(24px) saturate(200%);
  backdrop-filter: blur(24px) saturate(200%);
  border: 1px solid rgba(255,255,255,0.35);
  border-radius: 16px;
  box-shadow: 0 16px 48px rgba(0,0,0,.25), inset 0 1px 0 rgba(255,255,255,.5), inset 0 -1px 0 rgba(255,255,255,.1);
  padding: 8px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.25s ease, transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
}

.dd-05__item:hover .dd-05__panel {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}

.dd-05__link {
  display: block;
  padding: 10px 14px;
  border-radius: 10px;
  text-decoration: none;
  color: rgba(255,255,255,0.9);
  font-size: 13.5px;
  font-weight: 500;
  transition: background 0.15s;
}

.dd-05__link:hover {
  background: rgba(255,255,255,0.2);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .dd-05__panel {
    transition: none;
  }
}
```
