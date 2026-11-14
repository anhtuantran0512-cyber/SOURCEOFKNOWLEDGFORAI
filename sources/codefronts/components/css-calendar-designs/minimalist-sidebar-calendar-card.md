---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/minimalist-sidebar-calendar-card/"
title: "Minimalist Sidebar Calendar Card"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "An ultra-clean compact widget sized for a dashboard rail or blog footer."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Sidebar Calendar Card
Source: https://codefronts.com/components/css-calendar-designs/minimalist-sidebar-calendar-card/

An ultra-clean compact widget sized for a dashboard rail or blog footer. Newsreader serif month, tight 1px grid, hairline dividers, a quiet today dot and black-fill selection, a 3-row mini agenda with tabular times, and a footer mini-stat with an add chip.
## HTML
```html
<div class="cal12">
  <div class="cal12__context">
    <div class="cal12__card">

      <div class="cal12__head">
        <div class="cal12__month">June <span>2026</span></div>
        <div class="cal12__nav">
          <div class="cal12__nav-btn">‹</div>
          <div class="cal12__nav-btn">›</div>
        </div>
      </div>

      <div class="cal12__dow">
        <div class="cal12__dw">S</div><div class="cal12__dw">M</div><div class="cal12__dw">T</div>
        <div class="cal12__dw">W</div><div class="cal12__dw">T</div><div class="cal12__dw">F</div><div class="cal12__dw">S</div>
      </div>

      <div class="cal12__grid" id="cal12Grid">
        <div class="cal12__cell other">25</div><div class="cal12__cell other">26</div><div class="cal12__cell other">27</div>
        <div class="cal12__cell other">28</div><div class="cal12__cell other">29</div><div class="cal12__cell other">30</div><div class="cal12__cell other">31</div>
        <div class="cal12__cell">1</div>
        <div class="cal12__cell has-ev">2</div>
        <div class="cal12__cell">3</div>
        <div class="cal12__cell has-ev">4</div>
        <div class="cal12__cell">5</div>
        <div class="cal12__cell">6</div>
        <div class="cal12__cell">7</div>
        <div class="cal12__cell today selected">8</div>
        <div class="cal12__cell has-ev">9</div>
        <div class="cal12__cell">10</div>
        <div class="cal12__cell has-ev">11</div>
        <div class="cal12__cell">12</div>
        <div class="cal12__cell has-ev">13</div>
        <div class="cal12__cell">14</div>
        <div class="cal12__cell">15</div>
        <div class="cal12__cell">16</div>
        <div class="cal12__cell has-ev">17</div>
        <div class="cal12__cell">18</div>
        <div class="cal12__cell">19</div>
        <div class="cal12__cell has-ev">20</div>
        <div class="cal12__cell">21</div>
        <div class="cal12__cell">22</div>
        <div class="cal12__cell">23</div>
        <div class="cal12__cell">24</div>
        <div class="cal12__cell has-ev">25</div>
        <div class="cal12__cell">26</div>
        <div class="cal12__cell">27</div>
        <div class="cal12__cell">28</div>
        <div class="cal12__cell">29</div>
        <div class="cal12__cell">30</div>
        <div class="cal12__cell other">1</div><div class="cal12__cell other">2</div><div class="cal12__cell other">3</div>
        <div class="cal12__cell other">4</div><div class="cal12__cell other">5</div>
      </div>

      <div class="cal12__rule"></div>

      <div class="cal12__agenda-label">Today</div>
      <div class="cal12__ev">
        <div class="cal12__ev-time">10:00</div>
        <div class="cal12__ev-bar" style="background:var(--accent)"></div>
        <div class="cal12__ev-name">Sprint Planning</div>
      </div>
      <div class="cal12__ev">
        <div class="cal12__ev-time">14:00</div>
        <div class="cal12__ev-bar" style="background:#3b82f6"></div>
        <div class="cal12__ev-name">Product Launch</div>
      </div>
      <div class="cal12__ev">
        <div class="cal12__ev-time">16:30</div>
        <div class="cal12__ev-bar" style="background:#10b981"></div>
        <div class="cal12__ev-name">Design Review</div>
      </div>

      <div class="cal12__foot">
        <div class="cal12__foot-text"><b>3</b> events today</div>
        <div class="cal12__foot-btn">+ Add</div>
      </div>

    </div>
    <div class="cal12__caption">— sidebar widget, actual size —</div>
  </div>
</div>
```
## CSS
```css
.cal12,
.cal12 *,
.cal12 *::before,
.cal12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal12 ::selection {
  background: #111;
  color: #fff;
}

.cal12 {
  --paper: #fcfcfa;
  --ink: #14140f;
  --ink2: #6e6e64;
  --ink3: #b8b8ad;
  --hair: #ebebe4;
  --accent: #d94f30;
  --accent-soft: #fbe9e4;
  font-family: 'Inter Tight', sans-serif;
  background: #f0f0eb;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

@keyframes cal12-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* Mock sidebar context to show scale */

.cal12__context {
  width: 100%;
  max-width: 300px;
  animation: cal12-in 0.45s ease both;
}
/* ── The compact card ── */

.cal12__card {
  background: var(--paper);
  border: 1px solid var(--hair);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03), 0 8px 24px rgba(0,0,0,0.04);
}
/* ── Header ── */

.cal12__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 18px;
}

.cal12__month {
  font-family: 'Newsreader', serif;
  font-size: 21px;
  font-weight: 500;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.cal12__month span {
  color: var(--ink3);
  font-weight: 400;
}

.cal12__nav {
  display: flex;
  gap: 2px;
}

.cal12__nav-btn {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  cursor: pointer;
  color: var(--ink2);
  font-size: 13px;
  transition: all 0.15s;
  user-select: none;
}

.cal12__nav-btn:hover {
  background: var(--hair);
  color: var(--ink);
}
/* ── DOW ── */

.cal12__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 6px;
}

.cal12__dw {
  text-align: center;
  font-size: 10px;
  font-weight: 600;
  color: var(--ink3);
  letter-spacing: 0.04em;
  padding: 2px 0;
}
/* ── Grid — tight ── */

.cal12__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 1px;
}

.cal12__cell {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 500;
  color: var(--ink);
  cursor: pointer;
  border-radius: 8px;
  position: relative;
  transition: all 0.13s;
}

.cal12__cell:hover {
  background: var(--hair);
}

.cal12__cell.other {
  color: var(--ink3);
  opacity: 0.55;
  pointer-events: none;
}

.cal12__cell.today {
  font-weight: 700;
  color: var(--accent);
}

.cal12__cell.today::after {
  content: '';
  position: absolute;
  bottom: 4px;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--accent);
}

.cal12__cell.selected {
  background: var(--ink);
  color: var(--paper);
  font-weight: 600;
}

.cal12__cell.selected.today {
  color: var(--paper);
}

.cal12__cell.selected.today::after {
  background: var(--paper);
}
/* tiny event marker */

.cal12__cell.has-ev:not(.selected)::before {
  content: '';
  position: absolute;
  top: 5px;
  right: 5px;
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: var(--ink3);
}
/* ── Divider ── */

.cal12__rule {
  height: 1px;
  background: var(--hair);
  margin: 18px 0 14px;
}
/* ── Mini agenda ── */

.cal12__agenda-label {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink3);
  margin-bottom: 12px;
}

.cal12__ev {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 0;
}

.cal12__ev-time {
  font-size: 11px;
  font-weight: 600;
  color: var(--ink2);
  width: 38px;
  flex-shrink: 0;
  font-variant-numeric: tabular-nums;
}

.cal12__ev-bar {
  width: 2px;
  align-self: stretch;
  border-radius: 1px;
  flex-shrink: 0;
}

.cal12__ev-name {
  font-size: 12px;
  font-weight: 500;
  color: var(--ink);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
/* ── Footer mini-stat ── */

.cal12__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--hair);
}

.cal12__foot-text {
  font-size: 11px;
  color: var(--ink2);
}

.cal12__foot-text b {
  color: var(--ink);
  font-weight: 700;
}

.cal12__foot-btn {
  font-size: 11px;
  font-weight: 600;
  color: var(--accent);
  cursor: pointer;
  padding: 4px 10px;
  border-radius: 8px;
  background: var(--accent-soft);
  transition: all 0.15s;
  user-select: none;
}

.cal12__foot-btn:hover {
  background: var(--accent);
  color: #fff;
}
/* Caption beneath card */

.cal12__caption {
  text-align: center;
  font-size: 11px;
  color: #aaa;
  margin-top: 14px;
  letter-spacing: 0.05em;
}

@media (prefers-reduced-motion: reduce) {
  .cal12 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal12Grid .cal12__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal12Grid .cal12__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
