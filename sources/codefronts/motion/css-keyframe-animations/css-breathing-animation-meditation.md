---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-breathing-animation-meditation/"
title: "CSS Breathing Animation Meditation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Six calming CSS breathing animations: classic expanding circle, box-breathing dot tracer, ripple rings, lotus bloom petals, SVG wave breath and…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Breathing Animation Meditation
Source: https://codefronts.com/motion/css-keyframe-animations/css-breathing-animation-meditation/

Six calming CSS breathing animations: classic expanding circle, box-breathing dot tracer, ripple rings, lotus bloom petals, SVG wave breath and stroke-dashoffset timer ring.
## HTML
```html
<div class="kf-24">
  <h2>CSS Breathing & Meditation Animations</h2>
  <div class="grid">

    <div class="breathe-card">
      <div class="breathe-circle"></div>
      <div class="breathe-label">breathe in · hold · breathe out</div>
      <label>Classic Breathing</label>
    </div>

    <div class="breathe-card">
      <div class="box-wrap">
        <div class="box-bg"></div>
        <div class="box-glow"></div>
        <div class="box-dot"></div>
      </div>
      <label>Box Breathing</label>
    </div>

    <div class="breathe-card">
      <div class="ripple-breath">
        <div class="ripple-ring"></div>
        <div class="ripple-ring"></div>
        <div class="ripple-ring"></div>
        <div class="ripple-core"></div>
      </div>
      <label>Ripple Breath</label>
    </div>

    <div class="breathe-card">
      <div class="lotus-wrap">
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="lotus-core"></div>
      </div>
      <label>Lotus Bloom</label>
    </div>

    <div class="breathe-card">
      <div class="wave-breath">
        <svg viewBox="0 0 200 80">
          <path d="M 0,40 Q 50,40 100,40 Q 150,40 200,40"/>
        </svg>
      </div>
      <label>Wave Breath</label>
    </div>

    <div class="breathe-card">
      <div class="timer-breath">
        <svg viewBox="0 0 120 120">
          <defs>
            <linearGradient id="kf24grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#7c6af7"/>
              <stop offset="100%" stop-color="#00d4ff"/>
            </linearGradient>
          </defs>
          <circle class="timer-track" cx="60" cy="60" r="52"/>
          <circle class="timer-prog" cx="60" cy="60" r="52"/>
        </svg>
        <div class="timer-text">◯</div>
      </div>
      <label>Breath Timer</label>
    </div>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

.kf-24 *,
.kf-24 *::before,
.kf-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-24 {
  font-family: 'Inter', sans-serif;
  background: #06080f;
  color: #fff;
  padding: 48px 24px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}

.kf-24 h2 {
  font-size: 1rem;
  color: #444;
  letter-spacing: 3px;
  text-transform: uppercase;
  font-weight: 300;
}

.kf-24 .grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 28px;
  width: 100%;
  max-width: 960px;
}
/* 1: Classic breathing circle */

.kf-24 .breathe-card {
  background: #0a0c18;
  border-radius: 20px;
  padding: 40px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  border: 1px solid #151830;
}

.kf-24 .breathe-card label {
  font-size: 0.75rem;
  color: #444;
  letter-spacing: 2px;
  text-transform: uppercase;
  font-weight: 300;
}

.kf-24 .breathe-circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(100,160,255,0.8) 0%, rgba(80,120,220,0.4) 50%, rgba(50,80,180,0.1) 100%);
  box-shadow: 0 0 0 0 rgba(100,160,255,0.4), 0 0 40px rgba(80,140,255,0.3);
  animation: kf-24-breathe 8s ease-in-out infinite;
}

@keyframes kf-24-breathe {
  0% {
    transform: scale(0.85);
    box-shadow: 0 0 0 0 rgba(100,160,255,0.6), 0 0 20px rgba(80,140,255,0.2);
  }

  35% {
    transform: scale(1.25);
    box-shadow: 0 0 0 20px rgba(100,160,255,0), 0 0 60px rgba(80,140,255,0.5);
  }

  65% {
    transform: scale(1.25);
    box-shadow: 0 0 0 0 rgba(100,160,255,0), 0 0 60px rgba(80,140,255,0.5);
  }

  100% {
    transform: scale(0.85);
    box-shadow: 0 0 0 0 rgba(100,160,255,0.6), 0 0 20px rgba(80,140,255,0.2);
  }
}

.kf-24 .breathe-label {
  font-size: 1rem;
  font-weight: 300;
  color: rgba(140,180,255,0.8);
  letter-spacing: 2px;
  animation: kf-24-breathe-label 8s ease-in-out infinite;
  text-align: center;
}

@keyframes kf-24-breathe-label {
  0%,
    5% {
    content: 'Breathe in';
    opacity: 0.5;
  }

  10% {
    opacity: 1;
  }

  30%,
    40% {
    opacity: 1;
  }

  45% {
    opacity: 0.3;
  }

  60% {
    opacity: 0.8;
  }

  80%,
    95% {
    opacity: 0.8;
  }

  100% {
    opacity: 0.5;
  }
}
/* 2: Box breathing */

.kf-24 .box-wrap {
  position: relative;
  width: 140px;
  height: 140px;
}

.kf-24 .box-bg {
  width: 100%;
  height: 100%;
  border-radius: 20px;
  background: #0f1020;
  border: 1px solid #1e2040;
}

.kf-24 .box-dot {
  position: absolute;
  width: 16px;
  height: 16px;
  background: #7c6af7;
  border-radius: 50%;
  top: -8px;
  left: -8px;
  box-shadow: 0 0 16px rgba(124,106,247,0.8);
  animation: kf-24-boxbreath 16s linear infinite;
}

@keyframes kf-24-boxbreath {
  0% {
    top: -8px;
    left: -8px;
  }

  25% {
    top: -8px;
    left: calc(100% - 8px);
  }

  50% {
    top: calc(100% - 8px);
    left: calc(100% - 8px);
  }

  75% {
    top: calc(100% - 8px);
    left: -8px;
  }

  100% {
    top: -8px;
    left: -8px;
  }
}

.kf-24 .box-glow {
  position: absolute;
  inset: 4px;
  border-radius: 16px;
  border: 2px solid transparent;
  animation: kf-24-boxglow 16s linear infinite;
}

@keyframes kf-24-boxglow {
  0%,
    100% {
    border-color: rgba(124,106,247,0.3);
  }

  12.5%,
    37.5%,
    62.5%,
    87.5% {
    border-color: rgba(124,106,247,0.8);
  }
}
/* 3: Ripple breath */

.kf-24 .ripple-breath {
  position: relative;
  width: 120px;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kf-24 .ripple-ring {
  position: absolute;
  border-radius: 50%;
  border: 2px solid rgba(0, 212, 106, 0.6);
  animation: kf-24-ripplering 4s ease-out infinite;
}

.kf-24 .ripple-ring:nth-child(1) {
  width: 40px;
  height: 40px;
  animation-delay: 0s;
}

.kf-24 .ripple-ring:nth-child(2) {
  width: 40px;
  height: 40px;
  animation-delay: 1s;
}

.kf-24 .ripple-ring:nth-child(3) {
  width: 40px;
  height: 40px;
  animation-delay: 2s;
}

.kf-24 .ripple-core {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: radial-gradient(circle, #00d46a, #00a050);
  z-index: 2;
  animation: kf-24-corePulse 4s ease-in-out infinite;
}

@keyframes kf-24-ripplering {
  0% {
    width: 40px;
    height: 40px;
    opacity: 0.8;
    border-color: rgba(0,212,106,0.8);
  }

  100% {
    width: 130px;
    height: 130px;
    opacity: 0;
    border-color: rgba(0,212,106,0);
  }
}

@keyframes kf-24-corePulse {
  0%,
    100% {
    transform: scale(0.9);
  }

  50% {
    transform: scale(1.1);
  }
}
/* 4: Petals / lotus breath */

.kf-24 .lotus-wrap {
  position: relative;
  width: 140px;
  height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kf-24 .petal {
  position: absolute;
  width: 40px;
  height: 60px;
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  transform-origin: bottom center;
  animation: kf-24-petal 6s ease-in-out infinite;
}

.kf-24 .petal:nth-child(1) {
  background: rgba(233,30,140,0.5);
  transform: rotate(0deg) translateY(-20px);
  animation-delay: 0s;
}

.kf-24 .petal:nth-child(2) {
  background: rgba(124,106,247,0.5);
  transform: rotate(45deg) translateY(-20px);
  animation-delay: 0.15s;
}

.kf-24 .petal:nth-child(3) {
  background: rgba(0,212,255,0.5);
  transform: rotate(90deg) translateY(-20px);
  animation-delay: 0.3s;
}

.kf-24 .petal:nth-child(4) {
  background: rgba(0,212,106,0.5);
  transform: rotate(135deg) translateY(-20px);
  animation-delay: 0.45s;
}

.kf-24 .petal:nth-child(5) {
  background: rgba(247,201,72,0.5);
  transform: rotate(180deg) translateY(-20px);
  animation-delay: 0.6s;
}

.kf-24 .petal:nth-child(6) {
  background: rgba(255,107,53,0.5);
  transform: rotate(225deg) translateY(-20px);
  animation-delay: 0.75s;
}

.kf-24 .petal:nth-child(7) {
  background: rgba(233,30,140,0.4);
  transform: rotate(270deg) translateY(-20px);
  animation-delay: 0.9s;
}

.kf-24 .petal:nth-child(8) {
  background: rgba(124,106,247,0.4);
  transform: rotate(315deg) translateY(-20px);
  animation-delay: 1.05s;
}

@keyframes kf-24-petal {
  0%,
    100% {
    transform: rotate(var(--r, 0deg)) translateY(-20px) scaleY(0.6);
    opacity: 0.5;
  }

  40%,
    60% {
    transform: rotate(var(--r, 0deg)) translateY(-25px) scaleY(1.1);
    opacity: 1;
  }
}
/* override with inline CSS instead; use nth-child combined with CSS vars via property */

.kf-24 .petal:nth-child(1) {
  --r: 0deg;
}

.kf-24 .petal:nth-child(2) {
  --r: 45deg;
}

.kf-24 .petal:nth-child(3) {
  --r: 90deg;
}

.kf-24 .petal:nth-child(4) {
  --r: 135deg;
}

.kf-24 .petal:nth-child(5) {
  --r: 180deg;
}

.kf-24 .petal:nth-child(6) {
  --r: 225deg;
}

.kf-24 .petal:nth-child(7) {
  --r: 270deg;
}

.kf-24 .petal:nth-child(8) {
  --r: 315deg;
}

.kf-24 .lotus-core {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: radial-gradient(circle, #fff 0%, rgba(255,255,255,0.3) 100%);
  z-index: 2;
  animation: kf-24-lotuscore 6s ease-in-out infinite;
}

@keyframes kf-24-lotuscore {
  0%,
    100% {
    transform: scale(0.8);
    opacity: 0.5;
  }

  50% {
    transform: scale(1.1);
    opacity: 1;
  }
}
/* 5: Waveform breathing */

.kf-24 .wave-breath {
  width: 200px;
  height: 80px;
  overflow: hidden;
  position: relative;
}

.kf-24 .wave-breath svg {
  width: 100%;
  height: 100%;
}

.kf-24 .wave-breath path {
  fill: none;
  stroke: rgba(0,212,255,0.8);
  stroke-width: 2.5;
  stroke-linecap: round;
  animation: kf-24-wavepath 4s ease-in-out infinite;
}

@keyframes kf-24-wavepath {
  0% {
    d: path("M 0,40 Q 50,40 100,40 Q 150,40 200,40");
    opacity: 0.5;
  }

  25% {
    d: path("M 0,40 Q 50,5  100,40 Q 150,75 200,40");
    opacity: 1;
  }

  50% {
    d: path("M 0,40 Q 50,40 100,40 Q 150,40 200,40");
    opacity: 0.5;
  }

  75% {
    d: path("M 0,40 Q 50,75 100,40 Q 150,5  200,40");
    opacity: 1;
  }

  100% {
    d: path("M 0,40 Q 50,40 100,40 Q 150,40 200,40");
    opacity: 0.5;
  }
}
/* 6: Timer circle */

.kf-24 .timer-breath {
  position: relative;
  width: 120px;
  height: 120px;
}

.kf-24 .timer-breath svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.kf-24 .timer-track {
  fill: none;
  stroke: #1e2040;
  stroke-width: 6;
}

.kf-24 .timer-prog {
  fill: none;
  stroke: url(#kf24grad);
  stroke-width: 6;
  stroke-linecap: round;
  stroke-dasharray: 327;
  animation: kf-24-timerprog 8s linear infinite;
}

@keyframes kf-24-timerprog {
  0% {
    stroke-dashoffset: 327;
  }

  100% {
    stroke-dashoffset: 0;
  }
}

.kf-24 .timer-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.4rem;
  font-weight: 300;
  color: rgba(180,200,255,0.9);
  animation: kf-24-timertext 8s linear infinite;
}

@keyframes kf-24-timertext {
  0% {
    content: '8';
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-24 .breathe-circle,
    .kf-24 .breathe-label,
    .kf-24 .box-dot,
    .kf-24 .box-glow,
    .kf-24 .ripple-ring,
    .kf-24 .ripple-core,
    .kf-24 .petal,
    .kf-24 .lotus-core,
    .kf-24 .wave-breath path,
    .kf-24 .timer-prog {
    animation: none;
  }
}
```
