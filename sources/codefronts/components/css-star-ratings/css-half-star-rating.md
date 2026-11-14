---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/css-half-star-rating/"
title: "CSS Half Star Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A dark-mode product card supporting half-star precision (0.5 increments) via a split-label overlay technique — two radio inputs per star position, mint-green…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Half Star Rating
Source: https://codefronts.com/components/css-star-ratings/css-half-star-rating/

A dark-mode product card supporting half-star precision (0.5 increments) via a split-label overlay technique — two radio inputs per star position, mint-green palette on charcoal.
## HTML
```html
<div class="sr-03">
  <div class="sr-03__card">
    <div class="sr-03__product">
      <div class="sr-03__thumb">🌿</div>
      <div class="sr-03__info">
        <div class="sr-03__pname">EcoBalance Supplement</div>
        <div class="sr-03__psub">Organic · 60 capsules · Subscribe & Save</div>
        <div class="sr-03__price">$34.99</div>
      </div>
    </div>

    <div class="sr-03__label">Your Rating (Half Stars Supported)</div>
    <form>
      <div class="sr-03__stars">
        <!-- 5 full + 5 half radios interleaved, reversed for CSS trick -->
        <input type="radio" class="sr-03__full-in" id="sr-03-f5" name="sr-03-r" value="5">
        <label for="sr-03-f5" class="sr-03__full">5 stars</label>
        <input type="radio" class="sr-03__half-in" id="sr-03-h5" name="sr-03-r" value="4.5">
        <label for="sr-03-h5" class="sr-03__half">4.5 stars</label>

        <input type="radio" class="sr-03__full-in" id="sr-03-f4" name="sr-03-r" value="4">
        <label for="sr-03-f4" class="sr-03__full">4 stars</label>
        <input type="radio" class="sr-03__half-in" id="sr-03-h4" name="sr-03-r" value="3.5">
        <label for="sr-03-h4" class="sr-03__half">3.5 stars</label>

        <input type="radio" class="sr-03__full-in" id="sr-03-f3" name="sr-03-r" value="3">
        <label for="sr-03-f3" class="sr-03__full">3 stars</label>
        <input type="radio" class="sr-03__half-in" id="sr-03-h3" name="sr-03-r" value="2.5">
        <label for="sr-03-h3" class="sr-03__half">2.5 stars</label>

        <input type="radio" class="sr-03__full-in" id="sr-03-f2" name="sr-03-r" value="2">
        <label for="sr-03-f2" class="sr-03__full">2 stars</label>
        <input type="radio" class="sr-03__half-in" id="sr-03-h2" name="sr-03-r" value="1.5">
        <label for="sr-03-h2" class="sr-03__half">1.5 stars</label>

        <input type="radio" class="sr-03__full-in" id="sr-03-f1" name="sr-03-r" value="1">
        <label for="sr-03-f1" class="sr-03__full">1 star</label>
        <input type="radio" class="sr-03__half-in" id="sr-03-h1" name="sr-03-r" value="0.5">
        <label for="sr-03-h1" class="sr-03__half">0.5 stars</label>
      </div>
    </form>

    <div class="sr-03__tally">
      <div class="sr-03__score">4.5</div>
      <div class="sr-03__breakdown">
        <div class="sr-03__bar-row">
          <span class="sr-03__bar-label">5</span>
          <div class="sr-03__bar-track"><div class="sr-03__bar-fill" style="width:68%"></div></div>
          <span class="sr-03__bar-pct">68%</span>
        </div>
        <div class="sr-03__bar-row">
          <span class="sr-03__bar-label">4</span>
          <div class="sr-03__bar-track"><div class="sr-03__bar-fill" style="width:20%"></div></div>
          <span class="sr-03__bar-pct">20%</span>
        </div>
        <div class="sr-03__bar-row">
          <span class="sr-03__bar-label">3</span>
          <div class="sr-03__bar-track"><div class="sr-03__bar-fill" style="width:8%"></div></div>
          <span class="sr-03__bar-pct">8%</span>
        </div>
        <div class="sr-03__bar-row">
          <span class="sr-03__bar-label">2</span>
          <div class="sr-03__bar-track"><div class="sr-03__bar-fill" style="width:3%"></div></div>
          <span class="sr-03__bar-pct">3%</span>
        </div>
        <div class="sr-03__bar-row">
          <span class="sr-03__bar-label">1</span>
          <div class="sr-03__bar-track"><div class="sr-03__bar-fill" style="width:1%"></div></div>
          <span class="sr-03__bar-pct">1%</span>
        </div>
      </div>
    </div>
    <div class="sr-03__count">Based on 2,847 verified reviews</div>
  </div>
</div>
```
## CSS
```css
.sr-03,
.sr-03 *,
.sr-03 *::before,
.sr-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-03 ::selection {
  background: #10b981;
  color: #fff;
}

.sr-03 {
  --mint: #10b981;
  --mint-light: #34d399;
  --mint-glow: rgba(16,185,129,0.35);
  --bg-dark: #111827;
  --bg-card: #1f2937;
  --bg-hover: #374151;
  --text: #f9fafb;
  --text-muted: #9ca3af;
  --border: #374151;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-dark);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-03__card {
  background: var(--bg-card);
  border-radius: 20px;
  border: 1px solid var(--border);
  padding: 28px 32px;
  max-width: 440px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.sr-03__product {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border);
}

.sr-03__thumb {
  width: 72px;
  height: 72px;
  border-radius: 14px;
  background: linear-gradient(135deg, #064e3b, #10b981);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 36px;
  flex-shrink: 0;
}

.sr-03__info {
  flex: 1;
}

.sr-03__pname {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-03__psub {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 10px;
}

.sr-03__price {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--mint-light);
}

.sr-03__label {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 12px;
}
/* Half-star implementation using radio pairs per position */

.sr-03__stars {
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-end;
  align-items: center;
  margin-bottom: 8px;
  /* Each full-star position = 2 labels (right half + left half) */
}

.sr-03__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
/* Full-star label: 44px wide */

.sr-03__stars label.sr-03__full {
  width: 44px;
  height: 44px;
  position: relative;
  cursor: pointer;
  font-size: 0;
}
/* Half-star label: 22px wide, overflows onto left half of the star */

.sr-03__stars label.sr-03__half {
  width: 22px;
  height: 44px;
  position: relative;
  cursor: pointer;
  font-size: 0;
  margin-right: -22px;
  /* overlap right half */
  z-index: 1;
}
/* Star shape as base layer */

.sr-03__stars label.sr-03__full::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 44px;
  height: 44px;
  background: #374151;
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.15s;
}
/* Left half fill overlay. Single clip-path traces the LEFT HALF
   OF THE STAR SHAPE — from the top tip, down the vertical
   centerline to the bottom inner notch, around the bottom-left
   arm, out to the outer-left tip, and back up to the top.
   The original CSS declared clip-path twice in this rule (once
   as the full star, then overridden by a left-half rectangle),
   so the cascade resolved to a rectangle and the demo rendered
   a green column instead of half a star on hover. */

.sr-03__stars label.sr-03__half::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 44px;
  height: 44px;
  background: var(--mint);
  clip-path: polygon(50% 0%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  opacity: 0;
  filter: drop-shadow(0 0 6px var(--mint-glow));
  transition: opacity 0.15s;
}
/* Hover states */

.sr-03__stars label.sr-03__full:hover::before,
.sr-03__stars label.sr-03__full:hover ~ label.sr-03__full::before {
  background: var(--mint);
  filter: drop-shadow(0 0 8px var(--mint-glow));
}

.sr-03__stars label.sr-03__half:hover::before {
  opacity: 1;
}
/* Hovering a half-star also fills every full star that follows
   it in DOM order with mint. Mirrors the :checked rule below,
   keeps the hover preview visually consistent with what selection
   will produce. */

.sr-03__stars label.sr-03__half:hover ~ label.sr-03__full::before {
  background: var(--mint);
  filter: drop-shadow(0 0 8px var(--mint-glow));
}
/* Checked states for full stars */

.sr-03__stars input.sr-03__full-in:checked ~ label.sr-03__full::before {
  background: var(--mint);
}
/* Half star checked: reveal the half-overlay on the picked star
   AND fill every full star that follows it in DOM order. Because
   .sr-03__stars uses flex-direction: row-reverse, "follows in DOM"
   maps visually to "to the LEFT of" — i.e. the lower-value stars.
   So checking 3.5 fills full stars 1 + 2 with mint and reveals the
   half-overlay on star 3. */

.sr-03__stars input.sr-03__half-in:checked + label.sr-03__half::before {
  opacity: 1;
}

.sr-03__stars input.sr-03__half-in:checked ~ label.sr-03__full::before {
  background: var(--mint);
}

.sr-03__tally {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 16px;
}

.sr-03__score {
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--mint-light);
  line-height: 1;
}

.sr-03__breakdown {
  flex: 1;
}

.sr-03__bar-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.sr-03__bar-label {
  font-size: 0.72rem;
  color: var(--text-muted);
  width: 8px;
}

.sr-03__bar-track {
  flex: 1;
  height: 5px;
  background: var(--bg-hover);
  border-radius: 3px;
  overflow: hidden;
}

.sr-03__bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--mint), var(--mint-light));
  border-radius: 3px;
  transition: width 0.3s ease;
}

.sr-03__bar-pct {
  font-size: 0.7rem;
  color: var(--text-muted);
  width: 28px;
  text-align: right;
}

.sr-03__count {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .sr-03__stars label.sr-03__full::before,
    .sr-03__stars label.sr-03__half::before,
    .sr-03__bar-fill {
    transition: none;
  }
}
```
