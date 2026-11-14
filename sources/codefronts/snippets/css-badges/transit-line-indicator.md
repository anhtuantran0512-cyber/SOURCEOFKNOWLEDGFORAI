---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/transit-line-indicator/"
title: "Transit Line Indicator"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Wayfinding distilled."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transit Line Indicator
Source: https://codefronts.com/snippets/css-badges/transit-line-indicator/

Wayfinding distilled. Bullet, name, live arrival, and a strip showing where you are on the line. Built to be read from across a platform — and the next-arrival time keeps counting down.
## HTML
```html
<div class="bdg-05-stage">
  <div class="bdg-05-platform">
    <div class="bdg-05-row">
      <div class="bdg-05-bullet">M7</div>
      <div>
        <div class="bdg-05-line">Northbrook Express</div>
        <div class="bdg-05-via">via Riverside · skip-stop after 18:00</div>
      </div>
      <div class="bdg-05-live">
        <span class="bdg-05-live-dot"></span>
        <span class="bdg-05-live-text">Next in <strong id="bdg-05-live-time">4 min</strong></span>
      </div>
    </div>

    <div class="bdg-05-route">
      <div class="bdg-05-route-line"></div>
      <div class="bdg-05-route-stops">
        <div class="bdg-05-stop bdg-05-stop-active"><span class="bdg-05-stop-label">Central</span></div>
        <div class="bdg-05-stop"><span class="bdg-05-stop-label">Park</span></div>
        <div class="bdg-05-stop"><span class="bdg-05-stop-label">9th Ave</span></div>
        <div class="bdg-05-stop bdg-05-stop-transfer"><span class="bdg-05-stop-label">Riverside</span></div>
        <div class="bdg-05-stop"><span class="bdg-05-stop-label">Northbrook</span></div>
      </div>
    </div>

    <div class="bdg-05-footer">
      <span>EASTBOUND · PLATFORM 3</span>
      <span>SVC OK</span>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-05-stage {
  background: #d9d3c4;
  padding: 50px 36px;
  background-image: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.06) 100%), linear-gradient(0deg, rgba(0,0,0,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.05) 1px, transparent 1px);
  background-size: 100% 100%, 60px 30px, 60px 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-05-platform {
  background: linear-gradient(180deg, #15171a 0%, #0c0e10 100%);
  padding: 28px 26px 26px;
  max-width: 460px;
  width: 100%;
  box-shadow: 0 30px 60px -22px rgba(0,0,0,0.7), 0 6px 16px -2px rgba(0,0,0,0.4);
  color: #fff;
  position: relative;
  border-top: 1px solid rgba(255,255,255,0.08);
}

.bdg-05-platform::before {
  content: 'M  T  A · LIVE';
  position: absolute;
  top: -12px;
  left: 0;
  background: #1a1a1a;
  padding: 4px 12px;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 9px;
  letter-spacing: 0.3em;
  color: #c8102e;
}

.bdg-05-row {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 18px;
  align-items: center;
  padding-bottom: 22px;
  border-bottom: 1px dashed rgba(255,255,255,0.18);
}

.bdg-05-bullet {
  width: 62px;
  height: 62px;
  border-radius: 50%;
  background: linear-gradient(180deg, #d4233d 0%, #b80e25 100%);
  color: #fff;
  font-family: "Bebas Neue", system-ui, sans-serif;
  font-size: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  letter-spacing: 0.03em;
  box-shadow: inset 0 -4px 6px rgba(0,0,0,0.35), inset 0 4px 5px rgba(255,255,255,0.25), 0 6px 14px rgba(200,16,46,0.5);
  text-shadow: 0 1px 2px rgba(0,0,0,0.3);
}

.bdg-05-line {
  font-family: "Bebas Neue", system-ui, sans-serif;
  font-size: 26px;
  letter-spacing: 0.03em;
  line-height: 1;
  margin-bottom: 5px;
}

.bdg-05-via {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 9px;
  letter-spacing: 0.06em;
  color: rgba(255,255,255,0.55);
  text-transform: uppercase;
}

.bdg-05-live {
  display: flex;
  align-items: center;
  gap: 7px;
  background: rgba(255,255,255,0.04);
  padding: 7px 12px;
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 2px;
}

.bdg-05-live-dot {
  width: 7px;
  height: 7px;
  background: #4ade80;
  border-radius: 50%;
  box-shadow: 0 0 7px #4ade80;
  animation: bdg-05-pulse 1.6s infinite;
}

@keyframes bdg-05-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.35;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-05-live-dot {
    animation: none;
  }
}

.bdg-05-live-text {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.08em;
  color: rgba(255,255,255,0.75);
  text-transform: uppercase;
}

.bdg-05-live-text strong {
  color: #fff;
  font-weight: 700;
  font-size: 11px;
}

.bdg-05-route {
  margin-top: 22px;
  position: relative;
  padding: 0 4px;
}

.bdg-05-route-line {
  position: absolute;
  top: 7px;
  left: 4px;
  right: 4px;
  height: 4px;
  background: #c8102e;
  border-radius: 2px;
}

.bdg-05-route-stops {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  position: relative;
  z-index: 1;
}

.bdg-05-stop {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
}

.bdg-05-stop::before {
  content: '';
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #1a1a1a;
  border: 3px solid #c8102e;
  margin-bottom: 8px;
  transition: transform 0.2s;
}

.bdg-05-stop:hover::before {
  transform: scale(1.2);
}

.bdg-05-stop-active::before {
  background: #fff;
  border-color: #fff;
  box-shadow: 0 0 0 2px #c8102e;
}

.bdg-05-stop-transfer::before {
  background: #fff;
  box-shadow: 0 0 0 2px #c8102e;
}

.bdg-05-stop-label {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 8.5px;
  letter-spacing: 0.06em;
  color: rgba(255,255,255,0.55);
  text-transform: uppercase;
  text-align: center;
  line-height: 1.25;
  white-space: nowrap;
}

.bdg-05-stop-active .bdg-05-stop-label {
  color: #fff;
}

.bdg-05-footer {
  margin-top: 22px;
  padding-top: 14px;
  border-top: 1px solid rgba(255,255,255,0.08);
  display: flex;
  justify-content: space-between;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 8px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.4);
}
```

## JavaScript
```js
// Next arrival countdown — decrements every 4s, resets to 5 min when
// it bottoms out so the demo never goes stale.
(function () {
  var nextIn = 4;
  var liveTimeEl = document.getElementById('bdg-05-live-time');
  if (!liveTimeEl) return;
  setInterval(function () {
    nextIn = nextIn > 1 ? nextIn - 1 : 5;
    liveTimeEl.textContent = nextIn + ' min';
  }, 4000);
})();
```
