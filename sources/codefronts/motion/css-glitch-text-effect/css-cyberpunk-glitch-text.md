---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/css-cyberpunk-glitch-text/"
title: "CSS Cyberpunk Glitch Text"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Neon pink and cyan RGB-channel split glitch over a deep dark background, with clip-path horizontal slice displacement that fires at asymmetric intervals on…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Cyberpunk Glitch Text
Source: https://codefronts.com/motion/css-glitch-text-effect/css-cyberpunk-glitch-text/

Neon pink and cyan RGB-channel split glitch over a deep dark background, with clip-path horizontal slice displacement that fires at asymmetric intervals on an Orbitron-style headline.
## HTML
```html
<div class="gt-01">
  <span class="gt-01__label">// system_breach_detected</span>
  <div class="gt-01__glitch" data-text="CYBERP∪NK">CYBERP∪NK</div>
  <div class="gt-01__bar"></div>
  <span class="gt-01__sub">Neural net v2.7.1 — online</span>
</div>
```
## CSS
```css
.gt-01,
.gt-01 *,
.gt-01 *::before,
.gt-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-01 ::selection {
  background: #ff0090;
  color: #000;
}

.gt-01 {
  --neon-pink: #ff0090;
  --neon-cyan: #00f5ff;
  --bg: #050515;
  --text-col: #e0e0ff;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 32px;
  padding: 40px 20px;
  font-family: 'Orbitron', 'Rajdhani', 'Share Tech Mono', monospace;
  position: relative;
  overflow: hidden;
}
/* Scanline overlay */

.gt-01::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,245,255,0.03) 2px,
      rgba(0,245,255,0.03) 4px
    );
  pointer-events: none;
  z-index: 10;
}

.gt-01__label {
  font-size: 11px;
  letter-spacing: 4px;
  color: var(--neon-cyan);
  opacity: 0.6;
  text-transform: uppercase;
}

.gt-01__glitch {
  position: relative;
  font-size: clamp(42px, 8vw, 80px);
  font-weight: 900;
  letter-spacing: 6px;
  text-transform: uppercase;
  color: var(--text-col);
  text-shadow: 0 0 10px rgba(255,0,144,0.8), 0 0 30px rgba(255,0,144,0.4), 0 0 60px rgba(255,0,144,0.2);
  animation: gt-01-flicker 4s infinite;
}

.gt-01__glitch::before,
.gt-01__glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  letter-spacing: inherit;
}
/* Pink channel — clips top slices */

.gt-01__glitch::before {
  color: var(--neon-pink);
  text-shadow: none;
  clip-path: polygon(0 0, 100% 0, 100% 33%, 0 33%);
  animation: gt-01-slice-top 2.5s steps(1) infinite;
  left: 3px;
}
/* Cyan channel — clips bottom slices */

.gt-01__glitch::after {
  color: var(--neon-cyan);
  text-shadow: none;
  clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  animation: gt-01-slice-bot 2.5s steps(1) infinite;
  left: -3px;
}

@keyframes gt-01-flicker {
  0%,
    94%,
    96%,
    100% {
    opacity: 1;
  }

  95% {
    opacity: 0.6;
  }
}

@keyframes gt-01-slice-top {
  0% {
    transform: translateX(0);
    clip-path: polygon(0 0,   100% 0,   100% 33%,  0 33%);
  }

  5% {
    transform: translateX(-8px);
    clip-path: polygon(0 10%, 100% 10%, 100% 28%, 0 28%);
  }

  10% {
    transform: translateX(6px);
    clip-path: polygon(0 5%,  100% 5%,  100% 20%, 0 20%);
  }

  15% {
    transform: translateX(0);
    clip-path: polygon(0 0,   100% 0,   100% 33%,  0 33%);
  }

  40% {
    transform: translateX(0);
    clip-path: polygon(0 0,   100% 0,   100% 33%,  0 33%);
  }

  42% {
    transform: translateX(10px);
    clip-path: polygon(0 15%, 100% 15%, 100% 35%, 0 35%);
  }

  44% {
    transform: translateX(-5px);
    clip-path: polygon(0 8%,  100% 8%,  100% 25%, 0 25%);
  }

  46% {
    transform: translateX(0);
    clip-path: polygon(0 0,   100% 0,   100% 33%,  0 33%);
  }

  100% {
    transform: translateX(0);
    clip-path: polygon(0 0,   100% 0,   100% 33%,  0 33%);
  }
}

@keyframes gt-01-slice-bot {
  0% {
    transform: translateX(0);
    clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  }

  5% {
    transform: translateX(8px);
    clip-path: polygon(0 65%, 100% 65%, 100% 90%,  0 90%);
  }

  10% {
    transform: translateX(-6px);
    clip-path: polygon(0 55%, 100% 55%, 100% 80%,  0 80%);
  }

  15% {
    transform: translateX(0);
    clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  }

  40% {
    transform: translateX(0);
    clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  }

  42% {
    transform: translateX(-10px);
    clip-path: polygon(0 70%, 100% 70%, 100% 95%,  0 95%);
  }

  44% {
    transform: translateX(4px);
    clip-path: polygon(0 58%, 100% 58%, 100% 85%,  0 85%);
  }

  46% {
    transform: translateX(0);
    clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  }

  100% {
    transform: translateX(0);
    clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  }
}
/* Glitch bar decoration */

.gt-01__bar {
  width: 200px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--neon-cyan), var(--neon-pink), transparent);
  animation: gt-01-bar 3s linear infinite;
}

@keyframes gt-01-bar {
  0% {
    transform: scaleX(0.3) translateX(-100%);
    opacity: 0;
  }

  50% {
    transform: scaleX(1) translateX(0%);
    opacity: 1;
  }

  100% {
    transform: scaleX(0.3) translateX(100%);
    opacity: 0;
  }
}

.gt-01__sub {
  font-size: 12px;
  letter-spacing: 8px;
  color: rgba(224,224,255,0.4);
  text-transform: uppercase;
}

@media (prefers-reduced-motion: reduce) {
  .gt-01__glitch,
    .gt-01__glitch::before,
    .gt-01__glitch::after,
    .gt-01__bar {
    animation: none;
  }

  .gt-01__glitch::before {
    left: 0;
  }

  .gt-01__glitch::after {
    left: 0;
  }
}
```
