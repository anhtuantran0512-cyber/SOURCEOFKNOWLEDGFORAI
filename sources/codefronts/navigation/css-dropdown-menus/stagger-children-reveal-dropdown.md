---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/stagger-children-reveal-dropdown/"
title: "Stagger Children Reveal Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "Each menu item cascades in one-by-one with staggered animation-delay values applied via nth-child, creating a flowing sequential reveal."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stagger Children Reveal Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/stagger-children-reveal-dropdown/

Each menu item cascades in one-by-one with staggered animation-delay values applied via nth-child, creating a flowing sequential reveal.
## HTML
```html
<div class="dd-06">
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
  <nav class="dd-06__nav">
    <span class="dd-06__brand">&#9670; Flow</span>
    <div class="dd-06__items">
      <div class="dd-06__item">
        <a href="#" class="dd-06__trigger">
          <span>Products</span>
          <span class="dd-06__arrow">▾</span>
        </a>
        <div class="dd-06__panel">
          <a href="#" class="dd-06__link" style="--i:0"><span class="dd-06__dot" style="--c:#6366f1"></span>Design Tokens</a>
          <a href="#" class="dd-06__link" style="--i:1"><span class="dd-06__dot" style="--c:#ec4899"></span>Component Kit</a>
          <a href="#" class="dd-06__link" style="--i:2"><span class="dd-06__dot" style="--c:#f59e0b"></span>Icon Library</a>
          <a href="#" class="dd-06__link" style="--i:3"><span class="dd-06__dot" style="--c:#10b981"></span>Figma Plugin</a>
          <a href="#" class="dd-06__link" style="--i:4"><span class="dd-06__dot" style="--c:#3b82f6"></span>CLI Tools</a>
        </div>
      </div>
      <div class="dd-06__item">
        <a href="#" class="dd-06__trigger">
          <span>Use Cases</span>
          <span class="dd-06__arrow">▾</span>
        </a>
        <div class="dd-06__panel">
          <a href="#" class="dd-06__link" style="--i:0"><span class="dd-06__dot" style="--c:#8b5cf6"></span>Startups</a>
          <a href="#" class="dd-06__link" style="--i:1"><span class="dd-06__dot" style="--c:#06b6d4"></span>Agencies</a>
          <a href="#" class="dd-06__link" style="--i:2"><span class="dd-06__dot" style="--c:#f97316"></span>Freelancers</a>
          <a href="#" class="dd-06__link" style="--i:3"><span class="dd-06__dot" style="--c:#14b8a6"></span>Enterprise</a>
        </div>
      </div>
      <div class="dd-06__item">
        <a href="#" class="dd-06__trigger">
          <span>Company</span>
          <span class="dd-06__arrow">▾</span>
        </a>
        <div class="dd-06__panel">
          <a href="#" class="dd-06__link" style="--i:0"><span class="dd-06__dot" style="--c:#ef4444"></span>About</a>
          <a href="#" class="dd-06__link" style="--i:1"><span class="dd-06__dot" style="--c:#a855f7"></span>Blog</a>
          <a href="#" class="dd-06__link" style="--i:2"><span class="dd-06__dot" style="--c:#0ea5e9"></span>Careers</a>
        </div>
      </div>
    </div>
  </nav>
</div>
```
## CSS
```css
.dd-06,
.dd-06 *,
.dd-06 *::before,
.dd-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-06 ::selection {
  background: #6366f1;
  color: #fff;
}

.dd-06 {
  --surface: #fff;
  --text: #1e293b;
  --border: #f1f5f9;
  --hover: #f8fafc;
  font-family: 'Nunito', sans-serif;
  min-height: 360px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 20px;
  background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 50%, #f0f9ff 100%);
}

.dd-06__nav {
  display: flex;
  align-items: center;
  gap: 4px;
  background: var(--surface);
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 10px 10px 10px 20px;
  box-shadow: 0 4px 20px rgba(0,0,0,.06);
  position: relative;
  z-index: 100;
}

.dd-06__brand {
  font-size: 17px;
  font-weight: 800;
  color: #6366f1;
  margin-right: 12px;
  letter-spacing: -0.3px;
}

.dd-06__items {
  display: flex;
  gap: 2px;
}

.dd-06__item {
  position: relative;
}

.dd-06__item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 10px;
  /* hover-bridge: invisible strip below the trigger covering
       the visible gap before the panel. Lives on .__item (not
       the panel, which has overflow:hidden / pointer-events:
       none in its closed state) so the parent :hover stays
       active while the cursor traverses the gap. */
}

.dd-06__trigger {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: 10px;
  color: var(--text);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  transition: background 0.15s, color 0.15s;
}

.dd-06__trigger:hover,
.dd-06__item:hover .dd-06__trigger {
  background: #eef2ff;
  color: #6366f1;
}

.dd-06__arrow {
  font-size: 12px;
  transition: transform 0.22s ease;
  color: #94a3b8;
}

.dd-06__item:hover .dd-06__arrow {
  transform: rotate(180deg);
  color: #6366f1;
}
/* panel */

.dd-06__panel {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
  min-width: 200px;
  background: var(--surface);
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  box-shadow: 0 12px 40px rgba(0,0,0,.10);
  padding: 8px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.18s ease;
}

.dd-06__item:hover .dd-06__panel {
  opacity: 1;
  pointer-events: auto;
}
/* stagger children */

@keyframes dd-06-slide-in {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.dd-06__link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 600;
  opacity: 0;
  transition: background 0.15s;
}

.dd-06__item:hover .dd-06__link {
  animation: dd-06-slide-in 0.32s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  animation-delay: calc(var(--i) * 60ms);
}

.dd-06__link:hover {
  background: var(--hover);
}

.dd-06__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--c, #6366f1);
  flex-shrink: 0;
}

@media (prefers-reduced-motion: reduce) {
  .dd-06__link {
    animation: none;
    opacity: 1;
  }

  .dd-06__panel {
    transition: none;
  }
}
```
