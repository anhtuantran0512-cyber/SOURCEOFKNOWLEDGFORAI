---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/vertical-timeline-slipstream-calendar/"
title: "Vertical Timeline Slipstream Calendar"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Dates cascade down a central spine, alternating left and right via a 2-column grid with directional slide-in."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Timeline Slipstream Calendar
Source: https://codefronts.com/components/css-calendar-designs/vertical-timeline-slipstream-calendar/

Dates cascade down a central spine, alternating left and right via a 2-column grid with directional slide-in. Nodes pin to a gradient line; today is a green card with a pulsing node. Each card stacks date, weekday and a dotted event list; collapses to a single rail on mobile.
## HTML
```html
<div class="cal25">
  <div class="cal25__wrap">

    <div class="cal25__head">
      <div class="cal25__title">June <b>2026</b></div>
      <div class="cal25__sub">Timeline · this week</div>
    </div>

    <div class="cal25__stream" id="cal25Stream">

      <div class="cal25__divider"><span>Week 23</span></div>

      <!-- Sun 8 — today -->
      <div class="cal25__item cal25__item--left cal25__item--today">
        <div class="cal25__node"></div>
        <div class="cal25__card">
          <div class="cal25__date-row">
            <span class="cal25__date-num">8</span>
            <span class="cal25__date-dow">Sun · Today</span>
          </div>
          <div class="cal25__events">
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:#fff"></span>Sprint Planning · 10:00</span>
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:#fff"></span>Product Launch · 14:00</span>
          </div>
        </div>
      </div>

      <!-- Mon 9 -->
      <div class="cal25__item cal25__item--right">
        <div class="cal25__node"></div>
        <div class="cal25__card">
          <div class="cal25__date-row">
            <span class="cal25__date-num">9</span>
            <span class="cal25__date-dow">Monday</span>
          </div>
          <div class="cal25__events">
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:var(--terra)"></span>Design Review · 11:00</span>
          </div>
        </div>
      </div>

      <!-- Tue 10 -->
      <div class="cal25__item cal25__item--left">
        <div class="cal25__node"></div>
        <div class="cal25__card">
          <div class="cal25__date-row">
            <span class="cal25__date-num">10</span>
            <span class="cal25__date-dow">Tuesday</span>
          </div>
          <div class="cal25__events">
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:var(--gold2)"></span>Free day</span>
          </div>
        </div>
      </div>

      <!-- Wed 11 -->
      <div class="cal25__item cal25__item--right">
        <div class="cal25__node"></div>
        <div class="cal25__card">
          <div class="cal25__date-row">
            <span class="cal25__date-num">11</span>
            <span class="cal25__date-dow">Wednesday</span>
          </div>
          <div class="cal25__events">
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:var(--terra)"></span>Board Meeting · 09:00</span>
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:var(--green)"></span>Team Dinner · 19:30</span>
          </div>
        </div>
      </div>

      <!-- Thu 12 -->
      <div class="cal25__item cal25__item--left">
        <div class="cal25__node"></div>
        <div class="cal25__card">
          <div class="cal25__date-row">
            <span class="cal25__date-num">12</span>
            <span class="cal25__date-dow">Thursday</span>
          </div>
          <div class="cal25__events">
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:var(--gold2)"></span>1:1 with Sam · 15:00</span>
          </div>
        </div>
      </div>

      <!-- Fri 13 -->
      <div class="cal25__item cal25__item--right">
        <div class="cal25__node"></div>
        <div class="cal25__card">
          <div class="cal25__date-row">
            <span class="cal25__date-num">13</span>
            <span class="cal25__date-dow">Friday</span>
          </div>
          <div class="cal25__events">
            <span class="cal25__ev"><span class="cal25__ev-dot" style="background:var(--green)"></span>Retro · 16:00</span>
          </div>
        </div>
      </div>

    </div>

  </div>
</div>
```
## CSS
```css
.cal25,
.cal25 *,
.cal25 *::before,
.cal25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal25 ::selection {
  background: #5b8a72;
  color: #fff;
}

.cal25 {
  --bg: #faf8f4;
  --line: #d9d2c4;
  --ink: #2a2620;
  --ink2: #6e665a;
  --ink3: #a59c8c;
  --green: #5b8a72;
  --terra: #c17a52;
  --gold: #c9a44a;
  --gold2: #b89344;
  --card: #ffffff;
  font-family: 'Inter', sans-serif;
  background: var(--bg);
  background-image: radial-gradient(circle at 50% 0%, #fffdf9, #f2ece1);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  padding: 48px 20px;
  color: var(--ink);
}

@keyframes cal25-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes cal25-slip-l {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes cal25-slip-r {
  from {
    opacity: 0;
    transform: translateX(30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes cal25-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(91,138,114,0.4);
  }

  50% {
    box-shadow: 0 0 0 8px rgba(91,138,114,0);
  }
}

.cal25__wrap {
  max-width: 680px;
  width: 100%;
  animation: cal25-in 0.5s ease both;
}
/* ── Header ── */

.cal25__head {
  text-align: center;
  margin-bottom: 40px;
}

.cal25__title {
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 46px;
  font-weight: 400;
  line-height: 1;
}

.cal25__title b {
  font-style: normal;
  font-weight: 600;
  color: var(--green);
}

.cal25__sub {
  font-size: 12px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ink3);
  margin-top: 8px;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   VERTICAL TIMELINE — central line,
   items alternate left/right via grid.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal25__stream {
  position: relative;
  padding: 10px 0;
}
/* the central spine */

.cal25__stream::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 2px;
  background: linear-gradient(180deg, transparent, var(--line) 6%, var(--line) 94%, transparent);
  transform: translateX(-50%);
}

.cal25__item {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-bottom: 14px;
}
/* node on the spine */

.cal25__node {
  position: absolute;
  left: 50%;
  top: 22px;
  transform: translateX(-50%);
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--card);
  border: 3px solid var(--ink3);
  z-index: 3;
}
/* card */

.cal25__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 16px 18px;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(42,38,32,0.05);
}

.cal25__card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(42,38,32,0.1);
  border-color: var(--green);
}
/* LEFT item: card in col 1, animate from left */

.cal25__item--left .cal25__card {
  grid-column: 1;
  margin-right: 32px;
  text-align: right;
  animation: cal25-slip-l 0.5s ease both;
}
/* RIGHT item: card in col 2, animate from right */

.cal25__item--right .cal25__card {
  grid-column: 2;
  margin-left: 32px;
  animation: cal25-slip-r 0.5s ease both;
}
/* card content */

.cal25__date-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.cal25__item--left .cal25__date-row {
  justify-content: flex-end;
}

.cal25__date-num {
  font-family: 'Fraunces', serif;
  font-size: 30px;
  font-weight: 600;
  line-height: 1;
  color: var(--ink);
}

.cal25__date-dow {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink3);
}

.cal25__events {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.cal25__item--left .cal25__events {
  align-items: flex-end;
}

.cal25__ev {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: var(--ink2);
}

.cal25__ev-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  flex-shrink: 0;
}
/* Today node + card emphasis */

.cal25__item--today .cal25__node {
  background: var(--green);
  border-color: var(--green);
  width: 18px;
  height: 18px;
  animation: cal25-pulse 2.5s ease-in-out infinite;
}

.cal25__item--today .cal25__card {
  background: linear-gradient(135deg, var(--green), #4a7560);
  border-color: transparent;
  color: #fff;
}

.cal25__item--today .cal25__date-num {
  color: #fff;
}

.cal25__item--today .cal25__date-dow {
  color: rgba(255,255,255,0.7);
}

.cal25__item--today .cal25__ev {
  color: rgba(255,255,255,0.9);
}
/* selected */

.cal25__card.selected {
  border-color: var(--terra);
  box-shadow: 0 0 0 2px var(--terra);
}
/* month divider chip */

.cal25__divider {
  position: relative;
  text-align: center;
  margin: 8px 0 20px;
  z-index: 3;
}

.cal25__divider span {
  display: inline-block;
  background: var(--bg);
  padding: 4px 16px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--ink3);
  border: 1px solid var(--line);
  border-radius: 20px;
}

@media (max-width: 560px) {
  .cal25__stream::before {
    left: 20px;
  }

  .cal25__item {
    grid-template-columns: 1fr;
  }

  .cal25__node {
    left: 20px;
  }

  .cal25__item--left .cal25__card,
    .cal25__item--right .cal25__card {
    grid-column: 1;
    margin-left: 44px;
    margin-right: 0;
    text-align: left;
    animation: cal25-slip-r 0.5s ease both;
  }

  .cal25__item--left .cal25__date-row,
    .cal25__item--left .cal25__events {
    justify-content: flex-start;
    align-items: flex-start;
  }

  .cal25__divider {
    text-align: left;
    padding-left: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal25 * {
    animation: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal25Stream .cal25__card').forEach(card => {
  card.addEventListener('click', function() {
    document.querySelectorAll('#cal25Stream .cal25__card').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
