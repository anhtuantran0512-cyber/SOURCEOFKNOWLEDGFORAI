---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/gradient-filled-star-rating/"
title: "Gradient Filled Star Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A luxury dark-mode agency feedback card where stars are filled with a vivid violet-to-fuchsia-to-orange diagonal gradient via CSS clip-path masking, with a…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Filled Star Rating
Source: https://codefronts.com/components/css-star-ratings/gradient-filled-star-rating/

A luxury dark-mode agency feedback card where stars are filled with a vivid violet-to-fuchsia-to-orange diagonal gradient via CSS clip-path masking, with a shimmer-animated gradient bar.
## HTML
```html
<div class="sr-11">
  <div class="sr-11__card">
    <div class="sr-11__logo-wrap">
      <div class="sr-11__logo-icon">✦</div>
      <span class="sr-11__logo-text">Prism Studio</span>
    </div>
    <div class="sr-11__heading">Project Feedback</div>
    <div class="sr-11__sub">Rate the quality of our delivered work</div>

    <form>
      <div class="sr-11__stars">
        <input type="radio" id="sr-11-g5" name="sr-11-g" value="5">
        <label for="sr-11-g5">5</label>
        <input type="radio" id="sr-11-g4" name="sr-11-g" value="4">
        <label for="sr-11-g4">4</label>
        <input type="radio" id="sr-11-g3" name="sr-11-g" value="3">
        <label for="sr-11-g3">3</label>
        <input type="radio" id="sr-11-g2" name="sr-11-g" value="2">
        <label for="sr-11-g2">2</label>
        <input type="radio" id="sr-11-g1" name="sr-11-g" value="1">
        <label for="sr-11-g1">1</label>
      </div>
    </form>

    <div class="sr-11__score-display">
      <div class="sr-11__big-num">4.9</div>
      <div class="sr-11__score-meta">
        <div class="sr-11__score-label">Overall Rating</div>
        <div class="sr-11__score-sub">Based on 876 client reviews</div>
      </div>
    </div>

    <div class="sr-11__gradient-bar"></div>

    <div class="sr-11__submit-wrap">
      <button class="sr-11__submit">Submit Feedback</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-11,
.sr-11 *,
.sr-11 *::before,
.sr-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-11 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.sr-11 {
  --grad-start: #7c3aed;
  --grad-mid: #c026d3;
  --grad-end: #f97316;
  --bg-dark: #09090b;
  --bg-card: #111113;
  --border: #27272a;
  --text: #fafafa;
  --text-muted: #71717a;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-dark);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-11__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 40px 44px 36px;
  max-width: 440px;
  width: 100%;
  text-align: center;
  position: relative;
  overflow: hidden;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7);
}
/* Ambient glow behind card */

.sr-11__card::before {
  content: '';
  position: absolute;
  top: -60px;
  left: 50%;
  width: 300px;
  height: 200px;
  background: radial-gradient(ellipse, rgba(124,58,237,0.15), transparent 70%);
  transform: translateX(-50%);
  pointer-events: none;
}

.sr-11__logo-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 24px;
}

.sr-11__logo-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--grad-start), var(--grad-end));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

.sr-11__logo-text {
  font-size: 1.05rem;
  font-weight: 800;
  background: linear-gradient(90deg, var(--grad-start), var(--grad-mid), var(--grad-end));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sr-11__heading {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.sr-11__sub {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 32px;
}
/* Gradient star rating */

.sr-11__stars {
  display: flex;
  flex-direction: row-reverse;
  justify-content: center;
  gap: 8px;
  margin-bottom: 24px;
}

.sr-11__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
/* Each star uses a pseudo-element star with a gradient fill */

.sr-11__stars label {
  display: block;
  width: 52px;
  height: 52px;
  cursor: pointer;
  position: relative;
  transition: transform 0.25s cubic-bezier(.34,1.56,.64,1);
  /* Hide the digit text content — star shape is drawn via ::before. */
  font-size: 0;
}

.sr-11__stars label::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 52px;
  height: 52px;
  /* Gradient fill via mask + background */
  background: linear-gradient(135deg, var(--grad-start), var(--grad-mid), var(--grad-end));
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  opacity: 0.18;
  transition: opacity 0.25s ease, filter 0.25s ease;
}
/* Hover cascade */

.sr-11__stars label:hover::before,
.sr-11__stars label:hover ~ label::before {
  opacity: 0.7;
  filter: drop-shadow(0 0 10px rgba(192,38,211,0.5));
}
/* Checked cascade */

.sr-11__stars input:checked ~ label::before {
  opacity: 1;
  filter: drop-shadow(0 0 12px rgba(192,38,211,0.45));
}

.sr-11__stars input:checked + label::before {
  filter: drop-shadow(0 0 18px rgba(192,38,211,0.6));
}

.sr-11__stars label:hover {
  transform: scale(1.15);
}

.sr-11__stars input:checked + label {
  transform: scale(1.12);
}
/* Gradient score badge */

.sr-11__score-display {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin-bottom: 28px;
}

.sr-11__big-num {
  font-size: 3.5rem;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(135deg, var(--grad-start), var(--grad-mid), var(--grad-end));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sr-11__score-meta {
  text-align: left;
}

.sr-11__score-label {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-11__score-sub {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.sr-11__gradient-bar {
  height: 6px;
  background: linear-gradient(90deg, var(--grad-start), var(--grad-mid), var(--grad-end));
  border-radius: 3px;
  margin-bottom: 28px;
  position: relative;
  overflow: hidden;
}

.sr-11__gradient-bar::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
  animation: sr-11-shimmer 2s infinite;
}

@keyframes sr-11-shimmer {
  100% {
    left: 200%;
  }
}

.sr-11__submit-wrap {
}

.sr-11__submit {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 14px;
  background: linear-gradient(135deg, var(--grad-start), var(--grad-mid), var(--grad-end));
  color: #fff;
  font-weight: 700;
  font-size: 0.92rem;
  cursor: pointer;
  letter-spacing: 0.4px;
  transition: opacity 0.2s, transform 0.15s;
  box-shadow: 0 8px 24px rgba(124,58,237,0.35);
}

.sr-11__submit:hover {
  opacity: 0.9;
  transform: translateY(-2px);
}

@media (prefers-reduced-motion: reduce) {
  .sr-11__gradient-bar::after {
    animation: none;
  }

  .sr-11__stars label,
    .sr-11__stars label::before {
    transition: none;
  }
}
```
