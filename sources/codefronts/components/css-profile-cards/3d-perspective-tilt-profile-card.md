---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/3d-perspective-tilt-profile-card/"
title: "3D Perspective Tilt Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A card that tilts in 3D toward the cursor with a moving specular sheen, driven by a small pointer handler that batches updates through requestAnimationFrame."
has_js: "true"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Perspective Tilt Profile Card
Source: https://codefronts.com/components/css-profile-cards/3d-perspective-tilt-profile-card/

A card that tilts in 3D toward the cursor with a moving specular sheen, driven by a small pointer handler that batches updates through requestAnimationFrame.
## HTML
```html
<div class="pc-08">
  <div class="pc-08__card" id="pc-08-tilt">
    <div class="pc-08__shine"></div>
    <div class="pc-08__content">
      <div class="pc-08__pfp">TN</div>
      <div class="pc-08__info">
        <h3>Theo Nakamura</h3>
        <p>3D / WebGL Developer</p>
      </div>
      <div class="pc-08__foot">
        <span class="pc-08__chip">Three.js</span>
        <span class="pc-08__chip">GLSL</span>
        <span class="pc-08__chip">Blender</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-08,
.pc-08 *,
.pc-08 *::before,
.pc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-08 ::selection {
  background: #ff4d6d;
  color: #fff;
}

.pc-08 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #0a0710;
  perspective: 900px;
  color: #fff;
}

.pc-08__card {
  position: relative;
  width: 320px;
  border-radius: 24px;
  padding: 30px;
  overflow: hidden;
  background: linear-gradient(150deg,#241033,#3a0f2e);
  border: 1px solid rgba(255,255,255,.1);
  box-shadow: 0 30px 70px -28px rgba(0,0,0,.85);
  transform-style: preserve-3d;
  transition: transform .12s ease-out;
  will-change: transform;
}

.pc-08__shine {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(300px 300px at var(--mx,50%) var(--my,0%),rgba(255,255,255,.22),transparent 60%);
  transition: background .1s;
}

.pc-08__content {
  transform: translateZ(40px);
}

.pc-08__pfp {
  width: 84px;
  height: 84px;
  border-radius: 22px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.6rem;
  background: linear-gradient(145deg,#ff4d6d,#c44dff);
  box-shadow: 0 14px 30px -10px #ff4d6d;
}

.pc-08__info {
  margin-top: 20px;
}

.pc-08__info h3 {
  font-size: 1.35rem;
  font-weight: 800;
}

.pc-08__info p {
  color: rgba(255,255,255,.6);
  font-size: .86rem;
  margin-top: 3px;
}

.pc-08__foot {
  display: flex;
  gap: 8px;
  margin-top: 22px;
}

.pc-08__chip {
  font-size: .72rem;
  padding: 6px 11px;
  border-radius: 9px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.14);
}

.pc-08__hint {
  position: absolute;
  bottom: 12px;
  right: 16px;
  font-size: .66rem;
  color: rgba(255,255,255,.3);
  letter-spacing: .1em;
}

@media (prefers-reduced-motion: reduce) {
  .pc-08__card {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var card = document.getElementById('pc-08-tilt');
  if(!card) return;
  var raf = null, tx=0, ty=0, mx=50, my=0;
  function onMove(e){
    var r = card.getBoundingClientRect();
    var px = (e.clientX - r.left) / r.width;
    var py = (e.clientY - r.top) / r.height;
    tx = (py - .5) * -16;
    ty = (px - .5) * 16;
    mx = px * 100; my = py * 100;
    if(!raf) raf = requestAnimationFrame(apply);
  }
  function apply(){
    raf = null;
    card.style.transform = 'rotateX(' + tx + 'deg) rotateY(' + ty + 'deg)';
    card.style.setProperty('--mx', mx + '%');
    card.style.setProperty('--my', my + '%');
  }
  function reset(){
    if(raf) cancelAnimationFrame(raf), raf=null;
    card.style.transform = 'rotateX(0) rotateY(0)';
    card.style.setProperty('--mx','50%');
    card.style.setProperty('--my','0%');
  }
  card.addEventListener('pointermove', onMove);
  card.addEventListener('pointerleave', reset);
})();
```
