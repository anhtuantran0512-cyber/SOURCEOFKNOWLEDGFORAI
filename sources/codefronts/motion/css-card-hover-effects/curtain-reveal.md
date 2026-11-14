---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/curtain-reveal/"
title: "Curtain Reveal"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A theater/event card where two striped velvet curtain halves part on hover to unveil the content behind, complete with a gold seam."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Curtain Reveal
Source: https://codefronts.com/motion/css-card-hover-effects/curtain-reveal/

A theater/event card where two striped velvet curtain halves part on hover to unveil the content behind, complete with a gold seam. Best for performing-arts, cinema, launch, or "reveal" moments where anticipation is part of the message.
## HTML
```html
<div class="card-11">
  <article class="card-11__card">
    <div class="card-11__back">
      <span class="card-11__num">— ACT III —</span>
      <h2 class="card-11__title">The Velvet<br>Hour</h2>
      <p class="card-11__desc">An evening of chamber music and candlelight. Doors open at eight.</p>
    </div>
    <div class="card-11__half card-11__left"></div>
    <div class="card-11__half card-11__right"></div>
    <div class="card-11__seam"></div>
    <span class="card-11__label">Hover to part the curtain</span>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,800;1,500&family=Cormorant+Garamond:wght@400;500&display=swap');

.card-11,
.card-11 *,
.card-11 *::before,
.card-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-11 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #1a0d12;
  font-family: 'Cormorant Garamond', serif;
  padding: 2rem;
}

.card-11__card {
  position: relative;
  width: 340px;
  height: 460px;
  border-radius: 6px;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}

.card-11__back {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(20,8,12,0.55), rgba(20,8,12,0.75)), radial-gradient(circle at 50% 35%, #5a2030, #1a0d12 70%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 2.5rem;
  color: #f3e3d3;
}

.card-11__num {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 1rem;
  letter-spacing: 0.2em;
  color: #d4a373;
}

.card-11__title {
  font-family: 'Playfair Display', serif;
  font-weight: 800;
  font-size: 2.6rem;
  line-height: 1.05;
  margin: 0.6rem 0 1rem;
}

.card-11__desc {
  font-size: 1.15rem;
  line-height: 1.5;
  color: #cbb8a6;
}

.card-11__half {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 50%;
  background: repeating-linear-gradient(90deg, #7a1f2b 0 10px, #5e1620 10px 20px);
  z-index: 2;
  transition: transform 0.7s cubic-bezier(0.77, 0, 0.18, 1);
  box-shadow: inset 0 0 40px rgba(0,0,0,0.4);
}

.card-11__half.card-11__left {
  left: 0;
  transform-origin: left;
}

.card-11__half.card-11__right {
  right: 0;
  transform-origin: right;
}

.card-11__half::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgba(0,0,0,0.25));
}

.card-11__half.card-11__right::after {
  background: linear-gradient(270deg, transparent, rgba(0,0,0,0.25));
}

.card-11__card:hover .card-11__half.card-11__left {
  transform: translateX(-100%);
}

.card-11__card:hover .card-11__half.card-11__right {
  transform: translateX(100%);
}

.card-11__seam {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 2px;
  background: linear-gradient(#d4a373, #8a5a2b);
  transform: translateX(-50%);
  z-index: 3;
  opacity: 0.8;
  transition: opacity 0.4s ease;
}

.card-11__card:hover .card-11__seam {
  opacity: 0;
}

.card-11__label {
  position: absolute;
  bottom: 1.4rem;
  left: 0;
  right: 0;
  text-align: center;
  z-index: 4;
  font-family: 'Playfair Display', serif;
  font-style: italic;
  color: #f3e3d3;
  font-size: 1.1rem;
  letter-spacing: 0.1em;
  transition: opacity 0.3s ease;
}

.card-11__card:hover .card-11__label {
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .card-11__half,
    .card-11__seam,
    .card-11__label {
    transition: none !important;
  }
}
```
