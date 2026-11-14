---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/blueprint-reveal/"
title: "Blueprint Reveal"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A product card where a circular wipe transforms the finished object into a technical blueprint drawing with dimension lines and specs."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blueprint Reveal
Source: https://codefronts.com/motion/css-card-hover-effects/blueprint-reveal/

A product card where a circular wipe transforms the finished object into a technical blueprint drawing with dimension lines and specs. Great for design, manufacturing, architecture, and engineering brands that want to show the craft behind the product.
## HTML
```html
<div class="card-28">
  <article class="card-28__card">
    <div class="card-28__product">
      <span class="card-28__meta" style="color:#5a6a7d;">MODEL · ARC-01</span>
      <div class="card-28__shape"></div>
      <div>
        <h2 class="card-28__title-p">Arc Pendant</h2>
        <p style="font-size:0.82rem;color:#5a6a7d;line-height:1.6;margin-top:0.4rem;">Hand-blown matte ceramic lamp.</p>
      </div>
    </div>
    <div class="card-28__blue">
      <span class="card-28__meta">DRAWING № 01 — REV C</span>
      <div class="card-28__draw"></div>
      <div>
        <h2 class="card-28__title-b">Arc Pendant<br>Cross-Section</h2>
        <p class="card-28__specs">Ø 130mm · cord 1.8m<br>E27 · 2700K · matte glaze<br>TOL ±0.5mm</p>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@500;700&family=Spline+Sans+Mono:wght@400;500&display=swap');

.card-28,
.card-28 *,
.card-28 *::before,
.card-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-28 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #e9ebee;
  font-family: 'Spline Sans Mono', monospace;
  padding: 2rem;
}

.card-28__card {
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 6px;
  cursor: pointer;
  overflow: hidden;
  background: #fdfdfb;
  border: 1px solid #d4d8de;
  box-shadow: 0 16px 36px rgba(30,50,80,0.15);
}

.card-28__product {
  position: absolute;
  inset: 0;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 2.4rem;
  color: #1a2533;
  background: radial-gradient(circle at 70% 20%, #f0f3f7, #fdfdfb 60%);
  transition: opacity 0.5s ease;
}

.card-28__shape {
  width: 130px;
  height: 130px;
  margin: 1rem auto;
  border-radius: 50% 50% 50% 12px;
  background: linear-gradient(145deg, #2d6cdf, #16306b);
  box-shadow: 0 14px 30px rgba(40,80,160,0.35);
}

.card-28__blue {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: #0d3b8c;
  background-image: linear-gradient(rgba(255,255,255,0.12) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.12) 1px, transparent 1px);
  background-size: 22px 22px;
  color: #cfe0ff;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  clip-path: circle(0% at 100% 0%);
  transition: clip-path 0.6s cubic-bezier(0.65,0,0.35,1);
}

.card-28__card:hover .card-28__blue {
  clip-path: circle(150% at 100% 0%);
}

.card-28__card:hover .card-28__product {
  opacity: 0;
}

.card-28__draw {
  width: 130px;
  height: 130px;
  margin: 1rem auto;
  border: 1.5px solid #9dc0ff;
  border-radius: 50% 50% 50% 12px;
  position: relative;
}

.card-28__draw::before,
.card-28__draw::after {
  content: "";
  position: absolute;
  background: #6f9aff;
}

.card-28__draw::before {
  left: -30px;
  right: -30px;
  top: 50%;
  height: 1px;
  background: repeating-linear-gradient(90deg, #6f9aff 0 6px, transparent 6px 10px);
}

.card-28__draw::after {
  top: -30px;
  bottom: -30px;
  left: 50%;
  width: 1px;
  background: repeating-linear-gradient(0deg, #6f9aff 0 6px, transparent 6px 10px);
}

.card-28__meta {
  font-size: 0.72rem;
  letter-spacing: 0.16em;
}

.card-28__title-p {
  font-family: 'Archivo', sans-serif;
  font-weight: 700;
  font-size: 2rem;
  line-height: 1;
}

.card-28__title-b {
  font-family: 'Archivo', sans-serif;
  font-weight: 700;
  font-size: 1.6rem;
  line-height: 1.05;
}

.card-28__specs {
  font-size: 0.74rem;
  line-height: 1.7;
  color: #aecaff;
}

@media (prefers-reduced-motion: reduce) {
  .card-28__product,
    .card-28__blue {
    transition: none !important;
  }
}
```
