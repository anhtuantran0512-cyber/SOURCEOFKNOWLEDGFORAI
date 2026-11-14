---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-fullscreen-background-image-hover/"
title: "CSS Fullscreen Background Image Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Navigation hover that swaps the entire viewport background by toggling an is-active class on one of several stacked background panels."
has_js: "true"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Fullscreen Background Image Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-fullscreen-background-image-hover/

Navigation hover that swaps the entire viewport background by toggling an is-active class on one of several stacked background panels.
## HTML
```html
<div class="ih-17" id="ih-17-root">
  <div class="ih-17__bg ih-17__bg--0 is-active" data-bg="0"></div>
  <div class="ih-17__bg ih-17__bg--1" data-bg="1"></div>
  <div class="ih-17__bg ih-17__bg--2" data-bg="2"></div>
  <div class="ih-17__bg ih-17__bg--3" data-bg="3"></div>
  <div class="ih-17__bg ih-17__bg--4" data-bg="4"></div>
  <div class="ih-17__bg ih-17__bg--5" data-bg="5"></div>

  <nav class="ih-17__nav">
    <p class="ih-17__kicker">Navigate · hover to preview</p>
    <ul class="ih-17__list">
      <li><a class="ih-17__link" data-target="1" href="#">
        <span class="ih-17__num">01</span>
        <span class="ih-17__emoji">🌌</span>
        <span class="ih-17__label">Deep Universe</span>
        <span class="ih-17__arrow">→</span>
      </a></li>
      <li><a class="ih-17__link" data-target="2" href="#">
        <span class="ih-17__num">02</span>
        <span class="ih-17__emoji">🌿</span>
        <span class="ih-17__label">Wild Canopy</span>
        <span class="ih-17__arrow">→</span>
      </a></li>
      <li><a class="ih-17__link" data-target="3" href="#">
        <span class="ih-17__num">03</span>
        <span class="ih-17__emoji">🏜️</span>
        <span class="ih-17__label">Desert Dunes</span>
        <span class="ih-17__arrow">→</span>
      </a></li>
      <li><a class="ih-17__link" data-target="4" href="#">
        <span class="ih-17__num">04</span>
        <span class="ih-17__emoji">🔮</span>
        <span class="ih-17__label">Violet Dreams</span>
        <span class="ih-17__arrow">→</span>
      </a></li>
      <li><a class="ih-17__link" data-target="5" href="#">
        <span class="ih-17__num">05</span>
        <span class="ih-17__emoji">🌊</span>
        <span class="ih-17__label">Ocean Horizon</span>
        <span class="ih-17__arrow">→</span>
      </a></li>
    </ul>
  </nav>
</div>
<script>
(function(){
  const root = document.getElementById('ih-17-root');
  if(!root)return;
  const links = root.querySelectorAll('.ih-17__link');
  const bgs = root.querySelectorAll('.ih-17__bg');
  function activate(idx){
    bgs.forEach(b=>{b.classList.toggle('is-active',b.dataset.bg===String(idx))});
  }
  links.forEach(link=>{
    link.addEventListener('mouseenter',()=>activate(link.dataset.target));
    link.addEventListener('mouseleave',()=>activate(0));
    link.addEventListener('click',e=>e.preventDefault());
  });
})();
</script>
```
## CSS
```css
.ih-17,
.ih-17 *,
.ih-17 *::before,
.ih-17 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-17 ::selection {
  background: #f472b6;
  color: #000;
}

.ih-17 {
  --accent: #f472b6;
  --bg: #06060a;
  --text: #f1f5f9;
  --muted: #64748b;
  --duration: 0.6s;
  --ease: cubic-bezier(0.16,1,0.3,1);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  position: relative;
  overflow: hidden;
}
/* Background panels — opacity cross-fade controlled by JS data-active */

.ih-17__bg {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity var(--duration) var(--ease),transform var(--duration) var(--ease);
  transform: scale(1.04);
  pointer-events: none;
}

.ih-17__bg.is-active {
  opacity: 1;
  transform: scale(1);
}

.ih-17__bg--0 {
  background: linear-gradient(135deg,#060606,#111);
}

.ih-17__bg--1 {
  background: linear-gradient(135deg,#0f0c29,#302b63,#24243e);
}

.ih-17__bg--2 {
  background: linear-gradient(135deg,#042f2e,#065f46,#059669);
}

.ih-17__bg--3 {
  background: linear-gradient(135deg,#1c1003,#451a03,#92400e);
}

.ih-17__bg--4 {
  background: linear-gradient(135deg,#1a0533,#4c1d95,#7c3aed);
}

.ih-17__bg--5 {
  background: linear-gradient(135deg,#0c1445,#1e3a8a,#1d4ed8);
}
/* Foreground nav list */

.ih-17__nav {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 100vh;
  padding: 40px;
}

.ih-17__kicker {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 20px;
}

.ih-17__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ih-17__link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease,color 0.2s ease;
  text-decoration: none;
}

.ih-17__link:hover,
.ih-17__link.is-active {
  background: rgba(255,255,255,0.06);
}

.ih-17__num {
  font-size: 11px;
  color: var(--muted);
  font-weight: 600;
  width: 22px;
  flex-shrink: 0;
}

.ih-17__label {
  font-size: 20px;
  font-weight: 800;
  color: rgba(255,255,255,0.25);
  transition: color var(--duration) var(--ease), transform var(--duration) var(--ease);
  letter-spacing: -0.02em;
}

.ih-17__link:hover .ih-17__label,
.ih-17__link.is-active .ih-17__label {
  color: var(--text);
  transform: translateX(6px);
}

.ih-17__arrow {
  margin-left: auto;
  opacity: 0;
  color: var(--accent);
  font-size: 16px;
  transform: translateX(-8px);
  transition: opacity 0.2s ease,transform 0.2s ease;
}

.ih-17__link:hover .ih-17__arrow,
.ih-17__link.is-active .ih-17__arrow {
  opacity: 1;
  transform: none;
}

.ih-17__emoji {
  font-size: 14px;
}
```

## JavaScript
```js
(function(){
  const root = document.getElementById('ih-17-root');
  if(!root)return;
  const links = root.querySelectorAll('.ih-17__link');
  const bgs = root.querySelectorAll('.ih-17__bg');
  function activate(idx){
    bgs.forEach(b=>{b.classList.toggle('is-active',b.dataset.bg===String(idx))});
  }
  links.forEach(link=>{
    link.addEventListener('mouseenter',()=>activate(link.dataset.target));
    link.addEventListener('mouseleave',()=>activate(0));
    link.addEventListener('click',e=>e.preventDefault());
  });
})();
```
