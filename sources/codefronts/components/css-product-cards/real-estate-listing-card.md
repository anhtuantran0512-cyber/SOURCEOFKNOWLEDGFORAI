---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/real-estate-listing-card/"
title: "Real-Estate Listing Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A property listing card with a price, address, a beds/baths/sqft feature row and a heart 'save to favourites' toggle — a pure-CSS checkbox that fills and…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real-Estate Listing Card
Source: https://codefronts.com/components/css-product-cards/real-estate-listing-card/

A property listing card with a price, address, a beds/baths/sqft feature row and a heart 'save to favourites' toggle — a pure-CSS checkbox that fills and pops when saved. The property-card layout real-estate and rental sites search for.
## HTML
```html
<article class="cpc-17">
  <div class="cpc-17__card">
    <div class="cpc-17__media" role="img" aria-label="Property photo: 12 Larch Grove">
      <span>property shot</span>
      <span class="cpc-17__status">For Sale</span>
      <input class="cpc-17__fav-in" type="checkbox" id="cpc-17-fav">
      <label class="cpc-17__fav" for="cpc-17-fav" aria-label="Save to favourites"><span aria-hidden="true">♥</span></label>
    </div>
    <div class="cpc-17__body">
      <p class="cpc-17__price">$685,000</p>
      <h3 class="cpc-17__addr">12 Larch Grove, Portland</h3>
      <p class="cpc-17__type">Detached · 2 storeys</p>
      <ul class="cpc-17__feat">
        <li><b>3</b><span>Beds</span></li>
        <li><b>2</b><span>Baths</span></li>
        <li><b>1,840</b><span>Sq&nbsp;Ft</span></li>
      </ul>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-17,
.cpc-17 *,
.cpc-17 *::before,
.cpc-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-17 ::selection {
  background: oklch(0.5 0.13 220);
  color: #fff;
}

.cpc-17 {
  --accent: oklch(0.48 0.13 220);
  --fav: oklch(0.6 0.2 15);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #eef1f4;
}

.cpc-17__card {
  width: 330px;
  border-radius: 18px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 16px 40px -22px rgba(16,24,40,.4);
}

.cpc-17__media {
  position: relative;
  aspect-ratio: 16/10;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#d7dfe8,#c3cdda),repeating-linear-gradient(45deg,rgba(255,255,255,.4) 0 14px,transparent 14px 28px);
}

.cpc-17__media {
  background-image: url("https://images.unsplash.com/photo-1418985991508-e47386d96a71?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-17__media>span:first-child {
  display: none;
}

.cpc-17__status {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 5px 12px;
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .04em;
}

.cpc-17__fav-in {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.cpc-17__fav {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,.92);
  box-shadow: 0 4px 12px -4px rgba(0,0,0,.3);
}

.cpc-17__fav span {
  font-size: 20px;
  line-height: 1;
  color: #b8c0cc;
  transition: transform .2s,color .2s;
}

.cpc-17__fav:hover span {
  color: var(--fav);
}

.cpc-17__fav-in:checked+.cpc-17__fav span {
  color: var(--fav);
  transform: scale(1.25);
}

.cpc-17__fav-in:focus-visible+.cpc-17__fav {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.cpc-17__body {
  padding: 18px 20px 20px;
}

.cpc-17__price {
  font-size: 24px;
  font-weight: 800;
  color: #101828;
}

.cpc-17__addr {
  margin-top: 4px;
  font-size: 16px;
  font-weight: 600;
  color: #344054;
}

.cpc-17__type {
  margin-top: 2px;
  font-size: 13px;
  color: #667085;
}

.cpc-17__feat {
  list-style: none;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #eaecf0;
  display: flex;
  justify-content: space-between;
}

.cpc-17__feat li {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.cpc-17__feat b {
  font-size: 17px;
  font-weight: 700;
  color: #101828;
}

.cpc-17__feat span {
  font-size: 11px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #98a2b8;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-17__fav span {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a visually-hidden checkbox drives the heart 'saved' state via :checked. */
```
