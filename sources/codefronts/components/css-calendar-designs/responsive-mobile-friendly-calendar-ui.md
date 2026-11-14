---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/responsive-mobile-friendly-calendar-ui/"
title: "Responsive Mobile-Friendly Calendar UI"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "An organic green calendar built to scale across three breakpoints."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Mobile-Friendly Calendar UI
Source: https://codefronts.com/components/css-calendar-designs/responsive-mobile-friendly-calendar-ui/

An organic green calendar built to scale across three breakpoints. Layout collapses from two columns to one, then compacts cell sizes and touch targets for small screens. Fraunces italic month, pulsing today ring, color pips and a desktop side panel with a mini activity chart.
## HTML
```html
<div class="cal06">
  <div class="cal06__layout">

    <!-- Main calendar -->
    <div class="cal06__main">

      <div class="cal06__top">
        <div class="cal06__month-block">
          <div class="cal06__month-label">June</div>
          <div class="cal06__year-label">2026 · Q2</div>
        </div>
        <div class="cal06__top-right">
          <div class="cal06__nav-row">
            <div class="cal06__nav-btn">‹</div>
            <div class="cal06__nav-btn">›</div>
          </div>
          <div class="cal06__today-pill">Today</div>
        </div>
      </div>

      <div class="cal06__dow">
        <div class="cal06__dow-lbl">S</div>
        <div class="cal06__dow-lbl">M</div>
        <div class="cal06__dow-lbl">T</div>
        <div class="cal06__dow-lbl">W</div>
        <div class="cal06__dow-lbl">T</div>
        <div class="cal06__dow-lbl">F</div>
        <div class="cal06__dow-lbl">S</div>
      </div>

      <div class="cal06__grid" id="cal06Grid">
        <!-- May overflow -->
        <div class="cal06__cell other weekend"><div class="cal06__cell-n">25</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">26</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">27</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">28</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">29</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">30</div></div>
        <div class="cal06__cell other weekend"><div class="cal06__cell-n">31</div></div>
        <!-- June 1-7 -->
        <div class="cal06__cell weekend"><div class="cal06__cell-n">1</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">2</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--g"></span></div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">3</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">4</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--y"></span></div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">5</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">6</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--p"></span></div></div>
        <div class="cal06__cell weekend"><div class="cal06__cell-n">7</div></div>
        <!-- June 8-14: today=8 -->
        <div class="cal06__cell today weekend"><div class="cal06__cell-n">8</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--g"></span></div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">9</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--g"></span><span class="cal06__pip cal06__pip--l"></span></div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">10</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">11</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--p"></span></div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">12</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">13</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--y"></span></div></div>
        <div class="cal06__cell weekend"><div class="cal06__cell-n">14</div></div>
        <!-- June 15-21 -->
        <div class="cal06__cell weekend"><div class="cal06__cell-n">15</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">16</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">17</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--g"></span><span class="cal06__pip cal06__pip--g"></span></div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">18</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">19</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">20</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--l"></span></div></div>
        <div class="cal06__cell weekend"><div class="cal06__cell-n">21</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--y"></span></div></div>
        <!-- June 22-28 -->
        <div class="cal06__cell weekend"><div class="cal06__cell-n">22</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">23</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">24</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--p"></span></div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">25</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">26</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">27</div><div class="cal06__pips"><span class="cal06__pip cal06__pip--g"></span></div></div>
        <div class="cal06__cell weekend"><div class="cal06__cell-n">28</div></div>
        <!-- June 29-30 + July -->
        <div class="cal06__cell weekend"><div class="cal06__cell-n">29</div></div>
        <div class="cal06__cell"><div class="cal06__cell-n">30</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">1</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">2</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">3</div></div>
        <div class="cal06__cell other"><div class="cal06__cell-n">4</div></div>
        <div class="cal06__cell other weekend"><div class="cal06__cell-n">5</div></div>
      </div>

    </div>

    <!-- Side panel -->
    <div class="cal06__side">

      <div class="cal06__side-card">
        <div class="cal06__side-label">Selected Day</div>
        <div class="cal06__date-big" id="cal06DateBig">08</div>
        <div class="cal06__date-info">Sunday, June 2026</div>
      </div>

      <div class="cal06__side-card">
        <div class="cal06__side-label">Upcoming Events</div>
        <div class="cal06__ev">
          <div class="cal06__ev-dot" style="background:var(--green)"></div>
          <div class="cal06__ev-body">
            <div class="cal06__ev-name">Sprint Planning</div>
            <div class="cal06__ev-time">Mon Jun 9 · 10:00 AM</div>
          </div>
        </div>
        <div class="cal06__ev">
          <div class="cal06__ev-dot" style="background:var(--peach)"></div>
          <div class="cal06__ev-body">
            <div class="cal06__ev-name">Product Launch</div>
            <div class="cal06__ev-time">Wed Jun 11 · 9:00 AM</div>
          </div>
        </div>
        <div class="cal06__ev">
          <div class="cal06__ev-dot" style="background:var(--yellow)"></div>
          <div class="cal06__ev-body">
            <div class="cal06__ev-name">Demo Day</div>
            <div class="cal06__ev-time">Fri Jun 13 · 2:00 PM</div>
          </div>
        </div>
      </div>

      <div class="cal06__side-card">
        <div class="cal06__side-label">Week Activity</div>
        <div class="cal06__week-bars">
          <div class="cal06__bar-col"><div class="cal06__bar" style="height:20px;opacity:.3"></div><div class="cal06__bar-lbl">S</div></div>
          <div class="cal06__bar-col"><div class="cal06__bar" style="height:32px"></div><div class="cal06__bar-lbl">M</div></div>
          <div class="cal06__bar-col"><div class="cal06__bar" style="height:18px;opacity:.5"></div><div class="cal06__bar-lbl">T</div></div>
          <div class="cal06__bar-col"><div class="cal06__bar" style="height:36px"></div><div class="cal06__bar-lbl">W</div></div>
          <div class="cal06__bar-col"><div class="cal06__bar" style="height:28px;opacity:.8"></div><div class="cal06__bar-lbl">T</div></div>
          <div class="cal06__bar-col"><div class="cal06__bar" style="height:22px;opacity:.6"></div><div class="cal06__bar-lbl">F</div></div>
          <div class="cal06__bar-col"><div class="cal06__bar" style="height:10px;opacity:.25"></div><div class="cal06__bar-lbl">S</div></div>
        </div>
      </div>

    </div>

  </div>
</div>
```
## CSS
```css
.cal06,
.cal06 *,
.cal06 *::before,
.cal06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal06 ::selection {
  background: #5b7e5f;
  color: #fff;
}

.cal06 {
  --bg: #eef3ec;
  --surface: #f7faf5;
  --card: #ffffff;
  --ink: #1e2b1f;
  --ink2: #4a5e4c;
  --muted: #8fa892;
  --green: #5b7e5f;
  --green2: #3d6641;
  --peach: #e07a5f;
  --yellow: #f2b94b;
  --lavender: #9b89c4;
  --today-bg: #e8f0e9;
  --sel-bg: #5b7e5f;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: var(--bg);
  background-image: radial-gradient(circle at 20% 80%, rgba(91,126,95,0.08) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(242,185,75,0.06) 0%, transparent 50%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

@keyframes cal06-in {
  from {
    opacity: 0;
    transform: scale(0.97) translateY(12px);
  }

  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

@keyframes cal06-pulse-ring {
  0% {
    box-shadow: 0 0 0 0 rgba(91,126,95,0.4);
  }

  70% {
    box-shadow: 0 0 0 8px rgba(91,126,95,0);
  }

  100% {
    box-shadow: 0 0 0 0 rgba(91,126,95,0);
  }
}

@keyframes cal06-slide {
  from {
    opacity: 0;
    transform: translateX(-8px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}
/* ── Outermost: full desktop layout ── */

.cal06__layout {
  display: grid;
  grid-template-columns: 1fr 310px;
  gap: 20px;
  max-width: 860px;
  width: 100%;
  animation: cal06-in 0.5s cubic-bezier(0.22,1,0.36,1) both;
}
/* ── Main Card ── */

.cal06__main {
  background: var(--card);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(30,43,31,0.08), 0 1px 4px rgba(30,43,31,0.06);
}
/* ── Top strip: month + year ── */

.cal06__top {
  background: var(--green);
  padding: 24px 28px 20px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}

.cal06__top::before {
  content: '';
  position: absolute;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: rgba(255,255,255,0.06);
  top: -60px;
  right: -60px;
}

.cal06__top::after {
  content: '';
  position: absolute;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: rgba(255,255,255,0.05);
  bottom: -30px;
  left: 40px;
}

.cal06__month-block {
  position: relative;
  z-index: 1;
}

.cal06__month-label {
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 44px;
  font-weight: 700;
  color: #fff;
  line-height: 1;
}

.cal06__year-label {
  font-size: 13px;
  font-weight: 500;
  color: rgba(255,255,255,0.65);
  letter-spacing: 0.12em;
  margin-top: 4px;
}

.cal06__top-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
  position: relative;
  z-index: 1;
}

.cal06__nav-row {
  display: flex;
  gap: 6px;
}

.cal06__nav-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.25);
  color: #fff;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
  user-select: none;
}

.cal06__nav-btn:hover {
  background: rgba(255,255,255,0.28);
}

.cal06__today-pill {
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.3);
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 5px 12px;
  border-radius: 20px;
  cursor: pointer;
}
/* ── DOW row ── */

.cal06__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 12px 16px 6px;
  background: var(--surface);
}

.cal06__dow-lbl {
  text-align: center;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 6px 0;
}

.cal06__dow-lbl:first-child,
.cal06__dow-lbl:last-child {
  color: var(--green);
  opacity: 0.7;
}
/* ── Grid ── */

.cal06__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 6px 16px 20px;
  gap: 4px;
}

.cal06__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 6px 2px 4px;
  border-radius: 14px;
  cursor: pointer;
  transition: background 0.15s, transform 0.15s;
  min-height: 52px;
  position: relative;
}

.cal06__cell:hover {
  background: var(--today-bg);
  transform: scale(1.04);
}

.cal06__cell.other {
  opacity: 0.22;
  pointer-events: none;
}

.cal06__cell-n {
  font-size: 15px;
  font-weight: 500;
  color: var(--ink);
  line-height: 1;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.15s;
}

.cal06__cell.weekend .cal06__cell-n {
  color: var(--green);
}

.cal06__cell.today .cal06__cell-n {
  background: var(--green);
  color: #fff;
  font-weight: 700;
  animation: cal06-pulse-ring 2.5s ease-in-out infinite;
}

.cal06__cell.selected .cal06__cell-n {
  background: var(--peach);
  color: #fff;
  font-weight: 700;
  box-shadow: 0 4px 14px rgba(224,122,95,0.45);
}
/* Event pips below number */

.cal06__pips {
  display: flex;
  gap: 3px;
  margin-top: 3px;
}

.cal06__pip {
  width: 5px;
  height: 5px;
  border-radius: 50%;
}

.cal06__pip--g {
  background: var(--green);
}

.cal06__pip--p {
  background: var(--peach);
}

.cal06__pip--y {
  background: var(--yellow);
}

.cal06__pip--l {
  background: var(--lavender);
}
/* ── Right panel (desktop only) ── */

.cal06__side {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.cal06__side-card {
  background: var(--card);
  border-radius: 20px;
  padding: 22px;
  box-shadow: 0 4px 20px rgba(30,43,31,0.07);
}

.cal06__side-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 16px;
}
/* Mini date display */

.cal06__date-big {
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 64px;
  font-weight: 700;
  color: var(--green2);
  line-height: 1;
}

.cal06__date-info {
  font-size: 13px;
  color: var(--muted);
  margin-top: 4px;
}
/* Event items */

.cal06__ev {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid rgba(30,43,31,0.06);
  animation: cal06-slide 0.3s ease both;
}

.cal06__ev:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.cal06__ev:nth-child(2) {
  animation-delay: 0.06s;
}

.cal06__ev:nth-child(3) {
  animation-delay: 0.12s;
}

.cal06__ev-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.cal06__ev-body {
  flex: 1;
  min-width: 0;
}

.cal06__ev-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal06__ev-time {
  font-size: 11px;
  color: var(--muted);
  margin-top: 2px;
}
/* Week summary mini bars */

.cal06__week-bars {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
  align-items: flex-end;
  height: 40px;
}

.cal06__bar-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.cal06__bar {
  width: 100%;
  background: var(--green);
  border-radius: 3px 3px 0 0;
  opacity: 0.7;
  transition: opacity 0.2s;
}

.cal06__bar:hover {
  opacity: 1;
}

.cal06__bar-lbl {
  font-size: 8px;
  color: var(--muted);
  font-weight: 600;
  letter-spacing: 0.05em;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   RESPONSIVE: tablet → collapse to 1 col
   RESPONSIVE: mobile → compact top strip,
   smaller cells, hide side panel under grid
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

@media (max-width: 780px) {
  .cal06__layout {
    grid-template-columns: 1fr;
    max-width: 500px;
  }

  .cal06__side {
    display: none;
  }
}

@media (max-width: 480px) {
  .cal06__top {
    padding: 18px 20px 16px;
  }

  .cal06__month-label {
    font-size: 34px;
  }

  .cal06__dow {
    padding: 8px 10px 4px;
  }

  .cal06__grid {
    padding: 4px 10px 14px;
    gap: 2px;
  }

  .cal06__cell {
    min-height: 42px;
    border-radius: 10px;
  }

  .cal06__cell-n {
    width: 28px;
    height: 28px;
    font-size: 13px;
  }

  .cal06__today-pill {
    display: none;
  }
}

@media (max-width: 360px) {
  .cal06__month-label {
    font-size: 28px;
  }

  .cal06__cell-n {
    width: 24px;
    height: 24px;
    font-size: 11px;
  }

  .cal06__dow-lbl {
    font-size: 8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal06 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal06Grid .cal06__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal06Grid .cal06__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
    const n = this.querySelector('.cal06__cell-n').textContent;
    const el = document.getElementById('cal06DateBig');
    if (el) el.textContent = n.padStart(2,'0');
  });
});
```
