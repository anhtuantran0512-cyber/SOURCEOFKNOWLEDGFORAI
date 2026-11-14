---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/retro-neon-cyberpunk-grid-calendar/"
title: "Retro Neon / Cyberpunk Grid Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Full synthwave: near-black canvas, animated perspective grid floor and glow sun."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Neon / Cyberpunk Grid Calendar
Source: https://codefronts.com/components/css-calendar-designs/retro-neon-cyberpunk-grid-calendar/

Full synthwave: near-black canvas, animated perspective grid floor and glow sun. Orbitron title with stacked text-shadow and a neon flicker keyframe; cells carry cyan glow borders that intensify on hover, today pulses, selection fills hot pink, glowing event dots.
## HTML
```html
<div class="cal17">
  <div class="cal17__frame">

    <div class="cal17__head">
      <div>
        <div class="cal17__title">JUNE<span>_26</span></div>
        <div class="cal17__year">// SYS.CAL.2026</div>
      </div>
      <div class="cal17__nav">
        <div class="cal17__nav-btn">‹</div>
        <div class="cal17__nav-btn">›</div>
      </div>
    </div>

    <div class="cal17__dow">
      <div class="cal17__dw">SUN</div><div class="cal17__dw">MON</div><div class="cal17__dw">TUE</div>
      <div class="cal17__dw">WED</div><div class="cal17__dw">THU</div><div class="cal17__dw">FRI</div><div class="cal17__dw">SAT</div>
    </div>

    <div class="cal17__grid" id="cal17Grid">
      <div class="cal17__cell other">25</div><div class="cal17__cell other">26</div><div class="cal17__cell other">27</div>
      <div class="cal17__cell other">28</div><div class="cal17__cell other">29</div><div class="cal17__cell other">30</div><div class="cal17__cell other">31</div>
      <div class="cal17__cell">01</div>
      <div class="cal17__cell">02<span class="ev ev--c"></span></div>
      <div class="cal17__cell">03</div>
      <div class="cal17__cell">04<span class="ev ev--y"></span></div>
      <div class="cal17__cell">05</div>
      <div class="cal17__cell">06</div>
      <div class="cal17__cell">07<span class="ev ev--p"></span></div>
      <div class="cal17__cell today selected">08</div>
      <div class="cal17__cell">09<span class="ev ev--c"></span></div>
      <div class="cal17__cell">10</div>
      <div class="cal17__cell">11<span class="ev ev--p"></span></div>
      <div class="cal17__cell">12</div>
      <div class="cal17__cell">13<span class="ev ev--y"></span></div>
      <div class="cal17__cell">14</div>
      <div class="cal17__cell">15</div>
      <div class="cal17__cell">16</div>
      <div class="cal17__cell">17<span class="ev ev--c"></span></div>
      <div class="cal17__cell">18</div>
      <div class="cal17__cell">19</div>
      <div class="cal17__cell">20<span class="ev ev--p"></span></div>
      <div class="cal17__cell">21</div>
      <div class="cal17__cell">22</div>
      <div class="cal17__cell">23<span class="ev ev--y"></span></div>
      <div class="cal17__cell">24</div>
      <div class="cal17__cell">25<span class="ev ev--c"></span></div>
      <div class="cal17__cell">26</div>
      <div class="cal17__cell">27</div>
      <div class="cal17__cell">28</div>
      <div class="cal17__cell">29</div>
      <div class="cal17__cell">30</div>
      <div class="cal17__cell other">01</div><div class="cal17__cell other">02</div><div class="cal17__cell other">03</div>
      <div class="cal17__cell other">04</div><div class="cal17__cell other">05</div>
    </div>

    <div class="cal17__foot">
      <div class="cal17__stat"><div class="cal17__stat-val">12</div><div class="cal17__stat-lbl">Events</div></div>
      <div class="cal17__stat"><div class="cal17__stat-val">07</div><div class="cal17__stat-lbl">Days_left</div></div>
      <div class="cal17__stat"><div class="cal17__stat-val">03</div><div class="cal17__stat-lbl">Priority</div></div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal17,
.cal17 *,
.cal17 *::before,
.cal17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal17 ::selection {
  background: #ff2bd6;
  color: #000;
}

.cal17 {
  --bg: #07060f;
  --bg2: #0d0a1f;
  --pink: #ff2bd6;
  --cyan: #00f0ff;
  --purple: #a64dff;
  --yellow: #f5ff3d;
  --grid: rgba(0,240,255,0.12);
  --text: #d8e8ff;
  --dim: #4a5a7a;
  font-family: 'Share Tech Mono', monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
  position: relative;
  overflow: hidden;
}
/* Perspective grid floor */

.cal17::before {
  content: '';
  position: fixed;
  bottom: 0;
  left: -50%;
  width: 200%;
  height: 60%;
  background-image: linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 50px 50px;
  transform: perspective(300px) rotateX(70deg);
  transform-origin: bottom;
  pointer-events: none;
  z-index: 0;
  animation: cal17-floor 8s linear infinite;
}

@keyframes cal17-floor {
  from {
    background-position: 0 0;
  }

  to {
    background-position: 0 50px;
  }
}
/* glow sun */

.cal17::after {
  content: '';
  position: fixed;
  top: 8%;
  left: 50%;
  transform: translateX(-50%);
  width: 380px;
  height: 380px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,43,214,0.18) 0%, rgba(166,77,255,0.08) 40%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

@keyframes cal17-flicker {
  0%,
    100% {
    opacity: 1;
  }

  41% {
    opacity: 1;
  }

  42% {
    opacity: 0.4;
  }

  43% {
    opacity: 1;
  }

  45% {
    opacity: 0.6;
  }

  46% {
    opacity: 1;
  }
}

@keyframes cal17-scan {
  0% {
    transform: translateY(0);
  }

  100% {
    transform: translateY(100%);
  }
}

@keyframes cal17-in {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.97);
  }

  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes cal17-pulse-border {
  0%,
    100% {
    box-shadow: 0 0 8px var(--cyan), inset 0 0 8px rgba(0,240,255,0.3);
  }

  50% {
    box-shadow: 0 0 18px var(--cyan), inset 0 0 14px rgba(0,240,255,0.5);
  }
}

.cal17__frame {
  position: relative;
  z-index: 1;
  max-width: 520px;
  width: 100%;
  background: rgba(13,10,31,0.85);
  backdrop-filter: blur(8px);
  border: 2px solid var(--cyan);
  border-radius: 4px;
  padding: 28px;
  box-shadow: 0 0 20px rgba(0,240,255,0.5), inset 0 0 30px rgba(0,240,255,0.08), 0 0 60px rgba(255,43,214,0.2);
  animation: cal17-in 0.6s ease both;
}
/* corner accents */

.cal17__frame::before,
.cal17__frame::after {
  content: '';
  position: absolute;
  width: 18px;
  height: 18px;
  border: 2px solid var(--pink);
}

.cal17__frame::before {
  top: -2px;
  left: -2px;
  border-right: none;
  border-bottom: none;
}

.cal17__frame::after {
  bottom: -2px;
  right: -2px;
  border-left: none;
  border-top: none;
}
/* ── Header ── */

.cal17__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(0,240,255,0.2);
}

.cal17__title {
  font-family: 'Orbitron', sans-serif;
  font-weight: 900;
  font-size: 30px;
  letter-spacing: 0.05em;
  color: var(--pink);
  text-shadow: 0 0 6px var(--pink), 0 0 14px var(--pink), 0 0 28px rgba(255,43,214,0.6);
  animation: cal17-flicker 6s infinite;
  line-height: 1;
}

.cal17__title span {
  color: var(--cyan);
  text-shadow: 0 0 6px var(--cyan), 0 0 14px var(--cyan);
}

.cal17__year {
  font-family: 'Orbitron', sans-serif;
  font-size: 13px;
  letter-spacing: 0.25em;
  color: var(--cyan);
  text-shadow: 0 0 8px var(--cyan);
  margin-top: 4px;
}

.cal17__nav {
  display: flex;
  gap: 8px;
}

.cal17__nav-btn {
  width: 40px;
  height: 40px;
  background: transparent;
  border: 1px solid var(--purple);
  color: var(--purple);
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  user-select: none;
  text-shadow: 0 0 6px var(--purple);
}

.cal17__nav-btn:hover {
  border-color: var(--cyan);
  color: var(--cyan);
  box-shadow: 0 0 14px var(--cyan), inset 0 0 8px rgba(0,240,255,0.3);
  text-shadow: 0 0 8px var(--cyan);
}
/* ── DOW ── */

.cal17__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
  margin-bottom: 5px;
}

.cal17__dw {
  text-align: center;
  font-family: 'Orbitron', sans-serif;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--cyan);
  text-shadow: 0 0 6px rgba(0,240,255,0.6);
  padding: 6px 0;
}
/* ── Grid ── */

.cal17__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
}

.cal17__cell {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Orbitron', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  cursor: pointer;
  border: 1px solid rgba(0,240,255,0.15);
  background: rgba(0,240,255,0.02);
  position: relative;
  transition: all 0.18s;
}

.cal17__cell:hover {
  border-color: var(--cyan);
  color: var(--cyan);
  box-shadow: 0 0 12px rgba(0,240,255,0.6), inset 0 0 8px rgba(0,240,255,0.2);
  text-shadow: 0 0 8px var(--cyan);
}

.cal17__cell.other {
  color: var(--dim);
  border-color: rgba(74,90,122,0.15);
  pointer-events: none;
  opacity: 0.4;
}
/* Today — neon cyan box */

.cal17__cell.today {
  border-color: var(--cyan);
  color: var(--cyan);
  text-shadow: 0 0 10px var(--cyan);
  animation: cal17-pulse-border 2s ease-in-out infinite;
}
/* Selected — hot pink fill */

.cal17__cell.selected {
  border-color: var(--pink);
  background: rgba(255,43,214,0.12);
  color: var(--pink);
  text-shadow: 0 0 10px var(--pink);
  box-shadow: 0 0 16px rgba(255,43,214,0.7), inset 0 0 10px rgba(255,43,214,0.3);
}
/* event marker */

.cal17__cell .ev {
  position: absolute;
  bottom: 4px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
}

.cal17__cell .ev--p {
  background: var(--pink);
  box-shadow: 0 0 6px var(--pink);
}

.cal17__cell .ev--y {
  background: var(--yellow);
  box-shadow: 0 0 6px var(--yellow);
}

.cal17__cell .ev--c {
  background: var(--cyan);
  box-shadow: 0 0 6px var(--cyan);
}
/* ── Footer readout ── */

.cal17__foot {
  margin-top: 22px;
  padding-top: 16px;
  border-top: 1px solid rgba(0,240,255,0.2);
  display: flex;
  gap: 10px;
}

.cal17__stat {
  flex: 1;
  border: 1px solid rgba(166,77,255,0.4);
  padding: 10px 12px;
  background: rgba(166,77,255,0.05);
}

.cal17__stat-val {
  font-family: 'Orbitron', sans-serif;
  font-weight: 900;
  font-size: 22px;
  color: var(--purple);
  text-shadow: 0 0 8px var(--purple);
  line-height: 1;
}

.cal17__stat-lbl {
  font-size: 9px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--dim);
  margin-top: 4px;
}

.cal17__stat:nth-child(1) .cal17__stat-val {
  color: var(--cyan);
  text-shadow: 0 0 8px var(--cyan);
}

.cal17__stat:nth-child(3) .cal17__stat-val {
  color: var(--pink);
  text-shadow: 0 0 8px var(--pink);
}

@media (max-width: 480px) {
  .cal17__title {
    font-size: 22px;
  }

  .cal17__cell {
    font-size: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal17 *,
    .cal17::before {
    animation: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal17Grid .cal17__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal17Grid .cal17__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
