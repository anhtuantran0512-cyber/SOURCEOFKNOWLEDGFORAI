---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/product-grid-card/"
title: "Product Grid Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "E-commerce product tile with CSS-drawn kettle silhouette, NEW badge, star rating, strikethrough price, and add-to-cart CTA on a warm peach gradient."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Grid Card
Source: https://codefronts.com/components/css-cards/product-grid-card/

E-commerce product tile with CSS-drawn kettle silhouette, NEW badge, star rating, strikethrough price, and add-to-cart CTA on a warm peach gradient.
## HTML
```html
<section class="card-01" aria-label="Products">
  <header class="card-01__head">
    <div class="card-01__eyebrow">
      <span class="card-01__eye-dot" aria-hidden="true"></span>
      NEW ARRIVALS · KITCHEN
    </div>
    <div class="card-01__title-row">
      <h3 class="card-01__title">Trending this week</h3>
      <div class="card-01__filter" role="tablist" aria-label="Sort">
        <button type="button" role="tab" aria-selected="true" class="card-01__filter-btn card-01__filter-btn--active">Popular</button>
        <button type="button" role="tab" aria-selected="false" class="card-01__filter-btn">New</button>
      </div>
    </div>
  </header>

  <div class="card-01__row">

    <article class="card-01__card card-01__card--hero">
      <div class="card-01__media">
        <img class="card-01__img" src="https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=1000&q=80&auto=format&fit=crop" alt="Ceramic pour-over kettle by Fellow" loading="lazy" decoding="async">
        <div class="card-01__badges">
          <span class="card-01__badge card-01__badge--new">NEW</span>
          <span class="card-01__badge card-01__badge--best">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            BESTSELLER
          </span>
        </div>
        <button type="button" class="card-01__wish" aria-label="Add to wishlist">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
          <span class="card-01__wish-count">248</span>
        </button>
        <div class="card-01__quick">
          <button type="button" class="card-01__quick-btn">Quick add · $68</button>
        </div>
        <div class="card-01__stock">
          <span class="card-01__stock-dot" aria-hidden="true"></span>
          Ships tomorrow · 12 left
        </div>
      </div>
      <div class="card-01__body">
        <p class="card-01__eyebrow-sm">KITCHEN &middot; BREW</p>
        <div class="card-01__name-row">
          <h4 class="card-01__name">Ceramic Pour-Over Kettle</h4>
          <span class="card-01__brand">
            <span class="card-01__brand-mark" aria-hidden="true">F</span>
            Fellow
          </span>
        </div>
        <div class="card-01__rating" role="img" aria-label="Rated 4.8 out of 5, 127 reviews">
          <span class="card-01__stars">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          </span>
          <span class="card-01__rating-num">4.8<span class="card-01__rating-count"> (127)</span></span>
        </div>
        <div class="card-01__swatches" aria-label="Available colors">
          <span class="card-01__swatch card-01__swatch--1" aria-label="Matte black"></span>
          <span class="card-01__swatch card-01__swatch--2 card-01__swatch--active" aria-label="Cream"></span>
          <span class="card-01__swatch card-01__swatch--3" aria-label="Sage"></span>
          <span class="card-01__swatch-more">+2</span>
        </div>
        <div class="card-01__price-row">
          <div class="card-01__price">
            <span class="card-01__amt">$68</span>
            <span class="card-01__strike">$84</span>
            <span class="card-01__save">−19%</span>
          </div>
          <button type="button" class="card-01__cta">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            Add
          </button>
        </div>
        <div class="card-01__social">
          <div class="card-01__avatars" aria-hidden="true">
            <span class="card-01__av card-01__av--1">AR</span>
            <span class="card-01__av card-01__av--2">JL</span>
            <span class="card-01__av card-01__av--3">MK</span>
          </div>
          <span class="card-01__social-text">
            <strong>34</strong> people bought today
          </span>
        </div>
      </div>
    </article>

    <div class="card-01__col">

      <article class="card-01__card card-01__card--sm">
        <div class="card-01__media card-01__media--sm">
          <img class="card-01__img" src="https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?w=600&q=80&auto=format&fit=crop" alt="Reusable coffee filter" loading="lazy" decoding="async">
          <span class="card-01__badge card-01__badge--eco">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/></svg>
            ECO
          </span>
          <button type="button" class="card-01__wish card-01__wish--sm" aria-label="Wishlist">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
          </button>
        </div>
        <div class="card-01__body card-01__body--sm">
          <h4 class="card-01__name-sm">Stainless Reusable Filter</h4>
          <p class="card-01__brand-sm">Barista &amp; Co</p>
          <div class="card-01__rating-sm">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.6<span class="card-01__rating-count-sm"> · 89</span>
          </div>
          <div class="card-01__price-row card-01__price-row--sm">
            <span class="card-01__amt-sm">$24</span>
            <button type="button" class="card-01__cta card-01__cta--sm" aria-label="Add">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
            </button>
          </div>
        </div>
      </article>

      <article class="card-01__card card-01__card--sm">
        <div class="card-01__media card-01__media--sm">
          <img class="card-01__img" src="https://images.unsplash.com/photo-1611854779393-1b2da9d400fe?w=600&q=80&auto=format&fit=crop" alt="Single-origin coffee bag" loading="lazy" decoding="async">
          <span class="card-01__badge card-01__badge--limited">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            LIMITED
          </span>
          <button type="button" class="card-01__wish card-01__wish--sm" aria-label="Wishlist">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
          </button>
        </div>
        <div class="card-01__body card-01__body--sm">
          <h4 class="card-01__name-sm">Single-Origin Yirgacheffe</h4>
          <p class="card-01__brand-sm">Blue Bottle</p>
          <div class="card-01__rating-sm">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.9<span class="card-01__rating-count-sm"> · 342</span>
          </div>
          <div class="card-01__price-row card-01__price-row--sm">
            <span class="card-01__amt-sm">$32</span>
            <button type="button" class="card-01__cta card-01__cta--sm" aria-label="Add">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
            </button>
          </div>
        </div>
      </article>

    </div>

  </div>
</section>
```
## CSS
```css
.card-01 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 15%, rgba(245, 158, 11, 0.05) 0%, transparent 45%), radial-gradient(ellipse at 80% 85%, rgba(236, 72, 153, 0.04) 0%, transparent 45%), linear-gradient(180deg, #fff8f1 0%, #f4ede4 100%);
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #1a1a1a;
  --accent: #ea580c;
}

.card-01 *,
.card-01 *::before,
.card-01 *::after {
  box-sizing: border-box;
}
/* ── header ── */

.card-01__head {
  width: 100%;
  max-width: 780px;
  margin: 0 auto 18px;
}

.card-01__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #9a3412;
  padding: 4px 10px;
  background: rgba(234, 88, 12, 0.08);
  border: 1px solid rgba(234, 88, 12, 0.18);
  border-radius: 999px;
  margin-bottom: 10px;
}

.card-01__eye-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #ea580c;
  box-shadow: 0 0 8px rgba(234, 88, 12, 0.5);
  animation: card-01-pulse 2s ease-in-out infinite;
}

.card-01__title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.card-01__title {
  font-size: 20px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.025em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-01__filter {
  display: inline-flex;
  gap: 2px;
  padding: 3px;
  background: rgba(255, 255, 255, 0.65);
  border: 1px solid rgba(0, 0, 0, 0.04);
  border-radius: 999px;
}

.card-01__filter-btn {
  min-height: 26px;
  padding: 4px 10px;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: #6b6459;
  font: 700 11px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.005em;
  transition: color 0.18s, background 0.18s;
}

.card-01__filter-btn--active {
  background: #1a1a1a;
  color: #fff;
}

.card-01__filter-btn:hover {
  color: #1a1a1a;
}

.card-01__filter-btn--active:hover {
  color: #fff;
}

.card-01__filter-btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── row: 1 hero + 2 stacked small ── */

.card-01__row {
  width: 100%;
  max-width: 780px;
  display: grid;
  grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr);
  gap: 14px;
  align-items: stretch;
}

.card-01__col {
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-width: 0;
}
/* ── card base ── */

.card-01__card {
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 12px 30px -18px rgba(80, 40, 10, 0.15), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transition: transform 0.35s ease, box-shadow 0.35s, border-color 0.35s;
  display: flex;
  flex-direction: column;
}

.card-01__card:hover {
  transform: translateY(-3px);
  border-color: rgba(234, 88, 12, 0.24);
  box-shadow: 0 24px 44px -18px rgba(80, 40, 10, 0.22), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}

.card-01__card--sm {
  flex: 1;
}
/* ── media ── */

.card-01__media {
  position: relative;
  overflow: hidden;
  background: #f5f1e6;
  aspect-ratio: 1;
}

.card-01__media--sm {
  aspect-ratio: 4/3;
}

.card-01__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease, filter 0.5s;
}

.card-01__card:hover .card-01__img {
  transform: scale(1.05);
  filter: brightness(1.02);
}
/* badges row */

.card-01__badges {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  max-width: calc(100% - 60px);
}

.card-01__badge {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 3px 8px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border-radius: 5px;
}

.card-01__badge--new {
  background: #1a1a1a;
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.14);
}

.card-01__badge--best {
  background: linear-gradient(180deg, #fef3c7 0%, #fde68a 100%);
  color: #78350f;
  border: 1px solid rgba(146, 64, 14, 0.22);
  box-shadow: 0 2px 5px rgba(245, 158, 11, 0.25);
}

.card-01__badge--eco {
  background: linear-gradient(180deg, #d1fae5 0%, #a7f3d0 100%);
  color: #065f46;
  border: 1px solid rgba(6, 95, 70, 0.2);
}

.card-01__badge--limited {
  background: rgba(220, 38, 38, 0.9);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.14);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}
/* wishlist */

.card-01__wish {
  position: absolute;
  top: 10px;
  right: 10px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px 4px 6px;
  background: rgba(255, 255, 255, 0.92);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  color: #1a1a1a;
  font: 700 10.5px 'Inter', sans-serif;
  cursor: pointer;
  transition: color 0.18s, background 0.18s, transform 0.18s;
}

.card-01__wish:hover {
  color: #dc2626;
  transform: scale(1.05);
  background: rgba(255, 255, 255, 0.98);
}

.card-01__wish:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-01__wish-count {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-variant-numeric: tabular-nums;
}

.card-01__wish--sm {
  padding: 5px;
  top: 8px;
  right: 8px;
}

.card-01__wish--sm .card-01__wish-count {
  display: none;
}
/* quick add on hover */

.card-01__quick {
  position: absolute;
  bottom: 46px;
  left: 12px;
  right: 12px;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.25s, transform 0.25s;
  pointer-events: none;
}

.card-01__card:hover .card-01__quick {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.card-01__quick-btn {
  width: 100%;
  min-height: 36px;
  padding: 8px 12px;
  background: rgba(26, 26, 26, 0.92);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 10px;
  color: #fff;
  font: 700 12px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.01em;
  transition: background 0.18s;
}

.card-01__quick-btn:hover {
  background: rgba(26, 26, 26, 1);
}

.card-01__quick-btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* stock indicator */

.card-01__stock {
  position: absolute;
  bottom: 10px;
  left: 12px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 8px;
  background: rgba(255, 255, 255, 0.92);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  color: #065f46;
  font: 700 10px 'Inter', sans-serif;
  letter-spacing: -0.005em;
}

.card-01__stock-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 6px #10b981;
  animation: card-01-pulse 2s ease-in-out infinite;
}
/* ── body ── */

.card-01__body {
  padding: 14px 16px 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.card-01__eyebrow-sm {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #ea580c;
  margin: 0;
}

.card-01__name-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 8px;
}

.card-01__name {
  font-size: 15px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.015em;
  line-height: 1.3;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-01__brand {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10.5px;
  font-weight: 700;
  color: #6b6459;
  flex-shrink: 0;
  padding-top: 2px;
  letter-spacing: -0.005em;
}

.card-01__brand-mark {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
  border-radius: 4px;
  background: linear-gradient(135deg, #1a1a1a 0%, #4b4b57 100%);
  color: #fff;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0;
}
/* rating */

.card-01__rating {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 3px 7px;
  background: rgba(245, 158, 11, 0.08);
  border: 1px solid rgba(245, 158, 11, 0.18);
  border-radius: 999px;
  align-self: flex-start;
}

.card-01__stars {
  display: inline-flex;
  gap: 1px;
}

.card-01__rating-num {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10.5px;
  font-weight: 800;
  color: #92400e;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
}

.card-01__rating-count {
  color: #a1a1aa;
  font-weight: 700;
}
/* color swatches */

.card-01__swatches {
  display: flex;
  align-items: center;
  gap: 5px;
}

.card-01__swatch {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  border: 1.5px solid rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: transform 0.18s;
}

.card-01__swatch:hover {
  transform: scale(1.15);
}

.card-01__swatch--1 {
  background: #1a1a1a;
}

.card-01__swatch--2 {
  background: #f4ede4;
}

.card-01__swatch--3 {
  background: #7a8471;
}

.card-01__swatch--active {
  box-shadow: 0 0 0 2px #ea580c;
  border-color: #fff;
}

.card-01__swatch-more {
  font-size: 10px;
  font-weight: 700;
  color: #6b6459;
  letter-spacing: -0.005em;
}
/* price row */

.card-01__price-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-top: 4px;
}

.card-01__price {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.card-01__amt {
  font-size: 20px;
  font-weight: 800;
  color: #1a1a1a;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-01__strike {
  font-size: 12px;
  color: #a1a1aa;
  text-decoration: line-through;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.005em;
}

.card-01__save {
  display: inline-flex;
  align-items: center;
  padding: 2px 6px;
  background: linear-gradient(180deg, #dc2626, #b91c1c);
  color: #fff;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.02em;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(220, 38, 38, 0.28);
}
/* CTA */

.card-01__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  min-height: 34px;
  padding: 8px 14px;
  border: 0;
  border-radius: 999px;
  background: linear-gradient(180deg, #1e1e2c 0%, #06070c 100%);
  color: #fff;
  font: 800 12px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.01em;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2), 0 0 0 1px rgba(255, 255, 255, 0.14) inset, 0 -1px 0 rgba(255, 255, 255, 0.06) inset;
  transition: transform 0.18s, box-shadow 0.18s, background 0.18s;
}

.card-01__cta:hover {
  transform: translateY(-1px);
  background: linear-gradient(180deg, #ea580c 0%, #9a3412 100%);
  box-shadow: 0 6px 16px rgba(234, 88, 12, 0.32), 0 0 0 1px rgba(255, 255, 255, 0.2) inset;
}

.card-01__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* social row */

.card-01__social {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 6px;
  padding: 8px 10px;
  background: rgba(234, 88, 12, 0.05);
  border: 1px solid rgba(234, 88, 12, 0.14);
  border-radius: 10px;
}

.card-01__avatars {
  display: flex;
}

.card-01__av {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: #fff;
  font-size: 8px;
  font-weight: 800;
  border: 1.5px solid #fff;
  margin-left: -6px;
  letter-spacing: -0.02em;
}

.card-01__av:first-child {
  margin-left: 0;
}

.card-01__av--1 {
  background: linear-gradient(135deg, #f472b6, #ec4899);
}

.card-01__av--2 {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
}

.card-01__av--3 {
  background: linear-gradient(135deg, #34d399, #10b981);
}

.card-01__social-text {
  font-size: 10.5px;
  color: #9a3412;
  letter-spacing: -0.005em;
}

.card-01__social-text strong {
  color: #ea580c;
  font-weight: 800;
}
/* ── small card variant ── */

.card-01__body--sm {
  padding: 10px 12px 12px;
  gap: 6px;
}

.card-01__name-sm {
  font-size: 12.5px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.01em;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-01__brand-sm {
  font-size: 10px;
  color: #6b6459;
  margin: 0;
  font-weight: 600;
  letter-spacing: -0.005em;
}

.card-01__rating-sm {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 800;
  color: #92400e;
  font-variant-numeric: tabular-nums;
  padding: 2px 6px;
  background: rgba(245, 158, 11, 0.08);
  border-radius: 999px;
  align-self: flex-start;
  letter-spacing: -0.005em;
}

.card-01__rating-count-sm {
  color: #a1a1aa;
  font-weight: 700;
}

.card-01__price-row--sm {
  margin-top: 3px;
}

.card-01__amt-sm {
  font-size: 16px;
  font-weight: 800;
  color: #1a1a1a;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.card-01__cta--sm {
  min-height: 28px;
  min-width: 28px;
  padding: 6px;
}
/* mobile */

@media (max-width: 700px) {
  .card-01__row {
    grid-template-columns: 1fr;
    max-width: 360px;
  }

  .card-01__title-row {
    flex-direction: column;
    align-items: flex-start;
  }
}

@keyframes card-01-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-01__card,
    .card-01__img,
    .card-01__cta,
    .card-01__quick,
    .card-01__wish,
    .card-01__swatch,
    .card-01__filter-btn {
    transition: none;
  }

  .card-01__card:hover {
    transform: none;
  }

  .card-01__card:hover .card-01__img {
    transform: none;
  }

  .card-01__cta:hover,
    .card-01__wish:hover,
    .card-01__swatch:hover {
    transform: none;
  }

  .card-01__eye-dot,
    .card-01__stock-dot {
    animation: none;
  }
}
```
