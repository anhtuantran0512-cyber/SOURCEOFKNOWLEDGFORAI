---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-bouncing-ball-animation/"
title: "CSS Bouncing Ball Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Realistic bouncing ball physics with squash-and-stretch, pendulum swing, stagger trio and rolling ball — all driven by cubic-bezier keyframes, no JavaScript."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Bouncing Ball Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-bouncing-ball-animation/

Realistic bouncing ball physics with squash-and-stretch, pendulum swing, stagger trio and rolling ball — all driven by cubic-bezier keyframes, no JavaScript.
## HTML
```html
<div class="kf-03">
  <div class="kf-03__title">CSS Bouncing Ball <span>Physics</span> Animations</div>

  <div class="kf-03__row">
    <div class="kf-03__scene">
      <div class="kf-03__arena">
        <div class="kf-03__ball kf-03__ball--1"></div>
        <div class="kf-03__shadow kf-03__shadow--1"></div>
      </div>
      <div class="kf-03__floor"></div>
      <div class="kf-03__label">Simple<br>Bounce</div>
    </div>

    <div class="kf-03__scene">
      <div class="kf-03__arena">
        <div class="kf-03__ball kf-03__ball--2"></div>
        <div class="kf-03__shadow kf-03__shadow--2"></div>
      </div>
      <div class="kf-03__floor"></div>
      <div class="kf-03__label">Squash &<br>Stretch</div>
    </div>

    <div class="kf-03__scene" style="width:80px">
      <div class="kf-03__pend" style="overflow:visible">
        <div class="kf-03__string">
          <div class="kf-03__pball"></div>
        </div>
      </div>
      <div class="kf-03__floor"></div>
      <div class="kf-03__label">Pendulum<br>Swing</div>
    </div>

    <div class="kf-03__scene" style="width:80px">
      <div class="kf-03__arena" style="width:80px">
        <div class="kf-03__triple">
          <div class="kf-03__ball--t"></div>
          <div class="kf-03__ball--t"></div>
          <div class="kf-03__ball--t"></div>
        </div>
      </div>
      <div class="kf-03__floor"></div>
      <div class="kf-03__label">Stagger<br>Trio</div>
    </div>
  </div>

  <div style="display:flex;flex-direction:column;align-items:center;gap:8px">
    <div class="kf-03__roll-wrap">
      <div class="kf-03__ball kf-03__ball--r"></div>
    </div>
    <div class="kf-03__label">Rolling Ball</div>
  </div>
</div>
```
## CSS
```css
.kf-03,
.kf-03 *,
.kf-03 *::before,
.kf-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-03 ::selection {
  background: #f72585;
  color: #fff;
}

.kf-03 {
  --bg: #fafaf8;
  --floor: #e8e5e0;
  --red: #f72585;
  --orange: #fb8500;
  --blue: #3a86ff;
  --green: #06d6a0;
  --purple: #7b2d8b;
  --shadow: rgba(0,0,0,.18);
  font-family: 'Segoe UI',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  gap: 48px;
  color: #1a1a1a;
}

.kf-03__label {
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #999;
  text-align: center;
  margin-top: 16px;
}

.kf-03__title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  letter-spacing: -.02em;
  text-align: center;
  color: #1a1a1a;
}

.kf-03__title span {
  color: var(--red);
}
/* Scene container */

.kf-03__row {
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-end;
}

.kf-03__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  width: 80px;
}

.kf-03__arena {
  width: 80px;
  height: 180px;
  position: relative;
  display: flex;
  justify-content: center;
}

.kf-03__floor {
  width: 100%;
  height: 4px;
  background: var(--floor);
  border-radius: 2px;
  box-shadow: 0 2px 0 #d8d5d0;
}
/* Ball base */

.kf-03__ball {
  position: absolute;
  border-radius: 50%;
  left: 50%;
  transform: translateX(-50%);
}
/* Shadow base */

.kf-03__shadow {
  position: absolute;
  bottom: 4px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--shadow);
  border-radius: 50%;
}
/* 1 — Simple bounce */

.kf-03__ball--1 {
  width: 42px;
  height: 42px;
  bottom: 4px;
  background: radial-gradient(circle at 36% 28%,#ff9eb5,var(--red));
  animation: kf-03-bounce1 0.7s cubic-bezier(.33,0,.66,0) infinite alternate;
}

.kf-03__shadow--1 {
  width: 36px;
  height: 10px;
  animation: kf-03-sh1 0.7s ease-in-out infinite alternate;
}

@keyframes kf-03-bounce1 {
  to {
    bottom: 130px;
  }
}

@keyframes kf-03-sh1 {
  from {
    opacity: .3;
    transform: translateX(-50%) scaleX(1);
  }

  to {
    opacity: .06;
    transform: translateX(-50%) scaleX(.4);
  }
}
/* 2 — Squash & stretch */

.kf-03__ball--2 {
  width: 44px;
  height: 44px;
  bottom: 4px;
  background: radial-gradient(circle at 36% 28%,#ffc06a,var(--orange));
  animation: kf-03-squash 0.8s ease-in-out infinite;
}

.kf-03__shadow--2 {
  width: 36px;
  height: 10px;
  animation: kf-03-sh2 0.8s ease-in-out infinite;
}

@keyframes kf-03-squash {
  0% {
    bottom: 4px;
    height: 30px;
    width: 52px;
    border-radius: 50%/30%;
  }

  20% {
    bottom: 100px;
    height: 48px;
    width: 36px;
    border-radius: 50%;
  }

  40% {
    bottom: 140px;
    height: 52px;
    width: 34px;
  }

  60% {
    bottom: 80px;
    height: 48px;
    width: 36px;
  }

  80% {
    bottom: 4px;
    height: 26px;
    width: 56px;
    border-radius: 50%/30%;
  }

  100% {
    bottom: 4px;
    height: 30px;
    width: 52px;
    border-radius: 50%/30%;
  }
}

@keyframes kf-03-sh2 {
  0%,
    80%,
    100% {
    opacity: .4;
    transform: translateX(-50%) scaleX(1.2);
  }

  40% {
    opacity: .06;
    transform: translateX(-50%) scaleX(.3);
  }
}
/* 3 — Pendulum swing */

.kf-03__pend {
  width: 80px;
  height: 180px;
  position: relative;
  display: flex;
  justify-content: center;
  overflow: visible;
}

.kf-03__string {
  position: absolute;
  top: 8px;
  left: 50%;
  width: 2px;
  height: 110px;
  background: #ccc;
  transform-origin: top center;
  animation: kf-03-pend 1.2s ease-in-out infinite alternate;
}

@keyframes kf-03-pend {
  from {
    transform: rotate(-35deg);
  }

  to {
    transform: rotate(35deg);
  }
}

.kf-03__pball {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: radial-gradient(circle at 36% 28%,#90e0ef,var(--blue));
}
/* 4 — Triple bounce stagger */

.kf-03__triple {
  display: flex;
  gap: 12px;
  align-items: flex-end;
  position: relative;
  height: 180px;
  padding: 0 4px;
}

.kf-03__ball--t {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  position: absolute;
  bottom: 4px;
}

.kf-03__ball--t:nth-child(1) {
  left: 4px;
  background: var(--green);
  animation: kf-03-bounce1 0.7s cubic-bezier(.33,0,.66,0) infinite alternate;
}

.kf-03__ball--t:nth-child(2) {
  left: 27px;
  background: var(--blue);
  animation: kf-03-bounce1 0.7s cubic-bezier(.33,0,.66,0) .15s infinite alternate;
}

.kf-03__ball--t:nth-child(3) {
  left: 50px;
  background: var(--purple);
  animation: kf-03-bounce1 0.7s cubic-bezier(.33,0,.66,0) .3s infinite alternate;
}
/* 5 — Rolling ball */

.kf-03__roll-wrap {
  width: 180px;
  height: 70px;
  position: relative;
  border-bottom: 4px solid var(--floor);
  border-radius: 0 0 4px 4px;
}

.kf-03__ball--r {
  width: 46px;
  height: 46px;
  bottom: 4px;
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle at 36% 28%,#c9b8ff,var(--purple));
  animation: kf-03-roll-x 2s linear infinite,kf-03-roll-spin 2s linear infinite;
}

@keyframes kf-03-roll-x {
  0% {
    left: -46px;
  }

  100% {
    left: 180px;
  }
}

@keyframes kf-03-roll-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 600px) {
  .kf-03__row {
    gap: 24px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-03 * {
    animation: none!important;
  }
}
```
