---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-mosaic-zoom-gallery/"
title: "CSS Mosaic Zoom Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A crisp mosaic grid where hovering a tile zooms its photo cleanly inside the frame — the image scales, the tile doesn't, so nothing overlaps its neighbours."
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Mosaic Zoom Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-mosaic-zoom-gallery/

A crisp mosaic grid where hovering a tile zooms its photo cleanly inside the frame — the image scales, the tile doesn't, so nothing overlaps its neighbours. The catalog zoom-on-hover micro-interaction, done the performant way.
## HTML
```html
<section class="gl-10" aria-label="Mosaic zoom gallery">
  <div class="gl-10__grid">
    <figure class="gl-10__tile gl-10__tile--big"><img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&h=800&auto=format&fit=crop" alt="Golden hour over rolling hills" loading="lazy" decoding="async"><figcaption>Hills</figcaption></figure>
    <figure class="gl-10__tile"><img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=400&h=400&auto=format&fit=crop" alt="Macro of a flower" loading="lazy" decoding="async"><figcaption>Bloom</figcaption></figure>
    <figure class="gl-10__tile"><img src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?q=80&w=400&h=400&auto=format&fit=crop" alt="Wild deer in a field" loading="lazy" decoding="async"><figcaption>Wildlife</figcaption></figure>
    <figure class="gl-10__tile"><img src="https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=400&h=400&auto=format&fit=crop" alt="Backlit green leaf" loading="lazy" decoding="async"><figcaption>Detail</figcaption></figure>
    <figure class="gl-10__tile"><img src="https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=400&h=400&auto=format&fit=crop" alt="Forest waterfall" loading="lazy" decoding="async"><figcaption>Falls</figcaption></figure>
    <figure class="gl-10__tile gl-10__tile--wide"><img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=800&h=400&auto=format&fit=crop" alt="Valley panorama" loading="lazy" decoding="async"><figcaption>Valley</figcaption></figure>
    <figure class="gl-10__tile"><img src="https://images.unsplash.com/photo-1589003077984-894e133dabab?q=80&w=400&h=400&auto=format&fit=crop" alt="Dramatic cloudscape" loading="lazy" decoding="async"><figcaption>Sky</figcaption></figure>
  </div>
</section>
```
## CSS
```css
.gl-10,
.gl-10 *,
.gl-10 *::before,
.gl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-10 ::selection {
  background: oklch(0.6 0.15 145);
  color: #fff;
}

.gl-10 {
  --accent: oklch(0.58 0.15 145);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f2f4f1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-10__grid {
  width: min(820px,100%);
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: 1fr;
  grid-auto-flow: dense;
}

.gl-10__tile {
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  background: #dfe4de;
  aspect-ratio: 1/1;
}

.gl-10__tile--big {
  grid-column: span 2;
  grid-row: span 2;
  aspect-ratio: auto;
}

.gl-10__tile--wide {
  grid-column: span 2;
  aspect-ratio: auto;
}

.gl-10__tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1);
  transition: transform .55s cubic-bezier(.2,.7,.2,1);
}

.gl-10__tile:hover img,
.gl-10__tile:focus-within img {
  transform: scale(1.16);
}

.gl-10__tile figcaption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 22px 12px 10px;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .04em;
  background: linear-gradient(0deg,rgba(8,20,12,.75),transparent);
  opacity: 0;
  transition: opacity .35s;
}

.gl-10__tile:hover figcaption,
.gl-10__tile:focus-within figcaption {
  opacity: 1;
}

@media (max-width: 600px) {
  .gl-10__grid {
    grid-template-columns: repeat(2,1fr);
  }

  .gl-10__tile--big,
    .gl-10__tile--wide {
    grid-column: span 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-10__tile img,
    .gl-10__tile figcaption {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the image scales inside an overflow:hidden tile, so the zoom is contained. */
```
