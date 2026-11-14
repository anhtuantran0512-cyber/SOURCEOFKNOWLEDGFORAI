---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/neumorphic-calendar-widget/"
title: "Neumorphic Calendar Widget"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Pure soft-UI on the canonical #e0e5ec base with the dual light/dark shadow recipe exposed as reusable variables."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Calendar Widget
Source: https://codefronts.com/components/css-calendar-designs/neumorphic-calendar-widget/

Pure soft-UI on the canonical #e0e5ec base with the dual light/dark shadow recipe exposed as reusable variables. Buttons extrude and press to inset, today is permanently inset, the selected day is a raised button, and the footer is one large inset event well.
## HTML
```html
<div class="cal10">
  <div class="cal10__widget">

    <div class="cal10__head">
      <div class="cal10__month-wrap">
        <div class="cal10__month">June</div>
        <div class="cal10__year">2026</div>
      </div>
      <div class="cal10__nav">
        <div class="cal10__nav-btn">‹</div>
        <div class="cal10__nav-btn">›</div>
      </div>
    </div>

    <div class="cal10__dow">
      <div class="cal10__dw">S</div><div class="cal10__dw">M</div><div class="cal10__dw">T</div>
      <div class="cal10__dw">W</div><div class="cal10__dw">T</div><div class="cal10__dw">F</div><div class="cal10__dw">S</div>
    </div>

    <div class="cal10__grid" id="cal10Grid">
      <div class="cal10__cell other">25</div><div class="cal10__cell other">26</div><div class="cal10__cell other">27</div>
      <div class="cal10__cell other">28</div><div class="cal10__cell other">29</div><div class="cal10__cell other">30</div><div class="cal10__cell other">31</div>
      <div class="cal10__cell">1</div>
      <div class="cal10__cell">2<span class="cal10__dot cal10__dot--a"></span></div>
      <div class="cal10__cell">3</div>
      <div class="cal10__cell">4<span class="cal10__dot cal10__dot--g"></span></div>
      <div class="cal10__cell">5</div>
      <div class="cal10__cell">6</div>
      <div class="cal10__cell">7<span class="cal10__dot cal10__dot--r"></span></div>
      <div class="cal10__cell today selected">8</div>
      <div class="cal10__cell">9<span class="cal10__dot cal10__dot--a"></span></div>
      <div class="cal10__cell">10</div>
      <div class="cal10__cell">11<span class="cal10__dot cal10__dot--r"></span></div>
      <div class="cal10__cell">12</div>
      <div class="cal10__cell">13<span class="cal10__dot cal10__dot--g"></span></div>
      <div class="cal10__cell">14</div>
      <div class="cal10__cell">15</div>
      <div class="cal10__cell">16</div>
      <div class="cal10__cell">17<span class="cal10__dot cal10__dot--a"></span></div>
      <div class="cal10__cell">18</div>
      <div class="cal10__cell">19</div>
      <div class="cal10__cell">20<span class="cal10__dot cal10__dot--r"></span></div>
      <div class="cal10__cell">21</div>
      <div class="cal10__cell">22</div>
      <div class="cal10__cell">23<span class="cal10__dot cal10__dot--g"></span></div>
      <div class="cal10__cell">24</div>
      <div class="cal10__cell">25<span class="cal10__dot cal10__dot--a"></span></div>
      <div class="cal10__cell">26</div>
      <div class="cal10__cell">27</div>
      <div class="cal10__cell">28</div>
      <div class="cal10__cell">29</div>
      <div class="cal10__cell">30</div>
      <div class="cal10__cell other">1</div><div class="cal10__cell other">2</div><div class="cal10__cell other">3</div>
      <div class="cal10__cell other">4</div><div class="cal10__cell other">5</div>
    </div>

    <div class="cal10__footer">
      <div class="cal10__footer-label">Today · June 8</div>
      <div class="cal10__ev">
        <div class="cal10__ev-icon">📋</div>
        <div class="cal10__ev-body">
          <div class="cal10__ev-name">Sprint Planning</div>
          <div class="cal10__ev-time">10:00 AM</div>
        </div>
        <div class="cal10__ev-pill cal10__ev-pill--a">1h</div>
      </div>
      <div class="cal10__ev">
        <div class="cal10__ev-icon">🚀</div>
        <div class="cal10__ev-body">
          <div class="cal10__ev-name">Product Launch</div>
          <div class="cal10__ev-time">2:00 PM</div>
        </div>
        <div class="cal10__ev-pill cal10__ev-pill--r">Now</div>
      </div>
      <div class="cal10__ev">
        <div class="cal10__ev-icon">☕</div>
        <div class="cal10__ev-body">
          <div class="cal10__ev-name">Team Coffee</div>
          <div class="cal10__ev-time">4:30 PM</div>
        </div>
        <div class="cal10__ev-pill cal10__ev-pill--g">30m</div>
      </div>
    </div>

    <div class="cal10__toggles">
      <div class="cal10__toggle active">Month</div>
      <div class="cal10__toggle">Week</div>
      <div class="cal10__toggle">Day</div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal10,
.cal10 *,
.cal10 *::before,
.cal10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal10 ::selection {
  background: #6d5dfc;
  color: #fff;
}

.cal10 {
  /* The neumorphic base — everything matches this exact bg */
  --bg: #e0e5ec;
  --light: #ffffff;
  --dark: #a3b1c6;
  --text: #4a5568;
  --text2: #8595ad;
  --text3: #b0bcce;
  --accent: #6d5dfc;
  --accent-l: #8a7cff;
  --red: #fc5d7c;
  --green: #4ecda6;
  --amber: #fcb15d;
  /* The famous dual-shadow recipe */
  --shadow-out: 8px 8px 16px var(--dark), -8px -8px 16px var(--light);
  --shadow-out-sm: 5px 5px 10px var(--dark), -5px -5px 10px var(--light);
  --shadow-in: inset 5px 5px 10px var(--dark), inset -5px -5px 10px var(--light);
  --shadow-in-sm: inset 3px 3px 6px var(--dark), inset -3px -3px 6px var(--light);
  font-family: 'Nunito', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
}

@keyframes cal10-in {
  from {
    opacity: 0;
    transform: scale(0.96);
  }

  to {
    opacity: 1;
    transform: scale(1);
  }
}

.cal10__widget {
  width: 100%;
  max-width: 420px;
  background: var(--bg);
  border-radius: 36px;
  padding: 32px;
  box-shadow: var(--shadow-out);
  animation: cal10-in 0.5s ease both;
}
/* ── Header ── */

.cal10__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.cal10__month-wrap {
}

.cal10__month {
  font-size: 28px;
  font-weight: 900;
  color: var(--text);
  line-height: 1;
}

.cal10__year {
  font-size: 13px;
  font-weight: 700;
  color: var(--text3);
  letter-spacing: 0.08em;
  margin-top: 2px;
}

.cal10__nav {
  display: flex;
  gap: 12px;
}
/* Neumorphic buttons — extruded, press to inset */

.cal10__nav-btn {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: var(--bg);
  box-shadow: var(--shadow-out-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--accent);
  font-size: 18px;
  font-weight: 800;
  transition: box-shadow 0.18s, color 0.18s;
  user-select: none;
}

.cal10__nav-btn:hover {
  color: var(--accent-l);
}

.cal10__nav-btn:active {
  box-shadow: var(--shadow-in-sm);
}
/* ── DOW row ── */

.cal10__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 16px;
}

.cal10__dw {
  text-align: center;
  font-size: 11px;
  font-weight: 800;
  color: var(--text3);
  letter-spacing: 0.05em;
}
/* ── Date grid ── */

.cal10__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 10px;
}

.cal10__cell {
  aspect-ratio: 1;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  cursor: pointer;
  position: relative;
  transition: box-shadow 0.18s, color 0.18s, transform 0.18s;
  background: var(--bg);
}
/* Default flat cells press in on hover */

.cal10__cell:hover {
  box-shadow: var(--shadow-in-sm);
  color: var(--accent);
}

.cal10__cell.other {
  color: var(--text3);
  opacity: 0.5;
  pointer-events: none;
}
/* Today — permanently inset (pressed look) */

.cal10__cell.today {
  box-shadow: var(--shadow-in);
  color: var(--accent);
  font-weight: 900;
}
/* Selected — raised + accent, the "active" button */

.cal10__cell.selected {
  box-shadow: var(--shadow-out-sm);
  color: var(--accent);
  font-weight: 900;
  transform: scale(1.02);
}

.cal10__cell.selected::after {
  content: '';
  position: absolute;
  inset: 6px;
  border-radius: 50%;
  border: 2px solid var(--accent);
  opacity: 0.25;
}
/* Event dots */

.cal10__dot {
  position: absolute;
  bottom: 7px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
}

.cal10__dot--a {
  background: var(--accent);
}

.cal10__dot--r {
  background: var(--red);
}

.cal10__dot--g {
  background: var(--green);
}
/* ── Footer event card — inset well ── */

.cal10__footer {
  margin-top: 28px;
  padding: 20px;
  border-radius: 24px;
  box-shadow: var(--shadow-in);
  background: var(--bg);
}

.cal10__footer-label {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--text3);
  margin-bottom: 14px;
}

.cal10__ev {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 8px 0;
}

.cal10__ev + .cal10__ev {
  border-top: 1px solid rgba(163,177,198,0.25);
}
/* Neumorphic mini icon */

.cal10__ev-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--bg);
  box-shadow: var(--shadow-out-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}

.cal10__ev-body {
  flex: 1;
  min-width: 0;
}

.cal10__ev-name {
  font-size: 14px;
  font-weight: 800;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal10__ev-time {
  font-size: 12px;
  font-weight: 600;
  color: var(--text2);
  margin-top: 1px;
}

.cal10__ev-pill {
  font-size: 11px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 20px;
  background: var(--bg);
  box-shadow: var(--shadow-out-sm);
  flex-shrink: 0;
}

.cal10__ev-pill--a {
  color: var(--accent);
}

.cal10__ev-pill--r {
  color: var(--red);
}

.cal10__ev-pill--g {
  color: var(--green);
}
/* ── Bottom toggle row (neumorphic switches) ── */

.cal10__toggles {
  display: flex;
  gap: 12px;
  margin-top: 20px;
}

.cal10__toggle {
  flex: 1;
  padding: 12px;
  border-radius: 16px;
  background: var(--bg);
  box-shadow: var(--shadow-out-sm);
  text-align: center;
  font-size: 12px;
  font-weight: 800;
  color: var(--text2);
  cursor: pointer;
  transition: box-shadow 0.18s, color 0.18s;
  user-select: none;
}

.cal10__toggle:hover {
  color: var(--accent);
}

.cal10__toggle.active {
  box-shadow: var(--shadow-in-sm);
  color: var(--accent);
}

@media (max-width: 460px) {
  .cal10__widget {
    padding: 24px;
    border-radius: 28px;
  }

  .cal10__grid {
    gap: 7px;
  }

  .cal10__cell {
    font-size: 13px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal10 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal10Grid .cal10__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal10Grid .cal10__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
document.querySelectorAll('.cal10__toggle').forEach(t => {
  t.addEventListener('click', function() {
    document.querySelectorAll('.cal10__toggle').forEach(x => x.classList.remove('active'));
    this.classList.add('active');
  });
});
```
