---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-spring-bounce-animation/"
title: "CSS Spring Bounce Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Eight CSS spring and elastic animations: drop ball with squash, elastic button, pop-in notification, stagger scale cards, spin, wobbly text, spring menu and…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Spring Bounce Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-spring-bounce-animation/

Eight CSS spring and elastic animations: drop ball with squash, elastic button, pop-in notification, stagger scale cards, spin, wobbly text, spring menu and rubber bars.
## HTML
```html
<div class="kf-22">
  <h2>CSS Spring Bounce Animations</h2>
  <div class="grid">

    <div class="card">
      <div class="ball-spring"></div>
      <label>Spring Drop</label>
    </div>

    <div class="card">
      <button class="spring-btn">Click Me ✦</button>
      <label>Elastic Button</label>
    </div>

    <div class="card">
      <div class="notif">
        <div class="notif-icon">✓</div>
        <div>
          <div class="notif-text">Success!</div>
          <div class="notif-sub">Task completed</div>
        </div>
      </div>
      <label>Spring Pop-in</label>
    </div>

    <div class="card">
      <div class="scale-grid">
        <div class="scale-card"></div>
        <div class="scale-card"></div>
        <div class="scale-card"></div>
        <div class="scale-card"></div>
      </div>
      <label>Stagger Scale</label>
    </div>

    <div class="card">
      <div class="spin-spring"></div>
      <label>Spring Rotation</label>
    </div>

    <div class="card">
      <div class="wobble-text">
        <span>S</span><span>P</span><span>R</span><span>I</span><span>N</span><span>G</span>
      </div>
      <label>Wobbly Text</label>
    </div>

    <div class="card">
      <div class="menu-spring">
        <div class="menu-item">Dashboard</div>
        <div class="menu-item">Analytics</div>
        <div class="menu-item">Settings</div>
        <div class="menu-item">Profile</div>
      </div>
      <label>Spring Menu</label>
    </div>

    <div class="card">
      <div class="rubber-wrap">
        <div class="rubber-bar"></div>
        <div class="rubber-bar"></div>
        <div class="rubber-bar"></div>
      </div>
      <label>Rubber Bars</label>
    </div>

  </div>
</div>
```
## CSS
```css
.kf-22 *,
.kf-22 *::before,
.kf-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-22 {
  font-family: 'Segoe UI', sans-serif;
  background: #f0f4ff;
  color: #1a1a2e;
  padding: 48px 24px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}

.kf-22 h2 {
  font-size: 1.1rem;
  color: #888;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.kf-22 .grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
  width: 100%;
  max-width: 960px;
}

.kf-22 .card {
  background: #fff;
  border-radius: 20px;
  padding: 40px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.07);
}

.kf-22 .card label {
  font-size: 0.75rem;
  color: #aaa;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Spring easings via keyframes */
/* 1: Ball spring drop */

.kf-22 .ball-spring {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7c6af7, #e91e8c);
  animation: kf-22-springdrop 1.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) infinite;
  box-shadow: 0 8px 24px rgba(124,106,247,0.4);
}

@keyframes kf-22-springdrop {
  0% {
    transform: translateY(-80px) scaleX(0.8) scaleY(1.2);
  }

  60% {
    transform: translateY(0) scaleX(1.2) scaleY(0.8);
  }

  75% {
    transform: translateY(-20px) scaleX(0.95) scaleY(1.05);
  }

  85% {
    transform: translateY(0) scaleX(1.05) scaleY(0.95);
  }

  92% {
    transform: translateY(-6px);
  }

  100% {
    transform: translateY(0) scaleX(1) scaleY(1);
  }
}
/* 2: Elastic button press */

.kf-22 .spring-btn {
  padding: 14px 32px;
  background: #7c6af7;
  color: #fff;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  animation: kf-22-btnspring 2s ease-in-out infinite;
  box-shadow: 0 6px 20px rgba(124,106,247,0.3);
}

@keyframes kf-22-btnspring {
  0%,
    60%,
    100% {
    transform: scale(1);
  }

  10% {
    transform: scaleX(0.85) scaleY(1.15);
  }

  25% {
    transform: scaleX(1.15) scaleY(0.85);
  }

  35% {
    transform: scaleX(0.95) scaleY(1.05);
  }

  45% {
    transform: scaleX(1.05) scaleY(0.97);
  }

  52% {
    transform: scaleX(0.98) scaleY(1.02);
  }
}
/* 3: Spring pop notification */

.kf-22 .notif {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  background: #fff;
  border-radius: 16px;
  padding: 12px 16px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.12);
  animation: kf-22-notifpop 2.5s cubic-bezier(0.34, 1.56, 0.64, 1) infinite;
  transform-origin: top center;
  min-width: 200px;
}

@keyframes kf-22-notifpop {
  0%,
    40%,
    100% {
    transform: scale(0);
    opacity: 0;
  }

  50% {
    transform: scale(1.08);
    opacity: 1;
  }

  60%,
    90% {
    transform: scale(1);
    opacity: 1;
  }

  100% {
    transform: scale(0);
    opacity: 0;
  }
}

.kf-22 .notif-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: linear-gradient(135deg, #00d46a, #00b050);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
}

.kf-22 .notif-text {
  font-size: 0.85rem;
  font-weight: 600;
  color: #333;
}

.kf-22 .notif-sub {
  font-size: 0.72rem;
  color: #aaa;
}
/* 4: Spring scale cards */

.kf-22 .scale-grid {
  display: flex;
  gap: 10px;
  align-items: flex-end;
}

.kf-22 .scale-card {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #ff6b35, #f7c948);
  animation: kf-22-scalepop 2.4s cubic-bezier(0.34, 1.56, 0.64, 1) infinite;
}

.kf-22 .scale-card:nth-child(2) {
  animation-delay: 0.15s;
  background: linear-gradient(135deg, #f7c948, #00d46a);
}

.kf-22 .scale-card:nth-child(3) {
  animation-delay: 0.3s;
  background: linear-gradient(135deg, #00d46a, #00d4ff);
}

.kf-22 .scale-card:nth-child(4) {
  animation-delay: 0.45s;
  background: linear-gradient(135deg, #00d4ff, #7c6af7);
}

@keyframes kf-22-scalepop {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.3);
  }
}
/* 5: Spring rotation */

.kf-22 .spin-spring {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #00d4ff, #7c6af7);
  border-radius: 16px;
  animation: kf-22-rotspring 2s cubic-bezier(0.34, 1.56, 0.64, 1) infinite;
}

@keyframes kf-22-rotspring {
  0% {
    transform: rotate(0deg);
  }

  50% {
    transform: rotate(200deg);
  }

  100% {
    transform: rotate(180deg);
  }
}
/* 6: Wobbly text */

.kf-22 .wobble-text {
  font-size: 1.8rem;
  font-weight: 900;
  color: #1a1a2e;
  letter-spacing: 6px;
  display: flex;
  gap: 2px;
}

.kf-22 .wobble-text span {
  display: inline-block;
  animation: kf-22-wobble 2s cubic-bezier(0.36, 0.07, 0.19, 0.97) infinite;
}

.kf-22 .wobble-text span:nth-child(1) {
  animation-delay: 0.0s;
  color: #7c6af7;
}

.kf-22 .wobble-text span:nth-child(2) {
  animation-delay: 0.08s;
  color: #e91e8c;
}

.kf-22 .wobble-text span:nth-child(3) {
  animation-delay: 0.16s;
  color: #ff6b35;
}

.kf-22 .wobble-text span:nth-child(4) {
  animation-delay: 0.24s;
  color: #f7c948;
}

.kf-22 .wobble-text span:nth-child(5) {
  animation-delay: 0.32s;
  color: #00d46a;
}

.kf-22 .wobble-text span:nth-child(6) {
  animation-delay: 0.40s;
  color: #00d4ff;
}

@keyframes kf-22-wobble {
  0%,
    60%,
    100% {
    transform: translateY(0) scaleX(1) scaleY(1);
  }

  15% {
    transform: translateY(-20px) scaleX(0.9) scaleY(1.1);
  }

  30% {
    transform: translateY(0) scaleX(1.1) scaleY(0.9);
  }

  40% {
    transform: translateY(-8px) scaleX(0.97) scaleY(1.03);
  }

  50% {
    transform: translateY(0) scaleX(1.02) scaleY(0.98);
  }
}
/* 7: Spring menu items */

.kf-22 .menu-spring {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
  max-width: 200px;
}

.kf-22 .menu-item {
  padding: 10px 16px;
  border-radius: 10px;
  font-size: 0.85rem;
  font-weight: 500;
  color: #fff;
  animation: kf-22-menuspring 3s cubic-bezier(0.34, 1.56, 0.64, 1) infinite;
  transform-origin: left center;
}

.kf-22 .menu-item:nth-child(1) {
  background: #7c6af7;
  animation-delay: 0.1s;
}

.kf-22 .menu-item:nth-child(2) {
  background: #e91e8c;
  animation-delay: 0.25s;
}

.kf-22 .menu-item:nth-child(3) {
  background: #00d4ff;
  animation-delay: 0.4s;
}

.kf-22 .menu-item:nth-child(4) {
  background: #ff6b35;
  animation-delay: 0.55s;
}

@keyframes kf-22-menuspring {
  0%,
    70%,
    100% {
    transform: translateX(0) scaleX(1);
    opacity: 1;
  }

  80% {
    transform: translateX(-100%) scaleX(0.8);
    opacity: 0;
  }

  85% {
    transform: translateX(-20px) scaleX(1.05);
    opacity: 1;
  }

  92% {
    transform: translateX(4px);
  }
}
/* 8: Elastic line/rubber band */

.kf-22 .rubber-wrap {
  width: 100%;
  max-width: 200px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.kf-22 .rubber-bar {
  height: 12px;
  border-radius: 6px;
  background: linear-gradient(90deg, #7c6af7, #e91e8c);
  animation: kf-22-rubber 2s cubic-bezier(0.34, 1.56, 0.64, 1) infinite;
  transform-origin: left center;
}

.kf-22 .rubber-bar:nth-child(2) {
  animation-delay: 0.2s;
  background: linear-gradient(90deg, #00d4ff, #00d46a);
  width: 75%;
}

.kf-22 .rubber-bar:nth-child(3) {
  animation-delay: 0.4s;
  background: linear-gradient(90deg, #ff6b35, #f7c948);
  width: 55%;
}

@keyframes kf-22-rubber {
  0% {
    transform: scaleX(0);
  }

  60% {
    transform: scaleX(1.1);
  }

  75% {
    transform: scaleX(0.97);
  }

  85% {
    transform: scaleX(1.03);
  }

  100% {
    transform: scaleX(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-22 .ball-spring,
    .kf-22 .spring-btn,
    .kf-22 .notif,
    .kf-22 .scale-card,
    .kf-22 .spin-spring,
    .kf-22 .wobble-text span,
    .kf-22 .menu-item,
    .kf-22 .rubber-bar {
    animation: none;
    transform: none;
    opacity: 1;
  }
}
```
