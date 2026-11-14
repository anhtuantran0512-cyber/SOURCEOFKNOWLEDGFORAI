---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/material-design-elevation-card/"
title: "Material-Design Elevation Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "The classic Material layout: a clean white card with realistic layered box-shadow depth that lifts to a higher elevation on hover, a coloured category chip…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material-Design Elevation Card
Source: https://codefronts.com/components/css-product-cards/material-design-elevation-card/

The classic Material layout: a clean white card with realistic layered box-shadow depth that lifts to a higher elevation on hover, a coloured category chip and a text-button CTA. The Google-Material product card devs search for by name.
## HTML
```html
<article class="cpc-10">
  <div class="cpc-10__card">
    <div class="cpc-10__media" role="img" aria-label="Product photo: Terra ceramic planter"><span>product shot</span></div>
    <div class="cpc-10__body">
      <span class="cpc-10__chip">Home</span>
      <h3 class="cpc-10__name">Terra Ceramic Planter</h3>
      <p class="cpc-10__sub">Matte glaze · 3 sizes</p>
      <div class="cpc-10__foot"><p class="cpc-10__price">$44</p><button class="cpc-10__cta" type="button">Add to Cart</button></div>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-10,
.cpc-10 *,
.cpc-10 *::before,
.cpc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-10 ::selection {
  background: oklch(0.6 0.14 145);
  color: #fff;
}

.cpc-10 {
  --accent: oklch(0.52 0.13 150);
  font-family: 'Segoe UI',Roboto,system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: #eceff1;
}

.cpc-10__card {
  width: 320px;
  border-radius: 12px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,.16),0 8px 20px -8px rgba(0,0,0,.22);
  transition: transform .28s cubic-bezier(.4,0,.2,1),box-shadow .28s cubic-bezier(.4,0,.2,1);
}

.cpc-10__card:hover,
.cpc-10__card:focus-within {
  transform: translateY(-6px);
  box-shadow: 0 8px 12px rgba(0,0,0,.2),0 24px 44px -12px rgba(0,0,0,.32);
}

.cpc-10__media {
  aspect-ratio: 16/10;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#d7e3d9,#c3d4c6),repeating-linear-gradient(45deg,rgba(255,255,255,.4) 0 14px,transparent 14px 28px);
}

.cpc-10__media {
  background-image: url("https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-10__media span {
  display: none;
}

.cpc-10__body {
  padding: 18px 18px 14px;
}

.cpc-10__chip {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 999px;
  background: color-mix(in oklch,var(--accent) 14%,#fff);
  color: var(--accent);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.cpc-10__name {
  margin-top: 12px;
  font-size: 19px;
  font-weight: 600;
  color: #1c2321;
}

.cpc-10__sub {
  margin-top: 4px;
  font-size: 13px;
  color: #6b7772;
}

.cpc-10__foot {
  margin-top: 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cpc-10__price {
  font-size: 20px;
  font-weight: 700;
  color: #1c2321;
}

.cpc-10__cta {
  position: relative;
  overflow: hidden;
  height: 40px;
  padding: 0 16px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  background: transparent;
  color: var(--accent);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.cpc-10__cta::before {
  content: "";
  position: absolute;
  inset: 0;
  background: currentColor;
  opacity: 0;
  transition: opacity .2s;
}

.cpc-10__cta:hover::before {
  opacity: .1;
}

.cpc-10__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-10__card,
    .cpc-10__cta::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two-layer key+ambient box-shadow lifts on :hover for Material elevation. */
```
