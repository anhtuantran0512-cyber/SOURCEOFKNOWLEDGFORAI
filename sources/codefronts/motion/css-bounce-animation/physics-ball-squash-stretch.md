---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/physics-ball-squash-stretch/"
title: "Physics Ball Squash Stretch"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A bouncing ball with realistic squash-and-stretch physics — falls fast, flattens on floor contact, rebounds with elastic stretch."
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Physics Ball Squash Stretch
Source: https://codefronts.com/motion/css-bounce-animation/physics-ball-squash-stretch/

A bouncing ball with realistic squash-and-stretch physics — falls fast, flattens on floor contact, rebounds with elastic stretch. The classic Disney animation principle rendered as pure CSS with a multi-stop keyframe. Coral ball on a warm beige floor with a soft ground shadow that scales with the ball's height. The pattern users search for when learning "how do I bounce a ball with real physics in CSS."
## HTML
```html
<div class="bn-11">
  <p class="bn-11__label">Squash-and-stretch physics ball</p>
  <div class="bn-11__scene" aria-hidden="true">
    <div class="bn-11__ball"></div>
    <div class="bn-11__shadow"></div>
    <div class="bn-11__floor"></div>
  </div>
  <p class="bn-11__hint">Ball stretches at descent + rebound, squashes at floor contact.</p>
</div>
```
## CSS
```css
.bn-11 {
  --page-bg: #faf7f0;
  --floor: #c9b78c;
  --ball: #ff6b6b;
  --ball-hi: #ffa8a8;
  --ball-shadow: rgba(191,64,64,.35);
  --shadow-color: rgba(58,42,26,.35);
  --ink: #3a2a1a;
  --sub: #8b7355;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 32px;
  background: radial-gradient(80% 60% at 50% 100%, rgba(191,157,111,.24) 0%, transparent 55%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-11 *,
.bn-11 *::before,
.bn-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-11 ::selection {
  background: var(--ball);
  color: #fff;
}

.bn-11__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-11__scene {
  position: relative;
  width: 200px;
  height: 240px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}

.bn-11__ball {
  position: absolute;
  bottom: 32px;
  left: 50%;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%,var(--ball-hi),var(--ball));
  box-shadow: 0 4px 8px -2px var(--ball-shadow);
  transform: translateX(-50%);
  animation: bn-11-ball 1.2s ease-in-out infinite;
  transform-origin: bottom center;
  will-change: transform;
}

@keyframes bn-11-ball {
  0% {
    transform: translateX(-50%) translateY(-160px) scale(1);
  }

  45% {
    transform: translateX(-50%) translateY(-40px) scaleY(1.15) scaleX(.9);
  }

  50% {
    transform: translateX(-50%) translateY(0) scaleY(.7) scaleX(1.3);
  }

  55% {
    transform: translateX(-50%) translateY(-40px) scaleY(1.15) scaleX(.9);
  }

  100% {
    transform: translateX(-50%) translateY(-160px) scale(1);
  }
}

.bn-11__shadow {
  position: absolute;
  bottom: 24px;
  left: 50%;
  width: 60px;
  height: 16px;
  border-radius: 50%;
  background: var(--shadow-color);
  filter: blur(4px);
  transform: translateX(-50%) scale(.5);
  animation: bn-11-shadow 1.2s ease-in-out infinite;
  will-change: transform;
}

@keyframes bn-11-shadow {
  0% {
    transform: translateX(-50%) scale(.5);
    opacity: .4;
  }

  50% {
    transform: translateX(-50%) scale(1.15);
    opacity: .85;
  }

  100% {
    transform: translateX(-50%) scale(.5);
    opacity: .4;
  }
}

.bn-11__floor {
  width: 180px;
  height: 6px;
  border-radius: 3px;
  background: linear-gradient(90deg,transparent,var(--floor) 20%,var(--floor) 80%,transparent);
}

.bn-11__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 360px;
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .bn-11__ball,
    .bn-11__shadow {
    animation: none!important;
  }

  .bn-11__ball {
    transform: translateX(-50%) translateY(0) scale(1)!important;
  }

  .bn-11__shadow {
    transform: translateX(-50%) scale(1)!important;
    opacity: .7!important;
  }
}
```
