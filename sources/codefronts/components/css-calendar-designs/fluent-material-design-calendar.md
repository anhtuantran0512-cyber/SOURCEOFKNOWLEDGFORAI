---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/fluent-material-design-calendar/"
title: "Fluent / Material Design Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Two design languages in one: a Material 3 calendar with accent-ring today, filled-circle selection, state layers and JS ripple animations plus a FAB; and a…"
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fluent / Material Design Calendar
Source: https://codefronts.com/components/css-calendar-designs/fluent-material-design-calendar/

Two design languages in one: a Material 3 calendar with accent-ring today, filled-circle selection, state layers and JS ripple animations plus a FAB; and a Fluent events list with pointer-tracking reveal glow borders built via radial-gradient and mask-composite.
## HTML
```html
<div class="cal15">
  <div class="cal15__card">

    <!-- Header -->
    <div class="cal15__header">
      <div class="cal15__header-label">Select date</div>
      <div class="cal15__header-row">
        <div class="cal15__header-date">June 2026</div>
        <div class="cal15__header-nav">
          <div class="cal15__icon-btn">‹</div>
          <div class="cal15__icon-btn">›</div>
        </div>
      </div>
    </div>

    <!-- DOW -->
    <div class="cal15__dow">
      <div class="cal15__dw">S</div><div class="cal15__dw">M</div><div class="cal15__dw">T</div>
      <div class="cal15__dw">W</div><div class="cal15__dw">T</div><div class="cal15__dw">F</div><div class="cal15__dw">S</div>
    </div>

    <!-- Grid -->
    <div class="cal15__grid" id="cal15Grid">
      <div class="cal15__cell other"><div class="cal15__day">25</div></div>
      <div class="cal15__cell other"><div class="cal15__day">26</div></div>
      <div class="cal15__cell other"><div class="cal15__day">27</div></div>
      <div class="cal15__cell other"><div class="cal15__day">28</div></div>
      <div class="cal15__cell other"><div class="cal15__day">29</div></div>
      <div class="cal15__cell other"><div class="cal15__day">30</div></div>
      <div class="cal15__cell other"><div class="cal15__day">31</div></div>
      <div class="cal15__cell"><div class="cal15__day">1</div></div>
      <div class="cal15__cell"><div class="cal15__day">2</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--p"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">3</div></div>
      <div class="cal15__cell"><div class="cal15__day">4</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--t"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">5</div></div>
      <div class="cal15__cell"><div class="cal15__day">6</div></div>
      <div class="cal15__cell"><div class="cal15__day">7</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--s"></span></div></div>
      <div class="cal15__cell today selected"><div class="cal15__day">8</div></div>
      <div class="cal15__cell"><div class="cal15__day">9</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--p"></span><span class="cal15__cdot cal15__cdot--s"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">10</div></div>
      <div class="cal15__cell"><div class="cal15__day">11</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--t"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">12</div></div>
      <div class="cal15__cell"><div class="cal15__day">13</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--p"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">14</div></div>
      <div class="cal15__cell"><div class="cal15__day">15</div></div>
      <div class="cal15__cell"><div class="cal15__day">16</div></div>
      <div class="cal15__cell"><div class="cal15__day">17</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--t"></span><span class="cal15__cdot cal15__cdot--p"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">18</div></div>
      <div class="cal15__cell"><div class="cal15__day">19</div></div>
      <div class="cal15__cell"><div class="cal15__day">20</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--s"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">21</div></div>
      <div class="cal15__cell"><div class="cal15__day">22</div></div>
      <div class="cal15__cell"><div class="cal15__day">23</div></div>
      <div class="cal15__cell"><div class="cal15__day">24</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--p"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">25</div></div>
      <div class="cal15__cell"><div class="cal15__day">26</div></div>
      <div class="cal15__cell"><div class="cal15__day">27</div><div class="cal15__cell-dots"><span class="cal15__cdot cal15__cdot--s"></span></div></div>
      <div class="cal15__cell"><div class="cal15__day">28</div></div>
      <div class="cal15__cell"><div class="cal15__day">29</div></div>
      <div class="cal15__cell"><div class="cal15__day">30</div></div>
      <div class="cal15__cell other"><div class="cal15__day">1</div></div>
      <div class="cal15__cell other"><div class="cal15__day">2</div></div>
      <div class="cal15__cell other"><div class="cal15__day">3</div></div>
      <div class="cal15__cell other"><div class="cal15__day">4</div></div>
      <div class="cal15__cell other"><div class="cal15__day">5</div></div>
    </div>

    <!-- Fluent reveal events -->
    <div class="cal15__fluent">
      <div class="cal15__fluent-label">Today · 3 events</div>
      <div class="cal15__event" id="ev1">
        <div class="cal15__event-icon cal15__event-icon--p">📋</div>
        <div class="cal15__event-body">
          <div class="cal15__event-name">Sprint Planning</div>
          <div class="cal15__event-time">10:00 AM · Teams</div>
        </div>
        <div class="cal15__event-chip" style="background:var(--primary-cont);color:var(--primary-ct)">1h</div>
      </div>
      <div class="cal15__event" id="ev2">
        <div class="cal15__event-icon cal15__event-icon--t">🚀</div>
        <div class="cal15__event-body">
          <div class="cal15__event-name">Product Launch</div>
          <div class="cal15__event-time">2:00 PM · All-hands</div>
        </div>
        <div class="cal15__event-chip" style="background:#ffd8e4;color:#31111d">2h</div>
      </div>
      <div class="cal15__event" id="ev3">
        <div class="cal15__event-icon cal15__event-icon--s">🎨</div>
        <div class="cal15__event-body">
          <div class="cal15__event-name">Design Review</div>
          <div class="cal15__event-time">4:30 PM · Figma</div>
        </div>
        <div class="cal15__event-chip" style="background:#e2e0f0;color:#1d192b">45m</div>
      </div>
    </div>

    <!-- Material FAB -->
    <div class="cal15__fab" id="cal15Fab">+</div>

  </div>
</div>
```
## CSS
```css
.cal15,
.cal15 *,
.cal15 *::before,
.cal15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal15 ::selection {
  background: #6750a4;
  color: #fff;
}

.cal15 {
  /* Material 3 tonal palette */
  --primary: #6750a4;
  --primary-c: #ffffff;
  --primary-ct: #21005d;
  --primary-cont: #eaddff;
  --surface: #fef7ff;
  --surface-2: #f7f2fa;
  --surface-v: #e7e0ec;
  --on-surface: #1d1b20;
  --on-surface-v: #49454f;
  --outline: #cac4d0;
  --tertiary: #7d5260;
  --secondary: #625b71;
  /* Fluent acrylic */
  --fluent-glow: rgba(103,80,164,0.4);
  font-family: 'Roboto', sans-serif;
  background: #e8def8;
  background-image: radial-gradient(circle at 30% 20%, #f0e7fb 0%, #e2d4f5 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--on-surface);
}

@keyframes cal15-in {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.98);
  }

  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes cal15-ripple {
  from {
    transform: scale(0);
    opacity: 0.5;
  }

  to {
    transform: scale(2.6);
    opacity: 0;
  }
}

@keyframes cal15-fab-in {
  from {
    transform: scale(0) rotate(-90deg);
  }

  to {
    transform: scale(1) rotate(0);
  }
}

.cal15__card {
  background: var(--surface);
  border-radius: 28px;
  max-width: 400px;
  width: 100%;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 8px 24px rgba(103,80,164,0.18), 0 24px 48px rgba(103,80,164,0.12);
  animation: cal15-in 0.5s cubic-bezier(0.2,0,0,1) both;
  position: relative;
}
/* ── Header (Material filled style) ── */

.cal15__header {
  background: var(--primary-cont);
  padding: 24px 24px 20px;
  position: relative;
}

.cal15__header-label {
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.06em;
  color: var(--primary-ct);
  opacity: 0.7;
  text-transform: uppercase;
}

.cal15__header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 6px;
}

.cal15__header-date {
  font-family: 'Roboto Flex', sans-serif;
  font-size: 30px;
  font-weight: 600;
  color: var(--primary-ct);
  letter-spacing: -0.01em;
}

.cal15__header-nav {
  display: flex;
  gap: 4px;
}
/* Material icon button with state layer + ripple */

.cal15__icon-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--primary-ct);
  font-size: 20px;
  position: relative;
  overflow: hidden;
  transition: background 0.2s;
  user-select: none;
}

.cal15__icon-btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--primary-ct);
  opacity: 0;
  transition: opacity 0.15s;
}

.cal15__icon-btn:hover::before {
  opacity: 0.08;
}

.cal15__icon-btn:active::before {
  opacity: 0.12;
}
/* ── DOW row ── */

.cal15__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 16px 16px 8px;
}

.cal15__dw {
  text-align: center;
  font-size: 12px;
  font-weight: 500;
  color: var(--on-surface-v);
}
/* ── Grid ── */

.cal15__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 0 16px 16px;
  gap: 2px;
}

.cal15__cell {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
}
/* The day number sits in a circular state-layer target */

.cal15__day {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 500;
  color: var(--on-surface);
  position: relative;
  overflow: hidden;
  transition: background 0.2s, color 0.2s;
}
/* Material state layer on hover */

.cal15__day::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--primary);
  opacity: 0;
  transition: opacity 0.15s;
}

.cal15__cell:hover:not(.other) .cal15__day::before {
  opacity: 0.08;
}

.cal15__cell.other .cal15__day {
  color: var(--on-surface-v);
  opacity: 0.38;
  pointer-events: none;
}
/* ── Material TODAY: bold accent ring ── */

.cal15__cell.today .cal15__day {
  border: 1px solid var(--primary);
  color: var(--primary);
  font-weight: 700;
}
/* ── Material SELECTED: filled accent circle ── */

.cal15__cell.selected .cal15__day {
  background: var(--primary);
  color: var(--primary-c);
  font-weight: 700;
}

.cal15__cell.selected.today .cal15__day {
  border-color: transparent;
}
/* Ripple element injected by JS */

.cal15__rip {
  position: absolute;
  border-radius: 50%;
  background: var(--primary);
  opacity: 0.4;
  pointer-events: none;
  transform: scale(0);
  animation: cal15-ripple 0.55s ease-out forwards;
}
/* Event indicator dots (Material small) */

.cal15__cell-dots {
  position: absolute;
  bottom: 3px;
  display: flex;
  gap: 3px;
}

.cal15__cdot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
}

.cal15__cdot--p {
  background: var(--primary);
}

.cal15__cdot--t {
  background: var(--tertiary);
}

.cal15__cdot--s {
  background: var(--secondary);
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   FLUENT SECTION — reveal-on-hover
   glow border that follows the card,
   acrylic translucency.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal15__fluent {
  margin: 0 16px 16px;
  padding: 4px;
  border-radius: 18px;
  background: var(--surface-2);
}

.cal15__fluent-label {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--on-surface-v);
  padding: 10px 14px 6px;
}

.cal15__event {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 14px;
  border-radius: 14px;
  cursor: pointer;
  position: relative;
  background: var(--surface);
  margin-bottom: 4px;
  transition: background 0.2s, box-shadow 0.2s;
  /* Fluent reveal border base */
  border: 1px solid transparent;
}

.cal15__event:last-child {
  margin-bottom: 0;
}
/* Fluent glow-border reveal on hover */

.cal15__event::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 14px;
  padding: 1px;
  background: radial-gradient(120px circle at var(--mx, 50%) var(--my, 50%), var(--fluent-glow), transparent 60%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.2s;
  pointer-events: none;
}

.cal15__event:hover {
  box-shadow: 0 2px 8px rgba(103,80,164,0.12);
}

.cal15__event:hover::after {
  opacity: 1;
}

.cal15__event-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}

.cal15__event-icon--p {
  background: var(--primary-cont);
}

.cal15__event-icon--t {
  background: #ffd8e4;
}

.cal15__event-icon--s {
  background: #e2e0f0;
}

.cal15__event-body {
  flex: 1;
  min-width: 0;
}

.cal15__event-name {
  font-size: 14px;
  font-weight: 500;
  color: var(--on-surface);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal15__event-time {
  font-size: 12px;
  color: var(--on-surface-v);
  margin-top: 1px;
}

.cal15__event-chip {
  font-size: 11px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: 8px;
  flex-shrink: 0;
}
/* Material FAB */

.cal15__fab {
  position: absolute;
  bottom: 20px;
  right: 20px;
  width: 56px;
  height: 56px;
  border-radius: 18px;
  background: var(--primary-cont);
  color: var(--primary-ct);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  cursor: pointer;
  box-shadow: 0 3px 8px rgba(0,0,0,0.2), 0 1px 3px rgba(0,0,0,0.12);
  transition: box-shadow 0.2s, transform 0.15s;
  animation: cal15-fab-in 0.5s cubic-bezier(0.2,0,0,1) 0.3s both;
  overflow: hidden;
  z-index: 5;
}

.cal15__fab:hover {
  box-shadow: 0 5px 14px rgba(0,0,0,0.28);
}

.cal15__fab:active {
  transform: scale(0.94);
}

.cal15__fab::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--primary-ct);
  opacity: 0;
  transition: opacity 0.15s;
}

.cal15__fab:hover::before {
  opacity: 0.08;
}

@media (prefers-reduced-motion: reduce) {
  .cal15 *,
    .cal15__rip {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
// Material ripple on date cells
function ripple(target, e) {
  const day = target.querySelector('.cal15__day');
  const rect = day.getBoundingClientRect();
  const rip = document.createElement('span');
  rip.className = 'cal15__rip';
  const size = rect.width;
  rip.style.width = rip.style.height = size + 'px';
  const x = (e.clientX || rect.left + rect.width/2) - rect.left - size/2;
  const y = (e.clientY || rect.top + rect.height/2) - rect.top - size/2;
  rip.style.left = x + 'px';
  rip.style.top = y + 'px';
  day.appendChild(rip);
  setTimeout(() => rip.remove(), 600);
}

document.querySelectorAll('#cal15Grid .cal15__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function(e) {
    document.querySelectorAll('#cal15Grid .cal15__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
    ripple(this, e);
  });
});

// Fluent pointer-tracking glow border
document.querySelectorAll('.cal15__event').forEach(ev => {
  ev.addEventListener('pointermove', function(e) {
    const r = this.getBoundingClientRect();
    this.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    this.style.setProperty('--my', (e.clientY - r.top) + 'px');
  });
});

// FAB ripple
const fab = document.getElementById('cal15Fab');
fab.addEventListener('click', function(e) {
  const rect = this.getBoundingClientRect();
  const rip = document.createElement('span');
  rip.className = 'cal15__rip';
  rip.style.width = rip.style.height = rect.width + 'px';
  rip.style.left = (e.clientX - rect.left - rect.width/2) + 'px';
  rip.style.top = (e.clientY - rect.top - rect.width/2) + 'px';
  rip.style.borderRadius = '50%';
  this.appendChild(rip);
  setTimeout(() => rip.remove(), 600);
});
```
