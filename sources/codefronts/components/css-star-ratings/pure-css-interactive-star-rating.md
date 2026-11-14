---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/pure-css-interactive-star-rating/"
title: "Pure CSS Interactive Star Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A golden-amber five-star radio-button rating widget built entirely in CSS, wrapped in a realistic product review card with hover cascade and :has()-powered…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Interactive Star Rating
Source: https://codefronts.com/components/css-star-ratings/pure-css-interactive-star-rating/

A golden-amber five-star radio-button rating widget built entirely in CSS, wrapped in a realistic product review card with hover cascade and :has()-powered feedback text.
## HTML
```html
<div class="sr-01">
  <div class="sr-01__card">
    <div class="sr-01__product-icon">☕</div>
    <div class="sr-01__title">Morning Brew Pro</div>
    <div class="sr-01__subtitle">How would you rate your experience?</div>
    <form class="sr-01__form">
      <div class="sr-01__stars">
        <input type="radio" id="sr-01-s5" name="sr-01-rating" value="5">
        <label for="sr-01-s5">5 stars</label>
        <input type="radio" id="sr-01-s4" name="sr-01-rating" value="4">
        <label for="sr-01-s4">4 stars</label>
        <input type="radio" id="sr-01-s3" name="sr-01-rating" value="3">
        <label for="sr-01-s3">3 stars</label>
        <input type="radio" id="sr-01-s2" name="sr-01-rating" value="2">
        <label for="sr-01-s2">2 stars</label>
        <input type="radio" id="sr-01-s1" name="sr-01-rating" value="1">
        <label for="sr-01-s1">1 star</label>
      </div>
      <div class="sr-01__feedback"></div>
      <button type="submit" class="sr-01__submit">Submit Rating</button>
    </form>
  </div>
</div>
```
## CSS
```css
.sr-01,
.sr-01 *,
.sr-01 *::before,
.sr-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-01 ::selection {
  background: #ffb000;
  color: #1a1200;
}

.sr-01 {
  --gold: #ffb000;
  --gold-glow: #ffd54f;
  --gold-dark: #e65100;
  --bg: #ffffff;
  --card-bg: #fff;
  --text-primary: #1a1a2e;
  --text-secondary: #555;
  --border: #e8e8e8;
  --shadow: rgba(255,176,0,0.18);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #f4f6fb;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-01__card {
  background: var(--card-bg);
  border-radius: 20px;
  box-shadow: 0 4px 32px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.04);
  padding: 36px 40px 32px;
  max-width: 400px;
  width: 100%;
  text-align: center;
}

.sr-01__product-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #ff8c00, #ffb000);
  border-radius: 16px;
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
}

.sr-01__title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 4px;
}

.sr-01__subtitle {
  font-size: 0.82rem;
  color: var(--text-secondary);
  margin-bottom: 24px;
}
/* Hide native radio inputs */

.sr-01__form input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
  pointer-events: none;
}
/* Star container — flex reversed so CSS sibling trick works */

.sr-01__stars {
  display: flex;
  flex-direction: row-reverse;
  justify-content: center;
  gap: 6px;
  margin-bottom: 20px;
}
/* Each label holds one star via clip-path polygon */

.sr-01__stars label {
  cursor: pointer;
  font-size: 0;
  width: 44px;
  height: 44px;
  position: relative;
  transition: transform 0.15s cubic-bezier(.34,1.56,.64,1);
}

.sr-01__stars label::before {
  content: '';
  display: block;
  width: 44px;
  height: 44px;
  background: #e8e8e8;
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.18s ease, filter 0.18s ease, transform 0.15s cubic-bezier(.34,1.56,.64,1);
}
/* Hover: fill this star and all stars to the right (higher value = reversed) */

.sr-01__stars label:hover::before,
.sr-01__stars label:hover ~ label::before {
  background: var(--gold-glow);
  filter: drop-shadow(0 0 6px rgba(255,176,0,0.5));
}
/* Checked: fill checked and all stars to the right */

.sr-01__stars input:checked ~ label::before {
  background: var(--gold);
  filter: drop-shadow(0 0 8px var(--shadow));
}
/* Scale the directly-hovered/checked star slightly */

.sr-01__stars label:hover {
  transform: scale(1.2);
}

.sr-01__stars input:checked + label {
  transform: scale(1.15);
}
/* Rating label feedback */

.sr-01__feedback {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-secondary);
  min-height: 22px;
  transition: color 0.2s;
}
/* Show rating text based on selected radio */

.sr-01__form:has(#sr-01-s1:checked) .sr-01__feedback::after {
  content: '★ Poor';
  color: #e53935;
}

.sr-01__form:has(#sr-01-s2:checked) .sr-01__feedback::after {
  content: '★★ Fair';
  color: #ff8c00;
}

.sr-01__form:has(#sr-01-s3:checked) .sr-01__feedback::after {
  content: '★★★ Good';
  color: #ffb000;
}

.sr-01__form:has(#sr-01-s4:checked) .sr-01__feedback::after {
  content: '★★★★ Very Good';
  color: #7cb342;
}

.sr-01__form:has(#sr-01-s5:checked) .sr-01__feedback::after {
  content: '★★★★★ Excellent!';
  color: #2e7d32;
}

.sr-01__submit {
  margin-top: 20px;
  padding: 10px 32px;
  background: linear-gradient(135deg, #ff8c00, #ffb000);
  border: none;
  border-radius: 50px;
  color: #1a1200;
  font-weight: 700;
  font-size: 0.88rem;
  cursor: pointer;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 16px rgba(255,176,0,0.3);
  transition: transform 0.15s, box-shadow 0.15s;
}

.sr-01__submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255,176,0,0.4);
}

@media (prefers-reduced-motion: reduce) {
  .sr-01__stars label,
    .sr-01__stars label::before,
    .sr-01__submit {
    transition: none;
  }
}
```
