---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/css-grid-responsive-team-member-row/"
title: "CSS Grid Responsive Team Member Row"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A four-across team row that reflows to two columns on narrow screens, dimming every sibling card while the hovered one lifts and highlights."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Responsive Team Member Row
Source: https://codefronts.com/components/css-profile-cards/css-grid-responsive-team-member-row/

A four-across team row that reflows to two columns on narrow screens, dimming every sibling card while the hovered one lifts and highlights.
## HTML
```html
<div class="pc-07">
  <div class="pc-07__grid">
    <article class="pc-07__card" style="--h:275">
      <div class="pc-07__pfp">AL</div>
      <h3>Amara Liu</h3><p>Backend</p>
      <span class="pc-07__dot"></span>
    </article>
    <article class="pc-07__card" style="--h:200">
      <div class="pc-07__pfp">DV</div>
      <h3>Deepa V.</h3><p>ML Research</p>
      <span class="pc-07__dot"></span>
    </article>
    <article class="pc-07__card" style="--h:330">
      <div class="pc-07__pfp">RK</div>
      <h3>Rui Koda</h3><p>Design Sys</p>
      <span class="pc-07__dot"></span>
    </article>
    <article class="pc-07__card" style="--h:150">
      <div class="pc-07__pfp">MB</div>
      <h3>Marco B.</h3><p>DevOps</p>
      <span class="pc-07__dot"></span>
    </article>
  </div>
</div>
```
## CSS
```css
.pc-07,
.pc-07 *,
.pc-07 *::before,
.pc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-07 ::selection {
  background: #00e0a4;
  color: #062;
}

.pc-07 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #08120f;
  color: #eafff7;
}

.pc-07__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 14px;
  max-width: 640px;
  width: 100%;
}

.pc-07__card {
  position: relative;
  background: linear-gradient(160deg,#0f2620,#0c1c18);
  border: 1px solid #163a30;
  border-radius: 20px;
  padding: 22px 16px;
  text-align: center;
  box-shadow: 0 14px 34px -16px rgba(0,0,0,.7);
  transition: transform .4s cubic-bezier(.2,.8,.2,1),filter .4s,opacity .4s,box-shadow .4s;
}

.pc-07__grid:hover .pc-07__card {
  opacity: .5;
  filter: saturate(.6) brightness(.8);
}

.pc-07__grid .pc-07__card:hover {
  opacity: 1;
  filter: none;
  transform: translateY(-8px) scale(1.04);
  box-shadow: 0 26px 50px -18px rgba(0,224,164,.4);
  border-color: #00e0a4;
}

.pc-07__pfp {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  margin: 0 auto 12px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.15rem;
  color: #062;
  background: conic-gradient(from calc(var(--h) * 1deg),#00e0a4,#00b4dc,#00e0a4);
}

.pc-07__card h3 {
  font-size: 1rem;
  font-weight: 800;
}

.pc-07__card p {
  font-size: .76rem;
  color: #7fd9c4;
  margin-top: 2px;
}

.pc-07__dot {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #00e0a4;
  box-shadow: 0 0 10px #00e0a4;
  animation: pc-07-blink 2s ease-in-out infinite;
}

@keyframes pc-07-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .3;
  }
}

@media (max-width: 560px) {
  .pc-07__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .pc-07 * {
    animation: none!important;
    transition: opacity .3s,filter .3s!important;
  }
}
```
