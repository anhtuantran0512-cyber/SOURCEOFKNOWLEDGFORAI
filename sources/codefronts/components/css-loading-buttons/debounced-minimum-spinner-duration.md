---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/debounced-minimum-spinner-duration/"
title: "Debounced Minimum Spinner Duration"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "A 90 ms response makes a spinner appear and vanish inside three frames, which reads as a glitch rather than progress."
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Debounced Minimum Spinner Duration
Source: https://codefronts.com/components/css-loading-buttons/debounced-minimum-spinner-duration/

A 90 ms response makes a spinner appear and vanish inside three frames, which reads as a glitch rather than progress. The fix is two thresholds: do not show the pending state at all under about 150 ms, and once shown hold it for a floor of about 400 ms. Fire a fast request and a slow one from the same panel and the difference is immediately obvious.
## HTML
```html
<div class="lb-05">
  <div class="lb-05__stage">
    <section class="lb-05__term" aria-labelledby="lb-05-h">
      <header class="lb-05__bar">
        <span class="lb-05__dot" aria-hidden="true"></span>
        <h2 class="lb-05__h" id="lb-05-h">latency lab — sync engine</h2>
      </header>

      <p class="lb-05__sub">Show delay 150ms · minimum visible 400ms. Fire each request and watch whether the stripe appears at all.</p>

      <div class="lb-05__runs">
        <button class="lb-05__btn lb-05__run" type="button" data-ms="90" data-fail="false" data-state="idle" aria-busy="false">
          <span class="lb-05__stripe" aria-hidden="true"></span>
          <span class="lb-05__t">Sync now · 90ms</span>
        </button>
        <button class="lb-05__btn lb-05__run" type="button" data-ms="1400" data-fail="false" data-state="idle" aria-busy="false">
          <span class="lb-05__stripe" aria-hidden="true"></span>
          <span class="lb-05__t">Sync now · 1400ms</span>
        </button>
        <button class="lb-05__btn lb-05__run lb-05__btn--warn" type="button" data-ms="1100" data-fail="true" data-state="idle" aria-busy="false">
          <span class="lb-05__stripe" aria-hidden="true"></span>
          <span class="lb-05__t">Sync now · fails</span>
        </button>
      </div>

      <dl class="lb-05__out">
        <div class="lb-05__pair"><dt>response</dt><dd id="lb-05-ms">—</dd></div>
        <div class="lb-05__pair"><dt>spinner shown</dt><dd id="lb-05-shown">—</dd></div>
        <div class="lb-05__pair"><dt>result</dt><dd id="lb-05-res">—</dd></div>
      </dl>

      <p class="lb-05__live" id="lb-05-live" role="status" aria-live="polite">idle</p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-05 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #07110b;
  --surface: #0c1a11;
  --ink: #c9f5d9;
  --muted: #5f8f72;
  --rule: #1a3524;
  --accent: #35e07f;
  --bad: #ff8a5c;
  font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-05 *,
.lb-05 *::before,
.lb-05 *::after {
  box-sizing: border-box;
}

.lb-05__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-05__term {
  inline-size: 100%;
  max-inline-size: 40rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  padding: 0 0 18px;
}

.lb-05__bar {
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 11px 14px;
  border-block-end: 1px solid var(--rule);
}

.lb-05__dot {
  inline-size: 8px;
  block-size: 8px;
  background: var(--accent);
  flex: none;
}

.lb-05__h {
  margin: 0;
  font-size: 12.5px;
  font-weight: 500;
  letter-spacing: .02em;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-05__sub {
  margin: 16px 14px 0;
  font-size: 12px;
  line-height: 1.65;
  color: var(--muted);
  max-inline-size: 56ch;
}

.lb-05__runs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 16px 14px 0;
  min-inline-size: 0;
}

.lb-05__btn {
  appearance: none;
  position: relative;
  overflow: hidden;
  border: 1px solid var(--accent);
  background: transparent;
  color: var(--accent);
  border-radius: 0;
  font: inherit;
  font-size: 12.5px;
  padding: 0 14px;
  min-block-size: 44px;
  min-inline-size: 0;
  cursor: pointer;
  transition: background 150ms linear, color 150ms linear;
}

.lb-05__btn--warn {
  border-color: var(--bad);
  color: var(--bad);
}

.lb-05__btn:hover {
  background: rgba(53, 224, 127, .08);
}

.lb-05__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.lb-05__btn[data-state="pending"] {
  cursor: progress;
}

.lb-05__btn[data-state="done"] {
  background: var(--accent);
  color: var(--bg);
}

.lb-05__btn[data-state="error"] {
  background: var(--bad);
  color: #1a0d06;
  border-color: var(--bad);
}

.lb-05__t {
  position: relative;
  display: block;
  min-inline-size: 0;
}

.lb-05__stripe {
  position: absolute;
  inset: 0;
  opacity: 0;
  background: repeating-linear-gradient(115deg, currentColor 0 8px, transparent 8px 18px);
}

.lb-05__btn[data-state="pending"] .lb-05__stripe {
  opacity: .32;
  animation: lb-05-march 620ms linear infinite;
}

@keyframes lb-05-march {
  to {
    transform: translateX(18px);
  }
}

.lb-05__out {
  margin: 18px 14px 0;
  display: grid;
  gap: 6px;
  border-block-start: 1px solid var(--rule);
  padding-block-start: 14px;
}

.lb-05__pair {
  display: flex;
  gap: 12px;
  justify-content: space-between;
  font-size: 12px;
  min-inline-size: 0;
}

.lb-05__pair dt {
  color: var(--muted);
  min-inline-size: 0;
}

.lb-05__pair dd {
  margin: 0;
  font-variant-numeric: tabular-nums;
  min-inline-size: 0;
}

.lb-05__live {
  margin: 14px 14px 0;
  font-size: 11.5px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .lb-05__btn[data-state="pending"] .lb-05__stripe {
    animation: none;
    opacity: .4;
  }
}

@media (prefers-color-scheme: light) {
  .lb-05 {
    --bg: #eef4ee;
    --surface: #ffffff;
    --ink: #10281a;
    --muted: #4b7359;
    --rule: #cfe0d4;
    --accent: #0f7a45;
    --bad: #b34a20;
  }
}

[data-theme="light"] .lb-05 {
  --bg: #eef4ee;
  --surface: #ffffff;
  --ink: #10281a;
  --muted: #4b7359;
  --rule: #cfe0d4;
  --accent: #0f7a45;
  --bad: #b34a20;
}
```

