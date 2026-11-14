---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/elastic-bounce-dropdown/"
title: "Elastic Bounce Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A playful dropdown that springs open with an elastic overshoot using a carefully tuned cubic-bezier on scaleY, giving it a bouncy physical feel."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Elastic Bounce Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/elastic-bounce-dropdown/

A playful dropdown that springs open with an elastic overshoot using a carefully tuned cubic-bezier on scaleY, giving it a bouncy physical feel.
## HTML
```html
<div class="dd-04">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <nav class="dd-04__nav">
    <span class="dd-04__brand">&#9670; Bounce</span>
    <div class="dd-04__items">
      <div class="dd-04__item">
        <a href="#" class="dd-04__trigger">Explore ▾</a>
        <div class="dd-04__panel">
          <a href="#" class="dd-04__link">&#127775; Featured</a>
          <a href="#" class="dd-04__link">&#128293; Trending</a>
          <a href="#" class="dd-04__link">&#128640; New Arrivals</a>
          <a href="#" class="dd-04__link">&#127942; Top Rated</a>
          <div class="dd-04__divider"></div>
          <a href="#" class="dd-04__link dd-04__link--cta">View All &#8594;</a>
        </div>
      </div>
      <div class="dd-04__item">
        <a href="#" class="dd-04__trigger">Learn ▾</a>
        <div class="dd-04__panel">
          <a href="#" class="dd-04__link">&#128218; Tutorials</a>
          <a href="#" class="dd-04__link">&#127916; Video Courses</a>
          <a href="#" class="dd-04__link">&#127881; Workshops</a>
        </div>
      </div>
      <div class="dd-04__item">
        <a href="#" class="dd-04__trigger">Connect ▾</a>
        <div class="dd-04__panel">
          <a href="#" class="dd-04__link">&#128172; Community</a>
          <a href="#" class="dd-04__link">&#128101; Forum</a>
          <a href="#" class="dd-04__link">&#128236; Newsletter</a>
        </div>
      </div>
    </div>
  </nav>
</div>
```
## CSS
```css
.dd-04,
.dd-04 *,
.dd-04 *::before,
.dd-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-04 ::selection {
  background: #ec4899;
  color: #fff;
}

.dd-04 {
  --brand: #ec4899;
  --brand-light: #fdf2f8;
  --surface: #fff;
  --text: #1e1b4b;
  --muted: #6b7280;
  --border: #f3f4f6;
  font-family: 'Plus Jakarta Sans', sans-serif;
  min-height: 360px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 20px;
  background: linear-gradient(135deg, #fdf2f8 0%, #fce7f3 50%, #ede9fe 100%);
}

.dd-04__nav {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--surface);
  border-radius: 100px;
  padding: 8px 8px 8px 24px;
  box-shadow: 0 4px 24px rgba(236,72,153,.15), 0 1px 4px rgba(0,0,0,.05);
  position: relative;
  z-index: 100;
}

.dd-04__brand {
  font-size: 16px;
  font-weight: 700;
  color: var(--brand);
  margin-right: 8px;
  letter-spacing: -0.3px;
}

.dd-04__items {
  display: flex;
  gap: 2px;
}

.dd-04__item {
  position: relative;
}

.dd-04__item::after {
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

.dd-04__trigger {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 8px 16px;
  border-radius: 100px;
  color: var(--text);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  transition: background 0.15s, color 0.15s;
}

.dd-04__trigger:hover,
.dd-04__item:hover .dd-04__trigger {
  background: var(--brand-light);
  color: var(--brand);
}
/* elastic bounce panel */

.dd-04__panel {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) scaleY(0);
  transform-origin: top center;
  min-width: 190px;
  background: var(--surface);
  border: 1px solid rgba(236,72,153,.12);
  border-radius: 16px;
  box-shadow: 0 12px 40px rgba(236,72,153,.18), 0 2px 8px rgba(0,0,0,.05);
  padding: 8px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  pointer-events: none;
  opacity: 0;
  transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.18s ease;
}

.dd-04__item:hover .dd-04__panel {
  transform: translateX(-50%) scaleY(1);
  opacity: 1;
  pointer-events: auto;
}

.dd-04__link {
  display: block;
  padding: 10px 14px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 500;
  transition: background 0.15s, color 0.15s;
}

.dd-04__link:hover {
  background: var(--brand-light);
  color: var(--brand);
}

.dd-04__link--cta {
  color: var(--brand);
  font-weight: 700;
}

.dd-04__divider {
  height: 1px;
  background: var(--border);
  margin: 4px 0;
}

@media (prefers-reduced-motion: reduce) {
  .dd-04__panel {
    transition: none;
  }
}
```
