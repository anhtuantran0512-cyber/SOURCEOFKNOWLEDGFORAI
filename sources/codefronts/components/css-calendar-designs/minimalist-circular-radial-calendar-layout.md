---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/minimalist-circular-radial-calendar-layout/"
title: "Minimalist Circular / Radial Calendar Layout"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Days arranged around an elegant ring instead of a grid, positioned with trig-computed transforms."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Circular / Radial Calendar Layout
Source: https://codefronts.com/components/css-calendar-designs/minimalist-circular-radial-calendar-layout/

Days arranged around an elegant ring instead of a grid, positioned with trig-computed transforms. Concentric guide rings, a slowly rotating tick ring, a serif center hub, gold pulsing today, gold-outline selection, and radially placed weekday labels.
## HTML
```html
<div class="cal16">
  <div class="cal16__stage" id="cal16Stage">

    <div class="cal16__ring cal16__ring--1"></div>
    <div class="cal16__ring cal16__ring--2"></div>
    <div class="cal16__ring cal16__ring--3"></div>

    <div class="cal16__ticks" id="cal16Ticks"></div>
    <div class="cal16__wlabels" id="cal16Wlabels"></div>

    <!-- Center hub -->
    <div class="cal16__center">
      <div class="cal16__center-month">June</div>
      <div class="cal16__center-year">2026</div>
      <div class="cal16__center-divider"></div>
      <div class="cal16__center-today">the 8th</div>
      <div class="cal16__center-events">3 events today</div>
    </div>

    <!-- Days injected by JS around the ring -->
    <div id="cal16Days"></div>

    <div class="cal16__nav">
      <div class="cal16__nav-btn">‹</div>
      <div class="cal16__nav-btn">›</div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal16,
.cal16 *,
.cal16 *::before,
.cal16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal16 ::selection {
  background: #c89b6a;
  color: #fff;
}

.cal16 {
  --bg: #faf8f4;
  --ink: #2b2820;
  --ink2: #837c6e;
  --ink3: #c4bcab;
  --hair: #e7e1d5;
  --gold: #c89b6a;
  --gold-d: #a47c4c;
  --rose: #c97a6a;
  --ring: #ddd5c6;
  font-family: 'Jost', sans-serif;
  background: var(--bg);
  background-image: radial-gradient(circle at center, #fffdfa 0%, #f2ede3 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

@keyframes cal16-in {
  from {
    opacity: 0;
    transform: scale(0.9) rotate(-8deg);
  }

  to {
    opacity: 1;
    transform: scale(1) rotate(0);
  }
}

@keyframes cal16-spin-ring {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

@keyframes cal16-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(200,155,106,0.5);
  }

  50% {
    box-shadow: 0 0 0 8px rgba(200,155,106,0);
  }
}

.cal16__stage {
  position: relative;
  width: 560px;
  height: 560px;
  max-width: 92vw;
  max-height: 92vw;
  animation: cal16-in 0.7s cubic-bezier(0.22,1,0.36,1) both;
}
/* Decorative concentric rings */

.cal16__ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid var(--hair);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
/* Outer ring sits just inside where the day numbers orbit */

.cal16__ring--1 {
  width: 75%;
  height: 75%;
}
/* Middle dashed ring */

.cal16__ring--2 {
  width: 52%;
  height: 52%;
  border-style: dashed;
  border-color: var(--ring);
}
/* Inner ring hugs the center hub */

.cal16__ring--3 {
  width: 30%;
  height: 30%;
}
/* Slowly rotating tick marks ring — anchored at exact center, ticks pushed out by transform */

.cal16__ticks {
  position: absolute;
  width: 0;
  height: 0;
  top: 50%;
  left: 50%;
  animation: cal16-spin-ring 160s linear infinite;
}

.cal16__tick {
  position: absolute;
  top: 0;
  left: 0;
  width: 1px;
  height: 6px;
  background: var(--ink3);
  transform-origin: 0 0;
}
/* ── Day cells positioned around the circle ──
   Each cell uses: rotate(θ) translateY(-radius) rotate(-θ)
   to sit on the ring while keeping text upright.
   θ set inline per cell. ── */

.cal16__day {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 42px;
  height: 42px;
  margin: -21px 0 0 -21px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-family: 'Jost', sans-serif;
  font-size: 14px;
  font-weight: 400;
  color: var(--ink);
  cursor: pointer;
  transition: all 0.2s;
}

.cal16__day:hover {
  background: #fff;
  box-shadow: 0 4px 14px rgba(43,40,32,0.1);
}

.cal16__day.weekend {
  color: var(--rose);
}

.cal16__day.today {
  background: var(--gold);
  color: #fff;
  font-weight: 600;
  animation: cal16-pulse 2.5s ease-in-out infinite;
}

.cal16__day.selected:not(.today) {
  background: #fff;
  color: var(--gold-d);
  font-weight: 600;
  box-shadow: 0 0 0 1.5px var(--gold);
}
/* event dot */

.cal16__day .ev {
  position: absolute;
  bottom: 4px;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--rose);
}

.cal16__day.today .ev {
  background: #fff;
}
/* ── Center hub ── */

.cal16__center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 38%;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.cal16__center-month {
  font-family: 'Cormorant', serif;
  font-size: 54px;
  font-weight: 400;
  line-height: 0.9;
  color: var(--ink);
  letter-spacing: 0.01em;
}

.cal16__center-year {
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.4em;
  color: var(--ink3);
  margin-top: 8px;
  padding-left: 0.4em;
}

.cal16__center-divider {
  width: 40px;
  height: 1px;
  background: var(--gold);
  margin: 14px 0;
  opacity: 0.5;
}

.cal16__center-today {
  font-family: 'Cormorant', serif;
  font-style: italic;
  font-size: 18px;
  color: var(--ink2);
}

.cal16__center-events {
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--ink3);
  margin-top: 6px;
  text-transform: uppercase;
}
/* Weekday labels on the outer edge */

.cal16__wlabels {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.cal16__wlabel {
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--ink3);
  transform-origin: 0 0;
}
/* Nav buttons */

.cal16__nav {
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
}

.cal16__nav-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #fff;
  border: 1px solid var(--hair);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--gold-d);
  font-size: 15px;
  transition: all 0.2s;
  user-select: none;
  box-shadow: 0 2px 8px rgba(43,40,32,0.06);
}

.cal16__nav-btn:hover {
  background: var(--gold);
  color: #fff;
  border-color: var(--gold);
}

@media (max-width: 600px) {
  .cal16__center-month {
    font-size: 38px;
  }

  .cal16__day {
    width: 34px;
    height: 34px;
    margin: -17px 0 0 -17px;
    font-size: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal16 *,
    .cal16__ticks {
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.getElementById('cal16Stage');
  const daysWrap = document.getElementById('cal16Days');
  const ticksWrap = document.getElementById('cal16Ticks');
  const wlabelsWrap = document.getElementById('cal16Wlabels');

  const DAYS = 30;
  const today = 8;
  const events = {2:1, 4:1, 7:1, 8:1, 9:1, 11:1, 13:1, 17:1, 20:1, 25:1};
  // June 1, 2026 is a Monday → Sunday index. weekday of day d:
  // Jun 1 = Mon(1). day-of-week = (d) % 7 where 0=Sun... compute:
  const firstDow = 1; // Monday
  const isWeekend = d => { const dow = (firstDow + (d-1)) % 7; return dow === 0 || dow === 6; };

  const R = 210; // radius for day-number ring (stage radius = 280)

  for (let d = 1; d <= DAYS; d++) {
    const angle = (d / DAYS) * 360 - 90; // start at top
    const rad = angle * Math.PI / 180;
    const x = Math.cos(rad) * R;
    const y = Math.sin(rad) * R;
    const el = document.createElement('div');
    el.className = 'cal16__day';
    if (d === today) el.classList.add('today');
    if (isWeekend(d)) el.classList.add('weekend');
    el.style.transform = `translate(${x}px, ${y}px)`;
    el.innerHTML = d + (events[d] ? '<span class="ev"></span>' : '');
    el.addEventListener('click', function() {
      daysWrap.querySelectorAll('.cal16__day').forEach(c => c.classList.remove('selected'));
      this.classList.add('selected');
    });
    daysWrap.appendChild(el);
  }

  // tick marks — placed by rotate + translateY from the dead-center anchor
  const tickR = 232;
  for (let i = 0; i < 60; i++) {
    const t = document.createElement('div');
    t.className = 'cal16__tick';
    const ang = (i / 60) * 360;
    t.style.transform = `rotate(${ang}deg) translate(0, ${-tickR}px)`;
    if (i % 5 === 0) { t.style.height = '10px'; t.style.opacity = '0.6'; }
    ticksWrap.appendChild(t);
  }

  // weekday labels on the outer edge
  const labels = ['S','M','T','W','T','F','S'];
  const RL = 256;
  for (let i = 0; i < 7; i++) {
    const ang = (i / 7) * 360 - 90;
    const rad = ang * Math.PI / 180;
    const x = Math.cos(rad) * RL;
    const y = Math.sin(rad) * RL;
    const l = document.createElement('div');
    l.className = 'cal16__wlabel';
    l.style.transform = `translate(${x}px, ${y}px) translate(-50%, -50%)`;
    l.textContent = labels[i];
    wlabelsWrap.appendChild(l);
  }
})();
```
