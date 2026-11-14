---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/diagonal-slanted-grid-calendar/"
title: "Diagonal Slanted Grid Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Aggressive sports/gaming energy: a clip-path banner, week rows skewed with skewX and numbers counter-skewed to stay upright."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Slanted Grid Calendar
Source: https://codefronts.com/components/css-calendar-designs/diagonal-slanted-grid-calendar/

Aggressive sports/gaming energy: a clip-path banner, week rows skewed with skewX and numbers counter-skewed to stay upright. Today is a red diagonal-split block with a corner flag, event days get skew-corrected underline bars, and footer stat panels match the slant.
## HTML
```html
<div class="cal27">
  <div class="cal27__wrap">

    <div class="cal27__head">
      <div class="cal27__title">June · 2026</div>
      <div class="cal27__nav">
        <button class="cal27__nav-btn">‹</button>
        <button class="cal27__nav-btn">›</button>
      </div>
    </div>

    <div class="cal27__dow">
      <div class="cal27__dw">Sun</div><div class="cal27__dw">Mon</div><div class="cal27__dw">Tue</div>
      <div class="cal27__dw">Wed</div><div class="cal27__dw">Thu</div><div class="cal27__dw">Fri</div><div class="cal27__dw">Sat</div>
    </div>

    <div class="cal27__grid" id="cal27Grid">
      <div class="cal27__row">
        <div class="cal27__cell other"><span class="cal27__n">25</span></div>
        <div class="cal27__cell other"><span class="cal27__n">26</span></div>
        <div class="cal27__cell other"><span class="cal27__n">27</span></div>
        <div class="cal27__cell other"><span class="cal27__n">28</span></div>
        <div class="cal27__cell other"><span class="cal27__n">29</span></div>
        <div class="cal27__cell other"><span class="cal27__n">30</span></div>
        <div class="cal27__cell other"><span class="cal27__n">31</span></div>
      </div>
      <div class="cal27__row">
        <div class="cal27__cell"><span class="cal27__n">1</span></div>
        <div class="cal27__cell ev ev--lime"><span class="cal27__n">2</span></div>
        <div class="cal27__cell"><span class="cal27__n">3</span></div>
        <div class="cal27__cell ev ev--amber"><span class="cal27__n">4</span></div>
        <div class="cal27__cell"><span class="cal27__n">5</span></div>
        <div class="cal27__cell"><span class="cal27__n">6</span></div>
        <div class="cal27__cell ev ev--cyan"><span class="cal27__n">7</span></div>
      </div>
      <div class="cal27__row">
        <div class="cal27__cell today"><span class="cal27__n">8</span></div>
        <div class="cal27__cell ev ev--lime"><span class="cal27__n">9</span></div>
        <div class="cal27__cell"><span class="cal27__n">10</span></div>
        <div class="cal27__cell ev ev--cyan"><span class="cal27__n">11</span></div>
        <div class="cal27__cell"><span class="cal27__n">12</span></div>
        <div class="cal27__cell ev ev--amber"><span class="cal27__n">13</span></div>
        <div class="cal27__cell"><span class="cal27__n">14</span></div>
      </div>
      <div class="cal27__row">
        <div class="cal27__cell"><span class="cal27__n">15</span></div>
        <div class="cal27__cell"><span class="cal27__n">16</span></div>
        <div class="cal27__cell ev ev--lime"><span class="cal27__n">17</span></div>
        <div class="cal27__cell"><span class="cal27__n">18</span></div>
        <div class="cal27__cell"><span class="cal27__n">19</span></div>
        <div class="cal27__cell ev ev--cyan"><span class="cal27__n">20</span></div>
        <div class="cal27__cell"><span class="cal27__n">21</span></div>
      </div>
      <div class="cal27__row">
        <div class="cal27__cell"><span class="cal27__n">22</span></div>
        <div class="cal27__cell"><span class="cal27__n">23</span></div>
        <div class="cal27__cell ev ev--amber"><span class="cal27__n">24</span></div>
        <div class="cal27__cell"><span class="cal27__n">25</span></div>
        <div class="cal27__cell"><span class="cal27__n">26</span></div>
        <div class="cal27__cell ev ev--lime"><span class="cal27__n">27</span></div>
        <div class="cal27__cell"><span class="cal27__n">28</span></div>
      </div>
      <div class="cal27__row">
        <div class="cal27__cell"><span class="cal27__n">29</span></div>
        <div class="cal27__cell"><span class="cal27__n">30</span></div>
        <div class="cal27__cell other"><span class="cal27__n">1</span></div>
        <div class="cal27__cell other"><span class="cal27__n">2</span></div>
        <div class="cal27__cell other"><span class="cal27__n">3</span></div>
        <div class="cal27__cell other"><span class="cal27__n">4</span></div>
        <div class="cal27__cell other"><span class="cal27__n">5</span></div>
      </div>
    </div>

    <div class="cal27__foot">
      <div class="cal27__stat"><div class="cal27__stat-inner"><div class="cal27__stat-val">12</div><div class="cal27__stat-lbl">Events</div></div></div>
      <div class="cal27__stat"><div class="cal27__stat-inner"><div class="cal27__stat-val">08</div><div class="cal27__stat-lbl">Sessions</div></div></div>
      <div class="cal27__stat"><div class="cal27__stat-inner"><div class="cal27__stat-val">07</div><div class="cal27__stat-lbl">Days left</div></div></div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal27,
.cal27 *,
.cal27 *::before,
.cal27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal27 ::selection {
  background: #ff3b30;
  color: #fff;
}

.cal27 {
  --bg: #101216;
  --bg2: #16191f;
  --panel: #1d2129;
  --panel2: #252a34;
  --text: #f2f4f8;
  --text2: #8a92a6;
  --text3: #4a5160;
  --red: #ff3b30;
  --lime: #c6ff00;
  --cyan: #00e0ff;
  --amber: #ffb300;
  font-family: 'Saira', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
  overflow: hidden;
}
/* diagonal stripe background */

.cal27::before {
  content: '';
  position: fixed;
  inset: -20%;
  background: repeating-linear-gradient(
      -22deg,
      transparent 0, transparent 60px,
      rgba(255,255,255,0.015) 60px, rgba(255,255,255,0.015) 61px
    );
  pointer-events: none;
}

@keyframes cal27-in {
  from {
    opacity: 0;
    transform: translateX(-30px) skewX(-3deg);
  }

  to {
    opacity: 1;
    transform: translateX(0) skewX(0);
  }
}

@keyframes cal27-flash {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.6;
  }
}

.cal27__wrap {
  position: relative;
  z-index: 1;
  max-width: 720px;
  width: 100%;
  animation: cal27-in 0.5s cubic-bezier(0.22,1,0.36,1) both;
}
/* ── Header — slanted banner ── */

.cal27__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--red);
  padding: 14px 28px;
  clip-path: polygon(0 0, 100% 0, calc(100% - 22px) 100%, 0 100%);
  margin-bottom: 4px;
}

.cal27__title {
  font-family: 'Saira Condensed', sans-serif;
  font-weight: 900;
  font-size: 36px;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  font-style: italic;
  line-height: 1;
  color: #fff;
}

.cal27__nav {
  display: flex;
  gap: 6px;
}

.cal27__nav-btn {
  width: 38px;
  height: 38px;
  background: rgba(0,0,0,0.25);
  border: none;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%);
  transition: background 0.15s;
  user-select: none;
}

.cal27__nav-btn:hover {
  background: rgba(0,0,0,0.5);
}
/* DOW slanted strip */

.cal27__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  background: var(--panel2);
  clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
  margin-bottom: 8px;
}

.cal27__dw {
  text-align: center;
  font-family: 'Saira Condensed', sans-serif;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text2);
  padding: 8px 0;
  transform: skewX(-12deg);
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SLANTED GRID — each row is skewed,
   numbers counter-skewed to stay upright.
   Diagonal cut via clip-path + skewX.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal27__grid {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.cal27__row {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 6px;
  transform: skewX(-12deg);
}

.cal27__cell {
  aspect-ratio: 1.15;
  background: var(--panel);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  transition: all 0.18s;
  overflow: hidden;
  border-left: 3px solid transparent;
}

.cal27__cell:hover {
  background: var(--panel2);
  border-left-color: var(--lime);
}

.cal27__cell.other {
  background: var(--bg2);
  pointer-events: none;
}
/* counter-skew the contents so numbers read upright */

.cal27__n {
  font-family: 'Saira Condensed', sans-serif;
  font-weight: 700;
  font-size: 22px;
  color: var(--text);
  transform: skewX(12deg);
  line-height: 1;
}

.cal27__cell.other .cal27__n {
  color: var(--text3);
}
/* today — red slash block */

.cal27__cell.today {
  background: linear-gradient(110deg, var(--red) 60%, #d62d23 60%);
  border-left-color: var(--lime);
}

.cal27__cell.today .cal27__n {
  color: #fff;
  font-weight: 900;
  font-size: 26px;
}

.cal27__cell.today::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  border-style: solid;
  border-width: 0 14px 14px 0;
  border-color: transparent var(--lime) transparent transparent;
  transform: skewX(12deg);
}
/* selected */

.cal27__cell.selected {
  background: var(--panel2);
  border-left-color: var(--cyan);
}

.cal27__cell.selected .cal27__n {
  color: var(--cyan);
  font-weight: 900;
}
/* event flag — colored corner triangle */

.cal27__cell.ev::before {
  content: '';
  position: absolute;
  bottom: 5px;
  left: 8px;
  width: 16px;
  height: 3px;
  transform: skewX(12deg);
}

.cal27__cell.ev--lime::before {
  background: var(--lime);
}

.cal27__cell.ev--cyan::before {
  background: var(--cyan);
}

.cal27__cell.ev--amber::before {
  background: #ffb300;
}
/* ── Footer slanted stats ── */

.cal27__foot {
  display: flex;
  gap: 6px;
  margin-top: 10px;
}

.cal27__stat {
  flex: 1;
  background: var(--panel);
  padding: 12px 18px;
  transform: skewX(-12deg);
}

.cal27__stat-inner {
  transform: skewX(12deg);
}

.cal27__stat-val {
  font-family: 'Saira Condensed', sans-serif;
  font-weight: 900;
  font-size: 28px;
  line-height: 1;
  font-style: italic;
}

.cal27__stat-lbl {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--text2);
  margin-top: 3px;
}

.cal27__stat:nth-child(1) .cal27__stat-val {
  color: var(--red);
}

.cal27__stat:nth-child(2) .cal27__stat-val {
  color: var(--lime);
}

.cal27__stat:nth-child(3) .cal27__stat-val {
  color: var(--cyan);
}

@media (max-width: 560px) {
  .cal27__title {
    font-size: 26px;
  }

  .cal27__n {
    font-size: 17px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal27 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal27Grid .cal27__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal27Grid .cal27__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
