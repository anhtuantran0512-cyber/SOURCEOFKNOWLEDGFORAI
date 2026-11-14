---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-ken-burns-slideshow-gallery/"
title: "CSS Ken Burns Slideshow Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A cinematic auto-playing slideshow where each image slowly zooms and pans (the 'Ken Burns' effect) while cross-fading to the next — the high-production hero…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Ken Burns Slideshow Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-ken-burns-slideshow-gallery/

A cinematic auto-playing slideshow where each image slowly zooms and pans (the 'Ken Burns' effect) while cross-fading to the next — the high-production hero slideshow documentary sites and landing pages search for. Pure CSS keyframes.
## HTML
```html
<section class="gl-19" aria-label="Ken Burns slideshow" aria-roledescription="carousel">
  <div class="gl-19__frame">
    <figure class="gl-19__slide gl-19__slide--1"><img src="https://images.unsplash.com/photo-1418985991508-e47386d96a71?q=80&w=1200&h=700&auto=format&fit=crop" alt="Sweeping mountain vista" loading="lazy" decoding="async"><figcaption>The High Passes</figcaption></figure>
    <figure class="gl-19__slide gl-19__slide--2"><img src="https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?q=80&w=1200&h=700&auto=format&fit=crop" alt="Open ocean at golden hour" loading="lazy" decoding="async"><figcaption>Endless Blue</figcaption></figure>
    <figure class="gl-19__slide gl-19__slide--3"><img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?q=80&w=1200&h=700&auto=format&fit=crop" alt="Desert at dusk" loading="lazy" decoding="async"><figcaption>The Dry Lands</figcaption></figure>
    <figure class="gl-19__slide gl-19__slide--4"><img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=1200&h=700&auto=format&fit=crop" alt="Ancient forest interior" loading="lazy" decoding="async"><figcaption>Old Growth</figcaption></figure>
  </div>
</section>
```
## CSS
```css
.gl-19,
.gl-19 *,
.gl-19 *::before,
.gl-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-19 ::selection {
  background: oklch(0.7 0.13 60);
  color: #111;
}

.gl-19 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0a0a0c;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-19__frame {
  position: relative;
  width: min(920px,100%);
  aspect-ratio: 12/7;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 40px 80px -40px rgba(0,0,0,.9);
}

.gl-19__slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  animation: gl-19-fade 24s infinite;
}

.gl-19__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform-origin: center;
  animation: gl-19-kb 24s infinite;
}

.gl-19__slide figcaption {
  position: absolute;
  left: 0;
  bottom: 0;
  padding: 28px 30px;
  color: #fff;
  font-family: Georgia,serif;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -.01em;
  background: linear-gradient(0deg,rgba(0,0,0,.6),transparent);
  width: 100%;
}

.gl-19__slide--1 {
  animation-delay: 0s;
}

.gl-19__slide--1 img {
  animation-delay: 0s;
}

.gl-19__slide--2 {
  animation-delay: 6s;
}

.gl-19__slide--2 img {
  animation-delay: 6s;
}

.gl-19__slide--3 {
  animation-delay: 12s;
}

.gl-19__slide--3 img {
  animation-delay: 12s;
}

.gl-19__slide--4 {
  animation-delay: 18s;
}

.gl-19__slide--4 img {
  animation-delay: 18s;
}

@keyframes gl-19-fade {
  0% {
    opacity: 0;
  }

  2% {
    opacity: 1;
  }

  23% {
    opacity: 1;
  }

  27% {
    opacity: 0;
  }

  100% {
    opacity: 0;
  }
}

@keyframes gl-19-kb {
  0% {
    transform: scale(1) translate(0,0);
  }

  27% {
    transform: scale(1.18) translate(-3%,2%);
  }

  100% {
    transform: scale(1.18) translate(-3%,2%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-19__slide,
    .gl-19__slide img {
    animation: none;
  }

  .gl-19__slide--1 {
    opacity: 1;
  }

  .gl-19__slide--1 img {
    transform: scale(1.05);
  }
}
```

## JavaScript
```js
/* No JavaScript — staggered opacity cross-fade + a slow transform pan per slide. */
```
