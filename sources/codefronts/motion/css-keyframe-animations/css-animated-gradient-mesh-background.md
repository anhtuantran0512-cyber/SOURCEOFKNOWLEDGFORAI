---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-animated-gradient-mesh-background/"
title: "CSS Animated Gradient Mesh Background"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Animated gradient mesh using floating radial-gradient orbs on a dark base: full hero scene, four colour-variant cards (purple, pink, green, gold) and a…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Gradient Mesh Background
Source: https://codefronts.com/motion/css-keyframe-animations/css-animated-gradient-mesh-background/

Animated gradient mesh using floating radial-gradient orbs on a dark base: full hero scene, four colour-variant cards (purple, pink, green, gold) and a rainbow gradient text strip.
## HTML
```html
<div class="kf-30">
  <h2>CSS Animated Gradient Mesh</h2>

  <!-- Hero -->
  <div class="hero-mesh">
    <div class="mesh-bg">
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>
      <div class="orb orb-3"></div>
      <div class="orb orb-4"></div>
    </div>
    <div class="hero-content">
      <h3>Gradient Mesh</h3>
      <p>pure CSS · no canvas · no SVG</p>
    </div>
  </div>

  <!-- Cards -->
  <div class="cards">
    <div class="mesh-card mc-a">
      <div class="card-bg"></div>
      <div class="card-orb"></div>
      <div class="card-orb"></div>
      <div class="card-label">Purple · Cyan</div>
      <div class="card-title">Analytics</div>
    </div>
    <div class="mesh-card mc-b">
      <div class="card-bg"></div>
      <div class="card-orb"></div>
      <div class="card-orb"></div>
      <div class="card-label">Pink · Orange</div>
      <div class="card-title">Creative</div>
    </div>
    <div class="mesh-card mc-c">
      <div class="card-bg"></div>
      <div class="card-orb"></div>
      <div class="card-orb"></div>
      <div class="card-label">Green · Teal</div>
      <div class="card-title">Growth</div>
    </div>
    <div class="mesh-card mc-d">
      <div class="card-bg"></div>
      <div class="card-orb"></div>
      <div class="card-orb"></div>
      <div class="card-label">Gold · Warm</div>
      <div class="card-title">Premium</div>
    </div>
  </div>

  <!-- Gradient text -->
  <div class="gradient-text-demo">
    <div class="grad-text">VIVID</div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;700;900&display=swap');

.kf-30 *,
.kf-30 *::before,
.kf-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-30 {
  font-family: 'Inter', sans-serif;
  background: #050508;
  color: #fff;
  padding: 48px 24px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
}

.kf-30 h2 {
  font-size: 1rem;
  color: #333;
  letter-spacing: 3px;
  text-transform: uppercase;
  font-weight: 300;
}
/* ── 1: Full hero gradient mesh ── */

.kf-30 .hero-mesh {
  width: 100%;
  max-width: 960px;
  min-height: 320px;
  border-radius: 24px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kf-30 .mesh-bg {
  position: absolute;
  inset: 0;
  background: #0a0a14;
}
/* Floating gradient orbs */

.kf-30 .orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  mix-blend-mode: screen;
}

.kf-30 .orb-1 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(124,106,247,0.5) 0%, transparent 70%);
  top: -100px;
  left: -80px;
  animation: kf-30-orb1 8s ease-in-out infinite;
}

.kf-30 .orb-2 {
  width: 350px;
  height: 350px;
  background: radial-gradient(circle, rgba(233,30,140,0.4) 0%, transparent 70%);
  bottom: -80px;
  right: -60px;
  animation: kf-30-orb2 10s ease-in-out infinite;
}

.kf-30 .orb-3 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(0,212,255,0.35) 0%, transparent 70%);
  top: 30%;
  left: 40%;
  transform: translate(-50%, -50%);
  animation: kf-30-orb3 7s ease-in-out infinite;
}

.kf-30 .orb-4 {
  width: 250px;
  height: 250px;
  background: radial-gradient(circle, rgba(0,212,106,0.3) 0%, transparent 70%);
  bottom: 10%;
  left: 20%;
  animation: kf-30-orb4 12s ease-in-out infinite;
}

@keyframes kf-30-orb1 {
  0%,
    100% {
    transform: translate(0, 0) scale(1);
  }

  33% {
    transform: translate(80px, 60px) scale(1.1);
  }

  66% {
    transform: translate(-40px, 80px) scale(0.9);
  }
}

@keyframes kf-30-orb2 {
  0%,
    100% {
    transform: translate(0, 0) scale(1);
  }

  40% {
    transform: translate(-100px, -60px) scale(1.15);
  }

  70% {
    transform: translate(50px, -40px) scale(0.85);
  }
}

@keyframes kf-30-orb3 {
  0%,
    100% {
    transform: translate(-50%, -50%) scale(1);
  }

  50% {
    transform: translate(-40%, -60%) scale(1.2);
  }
}

@keyframes kf-30-orb4 {
  0%,
    100% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(80px, -50px) scale(1.1);
  }
}

.kf-30 .hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
}

.kf-30 .hero-content h3 {
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 900;
  letter-spacing: 2px;
  background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.7) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.kf-30 .hero-content p {
  font-size: 1rem;
  color: rgba(255,255,255,0.45);
  margin-top: 8px;
  letter-spacing: 2px;
  font-weight: 300;
}
/* ── 2: Card variants ── */

.kf-30 .cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  width: 100%;
  max-width: 960px;
}

.kf-30 .mesh-card {
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  min-height: 200px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.kf-30 .mesh-card .card-bg {
  position: absolute;
  inset: 0;
}

.kf-30 .mesh-card .card-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(40px);
  mix-blend-mode: screen;
}
/* Card A: Purple + cyan */

.kf-30 .mc-a .card-bg {
  background: #080814;
}

.kf-30 .mc-a .card-orb:nth-child(2) {
  width: 200px;
  height: 200px;
  background: rgba(124,106,247,0.6);
  top: -60px;
  left: -60px;
  animation: kf-30-ca1 6s ease-in-out infinite;
}

.kf-30 .mc-a .card-orb:nth-child(3) {
  width: 150px;
  height: 150px;
  background: rgba(0,212,255,0.4);
  bottom: -40px;
  right: -40px;
  animation: kf-30-ca2 8s ease-in-out infinite;
}

@keyframes kf-30-ca1 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(40px,30px);
  }
}

@keyframes kf-30-ca2 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(-30px,-40px);
  }
}
/* Card B: Pink + orange */

.kf-30 .mc-b .card-bg {
  background: #0e0810;
}

.kf-30 .mc-b .card-orb:nth-child(2) {
  width: 180px;
  height: 180px;
  background: rgba(233,30,140,0.6);
  top: -50px;
  right: -50px;
  animation: kf-30-cb1 7s ease-in-out infinite;
}

.kf-30 .mc-b .card-orb:nth-child(3) {
  width: 140px;
  height: 140px;
  background: rgba(255,107,53,0.5);
  bottom: -30px;
  left: -30px;
  animation: kf-30-cb2 9s ease-in-out infinite;
}

@keyframes kf-30-cb1 {
  0%,
    100% {
    transform: translate(0,0) scale(1);
  }

  50% {
    transform: translate(-40px,30px) scale(1.1);
  }
}

@keyframes kf-30-cb2 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(40px,-30px);
  }
}
/* Card C: Green + teal */

.kf-30 .mc-c .card-bg {
  background: #050e0a;
}

.kf-30 .mc-c .card-orb:nth-child(2) {
  width: 200px;
  height: 200px;
  background: rgba(0,212,106,0.5);
  bottom: -60px;
  left: -40px;
  animation: kf-30-cc1 8s ease-in-out infinite;
}

.kf-30 .mc-c .card-orb:nth-child(3) {
  width: 160px;
  height: 160px;
  background: rgba(0,180,220,0.4);
  top: -40px;
  right: -40px;
  animation: kf-30-cc2 6s ease-in-out infinite;
}

@keyframes kf-30-cc1 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(50px,-40px);
  }
}

@keyframes kf-30-cc2 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(-40px,40px);
  }
}
/* Card D: Gold + warm */

.kf-30 .mc-d .card-bg {
  background: #0d0a05;
}

.kf-30 .mc-d .card-orb:nth-child(2) {
  width: 220px;
  height: 220px;
  background: rgba(247,201,72,0.5);
  top: -80px;
  right: -40px;
  animation: kf-30-cd1 9s ease-in-out infinite;
}

.kf-30 .mc-d .card-orb:nth-child(3) {
  width: 160px;
  height: 160px;
  background: rgba(255,140,60,0.4);
  bottom: -40px;
  left: -20px;
  animation: kf-30-cd2 7s ease-in-out infinite;
}

@keyframes kf-30-cd1 {
  0%,
    100% {
    transform: translate(0,0) scale(1);
  }

  50% {
    transform: translate(-40px,50px) scale(0.9);
  }
}

@keyframes kf-30-cd2 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(50px,-30px);
  }
}

.kf-30 .card-label {
  position: relative;
  z-index: 2;
  font-size: 0.72rem;
  color: rgba(255,255,255,0.4);
  letter-spacing: 2px;
  text-transform: uppercase;
}

.kf-30 .card-title {
  position: relative;
  z-index: 2;
  font-size: 1.2rem;
  font-weight: 700;
  color: rgba(255,255,255,0.85);
  margin-top: 4px;
}
/* ── 3: Gradient text animation ── */

.kf-30 .gradient-text-demo {
  text-align: center;
}

.kf-30 .grad-text {
  font-size: clamp(2rem, 8vw, 4rem);
  font-weight: 900;
  background: linear-gradient(90deg,
      #7c6af7, #e91e8c, #ff6b35, #f7c948, #00d46a, #00d4ff, #7c6af7
    );
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: kf-30-gradshift 4s linear infinite;
  letter-spacing: 4px;
}

@keyframes kf-30-gradshift {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-30 .orb,
    .kf-30 .card-orb,
    .kf-30 .grad-text {
    animation: none;
  }
}
```
