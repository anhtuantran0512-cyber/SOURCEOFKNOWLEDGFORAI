---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-infinite-scroll-image-strip/"
title: "CSS Infinite Scroll Image Strip"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A seamless, endlessly looping horizontal banner of images that scrolls forever with no visible seam or reset — the marquee/logo-wall effect brand pages and…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Infinite Scroll Image Strip
Source: https://codefronts.com/snippets/css-image-gallery/css-infinite-scroll-image-strip/

A seamless, endlessly looping horizontal banner of images that scrolls forever with no visible seam or reset — the marquee/logo-wall effect brand pages and 'as featured in' rows search for. Pure CSS keyframes.
## HTML
```html
<section class="gl-18" aria-label="Infinite scrolling image strip">
  <div class="gl-18__viewport">
    <div class="gl-18__track">
      <img src="https://images.unsplash.com/photo-1449157291145-7efd050a4d0e?q=80&w=300&h=300&auto=format&fit=crop" alt="Gallery image 1" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&h=300&auto=format&fit=crop" alt="Gallery image 2" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=300&h=300&auto=format&fit=crop" alt="Gallery image 3" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?q=80&w=300&h=300&auto=format&fit=crop" alt="Gallery image 4" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?q=80&w=300&h=300&auto=format&fit=crop" alt="Gallery image 5" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=300&h=300&auto=format&fit=crop" alt="Gallery image 6" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1449157291145-7efd050a4d0e?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async">
      <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async">
    </div>
  </div>
</section>
```
## CSS
```css
.gl-18,
.gl-18 *,
.gl-18 *::before,
.gl-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-18 ::selection {
  background: oklch(0.7 0.14 30);
  color: #111;
}

.gl-18 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 0;
  background: #0f0f0f;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-18__viewport {
  width: 100%;
  overflow: hidden;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
  mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
}

.gl-18__track {
  display: flex;
  gap: 16px;
  width: max-content;
  animation: gl-18-marquee 30s linear infinite;
}

.gl-18__viewport:hover .gl-18__track {
  animation-play-state: paused;
}

.gl-18__track img {
  display: block;
  width: 220px;
  height: 220px;
  object-fit: cover;
  border-radius: 12px;
  flex: 0 0 auto;
  filter: grayscale(1) contrast(1.05);
  transition: filter .4s;
}

.gl-18__track img:hover {
  filter: none;
}

@keyframes gl-18-marquee {
  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-18__track {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a doubled track translated -50% loops seamlessly and forever. */
```
