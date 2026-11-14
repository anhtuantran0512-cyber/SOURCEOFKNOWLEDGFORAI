---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-liquid-fill-animation-progress-bar/"
title: "CSS Liquid Fill Animation Progress Bar"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Liquid-fill progress bars with wave-bubble effect and circular liquid-fill widgets using CSS clip-path, pseudo-element waves and scoped keyframes."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Liquid Fill Animation Progress Bar
Source: https://codefronts.com/motion/css-keyframe-animations/css-liquid-fill-animation-progress-bar/

Liquid-fill progress bars with wave-bubble effect and circular liquid-fill widgets using CSS clip-path, pseudo-element waves and scoped keyframes.
## HTML
```html
<div class="kf-13">
  <div class="kf-13__title">Liquid Fill <span>Progress</span> Bars</div>

  <div class="kf-13__grid">
    <div class="kf-13__row">
      <span class="kf-13__row-label">Design</span>
      <div class="kf-13__track"><div class="kf-13__fill"></div></div>
      <span class="kf-13__pct">87%</span>
    </div>
    <div class="kf-13__row">
      <span class="kf-13__row-label">Frontend</span>
      <div class="kf-13__track"><div class="kf-13__fill kf-13__fill--2"></div></div>
      <span class="kf-13__pct">65%</span>
    </div>
    <div class="kf-13__row">
      <span class="kf-13__row-label">Backend</span>
      <div class="kf-13__track"><div class="kf-13__fill kf-13__fill--3"></div></div>
      <span class="kf-13__pct">42%</span>
    </div>
    <div class="kf-13__row">
      <span class="kf-13__row-label">DevOps</span>
      <div class="kf-13__track"><div class="kf-13__fill kf-13__fill--4"></div></div>
      <span class="kf-13__pct">78%</span>
    </div>
    <div class="kf-13__row">
      <span class="kf-13__row-label">Testing</span>
      <div class="kf-13__track"><div class="kf-13__fill kf-13__fill--5"></div></div>
      <span class="kf-13__pct">55%</span>
    </div>
  </div>

  <div class="kf-13__circles">
    <div class="kf-13__circle-wrap">
      <div class="kf-13__circle kf-13__circle--blue">
        <div class="kf-13__liquid"></div>
        <span class="kf-13__num">70%</span>
      </div>
      <span class="kf-13__circle-label">CPU</span>
    </div>
    <div class="kf-13__circle-wrap">
      <div class="kf-13__circle kf-13__circle--teal">
        <div class="kf-13__liquid"></div>
        <span class="kf-13__num">45%</span>
      </div>
      <span class="kf-13__circle-label">Memory</span>
    </div>
    <div class="kf-13__circle-wrap">
      <div class="kf-13__circle kf-13__circle--orange">
        <div class="kf-13__liquid"></div>
        <span class="kf-13__num">82%</span>
      </div>
      <span class="kf-13__circle-label">Storage</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&display=swap');

.kf-13,
.kf-13 *,
.kf-13 *::before,
.kf-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-13 ::selection {
  background: #4361ee;
  color: #fff;
}

.kf-13 {
  --bg: #f0f4ff;
  --blue: #4361ee;
  --teal: #06d6a0;
  --red: #ef233c;
  --orange: #fb8500;
  --purple: #7209b7;
  font-family: 'Nunito',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 40px;
  color: #1a1a2e;
}

.kf-13__title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 900;
  letter-spacing: -.02em;
  text-align: center;
}

.kf-13__title span {
  color: var(--blue);
}

.kf-13__grid {
  display: flex;
  flex-direction: column;
  gap: 28px;
  width: 100%;
  max-width: 560px;
}

.kf-13__row {
  display: flex;
  align-items: center;
  gap: 16px;
}

.kf-13__row-label {
  font-weight: 800;
  font-size: .88rem;
  width: 80px;
  text-align: right;
  flex: 0 0 80px;
}

.kf-13__pct {
  font-weight: 900;
  font-size: .9rem;
  width: 42px;
  color: var(--blue);
}
/* Liquid fill bar */

.kf-13__track {
  flex: 1;
  height: 28px;
  border-radius: 14px;
  background: rgba(0,0,0,.06);
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 2px 4px rgba(0,0,0,.1);
}

.kf-13__fill {
  height: 100%;
  border-radius: 14px;
  position: relative;
  background: linear-gradient(90deg,var(--blue),#6c8fff);
  box-shadow: inset 0 2px 4px rgba(255,255,255,.3);
  animation: kf-13-fill1 3s cubic-bezier(.4,0,.2,1) forwards;
}

.kf-13__fill--2 {
  background: linear-gradient(90deg,var(--teal),#43efa0);
  animation: kf-13-fill2 3s cubic-bezier(.4,0,.2,1) 0.3s forwards;
  width: 0;
}

.kf-13__fill--3 {
  background: linear-gradient(90deg,var(--red),#ff7096);
  animation: kf-13-fill3 3s cubic-bezier(.4,0,.2,1) 0.6s forwards;
  width: 0;
}

.kf-13__fill--4 {
  background: linear-gradient(90deg,var(--orange),#ffd166);
  animation: kf-13-fill4 3s cubic-bezier(.4,0,.2,1) 0.9s forwards;
  width: 0;
}

.kf-13__fill--5 {
  background: linear-gradient(90deg,var(--purple),#b040f5);
  animation: kf-13-fill5 3s cubic-bezier(.4,0,.2,1) 1.2s forwards;
  width: 0;
}

@keyframes kf-13-fill1 {
  from {
    width: 0;
  }

  to {
    width: 87%;
  }
}

@keyframes kf-13-fill2 {
  from {
    width: 0;
  }

  to {
    width: 65%;
  }
}

@keyframes kf-13-fill3 {
  from {
    width: 0;
  }

  to {
    width: 42%;
  }
}

@keyframes kf-13-fill4 {
  from {
    width: 0;
  }

  to {
    width: 78%;
  }
}

@keyframes kf-13-fill5 {
  from {
    width: 0;
  }

  to {
    width: 55%;
  }
}
/* Liquid wave top */

.kf-13__fill::after {
  content: '';
  position: absolute;
  top: -8px;
  right: -10px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: inherit;
  animation: kf-13-bubble 2s ease-in-out infinite;
}

@keyframes kf-13-bubble {
  0%,
    100% {
    transform: scaleY(1) translateY(0);
  }

  50% {
    transform: scaleY(1.3) translateY(-3px);
  }
}
/* Circular liquid fill */

.kf-13__circles {
  display: flex;
  gap: 32px;
  flex-wrap: wrap;
  justify-content: center;
}

.kf-13__circle-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.kf-13__circle {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  border: 4px solid;
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
}

.kf-13__circle--blue {
  border-color: var(--blue);
  background: rgba(67,97,238,.08);
}

.kf-13__circle--teal {
  border-color: var(--teal);
  background: rgba(6,214,160,.08);
}

.kf-13__circle--orange {
  border-color: var(--orange);
  background: rgba(251,133,0,.08);
}

.kf-13__liquid {
  position: absolute;
  bottom: 0;
  left: -10%;
  width: 120%;
  border-radius: 50% 50% 0 0/20px;
}

.kf-13__liquid::before {
  content: '';
  position: absolute;
  top: -12px;
  left: 0;
  right: 0;
  height: 24px;
  border-radius: 50%;
  animation: kf-13-liq-wave 2.5s ease-in-out infinite;
}

.kf-13__circle--blue .kf-13__liquid {
  height: 70%;
  background: rgba(67,97,238,.25);
  animation: kf-13-liq-fill 2s ease-out forwards;
}

.kf-13__circle--blue .kf-13__liquid::before {
  background: rgba(67,97,238,.4);
}

.kf-13__circle--teal .kf-13__liquid {
  height: 45%;
  background: rgba(6,214,160,.3);
  animation: kf-13-liq-fill 2s ease-out .3s forwards;
}

.kf-13__circle--teal .kf-13__liquid::before {
  background: rgba(6,214,160,.5);
}

.kf-13__circle--orange .kf-13__liquid {
  height: 82%;
  background: rgba(251,133,0,.2);
  animation: kf-13-liq-fill 2s ease-out .6s forwards;
}

.kf-13__circle--orange .kf-13__liquid::before {
  background: rgba(251,133,0,.4);
}

@keyframes kf-13-liq-fill {
  from {
    height: 0;
  }
}

@keyframes kf-13-liq-wave {
  0%,
    100% {
    transform: translateX(-8px);
  }

  50% {
    transform: translateX(8px);
  }
}

.kf-13__num {
  position: relative;
  z-index: 1;
  font-size: 1.4rem;
  font-weight: 900;
}

.kf-13__circle--blue .kf-13__num {
  color: var(--blue);
}

.kf-13__circle--teal .kf-13__num {
  color: var(--teal);
}

.kf-13__circle--orange .kf-13__num {
  color: var(--orange);
}

.kf-13__circle-label {
  font-size: .75rem;
  font-weight: 800;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #888;
}

@media (prefers-reduced-motion: reduce) {
  .kf-13 * {
    animation: none!important;
  }

  .kf-13__fill {
    width: 87%;
  }

  .kf-13__fill--2 {
    width: 65%;
  }

  .kf-13__fill--3 {
    width: 42%;
  }

  .kf-13__fill--4 {
    width: 78%;
  }

  .kf-13__fill--5 {
    width: 55%;
  }

  .kf-13__liquid {
    height: 50%;
  }
}
```
