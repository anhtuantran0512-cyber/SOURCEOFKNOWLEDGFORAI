---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/trivia-quiz-q-a-card/"
title: "Trivia Quiz Q&A Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front states a challenging trivia question with multiple-choice options; back reveals the correct answer with a brief context paragraph and score indicator."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Trivia Quiz Q&A Card
Source: https://codefronts.com/components/css-flip-cards/trivia-quiz-q-a-card/

Front states a challenging trivia question with multiple-choice options; back reveals the correct answer with a brief context paragraph and score indicator.
## HTML
```html
<div class="fc-07">
  <div class="fc-07__scene">
    <div class="fc-07__card">
      <div class="fc-07__front">
        <div class="fc-07__q-num">Q7</div>
        <div class="fc-07__category"><span class="fc-07__cat-dot"></span>Space & Astronomy</div>
        <div class="fc-07__difficulty">
          <span class="fc-07__star">★</span>
          <span class="fc-07__star">★</span>
          <span class="fc-07__star">★</span>
          <span class="fc-07__star empty">★</span>
          <span class="fc-07__star empty">★</span>
        </div>
        <div class="fc-07__question">Which planet in our solar system has the most known natural moons?</div>
        <div class="fc-07__options">
          <div class="fc-07__opt"><span class="fc-07__opt-letter">A</span>Jupiter</div>
          <div class="fc-07__opt"><span class="fc-07__opt-letter">B</span>Saturn</div>
          <div class="fc-07__opt"><span class="fc-07__opt-letter">C</span>Uranus</div>
          <div class="fc-07__opt"><span class="fc-07__opt-letter">D</span>Neptune</div>
        </div>
        <div class="fc-07__front-hint">Hover to reveal the answer →</div>
      </div>
      <div class="fc-07__back">
        <div class="fc-07__correct-label">✓ Correct Answer</div>
        <div class="fc-07__tick-circle">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        </div>
        <div class="fc-07__answer">B — Saturn</div>
        <div class="fc-07__divider-line"></div>
        <div class="fc-07__context">Saturn holds the record with 146 confirmed moons as of 2025, edging past Jupiter's 95. Saturn's moon Titan has a thick atmosphere and lakes of liquid methane.</div>
        <div class="fc-07__score-row">
          <div class="fc-07__score-item"><div class="fc-07__score-num">+10</div><div class="fc-07__score-lbl">Points</div></div>
          <div class="fc-07__score-item"><div class="fc-07__score-num">7/10</div><div class="fc-07__score-lbl">Progress</div></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-07,
.fc-07 *,
.fc-07 *::before,
.fc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-07 ::selection {
  background: #eab308;
  color: #000;
}

.fc-07 {
  --bg: #0c0c00;
  --yellow: #eab308;
  --amber: #f59e0b;
  --green: #22c55e;
  --white: #fefce8;
  --card-w: 360px;
  --card-h: 420px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 30%,#1a1500,#0c0c00 65%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-07__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-07__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-07__scene:hover .fc-07__card {
  transform: rotateY(180deg);
}

.fc-07__front,
.fc-07__back {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-07__front {
  background: linear-gradient(145deg,#1a1400,#150f00);
  border: 1px solid rgba(234,179,8,.25);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 36px 28px;
}

.fc-07__front::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 0%,rgba(234,179,8,.12),transparent 60%);
}

.fc-07__category {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--amber);
  font-weight: 700;
  position: relative;
  z-index: 1;
}

.fc-07__cat-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--amber);
}

.fc-07__difficulty {
  position: relative;
  z-index: 1;
  margin-top: 6px;
  display: flex;
  gap: 4px;
}

.fc-07__star {
  color: var(--yellow);
  font-size: 14px;
}

.fc-07__star.empty {
  opacity: .2;
}

.fc-07__q-num {
  font-size: 80px;
  font-weight: 900;
  color: rgba(234,179,8,.07);
  position: absolute;
  top: 20px;
  right: 24px;
  line-height: 1;
  font-style: italic;
}

.fc-07__question {
  position: relative;
  z-index: 1;
  margin-top: 24px;
  font-size: 20px;
  font-weight: 700;
  line-height: 1.5;
  text-align: center;
  color: var(--white);
}

.fc-07__options {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
  margin-top: 28px;
  position: relative;
  z-index: 1;
}

.fc-07__opt {
  padding: 11px 16px;
  border-radius: 12px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(234,179,8,.15);
  font-size: 13px;
  color: rgba(254,252,232,.7);
  cursor: pointer;
  transition: background .2s,border-color .2s;
  display: flex;
  align-items: center;
  gap: 10px;
}

.fc-07__opt:hover {
  background: rgba(234,179,8,.1);
  border-color: rgba(234,179,8,.35);
  color: var(--white);
}

.fc-07__opt-letter {
  width: 22px;
  height: 22px;
  border-radius: 6px;
  background: rgba(234,179,8,.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  color: var(--amber);
  flex-shrink: 0;
}

.fc-07__front-hint {
  margin-top: auto;
  font-size: 10px;
  color: rgba(254,252,232,.2);
  letter-spacing: .08em;
}
/* BACK */

.fc-07__back {
  background: linear-gradient(145deg,#051a08,#071a0e);
  border: 1px solid rgba(34,197,94,.25);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 36px 28px;
  gap: 16px;
}

.fc-07__back::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 30%,rgba(34,197,94,.1),transparent 60%);
}

.fc-07__correct-label {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--green);
  font-weight: 700;
}

.fc-07__tick-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(34,197,94,.15);
  border: 2px solid rgba(34,197,94,.35);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}

.fc-07__answer {
  position: relative;
  z-index: 1;
  font-size: 26px;
  font-weight: 900;
  color: var(--white);
  text-align: center;
  line-height: 1.2;
}

.fc-07__divider-line {
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg,transparent,rgba(34,197,94,.4),transparent);
  position: relative;
  z-index: 1;
}

.fc-07__context {
  position: relative;
  z-index: 1;
  font-size: 13px;
  color: rgba(254,252,232,.6);
  line-height: 1.7;
  text-align: center;
}

.fc-07__score-row {
  position: relative;
  z-index: 1;
  display: flex;
  gap: 20px;
  margin-top: 4px;
}

.fc-07__score-item {
  text-align: center;
}

.fc-07__score-num {
  font-size: 22px;
  font-weight: 800;
  color: var(--green);
}

.fc-07__score-lbl {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: rgba(254,252,232,.3);
}

@media (prefers-reduced-motion: reduce) {
  .fc-07__card {
    transition: none;
  }
}
```
