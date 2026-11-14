---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/css-grid-advent-calendar/"
title: "CSS Grid Advent Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A festive mosaic using grid-auto-flow:dense so wide/tall/big door tiles pack together."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Advent Calendar
Source: https://codefronts.com/components/css-calendar-designs/css-grid-advent-calendar/

A festive mosaic using grid-auto-flow:dense so wide/tall/big door tiles pack together. Each door is a real 3D flip card (perspective + preserve-3d + rotateY) revealing an emoji surprise. Falling-snow background, glowing today door, click to flip open.
## HTML
```html
<div class="cal14">
  <div class="cal14__snow"></div>

  <div class="cal14__wrap">
    <div class="cal14__head">
      <div class="cal14__title">Advent Calendar</div>
      <div class="cal14__sub">December 2026 · Tap a door</div>
    </div>

    <div class="cal14__grid" id="cal14Grid">
      <!-- Mosaic of doors; sizes vary via modifier classes -->
      <div class="cal14__door cal14__door--big"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">1</div><div class="cal14__door-deco">❄</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🎁</div><div class="cal14__back-label">A gift!</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">2</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🍪</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">3</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">⭐</div></div></div></div>
      <div class="cal14__door cal14__door--tall"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">4</div><div class="cal14__door-deco">🎄</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🕯️</div><div class="cal14__back-label">Candle</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">5</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🦌</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">6</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🔔</div></div></div></div>
      <div class="cal14__door cal14__door--wide"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">7</div><div class="cal14__door-deco">✨</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🧦</div><div class="cal14__back-label">Stocking</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">8</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">☃️</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">9</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🍬</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">10</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🎅</div></div></div></div>
      <div class="cal14__door cal14__door--tall"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">11</div><div class="cal14__door-deco">❄</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🎶</div><div class="cal14__back-label">Carols</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">12</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🧣</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">13</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🌟</div></div></div></div>
      <div class="cal14__door cal14__door--wide"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">14</div><div class="cal14__door-deco">🎄</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🥮</div><div class="cal14__back-label">Treat</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">15</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🎀</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">16</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🍫</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">17</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🦌</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">18</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">⛄</div></div></div></div>
      <div class="cal14__door cal14__door--wide"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">19</div><div class="cal14__door-deco">✨</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🎁</div><div class="cal14__back-label">Surprise</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">20</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🔔</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">21</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🌟</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">22</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🍷</div></div></div></div>
      <div class="cal14__door"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">23</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🎶</div></div></div></div>
      <div class="cal14__door today cal14__door--big"><div class="cal14__door-inner"><div class="cal14__face cal14__front"><div class="cal14__door-num">24</div><div class="cal14__door-deco">⭐ Today ⭐</div></div><div class="cal14__face cal14__back"><div class="cal14__back-emoji">🎄</div><div class="cal14__back-label">Christmas Eve!</div></div></div></div>
    </div>

    <div class="cal14__hint">🎁 <b>1 door</b> opened · 23 to go · come back tomorrow!</div>
  </div>
</div>
```
## CSS
```css
.cal14,
.cal14 *,
.cal14 *::before,
.cal14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal14 ::selection {
  background: #c0392b;
  color: #fff;
}

.cal14 {
  --bg1: #0a2342;
  --bg2: #123c63;
  --red: #c0392b;
  --red-d: #8e2820;
  --green: #1e6f5c;
  --green-l: #2a9d8f;
  --gold: #e9c46a;
  --gold-d: #d4a843;
  --cream: #fdf6ec;
  --snow: #ffffff;
  font-family: 'Quicksand', sans-serif;
  background: radial-gradient(ellipse at top, var(--bg2) 0%, var(--bg1) 70%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--cream);
  position: relative;
  overflow: hidden;
}
/* Falling snow */

.cal14__snow {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background-image: radial-gradient(2px 2px at 10% 10%, #fff, transparent), radial-gradient(2px 2px at 30% 40%, rgba(255,255,255,.8), transparent), radial-gradient(1px 1px at 50% 20%, #fff, transparent), radial-gradient(2px 2px at 70% 60%, rgba(255,255,255,.7), transparent), radial-gradient(1px 1px at 90% 30%, #fff, transparent), radial-gradient(2px 2px at 20% 80%, rgba(255,255,255,.6), transparent), radial-gradient(1px 1px at 60% 90%, #fff, transparent), radial-gradient(2px 2px at 85% 75%, rgba(255,255,255,.7), transparent);
  background-size: 100% 100%;
  animation: cal14-snowfall 12s linear infinite;
  opacity: 0.5;
}

@keyframes cal14-snowfall {
  from {
    background-position: 0 0, 0 0, 0 0, 0 0, 0 0, 0 0, 0 0, 0 0;
  }

  to {
    background-position: 0 100vh, 0 100vh, 0 100vh, 0 100vh, 0 100vh, 0 100vh, 0 100vh, 0 100vh;
  }
}

@keyframes cal14-in {
  from {
    opacity: 0;
    transform: scale(0.95);
  }

  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes cal14-twinkle {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.4;
  }
}

@keyframes cal14-pop {
  0% {
    transform: scale(0.6) rotate(-10deg);
    opacity: 0;
  }

  60% {
    transform: scale(1.15) rotate(4deg);
  }

  100% {
    transform: scale(1) rotate(0);
    opacity: 1;
  }
}

.cal14__wrap {
  position: relative;
  z-index: 1;
  max-width: 680px;
  width: 100%;
  animation: cal14-in 0.6s ease both;
}
/* ── Header ── */

.cal14__head {
  text-align: center;
  margin-bottom: 24px;
}

.cal14__title {
  font-family: 'Mountains of Christmas', cursive;
  font-weight: 700;
  font-size: 52px;
  line-height: 1;
  color: var(--gold);
  text-shadow: 0 2px 0 var(--gold-d), 0 0 30px rgba(233,196,106,0.4);
}

.cal14__sub {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: rgba(253,246,236,0.6);
  margin-top: 6px;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CSS GRID with auto-flow:dense — doors
   of varying sizes pack like a mosaic.
   grid-auto-flow:dense lets big tiles
   slot in wherever they fit.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal14__grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-auto-rows: 80px;
  grid-auto-flow: dense;
  gap: 10px;
}
/* ── Each door — 3D flip card ── */

.cal14__door {
  perspective: 600px;
  cursor: pointer;
  position: relative;
}
/* Size variants for mosaic effect */

.cal14__door--wide {
  grid-column: span 2;
}

.cal14__door--tall {
  grid-row: span 2;
}

.cal14__door--big {
  grid-column: span 2;
  grid-row: span 2;
}

.cal14__door-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.34,1.2,0.64,1);
  transform-style: preserve-3d;
  border-radius: 14px;
}

.cal14__door.open .cal14__door-inner {
  transform: rotateY(180deg);
}
/* Faces */

.cal14__face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border-radius: 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
/* Front face — the closed door */

.cal14__front {
  background: linear-gradient(145deg, var(--red) 0%, var(--red-d) 100%);
  border: 2px solid rgba(255,255,255,0.15);
  box-shadow: inset 0 2px 8px rgba(255,255,255,0.15), 0 6px 16px rgba(0,0,0,0.35);
}

.cal14__door:nth-child(3n) .cal14__front {
  background: linear-gradient(145deg, var(--green-l) 0%, var(--green) 100%);
}

.cal14__door:nth-child(4n) .cal14__front {
  background: linear-gradient(145deg, var(--gold) 0%, var(--gold-d) 100%);
}

.cal14__door-num {
  font-family: 'Mountains of Christmas', cursive;
  font-weight: 700;
  font-size: 32px;
  color: var(--cream);
  text-shadow: 0 2px 3px rgba(0,0,0,0.3);
  line-height: 1;
}

.cal14__door--big .cal14__door-num {
  font-size: 56px;
}

.cal14__door:nth-child(4n) .cal14__door-num {
  color: var(--bg1);
  text-shadow: none;
}

.cal14__door-deco {
  font-size: 14px;
  margin-top: 2px;
  opacity: 0.7;
}
/* Back face — the surprise behind the door */

.cal14__back {
  background: linear-gradient(145deg, var(--cream) 0%, #f0e6d2 100%);
  transform: rotateY(180deg);
  border: 2px solid var(--gold);
  padding: 6px;
  text-align: center;
}

.cal14__back-emoji {
  font-size: 28px;
  animation: cal14-pop 0.5s ease both;
}

.cal14__door--big .cal14__back-emoji {
  font-size: 52px;
}

.cal14__back-label {
  font-size: 9px;
  font-weight: 700;
  color: var(--red-d);
  margin-top: 3px;
  letter-spacing: 0.04em;
}

.cal14__door--big .cal14__back-label,
.cal14__door--wide .cal14__back-label {
  font-size: 11px;
}
/* Today's door — glowing gold ring + twinkle */

.cal14__door.today .cal14__front {
  border-color: var(--gold);
  box-shadow: inset 0 2px 8px rgba(255,255,255,0.2), 0 0 0 3px var(--gold), 0 0 24px rgba(233,196,106,0.6);
}

.cal14__door.today .cal14__door-deco {
  animation: cal14-twinkle 1.5s ease-in-out infinite;
}
/* Hover lift */

.cal14__door:hover .cal14__door-inner:not(.open) {
  transform: translateY(-4px) scale(1.03);
}

.cal14__door.open:hover .cal14__door-inner {
  transform: rotateY(180deg) translateY(4px) scale(1.03);
}
/* ── Footer hint ── */

.cal14__hint {
  text-align: center;
  margin-top: 22px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: rgba(253,246,236,0.5);
}

.cal14__hint b {
  color: var(--gold);
}

@media (max-width: 560px) {
  .cal14__title {
    font-size: 38px;
  }

  .cal14__grid {
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 70px;
    gap: 8px;
  }

  .cal14__door-num {
    font-size: 24px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal14 *,
    .cal14__snow {
    animation: none !important;
  }

  .cal14__door-inner {
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal14Grid .cal14__door').forEach(door => {
  door.addEventListener('click', function() {
    this.classList.toggle('open');
  });
});
```
