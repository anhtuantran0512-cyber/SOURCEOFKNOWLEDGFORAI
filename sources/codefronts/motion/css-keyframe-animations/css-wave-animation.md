---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-wave-animation/"
title: "CSS Wave Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Ocean waves with animated boat, gradient wave, liquid-level vial and expanding pulse rings using CSS clip-path and sinusoidal keyframe paths."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Wave Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-wave-animation/

Ocean waves with animated boat, gradient wave, liquid-level vial and expanding pulse rings using CSS clip-path and sinusoidal keyframe paths.
## HTML
```html
<div class="kf-07">
  <div class="kf-07__cell" style="width:100%;max-width:700px">
    <div class="kf-07__ocean">
      <div class="kf-07__wave kf-07__wave--1"></div>
      <div class="kf-07__wave kf-07__wave--2"></div>
      <div class="kf-07__wave kf-07__wave--3"></div>
      <div class="kf-07__ship">⛵</div>
    </div>
    <span class="kf-07__label">Ocean Waves</span>
  </div>

  <div class="kf-07__cell" style="width:100%;max-width:600px">
    <div class="kf-07__grad-wave">
      <div class="kf-07__grad-text">FLOWING</div>
    </div>
    <span class="kf-07__label">Gradient Wave</span>
  </div>

  <div class="kf-07__row">
    <div class="kf-07__cell">
      <div class="kf-07__vial"><div class="kf-07__liquid"></div><div class="kf-07__pct">65%</div></div>
      <span class="kf-07__label">Liquid Level</span>
    </div>
    <div class="kf-07__cell">
      <div class="kf-07__rings">
        <div class="kf-07__ring"></div><div class="kf-07__ring"></div>
        <div class="kf-07__ring"></div><div class="kf-07__ring"></div>
      </div>
      <span class="kf-07__label">Pulse Rings</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&display=swap');

.kf-07,
.kf-07 *,
.kf-07 *::before,
.kf-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-07 ::selection {
  background: #0077b6;
  color: #fff;
}

.kf-07 {
  --bg: #03045e;
  --deep: #0077b6;
  --mid: #00b4d8;
  --light: #90e0ef;
  --foam: #caf0f8;
  --white: #fff;
  --gold: #ffd60a;
  font-family: 'DM Sans',sans-serif;
  background: linear-gradient(180deg,#03045e 0%,#0096c7 60%,#00b4d8 100%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 56px;
  overflow: hidden;
  position: relative;
  color: var(--white);
}
/* 1 — Ocean waves stacked */

.kf-07__ocean {
  position: relative;
  width: 100%;
  max-width: 700px;
  height: 180px;
  background: linear-gradient(180deg,rgba(0,150,199,.3),rgba(0,77,110,.6));
  border-radius: 12px;
  overflow: hidden;
}

.kf-07__wave {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--mid);
  border-radius: 100% 100% 0 0/40px;
}

.kf-07__wave--1 {
  height: 60px;
  background: rgba(0,180,216,.7);
  animation: kf-07-wave1 4s ease-in-out infinite;
}

.kf-07__wave--2 {
  height: 50px;
  background: rgba(144,224,239,.5);
  animation: kf-07-wave2 5s ease-in-out infinite .3s;
}

.kf-07__wave--3 {
  height: 40px;
  background: rgba(202,240,248,.4);
  animation: kf-07-wave1 6s ease-in-out infinite .6s;
}

@keyframes kf-07-wave1 {
  0%,
    100% {
    transform: translateX(-50px) scaleY(1);
  }

  50% {
    transform: translateX(30px) scaleY(1.1);
  }
}

@keyframes kf-07-wave2 {
  0%,
    100% {
    transform: translateX(40px) scaleY(1);
  }

  50% {
    transform: translateX(-30px) scaleY(.9);
  }
}

.kf-07__ship {
  position: absolute;
  top: 16px;
  left: 0;
  font-size: 28px;
  animation: kf-07-sail 8s linear infinite;
}

@keyframes kf-07-sail {
  from {
    left: -40px;
  }

  to {
    left: calc(100% + 40px);
  }
}
/* 2 — Sine wave line */

.kf-07__sine {
  width: 100%;
  max-width: 600px;
  height: 80px;
  position: relative;
  overflow: hidden;
}

.kf-07__sine-line {
  position: absolute;
  bottom: 0;
  left: -100%;
  width: 300%;
  height: 100%;
  background: none;
  border-top: 3px solid var(--mid);
  border-radius: 100%;
  animation: kf-07-sine 3s linear infinite;
}

.kf-07__sine-line--2 {
  border-top-color: var(--light);
  animation-delay: .5s;
  opacity: .6;
}

.kf-07__sine-line--3 {
  border-top-color: var(--foam);
  animation-delay: 1s;
  opacity: .3;
}

@keyframes kf-07-sine {
  to {
    transform: translateX(33.33%);
  }
}
/* 3 — Animated gradient wave bg */

.kf-07__grad-wave {
  width: 100%;
  max-width: 700px;
  height: 120px;
  position: relative;
  border-radius: 12px;
  overflow: hidden;
}

.kf-07__grad-wave::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,#03045e,var(--deep),var(--mid),var(--light),var(--mid),var(--deep),#03045e);
  background-size: 400% 100%;
  animation: kf-07-gradwave 4s linear infinite;
}

@keyframes kf-07-gradwave {
  to {
    background-position: -400% 0;
  }
}

.kf-07__grad-text {
  position: relative;
  z-index: 1;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: .1em;
}
/* 4 — Liquid level */

.kf-07__vial {
  width: 90px;
  height: 180px;
  border: 3px solid var(--foam);
  border-radius: 45px;
  position: relative;
  overflow: hidden;
  background: rgba(0,0,0,.2);
}

.kf-07__liquid {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 65%;
  background: linear-gradient(180deg,var(--mid),var(--deep));
}

.kf-07__liquid::before {
  content: '';
  position: absolute;
  top: -18px;
  left: -50%;
  width: 200%;
  height: 36px;
  background: var(--mid);
  border-radius: 50%;
  animation: kf-07-liq 2.5s ease-in-out infinite;
}

@keyframes kf-07-liq {
  0%,
    100% {
    transform: translateX(-10px) rotateZ(-2deg);
  }

  50% {
    transform: translateX(10px) rotateZ(2deg);
  }
}

.kf-07__pct {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--white);
}
/* 5 — Pulse ring wave */

.kf-07__rings {
  position: relative;
  width: 120px;
  height: 120px;
  display: grid;
  place-items: center;
}

.kf-07__ring {
  position: absolute;
  border-radius: 50%;
  border: 2px solid var(--mid);
  animation: kf-07-ring 2.4s ease-out infinite;
}

.kf-07__ring:nth-child(1) {
  inset: 40px;
  animation-delay: 0s;
}

.kf-07__ring:nth-child(2) {
  inset: 30px;
  animation-delay: .4s;
  border-color: var(--light);
}

.kf-07__ring:nth-child(3) {
  inset: 20px;
  animation-delay: .8s;
  border-color: var(--foam);
}

.kf-07__ring:nth-child(4) {
  inset: 10px;
  animation-delay: 1.2s;
}

@keyframes kf-07-ring {
  0% {
    transform: scale(1);
    opacity: 1;
  }

  100% {
    transform: scale(3);
    opacity: 0;
  }
}

.kf-07__row {
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-width: 700px;
}

.kf-07__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.kf-07__label {
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(202,240,248,.6);
}

@media (prefers-reduced-motion: reduce) {
  .kf-07 * {
    animation: none!important;
  }
}
```
