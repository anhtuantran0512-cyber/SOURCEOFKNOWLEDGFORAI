---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-morphing-progress-steps-animation/"
title: "CSS Morphing Progress Steps Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Four animated progress step UI patterns: horizontal step track, radial ring steps, morphing pill steps and animated vertical timeline — all scoped CSS…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Morphing Progress Steps Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-morphing-progress-steps-animation/

Four animated progress step UI patterns: horizontal step track, radial ring steps, morphing pill steps and animated vertical timeline — all scoped CSS keyframes.
## HTML
```html
<div class="kf-29">
  <h2>CSS Morphing Progress Steps</h2>

  <!-- Horizontal steps -->
  <div class="h-steps">
    <div class="step-track">
      <div class="step-node done">
        <div class="node-circle">✓</div>
        <div class="node-label">Account</div>
      </div>
      <div class="step-line done"></div>
      <div class="step-node done">
        <div class="node-circle">✓</div>
        <div class="node-label">Profile</div>
      </div>
      <div class="step-line active"></div>
      <div class="step-node active">
        <div class="node-circle">3</div>
        <div class="node-label">Payment</div>
      </div>
      <div class="step-line pending"></div>
      <div class="step-node pending">
        <div class="node-circle">4</div>
        <div class="node-label">Review</div>
      </div>
      <div class="step-line pending"></div>
      <div class="step-node pending">
        <div class="node-circle">5</div>
        <div class="node-label">Launch</div>
      </div>
    </div>
  </div>

  <!-- Radial rings -->
  <div class="radial-steps">
    <div class="radial-step">
      <div class="radial-ring">
        <svg viewBox="0 0 80 80"><circle class="ring-bg" cx="40" cy="40" r="35"/><circle class="ring-fill s1" cx="40" cy="40" r="35"/></svg>
        <div class="ring-icon">📦</div>
      </div>
      <label>Order</label>
    </div>
    <div class="radial-step">
      <div class="radial-ring">
        <svg viewBox="0 0 80 80"><circle class="ring-bg" cx="40" cy="40" r="35"/><circle class="ring-fill s2" cx="40" cy="40" r="35"/></svg>
        <div class="ring-icon">🚚</div>
      </div>
      <label>Shipped</label>
    </div>
    <div class="radial-step">
      <div class="radial-ring">
        <svg viewBox="0 0 80 80"><circle class="ring-bg" cx="40" cy="40" r="35"/><circle class="ring-fill s3" cx="40" cy="40" r="35"/></svg>
        <div class="ring-icon">🗺️</div>
      </div>
      <label>Transit</label>
    </div>
    <div class="radial-step">
      <div class="radial-ring">
        <svg viewBox="0 0 80 80"><circle class="ring-bg" cx="40" cy="40" r="35"/><circle class="ring-fill s4" cx="40" cy="40" r="35"/></svg>
        <div class="ring-icon">📬</div>
      </div>
      <label>Deliver</label>
    </div>
  </div>

  <!-- Pill steps -->
  <div class="pill-steps">
    <div class="pill done-p"><span class="pill-dot"></span>Set up</div>
    <div class="pill done-p"><span class="pill-dot"></span>Design</div>
    <div class="pill active-p"><span class="pill-dot"></span>Build</div>
    <div class="pill pending-p"><span class="pill-dot"></span>Review</div>
    <div class="pill pending-p"><span class="pill-dot"></span>Deploy</div>
  </div>

  <!-- Vertical timeline -->
  <div class="v-steps">
    <div class="v-step done">
      <div class="v-step-left">
        <div class="v-dot">✓</div>
        <div class="v-connector"></div>
      </div>
      <div class="v-step-right">
        <h4>Requirements Gathered</h4>
        <p>All project requirements documented and approved.</p>
      </div>
    </div>
    <div class="v-step done">
      <div class="v-step-left">
        <div class="v-dot">✓</div>
        <div class="v-connector"></div>
      </div>
      <div class="v-step-right">
        <h4>Design Approved</h4>
        <p>Wireframes and visual design signed off by stakeholders.</p>
      </div>
    </div>
    <div class="v-step active-v">
      <div class="v-step-left">
        <div class="v-dot">●</div>
        <div class="v-connector"></div>
      </div>
      <div class="v-step-right">
        <h4>Development in Progress</h4>
        <p>Frontend and backend implementation underway.</p>
      </div>
    </div>
    <div class="v-step pend">
      <div class="v-step-left">
        <div class="v-dot">4</div>
        <div class="v-connector"></div>
      </div>
      <div class="v-step-right">
        <h4>QA Testing</h4>
        <p>Automated and manual testing pipeline.</p>
      </div>
    </div>
    <div class="v-step pend">
      <div class="v-step-left">
        <div class="v-dot">5</div>
      </div>
      <div class="v-step-right">
        <h4>Production Launch</h4>
        <p>Deploy to production and monitor.</p>
      </div>
    </div>
  </div>

</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.kf-29 *,
.kf-29 *::before,
.kf-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-29 {
  font-family: 'Inter', sans-serif;
  background: #09090f;
  color: #fff;
  padding: 48px 24px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}

.kf-29 h2 {
  font-size: 1rem;
  color: #444;
  letter-spacing: 3px;
  text-transform: uppercase;
}
/* ── 1: Horizontal step progress ── */

.kf-29 .h-steps {
  width: 100%;
  max-width: 700px;
}

.kf-29 .step-track {
  display: flex;
  align-items: center;
  position: relative;
}

.kf-29 .step-node {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  z-index: 2;
}

.kf-29 .node-circle {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  font-weight: 600;
  position: relative;
  transition: all 0.3s;
}

.kf-29 .node-label {
  font-size: 0.72rem;
  color: #555;
  letter-spacing: 0.5px;
  text-align: center;
  max-width: 80px;
}

.kf-29 .step-line {
  flex: 1;
  height: 3px;
  background: #1e1e2a;
  position: relative;
  margin: 0 -2px;
  margin-bottom: 28px;
}

.kf-29 .step-line::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  border-radius: 2px;
}
/* Completed step */

.kf-29 .step-node.done .node-circle {
  background: #7c6af7;
  color: #fff;
  box-shadow: 0 0 0 0 rgba(124,106,247,0.4);
  animation: kf-29-nodeshine 3s ease-in-out infinite;
}

@keyframes kf-29-nodeshine {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(124,106,247,0.4);
  }

  50% {
    box-shadow: 0 0 0 8px rgba(124,106,247,0);
  }
}

.kf-29 .step-node.done .node-label {
  color: #7c6af7;
}
/* Active step */

.kf-29 .step-node.active .node-circle {
  background: transparent;
  border: 3px solid #7c6af7;
  color: #7c6af7;
  animation: kf-29-activepulse 1.5s ease-in-out infinite;
}

@keyframes kf-29-activepulse {
  0%,
    100% {
    border-color: #7c6af7;
    box-shadow: 0 0 0 0 rgba(124,106,247,0.5);
  }

  50% {
    border-color: #a898fc;
    box-shadow: 0 0 0 6px rgba(124,106,247,0);
  }
}

.kf-29 .step-node.active .node-label {
  color: #ccc;
}
/* Pending step */

.kf-29 .step-node.pending .node-circle {
  background: #151525;
  border: 2px solid #2a2a40;
  color: #444;
}
/* Line fills */

.kf-29 .step-line.done::after {
  background: #7c6af7;
  width: 100%;
}

.kf-29 .step-line.active::after {
  background: linear-gradient(90deg, #7c6af7, #b8acff);
  animation: kf-29-linefill 2s ease-in-out infinite alternate;
}

@keyframes kf-29-linefill {
  0% {
    width: 30%;
  }

  100% {
    width: 85%;
  }
}

.kf-29 .step-line.pending::after {
  width: 0;
}
/* ── 2: Circular / radial progress ── */

.kf-29 .radial-steps {
  display: flex;
  gap: 32px;
  flex-wrap: wrap;
  justify-content: center;
}

.kf-29 .radial-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.kf-29 .radial-ring {
  position: relative;
  width: 80px;
  height: 80px;
}

.kf-29 .radial-ring svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.kf-29 .ring-bg {
  fill: none;
  stroke: #1e1e30;
  stroke-width: 6;
}

.kf-29 .ring-fill {
  fill: none;
  stroke-width: 6;
  stroke-linecap: round;
  stroke-dasharray: 220;
}

.kf-29 .ring-fill.s1 {
  stroke: #7c6af7;
  stroke-dashoffset: 0;
  animation: kf-29-ring1 3s ease-in-out infinite;
}

.kf-29 .ring-fill.s2 {
  stroke: #00d4ff;
  stroke-dashoffset: 55;
  animation: kf-29-ring2 3s ease-in-out infinite;
}

.kf-29 .ring-fill.s3 {
  stroke: #ff6b35;
  stroke-dashoffset: 110;
  animation: kf-29-ring3 3s ease-in-out infinite;
}

.kf-29 .ring-fill.s4 {
  stroke: #f7c948;
  stroke-dashoffset: 165;
  animation: kf-29-ring4 3s ease-in-out infinite;
}

@keyframes kf-29-ring1 {
  0%,
    100% {
    stroke-dashoffset: 0;
  }

  50% {
    stroke-dashoffset: -10;
  }
}

@keyframes kf-29-ring2 {
  0%,
    100% {
    stroke-dashoffset: 55;
  }

  50% {
    stroke-dashoffset: 45;
  }
}

@keyframes kf-29-ring3 {
  0%,
    100% {
    stroke-dashoffset: 110;
  }

  50% {
    stroke-dashoffset: 90;
  }
}

@keyframes kf-29-ring4 {
  0%,
    100% {
    stroke-dashoffset: 165;
  }

  50% {
    stroke-dashoffset: 155;
  }
}

.kf-29 .ring-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.2rem;
}

.kf-29 .radial-step label {
  font-size: 0.7rem;
  color: #555;
  letter-spacing: 1px;
  text-align: center;
  text-transform: uppercase;
}
/* ── 3: Morphing pill steps ── */

.kf-29 .pill-steps {
  display: flex;
  gap: 8px;
  align-items: center;
}

.kf-29 .pill {
  height: 36px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 0.8rem;
  font-weight: 500;
  overflow: hidden;
  white-space: nowrap;
  transition: all 0.4s;
}

.kf-29 .pill.done-p {
  background: rgba(124,106,247,0.15);
  border: 1px solid #7c6af7;
  color: #7c6af7;
  padding: 0 16px;
  animation: kf-29-pilldone 4s ease infinite;
}

.kf-29 .pill.active-p {
  background: #7c6af7;
  color: #fff;
  padding: 0 20px;
  animation: kf-29-pillactive 4s ease infinite;
  box-shadow: 0 4px 20px rgba(124,106,247,0.4);
}

.kf-29 .pill.pending-p {
  background: #111125;
  border: 1px solid #1e1e35;
  color: #444;
  padding: 0 14px;
  animation: kf-29-pillpending 4s ease infinite;
}

@keyframes kf-29-pilldone {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(0.98);
  }
}

@keyframes kf-29-pillactive {
  0%,
    100% {
    box-shadow: 0 4px 20px rgba(124,106,247,0.4);
    transform: scale(1);
  }

  50% {
    box-shadow: 0 6px 30px rgba(124,106,247,0.6);
    transform: scale(1.03);
  }
}

@keyframes kf-29-pillpending {
  0%,
    100% {
    opacity: 0.6;
  }

  50% {
    opacity: 0.8;
  }
}

.kf-29 .pill-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  flex-shrink: 0;
}
/* ── 4: Vertical timeline steps ── */

.kf-29 .v-steps {
  display: flex;
  flex-direction: column;
  gap: 0;
  position: relative;
  width: 100%;
  max-width: 440px;
}

.kf-29 .v-step {
  display: flex;
  gap: 20px;
  position: relative;
}

.kf-29 .v-step-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 40px;
  flex-shrink: 0;
}

.kf-29 .v-dot {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  flex-shrink: 0;
  z-index: 2;
}

.kf-29 .v-connector {
  width: 2px;
  flex: 1;
  min-height: 32px;
  margin: 2px 0;
}

.kf-29 .v-step-right {
  padding: 4px 0 32px;
}

.kf-29 .v-step-right h4 {
  font-size: 0.9rem;
  font-weight: 600;
  color: #ccc;
  margin-bottom: 4px;
}

.kf-29 .v-step-right p {
  font-size: 0.78rem;
  color: #555;
  line-height: 1.5;
}
/* done */

.kf-29 .v-step.done .v-dot {
  background: #7c6af7;
  color: #fff;
  animation: kf-29-vdoneshine 3s ease-in-out infinite;
}

@keyframes kf-29-vdoneshine {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(124,106,247,0.4);
  }

  50% {
    box-shadow: 0 0 0 6px rgba(124,106,247,0);
  }
}

.kf-29 .v-step.done .v-connector {
  background: linear-gradient(180deg, #7c6af7, #a898fc);
}

.kf-29 .v-step.done .v-step-right h4 {
  color: #fff;
}
/* active */

.kf-29 .v-step.active-v .v-dot {
  background: transparent;
  border: 3px solid #7c6af7;
  color: #7c6af7;
  animation: kf-29-activepulse 1.5s ease-in-out infinite;
}

.kf-29 .v-step.active-v .v-connector {
  background: linear-gradient(180deg, #a898fc, transparent);
  animation: kf-29-vline 2s ease infinite alternate;
}

@keyframes kf-29-vline {
  0% {
    opacity: 0.4;
  }

  100% {
    opacity: 1;
  }
}
/* pending */

.kf-29 .v-step.pend .v-dot {
  background: #111120;
  border: 2px solid #1e1e30;
  color: #333;
}

.kf-29 .v-step.pend .v-connector {
  background: #1a1a28;
}

.kf-29 .v-step.pend .v-step-right h4 {
  color: #444;
}

@media (prefers-reduced-motion: reduce) {
  .kf-29 .node-circle,
    .kf-29 .step-line.active::after,
    .kf-29 .ring-fill,
    .kf-29 .pill,
    .kf-29 .v-dot,
    .kf-29 .v-connector {
    animation: none;
  }

  .kf-29 .step-line.active::after {
    width: 60%;
  }
}
```
