---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-polaroid-stack-gallery/"
title: "CSS Polaroid Stack Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Photos styled as vintage Polaroid snapshots — thick white frame, deep bottom border, handwritten caption — scattered at playful angles and straightening with…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Polaroid Stack Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-polaroid-stack-gallery/

Photos styled as vintage Polaroid snapshots — thick white frame, deep bottom border, handwritten caption — scattered at playful angles and straightening with a lift on hover. The nostalgic photo-stack look boutique and wedding sites search for.
## HTML
```html
<section class="gl-21" aria-label="Polaroid stack gallery">
  <div class="gl-21__pile">
    <figure class="gl-21__pola" tabindex="0"><img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=400&h=400&auto=format&fit=crop" alt="Friends on a summer trip" loading="lazy" decoding="async"><figcaption>Summer '24</figcaption></figure>
    <figure class="gl-21__pola" tabindex="0"><img src="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=400&h=400&auto=format&fit=crop" alt="Sunset on the beach" loading="lazy" decoding="async"><figcaption>Last light</figcaption></figure>
    <figure class="gl-21__pola" tabindex="0"><img src="https://images.unsplash.com/photo-1499346030926-9a72daac6c63?q=80&w=400&h=400&auto=format&fit=crop" alt="Road trip stop" loading="lazy" decoding="async"><figcaption>Route 1</figcaption></figure>
    <figure class="gl-21__pola" tabindex="0"><img src="https://images.unsplash.com/photo-1620121692029-d088224ddc74?q=80&w=400&h=400&auto=format&fit=crop" alt="Picnic in the park" loading="lazy" decoding="async"><figcaption>Sunday</figcaption></figure>
    <figure class="gl-21__pola" tabindex="0"><img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=400&h=400&auto=format&fit=crop" alt="Mountain hike" loading="lazy" decoding="async"><figcaption>The climb</figcaption></figure>
  </div>
</section>
```
## CSS
```css
.gl-21,
.gl-21 *,
.gl-21 *::before,
.gl-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-21 ::selection {
  background: oklch(0.6 0.12 40);
  color: #fff;
}

.gl-21 {
  --accent: oklch(0.55 0.13 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #d9cfc0;
  background-image: radial-gradient(rgba(120,100,80,.12) 1px,transparent 1px);
  background-size: 6px 6px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-21__pile {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
  align-items: center;
  width: min(820px,100%);
}

.gl-21__pola {
  background: #fffdf8;
  padding: 12px 12px 44px;
  border-radius: 2px;
  width: 190px;
  box-shadow: 0 10px 24px -10px rgba(60,40,20,.5);
  transition: transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s;
  outline: none;
}

.gl-21__pola img {
  display: block;
  width: 100%;
  aspect-ratio: 1/1;
  object-fit: cover;
  background: #e7e0d4;
  filter: sepia(.18) contrast(1.02);
}

.gl-21__pola figcaption {
  margin-top: 12px;
  text-align: center;
  font-family: 'Segoe Script','Bradley Hand',cursive;
  font-size: 17px;
  color: #5a4a38;
}

.gl-21__pola:nth-child(1) {
  transform: rotate(-6deg);
}

.gl-21__pola:nth-child(2) {
  transform: rotate(4deg);
}

.gl-21__pola:nth-child(3) {
  transform: rotate(-3deg);
}

.gl-21__pola:nth-child(4) {
  transform: rotate(5deg);
}

.gl-21__pola:nth-child(5) {
  transform: rotate(-5deg);
}

.gl-21__pola:hover,
.gl-21__pola:focus-visible {
  transform: rotate(0) scale(1.06);
  z-index: 5;
  box-shadow: 0 24px 44px -16px rgba(60,40,20,.6);
}

.gl-21__pola:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .gl-21__pola {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — nth-child rotations scatter the pile; hover straightens and lifts each print. */
```
