---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-floating-elements-animation/"
title: "CSS Floating Elements Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Hero section with six floating stat cards and a floating icon grid using staggered translateY + rotate keyframe animations with unique durations per element."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Elements Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-floating-elements-animation/

Hero section with six floating stat cards and a floating icon grid using staggered translateY + rotate keyframe animations with unique durations per element.
## HTML
```html
<div class="kf-17">
  <div class="kf-17__hero">
    <!-- Floating cards -->
    <div class="kf-17__float kf-17__f1">
      <div class="kf-17__badge"><div class="kf-17__badge-dot" style="background:#34d399"></div><b style="color:#34d399">+24.6%</b> Growth</div>
    </div>
    <div class="kf-17__float kf-17__f2">
      <div class="kf-17__badge"><span>⚡</span><b>98ms</b> response</div>
    </div>
    <div class="kf-17__float kf-17__f3">
      <div class="kf-17__stat">2.4M</div>
      <div class="kf-17__stat-l">Active Users</div>
    </div>
    <div class="kf-17__float kf-17__f4">
      <div class="kf-17__badge"><div class="kf-17__badge-dot" style="background:#f472b6"></div>Live</div>
      <div class="kf-17__stat" style="font-size:1.2rem">Production</div>
    </div>
    <div class="kf-17__float kf-17__f5">
      <div class="kf-17__badge">🏆 <b>#1</b> Ranked</div>
    </div>
    <div class="kf-17__float kf-17__f6">
      <div class="kf-17__badge">🔒 <b>SSL</b> Secured</div>
    </div>

    <div class="kf-17__center">
      <h1>Build <span>Faster.</span><br>Ship Smarter.</h1>
      <p>CSS floating elements animation — pure keyframes.</p>
      <a href="#" class="kf-17__cta">Get Started →</a>
    </div>
  </div>

  <div class="kf-17__icons">
    <div class="kf-17__icon">🎨</div>
    <div class="kf-17__icon">⚡</div>
    <div class="kf-17__icon">🚀</div>
    <div class="kf-17__icon">🔐</div>
    <div class="kf-17__icon">📊</div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&display=swap');

.kf-17,
.kf-17 *,
.kf-17 *::before,
.kf-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-17 ::selection {
  background: #a855f7;
  color: #fff;
}

.kf-17 {
  --bg: #0c0118;
  --purple: #a855f7;
  --blue: #38bdf8;
  --pink: #f472b6;
  --green: #34d399;
  --gold: #fbbf24;
  --white: #f0f0ff;
  font-family: 'Manrope',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 40px;
  position: relative;
  overflow: hidden;
  color: var(--white);
}
/* BG glow */

.kf-17::before {
  content: '';
  position: absolute;
  top: 20%;
  left: 30%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle,rgba(168,85,247,.1),transparent 60%);
  pointer-events: none;
}
/* ——— Hero section with floating UI elements ——— */

.kf-17__hero {
  width: min(700px,100%);
  position: relative;
  min-height: 420px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kf-17__center {
  text-align: center;
  z-index: 5;
  position: relative;
}

.kf-17__center h1 {
  font-size: clamp(2rem,7vw,4rem);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1;
}

.kf-17__center h1 span {
  background: linear-gradient(135deg,var(--purple),var(--blue));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.kf-17__center p {
  font-size: .95rem;
  color: rgba(240,240,255,.6);
  margin-top: 12px;
}

.kf-17__cta {
  display: inline-block;
  margin-top: 20px;
  background: linear-gradient(135deg,var(--purple),var(--blue));
  color: #fff;
  border-radius: 8px;
  padding: 12px 28px;
  font-weight: 700;
  font-size: .9rem;
  text-decoration: none;
  box-shadow: 0 8px 24px rgba(168,85,247,.35);
}
/* Floating cards */

.kf-17__float {
  position: absolute;
  border-radius: 16px;
  background: rgba(255,255,255,.04);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.08);
  padding: 16px 20px;
  font-size: .82rem;
  white-space: nowrap;
  box-shadow: 0 8px 32px rgba(0,0,0,.3);
}

.kf-17__f1 {
  top: 5%;
  left: 2%;
  animation: kf-17-float1 6s ease-in-out infinite;
}

.kf-17__f2 {
  top: 8%;
  right: 2%;
  animation: kf-17-float2 7s ease-in-out infinite 0.5s;
}

.kf-17__f3 {
  top: 50%;
  left: 0%;
  transform: translateY(-50%);
  animation: kf-17-float1 8s ease-in-out infinite 1s;
}

.kf-17__f4 {
  top: 50%;
  right: 0%;
  transform: translateY(-50%);
  animation: kf-17-float2 6.5s ease-in-out infinite 1.5s;
}

.kf-17__f5 {
  bottom: 5%;
  left: 8%;
  animation: kf-17-float1 7.5s ease-in-out infinite 0.8s;
}

.kf-17__f6 {
  bottom: 5%;
  right: 8%;
  animation: kf-17-float2 6s ease-in-out infinite 0.3s;
}

@keyframes kf-17-float1 {
  0%,
    100% {
    transform: translateY(0) rotate(-1deg);
  }

  50% {
    transform: translateY(-16px) rotate(1deg);
  }
}

@keyframes kf-17-float2 {
  0%,
    100% {
    transform: translateY(0) rotate(1deg);
  }

  50% {
    transform: translateY(-12px) rotate(-1deg);
  }
}
/* Adjust for f3/f4 which have extra transform */

.kf-17__f3 {
  animation: kf-17-float-mid1 8s ease-in-out infinite 1s;
}

.kf-17__f4 {
  animation: kf-17-float-mid2 6.5s ease-in-out infinite 1.5s;
}

@keyframes kf-17-float-mid1 {
  0%,
    100% {
    transform: translateY(calc(-50% + 0px));
  }

  50% {
    transform: translateY(calc(-50% - 14px));
  }
}

@keyframes kf-17-float-mid2 {
  0%,
    100% {
    transform: translateY(calc(-50% + 0px));
  }

  50% {
    transform: translateY(calc(-50% - 10px));
  }
}

.kf-17__badge {
  display: flex;
  align-items: center;
  gap: 8px;
}

.kf-17__badge-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.kf-17__badge b {
  font-weight: 700;
  font-size: .9rem;
}

.kf-17__stat {
  font-weight: 800;
  font-size: 1.6rem;
  color: var(--white);
}

.kf-17__stat-l {
  font-size: .7rem;
  color: rgba(240,240,255,.5);
  letter-spacing: .1em;
  text-transform: uppercase;
  margin-top: 2px;
}
/* ——— Floating icon grid ——— */

.kf-17__icons {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  justify-content: center;
}

.kf-17__icon {
  width: 72px;
  height: 72px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  font-size: 1.8rem;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 8px 24px rgba(0,0,0,.2);
}

.kf-17__icon:nth-child(1) {
  animation: kf-17-float1 5s ease-in-out infinite 0s;
  background: rgba(168,85,247,.1);
  border-color: rgba(168,85,247,.2);
}

.kf-17__icon:nth-child(2) {
  animation: kf-17-float2 6s ease-in-out infinite 0.4s;
  background: rgba(56,189,248,.1);
  border-color: rgba(56,189,248,.2);
}

.kf-17__icon:nth-child(3) {
  animation: kf-17-float1 7s ease-in-out infinite 0.8s;
  background: rgba(244,114,182,.1);
  border-color: rgba(244,114,182,.2);
}

.kf-17__icon:nth-child(4) {
  animation: kf-17-float2 5.5s ease-in-out infinite 1.2s;
  background: rgba(52,211,153,.1);
  border-color: rgba(52,211,153,.2);
}

.kf-17__icon:nth-child(5) {
  animation: kf-17-float1 6.5s ease-in-out infinite 0.6s;
  background: rgba(251,191,36,.1);
  border-color: rgba(251,191,36,.2);
}

@media (max-width: 640px) {
  .kf-17__f3,
    .kf-17__f4 {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-17 * {
    animation: none!important;
  }
}
```
