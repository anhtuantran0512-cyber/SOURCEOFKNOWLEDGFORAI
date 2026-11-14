---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-pulse-glow-animation-button/"
title: "CSS Pulse Glow Animation Button"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Nine glowing button animation styles: ripple pulse, neon glow, heartbeat, shimmer sweep, border spin, breath expand, lightning flash, radar sweep and glow…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pulse Glow Animation Button
Source: https://codefronts.com/motion/css-keyframe-animations/css-pulse-glow-animation-button/

Nine glowing button animation styles: ripple pulse, neon glow, heartbeat, shimmer sweep, border spin, breath expand, lightning flash, radar sweep and glow bloom.
## HTML
```html
<div class="kf-04">
  <div class="kf-04__grid">
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--1">Launch</button>
      <span class="kf-04__sublabel">Ripple Pulse</span>
    </div>
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--2">Connect</button>
      <span class="kf-04__sublabel">Neon Glow</span>
    </div>
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--3">❤ Like</button>
      <span class="kf-04__sublabel">Heartbeat</span>
    </div>
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--4">Upgrade</button>
      <span class="kf-04__sublabel">Shimmer Sweep</span>
    </div>
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--5">Premium</button>
      <span class="kf-04__sublabel">Border Spin</span>
    </div>
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--6">Inhale</button>
      <span class="kf-04__sublabel">Breath Expand</span>
    </div>
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--7">Strike</button>
      <span class="kf-04__sublabel">Lightning Flash</span>
    </div>
    <div class="kf-04__cell">
      <div class="kf-04__radar"><div class="kf-04__radar-beam"></div><div class="kf-04__radar-dot"></div></div>
      <span class="kf-04__sublabel">Radar Sweep</span>
    </div>
    <div class="kf-04__cell">
      <button class="kf-04__btn kf-04__btn--9">Get Started</button>
      <span class="kf-04__sublabel">Glow Bloom</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700&display=swap');

.kf-04,
.kf-04 *,
.kf-04 *::before,
.kf-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-04 ::selection {
  background: #00ff88;
  color: #000;
}

.kf-04 {
  --bg: #06070a;
  --green: #00ff88;
  --blue: #00b4ff;
  --purple: #a855f7;
  --red: #ff3366;
  --gold: #ffbe0b;
  --white: #f8f9fa;
  font-family: 'Inter',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 40px;
}

.kf-04__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 32px;
  max-width: 820px;
  width: 100%;
}

.kf-04__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.kf-04__sublabel {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: #444;
}
/* Base button */

.kf-04__btn {
  position: relative;
  padding: 14px 32px;
  border: none;
  border-radius: 8px;
  font-family: 'Inter';
  font-weight: 700;
  font-size: .95rem;
  letter-spacing: .04em;
  cursor: pointer;
  overflow: visible;
  text-transform: uppercase;
}
/* 1 — Ripple pulse */

.kf-04__btn--1 {
  background: var(--green);
  color: #000;
}

.kf-04__btn--1::before,
.kf-04__btn--1::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 8px;
  background: var(--green);
  opacity: .5;
  animation: kf-04-ripple 2s ease-out infinite;
}

.kf-04__btn--1::after {
  animation-delay: .6s;
}

@keyframes kf-04-ripple {
  0% {
    transform: scale(1);
    opacity: .6;
  }

  100% {
    transform: scale(1.8);
    opacity: 0;
  }
}
/* 2 — Neon glow pulse */

.kf-04__btn--2 {
  background: transparent;
  color: var(--blue);
  border: 2px solid var(--blue);
  animation: kf-04-neon 2s ease-in-out infinite alternate;
}

@keyframes kf-04-neon {
  from {
    box-shadow: 0 0 8px var(--blue),0 0 20px var(--blue),inset 0 0 8px rgba(0,180,255,.1);
  }

  to {
    box-shadow: 0 0 20px var(--blue),0 0 50px var(--blue),0 0 80px rgba(0,180,255,.3),inset 0 0 20px rgba(0,180,255,.15);
  }
}
/* 3 — Heartbeat */

.kf-04__btn--3 {
  background: var(--red);
  color: #fff;
  animation: kf-04-heart 1.2s ease-in-out infinite;
}

@keyframes kf-04-heart {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 rgba(255,51,102,.4);
  }

  14% {
    transform: scale(1.1);
    box-shadow: 0 0 0 rgba(255,51,102,.2);
  }

  28% {
    transform: scale(1);
    box-shadow: 0 0 0 rgba(255,51,102,.4);
  }

  42% {
    transform: scale(1.06);
    box-shadow: 0 0 20px rgba(255,51,102,.5);
  }

  70% {
    transform: scale(1);
  }
}
/* 4 — Shimmer sweep */

.kf-04__btn--4 {
  background: linear-gradient(135deg,#1a1a2e,#16213e,#0f3460);
  color: var(--purple);
  border: 1px solid rgba(168,85,247,.3);
  overflow: hidden;
}

.kf-04__btn--4::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg,transparent,rgba(168,85,247,.4),transparent);
  animation: kf-04-shimmer 2.5s ease-in-out infinite;
}

@keyframes kf-04-shimmer {
  to {
    left: 160%;
  }
}
/* 5 — Border spin */

.kf-04__btn--5 {
  background: #0d0d0d;
  color: var(--gold);
  border: 2px solid transparent;
  background-clip: padding-box;
}

.kf-04__btn--5::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 10px;
  z-index: -1;
  background: conic-gradient(from 0deg,var(--gold),transparent,var(--gold));
  animation: kf-04-borderspin 2s linear infinite;
}

@keyframes kf-04-borderspin {
  to {
    transform: rotate(360deg);
  }
}
/* 6 — Breath expand */

.kf-04__btn--6 {
  background: var(--purple);
  color: #fff;
  animation: kf-04-breath 3s ease-in-out infinite;
}

@keyframes kf-04-breath {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(168,85,247,.4);
  }

  50% {
    transform: scale(1.05);
    box-shadow: 0 0 0 18px rgba(168,85,247,0);
  }
}
/* 7 — Lightning flash */

.kf-04__btn--7 {
  background: linear-gradient(135deg,#1a1a1a,#222);
  color: var(--gold);
  border: 1px solid #333;
}

.kf-04__btn--7::before {
  content: '⚡';
  position: absolute;
  left: -14px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 16px;
  animation: kf-04-lightning 2s steps(1) infinite;
}

.kf-04__btn--7::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 8px;
  background: var(--gold);
  opacity: 0;
  animation: kf-04-flash 2s steps(1) infinite;
}

@keyframes kf-04-lightning {
  0%,
    90%,
    100% {
    opacity: 0;
  }

  92% {
    opacity: 1;
  }

  94% {
    opacity: 0;
  }

  96% {
    opacity: 1;
  }
}

@keyframes kf-04-flash {
  0%,
    90%,
    100% {
    opacity: 0;
  }

  92% {
    opacity: .15;
  }

  94% {
    opacity: 0;
  }

  96% {
    opacity: .1;
  }
}
/* 8 — Radar sweep */

.kf-04__radar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  position: relative;
  border: 2px solid rgba(0,255,136,.3);
  background: radial-gradient(circle,rgba(0,255,136,.05),transparent);
}

.kf-04__radar::before,
.kf-04__radar::after {
  content: '';
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(0,255,136,.2);
}

.kf-04__radar::before {
  inset: 18px;
}

.kf-04__radar::after {
  inset: 36px;
}

.kf-04__radar-beam {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(from 0deg,rgba(0,255,136,.6) 0deg,rgba(0,255,136,.1) 40deg,transparent 40deg);
  animation: kf-04-borderspin 2s linear infinite;
}

.kf-04__radar-dot {
  position: absolute;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--green);
  top: 22%;
  left: 62%;
  box-shadow: 0 0 6px var(--green);
  animation: kf-04-blink 2s steps(1) infinite;
}

@keyframes kf-04-blink {
  0%,
    50% {
    opacity: 1;
  }

  51%,
    100% {
    opacity: 0;
  }
}
/* 9 — CTA with particles */

.kf-04__btn--9 {
  background: linear-gradient(135deg,var(--red),var(--purple));
  color: #fff;
  padding: 16px 40px;
  font-size: 1rem;
  border-radius: 50px;
}

.kf-04__btn--9::before {
  content: '';
  position: absolute;
  inset: -3px;
  border-radius: 52px;
  background: linear-gradient(135deg,var(--red),var(--purple));
  z-index: -1;
  filter: blur(10px);
  opacity: .6;
  animation: kf-04-glow 2s ease-in-out infinite alternate;
}

@keyframes kf-04-glow {
  to {
    filter: blur(18px);
    opacity: .9;
  }
}

@media (max-width: 640px) {
  .kf-04__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 400px) {
  .kf-04__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-04 * {
    animation: none!important;
  }
}
```
