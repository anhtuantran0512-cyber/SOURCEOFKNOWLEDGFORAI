---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/infinite-isometric-dashboard-calendar-view/"
title: "Infinite Isometric Dashboard Calendar View"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "The grid tilts into an architectural floating plane via rotateX/rotateZ with a float loop."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinite Isometric Dashboard Calendar View
Source: https://codefronts.com/components/css-calendar-designs/infinite-isometric-dashboard-calendar-view/

The grid tilts into an architectural floating plane via rotateX/rotateZ with a float loop. Each date is an extruded 3D block with pseudo-element sides; numbers are counter-rotated to stay upright and legible. Today is a tall bobbing tower, with a floating HUD and legend.
## HTML
```html
<div class="cal20">
  <div class="cal20__dash">

    <!-- HUD -->
    <div class="cal20__hud">
      <div>
        <div class="cal20__hud-title">June <span>2026</span></div>
        <div class="cal20__hud-sub">// isometric.view · q2.dashboard</div>
      </div>
      <div class="cal20__hud-stats">
        <div class="cal20__hud-stat"><div class="cal20__hud-stat-v">12</div><div class="cal20__hud-stat-l">Events</div></div>
        <div class="cal20__hud-stat"><div class="cal20__hud-stat-v">8</div><div class="cal20__hud-stat-l">Done</div></div>
        <div class="cal20__hud-stat"><div class="cal20__hud-stat-v">4</div><div class="cal20__hud-stat-l">Due</div></div>
      </div>
    </div>

    <!-- Isometric plane -->
    <div class="cal20__stage">
      <div class="cal20__plane">
        <div class="cal20__plane-label">▦ JUNE.GRID</div>
        <div class="cal20__grid" id="cal20Grid">
          <div class="cal20__tile other">25</div><div class="cal20__tile other">26</div><div class="cal20__tile other">27</div>
          <div class="cal20__tile other">28</div><div class="cal20__tile other">29</div><div class="cal20__tile other">30</div><div class="cal20__tile other">31</div>
          <div class="cal20__tile">1</div>
          <div class="cal20__tile ev ev--teal">2<span class="marker"></span></div>
          <div class="cal20__tile">3</div>
          <div class="cal20__tile ev ev--amber">4<span class="marker"></span></div>
          <div class="cal20__tile">5</div>
          <div class="cal20__tile">6</div>
          <div class="cal20__tile ev ev--pink">7<span class="marker"></span></div>
          <div class="cal20__tile today">8</div>
          <div class="cal20__tile ev ev--teal">9<span class="marker"></span></div>
          <div class="cal20__tile">10</div>
          <div class="cal20__tile ev ev--pink">11<span class="marker"></span></div>
          <div class="cal20__tile">12</div>
          <div class="cal20__tile ev ev--amber">13<span class="marker"></span></div>
          <div class="cal20__tile">14</div>
          <div class="cal20__tile">15</div>
          <div class="cal20__tile">16</div>
          <div class="cal20__tile ev ev--teal">17<span class="marker"></span></div>
          <div class="cal20__tile">18</div>
          <div class="cal20__tile">19</div>
          <div class="cal20__tile ev ev--pink">20<span class="marker"></span></div>
          <div class="cal20__tile">21</div>
          <div class="cal20__tile">22</div>
          <div class="cal20__tile">23</div>
          <div class="cal20__tile ev ev--amber">24<span class="marker"></span></div>
          <div class="cal20__tile">25</div>
          <div class="cal20__tile">26</div>
          <div class="cal20__tile ev ev--teal">27<span class="marker"></span></div>
          <div class="cal20__tile">28</div>
          <div class="cal20__tile">29</div>
          <div class="cal20__tile">30</div>
          <div class="cal20__tile other">1</div><div class="cal20__tile other">2</div><div class="cal20__tile other">3</div>
          <div class="cal20__tile other">4</div><div class="cal20__tile other">5</div>
        </div>
      </div>
    </div>

    <!-- Legend -->
    <div class="cal20__legend">
      <div class="cal20__leg"><span class="cal20__leg-block" style="background:var(--blue)"></span>Today (tower)</div>
      <div class="cal20__leg"><span class="cal20__leg-block" style="background:var(--pink)"></span>Selected</div>
      <div class="cal20__leg"><span class="cal20__leg-block" style="background:var(--teal)"></span>Has event</div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal20,
.cal20 *,
.cal20 *::before,
.cal20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal20 ::selection {
  background: #5e72e4;
  color: #fff;
}

.cal20 {
  --bg1: #161a2e;
  --bg2: #1e2440;
  --tile: #2a3157;
  --tile-l: #343d6b;
  --tile-top: #3a4378;
  --border: rgba(255,255,255,0.1);
  --text: #eef1ff;
  --text2: #9aa3d4;
  --text3: #5a6394;
  --blue: #5e72e4;
  --blue-l: #8a9bff;
  --pink: #f56991;
  --teal: #2dd4bf;
  --amber: #fbbf24;
  font-family: 'Outfit', sans-serif;
  background: radial-gradient(ellipse at top, var(--bg2), var(--bg1) 80%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
  overflow: hidden;
}

@keyframes cal20-in {
  from {
    opacity: 0;
    transform: translateY(40px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes cal20-float {
  0%,
    100% {
    transform: rotateX(58deg) rotateZ(-45deg) translateZ(0);
  }

  50% {
    transform: rotateX(58deg) rotateZ(-45deg) translateZ(14px);
  }
}

@keyframes cal20-bob {
  0%,
    100% {
    transform: translateZ(40px);
  }

  50% {
    transform: translateZ(58px);
  }
}

.cal20__dash {
  display: grid;
  grid-template-columns: 1fr;
  gap: 28px;
  max-width: 720px;
  width: 100%;
  animation: cal20-in 0.7s cubic-bezier(0.22,1,0.36,1) both;
}
/* ── HUD header (flat, on top) ── */

.cal20__hud {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(42,49,87,0.5);
  backdrop-filter: blur(10px);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 16px 22px;
  position: relative;
  z-index: 10;
}

.cal20__hud-title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.01em;
}

.cal20__hud-title span {
  color: var(--blue-l);
}

.cal20__hud-sub {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  color: var(--text3);
  margin-top: 2px;
}

.cal20__hud-stats {
  display: flex;
  gap: 22px;
}

.cal20__hud-stat {
  text-align: right;
}

.cal20__hud-stat-v {
  font-size: 22px;
  font-weight: 700;
  line-height: 1;
}

.cal20__hud-stat-l {
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text3);
  margin-top: 3px;
}

.cal20__hud-stat:nth-child(1) .cal20__hud-stat-v {
  color: var(--blue-l);
}

.cal20__hud-stat:nth-child(2) .cal20__hud-stat-v {
  color: var(--teal);
}

.cal20__hud-stat:nth-child(3) .cal20__hud-stat-v {
  color: var(--pink);
}
/* ── Isometric stage ── */

.cal20__stage {
  perspective: 1400px;
  display: flex;
  justify-content: center;
  padding: 40px 0 60px;
  min-height: 480px;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ISOMETRIC TRANSFORM — the core.
   rotateX(58deg) rotateZ(-45deg) tilts
   the whole grid into an architectural
   floating-plane look.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal20__plane {
  transform: rotateX(52deg) rotateZ(-45deg);
  transform-style: preserve-3d;
  animation: cal20-float 6s ease-in-out infinite;
  position: relative;
}

.cal20__grid {
  display: grid;
  grid-template-columns: repeat(7, 56px);
  grid-auto-rows: 56px;
  gap: 8px;
  transform-style: preserve-3d;
}
/* Each tile is a raised 3D block */

.cal20__tile {
  position: relative;
  background: var(--tile-top);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 600;
  color: var(--text);
  cursor: pointer;
  transform-style: preserve-3d;
  transform: translateZ(14px);
  transition: transform 0.25s cubic-bezier(0.34,1.4,0.5,1);
  box-shadow: 0 0 0 1px rgba(255,255,255,0.05);
}
/* Counter-rotate the number to fully face the camera (undo the plane exactly),
   lift it above the tile face, and give it a subtle backing so digits read clearly. */

.cal20__tile .num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 26px;
  height: 22px;
  padding: 0 4px;
  border-radius: 6px;
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  background: rgba(20,26,46,0.55);
  transform: translateZ(6px) rotateZ(45deg) rotateX(-52deg);
  transform-origin: center;
  pointer-events: none;
  white-space: nowrap;
  text-shadow: 0 1px 3px rgba(0,0,0,0.6);
  will-change: transform;
}
/* Block sides via pseudo-elements for the extruded depth */

.cal20__tile::before {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 14px;
  background: var(--tile-l);
  transform: rotateX(-90deg);
  transform-origin: bottom;
  border-radius: 0 0 6px 6px;
}

.cal20__tile::after {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  width: 14px;
  height: 100%;
  background: var(--tile);
  transform: rotateY(90deg);
  transform-origin: right;
  border-radius: 0 6px 6px 0;
}

.cal20__tile:hover {
  transform: translateZ(34px);
}

.cal20__tile.other {
  opacity: 0.3;
  pointer-events: none;
  transform: translateZ(4px);
}
/* Today — tall blue tower, bobbing */

.cal20__tile.today {
  background: var(--blue);
  color: #fff;
  font-weight: 800;
  transform: translateZ(46px);
  animation: cal20-bob 2.5s ease-in-out infinite;
  box-shadow: 0 0 24px rgba(94,114,228,0.6);
}

.cal20__tile.today::before {
  background: #3a4bbf;
  height: 46px;
}

.cal20__tile.today::after {
  background: #4a5dd0;
}
/* Selected — pink raised */

.cal20__tile.selected {
  background: var(--pink);
  color: #fff;
  font-weight: 700;
  transform: translateZ(38px);
}

.cal20__tile.selected::before {
  background: #d04a72;
  height: 38px;
}

.cal20__tile.selected::after {
  background: #e05882;
}
/* Event tiles get a colored top stripe + raised a bit */

.cal20__tile.ev {
  transform: translateZ(24px);
}

.cal20__tile.ev::before {
  height: 24px;
}

.cal20__tile.ev .marker {
  position: absolute;
  top: 4px;
  right: 4px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: translateZ(8px);
}

.cal20__tile.ev--teal .marker {
  background: var(--teal);
}

.cal20__tile.ev--amber .marker {
  background: var(--amber);
}

.cal20__tile.ev--pink .marker {
  background: var(--pink);
}
/* On the bright today/selected towers, give the number a light frosted backing
   and lift it higher so it clears the raised tower geometry. */

.cal20__tile.today .num,
.cal20__tile.selected .num {
  background: rgba(255,255,255,0.28);
  color: #fff;
  transform: translateZ(30px) rotateZ(45deg) rotateX(-52deg);
  z-index: 5;
}
/* Floating month label on the plane */

.cal20__plane-label {
  position: absolute;
  top: -54px;
  left: 0;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: var(--blue-l);
  transform: translateZ(60px);
  white-space: nowrap;
}
/* ── Footer legend ── */

.cal20__legend {
  display: flex;
  justify-content: center;
  gap: 20px;
  position: relative;
  z-index: 10;
}

.cal20__leg {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: var(--text2);
}

.cal20__leg-block {
  width: 14px;
  height: 14px;
  border-radius: 3px;
}

@media (max-width: 600px) {
  .cal20__grid {
    grid-template-columns: repeat(7, 38px);
    grid-auto-rows: 38px;
    gap: 5px;
  }

  .cal20__tile {
    font-size: 12px;
  }

  .cal20__hud-stats {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal20 * {
    animation: none !important;
  }
}
```

## JavaScript
```js
// Wrap the leading number text of every tile in a counter-rotated .num span
// so digits stay upright/legible on the isometric plane (markers untouched).
document.querySelectorAll('#cal20Grid .cal20__tile').forEach(tile => {
  const first = tile.firstChild;
  if (first && first.nodeType === Node.TEXT_NODE && first.textContent.trim()) {
    const span = document.createElement('span');
    span.className = 'num';
    span.textContent = first.textContent.trim();
    tile.replaceChild(span, first);
  }
});

document.querySelectorAll('#cal20Grid .cal20__tile:not(.other)').forEach(tile => {
  tile.addEventListener('click', function() {
    document.querySelectorAll('#cal20Grid .cal20__tile').forEach(t => t.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
