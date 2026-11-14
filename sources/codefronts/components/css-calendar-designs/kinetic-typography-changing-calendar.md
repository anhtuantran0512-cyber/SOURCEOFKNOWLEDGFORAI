---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/kinetic-typography-changing-calendar/"
title: "Kinetic Typography Changing Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Hyper-minimal where the numbers are the layout, built on the Roboto Flex variable font."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Kinetic Typography Changing Calendar
Source: https://codefronts.com/components/css-calendar-designs/kinetic-typography-changing-calendar/

Hyper-minimal where the numbers are the layout, built on the Roboto Flex variable font. Cursor distance drives a decaying wave of font-variation-settings (weight, width and scale) so digits swell outward and settle on leave. Today stays heavy in accent lime.
## HTML
```html
<div class="cal26">
  <div class="cal26__wrap">

    <div class="cal26__head">
      <div class="cal26__title">JUNE<br><em>2026</em></div>
      <div class="cal26__hint">Hover across a row — the weights ripple like a wave</div>
    </div>

    <div class="cal26__dow">
      <div class="cal26__dw">Su</div><div class="cal26__dw">Mo</div><div class="cal26__dw">Tu</div>
      <div class="cal26__dw">We</div><div class="cal26__dw">Th</div><div class="cal26__dw">Fr</div><div class="cal26__dw">Sa</div>
    </div>

    <div class="cal26__grid" id="cal26Grid">
      <div class="cal26__cell other"><span class="cal26__n">25</span></div>
      <div class="cal26__cell other"><span class="cal26__n">26</span></div>
      <div class="cal26__cell other"><span class="cal26__n">27</span></div>
      <div class="cal26__cell other"><span class="cal26__n">28</span></div>
      <div class="cal26__cell other"><span class="cal26__n">29</span></div>
      <div class="cal26__cell other"><span class="cal26__n">30</span></div>
      <div class="cal26__cell other"><span class="cal26__n">31</span></div>
      <div class="cal26__cell"><span class="cal26__n">1</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">2</span></div>
      <div class="cal26__cell"><span class="cal26__n">3</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">4</span></div>
      <div class="cal26__cell"><span class="cal26__n">5</span></div>
      <div class="cal26__cell"><span class="cal26__n">6</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">7</span></div>
      <div class="cal26__cell today has-ev"><span class="cal26__n">8</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">9</span></div>
      <div class="cal26__cell"><span class="cal26__n">10</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">11</span></div>
      <div class="cal26__cell"><span class="cal26__n">12</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">13</span></div>
      <div class="cal26__cell"><span class="cal26__n">14</span></div>
      <div class="cal26__cell"><span class="cal26__n">15</span></div>
      <div class="cal26__cell"><span class="cal26__n">16</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">17</span></div>
      <div class="cal26__cell"><span class="cal26__n">18</span></div>
      <div class="cal26__cell"><span class="cal26__n">19</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">20</span></div>
      <div class="cal26__cell"><span class="cal26__n">21</span></div>
      <div class="cal26__cell"><span class="cal26__n">22</span></div>
      <div class="cal26__cell"><span class="cal26__n">23</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">24</span></div>
      <div class="cal26__cell"><span class="cal26__n">25</span></div>
      <div class="cal26__cell"><span class="cal26__n">26</span></div>
      <div class="cal26__cell has-ev"><span class="cal26__n">27</span></div>
      <div class="cal26__cell"><span class="cal26__n">28</span></div>
      <div class="cal26__cell"><span class="cal26__n">29</span></div>
      <div class="cal26__cell"><span class="cal26__n">30</span></div>
      <div class="cal26__cell other"><span class="cal26__n">1</span></div>
      <div class="cal26__cell other"><span class="cal26__n">2</span></div>
      <div class="cal26__cell other"><span class="cal26__n">3</span></div>
      <div class="cal26__cell other"><span class="cal26__n">4</span></div>
      <div class="cal26__cell other"><span class="cal26__n">5</span></div>
    </div>

    <div class="cal26__foot">
      <div class="cal26__foot-date">Sunday <em>08</em></div>
      <div class="cal26__foot-meta">3 EVENTS · WEIGHT-WAVE INTERACTION</div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal26,
.cal26 *,
.cal26 *::before,
.cal26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal26 ::selection {
  background: #e8ff3d;
  color: #000;
}

.cal26 {
  --bg: #0c0c0c;
  --text: #f5f5f5;
  --text2: #6a6a6a;
  --text3: #333333;
  --accent: #e8ff3d;
  font-family: 'Roboto Flex', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
}

@keyframes cal26-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.cal26__wrap {
  max-width: 760px;
  width: 100%;
  animation: cal26-in 0.6s ease both;
}
/* ── Header ── */

.cal26__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 40px;
  border-bottom: 1px solid var(--text3);
  padding-bottom: 18px;
}

.cal26__title {
  font-variation-settings: 'wght' 800, 'opsz' 100;
  font-size: 44px;
  line-height: 0.9;
  letter-spacing: -0.02em;
}

.cal26__title em {
  font-style: normal;
  color: var(--accent);
}

.cal26__hint {
  font-variation-settings: 'wght' 400;
  font-size: 12px;
  color: var(--text2);
  letter-spacing: 0.06em;
  text-align: right;
  max-width: 180px;
}
/* DOW */

.cal26__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 18px;
}

.cal26__dw {
  text-align: center;
  font-variation-settings: 'wght' 500;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text2);
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   KINETIC TYPE GRID — numbers ARE the
   layout. Hover drives a weight/width/
   scale wave via variable-font settings;
   neighbours respond at decaying strength
   through JS-set CSS custom properties.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal26__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 0;
}

.cal26__cell {
  aspect-ratio: 1.1;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
}

.cal26__n {
  --w: 200;
  /* weight */
  --wd: 100;
  /* width  */
  --s: 1;
  /* scale  */
  font-variation-settings: 'wght' var(--w), 'wdth' var(--wd), 'opsz' 144;
  font-size: 34px;
  color: var(--text);
  line-height: 1;
  transform: scale(var(--s));
  transition: font-variation-settings 0.35s cubic-bezier(0.22,1,0.36,1), transform 0.35s cubic-bezier(0.22,1,0.36,1), color 0.35s;
  will-change: font-variation-settings, transform;
}

.cal26__cell.other .cal26__n {
  color: var(--text3);
}

.cal26__cell.other {
  pointer-events: none;
}
/* today: persistent heavy + accent */

.cal26__cell.today .cal26__n {
  --w: 900;
  --wd: 130;
  color: var(--accent);
}
/* selected */

.cal26__cell.selected .cal26__n {
  --w: 800;
  color: var(--accent);
}

.cal26__cell.selected::after {
  content: '';
  position: absolute;
  bottom: 18%;
  width: 26px;
  height: 3px;
  background: var(--accent);
  border-radius: 2px;
}
/* event underline tick */

.cal26__cell.has-ev::before {
  content: '';
  position: absolute;
  bottom: 22%;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--text2);
  transition: background 0.3s;
}

.cal26__cell:hover.has-ev::before,
.cal26__cell.today.has-ev::before {
  background: var(--accent);
}
/* ── Footer readout ── */

.cal26__foot {
  margin-top: 36px;
  border-top: 1px solid var(--text3);
  padding-top: 20px;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}

.cal26__foot-date {
  font-variation-settings: 'wght' 700, 'wdth' 120;
  font-size: 26px;
}

.cal26__foot-date em {
  font-style: normal;
  color: var(--accent);
}

.cal26__foot-meta {
  font-variation-settings: 'wght' 400;
  font-size: 12px;
  color: var(--text2);
  letter-spacing: 0.08em;
}

@media (max-width: 560px) {
  .cal26__title {
    font-size: 30px;
  }

  .cal26__n {
    font-size: 24px;
  }

  .cal26__hint {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal26 *,
    .cal26__n {
    animation: none !important;
    transition: color 0.2s !important;
  }
}
```

