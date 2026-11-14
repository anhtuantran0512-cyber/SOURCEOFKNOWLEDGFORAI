---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/single-star-numerical-rating/"
title: "Single Star Numerical Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A compact dark app-store card with one large pulsing hero star and a smooth JS-animated number ticker that slides to the selected value when a radio button…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Single Star Numerical Rating
Source: https://codefronts.com/components/css-star-ratings/single-star-numerical-rating/

A compact dark app-store card with one large pulsing hero star and a smooth JS-animated number ticker that slides to the selected value when a radio button is chosen.
## HTML
```html
<div class="sr-12">
  <div class="sr-12__card">
    <div class="sr-12__context">
      <div class="sr-12__app-icon">🚀</div>
      <div class="sr-12__app-meta">
        <div class="sr-12__app-name">LaunchKit Pro</div>
        <div class="sr-12__app-cat">Productivity · Developer Tools</div>
        <div class="sr-12__app-tags">
          <span class="sr-12__tag">Free</span>
          <span class="sr-12__tag">4.8MB</span>
          <span class="sr-12__tag">v2.1.0</span>
        </div>
      </div>
    </div>

    <div class="sr-12__hero-rating">
      <div class="sr-12__single-star">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 2l2.9 6.1L22 9.3l-5 4.9 1.2 6.8L12 17.8l-6.2 3.2L7 14.2 2 9.3l7.1-1.2z"/>
        </svg>
      </div>
      <div class="sr-12__num-display">
        <div class="sr-12__ticker-wrap">
          <span class="sr-12__ticker-num" id="sr-12-ticker">4.8</span>
        </div>
        <div class="sr-12__num-label">out of <strong>5.0</strong> · 12,483 ratings</div>
      </div>
    </div>

    <div class="sr-12__radios">
      <input type="radio" id="sr-12-v1" name="sr-12-vote" value="1.0">
      <label for="sr-12-v1" class="sr-12__radio-btn">1.0</label>

      <input type="radio" id="sr-12-v2" name="sr-12-vote" value="2.0">
      <label for="sr-12-v2" class="sr-12__radio-btn">2.0</label>

      <input type="radio" id="sr-12-v3" name="sr-12-vote" value="3.0">
      <label for="sr-12-v3" class="sr-12__radio-btn">3.0</label>

      <input type="radio" id="sr-12-v4" name="sr-12-vote" value="4.0">
      <label for="sr-12-v4" class="sr-12__radio-btn">4.0</label>

      <input type="radio" id="sr-12-v5" name="sr-12-vote" value="5.0">
      <label for="sr-12-v5" class="sr-12__radio-btn">5.0</label>
    </div>

    <div class="sr-12__vote-counts">
      <div class="sr-12__vote-item"><div class="sr-12__vote-num">3.1k</div><div class="sr-12__vote-label">5-star</div></div>
      <div class="sr-12__vote-item"><div class="sr-12__vote-num">6.4k</div><div class="sr-12__vote-label">4-star</div></div>
      <div class="sr-12__vote-item"><div class="sr-12__vote-num">2.1k</div><div class="sr-12__vote-label">3-star</div></div>
      <div class="sr-12__vote-item"><div class="sr-12__vote-num">612</div><div class="sr-12__vote-label">2-star</div></div>
      <div class="sr-12__vote-item"><div class="sr-12__vote-num">213</div><div class="sr-12__vote-label">1-star</div></div>
    </div>

    <div class="sr-12__cta">
      <button class="sr-12__btn sr-12__btn--rate" onclick="submitRating()">Rate App</button>
      <button class="sr-12__btn sr-12__btn--later">Not Now</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-12,
.sr-12 *,
.sr-12 *::before,
.sr-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-12 ::selection {
  background: #f59e0b;
  color: #000;
}

.sr-12 {
  --amber: #f59e0b;
  --amber-bright: #fbbf24;
  --amber-glow: rgba(245,158,11,0.4);
  --bg-dark: #0a0a0a;
  --bg-card: #141414;
  --border: #2a2a2a;
  --text: #fff;
  --text-muted: #6b7280;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-dark);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-12__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 36px 40px;
  max-width: 460px;
  width: 100%;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7);
}

.sr-12__context {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  margin-bottom: 28px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--border);
}

.sr-12__app-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  flex-shrink: 0;
}

.sr-12__app-meta {
  flex: 1;
}

.sr-12__app-name {
  font-size: 1rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-12__app-cat {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-bottom: 8px;
}

.sr-12__app-tags {
  display: flex;
  gap: 6px;
}

.sr-12__tag {
  font-size: 0.68rem;
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 2px 9px;
  color: var(--text-muted);
}
/* The hero rating display */

.sr-12__hero-rating {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 28px;
}
/* Single large star */

.sr-12__single-star {
  width: 88px;
  height: 88px;
  flex-shrink: 0;
  position: relative;
}

.sr-12__single-star svg {
  width: 88px;
  height: 88px;
  filter: drop-shadow(0 0 20px var(--amber-glow));
  animation: sr-12-pulse 3s ease-in-out infinite;
}

.sr-12__single-star svg path {
  fill: var(--amber);
}

@keyframes sr-12-pulse {
  0%,
    100% {
    filter: drop-shadow(0 0 14px var(--amber-glow));
  }

  50% {
    filter: drop-shadow(0 0 28px rgba(245,158,11,0.6));
  }
}
/* Numeric ticker */

.sr-12__num-display {
  flex: 1;
}

.sr-12__ticker-wrap {
  overflow: hidden;
  height: 72px;
  position: relative;
}
/* The ticker: slides vertically. JS toggles active class to trigger animation */

.sr-12__ticker-num {
  font-size: 4.5rem;
  font-weight: 900;
  line-height: 72px;
  color: var(--text);
  display: block;
  transition: transform 0.45s cubic-bezier(.34,1.2,.64,1);
}

.sr-12__num-label {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 4px;
}

.sr-12__num-label strong {
  color: var(--amber);
}
/* Compact radio row */

.sr-12__radios {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
  margin-bottom: 24px;
}

.sr-12__radios input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-12__radio-btn {
  display: block;
  text-align: center;
  padding: 10px 4px;
  border-radius: 10px;
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border);
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text-muted);
  cursor: pointer;
  transition: background 0.2s, border-color 0.2s, color 0.2s, transform 0.2s;
}

.sr-12__radios input:checked + .sr-12__radio-btn {
  background: rgba(245,158,11,0.15);
  border-color: var(--amber);
  color: var(--amber-bright);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(245,158,11,0.2);
}

.sr-12__radio-btn:hover {
  background: rgba(255,255,255,0.08);
  color: var(--text);
}

.sr-12__vote-counts {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.sr-12__vote-item {
  text-align: center;
}

.sr-12__vote-num {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-muted);
}

.sr-12__vote-label {
  font-size: 0.65rem;
  color: var(--text-muted);
  opacity: 0.6;
  margin-top: 2px;
}

.sr-12__cta {
  display: flex;
  gap: 10px;
}

.sr-12__btn {
  flex: 1;
  padding: 12px;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: transform 0.15s, opacity 0.15s;
}

.sr-12__btn--rate {
  background: var(--amber);
  color: #1a0a00;
  box-shadow: 0 6px 20px rgba(245,158,11,0.3);
}

.sr-12__btn--rate:hover {
  transform: translateY(-2px);
  opacity: 0.9;
}

.sr-12__btn--later {
  background: rgba(255,255,255,0.06);
  color: var(--text-muted);
  border: 1px solid var(--border);
}

.sr-12__btn--later:hover {
  background: rgba(255,255,255,0.1);
}

@media (prefers-reduced-motion: reduce) {
  .sr-12__single-star svg {
    animation: none;
  }

  .sr-12__ticker-num,
    .sr-12__radio-btn,
    .sr-12__btn {
    transition: none;
  }
}
```

## JavaScript
```js
// Update ticker number smoothly when a radio is selected
document.querySelectorAll('input[name="sr-12-vote"]').forEach(r => {
  r.addEventListener('change', function() {
    const ticker = document.getElementById('sr-12-ticker');
    if (!ticker) return;
    ticker.style.transform = 'translateY(-8px)';
    ticker.style.opacity = '0';
    setTimeout(() => {
      ticker.textContent = this.value;
      ticker.style.transform = 'translateY(8px)';
      setTimeout(() => {
        ticker.style.transition = 'transform 0.45s cubic-bezier(.34,1.2,.64,1), opacity 0.35s ease';
        ticker.style.transform = 'translateY(0)';
        ticker.style.opacity = '1';
      }, 30);
    }, 200);
  });
});
function submitRating() {
  const sel = document.querySelector('input[name="sr-12-vote"]:checked');
  if (!sel) alert('Please select a rating first!');
}
```
