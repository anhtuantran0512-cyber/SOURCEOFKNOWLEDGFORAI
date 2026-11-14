---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/ecg-heartbeat/"
title: "ECG Heartbeat"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Live BPM with a continuously scrolling waveform."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: ECG Heartbeat
Source: https://codefronts.com/snippets/css-badges/ecg-heartbeat/

Live BPM with a continuously scrolling waveform. Scroll speed equals beats per minute literally — change the duration and you change the rate. The badge and the data are the same thing.
## HTML
```html
<div class="bdg-13-stage">
  <div class="bdg-13-card">
    <div class="bdg-13-header">
      <div class="bdg-13-system">SRV-PROD-01 · Heartbeat</div>
      <div class="bdg-13-status">Normal</div>
    </div>

    <div class="bdg-13-viewport">
      <svg class="bdg-13-svg" width="880" height="68" viewBox="0 0 880 68" style="animation-duration: 0.833s" aria-hidden="true">
        <polyline
          fill="none"
          stroke="#00e5a0"
          stroke-width="2"
          stroke-linejoin="round"
          stroke-linecap="round"
          opacity="0.9"
          points="
            0,48 58,48
            64,42 70,38 76,42 82,48
            132,48 136,53 139,10 143,60 147,48
            170,48 185,40 200,36 215,40 230,48
            300,48
            358,48
            364,42 370,38 376,42 382,48
            432,48 436,53 439,10 443,60 447,48
            470,48 485,40 500,36 515,40 530,48
            600,48
            658,48
            664,42 670,38 676,42 682,48
            732,48 736,53 739,10 743,60 747,48
            770,48 785,40 800,36 815,40 830,48
            880,48
          "/>
        <line x1="0" y1="48" x2="880" y2="48" stroke="#00e5a0" stroke-width="0.3" opacity="0.2"/>
      </svg>
    </div>

    <div class="bdg-13-metrics">
      <div class="bdg-13-bpm">
        <div class="bdg-13-bpm-val" id="bdg-13-bpm">72</div>
        <div class="bdg-13-bpm-unit">BPM</div>
      </div>
      <div class="bdg-13-secondary">
        <div class="bdg-13-sec-val">P–R 160ms</div>
        <div class="bdg-13-sec-label">Interval</div>
      </div>
      <div class="bdg-13-secondary">
        <div class="bdg-13-sec-val">QRS 88ms</div>
        <div class="bdg-13-sec-label">Duration</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-13-stage {
  background: #050c12;
  padding: 48px 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-13-card {
  background: #0a1520;
  border: 1px solid #0f2030;
  border-radius: 8px;
  padding: 20px 24px;
  width: 100%;
  max-width: 440px;
}

.bdg-13-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.bdg-13-system {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: #00e5a0;
  opacity: 0.7;
}

.bdg-13-status {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #00e5a0;
  padding: 3px 10px;
  border: 1px solid rgba(0,229,160,0.3);
  border-radius: 20px;
  animation: bdg-13-glow 3s ease-in-out infinite;
}

@keyframes bdg-13-glow {
  0%,
    100% {
    box-shadow: 0 0 0 rgba(0,229,160,0.3);
  }

  50% {
    box-shadow: 0 0 8px rgba(0,229,160,0.3);
  }
}

.bdg-13-viewport {
  width: 100%;
  height: 68px;
  overflow: hidden;
  position: relative;
  margin-bottom: 14px;
}

.bdg-13-svg {
  display: block;
  animation: bdg-13-scroll 0.833s linear infinite;
}

@keyframes bdg-13-scroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-13-svg,
    .bdg-13-status {
    animation: none;
  }
}

.bdg-13-metrics {
  display: flex;
  align-items: flex-end;
  gap: 24px;
  padding-top: 12px;
  border-top: 1px solid #0f2030;
}

.bdg-13-bpm {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.bdg-13-bpm-val {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 42px;
  font-weight: 700;
  color: #00e5a0;
  line-height: 0.9;
  letter-spacing: -0.02em;
}

.bdg-13-bpm-unit {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 12px;
  letter-spacing: 0.12em;
  color: rgba(0,229,160,0.6);
  text-transform: uppercase;
}

.bdg-13-secondary {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-left: auto;
  text-align: right;
}

.bdg-13-sec-val {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 14px;
  color: rgba(0,229,160,0.8);
  letter-spacing: 0.04em;
}

.bdg-13-sec-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: rgba(0,229,160,0.4);
}
```

## JavaScript
```js
// BPM drifts slightly around 72 so the badge feels alive. Animation
// duration is tied to BPM literally — 60 / bpm seconds per cycle.
(function () {
  var bpmEl = document.getElementById('bdg-13-bpm');
  var ecgSvg = document.querySelector('.bdg-13-svg');
  var bpm = 72;
  setInterval(function () {
    bpm += (Math.random() - 0.5) * 2;
    bpm = Math.max(68, Math.min(78, bpm));
    var rounded = Math.round(bpm);
    bpmEl.textContent = rounded;
    ecgSvg.style.animationDuration = (60 / bpm).toFixed(3) + 's';
  }, 4000);
})();
```
