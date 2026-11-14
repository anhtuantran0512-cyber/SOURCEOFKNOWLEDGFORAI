---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/retro-vhs-scanline-glitch/"
title: "Retro VHS Scanline Glitch"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Analog VHS tape aesthetic with drifting transparent scanlines, a slow upward tracking line, chunky serif headline with purple-magenta text-shadow jitter, and…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro VHS Scanline Glitch
Source: https://codefronts.com/motion/css-glitch-text-effect/retro-vhs-scanline-glitch/

Analog VHS tape aesthetic with drifting transparent scanlines, a slow upward tracking line, chunky serif headline with purple-magenta text-shadow jitter, and an authentic REC indicator.
## HTML
```html
<div class="gt-03">
  <div class="gt-03__tape">
    <div class="gt-03__scanlines"></div>
    <div class="gt-03__track"></div>
    <span class="gt-03__timestamp">00:47:22:14</span>
    <div class="gt-03__rec"><div class="gt-03__rec-dot"></div>REC</div>
    <h1 class="gt-03__title">VHS STATIC</h1>
    <span class="gt-03__sub">rewind to remember</span>
    <span class="gt-03__speed">SP · HI-FI · STEREO</span>
  </div>
</div>
```
## CSS
```css
.gt-03,
.gt-03 *,
.gt-03 *::before,
.gt-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-03 ::selection {
  background: #b45bd4;
  color: #fff;
}

.gt-03 {
  --magenta: #e040fb;
  --purple: #7b2d8b;
  --light-purple: #ce93d8;
  --tape-bg: #12091a;
  --screen-glow: rgba(180,91,212,0.15);
  min-height: 100vh;
  background: var(--tape-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  font-family: Georgia, 'Times New Roman', serif;
  position: relative;
  overflow: hidden;
}
/* Ambient glow */

.gt-03::before {
  content: '';
  position: absolute;
  width: 400px;
  height: 200px;
  background: radial-gradient(ellipse, var(--screen-glow) 0%, transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

.gt-03__tape {
  position: relative;
  width: 100%;
  max-width: 480px;
  aspect-ratio: 4/3;
  background: #0d0613;
  border: 2px solid rgba(180,91,212,0.3);
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 0 0 30px rgba(180,91,212,0.2), inset 0 0 40px rgba(0,0,0,0.6);
}
/* Moving scanlines */

.gt-03__scanlines {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      0deg,
      rgba(0,0,0,0.18) 0px,
      rgba(0,0,0,0.18) 1px,
      transparent 1px,
      transparent 3px
    );
  animation: gt-03-scan-drift 8s linear infinite;
  pointer-events: none;
  z-index: 5;
}

@keyframes gt-03-scan-drift {
  from {
    background-position: 0 0;
  }

  to {
    background-position: 0 60px;
  }
}
/* Tracking line that drifts up */

.gt-03__track {
  position: absolute;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, transparent 0%, rgba(228,64,251,0.6) 20%, rgba(255,255,255,0.4) 50%, rgba(228,64,251,0.6) 80%, transparent 100%);
  filter: blur(1px);
  animation: gt-03-track-move 5s linear infinite;
  z-index: 6;
}

@keyframes gt-03-track-move {
  from {
    top: 110%;
  }

  to {
    top: -10%;
  }
}
/* Corner timestamp */

.gt-03__timestamp {
  position: absolute;
  top: 12px;
  left: 14px;
  font-family: 'Courier New', monospace;
  font-size: 11px;
  color: var(--magenta);
  opacity: 0.7;
  letter-spacing: 1px;
  animation: gt-03-blink 2s steps(1) infinite;
  z-index: 8;
}

@keyframes gt-03-blink {
  0%,
    49% {
    opacity: 0.7;
  }

  50%,
    100% {
    opacity: 0;
  }
}
/* REC badge */

.gt-03__rec {
  position: absolute;
  top: 12px;
  right: 14px;
  font-family: 'Courier New', monospace;
  font-size: 11px;
  color: #ff4444;
  letter-spacing: 2px;
  display: flex;
  align-items: center;
  gap: 5px;
  z-index: 8;
}

.gt-03__rec-dot {
  width: 7px;
  height: 7px;
  background: #ff4444;
  border-radius: 50%;
  animation: gt-03-blink 1s steps(1) infinite;
}
/* Main text */

.gt-03__title {
  font-size: clamp(32px, 6vw, 60px);
  font-weight: 700;
  color: var(--light-purple);
  text-align: center;
  text-shadow: 2px 0 var(--magenta), -2px 0 rgba(0,255,255,0.5), 0 0 20px rgba(180,91,212,0.6);
  position: relative;
  z-index: 4;
  animation: gt-03-jitter 6s steps(1) infinite;
  letter-spacing: 3px;
}
/* Horizontal tracking jitter */

@keyframes gt-03-jitter {
  0%,
    90%,
    100% {
    transform: translateX(0);
    text-shadow: 2px 0 var(--magenta), -2px 0 rgba(0,255,255,0.5), 0 0 20px rgba(180,91,212,0.6);
  }

  92% {
    transform: translateX(-6px);
    text-shadow: 6px 0 var(--magenta), -6px 0 rgba(0,255,255,0.7);
  }

  94% {
    transform: translateX(4px);
    text-shadow: -4px 0 var(--magenta), 4px 0 rgba(0,255,255,0.7);
  }

  96% {
    transform: translateX(-2px);
  }

  98% {
    transform: translateX(0);
  }
}

.gt-03__sub {
  font-family: 'Courier New', monospace;
  font-size: 12px;
  color: rgba(206,147,216,0.5);
  letter-spacing: 5px;
  text-transform: uppercase;
  margin-top: 12px;
  position: relative;
  z-index: 4;
}
/* Tape speed indicator */

.gt-03__speed {
  position: absolute;
  bottom: 10px;
  left: 14px;
  font-family: 'Courier New', monospace;
  font-size: 10px;
  color: rgba(206,147,216,0.4);
  z-index: 8;
  letter-spacing: 1px;
}

@media (prefers-reduced-motion: reduce) {
  .gt-03__scanlines,
    .gt-03__track,
    .gt-03__timestamp,
    .gt-03__rec-dot,
    .gt-03__title {
    animation: none;
  }
}
```
