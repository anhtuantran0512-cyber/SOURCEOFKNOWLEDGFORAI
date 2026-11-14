---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/404-error-glitch-page/"
title: "404 Error Glitch Page"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Massive \"404\" numerals with jagged horizontal cut lines and colour-channel pseudo-layers that erupt in synchronised violent bursts, reinforcing a…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 404 Error Glitch Page
Source: https://codefronts.com/motion/css-glitch-text-effect/404-error-glitch-page/

Massive "404" numerals with jagged horizontal cut lines and colour-channel pseudo-layers that erupt in synchronised violent bursts, reinforcing a corrupted-data error page aesthetic.
## HTML
```html
<div class="gt-05">
  <div class="gt-05__corrupt-bar"></div>
  <div class="gt-05__corrupt-bar"></div>
  <div class="gt-05__corrupt-bar"></div>
  <div class="gt-05__crack"></div>
  <div class="gt-05__crack"></div>
  <div class="gt-05__num" data-text="404">404</div>
  <p class="gt-05__msg">Page data corrupted</p>
  <span class="gt-05__detail">ERR_DATA_INTEGRITY_0x4F4F34</span>
</div>
```
## CSS
```css
.gt-05,
.gt-05 *,
.gt-05 *::before,
.gt-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-05 ::selection {
  background: #ff2d55;
  color: #fff;
}

.gt-05 {
  --red: #ff2d55;
  --orange: #ff6b35;
  --bg: #09090e;
  --text: #f5f5fa;
  --dim: rgba(245,245,250,0.35);
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 48px 20px;
  font-family: 'Inter', system-ui, sans-serif;
  position: relative;
  overflow: hidden;
}
/* Corruption bars that occasionally flash */

.gt-05__corrupt-bar {
  position: absolute;
  left: 0;
  right: 0;
  height: 6px;
  background: linear-gradient(90deg, transparent 0%, var(--red) 20%, rgba(255,255,255,0.9) 50%, var(--red) 80%, transparent);
  opacity: 0;
  animation: gt-05-corrupt-flash 4.5s steps(1) infinite;
}

.gt-05__corrupt-bar:nth-child(1) {
  top: 30%;
  animation-delay: 0s;
}

.gt-05__corrupt-bar:nth-child(2) {
  top: 55%;
  animation-delay: 1.8s;
  height: 3px;
}

.gt-05__corrupt-bar:nth-child(3) {
  top: 75%;
  animation-delay: 3.2s;
  height: 10px;
}

@keyframes gt-05-corrupt-flash {
  0%,
    88%,
    92%,
    100% {
    opacity: 0;
    transform: scaleX(1);
  }

  89% {
    opacity: 0.8;
    transform: scaleX(1.02);
  }

  90% {
    opacity: 0.4;
    transform: scaleX(0.98);
  }

  91% {
    opacity: 0.9;
    transform: scaleX(1.01);
  }
}
/* Giant 404 */

.gt-05__num {
  position: relative;
  font-size: clamp(80px, 18vw, 160px);
  font-weight: 900;
  color: var(--text);
  letter-spacing: -4px;
  line-height: 1;
  text-align: center;
}
/* Slice cuts. Originally the slices had opacity: 0 at idle (94% of
   the animation cycle), meaning thumbnails caught between bursts
   showed plain 404 text with zero glitch. Now: baseline
   opacity 0.65 with permanent red/cyan offsets so the broken-data
   chromatic split is visible at every animation frame; the burst
   keyframes still amplify the displacement and clip-path
   wobble for the live demo. */

.gt-05__num::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--red);
  clip-path: polygon(0 0, 100% 0, 100% 30%, 0 30%);
  transform: translateX(-5px);
  opacity: 0.65;
  animation: gt-05-top-slice 3s steps(1) infinite;
}

.gt-05__num::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: #00e5ff;
  clip-path: polygon(0 68%, 100% 68%, 100% 100%, 0 100%);
  transform: translateX(5px);
  opacity: 0.65;
  animation: gt-05-bot-slice 3s steps(1) infinite;
  animation-delay: 0.2s;
}

@keyframes gt-05-top-slice {
  0%,
    78%,
    100% {
    transform: translateX(-5px);
    opacity: 0.65;
  }

  80% {
    transform: translateX(-18px);
    opacity: 1;
    clip-path: polygon(0 5%, 100% 5%, 100% 28%, 0 28%);
  }

  82% {
    transform: translateX(12px);
    opacity: 0.9;
    clip-path: polygon(0 0,   100% 0,   100% 22%, 0 22%);
  }

  84% {
    transform: translateX(-8px);
    opacity: 1;
    clip-path: polygon(0 3%,  100% 3%,  100% 30%, 0 30%);
  }

  86% {
    transform: translateX(-5px);
    opacity: 0.65;
  }
}

@keyframes gt-05-bot-slice {
  0%,
    78%,
    100% {
    transform: translateX(5px);
    opacity: 0.65;
  }

  80% {
    transform: translateX(20px);
    opacity: 1;
    clip-path: polygon(0 70%, 100% 70%, 100% 95%,  0 95%);
  }

  82% {
    transform: translateX(-12px);
    opacity: 0.9;
    clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
  }

  84% {
    transform: translateX(9px);
    opacity: 1;
    clip-path: polygon(0 68%, 100% 68%, 100% 92%,  0 92%);
  }

  86% {
    transform: translateX(5px);
    opacity: 0.65;
  }
}
/* Jagged divider lines to simulate broken data */

.gt-05__crack {
  position: absolute;
  left: 0;
  right: 0;
  height: 2px;
  background: rgba(255,45,85,0.6);
  z-index: 2;
}

.gt-05__crack:nth-child(4) {
  top: 32%;
  animation: gt-05-crack 3s steps(1) infinite;
}

.gt-05__crack:nth-child(5) {
  top: 60%;
  animation: gt-05-crack 3s steps(1) infinite;
  animation-delay: 0.2s;
}

@keyframes gt-05-crack {
  0%,
    78%,
    88%,
    100% {
    opacity: 0;
  }

  80%,
    86% {
    opacity: 0.8;
  }
}

.gt-05__msg {
  font-size: 13px;
  letter-spacing: 5px;
  color: var(--dim);
  text-transform: uppercase;
  margin-top: 4px;
}

.gt-05__detail {
  font-size: 12px;
  color: rgba(245,245,250,0.2);
  font-family: 'Courier New', monospace;
  letter-spacing: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .gt-05__corrupt-bar,
    .gt-05__num::before,
    .gt-05__num::after,
    .gt-05__crack {
    animation: none;
    opacity: 0;
  }
}
```
