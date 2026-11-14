---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-stagger-animation-list-items/"
title: "CSS Stagger Animation List Items"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Three stagger animation patterns: slide-from-left list items, scale-and-fade cards and cascade drop timeline entries using nth-child animation-delay."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stagger Animation List Items
Source: https://codefronts.com/motion/css-keyframe-animations/css-stagger-animation-list-items/

Three stagger animation patterns: slide-from-left list items, scale-and-fade cards and cascade drop timeline entries using nth-child animation-delay.
## HTML
```html
<div class="kf-14">

  <div class="kf-14__col">
    <div class="kf-14__col-title">Slide from Left</div>
    <div class="kf-14__item"><div class="kf-14__icon kf-14__icon--1">🎨</div><div class="kf-14__info"><b>UI Design</b><span>Figma · 24 components</span></div></div>
    <div class="kf-14__item"><div class="kf-14__icon kf-14__icon--2">⚡</div><div class="kf-14__info"><b>Animation</b><span>CSS keyframes</span></div></div>
    <div class="kf-14__item"><div class="kf-14__icon kf-14__icon--3">🧪</div><div class="kf-14__info"><b>Testing</b><span>Coverage 94%</span></div></div>
    <div class="kf-14__item"><div class="kf-14__icon kf-14__icon--4">🚀</div><div class="kf-14__info"><b>Deploy</b><span>CI/CD pipeline</span></div></div>
    <div class="kf-14__item"><div class="kf-14__icon kf-14__icon--5">📊</div><div class="kf-14__info"><b>Analytics</b><span>Live dashboard</span></div></div>
    <div class="kf-14__item"><div class="kf-14__icon kf-14__icon--6">🔐</div><div class="kf-14__info"><b>Security</b><span>Auth + tokens</span></div></div>
  </div>

  <div class="kf-14__cards">
    <div class="kf-14__col-title">Scale + Fade</div>
    <div class="kf-14__card"><h3>Motion Design</h3><p>Spring-based animations for delightful micro-interactions.</p><span class="kf-14__card-tag">CSS</span></div>
    <div class="kf-14__card"><h3>Glassmorphism</h3><p>Frosted glass layers with backdrop-filter blur.</p><span class="kf-14__card-tag">DESIGN</span></div>
    <div class="kf-14__card"><h3>Dark Mode</h3><p>Adaptive color palettes with CSS custom properties.</p><span class="kf-14__card-tag">THEME</span></div>
    <div class="kf-14__card"><h3>Accessibility</h3><p>prefers-reduced-motion and focus management.</p><span class="kf-14__card-tag">A11Y</span></div>
  </div>

  <div class="kf-14__timeline">
    <div class="kf-14__col-title">Cascade Drop</div>
    <div class="kf-14__titem"><div class="kf-14__dot"></div><div class="kf-14__tbody"><b>Project Kickoff</b><span>Jan 2025 · Initial scope</span></div></div>
    <div class="kf-14__titem"><div class="kf-14__dot"></div><div class="kf-14__tbody"><b>Design Sprint</b><span>Feb 2025 · 12 screens</span></div></div>
    <div class="kf-14__titem"><div class="kf-14__dot"></div><div class="kf-14__tbody"><b>Dev Phase</b><span>Mar 2025 · Component library</span></div></div>
    <div class="kf-14__titem"><div class="kf-14__dot"></div><div class="kf-14__tbody"><b>Beta Launch</b><span>Apr 2025 · 500 users</span></div></div>
    <div class="kf-14__titem"><div class="kf-14__dot"></div><div class="kf-14__tbody"><b>Go Live</b><span>May 2025 · Public release</span></div></div>
  </div>

</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap');

.kf-14,
.kf-14 *,
.kf-14 *::before,
.kf-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-14 ::selection {
  background: #f72585;
  color: #fff;
}

.kf-14 {
  --bg: #0f0f23;
  --pink: #f72585;
  --cyan: #4cc9f0;
  --green: #80ffdb;
  --gold: #ffd60a;
  --white: #e8e8ff;
  --card: #16162a;
  font-family: 'Plus Jakarta Sans',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: center;
  padding: 60px 24px;
  gap: 48px;
  color: var(--white);
}
/* ——— 1: Slide-in from left ——— */

.kf-14__col {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 240px;
  max-width: 320px;
  flex: 1;
}

.kf-14__col-title {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #555;
  margin-bottom: 4px;
}

.kf-14__item {
  background: var(--card);
  border-radius: 12px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 14px;
  border: 1px solid rgba(255,255,255,.05);
  opacity: 0;
  transform: translateX(-30px);
  animation: kf-14-slide-in .5s cubic-bezier(.2,.8,.2,1) forwards;
}

.kf-14__item:nth-child(2) {
  animation-delay: .1s;
}

.kf-14__item:nth-child(3) {
  animation-delay: .2s;
}

.kf-14__item:nth-child(4) {
  animation-delay: .3s;
}

.kf-14__item:nth-child(5) {
  animation-delay: .4s;
}

.kf-14__item:nth-child(6) {
  animation-delay: .5s;
}

@keyframes kf-14-slide-in {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.kf-14__icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: grid;
  place-items: center;
  font-size: 1.1rem;
  flex: 0 0 40px;
}

.kf-14__info {
  flex: 1;
}

.kf-14__info b {
  display: block;
  font-size: .9rem;
  font-weight: 700;
}

.kf-14__info span {
  font-size: .75rem;
  color: #888;
  margin-top: 2px;
  display: block;
}
/* ——— 2: Fade + scale up ——— */

.kf-14__cards {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 240px;
  max-width: 320px;
  flex: 1;
}

.kf-14__card {
  background: linear-gradient(135deg,rgba(247,37,133,.1),rgba(76,201,240,.08));
  border: 1px solid rgba(247,37,133,.2);
  border-radius: 16px;
  padding: 20px;
  opacity: 0;
  transform: scale(.88);
  animation: kf-14-pop .5s cubic-bezier(.34,1.56,.64,1) forwards;
}

.kf-14__card:nth-child(2) {
  animation-delay: .12s;
}

.kf-14__card:nth-child(3) {
  animation-delay: .24s;
}

.kf-14__card:nth-child(4) {
  animation-delay: .36s;
}

@keyframes kf-14-pop {
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.kf-14__card h3 {
  font-size: .95rem;
  font-weight: 800;
  margin-bottom: 6px;
}

.kf-14__card p {
  font-size: .78rem;
  color: #888;
  line-height: 1.4;
}

.kf-14__card-tag {
  display: inline-block;
  font-size: .65rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  margin-top: 10px;
}
/* ——— 3: Cascade drop ——— */

.kf-14__timeline {
  display: flex;
  flex-direction: column;
  gap: 0;
  min-width: 240px;
  max-width: 300px;
  flex: 1;
  position: relative;
}

.kf-14__timeline::before {
  content: '';
  position: absolute;
  left: 19px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: rgba(128,255,219,.15);
}

.kf-14__titem {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  padding: 12px 0;
  opacity: 0;
  transform: translateY(-20px);
  animation: kf-14-drop .4s cubic-bezier(.4,0,.2,1) forwards;
}

.kf-14__titem:nth-child(1) {
  animation-delay: .05s;
}

.kf-14__titem:nth-child(2) {
  animation-delay: .2s;
}

.kf-14__titem:nth-child(3) {
  animation-delay: .35s;
}

.kf-14__titem:nth-child(4) {
  animation-delay: .5s;
}

.kf-14__titem:nth-child(5) {
  animation-delay: .65s;
}

@keyframes kf-14-drop {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.kf-14__dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  flex: 0 0 16px;
  margin-top: 2px;
  border: 2px solid;
}

.kf-14__tbody {
  flex: 1;
}

.kf-14__tbody b {
  font-size: .88rem;
  font-weight: 700;
  display: block;
}

.kf-14__tbody span {
  font-size: .72rem;
  color: #666;
  display: block;
  margin-top: 2px;
}
/* Icon colors */

.kf-14__icon--1 {
  background: rgba(247,37,133,.15);
  color: var(--pink);
}

.kf-14__icon--2 {
  background: rgba(76,201,240,.15);
  color: var(--cyan);
}

.kf-14__icon--3 {
  background: rgba(128,255,219,.15);
  color: var(--green);
}

.kf-14__icon--4 {
  background: rgba(255,214,10,.15);
  color: var(--gold);
}

.kf-14__icon--5 {
  background: rgba(247,37,133,.1);
  color: var(--pink);
}

.kf-14__icon--6 {
  background: rgba(76,201,240,.1);
  color: var(--cyan);
}

.kf-14__card:nth-child(1) .kf-14__card-tag {
  background: rgba(247,37,133,.2);
  color: var(--pink);
}

.kf-14__card:nth-child(2) .kf-14__card-tag {
  background: rgba(76,201,240,.2);
  color: var(--cyan);
}

.kf-14__card:nth-child(3) .kf-14__card-tag {
  background: rgba(128,255,219,.2);
  color: var(--green);
}

.kf-14__card:nth-child(4) .kf-14__card-tag {
  background: rgba(255,214,10,.2);
  color: var(--gold);
}

.kf-14__dot:nth-child(1) {
  border-color: var(--pink);
  background: rgba(247,37,133,.2);
}

.kf-14__titem:nth-child(1) .kf-14__dot {
  border-color: var(--pink);
}

.kf-14__titem:nth-child(2) .kf-14__dot {
  border-color: var(--cyan);
}

.kf-14__titem:nth-child(3) .kf-14__dot {
  border-color: var(--green);
}

.kf-14__titem:nth-child(4) .kf-14__dot {
  border-color: var(--gold);
}

.kf-14__titem:nth-child(5) .kf-14__dot {
  border-color: var(--pink);
}

@media (prefers-reduced-motion: reduce) {
  .kf-14 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
