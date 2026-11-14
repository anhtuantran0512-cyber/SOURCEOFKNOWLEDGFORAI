---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/dark-mode-gadget-card/"
title: "Dark-Mode Gadget Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A high-contrast dark card with a subtle grey border and an accent glow that blooms on hover — tuned for gaming gear, crypto hardware and tech gadgets."
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark-Mode Gadget Card
Source: https://codefronts.com/components/css-product-cards/dark-mode-gadget-card/

A high-contrast dark card with a subtle grey border and an accent glow that blooms on hover — tuned for gaming gear, crypto hardware and tech gadgets. The dark-mode product card devs search for that doesn't look washed out.
## HTML
```html
<article class="cpc-08">
  <div class="cpc-08__card">
    <div class="cpc-08__media" role="img" aria-label="Product photo: Vantage gaming mouse">
      <span>product shot</span><span class="cpc-08__stock">In stock</span>
    </div>
    <div class="cpc-08__body">
      <p class="cpc-08__brand">Vantage</p>
      <h3 class="cpc-08__name">Vantage Pro Wireless Mouse</h3>
      <p class="cpc-08__spec">26K DPI · 74g · 90h battery</p>
      <div class="cpc-08__row"><p class="cpc-08__price">$99</p><button class="cpc-08__cta" type="button">Add to Cart</button></div>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-08,
.cpc-08 *,
.cpc-08 *::before,
.cpc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-08 ::selection {
  background: oklch(0.82 0.16 195);
  color: #03121a;
}

.cpc-08 {
  --accent: oklch(0.82 0.16 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(120% 120% at 50% 20%,#0d1014,#050609);
}

.cpc-08__card {
  width: 320px;
  border-radius: 18px;
  overflow: hidden;
  background: linear-gradient(180deg,#12161b,#0c0f13);
  border: 1px solid #1e252c;
  box-shadow: 0 30px 60px -34px #000;
  transition: transform .35s,box-shadow .35s,border-color .35s;
}

.cpc-08__card:hover {
  transform: translateY(-4px);
  border-color: color-mix(in oklch,var(--accent) 45%,#1e252c);
  box-shadow: 0 34px 70px -34px #000,0 0 40px -12px color-mix(in oklch,var(--accent) 60%,transparent);
}

.cpc-08__media {
  position: relative;
  aspect-ratio: 16/11;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#1a2027,#11161b),repeating-linear-gradient(45deg,rgba(255,255,255,.04) 0 14px,transparent 14px 28px);
}

.cpc-08__media {
  background-image: url("https://images.unsplash.com/photo-1511499767150-a48a237f0083?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-08__media>span:first-child {
  display: none;
}

.cpc-08__stock {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 5px 12px;
  border-radius: 999px;
  font: 10px ui-monospace,Menlo,monospace;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  background: color-mix(in oklch,var(--accent) 14%,#0c0f13);
  border: 1px solid color-mix(in oklch,var(--accent) 40%,transparent);
  box-shadow: 0 0 16px -4px var(--accent);
}

.cpc-08__body {
  padding: 20px 22px 22px;
}

.cpc-08__brand {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #67757f;
}

.cpc-08__name {
  margin-top: 6px;
  font-size: 18px;
  font-weight: 600;
  color: #eef4f8;
  line-height: 1.3;
}

.cpc-08__spec {
  margin-top: 8px;
  font-size: 13px;
  color: #8090a0;
}

.cpc-08__row {
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cpc-08__price {
  font-size: 22px;
  font-weight: 800;
  color: #fff;
  text-shadow: 0 0 18px color-mix(in oklch,var(--accent) 45%,transparent);
}

.cpc-08__cta {
  height: 44px;
  padding: 0 22px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
  color: #04141a;
  font-size: 14px;
  font-weight: 700;
  box-shadow: 0 0 22px -6px var(--accent);
}

.cpc-08__cta:hover {
  filter: brightness(1.1);
}

.cpc-08__cta:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 55%,#000);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-08__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — accent glow blooms via box-shadow on :hover. */
```
