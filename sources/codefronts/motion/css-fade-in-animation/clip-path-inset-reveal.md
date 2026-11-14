---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/clip-path-inset-reveal/"
title: "Clip-Path Inset Reveal"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A cyberpunk status panel that sweeps into view from left using clip-path: inset(0 100% 0 0 round 16px) animated to inset(0 0% 0 0), revealing content like a…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clip-Path Inset Reveal
Source: https://codefronts.com/motion/css-fade-in-animation/clip-path-inset-reveal/

A cyberpunk status panel that sweeps into view from left using clip-path: inset(0 100% 0 0 round 16px) animated to inset(0 0% 0 0), revealing content like a shutter opening.
## HTML
```html
<div class="fi-02">
  <div class="fi-02__panel">
    <span class="fi-02__label">System Status</span>
    <div class="fi-02__title">Neural Core<br>Online</div>
    <div class="fi-02__bar"></div>
    <p class="fi-02__desc">All subsystems operational. Processing at peak efficiency with zero latency degradation.</p>
    <div class="fi-02__stats">
      <div class="fi-02__stat"><span>99.9%</span><small>Uptime</small></div>
      <div class="fi-02__stat"><span>0.4ms</span><small>Latency</small></div>
      <div class="fi-02__stat"><span>4.2TB</span><small>Processed</small></div>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-02 {
  --bg: #06060f;
  --neon: #00ffe0;
  --neon2: #ff006e;
  --text: #e0fff9;
  font-family: 'Inter',sans-serif;
  min-height: 320px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  padding: 40px;
  overflow: hidden;
  position: relative;
}

.fi-02 *,
.fi-02 *::before,
.fi-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-02 ::selection {
  background: var(--neon);
  color: #000;
}
/* clip-path reveal: inset(0 100% 0 0) → inset(0 0% 0 0) */

.fi-02__panel {
  background: linear-gradient(135deg,rgba(0,255,224,.06),rgba(255,0,110,.06));
  border: 1px solid rgba(0,255,224,.2);
  border-radius: 16px;
  padding: 32px 40px;
  text-align: center;
  max-width: 500px;
  clip-path: inset(0 100% 0 0 round 16px);
  animation: fi-02-clip-reveal .9s cubic-bezier(.77,0,.18,1) .2s forwards;
}

.fi-02__label {
  font-size: .7rem;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: var(--neon);
  margin-bottom: 16px;
  display: block;
}

.fi-02__title {
  font-family: 'Orbitron',monospace;
  font-size: clamp(1.6rem,4vw,2.4rem);
  font-weight: 900;
  color: var(--text);
  margin-bottom: 12px;
  text-shadow: 0 0 20px rgba(0,255,224,.4);
}

.fi-02__bar {
  height: 3px;
  background: linear-gradient(90deg,var(--neon),var(--neon2));
  border-radius: 2px;
  margin: 16px 0;
}

.fi-02__desc {
  font-size: .9rem;
  color: rgba(224,255,249,.6);
  line-height: 1.6;
}

.fi-02__stats {
  display: flex;
  gap: 24px;
  justify-content: center;
  margin-top: 24px;
}

.fi-02__stat span {
  display: block;
  font-family: 'Orbitron',monospace;
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--neon);
}

.fi-02__stat small {
  font-size: .7rem;
  color: rgba(224,255,249,.5);
  text-transform: uppercase;
  letter-spacing: .1em;
}

@keyframes fi-02-clip-reveal {
  to {
    clip-path: inset(0 0% 0 0 round 16px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-02 * {
    animation: none!important;
    clip-path: none!important;
  }
}
```
