---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/glassmorphism-css-calendar-widget/"
title: "Glassmorphism CSS Calendar Widget"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A frosted-glass calendar on an animated indigo aurora gradient with two drifting light orbs."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism CSS Calendar Widget
Source: https://codefronts.com/components/css-calendar-designs/glassmorphism-css-calendar-widget/

A frosted-glass calendar on an animated indigo aurora gradient with two drifting light orbs. Heavy backdrop-filter blur, a shimmering gradient month title, a dual-ring pulse on today, plus a glass side panel with a floating date tile, live event strip and emoji mood tracker.
## HTML
```html
<div class="cal-01-scene">

  <!-- Main Calendar -->
  <div class="cal-01-card">
    <div class="cal-01-header">
      <div class="cal-01-month-display">
        <div class="cal-01-month-name">June</div>
        <div class="cal-01-year">2026</div>
      </div>
      <div class="cal-01-nav">
        <div class="cal-01-nav-btn">‹</div>
        <div class="cal-01-nav-btn">›</div>
      </div>
    </div>

    <div class="cal-01-days-header">
      <div class="cal-01-day-label">Su</div>
      <div class="cal-01-day-label">Mo</div>
      <div class="cal-01-day-label">Tu</div>
      <div class="cal-01-day-label">We</div>
      <div class="cal-01-day-label">Th</div>
      <div class="cal-01-day-label">Fr</div>
      <div class="cal-01-day-label">Sa</div>
    </div>

    <div class="cal-01-grid" id="cal-01-calGrid">
      <!-- Week 1 (May overflow) -->
      <div class="cal-01-cell cal-01-other-month cal-01-weekend">25</div>
      <div class="cal-01-cell cal-01-other-month">26</div>
      <div class="cal-01-cell cal-01-other-month">27</div>
      <div class="cal-01-cell cal-01-other-month">28</div>
      <div class="cal-01-cell cal-01-other-month">29</div>
      <div class="cal-01-cell cal-01-other-month">30</div>
      <div class="cal-01-cell cal-01-other-month cal-01-weekend">31</div>
      <!-- Week 2 -->
      <div class="cal-01-cell cal-01-weekend">1</div>
      <div class="cal-01-cell">2<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--purple"></span></div></div>
      <div class="cal-01-cell">3</div>
      <div class="cal-01-cell">4<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--pink"></span><span class="cal-01-dot cal-01-dot--green"></span></div></div>
      <div class="cal-01-cell">5</div>
      <div class="cal-01-cell">6</div>
      <div class="cal-01-cell cal-01-weekend">7<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--purple"></span></div></div>
      <!-- Week 3 -->
      <div class="cal-01-cell cal-01-today cal-01-selected cal-01-weekend">8</div>
      <div class="cal-01-cell">9</div>
      <div class="cal-01-cell">10</div>
      <div class="cal-01-cell">11<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--green"></span></div></div>
      <div class="cal-01-cell">12</div>
      <div class="cal-01-cell">13<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--pink"></span></div></div>
      <div class="cal-01-cell cal-01-weekend">14</div>
      <!-- Week 4 -->
      <div class="cal-01-cell cal-01-weekend">15</div>
      <div class="cal-01-cell">16</div>
      <div class="cal-01-cell">17<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--purple"></span><span class="cal-01-dot cal-01-dot--purple"></span></div></div>
      <div class="cal-01-cell">18</div>
      <div class="cal-01-cell">19</div>
      <div class="cal-01-cell">20<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--pink"></span></div></div>
      <div class="cal-01-cell cal-01-weekend">21</div>
      <!-- Week 5 -->
      <div class="cal-01-cell cal-01-weekend">22</div>
      <div class="cal-01-cell">23<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--green"></span></div></div>
      <div class="cal-01-cell">24</div>
      <div class="cal-01-cell">25<div class="cal-01-dot-row"><span class="cal-01-dot cal-01-dot--purple"></span><span class="cal-01-dot cal-01-dot--pink"></span></div></div>
      <div class="cal-01-cell">26</div>
      <div class="cal-01-cell">27</div>
      <div class="cal-01-cell cal-01-weekend">28</div>
      <!-- Week 6 -->
      <div class="cal-01-cell cal-01-weekend">29</div>
      <div class="cal-01-cell">30</div>
      <div class="cal-01-cell cal-01-other-month">1</div>
      <div class="cal-01-cell cal-01-other-month">2</div>
      <div class="cal-01-cell cal-01-other-month">3</div>
      <div class="cal-01-cell cal-01-other-month">4</div>
      <div class="cal-01-cell cal-01-other-month cal-01-weekend">5</div>
    </div>
  </div>

  <!-- Side Panel -->
  <div class="cal-01-side">

    <div class="cal-01-mini-card cal-01-today-card">
      <div class="cal-01-today-label">Today</div>
      <div class="cal-01-today-date">8</div>
      <div class="cal-01-today-info">Sunday, June 2026</div>
    </div>

    <div class="cal-01-mini-card">
      <div class="cal-01-events-title">Upcoming</div>

      <div class="cal-01-event-item">
        <div class="cal-01-event-stripe" style="background: var(--accent);"></div>
        <div class="cal-01-event-body">
          <div class="cal-01-event-name">Design Review</div>
          <div class="cal-01-event-time">Mon, Jun 9 · 10:00 AM</div>
        </div>
      </div>

      <div class="cal-01-event-item">
        <div class="cal-01-event-stripe" style="background: var(--accent2);"></div>
        <div class="cal-01-event-body">
          <div class="cal-01-event-name">Team Sprint Planning</div>
          <div class="cal-01-event-time">Tue, Jun 10 · 2:00 PM</div>
        </div>
      </div>

      <div class="cal-01-event-item">
        <div class="cal-01-event-stripe" style="background: var(--accent3);"></div>
        <div class="cal-01-event-body">
          <div class="cal-01-event-name">Product Launch</div>
          <div class="cal-01-event-time">Wed, Jun 11 · 9:00 AM</div>
        </div>
      </div>

      <div class="cal-01-event-item">
        <div class="cal-01-event-stripe" style="background: var(--accent);"></div>
        <div class="cal-01-event-body">
          <div class="cal-01-event-name">Quarterly Sync</div>
          <div class="cal-01-event-time">Fri, Jun 13 · 3:30 PM</div>
        </div>
      </div>
    </div>

    <div class="cal-01-mini-card">
      <div class="cal-01-mood-title">Today's Mood</div>
      <div class="cal-01-mood-row">
        <span class="cal-01-mood-btn" title="Great">😄</span>
        <span class="cal-01-mood-btn cal-01-active" title="Good">🙂</span>
        <span class="cal-01-mood-btn" title="Meh">😐</span>
        <span class="cal-01-mood-btn" title="Off">😔</span>
        <span class="cal-01-mood-btn" title="Rough">😩</span>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --bg1: #0f0c29;
  --bg2: #302b63;
  --bg3: #24243e;
  --glass: rgba(255,255,255,0.07);
  --glass-border: rgba(255,255,255,0.15);
  --glass-strong: rgba(255,255,255,0.13);
  --accent: #a78bfa;
  --accent2: #f472b6;
  --accent3: #34d399;
  --text: #f1f5f9;
  --muted: rgba(255,255,255,0.45);
  --today-glow: rgba(167,139,250,0.5);
}

body {
  font-family: 'Outfit', sans-serif;
  background: linear-gradient(135deg, var(--bg1) 0%, var(--bg2) 50%, var(--bg3) 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  overflow: hidden;
  position: relative;
}
/* Animated background orbs */

body::before {
  content: '';
  position: fixed;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(167,139,250,0.25) 0%, transparent 70%);
  top: -100px;
  left: -100px;
  border-radius: 50%;
  animation: cal01-drift 12s ease-in-out infinite alternate;
}

body::after {
  content: '';
  position: fixed;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(244,114,182,0.2) 0%, transparent 70%);
  bottom: -80px;
  right: -80px;
  border-radius: 50%;
  animation: cal01-drift 9s ease-in-out infinite alternate-reverse;
}

@keyframes cal01-drift {
  from {
    transform: translate(0, 0) scale(1);
  }

  to {
    transform: translate(40px, 30px) scale(1.15);
  }
}

@keyframes cal01-pulse {
  0%,
    100% {
    box-shadow: 0 0 20px var(--today-glow), 0 0 40px rgba(167,139,250,0.3);
  }

  50% {
    box-shadow: 0 0 30px var(--today-glow), 0 0 60px rgba(167,139,250,0.5);
  }
}

@keyframes cal01-float {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-6px);
  }
}

@keyframes cal01-shimmer {
  0% {
    background-position: -200% center;
  }

  100% {
    background-position: 200% center;
  }
}

@keyframes cal01-fadein {
  from {
    opacity: 0;
    transform: translateY(16px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.cal-01-scene {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 20px;
  max-width: 860px;
  width: 100%;
  position: relative;
  z-index: 1;
  animation: cal01-fadein 0.8s ease both;
}
/* ── Main Calendar Card ── */

.cal-01-card {
  background: var(--glass);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--glass-border);
  border-radius: 28px;
  padding: 32px;
  box-shadow: 0 32px 64px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.12);
}

.cal-01-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 32px;
}

.cal-01-month-display {
  display: flex;
  flex-direction: column;
}

.cal-01-month-name {
  font-family: 'DM Serif Display', serif;
  font-size: 36px;
  font-style: italic;
  background: linear-gradient(135deg, #fff 0%, var(--accent) 60%, var(--accent2) 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: cal01-shimmer 4s linear infinite;
  line-height: 1;
}

.cal-01-year {
  font-size: 13px;
  font-weight: 500;
  color: var(--muted);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-top: 4px;
}

.cal-01-nav {
  display: flex;
  gap: 8px;
}

.cal-01-nav-btn {
  width: 42px;
  height: 42px;
  background: var(--glass-strong);
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--text);
  font-size: 18px;
  transition: all 0.2s;
  user-select: none;
}

.cal-01-nav-btn:hover {
  background: rgba(167,139,250,0.25);
  border-color: var(--accent);
  transform: scale(1.08);
}
/* Day labels */

.cal-01-days-header {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 10px;
}

.cal-01-day-label {
  text-align: center;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 8px 0;
}
/* Grid */

.cal-01-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
}

.cal-01-cell {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  cursor: pointer;
  position: relative;
  transition: all 0.2s;
  padding-bottom: 6px;
}

.cal-01-cell:hover {
  background: var(--glass-strong);
}

.cal-01-cell.cal-01-other-month {
  color: rgba(255,255,255,0.2);
}

.cal-01-cell.cal-01-today {
  background: linear-gradient(135deg, rgba(167,139,250,0.3), rgba(244,114,182,0.2));
  border: 1px solid rgba(167,139,250,0.5);
  animation: cal01-pulse 2.5s ease-in-out infinite;
  font-weight: 700;
}

.cal-01-cell.cal-01-selected {
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  color: #fff;
  font-weight: 700;
  box-shadow: 0 6px 24px rgba(167,139,250,0.45);
  transform: scale(1.1);
  z-index: 2;
}
/* Event dots */

.cal-01-dot-row {
  display: flex;
  gap: 3px;
  position: absolute;
  bottom: 4px;
}

.cal-01-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
}

.cal-01-dot--purple {
  background: var(--accent);
}

.cal-01-dot--pink {
  background: var(--accent2);
}

.cal-01-dot--green {
  background: var(--accent3);
}
/* Weekend tint */

.cal-01-cell.cal-01-weekend {
  color: rgba(244,114,182,0.8);
}

.cal-01-cell.cal-01-weekend.cal-01-today {
  color: #fff;
}
/* ── Side Panel ── */

.cal-01-side {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.cal-01-mini-card {
  background: var(--glass);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid var(--glass-border);
  border-radius: 22px;
  padding: 22px;
  box-shadow: 0 16px 40px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
}
/* Today's highlight card */

.cal-01-today-card {
  background: linear-gradient(135deg, rgba(167,139,250,0.2), rgba(244,114,182,0.15));
  border-color: rgba(167,139,250,0.35);
  animation: cal01-float 4s ease-in-out infinite;
}

.cal-01-today-label {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.cal-01-today-date {
  font-family: 'DM Serif Display', serif;
  font-size: 52px;
  line-height: 1;
  color: #fff;
  font-style: italic;
}

.cal-01-today-info {
  font-size: 13px;
  color: var(--muted);
  margin-top: 6px;
}
/* Upcoming events */

.cal-01-events-title {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 14px;
}

.cal-01-event-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.cal-01-event-item:last-child {
  border-bottom: none;
}

.cal-01-event-stripe {
  width: 3px;
  height: 36px;
  border-radius: 3px;
  flex-shrink: 0;
  margin-top: 2px;
}

.cal-01-event-body {
  flex: 1;
  min-width: 0;
}

.cal-01-event-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal-01-event-time {
  font-size: 11px;
  color: var(--muted);
  margin-top: 2px;
}
/* Mood tracker mini */

.cal-01-mood-title {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 14px;
}

.cal-01-mood-row {
  display: flex;
  justify-content: space-between;
}

.cal-01-mood-btn {
  font-size: 24px;
  cursor: pointer;
  transition: transform 0.2s;
  filter: grayscale(0.4);
  opacity: 0.7;
}

.cal-01-mood-btn:hover,
.cal-01-mood-btn.cal-01-active {
  transform: scale(1.25);
  filter: grayscale(0);
  opacity: 1;
}

@media (max-width: 680px) {
  .cal-01-scene {
    grid-template-columns: 1fr;
  }

  .cal-01-side {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
    *::before,
    *::after {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
// Cell click selection
document.querySelectorAll('.cal-01-cell:not(.cal-01-other-month)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('.cal-01-cell').forEach(c => c.classList.remove('cal-01-selected'));
    this.classList.add('cal-01-selected');
  });
});
// Mood selection
document.querySelectorAll('.cal-01-mood-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    document.querySelectorAll('.cal-01-mood-btn').forEach(b => b.classList.remove('cal-01-active'));
    this.classList.add('cal-01-active');
  });
});
```
