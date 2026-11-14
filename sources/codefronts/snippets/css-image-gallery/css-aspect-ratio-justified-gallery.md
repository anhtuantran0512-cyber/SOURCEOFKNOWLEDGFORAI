---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-aspect-ratio-justified-gallery/"
title: "CSS Aspect-Ratio Justified Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "The Google-Images / Flickr look: fluid rows where every photo keeps its native aspect ratio (no cropping) yet each row stretches flush to both edges."
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect-Ratio Justified Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-aspect-ratio-justified-gallery/

The Google-Images / Flickr look: fluid rows where every photo keeps its native aspect ratio (no cropping) yet each row stretches flush to both edges. Achieved with flex-grow weighting and aspect-ratio — no JS measuring.
## HTML
```html
<section class="gl-05" aria-label="Justified aspect-ratio gallery">
  <div class="gl-05__gallery">
    <div class="gl-05__row">
      <figure class="gl-05__item" style="--r:1.5"><img src="https://images.unsplash.com/photo-1618773928121-c32242e63f39?q=80&w=600&h=400&auto=format&fit=crop" alt="Wide sandy beach" loading="lazy" decoding="async"></figure>
      <figure class="gl-05__item" style="--r:0.75"><img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=450&h=600&auto=format&fit=crop" alt="Coastal lighthouse" loading="lazy" decoding="async"></figure>
      <figure class="gl-05__item" style="--r:1.33"><img src="https://images.unsplash.com/photo-1475721027785-f74eccf877e2?q=80&w=600&h=450&auto=format&fit=crop" alt="Wooden pier over water" loading="lazy" decoding="async"></figure>
    </div>
    <div class="gl-05__row">
      <figure class="gl-05__item" style="--r:1.78"><img src="https://images.unsplash.com/photo-1483412033650-1015ddeb83d1?q=80&w=640&h=360&auto=format&fit=crop" alt="Green valley panorama" loading="lazy" decoding="async"></figure>
      <figure class="gl-05__item" style="--r:1"><img src="https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?q=80&w=500&h=500&auto=format&fit=crop" alt="Close-up of a wildflower" loading="lazy" decoding="async"></figure>
      <figure class="gl-05__item" style="--r:1.4"><img src="https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=560&h=400&auto=format&fit=crop" alt="River through a forest" loading="lazy" decoding="async"></figure>
    </div>
    <div class="gl-05__row">
      <figure class="gl-05__item" style="--r:0.8"><img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=480&h=600&auto=format&fit=crop" alt="Tall narrow waterfall" loading="lazy" decoding="async"></figure>
      <figure class="gl-05__item" style="--r:1.6"><img src="https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=640&h=400&auto=format&fit=crop" alt="Sunlit sand dunes" loading="lazy" decoding="async"></figure>
      <figure class="gl-05__item" style="--r:1.2"><img src="https://images.unsplash.com/photo-1522542550221-31fd19575a2d?q=80&w=540&h=450&auto=format&fit=crop" alt="Alpine meadow in bloom" loading="lazy" decoding="async"></figure>
    </div>
  </div>
</section>
```
## CSS
```css
.gl-05,
.gl-05 *,
.gl-05 *::before,
.gl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-05 ::selection {
  background: oklch(0.6 0.15 160);
  color: #fff;
}

.gl-05 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #fafafa;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-05__gallery {
  width: min(920px,100%);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.gl-05__row {
  display: flex;
  gap: 8px;
}

.gl-05__item {
  flex: var(--r) 1 0;
  aspect-ratio: var(--r);
  border-radius: 8px;
  overflow: hidden;
  background: #e6e8ea;
}

.gl-05__item img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1);
  transition: transform .4s;
}

.gl-05__item:hover img {
  transform: scale(1.05);
}

@media (max-width: 600px) {
  .gl-05__row {
    flex-wrap: wrap;
  }

  .gl-05__item {
    flex: 1 1 40%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-05__item img {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — flex-grow weighted by aspect-ratio justifies each row with no cropping. */
```
