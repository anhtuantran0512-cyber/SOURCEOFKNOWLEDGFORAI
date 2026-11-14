---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/dark-mode-calendar-design/"
title: "Dark Mode Calendar Design"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "Luxury obsidian calendar whose entire theme lives in CSS variables."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Calendar Design
Source: https://codefronts.com/components/css-calendar-designs/dark-mode-calendar-design/

Luxury obsidian calendar whose entire theme lives in CSS variables. A single data-theme toggle swaps all 15 variables between dark and light with no extra selectors. Instrument Serif month, gold accents, today ring pulse, and a sidebar event list plus sparkline.
## HTML
```html
<div class="cal08" id="cal08Root">

  <div class="cal08__shell">

    <!-- Main calendar -->
    <div class="cal08__main">
      <div class="cal08__header">
        <div class="cal08__header-left">
          <div class="cal08__month-big">J<em>une</em></div>
          <div class="cal08__header-meta">
            <span class="cal08__meta-item">2026</span>
            <div class="cal08__meta-dot"></div>
            <span class="cal08__meta-item">Q2</span>
            <div class="cal08__meta-dot"></div>
            <span class="cal08__meta-item">Week 23</span>
          </div>
        </div>
        <div class="cal08__header-right">
          <div class="cal08__nav">
            <div class="cal08__nav-btn">←</div>
            <div class="cal08__nav-btn">→</div>
          </div>
          <!-- Theme toggle — pure CSS vars swap -->
          <div class="cal08__theme-toggle" id="cal08Toggle">
            <span class="cal08__toggle-icon" id="cal08Icon">☽</span>
            <span id="cal08ThemeLabel">Dark</span>
          </div>
        </div>
      </div>

      <div class="cal08__dow">
        <div class="cal08__dw">Sun</div><div class="cal08__dw">Mon</div>
        <div class="cal08__dw">Tue</div><div class="cal08__dw">Wed</div>
        <div class="cal08__dw">Thu</div><div class="cal08__dw">Fri</div>
        <div class="cal08__dw">Sat</div>
      </div>

      <div class="cal08__grid" id="cal08Grid">
        <!-- May overflow -->
        <div class="cal08__cell other weekend"><div class="cal08__cell-n">25</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">26</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">27</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">28</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">29</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">30</div></div>
        <div class="cal08__cell other weekend"><div class="cal08__cell-n">31</div></div>
        <!-- June 1-7 -->
        <div class="cal08__cell weekend"><div class="cal08__cell-n">1</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">2</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--gold">Sprint</div></div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">3</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">4</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--emerald">Holiday</div></div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">5</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">6</div></div>
        <div class="cal08__cell weekend"><div class="cal08__cell-n">7</div></div>
        <!-- June 8-14: today=8 -->
        <div class="cal08__cell today weekend"><div class="cal08__cell-n">8</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">9</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--sky">Planning</div></div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">10</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">11</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--gold">Launch</div><div class="cal08__ev-block cal08__ev-block--red">Deadline</div></div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">12</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">13</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--emerald">Review</div></div></div>
        <div class="cal08__cell weekend"><div class="cal08__cell-n">14</div></div>
        <!-- June 15-21 -->
        <div class="cal08__cell weekend"><div class="cal08__cell-n">15</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">16</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">17</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--sky">Demo</div></div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">18</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">19</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">20</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--gold">1:1</div></div></div>
        <div class="cal08__cell weekend"><div class="cal08__cell-n">21</div></div>
        <!-- June 22-28 -->
        <div class="cal08__cell weekend"><div class="cal08__cell-n">22</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">23</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">24</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--red">Board</div></div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">25</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">26</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">27</div><div class="cal08__cell-evs"><div class="cal08__ev-block cal08__ev-block--emerald">Retro</div></div></div>
        <div class="cal08__cell weekend"><div class="cal08__cell-n">28</div></div>
        <!-- June 29-30 + July -->
        <div class="cal08__cell weekend"><div class="cal08__cell-n">29</div></div>
        <div class="cal08__cell"><div class="cal08__cell-n">30</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">1</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">2</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">3</div></div>
        <div class="cal08__cell other"><div class="cal08__cell-n">4</div></div>
        <div class="cal08__cell other weekend"><div class="cal08__cell-n">5</div></div>
      </div>
    </div>

    <!-- Sidebar -->
    <div class="cal08__side">

      <div class="cal08__side-card">
        <div class="cal08__side-lbl">Today</div>
        <div class="cal08__big-date">08</div>
        <div class="cal08__big-sub">Sunday · June 2026</div>
      </div>

      <div class="cal08__side-card">
        <div class="cal08__side-lbl">This Week</div>
        <div class="cal08__ev-item">
          <div class="cal08__ev-bar" style="background:var(--sky)"></div>
          <div class="cal08__ev-info"><div class="cal08__ev-name">Sprint Planning</div><div class="cal08__ev-time">Mon · 10:00 AM</div></div>
        </div>
        <div class="cal08__ev-item">
          <div class="cal08__ev-bar" style="background:var(--gold)"></div>
          <div class="cal08__ev-info"><div class="cal08__ev-name">Product Launch</div><div class="cal08__ev-time">Wed · 9:00 AM</div></div>
        </div>
        <div class="cal08__ev-item">
          <div class="cal08__ev-bar" style="background:var(--red)"></div>
          <div class="cal08__ev-info"><div class="cal08__ev-name">Hard Deadline</div><div class="cal08__ev-time">Wed · 5:00 PM</div></div>
        </div>
        <div class="cal08__ev-item">
          <div class="cal08__ev-bar" style="background:var(--emerald)"></div>
          <div class="cal08__ev-info"><div class="cal08__ev-name">Design Review</div><div class="cal08__ev-time">Fri · 2:00 PM</div></div>
        </div>
      </div>

      <div class="cal08__side-card">
        <div class="cal08__side-lbl">Event Load</div>
        <div class="cal08__bars">
          <div class="cal08__bar-w"><div class="cal08__bar-fill" style="height:18px"></div><div class="cal08__bar-lbl">W1</div></div>
          <div class="cal08__bar-w"><div class="cal08__bar-fill" style="height:28px"></div><div class="cal08__bar-lbl">W2</div></div>
          <div class="cal08__bar-w"><div class="cal08__bar-fill" style="height:38px"></div><div class="cal08__bar-lbl">W3</div></div>
          <div class="cal08__bar-w"><div class="cal08__bar-fill" style="height:22px"></div><div class="cal08__bar-lbl">W4</div></div>
          <div class="cal08__bar-w"><div class="cal08__bar-fill" style="height:14px"></div><div class="cal08__bar-lbl">W5</div></div>
        </div>
      </div>

    </div>

  </div>
</div>
```
## CSS
```css
.cal08,
.cal08 *,
.cal08 *::before,
.cal08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CSS VARIABLES — the entire theme lives here.
   Toggle between dark / light by swapping values.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.cal08 {
  /* Dark theme (default) */
  --bg: #0d0d0d;
  --surface: #161616;
  --card: #1c1c1c;
  --card2: #222222;
  --border: rgba(255,255,255,0.08);
  --border2: rgba(255,255,255,0.13);
  --text: #f0ece4;
  --text2: #a09890;
  --text3: #5a5550;
  --gold: #c9a84c;
  --gold2: #e8c87a;
  --red: #e05252;
  --emerald: #3d9970;
  --sky: #5ab0d4;
  --shadow: rgba(0,0,0,0.5);
  --today-ring: rgba(201,168,76,0.5);
  --sel-bg: #c9a84c;
  --sel-text: #0d0d0d;
  --toggle-bg: #2a2a2a;
  --icon-sun: '☀';
  --icon-moon: '☽';
}
/* Light theme override — all via CSS vars, zero new selectors needed for the calendar */

.cal08[data-theme="light"] {
  --bg: #f9f6f0;
  --surface: #f2ede4;
  --card: #ffffff;
  --card2: #f7f4ee;
  --border: rgba(0,0,0,0.08);
  --border2: rgba(0,0,0,0.14);
  --text: #1a1410;
  --text2: #6b5f50;
  --text3: #b0a090;
  --gold: #b8892a;
  --gold2: #d4a040;
  --shadow: rgba(0,0,0,0.1);
  --today-ring: rgba(184,137,42,0.4);
  --sel-bg: #b8892a;
  --sel-text: #fff;
  --toggle-bg: #e8e2d8;
}

.cal08 {
  font-family: 'Instrument Sans', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--text);
  transition: background 0.4s ease, color 0.4s ease;
  position: relative;
}
/* Subtle noise overlay for dark mode texture */

.cal08::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  opacity: 0.5;
  pointer-events: none;
  z-index: 0;
}

@keyframes cal08-enter {
  from {
    opacity: 0;
    transform: translateY(16px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes cal08-today-ring {
  0%,
    100% {
    box-shadow: 0 0 0 2px var(--today-ring), 0 0 16px var(--today-ring);
  }

  50% {
    box-shadow: 0 0 0 4px var(--today-ring), 0 0 28px var(--today-ring);
  }
}

@keyframes cal08-bar-grow {
  from {
    transform: scaleY(0);
  }

  to {
    transform: scaleY(1);
  }
}

@keyframes cal08-theme-flip {
  0% {
    transform: rotate(0deg) scale(1);
  }

  50% {
    transform: rotate(180deg) scale(0.8);
  }

  100% {
    transform: rotate(360deg) scale(1);
  }
}

.cal08__shell {
  position: relative;
  z-index: 1;
  max-width: 860px;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 256px;
  gap: 16px;
  animation: cal08-enter 0.55s cubic-bezier(0.22,1,0.36,1) both;
}
/* ── Main card ── */

.cal08__main {
  background: var(--card);
  border: 1px solid var(--border2);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 24px 60px var(--shadow);
  transition: background 0.4s, border-color 0.4s, box-shadow 0.4s;
}
/* ── Header ── */

.cal08__header {
  padding: 28px 28px 20px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  border-bottom: 1px solid var(--border);
  position: relative;
}
/* Gold accent top bar */

.cal08__header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 28px;
  right: 28px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  opacity: 0.6;
}

.cal08__header-left {
}

.cal08__month-big {
  font-family: 'Instrument Serif', serif;
  font-style: italic;
  font-size: 52px;
  line-height: 1;
  color: var(--text);
  letter-spacing: -0.01em;
  transition: color 0.4s;
}

.cal08__month-big em {
  font-style: normal;
  color: var(--gold);
}

.cal08__header-meta {
  margin-top: 5px;
  display: flex;
  gap: 12px;
  align-items: center;
}

.cal08__meta-item {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text3);
  transition: color 0.4s;
}

.cal08__meta-dot {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: var(--text3);
  opacity: 0.4;
}

.cal08__header-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
}

.cal08__nav {
  display: flex;
  border: 1px solid var(--border2);
  border-radius: 10px;
  overflow: hidden;
  transition: border-color 0.4s;
}

.cal08__nav-btn {
  padding: 8px 14px;
  background: transparent;
  border: none;
  color: var(--text2);
  font-size: 15px;
  cursor: pointer;
  transition: all 0.15s;
  user-select: none;
  font-family: 'Instrument Sans', sans-serif;
  border-right: 1px solid var(--border2);
}

.cal08__nav-btn:last-child {
  border-right: none;
}

.cal08__nav-btn:hover {
  background: var(--card2);
  color: var(--gold);
}
/* Theme toggle button */

.cal08__theme-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--toggle-bg);
  border: 1px solid var(--border2);
  border-radius: 24px;
  padding: 6px 14px 6px 10px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
  color: var(--text2);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transition: all 0.25s;
  user-select: none;
}

.cal08__theme-toggle:hover {
  border-color: var(--gold);
  color: var(--gold);
}

.cal08__toggle-icon {
  font-size: 16px;
  transition: transform 0.4s;
  line-height: 1;
}

.cal08__theme-toggle:active .cal08__toggle-icon {
  animation: cal08-theme-flip 0.4s ease;
}
/* ── DOW row ── */

.cal08__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 14px 20px 0;
}

.cal08__dw {
  text-align: center;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--text3);
  padding-bottom: 10px;
  transition: color 0.4s;
}

.cal08__dw:first-child,
.cal08__dw:last-child {
  color: var(--gold);
  opacity: 0.7;
}
/* ── Date grid ── */

.cal08__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 4px 20px 24px;
  gap: 3px;
}

.cal08__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px 0;
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.15s;
  min-height: 60px;
  position: relative;
  gap: 3px;
}

.cal08__cell:hover {
  background: var(--card2);
}

.cal08__cell.other {
  opacity: 0.2;
  pointer-events: none;
}

.cal08__cell-n {
  font-family: 'Instrument Serif', serif;
  font-size: 18px;
  color: var(--text);
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  line-height: 1;
  transition: all 0.15s, color 0.4s;
}

.cal08__cell.weekend .cal08__cell-n {
  color: var(--gold);
  opacity: 0.8;
}

.cal08__cell.other .cal08__cell-n {
  color: var(--text3);
}

.cal08__cell.today .cal08__cell-n {
  background: var(--gold);
  color: var(--sel-text);
  font-weight: 700;
  animation: cal08-today-ring 2.5s ease-in-out infinite;
  font-style: italic;
}

.cal08__cell.selected:not(.today) .cal08__cell-n {
  background: var(--card2);
  border: 2px solid var(--gold);
  color: var(--gold);
}
/* Event blocks inside cells */

.cal08__cell-evs {
  display: flex;
  flex-direction: column;
  gap: 2px;
  width: 100%;
  padding: 0 3px;
}

.cal08__ev-block {
  font-size: 8.5px;
  font-weight: 600;
  padding: 2px 4px;
  border-radius: 3px;
  text-align: left;
  letter-spacing: 0.02em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-transform: uppercase;
}

.cal08__ev-block--gold {
  background: rgba(201,168,76,0.15);
  color: var(--gold);
}

.cal08__ev-block--red {
  background: rgba(224,82,82,0.15);
  color: var(--red);
}

.cal08__ev-block--emerald {
  background: rgba(61,153,112,0.15);
  color: var(--emerald);
}

.cal08__ev-block--sky {
  background: rgba(90,176,212,0.15);
  color: var(--sky);
}
/* ── Right sidebar ── */

.cal08__side {
  display: flex;
  flex-direction: column;
  gap: 14px;
  transition: all 0.4s;
}

.cal08__side-card {
  background: var(--card);
  border: 1px solid var(--border2);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 8px 24px var(--shadow);
  transition: background 0.4s, border-color 0.4s, box-shadow 0.4s;
}

.cal08__side-lbl {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--text3);
  margin-bottom: 14px;
  transition: color 0.4s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.cal08__side-lbl::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}
/* Big date */

.cal08__big-date {
  font-family: 'Instrument Serif', serif;
  font-style: italic;
  font-size: 72px;
  line-height: 1;
  color: var(--gold);
  text-shadow: 0 0 30px var(--today-ring);
  letter-spacing: -0.02em;
  transition: color 0.4s, text-shadow 0.4s;
}

.cal08__big-sub {
  font-size: 12px;
  color: var(--text3);
  margin-top: 6px;
  letter-spacing: 0.08em;
  transition: color 0.4s;
}
/* Event list */

.cal08__ev-item {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
  transition: border-color 0.4s;
}

.cal08__ev-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.cal08__ev-bar {
  width: 2px;
  min-height: 30px;
  border-radius: 1px;
  flex-shrink: 0;
  margin-top: 2px;
}

.cal08__ev-info {
  flex: 1;
  min-width: 0;
}

.cal08__ev-name {
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: color 0.4s;
}

.cal08__ev-time {
  font-size: 10px;
  color: var(--text3);
  margin-top: 2px;
  transition: color 0.4s;
}
/* Sparkline / bar chart */

.cal08__bars {
  display: flex;
  align-items: flex-end;
  gap: 5px;
  height: 40px;
}

.cal08__bar-w {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  height: 100%;
  justify-content: flex-end;
}

.cal08__bar-fill {
  width: 100%;
  border-radius: 3px 3px 0 0;
  background: var(--gold);
  opacity: 0.6;
  transform-origin: bottom;
  animation: cal08-bar-grow 0.7s cubic-bezier(0.22,1,0.36,1) both;
}

.cal08__bar-fill:nth-child(1) {
  animation-delay: 0.05s;
}

.cal08__bar-lbl {
  font-size: 8px;
  color: var(--text3);
  font-weight: 600;
  letter-spacing: 0.05em;
  transition: color 0.4s;
}
/* Color bar overrides */

.cal08__bar-w:nth-child(4) .cal08__bar-fill {
  background: var(--gold2);
  opacity: 1;
}

.cal08__bar-w:nth-child(2) .cal08__bar-fill,
.cal08__bar-w:nth-child(6) .cal08__bar-fill {
  background: var(--emerald);
}

@media (max-width: 700px) {
  .cal08__shell {
    grid-template-columns: 1fr;
  }

  .cal08__side {
    display: none;
  }

  .cal08__month-big {
    font-size: 38px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal08 * {
    animation: none !important;
    transition: color 0.1s, background 0.1s !important;
  }
}
```

## JavaScript
```js
// Date cell selection
document.querySelectorAll('#cal08Grid .cal08__cell:not(.other)').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('#cal08Grid .cal08__cell').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
  });
});

// Theme toggle — just flips data-theme, CSS vars do ALL the work
const root   = document.getElementById('cal08Root');
const toggle = document.getElementById('cal08Toggle');
const icon   = document.getElementById('cal08Icon');
const label  = document.getElementById('cal08ThemeLabel');

toggle.addEventListener('click', function() {
  const isDark = root.getAttribute('data-theme') === 'dark';
  root.setAttribute('data-theme', isDark ? 'light' : 'dark');
  icon.textContent  = isDark ? '☀' : '☽';
  label.textContent = isDark ? 'Light' : 'Dark';
});
```
