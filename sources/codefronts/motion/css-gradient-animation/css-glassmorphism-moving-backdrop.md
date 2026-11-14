---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-glassmorphism-moving-backdrop/"
title: "CSS Glassmorphism Moving Backdrop"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Four animated radial-gradient blobs drift behind a frosted-glass modal card that uses backdrop-filter: blur(28px), magnifying the depth illusion as the…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glassmorphism Moving Backdrop
Source: https://codefronts.com/motion/css-gradient-animation/css-glassmorphism-moving-backdrop/

Four animated radial-gradient blobs drift behind a frosted-glass modal card that uses backdrop-filter: blur(28px), magnifying the depth illusion as the colourful layer shifts continuously beneath the transparency.
## HTML
```html
<div class="ga-11">
  <div class="ga-11__blob ga-11__blob--1"></div>
  <div class="ga-11__blob ga-11__blob--2"></div>
  <div class="ga-11__blob ga-11__blob--3"></div>
  <div class="ga-11__blob ga-11__blob--4"></div>

  <div class="ga-11__glass">
    <div class="ga-11__card-head">
      <div class="ga-11__logo">
        <div class="ga-11__logo-box">✦</div>
        <span class="ga-11__logo-name">Prism</span>
      </div>
      <div class="ga-11__status">
        <div class="ga-11__status-dot"></div>
        Secure
      </div>
    </div>
    <div class="ga-11__divider"></div>
    <div class="ga-11__form-field">
      <span class="ga-11__form-label">Email address</span>
      <input class="ga-11__form-input" type="email" placeholder="[email protected]">
    </div>
    <div class="ga-11__form-field">
      <span class="ga-11__form-label">Password</span>
      <input class="ga-11__form-input" type="password" placeholder="••••••••••">
    </div>
    <div class="ga-11__btn-row">
      <button class="ga-11__btn ga-11__btn--fill">Sign In</button>
      <button class="ga-11__btn ga-11__btn--ghost">Register</button>
    </div>
    <p class="ga-11__note">The blobs behind the glass card are pure CSS animated gradients. The glass card uses <code>backdrop-filter: blur(28px)</code>.</p>
  </div>

  <div class="ga-11__ctrl">
    <button class="ga-11__ctrl-btn" data-dur="22s">Slow</button>
    <button class="ga-11__ctrl-btn active" data-dur="10s">Normal</button>
    <button class="ga-11__ctrl-btn" data-dur="4s">Fast</button>
  </div>
</div>
```
## CSS
```css
.ga-11,
.ga-11 *,
.ga-11 *::before,
.ga-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-11 ::selection {
  background: rgba(99,102,241,.5);
  color: #fff;
}

.ga-11 {
  --bg: #080a12;
  --dur: 10s;
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}
/* ── Animated gradient backdrop blobs ── */

.ga-11__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(50px);
  will-change: transform;
}

.ga-11__blob--1 {
  width: 420px;
  height: 420px;
  background: radial-gradient(circle, rgba(124,58,237,.7), transparent 65%);
  top: -80px;
  left: -80px;
  animation: ga-11-b1 var(--dur) ease-in-out infinite alternate;
}

.ga-11__blob--2 {
  width: 380px;
  height: 380px;
  background: radial-gradient(circle, rgba(6,182,212,.6), transparent 65%);
  bottom: -60px;
  right: -60px;
  animation: ga-11-b2 calc(var(--dur) * 1.3) ease-in-out infinite alternate;
}

.ga-11__blob--3 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(236,72,153,.55), transparent 65%);
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation: ga-11-b3 calc(var(--dur) * 1.6) ease-in-out infinite alternate;
}

.ga-11__blob--4 {
  width: 250px;
  height: 250px;
  background: radial-gradient(circle, rgba(16,185,129,.5), transparent 65%);
  bottom: 10%;
  left: 10%;
  animation: ga-11-b4 calc(var(--dur) * .9) ease-in-out infinite alternate;
}

@keyframes ga-11-b1 {
  0% {
    transform: translate(0, 0) scale(1);
  }

  100% {
    transform: translate(180px, 130px) scale(1.2);
  }
}

@keyframes ga-11-b2 {
  0% {
    transform: translate(0, 0) scale(1);
  }

  100% {
    transform: translate(-150px, -120px) scale(1.1);
  }
}

@keyframes ga-11-b3 {
  0% {
    transform: translate(-50%, -50%) scale(1);
  }

  100% {
    transform: translate(-30%, -70%) scale(.85);
  }
}

@keyframes ga-11-b4 {
  0% {
    transform: translate(0, 0);
  }

  100% {
    transform: translate(100px, -80px) scale(1.15);
  }
}
/* ── Glass card ── */

.ga-11__glass {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 440px;
  border-radius: 24px;
  padding: 36px;
  background: rgba(255,255,255,.055);
  border: 1px solid rgba(255,255,255,.1);
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  box-shadow: 0 0 0 1px rgba(255,255,255,.04) inset, 0 24px 60px rgba(0,0,0,.4);
  display: flex;
  flex-direction: column;
  gap: 22px;
}
/* Card inner content */

.ga-11__card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ga-11__logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ga-11__logo-box {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: linear-gradient(135deg, #7c3aed, #06b6d4);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
}

.ga-11__logo-name {
  font-size: .9rem;
  font-weight: 700;
  color: rgba(255,255,255,.9);
}

.ga-11__status {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: .72rem;
  font-weight: 700;
  color: #34d399;
  text-transform: uppercase;
  letter-spacing: .08em;
}

.ga-11__status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #34d399;
  animation: ga-11-blink 2s ease-in-out infinite;
}

@keyframes ga-11-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .3;
  }
}

.ga-11__divider {
  height: 1px;
  background: rgba(255,255,255,.07);
}

.ga-11__form-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ga-11__form-label {
  font-size: .7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .09em;
  color: rgba(255,255,255,.35);
}

.ga-11__form-input {
  padding: 11px 14px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 10px;
  font-size: .88rem;
  color: rgba(255,255,255,.8);
  outline: none;
  transition: border-color .2s, background .2s;
}

.ga-11__form-input:focus {
  border-color: rgba(124,58,237,.5);
  background: rgba(124,58,237,.07);
}

.ga-11__form-input::placeholder {
  color: rgba(255,255,255,.2);
}

.ga-11__btn-row {
  display: flex;
  gap: 10px;
}

.ga-11__btn {
  flex: 1;
  padding: 11px;
  border-radius: 10px;
  font-size: .85rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: all .2s;
}

.ga-11__btn--fill {
  background: linear-gradient(135deg, #7c3aed, #06b6d4);
  color: #fff;
}

.ga-11__btn--fill:hover {
  box-shadow: 0 4px 20px rgba(124,58,237,.4);
  transform: translateY(-1px);
}

.ga-11__btn--ghost {
  background: rgba(255,255,255,.06);
  color: rgba(255,255,255,.5);
  border: 1px solid rgba(255,255,255,.1);
}

.ga-11__btn--ghost:hover {
  background: rgba(255,255,255,.1);
  color: rgba(255,255,255,.75);
}

.ga-11__note {
  font-size: .72rem;
  color: rgba(255,255,255,.25);
  text-align: center;
  line-height: 1.5;
}
/* Speed control */

.ga-11__ctrl {
  position: absolute;
  bottom: 16px;
  right: 16px;
  z-index: 10;
  display: flex;
  gap: 6px;
}

.ga-11__ctrl-btn {
  padding: 4px 10px;
  font-size: .7rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.05);
  color: rgba(255,255,255,.35);
  cursor: pointer;
  transition: all .2s;
  backdrop-filter: blur(4px);
}

.ga-11__ctrl-btn.active,
.ga-11__ctrl-btn:hover {
  background: rgba(124,58,237,.2);
  border-color: rgba(124,58,237,.4);
  color: #c4b5fd;
}

@media (prefers-reduced-motion: reduce) {
  .ga-11__blob {
    animation: none;
  }

  .ga-11__status-dot {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-11');
  w.querySelectorAll('.ga-11__ctrl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-11__ctrl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur', btn.dataset.dur);
    });
  });
})();
```
