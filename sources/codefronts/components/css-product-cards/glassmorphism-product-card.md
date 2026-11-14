---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/glassmorphism-product-card/"
title: "Glassmorphism Product Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A frosted-glass card — backdrop-filter blur, a semi-transparent white fill and a fine light border — floating over a colourful gradient scene."
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Product Card
Source: https://codefronts.com/components/css-product-cards/glassmorphism-product-card/

A frosted-glass card — backdrop-filter blur, a semi-transparent white fill and a fine light border — floating over a colourful gradient scene. The Web3, SaaS and digital-goods look devs search for as 'glassmorphism'.
## HTML
```html
<article class="cpc-07">
  <div class="cpc-07__card">
    <div class="cpc-07__img" role="img" aria-label="Product photo: Prism smart lamp"><span>product shot</span></div>
    <p class="cpc-07__tag">New drop</p>
    <h3 class="cpc-07__name">Prism Smart Lamp</h3>
    <p class="cpc-07__desc">16M colours, app-controlled, ambient sync.</p>
    <div class="cpc-07__row"><p class="cpc-07__price">$89</p><button class="cpc-07__cta" type="button">Add to Cart</button></div>
  </div>
</article>
```
## CSS
```css
.cpc-07,
.cpc-07 *,
.cpc-07 *::before,
.cpc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-07 ::selection {
  background: rgba(255,255,255,.85);
  color: #2a1a4a;
}

.cpc-07 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(50% 60% at 15% 20%,oklch(0.7 0.2 20 / .9),transparent 60%), radial-gradient(50% 60% at 85% 30%,oklch(0.72 0.2 260 / .9),transparent 60%), radial-gradient(60% 70% at 60% 90%,oklch(0.75 0.19 180 / .85),transparent 60%), linear-gradient(135deg,#2a1a52,#0f1030);
}

.cpc-07__card {
  position: relative;
  width: 310px;
  padding: 22px;
  border-radius: 22px;
  overflow: hidden;
  background: rgba(255,255,255,.14);
  -webkit-backdrop-filter: blur(18px) saturate(1.4);
  backdrop-filter: blur(18px) saturate(1.4);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.4);
  transition: transform .4s,box-shadow .4s,border-color .4s;
}

.cpc-07__card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 12%;
  right: 12%;
  height: 1px;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.8),transparent);
}

.cpc-07__card:hover {
  transform: translateY(-4px);
  border-color: rgba(255,255,255,.45);
  box-shadow: 0 40px 70px -30px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.5);
}

.cpc-07__img {
  aspect-ratio: 16/10;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,rgba(255,255,255,.3),rgba(255,255,255,.08));
  border: 1px solid rgba(255,255,255,.2);
}

.cpc-07__img {
  background-image: url("https://images.unsplash.com/photo-1505373877841-8d25f7d46678?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-07__img span {
  display: none;
}

.cpc-07__tag {
  margin-top: 16px;
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(255,255,255,.75);
}

.cpc-07__name {
  margin-top: 6px;
  font-size: 20px;
  font-weight: 700;
  color: #fff;
  text-shadow: 0 1px 6px rgba(0,0,0,.2);
}

.cpc-07__desc {
  margin-top: 6px;
  font-size: 13.5px;
  line-height: 1.5;
  color: rgba(255,255,255,.82);
}

.cpc-07__row {
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cpc-07__price {
  font-size: 22px;
  font-weight: 800;
  color: #fff;
}

.cpc-07__cta {
  height: 44px;
  padding: 0 22px;
  border: 1px solid rgba(255,255,255,.5);
  border-radius: 12px;
  cursor: pointer;
  background: rgba(255,255,255,.9);
  color: #241844;
  font-size: 14px;
  font-weight: 700;
}

.cpc-07__cta:hover {
  background: #fff;
}

.cpc-07__cta:focus-visible {
  outline: 3px solid rgba(255,255,255,.8);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-07__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter frosts the gradient scene behind the card. */
```
