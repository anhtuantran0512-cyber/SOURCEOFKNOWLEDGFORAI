---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-3d-flip-card-animation/"
title: "CSS 3D Flip Card Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Four CSS 3D card flip animations: auto-flip Y-axis, hover-triggered flip, X-axis flip and diagonal flip using CSS perspective and rotateY/X keyframes."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Flip Card Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-3d-flip-card-animation/

Four CSS 3D card flip animations: auto-flip Y-axis, hover-triggered flip, X-axis flip and diagonal flip using CSS perspective and rotateY/X keyframes.
## HTML
```html
<div class="kf-08">
  <div class="kf-08__grid">

    <div class="kf-08__cell">
      <div class="kf-08__card">
        <div class="kf-08__inner kf-08__inner--auto">
          <div class="kf-08__front kf-08__f1">
            <span class="icon">🎧</span>
            <h3>Pro Headset X</h3>
            <p>Studio quality. Wireless freedom.</p>
          </div>
          <div class="kf-08__back kf-08__b1">
            <div class="price">$129</div>
            <div class="cta">Buy Now</div>
          </div>
        </div>
      </div>
      <span class="kf-08__label">Auto Flip Y</span>
    </div>

    <div class="kf-08__cell">
      <div class="kf-08__card">
        <div class="kf-08__inner kf-08__inner--hover">
          <div class="kf-08__front kf-08__f2">
            <div class="avatar">👩‍🎨</div>
            <h3>Mara Solano</h3>
            <small>Creative Director</small>
          </div>
          <div class="kf-08__back kf-08__b2">
            <div class="stats">
              <div class="stat"><b>142</b><small>Projects</small></div>
              <div class="stat"><b>98%</b><small>Rating</small></div>
            </div>
          </div>
        </div>
      </div>
      <span class="kf-08__label">Hover Flip</span>
    </div>

    <div class="kf-08__cell">
      <div class="kf-08__card">
        <div class="kf-08__inner kf-08__inner--x">
          <div class="kf-08__front kf-08__f3">
            <span class="icon">✨</span>
            <h3>Magic Card</h3>
          </div>
          <div class="kf-08__back kf-08__b3 kf-08__back--x">
            <p>Flip on the X axis for a fresh perspective on card reveals.</p>
          </div>
        </div>
      </div>
      <span class="kf-08__label">Flip X Axis</span>
    </div>

    <div class="kf-08__cell">
      <div class="kf-08__card">
        <div class="kf-08__inner kf-08__inner--diag">
          <div class="kf-08__front kf-08__f4">
            <div class="num">42</div>
            <p>Diagonal axis flip</p>
          </div>
          <div class="kf-08__back kf-08__b4 kf-08__back--diag">
            <span class="check">✅</span>
            <p>Task complete!</p>
          </div>
        </div>
      </div>
      <span class="kf-08__label">Diagonal Flip</span>
    </div>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700;900&display=swap');

.kf-08,
.kf-08 *,
.kf-08 *::before,
.kf-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-08 ::selection {
  background: #f4a261;
  color: #fff;
}

.kf-08 {
  --bg: #1c1c1e;
  --orange: #f4a261;
  --teal: #2a9d8f;
  --sand: #e9c46a;
  --red: #e76f51;
  --blue: #264653;
  --white: #f8f9fa;
  font-family: 'Raleway',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 48px;
  color: var(--white);
}

.kf-08__grid {
  display: flex;
  gap: 32px;
  flex-wrap: wrap;
  justify-content: center;
}

.kf-08__label {
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #666;
  text-align: center;
}

.kf-08__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}
/* 3D card base */

.kf-08__card {
  perspective: 800px;
  width: 180px;
  height: 240px;
  cursor: pointer;
}

.kf-08__inner {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .6s ease;
}

.kf-08__front,
.kf-08__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 24px;
}

.kf-08__back {
  transform: rotateY(180deg);
}
/* Auto-flip animation */

.kf-08__inner--auto {
  animation: kf-08-flip 4s ease-in-out infinite;
}

@keyframes kf-08-flip {
  0%,
    40% {
    transform: rotateY(0deg);
  }

  50%,
    90% {
    transform: rotateY(180deg);
  }

  100% {
    transform: rotateY(0deg);
  }
}
/* Hover flip */

.kf-08__card:hover .kf-08__inner--hover {
  transform: rotateY(180deg);
}
/* X-axis flip */

.kf-08__inner--x {
  animation: kf-08-flipx 4s ease-in-out infinite 1s;
}

@keyframes kf-08-flipx {
  0%,
    40% {
    transform: rotateX(0deg);
  }

  50%,
    90% {
    transform: rotateX(180deg);
  }

  100% {
    transform: rotateX(0deg);
  }
}

.kf-08__back--x {
  transform: rotateX(180deg);
}
/* 4 — diagonal flip */

.kf-08__inner--diag {
  animation: kf-08-diag 4s ease-in-out infinite 0.5s;
}

@keyframes kf-08-diag {
  0%,
    40% {
    transform: rotate3d(1,1,0,0deg);
  }

  50%,
    90% {
    transform: rotate3d(1,1,0,180deg);
  }

  100% {
    transform: rotate3d(1,1,0,0deg);
  }
}

.kf-08__back--diag {
  transform: rotate3d(1,1,0,180deg);
}
/* Card 1 — Product card */

.kf-08__f1 {
  background: linear-gradient(135deg,#264653,#2a9d8f);
  box-shadow: 0 20px 40px rgba(0,0,0,.4);
}

.kf-08__f1 .icon {
  font-size: 3rem;
}

.kf-08__f1 h3 {
  font-size: 1.1rem;
  font-weight: 900;
  text-align: center;
}

.kf-08__f1 p {
  font-size: .8rem;
  opacity: .7;
  text-align: center;
}

.kf-08__b1 {
  background: linear-gradient(135deg,#e9c46a,#f4a261);
  color: #1c1c1e;
  box-shadow: 0 20px 40px rgba(0,0,0,.4);
}

.kf-08__b1 .price {
  font-size: 2.2rem;
  font-weight: 900;
}

.kf-08__b1 .cta {
  background: #1c1c1e;
  color: #f4a261;
  border-radius: 8px;
  padding: 8px 20px;
  font-weight: 700;
  font-size: .85rem;
}
/* Card 2 — Profile card */

.kf-08__f2 {
  background: linear-gradient(135deg,#e76f51,#f4a261);
  box-shadow: 0 20px 40px rgba(231,111,81,.3);
}

.kf-08__f2 .avatar {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: rgba(255,255,255,.3);
  display: grid;
  place-items: center;
  font-size: 2.2rem;
}

.kf-08__f2 h3 {
  font-weight: 900;
}

.kf-08__f2 small {
  opacity: .7;
  font-size: .8rem;
}

.kf-08__b2 {
  background: linear-gradient(135deg,#264653,#023e8a);
  box-shadow: 0 20px 40px rgba(0,0,0,.4);
}

.kf-08__b2 .stat {
  text-align: center;
}

.kf-08__b2 .stat b {
  display: block;
  font-size: 1.6rem;
  font-weight: 900;
  color: var(--sand);
}

.kf-08__b2 .stat small {
  font-size: .7rem;
  opacity: .6;
}

.kf-08__b2 .stats {
  display: flex;
  gap: 16px;
}
/* Card 3 */

.kf-08__f3 {
  background: linear-gradient(135deg,#7b2d8b,#c264f0);
  box-shadow: 0 20px 40px rgba(123,45,139,.4);
}

.kf-08__f3 .icon {
  font-size: 3rem;
}

.kf-08__f3 h3 {
  font-weight: 900;
  font-size: 1.2rem;
  text-align: center;
}

.kf-08__b3 {
  background: linear-gradient(135deg,#ff6b6b,#ffd166);
  color: #1c1c1e;
  box-shadow: 0 20px 40px rgba(0,0,0,.3);
}

.kf-08__b3 p {
  font-size: .88rem;
  text-align: center;
  line-height: 1.5;
}
/* Card 4 — diagonal */

.kf-08__f4 {
  background: linear-gradient(135deg,#0d1b2a,#1b4332);
  box-shadow: 0 20px 40px rgba(0,0,0,.5);
  border: 1px solid rgba(255,255,255,.05);
}

.kf-08__f4 .num {
  font-size: 4rem;
  font-weight: 900;
  color: var(--teal);
  line-height: 1;
}

.kf-08__f4 p {
  font-size: .8rem;
  opacity: .5;
  text-align: center;
}

.kf-08__b4 {
  background: linear-gradient(135deg,#2d6a4f,#40916c);
  box-shadow: 0 20px 40px rgba(0,0,0,.4);
}

.kf-08__b4 .check {
  font-size: 2.5rem;
}

.kf-08__b4 p {
  font-size: .9rem;
  text-align: center;
  font-weight: 700;
}

@media (max-width: 500px) {
  .kf-08__card {
    width: 150px;
    height: 200px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-08 * {
    animation: none!important;
    transition: none!important;
  }
}
```
