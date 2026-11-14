---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/bento-grid-style-booking-system/"
title: "Bento Grid Style Booking System"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Apple-style asymmetric bento on a 7-column grid."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Grid Style Booking System
Source: https://codefronts.com/components/css-calendar-designs/bento-grid-style-booking-system/

Apple-style asymmetric bento on a 7-column grid. Special cells break uniformity: a 2x2 gradient today hero with event chips, 2x1 event cells with icon+title+time, and a 1x2 cell holding an animated SVG progress ring. Cells lift and shadow on hover.
## HTML
```html
<div class="cal23">
  <div class="cal23__wrap">

    <div class="cal23__head">
      <div>
        <div class="cal23__title">June <span>2026</span></div>
        <div class="cal23__sub">Bento booking · 4 of 7 days available</div>
      </div>
      <div class="cal23__nav">
        <div class="cal23__nav-btn">‹</div>
        <div class="cal23__nav-btn">›</div>
      </div>
    </div>

    <!-- Bento: showing the current week with asymmetric emphasis -->
    <div class="cal23__bento" id="cal23Bento">

      <!-- TODAY hero spans 2x2 -->
      <div class="cal23__cell cal23__cell--today">
        <div class="cal23__today-top">
          <div>
            <div class="cal23__today-n">8</div>
            <div class="cal23__today-label">Sunday · Today</div>
          </div>
          <div class="cal23__today-badge">3 events</div>
        </div>
        <div class="cal23__today-events">
          <div class="cal23__today-ev">10:00 Sprint</div>
          <div class="cal23__today-ev">14:00 Launch</div>
        </div>
      </div>

      <!-- Mon 9 -->
      <div class="cal23__cell weekend">
        <div class="cal23__n">9</div>
        <div class="dow-mini">Mon</div>
        <div class="cal23__dots"><span style="background:var(--accent2)"></span></div>
      </div>

      <!-- Tue 10 -->
      <div class="cal23__cell">
        <div class="cal23__n">10</div>
        <div class="dow-mini">Tue</div>
      </div>

      <!-- Wed 11: event-rich 2x1 -->
      <div class="cal23__cell cal23__cell--2x1 cal23__cell--event">
        <div style="display:flex;align-items:flex-start;justify-content:space-between">
          <div><div class="cal23__n">11</div><div class="dow-mini">Wed</div></div>
        </div>
        <div class="cal23__ev-row">
          <div class="cal23__ev-icon" style="background:rgba(244,63,94,0.12);color:var(--rose)">🚀</div>
          <div class="cal23__ev-text">
            <div class="cal23__ev-name">Product Launch</div>
            <div class="cal23__ev-time">2:00 PM · All-hands</div>
          </div>
        </div>
      </div>

      <!-- Thu 12 -->
      <div class="cal23__cell">
        <div class="cal23__n">12</div>
        <div class="dow-mini">Thu</div>
      </div>

      <!-- Fri 13: progress ring cell 1x2 -->
      <div class="cal23__cell cal23__cell--1x2">
        <div style="display:flex;align-items:flex-start;justify-content:space-between">
          <div><div class="cal23__n">13</div><div class="dow-mini">Fri</div></div>
        </div>
        <div class="cal23__ring-wrap">
          <div style="position:relative;width:60px;height:60px">
            <svg class="cal23__ring" width="60" height="60" viewBox="0 0 60 60">
              <circle class="cal23__ring-bg" cx="30" cy="30" r="24"></circle>
              <circle class="cal23__ring-fg" cx="30" cy="30" r="24" stroke="var(--green)" style="--target:45.2; stroke-dashoffset:150.8"></circle>
            </svg>
            <div class="cal23__ring-label">70%</div>
          </div>
        </div>
      </div>

      <!-- Sat 14 -->
      <div class="cal23__cell weekend">
        <div class="cal23__n">14</div>
        <div class="dow-mini">Sat</div>
        <div class="cal23__dots"><span style="background:var(--amber)"></span><span style="background:var(--accent)"></span></div>
      </div>

      <!-- Sun 15 -->
      <div class="cal23__cell weekend">
        <div class="cal23__n">15</div>
        <div class="dow-mini">Sun</div>
      </div>

      <!-- Mon 16 -->
      <div class="cal23__cell">
        <div class="cal23__n">16</div>
        <div class="dow-mini">Mon</div>
      </div>

      <!-- Tue 17: event 2x1 -->
      <div class="cal23__cell cal23__cell--2x1 cal23__cell--event">
        <div><div class="cal23__n">17</div><div class="dow-mini">Tue</div></div>
        <div class="cal23__ev-row">
          <div class="cal23__ev-icon" style="background:rgba(6,182,212,0.12);color:var(--accent2)">📊</div>
          <div class="cal23__ev-text">
            <div class="cal23__ev-name">Demo Day + Q2 Report</div>
            <div class="cal23__ev-time">11:00 AM · 2 sessions</div>
          </div>
        </div>
      </div>

      <!-- Wed 18 -->
      <div class="cal23__cell">
        <div class="cal23__n">18</div>
        <div class="dow-mini">Wed</div>
      </div>

    </div>

  </div>
</div>
```
## CSS
```css
.cal23,
.cal23 *,
.cal23 *::before,
.cal23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal23 ::selection {
  background: #111;
  color: #fff;
}

.cal23 {
  --bg: #ececef;
  --card: #ffffff;
  --ink: #18181b;
  --ink2: #71717a;
  --ink3: #a1a1aa;
  --line: #e4e4e7;
  --accent: #4f46e5;
  --accent2: #06b6d4;
  --green: #10b981;
  --amber: #f59e0b;
  --rose: #f43f5e;
  font-family: 'Geist', -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 20px;
  color: var(--ink);
}

@keyframes cal23-in {
  from {
    opacity: 0;
    transform: translateY(14px) scale(0.99);
  }

  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes cal23-ring {
  to {
    stroke-dashoffset: var(--target);
  }
}

.cal23__wrap {
  max-width: 720px;
  width: 100%;
  animation: cal23-in 0.5s ease both;
}
/* ── Header ── */

.cal23__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 16px;
  padding: 0 2px;
}

.cal23__title {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.cal23__title span {
  color: var(--ink3);
  font-weight: 500;
}

.cal23__sub {
  font-size: 13px;
  color: var(--ink2);
  margin-top: 2px;
}

.cal23__nav {
  display: flex;
  gap: 6px;
}

.cal23__nav-btn {
  width: 38px;
  height: 38px;
  border-radius: 12px;
  background: var(--card);
  border: 1px solid var(--line);
  cursor: pointer;
  color: var(--ink2);
  font-size: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.18s;
  user-select: none;
}

.cal23__nav-btn:hover {
  border-color: var(--ink);
  color: var(--ink);
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   BENTO GRID — asymmetric spans.
   7 base columns; special cells span
   2×2 / 2×1 / 1×2 for the bento look.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal23__bento {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 78px;
  gap: 8px;
}

.cal23__cell {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 12px;
  cursor: pointer;
  transition: all 0.18s;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.cal23__cell:hover {
  border-color: var(--ink);
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(24,24,27,0.1);
}

.cal23__cell.other {
  background: transparent;
  border-color: transparent;
  pointer-events: none;
}

.cal23__cell.other .cal23__n {
  color: var(--ink3);
  opacity: 0.5;
}

.cal23__n {
  font-size: 16px;
  font-weight: 600;
  line-height: 1;
}

.cal23__cell .dow-mini {
  font-size: 10px;
  color: var(--ink3);
  font-weight: 500;
  margin-top: 2px;
}
/* span helpers */

.cal23__cell--2x2 {
  grid-column: span 2;
  grid-row: span 2;
}

.cal23__cell--2x1 {
  grid-column: span 2;
}

.cal23__cell--1x2 {
  grid-row: span 2;
}
/* ── TODAY: big 2×2 hero cell ── */

.cal23__cell--today {
  grid-column: span 2;
  grid-row: span 2;
  background: linear-gradient(135deg, var(--accent), #7c3aed);
  border-color: transparent;
  color: #fff;
  padding: 16px;
  justify-content: space-between;
}

.cal23__cell--today:hover {
  box-shadow: 0 14px 32px rgba(79,70,229,0.4);
}

.cal23__today-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.cal23__today-n {
  font-size: 40px;
  font-weight: 800;
  line-height: 0.9;
}

.cal23__today-badge {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: rgba(255,255,255,0.2);
  padding: 4px 9px;
  border-radius: 20px;
}

.cal23__today-label {
  font-size: 12px;
  opacity: 0.8;
}

.cal23__today-events {
  display: flex;
  gap: 5px;
  margin-top: 8px;
}

.cal23__today-ev {
  flex: 1;
  background: rgba(255,255,255,0.16);
  border-radius: 8px;
  padding: 6px 8px;
  font-size: 10px;
  font-weight: 500;
}
/* progress ring cell (an event with a goal) */

.cal23__ring-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
}

.cal23__ring {
  transform: rotate(-90deg);
}

.cal23__ring-bg {
  fill: none;
  stroke: var(--line);
  stroke-width: 6;
}

.cal23__ring-fg {
  fill: none;
  stroke-width: 6;
  stroke-linecap: round;
  stroke-dasharray: 150.8;
  animation: cal23-ring 1.1s cubic-bezier(0.22,1,0.36,1) forwards;
}

.cal23__ring-label {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  font-size: 13px;
  font-weight: 700;
}
/* event-rich 2x1 cell */

.cal23__cell--event {
  justify-content: space-between;
}

.cal23__cell--event .cal23__ev-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: auto;
}

.cal23__ev-icon {
  width: 24px;
  height: 24px;
  border-radius: 7px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  flex-shrink: 0;
}

.cal23__ev-text {
  min-width: 0;
}

.cal23__ev-name {
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal23__ev-time {
  font-size: 10px;
  color: var(--ink2);
}
/* selected */

.cal23__cell.selected {
  border-color: var(--accent);
  box-shadow: 0 0 0 2px var(--accent);
}
/* mini event dots */

.cal23__dots {
  display: flex;
  gap: 3px;
  margin-top: auto;
}

.cal23__dots span {
  width: 5px;
  height: 5px;
  border-radius: 50%;
}
/* corner pill for weekend */

.cal23__cell.weekend .cal23__n {
  color: var(--accent);
}

@media (max-width: 600px) {
  .cal23__bento {
    grid-auto-rows: 64px;
    gap: 6px;
  }

  .cal23__today-n {
    font-size: 30px;
  }

  .cal23__title {
    font-size: 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal23 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal23Bento .cal23__cell:not(.other):not(.cal23__cell--today)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal23Bento .cal23__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
