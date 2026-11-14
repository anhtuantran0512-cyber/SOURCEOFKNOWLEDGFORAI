---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/disabled-pending-state-button/"
title: "Disabled Pending State Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "Guarding against the double submit: set the disabled property on the element itself, not a class, so the browser blocks the second activation including Enter…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Disabled Pending State Button
Source: https://codefronts.com/components/css-loading-buttons/disabled-pending-state-button/

Guarding against the double submit: set the disabled property on the element itself, not a class, so the browser blocks the second activation including Enter and space. Two buttons run side by side — one properly disabled, one guarded only by a class — with a live counter showing how many requests each one actually fired. The class-only version double posts every time.
## HTML
```html
<div class="lb-03">
  <div class="lb-03__stage">
    <section class="lb-03__panel" aria-labelledby="lb-03-h">
      <h2 class="lb-03__h" id="lb-03-h">Double-submit guard</h2>
      <p class="lb-03__sub">Click each button twice, fast. Then tab to it and hold Enter. The counter is the number of requests that actually left.</p>

      <div class="lb-03__thread">
        <div class="lb-03__avatar" aria-hidden="true">PS</div>
        <div class="lb-03__box">
          <p class="lb-03__author">Priya Sharma</p>
          <p class="lb-03__draft">Shipping the migration behind a flag on Thursday. Anything blocking on your side?</p>
        </div>
      </div>

      <div class="lb-03__cases">
        <div class="lb-03__case">
          <p class="lb-03__ctag">disabled property</p>
          <button class="lb-03__btn" type="button" id="lb-03-good" data-state="idle" aria-busy="false">
            <span class="lb-03__btntext">Post comment</span>
            <span class="lb-03__bar" aria-hidden="true"></span>
          </button>
          <p class="lb-03__count">Requests fired: <output id="lb-03-good-n">0</output></p>
        </div>

        <div class="lb-03__case">
          <p class="lb-03__ctag lb-03__ctag--bad">class only</p>
          <button class="lb-03__btn lb-03__btn--weak" type="button" id="lb-03-bad" data-state="idle" aria-busy="false">
            <span class="lb-03__btntext">Post comment</span>
            <span class="lb-03__bar" aria-hidden="true"></span>
          </button>
          <p class="lb-03__count">Requests fired: <output id="lb-03-bad-n">0</output></p>
        </div>
      </div>

      <p class="lb-03__live" id="lb-03-live" role="status" aria-live="polite">No requests yet.</p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-03 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #eef2f8;
  --surface: #ffffff;
  --ink: #0b2540;
  --muted: #5b7089;
  --rule: #d3dded;
  --accent: #1f5fd0;
  --lock: #94a9c4;
  --bad: #c0392b;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-03 *,
.lb-03 *::before,
.lb-03 *::after {
  box-sizing: border-box;
}

.lb-03__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-03__panel {
  inline-size: 100%;
  max-inline-size: 40rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0;
  padding: 24px 22px;
  box-shadow: inset 0 2px 0 var(--accent);
}

.lb-03__h {
  margin: 0;
  font-size: 20px;
  font-weight: 650;
  letter-spacing: -.015em;
}

.lb-03__sub {
  margin: 8px 0 20px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 52ch;
}

.lb-03__thread {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 14px;
  background: var(--bg);
  border: 1px solid var(--rule);
  min-inline-size: 0;
}

.lb-03__avatar {
  flex: none;
  inline-size: 34px;
  block-size: 34px;
  display: grid;
  place-items: center;
  background: var(--accent);
  color: #fff;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .04em;
}

.lb-03__box {
  min-inline-size: 0;
}

.lb-03__author {
  margin: 0;
  font-size: 12.5px;
  font-weight: 640;
}

.lb-03__draft {
  margin: 5px 0 0;
  font-size: 13px;
  line-height: 1.55;
  color: var(--muted);
}

.lb-03__cases {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  margin: 18px 0 0;
}

.lb-03__case {
  min-inline-size: 0;
}

.lb-03__ctag {
  margin: 0 0 8px;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
}

.lb-03__ctag--bad {
  color: var(--bad);
}

.lb-03__btn {
  appearance: none;
  position: relative;
  overflow: hidden;
  inline-size: 100%;
  border: 0;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  padding: 0 16px;
  min-block-size: 44px;
  min-inline-size: 0;
  cursor: pointer;
  box-shadow: inset 0 -2px 0 rgba(0, 0, 0, .22);
}

.lb-03__btn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

.lb-03__btn:disabled,
.lb-03__btn[data-state="pending"] {
  background: var(--lock);
  color: #f4f8ff;
  cursor: progress;
  box-shadow: inset 0 2px 4px rgba(11, 37, 64, .28);
}

.lb-03__btntext {
  display: block;
  min-inline-size: 0;
}

.lb-03__bar {
  position: absolute;
  inset-block-end: 0;
  inset-inline: 0;
  block-size: 3px;
  opacity: 0;
  overflow: hidden;
}

.lb-03__btn[data-state="pending"] .lb-03__bar {
  opacity: 1;
}

.lb-03__bar::before {
  content: "";
  position: absolute;
  inset-block: 0;
  inline-size: 42%;
  background: #fff;
  animation: lb-03-slide 1s cubic-bezier(.65, .05, .36, 1) infinite;
}

@keyframes lb-03-slide {
  from {
    transform: translateX(-110%);
  }

  to {
    transform: translateX(280%);
  }
}

.lb-03__count {
  margin: 10px 0 0;
  font-size: 12px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.lb-03__count output {
  font-weight: 700;
  color: var(--ink);
}

.lb-03__live {
  margin: 18px 0 0;
  font-size: 12.5px;
  color: var(--muted);
  border-top: 1px solid var(--rule);
  padding-top: 12px;
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-03__bar::before {
    animation: none;
    inline-size: 100%;
    opacity: .55;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-03 {
    --bg: #0e1620;
    --surface: #16202c;
    --ink: #e6eef8;
    --muted: #93a7bf;
    --rule: #26333f;
    --accent: #5b9bff;
    --lock: #3c4c60;
    --bad: #f0806f;
  }

  .lb-03__btn {
    color: #08131f;
  }
}

[data-theme="dark"] .lb-03 {
  --bg: #0e1620;
  --surface: #16202c;
  --ink: #e6eef8;
  --muted: #93a7bf;
  --rule: #26333f;
  --accent: #5b9bff;
  --lock: #3c4c60;
  --bad: #f0806f;
}
```

## JavaScript
```js
const live = document.getElementById('lb-03-live');
const counts = { good: 0, bad: 0 };
const timers = {};

const start = (key, btn, lock) => {
  if (btn.disabled) return;
  counts[key] += 1;
  document.getElementById('lb-03-' + key + '-n').textContent = String(counts[key]);
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  if (lock) btn.disabled = true;
  live.textContent = 'Guarded button fired ' + counts.good + ' request(s); class-only button fired ' + counts.bad + '.';
  clearTimeout(timers[key]);
  timers[key] = setTimeout(() => {
    btn.dataset.state = 'idle';
    btn.setAttribute('aria-busy', 'false');
    btn.disabled = false;
  }, 1500);
};

const good = document.getElementById('lb-03-good');
const bad = document.getElementById('lb-03-bad');
good.addEventListener('click', () => start('good', good, true));
bad.addEventListener('click', () => start('bad', bad, false));
```
