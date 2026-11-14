---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/perspective-deck/"
title: "Perspective Deck"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A tunnel of glassmorphic sci-fi panels receding into depth with neon edges."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Perspective Deck
Source: https://codefronts.com/components/css-stacked-cards/perspective-deck/

A tunnel of glassmorphic sci-fi panels receding into depth with neon edges. Hover tilts the whole stack in 3D and pushes the front card toward you. Suited to dashboards, status boards, and tech product pages.
## HTML
```html
<div class="scd-33">
  <div class="scd-33__stage">
    <div class="scd-33__deck">
      <div class="scd-33__card"><h3>SECTOR 01</h3><p>Active node // online</p></div>
      <div class="scd-33__card"><h3>SECTOR 02</h3><p>Buffered // standby</p></div>
      <div class="scd-33__card"><h3>SECTOR 03</h3><p>Cached // idle</p></div>
      <div class="scd-33__card"><h3>SECTOR 04</h3><p>Archived // sleep</p></div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Rajdhani:wght@500&display=swap');

.scd-33,
.scd-33 *,
.scd-33 *::before,
.scd-33 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-33 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 50%,#10131f,#05060a);
  font-family: 'Rajdhani', sans-serif;
}

.scd-33__stage {
  perspective: 900px;
  width: 300px;
  height: 380px;
}

.scd-33__deck {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .8s ease;
}

.scd-33__card {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  background: linear-gradient(155deg,rgba(40,52,90,.9),rgba(18,22,40,.95));
  border: 1px solid rgba(120,170,255,.35);
  box-shadow: 0 0 40px rgba(70,120,255,.18);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 26px;
  color: #cfe0ff;
  backdrop-filter: blur(2px);
  transition: transform .8s cubic-bezier(.2,.8,.2,1), opacity .8s;
}

.scd-33__card h3 {
  font-family: 'Orbitron', sans-serif;
  font-size: 1.3rem;
  letter-spacing: .08em;
}

.scd-33__card p {
  opacity: .6;
  font-size: .95rem;
  letter-spacing: .05em;
}

.scd-33__card:nth-child(1) {
  transform: translateZ(0px);
}

.scd-33__card:nth-child(2) {
  transform: translateZ(-80px) translateY(-26px);
  opacity: .85;
}

.scd-33__card:nth-child(3) {
  transform: translateZ(-160px) translateY(-52px);
  opacity: .6;
}

.scd-33__card:nth-child(4) {
  transform: translateZ(-240px) translateY(-78px);
  opacity: .4;
}

.scd-33__stage:hover .scd-33__deck {
  transform: rotateX(18deg) rotateY(-12deg);
}

.scd-33__stage:hover .scd-33__card:nth-child(1) {
  transform: translateZ(60px);
}

@media (prefers-reduced-motion: reduce) {
  .scd-33__deck,
    .scd-33__card {
    transition: none !important;
  }
}
```
