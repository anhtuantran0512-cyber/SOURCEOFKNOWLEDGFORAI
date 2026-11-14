---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/hotel-search-results-slide-in/"
title: "Hotel Search Results Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Three hotel search result cards that slide up from below, each showing a property photo, star rating, review count, location, price per night, and \"View…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hotel Search Results Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/hotel-search-results-slide-in/

Three hotel search result cards that slide up from below, each showing a property photo, star rating, review count, location, price per night, and "View deal" CTA — the layout used by Booking.com, Kayak, Expedia, and Hotels.com search results.
## HTML
```html
<div class="sl-10">
  <div class="sl-10__inner">
    <div class="sl-10__head">
      <p class="sl-10__kicker">Manhattan · Dec 15 – 18</p>
      <h2>3 hotels found near Times Square</h2>
    </div>
    <article class="sl-10__result">
      <div class="sl-10__photo" style="--g:linear-gradient(135deg,#4a90c8,#0055a5)"></div>
      <div class="sl-10__body">
        <div class="sl-10__meta">
          <span class="sl-10__stars">★★★★★</span>
          <span class="sl-10__score">9.4</span>
          <small>Superb · 2,847 reviews</small>
        </div>
        <h3>The Manhattan Plaza</h3>
        <p class="sl-10__loc">Midtown · 0.3 mi from Times Square</p>
        <span class="sl-10__perk sl-10__perk--free">✓ Free cancellation</span>
      </div>
      <div class="sl-10__pricing">
        <span class="sl-10__urgency">Only 2 rooms left!</span>
        <div class="sl-10__price">$328<small>/night</small></div>
        <button class="sl-10__cta">View deal</button>
      </div>
    </article>
    <article class="sl-10__result">
      <div class="sl-10__photo" style="--g:linear-gradient(135deg,#8fb8d8,#5b8fb0)"></div>
      <div class="sl-10__body">
        <div class="sl-10__meta">
          <span class="sl-10__stars">★★★★☆</span>
          <span class="sl-10__score">8.7</span>
          <small>Very good · 1,203 reviews</small>
        </div>
        <h3>Broadway Boutique Hotel</h3>
        <p class="sl-10__loc">Theater District · 0.5 mi from Times Square</p>
        <span class="sl-10__perk sl-10__perk--free">✓ Free breakfast</span>
      </div>
      <div class="sl-10__pricing">
        <div class="sl-10__price">$228<small>/night</small></div>
        <button class="sl-10__cta">View deal</button>
      </div>
    </article>
    <article class="sl-10__result">
      <div class="sl-10__photo" style="--g:linear-gradient(135deg,#c4a878,#8a6f4a)"></div>
      <div class="sl-10__body">
        <div class="sl-10__meta">
          <span class="sl-10__stars">★★★★☆</span>
          <span class="sl-10__score">8.2</span>
          <small>Very good · 968 reviews</small>
        </div>
        <h3>Times Square Value Inn</h3>
        <p class="sl-10__loc">Hell's Kitchen · 0.7 mi from Times Square</p>
        <span class="sl-10__perk sl-10__perk--free">✓ Free cancellation</span>
      </div>
      <div class="sl-10__pricing">
        <div class="sl-10__price">$148<small>/night</small></div>
        <button class="sl-10__cta">View deal</button>
      </div>
    </article>
  </div>
</div>
```
## CSS
```css
.sl-10 {
  --bg: #f4f7fb;
  --card: #fff;
  --blue: #0055a5;
  --sun: #febb02;
  --good: #0a8754;
  --ink: #1a2a3a;
  --sub: #5c6b7d;
  --line: #e0e6ee;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(0,85,165,.05) 0%, transparent 55%), var(--bg);
  color: var(--ink);
}

.sl-10 *,
.sl-10 *::before,
.sl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-10 ::selection {
  background: var(--blue);
  color: #fff;
}

.sl-10__inner {
  width: 100%;
  max-width: 820px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sl-10__head {
  margin-bottom: 8px;
}

.sl-10__kicker {
  font-size: .72rem;
  font-weight: 600;
  color: var(--sub);
  margin-bottom: 2px;
}

.sl-10__head h2 {
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -.01em;
}

.sl-10__result {
  display: grid;
  grid-template-columns: 160px 1fr auto;
  gap: 0;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 8px 20px -12px rgba(0,85,165,.15);
  opacity: 0;
  transform: translateY(30px);
  animation: sl-10-card .55s cubic-bezier(.22,1,.36,1) forwards;
  transition: transform .18s ease,box-shadow .18s ease;
}

.sl-10__result:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px -12px rgba(0,85,165,.22);
}

.sl-10__result:nth-child(2) {
  animation-delay: .2s;
}

.sl-10__result:nth-child(3) {
  animation-delay: .35s;
}

.sl-10__result:nth-child(4) {
  animation-delay: .5s;
}

.sl-10__photo {
  background: var(--g,#ccc);
}

.sl-10__body {
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
}

.sl-10__meta {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.sl-10__stars {
  color: var(--sun);
  font-size: .85rem;
  letter-spacing: 1px;
  line-height: 1;
}

.sl-10__score {
  padding: 2px 7px;
  border-radius: 5px;
  background: var(--blue);
  color: #fff;
  font-size: .78rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.sl-10__meta small {
  font-size: .72rem;
  color: var(--sub);
}

.sl-10__body h3 {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.01em;
  line-height: 1.15;
}

.sl-10__loc {
  font-size: .78rem;
  color: var(--sub);
}

.sl-10__perk {
  align-self: flex-start;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .02em;
  margin-top: 2px;
}

.sl-10__perk--free {
  background: rgba(10,135,84,.12);
  color: var(--good);
}

.sl-10__pricing {
  padding: 16px 18px;
  background: #fafbfd;
  border-left: 1px solid var(--line);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  gap: 6px;
  min-width: 130px;
}

.sl-10__urgency {
  padding: 2px 7px;
  border-radius: 4px;
  background: rgba(215,30,40,.12);
  color: #d71e28;
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .02em;
}

.sl-10__price {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.sl-10__price small {
  font-size: .72rem;
  font-weight: 500;
  color: var(--sub);
  margin-left: 2px;
}

.sl-10__cta {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  background: var(--blue);
  color: #fff;
  font-family: inherit;
  font-size: .82rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease;
}

.sl-10__cta:hover {
  background: #004080;
}

@keyframes sl-10-card {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-10__result {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 640px) {
  .sl-10__result {
    grid-template-columns: 100px 1fr;
    grid-template-rows: auto auto;
  }

  .sl-10__pricing {
    grid-column: 1/-1;
    border-left: 0;
    border-top: 1px solid var(--line);
    align-items: stretch;
    flex-direction: row;
    justify-content: space-between;
  }

  .sl-10__cta {
    flex-shrink: 0;
  }
}
```
