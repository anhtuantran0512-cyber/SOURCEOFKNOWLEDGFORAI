---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-particle-burst-animation/"
title: "CSS Particle Burst Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Four particle burst effects: shockwave rings, firework sparks, spinning petals and confetti rain — all pure CSS translate + scale keyframes, no canvas."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Particle Burst Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-particle-burst-animation/

Four particle burst effects: shockwave rings, firework sparks, spinning petals and confetti rain — all pure CSS translate + scale keyframes, no canvas.
## HTML
```html
<div class="kf-06">
  <div class="kf-06__row">
    <div class="kf-06__cell">
      <div class="kf-06__burst">
        <div class="kf-06__burst-ring"></div>
        <div class="kf-06__burst-ring"></div>
        <div class="kf-06__burst-ring"></div>
        <div class="kf-06__burst-dot"></div>
      </div>
      <span class="kf-06__label">Shockwave</span>
    </div>
    <div class="kf-06__cell">
      <div class="kf-06__firework">
        <div class="kf-06__spark"></div><div class="kf-06__spark"></div>
        <div class="kf-06__spark"></div><div class="kf-06__spark"></div>
        <div class="kf-06__spark"></div><div class="kf-06__spark"></div>
        <div class="kf-06__spark"></div><div class="kf-06__spark"></div>
      </div>
      <span class="kf-06__label">Firework Sparks</span>
    </div>
    <div class="kf-06__cell">
      <div class="kf-06__starburst">
        <div class="kf-06__petal"></div><div class="kf-06__petal"></div>
        <div class="kf-06__petal"></div><div class="kf-06__petal"></div>
        <div class="kf-06__petal"></div><div class="kf-06__petal"></div>
        <div class="kf-06__petal"></div><div class="kf-06__petal"></div>
      </div>
      <span class="kf-06__label">Spinning Petals</span>
    </div>
  </div>
  <div class="kf-06__cell">
    <div class="kf-06__confetti">
      <div class="kf-06__c"></div><div class="kf-06__c"></div>
      <div class="kf-06__c"></div><div class="kf-06__c"></div>
      <div class="kf-06__c"></div><div class="kf-06__c"></div>
      <div class="kf-06__c"></div><div class="kf-06__c"></div>
    </div>
    <span class="kf-06__label">Confetti Rain</span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap');

.kf-06,
.kf-06 *,
.kf-06 *::before,
.kf-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-06 ::selection {
  background: #ff9f1c;
  color: #000;
}

.kf-06 {
  --bg: #09090b;
  --orange: #ff9f1c;
  --teal: #2ec4b6;
  --pink: #e71d73;
  --lime: #cbff4d;
  --white: #f4f4f5;
  font-family: 'Space Grotesk',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 72px;
  overflow: hidden;
}
/* ——— Burst 1: radial lines ——— */

.kf-06__burst {
  position: relative;
  width: 120px;
  height: 120px;
  display: grid;
  place-items: center;
}

.kf-06__burst-ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 3px solid var(--orange);
  animation: kf-06-expand 2s ease-out infinite;
}

.kf-06__burst-ring:nth-child(2) {
  animation-delay: .4s;
  border-color: rgba(255,159,28,.6);
}

.kf-06__burst-ring:nth-child(3) {
  animation-delay: .8s;
  border-color: rgba(255,159,28,.3);
}

@keyframes kf-06-expand {
  0% {
    transform: scale(.1);
    opacity: 1;
  }

  100% {
    transform: scale(2.5);
    opacity: 0;
  }
}

.kf-06__burst-dot {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--orange);
  box-shadow: 0 0 20px var(--orange);
}
/* ——— Burst 2: firework sparks ——— */

.kf-06__firework {
  position: relative;
  width: 140px;
  height: 140px;
}

.kf-06__spark {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  margin: -3px 0 0 -3px;
  animation: kf-06-spark 1.8s ease-out infinite;
}

.kf-06__spark:nth-child(1) {
  background: var(--teal);
  --angle: 0deg;
  animation-delay: 0s;
}

.kf-06__spark:nth-child(2) {
  background: var(--pink);
  --angle: 45deg;
  animation-delay: .05s;
}

.kf-06__spark:nth-child(3) {
  background: var(--lime);
  --angle: 90deg;
  animation-delay: .1s;
}

.kf-06__spark:nth-child(4) {
  background: var(--orange);
  --angle: 135deg;
  animation-delay: .15s;
}

.kf-06__spark:nth-child(5) {
  background: var(--teal);
  --angle: 180deg;
  animation-delay: .2s;
}

.kf-06__spark:nth-child(6) {
  background: var(--pink);
  --angle: 225deg;
  animation-delay: .25s;
}

.kf-06__spark:nth-child(7) {
  background: var(--lime);
  --angle: 270deg;
  animation-delay: .3s;
}

.kf-06__spark:nth-child(8) {
  background: var(--orange);
  --angle: 315deg;
  animation-delay: .35s;
}

@keyframes kf-06-spark {
  0% {
    transform: rotate(var(--angle)) translateX(0);
    opacity: 1;
    width: 6px;
    height: 6px;
  }

  60% {
    opacity: 1;
  }

  100% {
    transform: rotate(var(--angle)) translateX(60px);
    opacity: 0;
    width: 3px;
    height: 3px;
  }
}
/* ——— Burst 3: starburst petals ——— */

.kf-06__starburst {
  position: relative;
  width: 120px;
  height: 120px;
  animation: kf-06-rotate 6s linear infinite;
}

@keyframes kf-06-rotate {
  to {
    transform: rotate(360deg);
  }
}

.kf-06__petal {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 12px;
  height: 40px;
  border-radius: 50%;
  margin: -20px 0 0 -6px;
  transform-origin: 50% 100%;
  opacity: .8;
}

.kf-06__petal:nth-child(1) {
  background: var(--teal);
  transform: rotate(0deg);
  animation: kf-06-petal 2s ease-in-out infinite;
}

.kf-06__petal:nth-child(2) {
  background: var(--pink);
  transform: rotate(45deg);
  animation: kf-06-petal 2s ease-in-out infinite .25s;
}

.kf-06__petal:nth-child(3) {
  background: var(--lime);
  transform: rotate(90deg);
  animation: kf-06-petal 2s ease-in-out infinite .5s;
}

.kf-06__petal:nth-child(4) {
  background: var(--orange);
  transform: rotate(135deg);
  animation: kf-06-petal 2s ease-in-out infinite .75s;
}

.kf-06__petal:nth-child(5) {
  background: var(--teal);
  transform: rotate(180deg);
  animation: kf-06-petal 2s ease-in-out infinite 1s;
}

.kf-06__petal:nth-child(6) {
  background: var(--pink);
  transform: rotate(225deg);
  animation: kf-06-petal 2s ease-in-out infinite 1.25s;
}

.kf-06__petal:nth-child(7) {
  background: var(--lime);
  transform: rotate(270deg);
  animation: kf-06-petal 2s ease-in-out infinite 1.5s;
}

.kf-06__petal:nth-child(8) {
  background: var(--orange);
  transform: rotate(315deg);
  animation: kf-06-petal 2s ease-in-out infinite 1.75s;
}

@keyframes kf-06-petal {
  0%,
    100% {
    height: 30px;
    opacity: .6;
  }

  50% {
    height: 50px;
    opacity: 1;
  }
}
/* ——— Burst 4: confetti fall ——— */

.kf-06__confetti {
  position: relative;
  width: 200px;
  height: 100px;
  overflow: hidden;
}

.kf-06__c {
  position: absolute;
  width: 8px;
  height: 8px;
  animation: kf-06-fall linear infinite;
}

.kf-06__c:nth-child(1) {
  left: 10%;
  background: var(--teal);
  animation-duration: 2.4s;
  animation-delay: 0s;
  border-radius: 2px;
}

.kf-06__c:nth-child(2) {
  left: 25%;
  background: var(--pink);
  animation-duration: 2s;
  animation-delay: .3s;
  border-radius: 50%;
}

.kf-06__c:nth-child(3) {
  left: 40%;
  background: var(--lime);
  animation-duration: 2.8s;
  animation-delay: .6s;
}

.kf-06__c:nth-child(4) {
  left: 55%;
  background: var(--orange);
  animation-duration: 2.2s;
  animation-delay: .9s;
  border-radius: 50%;
}

.kf-06__c:nth-child(5) {
  left: 70%;
  background: var(--teal);
  animation-duration: 2.6s;
  animation-delay: .2s;
}

.kf-06__c:nth-child(6) {
  left: 85%;
  background: var(--pink);
  animation-duration: 2.1s;
  animation-delay: .7s;
  border-radius: 2px;
}

.kf-06__c:nth-child(7) {
  left: 15%;
  background: var(--lime);
  animation-duration: 2.9s;
  animation-delay: 1.1s;
  border-radius: 50%;
}

.kf-06__c:nth-child(8) {
  left: 60%;
  background: var(--orange);
  animation-duration: 2.3s;
  animation-delay: .4s;
}

@keyframes kf-06-fall {
  0% {
    top: -8px;
    transform: rotate(0) translateX(0);
    opacity: 1;
  }

  100% {
    top: 100%;
    transform: rotate(720deg) translateX(20px);
    opacity: 0;
  }
}

.kf-06__row {
  display: flex;
  gap: 56px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.kf-06__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
}

.kf-06__label {
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #555;
}

@media (prefers-reduced-motion: reduce) {
  .kf-06 * {
    animation: none!important;
  }
}
```
