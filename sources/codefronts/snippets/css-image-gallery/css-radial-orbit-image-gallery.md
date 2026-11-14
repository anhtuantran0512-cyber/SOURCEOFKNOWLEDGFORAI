---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-radial-orbit-image-gallery/"
title: "CSS Radial Orbit Image Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Circular thumbnails arranged evenly around a central hero and slowly revolving around it like planets — a radial orbit gallery for 'our services', galleries…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Radial Orbit Image Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-radial-orbit-image-gallery/

Circular thumbnails arranged evenly around a central hero and slowly revolving around it like planets — a radial orbit gallery for 'our services', galleries and playful hero sections. Pure CSS transforms, pauses on hover.
## HTML
```html
<section class="gl-17" aria-label="Radial orbit gallery">
  <div class="gl-17__system">
    <div class="gl-17__center"><img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=300&h=300&auto=format&fit=crop" alt="Featured central image" loading="lazy" decoding="async"></div>
    <div class="gl-17__ring">
      <a class="gl-17__sat" href="#" style="--a:0deg"><img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 1" loading="lazy" decoding="async"></a>
      <a class="gl-17__sat" href="#" style="--a:45deg"><img src="https://images.unsplash.com/photo-1620121692029-d088224ddc74?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 2" loading="lazy" decoding="async"></a>
      <a class="gl-17__sat" href="#" style="--a:90deg"><img src="https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 3" loading="lazy" decoding="async"></a>
      <a class="gl-17__sat" href="#" style="--a:135deg"><img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 4" loading="lazy" decoding="async"></a>
      <a class="gl-17__sat" href="#" style="--a:180deg"><img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 5" loading="lazy" decoding="async"></a>
      <a class="gl-17__sat" href="#" style="--a:225deg"><img src="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 6" loading="lazy" decoding="async"></a>
      <a class="gl-17__sat" href="#" style="--a:270deg"><img src="https://images.unsplash.com/photo-1590490360182-c33d57733427?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 7" loading="lazy" decoding="async"></a>
      <a class="gl-17__sat" href="#" style="--a:315deg"><img src="https://images.unsplash.com/photo-1444723121867-7a241cacace9?q=80&w=200&h=200&auto=format&fit=crop" alt="Orbit photo 8" loading="lazy" decoding="async"></a>
    </div>
  </div>
</section>
```
## CSS
```css
.gl-17,
.gl-17 *,
.gl-17 *::before,
.gl-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-17 ::selection {
  background: oklch(0.7 0.16 270);
  color: #fff;
}

.gl-17 {
  --r: 170px;
  --accent: oklch(0.72 0.16 270);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 40%,#1a1836,#06060f);
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-17__system {
  position: relative;
  width: calc(var(--r) * 2 + 90px);
  height: calc(var(--r) * 2 + 90px);
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-17__center {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  z-index: 2;
  box-shadow: 0 0 40px -6px var(--accent),0 0 0 4px rgba(255,255,255,.1);
}

.gl-17__center img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gl-17__ring {
  position: absolute;
  inset: 0;
  animation: gl-17-spin 26s linear infinite;
}

.gl-17__system:hover .gl-17__ring,
.gl-17__system:focus-within .gl-17__ring {
  animation-play-state: paused;
}

.gl-17__sat {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 66px;
  height: 66px;
  margin: -33px;
  border-radius: 50%;
  overflow: hidden;
  text-decoration: none;
  transform: rotate(var(--a)) translate(var(--r)) rotate(calc(-1 * var(--a)));
  box-shadow: 0 0 0 3px rgba(255,255,255,.12),0 8px 20px -8px rgba(0,0,0,.6);
  animation: gl-17-spin 26s linear infinite reverse;
  transition: box-shadow .3s;
}

.gl-17__sat img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .3s;
}

.gl-17__sat:hover img,
.gl-17__sat:focus-visible img {
  transform: scale(1.12);
}

.gl-17__sat:hover,
.gl-17__sat:focus-visible {
  box-shadow: 0 0 0 3px var(--accent),0 10px 26px -8px rgba(0,0,0,.7);
}

.gl-17__sat:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@keyframes gl-17-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 560px) {
  .gl-17 {
    --r: 120px;
  }

  .gl-17__sat {
    width: 54px;
    height: 54px;
    margin: -27px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-17__ring,
    .gl-17__sat {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a revolving ring with counter-rotating thumbnails; pauses on hover. */
```
