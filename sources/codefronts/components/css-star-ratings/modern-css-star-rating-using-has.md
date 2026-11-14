---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/modern-css-star-rating-using-has/"
title: "Modern CSS Star Rating using has()"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A dark-mode developer-review card demonstrating :has() for forward and backward sibling selection, with electric-indigo star hover and a clean slate-on-dark…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern CSS Star Rating using has()
Source: https://codefronts.com/components/css-star-ratings/modern-css-star-rating-using-has/

A dark-mode developer-review card demonstrating :has() for forward and backward sibling selection, with electric-indigo star hover and a clean slate-on-dark aesthetic.
## HTML
```html
<div class="sr-02">
  <div class="sr-02__card">
    <div class="sr-02__header">
      <div class="sr-02__avatar">🧑‍💻</div>
      <div class="sr-02__meta">
        <div class="sr-02__name">Rate this API</div>
        <div class="sr-02__date">CloudBase SDK v3.2</div>
      </div>
      <span class="sr-02__badge">:has()</span>
    </div>
    <div class="sr-02__prompt">How satisfied are you with the developer experience?</div>
    <form class="sr-02__form">
      <div class="sr-02__stars">
        <input type="radio" id="sr-02-r5" name="sr-02-rate" value="5">
        <label for="sr-02-r5">5</label>
        <input type="radio" id="sr-02-r4" name="sr-02-rate" value="4">
        <label for="sr-02-r4">4</label>
        <input type="radio" id="sr-02-r3" name="sr-02-rate" value="3">
        <label for="sr-02-r3">3</label>
        <input type="radio" id="sr-02-r2" name="sr-02-rate" value="2">
        <label for="sr-02-r2">2</label>
        <input type="radio" id="sr-02-r1" name="sr-02-rate" value="1">
        <label for="sr-02-r1">1</label>
      </div>
      <div class="sr-02__hint">Tap a star to rate</div>
      <div class="sr-02__tags">
        <span class="sr-02__tag">DX Quality</span>
        <span class="sr-02__tag">Docs</span>
        <span class="sr-02__tag">Performance</span>
      </div>
      <div class="sr-02__actions">
        <button type="submit" class="sr-02__btn sr-02__btn--primary">Submit Review</button>
        <button type="reset" class="sr-02__btn sr-02__btn--ghost">Clear</button>
      </div>
    </form>
  </div>
</div>
```
## CSS
```css
.sr-02,
.sr-02 *,
.sr-02 *::before,
.sr-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-02 ::selection {
  background: #6366f1;
  color: #fff;
}

.sr-02 {
  --indigo: #6366f1;
  --indigo-light: #818cf8;
  --indigo-glow: rgba(99,102,241,0.4);
  --slate: #94a3b8;
  --bg-card: #1e293b;
  --bg-page: #0f172a;
  --text: #f1f5f9;
  --text-muted: #94a3b8;
  --outline: #334155;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-page);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-02__card {
  background: var(--bg-card);
  border: 1px solid var(--outline);
  border-radius: 18px;
  padding: 32px 36px 28px;
  max-width: 420px;
  width: 100%;
  box-shadow: 0 8px 40px rgba(0,0,0,0.4);
}

.sr-02__header {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--outline);
}

.sr-02__avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}

.sr-02__meta {
  flex: 1;
}

.sr-02__name {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--text);
}

.sr-02__date {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 2px;
}

.sr-02__badge {
  font-size: 0.7rem;
  font-weight: 700;
  background: rgba(99,102,241,0.2);
  color: var(--indigo-light);
  border: 1px solid rgba(99,102,241,0.3);
  border-radius: 50px;
  padding: 3px 10px;
  letter-spacing: 0.5px;
}

.sr-02__prompt {
  font-size: 0.88rem;
  color: var(--text-muted);
  margin-bottom: 14px;
}
/* :has() based rating — no flex-reverse needed */

.sr-02__form {
  position: relative;
}

.sr-02__stars {
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-end;
  gap: 4px;
  margin-bottom: 18px;
}

.sr-02__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
  pointer-events: none;
}

.sr-02__stars label {
  cursor: pointer;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0;
  position: relative;
  transition: transform 0.2s cubic-bezier(.34,1.56,.64,1);
}

.sr-02__stars label::before {
  content: '';
  width: 36px;
  height: 36px;
  display: block;
  /* Outlined star via SVG background */
  background: var(--slate);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.2s ease, filter 0.25s ease;
}
/* :has() sibling fill — hover this label and all labels after it (lower values) */

.sr-02__stars:has(label:hover) label:hover::before,
.sr-02__stars:has(label:hover) label:hover ~ label::before {
  background: var(--indigo-light);
  filter: drop-shadow(0 0 8px var(--indigo-glow));
}
/* Checked state via :has() targeting the PARENT */

.sr-02__form:has(#sr-02-r5:checked) .sr-02__stars label::before,
.sr-02__form:has(#sr-02-r4:checked) .sr-02__stars label:nth-child(n+4)::before,
.sr-02__form:has(#sr-02-r3:checked) .sr-02__stars label:nth-child(n+6)::before,
.sr-02__form:has(#sr-02-r2:checked) .sr-02__stars label:nth-child(n+8)::before,
.sr-02__form:has(#sr-02-r1:checked) .sr-02__stars label:nth-child(10)::before {
  background: var(--indigo);
  filter: drop-shadow(0 0 10px var(--indigo-glow));
}

.sr-02__stars label:hover {
  transform: scale(1.18);
}
/* Hover state hint text */

.sr-02__hint {
  font-size: 0.82rem;
  color: var(--text-muted);
  min-height: 20px;
  transition: color 0.2s;
}

.sr-02__form:has(#sr-02-r1:checked) .sr-02__hint {
  content: 'Terrible';
}

.sr-02__tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 18px;
}

.sr-02__tag {
  font-size: 0.75rem;
  background: rgba(99,102,241,0.12);
  color: var(--indigo-light);
  border: 1px solid rgba(99,102,241,0.2);
  border-radius: 6px;
  padding: 4px 10px;
}

.sr-02__actions {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.sr-02__btn {
  flex: 1;
  padding: 10px;
  border-radius: 10px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: background 0.2s, transform 0.15s;
}

.sr-02__btn--primary {
  background: var(--indigo);
  color: #fff;
}

.sr-02__btn--primary:hover {
  background: var(--indigo-light);
  transform: translateY(-1px);
}

.sr-02__btn--ghost {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--outline);
}

.sr-02__btn--ghost:hover {
  background: var(--outline);
}

@media (prefers-reduced-motion: reduce) {
  .sr-02__stars label,
    .sr-02__stars label::before,
    .sr-02__btn {
    transition: none;
  }
}
```
