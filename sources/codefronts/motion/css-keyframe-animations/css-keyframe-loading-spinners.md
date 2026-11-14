---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-keyframe-loading-spinners/"
title: "CSS Keyframe Loading Spinners"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Nine animated CSS loading spinners — ring, dual-rotate, dot orbit, morph shape, pulse dots, audio wave, comet trail, folding grid, and progress sweep — each…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Keyframe Loading Spinners
Source: https://codefronts.com/motion/css-keyframe-animations/css-keyframe-loading-spinners/

Nine animated CSS loading spinners — ring, dual-rotate, dot orbit, morph shape, pulse dots, audio wave, comet trail, folding grid, and progress sweep — each driven by a single scoped keyframe.
## HTML
```html
<div class="kf-01">
  <div class="kf-01__stage">
    <div class="kf-01__cell">
      <div class="kf-01__ring"></div>
      <span class="kf-01__label">Classic Ring</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__dual"><i></i><i></i></div>
      <span class="kf-01__label">Dual Rotate</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__orbit"><span></span><span></span><span></span><span></span></div>
      <span class="kf-01__label">Dot Orbit</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__morph"></div>
      <span class="kf-01__label">Morph Shape</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__dots"><span></span><span></span><span></span></div>
      <span class="kf-01__label">Pulse Dots</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__wave"><span></span><span></span><span></span><span></span><span></span></div>
      <span class="kf-01__label">Audio Wave</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__comet"></div>
      <span class="kf-01__label">Comet Trail</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__fold"><span></span><span></span><span></span><span></span></div>
      <span class="kf-01__label">Folding Grid</span>
    </div>
    <div class="kf-01__cell">
      <div class="kf-01__bar"><div class="kf-01__bar-track"><div class="kf-01__bar-fill"></div></div></div>
      <span class="kf-01__label">Progress Sweep</span>
    </div>
  </div>
</div>
```
## CSS
```css
.kf-01,
.kf-01 *,
.kf-01 *::before,
.kf-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-01 ::selection {
  background: #6c63ff;
  color: #fff;
}

.kf-01 {
  --bg: #0f0e17;
  --purple: #6c63ff;
  --pink: #ff6584;
  --cyan: #43e8d8;
  --gold: #ffd166;
  --white: #fffffe;
  font-family: 'Segoe UI',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.kf-01__stage {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 40px;
  max-width: 860px;
  width: 100%;
}

.kf-01__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 32px 20px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 16px;
}

.kf-01__label {
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(255,255,255,.4);
  text-align: center;
}
/* 1 — classic ring */

.kf-01__ring {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  border: 4px solid rgba(108,99,255,.2);
  border-top-color: var(--purple);
  animation: kf-01-spin .9s linear infinite;
}

@keyframes kf-01-spin {
  to {
    transform: rotate(360deg);
  }
}
/* 2 — dual counter-rotate */

.kf-01__dual {
  width: 64px;
  height: 64px;
  position: relative;
}

.kf-01__dual i {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 4px solid transparent;
}

.kf-01__dual i:nth-child(1) {
  border-top-color: var(--pink);
  border-right-color: var(--pink);
  animation: kf-01-spin .8s linear infinite;
}

.kf-01__dual i:nth-child(2) {
  inset: 12px;
  border-bottom-color: var(--cyan);
  border-left-color: var(--cyan);
  animation: kf-01-spin .8s linear infinite reverse;
}
/* 3 — dotted orbit */

.kf-01__orbit {
  width: 64px;
  height: 64px;
  position: relative;
  animation: kf-01-spin 1.4s linear infinite;
}

.kf-01__orbit span {
  position: absolute;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--gold);
  top: 0;
  left: 50%;
  transform: translateX(-50%);
}

.kf-01__orbit span:nth-child(2) {
  animation: kf-01-spin 1.4s linear infinite reverse;
  background: var(--purple);
  top: auto;
  bottom: 0;
}

.kf-01__orbit span:nth-child(3) {
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  background: var(--pink);
}

.kf-01__orbit span:nth-child(4) {
  top: 50%;
  right: 0;
  left: auto;
  transform: translateY(-50%);
  background: var(--cyan);
}
/* 4 — morphing square */

.kf-01__morph {
  width: 52px;
  height: 52px;
  background: var(--purple);
  animation: kf-01-morph 1.6s ease-in-out infinite;
}

@keyframes kf-01-morph {
  0% {
    border-radius: 0;
    transform: rotate(0);
  }

  25% {
    border-radius: 50%;
    transform: rotate(90deg);
  }

  50% {
    border-radius: 0;
    transform: rotate(180deg) scaleX(.5);
  }

  75% {
    border-radius: 50%;
    transform: rotate(270deg);
  }

  100% {
    border-radius: 0;
    transform: rotate(360deg);
  }
}
/* 5 — pulse dots */

.kf-01__dots {
  display: flex;
  gap: 10px;
  align-items: center;
}

.kf-01__dots span {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--cyan);
  animation: kf-01-pulse 1.2s ease-in-out infinite;
}

.kf-01__dots span:nth-child(2) {
  animation-delay: .2s;
  background: var(--purple);
}

.kf-01__dots span:nth-child(3) {
  animation-delay: .4s;
  background: var(--pink);
}

@keyframes kf-01-pulse {
  0%,
    80%,
    100% {
    transform: scale(.6);
    opacity: .4;
  }

  40% {
    transform: scale(1);
    opacity: 1;
  }
}
/* 6 — wave bars */

.kf-01__wave {
  display: flex;
  gap: 5px;
  align-items: flex-end;
  height: 48px;
}

.kf-01__wave span {
  width: 8px;
  border-radius: 4px 4px 0 0;
  background: var(--gold);
  animation: kf-01-wave 1s ease-in-out infinite;
}

.kf-01__wave span:nth-child(1) {
  animation-delay: 0s;
}

.kf-01__wave span:nth-child(2) {
  animation-delay: .1s;
}

.kf-01__wave span:nth-child(3) {
  animation-delay: .2s;
}

.kf-01__wave span:nth-child(4) {
  animation-delay: .3s;
}

.kf-01__wave span:nth-child(5) {
  animation-delay: .4s;
}

@keyframes kf-01-wave {
  0%,
    100% {
    height: 12px;
    opacity: .4;
  }

  50% {
    height: 42px;
    opacity: 1;
  }
}
/* 7 — comet trail */

.kf-01__comet {
  width: 64px;
  height: 64px;
  position: relative;
}

.kf-01__comet::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(transparent 60%,var(--pink));
  animation: kf-01-spin .8s linear infinite;
}

.kf-01__comet::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 10px;
  height: 10px;
  margin: -5px 0 0 -5px;
  border-radius: 50%;
  background: var(--white);
  box-shadow: 0 0 12px var(--pink);
}
/* 8 — folding squares */

.kf-01__fold {
  width: 40px;
  height: 40px;
  position: relative;
  transform: rotate(45deg);
}

.kf-01__fold span {
  position: absolute;
  width: 50%;
  height: 50%;
  background: var(--purple);
}

.kf-01__fold span:nth-child(1) {
  top: 0;
  left: 0;
  animation: kf-01-fold 2s ease-in-out infinite;
}

.kf-01__fold span:nth-child(2) {
  top: 0;
  right: 0;
  background: var(--cyan);
  animation: kf-01-fold 2s ease-in-out infinite .5s;
}

.kf-01__fold span:nth-child(3) {
  bottom: 0;
  right: 0;
  background: var(--pink);
  animation: kf-01-fold 2s ease-in-out infinite 1s;
}

.kf-01__fold span:nth-child(4) {
  bottom: 0;
  left: 0;
  background: var(--gold);
  animation: kf-01-fold 2s ease-in-out infinite 1.5s;
}

@keyframes kf-01-fold {
  0%,
    10%,
    90%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0;
    transform: scale(0);
  }
}
/* 9 — progress bar */

.kf-01__bar {
  width: 100%;
  max-width: 160px;
}

.kf-01__bar-track {
  height: 6px;
  background: rgba(255,255,255,.1);
  border-radius: 3px;
  overflow: hidden;
}

.kf-01__bar-fill {
  height: 100%;
  border-radius: 3px;
  background: linear-gradient(90deg,var(--purple),var(--pink));
  animation: kf-01-bar 2s ease-in-out infinite;
}

@keyframes kf-01-bar {
  0% {
    width: 0%;
    margin-left: 0;
  }

  50% {
    width: 80%;
  }

  100% {
    width: 0%;
    margin-left: 100%;
  }
}

@media (max-width: 640px) {
  .kf-01__stage {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 380px) {
  .kf-01__stage {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-01 * {
    animation: none!important;
  }
}
```
