---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-path-drawing-animation/"
title: "CSS Path Drawing Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "SVG stroke-drawing animations: signature handwriting, success checkmark, map route, logo outline, circuit trace and infinite symbol — stroke-dashoffset…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Path Drawing Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-path-drawing-animation/

SVG stroke-drawing animations: signature handwriting, success checkmark, map route, logo outline, circuit trace and infinite symbol — stroke-dashoffset keyframes only.
## HTML
```html
<div class="kf-20">
  <h2>CSS Path Drawing Animations</h2>
  <div class="grid">

    <!-- Signature -->
    <div class="card">
      <svg class="sig-svg" width="200" height="100" viewBox="0 0 200 100">
        <path d="M20,70 C30,20 50,20 60,50 C70,80 80,80 90,50 C100,20 110,30 120,60 C130,80 140,70 160,40 C170,25 180,40 185,60"/>
      </svg>
      <label>Signature Draw</label>
    </div>

    <!-- Check mark -->
    <div class="card">
      <svg class="check-svg" width="100" height="100" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="40"/>
        <polyline points="28,52 42,66 72,36"/>
      </svg>
      <label>Success Check</label>
    </div>

    <!-- Map route -->
    <div class="card">
      <div class="route-wrap">
        <svg class="route-svg" width="200" height="130" viewBox="0 0 200 130">
          <polyline points="20,110 20,60 80,60 80,30 160,30 160,80 140,80"/>
          <circle class="dot-start" cx="20" cy="110" r="6" fill="#ff6b35"/>
          <circle class="dot-end" cx="140" cy="80" r="6" fill="#ff6b35"/>
        </svg>
      </div>
      <label>Map Route</label>
    </div>

    <!-- Logo outline -->
    <div class="card">
      <svg class="logo-svg" width="120" height="120" viewBox="0 0 120 120">
        <path d="M60,10 L110,95 L10,95 Z"/>
        <path d="M60,30 L90,80 L30,80 Z"/>
        <path d="M60,50 L75,75 L45,75 Z"/>
      </svg>
      <label>Logo Outline</label>
    </div>

    <!-- Circuit board -->
    <div class="card">
      <svg class="circuit-svg" width="200" height="120" viewBox="0 0 200 120">
        <line class="trace" x1="10" y1="60" x2="190" y2="60"/>
        <line class="trace" x1="60" y1="10" x2="60" y2="110"/>
        <line class="trace" x1="130" y1="10" x2="130" y2="110"/>
        <path class="trace" d="M60,60 Q95,20 130,60"/>
        <circle class="node" cx="60" cy="60" r="5"/>
        <circle class="node" cx="130" cy="60" r="5"/>
        <circle class="node" cx="10" cy="60" r="4"/>
        <circle class="node" cx="190" cy="60" r="4"/>
      </svg>
      <label>Circuit Trace</label>
    </div>

    <!-- Infinity -->
    <div class="card">
      <svg class="inf-svg" width="200" height="100" viewBox="0 0 200 100">
        <defs>
          <linearGradient id="kf20grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#7c6af7"/>
            <stop offset="50%" stop-color="#e91e8c"/>
            <stop offset="100%" stop-color="#00d4ff"/>
          </linearGradient>
        </defs>
        <path d="M50,50 C50,25 75,10 100,50 C125,90 150,75 150,50 C150,25 125,10 100,50 C75,90 50,75 50,50 Z"/>
      </svg>
      <label>Infinity Stroke</label>
    </div>

  </div>
</div>
```
## CSS
```css
.kf-20 *,
.kf-20 *::before,
.kf-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-20 {
  font-family: 'Segoe UI', sans-serif;
  background: #0d0d1a;
  color: #fff;
  padding: 40px 20px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}

.kf-20 h2 {
  font-size: 1.1rem;
  color: #888;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-align: center;
}

.kf-20 .grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 32px;
  width: 100%;
  max-width: 900px;
}

.kf-20 .card {
  background: #13132a;
  border: 1px solid #2a2a4a;
  border-radius: 16px;
  padding: 32px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.kf-20 .card label {
  font-size: 0.8rem;
  color: #666;
  letter-spacing: 1px;
  text-transform: uppercase;
}
/* 1: Signature handwriting */

.kf-20 .sig-svg path {
  fill: none;
  stroke: #7c6af7;
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 600;
  stroke-dashoffset: 600;
  animation: kf-20-draw 2.5s ease forwards infinite;
}

@keyframes kf-20-draw {
  0% {
    stroke-dashoffset: 600;
    opacity: 1;
  }

  70% {
    stroke-dashoffset: 0;
    opacity: 1;
  }

  85% {
    stroke-dashoffset: 0;
    opacity: 1;
  }

  100% {
    stroke-dashoffset: -600;
    opacity: 0;
  }
}
/* 2: Check mark */

.kf-20 .check-svg circle {
  fill: none;
  stroke: #00d46a;
  stroke-width: 4;
  stroke-dasharray: 251;
  stroke-dashoffset: 251;
  animation: kf-20-circle 0.6s ease forwards infinite;
  animation-delay: 0.2s;
  transform-origin: center;
  transform: rotate(-90deg);
}

.kf-20 .check-svg polyline {
  fill: none;
  stroke: #00d46a;
  stroke-width: 4;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 80;
  stroke-dashoffset: 80;
  animation: kf-20-check 0.4s ease forwards infinite;
  animation-delay: 0.8s;
}

@keyframes kf-20-circle {
  0% {
    stroke-dashoffset: 251;
  }

  70% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: 0;
  }
}

@keyframes kf-20-check {
  0% {
    stroke-dashoffset: 80;
  }

  100% {
    stroke-dashoffset: 0;
  }
}

.kf-20 .check-svg {
  animation: kf-20-checkloop 2.5s ease infinite;
}

@keyframes kf-20-checkloop {
  0%,
    30% {
    opacity: 0;
  }

  35%,
    80% {
    opacity: 1;
  }

  90%,
    100% {
    opacity: 0;
  }
}
/* 3: Map route */

.kf-20 .route-svg polyline {
  fill: none;
  stroke: #ff6b35;
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 400;
  stroke-dashoffset: 400;
  animation: kf-20-route 3s ease forwards infinite;
}

.kf-20 .route-svg .dot-start,
.kf-20 .route-svg .dot-end {
  animation: kf-20-dotpop 0.3s ease forwards;
  transform-origin: center;
}

.kf-20 .route-svg .dot-start {
  animation-delay: 0s;
}

.kf-20 .route-svg .dot-end {
  animation-delay: 2.8s;
}

@keyframes kf-20-route {
  0% {
    stroke-dashoffset: 400;
  }

  80% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: 0;
  }
}

@keyframes kf-20-dotpop {
  0% {
    r: 0;
  }

  70% {
    r: 8;
  }

  100% {
    r: 6;
  }
}

.kf-20 .route-wrap {
  animation: kf-20-routeloop 4s ease infinite;
}

@keyframes kf-20-routeloop {
  0% {
    opacity: 0;
  }

  5%,
    85% {
    opacity: 1;
  }

  95%,
    100% {
    opacity: 0;
  }
}
/* 4: Logo outline */

.kf-20 .logo-svg path {
  fill: none;
  stroke: #e91e8c;
  stroke-width: 2.5;
  stroke-linecap: round;
  stroke-dasharray: 800;
  stroke-dashoffset: 800;
  animation: kf-20-logo 3s ease forwards infinite;
}

.kf-20 .logo-svg path:nth-child(2) {
  animation-delay: 1s;
  stroke: #7c6af7;
}

.kf-20 .logo-svg path:nth-child(3) {
  animation-delay: 2s;
  stroke: #00d4ff;
}

@keyframes kf-20-logo {
  0% {
    stroke-dashoffset: 800;
  }

  60% {
    stroke-dashoffset: 0;
  }

  80% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: -800;
  }
}
/* 5: Circuit board */

.kf-20 .circuit-svg line,
.kf-20 .circuit-svg path {
  fill: none;
  stroke: #00d4ff;
  stroke-width: 2;
  stroke-linecap: square;
}

.kf-20 .circuit-svg .trace {
  stroke-dasharray: 300;
  stroke-dashoffset: 300;
  animation: kf-20-circuit 2s linear infinite;
}

.kf-20 .circuit-svg .trace:nth-child(2) {
  animation-delay: 0.3s;
  stroke: #7c6af7;
}

.kf-20 .circuit-svg .trace:nth-child(3) {
  animation-delay: 0.6s;
  stroke: #00d46a;
}

.kf-20 .circuit-svg .trace:nth-child(4) {
  animation-delay: 0.9s;
  stroke: #ff6b35;
}

@keyframes kf-20-circuit {
  0% {
    stroke-dashoffset: 300;
  }

  100% {
    stroke-dashoffset: -300;
  }
}

.kf-20 .circuit-svg .node {
  fill: #00d4ff;
  animation: kf-20-nodeflash 2s ease infinite;
}

@keyframes kf-20-nodeflash {
  0%,
    100% {
    opacity: 0.3;
  }

  50% {
    opacity: 1;
  }
}
/* 6: Infinity symbol */

.kf-20 .inf-svg path {
  fill: none;
  stroke: url(#kf20grad);
  stroke-width: 6;
  stroke-linecap: round;
  stroke-dasharray: 500;
  stroke-dashoffset: 0;
  animation: kf-20-inf 3s linear infinite;
}

@keyframes kf-20-inf {
  0% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: -500;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-20 .sig-svg path,
    .kf-20 .check-svg circle,
    .kf-20 .check-svg polyline,
    .kf-20 .check-svg,
    .kf-20 .route-svg polyline,
    .kf-20 .route-wrap,
    .kf-20 .logo-svg path,
    .kf-20 .circuit-svg .trace,
    .kf-20 .circuit-svg .node,
    .kf-20 .inf-svg path {
    animation: none;
    stroke-dashoffset: 0;
    opacity: 1;
  }
}
```
