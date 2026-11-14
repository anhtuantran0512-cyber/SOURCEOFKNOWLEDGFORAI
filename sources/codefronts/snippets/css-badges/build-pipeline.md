---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/build-pipeline/"
title: "Build Pipeline"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "CI/CD stage tracker with a spinning arc on the active step."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Build Pipeline
Source: https://codefronts.com/snippets/css-badges/build-pipeline/

CI/CD stage tracker with a spinning arc on the active step. Sequential steps light up — you know roughly how long remains by which step is spinning. Restarts automatically.
## HTML
```html
<div class="bdg-14-stage">
  <div class="bdg-14-card">
    <div class="bdg-14-header">
      <div class="bdg-14-title" id="bdg-14-title">⏳ Running</div>
      <div class="bdg-14-branch">feat/badge-v5 · a3f9c2e</div>
    </div>
    <div class="bdg-14-steps" id="bdg-14-steps"></div>
    <div class="bdg-14-footer">
      <span id="bdg-14-elapsed">Elapsed: 0s</span>
      <button class="bdg-14-restart" id="bdg-14-restart" type="button">↺ Restart demo</button>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-14-stage {
  background: #0d1117;
  padding: 40px 32px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-14-card {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  width: 100%;
  max-width: 420px;
  overflow: hidden;
  font-family: ui-monospace, "JetBrains Mono", monospace;
}

.bdg-14-header {
  padding: 14px 18px;
  border-bottom: 1px solid #21262d;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.bdg-14-title {
  font-size: 12px;
  letter-spacing: 0.06em;
  color: #e6edf3;
}

.bdg-14-branch {
  font-size: 10px;
  color: #8b949e;
  letter-spacing: 0.06em;
}

.bdg-14-steps {
  padding: 8px 0;
}

.bdg-14-step {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 18px;
  transition: background 0.3s;
}

.bdg-14-step.is-active {
  background: rgba(255,255,255,0.03);
}

.bdg-14-step-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.bdg-14-spinner-arc {
  transform-origin: 10px 10px;
  animation: bdg-14-spin 0.8s linear infinite;
}

@keyframes bdg-14-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-14-spinner-arc {
    animation: none;
  }
}

.bdg-14-step-info {
  flex: 1;
}

.bdg-14-step-name {
  font-size: 12px;
  color: #e6edf3;
  letter-spacing: 0.02em;
  line-height: 1;
  margin-bottom: 3px;
}

.bdg-14-step-name.is-dim {
  color: #484f58;
}

.bdg-14-step-meta {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.1em;
  color: #8b949e;
  text-transform: uppercase;
}

.bdg-14-step-dur {
  font-size: 11px;
  color: #8b949e;
  letter-spacing: 0.06em;
  flex-shrink: 0;
}

.bdg-14-footer {
  padding: 12px 18px;
  border-top: 1px solid #21262d;
  font-size: 10px;
  letter-spacing: 0.08em;
  color: #8b949e;
  display: flex;
  justify-content: space-between;
}

.bdg-14-restart {
  cursor: pointer;
  color: #4a90d9;
  text-decoration: underline;
  background: none;
  border: none;
  font-family: inherit;
  font-size: inherit;
  letter-spacing: inherit;
}
```

## JavaScript
```js
// Build pipeline — 6 sequential CI stages, each takes a few seconds.
// Active step shows a spinning arc; completed steps show a checkmark.
// Restarts automatically 3s after completion.
(function () {
  var STEPS = [
    { label: 'Checkout',      meta: 'actions/checkout@v4',      dur: 2  },
    { label: 'npm install',   meta: 'node 20 · 1,284 packages', dur: 14 },
    { label: 'ESLint',        meta: '0 errors · 3 warnings',    dur: 5  },
    { label: 'Jest',          meta: '142 tests · 3 suites',     dur: 24 },
    { label: 'Vite build',    meta: '1.4 MB bundle',            dur: 18 },
    { label: 'fly.io deploy', meta: 'prod · us-east region',    dur: 9  }
  ];
  var active = 0;
  var elapsed = 0;
  var elapsedTimer;
  var stepsEl   = document.getElementById('bdg-14-steps');
  var titleEl   = document.getElementById('bdg-14-title');
  var elapsedEl = document.getElementById('bdg-14-elapsed');
  var restartBtn = document.getElementById('bdg-14-restart');

  function iconDone() {
    return '<svg class="bdg-14-step-icon" viewBox="0 0 20 20">'
         + '<circle cx="10" cy="10" r="9" fill="rgba(63,185,80,0.12)" stroke="rgba(63,185,80,0.4)" stroke-width="1.5"/>'
         + '<path d="M 5.5 10.5 L 8.5 13.5 L 14.5 7" fill="none" stroke="#3fb950" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
         + '</svg>';
  }
  function iconRunning() {
    return '<svg class="bdg-14-step-icon" viewBox="0 0 20 20">'
         + '<circle cx="10" cy="10" r="8" fill="none" stroke="#30363d" stroke-width="2"/>'
         + '<circle cx="10" cy="10" r="8" fill="none" stroke="#e3b341" stroke-width="2" stroke-dasharray="18 32" stroke-linecap="round" class="bdg-14-spinner-arc"/>'
         + '</svg>';
  }
  function iconWaiting() {
    return '<svg class="bdg-14-step-icon" viewBox="0 0 20 20">'
         + '<circle cx="10" cy="10" r="9" fill="none" stroke="#30363d" stroke-width="1.5"/>'
         + '</svg>';
  }

  function render() {
    stepsEl.innerHTML = STEPS.map(function (s, i) {
      var done    = i < active;
      var running = i === active;
      var waiting = i > active;
      var icon    = done ? iconDone() : running ? iconRunning() : iconWaiting();
      var nameClass = waiting ? 'bdg-14-step-name is-dim' : 'bdg-14-step-name';
      var dur = done ? s.dur + 's' : running ? elapsed + 's' : '';
      var durColor = done ? '#3fb950' : running ? '#e3b341' : '#30363d';
      return '<div class="bdg-14-step ' + (running ? 'is-active' : '') + '">'
           + icon
           + '<div class="bdg-14-step-info">'
           + '<div class="' + nameClass + '">' + s.label + '</div>'
           + '<div class="bdg-14-step-meta" style="color:' + (waiting ? '#30363d' : '') + '">'
           + (waiting ? '—' : s.meta) + '</div>'
           + '</div>'
           + '<div class="bdg-14-step-dur" style="color:' + durColor + '">' + dur + '</div>'
           + '</div>';
    }).join('');
    elapsedEl.textContent = 'Elapsed: ' + STEPS.slice(0, active).reduce(function (a, s) { return a + s.dur; }, 0) + 's';
    if (active >= STEPS.length) {
      titleEl.textContent = '✓ Passed';
      titleEl.style.color = '#3fb950';
    } else {
      titleEl.textContent = '⏳ Running';
      titleEl.style.color = '#e3b341';
    }
  }

  function start() {
    active = 0;
    elapsed = 0;
    clearInterval(elapsedTimer);
    render();
    elapsedTimer = setInterval(function () { elapsed++; render(); }, 1000);
    var advance = setInterval(function () {
      elapsed = 0;
      active++;
      render();
      if (active >= STEPS.length) {
        clearInterval(advance);
        clearInterval(elapsedTimer);
        setTimeout(start, 3000);
      }
    }, 2500);
  }

  restartBtn.addEventListener('click', start);
  start();
})();
```
