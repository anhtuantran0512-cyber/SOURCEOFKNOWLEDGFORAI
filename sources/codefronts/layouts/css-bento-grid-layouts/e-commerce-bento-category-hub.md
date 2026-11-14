---
source: "codefronts"
url: "https://codefronts.com/layouts/css-bento-grid-layouts/e-commerce-bento-category-hub/"
title: "E-commerce Bento Category Hub"
section: "layouts"
category: "css-bento-grid-layouts"
category_name: "CSS Bento Grid Layouts"
description: "The retail bento grid layout replacing boring row-and-column product listings: a New Arrivals image spanning two rows vertically, a horizontal 30%-off sale…"
has_js: "false"
---

Here's a working CSS Bento Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-commerce Bento Category Hub
Source: https://codefronts.com/layouts/css-bento-grid-layouts/e-commerce-bento-category-hub/

The retail bento grid layout replacing boring row-and-column product listings: a New Arrivals image spanning two rows vertically, a horizontal 30%-off sale banner with an animated gradient, and square blocks for trending product categories with image zoom hover states — category collections and current promotions bundled into one balanced view. Variant B is a minimal boutique take where hover reveals a sliding Shop link.
## HTML
```html
<div class="bgl-05-group">
<section class="bgl-05a" aria-labelledby="bgl-05a-h">
  <h2 class="bgl-05a__sr" id="bgl-05a-h">Shop by category</h2>
  <div class="bgl-05a__grid">
    <a class="bgl-05a__card bgl-05a__tall" href="#">
      <img src="https://picsum.photos/seed/bglnew/700/1000" alt="New arrivals — autumn outerwear collection" loading="lazy">
      <span class="bgl-05a__label"><em>Just in</em>New arrivals</span>
    </a>
    <a class="bgl-05a__card bgl-05a__banner" href="#">
      <span class="bgl-05a__off">30% OFF</span>
      <span class="bgl-05a__bannersub">End-of-season sale &mdash; ends Sunday</span>
    </a>
    <a class="bgl-05a__card" href="#"><img src="https://picsum.photos/seed/bglshoe/500/500" alt="Trending sneakers category" loading="lazy"><span class="bgl-05a__label">Sneakers</span></a>
    <a class="bgl-05a__card" href="#"><img src="https://picsum.photos/seed/bglbag/500/500" alt="Bags and accessories category" loading="lazy"><span class="bgl-05a__label">Bags</span></a>
    <a class="bgl-05a__card" href="#"><img src="https://picsum.photos/seed/bglwatch/500/500" alt="Watches category" loading="lazy"><span class="bgl-05a__label">Watches</span></a>
    <a class="bgl-05a__card" href="#"><img src="https://picsum.photos/seed/bglknit/500/500" alt="Knitwear category" loading="lazy"><span class="bgl-05a__label">Knitwear</span></a>
  </div>
</section>
<section class="bgl-05b" aria-labelledby="bgl-05b-h">
  <div class="bgl-05b__grid">
    <div class="bgl-05b__card bgl-05b__head">
      <h2 id="bgl-05b-h">The Edit</h2>
      <p>Curated pieces, small batches, honest materials. Free shipping over $80.</p>
    </div>
    <a class="bgl-05b__card bgl-05b__shot bgl-05b__tall" href="#">
      <img src="https://picsum.photos/seed/bglceramic/700/1000" alt="Ceramics collection — hand-thrown stoneware" loading="lazy">
      <span class="bgl-05b__tag">Ceramics<b>Shop &rarr;</b></span>
    </a>
    <a class="bgl-05b__card bgl-05b__shot" href="#"><img src="https://picsum.photos/seed/bgllinen/600/450" alt="Linen goods collection" loading="lazy"><span class="bgl-05b__tag">Linen<b>Shop &rarr;</b></span></a>
    <a class="bgl-05b__card bgl-05b__shot" href="#"><img src="https://picsum.photos/seed/bglcandle/600/450" alt="Candles and home fragrance collection" loading="lazy"><span class="bgl-05b__tag">Candles<b>Shop &rarr;</b></span></a>
    <a class="bgl-05b__card bgl-05b__promo" href="#"><span>Members get early access to every drop</span><b>Join &rarr;</b></a>
  </div>
</section>
</div>
```
## CSS
```css
.bgl-05-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.bgl-05-group > section {
  flex: 1 1 480px;
  min-width: 320px;
}

.bgl-05a,
.bgl-05a *,
.bgl-05a *::before,
.bgl-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-05a {
  width: 100%;
  min-height: 100vh;
  --sale1: oklch(0.62 0.22 25);
  --sale2: oklch(0.55 0.24 300);
  --gap: 16px;
  --radius: 18px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #101014;
  color: #fff;
}

.bgl-05a__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bgl-05a__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(170px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-05a__card {
  position: relative;
  overflow: hidden;
  grid-column: span 3;
  display: flex;
  align-items: flex-end;
  border-radius: var(--radius);
  text-decoration: none;
  color: #fff;
  background: #1a1a22;
}

.bgl-05a__card img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .6s cubic-bezier(.2,.9,.2,1);
}

.bgl-05a__card:hover img,
.bgl-05a__card:focus-visible img {
  transform: scale(1.07);
}

.bgl-05a__card:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.bgl-05a__label {
  position: relative;
  width: 100%;
  padding: 18px;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.01em;
  background: linear-gradient(transparent,rgba(0,0,0,.62));
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.bgl-05a__label em {
  font-style: normal;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,255,255,.75);
}

.bgl-05a__tall {
  grid-column: span 4;
  grid-row: span 2;
}

.bgl-05a__tall .bgl-05a__label {
  font-size: 22px;
  padding: 24px;
}

.bgl-05a__banner {
  grid-column: span 8;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: 6px;
  padding: 28px;
  background: linear-gradient(100deg,var(--sale1),var(--sale2),var(--sale1)) 0 0/200% 100%;
  animation: bgl-05a-sheen 7s linear infinite;
}

.bgl-05a__off {
  font-size: clamp(36px,5cqw,58px);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1;
}

.bgl-05a__bannersub {
  font-size: 15px;
  font-weight: 600;
  color: rgba(255,255,255,.85);
}

.bgl-05a__banner:hover .bgl-05a__off {
  text-decoration: underline;
  text-decoration-thickness: 4px;
  text-underline-offset: 8px;
}

@keyframes bgl-05a-sheen {
  to {
    background-position: 200% 0;
  }
}

@container (max-width: 880px) {
  .bgl-05a__tall {
    grid-column: span 6;
  }

  .bgl-05a__banner {
    grid-column: span 6;
  }

  .bgl-05a__card {
    grid-column: span 6;
  }

  .bgl-05a__tall {
    grid-column: span 6;
  }
}

@container (max-width: 560px) {
  .bgl-05a__card,
    .bgl-05a__tall,
    .bgl-05a__banner {
    grid-column: span 12;
  }

  .bgl-05a__tall {
    min-height: 340px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-05a__card img {
    transition: none;
  }

  .bgl-05a__card:hover img {
    transform: none;
  }

  .bgl-05a__banner {
    animation: none;
  }
}

.bgl-05b,
.bgl-05b *,
.bgl-05b *::before,
.bgl-05b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-05b {
  width: 100%;
  min-height: 100vh;
  --ink: #26221c;
  --gap: 14px;
  --radius: 6px;
  container-type: inline-size;
  font-family: Georgia,'Times New Roman',serif;
  padding: 48px 24px;
  background: #faf8f4;
  color: var(--ink);
}

.bgl-05b__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(160px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-05b__card {
  grid-column: span 4;
  border-radius: var(--radius);
  overflow: hidden;
  text-decoration: none;
  color: var(--ink);
}

.bgl-05b__head {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  padding: 28px;
  border: 1px solid rgba(38,34,28,.18);
}

.bgl-05b__head h2 {
  font-size: clamp(30px,3.6cqw,42px);
  font-weight: 400;
  font-style: italic;
  letter-spacing: -.01em;
}

.bgl-05b__head p {
  font-size: 14.5px;
  line-height: 1.65;
  color: rgba(38,34,28,.65);
  text-wrap: pretty;
}

.bgl-05b__shot {
  position: relative;
  display: flex;
  align-items: flex-end;
}

.bgl-05b__shot img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .7s cubic-bezier(.2,.9,.2,1),filter .7s;
}

.bgl-05b__shot:hover img,
.bgl-05b__shot:focus-visible img {
  transform: scale(1.06);
  filter: brightness(.92);
}

.bgl-05b__shot:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.bgl-05b__tag {
  position: relative;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  width: 100%;
  padding: 16px 18px;
  font-size: 17px;
  font-style: italic;
  background: linear-gradient(transparent,rgba(38,34,28,.55));
  color: #faf8f4;
  overflow: hidden;
}

.bgl-05b__tag b {
  font-style: normal;
  font-weight: 400;
  font-size: 13px;
  letter-spacing: .06em;
  transform: translateY(110%);
  opacity: 0;
  transition: transform .35s,opacity .35s;
}

.bgl-05b__shot:hover .bgl-05b__tag b,
.bgl-05b__shot:focus-visible .bgl-05b__tag b {
  transform: translateY(0);
  opacity: 1;
}

.bgl-05b__tall {
  grid-row: span 2;
}

.bgl-05b__promo {
  grid-column: span 8;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 24px 28px;
  background: var(--ink);
  color: #faf8f4;
  font-size: clamp(17px,2cqw,21px);
  font-style: italic;
}

.bgl-05b__promo b {
  font-style: normal;
  font-size: 13px;
  letter-spacing: .06em;
  white-space: nowrap;
  border-bottom: 1px solid #faf8f4;
  padding-bottom: 2px;
  transition: transform .3s;
}

.bgl-05b__promo:hover b {
  transform: translateX(4px);
}

.bgl-05b__promo:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

@container (max-width: 880px) {
  .bgl-05b__card {
    grid-column: span 6;
  }

  .bgl-05b__promo {
    grid-column: span 12;
  }
}

@container (max-width: 560px) {
  .bgl-05b__card,
    .bgl-05b__promo,
    .bgl-05b__tall {
    grid-column: span 12;
  }

  .bgl-05b__tall {
    min-height: 320px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-05b__shot img,
    .bgl-05b__tag b,
    .bgl-05b__promo b {
    transition: none;
  }

  .bgl-05b__tag b {
    transform: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — anchor cards with object-fit:cover images, compositor-only zoom on hover, and a 200%-wide gradient banner sheened by background-position keyframes. */

/* No JavaScript — serif boutique grid; the Shop → affordance slides up from translateY(110%) on hover and stays visible under keyboard focus. */
```
