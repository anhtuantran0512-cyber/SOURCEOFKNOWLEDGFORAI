---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/real-estate-property-listing-card-reveal/"
title: "Real Estate Property Listing Card Reveal"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Three property listing cards that slide up from below, each with a hero photo, price, address, bed/bath/sqft specs, and \"View listing\" CTA — the layout used…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real Estate Property Listing Card Reveal
Source: https://codefronts.com/motion/css-slide-in-animation/real-estate-property-listing-card-reveal/

Three property listing cards that slide up from below, each with a hero photo, price, address, bed/bath/sqft specs, and "View listing" CTA — the layout used by Zillow, Redfin, Compass, and modern real estate marketing sites.
## HTML
```html
<div class="sl-05">
  <div class="sl-05__inner">
    <div class="sl-05__head">
      <p class="sl-05__kicker">Featured listings</p>
      <h2>Homes for sale · Pacific Heights, SF</h2>
    </div>
    <div class="sl-05__grid">
      <article class="sl-05__card">
        <div class="sl-05__photo" style="--g:linear-gradient(135deg,#8fa876,#5c7a4f)">
          <span class="sl-05__badge">Just listed</span>
        </div>
        <div class="sl-05__body">
          <div class="sl-05__price">$2,485,000</div>
          <p class="sl-05__addr">2847 Pacific Ave · Pacific Heights</p>
          <div class="sl-05__specs">
            <span><strong>4</strong>bd</span>
            <span><strong>3</strong>ba</span>
            <span><strong>2,850</strong>sqft</span>
          </div>
          <button class="sl-05__cta">View listing</button>
        </div>
      </article>
      <article class="sl-05__card">
        <div class="sl-05__photo" style="--g:linear-gradient(135deg,#c6a875,#8a6f4a)"></div>
        <div class="sl-05__body">
          <div class="sl-05__price">$1,875,000</div>
          <p class="sl-05__addr">1420 Broadway · Pacific Heights</p>
          <div class="sl-05__specs">
            <span><strong>3</strong>bd</span>
            <span><strong>2.5</strong>ba</span>
            <span><strong>2,140</strong>sqft</span>
          </div>
          <button class="sl-05__cta">View listing</button>
        </div>
      </article>
      <article class="sl-05__card">
        <div class="sl-05__photo" style="--g:linear-gradient(135deg,#7a8ea8,#4a5f7a)">
          <span class="sl-05__badge sl-05__badge--reduced">Price reduced</span>
        </div>
        <div class="sl-05__body">
          <div class="sl-05__price">$1,285,000</div>
          <p class="sl-05__addr">2210 Fillmore St · Pacific Heights</p>
          <div class="sl-05__specs">
            <span><strong>2</strong>bd</span>
            <span><strong>2</strong>ba</span>
            <span><strong>1,650</strong>sqft</span>
          </div>
          <button class="sl-05__cta">View listing</button>
        </div>
      </article>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-05 {
  --bg: #faf9f5;
  --card: #fff;
  --accent: #5c7a4f;
  --gold: #b8934a;
  --ink: #2a2620;
  --sub: #5c5548;
  --line: #e6e2d6;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(92,122,79,.05) 0%, transparent 55%), var(--bg);
  color: var(--ink);
}

.sl-05 *,
.sl-05 *::before,
.sl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-05 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-05__inner {
  width: 100%;
  max-width: 1000px;
}

.sl-05__head {
  margin-bottom: 28px;
  text-align: center;
}

.sl-05__kicker {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: .85rem;
  font-weight: 400;
  font-style: italic;
  letter-spacing: .06em;
  color: var(--gold);
  margin-bottom: 6px;
}

.sl-05__head h2 {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: clamp(1.5rem,3vw,2rem);
  font-weight: 800;
  letter-spacing: -.015em;
}

.sl-05__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
}

.sl-05__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 12px 28px -14px rgba(42,38,32,.2);
  opacity: 0;
  transform: translateY(30px);
  animation: sl-05-listing .6s cubic-bezier(.22,1,.36,1) forwards;
  transition: transform .2s ease,box-shadow .2s ease;
}

.sl-05__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 20px 40px -14px rgba(42,38,32,.25);
}

.sl-05__card:nth-child(1) {
  animation-delay: .15s;
}

.sl-05__card:nth-child(2) {
  animation-delay: .3s;
}

.sl-05__card:nth-child(3) {
  animation-delay: .45s;
}

.sl-05__photo {
  position: relative;
  aspect-ratio: 4/3;
  background: var(--g,#ddd);
}

.sl-05__badge {
  position: absolute;
  top: 10px;
  left: 10px;
  padding: 4px 10px;
  border-radius: 6px;
  background: var(--accent);
  color: #fff;
  font-family: 'Playfair Display',Georgia,serif;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .02em;
}

.sl-05__badge--reduced {
  background: #b8934a;
}

.sl-05__body {
  padding: 18px 20px 20px;
}

.sl-05__price {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  margin-bottom: 4px;
}

.sl-05__addr {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.4;
  margin-bottom: 12px;
}

.sl-05__specs {
  display: flex;
  gap: 14px;
  padding-bottom: 14px;
  margin-bottom: 14px;
  border-bottom: 1px solid var(--line);
}

.sl-05__specs span {
  font-size: .78rem;
  color: var(--sub);
}

.sl-05__specs strong {
  color: var(--ink);
  font-weight: 700;
  margin-right: 2px;
  font-variant-numeric: tabular-nums;
}

.sl-05__cta {
  width: 100%;
  padding: 10px 16px;
  border: 1px solid var(--accent);
  border-radius: 8px;
  background: transparent;
  color: var(--accent);
  font-family: inherit;
  font-size: .82rem;
  font-weight: 600;
  letter-spacing: .02em;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.sl-05__cta:hover {
  background: var(--accent);
  color: #fff;
}

@keyframes sl-05-listing {
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
  .sl-05__card {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 820px) {
  .sl-05__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 520px) {
  .sl-05__grid {
    grid-template-columns: 1fr;
  }
}
```
