---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/peel-back/"
title: "Peel Back"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "The top sticker-card curls away at the corner like peeling a label, revealing layers beneath."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Peel Back
Source: https://codefronts.com/components/css-stacked-cards/peel-back/

The top sticker-card curls away at the corner like peeling a label, revealing layers beneath. Vivid gradients with a folded-corner shadow. Eye-catching for reveals, "what’s inside" teasers, or onboarding.
## HTML
```html
<div class="scd-34">
  <div class="scd-34__stage">
    <div class="scd-34__card scd-34__card--c3"><div class="scd-34__inner"><h3>Layer C</h3><p>Bottom of the stack</p></div></div>
    <div class="scd-34__card scd-34__card--c2"><div class="scd-34__inner"><h3>Layer B</h3><p>The middle ground</p></div></div>
    <div class="scd-34__card scd-34__card--c1"><div class="scd-34__inner"><h3>Peel me</h3><p>Hover to lift the top</p></div></div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@700;800&family=Outfit:wght@400&display=swap');

.scd-34,
.scd-34 *,
.scd-34 *::before,
.scd-34 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-34 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #ececec;
  font-family: 'Outfit', sans-serif;
}

.scd-34__stage {
  position: relative;
  width: 260px;
  height: 340px;
}

.scd-34__card {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  box-shadow: 0 12px 26px rgba(0,0,0,.18);
  transition: transform .7s cubic-bezier(.2,.8,.2,1), border-radius .7s;
  transform-origin: top right;
  cursor: pointer;
  overflow: hidden;
}

.scd-34__inner {
  position: absolute;
  inset: 0;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  color: #fff;
}

.scd-34__card h3 {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 2rem;
  line-height: 1;
}

.scd-34__card p {
  opacity: .85;
  margin-top: 6px;
}

.scd-34__card--c1 {
  background: linear-gradient(150deg,#ff6a3d,#f9484a);
  z-index: 3;
}

.scd-34__card--c2 {
  background: linear-gradient(150deg,#1fa2ff,#12d8fa);
  z-index: 2;
}

.scd-34__card--c3 {
  background: linear-gradient(150deg,#43e97b,#38f9d7);
  z-index: 1;
  color: #063;
}

.scd-34__stage:hover .scd-34__card--c1 {
  transform: rotate(-14deg) translate(-30px,-30px) scale(.78);
  border-radius: 22px 22px 22px 90px;
  box-shadow: -20px 20px 40px rgba(0,0,0,.3);
}

.scd-34__stage:hover .scd-34__card--c2 {
  transform: translateY(-10px);
}

@media (prefers-reduced-motion: reduce) {
  .scd-34__card {
    transition: none !important;
  }
}
```
