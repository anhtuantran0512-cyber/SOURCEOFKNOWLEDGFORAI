---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-masonry-ecommerce-product-listing-grid/"
title: "CSS Masonry Ecommerce Product Listing Grid"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "A category page that packs mixed-ratio product tiles — square accessories, 3:4 apparel, one double-height editorial feature — with grid-auto-flow: dense…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Ecommerce Product Listing Grid
Source: https://codefronts.com/layouts/css-masonry-layouts/css-masonry-ecommerce-product-listing-grid/

A category page that packs mixed-ratio product tiles — square accessories, 3:4 apparel, one double-height editorial feature — with grid-auto-flow: dense backfilling every hole. Sale and New badges, star ratings, strike-through compare-at pricing, and a Quick add bar that slides up on hover AND :focus-within, because a keyboard shopper is still a shopper. Includes the honest talk about when dense packing is wrong for commerce.
## HTML
```html
<section class="msn-05" aria-label="CSS masonry ecommerce product grid demo">
  <div class="msn-05__stage" tabindex="0">
    <header class="msn-05__head">
      <div><h2>New in · Studio</h2><p>128 products</p></div>
      <div class="msn-05__tools"><a href="#filter">Filter</a><a href="#sort">Sort: Featured</a></div>
    </header>
    <div class="msn-05__grid">
      <article class="msn-05__tile" style="--r:96%"><a class="msn-05__media" href="#pd-1" style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=800&auto=format&fit=crop');--a:oklch(0.85 0.03 90);--b:oklch(0.65 0.05 70)"><span class="msn-05__flag msn-05__flag--sale">−30%</span></a><button class="msn-05__wish" type="button" aria-label="Save Field Watch to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-1">Field Watch 36</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.8 out of 5, 214 reviews</span><p class="msn-05__price"><strong>$149</strong><s>$212</s></p></div><a class="msn-05__quick" href="#add-1">Quick add</a></article>
      <article class="msn-05__tile msn-05__tile--feature" style="--r:98%"><a class="msn-05__media" href="#pd-2" style="--ar:auto;--img:url('https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.65 0.19 25);--b:oklch(0.4 0.16 15)"><span class="msn-05__flag msn-05__flag--new">The drop</span></a><button class="msn-05__wish" type="button" aria-label="Save Velocity Runner to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-2">Velocity Runner — Ember</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.9 out of 5, 1,032 reviews</span><p class="msn-05__price"><strong>$180</strong></p></div><a class="msn-05__quick" href="#add-2">Quick add</a></article>
      <article class="msn-05__tile" style="--r:88%"><a class="msn-05__media" href="#pd-3" style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1591047139829-d91aecb6caea?q=80&w=800&auto=format&fit=crop');--a:oklch(0.6 0.05 250);--b:oklch(0.38 0.06 270)"></a><button class="msn-05__wish" type="button" aria-label="Save Shell Jacket to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-3">Shell Jacket — Slate</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.4 out of 5, 156 reviews</span><p class="msn-05__price"><strong>$248</strong></p></div><a class="msn-05__quick" href="#add-3">Quick add</a></article>
      <article class="msn-05__tile" style="--r:92%"><a class="msn-05__media" href="#pd-4" style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1572635196237-14b3f281503f?q=80&w=800&auto=format&fit=crop');--a:oklch(0.82 0.06 80);--b:oklch(0.6 0.09 60)"><span class="msn-05__flag msn-05__flag--sale">−15%</span></a><button class="msn-05__wish" type="button" aria-label="Save Coast Sunglasses to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-4">Coast Sunglasses</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.6 out of 5, 89 reviews</span><p class="msn-05__price"><strong>$76</strong><s>$90</s></p></div><a class="msn-05__quick" href="#add-4">Quick add</a></article>
      <article class="msn-05__tile" style="--r:90%"><a class="msn-05__media" href="#pd-5" style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1523381210434-271e8be1f52b?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.04 140);--b:oklch(0.6 0.06 120)"></a><button class="msn-05__wish" type="button" aria-label="Save Organic Tee to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-5">Organic Tee 3-Pack</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.5 out of 5, 412 reviews</span><p class="msn-05__price"><strong>$58</strong></p></div><a class="msn-05__quick" href="#add-5">Quick add</a></article>
      <article class="msn-05__tile" style="--r:94%"><a class="msn-05__media" href="#pd-6" style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=800&auto=format&fit=crop');--a:oklch(0.75 0.05 250);--b:oklch(0.52 0.07 270)"><span class="msn-05__flag msn-05__flag--new">New</span></a><button class="msn-05__wish" type="button" aria-label="Save Commuter Pack to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-6">Commuter Pack 18L</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.7 out of 5, 267 reviews</span><p class="msn-05__price"><strong>$132</strong></p></div><a class="msn-05__quick" href="#add-6">Quick add</a></article>
      <article class="msn-05__tile" style="--r:86%"><a class="msn-05__media" href="#pd-7" style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1585386959984-a4155224a1ad?q=80&w=800&auto=format&fit=crop');--a:oklch(0.85 0.05 340);--b:oklch(0.65 0.08 320)"></a><button class="msn-05__wish" type="button" aria-label="Save Eau de Cèdre to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-7">Eau de Cèdre 50ml</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.3 out of 5, 74 reviews</span><p class="msn-05__price"><strong>$95</strong></p></div><a class="msn-05__quick" href="#add-7">Quick add</a></article>
      <article class="msn-05__tile" style="--r:97%"><a class="msn-05__media" href="#pd-8" style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=800&auto=format&fit=crop');--a:oklch(0.7 0.06 260);--b:oklch(0.45 0.08 280)"><span class="msn-05__flag msn-05__flag--sale">−20%</span></a><button class="msn-05__wish" type="button" aria-label="Save Pulse Band to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-8">Pulse Band 2</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.9 out of 5, 1,845 reviews</span><p class="msn-05__price"><strong>$199</strong><s>$249</s></p></div><a class="msn-05__quick" href="#add-8">Quick add</a></article>
      <article class="msn-05__tile" style="--r:91%"><a class="msn-05__media" href="#pd-9" style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?q=80&w=800&auto=format&fit=crop');--a:oklch(0.78 0.07 60);--b:oklch(0.55 0.1 40)"></a><button class="msn-05__wish" type="button" aria-label="Save Court Classic to wishlist">♡</button><div class="msn-05__info"><h3><a href="#pd-9">Court Classic — Bone</a></h3><p class="msn-05__stars" aria-hidden="true"></p><span class="msn-05__sr">Rated 4.6 out of 5, 523 reviews</span><p class="msn-05__price"><strong>$110</strong></p></div><a class="msn-05__quick" href="#add-9">Quick add</a></article>
    </div>
  </div>
</section>
```
## CSS
```css
.msn-05,
.msn-05 *,
.msn-05 *::before,
.msn-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-05 {
  --bg: oklch(0.98 0.003 90);
  --card: oklch(1 0 0);
  --ink: oklch(0.22 0.01 60);
  --mut: oklch(0.54 0.012 60);
  --line: oklch(0.9 0.006 90);
  --acc: oklch(0.55 0.19 25);
  --star: oklch(0.72 0.15 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-05__stage {
  width: 100%;
  container: msn05/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-05__head {
  position: sticky;
  top: 0;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 15px clamp(16px,3cqi,28px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-05__head h2 {
  font-size: clamp(17px,2.4cqi,22px);
  letter-spacing: -.02em;
}

.msn-05__head p {
  font-size: 12px;
  color: var(--mut);
  margin-top: 1px;
}

.msn-05__tools {
  display: flex;
  gap: 8px;
}

.msn-05__tools a {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 14px;
  border: 1px solid var(--line);
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 600;
  text-decoration: none;
  color: var(--ink);
  background: var(--card);
  transition: border-color .2s,background .2s;
}

.msn-05__tools a:hover,
.msn-05__tools a:focus-visible {
  border-color: oklch(0.75 0.01 60);
  background: oklch(0.96 0.004 90);
}

.msn-05__tools a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.msn-05__grid {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fill,minmax(min(200px,100%),1fr));
  grid-auto-flow: row dense;
  padding: clamp(16px,3cqi,28px);
}

.msn-05__tile {
  position: relative;
  display: flex;
  flex-direction: column;
  border-radius: 16px;
  background: var(--card);
  border: 1px solid var(--line);
  overflow: clip;
  transition: box-shadow .25s,translate .25s;
}

.msn-05__tile:hover,
.msn-05__tile:focus-within {
  translate: 0 -3px;
  box-shadow: 0 14px 30px -16px oklch(0.35 0.02 60/.4);
}

.msn-05__tile--feature {
  grid-row: span 2;
  grid-column: span 2;
}

.msn-05__media {
  position: relative;
  display: block;
  aspect-ratio: var(--ar,1/1);
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  transition: opacity .3s;
}

.msn-05__tile--feature .msn-05__media {
  flex: 1;
  aspect-ratio: auto;
  min-height: 0;
}

.msn-05__media:hover,
.msn-05__media:focus-visible {
  opacity: .93;
}

.msn-05__media:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: -3px;
}

.msn-05__flag {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .04em;
  padding: 5px 10px;
  border-radius: 99px;
  color: oklch(0.99 0 0);
}

.msn-05__flag--sale {
  background: var(--acc);
}

.msn-05__flag--new {
  background: var(--ink);
}

.msn-05__wish {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 1;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid var(--line);
  background: color-mix(in oklch,var(--card) 88%,transparent);
  backdrop-filter: blur(4px);
  font-size: 17px;
  line-height: 1;
  color: var(--ink);
  cursor: pointer;
  transition: background .2s,color .2s,scale .15s;
}

.msn-05__wish:hover,
.msn-05__wish:focus-visible {
  background: var(--card);
  color: var(--acc);
  scale: 1.06;
}

.msn-05__wish:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.msn-05__wish[aria-pressed="true"] {
  color: var(--acc);
}

.msn-05__info {
  display: grid;
  gap: 5px;
  padding: 13px 14px 52px;
  justify-items: start;
}

.msn-05__info h3 {
  font-size: 13.5px;
  letter-spacing: -.01em;
}

.msn-05__info h3 a {
  color: inherit;
  text-decoration: none;
}

.msn-05__info h3 a:hover,
.msn-05__info h3 a:focus-visible {
  color: var(--acc);
}

.msn-05__info h3 a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 4px;
}

.msn-05__stars {
  --pct: var(--r,90%);
  font-size: 12px;
  letter-spacing: 2px;
  line-height: 1;
}

.msn-05__stars::before {
  content: "★★★★★";
  background: linear-gradient(90deg,var(--star) var(--pct),oklch(0.87 0.008 90) var(--pct));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.msn-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.msn-05__price {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-size: 14px;
}

.msn-05__price strong {
  font-weight: 800;
}

.msn-05__price s {
  font-size: 12px;
  color: var(--mut);
}

.msn-05__quick {
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 10px;
  display: grid;
  place-items: center;
  min-height: 40px;
  border-radius: 11px;
  font-size: 12.5px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.99 0 0);
  background: var(--ink);
  translate: 0 calc(100% + 12px);
  transition: translate .28s cubic-bezier(.2,.7,.2,1),background .2s;
}

.msn-05__tile:hover .msn-05__quick,
.msn-05__tile:focus-within .msn-05__quick {
  translate: 0 0;
}

.msn-05__quick:hover {
  background: var(--acc);
}

.msn-05__quick:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@media (hover: none) {
  .msn-05__quick {
    translate: 0 0;
  }
}

@container msn05 (width < 520px) {
  .msn-05__grid {
    grid-template-columns: repeat(2,1fr);
    gap: 9px;
  }

  .msn-05__tile--feature {
    grid-column: span 2;
    grid-row: span 1;
  }

  .msn-05__tile--feature .msn-05__media {
    aspect-ratio: 16/9;
    flex: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-05 * {
    transition-duration: .01ms !important;
  }
}
```