## JavaScript
```js
const DELAY = 150;
const FLOOR = 400;
const live = document.getElementById('lb-05-live');
const outMs = document.getElementById('lb-05-ms');
const outShown = document.getElementById('lb-05-shown');
const outRes = document.getElementById('lb-05-res');
let timers = [];

const reset = () => { timers.forEach(clearTimeout); timers = []; };
const set = (btn, state) => {
  btn.dataset.state = state;
  btn.setAttribute('aria-busy', String(state === 'pending'));
};

document.querySelectorAll('.lb-05__run').forEach((btn) => {
  btn.addEventListener('click', () => {
    reset();
    document.querySelectorAll('.lb-05__run').forEach((b) => set(b, 'idle'));
    const ms = Number(btn.dataset.ms);
    const fails = btn.dataset.fail === 'true';
    let shownAt = 0;
    outMs.textContent = ms + 'ms';
    outShown.textContent = 'waiting';
    outRes.textContent = '—';
    live.textContent = 'request sent';
    timers.push(setTimeout(() => { shownAt = performance.now(); set(btn, 'pending'); outShown.textContent = 'yes, after ' + DELAY + 'ms'; }, DELAY));
    timers.push(setTimeout(() => {
      const held = shownAt ? Math.max(0, FLOOR - (performance.now() - shownAt)) : 0;
      if (!shownAt) outShown.textContent = 'no — under threshold';
      timers.push(setTimeout(() => {
        set(btn, fails ? 'error' : 'done');
        outRes.textContent = fails ? 'error · retry available' : 'synced';
        live.textContent = fails ? 'sync failed' : 'sync complete';
        timers.push(setTimeout(() => set(btn, 'idle'), 1600));
      }, held));
    }, ms));
  });
});
```
