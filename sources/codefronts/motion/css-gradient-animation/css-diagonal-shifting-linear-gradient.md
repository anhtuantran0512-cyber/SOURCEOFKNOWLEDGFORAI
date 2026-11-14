---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-diagonal-shifting-linear-gradient/"
title: "CSS Diagonal Shifting Linear Gradient"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A continuously sweeping diagonal linear gradient background that animates its background-position across a 300% × 300% canvas to simulate uninterrupted color…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Shifting Linear Gradient
Source: https://codefronts.com/motion/css-gradient-animation/css-diagonal-shifting-linear-gradient/

A continuously sweeping diagonal linear gradient background that animates its background-position across a 300% × 300% canvas to simulate uninterrupted color flow across the full page.
## HTML
```html
<div class="ga-02">
  <div class="ga-02__content">
    <div class="ga-02__eyebrow">
      <div class="ga-02__dot"></div>
      <span class="ga-02__eyebrow-text">Live Platform</span>
    </div>
    <h1 class="ga-02__title">Design Without<br>Limits</h1>
    <p class="ga-02__sub">A professional-grade design suite that moves as fast as your ideas. Collaborate, prototype, and ship — all from one place.</p>
    <div class="ga-02__stats">
      <div class="ga-02__stat">
        <span class="ga-02__stat-num">4M+</span>
        <span class="ga-02__stat-label">Creators</span>
      </div>
      <div class="ga-02__stat">
        <span class="ga-02__stat-num">98%</span>
        <span class="ga-02__stat-label">Uptime</span>
      </div>
      <div class="ga-02__stat">
        <span class="ga-02__stat-num">12ms</span>
        <span class="ga-02__stat-label">Latency</span>
      </div>
    </div>
  </div>
  <div class="ga-02__controls">
    <span class="ga-02__ctrl-label">Angle:</span>
    <button class="ga-02__angle-btn" data-angle="45deg">45°</button>
    <button class="ga-02__angle-btn active" data-angle="135deg">135°</button>
    <button class="ga-02__angle-btn" data-angle="180deg">180°</button>
    <button class="ga-02__angle-btn" data-angle="90deg">90°</button>
  </div>
</div>
```
## CSS
```css
.ga-02,
.ga-02 *,
.ga-02 *::before,
.ga-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-02 ::selection {
  background: rgba(236,72,153,.4);
  color: #fff;
}

.ga-02 {
  --dur: 8s;
  --angle: 135deg;
  --c1: #1e0533;
  --c2: #312e81;
  --c3: #0c4a6e;
  --c4: #831843;
  --c5: #1e0533;
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 40px;
  padding: 48px 24px;
}
/* The animated background sits on a pseudo-element so background-size can be animated */

.ga-02::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(var(--angle),
      var(--c1) 0%,
      var(--c2) 20%,
      var(--c3) 40%,
      var(--c4) 60%,
      var(--c2) 80%,
      var(--c5) 100%
    );
  background-size: 300% 300%;
  animation: ga-02-sweep var(--dur) ease-in-out infinite;
}

@keyframes ga-02-sweep {
  0% {
    background-position: 0% 0%;
  }

  25% {
    background-position: 100% 0%;
  }

  50% {
    background-position: 100% 100%;
  }

  75% {
    background-position: 0% 100%;
  }

  100% {
    background-position: 0% 0%;
  }
}
/* Noise overlay for depth */

.ga-02::after {
  content: '';
  position: absolute;
  inset: 0;
  opacity: .04;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 200px 200px;
  pointer-events: none;
}
/* Content */

.ga-02__content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 680px;
}

.ga-02__eyebrow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 20px;
}

.ga-02__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #f472b6;
  animation: ga-02-pulse-dot 2s ease-in-out infinite;
}

@keyframes ga-02-pulse-dot {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: .5;
    transform: scale(.7);
  }
}

.ga-02__eyebrow-text {
  color: #f9a8d4;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.ga-02__title {
  font-size: clamp(2.2rem, 5.5vw, 3.6rem);
  font-weight: 900;
  line-height: 1.08;
  letter-spacing: -.03em;
  color: #fff;
  margin-bottom: 18px;
  text-shadow: 0 2px 30px rgba(0,0,0,.4);
}

.ga-02__sub {
  font-size: 1.05rem;
  color: rgba(255,255,255,.65);
  line-height: 1.7;
  margin-bottom: 36px;
}

.ga-02__stats {
  display: flex;
  gap: 0;
  justify-content: center;
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 14px;
  overflow: hidden;
  backdrop-filter: blur(12px);
  background: rgba(0,0,0,.2);
  max-width: 460px;
  margin: 0 auto;
}

.ga-02__stat {
  flex: 1;
  padding: 16px 8px;
  text-align: center;
  border-right: 1px solid rgba(255,255,255,.1);
}

.ga-02__stat:last-child {
  border-right: none;
}

.ga-02__stat-num {
  font-size: 1.5rem;
  font-weight: 800;
  color: #fff;
  display: block;
}

.ga-02__stat-label {
  font-size: .7rem;
  font-weight: 600;
  color: rgba(255,255,255,.45);
  text-transform: uppercase;
  letter-spacing: .07em;
  margin-top: 2px;
}
/* Angle control */

.ga-02__controls {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 10px;
}

.ga-02__ctrl-label {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,.4);
  text-transform: uppercase;
  letter-spacing: .08em;
}

.ga-02__angle-btn {
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.15);
  background: rgba(255,255,255,.07);
  color: rgba(255,255,255,.5);
  transition: all .2s;
}

.ga-02__angle-btn.active,
.ga-02__angle-btn:hover {
  background: rgba(244,114,182,.2);
  border-color: rgba(244,114,182,.5);
  color: #f9a8d4;
}

@media (prefers-reduced-motion: reduce) {
  .ga-02::before {
    animation: none;
    background-position: 50% 50%;
  }

  .ga-02__dot {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const wrapper = document.querySelector('.ga-02');
  const btns = wrapper.querySelectorAll('.ga-02__angle-btn');
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      wrapper.style.setProperty('--angle', btn.dataset.angle);
    });
  });
})();
```
