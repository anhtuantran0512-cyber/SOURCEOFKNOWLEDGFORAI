---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/fluid-split-screen-hero-calendar/"
title: "Fluid Split-Screen Hero Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A landing-page hero split into an immersive seasonal half (sunset gradient, drifting sun orb, layered hills, giant Fraunces month) and a clean date-selector…"
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fluid Split-Screen Hero Calendar
Source: https://codefronts.com/components/css-calendar-designs/fluid-split-screen-hero-calendar/

A landing-page hero split into an immersive seasonal half (sunset gradient, drifting sun orb, layered hills, giant Fraunces month) and a clean date-selector half with pulsing today, event dots, a live selected-day readout and a CTA. Stacks vertically on mobile.
## HTML
```html
<div class="cal21">
  <div class="cal21__hero">

    <!-- LEFT: seasonal immersive -->
    <div class="cal21__left">
      <div class="cal21__hills">
        <div class="cal21__hill cal21__hill--1"></div>
        <div class="cal21__hill cal21__hill--2"></div>
        <div class="cal21__hill cal21__hill--3"></div>
      </div>

      <div class="cal21__left-top">
        <div class="cal21__eyebrow">Early Summer</div>
        <div class="cal21__left-meta">Long days, warm light</div>
      </div>

      <div class="cal21__bigmonth">
        <div class="cal21__bigmonth-name">June</div>
        <div class="cal21__bigmonth-year">2026</div>
      </div>

      <div class="cal21__left-foot">
        <div class="cal21__lf-stat">
          <div class="cal21__lf-num">21°</div>
          <div class="cal21__lf-lbl">Avg high</div>
        </div>
        <div class="cal21__lf-stat">
          <div class="cal21__lf-num">15h</div>
          <div class="cal21__lf-lbl">Daylight</div>
        </div>
        <div class="cal21__lf-stat">
          <div class="cal21__lf-num">12</div>
          <div class="cal21__lf-lbl">Events</div>
        </div>
      </div>
    </div>

    <!-- RIGHT: selector -->
    <div class="cal21__right">
      <div class="cal21__right-head">
        <div class="cal21__right-title">Pick a date</div>
        <div class="cal21__right-nav">
          <div class="cal21__rn-btn">‹</div>
          <div class="cal21__rn-btn">›</div>
        </div>
      </div>

      <div class="cal21__dow">
        <div class="cal21__dw">S</div><div class="cal21__dw">M</div><div class="cal21__dw">T</div>
        <div class="cal21__dw">W</div><div class="cal21__dw">T</div><div class="cal21__dw">F</div><div class="cal21__dw">S</div>
      </div>

      <div class="cal21__grid" id="cal21Grid">
        <div class="cal21__cell other weekend">25</div><div class="cal21__cell other">26</div><div class="cal21__cell other">27</div>
        <div class="cal21__cell other">28</div><div class="cal21__cell other">29</div><div class="cal21__cell other">30</div><div class="cal21__cell other weekend">31</div>
        <div class="cal21__cell weekend">1</div>
        <div class="cal21__cell">2<span class="ev"></span></div>
        <div class="cal21__cell">3</div>
        <div class="cal21__cell">4<span class="ev"></span></div>
        <div class="cal21__cell">5</div>
        <div class="cal21__cell">6</div>
        <div class="cal21__cell weekend">7<span class="ev"></span></div>
        <div class="cal21__cell today weekend">8</div>
        <div class="cal21__cell">9<span class="ev"></span></div>
        <div class="cal21__cell">10</div>
        <div class="cal21__cell">11<span class="ev"></span></div>
        <div class="cal21__cell">12</div>
        <div class="cal21__cell">13<span class="ev"></span></div>
        <div class="cal21__cell weekend">14</div>
        <div class="cal21__cell weekend">15</div>
        <div class="cal21__cell">16</div>
        <div class="cal21__cell">17<span class="ev"></span></div>
        <div class="cal21__cell">18</div>
        <div class="cal21__cell">19</div>
        <div class="cal21__cell">20<span class="ev"></span></div>
        <div class="cal21__cell weekend">21</div>
        <div class="cal21__cell weekend">22</div>
        <div class="cal21__cell">23</div>
        <div class="cal21__cell">24<span class="ev"></span></div>
        <div class="cal21__cell">25</div>
        <div class="cal21__cell">26</div>
        <div class="cal21__cell">27<span class="ev"></span></div>
        <div class="cal21__cell weekend">28</div>
        <div class="cal21__cell weekend">29</div>
        <div class="cal21__cell">30</div>
        <div class="cal21__cell other">1</div><div class="cal21__cell other">2</div><div class="cal21__cell other">3</div>
        <div class="cal21__cell other">4</div><div class="cal21__cell other weekend">5</div>
      </div>

      <div class="cal21__readout">
        <div class="cal21__readout-date" id="cal21RoDate">08</div>
        <div class="cal21__readout-body">
          <div class="cal21__readout-title" id="cal21RoTitle">Sunday, June 8</div>
          <div class="cal21__readout-sub">3 events · Sprint, Launch, Review</div>
        </div>
      </div>

      <div class="cal21__cta">Reserve this date →</div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal21,
.cal21 *,
.cal21 *::before,
.cal21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal21 ::selection {
  background: #e8643c;
  color: #fff;
}

.cal21 {
  --cream: #f6f1e9;
  --ink: #2a2520;
  --ink2: #6e665a;
  --ink3: #b5ad9e;
  --hair: #e4ddd0;
  --sun: #e8643c;
  --sun-d: #c44e2c;
  --leaf: #4a7c59;
  --sky: #f3a953;
  font-family: 'Manrope', sans-serif;
  background: var(--cream);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink);
}

@keyframes cal21-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes cal21-slide-left {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes cal21-slide-right {
  from {
    opacity: 0;
    transform: translateX(30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes cal21-sun-drift {
  0%,
    100% {
    transform: translate(0,0) scale(1);
  }

  50% {
    transform: translate(-20px, 16px) scale(1.05);
  }
}

@keyframes cal21-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(232,100,60,0.4);
  }

  50% {
    box-shadow: 0 0 0 7px rgba(232,100,60,0);
  }
}

.cal21__hero {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  width: 100%;
  min-height: 100vh;
  animation: cal21-in 0.6s ease both;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   LEFT — immersive seasonal panel
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal21__left {
  position: relative;
  overflow: hidden;
  background: linear-gradient(160deg, #f3a953 0%, #e8643c 55%, #c44e2c 100%);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 56px 52px;
  color: var(--cream);
}
/* Big sun orb */

.cal21__left::before {
  content: '';
  position: absolute;
  top: 12%;
  right: -10%;
  width: 380px;
  height: 380px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,236,200,0.9) 0%, rgba(248,200,120,0.5) 45%, transparent 70%);
  animation: cal21-sun-drift 10s ease-in-out infinite;
}
/* Layered hill silhouettes */

.cal21__hills {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 45%;
  pointer-events: none;
}

.cal21__hill {
  position: absolute;
  bottom: 0;
  left: -10%;
  width: 120%;
  border-radius: 50% 50% 0 0 / 100% 100% 0 0;
}

.cal21__hill--1 {
  height: 70%;
  background: rgba(74,124,89,0.4);
}

.cal21__hill--2 {
  height: 50%;
  background: rgba(58,98,70,0.5);
  left: 20%;
  width: 100%;
}

.cal21__hill--3 {
  height: 32%;
  background: rgba(42,72,52,0.55);
  left: -20%;
}

.cal21__left-top {
  position: relative;
  z-index: 2;
}

.cal21__eyebrow {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  opacity: 0.85;
}

.cal21__left-meta {
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 18px;
  margin-top: 8px;
  opacity: 0.9;
}

.cal21__bigmonth {
  position: relative;
  z-index: 2;
}

.cal21__bigmonth-name {
  font-family: 'Fraunces', serif;
  font-weight: 300;
  font-size: 110px;
  line-height: 0.82;
  letter-spacing: -0.02em;
}

.cal21__bigmonth-year {
  font-family: 'Fraunces', serif;
  font-size: 28px;
  font-weight: 300;
  opacity: 0.8;
  margin-top: 4px;
}

.cal21__left-foot {
  position: relative;
  z-index: 2;
  display: flex;
  gap: 28px;
}

.cal21__lf-stat {
}

.cal21__lf-num {
  font-family: 'Fraunces', serif;
  font-size: 32px;
  font-weight: 600;
  line-height: 1;
}

.cal21__lf-lbl {
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  opacity: 0.8;
  margin-top: 3px;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   RIGHT — minimalist date selector
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal21__right {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 52px;
  background: var(--cream);
  animation: cal21-slide-right 0.6s ease 0.1s both;
}

.cal21__right-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 32px;
}

.cal21__right-title {
  font-family: 'Fraunces', serif;
  font-size: 22px;
  font-weight: 600;
}

.cal21__right-nav {
  display: flex;
  gap: 6px;
}

.cal21__rn-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid var(--hair);
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--ink2);
  font-size: 15px;
  transition: all 0.2s;
  user-select: none;
}

.cal21__rn-btn:hover {
  background: var(--sun);
  color: #fff;
  border-color: var(--sun);
}

.cal21__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 10px;
}

.cal21__dw {
  text-align: center;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: var(--ink3);
  text-transform: uppercase;
}

.cal21__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
}

.cal21__cell {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 14px;
  font-size: 15px;
  font-weight: 500;
  color: var(--ink);
  cursor: pointer;
  position: relative;
  transition: all 0.18s;
}

.cal21__cell:hover {
  background: #fff;
  box-shadow: 0 4px 14px rgba(42,37,32,0.08);
}

.cal21__cell.other {
  color: var(--ink3);
  opacity: 0.4;
  pointer-events: none;
}

.cal21__cell.weekend {
  color: var(--sun-d);
}

.cal21__cell.today {
  background: var(--sun);
  color: #fff;
  font-weight: 700;
  animation: cal21-pulse 2.5s ease-in-out infinite;
}

.cal21__cell.selected:not(.today) {
  background: var(--ink);
  color: var(--cream);
  font-weight: 600;
}

.cal21__cell .ev {
  position: absolute;
  bottom: 6px;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--leaf);
}

.cal21__cell.today .ev,
.cal21__cell.selected .ev {
  background: currentColor;
}
/* Selected day readout */

.cal21__readout {
  margin-top: 36px;
  padding-top: 24px;
  border-top: 1px solid var(--hair);
  display: flex;
  align-items: center;
  gap: 18px;
}

.cal21__readout-date {
  font-family: 'Fraunces', serif;
  font-size: 50px;
  font-weight: 300;
  color: var(--sun);
  line-height: 1;
}

.cal21__readout-body {
}

.cal21__readout-title {
  font-size: 15px;
  font-weight: 700;
}

.cal21__readout-sub {
  font-size: 13px;
  color: var(--ink2);
  margin-top: 3px;
}

.cal21__cta {
  margin-top: 28px;
  padding: 16px;
  border-radius: 16px;
  background: var(--ink);
  color: var(--cream);
  text-align: center;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.03em;
  cursor: pointer;
  transition: all 0.2s;
  user-select: none;
}

.cal21__cta:hover {
  background: var(--sun);
}
/* ── Responsive: stack ── */

@media (max-width: 860px) {
  .cal21__hero {
    grid-template-columns: 1fr;
    min-height: auto;
  }

  .cal21__left {
    padding: 44px 36px;
    min-height: 360px;
    gap: 40px;
  }

  .cal21__bigmonth-name {
    font-size: 72px;
  }

  .cal21__right {
    padding: 40px 36px;
  }
}

@media (max-width: 480px) {
  .cal21__left {
    padding: 32px 24px;
  }

  .cal21__bigmonth-name {
    font-size: 56px;
  }

  .cal21__right {
    padding: 32px 24px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal21 *,
    .cal21__left::before {
    animation: none !important;
  }
}
```

## JavaScript
```js
const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
// Jun 1 2026 = Monday; cell index 7 = Jun 1
document.querySelectorAll('#cal21Grid .cal21__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal21Grid .cal21__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
    const n = parseInt(this.textContent);
    document.getElementById('cal21RoDate').textContent = String(n).padStart(2,'0');
    const dow = days[(1 + (n-1)) % 7];
    document.getElementById('cal21RoTitle').textContent = dow + ', June ' + n;
  });
});
```
