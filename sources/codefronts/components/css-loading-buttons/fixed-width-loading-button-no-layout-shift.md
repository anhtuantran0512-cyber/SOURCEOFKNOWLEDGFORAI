---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/fixed-width-loading-button-no-layout-shift/"
title: "Fixed Width Loading Button No Layout Shift"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The width problem stated plainly: Save is narrower than Saving…, so a naive label swap makes the button jump and shoves whatever sits beside it."
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fixed Width Loading Button No Layout Shift
Source: https://codefronts.com/components/css-loading-buttons/fixed-width-loading-button-no-layout-shift/

The width problem stated plainly: Save is narrower than Saving…, so a naive label swap makes the button jump and shoves whatever sits beside it. Three fixes run side by side against the broken control — both labels stacked in one grid cell, a min-inline-size floor in ch units, and reserving the spinner box with visibility instead of display. Pick whichever fits your markup.
## HTML
```html
<div class="lb-02">
  <div class="lb-02__stage">
    <section class="lb-02__lab" aria-labelledby="lb-02-h">
      <header class="lb-02__head">
        <h2 class="lb-02__h" id="lb-02-h">Three ways to stop the jump</h2>
        <p class="lb-02__sub">The chip after each button is the shift detector. Run the request and watch which chips move.</p>
      </header>

      <div class="lb-02__grid">
        <article class="lb-02__case">
          <p class="lb-02__tag lb-02__tag--bad">Broken · label swap</p>
          <div class="lb-02__mount">
            <button class="lb-02__btn lb-02__btn--naive" type="button" data-state="idle" aria-busy="false">
              <span class="lb-02__naivetext">Save</span>
            </button>
            <span class="lb-02__chip">Cancel</span>
          </div>
          <p class="lb-02__note">textContent is replaced, so the box grows by the width of three characters.</p>
        </article>

        <article class="lb-02__case">
          <p class="lb-02__tag">Fix 1 · stacked faces</p>
          <div class="lb-02__mount">
            <button class="lb-02__btn lb-02__btn--stack" type="button" data-state="idle" aria-busy="false">
              <span class="lb-02__faces">
                <span class="lb-02__face lb-02__face--idle">Save</span>
                <span class="lb-02__face lb-02__face--pending">Saving<span class="lb-02__dots" aria-hidden="true"><i></i><i></i><i></i></span></span>
              </span>
            </button>
            <span class="lb-02__chip">Cancel</span>
          </div>
          <p class="lb-02__note">One grid cell holds both labels, so the button is born at the wider measurement.</p>
        </article>

        <article class="lb-02__case">
          <p class="lb-02__tag">Fix 2 · min-inline-size in ch</p>
          <div class="lb-02__mount">
            <button class="lb-02__btn lb-02__btn--ch" type="button" data-state="idle" aria-busy="false">
              <span class="lb-02__chtext">Save</span>
            </button>
            <span class="lb-02__chip">Cancel</span>
          </div>
          <p class="lb-02__note">A 12ch floor absorbs the longer label without measuring anything in pixels.</p>
        </article>

        <article class="lb-02__case">
          <p class="lb-02__tag">Fix 3 · reserved spinner box</p>
          <div class="lb-02__mount">
            <button class="lb-02__btn lb-02__btn--slot" type="button" data-state="idle" aria-busy="false">
              <span class="lb-02__slot" aria-hidden="true"><span class="lb-02__dots"><i></i><i></i><i></i></span></span>
              <span>Save</span>
            </button>
            <span class="lb-02__chip">Cancel</span>
          </div>
          <p class="lb-02__note">visibility: hidden keeps the indicator box in the layout while it is invisible.</p>
        </article>
      </div>

      <div class="lb-02__controls">
        <button class="lb-02__run" type="button" id="lb-02-run">Run request</button>
        <button class="lb-02__run lb-02__run--ghost" type="button" id="lb-02-fail">Run and fail</button>
        <p class="lb-02__live" id="lb-02-live" role="status" aria-live="polite">Idle</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-02 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #1d1b19;
  --surface: #262320;
  --ink: #f5f0e7;
  --muted: #a49a8b;
  --rule: #38332d;
  --amber: #f5a524;
  --bad: #e46a52;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 18px;
}

.lb-02 *,
.lb-02 *::before,
.lb-02 *::after {
  box-sizing: border-box;
}

.lb-02__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-02__lab {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
}

.lb-02__h {
  margin: 0;
  font-size: 21px;
  font-weight: 600;
  letter-spacing: -.02em;
}

.lb-02__sub {
  margin: 8px 0 0;
  font-size: 13px;
  line-height: 1.55;
  color: var(--muted);
  max-inline-size: 46ch;
}

.lb-02__grid {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  margin: 22px 0 18px;
}

.lb-02__case {
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 14px;
}

.lb-02__tag {
  margin: 0 0 12px;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--amber);
}

.lb-02__tag--bad {
  color: var(--bad);
}

.lb-02__mount {
  display: flex;
  align-items: center;
  gap: 8px;
  min-inline-size: 0;
}

.lb-02__chip {
  flex: none;
  font-size: 11.5px;
  color: var(--muted);
  border: 1px dashed var(--rule);
  border-radius: 999px;
  padding: 5px 10px;
}

.lb-02__note {
  margin: 12px 0 0;
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-02__btn {
  appearance: none;
  border: 0;
  background: var(--amber);
  color: #241a06;
  border-radius: 999px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  padding: 0 16px;
  min-block-size: 44px;
  min-inline-size: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  white-space: nowrap;
}

.lb-02__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.lb-02__btn[data-state="pending"] {
  cursor: progress;
}

.lb-02__btn[data-state="error"] {
  background: var(--bad);
  color: #21100b;
}

.lb-02__btn--ch {
  min-inline-size: 12ch;
}

.lb-02__faces {
  display: grid;
  place-items: center;
}

.lb-02__face {
  grid-area: 1 / 1;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
  visibility: hidden;
}

.lb-02__btn[data-state="idle"] .lb-02__face--idle,
.lb-02__btn[data-state="error"] .lb-02__face--idle,
.lb-02__btn[data-state="pending"] .lb-02__face--pending {
  visibility: visible;
}

.lb-02__slot {
  visibility: hidden;
  display: inline-flex;
}

.lb-02__btn--slot[data-state="pending"] .lb-02__slot {
  visibility: visible;
}

.lb-02__dots {
  display: inline-flex;
  align-items: center;
  gap: 3px;
}

.lb-02__dots i {
  inline-size: 4px;
  block-size: 4px;
  border-radius: 50%;
  background: currentColor;
  animation: lb-02-pulse 900ms ease-in-out infinite;
}

.lb-02__dots i:nth-child(2) {
  animation-delay: 150ms;
}

.lb-02__dots i:nth-child(3) {
  animation-delay: 300ms;
}

@keyframes lb-02-pulse {
  0%,
    100% {
    opacity: .3;
    transform: translateY(0);
  }

  50% {
    opacity: 1;
    transform: translateY(-2px);
  }
}

.lb-02__controls {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  border-top: 1px solid var(--rule);
  padding-top: 16px;
  min-inline-size: 0;
}

.lb-02__run {
  appearance: none;
  border: 1px solid var(--ink);
  background: var(--ink);
  color: var(--bg);
  border-radius: 999px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 600;
  padding: 0 16px;
  min-block-size: 44px;
  cursor: pointer;
}

.lb-02__run--ghost {
  background: transparent;
  color: var(--ink);
  border-color: var(--rule);
}

.lb-02__run:focus-visible {
  outline: 2px solid var(--amber);
  outline-offset: 3px;
}

.lb-02__live {
  margin: 0;
  font-size: 12px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-02__dots i {
    animation: none;
    opacity: .85;
  }
}

@media (prefers-color-scheme: light) {
  .lb-02 {
    --bg: #f6f1e8;
    --surface: #ffffff;
    --ink: #241f19;
    --muted: #776d5f;
    --rule: #e3dccf;
    --amber: #b9740c;
    --bad: #b1402c;
  }

  .lb-02__btn {
    color: #fff8ea;
  }

  .lb-02__btn[data-state="error"] {
    color: #fff2ee;
  }
}

[data-theme="light"] .lb-02 {
  --bg: #f6f1e8;
  --surface: #ffffff;
  --ink: #241f19;
  --muted: #776d5f;
  --rule: #e3dccf;
  --amber: #b9740c;
  --bad: #b1402c;
}
```

## JavaScript
```js
const buttons = document.querySelectorAll('.lb-02__btn');
const naive = document.querySelector('.lb-02__naivetext');
const ch = document.querySelector('.lb-02__chtext');
const live = document.getElementById('lb-02-live');
let timer;

const apply = (state) => {
  buttons.forEach((b) => {
    b.dataset.state = state;
    b.setAttribute('aria-busy', String(state === 'pending'));
  });
  naive.textContent = state === 'pending' ? 'Saving…' : state === 'error' ? 'Retry' : 'Save';
  ch.textContent = naive.textContent;
};

const run = (fails) => {
  clearTimeout(timer);
  apply('pending');
  live.textContent = 'Request in flight';
  timer = setTimeout(() => {
    apply(fails ? 'error' : 'idle');
    live.textContent = fails ? 'Request failed — labels show Retry' : 'Request finished';
  }, 1600);
};

document.getElementById('lb-02-run').addEventListener('click', () => run(false));
document.getElementById('lb-02-fail').addEventListener('click', () => run(true));
```
