---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-card-grid-layout/"
title: "CSS Flexbox Card Grid Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A responsive flex card grid with a featured wide card and uniform standard cards that wrap automatically — no media queries required for the basic reflow."
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Card Grid Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-card-grid-layout/

A responsive flex card grid with a featured wide card and uniform standard cards that wrap automatically — no media queries required for the basic reflow.
## HTML
```html
<div class="fl-02">
  <div class="fl-02__header">
    <h1 class="fl-02__title">Flex Card Grid</h1>
  </div>
  <p class="fl-02__subtitle">flex-wrap row layout with featured & standard cards</p>
  <div class="fl-02__filter-tabs">
    <div class="fl-02__tab is-active">All</div>
    <div class="fl-02__tab">Design</div>
    <div class="fl-02__tab">Dev</div>
    <div class="fl-02__tab">Motion</div>
  </div>

  <div class="fl-02__grid">

    <!-- Featured card -->
    <div class="fl-02__card fl-02__card--featured">
      <div class="fl-02__card-thumb">
        <div class="fl-02__card-thumb-bg" style="background: linear-gradient(135deg,#1a0533,#3b0f6e)">
          <div class="fl-02__card-thumb-shape" style="background:#b46fff;width:90px;height:90px"></div>
        </div>
        <div class="fl-02__card-badge" style="background:#ff6b6b">Featured</div>
      </div>
      <div class="fl-02__card-body">
        <div class="fl-02__card-category">Design System</div>
        <div class="fl-02__card-name">Flexbox Grid Patterns for Modern UIs</div>
        <div class="fl-02__card-desc">Master flex-wrap, flex-basis, and gap to build fluid, responsive card grids without a single media query. Featured items use flex: 2 for visual hierarchy.</div>
        <div class="fl-02__card-footer">
          <div class="fl-02__card-price">Free</div>
          <div class="fl-02__card-cta" style="background:#ff6b6b">Read More</div>
        </div>
      </div>
    </div>

    <!-- Card 2 -->
    <div class="fl-02__card">
      <div class="fl-02__card-thumb">
        <div class="fl-02__card-thumb-bg" style="background: linear-gradient(135deg,#003344,#006688)">
          <div class="fl-02__card-thumb-shape" style="background:#4d96ff"></div>
        </div>
        <div class="fl-02__card-badge" style="background:#4d96ff">New</div>
      </div>
      <div class="fl-02__card-body">
        <div class="fl-02__card-category">CSS Layout</div>
        <div class="fl-02__card-name">Auto Sizing with flex-basis</div>
        <div class="fl-02__card-desc">Use <code style="color:#4d96ff">flex: 1 1 200px</code> for columns that grow and wrap naturally.</div>
        <div class="fl-02__card-footer">
          <div class="fl-02__card-price">$12</div>
          <div class="fl-02__card-cta" style="background:#4d96ff">View</div>
        </div>
      </div>
    </div>

    <!-- Card 3 -->
    <div class="fl-02__card">
      <div class="fl-02__card-thumb">
        <div class="fl-02__card-thumb-bg" style="background: linear-gradient(135deg,#001a0d,#004d2a)">
          <div class="fl-02__card-thumb-shape" style="background:#6bcb77"></div>
        </div>
        <div class="fl-02__card-badge" style="background:#6bcb77">Guide</div>
      </div>
      <div class="fl-02__card-body">
        <div class="fl-02__card-category">Performance</div>
        <div class="fl-02__card-name">Gap vs Margin in Flex Rows</div>
        <div class="fl-02__card-desc">The <code style="color:#6bcb77">gap</code> property skips edge gutters. No negative-margin hacks needed.</div>
        <div class="fl-02__card-footer">
          <div class="fl-02__card-price">$8</div>
          <div class="fl-02__card-cta" style="background:#6bcb77">View</div>
        </div>
      </div>
    </div>

    <!-- Card 4 -->
    <div class="fl-02__card">
      <div class="fl-02__card-thumb">
        <div class="fl-02__card-thumb-bg" style="background: linear-gradient(135deg,#1a1000,#4d3500)">
          <div class="fl-02__card-thumb-shape" style="background:#ffd93d"></div>
        </div>
        <div class="fl-02__card-badge" style="background:#ffd93d;color:#1a1000">Pro</div>
      </div>
      <div class="fl-02__card-body">
        <div class="fl-02__card-category">Advanced</div>
        <div class="fl-02__card-name">Order & Reordering Flex Items</div>
        <div class="fl-02__card-desc">The <code style="color:#ffd93d">order</code> property reshuffles DOM order visually, ideal for mobile-first designs.</div>
        <div class="fl-02__card-footer">
          <div class="fl-02__card-price">$15</div>
          <div class="fl-02__card-cta" style="background:#ffd93d;color:#1a1000">View</div>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.fl-02,
.fl-02 *,
.fl-02 *::before,
.fl-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-02 ::selection {
  background: #ff6b6b;
  color: #fff;
}

.fl-02 {
  --ink: #1c1c1e;
  --muted: #8e8e93;
  --accent: #ff6b6b;
  --accent2: #ffd93d;
  --green: #6bcb77;
  --blue: #4d96ff;
  --surface: #0f0f13;
  --card: #1c1c24;
  --card-border: rgba(255,255,255,0.07);
  font-family: 'DM Sans', sans-serif;
  background: var(--surface);
  padding: 28px;
  min-height: 500px;
  border-radius: 16px;
}

.fl-02__header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 6px;
}

.fl-02__title {
  font-family: 'DM Serif Display', serif;
  font-size: 1.5rem;
  color: #fff;
}

.fl-02__subtitle {
  font-size: 0.78rem;
  color: var(--muted);
  margin-bottom: 20px;
}

.fl-02__filter-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

.fl-02__tab {
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  background: var(--card);
  color: var(--muted);
  border: 1px solid var(--card-border);
  transition: all 0.2s;
}

.fl-02__tab.is-active {
  background: var(--accent);
  color: #fff;
  border-color: transparent;
}
/* Card grid: flex-wrap row */

.fl-02__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
}
/* Featured: 2/3 width */

.fl-02__card {
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 14px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  flex: 1 1 calc(33% - 14px);
  min-width: 160px;
  transition: transform 0.2s, box-shadow 0.2s;
  cursor: pointer;
}

.fl-02__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}

.fl-02__card--featured {
  flex: 2 1 calc(66% - 7px);
  flex-direction: row;
}

.fl-02__card-thumb {
  height: 120px;
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}

.fl-02__card--featured .fl-02__card-thumb {
  width: 200px;
  height: auto;
}

.fl-02__card-thumb-bg {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fl-02__card-thumb-shape {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  opacity: 0.3;
  animation: fl-02-pulse 3s ease-in-out infinite;
}

@keyframes fl-02-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 0.3;
  }

  50% {
    transform: scale(1.15);
    opacity: 0.5;
  }
}

.fl-02__card-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  color: #fff;
}

.fl-02__card-body {
  padding: 14px;
  display: flex;
  flex-direction: column;
  flex: 1;
  gap: 6px;
}

.fl-02__card-category {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fl-02__card-name {
  font-size: 0.92rem;
  font-weight: 700;
  color: #fff;
  line-height: 1.3;
}

.fl-02__card--featured .fl-02__card-name {
  font-size: 1.1rem;
}

.fl-02__card-desc {
  font-size: 0.75rem;
  color: var(--muted);
  line-height: 1.6;
  flex: 1;
}

.fl-02__card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 4px;
  padding-top: 10px;
  border-top: 1px solid var(--card-border);
}

.fl-02__card-price {
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
}

.fl-02__card-cta {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 5px 12px;
  border-radius: 6px;
  color: #fff;
  letter-spacing: 0.04em;
}

@media (prefers-reduced-motion: reduce) {
  .fl-02__card-thumb-shape {
    animation: none;
  }

  .fl-02__card {
    transition: none;
  }
}
```
