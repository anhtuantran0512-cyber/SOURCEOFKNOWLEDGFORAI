---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/vibrant-gradient-border-profile-card/"
title: "Vibrant Gradient Border Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A minimal dark card wrapped in a glowing Instagram/Stripe-style gradient border created by a rotating conic gradient behind a padding-inset inner panel."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vibrant Gradient Border Profile Card
Source: https://codefronts.com/components/css-profile-cards/vibrant-gradient-border-profile-card/

A minimal dark card wrapped in a glowing Instagram/Stripe-style gradient border created by a rotating conic gradient behind a padding-inset inner panel.
## HTML
```html
<div class="pc-13">
  <div class="pc-13__card">
    <div class="pc-13__inner">
      <div class="pc-13__pfp">IZ</div>
      <div class="pc-13__id">
        <h3>Iris Zhang</h3>
        <p>Content Creator</p>
      </div>
      <p class="pc-13__bio">Sharing daily design tips to 240k makers. Sponsored by curiosity.</p>
      <div class="pc-13__foot">
        <span class="pc-13__followers"><b>240k</b> followers</span>
        <button class="pc-13__cta">Subscribe</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-13,
.pc-13 *,
.pc-13 *::before,
.pc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-13 ::selection {
  background: #fd5949;
  color: #fff;
}

.pc-13 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #0f0d14;
  color: #fff;
}

.pc-13__card {
  position: relative;
  width: 310px;
  border-radius: 24px;
  padding: 2.5px;
  overflow: hidden;
}

.pc-13__card::before {
  content: '';
  position: absolute;
  inset: -40%;
  z-index: 0;
  background: conic-gradient(from 0deg,#feda75,#fa7e1e,#d62976,#962fbf,#4f5bd5,#feda75);
  animation: pc-13-rot 5s linear infinite;
}

@keyframes pc-13-rot {
  to {
    transform: rotate(360deg);
  }
}

.pc-13__inner {
  position: relative;
  z-index: 1;
  border-radius: 22px;
  padding: 26px;
  background: #16131e;
}

.pc-13__pfp {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.4rem;
  color: #fff;
  background: linear-gradient(135deg,#d62976,#feda75);
}

.pc-13__id {
  margin-top: 16px;
}

.pc-13__id h3 {
  font-size: 1.35rem;
  font-weight: 800;
}

.pc-13__id p {
  color: rgba(255,255,255,.55);
  font-size: .85rem;
  margin-top: 2px;
}

.pc-13__bio {
  font-size: .85rem;
  line-height: 1.5;
  color: rgba(255,255,255,.8);
  margin-top: 14px;
  text-wrap: balance;
}

.pc-13__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 22px;
}

.pc-13__followers {
  font-size: .82rem;
  color: rgba(255,255,255,.6);
}

.pc-13__followers b {
  color: #fff;
}

.pc-13__cta {
  padding: 10px 22px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  font-size: .85rem;
  color: #fff;
  background: linear-gradient(135deg,#d62976,#fa7e1e);
  box-shadow: 0 8px 20px -8px #d62976;
  transition: transform .2s,filter .25s;
}

.pc-13__cta:hover {
  filter: brightness(1.1);
}

.pc-13__cta:active {
  transform: scale(.96);
}

@media (prefers-reduced-motion: reduce) {
  .pc-13__card::before {
    animation: none;
  }
}
```
