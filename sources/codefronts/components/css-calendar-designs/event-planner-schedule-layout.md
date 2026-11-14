---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/event-planner-schedule-layout/"
title: "Event Planner & Schedule Layout"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A dense event planner where each date cell anchors layered events via position:relative: an absolute count badge, a flex stack of color-coded event blocks…"
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Event Planner & Schedule Layout
Source: https://codefronts.com/components/css-calendar-designs/event-planner-schedule-layout/

A dense event planner where each date cell anchors layered events via position:relative: an absolute count badge, a flex stack of color-coded event blocks with ::before accent bars, and a +N more overflow. Sidebar shows a time-blocked agenda and a counted legend.
## HTML
```html
<div class="cal09">
  <div class="cal09__shell">

    <!-- Toolbar -->
    <div class="cal09__toolbar">
      <div class="cal09__toolbar-left">
        <div class="cal09__title">June 2026</div>
        <div class="cal09__title-badge">Event Planner</div>
      </div>
      <div class="cal09__toolbar-right">
        <div class="cal09__view-btn active">Month</div>
        <div class="cal09__view-btn">Week</div>
        <div class="cal09__view-btn">Agenda</div>
        <div class="cal09__nav-group">
          <div class="cal09__nav-b">←</div>
          <div class="cal09__nav-b">→</div>
        </div>
      </div>
    </div>

    <!-- Body -->
    <div class="cal09__body">

      <!-- Calendar panel -->
      <div class="cal09__cal-panel">

        <div class="cal09__dow">
          <div class="cal09__dw wkend">Sun</div>
          <div class="cal09__dw">Mon</div>
          <div class="cal09__dw">Tue</div>
          <div class="cal09__dw">Wed</div>
          <div class="cal09__dw">Thu</div>
          <div class="cal09__dw">Fri</div>
          <div class="cal09__dw wkend">Sat</div>
        </div>

        <div class="cal09__grid" id="cal09Grid">

          <!-- Row 1: May overflow -->
          <div class="cal09__cell other wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">25</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">26</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">27</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">28</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">29</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">30</div></div></div>
          <div class="cal09__cell other wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">31</div></div></div>

          <!-- Row 2: Jun 1-7 -->
          <div class="cal09__cell wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">1</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">2</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--g">1</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--green"><div class="cal09__ev-dot" style="background:var(--green)"></div>Design Sprint</div>
            </div>
          </div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">3</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">4</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--a">2</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--amber"><div class="cal09__ev-dot" style="background:var(--amber)"></div>Holiday</div>
              <div class="cal09__ev cal09__ev--sky"><div class="cal09__ev-dot" style="background:var(--sky)"></div>BBQ</div>
            </div>
          </div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">5</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">6</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--g">1</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--lime"><div class="cal09__ev-dot" style="background:var(--lime)"></div>Deadline</div>
            </div>
          </div>
          <div class="cal09__cell wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">7</div></div></div>

          <!-- Row 3: Jun 8-14 (today = 8) -->
          <div class="cal09__cell today wkend">
            <div class="cal09__cell-top"><div class="cal09__cell-n">8</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--g">1</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--green"><div class="cal09__ev-dot" style="background:var(--green)"></div>Today</div>
            </div>
          </div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">9</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--a">2</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--sky"><div class="cal09__ev-dot" style="background:var(--sky)"></div>Sprint Plan</div>
              <div class="cal09__ev cal09__ev--violet"><div class="cal09__ev-dot" style="background:var(--violet)"></div>1:1 w/ Sam</div>
            </div>
          </div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">10</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">11</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--r">3</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--rose"><div class="cal09__ev-dot" style="background:var(--rose)"></div>🚀 Launch</div>
              <div class="cal09__ev cal09__ev--amber"><div class="cal09__ev-dot" style="background:var(--amber)"></div>Deadline</div>
              <div class="cal09__more">+1 more</div>
            </div>
          </div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">12</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">13</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--g">2</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--lime"><div class="cal09__ev-dot" style="background:var(--lime)"></div>Review</div>
              <div class="cal09__ev cal09__ev--sand"><div class="cal09__ev-dot" style="background:var(--sand)"></div>Lunch</div>
            </div>
          </div>
          <div class="cal09__cell wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">14</div></div></div>

          <!-- Row 4: Jun 15-21 -->
          <div class="cal09__cell wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">15</div></div></div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">16</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">17</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--a">3</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--amber"><div class="cal09__ev-dot" style="background:var(--amber)"></div>Demo Day</div>
              <div class="cal09__ev cal09__ev--violet"><div class="cal09__ev-dot" style="background:var(--violet)"></div>Q2 Report</div>
              <div class="cal09__more">+1 more</div>
            </div>
          </div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">18</div></div></div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">19</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">20</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--g">1</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--green"><div class="cal09__ev-dot" style="background:var(--green)"></div>Board Mtg</div>
            </div>
          </div>
          <div class="cal09__cell wkend">
            <div class="cal09__cell-top"><div class="cal09__cell-n">21</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--a">1</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--sand"><div class="cal09__ev-dot" style="background:var(--sand)"></div>Summer!</div>
            </div>
          </div>

          <!-- Row 5: Jun 22-28 -->
          <div class="cal09__cell wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">22</div></div></div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">23</div></div></div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">24</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">25</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--g">2</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--sky"><div class="cal09__ev-dot" style="background:var(--sky)"></div>Planning</div>
              <div class="cal09__ev cal09__ev--lime"><div class="cal09__ev-dot" style="background:var(--lime)"></div>Team Dinner</div>
            </div>
          </div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">26</div></div></div>
          <div class="cal09__cell">
            <div class="cal09__cell-top"><div class="cal09__cell-n">27</div></div>
            <div class="cal09__cell-badge cal09__cell-badge--g">1</div>
            <div class="cal09__cell-events">
              <div class="cal09__ev cal09__ev--green"><div class="cal09__ev-dot" style="background:var(--green)"></div>Retro</div>
            </div>
          </div>
          <div class="cal09__cell wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">28</div></div></div>

          <!-- Row 6: Jun 29-30 + July overflow -->
          <div class="cal09__cell wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">29</div></div></div>
          <div class="cal09__cell"><div class="cal09__cell-top"><div class="cal09__cell-n">30</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">1</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">2</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">3</div></div></div>
          <div class="cal09__cell other"><div class="cal09__cell-top"><div class="cal09__cell-n">4</div></div></div>
          <div class="cal09__cell other wkend"><div class="cal09__cell-top"><div class="cal09__cell-n">5</div></div></div>

        </div>
      </div>

      <!-- Sidebar -->
      <div class="cal09__sidebar">

        <div class="cal09__sb-card">
          <div class="cal09__sb-lbl">Today</div>
          <div class="cal09__today-date" id="cal09BigDate">08</div>
          <div class="cal09__today-info">Sunday, June 2026</div>
        </div>

        <div class="cal09__sb-card">
          <div class="cal09__sb-lbl">Today's Agenda</div>
          <div class="cal09__agenda-item">
            <div class="cal09__ag-time">09:00</div>
            <div class="cal09__ag-body">
              <div class="cal09__ag-name">Sprint Planning</div>
              <div class="cal09__ag-meta">Zoom · 1h</div>
              <div class="cal09__ag-tag" style="background:rgba(90,180,212,0.12);color:var(--sky)">● Team</div>
            </div>
          </div>
          <div class="cal09__agenda-item">
            <div class="cal09__ag-time">14:00</div>
            <div class="cal09__ag-body">
              <div class="cal09__ag-name">Product Launch</div>
              <div class="cal09__ag-meta">All-hands · 2h</div>
              <div class="cal09__ag-tag" style="background:rgba(224,88,112,0.12);color:var(--rose)">● Critical</div>
            </div>
          </div>
          <div class="cal09__agenda-item">
            <div class="cal09__ag-time">17:30</div>
            <div class="cal09__ag-body">
              <div class="cal09__ag-name">Design Review</div>
              <div class="cal09__ag-meta">Figma share · 45m</div>
              <div class="cal09__ag-tag" style="background:rgba(76,175,125,0.12);color:var(--green)">● Design</div>
            </div>
          </div>
        </div>

        <div class="cal09__sb-card">
          <div class="cal09__sb-lbl">Event Legend</div>
          <div class="cal09__legend">
            <div class="cal09__legend-row"><div class="cal09__legend-swatch" style="background:var(--green)"></div>Team & sprints<span class="cal09__legend-count">5</span></div>
            <div class="cal09__legend-row"><div class="cal09__legend-swatch" style="background:var(--rose)"></div>Critical / launches<span class="cal09__legend-count">3</span></div>
            <div class="cal09__legend-row"><div class="cal09__legend-swatch" style="background:var(--amber)"></div>Deadlines<span class="cal09__legend-count">4</span></div>
            <div class="cal09__legend-row"><div class="cal09__legend-swatch" style="background:var(--sky)"></div>Meetings<span class="cal09__legend-count">6</span></div>
            <div class="cal09__legend-row"><div class="cal09__legend-swatch" style="background:var(--violet)"></div>1:1s<span class="cal09__legend-count">2</span></div>
            <div class="cal09__legend-row"><div class="cal09__legend-swatch" style="background:var(--sand)"></div>Social<span class="cal09__legend-count">3</span></div>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.cal09,
.cal09 *,
.cal09 *::before,
.cal09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal09 ::selection {
  background: #2d4a3e;
  color: #fff;
}

.cal09 {
  --bg: #1a1f1c;
  --surface: #222820;
  --card: #262d24;
  --card2: #2d3529;
  --border: rgba(255,255,255,0.07);
  --border2: rgba(255,255,255,0.12);
  --text: #e8ede4;
  --text2: #8fa888;
  --text3: #4a574a;
  --green: #4caf7d;
  --lime: #97c95c;
  --amber: #e8a23a;
  --rose: #e05870;
  --sky: #5ab4d4;
  --violet: #a07dd4;
  --sand: #d4b87a;
  font-family: 'Space Grotesk', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 36px 20px;
  color: var(--text);
  position: relative;
  overflow-x: hidden;
}
/* Subtle grid pattern background */

.cal09::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: linear-gradient(rgba(76,175,125,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(76,175,125,0.03) 1px, transparent 1px);
  background-size: 28px 28px;
  pointer-events: none;
  z-index: 0;
}

@keyframes cal09-in {
  from {
    opacity: 0;
    transform: translateY(14px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes cal09-badge-pop {
  from {
    transform: scale(0.7);
    opacity: 0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes cal09-event-slide {
  from {
    transform: translateX(-6px);
    opacity: 0;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes cal09-today-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(76,175,125,0.5);
  }

  50% {
    box-shadow: 0 0 0 5px rgba(76,175,125,0);
  }
}

.cal09__shell {
  position: relative;
  z-index: 1;
  max-width: 980px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
  animation: cal09-in 0.5s ease both;
}
/* ── Top toolbar ── */

.cal09__toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 4px;
}

.cal09__toolbar-left {
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.cal09__title {
  font-family: 'Libre Baskerville', serif;
  font-style: italic;
  font-size: 36px;
  color: var(--text);
  line-height: 1;
}

.cal09__title-badge {
  font-family: 'Space Grotesk', sans-serif;
  font-style: normal;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--green);
  background: rgba(76,175,125,0.12);
  border: 1px solid rgba(76,175,125,0.25);
  padding: 4px 10px;
  border-radius: 20px;
  animation: cal09-badge-pop 0.4s cubic-bezier(0.34,1.56,0.64,1) 0.3s both;
}

.cal09__toolbar-right {
  display: flex;
  gap: 8px;
  align-items: center;
}

.cal09__view-btn {
  padding: 7px 16px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: all 0.15s;
  user-select: none;
  background: var(--card);
  border: 1px solid var(--border2);
  color: var(--text2);
}

.cal09__view-btn:hover {
  border-color: var(--green);
  color: var(--green);
}

.cal09__view-btn.active {
  background: rgba(76,175,125,0.15);
  border-color: var(--green);
  color: var(--green);
}

.cal09__nav-group {
  display: flex;
  border: 1px solid var(--border2);
  border-radius: 8px;
  overflow: hidden;
}

.cal09__nav-b {
  padding: 7px 12px;
  font-size: 15px;
  cursor: pointer;
  color: var(--text2);
  border-right: 1px solid var(--border2);
  transition: all 0.15s;
  user-select: none;
}

.cal09__nav-b:last-child {
  border-right: none;
}

.cal09__nav-b:hover {
  background: var(--card2);
  color: var(--green);
}
/* ── Body: 2-col layout ── */

.cal09__body {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 14px;
}
/* ── Calendar grid panel ── */

.cal09__cal-panel {
  background: var(--card);
  border: 1px solid var(--border2);
  border-radius: 20px;
  overflow: hidden;
}
/* DOW headers */

.cal09__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  border-bottom: 1px solid var(--border);
  padding: 0;
}

.cal09__dw {
  padding: 12px 10px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text3);
  text-align: center;
  border-right: 1px solid var(--border);
}

.cal09__dw:last-child {
  border-right: none;
}

.cal09__dw.wkend {
  color: var(--green);
  opacity: 0.6;
}
/* ── The Event Planner Grid — THE CORE TECHNIQUE ──
   Each cell uses:
   - display: grid / flex for inner layout
   - position: relative for absolute-positioned event blocks
   - Nested grids for multi-event day layouts
   - CSS absolute positioning for spanning events
   - z-index layers for overlapping badges
   ── */

.cal09__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: minmax(110px, auto);
}

.cal09__cell {
  border-right: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: 8px 6px 6px;
  position: relative;
  /* ← enables absolute event blocks */
  transition: background 0.15s;
  display: flex;
  flex-direction: column;
  gap: 4px;
  cursor: pointer;
}

.cal09__cell:nth-child(7n) {
  border-right: none;
}

.cal09__cell:hover {
  background: var(--card2);
}

.cal09__cell.other {
  opacity: 0.2;
  pointer-events: none;
}

.cal09__cell-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.cal09__cell-n {
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  line-height: 1;
  font-family: 'Libre Baskerville', serif;
  transition: all 0.15s;
}

.cal09__cell.wkend .cal09__cell-n {
  color: var(--green);
  opacity: 0.8;
}
/* Today */

.cal09__cell.today {
  background: rgba(76,175,125,0.06);
  border-color: rgba(76,175,125,0.2);
}

.cal09__cell.today .cal09__cell-n {
  background: var(--green);
  color: #0d1a12;
  animation: cal09-today-pulse 2.5s ease-in-out infinite;
}

.cal09__cell.selected {
  background: rgba(76,175,125,0.08);
}

.cal09__cell.selected .cal09__cell-n {
  background: var(--card2);
  border: 2px solid var(--green);
  color: var(--green);
}
/* Event count badge — top right, absolutely positioned */

.cal09__cell-badge {
  position: absolute;
  top: 8px;
  right: 6px;
  min-width: 18px;
  height: 18px;
  border-radius: 9px;
  font-size: 9px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 5px;
  animation: cal09-badge-pop 0.3s cubic-bezier(0.34,1.56,0.64,1) both;
}

.cal09__cell-badge--g {
  background: rgba(76,175,125,0.25);
  color: var(--green);
}

.cal09__cell-badge--a {
  background: rgba(232,162,58,0.25);
  color: var(--amber);
}

.cal09__cell-badge--r {
  background: rgba(224,88,112,0.2);
  color: var(--rose);
}
/* ── Event blocks inside cells ──
   Technique 1: stacked flex column (normal flow)
   Technique 2: absolute positioned for "spanning" look
   Technique 3: color-coded left border + bg
   ── */

.cal09__cell-events {
  display: flex;
  flex-direction: column;
  gap: 3px;
  margin-top: 4px;
  flex: 1;
}

.cal09__ev {
  padding: 3px 6px 3px 8px;
  border-radius: 5px;
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: 0.02em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  position: relative;
  animation: cal09-event-slide 0.3s ease both;
  cursor: default;
  display: flex;
  align-items: center;
  gap: 5px;
}
/* Left accent bar via ::before */

.cal09__ev::before {
  content: '';
  position: absolute;
  left: 0;
  top: 2px;
  bottom: 2px;
  width: 3px;
  border-radius: 2px;
}
/* Color variants */

.cal09__ev--green {
  background: rgba(76,175,125,0.12);
  color: var(--green);
}

.cal09__ev--green::before {
  background: var(--green);
}

.cal09__ev--amber {
  background: rgba(232,162,58,0.12);
  color: var(--amber);
}

.cal09__ev--amber::before {
  background: var(--amber);
}

.cal09__ev--rose {
  background: rgba(224,88,112,0.12);
  color: var(--rose);
}

.cal09__ev--rose::before {
  background: var(--rose);
}

.cal09__ev--sky {
  background: rgba(90,180,212,0.12);
  color: var(--sky);
}

.cal09__ev--sky::before {
  background: var(--sky);
}

.cal09__ev--violet {
  background: rgba(160,125,212,0.12);
  color: var(--violet);
}

.cal09__ev--violet::before {
  background: var(--violet);
}

.cal09__ev--lime {
  background: rgba(151,201,92,0.12);
  color: var(--lime);
}

.cal09__ev--lime::before {
  background: var(--lime);
}

.cal09__ev--sand {
  background: rgba(212,184,122,0.12);
  color: var(--sand);
}

.cal09__ev--sand::before {
  background: var(--sand);
}
/* Event dot icon */

.cal09__ev-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  flex-shrink: 0;
}
/* "+N more" overflow badge — absolutely placed bottom */

.cal09__more {
  font-size: 9px;
  font-weight: 600;
  color: var(--text3);
  letter-spacing: 0.06em;
  padding: 2px 6px;
  text-align: right;
  cursor: pointer;
  margin-top: auto;
}

.cal09__more:hover {
  color: var(--green);
}
/* ── Right sidebar ── */

.cal09__sidebar {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cal09__sb-card {
  background: var(--card);
  border: 1px solid var(--border2);
  border-radius: 16px;
  padding: 18px;
}

.cal09__sb-lbl {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--text3);
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.cal09__sb-lbl::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}
/* Today summary */

.cal09__today-date {
  font-family: 'Libre Baskerville', serif;
  font-style: italic;
  font-size: 56px;
  color: var(--green);
  line-height: 1;
}

.cal09__today-info {
  font-size: 12px;
  color: var(--text3);
  margin-top: 4px;
}
/* Agenda list — time-blocked */

.cal09__agenda-item {
  display: grid;
  grid-template-columns: 38px auto;
  gap: 10px;
  align-items: start;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
  animation: cal09-event-slide 0.3s ease both;
}

.cal09__agenda-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.cal09__agenda-item:nth-child(2) {
  animation-delay: 0.07s;
}

.cal09__agenda-item:nth-child(3) {
  animation-delay: 0.14s;
}

.cal09__agenda-item:nth-child(4) {
  animation-delay: 0.21s;
}

.cal09__ag-time {
  font-size: 10px;
  color: var(--text3);
  font-weight: 600;
  letter-spacing: 0.04em;
  padding-top: 3px;
}

.cal09__ag-body {
}

.cal09__ag-name {
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cal09__ag-meta {
  font-size: 10px;
  color: var(--text3);
  margin-top: 2px;
}

.cal09__ag-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 9px;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: 10px;
  margin-top: 5px;
  letter-spacing: 0.04em;
}
/* Legend */

.cal09__legend {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.cal09__legend-row {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  color: var(--text2);
}

.cal09__legend-swatch {
  width: 12px;
  height: 4px;
  border-radius: 2px;
  flex-shrink: 0;
}

.cal09__legend-count {
  margin-left: auto;
  font-size: 10px;
  color: var(--text3);
  font-weight: 600;
}

@media (max-width: 780px) {
  .cal09__body {
    grid-template-columns: 1fr;
  }

  .cal09__sidebar {
    display: none;
  }

  .cal09__cell {
    min-height: 80px;
  }
}

@media (max-width: 480px) {
  .cal09__title {
    font-size: 26px;
  }

  .cal09__cell {
    padding: 5px 4px;
    min-height: 60px;
  }

  .cal09__cell-n {
    font-size: 12px;
    width: 22px;
    height: 22px;
  }

  .cal09__ev {
    font-size: 8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal09 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
document.querySelectorAll('#cal09Grid .cal09__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal09Grid .cal09__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
    const n = this.querySelector('.cal09__cell-n');
    if (n) document.getElementById('cal09BigDate').textContent = n.textContent.padStart(2,'0');
  });
});
```
