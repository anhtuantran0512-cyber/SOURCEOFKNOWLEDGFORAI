---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-perspective-depth-stack-gallery/"
title: "CSS Perspective Depth Stack Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A deck of photos stacked in 3D space that fans out into a cascade when you hover or focus the stack — a spatial, depth-layered gallery for hero sections and…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Perspective Depth Stack Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-perspective-depth-stack-gallery/

A deck of photos stacked in 3D space that fans out into a cascade when you hover or focus the stack — a spatial, depth-layered gallery for hero sections and 'featured shots'. Built with perspective and translateZ.
## HTML
```html
<section class="gl-16" aria-label="Perspective depth stack gallery">
  <div class="gl-16__stack" tabindex="-1">
    <a class="gl-16__card" href="#"><img src="https://images.unsplash.com/photo-1607746882042-944635dfe10e?q=80&w=500&h=620&auto=format&fit=crop" alt="Featured photo 1" loading="lazy" decoding="async"></a>
    <a class="gl-16__card" href="#"><img src="https://images.unsplash.com/photo-1505691938895-1758d7feb511?q=80&w=500&h=620&auto=format&fit=crop" alt="Featured photo 2" loading="lazy" decoding="async"></a>
    <a class="gl-16__card" href="#"><img src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=500&h=620&auto=format&fit=crop" alt="Featured photo 3" loading="lazy" decoding="async"></a>
    <a class="gl-16__card" href="#"><img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?q=80&w=500&h=620&auto=format&fit=crop" alt="Featured photo 4" loading="lazy" decoding="async"></a>
  </div>
  <p class="gl-16__hint">hover or focus the stack to fan it out</p>
</section>
```
## CSS
```css
.gl-16,
.gl-16 *,
.gl-16 *::before,
.gl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-16 ::selection {
  background: oklch(0.65 0.16 320);
  color: #fff;
}

.gl-16 {
  --accent: oklch(0.66 0.17 320);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #14101a;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
}

.gl-16__stack {
  position: relative;
  width: 260px;
  height: 330px;
  perspective: 1200px;
}

.gl-16__card {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  overflow: hidden;
  transform-style: preserve-3d;
  transform-origin: bottom center;
  box-shadow: 0 20px 40px -20px rgba(0,0,0,.7);
  transition: transform .55s cubic-bezier(.2,.7,.2,1);
}

.gl-16__card img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gl-16__card:nth-child(1) {
  transform: translateZ(60px);
}

.gl-16__card:nth-child(2) {
  transform: translateZ(40px) translateY(10px) scale(.97);
}

.gl-16__card:nth-child(3) {
  transform: translateZ(20px) translateY(20px) scale(.94);
}

.gl-16__card:nth-child(4) {
  transform: translateZ(0) translateY(30px) scale(.91);
}

.gl-16__stack:hover .gl-16__card:nth-child(1),
.gl-16__stack:focus-within .gl-16__card:nth-child(1) {
  transform: translateX(-150px) rotate(-9deg);
}

.gl-16__stack:hover .gl-16__card:nth-child(2),
.gl-16__stack:focus-within .gl-16__card:nth-child(2) {
  transform: translateX(-50px) rotate(-3deg);
}

.gl-16__stack:hover .gl-16__card:nth-child(3),
.gl-16__stack:focus-within .gl-16__card:nth-child(3) {
  transform: translateX(50px) rotate(3deg);
}

.gl-16__stack:hover .gl-16__card:nth-child(4),
.gl-16__stack:focus-within .gl-16__card:nth-child(4) {
  transform: translateX(150px) rotate(9deg);
}

.gl-16__card:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  z-index: 5;
}

.gl-16__hint {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #8a7e96;
}

@media (prefers-reduced-motion: reduce) {
  .gl-16__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — resting translateZ stack fans out via per-card transforms on hover/focus. */
```
