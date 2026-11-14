---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/css-star-rating-for-read-only-reviews/"
title: "CSS Star Rating for Read-Only Reviews"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A crimson-red editorial product review card with fractional star fills via a CSS custom property width on an absolutely-positioned fill layer — fully…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Star Rating for Read-Only Reviews
Source: https://codefronts.com/components/css-star-ratings/css-star-rating-for-read-only-reviews/

A crimson-red editorial product review card with fractional star fills via a CSS custom property width on an absolutely-positioned fill layer — fully display-only with no interaction.
## HTML
```html
<div class="sr-06">
  <div class="sr-06__card">
    <div class="sr-06__hero">
      <div class="sr-06__product-img">🎧</div>
      <div class="sr-06__hero-text">
        <div class="sr-06__pname">SoundCraft Pro X1</div>
        <div class="sr-06__pcategory">Wireless Noise Cancelling · 40hr Battery</div>
      </div>
      <div class="sr-06__hero-score">
        <div class="sr-06__big-score">4.6</div>
        <div class="sr-06__max">out of 5</div>
      </div>
    </div>

    <div class="sr-06__body">
      <!-- Fractional read-only strip (4.6 = 4 full + 60% partial) -->
      <div class="sr-06__rating-row">
        <div class="sr-06__stars-ro">
          <div class="sr-06__stars-ro__bg">
            <div class="sr-06__star-ro"><div class="sr-06__fill" style="--fill:100%"></div></div>
            <div class="sr-06__star-ro"><div class="sr-06__fill" style="--fill:100%"></div></div>
            <div class="sr-06__star-ro"><div class="sr-06__fill" style="--fill:100%"></div></div>
            <div class="sr-06__star-ro"><div class="sr-06__fill" style="--fill:100%"></div></div>
            <div class="sr-06__star-ro"><div class="sr-06__fill" style="--fill:60%"></div></div>
          </div>
        </div>
        <div class="sr-06__rating-text"><strong>4.6</strong> / 5 · 3,214 reviews</div>
      </div>

      <div class="sr-06__reviews">
        <div class="sr-06__review">
          <div class="sr-06__review-header">
            <div class="sr-06__reviewer-av" style="background:#fee2e2;color:#b91c1c">JL</div>
            <div>
              <div class="sr-06__reviewer-name">Jamie L.</div>
              <div class="sr-06__review-date">December 2024</div>
            </div>
          </div>
          <div class="sr-06__mini-stars">
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star filled"></div>
          </div>
          <div class="sr-06__review-text">Absolutely incredible sound quality. The ANC is the best I've tested at this price point. Build feels premium too.</div>
          <span class="sr-06__verified">✓ Verified Purchase</span>
        </div>

        <div class="sr-06__review">
          <div class="sr-06__review-header">
            <div class="sr-06__reviewer-av" style="background:#fce7f3;color:#be185d">MR</div>
            <div>
              <div class="sr-06__reviewer-name">Morgan R.</div>
              <div class="sr-06__review-date">November 2024</div>
            </div>
          </div>
          <div class="sr-06__mini-stars">
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star filled"></div>
            <div class="sr-06__mini-star half"></div>
          </div>
          <div class="sr-06__review-text">Battery life is exceptional. Slight discomfort after 4+ hours but overall a fantastic daily driver.</div>
          <span class="sr-06__verified">✓ Verified Purchase</span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-06,
.sr-06 *,
.sr-06 *::before,
.sr-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-06 ::selection {
  background: #b91c1c;
  color: #fff;
}

.sr-06 {
  --crimson: #dc2626;
  --crimson-light: #ef4444;
  --crimson-pale: #fee2e2;
  --bg: #fff;
  --bg-alt: #fafafa;
  --text: #111827;
  --text-muted: #6b7280;
  --border: #e5e7eb;
  --star-empty: #e5e7eb;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-alt);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-06__card {
  background: var(--bg);
  border-radius: 18px;
  border: 1px solid var(--border);
  max-width: 460px;
  width: 100%;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}

.sr-06__hero {
  background: linear-gradient(135deg, #1f1919, #3b0d0d);
  padding: 24px 28px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.sr-06__product-img {
  width: 72px;
  height: 72px;
  border-radius: 14px;
  background: linear-gradient(135deg, #7f1d1d, #dc2626);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 36px;
  flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(220,38,38,0.4);
}

.sr-06__hero-text {
  flex: 1;
}

.sr-06__pname {
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 4px;
}

.sr-06__pcategory {
  font-size: 0.78rem;
  color: rgba(255,255,255,0.5);
}

.sr-06__hero-score {
  text-align: center;
}

.sr-06__big-score {
  font-size: 2.8rem;
  font-weight: 900;
  color: var(--crimson-light);
  line-height: 1;
}

.sr-06__max {
  font-size: 0.78rem;
  color: rgba(255,255,255,0.4);
}

.sr-06__body {
  padding: 24px 28px;
}
/* Read-only fractional star using CSS custom property for fill width */

.sr-06__rating-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}
/* Star strip: 5 stars as a single background clip trick */

.sr-06__stars-ro {
  position: relative;
  display: inline-flex;
  gap: 4px;
  user-select: none;
  pointer-events: none;
}

.sr-06__stars-ro__bg {
  display: flex;
  gap: 4px;
}

.sr-06__star-ro {
  width: 28px;
  height: 28px;
  background: var(--star-empty);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  position: relative;
}
/* Filled overlay with exact percentage via custom property */

.sr-06__star-ro .sr-06__fill {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: var(--fill, 0%);
  background: var(--crimson);
}

.sr-06__rating-text {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-muted);
}

.sr-06__rating-text strong {
  color: var(--crimson);
}
/* Review list */

.sr-06__reviews {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.sr-06__review {
  padding: 16px;
  background: var(--bg-alt);
  border-radius: 12px;
  border: 1px solid var(--border);
}

.sr-06__review-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.sr-06__reviewer-av {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  flex-shrink: 0;
}

.sr-06__reviewer-name {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text);
}

.sr-06__review-date {
  font-size: 0.75rem;
  color: var(--text-muted);
}
/* Mini inline stars per review */

.sr-06__mini-stars {
  display: inline-flex;
  gap: 2px;
  margin-bottom: 8px;
  position: relative;
  pointer-events: none;
}

.sr-06__mini-star {
  width: 14px;
  height: 14px;
  background: var(--star-empty);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
}

.sr-06__mini-star.filled {
  background: var(--crimson);
}

.sr-06__mini-star.half {
  position: relative;
  overflow: hidden;
}

.sr-06__mini-star.half::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 50%;
  height: 100%;
  background: var(--crimson);
}

.sr-06__review-text {
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.55;
}

.sr-06__verified {
  display: inline-block;
  margin-top: 8px;
  font-size: 0.72rem;
  color: #059669;
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  /* No animations in this demo — nothing to disable */
}
```
