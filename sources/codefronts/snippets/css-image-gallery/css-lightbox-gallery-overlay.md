---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-lightbox-gallery-overlay/"
title: "CSS Lightbox Gallery Overlay"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Click a thumbnail and the background dims while the full image expands into a centred modal — a complete lightbox with zero JavaScript, driven entirely by…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Lightbox Gallery Overlay
Source: https://codefronts.com/snippets/css-image-gallery/css-lightbox-gallery-overlay/

Click a thumbnail and the background dims while the full image expands into a centred modal — a complete lightbox with zero JavaScript, driven entirely by the :target pseudo-class. The pattern devs search for to drop a JS dependency.
## HTML
```html
<section class="gl-06" id="gl-06" aria-label="Lightbox image gallery">
  <div class="gl-06__grid">
    <a class="gl-06__thumb" href="#gl-06-1" aria-label="Open image 1: desert road"><img src="https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?q=80&w=400&h=300&auto=format&fit=crop" alt="Desert road stretching to the horizon" loading="lazy" decoding="async"></a>
    <a class="gl-06__thumb" href="#gl-06-2" aria-label="Open image 2: forest path"><img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=400&h=300&auto=format&fit=crop" alt="Sunlit path through a forest" loading="lazy" decoding="async"></a>
    <a class="gl-06__thumb" href="#gl-06-3" aria-label="Open image 3: mountain lake"><img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=400&h=300&auto=format&fit=crop" alt="Mountain lake at sunrise" loading="lazy" decoding="async"></a>
    <a class="gl-06__thumb" href="#gl-06-4" aria-label="Open image 4: city night"><img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=400&h=300&auto=format&fit=crop" alt="City lights at night" loading="lazy" decoding="async"></a>
    <a class="gl-06__thumb" href="#gl-06-5" aria-label="Open image 5: snowy peak"><img src="https://images.unsplash.com/photo-1486718448742-163732cd1544?q=80&w=400&h=300&auto=format&fit=crop" alt="Snow-covered mountain peak" loading="lazy" decoding="async"></a>
    <a class="gl-06__thumb" href="#gl-06-6" aria-label="Open image 6: coastal cliffs"><img src="https://images.unsplash.com/photo-1485955900006-10f4d324d411?q=80&w=400&h=300&auto=format&fit=crop" alt="Rugged coastal cliffs" loading="lazy" decoding="async"></a>
  </div>
  <div class="gl-06__lb" id="gl-06-1" role="dialog" aria-label="Image 1 enlarged"><a class="gl-06__back" href="#gl-06" aria-label="Close"></a><figure class="gl-06__panel"><img src="https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?q=80&w=1000&h=700&auto=format&fit=crop" alt="Desert road stretching to the horizon" loading="lazy" decoding="async"><a class="gl-06__x" href="#gl-06" aria-label="Close image">✕</a></figure></div>
  <div class="gl-06__lb" id="gl-06-2" role="dialog" aria-label="Image 2 enlarged"><a class="gl-06__back" href="#gl-06" aria-label="Close"></a><figure class="gl-06__panel"><img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=1000&h=700&auto=format&fit=crop" alt="Sunlit path through a forest" loading="lazy" decoding="async"><a class="gl-06__x" href="#gl-06" aria-label="Close image">✕</a></figure></div>
  <div class="gl-06__lb" id="gl-06-3" role="dialog" aria-label="Image 3 enlarged"><a class="gl-06__back" href="#gl-06" aria-label="Close"></a><figure class="gl-06__panel"><img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=1000&h=700&auto=format&fit=crop" alt="Mountain lake at sunrise" loading="lazy" decoding="async"><a class="gl-06__x" href="#gl-06" aria-label="Close image">✕</a></figure></div>
  <div class="gl-06__lb" id="gl-06-4" role="dialog" aria-label="Image 4 enlarged"><a class="gl-06__back" href="#gl-06" aria-label="Close"></a><figure class="gl-06__panel"><img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=1000&h=700&auto=format&fit=crop" alt="City lights at night" loading="lazy" decoding="async"><a class="gl-06__x" href="#gl-06" aria-label="Close image">✕</a></figure></div>
  <div class="gl-06__lb" id="gl-06-5" role="dialog" aria-label="Image 5 enlarged"><a class="gl-06__back" href="#gl-06" aria-label="Close"></a><figure class="gl-06__panel"><img src="https://images.unsplash.com/photo-1486718448742-163732cd1544?q=80&w=1000&h=700&auto=format&fit=crop" alt="Snow-covered mountain peak" loading="lazy" decoding="async"><a class="gl-06__x" href="#gl-06" aria-label="Close image">✕</a></figure></div>
  <div class="gl-06__lb" id="gl-06-6" role="dialog" aria-label="Image 6 enlarged"><a class="gl-06__back" href="#gl-06" aria-label="Close"></a><figure class="gl-06__panel"><img src="https://images.unsplash.com/photo-1485955900006-10f4d324d411?q=80&w=1000&h=700&auto=format&fit=crop" alt="Rugged coastal cliffs" loading="lazy" decoding="async"><a class="gl-06__x" href="#gl-06" aria-label="Close image">✕</a></figure></div>
</section>
```
## CSS
```css
.gl-06,
.gl-06 *,
.gl-06 *::before,
.gl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-06 ::selection {
  background: oklch(0.6 0.16 250);
  color: #fff;
}

.gl-06 {
  --accent: oklch(0.6 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0f1116;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-06__grid {
  width: min(760px,100%);
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(3,1fr);
}

.gl-06__thumb {
  display: block;
  border-radius: 10px;
  overflow: hidden;
  background: #1a1d24;
}

.gl-06__thumb img {
  display: block;
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  transform: scale(1);
  transition: transform .4s;
}

.gl-06__thumb:hover img,
.gl-06__thumb:focus-visible img {
  transform: scale(1.07);
}

.gl-06__thumb:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.gl-06__lb {
  position: fixed;
  inset: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s,visibility .3s;
}

.gl-06__lb:target {
  opacity: 1;
  visibility: visible;
}

.gl-06__back {
  position: absolute;
  inset: 0;
  background: rgba(6,8,12,.86);
  -webkit-backdrop-filter: blur(3px);
  backdrop-filter: blur(3px);
}

.gl-06__panel {
  position: relative;
  max-width: min(1000px,92vw);
  max-height: 86vh;
  transform: scale(.92);
  transition: transform .35s cubic-bezier(.2,.8,.2,1);
}

.gl-06__lb:target .gl-06__panel {
  transform: scale(1);
}

.gl-06__panel img {
  display: block;
  max-width: 100%;
  max-height: 86vh;
  border-radius: 8px;
  box-shadow: 0 40px 80px -30px rgba(0,0,0,.8);
}

.gl-06__x {
  position: absolute;
  top: -14px;
  right: -14px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  background: #fff;
  color: #0f1116;
  font-size: 16px;
  font-weight: 700;
  box-shadow: 0 6px 16px -4px rgba(0,0,0,.5);
}

.gl-06__x:hover {
  background: var(--accent);
  color: #fff;
}

.gl-06__x:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (max-width: 560px) {
  .gl-06__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-06__thumb img,
    .gl-06__lb,
    .gl-06__panel {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :target opens each modal; a close link resets the URL fragment. */
```
