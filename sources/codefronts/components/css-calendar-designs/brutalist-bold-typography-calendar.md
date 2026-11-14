---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/brutalist-bold-typography-calendar/"
title: "Brutalist Bold Typography Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Neo-brutalism with 5px solid borders, hard offset shadow, zero radius and a slam entrance."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Bold Typography Calendar
Source: https://codefronts.com/components/css-calendar-designs/brutalist-bold-typography-calendar/

Neo-brutalism with 5px solid borders, hard offset shadow, zero radius and a slam entrance. Archivo Black 64px month, oversized date numerals, mismatched primary colors, a red NOW tag and bordered event squares, plus clashing solid-color footer stat blocks.
## HTML
```html
<div class="cal18">
  <div class="cal18__wrap">

    <div class="cal18__head">
      <div class="cal18__month">
        <div class="cal18__month-name">JUNE</div>
        <div class="cal18__month-year">2026 // Q2 // WK23</div>
      </div>
      <div class="cal18__nav">
        <button class="cal18__nav-btn">↑</button>
        <button class="cal18__nav-btn">↓</button>
      </div>
    </div>

    <div class="cal18__dow">
      <div class="cal18__dw">SU</div><div class="cal18__dw">MO</div><div class="cal18__dw">TU</div>
      <div class="cal18__dw">WE</div><div class="cal18__dw">TH</div><div class="cal18__dw">FR</div><div class="cal18__dw">SA</div>
    </div>

    <div class="cal18__grid" id="cal18Grid">
      <div class="cal18__cell other">25</div><div class="cal18__cell other">26</div><div class="cal18__cell other">27</div>
      <div class="cal18__cell other">28</div><div class="cal18__cell other">29</div><div class="cal18__cell other">30</div><div class="cal18__cell other">31</div>
      <div class="cal18__cell">1</div>
      <div class="cal18__cell">2<span class="ev ev--r"></span></div>
      <div class="cal18__cell">3</div>
      <div class="cal18__cell">4<span class="ev ev--g"></span></div>
      <div class="cal18__cell">5</div>
      <div class="cal18__cell">6</div>
      <div class="cal18__cell">7<span class="ev ev--p"></span></div>
      <div class="cal18__cell today selected">8</div>
      <div class="cal18__cell">9<span class="ev ev--r"></span></div>
      <div class="cal18__cell">10</div>
      <div class="cal18__cell">11<span class="ev ev--g"></span></div>
      <div class="cal18__cell">12</div>
      <div class="cal18__cell">13<span class="ev ev--p"></span></div>
      <div class="cal18__cell">14</div>
      <div class="cal18__cell">15</div>
      <div class="cal18__cell">16</div>
      <div class="cal18__cell">17<span class="ev ev--r"></span></div>
      <div class="cal18__cell">18</div>
      <div class="cal18__cell">19</div>
      <div class="cal18__cell">20<span class="ev ev--g"></span></div>
      <div class="cal18__cell">21</div>
      <div class="cal18__cell">22</div>
      <div class="cal18__cell">23<span class="ev ev--p"></span></div>
      <div class="cal18__cell">24</div>
      <div class="cal18__cell">25<span class="ev ev--r"></span></div>
      <div class="cal18__cell">26</div>
      <div class="cal18__cell">27</div>
      <div class="cal18__cell">28</div>
      <div class="cal18__cell">29</div>
      <div class="cal18__cell">30</div>
      <div class="cal18__cell other">1</div><div class="cal18__cell other">2</div><div class="cal18__cell other">3</div>
      <div class="cal18__cell other">4</div><div class="cal18__cell other">5</div>
    </div>

    <div class="cal18__foot">
      <div class="cal18__stat"><div class="cal18__stat-val">12</div><div class="cal18__stat-lbl">Events</div></div>
      <div class="cal18__stat"><div class="cal18__stat-val">04</div><div class="cal18__stat-lbl">Deadlines</div></div>
      <div class="cal18__stat"><div class="cal18__stat-val">07</div><div class="cal18__stat-lbl">Left</div></div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal18,
.cal18 *,
.cal18 *::before,
.cal18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal18 ::selection {
  background: #000;
  color: #ffe600;
}

.cal18 {
  --black: #000000;
  --paper: #f4f2e9;
  --yellow: #ffe600;
  --blue: #2b3fff;
  --red: #ff2e2e;
  --green: #00d97e;
  --pink: #ff6ec7;
  font-family: 'Space Mono', monospace;
  background: var(--paper);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 30px 20px;
  color: var(--black);
}

@keyframes cal18-slam {
  0% {
    transform: scale(1.15) rotate(1deg);
    opacity: 0;
  }

  100% {
    transform: scale(1) rotate(0);
    opacity: 1;
  }
}

.cal18__wrap {
  max-width: 760px;
  width: 100%;
  border: 5px solid var(--black);
  background: var(--paper);
  box-shadow: 12px 12px 0 var(--black);
  animation: cal18-slam 0.4s cubic-bezier(0.34,1.3,0.64,1) both;
}
/* ── Header ── */

.cal18__head {
  display: flex;
  align-items: stretch;
  border-bottom: 5px solid var(--black);
}

.cal18__month {
  flex: 1;
  padding: 18px 22px;
  background: var(--yellow);
  border-right: 5px solid var(--black);
}

.cal18__month-name {
  font-family: 'Archivo Black', sans-serif;
  font-size: 64px;
  line-height: 0.85;
  text-transform: uppercase;
  letter-spacing: -0.03em;
}

.cal18__month-year {
  font-family: 'Space Mono', monospace;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 0.2em;
  margin-top: 6px;
}

.cal18__nav {
  display: flex;
  flex-direction: column;
}

.cal18__nav-btn {
  flex: 1;
  width: 64px;
  background: var(--paper);
  border: none;
  border-bottom: 5px solid var(--black);
  font-family: 'Archivo Black', sans-serif;
  font-size: 24px;
  cursor: pointer;
  transition: background 0.1s;
  user-select: none;
}

.cal18__nav-btn:last-child {
  border-bottom: none;
}

.cal18__nav-btn:hover {
  background: var(--blue);
  color: var(--paper);
}
/* ── DOW ── */

.cal18__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  border-bottom: 5px solid var(--black);
}

.cal18__dw {
  padding: 8px 0;
  text-align: center;
  font-family: 'Archivo Black', sans-serif;
  font-size: 12px;
  text-transform: uppercase;
  border-right: 3px solid var(--black);
}

.cal18__dw:last-child {
  border-right: none;
}

.cal18__dw:first-child,
.cal18__dw:last-child {
  background: var(--black);
  color: var(--paper);
}
/* ── Grid ── */

.cal18__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}

.cal18__cell {
  aspect-ratio: 1;
  border-right: 3px solid var(--black);
  border-bottom: 3px solid var(--black);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Archivo Black', sans-serif;
  font-size: 28px;
  cursor: pointer;
  position: relative;
  transition: all 0.08s;
  background: var(--paper);
}

.cal18__cell:nth-child(7n) {
  border-right: none;
}

.cal18__cell:nth-last-child(-n+7) {
  border-bottom: none;
}

.cal18__cell:hover {
  background: var(--black);
  color: var(--paper);
  transform: scale(1.04);
  z-index: 2;
  box-shadow: 4px 4px 0 var(--blue);
}

.cal18__cell.other {
  color: #b8b5a8;
  pointer-events: none;
}
/* Today — yellow block, oversized */

.cal18__cell.today {
  background: var(--yellow);
  font-size: 38px;
}

.cal18__cell.today::after {
  content: 'NOW';
  position: absolute;
  top: 5px;
  right: 5px;
  font-family: 'Space Mono', monospace;
  font-size: 8px;
  font-weight: 700;
  background: var(--red);
  color: var(--paper);
  padding: 1px 4px;
}
/* Selected — blue invert */

.cal18__cell.selected {
  background: var(--blue);
  color: var(--paper);
}
/* Event corner blocks */

.cal18__cell .ev {
  position: absolute;
  bottom: 5px;
  left: 5px;
  width: 12px;
  height: 12px;
  border: 2px solid var(--black);
}

.cal18__cell.today .ev,
.cal18__cell.selected .ev {
  border-color: var(--paper);
}

.cal18__cell .ev--r {
  background: var(--red);
}

.cal18__cell .ev--g {
  background: var(--green);
}

.cal18__cell .ev--p {
  background: var(--pink);
}
/* ── Footer ── */

.cal18__foot {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  border-top: 5px solid var(--black);
}

.cal18__stat {
  padding: 16px 18px;
  border-right: 5px solid var(--black);
}

.cal18__stat:last-child {
  border-right: none;
}

.cal18__stat:nth-child(1) {
  background: var(--red);
  color: var(--paper);
}

.cal18__stat:nth-child(2) {
  background: var(--green);
}

.cal18__stat:nth-child(3) {
  background: var(--pink);
}

.cal18__stat-val {
  font-family: 'Archivo Black', sans-serif;
  font-size: 36px;
  line-height: 1;
}

.cal18__stat-lbl {
  font-family: 'Space Mono', monospace;
  font-weight: 700;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 4px;
}

@media (max-width: 560px) {
  .cal18__month-name {
    font-size: 40px;
  }

  .cal18__cell {
    font-size: 18px;
  }

  .cal18__cell.today {
    font-size: 22px;
  }

  .cal18__stat-val {
    font-size: 24px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal18 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal18Grid .cal18__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal18Grid .cal18__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
