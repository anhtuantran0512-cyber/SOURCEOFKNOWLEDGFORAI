---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/mega-menu-accordion/"
title: "Mega Menu Accordion"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A light-mode mobile nav where a hamburger toggles a full-height drawer containing three accordion sections."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mega Menu Accordion
Source: https://codefronts.com/navigation/css-mobile-navigation/mega-menu-accordion/

A light-mode mobile nav where a hamburger toggles a full-height drawer containing three accordion sections. Sections expand via max-height transitions with animated chevrons, all driven by Pure CSS checkboxes.
## HTML
```html
<div class="mn-09">
  <input type="checkbox" id="mn-09-main">
  <input type="checkbox" id="mn-09-a1" class="mn-09__acc-check">
  <input type="checkbox" id="mn-09-a2" class="mn-09__acc-check">
  <input type="checkbox" id="mn-09-a3" class="mn-09__acc-check">

  <div class="mn-09__topbar">
    <div class="mn-09__logo">Green<span>Co</span></div>
    <label for="mn-09-main" class="mn-09__nav-toggle">
      <div class="mn-09__nav-toggle-bars">
        <span></span><span></span><span></span>
      </div>
      Menu
    </label>
  </div>

  <nav class="mn-09__nav-drawer">
    <div class="mn-09__acc-item">
      <label for="mn-09-a1" class="mn-09__acc-label">
        <div class="mn-09__acc-label-left">
          <div class="mn-09__acc-icon" style="background:rgba(5,150,105,0.1)">🌿</div>
          Products
        </div>
        <div class="mn-09__acc-chevron">▼</div>
      </label>
      <div class="mn-09__acc-body">
        <div class="mn-09__sub-links">
          <a href="#">Organic Skincare <span class="mn-09__sub-badge">New</span></a>
          <a href="#">Supplements</a>
          <a href="#">Home & Garden</a>
          <a href="#">Food & Beverages</a>
        </div>
      </div>
    </div>

    <div class="mn-09__acc-item">
      <label for="mn-09-a2" class="mn-09__acc-label">
        <div class="mn-09__acc-label-left">
          <div class="mn-09__acc-icon" style="background:rgba(8,145,178,0.1)">📚</div>
          Resources
        </div>
        <div class="mn-09__acc-chevron">▼</div>
      </label>
      <div class="mn-09__acc-body">
        <div class="mn-09__sub-links">
          <a href="#">Blog & Articles</a>
          <a href="#">Sustainability Guide</a>
          <a href="#">Community</a>
        </div>
        <div class="mn-09__acc-promo">
          <span style="font-size:24px">🌱</span>
          <p>Join <strong>12,000+</strong> readers — free newsletter every week.</p>
        </div>
      </div>
    </div>

    <div class="mn-09__acc-item">
      <label for="mn-09-a3" class="mn-09__acc-label">
        <div class="mn-09__acc-label-left">
          <div class="mn-09__acc-icon" style="background:rgba(124,58,237,0.1)">🏢</div>
          Company
        </div>
        <div class="mn-09__acc-chevron">▼</div>
      </label>
      <div class="mn-09__acc-body">
        <div class="mn-09__sub-links">
          <a href="#">About Us</a>
          <a href="#">Careers <span class="mn-09__sub-badge">Hiring</span></a>
          <a href="#">Press</a>
          <a href="#">Contact</a>
        </div>
      </div>
    </div>

    <div class="mn-09__nav-footer">
      <a href="#">Sign In</a>
      <a href="#">Get Started →</a>
    </div>
  </nav>

  <div class="mn-09__page">
    <h2>Sustainable Living</h2>
    <p>Eco-friendly products for a greener lifestyle.</p>
    <div class="mn-09__feature-grid">
      <div class="mn-09__feature">
        <div class="mn-09__feature-icon">♻️</div>
        <h4>100% Recycled</h4>
        <p>All packaging uses post-consumer materials.</p>
      </div>
      <div class="mn-09__feature">
        <div class="mn-09__feature-icon">🌍</div>
        <h4>Carbon Neutral</h4>
        <p>Certified carbon-neutral shipping worldwide.</p>
      </div>
      <div class="mn-09__feature">
        <div class="mn-09__feature-icon">🌿</div>
        <h4>Organic</h4>
        <p>USDA certified organic ingredients only.</p>
      </div>
      <div class="mn-09__feature">
        <div class="mn-09__feature-icon">🐰</div>
        <h4>Cruelty-Free</h4>
        <p>Never tested on animals. Leaping Bunny certified.</p>
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

.mn-09 {
  --bg: #ffffff;
  --surface: #f9fafb;
  --border: #e5e7eb;
  --accent: #059669;
  --accent2: #0891b2;
  --accent3: #7c3aed;
  --text: #111827;
  --muted: #6b7280;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
}

.mn-09 input[type="checkbox"],
.mn-09 input[type="radio"] {
  display: none;
}
/* Top bar */

.mn-09__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
  z-index: 10;
  flex-shrink: 0;
}

.mn-09__logo {
  font-size: 18px;
  font-weight: 800;
  color: var(--text);
}

.mn-09__logo span {
  color: var(--accent);
}

.mn-09__nav-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  cursor: pointer;
  padding: 8px 14px;
  border: 1px solid var(--border);
  border-radius: 20px;
  transition: background 0.2s;
}

.mn-09__nav-toggle:hover {
  background: var(--surface);
}

.mn-09__nav-toggle-bars {
  width: 16px;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.mn-09__nav-toggle-bars span {
  display: block;
  height: 2px;
  background: var(--text);
  border-radius: 1px;
  transition: all 0.3s;
}

.mn-09__nav-toggle-bars span:nth-child(2) {
  width: 12px;
}

#mn-09-main:checked ~ .mn-09__topbar .mn-09__nav-toggle .mn-09__nav-toggle-bars span:nth-child(1) {
  transform: translateY(5px) rotate(45deg);
}

#mn-09-main:checked ~ .mn-09__topbar .mn-09__nav-toggle .mn-09__nav-toggle-bars span:nth-child(2) {
  opacity: 0;
}

#mn-09-main:checked ~ .mn-09__topbar .mn-09__nav-toggle .mn-09__nav-toggle-bars span:nth-child(3) {
  transform: translateY(-5px) rotate(-45deg);
  width: 16px;
}
/* Full nav drawer */

.mn-09__nav-drawer {
  position: absolute;
  top: 57px;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--bg);
  z-index: 9;
  transform: translateY(-100%);
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
}

#mn-09-main:checked ~ .mn-09__nav-drawer {
  transform: translateY(0);
}
/* Accordion items */

.mn-09__acc-item {
  border-bottom: 1px solid var(--border);
}

.mn-09__acc-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
  cursor: pointer;
  gap: 8px;
}

.mn-09__acc-label-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.mn-09__acc-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
}

.mn-09__acc-chevron {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--surface);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  transition: transform 0.3s;
  color: var(--muted);
}

.mn-09__acc-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  background: var(--surface);
}

.mn-09__acc-check:checked ~ .mn-09__acc-item .mn-09__acc-body {
  max-height: 300px;
}

.mn-09__acc-check:checked ~ .mn-09__acc-item .mn-09__acc-chevron {
  transform: rotate(180deg);
}

.mn-09__sub-links {
  padding: 8px 0 16px 60px;
}

.mn-09__sub-links a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px 10px 0;
  color: var(--muted);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.15s;
  border-bottom: 1px solid rgba(0,0,0,0.04);
}

.mn-09__sub-links a:last-child {
  border-bottom: none;
}

.mn-09__sub-links a:hover {
  color: var(--text);
}

.mn-09__sub-badge {
  margin-left: auto;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 10px;
  background: rgba(5,150,105,0.12);
  color: var(--accent);
}
/* Promo strip in accordion */

.mn-09__acc-promo {
  margin: 0 16px 16px;
  padding: 14px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(5,150,105,0.08), rgba(8,145,178,0.08));
  border: 1px solid rgba(5,150,105,0.2);
  display: flex;
  align-items: center;
  gap: 12px;
}

.mn-09__acc-promo p {
  font-size: 13px;
  color: var(--text);
  line-height: 1.4;
}

.mn-09__acc-promo strong {
  font-weight: 700;
  color: var(--accent);
}
/* Nav footer */

.mn-09__nav-footer {
  padding: 20px;
  display: flex;
  gap: 10px;
}

.mn-09__nav-footer a {
  flex: 1;
  text-align: center;
  padding: 12px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
}

.mn-09__nav-footer a:first-child {
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--border);
}

.mn-09__nav-footer a:last-child {
  background: var(--accent);
  color: #fff;
}
/* Page content */

.mn-09__page {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.mn-09__page h2 {
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.mn-09__page p {
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 20px;
}

.mn-09__feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.mn-09__feature {
  background: var(--surface);
  border-radius: 14px;
  padding: 16px;
  border: 1px solid var(--border);
}

.mn-09__feature-icon {
  font-size: 24px;
  margin-bottom: 8px;
}

.mn-09__feature h4 {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 4px;
}

.mn-09__feature p {
  font-size: 11px;
  color: var(--muted);
  line-height: 1.4;
  margin-bottom: 0;
}

@media (prefers-reduced-motion: reduce) {
  .mn-09__nav-drawer,
    .mn-09__acc-body,
    .mn-09__acc-chevron,
    .mn-09__nav-toggle-bars span {
    transition: none;
  }
}
```
