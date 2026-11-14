---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/flip-card/"
title: "Flip Card"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A credit-card-style component that performs a full 180° 3D flip to reveal the reverse face, complete with magnetic strip and CVV."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flip Card
Source: https://codefronts.com/motion/css-card-hover-effects/flip-card/

A credit-card-style component that performs a full 180° 3D flip to reveal the reverse face, complete with magnetic strip and CVV. Ideal for fintech, membership cards, profiles, or any front/back information pairing.
## HTML
```html
<div class="card-19">
  <article class="card-19__card">
    <div class="card-19__face card-19__front">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div class="card-19__front-logo">◈</div>
        <span style="font-family:'IBM Plex Mono';font-size:0.75rem;letter-spacing:0.2em;">PLATINUM</span>
      </div>
      <div class="card-19__front-num">4921 ·· 7755 ·· 0042</div>
      <div class="card-19__front-row">
        <span class="card-19__front-name">A. Marlowe</span>
        <span>12/29</span>
      </div>
    </div>
    <div class="card-19__face card-19__back">
      <div class="card-19__back-strip"></div>
      <h2 class="card-19__back-title">Flip to<br>the back</h2>
      <p class="card-19__back-desc">Same card, two faces. A full 180° rotation reveals account details on the reverse.</p>
      <span class="card-19__back-cvv">··· 309</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;600;800&family=IBM+Plex+Mono:wght@400;500&display=swap');

.card-19,
.card-19 *,
.card-19 *::before,
.card-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-19 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #0e1116;
  font-family: 'Libre Franklin', sans-serif;
  padding: 2rem;
  perspective: 1500px;
}

.card-19__card {
  width: 330px;
  height: 440px;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.7s cubic-bezier(0.4, 0.2, 0.2, 1);
  position: relative;
}

.card-19__card:hover {
  transform: rotateY(180deg);
}

.card-19__face {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 20px 45px rgba(0,0,0,0.45);
}

.card-19__front {
  background: linear-gradient(160deg, #12806a, #064237);
  color: #eafff7;
}

.card-19__front-logo {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: #eafff7;
  color: #064237;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.3rem;
}

.card-19__front-num {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 1.4rem;
  letter-spacing: 0.16em;
}

.card-19__front-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  font-size: 0.78rem;
}

.card-19__front-name {
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.card-19__back {
  background: linear-gradient(160deg, #1a1f29, #0c0f14);
  color: #dfe4ec;
  transform: rotateY(180deg);
}

.card-19__back-strip {
  height: 46px;
  background: #000;
  margin: 0 -2.4rem;
}

.card-19__back-title {
  font-weight: 800;
  font-size: 1.6rem;
  line-height: 1.1;
}

.card-19__back-desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #9aa3b2;
}

.card-19__back-cvv {
  font-family: 'IBM Plex Mono', monospace;
  background: #e8ecf3;
  color: #0c0f14;
  align-self: flex-end;
  padding: 0.3rem 0.9rem;
  border-radius: 6px;
  letter-spacing: 0.2em;
  font-weight: 500;
}

@media (prefers-reduced-motion: reduce) {
  .card-19__card {
    transition: none !important;
  }
}
```
