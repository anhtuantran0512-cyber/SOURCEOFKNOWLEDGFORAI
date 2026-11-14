---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-scattered-photos-gallery/"
title: "CSS Scattered Photos Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A casual collage of photos strewn across the surface at random angles; click any one and it springs to the centre, straightens and rises to the top of the…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scattered Photos Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-scattered-photos-gallery/

A casual collage of photos strewn across the surface at random angles; click any one and it springs to the centre, straightens and rises to the top of the pile — an interactive scatter board built with position:absolute and the :target selector.
## HTML
```html
<section class="gl-22" id="gl-22" aria-label="Scattered photos collage">
  <a class="gl-22__reset" href="#gl-22" aria-label="Reset collage"></a>
  <div class="gl-22__board">
    <a class="gl-22__photo" id="gl-22-1" href="#gl-22-1" style="--rot:-8deg;top:8%;left:10%"><img src="https://images.unsplash.com/photo-1501554728187-ce583db33af7?q=80&w=400&h=300&auto=format&fit=crop" alt="Collage photo 1" loading="lazy" decoding="async"></a>
    <a class="gl-22__photo" id="gl-22-2" href="#gl-22-2" style="--rot:6deg;top:14%;left:38%"><img src="https://images.unsplash.com/photo-1589003077984-894e133dabab?q=80&w=400&h=300&auto=format&fit=crop" alt="Collage photo 2" loading="lazy" decoding="async"></a>
    <a class="gl-22__photo" id="gl-22-3" href="#gl-22-3" style="--rot:-5deg;top:10%;left:64%"><img src="https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3?q=80&w=400&h=300&auto=format&fit=crop" alt="Collage photo 3" loading="lazy" decoding="async"></a>
    <a class="gl-22__photo" id="gl-22-4" href="#gl-22-4" style="--rot:9deg;top:46%;left:18%"><img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=400&h=300&auto=format&fit=crop" alt="Collage photo 4" loading="lazy" decoding="async"></a>
    <a class="gl-22__photo" id="gl-22-5" href="#gl-22-5" style="--rot:-7deg;top:50%;left:48%"><img src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?q=80&w=400&h=300&auto=format&fit=crop" alt="Collage photo 5" loading="lazy" decoding="async"></a>
    <a class="gl-22__photo" id="gl-22-6" href="#gl-22-6" style="--rot:4deg;top:44%;left:70%"><img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=400&h=300&auto=format&fit=crop" alt="Collage photo 6" loading="lazy" decoding="async"></a>
  </div>
  <p class="gl-22__hint">click a photo to bring it forward · click the background to reset</p>
</section>
```
## CSS
```css
.gl-22,
.gl-22 *,
.gl-22 *::before,
.gl-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-22 ::selection {
  background: oklch(0.6 0.15 250);
  color: #fff;
}

.gl-22 {
  --accent: oklch(0.62 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #1c1a17;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
}

.gl-22__reset {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.gl-22__board {
  position: relative;
  width: min(820px,100%);
  aspect-ratio: 16/10;
  z-index: 1;
}

.gl-22__photo {
  position: absolute;
  width: 26%;
  border-radius: 3px;
  overflow: hidden;
  padding: 8px 8px 8px;
  background: #fffdf8;
  text-decoration: none;
  transform: rotate(var(--rot));
  transform-origin: center;
  box-shadow: 0 12px 28px -12px rgba(0,0,0,.7);
  transition: transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .4s,z-index 0s;
}

.gl-22__photo img {
  display: block;
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  background: #e0dacd;
}

.gl-22__photo:hover {
  transform: rotate(var(--rot)) scale(1.04);
  z-index: 6;
  box-shadow: 0 18px 36px -14px rgba(0,0,0,.75);
}

.gl-22__photo:target {
  top: 50% !important;
  left: 50% !important;
  transform: translate(-50%,-50%) rotate(0deg) scale(1.5);
  z-index: 10;
  box-shadow: 0 30px 60px -18px rgba(0,0,0,.85);
}

.gl-22__photo:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.gl-22__hint {
  position: relative;
  z-index: 1;
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #8a8378;
}

@media (max-width: 560px) {
  .gl-22__photo {
    width: 38%;
  }

  .gl-22__photo:target {
    transform: translate(-50%,-50%) rotate(0) scale(1.3);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-22__photo {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :target lifts the clicked photo to centre; a full-board link resets. */
```
