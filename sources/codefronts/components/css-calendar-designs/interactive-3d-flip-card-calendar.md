---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/interactive-3d-flip-card-calendar/"
title: "Interactive 3D Flip Card Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Every day is a true 3D flip card using perspective, preserve-3d and rotateY with hidden backfaces."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive 3D Flip Card Calendar
Source: https://codefronts.com/components/css-calendar-designs/interactive-3d-flip-card-calendar/

Every day is a true 3D flip card using perspective, preserve-3d and rotateY with hidden backfaces. Event days flip on hover; any day flips and stays on click to reveal an emoji, title and time on the back. Dark indigo theme with a selected-event detail panel.
## HTML
```html
<div class="cal19">
  <div class="cal19__wrap">

    <div class="cal19__head">
      <div>
        <div class="cal19__title">June <span>2026</span></div>
        <div class="cal19__hint">// hover or tap a marked day to flip</div>
      </div>
      <div class="cal19__nav">
        <div class="cal19__nav-btn">‹</div>
        <div class="cal19__nav-btn">›</div>
      </div>
    </div>

    <div class="cal19__dow">
      <div class="cal19__dw">SUN</div><div class="cal19__dw">MON</div><div class="cal19__dw">TUE</div>
      <div class="cal19__dw">WED</div><div class="cal19__dw">THU</div><div class="cal19__dw">FRI</div><div class="cal19__dw">SAT</div>
    </div>

    <div class="cal19__grid" id="cal19Grid">
      <!-- other -->
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">25</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">26</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">27</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">28</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">29</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">30</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">31</div><div class="cal19__face cal19__back"></div></div></div>
      <!-- week 2 -->
      <div class="cal19__card3d weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">1</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">2<div class="cal19__ev-dots"><span style="background:var(--teal)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">📋</div><div class="cal19__back-title">Standup</div><div class="cal19__back-time">09:00</div></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">3</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">4<div class="cal19__ev-dots"><span style="background:var(--amber)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">🎉</div><div class="cal19__back-title">Holiday</div><div class="cal19__back-time">All day</div></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">5</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">6</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d weekend has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">7<div class="cal19__ev-dots"><span style="background:var(--pink)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">🍷</div><div class="cal19__back-title">Dinner</div><div class="cal19__back-time">19:30</div></div></div></div>
      <!-- week 3: today=8 -->
      <div class="cal19__card3d today weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">8</div><div class="cal19__face cal19__back"><div class="cal19__back-icon">⭐</div><div class="cal19__back-title">Today</div><div class="cal19__back-time">3 events</div></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">9<div class="cal19__ev-dots"><span style="background:var(--teal)"></span><span style="background:var(--violet-l)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">🗓️</div><div class="cal19__back-title">Sprint</div><div class="cal19__back-time">10:00</div></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">10</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">11<div class="cal19__ev-dots"><span style="background:var(--pink)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">🚀</div><div class="cal19__back-title">Launch</div><div class="cal19__back-time">14:00</div></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">12</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">13<div class="cal19__ev-dots"><span style="background:var(--amber)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">🎨</div><div class="cal19__back-title">Review</div><div class="cal19__back-time">16:30</div></div></div></div>
      <div class="cal19__card3d weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">14</div><div class="cal19__face cal19__back"></div></div></div>
      <!-- week 4 -->
      <div class="cal19__card3d weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">15</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">16</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">17<div class="cal19__ev-dots"><span style="background:var(--teal)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">📊</div><div class="cal19__back-title">Demo Day</div><div class="cal19__back-time">11:00</div></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">18</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">19</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">20<div class="cal19__ev-dots"><span style="background:var(--violet-l)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">👥</div><div class="cal19__back-title">1:1</div><div class="cal19__back-time">15:00</div></div></div></div>
      <div class="cal19__card3d weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">21</div><div class="cal19__face cal19__back"></div></div></div>
      <!-- week 5 -->
      <div class="cal19__card3d weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">22</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">23</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">24<div class="cal19__ev-dots"><span style="background:var(--pink)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">🏛️</div><div class="cal19__back-title">Board</div><div class="cal19__back-time">14:00</div></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">25</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">26</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d has-ev"><div class="cal19__inner"><div class="cal19__face cal19__front">27<div class="cal19__ev-dots"><span style="background:var(--teal)"></span></div></div><div class="cal19__face cal19__back"><div class="cal19__back-icon">🔄</div><div class="cal19__back-title">Retro</div><div class="cal19__back-time">16:00</div></div></div></div>
      <div class="cal19__card3d weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">28</div><div class="cal19__face cal19__back"></div></div></div>
      <!-- week 6 -->
      <div class="cal19__card3d weekend"><div class="cal19__inner"><div class="cal19__face cal19__front">29</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d"><div class="cal19__inner"><div class="cal19__face cal19__front">30</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">1</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">2</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">3</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">4</div><div class="cal19__face cal19__back"></div></div></div>
      <div class="cal19__card3d other"><div class="cal19__inner"><div class="cal19__face cal19__front">5</div><div class="cal19__face cal19__back"></div></div></div>
    </div>

    <div class="cal19__detail">
      <div class="cal19__detail-date">11</div>
      <div class="cal19__detail-body">
        <div class="cal19__detail-title">Product Launch 🚀</div>
        <div class="cal19__detail-sub">Wednesday, June 11 · 2:00 PM · All-hands</div>
        <div class="cal19__detail-tags">
          <span class="cal19__tag" style="background:rgba(253,121,168,0.15);color:var(--pink)">High priority</span>
          <span class="cal19__tag" style="background:rgba(0,206,201,0.15);color:var(--teal)">2 hours</span>
          <span class="cal19__tag" style="background:rgba(108,92,231,0.15);color:var(--violet-l)">28 invited</span>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal19,
.cal19 *,
.cal19 *::before,
.cal19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal19 ::selection {
  background: #6c5ce7;
  color: #fff;
}

.cal19 {
  --bg1: #1a1a2e;
  --bg2: #16213e;
  --card: #232444;
  --card2: #2c2d52;
  --border: rgba(255,255,255,0.08);
  --text: #eef0ff;
  --text2: #9a9cc4;
  --text3: #5a5c88;
  --violet: #6c5ce7;
  --violet-l: #a29bfe;
  --pink: #fd79a8;
  --teal: #00cec9;
  --amber: #fdcb6e;
  font-family: 'Sora', sans-serif;
  background: linear-gradient(135deg, var(--bg1), var(--bg2));
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
}

@keyframes cal19-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.cal19__wrap {
  max-width: 580px;
  width: 100%;
  animation: cal19-in 0.55s ease both;
}
/* ── Header ── */

.cal19__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 22px;
  padding: 0 4px;
}

.cal19__title {
  font-size: 30px;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.cal19__title span {
  color: var(--violet-l);
}

.cal19__hint {
  font-family: 'Spline Sans Mono', monospace;
  font-size: 11px;
  color: var(--text3);
  letter-spacing: 0.05em;
  margin-top: 3px;
}

.cal19__nav {
  display: flex;
  gap: 8px;
}

.cal19__nav-btn {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--card);
  border: 1px solid var(--border);
  color: var(--text2);
  font-size: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  user-select: none;
}

.cal19__nav-btn:hover {
  background: var(--card2);
  color: var(--violet-l);
  border-color: var(--violet);
}
/* ── DOW ── */

.cal19__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 6px;
  margin-bottom: 6px;
}

.cal19__dw {
  text-align: center;
  font-family: 'Spline Sans Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--text3);
  padding: 4px 0;
}
/* ── Grid of flip cards ── */

.cal19__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 6px;
}
/* The flip card mechanism */

.cal19__card3d {
  aspect-ratio: 1;
  perspective: 700px;
  cursor: pointer;
}

.cal19__card3d.other {
  pointer-events: none;
  opacity: 0.25;
}

.cal19__inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.34,1.1,0.5,1);
  transform-style: preserve-3d;
}
/* Flip when card has .flipped OR on hover (for days with events) */

.cal19__card3d.flipped .cal19__inner {
  transform: rotateY(180deg);
}

.cal19__card3d.has-ev:hover .cal19__inner {
  transform: rotateY(180deg);
}

.cal19__face {
  position: absolute;
  inset: 0;
  border-radius: 12px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
/* Front */

.cal19__front {
  background: var(--card);
  border: 1px solid var(--border);
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
  flex-direction: column;
  gap: 4px;
}

.cal19__card3d.weekend .cal19__front {
  color: var(--violet-l);
}

.cal19__front .cal19__ev-dots {
  display: flex;
  gap: 3px;
}

.cal19__front .cal19__ev-dots span {
  width: 4px;
  height: 4px;
  border-radius: 50%;
}
/* Today front */

.cal19__card3d.today .cal19__front {
  background: linear-gradient(135deg, var(--violet), var(--pink));
  border-color: transparent;
  color: #fff;
  font-weight: 800;
  box-shadow: 0 6px 20px rgba(108,92,231,0.4);
}
/* Back — reveals event detail */

.cal19__back {
  transform: rotateY(180deg);
  background: linear-gradient(135deg, var(--card2), var(--card));
  border: 1px solid var(--violet);
  padding: 6px 4px;
  flex-direction: column;
  text-align: center;
  gap: 2px;
}

.cal19__back-icon {
  font-size: 16px;
  line-height: 1;
}

.cal19__back-title {
  font-size: 8px;
  font-weight: 700;
  color: var(--violet-l);
  letter-spacing: 0.02em;
  line-height: 1.1;
}

.cal19__back-time {
  font-family: 'Spline Sans Mono', monospace;
  font-size: 7px;
  color: var(--text3);
}
/* Selected (clicked) keeps flip + glow */

.cal19__card3d.flipped .cal19__back {
  box-shadow: inset 0 0 16px rgba(108,92,231,0.25);
}
/* ── Detail readout ── */

.cal19__detail {
  margin-top: 20px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 22px;
  display: flex;
  align-items: center;
  gap: 18px;
}

.cal19__detail-date {
  font-size: 44px;
  font-weight: 800;
  color: var(--violet-l);
  line-height: 1;
  flex-shrink: 0;
}

.cal19__detail-body {
  flex: 1;
}

.cal19__detail-title {
  font-size: 15px;
  font-weight: 700;
}

.cal19__detail-sub {
  font-size: 12px;
  color: var(--text2);
  margin-top: 3px;
}

.cal19__detail-tags {
  display: flex;
  gap: 6px;
  margin-top: 10px;
  flex-wrap: wrap;
}

.cal19__tag {
  font-family: 'Spline Sans Mono', monospace;
  font-size: 10px;
  padding: 3px 9px;
  border-radius: 20px;
  font-weight: 500;
}

@media (max-width: 480px) {
  .cal19__title {
    font-size: 24px;
  }

  .cal19__front {
    font-size: 13px;
  }

  .cal19__detail {
    flex-direction: column;
    text-align: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal19 * {
    animation: none !important;
  }

  .cal19__inner {
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal19Grid .cal19__card3d:not(.other)').forEach(card => {
  card.addEventListener('click', function() {
    this.classList.toggle('flipped');
  });
});
```
