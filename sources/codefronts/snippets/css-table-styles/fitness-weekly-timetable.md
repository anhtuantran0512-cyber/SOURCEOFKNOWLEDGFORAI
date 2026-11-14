---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/fitness-weekly-timetable/"
title: "Fitness Weekly Timetable"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A Google-Calendar-style weekly class schedule built as an HTML table with colour-coded event blocks per class type, a \"today\" column highlight, and smooth…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fitness Weekly Timetable
Source: https://codefronts.com/snippets/css-table-styles/fitness-weekly-timetable/

A Google-Calendar-style weekly class schedule built as an HTML table with colour-coded event blocks per class type, a "today" column highlight, and smooth hover scale micro-interactions.
## HTML
```html
<div class="ct-10">
  <div class="ct-10__header">
    <div class="ct-10__title">🏋️ Studio Class Schedule</div>
    <div class="ct-10__week">Week of Jun 23 – Jun 29</div>
  </div>
  <div class="ct-10__legend">
    <div class="ct-10__legend-item"><div class="ct-10__legend-dot" style="background:var(--yoga)"></div>Yoga</div>
    <div class="ct-10__legend-item"><div class="ct-10__legend-dot" style="background:var(--hiit)"></div>HIIT</div>
    <div class="ct-10__legend-item"><div class="ct-10__legend-dot" style="background:var(--spin)"></div>Spin</div>
    <div class="ct-10__legend-item"><div class="ct-10__legend-dot" style="background:var(--pilates)"></div>Pilates</div>
    <div class="ct-10__legend-item"><div class="ct-10__legend-dot" style="background:var(--boxing)"></div>Boxing</div>
    <div class="ct-10__legend-item"><div class="ct-10__legend-dot" style="background:var(--strength)"></div>Strength</div>
  </div>
  <table>
    <thead>
      <tr>
        <th>Time</th>
        <th>Mon 23</th>
        <th>Tue 24</th>
        <th>Wed 25</th>
        <th class="ct-10--today">Thu 26</th>
        <th>Fri 27</th>
        <th>Sat 28</th>
        <th>Sun 29</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>6:00 AM</td>
        <td><div class="ct-10__event ct-10__event--yoga"><div class="ct-10__event-name">Morning Flow</div><div class="ct-10__event-instructor">Maya Singh</div></div></td>
        <td></td>
        <td><div class="ct-10__event ct-10__event--hiit"><div class="ct-10__event-name">HIIT Blast</div><div class="ct-10__event-instructor">Diego R.</div></div></td>
        <td class="ct-10--today-col"><div class="ct-10__event ct-10__event--spin"><div class="ct-10__event-name">Spin Express</div><div class="ct-10__event-instructor">Leah T.</div></div></td>
        <td></td>
        <td><div class="ct-10__event ct-10__event--strength"><div class="ct-10__event-name">Power Lift</div><div class="ct-10__event-instructor">Max Chen</div></div></td>
        <td></td>
      </tr>
      <tr>
        <td>9:00 AM</td>
        <td></td>
        <td><div class="ct-10__event ct-10__event--pilates"><div class="ct-10__event-name">Pilates Core</div><div class="ct-10__event-instructor">Nina B.</div></div></td>
        <td><div class="ct-10__event ct-10__event--yoga"><div class="ct-10__event-name">Vinyasa</div><div class="ct-10__event-instructor">Maya Singh</div></div></td>
        <td class="ct-10--today-col"><div class="ct-10__event ct-10__event--boxing"><div class="ct-10__event-name">Box Fit</div><div class="ct-10__event-instructor">Jake O.</div></div></td>
        <td><div class="ct-10__event ct-10__event--pilates"><div class="ct-10__event-name">Reformer</div><div class="ct-10__event-instructor">Nina B.</div></div></td>
        <td><div class="ct-10__event ct-10__event--yoga"><div class="ct-10__event-name">Yin Yoga</div><div class="ct-10__event-instructor">Maya Singh</div></div></td>
        <td><div class="ct-10__event ct-10__event--hiit"><div class="ct-10__event-name">Sunday Burn</div><div class="ct-10__event-instructor">Diego R.</div></div></td>
      </tr>
      <tr>
        <td>12:00 PM</td>
        <td><div class="ct-10__event ct-10__event--strength"><div class="ct-10__event-name">Lunch Lift</div><div class="ct-10__event-instructor">Max Chen</div></div></td>
        <td><div class="ct-10__event ct-10__event--boxing"><div class="ct-10__event-name">Kickbox</div><div class="ct-10__event-instructor">Jake O.</div></div></td>
        <td></td>
        <td class="ct-10--today-col"></td>
        <td><div class="ct-10__event ct-10__event--spin"><div class="ct-10__event-name">Sprint Cycle</div><div class="ct-10__event-instructor">Leah T.</div></div></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td>5:30 PM</td>
        <td><div class="ct-10__event ct-10__event--hiit"><div class="ct-10__event-name">HIIT Storm</div><div class="ct-10__event-instructor">Diego R.</div></div></td>
        <td><div class="ct-10__event ct-10__event--spin"><div class="ct-10__event-name">Evening Ride</div><div class="ct-10__event-instructor">Leah T.</div></div></td>
        <td><div class="ct-10__event ct-10__event--boxing"><div class="ct-10__event-name">Muay Thai</div><div class="ct-10__event-instructor">Jake O.</div></div></td>
        <td class="ct-10--today-col"><div class="ct-10__event ct-10__event--yoga"><div class="ct-10__event-name">Restorative</div><div class="ct-10__event-instructor">Maya Singh</div></div></td>
        <td><div class="ct-10__event ct-10__event--strength"><div class="ct-10__event-name">Barbell Club</div><div class="ct-10__event-instructor">Max Chen</div></div></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td>7:00 PM</td>
        <td><div class="ct-10__event ct-10__event--pilates"><div class="ct-10__event-name">Night Pilates</div><div class="ct-10__event-instructor">Nina B.</div></div></td>
        <td></td>
        <td><div class="ct-10__event ct-10__event--strength"><div class="ct-10__event-name">Strength Max</div><div class="ct-10__event-instructor">Max Chen</div></div></td>
        <td class="ct-10--today-col"><div class="ct-10__event ct-10__event--hiit"><div class="ct-10__event-name">Night HIIT</div><div class="ct-10__event-instructor">Diego R.</div></div></td>
        <td><div class="ct-10__event ct-10__event--yoga"><div class="ct-10__event-name">Wind Down</div><div class="ct-10__event-instructor">Maya Singh</div></div></td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
  </table>
</div>
```
## CSS
```css
.ct-10,
.ct-10 *,
.ct-10 *::before,
.ct-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-10 ::selection {
  background: #f43f5e;
  color: #fff;
}

.ct-10 {
  --bg: #0c0c16;
  --surface: #141420;
  --border: #22223a;
  --text: #e8e8f8;
  --muted: #5a5a7a;
  --time-col: #1a1a28;
  /* Class type colors */
  --yoga: #f43f5e;
  --yoga-bg: rgba(244,63,94,0.12);
  --hiit: #f97316;
  --hiit-bg: rgba(249,115,22,0.12);
  --spin: #a855f7;
  --spin-bg: rgba(168,85,247,0.12);
  --pilates: #06b6d4;
  --pilates-bg: rgba(6,182,212,0.12);
  --boxing: #eab308;
  --boxing-bg: rgba(234,179,8,0.12);
  --strength: #10b981;
  --strength-bg: rgba(16,185,129,0.12);
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  padding: 28px 16px;
  min-height: 100vh;
  color: var(--text);
  overflow-x: auto;
}

.ct-10__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 10px;
}

.ct-10__title {
  font-size: 18px;
  font-weight: 800;
}

.ct-10__week {
  font-size: 12px;
  color: var(--muted);
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 5px 14px;
  border-radius: 8px;
}

.ct-10__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
}

.ct-10__legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 600;
  color: var(--muted);
}

.ct-10__legend-dot {
  width: 8px;
  height: 8px;
  border-radius: 2px;
}

.ct-10 table {
  width: 100%;
  border-collapse: collapse;
  min-width: 680px;
}

.ct-10 thead th {
  padding: 10px 8px;
  text-align: center;
  font-size: 12px;
  font-weight: 700;
  color: var(--muted);
  border-bottom: 2px solid var(--border);
}

.ct-10 thead th:first-child {
  width: 70px;
  text-align: left;
}

.ct-10 thead th.ct-10--today {
  color: var(--text);
  background: rgba(255,255,255,0.03);
  border-radius: 8px 8px 0 0;
  position: relative;
}

.ct-10 thead th.ct-10--today::after {
  content: '• Today';
  display: block;
  font-size: 9px;
  color: #f43f5e;
  font-weight: 800;
  letter-spacing: 1px;
}

.ct-10 tbody tr {
  border-bottom: 1px solid var(--border);
}

.ct-10 tbody td {
  padding: 6px 6px;
  vertical-align: top;
  min-height: 56px;
  height: 56px;
}

.ct-10 tbody td:first-child {
  font-size: 11px;
  color: var(--muted);
  font-weight: 600;
  text-align: left;
  vertical-align: middle;
  background: var(--time-col);
  width: 70px;
  padding: 0 10px;
  border-right: 1px solid var(--border);
}

.ct-10 tbody td.ct-10--today-col {
  background: rgba(255,255,255,0.015);
}
/* Class event block */

.ct-10__event {
  border-radius: 8px;
  padding: 7px 10px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
  border-left: 3px solid;
}

.ct-10__event::before {
  content: '';
  position: absolute;
  inset: 0;
  background: inherit;
  opacity: 0;
  transition: opacity 0.2s;
}

.ct-10__event:hover {
  transform: scale(1.03);
  z-index: 2;
}

.ct-10__event:hover::before {
  opacity: 0.4;
}

.ct-10__event--yoga {
  background: var(--yoga-bg);
  border-color: var(--yoga);
  color: var(--yoga);
}

.ct-10__event--hiit {
  background: var(--hiit-bg);
  border-color: var(--hiit);
  color: var(--hiit);
}

.ct-10__event--spin {
  background: var(--spin-bg);
  border-color: var(--spin);
  color: var(--spin);
}

.ct-10__event--pilates {
  background: var(--pilates-bg);
  border-color: var(--pilates);
  color: var(--pilates);
}

.ct-10__event--boxing {
  background: var(--boxing-bg);
  border-color: var(--boxing);
  color: var(--boxing);
}

.ct-10__event--strength {
  background: var(--strength-bg);
  border-color: var(--strength);
  color: var(--strength);
}

.ct-10__event-name {
  font-size: 12px;
  font-weight: 700;
  line-height: 1.2;
}

.ct-10__event-instructor {
  font-size: 10px;
  opacity: 0.7;
  margin-top: 2px;
}
/* Span helper - spans 2 time slots */

.ct-10__event--tall {
  height: calc(200% + 12px);
}

@media (prefers-reduced-motion: reduce) {
  .ct-10__event {
    transition: none;
  }
}
```
