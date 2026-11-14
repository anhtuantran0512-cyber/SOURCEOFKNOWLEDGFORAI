---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/details-summary-native-dropdown/"
title: "Details Summary Native Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A fully CSS-only dropdown built on the native HTML details/summary element, styled with custom markers and animated with the [open] attribute selector."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Details Summary Native Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/details-summary-native-dropdown/

A fully CSS-only dropdown built on the native HTML details/summary element, styled with custom markers and animated with the [open] attribute selector.
## HTML
```html
<div class="dd-09">
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Source+Sans+3:wght@400;500;600&display=swap" rel="stylesheet">
  <div class="dd-09__layout">
    <nav class="dd-09__nav">
      <details class="dd-09__details">
        <summary class="dd-09__summary">
          <span class="dd-09__label">Discover</span>
          <span class="dd-09__arrow"></span>
        </summary>
        <div class="dd-09__panel">
          <a href="#" class="dd-09__link">Destinations</a>
          <a href="#" class="dd-09__link">Experiences</a>
          <a href="#" class="dd-09__link">Collections</a>
          <a href="#" class="dd-09__link">Guides</a>
        </div>
      </details>

      <details class="dd-09__details">
        <summary class="dd-09__summary">
          <span class="dd-09__label">Plan</span>
          <span class="dd-09__arrow"></span>
        </summary>
        <div class="dd-09__panel">
          <a href="#" class="dd-09__link">Trip Builder</a>
          <a href="#" class="dd-09__link">Booking</a>
          <a href="#" class="dd-09__link">Itineraries</a>
        </div>
      </details>

      <details class="dd-09__details">
        <summary class="dd-09__summary">
          <span class="dd-09__label">Journal</span>
          <span class="dd-09__arrow"></span>
        </summary>
        <div class="dd-09__panel">
          <a href="#" class="dd-09__link">Stories</a>
          <a href="#" class="dd-09__link">Photography</a>
          <a href="#" class="dd-09__link">Reviews</a>
        </div>
      </details>
    </nav>
    <p class="dd-09__hint">Click any nav item to toggle</p>
  </div>
</div>
```
## CSS
```css
.dd-09,
.dd-09 *,
.dd-09 *::before,
.dd-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-09 ::selection {
  background: #92400e;
  color: #fffbeb;
}

.dd-09 {
  --brand: #b45309;
  --surface: #fffbeb;
  --panel: #fff;
  --text: #1c1917;
  --muted: #78716c;
  --border: #e7e5e4;
  --hover: #fef3c7;
  font-family: 'Source Sans 3', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg, #fffbeb 0%, #fef3c7 100%);
  padding: 40px 20px;
}

.dd-09__layout {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: 100%;
  max-width: 640px;
}

.dd-09__nav {
  display: flex;
  gap: 12px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 10px;
  box-shadow: 0 4px 16px rgba(0,0,0,.06);
  width: 100%;
  justify-content: center;
}

.dd-09__details {
  position: relative;
  flex: 1;
  max-width: 180px;
}
/* hide default marker */

.dd-09__details > summary {
  list-style: none;
}

.dd-09__details > summary::-webkit-details-marker {
  display: none;
}

.dd-09__details > summary::marker {
  display: none;
}

.dd-09__summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
  user-select: none;
  color: var(--text);
  font-size: 14px;
  font-weight: 600;
  transition: background 0.15s, color 0.15s;
  gap: 8px;
}

.dd-09__summary:hover {
  background: var(--hover);
  color: var(--brand);
}

.dd-09__details[open] .dd-09__summary {
  background: var(--hover);
  color: var(--brand);
}

.dd-09__label {
  font-family: 'Lora', serif;
  font-size: 15px;
}

.dd-09__arrow {
  width: 16px;
  height: 16px;
  position: relative;
  flex-shrink: 0;
  overflow: hidden;
}

.dd-09__arrow::before,
.dd-09__arrow::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 7px;
  height: 1.5px;
  background: currentColor;
  transition: transform 0.22s ease;
}

.dd-09__arrow::before {
  left: 3px;
  transform: translateY(-50%) rotate(45deg);
  transform-origin: center;
}

.dd-09__arrow::after {
  right: 3px;
  transform: translateY(-50%) rotate(-45deg);
  transform-origin: center;
}

.dd-09__details[open] .dd-09__arrow::before {
  transform: translateY(-50%) rotate(-45deg);
}

.dd-09__details[open] .dd-09__arrow::after {
  transform: translateY(-50%) rotate(45deg);
}

.dd-09__panel {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  width: 100%;
  min-width: 160px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 10px;
  box-shadow: 0 8px 24px rgba(0,0,0,.10);
  padding: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  overflow: hidden;
  max-height: 0;
  opacity: 0;
  transition: max-height 0.34s ease, opacity 0.22s ease;
  z-index: 10;
}

.dd-09__details[open] .dd-09__panel {
  max-height: 400px;
  opacity: 1;
}

.dd-09__link {
  display: block;
  padding: 9px 12px;
  border-radius: 7px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 500;
  font-family: 'Lora', serif;
  transition: background 0.15s, color 0.15s;
}

.dd-09__link:hover {
  background: var(--hover);
  color: var(--brand);
}

.dd-09__hint {
  font-size: 12px;
  color: var(--muted);
  font-style: italic;
}

@media (prefers-reduced-motion: reduce) {
  .dd-09__panel,
    .dd-09__arrow::before,
    .dd-09__arrow::after,
    .dd-09__summary {
    transition: none;
  }
}
```
