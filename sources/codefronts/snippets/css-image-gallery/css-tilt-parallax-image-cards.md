---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-tilt-parallax-image-cards/"
title: "CSS Tilt Parallax Image Cards"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Photo cards that tilt in 3D toward the cursor with a moving specular glare and a parallax caption that floats above the image — the interactive tilt effect…"
has_js: "true"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Tilt Parallax Image Cards
Source: https://codefronts.com/snippets/css-image-gallery/css-tilt-parallax-image-cards/

Photo cards that tilt in 3D toward the cursor with a moving specular glare and a parallax caption that floats above the image — the interactive tilt effect portfolios and product heroes search for. A few lines of pointer JS feed CSS variables; CSS does the rendering.
## HTML
```html
<section class="gl-14" id="gl-14" aria-label="3D tilt parallax cards">
  <div class="gl-14__row">
    <article class="gl-14__card" data-tilt><div class="gl-14__media"><img src="https://images.unsplash.com/photo-1516031190212-da133013de50?q=80&w=500&h=620&auto=format&fit=crop" alt="Aurora over mountains" loading="lazy" decoding="async"></div><figcaption class="gl-14__cap"><span class="gl-14__k">Iceland</span><h3>Northern Skies</h3></figcaption></article>
    <article class="gl-14__card" data-tilt><div class="gl-14__media"><img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=500&h=620&auto=format&fit=crop" alt="Canyon at sunset" loading="lazy" decoding="async"></div><figcaption class="gl-14__cap"><span class="gl-14__k">Utah</span><h3>Red Horizon</h3></figcaption></article>
    <article class="gl-14__card" data-tilt><div class="gl-14__media"><img src="https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?q=80&w=500&h=620&auto=format&fit=crop" alt="Foggy forest" loading="lazy" decoding="async"></div><figcaption class="gl-14__cap"><span class="gl-14__k">Oregon</span><h3>Deep Green</h3></figcaption></article>
  </div>
</section>
```
## CSS
```css
.gl-14,
.gl-14 *,
.gl-14 *::before,
.gl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-14 ::selection {
  background: oklch(0.72 0.16 285);
  color: #0a0616;
}

@property --rx {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

@property --ry {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

.gl-14 {
  --accent: oklch(0.74 0.16 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 15%,#141021,#08060f);
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1000px;
}

.gl-14__row {
  display: flex;
  gap: 26px;
  flex-wrap: wrap;
  justify-content: center;
  width: min(940px,100%);
}

.gl-14__card {
  --rx: 0deg;
  --ry: 0deg;
  --mx: 50%;
  --my: 50%;
  position: relative;
  width: 260px;
  border-radius: 20px;
  overflow: hidden;
  cursor: pointer;
  transform: rotateX(var(--rx)) rotateY(var(--ry));
  transform-style: preserve-3d;
  transition: transform .4s ease,box-shadow .4s;
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.8);
  background: #12101d;
}

.gl-14__card::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  background: radial-gradient(300px 300px at var(--mx) var(--my),rgba(255,255,255,.28),transparent 60%);
  opacity: 0;
  transition: opacity .3s;
  mix-blend-mode: screen;
}

.gl-14__card:hover::after {
  opacity: 1;
}

.gl-14__media {
  overflow: hidden;
}

.gl-14__media img {
  display: block;
  width: 100%;
  aspect-ratio: 5/6;
  object-fit: cover;
  transform: translateZ(0);
}

.gl-14__cap {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 22px 20px;
  z-index: 2;
  transform: translateZ(50px);
  background: linear-gradient(0deg,rgba(8,6,15,.85),transparent);
}

.gl-14__k {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.gl-14__cap h3 {
  margin-top: 4px;
  font-size: 19px;
  font-weight: 700;
  color: #fff;
}

.gl-14__card:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (hover: none),(prefers-reduced-motion: reduce) {
  .gl-14__card {
    transform: none;
    transition: none;
  }

  .gl-14__card::after {
    display: none;
  }

  .gl-14__cap {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('gl-14');
  if(!root) return;
  if(matchMedia('(hover:none)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  var MAX = 12; // max tilt in degrees
  root.querySelectorAll('[data-tilt]').forEach(function(card){
    card.addEventListener('pointermove', function(e){
      var r = card.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width;
      var py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--ry', ((px - .5) * 2 * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--rx', ((.5 - py) * 2 * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
      card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
    });
    card.addEventListener('pointerleave', function(){
      card.style.setProperty('--rx','0deg');
      card.style.setProperty('--ry','0deg');
    });
  });
})();
```
