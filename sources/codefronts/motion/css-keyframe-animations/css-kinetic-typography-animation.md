---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-kinetic-typography-animation/"
title: "CSS Kinetic Typography Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Five kinetic type scenes: stagger letter spring-drop, explode-and-reassemble, sinusoidal wave, scale-pulse mixed-weight headline and RGB-split glitch — pure…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Kinetic Typography Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-kinetic-typography-animation/

Five kinetic type scenes: stagger letter spring-drop, explode-and-reassemble, sinusoidal wave, scale-pulse mixed-weight headline and RGB-split glitch — pure CSS keyframes.
## HTML
```html
<div class="kf-28">

  <!-- Letter drop -->
  <div class="scene scene-1">
    <div class="letter-drop">
      <span>K</span><span>I</span><span>N</span><span>E</span><span>T</span><span>I</span><span>C</span>
    </div>
  </div>

  <!-- Explode -->
  <div class="scene scene-2">
    <div class="explode-word">
      <span>D</span><span>E</span><span>S</span><span>I</span><span>G</span><span>N</span><span>.</span>
    </div>
  </div>

  <!-- Wave -->
  <div class="scene scene-3">
    <div class="wave-word">
      <span>W</span><span>A</span><span>V</span><span>E</span><span>S</span><span>!</span>
    </div>
  </div>

  <!-- Scale pulse -->
  <div class="scene scene-4">
    <div class="scale-words">
      <span class="sw sw-1">THINK</span>
      <span class="sw sw-2">outside</span>
      <span class="sw sw-3">THE</span>
      <span class="sw sw-4">the</span>
      <span class="sw sw-5">BOX</span>
    </div>
  </div>

  <!-- Glitch -->
  <div class="scene scene-5">
    <div class="glitch-kine" data-text="MOTION">MOTION</div>
  </div>

</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,200;0,400;0,700;0,900;1,900&family=Bebas+Neue&display=swap');

.kf-28 *,
.kf-28 *::before,
.kf-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-28 {
  font-family: 'Inter', sans-serif;
  background: #060608;
  color: #fff;
  min-height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}
/* ── Scene 1: Kinetic splash hero ── */

.kf-28 .scene {
  width: 100%;
  max-width: 960px;
  padding: 60px 24px;
  min-height: 280px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}
/* Scene 1: Stagger letter drop */

.kf-28 .scene-1 {
  background: #060608;
  border-bottom: 1px solid #111;
}

.kf-28 .letter-drop {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3rem, 10vw, 6rem);
  letter-spacing: 8px;
  display: flex;
  gap: 4px;
  overflow: hidden;
}

.kf-28 .letter-drop span {
  display: inline-block;
  animation: kf-28-drop 3s cubic-bezier(0.34, 1.56, 0.64, 1) infinite;
}

.kf-28 .letter-drop span:nth-child(1) {
  color: #7c6af7;
  animation-delay: 0.05s;
}

.kf-28 .letter-drop span:nth-child(2) {
  color: #896cf9;
  animation-delay: 0.1s;
}

.kf-28 .letter-drop span:nth-child(3) {
  color: #9870fa;
  animation-delay: 0.15s;
}

.kf-28 .letter-drop span:nth-child(4) {
  color: #a975fb;
  animation-delay: 0.2s;
}

.kf-28 .letter-drop span:nth-child(5) {
  color: #bb79fc;
  animation-delay: 0.25s;
}

.kf-28 .letter-drop span:nth-child(6) {
  color: #cd7dfd;
  animation-delay: 0.3s;
}

.kf-28 .letter-drop span:nth-child(7) {
  color: #e080fe;
  animation-delay: 0.35s;
}

@keyframes kf-28-drop {
  0%,
    60%,
    100% {
    transform: translateY(0);
  }

  15% {
    transform: translateY(-40px);
  }

  30% {
    transform: translateY(4px);
  }

  42% {
    transform: translateY(-10px);
  }

  52% {
    transform: translateY(2px);
  }
}
/* Scene 2: Explode and reassemble */

.kf-28 .scene-2 {
  background: #080808;
  border-bottom: 1px solid #111;
}

.kf-28 .explode-word {
  font-size: clamp(2rem, 8vw, 4rem);
  font-weight: 900;
  letter-spacing: 2px;
  display: flex;
  gap: 0;
}

.kf-28 .explode-word span {
  display: inline-block;
  animation: kf-28-explode 4s ease-in-out infinite;
}

.kf-28 .explode-word span:nth-child(1) {
  color: #e91e8c;
  animation-delay: 0s;
  --tx: -120px;
  --ty: -60px;
  --r: -90deg;
}

.kf-28 .explode-word span:nth-child(2) {
  color: #ee3f9a;
  animation-delay: 0.06s;
  --tx: -60px;
  --ty: -90px;
  --r: 45deg;
}

.kf-28 .explode-word span:nth-child(3) {
  color: #f356a8;
  animation-delay: 0.12s;
  --tx: 0px;
  --ty: -100px;
  --r: -20deg;
}

.kf-28 .explode-word span:nth-child(4) {
  color: #f767b4;
  animation-delay: 0.18s;
  --tx: 60px;
  --ty: -80px;
  --r: 60deg;
}

.kf-28 .explode-word span:nth-child(5) {
  color: #fb7cbf;
  animation-delay: 0.24s;
  --tx: 100px;
  --ty: -50px;
  --r: -45deg;
}

.kf-28 .explode-word span:nth-child(6) {
  color: #fe8ec8;
  animation-delay: 0.3s;
  --tx: 130px;
  --ty: -70px;
  --r: 80deg;
}

.kf-28 .explode-word span:nth-child(7) {
  color: #ffa1d3;
  animation-delay: 0.36s;
  --tx: 80px;
  --ty: 60px;
  --r: -60deg;
}

@keyframes kf-28-explode {
  0%,
    20% {
    transform: translate(0,0) rotate(0deg) scale(1);
    opacity: 1;
  }

  45% {
    transform: translate(var(--tx), var(--ty)) rotate(var(--r)) scale(0.5);
    opacity: 0;
  }

  55% {
    transform: translate(var(--tx), var(--ty)) rotate(var(--r)) scale(0.5);
    opacity: 0;
  }

  80%,
    100% {
    transform: translate(0,0) rotate(0deg) scale(1);
    opacity: 1;
  }
}
/* Scene 3: Wave text */

.kf-28 .scene-3 {
  background: #06060a;
  border-bottom: 1px solid #111;
}

.kf-28 .wave-word {
  font-size: clamp(2.5rem, 9vw, 5rem);
  font-weight: 900;
  display: flex;
  gap: 2px;
  font-style: italic;
}

.kf-28 .wave-word span {
  display: inline-block;
  animation: kf-28-wave 2s ease-in-out infinite;
}

.kf-28 .wave-word span:nth-child(1) {
  color: #00d4ff;
  animation-delay: 0s;
}

.kf-28 .wave-word span:nth-child(2) {
  color: #20d8ff;
  animation-delay: 0.08s;
}

.kf-28 .wave-word span:nth-child(3) {
  color: #40dcfe;
  animation-delay: 0.16s;
}

.kf-28 .wave-word span:nth-child(4) {
  color: #5fdffe;
  animation-delay: 0.24s;
}

.kf-28 .wave-word span:nth-child(5) {
  color: #7fe3fd;
  animation-delay: 0.32s;
}

.kf-28 .wave-word span:nth-child(6) {
  color: #9fe6fc;
  animation-delay: 0.40s;
}

@keyframes kf-28-wave {
  0%,
    100% {
    transform: translateY(0) scaleY(1);
  }

  25% {
    transform: translateY(-20px) scaleY(1.1);
  }

  50% {
    transform: translateY(0) scaleY(1);
  }

  75% {
    transform: translateY(8px) scaleY(0.95);
  }
}
/* Scene 4: Scale pulse words */

.kf-28 .scene-4 {
  background: #070709;
  border-bottom: 1px solid #111;
}

.kf-28 .scale-words {
  display: flex;
  align-items: baseline;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
}

.kf-28 .scale-words .sw {
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  animation: kf-28-scalepulse 3s ease-in-out infinite;
}

.kf-28 .sw-1 {
  color: #f7c948;
  animation-delay: 0s;
}

.kf-28 .sw-2 {
  color: #fff;
  font-size: clamp(0.9rem, 3vw, 1.2rem) !important;
  animation-delay: 0.5s;
  font-weight: 300;
}

.kf-28 .sw-3 {
  color: #ff6b35;
  animation-delay: 1s;
}

.kf-28 .sw-4 {
  color: #fff;
  font-size: clamp(0.9rem, 3vw, 1.2rem) !important;
  animation-delay: 1.5s;
  font-weight: 300;
}

.kf-28 .sw-5 {
  color: #00d46a;
  animation-delay: 2s;
}

@keyframes kf-28-scalepulse {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.1);
  }
}
/* Scene 5: Glitch kinetic */

.kf-28 .scene-5 {
  background: #040406;
}

.kf-28 .glitch-kine {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3rem, 10vw, 5rem);
  letter-spacing: 6px;
  position: relative;
  color: #fff;
}

.kf-28 .glitch-kine::before {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  color: #e91e8c;
  animation: kf-28-glitch1 3s linear infinite;
  clip-path: polygon(0 30%, 100% 30%, 100% 60%, 0 60%);
}

.kf-28 .glitch-kine::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  color: #00d4ff;
  animation: kf-28-glitch2 3s linear infinite;
  clip-path: polygon(0 60%, 100% 60%, 100% 80%, 0 80%);
}

@keyframes kf-28-glitch1 {
  0%,
    85%,
    100% {
    transform: translate(0);
  }

  87% {
    transform: translate(-4px, 2px);
  }

  89% {
    transform: translate(4px, -2px);
  }

  91% {
    transform: translate(-4px, 0);
  }

  93% {
    transform: translate(3px, 1px);
  }

  95% {
    transform: translate(0);
  }
}

@keyframes kf-28-glitch2 {
  0%,
    80%,
    100% {
    transform: translate(0);
  }

  82% {
    transform: translate(4px, -3px);
  }

  84% {
    transform: translate(-3px, 2px);
  }

  86% {
    transform: translate(2px, -1px);
  }

  88% {
    transform: translate(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-28 .letter-drop span,
    .kf-28 .explode-word span,
    .kf-28 .wave-word span,
    .kf-28 .scale-words .sw,
    .kf-28 .glitch-kine::before,
    .kf-28 .glitch-kine::after {
    animation: none;
    transform: none;
  }
}
```
