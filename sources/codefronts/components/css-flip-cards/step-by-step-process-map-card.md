---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/step-by-step-process-map-card/"
title: "Step-by-Step Process Map Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A four-card grid where each front marks a numbered process step; back outlines execution tasks, deliverables, and time estimates."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Step-by-Step Process Map Card
Source: https://codefronts.com/components/css-flip-cards/step-by-step-process-map-card/

A four-card grid where each front marks a numbered process step; back outlines execution tasks, deliverables, and time estimates.
## HTML
```html
<div class="fc-14">
  <div class="fc-14__grid">
    <!-- Step 01 -->
    <div class="fc-14__scene">
      <div class="fc-14__card">
        <div class="fc-14__front">
          <div class="fc-14__step-num-bg">01</div>
          <div class="fc-14__step-icon">🎯</div>
          <div class="fc-14__step-num">01 · Strategy</div>
          <div class="fc-14__step-title">Define Goals & Scope</div>
          <div class="fc-14__step-hint">Hover for details →</div>
        </div>
        <div class="fc-14__back">
          <div class="fc-14__back-step">Step 01 · Strategy</div>
          <div class="fc-14__back-title">Define Goals & Scope</div>
          <div class="fc-14__task-list">
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Stakeholder interviews & alignment</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>OKR definition & success metrics</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Risk & constraint mapping</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Project charter sign-off</div>
          </div>
          <div class="fc-14__duration">⏱ 1–2 weeks</div>
        </div>
      </div>
    </div>
    <!-- Step 02 -->
    <div class="fc-14__scene">
      <div class="fc-14__card">
        <div class="fc-14__front">
          <div class="fc-14__step-num-bg">02</div>
          <div class="fc-14__step-icon">🔬</div>
          <div class="fc-14__step-num">02 · Research</div>
          <div class="fc-14__step-title">Discover & Validate</div>
          <div class="fc-14__step-hint">Hover for details →</div>
        </div>
        <div class="fc-14__back">
          <div class="fc-14__back-step">Step 02 · Research</div>
          <div class="fc-14__back-title">Discover & Validate</div>
          <div class="fc-14__task-list">
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>User interviews (12+ sessions)</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Competitive analysis matrix</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Journey & persona mapping</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Insights synthesis report</div>
          </div>
          <div class="fc-14__duration">⏱ 2–3 weeks</div>
        </div>
      </div>
    </div>
    <!-- Step 03 -->
    <div class="fc-14__scene">
      <div class="fc-14__card">
        <div class="fc-14__front">
          <div class="fc-14__step-num-bg">03</div>
          <div class="fc-14__step-icon">✏️</div>
          <div class="fc-14__step-num">03 · Design</div>
          <div class="fc-14__step-title">Prototype & Test</div>
          <div class="fc-14__step-hint">Hover for details →</div>
        </div>
        <div class="fc-14__back">
          <div class="fc-14__back-step">Step 03 · Design</div>
          <div class="fc-14__back-title">Prototype & Test</div>
          <div class="fc-14__task-list">
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Information architecture</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Hi-fi Figma prototypes</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Usability test rounds</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Design system tokens</div>
          </div>
          <div class="fc-14__duration">⏱ 3–4 weeks</div>
        </div>
      </div>
    </div>
    <!-- Step 04 -->
    <div class="fc-14__scene">
      <div class="fc-14__card">
        <div class="fc-14__front">
          <div class="fc-14__step-num-bg">04</div>
          <div class="fc-14__step-icon">🚀</div>
          <div class="fc-14__step-num">04 · Launch</div>
          <div class="fc-14__step-title">Ship & Measure</div>
          <div class="fc-14__step-hint">Hover for details →</div>
        </div>
        <div class="fc-14__back">
          <div class="fc-14__back-step">Step 04 · Launch</div>
          <div class="fc-14__back-title">Ship & Measure</div>
          <div class="fc-14__task-list">
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Staged rollout & QA pass</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Analytics instrumentation</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>30/60/90 day OKR review</div>
            <div class="fc-14__task"><span class="fc-14__task-check"><svg viewBox="0 0 10 10"><polyline points="2,5 4,8 8,2"/></svg></span>Retrospective & iteration</div>
          </div>
          <div class="fc-14__duration">⏱ Ongoing</div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-14,
.fc-14 *,
.fc-14 *::before,
.fc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-14 ::selection {
  background: #6366f1;
  color: #fff;
}

.fc-14 {
  --bg: #070710;
  --indigo: #6366f1;
  --sky: #38bdf8;
  --white: #eef2ff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 30%,#0e0e2e,#070710 65%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
  flex-direction: column;
  gap: 20px;
}

.fc-14__grid {
  display: grid;
  grid-template-columns: repeat(4,200px);
  gap: 20px;
}

.fc-14__scene {
  width: 200px;
  height: 280px;
  perspective: 1000px;
  cursor: pointer;
}

.fc-14__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-14__scene:hover .fc-14__card {
  transform: rotateY(180deg);
}

.fc-14__front,
.fc-14__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-14__front {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 24px 16px;
  border: 1px solid rgba(99,102,241,.2);
}

.fc-14__step-num-bg {
  position: absolute;
  bottom: -20px;
  right: -10px;
  font-size: 80px;
  font-weight: 900;
  color: rgba(99,102,241,.07);
  font-style: italic;
  line-height: 1;
  pointer-events: none;
}

.fc-14__step-icon {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  position: relative;
  z-index: 1;
  border: 1px solid rgba(255,255,255,.12);
}

.fc-14__step-num {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  position: relative;
  z-index: 1;
}

.fc-14__step-title {
  font-size: 16px;
  font-weight: 800;
  text-align: center;
  position: relative;
  z-index: 1;
  line-height: 1.3;
}

.fc-14__step-hint {
  font-size: 9px;
  color: rgba(238,242,255,.25);
  letter-spacing: .08em;
  position: absolute;
  bottom: 12px;
  text-align: center;
}
/* BACK */

.fc-14__back {
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 18px 16px;
  gap: 10px;
  border: 1px solid rgba(56,189,248,.2);
  background: linear-gradient(160deg,#0d0d22,#0a1020);
}

.fc-14__back-step {
  font-size: 9px;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 700;
}

.fc-14__back-title {
  font-size: 15px;
  font-weight: 800;
  color: var(--white);
  line-height: 1.2;
}

.fc-14__task-list {
  display: flex;
  flex-direction: column;
  gap: 7px;
  flex: 1;
}

.fc-14__task {
  display: flex;
  align-items: flex-start;
  gap: 7px;
  font-size: 11px;
  color: rgba(238,242,255,.65);
  line-height: 1.4;
}

.fc-14__task-check {
  width: 14px;
  height: 14px;
  border-radius: 4px;
  flex-shrink: 0;
  margin-top: 1px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fc-14__task-check svg {
  width: 9px;
  height: 9px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.5;
}

.fc-14__duration {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 10px;
  color: rgba(238,242,255,.4);
  padding-top: 8px;
  border-top: 1px solid rgba(255,255,255,.06);
}
/* per-step colors */

.fc-14__scene:nth-child(1) .fc-14__front {
  background: linear-gradient(160deg,#0f0f2e,#080820);
}

.fc-14__scene:nth-child(1) .fc-14__step-icon {
  background: rgba(99,102,241,.15);
}

.fc-14__scene:nth-child(1) .fc-14__step-num {
  color: #818cf8;
}

.fc-14__scene:nth-child(1) .fc-14__step-title {
  color: #c7d2fe;
}

.fc-14__scene:nth-child(2) .fc-14__front {
  background: linear-gradient(160deg,#0d1a10,#080e0a);
}

.fc-14__scene:nth-child(2) .fc-14__step-icon {
  background: rgba(34,197,94,.12);
}

.fc-14__scene:nth-child(2) .fc-14__step-num {
  color: #4ade80;
}

.fc-14__scene:nth-child(2) .fc-14__step-title {
  color: #bbf7d0;
}

.fc-14__scene:nth-child(3) .fc-14__front {
  background: linear-gradient(160deg,#1a0d0d,#0e0808);
}

.fc-14__scene:nth-child(3) .fc-14__step-icon {
  background: rgba(249,115,22,.12);
}

.fc-14__scene:nth-child(3) .fc-14__step-num {
  color: #fb923c;
}

.fc-14__scene:nth-child(3) .fc-14__step-title {
  color: #fed7aa;
}

.fc-14__scene:nth-child(4) .fc-14__front {
  background: linear-gradient(160deg,#0d0a20,#080614);
}

.fc-14__scene:nth-child(4) .fc-14__step-icon {
  background: rgba(168,85,247,.12);
}

.fc-14__scene:nth-child(4) .fc-14__step-num {
  color: #c084fc;
}

.fc-14__scene:nth-child(4) .fc-14__step-title {
  color: #e9d5ff;
}

.fc-14__scene:nth-child(1) .fc-14__back-step,
.fc-14__scene:nth-child(1) .fc-14__task-check {
  color: #818cf8;
}

.fc-14__scene:nth-child(2) .fc-14__back-step,
.fc-14__scene:nth-child(2) .fc-14__task-check {
  color: #4ade80;
}

.fc-14__scene:nth-child(3) .fc-14__back-step,
.fc-14__scene:nth-child(3) .fc-14__task-check {
  color: #fb923c;
}

.fc-14__scene:nth-child(4) .fc-14__back-step,
.fc-14__scene:nth-child(4) .fc-14__task-check {
  color: #c084fc;
}

@media (max-width: 900px) {
  .fc-14__grid {
    grid-template-columns: repeat(2,200px);
  }
}

@media (max-width: 480px) {
  .fc-14__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fc-14__card {
    transition: none;
  }
}
```
