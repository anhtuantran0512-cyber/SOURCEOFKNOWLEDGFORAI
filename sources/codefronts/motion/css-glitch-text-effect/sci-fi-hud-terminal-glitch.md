---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/sci-fi-hud-terminal-glitch/"
title: "Sci-Fi HUD Terminal Glitch"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Amber CRT-monitor aesthetic wrapped in a corner-bracketed HUD panel, with a failing-hardware opacity flicker on the headline, a blinking cursor, and animated…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sci-Fi HUD Terminal Glitch
Source: https://codefronts.com/motion/css-glitch-text-effect/sci-fi-hud-terminal-glitch/

Amber CRT-monitor aesthetic wrapped in a corner-bracketed HUD panel, with a failing-hardware opacity flicker on the headline, a blinking cursor, and animated data readout bars.
## HTML
```html
<div class="gt-07">
  <div class="gt-07__hud">
    <div class="gt-07__header">
      <span class="gt-07__sys">SYS·HUD·v9.4.1</span>
      <div class="gt-07__status-dot"></div>
    </div>
    <div class="gt-07__main-wrap">
      <span class="gt-07__main">NEURAL LINK</span><span class="gt-07__cursor"></span>
    </div>
    <div class="gt-07__lines">
      <div class="gt-07__line"><span>UPLINK FREQ</span><span class="gt-07__line-val">847.3 THz</span></div>
      <div class="gt-07__line"><span>LATENCY</span><span class="gt-07__line-val">0.4 ms</span></div>
      <div class="gt-07__line"><span>INTEGRITY</span><span class="gt-07__line-val">99.7%</span></div>
    </div>
    <div class="gt-07__bar-wrap">
      <div class="gt-07__bar-fill"></div>
    </div>
  </div>
</div>
```
## CSS
```css
.gt-07,
.gt-07 *,
.gt-07 *::before,
.gt-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-07 ::selection {
  background: #f59e0b;
  color: #000;
}

.gt-07 {
  --amber: #f59e0b;
  --amber-dim: #92400e;
  --amber-glow: rgba(245,158,11,0.15);
  --bg: #080603;
  --grid: rgba(245,158,11,0.06);
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  font-family: 'Courier New', monospace;
  position: relative;
  overflow: hidden;
}
/* CRT grid */

.gt-07::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 30px 30px;
  pointer-events: none;
}
/* Corner HUD decorations */

.gt-07__hud {
  position: relative;
  width: 100%;
  max-width: 540px;
  padding: 32px 28px;
  border: 1px solid rgba(245,158,11,0.25);
  border-radius: 4px;
  box-shadow: 0 0 40px var(--amber-glow), inset 0 0 30px rgba(0,0,0,0.5);
}
/* Corner brackets */

.gt-07__hud::before,
.gt-07__hud::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  border-color: var(--amber);
  border-style: solid;
}

.gt-07__hud::before {
  top: -1px;
  left: -1px;
  border-width: 2px 0 0 2px;
}

.gt-07__hud::after {
  bottom: -1px;
  right: -1px;
  border-width: 0 2px 2px 0;
}

.gt-07__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(245,158,11,0.15);
}

.gt-07__sys {
  font-size: 10px;
  color: var(--amber);
  letter-spacing: 3px;
  opacity: 0.7;
}

.gt-07__status-dot {
  width: 6px;
  height: 6px;
  background: var(--amber);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--amber);
  animation: gt-07-status-blink 3s steps(1) infinite;
}

@keyframes gt-07-status-blink {
  0%,
    80%,
    84%,
    88%,
    100% {
    opacity: 1;
  }

  82%,
    86% {
    opacity: 0;
  }
}
/* Main glitch text with CRT flicker */

.gt-07__main {
  font-size: clamp(30px, 5vw, 52px);
  font-weight: 700;
  color: var(--amber);
  text-shadow: 0 0 10px var(--amber), 0 0 30px rgba(245,158,11,0.5);
  letter-spacing: 6px;
  text-transform: uppercase;
  animation: gt-07-crt-flicker 0.15s steps(1) infinite;
}

@keyframes gt-07-crt-flicker {
  0% {
    opacity: 1;
  }

  50% {
    opacity: 0.97;
  }

  75% {
    opacity: 1;
  }
  /* Occasional hard blink */
}
/* Separate big-flicker overlay */

.gt-07__main-wrap {
  position: relative;
  animation: gt-07-big-flicker 5s steps(1) infinite;
}

@keyframes gt-07-big-flicker {
  0%,
    90%,
    92%,
    94%,
    100% {
    opacity: 1;
  }

  91%,
    93% {
    opacity: 0.3;
  }
}
/* Blinking cursor after text */

.gt-07__cursor {
  display: inline-block;
  width: 0.55em;
  height: 1em;
  background: var(--amber);
  margin-left: 4px;
  vertical-align: bottom;
  box-shadow: 0 0 8px var(--amber);
  animation: gt-07-cur 1s steps(1) infinite;
}

@keyframes gt-07-cur {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}
/* Readout lines */

.gt-07__lines {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.gt-07__line {
  font-size: 11px;
  color: rgba(245,158,11,0.5);
  letter-spacing: 1px;
  display: flex;
  justify-content: space-between;
}

.gt-07__line-val {
  color: rgba(245,158,11,0.8);
  animation: gt-07-val-shift 2s linear infinite;
}

@keyframes gt-07-val-shift {
  0%,
    89%,
    100% {
    opacity: 1;
  }

  90% {
    opacity: 0.4;
  }
}

.gt-07__bar-wrap {
  margin-top: 16px;
  height: 3px;
  background: rgba(245,158,11,0.12);
  border-radius: 2px;
  overflow: hidden;
}

.gt-07__bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--amber-dim), var(--amber));
  box-shadow: 0 0 8px var(--amber);
  animation: gt-07-bar-scan 3s linear infinite;
}

@keyframes gt-07-bar-scan {
  0% {
    width: 0%;
  }

  85% {
    width: 100%;
  }

  100% {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-07__main,
    .gt-07__main-wrap,
    .gt-07__cursor,
    .gt-07__status-dot,
    .gt-07__line-val,
    .gt-07__bar-fill {
    animation: none;
  }
}
```
