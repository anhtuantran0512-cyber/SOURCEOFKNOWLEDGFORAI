---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/horizontal-scroll-timeline-calendar/"
title: "Horizontal Scroll / Timeline Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A fitness/booking-app date strip using display:flex with overflow-x:auto and scroll-snap."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Scroll / Timeline Calendar
Source: https://codefronts.com/components/css-calendar-designs/horizontal-scroll-timeline-calendar/

A fitness/booking-app date strip using display:flex with overflow-x:auto and scroll-snap. Day pills spring on hover, today glows lime, edge gradient masks hint at more, and a selected-day detail panel renders a vertical timeline with connector line and node dots.
## HTML
```html
<div class="cal11">
  <div class="cal11__wrap">

    <div class="cal11__head">
      <div class="cal11__title-block">
        <div class="cal11__eyebrow">June 2026 · Week 23</div>
        <div class="cal11__title">Schedule</div>
      </div>
      <div class="cal11__month-toggle">
        <div class="cal11__mt-btn">‹</div>
        <div class="cal11__mt-btn">›</div>
      </div>
    </div>

    <div class="cal11__strip-wrap">
      <div class="cal11__strip" id="cal11Strip">
        <div class="cal11__day weekend"><div class="cal11__day-dow">Sun</div><div class="cal11__day-num">1</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Mon</div><div class="cal11__day-num">2</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--l"></span></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Tue</div><div class="cal11__day-num">3</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Wed</div><div class="cal11__day-num">4</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--y"></span><span class="cal11__pip cal11__pip--c"></span></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Thu</div><div class="cal11__day-num">5</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Fri</div><div class="cal11__day-num">6</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--v"></span></div></div>
        <div class="cal11__day weekend"><div class="cal11__day-dow">Sat</div><div class="cal11__day-num">7</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>

        <div class="cal11__day today weekend"><div class="cal11__day-dow">Sun</div><div class="cal11__day-num">8</div><div class="cal11__day-mon">Today</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--l"></span><span class="cal11__pip cal11__pip--c"></span><span class="cal11__pip cal11__pip--y"></span></div></div>

        <div class="cal11__day selected"><div class="cal11__day-dow">Mon</div><div class="cal11__day-num">9</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--y"></span><span class="cal11__pip cal11__pip--v"></span></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Tue</div><div class="cal11__day-num">10</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Wed</div><div class="cal11__day-num">11</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--c"></span><span class="cal11__pip cal11__pip--l"></span></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Thu</div><div class="cal11__day-num">12</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Fri</div><div class="cal11__day-num">13</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--y"></span></div></div>
        <div class="cal11__day weekend"><div class="cal11__day-dow">Sat</div><div class="cal11__day-num">14</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day weekend"><div class="cal11__day-dow">Sun</div><div class="cal11__day-num">15</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Mon</div><div class="cal11__day-num">16</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Tue</div><div class="cal11__day-num">17</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--c"></span><span class="cal11__pip cal11__pip--v"></span></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Wed</div><div class="cal11__day-num">18</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Thu</div><div class="cal11__day-num">19</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
        <div class="cal11__day"><div class="cal11__day-dow">Fri</div><div class="cal11__day-num">20</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"><span class="cal11__pip cal11__pip--l"></span></div></div>
        <div class="cal11__day weekend"><div class="cal11__day-dow">Sat</div><div class="cal11__day-num">21</div><div class="cal11__day-mon">Jun</div><div class="cal11__day-pips"></div></div>
      </div>
    </div>

    <div class="cal11__detail">
      <div class="cal11__detail-head">
        <div class="cal11__detail-date">Monday, <span>June 9</span></div>
        <div class="cal11__detail-count">2 events</div>
      </div>
      <div class="cal11__timeline">
        <div class="cal11__tl-item cal11__tl-item--y">
          <div class="cal11__tl-time">10:00 — 11:00 AM</div>
          <div class="cal11__tl-name">Sprint Planning</div>
          <div class="cal11__tl-meta">Zoom · 8 attendees</div>
        </div>
        <div class="cal11__tl-item cal11__tl-item--v">
          <div class="cal11__tl-time">3:00 — 3:30 PM</div>
          <div class="cal11__tl-name">1:1 with Sam</div>
          <div class="cal11__tl-meta">Office · Recurring</div>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal11,
.cal11 *,
.cal11 *::before,
.cal11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal11 ::selection {
  background: #ff4d4d;
  color: #fff;
}

.cal11 {
  --bg: #0e0e12;
  --surface: #16161d;
  --card: #1d1d27;
  --card2: #25252f;
  --border: rgba(255,255,255,0.08);
  --text: #f5f5f7;
  --text2: #9a9aa8;
  --text3: #55555f;
  --lime: #d4ff3d;
  --coral: #ff5e4d;
  --cyan: #3dd4ff;
  --violet: #9d7dff;
  font-family: 'Sora', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 0;
  color: var(--text);
}

@keyframes cal11-in {
  from {
    opacity: 0;
    transform: translateY(16px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes cal11-glow {
  0%,
    100% {
    box-shadow: 0 0 20px rgba(212,255,61,0.4);
  }

  50% {
    box-shadow: 0 0 36px rgba(212,255,61,0.65);
  }
}

.cal11__wrap {
  width: 100%;
  max-width: 720px;
  padding: 0 24px;
  animation: cal11-in 0.5s ease both;
}
/* ── Header ── */

.cal11__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 28px;
  padding: 0 4px;
}

.cal11__title-block {
}

.cal11__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--lime);
  margin-bottom: 6px;
}

.cal11__title {
  font-family: 'Archivo Black', sans-serif;
  font-size: 40px;
  line-height: 0.95;
  letter-spacing: -0.02em;
}

.cal11__month-toggle {
  display: flex;
  gap: 6px;
}

.cal11__mt-btn {
  width: 42px;
  height: 42px;
  border-radius: 14px;
  background: var(--card);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--text2);
  font-size: 18px;
  transition: all 0.2s;
  user-select: none;
}

.cal11__mt-btn:hover {
  background: var(--card2);
  color: var(--lime);
  border-color: var(--lime);
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   HORIZONTAL SCROLL STRIP — the core.
   display: flex; overflow-x: auto;
   scroll-snap for that booking-app feel.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal11__strip {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding: 8px 4px 20px;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
  scrollbar-color: var(--card2) transparent;
}

.cal11__strip::-webkit-scrollbar {
  height: 6px;
}

.cal11__strip::-webkit-scrollbar-track {
  background: transparent;
}

.cal11__strip::-webkit-scrollbar-thumb {
  background: var(--card2);
  border-radius: 3px;
}

.cal11__strip::-webkit-scrollbar-thumb:hover {
  background: var(--text3);
}
/* Each day pill */

.cal11__day {
  flex: 0 0 auto;
  width: 76px;
  padding: 18px 10px 14px;
  border-radius: 20px;
  background: var(--card);
  border: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  scroll-snap-align: center;
  transition: all 0.22s cubic-bezier(0.34,1.56,0.64,1);
  position: relative;
}

.cal11__day:hover {
  transform: translateY(-4px);
  border-color: var(--text3);
  background: var(--card2);
}

.cal11__day-dow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text2);
}

.cal11__day-num {
  font-family: 'Archivo Black', sans-serif;
  font-size: 26px;
  line-height: 1;
  color: var(--text);
}

.cal11__day-mon {
  font-size: 10px;
  font-weight: 600;
  color: var(--text3);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
/* Event pips on the pill */

.cal11__day-pips {
  display: flex;
  gap: 4px;
  height: 6px;
}

.cal11__pip {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.cal11__pip--l {
  background: var(--lime);
}

.cal11__pip--c {
  background: var(--coral);
}

.cal11__pip--y {
  background: var(--cyan);
}

.cal11__pip--v {
  background: var(--violet);
}
/* Weekend tint */

.cal11__day.weekend .cal11__day-dow {
  color: var(--coral);
}
/* Today */

.cal11__day.today {
  background: var(--lime);
  border-color: var(--lime);
  animation: cal11-glow 2.5s ease-in-out infinite;
}

.cal11__day.today .cal11__day-dow,
.cal11__day.today .cal11__day-num,
.cal11__day.today .cal11__day-mon {
  color: #0e0e12;
}

.cal11__day.today .cal11__pip--l {
  background: #0e0e12;
}
/* Selected */

.cal11__day.selected:not(.today) {
  background: var(--card2);
  border-color: var(--lime);
  transform: translateY(-4px);
}

.cal11__day.selected:not(.today)::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 50%;
  transform: translateX(-50%);
  width: 24px;
  height: 3px;
  background: var(--lime);
  border-radius: 2px;
}
/* Scroll hint gradient masks */

.cal11__strip-wrap {
  position: relative;
}

.cal11__strip-wrap::before,
.cal11__strip-wrap::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 20px;
  width: 40px;
  pointer-events: none;
  z-index: 2;
}

.cal11__strip-wrap::before {
  left: 0;
  background: linear-gradient(90deg, var(--bg), transparent);
}

.cal11__strip-wrap::after {
  right: 0;
  background: linear-gradient(270deg, var(--bg), transparent);
}
/* ── Selected day detail panel ── */

.cal11__detail {
  margin-top: 16px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 24px;
}

.cal11__detail-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}

.cal11__detail-date {
  font-size: 18px;
  font-weight: 700;
}

.cal11__detail-date span {
  color: var(--lime);
}

.cal11__detail-count {
  font-size: 12px;
  font-weight: 600;
  color: var(--text2);
  background: var(--card2);
  padding: 5px 12px;
  border-radius: 20px;
}
/* Timeline of the day */

.cal11__timeline {
  position: relative;
  padding-left: 20px;
}

.cal11__timeline::before {
  content: '';
  position: absolute;
  left: 4px;
  top: 6px;
  bottom: 6px;
  width: 2px;
  background: var(--border);
}

.cal11__tl-item {
  position: relative;
  padding: 10px 0 10px 18px;
}

.cal11__tl-item::before {
  content: '';
  position: absolute;
  left: -20px;
  top: 14px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 2px solid var(--bg);
}

.cal11__tl-item--l::before {
  background: var(--lime);
}

.cal11__tl-item--c::before {
  background: var(--coral);
}

.cal11__tl-item--y::before {
  background: var(--cyan);
}

.cal11__tl-item--v::before {
  background: var(--violet);
}

.cal11__tl-time {
  font-size: 11px;
  font-weight: 700;
  color: var(--text3);
  letter-spacing: 0.05em;
}

.cal11__tl-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  margin-top: 2px;
}

.cal11__tl-meta {
  font-size: 12px;
  color: var(--text2);
  margin-top: 2px;
}

@media (max-width: 480px) {
  .cal11__title {
    font-size: 30px;
  }

  .cal11__day {
    width: 66px;
    padding: 14px 8px 12px;
  }

  .cal11__day-num {
    font-size: 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal11 * {
    animation: none !important;
    transition: none !important;
  }

  .cal11__strip {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal11Strip .cal11__day').forEach(d => {
  d.addEventListener('click', function() {
    document.querySelectorAll('#cal11Strip .cal11__day').forEach(x => x.classList.remove('selected'));
    if (!this.classList.contains('today')) this.classList.add('selected');
    this.scrollIntoView({behavior:'smooth', inline:'center', block:'nearest'});
  });
});
```
