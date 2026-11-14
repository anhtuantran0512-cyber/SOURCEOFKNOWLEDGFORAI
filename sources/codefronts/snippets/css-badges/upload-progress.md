---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/upload-progress/"
title: "Upload Progress"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "A static 73% could be a live transfer or stalled."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Upload Progress
Source: https://codefronts.com/snippets/css-badges/upload-progress/

A static 73% could be a live transfer or stalled. The shimmer moving through the bar means bytes are flowing; when it becomes a slow pulse, the transfer has stalled; when it stops, it's done. Three states, one animation property.
## HTML
```html
<div class="bdg-01-stage">
  <div class="bdg-01-badge" id="bdg-01-badge" style="--bdg-01-ext-color:#6b3aa0">
    <div class="bdg-01-top">
      <div class="bdg-01-ext">ZIP</div>
      <div class="bdg-01-file-info">
        <div class="bdg-01-filename">design-assets-v4.zip</div>
        <div class="bdg-01-filesize">340 MB · 1,284 files</div>
      </div>
      <svg class="bdg-01-status-icon" viewBox="0 0 28 28" aria-hidden="true">
        <circle class="bdg-01-check-circle" cx="14" cy="14" r="13" fill="none" stroke="#e8e4da" stroke-width="2"/>
        <path class="bdg-01-check-path" d="M 7 14 L 11.5 18.5 L 21 9" fill="none" stroke="#aaa" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="bdg-01-bar-wrap">
      <div class="bdg-01-bar-fill" id="bdg-01-fill" style="--bdg-01-color:#6b3aa0"></div>
    </div>
    <div class="bdg-01-bottom">
      <div class="bdg-01-pct" id="bdg-01-pct">0%</div>
      <div class="bdg-01-speed-eta" id="bdg-01-meta">Waiting…</div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-01-stage {
  background: #f2f4f7;
  padding: 48px 40px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  justify-content: center;
  align-items: flex-start;
  width: 100%;
  min-height: 100vh;
  align-items: center;
}

.bdg-01-badge {
  width: 100%;
  max-width: 420px;
  background: #fff;
  border: 1px solid #dde3ec;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.bdg-01-top {
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.bdg-01-ext {
  width: 40px;
  height: 40px;
  border-radius: 5px;
  background: var(--bdg-01-ext-color, #555);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 9px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.08em;
  flex-shrink: 0;
}

.bdg-01-file-info {
  flex: 1;
  min-width: 0;
}

.bdg-01-filename {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 13px;
  font-weight: 600;
  color: #1a1612;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1;
  margin-bottom: 3px;
}

.bdg-01-filesize {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #888;
}

.bdg-01-status-icon {
  width: 28px;
  height: 28px;
  flex-shrink: 0;
}

.bdg-01-check-circle {
  transition: stroke 0.4s;
}

.bdg-01-check-path {
  stroke-dasharray: 20;
  stroke-dashoffset: 20;
  transition: stroke-dashoffset 0.5s cubic-bezier(0.4, 0, 0.2, 1) 0.15s, stroke 0.3s;
}

.bdg-01-badge.is-complete .bdg-01-check-circle {
  stroke: #0cce6b;
}

.bdg-01-badge.is-complete .bdg-01-check-path {
  stroke: #0cce6b;
  stroke-dashoffset: 0;
}

.bdg-01-bar-wrap {
  height: 4px;
  background: #f0eee8;
  position: relative;
}

.bdg-01-bar-fill {
  height: 100%;
  background: var(--bdg-01-color, #4285f4);
  width: 0%;
  transition: width 0.5s linear, background 0.5s ease;
  position: relative;
  overflow: hidden;
}

.bdg-01-bar-fill::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.4) 50%, transparent 100%);
  animation: bdg-01-shimmer 1.2s ease-in-out infinite;
}

@keyframes bdg-01-shimmer {
  from {
    transform: translateX(-100%);
  }

  to {
    transform: translateX(100%);
  }
}

.bdg-01-badge.is-complete .bdg-01-bar-fill::after {
  animation: none;
}

.bdg-01-badge.is-stalled .bdg-01-bar-fill::after {
  animation: bdg-01-stall 1.5s ease-in-out infinite;
}

@keyframes bdg-01-stall {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-01-bar-fill::after {
    animation: none;
  }
}

.bdg-01-bottom {
  padding: 8px 16px 12px;
  display: flex;
  justify-content: space-between;
}

.bdg-01-pct {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  color: #1a1612;
}

.bdg-01-speed-eta {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #888;
  text-align: right;
}
```

## JavaScript
```js
// Simulate an upload — progresses, stalls briefly at ~42% to show the
// stall state, resumes, completes. Then idle. Click to restart not
// included; in real use the lifecycle is driven by actual XHR events.
(function () {
  var badge  = document.getElementById('bdg-01-badge');
  var fill   = document.getElementById('bdg-01-fill');
  var pctEl  = document.getElementById('bdg-01-pct');
  var metaEl = document.getElementById('bdg-01-meta');
  var pct = 0;
  var stalled = false;

  function update() {
    fill.style.width = pct + '%';
    pctEl.textContent = Math.floor(pct) + '%';
    if (pct >= 100) {
      badge.classList.remove('is-stalled');
      badge.classList.add('is-complete');
      fill.style.background = '#0cce6b';
      pctEl.textContent = '100%';
      metaEl.textContent = 'Complete';
      return;
    }
    if (stalled) {
      badge.classList.add('is-stalled');
      metaEl.textContent = 'Connection interrupted…';
    } else {
      badge.classList.remove('is-stalled');
      var speed = (2.4 + Math.random() * 0.8).toFixed(1);
      var remaining = ((340 - 340 * pct / 100) / parseFloat(speed)).toFixed(0);
      metaEl.textContent = speed + ' MB/s · ' + remaining + 's left';
    }
  }

  var ticker = setInterval(function () {
    if (pct >= 100) { clearInterval(ticker); return; }
    if (pct >= 42 && pct < 48 && !stalled) {
      stalled = true;
      update();
      return;
    }
    if (stalled && pct < 48) {
      setTimeout(function () { stalled = false; }, 3000);
      return;
    }
    pct = Math.min(100, pct + 1.8 + Math.random() * 0.6);
    update();
  }, 400);

  update();
})();
```
