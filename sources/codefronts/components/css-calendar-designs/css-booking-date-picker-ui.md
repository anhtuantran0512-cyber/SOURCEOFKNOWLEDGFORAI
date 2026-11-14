---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/css-booking-date-picker-ui/"
title: "CSS Booking Date Picker UI"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A travel/reservation dual-month range picker."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Booking Date Picker UI
Source: https://codefronts.com/components/css-calendar-designs/css-booking-date-picker-ui/

A travel/reservation dual-month range picker. Range days get a band that stretches edge-to-edge via full-width ::before; endpoints use half-width bands so the highlight connects across rows. Live check-in/out summary and night count; click to set start then end.
## HTML
```html
<div class="cal13">
  <div class="cal13__card">

    <!-- Summary -->
    <div class="cal13__summary">
      <div class="cal13__sum-block active">
        <div class="cal13__sum-label">Check-in</div>
        <div class="cal13__sum-value" id="cal13In">Jun 11</div>
      </div>
      <div class="cal13__sum-arrow">→</div>
      <div class="cal13__sum-block">
        <div class="cal13__sum-label">Check-out</div>
        <div class="cal13__sum-value" id="cal13Out">Jun 17</div>
      </div>
      <div class="cal13__sum-nights">
        <div class="cal13__nights-num" id="cal13Nights">6</div>
        <div class="cal13__nights-lbl">Nights</div>
      </div>
    </div>

    <!-- Dual months -->
    <div class="cal13__months">

      <!-- June -->
      <div class="cal13__month">
        <div class="cal13__month-head">
          <div class="cal13__month-nav" id="cal13Prev">‹</div>
          <div class="cal13__month-name">June 2026</div>
          <div class="cal13__month-nav ghost">›</div>
        </div>
        <div class="cal13__dow">
          <div class="cal13__dw">Su</div><div class="cal13__dw">Mo</div><div class="cal13__dw">Tu</div>
          <div class="cal13__dw">We</div><div class="cal13__dw">Th</div><div class="cal13__dw">Fr</div><div class="cal13__dw">Sa</div>
        </div>
        <div class="cal13__grid" id="cal13June">
          <div class="cal13__cell other"><span class="n">25</span></div><div class="cal13__cell other"><span class="n">26</span></div><div class="cal13__cell other"><span class="n">27</span></div>
          <div class="cal13__cell other"><span class="n">28</span></div><div class="cal13__cell other"><span class="n">29</span></div><div class="cal13__cell other"><span class="n">30</span></div><div class="cal13__cell other"><span class="n">31</span></div>
          <div class="cal13__cell disabled"><span class="n">1</span></div>
          <div class="cal13__cell disabled"><span class="n">2</span></div>
          <div class="cal13__cell disabled"><span class="n">3</span></div>
          <div class="cal13__cell disabled"><span class="n">4</span></div>
          <div class="cal13__cell disabled"><span class="n">5</span></div>
          <div class="cal13__cell disabled"><span class="n">6</span></div>
          <div class="cal13__cell disabled"><span class="n">7</span></div>
          <div class="cal13__cell today" data-d="8"><span class="n">8</span></div>
          <div class="cal13__cell" data-d="9"><span class="n">9</span></div>
          <div class="cal13__cell" data-d="10"><span class="n">10</span></div>
          <div class="cal13__cell range-start" data-d="11"><span class="n">11</span></div>
          <div class="cal13__cell in-range" data-d="12"><span class="n">12</span></div>
          <div class="cal13__cell in-range" data-d="13"><span class="n">13</span></div>
          <div class="cal13__cell in-range" data-d="14"><span class="n">14</span></div>
          <div class="cal13__cell in-range" data-d="15"><span class="n">15</span></div>
          <div class="cal13__cell in-range" data-d="16"><span class="n">16</span></div>
          <div class="cal13__cell range-end" data-d="17"><span class="n">17</span></div>
          <div class="cal13__cell" data-d="18"><span class="n">18</span></div>
          <div class="cal13__cell" data-d="19"><span class="n">19</span></div>
          <div class="cal13__cell" data-d="20"><span class="n">20</span></div>
          <div class="cal13__cell" data-d="21"><span class="n">21</span></div>
          <div class="cal13__cell" data-d="22"><span class="n">22</span></div>
          <div class="cal13__cell" data-d="23"><span class="n">23</span></div>
          <div class="cal13__cell" data-d="24"><span class="n">24</span></div>
          <div class="cal13__cell" data-d="25"><span class="n">25</span></div>
          <div class="cal13__cell" data-d="26"><span class="n">26</span></div>
          <div class="cal13__cell" data-d="27"><span class="n">27</span></div>
          <div class="cal13__cell" data-d="28"><span class="n">28</span></div>
          <div class="cal13__cell" data-d="29"><span class="n">29</span></div>
          <div class="cal13__cell" data-d="30"><span class="n">30</span></div>
        </div>
      </div>

      <!-- July -->
      <div class="cal13__month">
        <div class="cal13__month-head">
          <div class="cal13__month-nav ghost">‹</div>
          <div class="cal13__month-name">July 2026</div>
          <div class="cal13__month-nav" id="cal13Next">›</div>
        </div>
        <div class="cal13__dow">
          <div class="cal13__dw">Su</div><div class="cal13__dw">Mo</div><div class="cal13__dw">Tu</div>
          <div class="cal13__dw">We</div><div class="cal13__dw">Th</div><div class="cal13__dw">Fr</div><div class="cal13__dw">Sa</div>
        </div>
        <div class="cal13__grid" id="cal13July">
          <div class="cal13__cell other"><span class="n">29</span></div><div class="cal13__cell other"><span class="n">30</span></div>
          <div class="cal13__cell" data-d="101"><span class="n">1</span></div>
          <div class="cal13__cell" data-d="102"><span class="n">2</span></div>
          <div class="cal13__cell" data-d="103"><span class="n">3</span></div>
          <div class="cal13__cell" data-d="104"><span class="n">4</span></div>
          <div class="cal13__cell" data-d="105"><span class="n">5</span></div>
          <div class="cal13__cell" data-d="106"><span class="n">6</span></div>
          <div class="cal13__cell" data-d="107"><span class="n">7</span></div>
          <div class="cal13__cell" data-d="108"><span class="n">8</span></div>
          <div class="cal13__cell" data-d="109"><span class="n">9</span></div>
          <div class="cal13__cell" data-d="110"><span class="n">10</span></div>
          <div class="cal13__cell" data-d="111"><span class="n">11</span></div>
          <div class="cal13__cell" data-d="112"><span class="n">12</span></div>
          <div class="cal13__cell" data-d="113"><span class="n">13</span></div>
          <div class="cal13__cell" data-d="114"><span class="n">14</span></div>
          <div class="cal13__cell" data-d="115"><span class="n">15</span></div>
          <div class="cal13__cell" data-d="116"><span class="n">16</span></div>
          <div class="cal13__cell" data-d="117"><span class="n">17</span></div>
          <div class="cal13__cell" data-d="118"><span class="n">18</span></div>
          <div class="cal13__cell" data-d="119"><span class="n">19</span></div>
          <div class="cal13__cell" data-d="120"><span class="n">20</span></div>
          <div class="cal13__cell" data-d="121"><span class="n">21</span></div>
          <div class="cal13__cell" data-d="122"><span class="n">22</span></div>
          <div class="cal13__cell" data-d="123"><span class="n">23</span></div>
          <div class="cal13__cell" data-d="124"><span class="n">24</span></div>
          <div class="cal13__cell" data-d="125"><span class="n">25</span></div>
          <div class="cal13__cell" data-d="126"><span class="n">26</span></div>
          <div class="cal13__cell" data-d="127"><span class="n">27</span></div>
          <div class="cal13__cell" data-d="128"><span class="n">28</span></div>
          <div class="cal13__cell" data-d="129"><span class="n">29</span></div>
          <div class="cal13__cell" data-d="130"><span class="n">30</span></div>
          <div class="cal13__cell" data-d="131"><span class="n">31</span></div>
        </div>
      </div>

    </div>

    <!-- Footer -->
    <div class="cal13__foot">
      <div class="cal13__foot-legend">
        <div class="cal13__leg"><span class="cal13__leg-sw" style="background:var(--teal)"></span>Selected</div>
        <div class="cal13__leg"><span class="cal13__leg-sw" style="background:var(--range)"></span>In range</div>
      </div>
      <div class="cal13__foot-actions">
        <button class="cal13__btn cal13__btn--ghost" id="cal13Clear">Clear</button>
        <button class="cal13__btn cal13__btn--solid">Reserve · 6 nights</button>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal13,
.cal13 *,
.cal13 *::before,
.cal13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal13 ::selection {
  background: #1f6f5c;
  color: #fff;
}

.cal13 {
  --bg: #f4f1ec;
  --card: #ffffff;
  --ink: #1c2825;
  --ink2: #5e6e69;
  --ink3: #a3afab;
  --hair: #ebe7e0;
  --teal: #1f6f5c;
  --teal-d: #16513f;
  --range: #e3f0eb;
  --range-edge: #1f6f5c;
  font-family: 'DM Sans', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

@keyframes cal13-in {
  from {
    opacity: 0;
    transform: translateY(14px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.cal13__card {
  background: var(--card);
  border-radius: 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 24px 60px rgba(28,40,37,0.1);
  overflow: hidden;
  max-width: 720px;
  width: 100%;
  animation: cal13-in 0.5s ease both;
}
/* ── Summary header ── */

.cal13__summary {
  display: flex;
  align-items: stretch;
  border-bottom: 1px solid var(--hair);
}

.cal13__sum-block {
  flex: 1;
  padding: 20px 24px;
  cursor: pointer;
  transition: background 0.15s;
  position: relative;
}

.cal13__sum-block:hover {
  background: #faf9f6;
}

.cal13__sum-block.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 24px;
  right: 24px;
  height: 2px;
  background: var(--teal);
}

.cal13__sum-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink3);
  margin-bottom: 5px;
}

.cal13__sum-value {
  font-family: 'Fraunces', serif;
  font-size: 22px;
  font-weight: 600;
  color: var(--ink);
}

.cal13__sum-value.empty {
  color: var(--ink3);
  font-weight: 400;
}

.cal13__sum-arrow {
  display: flex;
  align-items: center;
  padding: 0 8px;
  color: var(--ink3);
  font-size: 18px;
}

.cal13__sum-nights {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 24px;
  border-left: 1px solid var(--hair);
  background: var(--range);
  min-width: 90px;
}

.cal13__nights-num {
  font-family: 'Fraunces', serif;
  font-size: 28px;
  font-weight: 600;
  color: var(--teal-d);
  line-height: 1;
}

.cal13__nights-lbl {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--teal);
  margin-top: 3px;
}
/* ── Dual month container ── */

.cal13__months {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  padding: 24px;
}

.cal13__month {
  padding: 0 16px;
}

.cal13__month:first-child {
  border-right: 1px solid var(--hair);
}

.cal13__month-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.cal13__month-name {
  font-family: 'Fraunces', serif;
  font-size: 17px;
  font-weight: 600;
  color: var(--ink);
}

.cal13__month-nav {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--ink2);
  font-size: 14px;
  transition: all 0.15s;
  user-select: none;
}

.cal13__month-nav:hover {
  background: var(--hair);
  color: var(--teal);
}

.cal13__month-nav.ghost {
  visibility: hidden;
}

.cal13__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 6px;
}

.cal13__dw {
  text-align: center;
  font-size: 10px;
  font-weight: 700;
  color: var(--ink3);
  letter-spacing: 0.03em;
}

.cal13__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 0;
  row-gap: 2px;
}
/* Each date cell */

.cal13__cell {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 500;
  color: var(--ink);
  cursor: pointer;
  position: relative;
  transition: color 0.12s;
}

.cal13__cell .n {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: relative;
  z-index: 2;
  transition: all 0.12s;
}

.cal13__cell:hover:not(.other):not(.disabled) .n {
  background: var(--hair);
}

.cal13__cell.other {
  color: var(--ink3);
  opacity: 0;
  pointer-events: none;
}

.cal13__cell.disabled {
  color: var(--ink3);
  opacity: 0.4;
  pointer-events: none;
  text-decoration: line-through;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   RANGE SELECTION — the key feature.
   .in-range  → light band background that stretches
   .range-start / .range-end → solid teal endpoints
   The band uses a ::before that fills the full cell width.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal13__cell.in-range::before {
  content: '';
  position: absolute;
  top: 3px;
  bottom: 3px;
  left: 0;
  right: 0;
  background: var(--range);
  z-index: 1;
}

.cal13__cell.range-start::before,
.cal13__cell.range-end::before {
  content: '';
  position: absolute;
  top: 3px;
  bottom: 3px;
  background: var(--range);
  z-index: 1;
}
/* start: band only extends right */

.cal13__cell.range-start::before {
  left: 50%;
  right: 0;
}
/* end: band only extends left */

.cal13__cell.range-end::before {
  left: 0;
  right: 50%;
}
/* single day (start==end): no band */

.cal13__cell.range-start.range-end::before {
  display: none;
}
/* endpoint circles */

.cal13__cell.range-start .n,
.cal13__cell.range-end .n {
  background: var(--teal);
  color: #fff;
  font-weight: 700;
  box-shadow: 0 4px 12px rgba(31,111,92,0.3);
}
/* today marker */

.cal13__cell.today .n {
  border: 1.5px solid var(--teal);
  color: var(--teal);
  font-weight: 700;
}

.cal13__cell.today.range-start .n,
.cal13__cell.today.range-end .n {
  color: #fff;
  border-color: var(--teal);
}
/* ── Footer ── */

.cal13__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 24px;
  border-top: 1px solid var(--hair);
  background: #faf9f6;
}

.cal13__foot-legend {
  display: flex;
  gap: 16px;
}

.cal13__leg {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  color: var(--ink2);
}

.cal13__leg-sw {
  width: 14px;
  height: 14px;
  border-radius: 4px;
}

.cal13__foot-actions {
  display: flex;
  gap: 10px;
}

.cal13__btn {
  padding: 10px 20px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
  user-select: none;
  border: none;
  font-family: 'DM Sans', sans-serif;
}

.cal13__btn--ghost {
  background: transparent;
  color: var(--ink2);
}

.cal13__btn--ghost:hover {
  background: var(--hair);
}

.cal13__btn--solid {
  background: var(--teal);
  color: #fff;
}

.cal13__btn--solid:hover {
  background: var(--teal-d);
}

@media (max-width: 600px) {
  .cal13__months {
    grid-template-columns: 1fr;
  }

  .cal13__month:first-child {
    border-right: none;
    border-bottom: 1px solid var(--hair);
    padding-bottom: 20px;
    margin-bottom: 20px;
  }

  .cal13__sum-nights {
    display: none;
  }

  .cal13__foot {
    flex-direction: column;
    gap: 14px;
    align-items: stretch;
  }

  .cal13__foot-actions {
    justify-content: flex-end;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal13 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const cells = Array.from(document.querySelectorAll('.cal13__cell[data-d]'));
  // Build an ordered index for range math (June 1-30 = 1..30, July = 101..131)
  const order = d => d > 100 ? (30 + (d - 100)) : d;
  let start = 11, end = 17; // June 11 -> June 17

  const monNames = {June:'Jun', July:'Jul'};
  function fmt(d) {
    if (d > 100) return 'Jul ' + (d - 100);
    return 'Jun ' + d;
  }

  function paint() {
    const lo = Math.min(order(start), end ? order(end) : order(start));
    const hi = end ? Math.max(order(start), order(end)) : order(start);
    cells.forEach(c => {
      c.classList.remove('range-start','range-end','in-range');
      const o = order(+c.dataset.d);
      if (end === null) {
        if (+c.dataset.d === start) { c.classList.add('range-start','range-end'); }
      } else {
        if (o === lo) c.classList.add('range-start');
        else if (o === hi) c.classList.add('range-end');
        else if (o > lo && o < hi) c.classList.add('in-range');
      }
    });
    // summary
    const inEl = document.getElementById('cal13In');
    const outEl = document.getElementById('cal13Out');
    const nightsEl = document.getElementById('cal13Nights');
    const sLo = Math.min(order(start), end ? order(end) : order(start));
    const sHi = end ? Math.max(order(start), order(end)) : null;
    inEl.textContent = fmt(order(start) <= (end ? order(end) : 1e9) ? start : end);
    if (end !== null) {
      const lowD = order(start) <= order(end) ? start : end;
      const highD = order(start) <= order(end) ? end : start;
      inEl.textContent = fmt(lowD);
      outEl.textContent = fmt(highD);
      outEl.classList.remove('empty');
      nightsEl.textContent = Math.abs(order(end) - order(start));
    } else {
      outEl.textContent = 'Select';
      outEl.classList.add('empty');
      nightsEl.textContent = '0';
    }
  }

  cells.forEach(c => {
    c.addEventListener('click', () => {
      const d = +c.dataset.d;
      if (end === null) {
        // completing a range
        end = d;
      } else {
        // start a new range
        start = d; end = null;
      }
      paint();
    });
  });

  document.getElementById('cal13Clear').addEventListener('click', () => {
    start = 11; end = 17; paint();
  });

  paint();
})();
```
