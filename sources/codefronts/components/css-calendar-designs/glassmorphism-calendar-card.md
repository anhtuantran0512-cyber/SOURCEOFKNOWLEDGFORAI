---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/glassmorphism-calendar-card/"
title: "Glassmorphism Calendar Card"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "The definitive glassmorphism reference on an aurora-borealis scene with four animated gradient blobs and a starfield."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Calendar Card
Source: https://codefronts.com/components/css-calendar-designs/glassmorphism-calendar-card/

The definitive glassmorphism reference on an aurora-borealis scene with four animated gradient blobs and a starfield. The card uses backdrop-filter blur/saturate with a layered inner shine; today glows, the card floats, and frosted event pills demonstrate layered glass depth.
## HTML
```html
<div class="cal07">

  <!-- Aurora background -->
  <div class="cal07__aurora">
    <div class="cal07__aurora-blob"></div>
    <div class="cal07__aurora-blob"></div>
    <div class="cal07__aurora-blob"></div>
    <div class="cal07__aurora-blob"></div>
  </div>
  <div class="cal07__stars"></div>

  <div class="cal07__scene">

    <!-- Glass calendar card -->
    <div class="cal07__card">

      <div class="cal07__hd">
        <div class="cal07__hd-left">
          <div class="cal07__card-month">June</div>
          <div class="cal07__card-year-row">
            <div class="cal07__card-year">2026</div>
            <div class="cal07__card-badge">Q2</div>
          </div>
        </div>
        <div class="cal07__hd-right">
          <div class="cal07__nav">
            <div class="cal07__nav-btn">‹</div>
            <div class="cal07__nav-btn">›</div>
          </div>
        </div>
      </div>

      <div class="cal07__dow">
        <div class="cal07__dw">S</div><div class="cal07__dw">M</div>
        <div class="cal07__dw">T</div><div class="cal07__dw">W</div>
        <div class="cal07__dw">T</div><div class="cal07__dw">F</div>
        <div class="cal07__dw">S</div>
      </div>

      <div class="cal07__dates" id="cal07Dates">
        <!-- May -->
        <div class="cal07__date dim weekend"><div class="cal07__date-n">25</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">26</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">27</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">28</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">29</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">30</div></div>
        <div class="cal07__date dim weekend"><div class="cal07__date-n">31</div></div>
        <!-- June 1–7 -->
        <div class="cal07__date weekend"><div class="cal07__date-n">1</div></div>
        <div class="cal07__date"><div class="cal07__date-n">2</div><div class="cal07__date-pip cal07__date-pip--t"></div></div>
        <div class="cal07__date"><div class="cal07__date-n">3</div></div>
        <div class="cal07__date"><div class="cal07__date-n">4</div><div class="cal07__date-pip cal07__date-pip--a"></div></div>
        <div class="cal07__date"><div class="cal07__date-n">5</div></div>
        <div class="cal07__date"><div class="cal07__date-n">6</div></div>
        <div class="cal07__date weekend"><div class="cal07__date-n">7</div><div class="cal07__date-pip cal07__date-pip--p"></div></div>
        <!-- June 8–14 -->
        <div class="cal07__date today weekend"><div class="cal07__date-n">8</div></div>
        <div class="cal07__date"><div class="cal07__date-n">9</div><div class="cal07__date-pip cal07__date-pip--t"></div></div>
        <div class="cal07__date"><div class="cal07__date-n">10</div></div>
        <div class="cal07__date"><div class="cal07__date-n">11</div><div class="cal07__date-pip cal07__date-pip--p"></div></div>
        <div class="cal07__date"><div class="cal07__date-n">12</div></div>
        <div class="cal07__date"><div class="cal07__date-n">13</div><div class="cal07__date-pip cal07__date-pip--a"></div></div>
        <div class="cal07__date weekend"><div class="cal07__date-n">14</div></div>
        <!-- June 15–21 -->
        <div class="cal07__date weekend"><div class="cal07__date-n">15</div></div>
        <div class="cal07__date"><div class="cal07__date-n">16</div></div>
        <div class="cal07__date"><div class="cal07__date-n">17</div><div class="cal07__date-pip cal07__date-pip--t"></div></div>
        <div class="cal07__date"><div class="cal07__date-n">18</div></div>
        <div class="cal07__date"><div class="cal07__date-n">19</div></div>
        <div class="cal07__date"><div class="cal07__date-n">20</div><div class="cal07__date-pip cal07__date-pip--p"></div></div>
        <div class="cal07__date weekend"><div class="cal07__date-n">21</div></div>
        <!-- June 22–28 -->
        <div class="cal07__date weekend"><div class="cal07__date-n">22</div></div>
        <div class="cal07__date"><div class="cal07__date-n">23</div><div class="cal07__date-pip cal07__date-pip--a"></div></div>
        <div class="cal07__date"><div class="cal07__date-n">24</div></div>
        <div class="cal07__date"><div class="cal07__date-n">25</div><div class="cal07__date-pip cal07__date-pip--t"></div></div>
        <div class="cal07__date"><div class="cal07__date-n">26</div></div>
        <div class="cal07__date"><div class="cal07__date-n">27</div></div>
        <div class="cal07__date weekend"><div class="cal07__date-n">28</div></div>
        <!-- June 29–30 + July -->
        <div class="cal07__date weekend"><div class="cal07__date-n">29</div></div>
        <div class="cal07__date"><div class="cal07__date-n">30</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">1</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">2</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">3</div></div>
        <div class="cal07__date dim"><div class="cal07__date-n">4</div></div>
        <div class="cal07__date dim weekend"><div class="cal07__date-n">5</div></div>
      </div>

      <div class="cal07__strip">
        <div class="cal07__strip-stat">
          <div class="cal07__strip-val">12</div>
          <div class="cal07__strip-lbl">Events</div>
        </div>
        <div class="cal07__strip-stat">
          <div class="cal07__strip-val">4</div>
          <div class="cal07__strip-lbl">Holidays</div>
        </div>
        <div class="cal07__strip-stat">
          <div class="cal07__strip-val">7</div>
          <div class="cal07__strip-lbl">Left</div>
        </div>
      </div>

    </div>

    <!-- Event glass pills below -->
    <div class="cal07__events-row">
      <div class="cal07__ev-glass">
        <div class="cal07__ev-icon" style="background:rgba(0,201,177,0.15)">🚀</div>
        <div class="cal07__ev-body">
          <div class="cal07__ev-name">Product Launch</div>
          <div class="cal07__ev-time">Wed Jun 11 · 9:00 AM</div>
        </div>
        <div class="cal07__ev-pill" style="background:rgba(0,201,177,0.15);color:var(--teal);border:1px solid rgba(0,201,177,0.3)">Today+3</div>
      </div>
      <div class="cal07__ev-glass">
        <div class="cal07__ev-icon" style="background:rgba(147,51,234,0.15)">📊</div>
        <div class="cal07__ev-body">
          <div class="cal07__ev-name">Board Meeting</div>
          <div class="cal07__ev-time">Thu Jun 25 · 2:00 PM</div>
        </div>
        <div class="cal07__ev-pill" style="background:rgba(147,51,234,0.15);color:var(--purple);border:1px solid rgba(147,51,234,0.3)">In 17d</div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cal07,
.cal07 *,
.cal07 *::before,
.cal07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal07 ::selection {
  background: rgba(255,255,255,0.3);
  color: #fff;
}

.cal07 {
  --teal: #00c9b1;
  --blue: #3b82f6;
  --purple: #9333ea;
  --pink: #f472b6;
  --amber: #fbbf24;
  --white: #ffffff;
  --text: rgba(255,255,255,0.92);
  --muted: rgba(255,255,255,0.45);
  --dim: rgba(255,255,255,0.18);
  --glass: rgba(255,255,255,0.09);
  --glass2: rgba(255,255,255,0.14);
  --border: rgba(255,255,255,0.18);
  --border2: rgba(255,255,255,0.28);
  font-family: 'Manrope', sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  position: relative;
  overflow: hidden;
  /* Aurora background */
  background: #060b14;
}
/* ── Aurora mesh background ── */

.cal07__aurora {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
}

.cal07__aurora-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.55;
  animation: cal07-aurora 14s ease-in-out infinite alternate;
}

.cal07__aurora-blob:nth-child(1) {
  width: 700px;
  height: 500px;
  background: radial-gradient(ellipse, #00c9b1 0%, transparent 70%);
  top: -150px;
  left: -200px;
  animation-duration: 16s;
}

.cal07__aurora-blob:nth-child(2) {
  width: 600px;
  height: 500px;
  background: radial-gradient(ellipse, #9333ea 0%, transparent 70%);
  top: -100px;
  right: -150px;
  animation-duration: 12s;
  animation-direction: alternate-reverse;
}

.cal07__aurora-blob:nth-child(3) {
  width: 500px;
  height: 400px;
  background: radial-gradient(ellipse, #3b82f6 0%, transparent 70%);
  bottom: -100px;
  left: 10%;
  animation-duration: 18s;
}

.cal07__aurora-blob:nth-child(4) {
  width: 300px;
  height: 300px;
  background: radial-gradient(ellipse, #f472b6 0%, transparent 70%);
  bottom: 20%;
  right: 10%;
  animation-duration: 10s;
  animation-direction: alternate-reverse;
}
/* Stars overlay */

.cal07__stars {
  position: fixed;
  inset: 0;
  background-image: radial-gradient(1px 1px at 20% 30%, rgba(255,255,255,0.5), transparent), radial-gradient(1px 1px at 80% 10%, rgba(255,255,255,0.4), transparent), radial-gradient(1px 1px at 50% 60%, rgba(255,255,255,0.3), transparent), radial-gradient(1px 1px at 10% 80%, rgba(255,255,255,0.35), transparent), radial-gradient(1px 1px at 70% 85%, rgba(255,255,255,0.25), transparent), radial-gradient(1px 1px at 35% 45%, rgba(255,255,255,0.4), transparent), radial-gradient(1px 1px at 90% 50%, rgba(255,255,255,0.3), transparent), radial-gradient(1px 1px at 15% 15%, rgba(255,255,255,0.45), transparent), radial-gradient(1px 1px at 60% 25%, rgba(255,255,255,0.2), transparent), radial-gradient(1px 1px at 45% 75%, rgba(255,255,255,0.35), transparent);
  z-index: 0;
  pointer-events: none;
}

@keyframes cal07-aurora {
  from {
    transform: translate(0, 0) scale(1);
  }

  to {
    transform: translate(40px, 30px) scale(1.12);
  }
}

@keyframes cal07-float {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-8px);
  }
}

@keyframes cal07-glow {
  0%,
    100% {
    box-shadow: 0 0 20px rgba(0,201,177,0.3), 0 0 60px rgba(0,201,177,0.15);
  }

  50% {
    box-shadow: 0 0 35px rgba(0,201,177,0.5), 0 0 80px rgba(0,201,177,0.25);
  }
}

@keyframes cal07-shimmer {
  0% {
    opacity: 0.5;
  }

  50% {
    opacity: 1;
  }

  100% {
    opacity: 0.5;
  }
}

@keyframes cal07-enter {
  from {
    opacity: 0;
    transform: scale(0.94) translateY(20px);
  }

  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}
/* ── Main glass card ── */

.cal07__card {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: 420px;
  background: var(--glass);
  backdrop-filter: blur(32px) saturate(180%) brightness(1.1);
  -webkit-backdrop-filter: blur(32px) saturate(180%) brightness(1.1);
  border: 1px solid var(--border2);
  border-radius: 32px;
  padding: 32px;
  box-shadow: 0 0 0 1px rgba(255,255,255,0.05) inset, 0 40px 80px rgba(0,0,0,0.5), 0 8px 32px rgba(0,0,0,0.3);
  animation: cal07-enter 0.7s cubic-bezier(0.22,1,0.36,1) both, cal07-float 6s ease-in-out 1s infinite;
}
/* Inner shine edge */

.cal07__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 32px;
  background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, transparent 50%, rgba(255,255,255,0.04) 100%);
  pointer-events: none;
}
/* ── Card header ── */

.cal07__hd {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 28px;
}

.cal07__hd-left {
}

.cal07__card-month {
  font-family: 'Gilda Display', serif;
  font-size: 42px;
  color: var(--white);
  line-height: 1;
  text-shadow: 0 0 30px rgba(0,201,177,0.4);
}

.cal07__card-year-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 4px;
}

.cal07__card-year {
  font-size: 13px;
  font-weight: 500;
  color: var(--muted);
  letter-spacing: 0.12em;
}

.cal07__card-badge {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 20px;
  background: rgba(0,201,177,0.18);
  border: 1px solid rgba(0,201,177,0.35);
  color: var(--teal);
  animation: cal07-shimmer 3s ease-in-out infinite;
}

.cal07__hd-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
}

.cal07__nav {
  display: flex;
  gap: 6px;
}

.cal07__nav-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--glass2);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--text);
  font-size: 16px;
  transition: all 0.2s;
  user-select: none;
  backdrop-filter: blur(10px);
}

.cal07__nav-btn:hover {
  background: rgba(0,201,177,0.2);
  border-color: var(--teal);
  color: var(--teal);
}
/* ── DOW row ── */

.cal07__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 6px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--dim);
}

.cal07__dw {
  text-align: center;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 4px 0;
}

.cal07__dw:first-child,
.cal07__dw:last-child {
  color: rgba(0,201,177,0.7);
}
/* ── Date grid ── */

.cal07__dates {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 3px;
}

.cal07__date {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.18s;
  position: relative;
  gap: 3px;
}

.cal07__date:hover {
  background: var(--glass2);
}

.cal07__date.dim {
  opacity: 0.22;
  pointer-events: none;
}

.cal07__date-n {
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
  line-height: 1;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.18s;
}

.cal07__date.weekend .cal07__date-n {
  color: rgba(0,201,177,0.85);
}
/* Today */

.cal07__date.today .cal07__date-n {
  background: linear-gradient(135deg, var(--teal), var(--blue));
  color: #fff;
  font-weight: 700;
  box-shadow: 0 4px 16px rgba(0,201,177,0.5);
  animation: cal07-glow 2.5s ease-in-out infinite;
}
/* Selected */

.cal07__date.selected .cal07__date-n {
  background: linear-gradient(135deg, var(--purple), var(--pink));
  color: #fff;
  font-weight: 700;
  box-shadow: 0 4px 16px rgba(147,51,234,0.45);
  transform: scale(1.1);
}
/* Pip */

.cal07__date-pip {
  width: 4px;
  height: 4px;
  border-radius: 50%;
}

.cal07__date-pip--t {
  background: var(--teal);
  box-shadow: 0 0 6px var(--teal);
}

.cal07__date-pip--p {
  background: var(--purple);
}

.cal07__date-pip--a {
  background: var(--amber);
}
/* ── Bottom summary strip ── */

.cal07__strip {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid var(--dim);
  display: flex;
  gap: 12px;
}

.cal07__strip-stat {
  flex: 1;
  background: var(--glass2);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 12px 14px;
  backdrop-filter: blur(10px);
}

.cal07__strip-val {
  font-family: 'Gilda Display', serif;
  font-size: 28px;
  color: var(--white);
  line-height: 1;
}

.cal07__strip-lbl {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  margin-top: 3px;
}
/* Color the values */

.cal07__strip-stat:nth-child(1) .cal07__strip-val {
  color: var(--teal);
  text-shadow: 0 0 16px rgba(0,201,177,0.5);
}

.cal07__strip-stat:nth-child(2) .cal07__strip-val {
  color: var(--amber);
}

.cal07__strip-stat:nth-child(3) .cal07__strip-val {
  color: var(--pink);
}
/* ── Event preview below card ── */

.cal07__events-row {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
  max-width: 420px;
  margin-top: 16px;
}

.cal07__ev-glass {
  background: var(--glass);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 14px 18px;
  display: flex;
  align-items: center;
  gap: 14px;
  animation: cal07-enter 0.5s ease both;
}

.cal07__ev-glass:nth-child(2) {
  animation-delay: 0.1s;
}

.cal07__ev-glass:nth-child(3) {
  animation-delay: 0.2s;
}

.cal07__ev-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}

.cal07__ev-body {
  flex: 1;
  min-width: 0;
}

.cal07__ev-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
}

.cal07__ev-time {
  font-size: 11px;
  color: var(--muted);
  margin-top: 2px;
}

.cal07__ev-pill {
  font-size: 10px;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 20px;
  flex-shrink: 0;
}
/* Scene wrapper */

.cal07__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  position: relative;
  z-index: 10;
}

@media (max-width: 480px) {
  .cal07__card {
    padding: 22px;
    border-radius: 24px;
  }

  .cal07__card-month {
    font-size: 32px;
  }

  .cal07__strip {
    gap: 8px;
  }

  .cal07__strip-stat {
    padding: 10px;
  }

  .cal07__strip-val {
    font-size: 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal07 * {
    animation: none !important;
    transition: none !important;
  }

  .cal07__aurora-blob {
    opacity: 0.3;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal07Dates .cal07__date:not(.dim)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal07Dates .cal07__date').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});
```
