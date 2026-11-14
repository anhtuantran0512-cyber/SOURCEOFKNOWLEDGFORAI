---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/responsive-css-grid-flip-card-matrix/"
title: "Responsive CSS Grid Flip Card Matrix"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A six-card portfolio grid that flips on hover, maintains correct 3D perspective at all breakpoints, and reflows from 3 columns to 2 to 1 via CSS Grid."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive CSS Grid Flip Card Matrix
Source: https://codefronts.com/components/css-flip-cards/responsive-css-grid-flip-card-matrix/

A six-card portfolio grid that flips on hover, maintains correct 3D perspective at all breakpoints, and reflows from 3 columns to 2 to 1 via CSS Grid.
## HTML
```html
<div class="fc-18">
  <div class="fc-18__header">
    <h2>Responsive CSS Grid Flip Card Matrix</h2>
    <p>3 columns desktop · 2 tablet · 1 mobile · perspective maintained per card at all breakpoints</p>
  </div>
  <div class="fc-18__grid">
    <!-- 01 -->
    <div class="fc-18__scene">
      <div class="fc-18__card">
        <div class="fc-18__front"><div class="fc-18__project-num">01</div><div class="fc-18__front-tag">Design Systems</div><div class="fc-18__front-icon">🎨</div><div class="fc-18__front-title">Token Architecture</div><div class="fc-18__front-sub">Scalable design token system</div><div class="fc-18__front-hint">Hover for details →</div></div>
        <div class="fc-18__back"><div class="fc-18__back-label">Design Systems</div><div class="fc-18__back-title">Token Architecture</div><div class="fc-18__back-list"><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Semantic color layers</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Typography scale (clamp)</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Multi-brand theming</div></div><button class="fc-18__back-cta">View Project</button></div>
      </div>
    </div>
    <!-- 02 -->
    <div class="fc-18__scene">
      <div class="fc-18__card">
        <div class="fc-18__front"><div class="fc-18__project-num">02</div><div class="fc-18__front-tag">Web Performance</div><div class="fc-18__front-icon">⚡</div><div class="fc-18__front-title">Core Web Vitals</div><div class="fc-18__front-sub">LCP under 1.2s in production</div><div class="fc-18__front-hint">Hover for details →</div></div>
        <div class="fc-18__back"><div class="fc-18__back-label">Web Performance</div><div class="fc-18__back-title">Core Web Vitals</div><div class="fc-18__back-list"><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>LCP: 1.1s (p75)</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>INP: &lt;60ms</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>CLS: 0.01</div></div><button class="fc-18__back-cta">Case Study</button></div>
      </div>
    </div>
    <!-- 03 -->
    <div class="fc-18__scene">
      <div class="fc-18__card">
        <div class="fc-18__front"><div class="fc-18__project-num">03</div><div class="fc-18__front-tag">Accessibility</div><div class="fc-18__front-icon">♿</div><div class="fc-18__front-title">WCAG 2.2 AA Audit</div><div class="fc-18__front-sub">Full accessibility review</div><div class="fc-18__front-hint">Hover for details →</div></div>
        <div class="fc-18__back"><div class="fc-18__back-label">Accessibility</div><div class="fc-18__back-title">WCAG 2.2 AA Audit</div><div class="fc-18__back-list"><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Colour contrast 4.5:1+</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Full keyboard flow</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>ARIA landmark audit</div></div><button class="fc-18__back-cta">Read Report</button></div>
      </div>
    </div>
    <!-- 04 -->
    <div class="fc-18__scene">
      <div class="fc-18__card">
        <div class="fc-18__front"><div class="fc-18__project-num">04</div><div class="fc-18__front-tag">Animation</div><div class="fc-18__front-icon">🎬</div><div class="fc-18__front-title">Motion Library</div><div class="fc-18__front-sub">60fps CSS keyframe suite</div><div class="fc-18__front-hint">Hover for details →</div></div>
        <div class="fc-18__back"><div class="fc-18__back-label">Animation</div><div class="fc-18__back-title">Motion Library</div><div class="fc-18__back-list"><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>48 keyframe demos</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Reduced-motion safe</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Zero JS dependencies</div></div><button class="fc-18__back-cta">Browse Library</button></div>
      </div>
    </div>
    <!-- 05 -->
    <div class="fc-18__scene">
      <div class="fc-18__card">
        <div class="fc-18__front"><div class="fc-18__project-num">05</div><div class="fc-18__front-tag">Architecture</div><div class="fc-18__front-icon">🏗</div><div class="fc-18__front-title">Micro-Frontend</div><div class="fc-18__front-sub">Module federation at scale</div><div class="fc-18__front-hint">Hover for details →</div></div>
        <div class="fc-18__back"><div class="fc-18__back-label">Architecture</div><div class="fc-18__back-title">Micro-Frontend</div><div class="fc-18__back-list"><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Webpack 5 federation</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Shared runtime deps</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>12 independent teams</div></div><button class="fc-18__back-cta">Architecture Docs</button></div>
      </div>
    </div>
    <!-- 06 -->
    <div class="fc-18__scene">
      <div class="fc-18__card">
        <div class="fc-18__front"><div class="fc-18__project-num">06</div><div class="fc-18__front-tag">Testing</div><div class="fc-18__front-icon">🧪</div><div class="fc-18__front-title">E2E Test Suite</div><div class="fc-18__front-sub">Playwright + CI pipeline</div><div class="fc-18__front-hint">Hover for details →</div></div>
        <div class="fc-18__back"><div class="fc-18__back-label">Testing</div><div class="fc-18__back-title">E2E Test Suite</div><div class="fc-18__back-list"><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>98% critical path coverage</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Cross-browser parallel runs</div><div class="fc-18__back-item"><span class="fc-18__back-dot"></span>Visual regression gates</div></div><button class="fc-18__back-cta">View Suite</button></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-18,
.fc-18 *,
.fc-18 *::before,
.fc-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-18 ::selection {
  background: #6366f1;
  color: #fff;
}

.fc-18 {
  --bg: #07080f;
  --indigo: #6366f1;
  --white: #eef2ff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 0%,#0d0f28,#07080f 65%);
  min-height: 100vh;
  padding: 40px 20px 60px;
  color: var(--white);
}

.fc-18__header {
  text-align: center;
  margin-bottom: 36px;
}

.fc-18__header h2 {
  font-size: 20px;
  font-weight: 800;
  color: var(--white);
}

.fc-18__header p {
  font-size: 12px;
  color: rgba(238,242,255,.4);
  margin-top: 6px;
}
/* Responsive grid — 3 cols desktop, 2 tablet, 1 mobile */

.fc-18__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
  max-width: 960px;
  margin: 0 auto;
}
/* Perspective must sit on the individual scene elements, not the grid */

.fc-18__scene {
  height: 260px;
  perspective: 1000px;
  cursor: pointer;
}

.fc-18__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-18__scene:hover .fc-18__card {
  transform: rotateY(180deg);
}

.fc-18__front,
.fc-18__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-18__front {
  display: flex;
  flex-direction: column;
  padding: 24px;
  border: 1px solid rgba(255,255,255,.08);
}

.fc-18__project-num {
  position: absolute;
  top: 16px;
  right: 18px;
  font-size: 32px;
  font-weight: 900;
  opacity: .07;
  font-style: italic;
  line-height: 1;
}

.fc-18__front-tag {
  font-size: 9px;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 10px;
}

.fc-18__front-icon {
  font-size: 28px;
  margin-bottom: 10px;
}

.fc-18__front-title {
  font-size: 17px;
  font-weight: 800;
  color: var(--white);
  line-height: 1.2;
}

.fc-18__front-sub {
  font-size: 12px;
  margin-top: 6px;
  line-height: 1.5;
  opacity: .55;
}

.fc-18__front-hint {
  margin-top: auto;
  font-size: 9px;
  opacity: .25;
  letter-spacing: .08em;
}
/* BACK */

.fc-18__back {
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 20px;
  gap: 10px;
  border: 1px solid rgba(255,255,255,.1);
}

.fc-18__back-label {
  font-size: 9px;
  letter-spacing: .14em;
  text-transform: uppercase;
  font-weight: 700;
}

.fc-18__back-title {
  font-size: 15px;
  font-weight: 800;
  color: var(--white);
  line-height: 1.2;
}

.fc-18__back-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}

.fc-18__back-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  opacity: .7;
}

.fc-18__back-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  flex-shrink: 0;
}

.fc-18__back-cta {
  padding: 10px;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .04em;
  transition: opacity .2s;
}

.fc-18__back-cta:hover {
  opacity: .85;
}
/* Per-card color schemes */
/* 1 — indigo */

.fc-18__scene:nth-child(1) .fc-18__front {
  background: linear-gradient(145deg,#0e0f28,#07080f);
}

.fc-18__scene:nth-child(1) .fc-18__front-tag {
  color: #818cf8;
}

.fc-18__scene:nth-child(1) .fc-18__front-sub {
  color: #c7d2fe;
}

.fc-18__scene:nth-child(1) .fc-18__back {
  background: linear-gradient(145deg,#0d0f26,#090a1a);
}

.fc-18__scene:nth-child(1) .fc-18__back-label {
  color: #818cf8;
}

.fc-18__scene:nth-child(1) .fc-18__back-dot {
  background: #6366f1;
}

.fc-18__scene:nth-child(1) .fc-18__back-cta {
  background: linear-gradient(135deg,#6366f1,#4f46e5);
  color: #fff;
}
/* 2 — emerald */

.fc-18__scene:nth-child(2) .fc-18__front {
  background: linear-gradient(145deg,#071a0e,#04100a);
}

.fc-18__scene:nth-child(2) .fc-18__front-tag {
  color: #4ade80;
}

.fc-18__scene:nth-child(2) .fc-18__front-sub {
  color: #bbf7d0;
}

.fc-18__scene:nth-child(2) .fc-18__back {
  background: linear-gradient(145deg,#071a0e,#030c07);
}

.fc-18__scene:nth-child(2) .fc-18__back-label {
  color: #4ade80;
}

.fc-18__scene:nth-child(2) .fc-18__back-dot {
  background: #22c55e;
}

.fc-18__scene:nth-child(2) .fc-18__back-cta {
  background: linear-gradient(135deg,#22c55e,#16a34a);
  color: #000;
}
/* 3 — rose */

.fc-18__scene:nth-child(3) .fc-18__front {
  background: linear-gradient(145deg,#1a0710,#0e0408);
}

.fc-18__scene:nth-child(3) .fc-18__front-tag {
  color: #fb7185;
}

.fc-18__scene:nth-child(3) .fc-18__front-sub {
  color: #fecdd3;
}

.fc-18__scene:nth-child(3) .fc-18__back {
  background: linear-gradient(145deg,#1a0710,#0a0306);
}

.fc-18__scene:nth-child(3) .fc-18__back-label {
  color: #fb7185;
}

.fc-18__scene:nth-child(3) .fc-18__back-dot {
  background: #f43f5e;
}

.fc-18__scene:nth-child(3) .fc-18__back-cta {
  background: linear-gradient(135deg,#f43f5e,#e11d48);
  color: #fff;
}
/* 4 — amber */

.fc-18__scene:nth-child(4) .fc-18__front {
  background: linear-gradient(145deg,#1a1000,#0e0900);
}

.fc-18__scene:nth-child(4) .fc-18__front-tag {
  color: #fbbf24;
}

.fc-18__scene:nth-child(4) .fc-18__front-sub {
  color: #fde68a;
}

.fc-18__scene:nth-child(4) .fc-18__back {
  background: linear-gradient(145deg,#1a1000,#0a0700);
}

.fc-18__scene:nth-child(4) .fc-18__back-label {
  color: #fbbf24;
}

.fc-18__scene:nth-child(4) .fc-18__back-dot {
  background: #f59e0b;
}

.fc-18__scene:nth-child(4) .fc-18__back-cta {
  background: linear-gradient(135deg,#f59e0b,#d97706);
  color: #000;
}
/* 5 — cyan */

.fc-18__scene:nth-child(5) .fc-18__front {
  background: linear-gradient(145deg,#041618,#020e10);
}

.fc-18__scene:nth-child(5) .fc-18__front-tag {
  color: #22d3ee;
}

.fc-18__scene:nth-child(5) .fc-18__front-sub {
  color: #a5f3fc;
}

.fc-18__scene:nth-child(5) .fc-18__back {
  background: linear-gradient(145deg,#041618,#020c0e);
}

.fc-18__scene:nth-child(5) .fc-18__back-label {
  color: #22d3ee;
}

.fc-18__scene:nth-child(5) .fc-18__back-dot {
  background: #06b6d4;
}

.fc-18__scene:nth-child(5) .fc-18__back-cta {
  background: linear-gradient(135deg,#06b6d4,#0284c7);
  color: #fff;
}
/* 6 — violet */

.fc-18__scene:nth-child(6) .fc-18__front {
  background: linear-gradient(145deg,#120820,#0a0414);
}

.fc-18__scene:nth-child(6) .fc-18__front-tag {
  color: #c084fc;
}

.fc-18__scene:nth-child(6) .fc-18__front-sub {
  color: #e9d5ff;
}

.fc-18__scene:nth-child(6) .fc-18__back {
  background: linear-gradient(145deg,#120820,#08031a);
}

.fc-18__scene:nth-child(6) .fc-18__back-label {
  color: #c084fc;
}

.fc-18__scene:nth-child(6) .fc-18__back-dot {
  background: #a855f7;
}

.fc-18__scene:nth-child(6) .fc-18__back-cta {
  background: linear-gradient(135deg,#a855f7,#7c3aed);
  color: #fff;
}

@media (max-width: 720px) {
  .fc-18__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 480px) {
  .fc-18__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fc-18__card {
    transition: none;
  }
}
```
