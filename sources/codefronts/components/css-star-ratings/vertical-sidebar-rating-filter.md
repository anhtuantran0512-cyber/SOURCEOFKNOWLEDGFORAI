---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/vertical-sidebar-rating-filter/"
title: "Vertical Sidebar Rating Filter"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "An e-commerce filter sidebar with stacked star-level checkboxes that highlight with a sky-blue accent border and tinted background on selection, beside a…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Sidebar Rating Filter
Source: https://codefronts.com/components/css-star-ratings/vertical-sidebar-rating-filter/

An e-commerce filter sidebar with stacked star-level checkboxes that highlight with a sky-blue accent border and tinted background on selection, beside a live product listing panel.
## HTML
```html
<div class="sr-10">
  <div class="sr-10__layout">
    <!-- Sidebar -->
    <aside class="sr-10__sidebar">
      <div class="sr-10__sidebar-title">Filters</div>

      <div class="sr-10__filter-group sr-10__stars-filter">
        <input type="checkbox" id="sr-10-f5" name="sr-10-filter" value="5">
        <label for="sr-10-f5" class="sr-10__filter-row">
          <div class="sr-10__mini">
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
          </div>
          <span class="sr-10__filter-text">&amp; up</span>
          <span class="sr-10__filter-count">148</span>
        </label>
      </div>

      <div class="sr-10__filter-group sr-10__stars-filter">
        <input type="checkbox" id="sr-10-f4" name="sr-10-filter" value="4">
        <label for="sr-10-f4" class="sr-10__filter-row">
          <div class="sr-10__mini">
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star"></div>
          </div>
          <span class="sr-10__filter-text">&amp; up</span>
          <span class="sr-10__filter-count">312</span>
        </label>
      </div>

      <div class="sr-10__filter-group sr-10__stars-filter">
        <input type="checkbox" id="sr-10-f3" name="sr-10-filter" value="3">
        <label for="sr-10-f3" class="sr-10__filter-row">
          <div class="sr-10__mini">
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star"></div>
            <div class="sr-10__mini-star"></div>
          </div>
          <span class="sr-10__filter-text">&amp; up</span>
          <span class="sr-10__filter-count">489</span>
        </label>
      </div>

      <div class="sr-10__filter-group sr-10__stars-filter">
        <input type="checkbox" id="sr-10-f2" name="sr-10-filter" value="2">
        <label for="sr-10-f2" class="sr-10__filter-row">
          <div class="sr-10__mini">
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star on"></div>
            <div class="sr-10__mini-star"></div>
            <div class="sr-10__mini-star"></div>
            <div class="sr-10__mini-star"></div>
          </div>
          <span class="sr-10__filter-text">&amp; up</span>
          <span class="sr-10__filter-count">531</span>
        </label>
      </div>

      <div class="sr-10__sidebar-divider"></div>

      <div class="sr-10__sidebar-section">
        <div class="sr-10__sidebar-section-title">Price Range</div>
        <div class="sr-10__price-range">
          <input type="number" class="sr-10__price-input" placeholder="$0" value="0">
          <input type="number" class="sr-10__price-input" placeholder="$999" value="999">
        </div>
      </div>
    </aside>

    <!-- Main -->
    <main class="sr-10__main">
      <div class="sr-10__main-title">Wireless Earbuds</div>
      <div class="sr-10__main-sub">531 results · sorted by rating</div>

      <div class="sr-10__products">
        <div class="sr-10__product">
          <div class="sr-10__product-img" style="background:#e0f2fe">🎵</div>
          <div class="sr-10__product-info">
            <div class="sr-10__product-name">AirPods Ultra Pro</div>
            <div class="sr-10__product-meta">
              <div class="sr-10__product-stars">
                <div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div>
              </div>
              <span class="sr-10__product-cnt">(2.1k)</span>
            </div>
          </div>
          <span class="sr-10__product-price">$189</span>
        </div>

        <div class="sr-10__product">
          <div class="sr-10__product-img" style="background:#fef3c7">🎧</div>
          <div class="sr-10__product-info">
            <div class="sr-10__product-name">SoundBuds Nano</div>
            <div class="sr-10__product-meta">
              <div class="sr-10__product-stars">
                <div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star"></div>
              </div>
              <span class="sr-10__product-cnt">(847)</span>
            </div>
          </div>
          <span class="sr-10__product-price">$79</span>
        </div>

        <div class="sr-10__product">
          <div class="sr-10__product-img" style="background:#f3e8ff">🔊</div>
          <div class="sr-10__product-info">
            <div class="sr-10__product-name">BassLine Sport X</div>
            <div class="sr-10__product-meta">
              <div class="sr-10__product-stars">
                <div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star"></div>
              </div>
              <span class="sr-10__product-cnt">(433)</span>
            </div>
          </div>
          <span class="sr-10__product-price">$59</span>
        </div>

        <div class="sr-10__product">
          <div class="sr-10__product-img" style="background:#dcfce7">🎤</div>
          <div class="sr-10__product-info">
            <div class="sr-10__product-name">ClearBuds Studio</div>
            <div class="sr-10__product-meta">
              <div class="sr-10__product-stars">
                <div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star on"></div><div class="sr-10__product-star"></div><div class="sr-10__product-star"></div>
              </div>
              <span class="sr-10__product-cnt">(219)</span>
            </div>
          </div>
          <span class="sr-10__product-price">$44</span>
        </div>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
.sr-10,
.sr-10 *,
.sr-10 *::before,
.sr-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-10 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.sr-10 {
  --sky: #0ea5e9;
  --sky-light: #38bdf8;
  --sky-glow: rgba(14,165,233,0.3);
  --bg-page: #f8fafc;
  --bg-white: #fff;
  --bg-hover: #f0f9ff;
  --text: #0f172a;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --star-empty: #cbd5e1;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-page);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-10__layout {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 0;
  max-width: 560px;
  width: 100%;
  background: var(--bg-white);
  border-radius: 18px;
  border: 1px solid var(--border);
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0,0,0,0.06);
}
/* Sidebar */

.sr-10__sidebar {
  border-right: 1px solid var(--border);
  padding: 24px 0;
}

.sr-10__sidebar-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--text-muted);
  padding: 0 20px 14px;
}

.sr-10__filter-group {
}

.sr-10__stars-filter input[type="checkbox"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-10__filter-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 20px;
  cursor: pointer;
  transition: background 0.15s;
  border-left: 2px solid transparent;
}

.sr-10__stars-filter input:checked + .sr-10__filter-row {
  background: var(--bg-hover);
  border-left-color: var(--sky);
}

.sr-10__filter-row:hover {
  background: var(--bg-hover);
}
/* Mini stars display (read-only) */

.sr-10__mini {
  display: flex;
  gap: 2px;
  flex-shrink: 0;
}

.sr-10__mini-star {
  width: 14px;
  height: 14px;
  background: var(--star-empty);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.15s;
}

.sr-10__mini-star.on {
  background: var(--sky);
}
/* Up-arrow label */

.sr-10__filter-text {
  flex: 1;
  font-size: 0.82rem;
  color: var(--text-muted);
  transition: color 0.15s;
}

.sr-10__stars-filter input:checked + .sr-10__filter-row .sr-10__filter-text {
  color: var(--sky);
  font-weight: 600;
}

.sr-10__filter-count {
  font-size: 0.72rem;
  color: var(--text-muted);
  background: var(--bg-page);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 1px 8px;
  font-weight: 600;
  transition: background 0.15s, border-color 0.15s, color 0.15s;
}

.sr-10__stars-filter input:checked + .sr-10__filter-row .sr-10__filter-count {
  background: rgba(14,165,233,0.1);
  border-color: rgba(14,165,233,0.3);
  color: var(--sky);
}

.sr-10__sidebar-divider {
  height: 1px;
  background: var(--border);
  margin: 16px 20px;
}

.sr-10__sidebar-section {
  padding: 0 20px;
}

.sr-10__sidebar-section-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--text-muted);
  margin-bottom: 12px;
}

.sr-10__price-range {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
}

.sr-10__price-input {
  flex: 1;
  /* min-width: 0 is critical — without it the native input's
       intrinsic content width (different for "0" vs "999") blocks
       flex: 1 from equalising the two inputs, so the max input
       renders much wider than the min input. */
  min-width: 0;
  width: 100%;
  padding: 6px 10px;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.8rem;
  color: var(--text);
  background: var(--bg-page);
  box-sizing: border-box;
}
/* Hide native number-input spinner buttons for a cleaner price-range
   look. Without these, Chrome/Safari add right-side stepper arrows
   that eat horizontal space inconsistently between the two fields. */

.sr-10__price-input::-webkit-inner-spin-button,
.sr-10__price-input::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.sr-10__price-input {
  -moz-appearance: textfield;
  appearance: textfield;
}
/* Main content area */

.sr-10__main {
  padding: 24px 20px;
}

.sr-10__main-title {
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-10__main-sub {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-bottom: 18px;
}
/* Product cards */

.sr-10__products {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.sr-10__product {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border: 1px solid var(--border);
  border-radius: 12px;
  transition: border-color 0.15s, background 0.15s;
}

.sr-10__product:hover {
  border-color: var(--sky-light);
  background: var(--bg-hover);
}

.sr-10__product-img {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  flex-shrink: 0;
}

.sr-10__product-info {
  flex: 1;
  min-width: 0;
}

.sr-10__product-name {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sr-10__product-meta {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 3px;
}

.sr-10__product-stars {
  display: flex;
  gap: 1px;
}

.sr-10__product-star {
  width: 10px;
  height: 10px;
  background: var(--star-empty);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
}

.sr-10__product-star.on {
  background: var(--sky);
}

.sr-10__product-cnt {
  font-size: 0.7rem;
  color: var(--text-muted);
}

.sr-10__product-price {
  font-size: 0.88rem;
  font-weight: 800;
  color: var(--sky);
  flex-shrink: 0;
}

@media (prefers-reduced-motion: reduce) {
  .sr-10__filter-row,
    .sr-10__product {
    transition: none;
  }
}
```
