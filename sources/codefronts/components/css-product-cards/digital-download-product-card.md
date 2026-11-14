---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/digital-download-product-card/"
title: "Digital-Download Product Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A clean card for software, e-books and templates: a file-type glyph, rating stars, file meta (format, size) and a prominent download button with a subtle…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Digital-Download Product Card
Source: https://codefronts.com/components/css-product-cards/digital-download-product-card/

A clean card for software, e-books and templates: a file-type glyph, rating stars, file meta (format, size) and a prominent download button with a subtle download-arrow micro-animation. The digital-goods layout template and SaaS sellers search for.
## HTML
```html
<article class="cpc-15">
  <div class="cpc-15__card">
    <div class="cpc-15__badge" aria-hidden="true">.ZIP</div>
    <div class="cpc-15__body">
      <h3 class="cpc-15__name">Nimbus UI Kit — 240 Components</h3>
      <p class="cpc-15__rating" aria-label="Rated 4.9 out of 5 from 860 reviews"><span aria-hidden="true">★★★★★</span> 4.9 · 860 reviews</p>
      <ul class="cpc-15__meta"><li>Figma + Sketch</li><li>48&nbsp;MB</li><li>v3.2</li></ul>
      <div class="cpc-15__foot">
        <p class="cpc-15__price">$39</p>
        <a class="cpc-15__dl" href="#" download>
          <span class="cpc-15__arw" aria-hidden="true">↓</span> Download
        </a>
      </div>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-15,
.cpc-15 *,
.cpc-15 *::before,
.cpc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-15 ::selection {
  background: oklch(0.6 0.15 285);
  color: #fff;
}

.cpc-15 {
  --accent: oklch(0.52 0.16 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f2f1f7;
}

.cpc-15__card {
  width: 320px;
  border-radius: 18px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 16px 40px -22px rgba(30,20,60,.4);
}

.cpc-15__badge {
  aspect-ratio: 16/9;
  display: flex;
  align-items: center;
  justify-content: center;
  font: 800 40px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .06em;
  color: #fff;
  background: linear-gradient(135deg,oklch(0.6 0.16 285),oklch(0.55 0.17 255));
  text-shadow: 0 2px 12px rgba(0,0,0,.25);
}

.cpc-15__body {
  padding: 20px 22px 22px;
}

.cpc-15__name {
  font-size: 18px;
  font-weight: 600;
  color: #1a1330;
  line-height: 1.35;
}

.cpc-15__rating {
  margin-top: 10px;
  font-size: 13px;
  color: #6b6480;
}

.cpc-15__rating span {
  color: oklch(0.78 0.15 80);
  letter-spacing: .05em;
}

.cpc-15__meta {
  list-style: none;
  margin-top: 14px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.cpc-15__meta li {
  padding: 5px 10px;
  border-radius: 8px;
  background: #f2f0f8;
  color: #544c6e;
  font-size: 12px;
  font-weight: 500;
}

.cpc-15__foot {
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.cpc-15__price {
  font-size: 22px;
  font-weight: 800;
  color: #1a1330;
}

.cpc-15__dl {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 46px;
  padding: 0 22px;
  border-radius: 12px;
  text-decoration: none;
  background: var(--accent);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  box-shadow: 0 10px 24px -12px var(--accent);
}

.cpc-15__dl:hover {
  background: color-mix(in oklch,var(--accent) 88%,#000);
}

.cpc-15__dl:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 45%,#fff);
  outline-offset: 2px;
}

.cpc-15__arw {
  display: inline-block;
  transition: transform .3s;
}

.cpc-15__dl:hover .cpc-15__arw {
  transform: translateY(3px);
}

@media (prefers-reduced-motion: reduce) {
  .cpc-15__arw {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a file badge, star rating and a download-arrow micro-animation. */
```
