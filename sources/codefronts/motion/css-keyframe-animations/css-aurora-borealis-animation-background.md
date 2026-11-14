---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-aurora-borealis-animation-background/"
title: "CSS Aurora Borealis Animation Background"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Animated northern-lights sky with skewed gradient curtain bands, tree silhouette and four colour-variant cards — green, purple/pink, blue-teal and…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aurora Borealis Animation Background
Source: https://codefronts.com/motion/css-keyframe-animations/css-aurora-borealis-animation-background/

Animated northern-lights sky with skewed gradient curtain bands, tree silhouette and four colour-variant cards — green, purple/pink, blue-teal and multicolour aurora.
## HTML
```html
<div class="kf-26">
  <h2>CSS Aurora Borealis Animations</h2>

  <div class="sky">
    <div class="aurora">
      <div class="aurora-band a1"></div>
      <div class="aurora-band a2"></div>
      <div class="aurora-band a3"></div>
      <div class="aurora-band a4"></div>
    </div>
    <div class="trees"></div>
    <div class="sky-caption">
      <h3>Aurora</h3>
      <p>Northern Lights</p>
    </div>
  </div>

  <div class="variants">
    <div class="variant-card var-a">
      <div class="mini-aurora"></div>
      <span>Green Aurora</span>
    </div>
    <div class="variant-card var-b">
      <div class="mini-aurora"></div>
      <span>Purple & Pink</span>
    </div>
    <div class="variant-card var-c">
      <div class="mini-aurora"></div>
      <span>Blue Teal</span>
    </div>
    <div class="variant-card var-d">
      <div class="mini-aurora"></div>
      <span>Multicolor</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;700&display=swap');

.kf-26 *,
.kf-26 *::before,
.kf-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-26 {
  font-family: 'Inter', sans-serif;
  background: #010308;
  color: #fff;
  padding: 48px 24px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
}

.kf-26 h2 {
  font-size: 1rem;
  color: #334;
  letter-spacing: 3px;
  text-transform: uppercase;
  font-weight: 300;
}
/* ── Scene 1: Full aurora sky ── */

.kf-26 .sky {
  position: relative;
  width: 100%;
  max-width: 960px;
  height: 340px;
  background: linear-gradient(180deg, #010308 0%, #020812 60%, #04101e 100%);
  border-radius: 20px;
  overflow: hidden;
}
/* Stars */

.kf-26 .sky::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(1px 1px at 10% 15%, rgba(255,255,255,0.8) 0%, transparent 100%), radial-gradient(1px 1px at 30% 8%, rgba(255,255,255,0.6) 0%, transparent 100%), radial-gradient(1px 1px at 55% 20%, rgba(255,255,255,0.9) 0%, transparent 100%), radial-gradient(1px 1px at 75% 6%, rgba(255,255,255,0.7) 0%, transparent 100%), radial-gradient(1px 1px at 90% 18%, rgba(255,255,255,0.5) 0%, transparent 100%), radial-gradient(1px 1px at 20% 30%, rgba(255,255,255,0.4) 0%, transparent 100%), radial-gradient(1px 1px at 65% 12%, rgba(255,255,255,0.8) 0%, transparent 100%), radial-gradient(1px 1px at 45% 5%,  rgba(255,255,255,0.6) 0%, transparent 100%), radial-gradient(1px 1px at 82% 28%, rgba(255,255,255,0.7) 0%, transparent 100%), radial-gradient(1px 1px at 5% 22%,  rgba(255,255,255,0.5) 0%, transparent 100%);
  animation: kf-26-twinkle 4s ease-in-out infinite;
}

@keyframes kf-26-twinkle {
  0%,
    100% {
    opacity: 0.6;
  }

  50% {
    opacity: 1;
  }
}
/* Ground silhouette */

.kf-26 .sky::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: linear-gradient(180deg, transparent 0%, #010205 100%);
}
/* Aurora curtains */

.kf-26 .aurora {
  position: absolute;
  bottom: 40px;
  width: 100%;
  height: 220px;
  filter: blur(18px);
  mix-blend-mode: screen;
}

.kf-26 .aurora-band {
  position: absolute;
  bottom: 0;
  height: 100%;
  border-radius: 50%;
  transform-origin: bottom center;
}

.kf-26 .a1 {
  width: 60%;
  left: -5%;
  background: linear-gradient(0deg,
      transparent 0%,
      rgba(0,220,120,0.15) 20%,
      rgba(0,255,160,0.4) 45%,
      rgba(0,230,130,0.2) 65%,
      transparent 100%
    );
  animation: kf-26-aurora1 8s ease-in-out infinite;
}

.kf-26 .a2 {
  width: 70%;
  left: 20%;
  background: linear-gradient(0deg,
      transparent 0%,
      rgba(100,0,220,0.1) 15%,
      rgba(140,80,255,0.35) 40%,
      rgba(180,100,255,0.2) 60%,
      transparent 100%
    );
  animation: kf-26-aurora2 10s ease-in-out infinite;
}

.kf-26 .a3 {
  width: 55%;
  right: -5%;
  background: linear-gradient(0deg,
      transparent 0%,
      rgba(0,180,220,0.1) 20%,
      rgba(0,220,255,0.3) 45%,
      rgba(50,200,240,0.15) 65%,
      transparent 100%
    );
  animation: kf-26-aurora3 7s ease-in-out infinite;
}

.kf-26 .a4 {
  width: 40%;
  left: 30%;
  background: linear-gradient(0deg,
      transparent 0%,
      rgba(0,240,180,0.05) 20%,
      rgba(100,255,200,0.25) 50%,
      transparent 100%
    );
  animation: kf-26-aurora4 12s ease-in-out infinite;
}

@keyframes kf-26-aurora1 {
  0% {
    transform: skewX(-5deg) scaleX(1) translateX(0);
    opacity: 0.8;
  }

  33% {
    transform: skewX(8deg) scaleX(1.1) translateX(3%);
    opacity: 1;
  }

  66% {
    transform: skewX(-3deg) scaleX(0.95) translateX(-2%);
    opacity: 0.9;
  }

  100% {
    transform: skewX(-5deg) scaleX(1) translateX(0);
    opacity: 0.8;
  }
}

@keyframes kf-26-aurora2 {
  0% {
    transform: skewX(3deg) scaleX(1) translateX(0);
    opacity: 0.7;
  }

  40% {
    transform: skewX(-10deg) scaleX(1.08) translateX(-4%);
    opacity: 0.9;
  }

  70% {
    transform: skewX(6deg) scaleX(0.92) translateX(3%);
    opacity: 0.8;
  }

  100% {
    transform: skewX(3deg) scaleX(1) translateX(0);
    opacity: 0.7;
  }
}

@keyframes kf-26-aurora3 {
  0% {
    transform: skewX(8deg) scaleX(1) translateX(0);
    opacity: 0.9;
  }

  45% {
    transform: skewX(-6deg) scaleX(1.12) translateX(-3%);
    opacity: 0.6;
  }

  75% {
    transform: skewX(4deg) scaleX(0.98) translateX(4%);
    opacity: 1;
  }

  100% {
    transform: skewX(8deg) scaleX(1) translateX(0);
    opacity: 0.9;
  }
}

@keyframes kf-26-aurora4 {
  0% {
    transform: scaleY(1) translateX(0);
    opacity: 0.6;
  }

  50% {
    transform: scaleY(1.3) translateX(-5%);
    opacity: 0.9;
  }

  100% {
    transform: scaleY(1) translateX(0);
    opacity: 0.6;
  }
}
/* Trees silhouette */

.kf-26 .trees {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: #010205;
  clip-path: polygon(
      0% 100%, 0% 80%, 3% 60%, 6% 80%, 9% 50%, 12% 70%, 15% 40%, 18% 65%,
      21% 45%, 24% 70%, 27% 35%, 30% 60%, 33% 50%, 36% 75%, 39% 45%, 42% 65%,
      45% 30%, 48% 55%, 51% 40%, 54% 60%, 57% 45%, 60% 70%, 63% 50%, 66% 75%,
      69% 40%, 72% 65%, 75% 35%, 78% 60%, 81% 50%, 84% 75%, 87% 45%, 90% 65%,
      93% 40%, 96% 60%, 100% 80%, 100% 100%
    );
}
/* Sky caption */

.kf-26 .sky-caption {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  z-index: 3;
}

.kf-26 .sky-caption h3 {
  font-size: 2rem;
  font-weight: 200;
  letter-spacing: 8px;
  color: rgba(200,240,220,0.85);
  text-shadow: 0 0 40px rgba(0,255,160,0.5);
  text-transform: uppercase;
}

.kf-26 .sky-caption p {
  font-size: 0.75rem;
  font-weight: 300;
  color: rgba(180,220,200,0.5);
  letter-spacing: 3px;
  margin-top: 4px;
}
/* ── Scene 2: Card variants ── */

.kf-26 .variants {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  width: 100%;
  max-width: 960px;
}

.kf-26 .variant-card {
  height: 160px;
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: flex-end;
  padding: 16px;
}
/* Variant A: Green only */

.kf-26 .var-a {
  background: #010308;
}

.kf-26 .var-a .mini-aurora {
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg,
      transparent 20%,
      rgba(0,255,140,0.15) 40%,
      rgba(0,220,100,0.35) 55%,
      rgba(0,180,80,0.1) 70%,
      transparent 85%
    );
  filter: blur(12px);
  animation: kf-26-varA 6s ease-in-out infinite;
}

@keyframes kf-26-varA {
  0%,
    100% {
    transform: translateX(-10%) skewY(-3deg);
    opacity: 0.7;
  }

  50% {
    transform: translateX(10%) skewY(3deg);
    opacity: 1;
  }
}
/* Variant B: Purple + pink */

.kf-26 .var-b {
  background: #060408;
}

.kf-26 .var-b .mini-aurora {
  position: absolute;
  inset: 0;
  background: linear-gradient(170deg,
      transparent 10%,
      rgba(200,0,255,0.1) 30%,
      rgba(255,50,150,0.3) 50%,
      rgba(180,0,220,0.15) 70%,
      transparent 90%
    );
  filter: blur(14px);
  animation: kf-26-varB 7s ease-in-out infinite;
}

@keyframes kf-26-varB {
  0%,
    100% {
    transform: rotate(-5deg) scale(1);
    opacity: 0.8;
  }

  50% {
    transform: rotate(5deg) scale(1.1);
    opacity: 1;
  }
}
/* Variant C: Blue teal */

.kf-26 .var-c {
  background: #010408;
}

.kf-26 .var-c .mini-aurora {
  position: absolute;
  inset: 0;
  background: linear-gradient(150deg,
      transparent 15%,
      rgba(0,150,255,0.1) 35%,
      rgba(0,220,255,0.35) 55%,
      rgba(0,180,220,0.1) 72%,
      transparent 88%
    );
  filter: blur(12px);
  animation: kf-26-varC 8s ease-in-out infinite;
}

@keyframes kf-26-varC {
  0%,
    100% {
    transform: skewX(5deg) translateY(-5%);
    opacity: 0.8;
  }

  50% {
    transform: skewX(-5deg) translateY(5%);
    opacity: 1;
  }
}
/* Variant D: Multi-color */

.kf-26 .var-d {
  background: #020308;
}

.kf-26 .var-d .mini-aurora {
  position: absolute;
  inset: 0;
  background: conic-gradient(from 200deg at 50% 80%,
      rgba(0,255,140,0.2) 0deg,
      rgba(100,80,255,0.2) 60deg,
      rgba(0,200,255,0.2) 120deg,
      rgba(0,255,140,0.05) 180deg,
      transparent 220deg
    );
  filter: blur(16px);
  animation: kf-26-varD 9s linear infinite;
}

@keyframes kf-26-varD {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.kf-26 .variant-card span {
  font-size: 0.72rem;
  color: rgba(255,255,255,0.4);
  letter-spacing: 2px;
  text-transform: uppercase;
  position: relative;
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {
  .kf-26 .sky::before,
    .kf-26 .a1,
    .kf-26 .a2,
    .kf-26 .a3,
    .kf-26 .a4,
    .kf-26 .var-a .mini-aurora,
    .kf-26 .var-b .mini-aurora,
    .kf-26 .var-c .mini-aurora,
    .kf-26 .var-d .mini-aurora {
    animation: none;
    opacity: 0.7;
  }
}
```
