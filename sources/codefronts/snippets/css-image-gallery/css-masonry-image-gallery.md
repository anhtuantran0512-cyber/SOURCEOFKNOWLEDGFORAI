---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-masonry-image-gallery/"
title: "CSS Masonry Image Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "The Pinterest classic: staggered vertical columns where images of different heights pack tightly together with no awkward gaps, and no JavaScript layout…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Image Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-masonry-image-gallery/

The Pinterest classic: staggered vertical columns where images of different heights pack tightly together with no awkward gaps, and no JavaScript layout library. The single most-searched gallery pattern in Tier-1 markets.
## HTML
```html
<section class="gl-01" aria-label="Masonry photo gallery">
  <div class="gl-01__grid">
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=500&h=700&auto=format&fit=crop" alt="Snow-capped mountain ridge at dawn" loading="lazy" decoding="async" width="500" height="700"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=500&h=400&auto=format&fit=crop" alt="Misty pine forest canopy" loading="lazy" decoding="async" width="500" height="400"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=500&h=560&auto=format&fit=crop" alt="Still alpine lake reflecting the sky" loading="lazy" decoding="async" width="500" height="560"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=500&h=620&auto=format&fit=crop" alt="Rolling desert sand dunes" loading="lazy" decoding="async" width="500" height="620"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=500&h=380&auto=format&fit=crop" alt="Turquoise ocean waves from above" loading="lazy" decoding="async" width="500" height="380"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=500&h=680&auto=format&fit=crop" alt="Tall waterfall in a green gorge" loading="lazy" decoding="async" width="500" height="680"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1509631179647-0177331693ae?q=80&w=500&h=460&auto=format&fit=crop" alt="City skyline at blue hour" loading="lazy" decoding="async" width="500" height="460"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?q=80&w=500&h=540&auto=format&fit=crop" alt="Autumn trees in gold and red" loading="lazy" decoding="async" width="500" height="540"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1449157291145-7efd050a4d0e?q=80&w=500&h=420&auto=format&fit=crop" alt="Layered red canyon walls" loading="lazy" decoding="async" width="500" height="420"></figure>
    <figure class="gl-01__item"><img src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?q=80&w=500&h=600&auto=format&fit=crop" alt="Green aurora over a snowy valley" loading="lazy" decoding="async" width="500" height="600"></figure>
  </div>
</section>
```
## CSS
```css
.gl-01,
.gl-01 *,
.gl-01 *::before,
.gl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-01 ::selection {
  background: oklch(0.6 0.16 250);
  color: #fff;
}

.gl-01 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f5f7;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.gl-01__grid {
  width: min(920px,100%);
  columns: 4;
  column-gap: 14px;
}

.gl-01__item {
  break-inside: avoid;
  margin: 0 0 14px;
  border-radius: 12px;
  overflow: hidden;
  background: #e7eaef;
  box-shadow: 0 8px 22px -16px rgba(16,24,40,.6);
  transition: box-shadow .3s;
}

.gl-01__item:hover {
  box-shadow: 0 16px 34px -18px rgba(16,24,40,.55);
}

.gl-01__item img {
  display: block;
  width: 100%;
  height: auto;
  transform: scale(1);
  transition: transform .5s cubic-bezier(.2,.7,.2,1);
}

.gl-01__item:hover img,
.gl-01__item:focus-within img {
  transform: scale(1.06);
}

.gl-01__item a:focus-visible {
  outline: 3px solid oklch(0.6 0.16 250);
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .gl-01__grid {
    columns: 3;
  }
}

@media (max-width: 560px) {
  .gl-01__grid {
    columns: 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-01__item,
    .gl-01__item img {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS multi-column + break-inside:avoid produce the masonry packing. */
```
