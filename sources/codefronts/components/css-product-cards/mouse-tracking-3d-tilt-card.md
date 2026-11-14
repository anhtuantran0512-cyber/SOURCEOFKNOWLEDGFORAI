---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/mouse-tracking-3d-tilt-card/"
title: "Mouse-Tracking 3D Tilt Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A premium tech/luxury card that tilts in 3D toward the cursor with a moving specular glare — the interactive VanillaTilt-style effect gaming, crypto and…"
has_js: "true"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mouse-Tracking 3D Tilt Card
Source: https://codefronts.com/components/css-product-cards/mouse-tracking-3d-tilt-card/

A premium tech/luxury card that tilts in 3D toward the cursor with a moving specular glare — the interactive VanillaTilt-style effect gaming, crypto and high-end product pages reach for. A few lines of pointer JS feed two CSS variables; all the rendering is CSS.
## HTML
```html
<article class="cpc-04" id="cpc-04-card">
  <div class="cpc-04__card" id="cpc-04-tilt">
    <div class="cpc-04__media" role="img" aria-label="Product photo: Nova mechanical keyboard"><span>product shot</span></div>
    <div class="cpc-04__body">
      <p class="cpc-04__brand">Nova Labs</p>
      <h3 class="cpc-04__name">Nova 75 Mechanical Keyboard</h3>
      <div class="cpc-04__row"><p class="cpc-04__price">$219</p><button class="cpc-04__cta" type="button">Buy Now</button></div>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-04,
.cpc-04 *,
.cpc-04 *::before,
.cpc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-04 ::selection {
  background: oklch(0.7 0.16 285);
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

.cpc-04 {
  --accent: oklch(0.72 0.17 285);
  --rx: 0deg;
  --ry: 0deg;
  --mx: 50%;
  --my: 50%;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(120% 120% at 50% 20%,#141021,#08060f);
  perspective: 900px;
}

.cpc-04__card {
  position: relative;
  width: 320px;
  border-radius: 20px;
  overflow: hidden;
  cursor: pointer;
  background: linear-gradient(160deg,#1b1730,#12101d);
  border: 1px solid rgba(255,255,255,.08);
  transform: rotateX(var(--rx)) rotateY(var(--ry));
  transform-style: preserve-3d;
  transition: transform .4s ease,box-shadow .4s;
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.8);
}

.cpc-04__card::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 3;
  background: radial-gradient(320px 320px at var(--mx) var(--my),rgba(255,255,255,.22),transparent 60%);
  opacity: 0;
  transition: opacity .3s;
  mix-blend-mode: screen;
}

.cpc-04__card:hover::after {
  opacity: 1;
}

.cpc-04__media {
  aspect-ratio: 16/11;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#2a2440,#1a1730),repeating-linear-gradient(45deg,rgba(255,255,255,.06) 0 14px,transparent 14px 28px);
}

.cpc-04__media {
  background-image: url("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-04__media span {
  display: none;
}

.cpc-04__body {
  padding: 20px 22px 22px;
}

.cpc-04__brand {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.cpc-04__name {
  margin-top: 6px;
  font-size: 18px;
  font-weight: 600;
  color: #f2f0fb;
  line-height: 1.3;
}

.cpc-04__row {
  margin-top: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cpc-04__price {
  font-size: 20px;
  font-weight: 700;
  color: #fff;
}

.cpc-04__cta {
  height: 44px;
  padding: 0 22px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
  color: #0a0616;
  font-size: 14px;
  font-weight: 700;
  box-shadow: 0 0 22px -6px var(--accent);
}

.cpc-04__cta:hover {
  filter: brightness(1.08);
}

.cpc-04__cta:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 55%,#000);
  outline-offset: 2px;
}

@media (hover: none),(prefers-reduced-motion: reduce) {
  .cpc-04__card {
    transform: none;
    transition: none;
  }

  .cpc-04__card::after {
    display: none;
  }
}
```

## JavaScript
```js
(function(){
  var card = document.getElementById('cpc-04-tilt');
  if(!card) return;
  if(matchMedia('(hover:none)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  var MAX = 12; // max tilt in degrees
  card.addEventListener('pointermove', function(e){
    var r = card.getBoundingClientRect();
    var px = (e.clientX - r.left) / r.width;   // 0..1
    var py = (e.clientY - r.top) / r.height;   // 0..1
    card.style.setProperty('--ry', ((px - .5) * 2 * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--rx', ((.5 - py) * 2 * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
    card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
  });
  card.addEventListener('pointerleave', function(){
    card.style.setProperty('--rx','0deg');
    card.style.setProperty('--ry','0deg');
  });
})();
```
