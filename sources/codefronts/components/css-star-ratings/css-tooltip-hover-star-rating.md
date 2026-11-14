---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/css-tooltip-hover-star-rating/"
title: "CSS Tooltip Hover Star Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A light-mode marketplace review card where hovering each star reveals a floating CSS pseudo-element tooltip (Poor / Fair / Good / Very Good / Excellent) via…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Tooltip Hover Star Rating
Source: https://codefronts.com/components/css-star-ratings/css-tooltip-hover-star-rating/

A light-mode marketplace review card where hovering each star reveals a floating CSS pseudo-element tooltip (Poor / Fair / Good / Very Good / Excellent) via fade-and-slide — no JavaScript.
## HTML
```html
<div class="sr-14">
  <div class="sr-14__card">
    <div class="sr-14__store-header">
      <div class="sr-14__store-logo">🛒</div>
      <div class="sr-14__store-info">
        <div class="sr-14__store-name">NexShop Marketplace</div>
        <div class="sr-14__store-sub">Order #NX-4892 · Delivered Dec 14</div>
      </div>
      <span class="sr-14__store-verified">✓ Verified</span>
    </div>

    <div class="sr-14__question">How was your overall experience?</div>
    <div class="sr-14__sub">Hover each star to see its label — click to select</div>

    <div class="sr-14__stars-wrap">
      <form>
        <div class="sr-14__stars">
          <input type="radio" id="sr-14-t5" name="sr-14-tip" value="5">
          <label for="sr-14-t5" data-tip="Excellent">5</label>

          <input type="radio" id="sr-14-t4" name="sr-14-tip" value="4">
          <label for="sr-14-t4" data-tip="Very Good">4</label>

          <input type="radio" id="sr-14-t3" name="sr-14-tip" value="3">
          <label for="sr-14-t3" data-tip="Good">3</label>

          <input type="radio" id="sr-14-t2" name="sr-14-tip" value="2">
          <label for="sr-14-t2" data-tip="Fair">2</label>

          <input type="radio" id="sr-14-t1" name="sr-14-tip" value="1">
          <label for="sr-14-t1" data-tip="Poor">1</label>
        </div>
      </form>
    </div>

    <div class="sr-14__aspects">
      <div class="sr-14__aspect-row">
        <span class="sr-14__aspect-label">Delivery</span>
        <div class="sr-14__aspect-track"><div class="sr-14__aspect-fill" style="width:92%"></div></div>
        <span class="sr-14__aspect-score">4.6</span>
      </div>
      <div class="sr-14__aspect-row">
        <span class="sr-14__aspect-label">Packaging</span>
        <div class="sr-14__aspect-track"><div class="sr-14__aspect-fill" style="width:84%"></div></div>
        <span class="sr-14__aspect-score">4.2</span>
      </div>
      <div class="sr-14__aspect-row">
        <span class="sr-14__aspect-label">Value</span>
        <div class="sr-14__aspect-track"><div class="sr-14__aspect-fill" style="width:76%"></div></div>
        <span class="sr-14__aspect-score">3.8</span>
      </div>
    </div>

    <div class="sr-14__footer">
      <button class="sr-14__btn sr-14__btn--primary">Submit Review</button>
      <button class="sr-14__btn sr-14__btn--ghost">Skip</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-14,
.sr-14 *,
.sr-14 *::before,
.sr-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-14 ::selection {
  background: #0284c7;
  color: #fff;
}

.sr-14 {
  --sky-blue: #0284c7;
  --sky-blue-light: #38bdf8;
  --sky-glow: rgba(2,132,199,0.35);
  --tooltip-bg: #1e293b;
  --tooltip-text: #f1f5f9;
  --bg-page: #f0f9ff;
  --bg-card: #fff;
  --text: #0f172a;
  --text-muted: #64748b;
  --border: #e0f2fe;
  --star-empty: #cbd5e1;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-page);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 16px 32px;
  /* extra top for tooltip space */
}

.sr-14__card {
  background: var(--bg-card);
  border-radius: 20px;
  border: 1px solid var(--border);
  padding: 36px 40px 32px;
  max-width: 460px;
  width: 100%;
  box-shadow: 0 4px 32px rgba(2,132,199,0.08);
}

.sr-14__store-header {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border);
}

.sr-14__store-logo {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: linear-gradient(135deg, #075985, #0284c7);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(2,132,199,0.3);
}

.sr-14__store-info {
  flex: 1;
}

.sr-14__store-name {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--text);
}

.sr-14__store-sub {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 2px;
}

.sr-14__store-verified {
  font-size: 0.72rem;
  background: #e0f2fe;
  color: var(--sky-blue);
  border-radius: 20px;
  padding: 3px 10px;
  font-weight: 600;
}

.sr-14__question {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.sr-14__sub {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 32px;
}
/* The tooltip star rating container */

.sr-14__stars-wrap {
  display: flex;
  justify-content: center;
  margin-bottom: 28px;
  padding-top: 48px;
  /* room for tooltip above */
}

.sr-14__stars {
  display: flex;
  flex-direction: row-reverse;
  gap: 8px;
}

.sr-14__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-14__stars label {
  position: relative;
  display: block;
  width: 48px;
  height: 48px;
  cursor: pointer;
  /* Hide the digit text content — star shape is drawn via ::after. */
  font-size: 0;
}
/* Star shape */

.sr-14__stars label::after {
  content: '';
  display: block;
  width: 48px;
  height: 48px;
  background: var(--star-empty);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.2s ease, filter 0.2s ease, transform 0.2s cubic-bezier(.34,1.56,.64,1);
}
/* Tooltip pseudo-element on the label */

.sr-14__stars label::before {
  position: absolute;
  bottom: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%) translateY(6px);
  background: var(--tooltip-bg);
  color: var(--tooltip-text);
  font-size: 0.72rem;
  font-weight: 700;
  white-space: nowrap;
  padding: 5px 10px;
  border-radius: 7px;
  letter-spacing: 0.3px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
  z-index: 10;
}
/* Tooltip arrow */

.sr-14__stars label::before {
  box-shadow: 0 4px 16px rgba(0,0,0,0.2);
}
/* Each label's tooltip content */

.sr-14__stars label[data-tip="Poor"]::before {
  content: '★ Poor';
}

.sr-14__stars label[data-tip="Fair"]::before {
  content: '★★ Fair';
}

.sr-14__stars label[data-tip="Good"]::before {
  content: '★★★ Good';
}

.sr-14__stars label[data-tip="Very Good"]::before {
  content: '★★★★ Very Good';
}

.sr-14__stars label[data-tip="Excellent"]::before {
  content: '★★★★★ Excellent!';
}
/* Show tooltip on hover */

.sr-14__stars label:hover::before {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
/* Hover cascade star fill */

.sr-14__stars label:hover::after,
.sr-14__stars label:hover ~ label::after {
  background: var(--sky-blue-light);
  filter: drop-shadow(0 0 8px var(--sky-glow));
  transform: scale(1.1);
}
/* Checked cascade fill */

.sr-14__stars input:checked ~ label::after {
  background: var(--sky-blue);
  filter: drop-shadow(0 0 8px var(--sky-glow));
}

.sr-14__stars input:checked + label::after {
  transform: scale(1.12);
  filter: drop-shadow(0 0 12px var(--sky-glow));
}
/* Show tooltip on checked too */

.sr-14__stars input:checked + label::before {
  opacity: 0;
  /* hidden when selected — shown only on hover */
}
/* Aspect strip */

.sr-14__aspects {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}

.sr-14__aspect-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.sr-14__aspect-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  width: 88px;
  flex-shrink: 0;
}

.sr-14__aspect-track {
  flex: 1;
  height: 6px;
  background: var(--border);
  border-radius: 3px;
  overflow: hidden;
}

.sr-14__aspect-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--sky-blue), var(--sky-blue-light));
  border-radius: 3px;
}

.sr-14__aspect-score {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--sky-blue);
  width: 24px;
  text-align: right;
}

.sr-14__footer {
  display: flex;
  gap: 10px;
}

.sr-14__btn {
  flex: 1;
  padding: 12px;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: transform 0.15s, box-shadow 0.15s;
}

.sr-14__btn--primary {
  background: var(--sky-blue);
  color: #fff;
  box-shadow: 0 4px 16px var(--sky-glow);
}

.sr-14__btn--primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--sky-glow);
}

.sr-14__btn--ghost {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--border);
}

.sr-14__btn--ghost:hover {
  background: var(--bg-page);
}

@media (prefers-reduced-motion: reduce) {
  .sr-14__stars label::before,
    .sr-14__stars label::after,
    .sr-14__btn {
    transition: none;
  }
}
```