## JavaScript
```js
(() => {
  const grid = document.getElementById('cal26Grid');
  const cells = Array.from(grid.querySelectorAll('.cal26__cell'));

  // map each real cell to its grid index for distance-based falloff
  cells.forEach((cell, i) => {
    if (cell.classList.contains('other')) return;
    cell.addEventListener('mousemove', () => {
      const col = i % 7, row = Math.floor(i / 7);
      cells.forEach((c, j) => {
        if (c.classList.contains('other') || c.classList.contains('today')) return;
        const cc = j % 7, cr = Math.floor(j / 7);
        const dist = Math.hypot(cc - col, cr - row);
        const n = c.querySelector('.cal26__n');
        // wave: closer = heavier/wider/bigger
        const f = Math.max(0, 1 - dist / 2.6);
        const w  = 200 + f * 700;       // 200 → 900
        const wd = 100 + f * 50;        // 100 → 150
        const s  = 1 + f * 0.35;        // 1 → 1.35
        n.style.setProperty('--w', w.toFixed(0));
        n.style.setProperty('--wd', wd.toFixed(0));
        n.style.setProperty('--s', s.toFixed(3));
      });
    });
  });

  grid.addEventListener('mouseleave', () => {
    cells.forEach(c => {
      if (c.classList.contains('today')) return;
      const n = c.querySelector('.cal26__n');
      n.style.setProperty('--w', '200');
      n.style.setProperty('--wd', '100');
      n.style.setProperty('--s', '1');
    });
  });

  cells.forEach(cell => {
    if (cell.classList.contains('other')) return;
    cell.addEventListener('click', function() {
      cells.forEach(c => c.classList.remove('selected'));
      this.classList.add('selected');
    });
  });
})();
```
