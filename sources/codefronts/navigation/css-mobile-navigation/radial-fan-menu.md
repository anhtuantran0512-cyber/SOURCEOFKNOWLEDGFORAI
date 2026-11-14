---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/radial-fan-menu/"
title: "Radial Fan Menu"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A floating action button that rotates 45° on activation and fans out five labelled radial action items in a bottom-right arc, each with a staggered spring…"
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radial Fan Menu
Source: https://codefronts.com/navigation/css-mobile-navigation/radial-fan-menu/

A floating action button that rotates 45° on activation and fans out five labelled radial action items in a bottom-right arc, each with a staggered spring entrance via CSS cubic-bezier.
## HTML
```html
<div class="mn-05">
  <input type="checkbox" id="mn-05-toggle">
  <div class="mn-05__overlay"></div>

  <div class="mn-05__page">
    <div class="mn-05__header">
      <div class="mn-05__logo">Spark<span>AI</span></div>
    </div>
    <div class="mn-05__hero-text">
      <h2>Your creative workspace</h2>
      <p>Generate, edit, and share stunning visuals with AI-powered tools.</p>
    </div>
    <div class="mn-05__stat-row">
      <div class="mn-05__stat">
        <div class="mn-05__stat-val">248</div>
        <div class="mn-05__stat-label">Creations</div>
      </div>
      <div class="mn-05__stat">
        <div class="mn-05__stat-val">12k</div>
        <div class="mn-05__stat-label">Views</div>
      </div>
      <div class="mn-05__stat">
        <div class="mn-05__stat-val">94</div>
        <div class="mn-05__stat-label">Likes</div>
      </div>
    </div>
  </div>

  <div class="mn-05__radial-items">
    <div class="mn-05__radial-item">
      <div class="mn-05__radial-btn" style="background:var(--accent3)">🖼️</div>
      <span class="mn-05__radial-label">Gallery</span>
    </div>
    <div class="mn-05__radial-item">
      <div class="mn-05__radial-btn" style="background:var(--accent4)">✏️</div>
      <span class="mn-05__radial-label">Edit</span>
    </div>
    <div class="mn-05__radial-item">
      <div class="mn-05__radial-btn" style="background:var(--accent5)">📤</div>
      <span class="mn-05__radial-label">Share</span>
    </div>
    <div class="mn-05__radial-item">
      <div class="mn-05__radial-btn" style="background:var(--accent2)">⭐</div>
      <span class="mn-05__radial-label">Favorites</span>
    </div>
    <div class="mn-05__radial-item">
      <div class="mn-05__radial-btn" style="background:#0ea5e9">⚙️</div>
      <span class="mn-05__radial-label">Settings</span>
    </div>
  </div>

  <label for="mn-05-toggle" class="mn-05__fab">
    <span class="mn-05__fab-icon">+</span>
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

.mn-05 {
  --bg: #0f172a;
  --surface: #1e293b;
  --accent: #6366f1;
  --accent2: #ec4899;
  --accent3: #14b8a6;
  --accent4: #f59e0b;
  --accent5: #22c55e;
  --text: #f1f5f9;
  --muted: #64748b;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7);
}

.mn-05 #mn-05-toggle {
  display: none;
}
/* Background overlay */

.mn-05__overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.5);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
  z-index: 5;
}

.mn-05 #mn-05-toggle:checked ~ .mn-05__overlay {
  opacity: 1;
  pointer-events: all;
}
/* Page content */

.mn-05__page {
  position: absolute;
  inset: 0;
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
}

.mn-05__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 32px;
}

.mn-05__logo {
  font-size: 22px;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -0.5px;
}

.mn-05__logo span {
  color: var(--accent);
}

.mn-05__hero-text {
  margin-bottom: 24px;
}

.mn-05__hero-text h2 {
  font-size: 28px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.7px;
  line-height: 1.2;
  margin-bottom: 8px;
}

.mn-05__hero-text p {
  color: var(--muted);
  font-size: 14px;
  line-height: 1.6;
}

.mn-05__stat-row {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.mn-05__stat {
  flex: 1;
  background: var(--surface);
  border-radius: 14px;
  padding: 16px;
  border: 1px solid rgba(255,255,255,0.06);
}

.mn-05__stat-val {
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
}

.mn-05__stat-label {
  font-size: 11px;
  color: var(--muted);
  margin-top: 2px;
}
/* FAB button */

.mn-05__fab {
  position: absolute;
  bottom: 28px;
  right: 24px;
  z-index: 20;
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: var(--accent);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 32px rgba(99,102,241,0.5);
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), background 0.3s;
}

.mn-05__fab:hover {
  transform: scale(1.08);
}

.mn-05 #mn-05-toggle:checked ~ .mn-05__fab {
  background: var(--accent2);
  transform: rotate(45deg);
}

.mn-05__fab-icon {
  font-size: 22px;
  color: #fff;
  transition: transform 0.3s;
  line-height: 1;
}
/* Radial items */

.mn-05__radial-item {
  position: absolute;
  z-index: 15;
  display: flex;
  /* row-reverse: label sits to the LEFT of the btn. The btn is on
       the right edge of the item (anchored to the right:Npx arc
       position), and the label extends LEFTWARD into the empty page
       area instead of stacking vertically below the btn — that fixes
       the label/adjacent-btn overlap when buttons sit close on the
       vertical part of the arc. */
  flex-direction: row-reverse;
  align-items: center;
  gap: 8px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s, transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mn-05__radial-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}

.mn-05__radial-label {
  font-size: 10px;
  font-weight: 600;
  color: var(--text);
  background: rgba(0,0,0,0.6);
  padding: 2px 7px;
  border-radius: 20px;
  white-space: nowrap;
}
/* Items positioned on a 140px arc fanning out from the FAB center.
   FAB at bottom:28 right:24 (58x58) so FAB center is at bottom:57
   right:53. Item buttons are 48x48 → subtract 24 to center btn on
   the arc. Result:
     right  = 53 + 140*sin(θ) - 24 = 29 + 140*sin(θ)
     bottom = 57 + 140*cos(θ) - 24 = 33 + 140*cos(θ)
   Five items spread across 10°-85° with NON-LINEAR angle distribution
   (10°, 32°, 50°, 68°, 85°) so vertical spacing between adjacent items
   increases progressively along the arc — the top items where cos
   changes slowly get larger angular jumps to avoid label overlap.
   Source-order matches visual order: Gallery near top, Settings near
   left. */

.mn-05__radial-item:nth-child(1) {
  bottom: 171px;
  right: 53px;
  transform: translateY(20px) scale(0.7);
}
/* 10° Gallery   */

.mn-05__radial-item:nth-child(2) {
  bottom: 152px;
  right: 103px;
  transform: translateY(20px) scale(0.7);
}
/* 32° Edit      */

.mn-05__radial-item:nth-child(3) {
  bottom: 123px;
  right: 136px;
  transform: translateY(20px) scale(0.7);
}
/* 50° Share     */

.mn-05__radial-item:nth-child(4) {
  bottom: 86px;
  right: 159px;
  transform: translateY(20px) scale(0.7);
}
/* 68° Favorites */

.mn-05__radial-item:nth-child(5) {
  bottom: 45px;
  right: 168px;
  transform: translateY(20px) scale(0.7);
}
/* 85° Settings  */

.mn-05 #mn-05-toggle:checked ~ .mn-05__radial-items .mn-05__radial-item {
  opacity: 1;
  pointer-events: all;
}

.mn-05 #mn-05-toggle:checked ~ .mn-05__radial-items .mn-05__radial-item:nth-child(1) {
  transform: translateY(0) scale(1);
  transition-delay: 0.03s;
}

.mn-05 #mn-05-toggle:checked ~ .mn-05__radial-items .mn-05__radial-item:nth-child(2) {
  transform: translateY(0) scale(1);
  transition-delay: 0.08s;
}

.mn-05 #mn-05-toggle:checked ~ .mn-05__radial-items .mn-05__radial-item:nth-child(3) {
  transform: translateY(0) scale(1);
  transition-delay: 0.13s;
}

.mn-05 #mn-05-toggle:checked ~ .mn-05__radial-items .mn-05__radial-item:nth-child(4) {
  transform: translateY(0) scale(1);
  transition-delay: 0.18s;
}

.mn-05 #mn-05-toggle:checked ~ .mn-05__radial-items .mn-05__radial-item:nth-child(5) {
  transform: translateY(0) scale(1);
  transition-delay: 0.23s;
}

@media (prefers-reduced-motion: reduce) {
  .mn-05__fab,
    .mn-05__radial-item,
    .mn-05__overlay {
    transition: none;
  }
}
```
