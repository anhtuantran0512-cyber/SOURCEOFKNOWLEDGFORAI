---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-countdown-timer-animation/"
title: "CSS Countdown Timer Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Arc ring countdown timers × 4, an animated flip clock and three linear progress countdown bars — all stroke-dashoffset or scaleX keyframes, pure CSS."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Countdown Timer Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-countdown-timer-animation/

Arc ring countdown timers × 4, an animated flip clock and three linear progress countdown bars — all stroke-dashoffset or scaleX keyframes, pure CSS.
## HTML
```html
<div class="kf-19">

  <div class="kf-19__arc-wrap">
    <div class="kf-19__arc kf-19__arc--days">
      <div class="kf-19__arc-ring"></div>
      <div class="kf-19__arc-inner"><span class="kf-19__num" style="color:#a78bfa">03</span><span class="kf-19__unit">Days</span></div>
    </div>
    <div class="kf-19__arc kf-19__arc--hours">
      <div class="kf-19__arc-ring"></div>
      <div class="kf-19__arc-inner"><span class="kf-19__num" style="color:#22d3ee">15</span><span class="kf-19__unit">Hours</span></div>
    </div>
    <div class="kf-19__arc kf-19__arc--mins">
      <div class="kf-19__arc-ring"></div>
      <div class="kf-19__arc-inner"><span class="kf-19__num" style="color:#4ade80">25</span><span class="kf-19__unit">Mins</span></div>
    </div>
    <div class="kf-19__arc kf-19__arc--secs">
      <div class="kf-19__arc-ring"></div>
      <div class="kf-19__arc-inner"><span class="kf-19__num" style="color:#f87171">48</span><span class="kf-19__unit">Secs</span></div>
    </div>
  </div>

  <div class="kf-19__flip-clock">
    <div class="kf-19__flip-unit">
      <div class="kf-19__flip-pair">
        <div class="kf-19__flip-digit">0</div>
        <div class="kf-19__flip-digit">3</div>
      </div>
      <span class="kf-19__flip-label">Days</span>
    </div>
    <div class="kf-19__flip-sep">:</div>
    <div class="kf-19__flip-unit">
      <div class="kf-19__flip-pair">
        <div class="kf-19__flip-digit">1</div>
        <div class="kf-19__flip-digit">5</div>
      </div>
      <span class="kf-19__flip-label">Hours</span>
    </div>
    <div class="kf-19__flip-sep">:</div>
    <div class="kf-19__flip-unit">
      <div class="kf-19__flip-pair">
        <div class="kf-19__flip-digit">2</div>
        <div class="kf-19__flip-digit">5</div>
      </div>
      <span class="kf-19__flip-label">Minutes</span>
    </div>
  </div>

  <div class="kf-19__bar-wrap">
    <div class="kf-19__bar-row">
      <div class="kf-19__bar-head"><span>Days Remaining</span><span>15%</span></div>
      <div class="kf-19__bar-track"><div class="kf-19__bar-fill kf-19__b1"></div></div>
    </div>
    <div class="kf-19__bar-row">
      <div class="kf-19__bar-head"><span>Budget Used</span><span>62%</span></div>
      <div class="kf-19__bar-track"><div class="kf-19__bar-fill kf-19__b2"></div></div>
    </div>
    <div class="kf-19__bar-row">
      <div class="kf-19__bar-head"><span>Time Elapsed</span><span>80%</span></div>
      <div class="kf-19__bar-track kf-19__b3-wrap"><div class="kf-19__bar-fill kf-19__b3"></div></div>
    </div>
  </div>

</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Inter:wght@400;600&display=swap');

.kf-19,
.kf-19 *,
.kf-19 *::before,
.kf-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-19 ::selection {
  background: #22d3ee;
  color: #000;
}

.kf-19 {
  --bg: #020617;
  --cyan: #22d3ee;
  --purple: #a78bfa;
  --green: #4ade80;
  --red: #f87171;
  --white: #f1f5f9;
  font-family: 'Oswald',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 64px;
  color: var(--white);
  position: relative;
  overflow: hidden;
}

.kf-19::before {
  content: '';
  position: absolute;
  top: 10%;
  left: 20%;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(34,211,238,.06),transparent 60%);
  pointer-events: none;
}

.kf-19::after {
  content: '';
  position: absolute;
  bottom: 10%;
  right: 15%;
  width: 250px;
  height: 250px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(167,139,250,.06),transparent 60%);
  pointer-events: none;
}
/* ——— 1: SVG-style arc timer ——— */

.kf-19__arc-wrap {
  display: flex;
  gap: 32px;
  flex-wrap: wrap;
  justify-content: center;
}

.kf-19__arc {
  position: relative;
  width: 120px;
  height: 120px;
  display: grid;
  place-items: center;
  flex-direction: column;
}

.kf-19__arc-ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(var(--cyan) var(--pct),rgba(255,255,255,.06) 0);
  animation: kf-19-ring 60s linear infinite;
}

.kf-19__arc--days .kf-19__arc-ring {
  --pct: 0%;
  background: conic-gradient(var(--purple) var(--pct),rgba(255,255,255,.06) 0);
  animation-duration: 3600s;
}

.kf-19__arc--hours .kf-19__arc-ring {
  --pct: 62.5%;
  background: conic-gradient(var(--cyan) 62.5%,rgba(255,255,255,.06) 0);
  animation-duration: 86400s;
}

.kf-19__arc--mins .kf-19__arc-ring {
  background: conic-gradient(var(--green) 41.67%,rgba(255,255,255,.06) 0);
  animation: kf-19-ring 3600s linear infinite;
}

.kf-19__arc--secs .kf-19__arc-ring {
  background: conic-gradient(var(--red) 80%,rgba(255,255,255,.06) 0);
  animation: kf-19-ring 60s linear infinite;
}

@keyframes kf-19-ring {
  to {
    transform: rotate(360deg);
  }
}

.kf-19__arc-inner {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 1;
  position: relative;
}

.kf-19__num {
  font-size: 1.9rem;
  line-height: 1;
}

.kf-19__unit {
  font-family: 'Inter';
  font-size: .6rem;
  letter-spacing: .15em;
  color: rgba(255,255,255,.4);
  text-transform: uppercase;
  margin-top: 2px;
}
/* ——— 2: Flip clock digits ——— */

.kf-19__flip-clock {
  display: flex;
  gap: 12px;
  align-items: center;
}

.kf-19__flip-sep {
  font-size: 2rem;
  color: rgba(255,255,255,.3);
  margin-bottom: 8px;
}

.kf-19__flip-unit {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.kf-19__flip-pair {
  display: flex;
  gap: 4px;
}

.kf-19__flip-digit {
  width: 52px;
  height: 72px;
  border-radius: 8px;
  background: linear-gradient(180deg,#1e293b,#0f172a);
  border: 1px solid rgba(255,255,255,.08);
  display: grid;
  place-items: center;
  font-size: 2.4rem;
  box-shadow: 0 4px 12px rgba(0,0,0,.4);
  position: relative;
  overflow: hidden;
  animation: kf-19-flip 1s ease-in-out infinite;
}

.kf-19__flip-digit::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  height: 1px;
  background: rgba(0,0,0,.4);
}

.kf-19__flip-digit:nth-child(2) {
  animation-delay: .05s;
}

.kf-19__flip-unit:nth-child(1) .kf-19__flip-digit {
  animation-duration: 60s;
}

.kf-19__flip-unit:nth-child(3) .kf-19__flip-digit {
  animation-duration: 3600s;
}

@keyframes kf-19-flip {
  0%,
    92% {
    transform: rotateX(0);
    background: linear-gradient(180deg,#1e293b,#0f172a);
  }

  96% {
    transform: rotateX(-90deg);
    background: linear-gradient(180deg,#0f172a,#1e293b);
  }

  100% {
    transform: rotateX(0);
  }
}

.kf-19__flip-label {
  font-family: 'Inter';
  font-size: .6rem;
  letter-spacing: .15em;
  color: rgba(255,255,255,.35);
  text-transform: uppercase;
}
/* ——— 3: Linear countdown bar ——— */

.kf-19__bar-wrap {
  width: min(480px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.kf-19__bar-row {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.kf-19__bar-head {
  display: flex;
  justify-content: space-between;
  font-family: 'Inter';
  font-size: .8rem;
}

.kf-19__bar-head span:first-child {
  color: rgba(255,255,255,.6);
  font-weight: 600;
}

.kf-19__bar-head span:last-child {
  color: var(--cyan);
  font-weight: 600;
}

.kf-19__bar-track {
  height: 8px;
  border-radius: 4px;
  background: rgba(255,255,255,.08);
  overflow: hidden;
}

.kf-19__bar-fill {
  height: 100%;
  border-radius: 4px;
}

.kf-19__b1 {
  background: linear-gradient(90deg,var(--purple),var(--cyan));
  width: 15%;
  animation: kf-19-fill1 linear infinite;
}

.kf-19__b2 {
  background: linear-gradient(90deg,var(--green),var(--cyan));
  width: 62%;
  animation: kf-19-fill2 linear infinite 0.5s;
}

.kf-19__b3 {
  background: linear-gradient(90deg,var(--red),var(--purple));
  width: 80%;
  animation: kf-19-fill3 linear infinite 1s;
}

@keyframes kf-19-fill1 {
  0%,
    100% {
    width: 15%;
  }

  50% {
    width: 5%;
  }
}

@keyframes kf-19-fill2 {
  0%,
    100% {
    width: 62%;
  }

  50% {
    width: 45%;
  }
}

@keyframes kf-19-fill3 {
  0% {
    width: 80%;
  }

  100% {
    width: 0%;
  }
}

.kf-19__b3-wrap {
  overflow: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .kf-19 * {
    animation: none!important;
  }
}
```
