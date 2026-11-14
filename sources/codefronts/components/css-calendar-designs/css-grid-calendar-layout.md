---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/css-grid-calendar-layout/"
title: "CSS Grid Calendar Layout"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "An editorial magazine layout showcasing display:grid with grid-template-columns:repeat(7,1fr)."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Calendar Layout
Source: https://codefronts.com/components/css-calendar-designs/css-grid-calendar-layout/

An editorial magazine layout showcasing display:grid with grid-template-columns:repeat(7,1fr). A 1px gap over a colored parent fakes clean grid lines; column headers and date grid share the same 7-track system. Playfair Display masthead, rust/sage/sand event labels.
## HTML
```html
<div class="cal05">
  <div class="cal05__shell">

    <!-- Masthead -->
    <div class="cal05__masthead">
      <div class="cal05__masthead-left">Vol. VI &nbsp;·&nbsp; Issue 6 &nbsp;·&nbsp; Q2 2026</div>
      <div class="cal05__masthead-center">
        <div class="cal05__title">June<span>.</span></div>
        <div class="cal05__subtitle">CSS Grid Calendar Layout &nbsp;·&nbsp; display: grid; repeat(7, 1fr)</div>
      </div>
      <div class="cal05__masthead-right">
        <div class="cal05__nav">
          <div class="cal05__nav-btn">←</div>
          <div class="cal05__nav-btn">→</div>
        </div>
      </div>
    </div>

    <!-- Column headers — also a 7-col grid -->
    <div class="cal05__col-headers">
      <div class="cal05__col-header cal05__col-header--weekend">
        <div class="cal05__col-day-abbr">Sun</div>
        <div class="cal05__col-day-num">wk</div>
      </div>
      <div class="cal05__col-header">
        <div class="cal05__col-day-abbr">Mon</div>
        <div class="cal05__col-day-num">col 2</div>
      </div>
      <div class="cal05__col-header">
        <div class="cal05__col-day-abbr">Tue</div>
        <div class="cal05__col-day-num">col 3</div>
      </div>
      <div class="cal05__col-header">
        <div class="cal05__col-day-abbr">Wed</div>
        <div class="cal05__col-day-num">col 4</div>
      </div>
      <div class="cal05__col-header">
        <div class="cal05__col-day-abbr">Thu</div>
        <div class="cal05__col-day-num">col 5</div>
      </div>
      <div class="cal05__col-header">
        <div class="cal05__col-day-abbr">Fri</div>
        <div class="cal05__col-day-num">col 6</div>
      </div>
      <div class="cal05__col-header cal05__col-header--weekend">
        <div class="cal05__col-day-abbr">Sat</div>
        <div class="cal05__col-day-num">col 7</div>
      </div>
    </div>

    <!--
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        CSS GRID: display:grid; grid-template-columns:repeat(7,1fr)
        Each .cal05__cell auto-places into the next column.
        grid-auto-rows: minmax(100px, auto) — rows expand to fit content.
        gap: 1px + background on parent = visible grid lines.
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    -->
    <div class="cal05__grid" id="cal05Grid">

      <!-- Row 1: May overflow (grid auto-places, starts col 1 = Sun) -->
      <div class="cal05__cell cal05__cell--other cal05__cell--weekend">
        <div class="cal05__week-tag">W21</div>
        <div class="cal05__cell-num">25</div>
      </div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">26</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">27</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">28</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">29</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">30</div></div>
      <div class="cal05__cell cal05__cell--other cal05__cell--weekend"><div class="cal05__cell-num">31</div></div>

      <!-- Row 2 -->
      <div class="cal05__cell cal05__cell--weekend">
        <div class="cal05__week-tag">W22</div>
        <div class="cal05__cell-num">1</div>
      </div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">2</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--rust">Design Sprint</div>
        </div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">3</div></div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">4</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--sand">Holiday</div>
        </div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">5</div></div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">6</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--sage">Deadline</div>
        </div>
      </div>
      <div class="cal05__cell cal05__cell--weekend"><div class="cal05__cell-num">7</div></div>

      <!-- Row 3: Today = Jun 8 (Sunday) -->
      <div class="cal05__cell cal05__cell--today cal05__cell--weekend" id="cal05Today">
        <div class="cal05__week-tag">W23</div>
        <div class="cal05__cell-num">8</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--rust">Today</div>
        </div>
      </div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">9</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--sage">Sprint</div>
        </div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">10</div></div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">11</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--rust">Launch</div>
          <div class="cal05__event cal05__event--ink">All-hands</div>
        </div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">12</div></div>
      <div class="cal05__cell"><div class="cal05__cell-num">13</div></div>
      <div class="cal05__cell cal05__cell--weekend"><div class="cal05__cell-num">14</div></div>

      <!-- Row 4 -->
      <div class="cal05__cell cal05__cell--weekend">
        <div class="cal05__week-tag">W24</div>
        <div class="cal05__cell-num">15</div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">16</div></div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">17</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--sand">Demo Day</div>
          <div class="cal05__event cal05__event--sage">Q2 Report</div>
        </div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">18</div></div>
      <div class="cal05__cell"><div class="cal05__cell-num">19</div></div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">20</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--rust">Board Mtg</div>
        </div>
      </div>
      <div class="cal05__cell cal05__cell--weekend"><div class="cal05__cell-num">21</div></div>

      <!-- Row 5 -->
      <div class="cal05__cell cal05__cell--weekend">
        <div class="cal05__week-tag">W25</div>
        <div class="cal05__cell-num">22</div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">23</div></div>
      <div class="cal05__cell"><div class="cal05__cell-num">24</div></div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">25</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--ink">Planning</div>
        </div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">26</div></div>
      <div class="cal05__cell">
        <div class="cal05__cell-num">27</div>
        <div class="cal05__cell-events">
          <div class="cal05__event cal05__event--sage">Retro</div>
        </div>
      </div>
      <div class="cal05__cell cal05__cell--weekend"><div class="cal05__cell-num">28</div></div>

      <!-- Row 6 -->
      <div class="cal05__cell cal05__cell--weekend">
        <div class="cal05__week-tag">W26</div>
        <div class="cal05__cell-num">29</div>
      </div>
      <div class="cal05__cell"><div class="cal05__cell-num">30</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">1</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">2</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">3</div></div>
      <div class="cal05__cell cal05__cell--other"><div class="cal05__cell-num">4</div></div>
      <div class="cal05__cell cal05__cell--other cal05__cell--weekend"><div class="cal05__cell-num">5</div></div>

    </div><!-- /grid -->

    <!-- Annotation strip -->
    <div class="cal05__annotation">
      <div class="cal05__ann-cell">
        <div class="cal05__ann-label">Grid columns</div>
        <div class="cal05__ann-value">7</div>
        <div class="cal05__ann-sub">repeat(7, 1fr)</div>
      </div>
      <div class="cal05__ann-cell">
        <div class="cal05__ann-label">Events this month</div>
        <div class="cal05__ann-value">11</div>
        <div class="cal05__ann-sub">across 30 days</div>
      </div>
      <div class="cal05__ann-cell">
        <div class="cal05__ann-label">Week in year</div>
        <div class="cal05__ann-value">W23</div>
        <div class="cal05__ann-sub">Q2 · Day 159</div>
      </div>
    </div>

    <!-- Legend -->
    <div class="cal05__legend">
      <span class="cal05__legend-label">Legend:</span>
      <div class="cal05__legend-item"><div class="cal05__legend-swatch" style="background:#c94f2c"></div>Priority</div>
      <div class="cal05__legend-item"><div class="cal05__legend-swatch" style="background:#4a7c6f"></div>Milestone</div>
      <div class="cal05__legend-item"><div class="cal05__legend-swatch" style="background:#d4a853"></div>Holiday</div>
      <div class="cal05__legend-item"><div class="cal05__legend-swatch" style="background:#1a1a2e"></div>General</div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal05,
.cal05 *,
.cal05 *::before,
.cal05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal05 ::selection {
  background: #1a1a2e;
  color: #f5e6c8;
}

.cal05 {
  --cream: #f8f4ed;
  --warm: #ede5d5;
  --ink: #1a1a2e;
  --ink2: #4a4a6a;
  --ink3: #8a8aaa;
  --rust: #c94f2c;
  --sage: #4a7c6f;
  --sand: #d4a853;
  --grid-gap: 1px;
  --border: rgba(26,26,46,0.1);
  font-family: 'Barlow', sans-serif;
  background: var(--cream);
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

@keyframes cal05-enter {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes cal05-highlight {
  from {
    background: rgba(201,79,44,0.15);
  }

  to {
    background: transparent;
  }
}
/* ── Shell ── */

.cal05__shell {
  width: 100%;
  max-width: 900px;
  animation: cal05-enter 0.5s ease both;
}
/* ── Masthead ── */

.cal05__masthead {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: end;
  padding-bottom: 20px;
  border-bottom: 3px double var(--ink);
  margin-bottom: 0;
}

.cal05__masthead-left {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--ink3);
  align-self: center;
}

.cal05__masthead-center {
  text-align: center;
  padding: 0 32px;
}

.cal05__title {
  font-family: 'Playfair Display', serif;
  font-size: 80px;
  font-weight: 900;
  font-style: italic;
  line-height: 0.9;
  letter-spacing: -0.02em;
  color: var(--ink);
}

.cal05__title span {
  color: var(--rust);
}

.cal05__subtitle {
  font-size: 11px;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--ink3);
  margin-top: 8px;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: 6px 0;
}

.cal05__masthead-right {
  text-align: right;
  align-self: center;
}

.cal05__nav {
  display: flex;
  gap: 4px;
  justify-content: flex-end;
}

.cal05__nav-btn {
  width: 36px;
  height: 36px;
  border: 1.5px solid var(--ink);
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 16px;
  color: var(--ink);
  transition: all 0.15s;
  font-family: 'Barlow', sans-serif;
  user-select: none;
}

.cal05__nav-btn:hover {
  background: var(--ink);
  color: var(--cream);
}
/* ── Column headers ── */

.cal05__col-headers {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: var(--grid-gap);
  background: var(--border);
  border-left: 1px solid var(--border);
  border-right: 1px solid var(--border);
  margin-top: 24px;
}

.cal05__col-header {
  background: var(--warm);
  padding: 10px 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.cal05__col-day-abbr {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ink3);
}

.cal05__col-day-num {
  font-family: 'Playfair Display', serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--ink);
  line-height: 1;
}
/* Highlight the current day column header */

.cal05__col-header--today .cal05__col-day-abbr {
  color: var(--rust);
}

.cal05__col-header--today .cal05__col-day-num {
  color: var(--rust);
}

.cal05__col-header--weekend .cal05__col-day-abbr {
  color: var(--sage);
  opacity: 0.7;
}
/* ── Main CSS Grid: The Star of the Show ── */
/*
  Core technique:
  - display: grid
  - grid-template-columns: repeat(7, 1fr) — 7 equal columns for 7 days
  - gap creates the gutters; background on the container "fakes" visible grid lines
  - Each cell: grid-column auto-places days correctly
  - named grid areas optionally mark special rows
*/

.cal05__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: minmax(100px, auto);
  gap: var(--grid-gap);
  background: var(--border);
  /* gap shows through as grid lines */
  border: 1px solid var(--border);
  border-top: none;
}
/* ── Individual date cells ── */

.cal05__cell {
  background: var(--cream);
  padding: 10px 12px 8px;
  cursor: pointer;
  transition: background 0.15s;
  display: flex;
  flex-direction: column;
  gap: 4px;
  position: relative;
  min-height: 100px;
}

.cal05__cell:hover {
  background: rgba(212,168,83,0.08);
}

.cal05__cell--other {
  background: var(--warm);
  opacity: 0.5;
  pointer-events: none;
}

.cal05__cell--weekend {
  background: #f5f0e6;
}

.cal05__cell--today {
  background: #fff9f0;
}

.cal05__cell--today::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--rust);
}

.cal05__cell--selected {
  background: rgba(201,79,44,0.06);
  outline: 2px solid var(--rust);
  outline-offset: -2px;
  z-index: 2;
}
/* Cell number */

.cal05__cell-num {
  font-family: 'Playfair Display', serif;
  font-size: 20px;
  font-weight: 700;
  line-height: 1;
  color: var(--ink);
}

.cal05__cell--today .cal05__cell-num {
  color: var(--rust);
}

.cal05__cell--other .cal05__cell-num {
  color: var(--ink3);
}

.cal05__cell--weekend:not(.cal05__cell--today) .cal05__cell-num {
  color: var(--sage);
}
/* Week number annotation */

.cal05__week-tag {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 9px;
  letter-spacing: 0.1em;
  color: var(--ink3);
  opacity: 0.5;
}
/* Events inside cells */

.cal05__cell-events {
  display: flex;
  flex-direction: column;
  gap: 3px;
  margin-top: auto;
}

.cal05__event {
  font-size: 10px;
  font-weight: 500;
  padding: 3px 6px;
  border-left: 3px solid transparent;
  letter-spacing: 0.02em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  background: rgba(26,26,46,0.04);
}

.cal05__event--rust {
  border-left-color: var(--rust);
  color: var(--rust);
  background: rgba(201,79,44,0.06);
}

.cal05__event--sage {
  border-left-color: var(--sage);
  color: var(--sage);
  background: rgba(74,124,111,0.08);
}

.cal05__event--sand {
  border-left-color: var(--sand);
  color: #8b6914;
  background: rgba(212,168,83,0.1);
}

.cal05__event--ink {
  border-left-color: var(--ink);
  color: var(--ink2);
}
/* ── Grid annotation panel below ── */

.cal05__annotation {
  margin-top: 20px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
}

.cal05__ann-cell {
  background: var(--cream);
  padding: 16px 20px;
}

.cal05__ann-label {
  font-size: 9px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--ink3);
  margin-bottom: 6px;
}

.cal05__ann-value {
  font-family: 'Playfair Display', serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--ink);
  line-height: 1;
}

.cal05__ann-sub {
  font-size: 11px;
  color: var(--ink3);
  margin-top: 4px;
}
/* ── Legend ── */

.cal05__legend {
  margin-top: 16px;
  display: flex;
  gap: 20px;
  align-items: center;
  padding: 12px 0;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

.cal05__legend-label {
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ink3);
  margin-right: 4px;
}

.cal05__legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  color: var(--ink2);
}

.cal05__legend-swatch {
  width: 16px;
  height: 3px;
  border-radius: 1px;
}

@media (max-width: 640px) {
  .cal05__title {
    font-size: 48px;
  }

  .cal05__masthead {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .cal05__masthead-right {
    text-align: left;
  }

  .cal05__grid {
    grid-auto-rows: minmax(70px, auto);
  }

  .cal05__cell {
    padding: 6px 8px;
  }

  .cal05__cell-num {
    font-size: 15px;
  }

  .cal05__event {
    display: none;
  }

  .cal05__annotation {
    grid-template-columns: 1fr 1fr;
  }

  .cal05__ann-cell:last-child {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal05 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal05Grid .cal05__cell:not(.cal05__cell--other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal05Grid .cal05__cell').forEach(c => c.classList.remove('cal05__cell--selected'));
    this.classList.add('cal05__cell--selected');
  });
});
```
