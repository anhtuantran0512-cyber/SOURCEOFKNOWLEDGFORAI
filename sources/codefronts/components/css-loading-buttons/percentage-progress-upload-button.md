---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/percentage-progress-upload-button/"
title: "Percentage Progress Upload Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "Numeric progress beside the fill, with tabular figures so the digits do not jitter as they climb, and a role=progressbar wrapper whose aria-valuenow stays in…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Percentage Progress Upload Button
Source: https://codefronts.com/components/css-loading-buttons/percentage-progress-upload-button/

Numeric progress beside the fill, with tabular figures so the digits do not jitter as they climb, and a role=progressbar wrapper whose aria-valuenow stays in sync with what is painted. A toggle switches the same control to indeterminate, because when the total size is unknown a percentage is a lie and a plain spinner is the honest answer.
## HTML
```html
<div class="lb-09">
  <div class="lb-09__stage">
    <section class="lb-09__panel" aria-labelledby="lb-09-h">
      <h2 class="lb-09__h" id="lb-09-h">Upload assets</h2>

      <div class="lb-09__item">
        <span class="lb-09__thumb" aria-hidden="true">
          <svg viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2.5" y="4" width="15" height="12" rx="1.5"/><path d="M2.5 13l4-3.5 3.5 3 3-2.5 4 3.5"/></svg>
        </span>
        <div class="lb-09__meta">
          <p class="lb-09__name">launch-hero-2400.png</p>
          <p class="lb-09__size">14.8 MB · PNG</p>
        </div>
      </div>

      <div class="lb-09__track" id="lb-09-track" role="progressbar" aria-labelledby="lb-09-h" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">
        <span class="lb-09__fill" id="lb-09-fill"></span>
      </div>

      <div class="lb-09__row">
        <button class="lb-09__btn" type="button" id="lb-09-btn" data-state="idle" aria-busy="false">
          <span class="lb-09__blabel" id="lb-09-label">Start upload</span>
          <output class="lb-09__pct" id="lb-09-pct"></output>
        </button>
        <button class="lb-09__cancel" type="button" id="lb-09-cancel" hidden>Cancel</button>
        <label class="lb-09__toggle"><input type="checkbox" id="lb-09-unknown"> Unknown total size</label>
      </div>

      <p class="lb-09__live" id="lb-09-live" role="status" aria-live="polite">Waiting to upload.</p>
      <p class="lb-09__alert" id="lb-09-alert" role="alert"></p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-09 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f4f5f7;
  --surface: #ffffff;
  --ink: #1b1f24;
  --muted: #6b7280;
  --rule: #e2e5ea;
  --accent: #3f4c5c;
  --bad: #b3392b;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-09 *,
.lb-09 *::before,
.lb-09 *::after {
  box-sizing: border-box;
}

.lb-09__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-09__panel {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  padding: 22px 20px;
}

.lb-09__h {
  margin: 0 0 16px;
  font-size: 19px;
  font-weight: 620;
  letter-spacing: -.015em;
}

.lb-09__item {
  display: flex;
  gap: 12px;
  align-items: center;
  padding: 12px;
  border: 1px solid var(--rule);
  min-inline-size: 0;
}

.lb-09__thumb {
  flex: none;
  color: var(--muted);
  display: inline-flex;
}

.lb-09__meta {
  min-inline-size: 0;
}

.lb-09__name {
  margin: 0;
  font-size: 13px;
  font-weight: 560;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.lb-09__size {
  margin: 3px 0 0;
  font-size: 11.5px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.lb-09__track {
  margin: 14px 0;
  block-size: 6px;
  background: var(--rule);
  overflow: hidden;
}

.lb-09__fill {
  display: block;
  block-size: 100%;
  inline-size: 0%;
  background: var(--accent);
  transition: inline-size 300ms linear;
}

.lb-09__track[data-mode="indeterminate"] .lb-09__fill {
  inline-size: 34%;
  animation: lb-09-sweep 1.1s ease-in-out infinite;
}

@keyframes lb-09-sweep {
  0% {
    transform: translateX(-110%);
  }

  100% {
    transform: translateX(320%);
  }
}

.lb-09__track[data-state="error"] .lb-09__fill {
  background: var(--bad);
}

.lb-09__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  min-inline-size: 0;
}

.lb-09__btn {
  appearance: none;
  border: 0;
  background: var(--accent);
  color: #f7f9fb;
  border-radius: 0;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  padding: 0 16px;
  min-block-size: 44px;
  min-inline-size: 0;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.lb-09__btn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

.lb-09__btn[data-state="pending"] {
  cursor: progress;
}

.lb-09__btn[data-state="error"] {
  background: var(--bad);
}

.lb-09__blabel {
  min-inline-size: 0;
}

.lb-09__pct {
  font-variant-numeric: tabular-nums;
  font-weight: 700;
  min-inline-size: 4ch;
  text-align: end;
}

.lb-09__cancel[hidden] {
  display: none;
}

.lb-09__cancel {
  appearance: none;
  border: 1px solid var(--rule);
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: 12.5px;
  padding: 0 14px;
  min-block-size: 44px;
  cursor: pointer;
}

.lb-09__cancel:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.lb-09__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
  min-inline-size: 0;
}

.lb-09__toggle input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

.lb-09__live {
  margin: 14px 0 0;
  font-size: 12.5px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-09__alert {
  margin: 4px 0 0;
  min-block-size: 17px;
  font-size: 12.5px;
  font-weight: 560;
  color: var(--bad);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-09__fill {
    transition: none;
  }

  .lb-09__track[data-mode="indeterminate"] .lb-09__fill {
    animation: none;
    inline-size: 100%;
    opacity: .5;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-09 {
    --bg: #14171b;
    --surface: #1c2027;
    --ink: #e9ecf1;
    --muted: #98a1ae;
    --rule: #2b3140;
    --accent: #94a8c0;
    --bad: #ef7f6d;
  }

  .lb-09__btn {
    color: #14171b;
  }
}

[data-theme="dark"] .lb-09 {
  --bg: #14171b;
  --surface: #1c2027;
  --ink: #e9ecf1;
  --muted: #98a1ae;
  --rule: #2b3140;
  --accent: #94a8c0;
  --bad: #ef7f6d;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-09-btn');
const track = document.getElementById('lb-09-track');
const fill = document.getElementById('lb-09-fill');
const pct = document.getElementById('lb-09-pct');
const label = document.getElementById('lb-09-label');
const cancel = document.getElementById('lb-09-cancel');
const live = document.getElementById('lb-09-live');
const alertBox = document.getElementById('lb-09-alert');
const unknown = document.getElementById('lb-09-unknown');
const marks = [25, 50, 75];
let tick;
let reset;

const stop = () => { clearInterval(tick); clearTimeout(reset); };
const idle = () => {
  btn.dataset.state = 'idle';
  btn.setAttribute('aria-busy', 'false');
  label.textContent = 'Start upload';
  pct.textContent = '';
  cancel.hidden = true;
  track.removeAttribute('data-mode');
  track.removeAttribute('data-state');
  fill.style.inlineSize = '0%';
  track.setAttribute('aria-valuenow', '0');
};

btn.addEventListener('click', () => {
  if (btn.dataset.state === 'pending') return;
  stop();
  alertBox.textContent = '';
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  cancel.hidden = false;
  if (unknown.checked) {
    track.dataset.mode = 'indeterminate';
    track.removeAttribute('aria-valuenow');
    label.textContent = 'Uploading';
    pct.textContent = '';
    live.textContent = 'Uploading, total size unknown';
    reset = setTimeout(() => { btn.dataset.state = 'error'; btn.setAttribute('aria-busy', 'false'); label.textContent = 'Retry upload'; alertBox.textContent = 'Upload rejected: file exceeds the 10 MB limit.'; cancel.hidden = true; track.dataset.state = 'error'; }, 2600);
    return;
  }
  let p = 0;
  label.textContent = 'Uploading';
  tick = setInterval(() => {
    p += 5;
    fill.style.inlineSize = p + '%';
    pct.textContent = p + '%';
    track.setAttribute('aria-valuenow', String(p));
    if (marks.includes(p)) live.textContent = 'Upload ' + p + ' percent complete';
    if (p >= 100) {
      clearInterval(tick);
      btn.dataset.state = 'done';
      btn.setAttribute('aria-busy', 'false');
      label.textContent = 'Uploaded';
      cancel.hidden = true;
      live.textContent = 'Upload complete';
      reset = setTimeout(idle, 2200);
    }
  }, 220);
});

cancel.addEventListener('click', () => { stop(); idle(); live.textContent = 'Upload cancelled.'; });
```
