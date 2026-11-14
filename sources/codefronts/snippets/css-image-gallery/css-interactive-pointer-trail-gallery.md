---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-interactive-pointer-trail-gallery/"
title: "CSS Interactive Pointer Trail Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A playful canvas where images bloom and float behind your cursor as you move across it, then gently drift and fade — the cursor-trail image effect creative…"
has_js: "true"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Interactive Pointer Trail Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-interactive-pointer-trail-gallery/

A playful canvas where images bloom and float behind your cursor as you move across it, then gently drift and fade — the cursor-trail image effect creative portfolios and landing pages search for. CSS owns the animation; a tiny script spawns the trail.
## HTML
```html
<section class="gl-20" aria-label="Interactive pointer trail gallery">
  <div class="gl-20__canvas" id="gl-20-canvas" role="img" aria-label="Move your cursor to leave a trail of images">
    <p class="gl-20__hint">move your cursor across the canvas</p>
  </div>
</section>
```
## CSS
```css
.gl-20,
.gl-20 *,
.gl-20 *::before,
.gl-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-20 ::selection {
  background: oklch(0.72 0.18 320);
  color: #fff;
}

.gl-20 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 30%,#171526,#08070f);
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-20__canvas {
  position: relative;
  width: min(860px,100%);
  height: min(520px,70vh);
  border-radius: 20px;
  overflow: hidden;
  cursor: crosshair;
  background: linear-gradient(135deg,rgba(255,255,255,.03),rgba(255,255,255,.01));
  border: 1px solid rgba(255,255,255,.08);
  touch-action: none;
}

.gl-20__hint {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255,255,255,.35);
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  pointer-events: none;
}

.gl-20__spark {
  position: absolute;
  width: 120px;
  height: 150px;
  margin: -75px 0 0 -60px;
  border-radius: 12px;
  object-fit: cover;
  pointer-events: none;
  will-change: transform,opacity;
  box-shadow: 0 12px 30px -12px rgba(0,0,0,.6);
  animation: gl-20-bloom 1.1s cubic-bezier(.2,.7,.2,1) forwards;
}

@keyframes gl-20-bloom {
  0% {
    opacity: 0;
    transform: scale(.4) rotate(-6deg);
  }

  18% {
    opacity: 1;
    transform: scale(1) rotate(0deg);
  }

  100% {
    opacity: 0;
    transform: scale(.86) translateY(40px) rotate(4deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-20__spark {
    display: none;
  }
}
```

## JavaScript
```js
(function(){
  var canvas = document.getElementById('gl-20-canvas');
  if(!canvas) return;
  if(matchMedia('(hover:none)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  var pool = [1801,1803,1002,1601,1101,1301].map(function(n){
    return 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=240&h=300&auto=format&fit=crop?lock=' + n;
  });
  var i = 0, last = 0;
  canvas.addEventListener('pointermove', function(e){
    var now = Date.now();
    if(now - last < 90) return;      // throttle spawn rate
    last = now;
    var r = canvas.getBoundingClientRect();
    var img = document.createElement('img');
    img.className = 'gl-20__spark';
    img.alt = '';
    img.setAttribute('aria-hidden','true');
    img.src = pool[i % pool.length]; i++;
    img.style.left = (e.clientX - r.left) + 'px';
    img.style.top  = (e.clientY - r.top) + 'px';
    img.addEventListener('animationend', function(){ img.remove(); });
    canvas.appendChild(img);
  });
})();
```
