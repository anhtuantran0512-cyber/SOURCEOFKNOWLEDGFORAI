---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-fire-animation-pure-css/"
title: "CSS Fire Animation Pure CSS"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Pure CSS fire: flickering candle with wick and wax, campfire with log base and IGNITE flame text — radial gradient bodies animated with scale and blur…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Fire Animation Pure CSS
Source: https://codefronts.com/motion/css-keyframe-animations/css-fire-animation-pure-css/

Pure CSS fire: flickering candle with wick and wax, campfire with log base and IGNITE flame text — radial gradient bodies animated with scale and blur keyframes.
## HTML
```html
<div class="kf-15">
  <div class="kf-15__text">IGNITE</div>
  <div class="kf-15__row">
    <div>
      <div class="kf-15__candle">
        <div class="kf-15__flame-wrap">
          <div class="kf-15__flame kf-15__f1"></div>
          <div class="kf-15__flame kf-15__f2"></div>
          <div class="kf-15__flame kf-15__f3"></div>
          <div class="kf-15__glow"></div>
        </div>
        <div class="kf-15__wick"></div>
        <div class="kf-15__wax"></div>
      </div>
      <div class="kf-15__label">Candle</div>
    </div>
    <div>
      <div class="kf-15__camp">
        <div class="kf-15__camp-flame">
          <div class="kf-15__cf kf-15__cf--5"></div>
          <div class="kf-15__cf kf-15__cf--4"></div>
          <div class="kf-15__cf kf-15__cf--1"></div>
          <div class="kf-15__cf kf-15__cf--2"></div>
          <div class="kf-15__cf kf-15__cf--3"></div>
        </div>
        <div class="kf-15__logs">
          <div class="kf-15__log"></div>
          <div class="kf-15__log"></div>
          <div class="kf-15__log"></div>
        </div>
      </div>
      <div class="kf-15__label">Campfire</div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Roboto+Mono:wght@500&display=swap');

.kf-15,
.kf-15 *,
.kf-15 *::before,
.kf-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-15 ::selection {
  background: #ff4500;
  color: #fff;
}

.kf-15 {
  --bg: #0d0800;
  --flame1: #ff4500;
  --flame2: #ff8c00;
  --flame3: #ffd700;
  --flame4: #fff5c0;
  font-family: 'Black Ops One',sans-serif;
  background: radial-gradient(circle at 50% 80%,#1a0800 0%,#0d0800 60%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 60px;
  overflow: hidden;
  position: relative;
  color: #ffd700;
}
/* ember particles */

.kf-15::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: radial-gradient(1px 1px at 20% 40%,rgba(255,69,0,.8),transparent), radial-gradient(1px 1px at 60% 20%,rgba(255,140,0,.6),transparent), radial-gradient(1.5px 1.5px at 80% 50%,rgba(255,215,0,.5),transparent);
  animation: kf-15-ember 3s linear infinite;
}

@keyframes kf-15-ember {
  to {
    background-position: 0 -200px;
    opacity: 0;
  }
}
/* ——— Candle flame ——— */

.kf-15__candle {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

.kf-15__flame-wrap {
  position: relative;
  width: 60px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.kf-15__flame {
  position: absolute;
  bottom: 0;
  border-radius: 50% 50% 20% 20%/60% 60% 40% 40%;
  filter: blur(1px);
  transform-origin: 50% 100%;
}

.kf-15__f1 {
  width: 28px;
  height: 80px;
  background: linear-gradient(180deg,var(--flame4) 0%,var(--flame3) 30%,var(--flame2) 65%,var(--flame1) 100%);
  animation: kf-15-flicker 0.8s ease-in-out infinite;
}

.kf-15__f2 {
  width: 22px;
  height: 64px;
  background: linear-gradient(180deg,#fff 0%,var(--flame4) 30%,var(--flame3) 70%,transparent 100%);
  animation: kf-15-flicker 0.6s ease-in-out infinite reverse;
}

.kf-15__f3 {
  width: 14px;
  height: 48px;
  background: linear-gradient(180deg,#fff 0%,rgba(255,245,192,.8) 50%,transparent 100%);
  animation: kf-15-flicker 0.9s ease-in-out infinite 0.2s;
}

@keyframes kf-15-flicker {
  0%,
    100% {
    transform: scaleX(1) scaleY(1) rotate(-2deg);
  }

  25% {
    transform: scaleX(0.88) scaleY(1.06) rotate(2deg);
  }

  50% {
    transform: scaleX(1.05) scaleY(0.96) rotate(-1deg);
  }

  75% {
    transform: scaleX(0.92) scaleY(1.04) rotate(1.5deg);
  }
}

.kf-15__wick {
  width: 3px;
  height: 14px;
  background: linear-gradient(180deg,#333,#888);
  margin-top: 0;
  z-index: 2;
  position: relative;
}

.kf-15__wax {
  width: 50px;
  height: 100px;
  background: linear-gradient(90deg,#f0ebe0,#e8e0d0 50%,#d8d0c0);
  border-radius: 4px;
  position: relative;
  display: flex;
  justify-content: center;
}

.kf-15__wax::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 30px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,220,180,.4);
  animation: kf-15-melt 3s ease-in-out infinite;
}

@keyframes kf-15-melt {
  50% {
    transform: translateX(-50%) scaleX(1.1);
    background: rgba(255,200,150,.3);
  }
}

.kf-15__glow {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 40px;
  background: radial-gradient(ellipse,rgba(255,140,0,.3),transparent);
  filter: blur(8px);
  animation: kf-15-glow 0.8s ease-in-out infinite alternate;
}

@keyframes kf-15-glow {
  to {
    opacity: .6;
    transform: translateX(-50%) scale(1.2);
  }
}
/* ——— Campfire ——— */

.kf-15__camp {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

.kf-15__logs {
  width: 120px;
  height: 24px;
  position: relative;
}

.kf-15__log {
  position: absolute;
  width: 80px;
  height: 12px;
  border-radius: 6px;
  background: linear-gradient(180deg,#5a3a1a,#3a2010);
}

.kf-15__log:nth-child(1) {
  bottom: 0;
  left: 20px;
}

.kf-15__log:nth-child(2) {
  bottom: 0;
  left: 20px;
  transform: rotate(40deg);
  transform-origin: 40% 50%;
}

.kf-15__log:nth-child(3) {
  bottom: 0;
  left: 20px;
  transform: rotate(-40deg);
  transform-origin: 60% 50%;
}

.kf-15__camp-flame {
  position: relative;
  width: 120px;
  height: 120px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.kf-15__cf {
  position: absolute;
  bottom: 0;
  border-radius: 50% 50% 20% 20%/60% 60% 40% 40%;
  transform-origin: 50% 100%;
  filter: blur(2px);
}

.kf-15__cf--1 {
  width: 60px;
  height: 100px;
  background: linear-gradient(180deg,var(--flame4),var(--flame3) 30%,var(--flame2) 65%,var(--flame1));
  animation: kf-15-flicker 1.1s ease-in-out infinite;
}

.kf-15__cf--2 {
  width: 44px;
  height: 82px;
  background: linear-gradient(180deg,#fff,var(--flame4) 30%,var(--flame3) 70%,transparent);
  animation: kf-15-flicker 0.7s ease-in-out infinite 0.1s;
}

.kf-15__cf--3 {
  width: 28px;
  height: 60px;
  background: linear-gradient(180deg,#fff,rgba(255,245,192,.9),transparent);
  animation: kf-15-flicker 0.9s ease-in-out infinite 0.3s;
}

.kf-15__cf--4 {
  width: 70px;
  height: 60px;
  left: 0;
  right: 0;
  margin: 0 auto;
  background: linear-gradient(180deg,transparent,var(--flame1) 50%,transparent);
  animation: kf-15-flicker 1.3s ease-in-out infinite;
  filter: blur(3px);
}

.kf-15__cf--5 {
  width: 50px;
  height: 40px;
  left: 0;
  right: 0;
  margin: 0 auto;
  background: var(--flame2);
  border-radius: 50%;
  bottom: 0;
  animation: kf-15-flicker 0.6s ease-in-out infinite 0.4s;
  filter: blur(4px);
}
/* ——— Torch text ——— */

.kf-15__text {
  font-size: clamp(2.5rem,10vw,5rem);
  letter-spacing: .1em;
  color: var(--flame2);
  text-shadow: 0 0 10px var(--flame1), 0 0 30px var(--flame2), 0 0 60px rgba(255,140,0,.4);
  animation: kf-15-text 2s ease-in-out infinite alternate;
  position: relative;
}

@keyframes kf-15-text {
  from {
    text-shadow: 0 0 10px var(--flame1),0 0 30px var(--flame2),0 0 60px rgba(255,140,0,.4);
  }

  to {
    text-shadow: 0 0 15px var(--flame3),0 0 40px var(--flame3),0 0 80px rgba(255,200,0,.5),0 0 120px rgba(255,140,0,.3);
  }
}

.kf-15__row {
  display: flex;
  gap: 60px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-end;
}

.kf-15__label {
  font-family: 'Roboto Mono';
  font-size: .7rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: rgba(255,140,0,.4);
  text-align: center;
  margin-top: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .kf-15 * {
    animation: none!important;
  }
}
```
