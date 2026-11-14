---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/brutalist-css-calendar-design/"
title: "Brutalist CSS Calendar Design"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Raw newspaper-meets-Bauhaus brutalism on graph-paper."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist CSS Calendar Design
Source: https://codefronts.com/components/css-calendar-designs/brutalist-css-calendar-design/

Raw newspaper-meets-Bauhaus brutalism on graph-paper. Full-width black header with a flickering Bebas Neue month, hard borders and solid box-shadow offsets, top-edge event bars, and an ink-black sidebar with stamp decoration, event list and a 2x2 stats grid.
## HTML
```html
<div class="cal-02-wrapper">

  <!-- Banner -->
  <div class="cal-02-banner">
    <div class="cal-02-banner-month">June</div>
    <div class="cal-02-banner-nav">
      <div class="cal-02-banner-navbtn">←</div>
      <div class="cal-02-banner-navbtn">→</div>
    </div>
    <div class="cal-02-banner-right">
      <div class="cal-02-banner-year">2026</div>
      <div class="cal-02-banner-sub">Q2 · Week 23</div>
    </div>
  </div>

  <!-- Main Grid -->
  <div class="cal-02-main">
    <div class="cal-02-day-labels">
      <div class="cal-02-dl cal-02-weekend">SUN</div>
      <div class="cal-02-dl">MON</div>
      <div class="cal-02-dl">TUE</div>
      <div class="cal-02-dl">WED</div>
      <div class="cal-02-dl">THU</div>
      <div class="cal-02-dl">FRI</div>
      <div class="cal-02-dl cal-02-weekend">SAT</div>
    </div>
    <div class="cal-02-grid" id="cal-02-brutCal">
      <!-- Row 1 (May) -->
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">25</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">26</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">27</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">28</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">29</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">30</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">31</div></div>
      <!-- Row 2 -->
      <div class="cal-02-cell"><div class="cal-02-num">1</div></div>
      <div class="cal-02-cell cal-02-has-event cal-02-ev-blue"><div class="cal-02-num">2</div><span class="cal-02-event-tag">Workshop</span></div>
      <div class="cal-02-cell"><div class="cal-02-num">3</div></div>
      <div class="cal-02-cell cal-02-has-event cal-02-ev-red"><div class="cal-02-num">4</div><span class="cal-02-event-tag cal-02-red">Deadline</span></div>
      <div class="cal-02-cell"><div class="cal-02-num">5</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">6</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">7</div></div>
      <!-- Row 3 — cal-02-today -->
      <div class="cal-02-cell cal-02-today cal-02-selected"><div class="cal-02-num">8</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">9</div></div>
      <div class="cal-02-cell cal-02-has-event cal-02-ev-blue"><div class="cal-02-num">10</div><span class="cal-02-event-tag">Sprint</span></div>
      <div class="cal-02-cell"><div class="cal-02-num">11</div></div>
      <div class="cal-02-cell cal-02-has-event cal-02-ev-red"><div class="cal-02-num">12</div><span class="cal-02-event-tag cal-02-red">Review</span></div>
      <div class="cal-02-cell"><div class="cal-02-num">13</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">14</div></div>
      <!-- Row 4 -->
      <div class="cal-02-cell"><div class="cal-02-num">15</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">16</div></div>
      <div class="cal-02-cell cal-02-has-event cal-02-ev-yellow"><div class="cal-02-num">17</div><span class="cal-02-event-tag">Demo Day</span></div>
      <div class="cal-02-cell"><div class="cal-02-num">18</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">19</div></div>
      <div class="cal-02-cell cal-02-has-event cal-02-ev-blue"><div class="cal-02-num">20</div><span class="cal-02-event-tag">Launch</span></div>
      <div class="cal-02-cell"><div class="cal-02-num">21</div></div>
      <!-- Row 5 -->
      <div class="cal-02-cell"><div class="cal-02-num">22</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">23</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">24</div></div>
      <div class="cal-02-cell cal-02-has-event cal-02-ev-red"><div class="cal-02-num">25</div><span class="cal-02-event-tag cal-02-red">Board Mtg</span></div>
      <div class="cal-02-cell"><div class="cal-02-num">26</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">27</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">28</div></div>
      <!-- Row 6 -->
      <div class="cal-02-cell"><div class="cal-02-num">29</div></div>
      <div class="cal-02-cell"><div class="cal-02-num">30</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">1</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">2</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">3</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">4</div></div>
      <div class="cal-02-cell cal-02-other-month"><div class="cal-02-num">5</div></div>
    </div>
  </div>

  <!-- Sidebar -->
  <div class="cal-02-sidebar">
    <div class="cal-02-sb-section">
      <div class="cal-02-sb-label">Today</div>
      <div class="cal-02-sb-big">08<span class="cal-02-cursor"></span></div>
      <div class="cal-02-sb-biginfo">Sunday / June / 2026</div>
      <div class="cal-02-stamp">Day 159</div>
    </div>

    <div class="cal-02-sb-section">
      <div class="cal-02-sb-label">This Week</div>
      <div class="cal-02-evlist-item">
        <div class="cal-02-ev-bar cal-02-blue"></div>
        <div class="cal-02-ev-info">
          <div class="cal-02-ev-name">Sprint Planning</div>
          <div class="cal-02-ev-time">MON 10 · 10:00</div>
        </div>
      </div>
      <div class="cal-02-evlist-item">
        <div class="cal-02-ev-bar cal-02-red"></div>
        <div class="cal-02-ev-info">
          <div class="cal-02-ev-name">Design Review</div>
          <div class="cal-02-ev-time">WED 12 · 14:00</div>
        </div>
      </div>
      <div class="cal-02-evlist-item">
        <div class="cal-02-ev-bar cal-02-yellow"></div>
        <div class="cal-02-ev-info">
          <div class="cal-02-ev-name">Client Presentation</div>
          <div class="cal-02-ev-time">FRI 13 · 16:30</div>
        </div>
      </div>
    </div>

    <div class="cal-02-sb-section">
      <div class="cal-02-sb-label">Month Stats</div>
      <div class="cal-02-stats">
        <div class="cal-02-stat">
          <div class="cal-02-stat-val">12</div>
          <div class="cal-02-stat-lbl">Events</div>
        </div>
        <div class="cal-02-stat">
          <div class="cal-02-stat-val">4</div>
          <div class="cal-02-stat-lbl">Deadlines</div>
        </div>
        <div class="cal-02-stat">
          <div class="cal-02-stat-val">23</div>
          <div class="cal-02-stat-lbl">Work days</div>
        </div>
        <div class="cal-02-stat">
          <div class="cal-02-stat-val">7</div>
          <div class="cal-02-stat-lbl">Remaining</div>
        </div>
      </div>
    </div>
  </div>

</div>
```
## CSS
```css
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --bg: #f5f0e8;
  --ink: #0d0d0d;
  --red: #e63e2f;
  --yellow: #f5c800;
  --blue: #1a4fff;
  --white: #fafaf7;
  --border: 3px solid var(--ink);
  --shadow: 5px 5px 0 var(--ink);
  --shadow-lg: 8px 8px 0 var(--ink);
}

body {
  font-family: 'IBM Plex Mono', monospace;
  background-color: var(--bg);
  background-image: repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(0,0,0,0.06) 39px, rgba(0,0,0,0.06) 40px), repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(0,0,0,0.06) 39px, rgba(0,0,0,0.06) 40px);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

@keyframes cal02-stamp {
  from {
    transform: scale(1.4) rotate(-3deg);
    opacity: 0;
  }

  to {
    transform: scale(1) rotate(0deg);
    opacity: 1;
  }
}

@keyframes cal02-flicker {
  0%,
    100% {
    opacity: 1;
  }

  92% {
    opacity: 1;
  }

  93% {
    opacity: 0.4;
  }

  94% {
    opacity: 1;
  }
}

@keyframes cal02-slide-in {
  from {
    transform: translateX(-30px);
    opacity: 0;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes cal02-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

.cal-02-wrapper {
  max-width: 880px;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 260px;
  gap: 0;
  border: var(--border);
  box-shadow: var(--shadow-lg);
  animation: cal02-stamp 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
}
/* ── Header Banner ── */

.cal-02-banner {
  background: var(--ink);
  color: var(--yellow);
  padding: 20px 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: var(--border);
  grid-column: 1 / -1;
}

.cal-02-banner-month {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 72px;
  line-height: 1;
  letter-spacing: 0.02em;
  color: var(--yellow);
  animation: cal02-flicker 5s infinite;
}

.cal-02-banner-right {
  text-align: right;
}

.cal-02-banner-year {
  font-family: 'Anton', sans-serif;
  font-size: 42px;
  color: var(--white);
  line-height: 1;
}

.cal-02-banner-sub {
  font-size: 11px;
  color: rgba(255,255,255,0.5);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-top: 4px;
}

.cal-02-banner-nav {
  display: flex;
  gap: 0;
  border: 2px solid var(--yellow);
  align-self: center;
}

.cal-02-banner-navbtn {
  padding: 8px 16px;
  background: transparent;
  border: none;
  color: var(--yellow);
  font-family: 'IBM Plex Mono', monospace;
  font-size: 18px;
  cursor: pointer;
  transition: background 0.1s;
  user-select: none;
}

.cal-02-banner-navbtn:first-child {
  border-right: 2px solid var(--yellow);
}

.cal-02-banner-navbtn:hover {
  background: var(--yellow);
  color: var(--ink);
}
/* ── Main Calendar Body ── */

.cal-02-main {
  background: var(--white);
  border-right: var(--border);
}

.cal-02-day-labels {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  border-bottom: var(--border);
}

.cal-02-dl {
  padding: 12px 0;
  text-align: center;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  border-right: 2px solid var(--ink);
}

.cal-02-dl:last-child {
  border-right: none;
}

.cal-02-dl.cal-02-weekend {
  background: var(--yellow);
}

.cal-02-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}

.cal-02-cell {
  min-height: 70px;
  border-right: 2px solid rgba(0,0,0,0.12);
  border-bottom: 2px solid rgba(0,0,0,0.12);
  padding: 8px;
  cursor: pointer;
  position: relative;
  transition: background 0.1s;
}

.cal-02-cell:nth-child(7n) {
  border-right: none;
}

.cal-02-cell:nth-last-child(-n+7) {
  border-bottom: none;
}

.cal-02-cell:hover {
  background: rgba(245,200,0,0.12);
}

.cal-02-cell.cal-02-other-month {
  background: rgba(0,0,0,0.03);
}

.cal-02-cell.cal-02-today {
  background: var(--yellow);
}

.cal-02-cell.cal-02-today .cal-02-num {
  color: var(--ink);
}

.cal-02-cell.cal-02-today::after {
  content: '◀ TODAY';
  position: absolute;
  right: 6px;
  bottom: 6px;
  font-size: 8px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--red);
}

.cal-02-cell.cal-02-selected {
  background: var(--red);
  box-shadow: inset 4px 4px 0 rgba(0,0,0,0.25);
}

.cal-02-cell.cal-02-selected .cal-02-num {
  color: #fff;
}

.cal-02-cell.cal-02-has-event::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}

.cal-02-cell.cal-02-ev-red::before {
  background: var(--red);
}

.cal-02-cell.cal-02-ev-blue::before {
  background: var(--blue);
}

.cal-02-cell.cal-02-ev-yellow::before {
  background: var(--yellow);
  border-bottom: 2px solid var(--ink);
}

.cal-02-num {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 28px;
  line-height: 1;
  color: var(--ink);
}

.cal-02-cell.cal-02-other-month .cal-02-num {
  color: rgba(0,0,0,0.2);
}

.cal-02-event-tag {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--white);
  background: var(--blue);
  padding: 2px 5px;
  display: inline-block;
  margin-top: 4px;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cal-02-event-tag.cal-02-red {
  background: var(--red);
}
/* ── Sidebar ── */

.cal-02-sidebar {
  background: var(--ink);
  color: var(--white);
  display: flex;
  flex-direction: column;
}

.cal-02-sb-section {
  padding: 20px;
  border-bottom: 2px solid rgba(255,255,255,0.1);
}

.cal-02-sb-section:last-child {
  border-bottom: none;
  flex: 1;
}

.cal-02-sb-label {
  font-size: 9px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.4);
  margin-bottom: 12px;
}

.cal-02-sb-big {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 64px;
  color: var(--yellow);
  line-height: 1;
  animation: cal02-flicker 7s infinite 1s;
}

.cal-02-sb-biginfo {
  font-size: 11px;
  color: rgba(255,255,255,0.5);
  margin-top: 4px;
  letter-spacing: 0.1em;
}
/* Event list */

.cal-02-evlist-item {
  display: flex;
  align-items: stretch;
  gap: 10px;
  margin-bottom: 12px;
  animation: cal02-slide-in 0.4s ease both;
}

.cal-02-evlist-item:nth-child(2) {
  animation-delay: 0.08s;
}

.cal-02-evlist-item:nth-child(3) {
  animation-delay: 0.16s;
}

.cal-02-ev-bar {
  width: 4px;
  flex-shrink: 0;
}

.cal-02-ev-bar.cal-02-red {
  background: var(--red);
}

.cal-02-ev-bar.cal-02-yellow {
  background: var(--yellow);
}

.cal-02-ev-bar.cal-02-blue {
  background: var(--blue);
}

.cal-02-ev-info {
}

.cal-02-ev-name {
  font-size: 12px;
  font-weight: 700;
  color: var(--white);
  letter-spacing: 0.02em;
}

.cal-02-ev-time {
  font-size: 10px;
  color: rgba(255,255,255,0.4);
  margin-top: 2px;
}
/* Cursor blink in terminal style */

.cal-02-cursor {
  display: inline-block;
  width: 10px;
  height: 14px;
  background: var(--yellow);
  vertical-align: middle;
  animation: cal02-blink 1s step-end infinite;
  margin-left: 4px;
}
/* Stats row */

.cal-02-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: rgba(255,255,255,0.1);
}

.cal-02-stat {
  padding: 12px;
  background: var(--ink);
}

.cal-02-stat-val {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 30px;
  color: var(--yellow);
}

.cal-02-stat-lbl {
  font-size: 9px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.35);
  margin-top: 2px;
}
/* Stamp decoration */

.cal-02-stamp {
  border: 3px solid var(--red);
  color: var(--red);
  font-family: 'Bebas Neue', sans-serif;
  font-size: 16px;
  letter-spacing: 0.2em;
  padding: 6px 10px;
  display: inline-block;
  transform: rotate(-8deg);
  opacity: 0.7;
  margin-top: 12px;
  align-self: flex-start;
}

@media (max-width: 680px) {
  .cal-02-wrapper {
    grid-template-columns: 1fr;
  }

  .cal-02-sidebar {
    display: none;
  }

  .cal-02-banner-month {
    font-size: 48px;
  }

  .cal-02-cell {
    min-height: 50px;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
    *::before,
    *::after {
    animation: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal-02-brutCal .cal-02-cell:not(.cal-02-other-month)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal-02-brutCal .cal-02-cell').forEach(c => c.classList.remove('cal-02-selected'));
    this.classList.add('cal-02-selected');
  });
});
```
