---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/neumorphic-soft-star-rating/"
title: "Neumorphic Soft Star Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A tactile soft-UI rating widget carved from a warm off-white canvas using CSS box-shadow neumorphism — stars toggle between debossed (sunken) and embossed…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft Star Rating
Source: https://codefronts.com/components/css-star-ratings/neumorphic-soft-star-rating/

A tactile soft-UI rating widget carved from a warm off-white canvas using CSS box-shadow neumorphism — stars toggle between debossed (sunken) and embossed (raised) states with a radiant golden inner glow.
## HTML
```html
<div class="sr-08">
  <div class="sr-08__panel">
    <div class="sr-08__icon-wrap">🛋️</div>
    <div class="sr-08__title">Comfort Rating</div>
    <div class="sr-08__sub">Press a star to feel the neumorphic depth</div>

    <form>
      <div class="sr-08__stars">
        <input type="radio" id="sr-08-n5" name="sr-08-neu" value="5">
        <label for="sr-08-n5">5</label>
        <input type="radio" id="sr-08-n4" name="sr-08-neu" value="4">
        <label for="sr-08-n4">4</label>
        <input type="radio" id="sr-08-n3" name="sr-08-neu" value="3">
        <label for="sr-08-n3">3</label>
        <input type="radio" id="sr-08-n2" name="sr-08-neu" value="2">
        <label for="sr-08-n2">2</label>
        <input type="radio" id="sr-08-n1" name="sr-08-neu" value="1">
        <label for="sr-08-n1">1</label>
      </div>
    </form>

    <div class="sr-08__score-strip">
      <div class="sr-08__score-item">
        <div class="sr-08__score-num">4.8</div>
        <div class="sr-08__score-label">Avg Score</div>
      </div>
      <hr class="sr-08__divider">
      <div class="sr-08__score-item">
        <div class="sr-08__score-num">1.2k</div>
        <div class="sr-08__score-label">Reviews</div>
      </div>
      <hr class="sr-08__divider">
      <div class="sr-08__score-item">
        <div class="sr-08__score-num">94%</div>
        <div class="sr-08__score-label">Recommend</div>
      </div>
    </div>

    <button type="submit" class="sr-08__submit">Submit Rating</button>
  </div>
</div>
```
## CSS
```css
.sr-08,
.sr-08 *,
.sr-08 *::before,
.sr-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-08 ::selection {
  background: #d4a847;
  color: #fff;
}

.sr-08 {
  --neu-bg: #e8e4de;
  --neu-shadow-dark: #bfbab4;
  --neu-shadow-light: #fff;
  --gold: #d4a847;
  --gold-glow: rgba(212,168,71,0.5);
  --gold-inner: #f0c060;
  --text: #5c5347;
  --text-muted: #9c9187;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--neu-bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 16px;
}

.sr-08__panel {
  background: var(--neu-bg);
  border-radius: 28px;
  box-shadow: 12px 12px 24px var(--neu-shadow-dark), -12px -12px 24px var(--neu-shadow-light);
  padding: 40px 44px 36px;
  max-width: 420px;
  width: 100%;
  text-align: center;
}

.sr-08__icon-wrap {
  width: 72px;
  height: 72px;
  border-radius: 18px;
  background: var(--neu-bg);
  box-shadow: 6px 6px 14px var(--neu-shadow-dark), -6px -6px 14px var(--neu-shadow-light), inset 0 0 0 transparent;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 34px;
}

.sr-08__title {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 6px;
}

.sr-08__sub {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 32px;
}

.sr-08__stars {
  display: flex;
  flex-direction: row-reverse;
  justify-content: center;
  gap: 14px;
  margin-bottom: 32px;
}

.sr-08__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-08__stars label {
  display: block;
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: var(--neu-bg);
  /* Debossed (sunken) state: inner shadows */
  box-shadow: 4px 4px 8px var(--neu-shadow-dark), -4px -4px 8px var(--neu-shadow-light);
  cursor: pointer;
  position: relative;
  transition: box-shadow 0.25s ease, transform 0.2s ease;
  /* Hide the digit text content — star shape is drawn via ::before,
       screen readers get the value via the input's aria-label. */
  font-size: 0;
}
/* Star shape inside each label */

.sr-08__stars label::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 36px;
  height: 36px;
  background: var(--text-muted);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.3s ease, filter 0.3s ease;
  opacity: 0.5;
}
/* Hover: emboss the button outward */

.sr-08__stars label:hover {
  box-shadow: 6px 6px 14px var(--neu-shadow-dark), -6px -6px 14px var(--neu-shadow-light), inset 0 0 0 transparent;
  transform: translateY(-2px);
}

.sr-08__stars label:hover::before {
  background: var(--gold);
  opacity: 0.7;
  filter: drop-shadow(0 0 6px var(--gold-glow));
}
/* Cascade hover fill */

.sr-08__stars label:hover ~ label::before {
  background: var(--gold);
  opacity: 0.7;
}
/* Checked: full emboss + golden inner glow */

.sr-08__stars input:checked ~ label {
  box-shadow: inset 4px 4px 8px var(--neu-shadow-dark), inset -4px -4px 8px var(--neu-shadow-light);
}

.sr-08__stars input:checked ~ label::before {
  background: var(--gold);
  opacity: 1;
  filter: drop-shadow(0 0 8px var(--gold-glow));
}
/* The actually-checked star gets strongest inner glow */

.sr-08__stars input:checked + label {
  box-shadow: inset 4px 4px 10px var(--neu-shadow-dark), inset -3px -3px 8px var(--neu-shadow-light), 0 0 0 2px var(--gold-inner);
}

.sr-08__stars input:checked + label::before {
  background: var(--gold-inner);
  filter: drop-shadow(0 0 14px var(--gold-glow));
  transform: translate(-50%, -50%) scale(1.08);
}
/* Score strip */

.sr-08__score-strip {
  display: flex;
  justify-content: space-between;
  margin-bottom: 24px;
}

.sr-08__score-item {
  text-align: center;
}

.sr-08__score-num {
  font-size: 1.3rem;
  font-weight: 900;
  color: var(--text);
}

.sr-08__score-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  margin-top: 2px;
}

.sr-08__divider {
  width: 1px;
  background: var(--neu-shadow-dark);
  margin: 4px 0;
  border: none;
  opacity: 0.4;
}

.sr-08__submit {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 14px;
  background: var(--neu-bg);
  box-shadow: 6px 6px 14px var(--neu-shadow-dark), -6px -6px 14px var(--neu-shadow-light);
  color: var(--gold);
  font-weight: 700;
  font-size: 0.92rem;
  cursor: pointer;
  transition: box-shadow 0.2s, transform 0.15s;
  letter-spacing: 0.4px;
}

.sr-08__submit:hover {
  box-shadow: 8px 8px 18px var(--neu-shadow-dark), -8px -8px 18px var(--neu-shadow-light);
  transform: translateY(-1px);
}

.sr-08__submit:active {
  box-shadow: inset 4px 4px 8px var(--neu-shadow-dark), inset -4px -4px 8px var(--neu-shadow-light);
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .sr-08__stars label,
    .sr-08__stars label::before,
    .sr-08__submit {
    transition: none;
  }
}
```
