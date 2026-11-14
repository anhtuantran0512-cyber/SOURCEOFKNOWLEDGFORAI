---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/live-price-ticker/"
title: "Live Price Ticker"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "A static price is history; an animated price is now."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Price Ticker
Source: https://codefronts.com/snippets/css-badges/live-price-ticker/

A static price is history; an animated price is now. Green or red flash on each update tells direction without comparison. Sparkline shows the recent walk. The animation IS the signal.
## HTML
```html
<div class="bdg-16-stage">
  <div class="bdg-16-card" id="bdg-16-card">
    <div class="bdg-16-top">
      <div class="bdg-16-symbol">BTC · USD</div>
      <div class="bdg-16-live-dot">Live · 3s</div>
    </div>
    <div class="bdg-16-value" id="bdg-16-value">$67,420.58</div>
    <div class="bdg-16-change">
      <span class="bdg-16-delta bdg-16-up" id="bdg-16-delta">+$234.12</span>
      <span class="bdg-16-delta bdg-16-up" id="bdg-16-pct">(+0.35%)</span>
      <span class="bdg-16-arrow" id="bdg-16-arrow">▲</span>
    </div>
    <svg class="bdg-16-sparkline" viewBox="0 0 200 36" preserveAspectRatio="none" aria-hidden="true">
      <defs>
        <linearGradient id="bdg-16-spark-grad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0cce6b" stop-opacity="0.3"/>
          <stop offset="100%" stop-color="#0cce6b" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <path id="bdg-16-spark-area" fill="url(#bdg-16-spark-grad)" opacity="0.6"/>
      <polyline id="bdg-16-spark-line" class="bdg-16-sparkline-path" stroke="#0cce6b"/>
    </svg>
    <div class="bdg-16-footer">
      <span id="bdg-16-updated">Updated just now</span>
      <span>24h Vol $42.8B</span>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-16-stage {
  background: #0d1117;
  padding: 48px 36px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-16-card {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  padding: 22px 24px;
  width: 100%;
  max-width: 380px;
  position: relative;
  overflow: hidden;
  font-family: ui-monospace, "JetBrains Mono", monospace;
}

.bdg-16-card.is-flash-up {
  animation: bdg-16-flash-up 0.65s ease-out;
}

.bdg-16-card.is-flash-down {
  animation: bdg-16-flash-down 0.65s ease-out;
}

@keyframes bdg-16-flash-up {
  0% {
    background: rgba(12,206,107,0.2);
  }

  100% {
    background: #161b22;
  }
}

@keyframes bdg-16-flash-down {
  0% {
    background: rgba(255,78,66,0.2);
  }

  100% {
    background: #161b22;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-16-card.is-flash-up,
    .bdg-16-card.is-flash-down {
    animation: none;
  }
}

.bdg-16-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.bdg-16-symbol {
  font-size: 11px;
  letter-spacing: 0.18em;
  color: #8b949e;
  text-transform: uppercase;
}

.bdg-16-live-dot {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #8b949e;
}

.bdg-16-live-dot::before {
  content: '';
  display: block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #0cce6b;
  box-shadow: 0 0 6px #0cce6b;
  animation: bdg-16-pulse 2s infinite;
}

@keyframes bdg-16-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.4;
  }
}

.bdg-16-value {
  font-size: 36px;
  font-weight: 700;
  color: #e6edf3;
  letter-spacing: -0.02em;
  margin-bottom: 6px;
  line-height: 1;
}

.bdg-16-change {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 14px;
}

.bdg-16-delta {
  font-size: 13px;
  font-weight: 600;
}

.bdg-16-up {
  color: #0cce6b;
}

.bdg-16-down {
  color: #ff4e42;
}

.bdg-16-arrow {
  font-size: 12px;
}

.bdg-16-sparkline {
  width: 100%;
  height: 36px;
}

.bdg-16-sparkline-path {
  fill: none;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.bdg-16-footer {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid #21262d;
  font-size: 9px;
  letter-spacing: 0.1em;
  color: #8b949e;
  text-transform: uppercase;
}
```

## JavaScript
```js
// Live price ticker — random-walks BTC around $67k. Every 3s the
// price moves, the delta + sparkline update, and the background
// flashes green or red depending on direction.
(function () {
  var price = 67420.58;
  var openPrice = 67186.46;
  var history = [];
  for (var k = 0; k < 24; k++) {
    history.push(67186 + Math.sin(k * 0.7) * 180 + k * 9.8 + Math.random() * 60);
  }
  history.push(price);

  var card    = document.getElementById('bdg-16-card');
  var valEl   = document.getElementById('bdg-16-value');
  var deltaEl = document.getElementById('bdg-16-delta');
  var pctEl   = document.getElementById('bdg-16-pct');
  var arrowEl = document.getElementById('bdg-16-arrow');
  var lineEl  = document.getElementById('bdg-16-spark-line');
  var areaEl  = document.getElementById('bdg-16-spark-area');
  var updEl   = document.getElementById('bdg-16-updated');

  function fmt(n) {
    return n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function redrawSpark() {
    var W = 200, H = 36, pad = 2;
    var min = Math.min.apply(null, history);
    var max = Math.max.apply(null, history);
    var range = max - min || 1;
    var pts = history.map(function (v, i) {
      var x = (i / (history.length - 1)) * (W - 2 * pad) + pad;
      var y = H - pad - ((v - min) / range) * (H - 2 * pad);
      return x.toFixed(1) + ',' + y.toFixed(1);
    }).join(' ');
    lineEl.setAttribute('points', pts);
    var areaD = 'M ' + pad + ' ' + H + ' L ' + history.map(function (v, i) {
      var x = (i / (history.length - 1)) * (W - 2 * pad) + pad;
      var y = H - pad - ((v - min) / range) * (H - 2 * pad);
      return x.toFixed(1) + ' ' + y.toFixed(1);
    }).join(' L ') + ' L ' + (W - pad) + ' ' + H + ' Z';
    areaEl.setAttribute('d', areaD);
  }

  function updatePrice() {
    var prev = price;
    price += (Math.random() - 0.47) * 110;
    price = Math.max(64000, Math.min(72000, price));
    history.push(price);
    if (history.length > 24) history.shift();

    var isUp = price >= prev;
    var totalChange = price - openPrice;
    var totalPct = (totalChange / openPrice) * 100;

    valEl.textContent   = '$' + fmt(price);
    deltaEl.textContent = (totalChange >= 0 ? '+$' : '-$') + fmt(Math.abs(totalChange));
    pctEl.textContent   = '(' + (totalPct >= 0 ? '+' : '') + totalPct.toFixed(2) + '%)';
    arrowEl.textContent = isUp ? '▲' : '▼';
    arrowEl.style.color = isUp ? '#0cce6b' : '#ff4e42';

    var cls = isUp ? 'bdg-16-up' : 'bdg-16-down';
    deltaEl.className = 'bdg-16-delta ' + cls;
    pctEl.className   = 'bdg-16-delta ' + cls;
    document.querySelectorAll('#bdg-16-spark-grad stop').forEach(function (s) {
      s.setAttribute('stop-color', isUp ? '#0cce6b' : '#ff4e42');
    });
    lineEl.setAttribute('stroke', isUp ? '#0cce6b' : '#ff4e42');

    card.classList.remove('is-flash-up', 'is-flash-down');
    void card.offsetWidth;
    card.classList.add(isUp ? 'is-flash-up' : 'is-flash-down');

    updEl.textContent = 'Updated just now';
    redrawSpark();
  }

  redrawSpark();
  setInterval(updatePrice, 3000);
})();
```
