---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-liquid-lava-lamp-blob-animation/"
title: "CSS Liquid Lava Lamp Blob Animation"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Three themed lava lamps — Ember (orange-pink), Aether (cyan-violet), and Growth (green-yellow) — each containing morphing radial-gradient blobs that…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Liquid Lava Lamp Blob Animation
Source: https://codefronts.com/motion/css-gradient-animation/css-liquid-lava-lamp-blob-animation/

Three themed lava lamps — Ember (orange-pink), Aether (cyan-violet), and Growth (green-yellow) — each containing morphing radial-gradient blobs that simultaneously change shape via border-radius keyframes and float vertically, simulating fluid droplets in a heated lamp.
## HTML
```html
<div class="ga-13">
  <div class="ga-13__lamp ga-13__lamp--a">
    <div class="ga-13__blob"></div>
    <div class="ga-13__blob"></div>
    <div class="ga-13__blob"></div>
    <span class="ga-13__lamp-label">Ember</span>
  </div>
  <div class="ga-13__lamp ga-13__lamp--b">
    <div class="ga-13__blob"></div>
    <div class="ga-13__blob"></div>
    <div class="ga-13__blob"></div>
    <span class="ga-13__lamp-label">Aether</span>
  </div>
  <div class="ga-13__lamp ga-13__lamp--c">
    <div class="ga-13__blob"></div>
    <div class="ga-13__blob"></div>
    <div class="ga-13__blob"></div>
    <span class="ga-13__lamp-label">Growth</span>
  </div>

  <div class="ga-13__ctrl">
    <button class="ga-13__ctrl-btn" data-dur="18s">Slow</button>
    <button class="ga-13__ctrl-btn active" data-dur="8s">Normal</button>
    <button class="ga-13__ctrl-btn" data-dur="3s">Fast</button>
  </div>
</div>
```
## CSS
```css
.ga-13,
.ga-13 *,
.ga-13 *::before,
.ga-13 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-13 ::selection {
  background: rgba(249,115,22,.4);
  color: #fff;
}

.ga-13 {
  --bg: #0a0510;
  --dur: 8s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 32px;
  flex-wrap: wrap;
  padding: 48px 24px;
  position: relative;
}
/* ── Single lava blob ── */

.ga-13__lamp {
  position: relative;
  width: 180px;
  height: 260px;
  border-radius: 16px;
  overflow: hidden;
  background: #100820;
  border: 1px solid rgba(255,255,255,.06);
  flex-shrink: 0;
}
/* Container label */

.ga-13__lamp-label {
  position: absolute;
  bottom: 14px;
  left: 0;
  right: 0;
  text-align: center;
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  z-index: 3;
}
/* Each blob is a div with morphing border-radius + position animation */

.ga-13__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(2px);
}
/* ── Lamp A: Orange-pink ── */

.ga-13__lamp--a {
  background: #0d060a;
}

.ga-13__lamp--a .ga-13__blob:nth-child(1) {
  width: 100px;
  height: 100px;
  background: radial-gradient(circle at 35% 40%, #ff6b2b, #ff2d7f);
  animation: ga-13-morph-a1 var(--dur) ease-in-out infinite, ga-13-float-a1 var(--dur) ease-in-out infinite;
  top: 60%;
  left: 40px;
}

.ga-13__lamp--a .ga-13__blob:nth-child(2) {
  width: 70px;
  height: 70px;
  background: radial-gradient(circle at 40% 35%, #ffab40, #ff5252);
  animation: ga-13-morph-a2 calc(var(--dur) * 1.3) ease-in-out infinite, ga-13-float-a2 calc(var(--dur) * 1.3) ease-in-out infinite;
  top: 20%;
  left: 55px;
  animation-delay: calc(var(--dur) * -.4);
}

.ga-13__lamp--a .ga-13__blob:nth-child(3) {
  width: 50px;
  height: 50px;
  background: radial-gradient(circle, #ff9d00, #ff3d00);
  animation: ga-13-morph-a2 calc(var(--dur) * .9) ease-in-out infinite, ga-13-float-a3 calc(var(--dur) * .9) ease-in-out infinite;
  top: 40%;
  left: 70px;
  animation-delay: calc(var(--dur) * -.65);
}

.ga-13__lamp--a .ga-13__lamp-label {
  color: #ff7b3a;
}
/* ── Lamp B: Cyan-violet ── */

.ga-13__lamp--b {
  background: #050a12;
}

.ga-13__lamp--b .ga-13__blob:nth-child(1) {
  width: 110px;
  height: 90px;
  background: radial-gradient(circle at 40% 45%, #00e5ff, #6c63ff);
  animation: ga-13-morph-b1 calc(var(--dur) * 1.1) ease-in-out infinite, ga-13-float-b1 calc(var(--dur) * 1.1) ease-in-out infinite;
  top: 55%;
  left: 35px;
}

.ga-13__lamp--b .ga-13__blob:nth-child(2) {
  width: 75px;
  height: 85px;
  background: radial-gradient(circle at 45% 35%, #18ffff, #7c4dff);
  animation: ga-13-morph-b2 calc(var(--dur) * .85) ease-in-out infinite, ga-13-float-b2 calc(var(--dur) * .85) ease-in-out infinite;
  top: 15%;
  left: 50px;
  animation-delay: calc(var(--dur) * -.3);
}

.ga-13__lamp--b .ga-13__blob:nth-child(3) {
  width: 45px;
  height: 55px;
  background: radial-gradient(circle, #64ffda, #536dfe);
  animation: ga-13-morph-b1 calc(var(--dur) * 1.4) ease-in-out infinite, ga-13-float-a3 calc(var(--dur) * 1.4) ease-in-out infinite;
  top: 35%;
  left: 60px;
  animation-delay: calc(var(--dur) * -.55);
}

.ga-13__lamp--b .ga-13__lamp-label {
  color: #00e5ff;
}
/* ── Lamp C: Green-yellow ── */

.ga-13__lamp--c {
  background: #030d07;
}

.ga-13__lamp--c .ga-13__blob:nth-child(1) {
  width: 95px;
  height: 105px;
  background: radial-gradient(circle at 38% 42%, #00e676, #ffea00);
  animation: ga-13-morph-c1 calc(var(--dur) * .95) ease-in-out infinite, ga-13-float-c1 calc(var(--dur) * .95) ease-in-out infinite;
  top: 58%;
  left: 42px;
}

.ga-13__lamp--c .ga-13__blob:nth-child(2) {
  width: 65px;
  height: 75px;
  background: radial-gradient(circle at 42% 38%, #b2ff59, #69f0ae);
  animation: ga-13-morph-c2 calc(var(--dur) * 1.2) ease-in-out infinite, ga-13-float-c2 calc(var(--dur) * 1.2) ease-in-out infinite;
  top: 18%;
  left: 58px;
  animation-delay: calc(var(--dur) * -.45);
}

.ga-13__lamp--c .ga-13__blob:nth-child(3) {
  width: 42px;
  height: 48px;
  background: radial-gradient(circle, #ccff90, #00c853);
  animation: ga-13-morph-c1 calc(var(--dur) * 1.5) ease-in-out infinite, ga-13-float-a1 calc(var(--dur) * 1.5) ease-in-out infinite;
  top: 38%;
  left: 68px;
  animation-delay: calc(var(--dur) * -.7);
}

.ga-13__lamp--c .ga-13__lamp-label {
  color: #69f0ae;
}
/* Morph keyframes (border-radius) */

@keyframes ga-13-morph-a1 {
  0% {
    border-radius: 60% 40% 70% 30% / 50% 60% 40% 50%;
  }

  25% {
    border-radius: 30% 70% 40% 60% / 60% 40% 70% 30%;
  }

  50% {
    border-radius: 50% 50% 30% 70% / 40% 60% 50% 60%;
  }

  75% {
    border-radius: 70% 30% 60% 40% / 30% 70% 40% 60%;
  }

  100% {
    border-radius: 60% 40% 70% 30% / 50% 60% 40% 50%;
  }
}

@keyframes ga-13-morph-a2 {
  0% {
    border-radius: 40% 60% 50% 50% / 60% 40% 60% 40%;
  }

  33% {
    border-radius: 60% 40% 70% 30% / 40% 60% 30% 70%;
  }

  66% {
    border-radius: 30% 70% 40% 60% / 70% 30% 60% 40%;
  }

  100% {
    border-radius: 40% 60% 50% 50% / 60% 40% 60% 40%;
  }
}

@keyframes ga-13-morph-b1 {
  0% {
    border-radius: 55% 45% 65% 35% / 45% 55% 45% 55%;
  }

  30% {
    border-radius: 35% 65% 45% 55% / 65% 35% 65% 35%;
  }

  60% {
    border-radius: 65% 35% 55% 45% / 35% 65% 35% 65%;
  }

  100% {
    border-radius: 55% 45% 65% 35% / 45% 55% 45% 55%;
  }
}

@keyframes ga-13-morph-b2 {
  0% {
    border-radius: 45% 55% 35% 65% / 55% 45% 65% 35%;
  }

  40% {
    border-radius: 65% 35% 55% 45% / 35% 65% 45% 55%;
  }

  80% {
    border-radius: 35% 65% 45% 55% / 65% 35% 55% 45%;
  }

  100% {
    border-radius: 45% 55% 35% 65% / 55% 45% 65% 35%;
  }
}

@keyframes ga-13-morph-c1 {
  0% {
    border-radius: 50% 50% 60% 40% / 40% 60% 50% 50%;
  }

  35% {
    border-radius: 70% 30% 40% 60% / 60% 40% 70% 30%;
  }

  70% {
    border-radius: 40% 60% 70% 30% / 30% 70% 40% 60%;
  }

  100% {
    border-radius: 50% 50% 60% 40% / 40% 60% 50% 50%;
  }
}

@keyframes ga-13-morph-c2 {
  0% {
    border-radius: 60% 40% 50% 50% / 50% 50% 40% 60%;
  }

  45% {
    border-radius: 40% 60% 60% 40% / 60% 40% 50% 50%;
  }

  90% {
    border-radius: 50% 50% 40% 60% / 40% 60% 60% 40%;
  }

  100% {
    border-radius: 60% 40% 50% 50% / 50% 50% 40% 60%;
  }
}
/* Float keyframes (position) */

@keyframes ga-13-float-a1 {
  0%,
    100% {
    top: 60%;
  }

  30% {
    top: 10%;
  }

  60% {
    top: 40%;
  }
}

@keyframes ga-13-float-a2 {
  0%,
    100% {
    top: 18%;
  }

  40% {
    top: 65%;
  }

  70% {
    top: 25%;
  }
}

@keyframes ga-13-float-a3 {
  0%,
    100% {
    top: 42%;
  }

  25% {
    top: 5%;
  }

  55% {
    top: 70%;
  }

  80% {
    top: 30%;
  }
}

@keyframes ga-13-float-b1 {
  0%,
    100% {
    top: 55%;
    left: 35px;
  }

  35% {
    top: 8%;
    left: 45px;
  }

  65% {
    top: 35%;
    left: 25px;
  }
}

@keyframes ga-13-float-b2 {
  0%,
    100% {
    top: 15%;
    left: 50px;
  }

  45% {
    top: 62%;
    left: 40px;
  }

  75% {
    top: 22%;
    left: 55px;
  }
}

@keyframes ga-13-float-c1 {
  0%,
    100% {
    top: 58%;
  }

  28% {
    top: 6%;
  }

  58% {
    top: 38%;
  }
}

@keyframes ga-13-float-c2 {
  0%,
    100% {
    top: 18%;
  }

  38% {
    top: 62%;
  }

  72% {
    top: 28%;
  }
}
/* Speed toggle */

.ga-13__ctrl {
  position: absolute;
  bottom: 14px;
  right: 14px;
  display: flex;
  gap: 5px;
}

.ga-13__ctrl-btn {
  padding: 4px 10px;
  font-size: .7rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.05);
  color: rgba(255,255,255,.35);
  cursor: pointer;
  transition: all .2s;
}

.ga-13__ctrl-btn.active,
.ga-13__ctrl-btn:hover {
  background: rgba(249,115,22,.15);
  border-color: rgba(249,115,22,.35);
  color: #fb923c;
}

@media (prefers-reduced-motion: reduce) {
  .ga-13__blob {
    animation: none !important;
    border-radius: 50%;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%);
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-13');
  w.querySelectorAll('.ga-13__ctrl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-13__ctrl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur', btn.dataset.dur);
    });
  });
})();
```
