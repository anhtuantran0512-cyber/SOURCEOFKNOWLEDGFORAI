---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/hover-reveal-add-to-cart-button/"
title: "Hover-Reveal \"Add to Cart\" Button"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A clean, minimal product card that keeps the layout calm by hiding the CTA — the 'Add to Cart' button slides and fades up into view only when the shopper…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hover-Reveal "Add to Cart" Button
Source: https://codefronts.com/components/css-product-cards/hover-reveal-add-to-cart-button/

A clean, minimal product card that keeps the layout calm by hiding the CTA — the 'Add to Cart' button slides and fades up into view only when the shopper hovers or keyboard-focuses the card. The single most-searched hover-CTA pattern in Tier-1 e-commerce.
## HTML
```html
<article class="cpc-01">
  <div class="cpc-01__card">
    <div class="cpc-01__media" role="img" aria-label="Product photo: Aurora wireless headphones"><span>product shot</span></div>
    <div class="cpc-01__body">
      <p class="cpc-01__brand">SoundField</p>
      <h3 class="cpc-01__name">Aurora Wireless Headphones</h3>
      <p class="cpc-01__price">$149.00</p>
      <button class="cpc-01__cta" type="button">Add to Cart</button>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-01,
.cpc-01 *,
.cpc-01 *::before,
.cpc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-01 ::selection {
  background: oklch(0.72 0.15 250);
  color: #fff;
}

.cpc-01 {
  --accent: oklch(0.55 0.16 255);
  --dur: .32s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f4f5f7;
}

.cpc-01__card {
  width: 300px;
  background: #fff;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(16,24,40,.06),0 12px 32px -18px rgba(16,24,40,.28);
  transition: box-shadow var(--dur);
}

.cpc-01__card:hover,
.cpc-01__card:focus-within {
  box-shadow: 0 1px 2px rgba(16,24,40,.06),0 26px 50px -22px rgba(16,24,40,.4);
}

.cpc-01__media {
  aspect-ratio: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#e9edf3,#dfe4ec),repeating-linear-gradient(45deg,rgba(255,255,255,.5) 0 12px,transparent 12px 24px);
}

.cpc-01__media {
  background-image: url("https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-01__media span {
  display: none;
}

.cpc-01__body {
  padding: 20px 20px 22px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.cpc-01__brand {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #98a2b3;
}

.cpc-01__name {
  font-size: 17px;
  font-weight: 600;
  color: #101828;
  line-height: 1.3;
}

.cpc-01__price {
  font-size: 18px;
  font-weight: 700;
  color: #101828;
  margin-top: 2px;
  transition: transform var(--dur);
}

.cpc-01__cta {
  margin-top: 14px;
  height: 46px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: .01em;
  opacity: 0;
  transform: translateY(14px);
  transition: opacity var(--dur),transform var(--dur),background var(--dur);
}

.cpc-01__card:hover .cpc-01__cta,
.cpc-01__card:focus-within .cpc-01__cta {
  opacity: 1;
  transform: translateY(0);
}

.cpc-01__cta:hover {
  background: color-mix(in oklch,var(--accent) 88%,#000);
}

.cpc-01__cta:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 45%,#fff);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-01__card,
    .cpc-01__cta,
    .cpc-01__price {
    transition: none;
  }

  .cpc-01__cta {
    opacity: 1;
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the CTA reveal is a pure :hover / :focus-within transition. */
```
