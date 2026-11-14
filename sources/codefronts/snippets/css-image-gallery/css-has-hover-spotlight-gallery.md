---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-has-hover-spotlight-gallery/"
title: "CSS :has() Hover Spotlight Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Hover any card and every other card in the grid instantly dims and desaturates, spotlighting the one you're on — the modern focus effect built with the…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS :has() Hover Spotlight Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-has-hover-spotlight-gallery/

Hover any card and every other card in the grid instantly dims and desaturates, spotlighting the one you're on — the modern focus effect built with the :has() relational selector (and :focus-within for keyboards). Zero JS.
## HTML
```html
<section class="gl-13" aria-label="Spotlight hover gallery">
  <div class="gl-13__grid">
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?q=80&w=400&h=400&auto=format&fit=crop" alt="Tokyo street" loading="lazy" decoding="async"><span>Tokyo</span></a>
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=400&h=400&auto=format&fit=crop" alt="Paris rooftops" loading="lazy" decoding="async"><span>Paris</span></a>
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1467003909585-2f8a72700288?q=80&w=400&h=400&auto=format&fit=crop" alt="New York skyline" loading="lazy" decoding="async"><span>New York</span></a>
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?q=80&w=400&h=400&auto=format&fit=crop" alt="London bridge" loading="lazy" decoding="async"><span>London</span></a>
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1482938289607-e9573fc25ebb?q=80&w=400&h=400&auto=format&fit=crop" alt="Sydney harbour" loading="lazy" decoding="async"><span>Sydney</span></a>
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?q=80&w=400&h=400&auto=format&fit=crop" alt="Rome architecture" loading="lazy" decoding="async"><span>Rome</span></a>
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?q=80&w=400&h=400&auto=format&fit=crop" alt="Dubai towers" loading="lazy" decoding="async"><span>Dubai</span></a>
    <a class="gl-13__card" href="#"><img src="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?q=80&w=400&h=400&auto=format&fit=crop" alt="Cairo skyline" loading="lazy" decoding="async"><span>Cairo</span></a>
  </div>
</section>
```
## CSS
```css
.gl-13,
.gl-13 *,
.gl-13 *::before,
.gl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-13 ::selection {
  background: oklch(0.7 0.17 60);
  color: #111;
}

.gl-13 {
  --accent: oklch(0.72 0.17 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0f1013;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-13__grid {
  width: min(760px,100%);
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(4,1fr);
}

.gl-13__card {
  position: relative;
  display: block;
  text-decoration: none;
  border-radius: 12px;
  overflow: hidden;
  background: #1a1c20;
  transition: transform .4s,opacity .4s,filter .4s;
}

.gl-13__card img {
  display: block;
  width: 100%;
  aspect-ratio: 1/1;
  object-fit: cover;
}

.gl-13__card span {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 20px 10px 8px;
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .03em;
  background: linear-gradient(0deg,rgba(0,0,0,.75),transparent);
}

.gl-13__grid:has(.gl-13__card:hover) .gl-13__card:not(:hover),
.gl-13__grid:has(.gl-13__card:focus-visible) .gl-13__card:not(:focus-visible) {
  opacity: .4;
  filter: saturate(.35) brightness(.7);
}

.gl-13__card:hover,
.gl-13__card:focus-visible {
  transform: scale(1.06);
  z-index: 2;
  box-shadow: 0 20px 40px -18px rgba(0,0,0,.7);
}

.gl-13__card:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 560px) {
  .gl-13__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-13__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — .grid:has(.card:hover) .card:not(:hover) dims every non-active card. */
```
