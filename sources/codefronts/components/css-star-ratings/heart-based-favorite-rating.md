---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/heart-based-favorite-rating/"
title: "Heart-Based Favorite Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A ruby-red movie-rating card where hearts replace stars — featuring a CSS heartbeat spring-scale animation on the clicked heart, a fluid fill cascade, and…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Heart-Based Favorite Rating
Source: https://codefronts.com/components/css-star-ratings/heart-based-favorite-rating/

A ruby-red movie-rating card where hearts replace stars — featuring a CSS heartbeat spring-scale animation on the clicked heart, a fluid fill cascade, and :has()-driven sentiment text.
## HTML
```html
<div class="sr-13">
  <div class="sr-13__card">
    <div class="sr-13__banner">
      <div class="sr-13__movie-poster">🎬</div>
      <div class="sr-13__movie-title">Eternal Embers</div>
      <div class="sr-13__movie-meta">2024 · Drama · 128 min · ★ 8.2 IMDb</div>
    </div>

    <div class="sr-13__body">
      <div class="sr-13__prompt">How much did you love it?</div>

      <form class="sr-13__hearts-form">
        <div class="sr-13__hearts">
          <input type="radio" id="sr-13-h5" name="sr-13-heart" value="5">
          <label for="sr-13-h5">5</label>
          <input type="radio" id="sr-13-h4" name="sr-13-heart" value="4">
          <label for="sr-13-h4">4</label>
          <input type="radio" id="sr-13-h3" name="sr-13-heart" value="3">
          <label for="sr-13-h3">3</label>
          <input type="radio" id="sr-13-h2" name="sr-13-heart" value="2">
          <label for="sr-13-h2">2</label>
          <input type="radio" id="sr-13-h1" name="sr-13-heart" value="1">
          <label for="sr-13-h1">1</label>
        </div>
      </form>

      <div class="sr-13__label-row">
        <span class="sr-13__label-item">Hate</span>
        <span class="sr-13__label-item">Dislike</span>
        <span class="sr-13__label-item">Okay</span>
        <span class="sr-13__label-item">Like</span>
        <span class="sr-13__label-item">Love!</span>
      </div>

      <div class="sr-13__status"></div>

      <button class="sr-13__save">❤️ Save to Favourites</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-13,
.sr-13 *,
.sr-13 *::before,
.sr-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-13 ::selection {
  background: #e11d48;
  color: #fff;
}

.sr-13 {
  --rose: #e11d48;
  --rose-light: #fb7185;
  --rose-glow: rgba(225,29,72,0.4);
  --rose-pale: #fff1f2;
  --bg: #fff;
  --bg-soft: #fafafa;
  --text: #1c1917;
  --text-muted: #78716c;
  --border: #e7e5e4;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-soft);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-13__card {
  background: var(--bg);
  border-radius: 24px;
  border: 1px solid var(--border);
  max-width: 440px;
  width: 100%;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(225,29,72,0.08), 0 2px 8px rgba(0,0,0,0.04);
}

.sr-13__banner {
  background: linear-gradient(135deg, #fff1f2, #fce7f3);
  padding: 28px 28px 24px;
  text-align: center;
  border-bottom: 1px solid #fce7f3;
}

.sr-13__movie-poster {
  width: 80px;
  height: 80px;
  border-radius: 18px;
  background: linear-gradient(135deg, #881337, #e11d48);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40px;
  margin: 0 auto 14px;
  box-shadow: 0 8px 24px rgba(225,29,72,0.3);
}

.sr-13__movie-title {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-13__movie-meta {
  font-size: 0.78rem;
  color: var(--text-muted);
}
/* Heart rating area */

.sr-13__body {
  padding: 28px;
}

.sr-13__prompt {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 20px;
  text-align: center;
}

.sr-13__hearts {
  display: flex;
  flex-direction: row-reverse;
  justify-content: center;
  gap: 10px;
  margin-bottom: 24px;
}

.sr-13__hearts input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-13__hearts label {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  cursor: pointer;
  /* Hide the digit text content — heart shape is drawn via SVG inside the label. */
  font-size: 0;
}
/* Heart shape via SVG path in CSS */

.sr-13__hearts label::before {
  content: '';
  display: block;
  width: 40px;
  height: 40px;
  background: #f5f5f4;
  /* Heart clip-path */
  clip-path: path('M20 34.4C20 34.4 4 24.2 4 13.4C4 8.4 8 4.4 13 4.4C16 4.4 18.6 5.8 20 8C21.4 5.8 24 4.4 27 4.4C32 4.4 36 8.4 36 13.4C36 24.2 20 34.4 20 34.4Z');
  transition: background 0.2s ease, transform 0.25s cubic-bezier(.34,1.56,.64,1), filter 0.25s ease;
}
/* Hover cascade fill */

.sr-13__hearts label:hover::before,
.sr-13__hearts label:hover ~ label::before {
  background: var(--rose-light);
  filter: drop-shadow(0 0 8px rgba(251,113,133,0.5));
}
/* Checked cascade fill */

.sr-13__hearts input:checked ~ label::before {
  background: var(--rose);
  filter: drop-shadow(0 0 8px var(--rose-glow));
}
/* The directly-checked heart gets the pulse */

.sr-13__hearts input:checked + label::before {
  background: var(--rose);
  filter: drop-shadow(0 0 14px var(--rose-glow));
  animation: sr-13-heartbeat 0.6s ease-out forwards;
}

.sr-13__hearts label:hover {
}

.sr-13__hearts label:hover::before {
  transform: scale(1.15);
}

@keyframes sr-13-heartbeat {
  0% {
    transform: scale(1);
  }

  30% {
    transform: scale(1.35);
    filter: drop-shadow(0 0 18px rgba(225,29,72,0.7));
  }

  60% {
    transform: scale(0.95);
  }

  80% {
    transform: scale(1.12);
  }

  100% {
    transform: scale(1.1);
  }
}
/* Selection label text — mirrors the .sr-13__hearts layout
   exactly (justify-content: center; gap: 10px) so each label sits
   directly under its heart. Without matching geometry, the
   hearts cluster centered ~300px wide while the labels stretch
   to the parent's full width via space-between, misaligning. */

.sr-13__label-row {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.sr-13__label-item {
  text-align: center;
  font-size: 0.65rem;
  color: var(--text-muted);
  width: 52px;
}
/* Status message */

.sr-13__status {
  text-align: center;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text-muted);
  min-height: 24px;
  margin-bottom: 20px;
  transition: color 0.2s;
}

.sr-13__hearts-form:has(#sr-13-h1:checked) ~ .sr-13__status {
  color: var(--rose);
}

.sr-13__hearts-form:has(#sr-13-h1:checked) ~ .sr-13__status::after {
  content: 'Not for me 💔';
}

.sr-13__hearts-form:has(#sr-13-h2:checked) ~ .sr-13__status {
  color: var(--rose-light);
}

.sr-13__hearts-form:has(#sr-13-h2:checked) ~ .sr-13__status::after {
  content: 'It was okay 🤷';
}

.sr-13__hearts-form:has(#sr-13-h3:checked) ~ .sr-13__status {
  color: #f97316;
}

.sr-13__hearts-form:has(#sr-13-h3:checked) ~ .sr-13__status::after {
  content: 'Pretty good 👍';
}

.sr-13__hearts-form:has(#sr-13-h4:checked) ~ .sr-13__status {
  color: #22c55e;
}

.sr-13__hearts-form:has(#sr-13-h4:checked) ~ .sr-13__status::after {
  content: 'Really loved it ❤️';
}

.sr-13__hearts-form:has(#sr-13-h5:checked) ~ .sr-13__status {
  color: var(--rose);
}

.sr-13__hearts-form:has(#sr-13-h5:checked) ~ .sr-13__status::after {
  content: 'Absolute favourite 💖';
}
/* The form must precede these */

.sr-13__inner {
  position: relative;
}
/* Save button */

.sr-13__save {
  width: 100%;
  padding: 13px;
  border: none;
  border-radius: 14px;
  background: linear-gradient(135deg, var(--rose), #f43f5e);
  color: #fff;
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
  box-shadow: 0 6px 20px rgba(225,29,72,0.3);
}

.sr-13__save:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(225,29,72,0.4);
}

@media (prefers-reduced-motion: reduce) {
  .sr-13__hearts label::before {
    transition: background 0.1s;
    animation: none !important;
  }
}
```
