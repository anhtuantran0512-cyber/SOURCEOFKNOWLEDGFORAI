---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/pure-css-3d-flip-product-card/"
title: "Pure-CSS 3D Flip Product Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A card that flips in 3D on hover (or keyboard focus) to reveal the back face — specs, size chart or fabric details — without a single line of JavaScript."
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure-CSS 3D Flip Product Card
Source: https://codefronts.com/components/css-product-cards/pure-css-3d-flip-product-card/

A card that flips in 3D on hover (or keyboard focus) to reveal the back face — specs, size chart or fabric details — without a single line of JavaScript. The structural flip layout apparel and gadget stores search for by name.
## HTML
```html
<article class="cpc-02" tabindex="0" aria-label="Trailhead running shoe — hover or focus to see specs">
  <div class="cpc-02__inner">
    <div class="cpc-02__face cpc-02__front">
      <div class="cpc-02__media" role="img" aria-label="Product photo: Trailhead running shoe"><span>product shot</span></div>
      <div class="cpc-02__meta"><h3 class="cpc-02__name">Trailhead GTX</h3><p class="cpc-02__price">$189</p></div>
      <p class="cpc-02__hint">hover / focus to flip</p>
    </div>
    <div class="cpc-02__face cpc-02__back">
      <h3 class="cpc-02__name">Specifications</h3>
      <ul class="cpc-02__specs">
        <li><span>Upper</span><b>Recycled knit</b></li>
        <li><span>Drop</span><b>8&nbsp;mm</b></li>
        <li><span>Weight</span><b>272&nbsp;g</b></li>
        <li><span>Grip</span><b>Vibram&reg; Megagrip</b></li>
      </ul>
      <button class="cpc-02__cta" type="button">Add to Cart</button>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-02,
.cpc-02 *,
.cpc-02 *::before,
.cpc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-02 ::selection {
  background: oklch(0.62 0.17 150);
  color: #fff;
}

.cpc-02 {
  --accent: oklch(0.55 0.15 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #eef1ee;
  perspective: 1100px;
  border-radius: 20px;
}

.cpc-02 {
  width: 100%;
}

.cpc-02:focus-visible {
  outline: none;
}

.cpc-02__inner {
  position: relative;
  width: 300px;
  height: 420px;
  margin: 0 auto;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.2,.7,.2,1);
}

.cpc-02:hover .cpc-02__inner,
.cpc-02:focus-visible .cpc-02__inner {
  transform: rotateY(180deg);
}

.cpc-02__face {
  position: absolute;
  inset: 0;
  border-radius: 18px;
  overflow: hidden;
  backface-visibility: hidden;
  background: #fff;
  box-shadow: 0 18px 44px -22px rgba(16,24,40,.5);
}

.cpc-02__front {
  display: flex;
  flex-direction: column;
}

.cpc-02__media {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#e3ebe4,#d5e0d6),repeating-linear-gradient(-45deg,rgba(255,255,255,.5) 0 12px,transparent 12px 24px);
}

.cpc-02__media {
  background-image: url("https://images.unsplash.com/photo-1581244277943-fe4a9c777189?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-02__media span {
  display: none;
}

.cpc-02__meta {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: 16px 20px 4px;
}

.cpc-02__name {
  font-size: 18px;
  font-weight: 600;
  color: #101c14;
}

.cpc-02__price {
  font-size: 18px;
  font-weight: 700;
  color: var(--accent);
}

.cpc-02__hint {
  padding: 0 20px 18px;
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #9aab9c;
}

.cpc-02__back {
  transform: rotateY(180deg);
  background: #101c14;
  color: #e7f0e9;
  padding: 26px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.cpc-02__back .cpc-02__name {
  color: #fff;
}

.cpc-02__specs {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.cpc-02__specs li {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255,255,255,.1);
}

.cpc-02__specs span {
  color: #9db6a6;
}

.cpc-02__specs b {
  color: #fff;
  font-weight: 600;
}

.cpc-02__cta {
  height: 46px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
}

.cpc-02__cta:hover {
  background: color-mix(in oklch,var(--accent) 85%,#fff);
}

.cpc-02__cta:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 50%,#fff);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-02__inner {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — perspective + rotateY on :hover/:focus-visible, backface-visibility hides the reverse. */
```
