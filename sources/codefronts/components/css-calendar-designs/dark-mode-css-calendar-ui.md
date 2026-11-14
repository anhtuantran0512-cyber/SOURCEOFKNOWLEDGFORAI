---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/dark-mode-css-calendar-ui/"
title: "Dark Mode CSS Calendar UI"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A premium dark productivity UI with a browser-style chrome bar, CRT scanline overlay and cyan glow accents."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode CSS Calendar UI
Source: https://codefronts.com/components/css-calendar-designs/dark-mode-css-calendar-ui/

A premium dark productivity UI with a browser-style chrome bar, CRT scanline overlay and cyan glow accents. Date cells carry inline color-coded event pills, today pings with a ripple ring, and the right panel holds a schedule, activity heatmap and animated goal bars.
## HTML
```html
<div class="cal-03-scanlines"></div>

<div class="cal-03-shell">

  <!-- Chrome bar -->
  <div class="cal-03-chrome">
    <div class="cal-03-chrome-dots">
      <div class="cal-03-chrome-dot"></div>
      <div class="cal-03-chrome-dot"></div>
      <div class="cal-03-chrome-dot"></div>
    </div>
    <div class="cal-03-chrome-tabs">
      <div class="cal-03-chrome-tab cal-03-active">Month</div>
      <div class="cal-03-chrome-tab">Week</div>
      <div class="cal-03-chrome-tab">Agenda</div>
    </div>
    <div class="cal-03-chrome-right">
      <div class="cal-03-chrome-status">
        <div class="cal-03-status-dot"></div>
        <span>Synced</span>
      </div>
      <span>SUN 08 JUN</span>
    </div>
  </div>

  <!-- Body -->
  <div class="cal-03-body">

    <!-- Calendar Panel -->
    <div class="cal-03-panel">
      <div class="cal-03-head">
        <div class="cal-03-title-group">
          <div class="cal-03-month-title"><span>June</span> 2026</div>
          <div class="cal-03-month-meta">Week 23 of 52 · Q2</div>
        </div>
        <div class="cal-03-controls">
          <div class="cal-03-ctrl-btn">‹</div>
          <div class="cal-03-ctrl-btn cal-03-ctrl-today">Today</div>
          <div class="cal-03-ctrl-btn">›</div>
        </div>
      </div>

      <div class="cal-03-weekdays">
        <div class="cal-03-wd cal-03-weekend">SUN</div>
        <div class="cal-03-wd">MON</div>
        <div class="cal-03-wd">TUE</div>
        <div class="cal-03-wd">WED</div>
        <div class="cal-03-wd">THU</div>
        <div class="cal-03-wd">FRI</div>
        <div class="cal-03-wd cal-03-weekend">SAT</div>
      </div>

      <div class="cal-03-dates" id="cal-03-darkCal">
        <!-- May overflow -->
        <div class="cal-03-date cal-03-dim cal-03-weekend"><div class="cal-03-date-num">25</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">26</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">27</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">28</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">29</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">30</div></div>
        <div class="cal-03-date cal-03-dim cal-03-weekend"><div class="cal-03-date-num">31</div></div>
        <!-- June -->
        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">1</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">2</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-cyan">Workshop</span></div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">3</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">4</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-orange">Deadline</span></div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">5</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">6</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-green">Retro</span></div></div>
        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">7</div></div>

        <div class="cal-03-date cal-03-today cal-03-selected cal-03-weekend"><div class="cal-03-date-num">8</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">9</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-cyan">Sprint</span></div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">10</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">11</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-green">Launch</span></div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">12</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">13</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-purple">Review</span></div></div>
        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">14</div></div>

        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">15</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">16</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">17</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-orange">Demo</span></div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">18</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">19</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">20</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-cyan">1:1</span></div></div>
        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">21</div></div>

        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">22</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">23</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">24</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-purple">Board</span></div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">25</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">26</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">27</div><div class="cal-03-date-events"><span class="cal-03-date-event cal-03-green">EOQ</span></div></div>
        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">28</div></div>

        <div class="cal-03-date cal-03-weekend"><div class="cal-03-date-num">29</div></div>
        <div class="cal-03-date"><div class="cal-03-date-num">30</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">1</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">2</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">3</div></div>
        <div class="cal-03-date cal-03-dim"><div class="cal-03-date-num">4</div></div>
        <div class="cal-03-date cal-03-dim cal-03-weekend"><div class="cal-03-date-num">5</div></div>
      </div>
    </div>

    <!-- Right Panel -->
    <div class="cal-03-right">

      <div class="cal-03-right-section">
        <div class="cal-03-right-label">Selected</div>
        <div class="cal-03-selected-date" id="cal-03-selDate">08</div>
        <div class="cal-03-selected-info" id="cal-03-selInfo">Sunday, June 2026</div>
      </div>

      <div class="cal-03-right-section">
        <div class="cal-03-right-label">Schedule</div>

        <div class="cal-03-schedule-item">
          <div class="cal-03-sch-dot" style="background:var(--cyan);box-shadow:0 0 8px var(--cyan)"></div>
          <div class="cal-03-sch-time">09:00</div>
          <div class="cal-03-sch-body">
            <div class="cal-03-sch-name">Sprint Planning</div>
            <div class="cal-03-sch-sub">1h · Zoom · 8 people</div>
          </div>
        </div>

        <div class="cal-03-schedule-item">
          <div class="cal-03-sch-dot" style="background:var(--orange);box-shadow:0 0 8px var(--orange)"></div>
          <div class="cal-03-sch-time">14:00</div>
          <div class="cal-03-sch-body">
            <div class="cal-03-sch-name">Design Review</div>
            <div class="cal-03-sch-sub">45m · Figma share</div>
          </div>
        </div>

        <div class="cal-03-schedule-item">
          <div class="cal-03-sch-dot" style="background:var(--green);box-shadow:0 0 8px var(--green)"></div>
          <div class="cal-03-sch-time">16:30</div>
          <div class="cal-03-sch-body">
            <div class="cal-03-sch-name">Client Call</div>
            <div class="cal-03-sch-sub">30m · Recurring</div>
          </div>
        </div>

        <div class="cal-03-schedule-item">
          <div class="cal-03-sch-dot" style="background:var(--purple);box-shadow:0 0 8px var(--purple)"></div>
          <div class="cal-03-sch-time">18:00</div>
          <div class="cal-03-sch-body">
            <div class="cal-03-sch-name">Team Retro</div>
            <div class="cal-03-sch-sub">1h · All hands</div>
          </div>
        </div>
      </div>

      <div class="cal-03-right-section">
        <div class="cal-03-right-label">Activity</div>
        <div class="cal-03-heatmap-grid">
          <div class="cal-03-heat-cell cal-03-h1"></div><div class="cal-03-heat-cell cal-03-h3"></div><div class="cal-03-heat-cell cal-03-h2"></div>
          <div class="cal-03-heat-cell cal-03-h4"></div><div class="cal-03-heat-cell cal-03-h1"></div><div class="cal-03-heat-cell cal-03-h2"></div>
          <div class="cal-03-heat-cell"></div><div class="cal-03-heat-cell cal-03-h3"></div><div class="cal-03-heat-cell cal-03-h2"></div>
          <div class="cal-03-heat-cell cal-03-h1"></div><div class="cal-03-heat-cell cal-03-h4"></div><div class="cal-03-heat-cell cal-03-h2"></div>
          <div class="cal-03-heat-cell cal-03-h2"></div><div class="cal-03-heat-cell"></div><div class="cal-03-heat-cell cal-03-h3"></div>
          <div class="cal-03-heat-cell cal-03-h1"></div><div class="cal-03-heat-cell cal-03-h2"></div><div class="cal-03-heat-cell cal-03-h4"></div>
          <div class="cal-03-heat-cell cal-03-h3"></div><div class="cal-03-heat-cell cal-03-h1"></div><div class="cal-03-heat-cell"></div>
          <div class="cal-03-heat-cell cal-03-h2"></div><div class="cal-03-heat-cell cal-03-h3"></div><div class="cal-03-heat-cell cal-03-h1"></div>
        </div>
      </div>

      <div class="cal-03-right-section">
        <div class="cal-03-right-label">Goals</div>
        <div class="cal-03-progress-item">
          <div class="cal-03-progress-head">
            <span class="cal-03-progress-name">Meetings</span>
            <span class="cal-03-progress-val">8/12</span>
          </div>
          <div class="cal-03-progress-track">
            <div class="cal-03-progress-fill" style="width:66%;background:var(--cyan);animation-delay:0.1s"></div>
          </div>
        </div>
        <div class="cal-03-progress-item">
          <div class="cal-03-progress-head">
            <span class="cal-03-progress-name">Deliverables</span>
            <span class="cal-03-progress-val">4/7</span>
          </div>
          <div class="cal-03-progress-track">
            <div class="cal-03-progress-fill" style="width:57%;background:var(--green);animation-delay:0.2s"></div>
          </div>
        </div>
        <div class="cal-03-progress-item">
          <div class="cal-03-progress-head">
            <span class="cal-03-progress-name">Month</span>
            <span class="cal-03-progress-val">27%</span>
          </div>
          <div class="cal-03-progress-track">
            <div class="cal-03-progress-fill" style="width:27%;background:var(--purple);animation-delay:0.3s"></div>
          </div>
        </div>
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
  --bg: #0a0a0f;
  --surface: #111118;
  --surface2: #181824;
  --surface3: #1e1e2e;
  --border: rgba(255,255,255,0.07);
  --border2: rgba(255,255,255,0.12);
  --text: #e8e8f0;
  --muted: rgba(232,232,240,0.4);
  --dim: rgba(232,232,240,0.15);
  --cyan: #00d4ff;
  --green: #00ff94;
  --orange: #ff6b35;
  --purple: #b347ff;
  --pink: #ff4da6;
  --glow-cyan: rgba(0,212,255,0.18);
  --glow-green: rgba(0,255,148,0.15);
}

body {
  font-family: 'Syne', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  overflow: hidden;
}
/* Ambient background glow */

body::before {
  content: '';
  position: fixed;
  width: 600px;
  height: 600px;
  background: radial-gradient(ellipse at center, rgba(0,212,255,0.05) 0%, transparent 65%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

@keyframes cal03-glow-pulse {
  0%,
    100% {
    opacity: 0.6;
  }

  50% {
    opacity: 1;
  }
}

@keyframes cal03-scan {
  0% {
    transform: translateY(-100%);
  }

  100% {
    transform: translateY(100vh);
  }
}

@keyframes cal03-enter {
  from {
    opacity: 0;
    transform: scale(0.96);
  }

  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes cal03-bar-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

@keyframes cal03-ping {
  0% {
    transform: scale(1);
    opacity: 1;
  }

  80%,
    100% {
    transform: scale(2);
    opacity: 0;
  }
}

@keyframes cal03-slide-up {
  from {
    transform: translateY(10px);
    opacity: 0;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}
/* CRT scanline effect */

.cal-03-scanlines {
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,0,0,0.03) 2px,
      rgba(0,0,0,0.03) 4px
    );
  pointer-events: none;
  z-index: 100;
}

.cal-03-shell {
  max-width: 900px;
  width: 100%;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 0;
  background: var(--surface);
  border: 1px solid var(--border2);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 0 0 1px rgba(0,212,255,0.08), 0 40px 80px rgba(0,0,0,0.6), 0 0 60px rgba(0,212,255,0.06);
  animation: cal03-enter 0.6s cubic-bezier(0.22,1,0.36,1) both;
  position: relative;
  z-index: 1;
}
/* ── Top Chrome Bar ── */

.cal-03-chrome {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 20px;
  background: var(--surface2);
  border-bottom: 1px solid var(--border);
}

.cal-03-chrome-dots {
  display: flex;
  gap: 6px;
}

.cal-03-chrome-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.cal-03-chrome-dot:nth-child(1) {
  background: #ff5f56;
}

.cal-03-chrome-dot:nth-child(2) {
  background: #febc2e;
}

.cal-03-chrome-dot:nth-child(3) {
  background: #28c840;
}

.cal-03-chrome-tabs {
  display: flex;
  gap: 2px;
  flex: 1;
}

.cal-03-chrome-tab {
  padding: 6px 16px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  border-radius: 6px;
  cursor: pointer;
  color: var(--muted);
  transition: all 0.2s;
}

.cal-03-chrome-tab:hover {
  color: var(--text);
  background: var(--border);
}

.cal-03-chrome-tab.cal-03-active {
  color: var(--cyan);
  background: rgba(0,212,255,0.08);
  border-bottom: 2px solid var(--cyan);
  border-radius: 6px 6px 0 0;
}

.cal-03-chrome-right {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--muted);
  display: flex;
  gap: 14px;
  align-items: center;
}

.cal-03-chrome-status {
  display: flex;
  align-items: center;
  gap: 5px;
}

.cal-03-status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 8px var(--green);
  animation: cal03-glow-pulse 2s ease-in-out infinite;
}
/* ── Body Layout ── */

.cal-03-body {
  display: grid;
  grid-template-columns: 1fr 280px;
}
/* ── Calendar Panel ── */

.cal-03-panel {
  padding: 28px;
  border-right: 1px solid var(--border);
}

.cal-03-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.cal-03-title-group {
  display: flex;
  flex-direction: column;
}

.cal-03-month-title {
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--text);
  line-height: 1;
}

.cal-03-month-title span {
  color: var(--cyan);
  text-shadow: 0 0 20px rgba(0,212,255,0.5);
}

.cal-03-month-meta {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 0.15em;
  margin-top: 5px;
}

.cal-03-controls {
  display: flex;
  gap: 6px;
  align-items: center;
}

.cal-03-ctrl-btn {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: var(--surface3);
  border: 1px solid var(--border2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--text);
  font-size: 16px;
  transition: all 0.2s;
  user-select: none;
}

.cal-03-ctrl-btn:hover {
  border-color: var(--cyan);
  color: var(--cyan);
  background: rgba(0,212,255,0.06);
}

.cal-03-ctrl-today {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0 12px;
  width: auto;
  color: var(--cyan);
  border-color: rgba(0,212,255,0.3);
}
/* Weekday headers */

.cal-03-weekdays {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 8px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}

.cal-03-wd {
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--dim);
  padding: 6px 0;
}

.cal-03-wd.cal-03-weekend {
  color: rgba(179,71,255,0.6);
}
/* Date cells */

.cal-03-dates {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 3px;
}

.cal-03-date {
  min-height: 64px;
  border-radius: 10px;
  padding: 9px;
  cursor: pointer;
  position: relative;
  transition: all 0.15s;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.cal-03-date:hover {
  background: var(--surface3);
}

.cal-03-date.cal-03-dim {
  opacity: 0.25;
  pointer-events: none;
}

.cal-03-date.cal-03-today {
  background: linear-gradient(135deg, rgba(0,212,255,0.12), rgba(179,71,255,0.08));
  border: 1px solid rgba(0,212,255,0.3);
}

.cal-03-date.cal-03-today::after {
  content: '';
  position: absolute;
  top: 8px;
  right: 8px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--cyan);
  box-shadow: 0 0 0 rgba(0,212,255,0.4);
  animation: cal03-ping 2s cubic-bezier(0,0,0.2,1) infinite;
}

.cal-03-date.cal-03-selected {
  background: rgba(0,212,255,0.12);
  border: 1px solid var(--cyan);
  box-shadow: 0 0 20px rgba(0,212,255,0.15);
}

.cal-03-date-num {
  font-weight: 700;
  font-size: 15px;
  color: var(--text);
  line-height: 1;
}

.cal-03-date.cal-03-today .cal-03-date-num {
  color: var(--cyan);
}

.cal-03-date.cal-03-weekend .cal-03-date-num {
  color: rgba(179,71,255,0.8);
}
/* Tiny event pills in cell */

.cal-03-date-events {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.cal-03-date-event {
  font-family: 'JetBrains Mono', monospace;
  font-size: 8px;
  font-weight: 500;
  padding: 2px 5px;
  border-radius: 3px;
  letter-spacing: 0.03em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal-03-date-event.cal-03-cyan {
  background: rgba(0,212,255,0.15);
  color: var(--cyan);
}

.cal-03-date-event.cal-03-green {
  background: rgba(0,255,148,0.1);
  color: var(--green);
}

.cal-03-date-event.cal-03-orange {
  background: rgba(255,107,53,0.15);
  color: var(--orange);
}

.cal-03-date-event.cal-03-purple {
  background: rgba(179,71,255,0.15);
  color: var(--purple);
}
/* ── Right Panel ── */

.cal-03-right {
  display: flex;
  flex-direction: column;
  background: var(--surface2);
}

.cal-03-right-section {
  padding: 22px 20px;
  border-bottom: 1px solid var(--border);
}

.cal-03-right-section:last-child {
  border-bottom: none;
  flex: 1;
}

.cal-03-right-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.cal-03-right-label::before {
  content: '';
  width: 3px;
  height: 10px;
  background: var(--cyan);
  border-radius: 2px;
  box-shadow: 0 0 8px var(--cyan);
}
/* Selected date info */

.cal-03-selected-date {
  font-size: 48px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--text);
  line-height: 1;
  animation: cal03-slide-up 0.3s ease;
}

.cal-03-selected-info {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--muted);
  margin-top: 6px;
}
/* Schedule list */

.cal-03-schedule-item {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  margin-bottom: 12px;
  animation: cal03-slide-up 0.3s ease both;
}

.cal-03-schedule-item:nth-child(2) {
  animation-delay: 0.05s;
}

.cal-03-schedule-item:nth-child(3) {
  animation-delay: 0.1s;
}

.cal-03-schedule-item:nth-child(4) {
  animation-delay: 0.15s;
}

.cal-03-sch-time {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: var(--muted);
  width: 38px;
  flex-shrink: 0;
  padding-top: 2px;
}

.cal-03-sch-body {
  flex: 1;
  min-width: 0;
}

.cal-03-sch-name {
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal-03-sch-sub {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: var(--muted);
  margin-top: 2px;
}

.cal-03-sch-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 4px;
}
/* Heatmap mini */

.cal-03-heatmap-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 3px;
  margin-top: 4px;
}

.cal-03-heat-cell {
  aspect-ratio: 1;
  border-radius: 3px;
  background: var(--surface3);
  transition: background 0.2s;
}

.cal-03-heat-cell.cal-03-h1 {
  background: rgba(0,212,255,0.2);
}

.cal-03-heat-cell.cal-03-h2 {
  background: rgba(0,212,255,0.4);
}

.cal-03-heat-cell.cal-03-h3 {
  background: rgba(0,212,255,0.65);
}

.cal-03-heat-cell.cal-03-h4 {
  background: var(--cyan);
  box-shadow: 0 0 8px rgba(0,212,255,0.4);
}
/* Progress bars */

.cal-03-progress-item {
  margin-bottom: 12px;
}

.cal-03-progress-head {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  margin-bottom: 5px;
}

.cal-03-progress-name {
  font-weight: 600;
  color: var(--text);
}

.cal-03-progress-val {
  font-family: 'JetBrains Mono', monospace;
  color: var(--muted);
}

.cal-03-progress-track {
  height: 4px;
  background: var(--surface3);
  border-radius: 2px;
  overflow: hidden;
}

.cal-03-progress-fill {
  height: 100%;
  border-radius: 2px;
  transform-origin: left;
  animation: cal03-bar-fill 1s cubic-bezier(0.22,1,0.36,1) both;
}

@media (max-width: 700px) {
  .cal-03-body {
    grid-template-columns: 1fr;
  }

  .cal-03-right {
    display: none;
  }

  .cal-03-date {
    min-height: 50px;
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
const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

document.querySelectorAll('#cal-03-darkCal .cal-03-date:not(.cal-03-dim)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal-03-darkCal .cal-03-date').forEach(c => c.classList.remove('cal-03-selected'));
    this.classList.add('cal-03-selected');
    const num = parseInt(this.querySelector('.cal-03-date-num').textContent);
    document.getElementById('cal-03-selDate').textContent = String(num).padStart(2,'0');
  });
});
```
