---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/rotatex-perspective-tilt-fade/"
title: "RotateX Perspective Tilt Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "Three feature tiles tumble forward into position via perspective(800px) rotateX(60deg → 0) with staggered delays, creating a card-dealing 3D tilt-down entrance."
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: RotateX Perspective Tilt Fade
Source: https://codefronts.com/motion/css-fade-in-animation/rotatex-perspective-tilt-fade/

Three feature tiles tumble forward into position via perspective(800px) rotateX(60deg → 0) with staggered delays, creating a card-dealing 3D tilt-down entrance.
## HTML
```html
<div class="fi-09">
  <div class="fi-09__tile">
    <div class="fi-09__icon">🌐</div>
    <div class="fi-09__name">Web Platform</div>
    <div class="fi-09__desc">Cards tumble into place with a 3D perspective rotation on the X axis.</div>
    <div class="fi-09__tag">rotateX</div>
  </div>
  <div class="fi-09__tile">
    <div class="fi-09__icon">📐</div>
    <div class="fi-09__name">Perspective</div>
    <div class="fi-09__desc">CSS perspective() gives depth, making 2D elements feel truly spatial.</div>
    <div class="fi-09__tag">perspective</div>
  </div>
  <div class="fi-09__tile">
    <div class="fi-09__icon">✨</div>
    <div class="fi-09__name">Depth Fade</div>
    <div class="fi-09__desc">Combined with opacity, the tilt creates a cinematic camera-drop entrance.</div>
    <div class="fi-09__tag">3D fade</div>
  </div>
</div>
```
## CSS
```css
.fi-09 {
  --bg: #0c0d1a;
  --blue: #3b82f6;
  --indigo: #6366f1;
  --text: #eff6ff;
  font-family: 'Inter',sans-serif;
  min-height: 360px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  padding: 40px;
  overflow: hidden;
  perspective: 1000px;
}

.fi-09 *,
.fi-09 *::before,
.fi-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-09 ::selection {
  background: var(--blue);
  color: #fff;
}
/* rotateX perspective fade: rotateX(60deg) opacity:0 → rotateX(0) opacity:1 */

.fi-09__tile {
  width: 160px;
  min-height: 180px;
  border-radius: 14px;
  padding: 24px 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  opacity: 0;
  transform: perspective(800px) rotateX(60deg) translateY(20px);
  animation: fi-09-flip-in .7s cubic-bezier(.16,1,.3,1) forwards;
}

.fi-09__tile:nth-child(1) {
  --d: .05s;
  background: linear-gradient(160deg,rgba(59,130,246,.18),rgba(99,102,241,.1));
  border: 1px solid rgba(59,130,246,.3);
}

.fi-09__tile:nth-child(2) {
  --d: .2s;
  background: linear-gradient(160deg,rgba(99,102,241,.18),rgba(139,92,246,.1));
  border: 1px solid rgba(99,102,241,.3);
}

.fi-09__tile:nth-child(3) {
  --d: .35s;
  background: linear-gradient(160deg,rgba(139,92,246,.18),rgba(167,139,250,.1));
  border: 1px solid rgba(139,92,246,.3);
}

.fi-09__tile {
  animation-delay: var(--d);
}

.fi-09__tile:hover {
  transform: perspective(800px) rotateX(-4deg) translateY(-4px)!important;
  transition: transform .3s;
}

.fi-09__icon {
  font-size: 2rem;
}

.fi-09__name {
  font-family: 'Syne',sans-serif;
  font-size: .95rem;
  font-weight: 700;
  color: var(--text);
}

.fi-09__desc {
  font-size: .75rem;
  color: rgba(239,246,255,.45);
  line-height: 1.5;
  flex: 1;
}

.fi-09__tag {
  font-size: .65rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 6px;
  background: rgba(59,130,246,.15);
  color: var(--blue);
  align-self: flex-start;
}

.fi-09__tile:nth-child(2) .fi-09__tag {
  background: rgba(99,102,241,.15);
  color: #818cf8;
}

.fi-09__tile:nth-child(3) .fi-09__tag {
  background: rgba(139,92,246,.15);
  color: #a78bfa;
}

@keyframes fi-09-flip-in {
  to {
    opacity: 1;
    transform: perspective(800px) rotateX(0deg) translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-09 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
