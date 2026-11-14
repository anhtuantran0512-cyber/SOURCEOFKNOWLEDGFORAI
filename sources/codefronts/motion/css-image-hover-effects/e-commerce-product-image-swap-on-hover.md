---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/e-commerce-product-image-swap-on-hover/"
title: "E-Commerce Product Image Swap on Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Shopping-grid hover that cross-fades between a primary product angle and a secondary lifestyle image using stacked absolute elements."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Product Image Swap on Hover
Source: https://codefronts.com/motion/css-image-hover-effects/e-commerce-product-image-swap-on-hover/

Shopping-grid hover that cross-fades between a primary product angle and a secondary lifestyle image using stacked absolute elements.
## HTML
```html
<div class="ih-03">
  <div class="ih-03__grid">
    <div class="ih-03__card">
      <div class="ih-03__img-wrap">
        <div class="ih-03__img-primary ih-03__img--1a"><span class="ih-03__emoji">👟</span></div>
        <div class="ih-03__img-secondary ih-03__img--1b"><span class="ih-03__emoji">👟</span></div>
        <span class="ih-03__swap-badge">Hover</span>
      </div>
      <div class="ih-03__body">
        <p class="ih-03__name">AeroStep Pro Runner</p>
        <div class="ih-03__price-row">
          <span class="ih-03__price">$129</span>
          <span class="ih-03__old-price">$189</span>
        </div>
        <div class="ih-03__swatches">
          <span class="ih-03__swatch" style="background:#4338ca"></span>
          <span class="ih-03__swatch" style="background:#38bdf8"></span>
          <span class="ih-03__swatch" style="background:#f59e0b"></span>
        </div>
      </div>
    </div>
    <div class="ih-03__card">
      <div class="ih-03__img-wrap">
        <div class="ih-03__img-primary ih-03__img--2a"><span class="ih-03__emoji">👜</span></div>
        <div class="ih-03__img-secondary ih-03__img--2b"><span class="ih-03__emoji">👜</span></div>
        <span class="ih-03__swap-badge">Hover</span>
      </div>
      <div class="ih-03__body">
        <p class="ih-03__name">Nomad Leather Tote</p>
        <div class="ih-03__price-row">
          <span class="ih-03__price">$249</span>
          <span class="ih-03__old-price">$320</span>
        </div>
        <div class="ih-03__swatches">
          <span class="ih-03__swatch" style="background:#92400e"></span>
          <span class="ih-03__swatch" style="background:#4ade80"></span>
          <span class="ih-03__swatch" style="background:#e5e7eb"></span>
        </div>
      </div>
    </div>
    <div class="ih-03__card">
      <div class="ih-03__img-wrap">
        <div class="ih-03__img-primary ih-03__img--3a"><span class="ih-03__emoji">⌚</span></div>
        <div class="ih-03__img-secondary ih-03__img--3b"><span class="ih-03__emoji">⌚</span></div>
        <span class="ih-03__swap-badge">Hover</span>
      </div>
      <div class="ih-03__body">
        <p class="ih-03__name">Vertex Titanium Watch</p>
        <div class="ih-03__price-row">
          <span class="ih-03__price">$589</span>
          <span class="ih-03__old-price">$750</span>
        </div>
        <div class="ih-03__swatches">
          <span class="ih-03__swatch" style="background:#9ca3af"></span>
          <span class="ih-03__swatch" style="background:#f87171"></span>
          <span class="ih-03__swatch" style="background:#fbbf24"></span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-03,
.ih-03 *,
.ih-03 *::before,
.ih-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-03 ::selection {
  background: #f59e0b;
  color: #000;
}

.ih-03 {
  --accent: #f59e0b;
  --accent2: #10b981;
  --bg: #0d0d11;
  --card-bg: #16161f;
  --text: #f1f5f9;
  --muted: #64748b;
  --border: rgba(255,255,255,0.07);
  --duration: 0.5s;
  font-family: 'Inter', system-ui, sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-03__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  max-width: 780px;
  width: 100%;
}

.ih-03__card {
  background: var(--card-bg);
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid var(--border);
  transition: box-shadow 0.3s ease;
  cursor: pointer;
}

.ih-03__card:hover {
  box-shadow: 0 16px 48px rgba(0,0,0,0.4);
}

.ih-03__img-wrap {
  position: relative;
  aspect-ratio: 1;
  overflow: hidden;
}
/* Primary and secondary images stacked */

.ih-03__img-primary,
.ih-03__img-secondary {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity var(--duration) cubic-bezier(0.4, 0, 0.2, 1), transform var(--duration) cubic-bezier(0.4, 0, 0.2, 1);
}
/* Primary visible by default */

.ih-03__img-primary {
  opacity: 1;
  transform: scale(1);
  z-index: 1;
}
/* Secondary hidden by default */

.ih-03__img-secondary {
  opacity: 0;
  transform: scale(1.04);
  z-index: 2;
}
/* On hover: fade primary out, secondary in */

.ih-03__card:hover .ih-03__img-primary {
  opacity: 0;
  transform: scale(0.96);
}

.ih-03__card:hover .ih-03__img-secondary {
  opacity: 1;
  transform: scale(1);
}
/* Colour swatches as stand-ins for product angles */

.ih-03__img--1a {
  background: linear-gradient(135deg, #1e1b4b, #312e81, #4338ca);
}

.ih-03__img--1b {
  background: linear-gradient(135deg, #0c4a6e, #0369a1, #38bdf8);
}

.ih-03__img--2a {
  background: linear-gradient(135deg, #1a1007, #451a03, #92400e);
}

.ih-03__img--2b {
  background: linear-gradient(135deg, #052e16, #166534, #4ade80);
}

.ih-03__img--3a {
  background: linear-gradient(135deg, #1f1f2e, #374151, #9ca3af);
}

.ih-03__img--3b {
  background: linear-gradient(135deg, #310a0a, #7f1d1d, #f87171);
}

.ih-03__emoji {
  font-size: 52px;
  opacity: 0.5;
}

.ih-03__swap-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 10;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 20px;
  padding: 3px 8px;
  font-size: 9px;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  transition: opacity 0.25s;
}

.ih-03__card:hover .ih-03__swap-badge {
  opacity: 0;
}

.ih-03__body {
  padding: 14px 16px;
}

.ih-03__name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 4px;
}

.ih-03__price-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ih-03__price {
  font-size: 15px;
  font-weight: 700;
  color: var(--accent);
}

.ih-03__old-price {
  font-size: 11px;
  color: var(--muted);
  text-decoration: line-through;
}

.ih-03__swatches {
  display: flex;
  gap: 5px;
  margin-top: 10px;
}

.ih-03__swatch {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  border: 2px solid rgba(255,255,255,0.15);
}

@media (prefers-reduced-motion: reduce) {
  .ih-03__img-primary,
    .ih-03__img-secondary,
    .ih-03__swap-badge {
    transition: none;
  }
}
```
