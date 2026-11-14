---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/airport-departures-board/"
title: "Airport Departures Board"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A Solari-flap inspired departures board — amber-on-charcoal monospace rows for six flights."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Airport Departures Board
Source: https://codefronts.com/snippets/css-tooltips/airport-departures-board/

A Solari-flap inspired departures board — amber-on-charcoal monospace rows for six flights. Hover any row to reveal the flight detail card: airline, route with duration, aircraft, seats, class, plus a status pill that pulses when a flight is boarding. For travel apps, status pages, and ops dashboards.
## HTML
```html
<div class="tp-13">
  <div class="tp-13__board">
    <div class="tp-13__headrow">
      <span>Time</span><span>Flight</span><span>Destination</span><span>Term</span><span>Gate</span><span>Status</span>
    </div>
    <div class="tp-13__row">
      <span class="tp-13__time">06:15</span>
      <span class="tp-13__num">AA 2847</span>
      <span class="tp-13__dest">New York <small>JFK</small></span>
      <span class="tp-13__term">T3</span>
      <span class="tp-13__gate">B12</span>
      <span class="tp-13__status tp-13__departed">Departed</span>
      <div class="tp-13__tip">
        <div class="tp-13__tip-head">
          <div><div class="tp-13__airline">American Airlines</div><div class="tp-13__flightnum">AA 2847</div></div>
          <span class="tp-13__badge tp-13__badge-departed">Departed</span>
        </div>
        <div class="tp-13__route">
          <div class="tp-13__airport"><div class="tp-13__code">LAX</div><div class="tp-13__city">Los Angeles</div></div>
          <div class="tp-13__arrow"><div class="tp-13__arrow-line"><div class="tp-13__duration">5h 22m</div></div><div class="tp-13__plane">→</div></div>
          <div class="tp-13__airport"><div class="tp-13__code">JFK</div><div class="tp-13__city">New York</div></div>
        </div>
        <div class="tp-13__grid">
          <div class="tp-13__cell"><div class="tp-13__cell-label">Aircraft</div><div class="tp-13__cell-val">B737-800</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Seats</div><div class="tp-13__cell-val">162</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Class</div><div class="tp-13__cell-val">F / Y</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Meals</div><div class="tp-13__cell-val">Yes</div></div>
        </div>
        <div class="tp-13__foot"><span>Departed 06:09 · 6 min early</span><span>T3 · Gate B12</span></div>
      </div>
    </div>
    <div class="tp-13__row">
      <span class="tp-13__time">07:40</span>
      <span class="tp-13__num">UA 5512</span>
      <span class="tp-13__dest">Chicago <small>ORD</small></span>
      <span class="tp-13__term">T7</span>
      <span class="tp-13__gate">C04</span>
      <span class="tp-13__status tp-13__ontime">On Time</span>
      <div class="tp-13__tip">
        <div class="tp-13__tip-head">
          <div><div class="tp-13__airline">United Airlines</div><div class="tp-13__flightnum">UA 5512</div></div>
          <span class="tp-13__badge tp-13__badge-ontime">On Time</span>
        </div>
        <div class="tp-13__route">
          <div class="tp-13__airport"><div class="tp-13__code">LAX</div><div class="tp-13__city">Los Angeles</div></div>
          <div class="tp-13__arrow"><div class="tp-13__arrow-line"><div class="tp-13__duration">3h 55m</div></div><div class="tp-13__plane">→</div></div>
          <div class="tp-13__airport"><div class="tp-13__code">ORD</div><div class="tp-13__city">Chicago</div></div>
        </div>
        <div class="tp-13__grid">
          <div class="tp-13__cell"><div class="tp-13__cell-label">Aircraft</div><div class="tp-13__cell-val">A320neo</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Seats</div><div class="tp-13__cell-val">150</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Class</div><div class="tp-13__cell-val">J / Y</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Wi-Fi</div><div class="tp-13__cell-val">Yes</div></div>
        </div>
        <div class="tp-13__foot"><span>Boards 07:10 · Gate closes 07:25</span><span>T7 · Gate C04</span></div>
      </div>
    </div>
    <div class="tp-13__row">
      <span class="tp-13__time">08:20</span>
      <span class="tp-13__num">DL 8831</span>
      <span class="tp-13__dest">London <small>LHR</small></span>
      <span class="tp-13__term">TB</span>
      <span class="tp-13__gate">A22</span>
      <span class="tp-13__status tp-13__boarding">Boarding</span>
      <div class="tp-13__tip">
        <div class="tp-13__tip-head">
          <div><div class="tp-13__airline">Delta Air Lines</div><div class="tp-13__flightnum">DL 8831</div></div>
          <span class="tp-13__badge tp-13__badge-boarding">Boarding</span>
        </div>
        <div class="tp-13__route">
          <div class="tp-13__airport"><div class="tp-13__code">LAX</div><div class="tp-13__city">Los Angeles</div></div>
          <div class="tp-13__arrow"><div class="tp-13__arrow-line"><div class="tp-13__duration">10h 15m</div></div><div class="tp-13__plane">→</div></div>
          <div class="tp-13__airport"><div class="tp-13__code">LHR</div><div class="tp-13__city">London</div></div>
        </div>
        <div class="tp-13__grid">
          <div class="tp-13__cell"><div class="tp-13__cell-label">Aircraft</div><div class="tp-13__cell-val">B767-400</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Seats</div><div class="tp-13__cell-val">245</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Class</div><div class="tp-13__cell-val">F / J / Y</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Meals</div><div class="tp-13__cell-val">Yes</div></div>
        </div>
        <div class="tp-13__foot"><span>Now boarding all groups · Final call</span><span>TB · Gate A22</span></div>
      </div>
    </div>
    <div class="tp-13__row">
      <span class="tp-13__time">10:30</span>
      <span class="tp-13__num">SQ 7736</span>
      <span class="tp-13__dest">Singapore <small>SIN</small></span>
      <span class="tp-13__term">TB</span>
      <span class="tp-13__gate">B44</span>
      <span class="tp-13__status tp-13__delayed">Delayed 45m</span>
      <div class="tp-13__tip">
        <div class="tp-13__tip-head">
          <div><div class="tp-13__airline">Singapore Airlines</div><div class="tp-13__flightnum">SQ 7736</div></div>
          <span class="tp-13__badge tp-13__badge-delayed">Delayed 45m</span>
        </div>
        <div class="tp-13__route">
          <div class="tp-13__airport"><div class="tp-13__code">LAX</div><div class="tp-13__city">Los Angeles</div></div>
          <div class="tp-13__arrow"><div class="tp-13__arrow-line"><div class="tp-13__duration">17h 30m</div></div><div class="tp-13__plane">→</div></div>
          <div class="tp-13__airport"><div class="tp-13__code">SIN</div><div class="tp-13__city">Singapore</div></div>
        </div>
        <div class="tp-13__grid">
          <div class="tp-13__cell"><div class="tp-13__cell-label">Aircraft</div><div class="tp-13__cell-val">A350-900ULR</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Seats</div><div class="tp-13__cell-val">161</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Class</div><div class="tp-13__cell-val">J / Y</div></div>
          <div class="tp-13__cell"><div class="tp-13__cell-label">Meals</div><div class="tp-13__cell-val">2× hot</div></div>
        </div>
        <div class="tp-13__foot"><span>Late inbound aircraft · New ETD 11:15</span><span>TB · Gate B44</span></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-13 {
  width: 100%;
  min-height: 100vh;
  background: #111111;
  /* Bottom room — flight detail cards drop down from each row, ~280px
       tall. The board sits high so the tooltips render inside the card. */
  padding: 36px 28px 320px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

.tp-13__board {
  max-width: 720px;
  margin: 0 auto;
  background: #181818;
  border: 1px solid #2a2a2a;
  border-radius: 4px;
}

.tp-13__headrow {
  display: grid;
  grid-template-columns: 60px 90px 1fr 50px 50px 90px;
  padding: 10px 18px;
  border-bottom: 1px solid #222;
  font-size: 9px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #3a3a3a;
  gap: 12px;
}

.tp-13__row {
  display: grid;
  grid-template-columns: 60px 90px 1fr 50px 50px 90px;
  align-items: center;
  padding: 13px 18px;
  border-bottom: 1px solid #1d1d1d;
  gap: 12px;
  cursor: help;
  position: relative;
  transition: background 0.12s;
}

.tp-13__row:last-child {
  border-bottom: none;
}

.tp-13__row:hover {
  background: rgba(255, 255, 255, 0.025);
}

.tp-13__time {
  font-size: 16px;
  font-weight: 500;
  color: #e8a020;
  letter-spacing: 0.06em;
}

.tp-13__num {
  font-size: 12px;
  color: #8a8a8a;
}

.tp-13__dest {
  font-size: 13px;
  color: #e0e0e0;
  letter-spacing: 0.02em;
}

.tp-13__dest small {
  font-size: 10px;
  color: #444;
  margin-left: 6px;
}

.tp-13__term {
  font-size: 12px;
  color: #6a6a6a;
}

.tp-13__gate {
  font-size: 13px;
  font-weight: 500;
  color: #c08010;
}

.tp-13__status {
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.05em;
}

.tp-13__ontime {
  color: #30b860;
}

.tp-13__boarding {
  color: #e8a020;
  animation: tp-13-blink 1.2s ease-in-out infinite;
}

.tp-13__delayed {
  color: #e05030;
}

.tp-13__departed {
  color: #404040;
}

@keyframes tp-13-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.4;
  }
}

.tp-13__tip {
  position: absolute;
  left: 50%;
  top: calc(100% + 8px);
  transform: translateX(-50%) translateY(6px);
  z-index: 100;
  width: 360px;
  background: #1c1c1c;
  border: 1px solid #2e2e2e;
  border-radius: 8px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.95);
  overflow: hidden;
}

.tp-13__row:hover .tp-13__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-13__tip-head {
  background: #222;
  padding: 13px 16px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid #2a2a2a;
}

.tp-13__airline {
  font-size: 10px;
  color: #5a5a5a;
  letter-spacing: 0.08em;
}

.tp-13__flightnum {
  font-size: 18px;
  font-weight: 500;
  color: #e8a020;
  margin-top: 2px;
}

.tp-13__badge {
  font-size: 9.5px;
  padding: 3px 9px;
  border-radius: 3px;
  letter-spacing: 0.08em;
  font-weight: 500;
}

.tp-13__badge-ontime {
  background: rgba(48, 184, 96, 0.12);
  color: #30b860;
  border: 1px solid rgba(48, 184, 96, 0.2);
}

.tp-13__badge-boarding {
  background: rgba(232, 160, 32, 0.12);
  color: #e8a020;
  border: 1px solid rgba(232, 160, 32, 0.2);
}

.tp-13__badge-delayed {
  background: rgba(224, 80, 48, 0.12);
  color: #e05030;
  border: 1px solid rgba(224, 80, 48, 0.2);
}

.tp-13__badge-departed {
  background: rgba(80, 80, 80, 0.1);
  color: #505050;
  border: 1px solid #282828;
}

.tp-13__route {
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid #242424;
}

.tp-13__airport {
  text-align: center;
}

.tp-13__code {
  font-size: 20px;
  font-weight: 500;
  color: #c0c0c0;
  letter-spacing: 0.04em;
}

.tp-13__city {
  font-size: 8.5px;
  color: #444;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-top: 3px;
}

.tp-13__arrow {
  flex: 1;
  display: flex;
  align-items: center;
  position: relative;
}

.tp-13__arrow-line {
  height: 1px;
  flex: 1;
  background: linear-gradient(to right, #2a2a2a, #3a3a3a, #2a2a2a);
  position: relative;
}

.tp-13__duration {
  font-size: 8.5px;
  color: #404040;
  text-align: center;
  position: absolute;
  top: -13px;
  width: 100%;
  letter-spacing: 0.08em;
}

.tp-13__plane {
  font-size: 13px;
  color: #505050;
  flex-shrink: 0;
}

.tp-13__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  border-bottom: 1px solid #242424;
}

.tp-13__cell {
  padding: 9px 14px;
  border-right: 1px solid #242424;
}

.tp-13__cell:last-child {
  border-right: none;
}

.tp-13__cell-label {
  font-size: 7.5px;
  color: #383838;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.tp-13__cell-val {
  font-size: 11.5px;
  color: #808080;
}

.tp-13__foot {
  padding: 9px 16px;
  font-size: 8.5px;
  color: #303030;
  display: flex;
  justify-content: space-between;
  letter-spacing: 0.06em;
}
```
