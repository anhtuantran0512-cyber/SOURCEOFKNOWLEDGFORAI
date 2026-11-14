---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/fab-speed-dial-navigation/"
title: "FAB Speed Dial Navigation"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A map-style UI with a floating action button that expands into a vertical speed-dial stack of four labelled action items, each with a spring entrance."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAB Speed Dial Navigation
Source: https://codefronts.com/navigation/css-mobile-navigation/fab-speed-dial-navigation/

A map-style UI with a floating action button that expands into a vertical speed-dial stack of four labelled action items, each with a spring entrance. The FAB morphs from a rounded square to a circle and rotates 45°.
## HTML
```html
<div class="mn-07">
  <input type="checkbox" id="mn-07-toggle">
  <label class="mn-07__scrim" for="mn-07-toggle"></label>

  <div class="mn-07__map">
    <div class="mn-07__map-road"></div>
    <div class="mn-07__map-road"></div>
    <div class="mn-07__map-road"></div>
    <div class="mn-07__map-road"></div>
    <div class="mn-07__map-road"></div>
    <div class="mn-07__map-pin">📍</div>
  </div>

  <div class="mn-07__search">
    <span>🔍</span>
    <p>Search places...</p>
  </div>

  <div class="mn-07__speed-items">
    <div class="mn-07__speed-item">
      <span class="mn-07__speed-label">Directions</span>
      <div class="mn-07__speed-btn" style="background:#3b82f6">🗺️</div>
    </div>
    <div class="mn-07__speed-item">
      <span class="mn-07__speed-label">Nearby</span>
      <div class="mn-07__speed-btn" style="background:#10b981">📌</div>
    </div>
    <div class="mn-07__speed-item">
      <span class="mn-07__speed-label">Save Location</span>
      <div class="mn-07__speed-btn" style="background:#f59e0b">⭐</div>
    </div>
    <div class="mn-07__speed-item">
      <span class="mn-07__speed-label">Share</span>
      <div class="mn-07__speed-btn" style="background:#8b5cf6">📤</div>
    </div>
  </div>

  <label for="mn-07-toggle" class="mn-07__fab">
    <span class="mn-07__fab-icon">+</span>
  </label>
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

.mn-07 {
  --bg: #fafaf9;
  --surface: #ffffff;
  --border: #e7e5e4;
  --accent: #dc2626;
  --text: #1c1917;
  --muted: #78716c;
  --shadow: rgba(0,0,0,0.12);
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.5);
}

.mn-07 #mn-07-toggle {
  display: none;
}
/* Scrim */

.mn-07__scrim {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0);
  pointer-events: none;
  transition: background 0.3s;
  z-index: 5;
}

.mn-07 #mn-07-toggle:checked ~ .mn-07__scrim {
  background: rgba(0,0,0,0.2);
  pointer-events: all;
}
/* Map-style page */

.mn-07__map {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(250,250,249,0) 0%, rgba(250,250,249,0) 100%), repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(0,0,0,0.05) 39px, rgba(0,0,0,0.05) 40px), repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(0,0,0,0.05) 39px, rgba(0,0,0,0.05) 40px);
  background-color: #f5f0e8;
}

.mn-07__map-road {
  position: absolute;
  background: #fff;
  border-radius: 4px;
}

.mn-07__map-road:nth-child(1) {
  top: 120px;
  left: 0;
  right: 0;
  height: 18px;
}

.mn-07__map-road:nth-child(2) {
  top: 0;
  bottom: 0;
  left: 140px;
  width: 18px;
}

.mn-07__map-road:nth-child(3) {
  top: 280px;
  left: 0;
  right: 0;
  height: 10px;
}

.mn-07__map-road:nth-child(4) {
  top: 0;
  bottom: 0;
  left: 60px;
  width: 10px;
}

.mn-07__map-road:nth-child(5) {
  top: 0;
  bottom: 0;
  right: 80px;
  width: 10px;
}

.mn-07__map-pin {
  position: absolute;
  top: 90px;
  left: 110px;
  font-size: 28px;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
  transform: translate(-50%, -100%);
  animation: mn-07-drop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}

@keyframes mn-07-drop {
  from {
    transform: translate(-50%, -160%) scale(0.5);
    opacity: 0;
  }

  to {
    transform: translate(-50%, -100%) scale(1);
    opacity: 1;
  }
}
/* Search bar */

.mn-07__search {
  position: absolute;
  top: 20px;
  left: 16px;
  right: 16px;
  background: var(--surface);
  border-radius: 28px;
  padding: 14px 18px;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 4px 16px var(--shadow);
  z-index: 3;
}

.mn-07__search p {
  color: var(--muted);
  font-size: 14px;
}
/* Speed dial items */

.mn-07__speed-item {
  position: absolute;
  right: 24px;
  z-index: 15;
  display: flex;
  align-items: center;
  gap: 12px;
  opacity: 0;
  pointer-events: none;
  transform: scale(0.6) translateY(20px);
  transition: opacity 0.25s, transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mn-07__speed-label {
  background: rgba(28,25,23,0.85);
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 20px;
  white-space: nowrap;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.mn-07__speed-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.2);
  flex-shrink: 0;
}
/* Stacked upward from FAB at bottom: 100px */

.mn-07__speed-item:nth-child(1) {
  bottom: 104px;
}

.mn-07__speed-item:nth-child(2) {
  bottom: 164px;
}

.mn-07__speed-item:nth-child(3) {
  bottom: 224px;
}

.mn-07__speed-item:nth-child(4) {
  bottom: 284px;
}

.mn-07 #mn-07-toggle:checked ~ .mn-07__speed-items .mn-07__speed-item {
  opacity: 1;
  pointer-events: all;
}

.mn-07 #mn-07-toggle:checked ~ .mn-07__speed-items .mn-07__speed-item:nth-child(1) {
  transform: scale(1) translateY(0);
  transition-delay: 0s;
}

.mn-07 #mn-07-toggle:checked ~ .mn-07__speed-items .mn-07__speed-item:nth-child(2) {
  transform: scale(1) translateY(0);
  transition-delay: 0.05s;
}

.mn-07 #mn-07-toggle:checked ~ .mn-07__speed-items .mn-07__speed-item:nth-child(3) {
  transform: scale(1) translateY(0);
  transition-delay: 0.1s;
}

.mn-07 #mn-07-toggle:checked ~ .mn-07__speed-items .mn-07__speed-item:nth-child(4) {
  transform: scale(1) translateY(0);
  transition-delay: 0.15s;
}
/* FAB */

.mn-07__fab {
  position: absolute;
  bottom: 28px;
  right: 24px;
  z-index: 20;
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: var(--accent);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(220,38,38,0.45);
  transition: border-radius 0.3s, transform 0.2s;
}

.mn-07__fab:hover {
  transform: scale(1.05);
}

.mn-07 #mn-07-toggle:checked ~ .mn-07__fab {
  border-radius: 50%;
  transform: rotate(45deg);
}

.mn-07__fab-icon {
  font-size: 22px;
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .mn-07__speed-item,
    .mn-07__fab,
    .mn-07__scrim,
    .mn-07__map-pin {
    transition: none;
    animation: none;
  }
}
```
