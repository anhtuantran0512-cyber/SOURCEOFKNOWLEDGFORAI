---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/countdown-ring/"
title: "Countdown Ring"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Ring depletes continuously in real time."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Countdown Ring
Source: https://codefronts.com/snippets/css-badges/countdown-ring/

Ring depletes continuously in real time. Color shifts green → amber → red as the deadline approaches. The depletion rate is the data. A static badge cannot know what time it is.
## HTML
```html
<div class="bdg-15-stage">
  <div class="bdg-15-wrap">
    <div class="bdg-15-event">Sprint Review</div>
    <div class="bdg-15-ring-wrap">
      <svg viewBox="0 0 180 180" aria-hidden="true">
        <circle class="bdg-15-ring-track" cx="90" cy="90" r="81"/>
        <circle class="bdg-15-ring-fill" id="bdg-15-ring" cx="90" cy="90" r="81" stroke="#0cce6b"/>
      </svg>
      <div class="bdg-15-inner">
        <div class="bdg-15-time" id="bdg-15-time">02:34:00</div>
        <div class="bdg-15-label">remaining</div>
      </div>
    </div>
    <div class="bdg-15-deadline" id="bdg-15-deadline">Deadline · Today, 17:00</div>
  </div>
</div>
```
## CSS
```css
.bdg-15-stage {
  background: #fafaf7;
  padding: 60px 48px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-15-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.bdg-15-ring-wrap {
  position: relative;
  width: 180px;
  height: 180px;
}

.bdg-15-ring-wrap svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.bdg-15-ring-track {
  fill: none;
  stroke: #e8e4da;
  stroke-width: 9;
}

.bdg-15-ring-fill {
  fill: none;
  stroke-width: 9;
  stroke-linecap: round;
  stroke-dasharray: 508;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 1s linear, stroke 0.8s ease;
}

.bdg-15-inner {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
}

.bdg-15-time {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 26px;
  font-weight: 700;
  color: #1a1612;
  letter-spacing: -0.02em;
  line-height: 1;
}

.bdg-15-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #4a4239;
}

.bdg-15-deadline {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
  text-align: center;
}

.bdg-15-event {
  font-family: Georgia, "Fraunces", serif;
  font-size: 20px;
  font-style: italic;
  color: #1a1612;
  text-align: center;
}
```

## JavaScript
```js
// Countdown ring — 4h total sprint, ~2h34m initially remaining.
// Ring depletes continuously, color shifts at 50% and 20% thresholds.
(function () {
  var TOTAL_MS = 4 * 3600 * 1000;
  var deadline = new Date(Date.now() + 2 * 3600 * 1000 + 34 * 60 * 1000);
  var ring   = document.getElementById('bdg-15-ring');
  var timeEl = document.getElementById('bdg-15-time');
  var deadEl = document.getElementById('bdg-15-deadline');
  var CIRCUM = 2 * Math.PI * 81;

  function pad2(n) { return String(n).padStart(2, '0'); }
  function tick() {
    var remaining = Math.max(0, deadline - Date.now());
    var frac = remaining / TOTAL_MS;
    ring.style.strokeDashoffset = CIRCUM * (1 - frac);
    ring.style.stroke = frac > 0.5 ? '#0cce6b' : frac > 0.2 ? '#ffa400' : '#ff4e42';
    var h = Math.floor(remaining / 3600000);
    var m = Math.floor((remaining % 3600000) / 60000);
    var s = Math.floor((remaining % 60000) / 1000);
    timeEl.textContent = pad2(h) + ':' + pad2(m) + ':' + pad2(s);
    deadEl.textContent = 'Deadline · Today, ' + deadline.getHours() + ':' + pad2(deadline.getMinutes());
  }
  tick();
  setInterval(tick, 1000);
})();
```
