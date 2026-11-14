---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-diagonal-slice-reveal-gallery/"
title: "CSS Diagonal Slice Reveal Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Sleek tiles split by a sharp diagonal line; on hover the two angled halves slide apart to reveal the photo and a label beneath — a geometric reveal effect…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Slice Reveal Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-diagonal-slice-reveal-gallery/

Sleek tiles split by a sharp diagonal line; on hover the two angled halves slide apart to reveal the photo and a label beneath — a geometric reveal effect agency and product-launch pages search for. Built with clip-path + transform.
## HTML
```html
<section class="gl-12" aria-label="Diagonal slice reveal gallery">
  <div class="gl-12__row">
    <a class="gl-12__tile" href="#"><img src="https://images.unsplash.com/photo-1511818966892-d7d671e672a2?q=80&w=500&h=500&auto=format&fit=crop" alt="Snowy mountain range" loading="lazy" decoding="async"><span class="gl-12__cover gl-12__cover--a"></span><span class="gl-12__cover gl-12__cover--b"></span><span class="gl-12__cap">Alps</span></a>
    <a class="gl-12__tile" href="#"><img src="https://images.unsplash.com/photo-1444723121867-7a241cacace9?q=80&w=500&h=500&auto=format&fit=crop" alt="Desert dunes" loading="lazy" decoding="async"><span class="gl-12__cover gl-12__cover--a"></span><span class="gl-12__cover gl-12__cover--b"></span><span class="gl-12__cap">Sahara</span></a>
    <a class="gl-12__tile" href="#"><img src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?q=80&w=500&h=500&auto=format&fit=crop" alt="Coral reef underwater" loading="lazy" decoding="async"><span class="gl-12__cover gl-12__cover--a"></span><span class="gl-12__cover gl-12__cover--b"></span><span class="gl-12__cap">Reef</span></a>
  </div>
</section>
```
## CSS
```css
.gl-12,
.gl-12 *,
.gl-12 *::before,
.gl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-12 ::selection {
  background: oklch(0.65 0.19 300);
  color: #fff;
}

.gl-12 {
  --accent: oklch(0.62 0.19 300);
  --c1: oklch(0.5 0.17 285);
  --c2: oklch(0.62 0.19 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0e0c14;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-12__row {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
  width: min(880px,100%);
}

.gl-12__tile {
  position: relative;
  width: 260px;
  aspect-ratio: 1/1;
  border-radius: 14px;
  overflow: hidden;
  display: block;
  text-decoration: none;
  background: #1a1622;
}

.gl-12__tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gl-12__cover {
  position: absolute;
  inset: 0;
  transition: transform .5s cubic-bezier(.5,0,.2,1);
}

.gl-12__cover--a {
  background: linear-gradient(135deg,var(--c1),color-mix(in oklch,var(--c1) 60%,#000));
  clip-path: polygon(0 0,100% 0,0 100%);
}

.gl-12__cover--b {
  background: linear-gradient(135deg,var(--c2),color-mix(in oklch,var(--c2) 60%,#000));
  clip-path: polygon(100% 0,100% 100%,0 100%);
}

.gl-12__tile:hover .gl-12__cover--a,
.gl-12__tile:focus-visible .gl-12__cover--a {
  transform: translate(-101%,-101%);
}

.gl-12__tile:hover .gl-12__cover--b,
.gl-12__tile:focus-visible .gl-12__cover--b {
  transform: translate(101%,101%);
}

.gl-12__cap {
  position: absolute;
  inset: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 20px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  pointer-events: none;
  transition: opacity .3s;
}

.gl-12__tile:hover .gl-12__cap,
.gl-12__tile:focus-visible .gl-12__cap {
  opacity: 0;
}

.gl-12__cap::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(0deg,rgba(0,0,0,.4),transparent);
  opacity: 0;
  transition: opacity .3s;
}

.gl-12__tile:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .gl-12__cover,
    .gl-12__cap {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two clip-path halves translate apart along the diagonal on hover. */
```
