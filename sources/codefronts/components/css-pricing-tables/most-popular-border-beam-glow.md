---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/most-popular-border-beam-glow/"
title: "Most Popular Border-Beam Glow"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "A continuous comet of light orbits the \"Most Popular\" card's border — the premium border-beam effect every SaaS landing page wants right now, built with one…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Most Popular Border-Beam Glow
Source: https://codefronts.com/components/css-pricing-tables/most-popular-border-beam-glow/

A continuous comet of light orbits the "Most Popular" card's border — the premium border-beam effect every SaaS landing page wants right now, built with one registered @property angle and a masked conic-gradient. No SVG, no canvas.
## HTML
```html
<section class="prc-06" aria-label="Pricing with highlighted popular plan">
  <div class="prc-06__grid">
    <article class="prc-06__card"><h3>Indie</h3><p class="prc-06__price">$10<small>/mo</small></p><ul><li>1 product</li><li>Standard checkout</li><li>2% fee</li></ul><a href="#" class="prc-06__cta">Go Indie</a></article>
    <article class="prc-06__card prc-06__card--beam"><span class="prc-06__flag">Most popular</span><h3>Business</h3><p class="prc-06__price">$29<small>/mo</small></p><ul><li>Unlimited products</li><li>Custom checkout</li><li>0.5% fee</li><li>Subscriptions</li></ul><a href="#" class="prc-06__cta prc-06__cta--hot">Go Business</a></article>
    <article class="prc-06__card"><h3>Platform</h3><p class="prc-06__price">$85<small>/mo</small></p><ul><li>Everything in Business</li><li>Marketplace payouts</li><li>0% fee</li></ul><a href="#" class="prc-06__cta">Go Platform</a></article>
  </div>
</section>
```
## CSS
```css
@property --prc06-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.prc-06,
.prc-06 *,
.prc-06 *::before,
.prc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-06 {
  --beam: oklch(0.8 0.16 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0d0f16;
  color: #e9ecf5;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
}

.prc-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 20px;
  width: min(880px,100%);
  align-items: center;
}

.prc-06__card {
  position: relative;
  background: #151824;
  border: 1px solid #252a3c;
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.prc-06__card--beam {
  background: #171b2a;
  border-color: transparent;
  padding: 30px 28px;
}

.prc-06__card--beam::before,
.prc-06__card--beam::after {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: 19px;
  background: conic-gradient(from var(--prc06-a),transparent 0deg 300deg,var(--beam) 342deg,#fff 351deg,var(--beam) 356deg,transparent 360deg);
  animation: prc-06-spin 4s linear infinite;
  pointer-events: none;
}

.prc-06__card--beam::before {
  padding: 2px;
  mask: linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask: linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
}

.prc-06__card--beam::after {
  filter: blur(18px);
  opacity: .35;
  z-index: -1;
}

@keyframes prc-06-spin {
  to {
    --prc06-a: 360deg;
  }
}

.prc-06__flag {
  width: max-content;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 4px 11px;
  border-radius: 99px;
  background: oklch(0.8 0.16 85/.15);
  color: var(--beam);
  border: 1px solid oklch(0.8 0.16 85/.4);
}

.prc-06__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #8b92ab;
}

.prc-06__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-06__price small {
  font-size: 15px;
  font-weight: 600;
  color: #8b92ab;
}

.prc-06__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 13.5px;
  color: #b6bcd0;
  flex: 1;
}

.prc-06__card li::before {
  content: "✓";
  color: var(--beam);
  font-weight: 700;
  margin-right: 9px;
}

.prc-06__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1px solid #2c3145;
  color: #e9ecf5;
  transition: border-color .2s;
}

.prc-06__cta:hover {
  border-color: var(--beam);
}

.prc-06__cta--hot {
  background: var(--beam);
  border-color: var(--beam);
  color: #141105;
}

.prc-06__cta--hot:hover {
  filter: brightness(1.08);
}

.prc-06__cta:focus-visible {
  outline: 3px solid var(--beam);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-06__card--beam::before,
    .prc-06__card--beam::after {
    animation: none;
    background: conic-gradient(from 210deg,transparent 0 300deg,var(--beam) 330deg,transparent 360deg);
  }
}
```

## JavaScript
```js
/* No JavaScript — a registered @property <angle> animates from 0 to 360deg, spinning a conic-gradient comet that a two-layer mask clips into a 2px border ring; a blurred copy behind the card supplies the glow. */
```
