---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-card-stack-animation/"
title: "CSS Card Stack Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Five card stack animations: flip-through financial deck, fanned playing cards, depth-rise pricing stack, Tinder-style swipe deck and floating credit card stack."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Card Stack Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-card-stack-animation/

Five card stack animations: flip-through financial deck, fanned playing cards, depth-rise pricing stack, Tinder-style swipe deck and floating credit card stack.
## HTML
```html
<div class="kf-27">
  <h2>CSS Card Stack Animations</h2>
  <div class="row">

    <!-- Flip through -->
    <div class="demo-wrap">
      <div class="flip-stack">
        <div class="fc">
          <div class="fc-amt">$2,450</div>
          <div class="fc-name">Savings Account</div>
        </div>
        <div class="fc">
          <div class="fc-amt">$8,100</div>
          <div class="fc-name">Investment</div>
        </div>
        <div class="fc">
          <div class="fc-amt">$320</div>
          <div class="fc-name">Daily Spend</div>
        </div>
      </div>
      <label>Flip Through</label>
    </div>

    <!-- Fan deck -->
    <div class="demo-wrap">
      <div class="fan-stack">
        <div class="fan-card">♠</div>
        <div class="fan-card">♥</div>
        <div class="fan-card">♦</div>
        <div class="fan-card">♣</div>
      </div>
      <label>Fanned Deck</label>
    </div>

    <!-- Rise stack -->
    <div class="demo-wrap">
      <div class="rise-stack">
        <div class="rise-card"></div>
        <div class="rise-card"></div>
        <div class="rise-card">
          <div class="rc-title">Pro Plan</div>
          <div class="rc-sub">Everything you need</div>
          <div class="rc-tag">Most Popular</div>
        </div>
      </div>
      <label>Depth Rise</label>
    </div>

    <!-- Swipe deck -->
    <div class="demo-wrap">
      <div class="swipe-stack">
        <div class="swipe-card">
          <div class="sc-header">Candidate</div>
          <div>
            <div class="sc-name">Alex Morgan</div>
            <div class="sc-role">Senior Designer</div>
          </div>
          <div class="sc-match">94% match</div>
        </div>
        <div class="swipe-card"></div>
        <div class="swipe-card"></div>
      </div>
      <label>Swipe Stack</label>
    </div>

    <!-- Credit card -->
    <div class="demo-wrap">
      <div class="credit-stack">
        <div class="credit-card">
          <div class="cc-chip"></div>
          <div class="cc-num">•••• •••• •••• 4291</div>
          <div class="cc-row">
            <div class="cc-name">J. Smith</div>
            <div class="cc-brand">◉◉</div>
          </div>
        </div>
        <div class="credit-card"></div>
        <div class="credit-card"></div>
      </div>
      <label>Credit Cards</label>
    </div>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap');

.kf-27 *,
.kf-27 *::before,
.kf-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-27 {
  font-family: 'Inter', sans-serif;
  background: #0f0f14;
  color: #fff;
  padding: 48px 24px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 56px;
}

.kf-27 h2 {
  font-size: 1rem;
  color: #444;
  letter-spacing: 3px;
  text-transform: uppercase;
}

.kf-27 .row {
  display: flex;
  flex-wrap: wrap;
  gap: 60px;
  justify-content: center;
  width: 100%;
  max-width: 960px;
}

.kf-27 .demo-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.kf-27 .demo-wrap label {
  font-size: 0.72rem;
  color: #444;
  letter-spacing: 2px;
  text-transform: uppercase;
}
/* ── 1: Flip Through Stack ── */

.kf-27 .flip-stack {
  position: relative;
  width: 240px;
  height: 160px;
}

.kf-27 .flip-stack .fc {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  backface-visibility: hidden;
}

.kf-27 .flip-stack .fc:nth-child(1) {
  background: linear-gradient(135deg, #7c6af7, #e91e8c);
  animation: kf-27-flip 6s ease-in-out infinite;
}

.kf-27 .flip-stack .fc:nth-child(2) {
  background: linear-gradient(135deg, #00d4ff, #00d46a);
  animation: kf-27-flip 6s ease-in-out infinite;
  animation-delay: 2s;
}

.kf-27 .flip-stack .fc:nth-child(3) {
  background: linear-gradient(135deg, #f7c948, #ff6b35);
  animation: kf-27-flip 6s ease-in-out infinite;
  animation-delay: 4s;
}

@keyframes kf-27-flip {
  0% {
    transform: translateY(0) scale(1);
    z-index: 3;
    opacity: 1;
  }

  25% {
    transform: translateY(-10px) scale(1.02);
    z-index: 3;
    opacity: 1;
  }

  35% {
    transform: translateX(120%) rotate(15deg) scale(0.95);
    z-index: 3;
    opacity: 0.8;
  }

  40% {
    transform: translateX(160%) rotate(20deg);
    z-index: 0;
    opacity: 0;
  }

  41% {
    transform: translateX(-10px) rotate(-3deg) scale(0.92);
    z-index: 1;
    opacity: 0.5;
  }

  60% {
    transform: translateX(0) rotate(0deg) scale(0.96);
    z-index: 1;
    opacity: 0.8;
  }

  80% {
    transform: translateX(0) scale(0.98);
    z-index: 2;
  }

  100% {
    transform: translateY(0) scale(1);
    z-index: 3;
    opacity: 1;
  }
}

.kf-27 .fc-amt {
  font-size: 1.6rem;
  font-weight: 900;
  color: rgba(255,255,255,0.95);
}

.kf-27 .fc-name {
  font-size: 0.78rem;
  color: rgba(255,255,255,0.7);
  font-weight: 500;
}
/* ── 2: Fanned deck ── */

.kf-27 .fan-stack {
  position: relative;
  width: 200px;
  height: 160px;
}

.kf-27 .fan-stack .fan-card {
  position: absolute;
  width: 140px;
  height: 100px;
  border-radius: 12px;
  top: 30px;
  left: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
}

.kf-27 .fan-card:nth-child(1) {
  background: #7c6af7;
  animation: kf-27-fan1 4s ease-in-out infinite;
}

.kf-27 .fan-card:nth-child(2) {
  background: #e91e8c;
  animation: kf-27-fan2 4s ease-in-out infinite;
}

.kf-27 .fan-card:nth-child(3) {
  background: #ff6b35;
  animation: kf-27-fan3 4s ease-in-out infinite;
}

.kf-27 .fan-card:nth-child(4) {
  background: #f7c948;
  animation: kf-27-fan4 4s ease-in-out infinite;
}

@keyframes kf-27-fan1 {
  0%,
    100% {
    transform: rotate(-20deg) translateX(-20px);
    z-index: 1;
  }

  50% {
    transform: rotate(-20deg) translateX(-25px);
    z-index: 1;
  }
}

@keyframes kf-27-fan2 {
  0%,
    100% {
    transform: rotate(-7deg) translateX(-6px);
    z-index: 2;
  }

  50% {
    transform: rotate(-9deg) translateX(-8px);
    z-index: 2;
  }
}

@keyframes kf-27-fan3 {
  0%,
    100% {
    transform: rotate(7deg) translateX(6px);
    z-index: 3;
  }

  50% {
    transform: rotate(9deg) translateX(8px);
    z-index: 3;
  }
}

@keyframes kf-27-fan4 {
  0%,
    100% {
    transform: rotate(20deg) translateX(20px);
    z-index: 4;
  }

  50% {
    transform: rotate(22deg) translateX(22px);
    z-index: 4;
  }
}
/* ── 3: Stacking rise ── */

.kf-27 .rise-stack {
  position: relative;
  width: 220px;
  height: 180px;
}

.kf-27 .rise-card {
  position: absolute;
  width: 100%;
  height: 120px;
  border-radius: 14px;
  padding: 16px;
}

.kf-27 .rise-card:nth-child(1) {
  bottom: 0;
  left: 0;
  background: #1a1a30;
  border: 1px solid #2a2a50;
  transform: scale(0.88) translateY(16px);
  z-index: 1;
  animation: kf-27-rise1 5s ease-in-out infinite;
}

.kf-27 .rise-card:nth-child(2) {
  bottom: 0;
  left: 0;
  background: #1e1e3a;
  border: 1px solid #303060;
  transform: scale(0.94) translateY(8px);
  z-index: 2;
  animation: kf-27-rise2 5s ease-in-out infinite;
}

.kf-27 .rise-card:nth-child(3) {
  bottom: 0;
  left: 0;
  background: #24243e;
  border: 1px solid #7c6af7;
  z-index: 3;
  animation: kf-27-rise3 5s ease-in-out infinite;
}

.kf-27 .rise-card .rc-title {
  font-size: 1rem;
  font-weight: 600;
  color: #7c6af7;
}

.kf-27 .rise-card .rc-sub {
  font-size: 0.78rem;
  color: #666;
  margin-top: 4px;
}

.kf-27 .rise-card .rc-tag {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 20px;
  background: rgba(124,106,247,0.15);
  font-size: 0.7rem;
  color: #7c6af7;
  margin-top: 8px;
}

@keyframes kf-27-rise1 {
  0%,
    40%,
    100% {
    transform: scale(0.88) translateY(16px);
  }

  60%,
    80% {
    transform: scale(0.88) translateY(14px);
  }
}

@keyframes kf-27-rise2 {
  0%,
    40%,
    100% {
    transform: scale(0.94) translateY(8px);
  }

  60%,
    80% {
    transform: scale(0.94) translateY(6px);
  }
}

@keyframes kf-27-rise3 {
  0%,
    30%,
    100% {
    transform: translateY(0) scale(1);
    box-shadow: 0 8px 32px rgba(124,106,247,0.2);
  }

  50% {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 50px rgba(124,106,247,0.4);
  }
}
/* ── 4: Swipe deck ── */

.kf-27 .swipe-stack {
  position: relative;
  width: 220px;
  height: 170px;
}

.kf-27 .swipe-card {
  position: absolute;
  width: 200px;
  height: 140px;
  border-radius: 16px;
  top: 15px;
  left: 10px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.kf-27 .swipe-card:nth-child(3) {
  background: #1a1a2a;
  border: 1px solid #222240;
  transform: scale(0.84) translateY(12px);
  z-index: 1;
}

.kf-27 .swipe-card:nth-child(2) {
  background: #1e1e32;
  border: 1px solid #282850;
  transform: scale(0.92) translateY(6px);
  z-index: 2;
}

.kf-27 .swipe-card:nth-child(1) {
  background: linear-gradient(135deg, #1a1a38, #22223a);
  border: 1px solid #3a3a6a;
  z-index: 3;
  animation: kf-27-swipe 4s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

@keyframes kf-27-swipe {
  0%,
    40% {
    transform: translateX(0) rotate(0deg);
    opacity: 1;
    z-index: 3;
  }

  55% {
    transform: translateX(160%) rotate(15deg);
    opacity: 0.6;
    z-index: 3;
  }

  56% {
    transform: translateX(-160%) rotate(-10deg);
    opacity: 0;
    z-index: 0;
  }

  70% {
    transform: translateX(0) rotate(0deg);
    opacity: 1;
    z-index: 1;
  }

  85% {
    z-index: 2;
  }

  100% {
    transform: translateX(0) rotate(0deg);
    z-index: 3;
    opacity: 1;
  }
}

.kf-27 .sc-header {
  font-size: 0.72rem;
  color: #555;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.kf-27 .sc-name {
  font-size: 1rem;
  font-weight: 600;
  color: #ccc;
}

.kf-27 .sc-role {
  font-size: 0.78rem;
  color: #666;
}

.kf-27 .sc-match {
  font-size: 0.78rem;
  color: #00d46a;
}
/* ── 5: Credit card stack ── */

.kf-27 .credit-stack {
  position: relative;
  width: 260px;
  height: 180px;
}

.kf-27 .credit-card {
  position: absolute;
  width: 240px;
  height: 150px;
  border-radius: 16px;
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.kf-27 .credit-card:nth-child(3) {
  background: linear-gradient(135deg, #1e1e30, #2a2a45);
  top: 20px;
  left: 10px;
  transform: rotate(-5deg) scale(0.9);
  z-index: 1;
}

.kf-27 .credit-card:nth-child(2) {
  background: linear-gradient(135deg, #241e40, #302855);
  top: 10px;
  left: 10px;
  transform: rotate(-2deg) scale(0.95);
  z-index: 2;
  animation: kf-27-credit2 3s ease-in-out infinite;
}

.kf-27 .credit-card:nth-child(1) {
  background: linear-gradient(135deg, #7c6af7, #e91e8c);
  top: 0;
  left: 10px;
  z-index: 3;
  animation: kf-27-credit1 3s ease-in-out infinite;
  box-shadow: 0 12px 40px rgba(124,106,247,0.4);
}

@keyframes kf-27-credit1 {
  0%,
    100% {
    transform: translateY(0) rotate(0deg);
    box-shadow: 0 12px 40px rgba(124,106,247,0.4);
  }

  50% {
    transform: translateY(-6px) rotate(0.5deg);
    box-shadow: 0 20px 60px rgba(124,106,247,0.6);
  }
}

@keyframes kf-27-credit2 {
  0%,
    100% {
    transform: rotate(-2deg) scale(0.95);
  }

  50% {
    transform: rotate(-3deg) scale(0.95) translateY(-2px);
  }
}

.kf-27 .cc-chip {
  width: 36px;
  height: 26px;
  background: rgba(255,215,100,0.8);
  border-radius: 4px;
}

.kf-27 .cc-num {
  font-size: 0.9rem;
  letter-spacing: 3px;
  color: rgba(255,255,255,0.85);
  font-family: 'JetBrains Mono', monospace;
}

.kf-27 .cc-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.kf-27 .cc-name {
  font-size: 0.75rem;
  color: rgba(255,255,255,0.7);
  letter-spacing: 1px;
  text-transform: uppercase;
}

.kf-27 .cc-brand {
  font-size: 1.4rem;
  color: rgba(255,255,255,0.5);
}

@media (prefers-reduced-motion: reduce) {
  .kf-27 .fc,
    .kf-27 .fan-card,
    .kf-27 .rise-card,
    .kf-27 .swipe-card:nth-child(1),
    .kf-27 .credit-card {
    animation: none;
  }
}
```
