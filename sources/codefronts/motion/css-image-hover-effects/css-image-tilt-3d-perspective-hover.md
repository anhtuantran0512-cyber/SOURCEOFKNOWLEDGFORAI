---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-tilt-3d-perspective-hover/"
title: "CSS Image Tilt 3D Perspective Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "A mousemove-driven 3D tilt illusion using CSS perspective and rotational transforms, with a specular highlight that tracks the pointer position."
has_js: "true"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Tilt 3D Perspective Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-tilt-3d-perspective-hover/

A mousemove-driven 3D tilt illusion using CSS perspective and rotational transforms, with a specular highlight that tracks the pointer position.
## HTML
```html
<div class="ih-12">
  <div class="ih-12__grid">
    <div class="ih-12__card" id="ih-12-card-1">
      <div class="ih-12__img ih-12__img--1">
        <span class="ih-12__icon">🔮</span>
        <div class="ih-12__shine"></div>
      </div>
      <div class="ih-12__body">
        <p class="ih-12__title">Mystic Artifacts</p>
        <p class="ih-12__sub">Interactive 3D collection</p>
      </div>
    </div>
    <div class="ih-12__card" id="ih-12-card-2">
      <div class="ih-12__img ih-12__img--2">
        <span class="ih-12__icon">🌿</span>
        <div class="ih-12__shine"></div>
      </div>
      <div class="ih-12__body">
        <p class="ih-12__title">Botanical Studies</p>
        <p class="ih-12__sub">Flora & fauna series</p>
      </div>
    </div>
    <div class="ih-12__card" id="ih-12-card-3">
      <div class="ih-12__img ih-12__img--3">
        <span class="ih-12__icon">🌊</span>
        <div class="ih-12__shine"></div>
      </div>
      <div class="ih-12__body">
        <p class="ih-12__title">Ocean Depths</p>
        <p class="ih-12__sub">Underwater photography</p>
      </div>
    </div>
  </div>
</div>
<script>
(function(){
  const cards = document.querySelectorAll('.ih-12__card');
  const INTENSITY = 18;
  cards.forEach(card => {
    const shine = card.querySelector('.ih-12__shine');
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width;
      const y = (e.clientY - r.top) / r.height;
      const rx = (y - 0.5) * -INTENSITY;
      const ry = (x - 0.5) * INTENSITY;
      card.style.transform = `perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg) scale3d(1.02,1.02,1.02)`;
      if(shine){
        shine.style.setProperty('--mx', (x*100)+'%');
        shine.style.setProperty('--my', (y*100)+'%');
      }
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)';
      card.style.transition = 'transform 0.5s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.3s ease';
      setTimeout(() => { card.style.transition = ''; }, 500);
    });
  });
})();
</script>
```
## CSS
```css
.ih-12,
.ih-12 *,
.ih-12 *::before,
.ih-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-12 ::selection {
  background: #38bdf8;
  color: #000;
}

.ih-12 {
  --accent: #38bdf8;
  --bg: #060a12;
  --text: #f1f5f9;
  --muted: #64748b;
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1200px;
}

.ih-12__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}

.ih-12__card {
  border-radius: 16px;
  overflow: hidden;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: box-shadow 0.3s ease;
  will-change: transform;
  /* transform applied by JS */
}

.ih-12__card:hover {
  box-shadow: 0 30px 80px rgba(0,0,0,0.6);
}

.ih-12__img {
  aspect-ratio: 3/4;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.ih-12__img--1 {
  background: linear-gradient(135deg,#0f0c29,#2d1b69,#7c3aed);
}

.ih-12__img--2 {
  background: linear-gradient(135deg,#022c22,#065f46,#10b981);
}

.ih-12__img--3 {
  background: linear-gradient(135deg,#0c1445,#1e3a8a,#3b82f6);
}

.ih-12__icon {
  font-size: 52px;
  opacity: 0.45;
  transition: opacity 0.3s ease;
}

.ih-12__card:hover .ih-12__icon {
  opacity: 0.2;
}
/* Specular shine layer — moves opposite to tilt for realism */

.ih-12__shine {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at var(--mx,50%) var(--my,50%), rgba(255,255,255,0.12) 0%, transparent 60%);
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
}

.ih-12__card:hover .ih-12__shine {
  opacity: 1;
}

.ih-12__body {
  padding: 14px;
  background: rgba(255,255,255,0.03);
  backdrop-filter: blur(2px);
}

.ih-12__title {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}

.ih-12__sub {
  font-size: 11px;
  color: var(--muted);
  margin-top: 3px;
}
```

## JavaScript
```js
(function(){
  const cards = document.querySelectorAll('.ih-12__card');
  const INTENSITY = 18;
  cards.forEach(card => {
    const shine = card.querySelector('.ih-12__shine');
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width;
      const y = (e.clientY - r.top) / r.height;
      const rx = (y - 0.5) * -INTENSITY;
      const ry = (x - 0.5) * INTENSITY;
      card.style.transform = `perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg) scale3d(1.02,1.02,1.02)`;
      if(shine){
        shine.style.setProperty('--mx', (x*100)+'%');
        shine.style.setProperty('--my', (y*100)+'%');
      }
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)';
      card.style.transition = 'transform 0.5s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.3s ease';
      setTimeout(() => { card.style.transition = ''; }, 500);
    });
  });
})();
```
