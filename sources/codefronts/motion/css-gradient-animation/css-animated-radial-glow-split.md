---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-animated-radial-glow-split/"
title: "CSS Animated Radial Glow Split"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A two-panel feature layout where independently pulsing radial gradient orbs shift position and scale on infinite keyframes, creating atmospheric lighting…"
has_js: "false"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Radial Glow Split
Source: https://codefronts.com/motion/css-gradient-animation/css-animated-radial-glow-split/

A two-panel feature layout where independently pulsing radial gradient orbs shift position and scale on infinite keyframes, creating atmospheric lighting that draws the eye to each side's content.
## HTML
```html
<div class="ga-03">
  <div class="ga-03__glow-a"></div>
  <div class="ga-03__glow-b"></div>
  <div class="ga-03__divider"></div>

  <div class="ga-03__panel ga-03__panel--left">
    <div class="ga-03__tag ga-03__tag--a">
      <span class="ga-03__tag-dot"></span> Infrastructure
    </div>
    <h2 class="ga-03__heading">Edge Network<br>Performance</h2>
    <p class="ga-03__body">Requests routed to the nearest PoP automatically. Sub-10ms response times across 190 regions with zero configuration.</p>
    <div class="ga-03__metric">
      <span class="ga-03__metric-val">9.4ms</span>
      <span class="ga-03__metric-label">Avg. global latency</span>
    </div>
  </div>

  <div class="ga-03__panel ga-03__panel--right">
    <div class="ga-03__tag ga-03__tag--b">
      <span class="ga-03__tag-dot"></span> Analytics
    </div>
    <h2 class="ga-03__heading">Real-Time<br>Intelligence</h2>
    <p class="ga-03__body">Stream millions of events per second into queryable dashboards. No sampling. No delays. Full fidelity at any scale.</p>
    <div class="ga-03__metric">
      <span class="ga-03__metric-val">3.2B</span>
      <span class="ga-03__metric-label">Events processed today</span>
    </div>
  </div>
</div>
```
## CSS
```css
.ga-03,
.ga-03 *,
.ga-03 *::before,
.ga-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-03 ::selection {
  background: rgba(249,115,22,.4);
  color: #fff;
}

.ga-03 {
  --bg: #070d1a;
  --glow-a: #f97316;
  --glow-b: #8b5cf6;
  --dur-a: 7s;
  --dur-b: 9s;
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
}
/* Radial glow A — left, orange */

.ga-03__glow-a {
  position: absolute;
  width: 560px;
  height: 560px;
  border-radius: 50%;
  background: radial-gradient(circle at center,
      color-mix(in srgb, var(--glow-a) 40%, transparent),
      transparent 70%);
  top: 50%;
  left: 0;
  transform: translate(-30%, -50%);
  animation: ga-03-pulse-a var(--dur-a) ease-in-out infinite;
  pointer-events: none;
}

@keyframes ga-03-pulse-a {
  0%,
    100% {
    transform: translate(-30%, -50%) scale(1);
    opacity: .7;
  }

  40% {
    transform: translate(-15%, -60%) scale(1.2);
    opacity: 1;
  }

  70% {
    transform: translate(-40%, -40%) scale(.85);
    opacity: .5;
  }
}
/* Radial glow B — right, violet */

.ga-03__glow-b {
  position: absolute;
  width: 520px;
  height: 520px;
  border-radius: 50%;
  background: radial-gradient(circle at center,
      color-mix(in srgb, var(--glow-b) 40%, transparent),
      transparent 70%);
  top: 50%;
  right: 0;
  transform: translate(30%, -50%);
  animation: ga-03-pulse-b var(--dur-b) ease-in-out infinite;
  pointer-events: none;
}

@keyframes ga-03-pulse-b {
  0%,
    100% {
    transform: translate(30%, -50%) scale(1);
    opacity: .65;
  }

  35% {
    transform: translate(20%, -65%) scale(1.15);
    opacity: .9;
  }

  65% {
    transform: translate(40%, -35%) scale(.9);
    opacity: .5;
  }
}
/* Thin divider */

.ga-03__divider {
  position: absolute;
  left: 50%;
  top: 10%;
  width: 1px;
  height: 80%;
  background: linear-gradient(to bottom,
      transparent, rgba(255,255,255,.1) 30%,
      rgba(255,255,255,.1) 70%, transparent);
  z-index: 1;
}
/* Left panel */

.ga-03__panel {
  position: relative;
  z-index: 2;
  padding: 52px 44px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ga-03__panel--left {
  padding-right: 52px;
}

.ga-03__panel--right {
  padding-left: 52px;
}

.ga-03__tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  width: fit-content;
}

.ga-03__tag--a {
  background: rgba(249,115,22,.12);
  border: 1px solid rgba(249,115,22,.3);
  color: #fb923c;
}

.ga-03__tag--b {
  background: rgba(139,92,246,.12);
  border: 1px solid rgba(139,92,246,.3);
  color: #a78bfa;
}

.ga-03__tag-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: currentColor;
  animation: ga-03-blink 2s ease-in-out infinite;
}

.ga-03__panel--right .ga-03__tag-dot {
  animation-delay: -.8s;
}

@keyframes ga-03-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .3;
  }
}

.ga-03__heading {
  font-size: clamp(1.5rem, 3vw, 2.1rem);
  font-weight: 800;
  line-height: 1.18;
  color: #fff;
  letter-spacing: -.025em;
}

.ga-03__body {
  font-size: .9rem;
  color: rgba(255,255,255,.55);
  line-height: 1.72;
}

.ga-03__metric {
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-top: 8px;
}

.ga-03__metric-val {
  font-size: 2.4rem;
  font-weight: 900;
  color: #fff;
  line-height: 1;
}

.ga-03__panel--left .ga-03__metric-val {
  color: #fb923c;
}

.ga-03__panel--right .ga-03__metric-val {
  color: #a78bfa;
}

.ga-03__metric-label {
  font-size: .75rem;
  font-weight: 600;
  color: rgba(255,255,255,.4);
  text-transform: uppercase;
  letter-spacing: .08em;
}
/* Hover to intensify */

.ga-03:hover .ga-03__glow-a,
.ga-03:hover .ga-03__glow-b {
  opacity: 1 !important;
  filter: blur(0px);
}

@media (max-width: 640px) {
  .ga-03 {
    grid-template-columns: 1fr;
  }

  .ga-03__divider {
    display: none;
  }

  .ga-03__panel--left {
    padding-right: 44px;
  }

  .ga-03__panel--right {
    padding-left: 44px;
    border-top: 1px solid rgba(255,255,255,.07);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ga-03__glow-a,
    .ga-03__glow-b {
    animation: none;
  }

  .ga-03__tag-dot {
    animation: none;
  }
}
```
