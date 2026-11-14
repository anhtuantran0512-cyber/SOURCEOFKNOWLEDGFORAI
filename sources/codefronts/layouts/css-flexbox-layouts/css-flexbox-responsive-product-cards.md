---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-responsive-product-cards/"
title: "CSS Flexbox Responsive Product Cards"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "An e-commerce product card grid using flex: 1 1 180px with a max-width cap — cards reflow from four columns to one with no JavaScript or media queries."
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Responsive Product Cards
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-responsive-product-cards/

An e-commerce product card grid using flex: 1 1 180px with a max-width cap — cards reflow from four columns to one with no JavaScript or media queries.
## HTML
```html
<div class="fl-06">
  <div class="fl-06__header">
    <h2 class="fl-06__title">Product Collection</h2>
    <div class="fl-06__sort">Sort: Popular ▾</div>
  </div>
  <p class="fl-06__subtitle">flex: 1 1 180px — naturally wraps to 4, 3, 2, or 1 column at any width</p>

  <div class="fl-06__grid">

    <div class="fl-06__card">
      <div class="fl-06__thumb">
        <div class="fl-06__thumb-bg" style="background:linear-gradient(145deg,#fff1eb,#ffd4ba)">
          <svg class="fl-06__product-shape" width="70" height="70" viewBox="0 0 70 70">
            <ellipse cx="35" cy="40" rx="28" ry="20" fill="#ea580c" opacity="0.15"/>
            <rect x="20" y="12" width="30" height="36" rx="8" fill="#ea580c"/>
            <rect x="26" y="6" width="18" height="12" rx="4" fill="#c2410c"/>
          </svg>
        </div>
        <div class="fl-06__badge" style="background:#ef4444;color:#fff">Sale</div>
        <div class="fl-06__wishlist">♡</div>
      </div>
      <div class="fl-06__body">
        <div class="fl-06__cat">Gear</div>
        <div class="fl-06__name">Thermal Flask Pro</div>
        <div class="fl-06__stars">
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star" style="opacity:0.3">★</span>
          <span class="fl-06__rating-count">(241)</span>
        </div>
        <div class="fl-06__footer">
          <div class="fl-06__price">
            <div class="fl-06__price-now">$24</div>
            <div class="fl-06__price-was">$39</div>
          </div>
          <div class="fl-06__add-btn">+</div>
        </div>
      </div>
    </div>

    <div class="fl-06__card">
      <div class="fl-06__thumb">
        <div class="fl-06__thumb-bg" style="background:linear-gradient(145deg,#fef9ec,#fde68a)">
          <svg class="fl-06__product-shape" width="70" height="70" viewBox="0 0 70 70">
            <circle cx="35" cy="35" r="26" fill="#fbbf24" opacity="0.3"/>
            <circle cx="35" cy="35" r="18" fill="#d97706"/>
            <circle cx="35" cy="35" r="8" fill="#fef9ec"/>
          </svg>
        </div>
        <div class="fl-06__badge" style="background:#0ea5e9;color:#fff">New</div>
        <div class="fl-06__wishlist">♡</div>
      </div>
      <div class="fl-06__body">
        <div class="fl-06__cat">Audio</div>
        <div class="fl-06__name">Studio Buds X</div>
        <div class="fl-06__stars">
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star">★</span>
          <span class="fl-06__rating-count">(88)</span>
        </div>
        <div class="fl-06__footer">
          <div class="fl-06__price">
            <div class="fl-06__price-now">$89</div>
          </div>
          <div class="fl-06__add-btn">+</div>
        </div>
      </div>
    </div>

    <div class="fl-06__card">
      <div class="fl-06__thumb">
        <div class="fl-06__thumb-bg" style="background:linear-gradient(145deg,#f0fdf4,#bbf7d0)">
          <svg class="fl-06__product-shape" width="70" height="70" viewBox="0 0 70 70">
            <rect x="15" y="20" width="40" height="30" rx="6" fill="#16a34a" opacity="0.2"/>
            <rect x="20" y="15" width="30" height="32" rx="6" fill="#22c55e"/>
            <circle cx="35" cy="42" r="4" fill="#f0fdf4"/>
          </svg>
        </div>
        <div class="fl-06__badge" style="background:#22c55e;color:#fff">Eco</div>
        <div class="fl-06__wishlist">♡</div>
      </div>
      <div class="fl-06__body">
        <div class="fl-06__cat">Home</div>
        <div class="fl-06__name">Bamboo Notebook Set</div>
        <div class="fl-06__stars">
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star" style="opacity:0.3">★</span>
          <span class="fl-06__rating-count">(56)</span>
        </div>
        <div class="fl-06__footer">
          <div class="fl-06__price">
            <div class="fl-06__price-now">$18</div>
            <div class="fl-06__price-was">$25</div>
          </div>
          <div class="fl-06__add-btn">+</div>
        </div>
      </div>
    </div>

    <div class="fl-06__card">
      <div class="fl-06__thumb">
        <div class="fl-06__thumb-bg" style="background:linear-gradient(145deg,#fdf4ff,#f5d0fe)">
          <svg class="fl-06__product-shape" width="70" height="70" viewBox="0 0 70 70">
            <rect x="18" y="18" width="34" height="34" rx="10" fill="#a855f7" opacity="0.25"/>
            <rect x="22" y="22" width="26" height="26" rx="8" fill="#7c3aed"/>
            <rect x="29" y="29" width="12" height="12" rx="4" fill="#f5d0fe"/>
          </svg>
        </div>
        <div class="fl-06__wishlist">♡</div>
      </div>
      <div class="fl-06__body">
        <div class="fl-06__cat">Tech</div>
        <div class="fl-06__name">Wireless Charger Pad</div>
        <div class="fl-06__stars">
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star">★</span><span class="fl-06__star">★</span>
          <span class="fl-06__star">★</span>
          <span class="fl-06__rating-count">(312)</span>
        </div>
        <div class="fl-06__footer">
          <div class="fl-06__price">
            <div class="fl-06__price-now">$42</div>
          </div>
          <div class="fl-06__add-btn" style="background:#7c3aed">+</div>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.fl-06,
.fl-06 *,
.fl-06 *::before,
.fl-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-06 ::selection {
  background: #fb923c;
  color: #fff;
}

.fl-06 {
  --bg: #fff8f4;
  --surface: #fff;
  --ink: #1a0a00;
  --muted: #9a7a65;
  --accent: #ea580c;
  --accent2: #fb923c;
  --border: rgba(234,88,12,0.12);
  --star: #fbbf24;
  font-family: 'Outfit', sans-serif;
  background: var(--bg);
  padding: 24px;
  border-radius: 16px;
  min-height: 500px;
}

.fl-06__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.fl-06__title {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--ink);
}

.fl-06__sort {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
}

.fl-06__subtitle {
  font-size: 0.78rem;
  color: var(--muted);
  margin-bottom: 18px;
}
/* Product grid: flex-wrap + flex-basis for fluid columns */

.fl-06__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
}

.fl-06__card {
  flex: 1 1 180px;
  /* grow, shrink, min-basis = fluid cols */
  max-width: calc(25% - 11px);
  /* max 4 per row */
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.fl-06__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 14px 40px rgba(234,88,12,0.12);
}

.fl-06__thumb {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.fl-06__thumb-bg {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fl-06__product-shape {
  transition: transform 0.3s;
}

.fl-06__card:hover .fl-06__product-shape {
  transform: scale(1.08) rotate(3deg);
}

.fl-06__badge {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 0.62rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.fl-06__wishlist {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 28px;
  height: 28px;
  background: rgba(255,255,255,0.9);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  cursor: pointer;
}

.fl-06__body {
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.fl-06__cat {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fl-06__name {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.3;
}

.fl-06__stars {
  display: flex;
  align-items: center;
  gap: 2px;
  font-size: 0.7rem;
}

.fl-06__star {
  color: var(--star);
}

.fl-06__rating-count {
  font-size: 0.65rem;
  color: var(--muted);
  margin-left: 4px;
}

.fl-06__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: auto;
  padding-top: 10px;
  border-top: 1px solid var(--border);
}

.fl-06__price {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.fl-06__price-now {
  font-size: 1rem;
  font-weight: 800;
  color: var(--accent);
}

.fl-06__price-was {
  font-size: 0.75rem;
  text-decoration: line-through;
  color: var(--muted);
}

.fl-06__add-btn {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: var(--accent);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
  flex-shrink: 0;
}

.fl-06__add-btn:hover {
  background: #c2410c;
  transform: scale(1.1);
}

@media (prefers-reduced-motion: reduce) {
  .fl-06__card,
    .fl-06__product-shape,
    .fl-06__add-btn {
    transition: none;
  }
}
```
