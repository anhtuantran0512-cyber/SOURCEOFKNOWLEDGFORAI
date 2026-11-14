---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-ripple-click-animation-effect/"
title: "CSS Ripple Click Animation Effect"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Material Design ripple animations on six button variants, FAB, chip groups and icon buttons using ::after pseudo-element scale + opacity keyframes."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Ripple Click Animation Effect
Source: https://codefronts.com/motion/css-keyframe-animations/css-ripple-click-animation-effect/

Material Design ripple animations on six button variants, FAB, chip groups and icon buttons using ::after pseudo-element scale + opacity keyframes.
## HTML
```html
<div class="kf-16">
  <div style="text-align:center">
    <div class="kf-16__title">CSS Ripple Click Animations</div>
    <div class="kf-16__subtitle">Material Design ripple effect — pure CSS keyframes</div>
  </div>
  <div class="kf-16__grid">
    <div class="kf-16__cell">
      <button class="kf-16__btn kf-16__btn--1">🚀 Launch</button>
      <span class="kf-16__label">Filled</span>
    </div>
    <div class="kf-16__cell">
      <button class="kf-16__btn kf-16__btn--2">♥ Like</button>
      <span class="kf-16__label">Filled Pink</span>
    </div>
    <div class="kf-16__cell">
      <button class="kf-16__btn kf-16__btn--3">Subscribe</button>
      <span class="kf-16__label">Outlined</span>
    </div>
    <div class="kf-16__cell">
      <button class="kf-16__btn kf-16__btn--4">Follow</button>
      <span class="kf-16__label">Pill Shape</span>
    </div>
    <div class="kf-16__cell">
      <button class="kf-16__btn kf-16__btn--5">Deploy →</button>
      <span class="kf-16__label">Orange Flat</span>
    </div>
    <div class="kf-16__cell">
      <button class="kf-16__btn kf-16__btn--6">✓ Confirm</button>
      <span class="kf-16__label">Rounded</span>
    </div>
    <div class="kf-16__cell">
      <button class="kf-16__fab">+</button>
      <span class="kf-16__label">FAB</span>
    </div>
    <div class="kf-16__cell">
      <div class="kf-16__chips">
        <button class="kf-16__chip">Design</button>
        <button class="kf-16__chip">React</button>
        <button class="kf-16__chip">CSS</button>
      </div>
      <span class="kf-16__label">Chips</span>
    </div>
    <div class="kf-16__cell">
      <div class="kf-16__icon-row">
        <button class="kf-16__iconbtn">🏠</button>
        <button class="kf-16__iconbtn">🔍</button>
        <button class="kf-16__iconbtn">⚙️</button>
        <button class="kf-16__iconbtn">👤</button>
      </div>
      <span class="kf-16__label">Icon Buttons</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

.kf-16,
.kf-16 *,
.kf-16 *::before,
.kf-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-16 ::selection {
  background: #6200ea;
  color: #fff;
}

.kf-16 {
  --bg: #fafafa;
  --dp: #6200ea;
  --purple: #7c4dff;
  --pink: #e91e63;
  --teal: #00bcd4;
  --orange: #ff6d00;
  --green: #00c853;
  --ink: #212121;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 48px;
  color: var(--ink);
}

.kf-16__title {
  font-size: clamp(1.2rem,4vw,1.8rem);
  font-weight: 700;
  letter-spacing: -.01em;
}

.kf-16__subtitle {
  font-size: .88rem;
  color: #666;
  margin-top: 4px;
  text-align: center;
}

.kf-16__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  justify-content: center;
  max-width: 800px;
}

.kf-16__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.kf-16__label {
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #999;
}
/* Material ripple base */

.kf-16__btn {
  position: relative;
  overflow: hidden;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: 'Roboto';
  font-weight: 500;
  font-size: .9rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 14px 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.kf-16__btn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  transform: translate(-50%,-50%);
  animation: kf-16-ripple 1.4s ease-out infinite;
}
/* Button variants */

.kf-16__btn--1 {
  background: var(--dp);
  color: #fff;
  box-shadow: 0 3px 6px rgba(98,0,234,.35);
}

.kf-16__btn--1::after {
  background: rgba(255,255,255,.4);
}

.kf-16__btn--2 {
  background: var(--pink);
  color: #fff;
  box-shadow: 0 3px 6px rgba(233,30,99,.35);
}

.kf-16__btn--2::after {
  background: rgba(255,255,255,.35);
}

.kf-16__btn--3 {
  background: #fff;
  color: var(--dp);
  border: 2px solid var(--dp);
  box-shadow: 0 2px 4px rgba(0,0,0,.1);
}

.kf-16__btn--3::after {
  background: rgba(98,0,234,.2);
}

.kf-16__btn--4 {
  background: var(--teal);
  color: #fff;
  border-radius: 50px;
  box-shadow: 0 3px 8px rgba(0,188,212,.35);
}

.kf-16__btn--4::after {
  background: rgba(255,255,255,.35);
}

.kf-16__btn--5 {
  background: var(--orange);
  color: #fff;
  border-radius: 2px;
  box-shadow: 0 4px 8px rgba(255,109,0,.35);
}

.kf-16__btn--5::after {
  background: rgba(255,255,255,.3);
  animation-delay: .2s;
}

.kf-16__btn--6 {
  background: var(--green);
  color: #fff;
  border-radius: 8px;
  box-shadow: 0 3px 6px rgba(0,200,83,.35);
}

.kf-16__btn--6::after {
  background: rgba(255,255,255,.3);
}

@keyframes kf-16-ripple {
  0% {
    width: 0;
    height: 0;
    opacity: .8;
  }

  100% {
    width: 220px;
    height: 220px;
    opacity: 0;
  }
}
/* FAB ripple */

.kf-16__fab {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  border: none;
  background: var(--dp);
  color: #fff;
  font-size: 1.4rem;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  box-shadow: 0 6px 16px rgba(98,0,234,.45);
  display: grid;
  place-items: center;
  flex: 0 0 56px;
}

.kf-16__fab::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  transform: translate(-50%,-50%);
  background: rgba(255,255,255,.4);
  animation: kf-16-ripple 1.4s ease-out infinite .3s;
}
/* Chip ripple */

.kf-16__chip {
  padding: 8px 18px;
  border-radius: 50px;
  border: 1.5px solid #ddd;
  background: #fff;
  font-size: .85rem;
  font-weight: 500;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  color: var(--ink);
}

.kf-16__chip::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  transform: translate(-50%,-50%);
  background: rgba(98,0,234,.12);
  animation: kf-16-ripple 1.2s ease-out infinite;
}

.kf-16__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
}

.kf-16__chip:nth-child(2)::after {
  animation-delay: .25s;
  background: rgba(233,30,99,.12);
}

.kf-16__chip:nth-child(3)::after {
  animation-delay: .5s;
  background: rgba(0,188,212,.12);
}
/* Icon button ripple */

.kf-16__iconbtn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: none;
  background: transparent;
  font-size: 1.3rem;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
}

.kf-16__iconbtn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  transform: translate(-50%,-50%);
  background: rgba(0,0,0,.1);
  animation: kf-16-ripple 1.2s ease-out infinite;
}

.kf-16__icon-row {
  display: flex;
  gap: 8px;
}

.kf-16__iconbtn:nth-child(2)::after {
  animation-delay: .2s;
}

.kf-16__iconbtn:nth-child(3)::after {
  animation-delay: .4s;
}

.kf-16__iconbtn:nth-child(4)::after {
  animation-delay: .6s;
}

@media (max-width: 500px) {
  .kf-16__grid {
    gap: 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-16 * {
    animation: none!important;
  }
}
```
