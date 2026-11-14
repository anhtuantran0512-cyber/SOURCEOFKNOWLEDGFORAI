---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-glitch-text-animation-effect/"
title: "CSS Glitch Text Animation Effect"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Four CSS glitch text effects: RGB channel split, terminal ghost, slice glitch and noise word distortion — using clip-path and translate keyframes with no JS."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glitch Text Animation Effect
Source: https://codefronts.com/motion/css-keyframe-animations/css-glitch-text-animation-effect/

Four CSS glitch text effects: RGB channel split, terminal ghost, slice glitch and noise word distortion — using clip-path and translate keyframes with no JS.
## HTML
```html
<div class="kf-11">
  <div class="kf-11__glitch" data-text="GLITCH">GLITCH</div>
  <div class="kf-11__terminal" data-text=">> SYSTEM_OVERRIDE.exe">&#62;&#62; SYSTEM_OVERRIDE.exe</div>
  <div class="kf-11__slice" data-text="CORRUPT">CORRUPT</div>
  <div class="kf-11__noise" data-text="SYSTEM">SYSTEM</div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Share+Tech+Mono&display=swap');

.kf-11,
.kf-11 *,
.kf-11 *::before,
.kf-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-11 ::selection {
  background: #00ff41;
  color: #000;
}

.kf-11 {
  --bg: #0a0a0a;
  --green: #00ff41;
  --red: #ff0055;
  --cyan: #00e5ff;
  --white: #f0f0f0;
  font-family: 'Orbitron',monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 72px;
  overflow: hidden;
  position: relative;
}
/* Scanline overlay */

.kf-11::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 10;
  background: repeating-linear-gradient(0deg,transparent 0 2px,rgba(0,255,65,.02) 2px 4px);
}
/* 1 — Classic RGB split glitch */

.kf-11__glitch {
  font-size: clamp(2.5rem,10vw,6rem);
  font-weight: 900;
  color: var(--white);
  position: relative;
  letter-spacing: .05em;
  animation: kf-11-shudder 4s steps(1) infinite;
}

.kf-11__glitch::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--red);
  clip-path: polygon(0 30%,100% 30%,100% 55%,0 55%);
  transform: translateX(-4px);
  animation: kf-11-glitch-r 4s steps(1) infinite;
}

.kf-11__glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--cyan);
  clip-path: polygon(0 55%,100% 55%,100% 80%,0 80%);
  transform: translateX(4px);
  animation: kf-11-glitch-c 4s steps(1) infinite .05s;
}

@keyframes kf-11-glitch-r {
  0%,
    85%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  86% {
    opacity: 1;
    transform: translateX(-6px);
  }

  87% {
    opacity: 1;
    transform: translateX(-2px);
    clip-path: polygon(0 20%,100% 20%,100% 40%,0 40%);
  }

  88% {
    opacity: 0;
  }

  92% {
    opacity: 1;
    transform: translateX(-8px);
    clip-path: polygon(0 60%,100% 60%,100% 80%,0 80%);
  }

  94% {
    opacity: 0;
  }
}

@keyframes kf-11-glitch-c {
  0%,
    85%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  86% {
    opacity: 1;
    transform: translateX(5px);
  }

  88% {
    opacity: 0;
  }

  92% {
    opacity: 1;
    transform: translateX(3px);
    clip-path: polygon(0 40%,100% 40%,100% 60%,0 60%);
  }

  94% {
    opacity: 0;
  }
}

@keyframes kf-11-shudder {
  0%,
    84%,
    100% {
    transform: skewX(0);
  }

  85% {
    transform: skewX(-2deg);
  }

  87% {
    transform: skewX(2deg);
  }

  89%,
    90% {
    transform: skewX(0);
  }
}
/* 2 — Green terminal glitch */

.kf-11__terminal {
  font-family: 'Share Tech Mono',monospace;
  font-size: clamp(1.2rem,4vw,2rem);
  color: var(--green);
  text-shadow: 0 0 8px rgba(0,255,65,.5);
  position: relative;
  animation: kf-11-term 5s steps(1) infinite;
}

.kf-11__terminal::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: rgba(0,255,65,.3);
  animation: kf-11-term-ghost 5s steps(1) infinite;
  overflow: hidden;
}

@keyframes kf-11-term {
  0%,
    78%,
    100% {
    transform: none;
    filter: none;
  }

  79% {
    transform: translateX(-3px);
    filter: brightness(1.3);
  }

  80% {
    transform: translateX(2px);
    filter: brightness(.8);
  }

  81% {
    transform: none;
    filter: none;
  }

  91% {
    transform: translateX(-1px) scaleY(1.02);
  }

  92% {
    transform: none;
  }
}

@keyframes kf-11-term-ghost {
  0%,
    78%,
    100% {
    opacity: 0;
    transform: none;
  }

  79%,
    80%,
    81% {
    opacity: 1;
    transform: translateY(3px);
  }

  82% {
    opacity: 0;
  }
}
/* 3 — Slice glitch */

.kf-11__slice {
  font-size: clamp(2rem,8vw,4.5rem);
  font-weight: 700;
  color: var(--white);
  position: relative;
  line-height: 1;
}

.kf-11__slice::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  background: linear-gradient(var(--bg) 45%,transparent 45%,transparent 55%,var(--bg) 55%);
  color: var(--cyan);
  animation: kf-11-slice 3s steps(1) infinite 1s;
}

@keyframes kf-11-slice {
  0%,
    89%,
    100% {
    transform: translateX(0);
    opacity: 0;
  }

  90% {
    transform: translateX(-8px);
    opacity: 1;
  }

  91% {
    transform: translateX(6px);
  }

  92% {
    transform: translateX(0);
    opacity: 0;
  }

  95% {
    transform: translateX(4px);
    opacity: .6;
  }

  96% {
    opacity: 0;
  }
}
/* 4 — Noise word */

.kf-11__noise {
  font-size: clamp(1.8rem,7vw,4rem);
  font-weight: 900;
  color: var(--white);
  position: relative;
  overflow: hidden;
}

.kf-11__noise::before {
  content: 'S!Yst3m#FaIL';
  position: absolute;
  inset: 0;
  color: var(--red);
  font-family: 'Share Tech Mono';
  font-size: .8em;
  letter-spacing: .2em;
  animation: kf-11-noise 4s steps(1) infinite 0.5s;
  opacity: 0;
}

@keyframes kf-11-noise {
  0%,
    87%,
    100% {
    opacity: 0;
    transform: none;
  }

  88% {
    opacity: 1;
    transform: translateY(-2px) scaleX(1.04);
  }

  89% {
    transform: translateY(2px) scaleX(.98);
  }

  90%,
    92% {
    opacity: 0;
  }

  91% {
    opacity: .8;
    transform: translateX(-4px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-11 *,
    .kf-11 *::before,
    .kf-11 *::after {
    animation: none!important;
  }
}
```
