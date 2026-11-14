---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/neon-glow-glitch-text/"
title: "Neon Glow Glitch Text"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Vivid hot-pink synthwave lettering with a broad multi-layer text-shadow bloom that pulses between heavy and light glow states, punctuated by a single-frame…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Glitch Text
Source: https://codefronts.com/motion/css-glitch-text-effect/neon-glow-glitch-text/

Vivid hot-pink synthwave lettering with a broad multi-layer text-shadow bloom that pulses between heavy and light glow states, punctuated by a single-frame snap to a crisp thin-blue channel before returning to maximum neon intensity.
## HTML
```html
<div class="gt-10">
  <div class="gt-10__neon" data-text="SYNTHWAVE">SYNTHWAVE</div>
  <div class="gt-10__neon-2">▸ open late — never closed ◂</div>
  <div class="gt-10__sub">Est. 2084 · Neon District</div>
</div>
```
## CSS
```css
.gt-10,
.gt-10 *,
.gt-10 *::before,
.gt-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-10 ::selection {
  background: #ff006e;
  color: #fff;
}

.gt-10 {
  --hot-pink: #ff006e;
  --hot-pink-glow: rgba(255,0,110,0.6);
  --cyan-snap: #00f0ff;
  --synthwave-bg: #0a0010;
  --purple-mid: #6b21a8;
  min-height: 100vh;
  background: var(--synthwave-bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 48px 20px;
  font-family: 'Orbitron', 'Rajdhani', 'Share Tech Mono', monospace;
  position: relative;
  overflow: hidden;
}
/* Synthwave horizon gradient */

.gt-10::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 35%;
  background: linear-gradient(0deg,
      rgba(107,33,168,0.4) 0%,
      transparent 100%
    );
  pointer-events: none;
}
/* Grid floor lines */

.gt-10::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 30%;
  background-image: linear-gradient(0deg, rgba(255,0,110,0.15) 1px, transparent 1px), linear-gradient(90deg, rgba(255,0,110,0.08) 1px, transparent 1px);
  background-size: 40px 20px, 40px 20px;
  perspective: 200px;
  pointer-events: none;
}
/* The big glowing neon text */

.gt-10__neon {
  position: relative;
  font-size: clamp(40px, 9vw, 88px);
  font-weight: 900;
  letter-spacing: 8px;
  text-transform: uppercase;
  color: var(--hot-pink);
  text-shadow: 0 0 7px #fff, 0 0 15px var(--hot-pink), 0 0 35px var(--hot-pink), 0 0 70px var(--hot-pink-glow), 0 0 120px rgba(255,0,110,0.3);
  animation: gt-10-glow-pulse 2.5s ease-in-out infinite alternate;
}

@keyframes gt-10-glow-pulse {
  from {
    text-shadow: 0 0 7px #fff, 0 0 15px var(--hot-pink), 0 0 35px var(--hot-pink), 0 0 70px var(--hot-pink-glow), 0 0 120px rgba(255,0,110,0.3);
  }

  to {
    text-shadow: 0 0 4px #fff, 0 0 10px var(--hot-pink), 0 0 20px var(--hot-pink), 0 0 50px var(--hot-pink-glow), 0 0 90px rgba(255,0,110,0.2);
  }
}
/* Snap-to-thin-blue override */

.gt-10__neon::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  letter-spacing: inherit;
  color: var(--cyan-snap);
  text-shadow: 0 0 4px var(--cyan-snap), 0 0 10px rgba(0,240,255,0.5);
  opacity: 0;
  animation: gt-10-snap 3s steps(1) infinite;
}

@keyframes gt-10-snap {
  0%,
    88%,
    90%,
    100% {
    opacity: 0;
  }

  89% {
    opacity: 1;
  }
}

.gt-10__sub {
  font-size: 11px;
  letter-spacing: 10px;
  color: rgba(255,0,110,0.4);
  text-transform: uppercase;
}
/* Flickering tube letters — neon sign imperfection */

.gt-10__neon-2 {
  font-size: clamp(14px, 2vw, 20px);
  letter-spacing: 6px;
  color: var(--cyan-snap);
  text-shadow: 0 0 8px var(--cyan-snap), 0 0 20px rgba(0,240,255,0.4);
  animation: gt-10-tube-flicker 6s steps(1) infinite;
  text-transform: uppercase;
}

@keyframes gt-10-tube-flicker {
  0%,
    60%,
    62%,
    64%,
    70%,
    100% {
    opacity: 1;
  }

  61%,
    63% {
    opacity: 0.2;
  }

  65%,
    69% {
    opacity: 0.6;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-10__neon,
    .gt-10__neon::before,
    .gt-10__neon-2 {
    animation: none;
  }

  .gt-10__neon::before {
    opacity: 0;
  }
}
```
