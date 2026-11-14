---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/background-progress-fill-button/"
title: "Background Progress Fill Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The button's own background fills from left to right as the work completes."
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Background Progress Fill Button
Source: https://codefronts.com/components/css-loading-buttons/background-progress-fill-button/

The button's own background fills from left to right as the work completes. A single --progress custom property drives a hard-stop gradient, and because the property is registered with @property the browser can interpolate it, so each update glides instead of stepping. One style write per progress event; no extra elements, no width animation.
## HTML
```html
<div class="lb-08">
  <div class="lb-08__stage">
    <section class="lb-08__panel" aria-labelledby="lb-08-h">
      <h2 class="lb-08__h" id="lb-08-h">Reports</h2>
      <p class="lb-08__sub">Export runs server-side. The button fills as rows are written.</p>

      <div class="lb-08__table" role="table" aria-label="Saved reports">
        <div class="lb-08__tr lb-08__tr--head" role="row">
          <span role="columnheader">Report</span><span role="columnheader">Rows</span><span role="columnheader">Owner</span>
        </div>
        <div class="lb-08__tr" role="row">
          <span role="cell">Churn cohort, Q3</span><span role="cell">48,210</span><span role="cell">Sam Rivera</span>
        </div>
        <div class="lb-08__tr" role="row">
          <span role="cell">Activation funnel</span><span role="cell">12,904</span><span role="cell">Alex Chen</span>
        </div>
      </div>

      <div class="lb-08__actions">
        <button class="lb-08__btn" type="button" id="lb-08-btn" data-state="idle" aria-busy="false">
          <span class="lb-08__label" id="lb-08-label">Export CSV</span>
        </button>
        <label class="lb-08__toggle"><input type="checkbox" id="lb-08-fail"> Fail at 60%</label>
      </div>

      <p class="lb-08__live" id="lb-08-live" role="status" aria-live="polite">No export running.</p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-08 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #0d1b2e;
  --surface: #12253c;
  --ink: #e8f0fa;
  --muted: #8ba6c4;
  --rule: #1f3854;
  --accent: #1b3c5e;
  --fill: #4aa3ff;
  --bad: #e2725b;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 18px;
}

.lb-08 *,
.lb-08 *::before,
.lb-08 *::after {
  box-sizing: border-box;
}

.lb-08__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-08__panel {
  inline-size: 100%;
  max-inline-size: 38rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 16px;
  padding: 24px 22px;
}

.lb-08__h {
  margin: 0;
  font-size: 20px;
  font-weight: 620;
  letter-spacing: -.015em;
}

.lb-08__sub {
  margin: 8px 0 18px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 48ch;
}

.lb-08__table {
  display: grid;
  gap: 1px;
  background: var(--rule);
  border: 1px solid var(--rule);
  border-radius: 10px;
  overflow: hidden;
}

.lb-08__tr {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) minmax(0, 1.2fr);
  gap: 10px;
  padding: 11px 14px;
  background: var(--surface);
  font-size: 12.5px;
  min-inline-size: 0;
}

.lb-08__tr span {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.lb-08__tr--head {
  color: var(--muted);
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.lb-08__tr span:nth-child(2) {
  font-variant-numeric: tabular-nums;
}

.lb-08__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  margin: 18px 0 0;
  min-inline-size: 0;
}

.lb-08__btn {
  appearance: none;
  position: relative;
  isolation: isolate;
  border: 1px solid var(--fill);
  background: var(--accent);
  color: var(--ink);
  border-radius: 14px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  padding: 0 20px;
  min-block-size: 46px;
  min-inline-size: 11rem;
  cursor: pointer;
}

.lb-08__btn:focus-visible {
  outline: 3px solid var(--fill);
  outline-offset: 3px;
}

.lb-08__btn[data-state="pending"] {
  cursor: progress;
}

.lb-08__label {
  position: relative;
  z-index: 1;
  display: block;
  min-inline-size: 0;
}

@supports (background: linear-gradient(90deg, red 0 10%, transparent 10%)) {
  .lb-08__btn {
    background: linear-gradient(90deg, var(--fill) 0 var(--lb-08-p, 0%), var(--accent) var(--lb-08-p, 0%));
  }
}

.lb-08__btn {
  transition: --lb-08-p 260ms linear, border-color 200ms linear;
}

@property --lb-08-p {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}

.lb-08__btn[data-state="error"] {
  border-color: var(--bad);
  background: linear-gradient(90deg, var(--bad) 0 var(--lb-08-p, 0%), var(--accent) var(--lb-08-p, 0%));
}

.lb-08__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
}

.lb-08__toggle input {
  accent-color: var(--fill);
  inline-size: 15px;
  block-size: 15px;
}

.lb-08__live {
  margin: 14px 0 0;
  font-size: 12.5px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-08__btn {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .lb-08 {
    --bg: #eef3f9;
    --surface: #ffffff;
    --ink: #0e2138;
    --muted: #5a7391;
    --rule: #d5e0ec;
    --accent: #e4edf7;
    --fill: #9ecbff;
    --bad: #d9573d;
  }
}

[data-theme="light"] .lb-08 {
  --bg: #eef3f9;
  --surface: #ffffff;
  --ink: #0e2138;
  --muted: #5a7391;
  --rule: #d5e0ec;
  --accent: #e4edf7;
  --fill: #9ecbff;
  --bad: #d9573d;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-08-btn');
const label = document.getElementById('lb-08-label');
const live = document.getElementById('lb-08-live');
const failBox = document.getElementById('lb-08-fail');
let tick;
let reset;

const setP = (p) => btn.style.setProperty('--lb-08-p', p + '%');

btn.addEventListener('click', () => {
  if (btn.dataset.state === 'pending') return;
  clearInterval(tick);
  clearTimeout(reset);
  let p = 0;
  setP(0);
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  tick = setInterval(() => {
    p += 20;
    setP(p);
    label.textContent = 'Exporting ' + p + '%';
    live.textContent = 'Export at ' + p + ' percent';
    if (failBox.checked && p >= 60) {
      clearInterval(tick);
      btn.dataset.state = 'error';
      btn.setAttribute('aria-busy', 'false');
      label.textContent = 'Export failed at 60% — retry';
      live.textContent = 'Export failed at 60 percent. The fill is frozen where it stopped.';
      return;
    }
    if (p >= 100) {
      clearInterval(tick);
      btn.dataset.state = 'done';
      btn.setAttribute('aria-busy', 'false');
      label.textContent = 'Download ready';
      live.textContent = 'Export complete';
      reset = setTimeout(() => { btn.dataset.state = 'idle'; label.textContent = 'Export CSV'; setP(0); }, 2200);
    }
  }, 420);
});
```
