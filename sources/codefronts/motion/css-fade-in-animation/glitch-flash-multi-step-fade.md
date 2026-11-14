---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/glitch-flash-multi-step-fade/"
title: "Glitch Flash Multi-Step Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A terminal-style display where the headline stutters into existence through a multi-step opacity flicker keyframe with micro translateX jitter, simulating a…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Flash Multi-Step Fade
Source: https://codefronts.com/motion/css-fade-in-animation/glitch-flash-multi-step-fade/

A terminal-style display where the headline stutters into existence through a multi-step opacity flicker keyframe with micro translateX jitter, simulating a signal locking on.
## HTML
```html
<div class="fi-15">
  <div class="fi-15__screen">
    <span class="fi-15__line">BOOT SEQUENCE INITIATED...</span>
    <span class="fi-15__line">LOADING KERNEL MODULES...</span>
    <span class="fi-15__line">SIGNAL ACQUIRED. RENDERING...</span>
    <div class="fi-15__glitch-text" data-text="GLITCH FADE">GLITCH FADE</div>
    <div class="fi-15__sub">MULTI-STEP OPACITY FLICKER TECHNIQUE<span class="fi-15__cursor"></span></div>
  </div>
</div>
```
## CSS
```css
.fi-15 {
  --bg: #050505;
  --red: #ff2244;
  --white: #f8f8f8;
  --dim: #888;
  font-family: 'Orbitron',monospace;
  min-height: 340px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  padding: 40px;
  overflow: hidden;
  position: relative;
}

.fi-15 *,
.fi-15 *::before,
.fi-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-15 ::selection {
  background: var(--red);
  color: #fff;
}
/* glitch-flash fade: multi-step opacity flicker + slight translateX jitter */

.fi-15__screen {
  text-align: center;
  position: relative;
}

.fi-15__line {
  display: block;
  font-family: 'Share Tech Mono',monospace;
  font-size: .7rem;
  letter-spacing: .15em;
  color: var(--dim);
  margin-bottom: 8px;
  opacity: 0;
  animation: fi-15-static .1s steps(1) forwards;
}

.fi-15__line:nth-child(1) {
  animation-delay: .1s;
}

.fi-15__line:nth-child(2) {
  animation-delay: .2s;
}

.fi-15__line:nth-child(3) {
  animation-delay: .3s;
}

.fi-15__glitch-text {
  font-size: clamp(2rem,6vw,4rem);
  font-weight: 900;
  color: var(--white);
  position: relative;
  display: inline-block;
  animation: fi-15-glitch-in 1.2s steps(1) .4s forwards;
  opacity: 0;
}

.fi-15__glitch-text::before,
.fi-15__glitch-text::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
}

.fi-15__glitch-text::before {
  color: var(--red);
  animation: fi-15-ghost-r 1.2s steps(1) .4s forwards;
  opacity: 0;
  clip-path: polygon(0 20%,100% 20%,100% 45%,0 45%);
}

.fi-15__glitch-text::after {
  color: #0ff;
  animation: fi-15-ghost-l 1.2s steps(1) .4s forwards;
  opacity: 0;
  clip-path: polygon(0 55%,100% 55%,100% 80%,0 80%);
}

.fi-15__sub {
  font-size: .65rem;
  letter-spacing: .2em;
  color: var(--dim);
  margin-top: 16px;
  opacity: 0;
  animation: fi-15-static .1s steps(1) 1.4s forwards;
}

.fi-15__cursor {
  display: inline-block;
  width: 2px;
  height: 1em;
  background: var(--red);
  vertical-align: middle;
  margin-left: 4px;
  animation: fi-15-blink .8s steps(1) infinite 1.4s;
  opacity: 0;
}

@keyframes fi-15-glitch-in {
  0% {
    opacity: 0;
    transform: translateX(-4px);
  }

  5% {
    opacity: 1;
    transform: translateX(3px);
  }

  8% {
    opacity: 0;
    transform: translateX(-2px);
  }

  12% {
    opacity: 1;
    transform: translateX(0);
  }

  20% {
    opacity: .3;
    transform: translateX(2px);
  }

  22% {
    opacity: 1;
    transform: translateX(0);
  }

  35% {
    opacity: .8;
    transform: translateX(-1px);
  }

  40% {
    opacity: 1;
    transform: translateX(0);
  }

  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fi-15-ghost-r {
  0% {
    opacity: 0;
  }

  5% {
    opacity: .8;
    transform: translateX(4px);
  }

  8% {
    opacity: 0;
  }

  20% {
    opacity: .6;
    transform: translateX(-3px);
  }

  22% {
    opacity: 0;
  }

  35% {
    opacity: .4;
    transform: translateX(2px);
  }

  40% {
    opacity: 0;
  }

  100% {
    opacity: 0;
  }
}

@keyframes fi-15-ghost-l {
  0% {
    opacity: 0;
  }

  12% {
    opacity: .7;
    transform: translateX(-3px);
  }

  15% {
    opacity: 0;
  }

  28% {
    opacity: .5;
    transform: translateX(2px);
  }

  30% {
    opacity: 0;
  }

  100% {
    opacity: 0;
  }
}

@keyframes fi-15-static {
  to {
    opacity: 1;
  }
}

@keyframes fi-15-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-15 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
