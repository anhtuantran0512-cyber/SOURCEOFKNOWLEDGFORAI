---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-neon-sign-flicker-animation/"
title: "CSS Neon Sign Flicker Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Five neon sign animations: cursive pink glow, cyan monospace, OPEN sign box, script yellow hum and multi-word stagger flicker using box-shadow and opacity…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Sign Flicker Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-neon-sign-flicker-animation/

Five neon sign animations: cursive pink glow, cyan monospace, OPEN sign box, script yellow hum and multi-word stagger flicker using box-shadow and opacity keyframes.
## HTML
```html
<div class="kf-09">
  <div class="kf-09__sign">
    <div class="kf-09__s1">Electric Dreams</div>
  </div>

  <div class="kf-09__sign">
    <div class="kf-09__s2">NEON DISTRICT</div>
  </div>

  <div class="kf-09__sign">
    <div class="kf-09__sign-box">
      <div class="kf-09__s3">OPEN</div>
    </div>
  </div>

  <div class="kf-09__sign">
    <div class="kf-09__s4">Late Night Vibes</div>
  </div>

  <div class="kf-09__sign">
    <div class="kf-09__multirow">
      <span class="kf-09__word">LIVE</span>
      <span class="kf-09__word">·</span>
      <span class="kf-09__word">CODE</span>
      <span class="kf-09__word">·</span>
      <span class="kf-09__word">CREATE</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Bebas+Neue&family=Sacramento&display=swap');

.kf-09,
.kf-09 *,
.kf-09 *::before,
.kf-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-09 ::selection {
  background: #ff2dce;
  color: #fff;
}

.kf-09 {
  --bg: #0a0008;
  --pink: #ff2dce;
  --cyan: #00fff5;
  --red: #ff3030;
  --yellow: #fff200;
  --blue: #4d79ff;
  --green: #39ff14;
  font-family: 'Bebas Neue',sans-serif;
  background: radial-gradient(circle at 50% 40%,#1a0b2e 0%,#0a0008 70%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 56px;
  overflow: hidden;
  position: relative;
}
/* Brick wall texture */

.kf-09::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(rgba(255,255,255,.02) 0 2px,transparent 2px 40px), repeating-linear-gradient(90deg,rgba(255,255,255,.015) 0 2px,transparent 2px 80px);
  pointer-events: none;
}
/* Floor reflection */

.kf-09::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 30%;
  background: linear-gradient(0deg,rgba(255,45,206,.08),transparent);
  pointer-events: none;
}
/* Shared neon base */

.kf-09__sign {
  text-align: center;
  position: relative;
}
/* 1 — Pink cursive */

.kf-09__s1 {
  font-family: 'Pacifico',cursive;
  font-size: clamp(2.4rem,10vw,5rem);
  color: var(--pink);
  text-shadow: 0 0 7px var(--pink), 0 0 20px var(--pink), 0 0 45px var(--pink), 0 0 80px rgba(255,45,206,.5);
  animation: kf-09-flicker1 6s steps(1) infinite;
}

@keyframes kf-09-flicker1 {
  0%,
    18%,
    22%,
    25%,
    53%,
    57%,
    100% {
    text-shadow: 0 0 7px var(--pink),0 0 20px var(--pink),0 0 45px var(--pink),0 0 80px rgba(255,45,206,.5);
    opacity: 1;
  }

  20%,
    24% {
    text-shadow: none;
    opacity: .4;
  }

  54% {
    opacity: .7;
    text-shadow: 0 0 7px var(--pink);
  }

  55%,
    56% {
    text-shadow: none;
    opacity: .3;
  }
}
/* 2 — Cyan mono */

.kf-09__s2 {
  font-family: 'Bebas Neue',sans-serif;
  font-size: clamp(2rem,8vw,4rem);
  letter-spacing: .2em;
  color: var(--cyan);
  text-shadow: 0 0 5px var(--cyan), 0 0 15px var(--cyan), 0 0 30px rgba(0,255,245,.4);
  animation: kf-09-flicker2 8s steps(1) infinite 1s;
}

@keyframes kf-09-flicker2 {
  0%,
    49%,
    51%,
    100% {
    opacity: 1;
    text-shadow: 0 0 5px var(--cyan),0 0 15px var(--cyan),0 0 30px rgba(0,255,245,.4);
  }

  50% {
    opacity: .1;
    text-shadow: none;
  }
}
/* 3 — Red OPEN sign */

.kf-09__sign-box {
  border: 4px solid var(--red);
  border-radius: 8px;
  padding: 12px 32px;
  display: inline-block;
  position: relative;
  box-shadow: 0 0 12px var(--red), 0 0 30px rgba(255,48,48,.4), inset 0 0 12px rgba(255,48,48,.1);
  animation: kf-09-box 5s steps(1) infinite 2s;
}

@keyframes kf-09-box {
  0%,
    89%,
    91%,
    93%,
    100% {
    box-shadow: 0 0 12px var(--red),0 0 30px rgba(255,48,48,.4),inset 0 0 12px rgba(255,48,48,.1);
  }

  90%,
    92% {
    box-shadow: none;
  }
}

.kf-09__s3 {
  font-size: clamp(1.8rem,6vw,3rem);
  color: var(--red);
  letter-spacing: .3em;
  text-shadow: 0 0 8px var(--red),0 0 20px rgba(255,48,48,.5);
  animation: kf-09-box 5s steps(1) infinite 2s;
}
/* Dots on box */

.kf-09__sign-box::before,
.kf-09__sign-box::after {
  content: '●';
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 12px;
  color: var(--red);
  text-shadow: 0 0 6px var(--red);
}

.kf-09__sign-box::before {
  left: -20px;
}

.kf-09__sign-box::after {
  right: -20px;
}
/* 4 — Script + glow halo */

.kf-09__s4 {
  font-family: 'Sacramento',cursive;
  font-size: clamp(2.4rem,8vw,4.5rem);
  color: var(--yellow);
  text-shadow: 0 0 6px var(--yellow), 0 0 18px var(--yellow), 0 0 40px rgba(255,242,0,.5);
  animation: kf-09-hum 2.5s ease-in-out infinite;
}

@keyframes kf-09-hum {
  0%,
    100% {
    text-shadow: 0 0 6px var(--yellow),0 0 18px var(--yellow),0 0 40px rgba(255,242,0,.5);
  }

  50% {
    text-shadow: 0 0 8px var(--yellow),0 0 25px var(--yellow),0 0 60px rgba(255,242,0,.7),0 0 90px rgba(255,242,0,.3);
  }
}
/* 5 — Multi-word stagger flicker */

.kf-09__multirow {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.kf-09__word {
  font-size: clamp(1.4rem,5vw,2.8rem);
  letter-spacing: .15em;
}

.kf-09__word:nth-child(1) {
  color: var(--pink);
  text-shadow: 0 0 10px var(--pink),0 0 30px rgba(255,45,206,.5);
  animation: kf-09-flicker1 7s steps(1) infinite 0s;
}

.kf-09__word:nth-child(2) {
  color: var(--blue);
  text-shadow: 0 0 10px var(--blue),0 0 30px rgba(77,121,255,.5);
  animation: kf-09-flicker2 9s steps(1) infinite .5s;
}

.kf-09__word:nth-child(3) {
  color: var(--green);
  text-shadow: 0 0 10px var(--green),0 0 30px rgba(57,255,20,.5);
  animation: kf-09-flicker1 5s steps(1) infinite 1s;
}

@media (prefers-reduced-motion: reduce) {
  .kf-09 * {
    animation: none!important;
  }
}
```
