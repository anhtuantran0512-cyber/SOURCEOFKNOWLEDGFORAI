---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-confetti-explosion-animation/"
title: "CSS Confetti Explosion Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Three confetti explosion styles: multi-directional radial burst, falling confetti rain and party-popper cracker — all pure CSS translate + rotate keyframes."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Confetti Explosion Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-confetti-explosion-animation/

Three confetti explosion styles: multi-directional radial burst, falling confetti rain and party-popper cracker — all pure CSS translate + rotate keyframes.
## HTML
```html
<div class="kf-23">
  <h2>CSS Confetti Explosion Animations</h2>
  <div class="scene-row">

    <!-- Burst explosion -->
    <div class="conf-wrap scene-1">
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <span class="conf-title">🎉 YAY!</span>
      <span class="conf-sub">Celebration burst</span>
    </div>

    <!-- Falling rain -->
    <div class="conf-wrap scene-2">
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <span class="conf-title" style="z-index:2">🎊</span>
      <span class="conf-sub" style="z-index:2">Confetti Rain</span>
    </div>

    <!-- Popper cracker -->
    <div class="cracker">
      <div class="popper-icon">🎉</div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
      <div class="piece"></div>
    </div>

  </div>
</div>
```
## CSS
```css
.kf-23 *,
.kf-23 *::before,
.kf-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-23 {
  font-family: 'Segoe UI', sans-serif;
  background: #0a0a14;
  color: #fff;
  padding: 40px 20px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}

.kf-23 h2 {
  font-size: 1.1rem;
  color: #555;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.kf-23 .scene-row {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  justify-content: center;
  width: 100%;
  max-width: 960px;
}
/* Confetti piece base */

.kf-23 .conf-wrap {
  position: relative;
  width: 300px;
  height: 260px;
  overflow: hidden;
  border-radius: 16px;
  background: #0d0d1e;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 8px;
}

.kf-23 .conf-title {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: 2px;
  z-index: 2;
  text-align: center;
}

.kf-23 .conf-sub {
  font-size: 0.8rem;
  color: #888;
  letter-spacing: 1px;
  z-index: 2;
}
/* Generic confetti piece */

.kf-23 .piece {
  position: absolute;
  width: 10px;
  height: 10px;
  border-radius: 2px;
  animation: kf-23-burst 2.5s ease-in infinite;
  transform-origin: center;
}
/* Scene 1: Celebration burst — pieces all directions */

.kf-23 .scene-1 .piece {
  animation-duration: 2s;
  animation-delay: calc(var(--d) * 0.08s);
}

.kf-23 .scene-1 .piece:nth-child(1) {
  --d: 1;
  left: 50%;
  top: 50%;
  background: #f7c948;
  width: 8px;
  height: 14px;
  animation-name: kf-23-p1;
}

.kf-23 .scene-1 .piece:nth-child(2) {
  --d: 2;
  left: 50%;
  top: 50%;
  background: #e91e8c;
  width: 12px;
  height: 8px;
  border-radius: 50%;
  animation-name: kf-23-p2;
}

.kf-23 .scene-1 .piece:nth-child(3) {
  --d: 3;
  left: 50%;
  top: 50%;
  background: #7c6af7;
  animation-name: kf-23-p3;
}

.kf-23 .scene-1 .piece:nth-child(4) {
  --d: 4;
  left: 50%;
  top: 50%;
  background: #00d4ff;
  width: 6px;
  height: 16px;
  animation-name: kf-23-p4;
}

.kf-23 .scene-1 .piece:nth-child(5) {
  --d: 5;
  left: 50%;
  top: 50%;
  background: #ff6b35;
  border-radius: 50%;
  animation-name: kf-23-p5;
}

.kf-23 .scene-1 .piece:nth-child(6) {
  --d: 6;
  left: 50%;
  top: 50%;
  background: #00d46a;
  width: 14px;
  height: 6px;
  animation-name: kf-23-p6;
}

.kf-23 .scene-1 .piece:nth-child(7) {
  --d: 7;
  left: 50%;
  top: 50%;
  background: #f7c948;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  animation-name: kf-23-p7;
}

.kf-23 .scene-1 .piece:nth-child(8) {
  --d: 8;
  left: 50%;
  top: 50%;
  background: #e91e8c;
  animation-name: kf-23-p8;
}

.kf-23 .scene-1 .piece:nth-child(9) {
  --d: 9;
  left: 50%;
  top: 50%;
  background: #7c6af7;
  width: 16px;
  height: 5px;
  animation-name: kf-23-p9;
}

.kf-23 .scene-1 .piece:nth-child(10) {
  --d: 10;
  left: 50%;
  top: 50%;
  background: #ff6b35;
  width: 6px;
  height: 12px;
  animation-name: kf-23-p10;
}

.kf-23 .scene-1 .piece:nth-child(11) {
  --d: 1;
  left: 50%;
  top: 50%;
  background: #00d4ff;
  width: 9px;
  height: 9px;
  animation-name: kf-23-p11;
}

.kf-23 .scene-1 .piece:nth-child(12) {
  --d: 2;
  left: 50%;
  top: 50%;
  background: #00d46a;
  border-radius: 50%;
  animation-name: kf-23-p12;
}

@keyframes kf-23-p1 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(-100px,-130px) rotate(540deg);
    opacity: 0;
  }
}

@keyframes kf-23-p2 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(80px,-150px) rotate(-360deg);
    opacity: 0;
  }
}

@keyframes kf-23-p3 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(130px,-90px) rotate(720deg);
    opacity: 0;
  }
}

@keyframes kf-23-p4 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(120px,60px) rotate(-540deg);
    opacity: 0;
  }
}

@keyframes kf-23-p5 {
  0% {
    transform: translate(0,0) scale(1);
  }

  100% {
    transform: translate(60px,140px) scale(0.3);
    opacity: 0;
  }
}

@keyframes kf-23-p6 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(-60px,130px) rotate(360deg);
    opacity: 0;
  }
}

@keyframes kf-23-p7 {
  0% {
    transform: translate(0,0) scale(1);
  }

  100% {
    transform: translate(-130px,80px) scale(0.2);
    opacity: 0;
  }
}

@keyframes kf-23-p8 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(-140px,-30px) rotate(-720deg);
    opacity: 0;
  }
}

@keyframes kf-23-p9 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(40px,-160px) rotate(480deg);
    opacity: 0;
  }
}

@keyframes kf-23-p10 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(150px,-50px) rotate(-400deg);
    opacity: 0;
  }
}

@keyframes kf-23-p11 {
  0% {
    transform: translate(0,0) rotate(0);
  }

  100% {
    transform: translate(-50px,-170px) rotate(600deg);
    opacity: 0;
  }
}

@keyframes kf-23-p12 {
  0% {
    transform: translate(0,0) scale(1);
  }

  100% {
    transform: translate(-120px,-100px) scale(0.2);
    opacity: 0;
  }
}
/* Scene 2: Rain confetti (falling from top) */

.kf-23 .scene-2 .piece {
  top: -20px;
  animation-name: kf-23-rain;
  animation-duration: 2.5s;
  animation-timing-function: linear;
}

.kf-23 .scene-2 .piece:nth-child(n) {
  animation-delay: calc(var(--i) * 0.18s);
}

.kf-23 .scene-2 .piece:nth-child(1) {
  --i: 0;
  left: 10%;
  background: #f7c948;
  width: 8px;
  height: 14px;
}

.kf-23 .scene-2 .piece:nth-child(2) {
  --i: 1;
  left: 22%;
  background: #e91e8c;
  border-radius: 50%;
}

.kf-23 .scene-2 .piece:nth-child(3) {
  --i: 2;
  left: 35%;
  background: #7c6af7;
  width: 14px;
  height: 6px;
}

.kf-23 .scene-2 .piece:nth-child(4) {
  --i: 3;
  left: 50%;
  background: #00d4ff;
  width: 6px;
  height: 14px;
}

.kf-23 .scene-2 .piece:nth-child(5) {
  --i: 4;
  left: 65%;
  background: #ff6b35;
  border-radius: 50%;
}

.kf-23 .scene-2 .piece:nth-child(6) {
  --i: 5;
  left: 78%;
  background: #00d46a;
  width: 12px;
  height: 8px;
}

.kf-23 .scene-2 .piece:nth-child(7) {
  --i: 0.5;
  left: 15%;
  background: #f7c948;
  border-radius: 50%;
}

.kf-23 .scene-2 .piece:nth-child(8) {
  --i: 1.5;
  left: 45%;
  background: #e91e8c;
  width: 8px;
  height: 12px;
}

.kf-23 .scene-2 .piece:nth-child(9) {
  --i: 2.5;
  left: 60%;
  background: #7c6af7;
  width: 12px;
  height: 8px;
}

.kf-23 .scene-2 .piece:nth-child(10) {
  --i: 3.5;
  left: 88%;
  background: #00d4ff;
  border-radius: 50%;
}

.kf-23 .scene-2 .piece:nth-child(11) {
  --i: 4.5;
  left: 5%;
  background: #ff6b35;
  width: 10px;
  height: 10px;
}

.kf-23 .scene-2 .piece:nth-child(12) {
  --i: 5.5;
  left: 72%;
  background: #00d46a;
  width: 6px;
  height: 16px;
}

@keyframes kf-23-rain {
  0% {
    transform: translateY(0) rotate(0deg) translateX(0);
    opacity: 1;
  }

  25% {
    transform: translateY(65px) rotate(180deg) translateX(15px);
  }

  50% {
    transform: translateY(130px) rotate(360deg) translateX(-10px);
  }

  75% {
    transform: translateY(195px) rotate(540deg) translateX(12px);
  }

  100% {
    transform: translateY(280px) rotate(720deg) translateX(-8px);
    opacity: 0.4;
  }
}
/* Scene 3: Popper / cracker */

.kf-23 .cracker {
  position: relative;
  width: 240px;
  height: 260px;
  overflow: hidden;
  border-radius: 16px;
  background: #0d0d1e;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kf-23 .popper-icon {
  font-size: 3rem;
  z-index: 2;
  animation: kf-23-poppericon 2s ease infinite;
}

@keyframes kf-23-poppericon {
  0%,
    40% {
    transform: rotate(-20deg) scale(0.9);
  }

  50% {
    transform: rotate(20deg) scale(1.2);
  }

  60%,
    100% {
    transform: rotate(-20deg) scale(0.9);
  }
}

.kf-23 .cracker .piece {
  animation-name: kf-23-cracker;
  animation-duration: 1.8s;
  animation-timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.kf-23 .cracker .piece:nth-child(2) {
  background: #f7c948;
  animation-delay: 0.05s;
}

.kf-23 .cracker .piece:nth-child(3) {
  background: #e91e8c;
  border-radius: 50%;
  animation-delay: 0.1s;
}

.kf-23 .cracker .piece:nth-child(4) {
  background: #7c6af7;
  width: 14px;
  height: 5px;
  animation-delay: 0.0s;
}

.kf-23 .cracker .piece:nth-child(5) {
  background: #00d4ff;
  animation-delay: 0.15s;
}

.kf-23 .cracker .piece:nth-child(6) {
  background: #ff6b35;
  border-radius: 50%;
  animation-delay: 0.08s;
}

.kf-23 .cracker .piece:nth-child(7) {
  background: #00d46a;
  animation-delay: 0.12s;
}

.kf-23 .cracker .piece:nth-child(8) {
  background: #f7c948;
  border-radius: 50%;
  animation-delay: 0.04s;
}

.kf-23 .cracker .piece:nth-child(9) {
  background: #e91e8c;
  width: 5px;
  height: 14px;
  animation-delay: 0.16s;
}

@keyframes kf-23-cracker {
  0% {
    transform: translate(0,0) rotate(0deg);
    opacity: 1;
    top: 50%;
    left: 50%;
  }

  30% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}
/* Individual cracker pieces radiate */

.kf-23 .cracker .piece:nth-child(2) {
  animation-name: kf-23-cp1;
}

.kf-23 .cracker .piece:nth-child(3) {
  animation-name: kf-23-cp2;
}

.kf-23 .cracker .piece:nth-child(4) {
  animation-name: kf-23-cp3;
}

.kf-23 .cracker .piece:nth-child(5) {
  animation-name: kf-23-cp4;
}

.kf-23 .cracker .piece:nth-child(6) {
  animation-name: kf-23-cp5;
}

.kf-23 .cracker .piece:nth-child(7) {
  animation-name: kf-23-cp6;
}

.kf-23 .cracker .piece:nth-child(8) {
  animation-name: kf-23-cp7;
}

.kf-23 .cracker .piece:nth-child(9) {
  animation-name: kf-23-cp8;
}

@keyframes kf-23-cp1 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 5%;
    left: 15%;
    transform: rotate(480deg);
    opacity: 0;
  }
}

@keyframes kf-23-cp2 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 8%;
    left: 55%;
    transform: rotate(-360deg);
    opacity: 0;
  }
}

@keyframes kf-23-cp3 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 15%;
    left: 85%;
    transform: rotate(540deg);
    opacity: 0;
  }
}

@keyframes kf-23-cp4 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 55%;
    left: 90%;
    transform: rotate(-480deg);
    opacity: 0;
  }
}

@keyframes kf-23-cp5 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 85%;
    left: 70%;
    transform: rotate(360deg);
    opacity: 0;
  }
}

@keyframes kf-23-cp6 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 88%;
    left: 30%;
    transform: rotate(-540deg);
    opacity: 0;
  }
}

@keyframes kf-23-cp7 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 80%;
    left: 8%;
    transform: rotate(720deg);
    opacity: 0;
  }
}

@keyframes kf-23-cp8 {
  0% {
    top: 50%;
    left: 50%;
    opacity: 1;
  }

  100% {
    top: 30%;
    left: 5%;
    transform: rotate(-720deg);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-23 .piece,
    .kf-23 .popper-icon {
    animation: none;
    opacity: 0.5;
  }
}
```
