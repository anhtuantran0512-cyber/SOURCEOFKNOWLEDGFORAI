---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-morphing-blob-animation/"
title: "CSS Morphing Blob Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Six organic morphing blob animations — duo-colour, gradient shift, blend cluster, breathing ring and labelled blob — using staggered border-radius keyframes."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Morphing Blob Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-morphing-blob-animation/

Six organic morphing blob animations — duo-colour, gradient shift, blend cluster, breathing ring and labelled blob — using staggered border-radius keyframes.
## HTML
```html
<div class="kf-05">
  <div class="kf-05__row">
    <div class="kf-05__cell">
      <div class="kf-05__blob--1"></div>
      <span class="kf-05__label">Classic Blob</span>
    </div>
    <div class="kf-05__cell">
      <div class="kf-05__blob--2"></div>
      <span class="kf-05__label">Duo-Color</span>
    </div>
    <div class="kf-05__cell">
      <div class="kf-05__blob--3"></div>
      <span class="kf-05__label">Gradient Shift</span>
    </div>
  </div>
  <div class="kf-05__row">
    <div class="kf-05__cell">
      <div class="kf-05__cluster"><div class="kf-05__cluster-b"></div><div class="kf-05__cluster-b"></div><div class="kf-05__cluster-b"></div></div>
      <span class="kf-05__label">Blend Cluster</span>
    </div>
    <div class="kf-05__cell">
      <div class="kf-05__blob--5"></div>
      <span class="kf-05__label">Breathing Ring</span>
    </div>
    <div class="kf-05__cell">
      <div class="kf-05__blob--6">FLUID<br>DESIGN</div>
      <span class="kf-05__label">Label Blob</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&display=swap');

.kf-05,
.kf-05 *,
.kf-05 *::before,
.kf-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-05 ::selection {
  background: #ff6bd6;
  color: #fff;
}

.kf-05 {
  --bg: #fff8f5;
  --coral: #ff6b6b;
  --teal: #06d6a0;
  --indigo: #3d5af1;
  --pink: #ff6bd6;
  --yellow: #ffe45e;
  --dark: #1a1a2e;
  font-family: 'Syne',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 64px;
  overflow: hidden;
  position: relative;
}
/* Soft BG blobs */

.kf-05::before {
  content: '';
  position: absolute;
  top: -10%;
  right: -5%;
  width: 500px;
  height: 500px;
  border-radius: 63% 37% 54% 46%/55% 48% 52% 45%;
  background: rgba(255,107,214,.08);
  animation: kf-05-bg 12s ease-in-out infinite;
  z-index: 0;
}

.kf-05::after {
  content: '';
  position: absolute;
  bottom: -10%;
  left: -5%;
  width: 400px;
  height: 400px;
  border-radius: 42% 58% 37% 63%/55% 38% 62% 45%;
  background: rgba(6,214,160,.07);
  animation: kf-05-bg 10s ease-in-out infinite reverse;
  z-index: 0;
}

@keyframes kf-05-bg {
  0%,
    100% {
    border-radius: 63% 37% 54% 46%/55% 48% 52% 45%;
  }

  50% {
    border-radius: 37% 63% 46% 54%/45% 55% 48% 52%;
    transform: scale(1.08);
  }
}

.kf-05__row {
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
  justify-content: center;
  position: relative;
  z-index: 1;
}

.kf-05__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.kf-05__label {
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #aaa;
}
/* 1 — Classic blob */

.kf-05__blob--1 {
  width: 140px;
  height: 140px;
  background: linear-gradient(135deg,var(--coral),var(--pink));
  animation: kf-05-blob1 6s ease-in-out infinite;
}

@keyframes kf-05-blob1 {
  0%,
    100% {
    border-radius: 63% 37% 54% 46%/55% 48% 52% 45%;
  }

  25% {
    border-radius: 40% 60% 35% 65%/60% 30% 70% 40%;
  }

  50% {
    border-radius: 55% 45% 65% 35%/35% 65% 45% 55%;
  }

  75% {
    border-radius: 30% 70% 50% 50%/40% 60% 70% 30%;
  }
}
/* 2 — Duo-color blob */

.kf-05__blob--2 {
  width: 140px;
  height: 140px;
  position: relative;
  animation: kf-05-blob2 7s ease-in-out infinite;
}

.kf-05__blob--2::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,var(--indigo),var(--teal));
  animation: kf-05-blob1 7s ease-in-out infinite;
  border-radius: 63% 37% 54% 46%/55% 48% 52% 45%;
}

.kf-05__blob--2::after {
  content: '';
  position: absolute;
  inset: 20px;
  background: rgba(255,248,245,.6);
  animation: kf-05-blob1 5s ease-in-out infinite reverse;
  border-radius: 50%;
}
/* 3 — Gradient shift blob */

.kf-05__blob--3 {
  width: 140px;
  height: 140px;
  animation: kf-05-blob3 8s ease-in-out infinite;
  background: linear-gradient(0deg,var(--yellow),var(--coral));
  background-size: 100% 200%;
}

@keyframes kf-05-blob3 {
  0%,
    100% {
    border-radius: 60% 40% 55% 45%/50% 55% 45% 50%;
    background-position: 0% 0%;
  }

  33% {
    border-radius: 40% 60% 30% 70%/60% 40% 60% 40%;
    background-position: 0% 50%;
  }

  66% {
    border-radius: 55% 45% 68% 32%/38% 68% 32% 62%;
    background-position: 0% 100%;
  }
}
/* 4 — Multi-blob cluster */

.kf-05__cluster {
  width: 180px;
  height: 180px;
  position: relative;
}

.kf-05__cluster-b {
  position: absolute;
  border-radius: 63% 37% 54% 46%/55% 48% 52% 45%;
  mix-blend-mode: multiply;
}

.kf-05__cluster-b:nth-child(1) {
  width: 100px;
  height: 100px;
  background: rgba(255,107,107,.7);
  top: 0;
  left: 0;
  animation: kf-05-blob1 5s ease-in-out infinite;
}

.kf-05__cluster-b:nth-child(2) {
  width: 100px;
  height: 100px;
  background: rgba(61,90,241,.7);
  top: 30px;
  left: 50px;
  animation: kf-05-blob1 6s ease-in-out infinite .5s;
}

.kf-05__cluster-b:nth-child(3) {
  width: 100px;
  height: 100px;
  background: rgba(255,228,94,.7);
  top: 60px;
  left: 20px;
  animation: kf-05-blob1 7s ease-in-out infinite 1s;
}
/* 5 — Breathing ring blob */

.kf-05__blob--5 {
  width: 140px;
  height: 140px;
  border: 12px solid var(--pink);
  background: transparent;
  animation: kf-05-blob1 6s ease-in-out infinite 0.5s,kf-05-ring 3s ease-in-out infinite;
}

@keyframes kf-05-ring {
  0%,
    100% {
    border-width: 12px;
    box-shadow: 0 0 0 0 rgba(255,107,214,.3);
  }

  50% {
    border-width: 4px;
    box-shadow: 0 0 0 20px rgba(255,107,214,0);
  }
}
/* 6 — Text inside blob */

.kf-05__blob--6 {
  width: 160px;
  height: 160px;
  background: linear-gradient(135deg,var(--indigo),#7c3aed);
  display: grid;
  place-items: center;
  color: #fff;
  font-weight: 800;
  font-size: 1.2rem;
  text-align: center;
  line-height: 1.2;
  animation: kf-05-blob1 7s ease-in-out infinite;
  box-shadow: 0 20px 60px rgba(61,90,241,.35);
}

@media (max-width: 600px) {
  .kf-05__row {
    gap: 24px;
  }

  .kf-05__blob--1,
    .kf-05__blob--2,
    .kf-05__blob--3,
    .kf-05__blob--5,
    .kf-05__blob--6 {
    width: 110px;
    height: 110px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-05 * {
    animation: none!important;
    border-radius: 50%!important;
  }
}
```
