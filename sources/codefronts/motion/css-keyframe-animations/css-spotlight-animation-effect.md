---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-spotlight-animation-effect/"
title: "CSS Spotlight Animation Effect"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Six spotlight effects: roving text highlight, stage light cones, security scan beam, product reveal orb, grid cell highlight and club sweep — radial-gradient…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Spotlight Animation Effect
Source: https://codefronts.com/motion/css-keyframe-animations/css-spotlight-animation-effect/

Six spotlight effects: roving text highlight, stage light cones, security scan beam, product reveal orb, grid cell highlight and club sweep — radial-gradient keyframes.
## HTML
```html
<div class="kf-21">
  <h2>CSS Spotlight Animations</h2>
  <div class="demos">
    <!-- Roving text spotlight -->
    <div class="spotlight-text">
      <h3>SPOTLIGHT</h3>
    </div>

    <!-- Stage cones -->
    <div class="stage">
      <div class="cone cone-1"></div>
      <div class="cone cone-2"></div>
      <div class="cone cone-3"></div>
      <span class="stage-label">LIVE</span>
    </div>

    <!-- Scanning beam -->
    <div class="scan-wrap">
      <div class="scan-beam"></div>
      <div class="scan-content">
        <div class="scan-line"></div>
        <div class="scan-line"></div>
        <div class="scan-line"></div>
      </div>
      <span class="scan-label">Scanning...</span>
    </div>

    <!-- Product spotlight -->
    <div class="product-spot">
      <div class="product-icon">✦</div>
    </div>

    <!-- Grid highlight -->
    <div class="grid-spot">
      <div class="grid-cell">🔴</div>
      <div class="grid-cell">🟠</div>
      <div class="grid-cell">🟡</div>
      <div class="grid-cell">🟢</div>
      <div class="grid-cell">🔵</div>
      <div class="grid-cell">🟣</div>
      <div class="grid-cell">⚫</div>
      <div class="grid-cell">⚪</div>
      <div class="grid-cell">🟤</div>
    </div>

    <!-- Club spotlight sweep -->
    <div class="club">
      <div class="club-beam"></div>
      <div class="club-beam-2"></div>
      <div class="club-label">TONIGHT</div>
    </div>
  </div>
</div>
```
## CSS
```css
.kf-21 *,
.kf-21 *::before,
.kf-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-21 {
  font-family: 'Segoe UI', sans-serif;
  background: #080810;
  color: #fff;
  padding: 40px 20px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
}

.kf-21 h2 {
  font-size: 1.1rem;
  color: #555;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.kf-21 .demos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  width: 100%;
  max-width: 960px;
}
/* 1: Roving spotlight on text */

.kf-21 .spotlight-text {
  position: relative;
  overflow: hidden;
  background: #0d0d1a;
  border-radius: 12px;
  padding: 48px 24px;
  text-align: center;
}

.kf-21 .spotlight-text h3 {
  font-size: 2rem;
  font-weight: 800;
  color: #111;
  position: relative;
  z-index: 2;
  background: linear-gradient(90deg, #333, #222, #333);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: 4px;
}

.kf-21 .spotlight-text::before {
  content: '';
  position: absolute;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(255,220,100,0.9) 0%, rgba(255,180,0,0.4) 40%, transparent 70%);
  border-radius: 50%;
  top: 50%;
  left: -100px;
  transform: translateY(-50%);
  animation: kf-21-rove 3s ease-in-out infinite;
  pointer-events: none;
  z-index: 1;
  mix-blend-mode: screen;
}

@keyframes kf-21-rove {
  0% {
    left: -100px;
  }

  50% {
    left: calc(100% - 100px);
  }

  100% {
    left: -100px;
  }
}
/* 2: Stage spotlight cones */

.kf-21 .stage {
  background: #050508;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  height: 200px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 20px;
  gap: 40px;
}

.kf-21 .cone {
  position: absolute;
  top: 0;
  width: 120px;
  height: 180px;
  clip-path: polygon(40% 0%, 60% 0%, 100% 100%, 0% 100%);
  background: linear-gradient(180deg, rgba(255,240,180,0.15) 0%, rgba(255,240,180,0.05) 100%);
  transform-origin: top center;
}

.kf-21 .cone-1 {
  left: 20%;
  animation: kf-21-cone1 4s ease-in-out infinite;
}

.kf-21 .cone-2 {
  left: 50%;
  transform: translateX(-50%);
  animation: kf-21-cone2 4s ease-in-out infinite;
  animation-delay: 0.5s;
}

.kf-21 .cone-3 {
  right: 20%;
  animation: kf-21-cone3 4s ease-in-out infinite;
  animation-delay: 1s;
}

@keyframes kf-21-cone1 {
  0%,
    100% {
    opacity: 0.4;
    transform: rotate(-10deg);
  }

  50% {
    opacity: 1;
    transform: rotate(10deg);
  }
}

@keyframes kf-21-cone2 {
  0%,
    100% {
    opacity: 1;
    transform: translateX(-50%) scaleX(1);
  }

  50% {
    opacity: 0.5;
    transform: translateX(-50%) scaleX(0.7);
  }
}

@keyframes kf-21-cone3 {
  0%,
    100% {
    opacity: 0.4;
    transform: rotate(10deg);
  }

  50% {
    opacity: 1;
    transform: rotate(-10deg);
  }
}

.kf-21 .stage-label {
  position: relative;
  z-index: 2;
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: 6px;
  color: rgba(255,240,180,0.9);
  text-shadow: 0 0 20px rgba(255,200,50,0.8);
  animation: kf-21-stagelabel 4s ease-in-out infinite;
}

@keyframes kf-21-stagelabel {
  0%,
    100% {
    text-shadow: 0 0 20px rgba(255,200,50,0.4);
  }

  50% {
    text-shadow: 0 0 40px rgba(255,200,50,1), 0 0 80px rgba(255,200,50,0.5);
  }
}
/* 3: Scanning spotlight */

.kf-21 .scan-wrap {
  position: relative;
  background: #0a0a16;
  border-radius: 12px;
  overflow: hidden;
  padding: 40px 24px;
  height: 180px;
}

.kf-21 .scan-beam {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg,
      transparent 0%,
      transparent 20%,
      rgba(100,200,255,0.08) 40%,
      rgba(100,200,255,0.2) 50%,
      rgba(100,200,255,0.08) 60%,
      transparent 80%,
      transparent 100%
    );
  animation: kf-21-scan 2.5s ease-in-out infinite;
}

@keyframes kf-21-scan {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(100%);
  }
}

.kf-21 .scan-content {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.kf-21 .scan-line {
  height: 10px;
  border-radius: 4px;
  background: #1e2030;
}

.kf-21 .scan-line:nth-child(1) {
  width: 70%;
}

.kf-21 .scan-line:nth-child(2) {
  width: 90%;
}

.kf-21 .scan-line:nth-child(3) {
  width: 60%;
}

.kf-21 .scan-label {
  position: absolute;
  bottom: 12px;
  right: 16px;
  font-size: 0.7rem;
  color: rgba(100,200,255,0.6);
  letter-spacing: 2px;
  text-transform: uppercase;
  animation: kf-21-blink 1s step-end infinite;
}

@keyframes kf-21-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}
/* 4: Product spotlight */

.kf-21 .product-spot {
  position: relative;
  background: #06060f;
  border-radius: 12px;
  overflow: hidden;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kf-21 .product-spot::before {
  content: '';
  position: absolute;
  width: 250px;
  height: 250px;
  background: radial-gradient(ellipse, rgba(180,120,255,0.25) 0%, rgba(100,50,200,0.1) 40%, transparent 70%);
  top: -80px;
  left: 50%;
  transform: translateX(-50%);
  animation: kf-21-prod 3s ease-in-out infinite;
}

@keyframes kf-21-prod {
  0%,
    100% {
    width: 200px;
    opacity: 0.6;
  }

  50% {
    width: 300px;
    opacity: 1;
  }
}

.kf-21 .product-icon {
  position: relative;
  z-index: 2;
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #7c6af7, #e91e8c);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.2rem;
  box-shadow: 0 20px 60px rgba(124,106,247,0.5);
  animation: kf-21-iconrise 3s ease-in-out infinite;
}

@keyframes kf-21-iconrise {
  0%,
    100% {
    transform: translateY(4px);
    box-shadow: 0 16px 40px rgba(124,106,247,0.4);
  }

  50% {
    transform: translateY(-4px);
    box-shadow: 0 24px 70px rgba(124,106,247,0.7);
  }
}
/* 5: Spotlight grid highlight */

.kf-21 .grid-spot {
  background: #080814;
  border-radius: 12px;
  overflow: hidden;
  padding: 24px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}

.kf-21 .grid-cell {
  aspect-ratio: 1;
  border-radius: 8px;
  background: #111125;
  border: 1px solid #1e1e3a;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  transition: all 0.3s;
}

.kf-21 .grid-cell:nth-child(1) {
  animation: kf-21-cellhl 4.5s ease infinite 0s;
}

.kf-21 .grid-cell:nth-child(2) {
  animation: kf-21-cellhl 4.5s ease infinite 0.5s;
}

.kf-21 .grid-cell:nth-child(3) {
  animation: kf-21-cellhl 4.5s ease infinite 1s;
}

.kf-21 .grid-cell:nth-child(4) {
  animation: kf-21-cellhl 4.5s ease infinite 1.5s;
}

.kf-21 .grid-cell:nth-child(5) {
  animation: kf-21-cellhl 4.5s ease infinite 2s;
}

.kf-21 .grid-cell:nth-child(6) {
  animation: kf-21-cellhl 4.5s ease infinite 2.5s;
}

.kf-21 .grid-cell:nth-child(7) {
  animation: kf-21-cellhl 4.5s ease infinite 3s;
}

.kf-21 .grid-cell:nth-child(8) {
  animation: kf-21-cellhl 4.5s ease infinite 3.5s;
}

.kf-21 .grid-cell:nth-child(9) {
  animation: kf-21-cellhl 4.5s ease infinite 4s;
}

@keyframes kf-21-cellhl {
  0%,
    80%,
    100% {
    background: #111125;
    border-color: #1e1e3a;
    box-shadow: none;
  }

  90% {
    background: rgba(124,106,247,0.2);
    border-color: #7c6af7;
    box-shadow: 0 0 20px rgba(124,106,247,0.4);
  }
}
/* 6: Sweeping club spotlight */

.kf-21 .club {
  background: #020205;
  border-radius: 12px;
  overflow: hidden;
  height: 200px;
  position: relative;
}

.kf-21 .club-beam {
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 300px;
  height: 280px;
  background: radial-gradient(ellipse at bottom center, rgba(255,50,150,0.5) 0%, rgba(150,0,100,0.2) 30%, transparent 70%);
  clip-path: polygon(40% 100%, 60% 100%, 95% 0%, 5% 0%);
  transform-origin: bottom center;
  transform: translateX(-50%);
  animation: kf-21-sweep 3s ease-in-out infinite;
}

.kf-21 .club-beam-2 {
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 300px;
  height: 280px;
  background: radial-gradient(ellipse at bottom center, rgba(50,150,255,0.4) 0%, transparent 70%);
  clip-path: polygon(40% 100%, 60% 100%, 95% 0%, 5% 0%);
  transform-origin: bottom center;
  transform: translateX(-50%);
  animation: kf-21-sweep 3s ease-in-out infinite reverse;
  animation-delay: 1.5s;
}

@keyframes kf-21-sweep {
  0%,
    100% {
    transform: translateX(-50%) rotate(-40deg);
  }

  50% {
    transform: translateX(-50%) rotate(40deg);
  }
}

.kf-21 .club-label {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: 4px;
  color: rgba(255,255,255,0.1);
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {
  .kf-21 .spotlight-text::before,
    .kf-21 .cone-1,
    .kf-21 .cone-2,
    .kf-21 .cone-3,
    .kf-21 .stage-label,
    .kf-21 .scan-beam,
    .kf-21 .scan-label,
    .kf-21 .product-spot::before,
    .kf-21 .product-icon,
    .kf-21 .grid-cell,
    .kf-21 .club-beam,
    .kf-21 .club-beam-2 {
    animation: none;
  }
}
```
