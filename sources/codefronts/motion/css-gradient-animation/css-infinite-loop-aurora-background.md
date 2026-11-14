---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-infinite-loop-aurora-background/"
title: "CSS Infinite Loop Aurora Background"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A slow-moving, organic multi-color aurora mesh background built from blurred radial-gradient blobs that rotate and scale on infinite CSS keyframes — ideal…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Infinite Loop Aurora Background
Source: https://codefronts.com/motion/css-gradient-animation/css-infinite-loop-aurora-background/

A slow-moving, organic multi-color aurora mesh background built from blurred radial-gradient blobs that rotate and scale on infinite CSS keyframes — ideal for SaaS landing page heroes.
## HTML
```html
<div class="ga-01">
  <div class="ga-01__aurora">
    <div class="ga-01__blob"></div>
    <div class="ga-01__blob"></div>
    <div class="ga-01__blob"></div>
    <div class="ga-01__blob"></div>
  </div>
  <div class="ga-01__content">
    <div class="ga-01__badge">✦ New — Now in Beta</div>
    <h1 class="ga-01__title">The AI Platform<br><span>Built for Teams</span></h1>
    <p class="ga-01__sub">Ship faster with AI-powered workflows, real-time collaboration, and intelligent automation that adapts to how your team actually works.</p>
    <div class="ga-01__cta">
      <button class="ga-01__btn ga-01__btn--primary">Start for Free</button>
      <button class="ga-01__btn ga-01__btn--ghost">View Demo →</button>
    </div>
  </div>
  <div class="ga-01__speed">
    <button class="ga-01__speed-btn" data-speed="slow">Slow</button>
    <button class="ga-01__speed-btn active" data-speed="normal">Normal</button>
    <button class="ga-01__speed-btn" data-speed="fast">Fast</button>
  </div>
</div>
```
## CSS
```css
.ga-01,
.ga-01 *,
.ga-01 *::before,
.ga-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-01 ::selection {
  background: rgba(139,92,246,.45);
  color: #fff;
}

.ga-01 {
  --c1: #0d0d1a;
  --c2: #6d28d9;
  --c3: #0ea5e9;
  --c4: #10b981;
  --c5: #7c3aed;
  --dur: 12s;
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: var(--c1);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* Aurora mesh layers */

.ga-01__aurora {
  position: absolute;
  inset: 0;
  filter: blur(60px);
  opacity: .75;
}

.ga-01__blob {
  position: absolute;
  border-radius: 60% 40% 70% 30% / 50% 60% 40% 50%;
  animation: ga-01-drift linear infinite;
  mix-blend-mode: screen;
}

.ga-01__blob:nth-child(1) {
  width: 65%;
  height: 70%;
  top: -15%;
  left: -10%;
  background: radial-gradient(ellipse at center, var(--c2) 0%, transparent 65%);
  animation-duration: var(--dur);
  animation-delay: 0s;
}

.ga-01__blob:nth-child(2) {
  width: 55%;
  height: 60%;
  bottom: -20%;
  right: -10%;
  background: radial-gradient(ellipse at center, var(--c3) 0%, transparent 65%);
  animation-duration: calc(var(--dur) * 1.3);
  animation-delay: calc(var(--dur) * -.4);
  animation-direction: reverse;
}

.ga-01__blob:nth-child(3) {
  width: 50%;
  height: 55%;
  top: 20%;
  left: 30%;
  background: radial-gradient(ellipse at center, var(--c4) 0%, transparent 65%);
  animation-duration: calc(var(--dur) * 1.6);
  animation-delay: calc(var(--dur) * -.7);
}

.ga-01__blob:nth-child(4) {
  width: 45%;
  height: 50%;
  top: -10%;
  right: 10%;
  background: radial-gradient(ellipse at center, var(--c5) 0%, transparent 65%);
  animation-duration: calc(var(--dur) * 1.1);
  animation-delay: calc(var(--dur) * -.2);
  animation-direction: reverse;
}

@keyframes ga-01-drift {
  0% {
    transform: translate(0, 0) rotate(0deg) scale(1);
  }

  25% {
    transform: translate(8%, 12%) rotate(90deg) scale(1.08);
  }

  50% {
    transform: translate(-5%, 8%) rotate(180deg) scale(.95);
  }

  75% {
    transform: translate(10%, -6%) rotate(270deg) scale(1.05);
  }

  100% {
    transform: translate(0, 0) rotate(360deg) scale(1);
  }
}
/* Content */

.ga-01__content {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 48px 32px;
  max-width: 640px;
}

.ga-01__badge {
  display: inline-block;
  padding: 5px 14px;
  border-radius: 999px;
  background: rgba(139,92,246,.18);
  border: 1px solid rgba(139,92,246,.4);
  color: #a78bfa;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.ga-01__title {
  font-size: clamp(2rem, 5vw, 3.2rem);
  font-weight: 800;
  line-height: 1.12;
  color: #fff;
  margin-bottom: 16px;
  letter-spacing: -.02em;
}

.ga-01__title span {
  background: linear-gradient(135deg, #a78bfa 0%, #38bdf8 50%, #34d399 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.ga-01__sub {
  font-size: 1.05rem;
  color: rgba(255,255,255,.6);
  line-height: 1.65;
  margin-bottom: 32px;
}

.ga-01__cta {
  display: inline-flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}

.ga-01__btn {
  padding: 12px 28px;
  border-radius: 10px;
  font-size: .95rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: transform .2s, box-shadow .2s;
}

.ga-01__btn:hover {
  transform: translateY(-2px);
}

.ga-01__btn--primary {
  background: linear-gradient(135deg, #7c3aed, #0ea5e9);
  color: #fff;
  box-shadow: 0 4px 24px rgba(124,58,237,.4);
}

.ga-01__btn--primary:hover {
  box-shadow: 0 8px 32px rgba(124,58,237,.6);
}

.ga-01__btn--ghost {
  background: rgba(255,255,255,.08);
  color: #fff;
  border: 1px solid rgba(255,255,255,.15);
}

.ga-01__btn--ghost:hover {
  background: rgba(255,255,255,.13);
}
/* Speed toggle */

.ga-01__speed {
  position: absolute;
  bottom: 16px;
  right: 16px;
  z-index: 3;
  display: flex;
  gap: 6px;
}

.ga-01__speed-btn {
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.15);
  background: rgba(255,255,255,.06);
  color: rgba(255,255,255,.55);
  transition: all .2s;
}

.ga-01__speed-btn.active,
.ga-01__speed-btn:hover {
  background: rgba(139,92,246,.25);
  border-color: rgba(139,92,246,.5);
  color: #c4b5fd;
}

@media (prefers-reduced-motion: reduce) {
  .ga-01__blob {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const wrapper = document.querySelector('.ga-01');
  const btns = wrapper.querySelectorAll('.ga-01__speed-btn');
  const speeds = { slow: '22s', normal: '12s', fast: '5s' };
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      wrapper.style.setProperty('--dur', speeds[btn.dataset.speed]);
    });
  });
})();
```
