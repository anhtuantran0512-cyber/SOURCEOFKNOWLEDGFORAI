---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/e-commerce-product-showcase-card-slider/"
title: "E-Commerce Product Showcase Card Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "E-commerce product image slider in pure CSS — scroll-snapping product cards with hover-to-zoom imagery, price badges, and a jump-to-product thumbnail strip."
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Product Showcase Card Slider
Source: https://codefronts.com/components/css-image-slider/e-commerce-product-showcase-card-slider/

E-commerce product image slider in pure CSS — scroll-snapping product cards with hover-to-zoom imagery, price badges, and a jump-to-product thumbnail strip. Drops into Shopify Dawn theme, WooCommerce Storefront, BigCommerce Cornerstone, and Stripe Checkout product cards without shipping Swiper (145KB) or Slick (85KB); container-query responsive so it adapts to whatever column it lands in.
## HTML
```html
<div class="cis-04">
  <div class="cis-04__rail">
    <article class="cis-04__card" id="cis-04-p1">
      <div class="cis-04__media"><img src="https://picsum.photos/seed/cis04a/700/700" alt="Matte ceramic pour-over set">
        <span class="cis-04__badge">$48</span></div>
      <div class="cis-04__body"><span class="cis-04__ey">Kitchen</span>
        <h3 class="cis-04__name">Nori Pour-Over Set</h3>
        <p class="cis-04__meta">Matte stoneware · 3 colours</p>
        <button class="cis-04__cta" type="button">Add to bag</button></div>
    </article>
    <article class="cis-04__card" id="cis-04-p2">
      <div class="cis-04__media"><img src="https://picsum.photos/seed/cis04b/700/700" alt="Wool throw blanket folded">
        <span class="cis-04__badge">$120</span></div>
      <div class="cis-04__body"><span class="cis-04__ey">Home</span>
        <h3 class="cis-04__name">Loom Wool Throw</h3>
        <p class="cis-04__meta">Undyed merino · 130×180cm</p>
        <button class="cis-04__cta" type="button">Add to bag</button></div>
    </article>
    <article class="cis-04__card" id="cis-04-p3">
      <div class="cis-04__media"><img src="https://picsum.photos/seed/cis04c/700/700" alt="Leather weekender bag">
        <span class="cis-04__badge">$260</span></div>
      <div class="cis-04__body"><span class="cis-04__ey">Travel</span>
        <h3 class="cis-04__name">Field Weekender</h3>
        <p class="cis-04__meta">Vegetable-tanned · brass hardware</p>
        <button class="cis-04__cta" type="button">Add to bag</button></div>
    </article>
    <article class="cis-04__card" id="cis-04-p4">
      <div class="cis-04__media"><img src="https://picsum.photos/seed/cis04d/700/700" alt="Desk lamp with linen shade">
        <span class="cis-04__badge">$95</span></div>
      <div class="cis-04__body"><span class="cis-04__ey">Lighting</span>
        <h3 class="cis-04__name">Arc Task Lamp</h3>
        <p class="cis-04__meta">Dimmable · linen shade</p>
        <button class="cis-04__cta" type="button">Add to bag</button></div>
    </article>
  </div>
  <nav class="cis-04__thumbs" aria-label="Jump to product">
    <a href="#cis-04-p1" style="--t:url(https://picsum.photos/seed/cis04a/160/160)" aria-label="Nori Pour-Over Set"></a>
    <a href="#cis-04-p2" style="--t:url(https://picsum.photos/seed/cis04b/160/160)" aria-label="Loom Wool Throw"></a>
    <a href="#cis-04-p3" style="--t:url(https://picsum.photos/seed/cis04c/160/160)" aria-label="Field Weekender"></a>
    <a href="#cis-04-p4" style="--t:url(https://picsum.photos/seed/cis04d/160/160)" aria-label="Arc Task Lamp"></a>
  </nav>
</div>
```
## CSS
```css
.cis-04,
.cis-04 *,
.cis-04 *::before,
.cis-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-04 ::selection {
  background: oklch(0.72 0.16 25);
  color: #fff;
}

.cis-04 {
  --accent: oklch(0.66 0.17 24);
  --card: 300px;
  --bg: #0d0d0f;
  --surface: #16161a;
  --line: #26262c;
  --text: #f2f2f4;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 44px 0;
  background: radial-gradient(130% 120% at 50% 0%,#17171b,#0a0a0c);
}

.cis-04__rail {
  display: flex;
  gap: 20px;
  width: min(900px,96vw);
  padding: 8px max(18px,calc(50% - 460px));
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
}

.cis-04__rail::-webkit-scrollbar {
  display: none;
}

.cis-04__card {
  container-type: inline-size;
  scroll-snap-align: center;
  flex: 0 0 var(--card);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  overflow: hidden;
  scroll-margin: 0 12px;
  transition: border-color .3s,box-shadow .3s,transform .3s;
}

.cis-04__card:target {
  border-color: var(--accent);
  box-shadow: 0 0 0 1px var(--accent),0 30px 60px -30px color-mix(in oklab,var(--accent) 50%,transparent);
}

.cis-04__media {
  position: relative;
  aspect-ratio: 1;
  overflow: hidden;
}

.cis-04__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform .5s cubic-bezier(.2,.7,.2,1);
}

.cis-04__card:hover .cis-04__media img {
  transform: scale(1.09);
}

.cis-04__badge {
  position: absolute;
  top: 12px;
  right: 12px;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  background: color-mix(in oklab,var(--accent) 82%,#000);
  border: 1px solid color-mix(in oklab,var(--accent) 60%,#fff);
  box-shadow: 0 6px 18px -6px rgba(0,0,0,.6);
}

.cis-04__body {
  padding: 16px 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.cis-04__ey {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--accent) 70%,#fff);
}

.cis-04__name {
  font-size: 18px;
  font-weight: 700;
}

.cis-04__meta {
  font-size: 13px;
  color: #9a9aa4;
}

.cis-04__cta {
  margin-top: 8px;
  padding: 11px 14px;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  color: #0a0a0c;
  background: var(--text);
  transition: background .2s,transform .1s;
}

.cis-04__cta:hover {
  background: var(--accent);
  color: #fff;
}

.cis-04__cta:active {
  transform: translateY(1px);
}
/* container query: widen a card and it lays out side-by-side */

@container (min-width: 40rem) {
  .cis-04__card {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }

  .cis-04__body {
    justify-content: center;
  }
}

.cis-04__thumbs {
  display: flex;
  gap: 10px;
}

.cis-04__thumbs a {
  width: 46px;
  height: 46px;
  border-radius: 12px;
  background-image: var(--t);
  background-size: cover;
  background-position: center;
  opacity: .5;
  border: 2px solid transparent;
  transition: opacity .25s,border-color .25s,transform .2s;
}

.cis-04__thumbs a:hover {
  opacity: 1;
  transform: translateY(-2px);
}

.cis-04__thumbs a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cis-04__rail {
    scroll-behavior: auto;
  }

  .cis-04__media img,
    .cis-04__card,
    .cis-04__thumbs a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — thumbnail navigation uses anchor links to card ids,
   scrolled smoothly by the snap rail; hover-zoom and active ring are pure CSS. */
```
