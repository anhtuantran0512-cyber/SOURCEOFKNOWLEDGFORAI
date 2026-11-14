---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/micro-interactions-liquid-bubble-date-hover/"
title: "Micro-Interactions & Liquid Bubble Date Hover"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A plain-looking grid whose magic is the hover."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Micro-Interactions & Liquid Bubble Date Hover
Source: https://codefronts.com/components/css-calendar-designs/micro-interactions-liquid-bubble-date-hover/

A plain-looking grid whose magic is the hover. A goo layer with filter:blur+contrast and screen blending fuses circles into a liquid metaball; each cell's hidden blob springs to scale under the cursor and melts away. Today wobbles a morphing gradient blob.
## HTML
```html
<div class="cal22">
  <div class="cal22__card">

    <div class="cal22__head">
      <div>
        <div class="cal22__title">June <span>2026</span></div>
        <div class="cal22__hint">// hover the dates — liquid goo</div>
      </div>
      <div class="cal22__nav">
        <div class="cal22__nav-btn">‹</div>
        <div class="cal22__nav-btn">›</div>
      </div>
    </div>

    <div class="cal22__dow">
      <div class="cal22__dw">S</div><div class="cal22__dw">M</div><div class="cal22__dw">T</div>
      <div class="cal22__dw">W</div><div class="cal22__dw">T</div><div class="cal22__dw">F</div><div class="cal22__dw">S</div>
    </div>

    <div class="cal22__gridwrap">
      <div class="cal22__goo" id="cal22Goo"></div>
      <div class="cal22__grid" id="cal22Grid">
        <div class="cal22__cell other">25</div><div class="cal22__cell other">26</div><div class="cal22__cell other">27</div>
        <div class="cal22__cell other">28</div><div class="cal22__cell other">29</div><div class="cal22__cell other">30</div><div class="cal22__cell other">31</div>
        <div class="cal22__cell">1</div>
        <div class="cal22__cell">2<span class="ev"></span></div>
        <div class="cal22__cell">3</div>
        <div class="cal22__cell">4<span class="ev"></span></div>
        <div class="cal22__cell">5</div>
        <div class="cal22__cell">6</div>
        <div class="cal22__cell">7<span class="ev"></span></div>
        <div class="cal22__cell today">8</div>
        <div class="cal22__cell">9<span class="ev"></span></div>
        <div class="cal22__cell">10</div>
        <div class="cal22__cell">11<span class="ev"></span></div>
        <div class="cal22__cell">12</div>
        <div class="cal22__cell">13<span class="ev"></span></div>
        <div class="cal22__cell">14</div>
        <div class="cal22__cell">15</div>
        <div class="cal22__cell">16</div>
        <div class="cal22__cell">17<span class="ev"></span></div>
        <div class="cal22__cell">18</div>
        <div class="cal22__cell">19</div>
        <div class="cal22__cell">20<span class="ev"></span></div>
        <div class="cal22__cell">21</div>
        <div class="cal22__cell">22</div>
        <div class="cal22__cell">23</div>
        <div class="cal22__cell">24<span class="ev"></span></div>
        <div class="cal22__cell">25</div>
        <div class="cal22__cell">26</div>
        <div class="cal22__cell">27<span class="ev"></span></div>
        <div class="cal22__cell">28</div>
        <div class="cal22__cell">29</div>
        <div class="cal22__cell">30</div>
        <div class="cal22__cell other">1</div><div class="cal22__cell other">2</div><div class="cal22__cell other">3</div>
        <div class="cal22__cell other">4</div><div class="cal22__cell other">5</div>
      </div>
    </div>

    <div class="cal22__foot">
      <div class="cal22__foot-blob"></div>
      <div class="cal22__foot-body">
        <div class="cal22__foot-title">Sunday, June 8</div>
        <div class="cal22__foot-sub">3 events · sprint, launch, review</div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal22,
.cal22 *,
.cal22 *::before,
.cal22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal22 ::selection {
  background: #ff5470;
  color: #fff;
}

.cal22 {
  --bg: #0f0e17;
  --surface: #16151f;
  --text: #fffffe;
  --text2: #a7a9be;
  --text3: #5a5b70;
  --blob: #ff5470;
  --blob2: #ff8906;
  --accent: #e53170;
  --soft: #2e2f3e;
  font-family: 'Bricolage Grotesque', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
}

@keyframes cal22-in {
  from {
    opacity: 0;
    transform: translateY(16px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes cal22-wobble {
  0%,
    100% {
    border-radius: 42% 58% 56% 44% / 48% 50% 50% 52%;
  }

  50% {
    border-radius: 56% 44% 48% 52% / 56% 44% 56% 44%;
  }
}

.cal22__card {
  max-width: 460px;
  width: 100%;
  background: var(--surface);
  border-radius: 28px;
  padding: 32px;
  box-shadow: 0 30px 70px rgba(0,0,0,0.5);
  animation: cal22-in 0.5s ease both;
  position: relative;
}
/* ── Header ── */

.cal22__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.cal22__title {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.cal22__title span {
  background: linear-gradient(135deg, var(--blob), var(--blob2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cal22__hint {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  color: var(--text3);
  margin-top: 3px;
}

.cal22__nav {
  display: flex;
  gap: 8px;
}

.cal22__nav-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--soft);
  border: none;
  color: var(--text2);
  font-size: 16px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
}

.cal22__nav-btn:hover {
  background: var(--blob);
  color: #fff;
}
/* ── DOW ── */

.cal22__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 8px;
}

.cal22__dw {
  text-align: center;
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  font-weight: 500;
  color: var(--text3);
  padding: 4px 0;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   GOOEY LIQUID LAYER — the core trick.
   A blurred + high-contrast filter on the
   blob container fuses overlapping circles
   into a single liquid mass (metaball effect).
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal22__gridwrap {
  position: relative;
}
/* Goo layer sits behind the numbers */

.cal22__goo {
  position: absolute;
  inset: 0;
  filter: blur(8px) contrast(22);
  pointer-events: none;
  z-index: 1;
  mix-blend-mode: screen;
}
/* Each blob is a small circle that grows + wobbles on its cell's hover */

.cal22__blob {
  position: absolute;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--blob);
  transform: translate(-50%, -50%) scale(0);
  transition: transform 0.35s cubic-bezier(0.34,1.56,0.64,1);
  will-change: transform;
}

.cal22__grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 2px;
}

.cal22__cell {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
  cursor: pointer;
  position: relative;
  border-radius: 50%;
  transition: color 0.2s;
}

.cal22__cell:hover {
  color: #fff;
}

.cal22__cell.other {
  color: var(--text3);
  opacity: 0.4;
  pointer-events: none;
}
/* Today — persistent gradient blob underneath via box-shadow ring */

.cal22__cell.today {
  color: #fff;
  font-weight: 800;
}

.cal22__cell.today::after {
  content: '';
  position: absolute;
  inset: 6px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--blob), var(--blob2));
  z-index: -1;
  animation: cal22-wobble 4s ease-in-out infinite;
}

.cal22__cell.selected {
  color: #fff;
  font-weight: 800;
}

.cal22__cell.selected::before {
  content: '';
  position: absolute;
  inset: 5px;
  border-radius: 50%;
  border: 2px solid var(--blob2);
  z-index: -1;
}
/* event dot */

.cal22__cell .ev {
  position: absolute;
  bottom: 8px;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--blob2);
}

.cal22__cell.today .ev,
.cal22__cell:hover .ev {
  background: #fff;
}
/* ── Footer readout ── */

.cal22__foot {
  margin-top: 26px;
  padding: 16px 18px;
  border-radius: 18px;
  background: var(--bg);
  display: flex;
  align-items: center;
  gap: 14px;
}

.cal22__foot-blob {
  width: 44px;
  height: 44px;
  border-radius: 42% 58% 56% 44% / 48% 50% 50% 52%;
  background: linear-gradient(135deg, var(--blob), var(--blob2));
  flex-shrink: 0;
  animation: cal22-wobble 4s ease-in-out infinite;
}

.cal22__foot-body {
}

.cal22__foot-title {
  font-size: 14px;
  font-weight: 600;
}

.cal22__foot-sub {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  color: var(--text3);
  margin-top: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cal22 * {
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const grid = document.getElementById('cal22Grid');
  const goo  = document.getElementById('cal22Goo');
  const cells = grid.querySelectorAll('.cal22__cell:not(.other)');

  // create one blob per real cell, track to its position
  cells.forEach(cell => {
    const blob = document.createElement('div');
    blob.className = 'cal22__blob';
    goo.appendChild(blob);

    function place() {
      const gr = grid.getBoundingClientRect();
      const cr = cell.getBoundingClientRect();
      blob.style.left = (cr.left - gr.left + cr.width/2) + 'px';
      blob.style.top  = (cr.top  - gr.top  + cr.height/2) + 'px';
    }
    cell.addEventListener('mouseenter', () => { place(); blob.style.transform = 'translate(-50%,-50%) scale(1.15)'; });
    cell.addEventListener('mouseleave', () => { blob.style.transform = 'translate(-50%,-50%) scale(0)'; });
    cell.addEventListener('click', function() {
      cells.forEach(c => c.classList.remove('selected'));
      this.classList.add('selected');
    });
  });
})();
```
