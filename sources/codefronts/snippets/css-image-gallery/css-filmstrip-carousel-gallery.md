---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-filmstrip-carousel-gallery/"
title: "CSS Filmstrip Carousel Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A low-profile horizontal strip of thumbnails that scrolls and snaps like a camera filmstrip, with sprocket-hole styling and momentum snapping to each frame."
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Filmstrip Carousel Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-filmstrip-carousel-gallery/

A low-profile horizontal strip of thumbnails that scrolls and snaps like a camera filmstrip, with sprocket-hole styling and momentum snapping to each frame. Built with CSS scroll-snap — no carousel library.
## HTML
```html
<section class="gl-07" aria-label="Filmstrip carousel gallery">
  <div class="gl-07__strip" tabindex="0" role="region" aria-label="Scrollable filmstrip, use arrow keys">
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 1" loading="lazy" decoding="async"></figure>
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 2" loading="lazy" decoding="async"></figure>
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1505142468610-359e7d316be0?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 3" loading="lazy" decoding="async"></figure>
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1511499767150-a48a237f0083?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 4" loading="lazy" decoding="async"></figure>
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 5" loading="lazy" decoding="async"></figure>
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1439066615861-d1af74d74000?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 6" loading="lazy" decoding="async"></figure>
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 7" loading="lazy" decoding="async"></figure>
    <figure class="gl-07__frame"><img src="https://images.unsplash.com/photo-1518495973542-4542c06a5843?q=80&w=500&h=340&auto=format&fit=crop" alt="Travel photo 8" loading="lazy" decoding="async"></figure>
  </div>
</section>
```
## CSS
```css
.gl-07,
.gl-07 *,
.gl-07 *::before,
.gl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-07 ::selection {
  background: oklch(0.7 0.15 90);
  color: #111;
}

.gl-07 {
  --accent: oklch(0.72 0.16 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 0;
  background: #111;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-07__strip {
  display: flex;
  gap: 10px;
  width: 100%;
  padding: 26px 20px;
  background: #0a0a0a;
  background-image: repeating-linear-gradient(90deg,#0a0a0a 0 14px,#1c1c1c 14px 22px,#0a0a0a 22px 36px), repeating-linear-gradient(90deg,#0a0a0a 0 14px,#1c1c1c 14px 22px,#0a0a0a 22px 36px);
  background-size: 36px 12px,36px 12px;
  background-position: 0 6px,0 calc(100% - 6px);
  background-repeat: repeat-x;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: thin;
  scrollbar-color: var(--accent) #222;
}

.gl-07__strip::-webkit-scrollbar {
  height: 8px;
}

.gl-07__strip::-webkit-scrollbar-thumb {
  background: var(--accent);
  border-radius: 8px;
}

.gl-07__frame {
  flex: 0 0 auto;
  width: min(340px,72vw);
  scroll-snap-align: center;
  border: 3px solid #e8e8e8;
  border-radius: 2px;
  background: #e8e8e8;
  overflow: hidden;
}

.gl-07__frame img {
  display: block;
  width: 100%;
  aspect-ratio: 3/2;
  object-fit: cover;
  filter: grayscale(.1) contrast(1.02);
  transition: filter .3s;
}

.gl-07__frame:hover img {
  filter: none;
}

.gl-07__strip:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

@media (prefers-reduced-motion: reduce) {
  .gl-07__strip {
    scroll-behavior: auto;
  }

  .gl-07__frame img {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — scroll-snap-type:x mandatory snaps each film frame into place. */
```
