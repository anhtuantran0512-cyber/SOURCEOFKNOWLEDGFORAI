---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/wcag-2-2-accessible-progress-bar-with-role-progressbar-semantics/"
title: "WCAG 2.2 Accessible Progress Bar with role progressbar Semantics"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The reference implementation, annotated: every required and recommended ARIA attribute labelled in a side panel, a live region that echoes what a screen…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: WCAG 2.2 Accessible Progress Bar with role progressbar Semantics
Source: https://codefronts.com/components/css-progress-bars/wcag-2-2-accessible-progress-bar-with-role-progressbar-semantics/

The reference implementation, annotated: every required and recommended ARIA attribute labelled in a side panel, a live region that echoes what a screen reader would say, and a focus indicator built to WCAG 2.2's 2.4.13 focus-appearance rules. Copy this one when an audit is coming.
## HTML
```html
<div class="pb-09">
  <button class="pb-09__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-09__stage">
    <div class="pb-09__card">
      <header class="pb-09__head">
        <p class="pb-09__eyebrow"><span class="pb-09__badge">WCAG 2.2 AA</span><span class="pb-09__mono">1.4.1 &middot; 1.4.3 &middot; 1.4.11 &middot; 2.4.13 &middot; 4.1.2</span></p>
        <h2 class="pb-09__title" id="pb-09-h">Project archive upload</h2>
      </header>

      <div class="pb-09__main">
        <div class="pb-09__barBlock">
          <p class="pb-09__row">
            <output class="pb-09__out pb-09__mono" id="pb-09-out" for="pb-09-bar">45</output>
            <span class="pb-09__ofText" id="pb-09-of">of 100 MB uploaded</span>
          </p>
          <div class="pb-09__bar" id="pb-09-bar" tabindex="0" role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" aria-valuetext="45 of 100 megabytes uploaded" aria-labelledby="pb-09-h" aria-describedby="pb-09-hint" style="--value:45">
            <span class="pb-09__fill"></span>
          </div>
          <p class="pb-09__hint" id="pb-09-hint">Resumes automatically if the connection drops.</p>

          <div class="pb-09__controls">
            <button class="pb-09__btn" type="button" id="pb-09-minus">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12h12" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
              <span>Back 15</span>
            </button>
            <button class="pb-09__btn pb-09__btn--primary" type="button" id="pb-09-plus">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 6v12M6 12h12" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
              <span>Advance 15</span>
            </button>
          </div>

          <p class="pb-09__srBox"><span class="pb-09__srLabel">Screen reader hears</span><span class="pb-09__srText" id="pb-09-sr">Project archive upload, progress bar, 45 of 100 megabytes uploaded</span></p>
          <p class="pb-09__live" id="pb-09-live" role="status" aria-live="polite"></p>
        </div>

        <aside class="pb-09__ann" aria-label="Attribute reference">
          <p class="pb-09__annHead pb-09__mono">Attribute map</p>
          <ul class="pb-09__annList">
            <li><code>role="progressbar"</code><span class="pb-09__req">required</span><span class="pb-09__why">declares the widget</span></li>
            <li><code>aria-valuenow</code><span class="pb-09__req">required</span><span class="pb-09__why">the current value; omit it and the bar is indeterminate</span></li>
            <li><code>aria-valuemin</code><span class="pb-09__req">required</span><span class="pb-09__why">the floor of the scale</span></li>
            <li><code>aria-valuemax</code><span class="pb-09__req">required</span><span class="pb-09__why">the ceiling of the scale</span></li>
            <li><code>aria-valuetext</code><span class="pb-09__rec">recommended</span><span class="pb-09__why">human-readable form: bytes, steps, time left</span></li>
            <li><code>aria-labelledby</code><span class="pb-09__rec">recommended</span><span class="pb-09__why">what is being measured, from a visible heading</span></li>
            <li><code>aria-describedby</code><span class="pb-09__opt">optional</span><span class="pb-09__why">extra context that is not the name</span></li>
          </ul>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-09 {
  --bg: #f7f8fa;
  --card: #ffffff;
  --card2: #f4f6f9;
  --ink: #101418;
  --muted: rgba(16,20,24,.62);
  --line: rgba(16,20,24,.13);
  --track: rgba(16,20,24,.09);
  --accent: #1d4ed8;
  --focus: #1d4ed8;
  --ok: #047857;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.pb-09 *,
.pb-09 *::before,
.pb-09 *::after {
  box-sizing: border-box;
}

.pb-09__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
}

.pb-09__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(16,20,24,.05);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-09__theme:hover {
  transform: translateY(-1px);
}

.pb-09__theme:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.pb-09__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-09__sun {
  display: block;
}

.pb-09__moon {
  display: none;
}

.pb-09__card {
  inline-size: min(56rem,100%);
  display: grid;
  gap: clamp(1rem,2.4vw,1.6rem);
  padding: clamp(1.3rem,3.2vw,2.2rem);
  border-radius: 1.25rem;
  border: 1px solid var(--line);
  background: var(--card);
  box-shadow: 0 1px 2px rgba(16,20,24,.05),0 24px 50px -38px rgba(16,20,24,.4);
}

.pb-09__head {
  display: grid;
  gap: .4rem;
}

.pb-09__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  align-items: center;
}

.pb-09__badge {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .11em;
  text-transform: uppercase;
  padding: .28rem .55rem;
  border-radius: .4rem;
  color: var(--ok);
  background: color-mix(in srgb,var(--ok) 10%,transparent);
  border: 1px solid color-mix(in srgb,var(--ok) 30%,transparent);
}

.pb-09__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-09__title {
  margin: 0;
  font-size: clamp(1.3rem,3vw,1.8rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 650;
}

.pb-09__main {
  display: grid;
  grid-template-columns: minmax(16rem,1fr) minmax(15rem,20rem);
  gap: clamp(1rem,2.6vw,1.8rem);
  align-items: start;
}

.pb-09__barBlock {
  display: grid;
  gap: .6rem;
}

.pb-09__row {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .5rem;
}

.pb-09__out {
  font-size: clamp(2rem,5vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.035em;
  color: var(--ink);
}

.pb-09__ofText {
  font-size: .88rem;
  color: var(--muted);
}

.pb-09__bar {
  position: relative;
  inline-size: 100%;
  block-size: 1rem;
  border-radius: 99px;
  overflow: hidden;
  background: var(--track);
  border: 1px solid var(--line);
  box-shadow: 0 1px 2px rgba(16,20,24,.12) inset;
}

.pb-09__bar:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.pb-09__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: var(--accent);
  transition: inline-size .35s cubic-bezier(.4,0,.2,1);
}

.pb-09__hint {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
}

.pb-09__controls {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  margin-block-start: .2rem;
}

.pb-09__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  min-inline-size: 2.75rem;
  padding: .65rem 1.05rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: var(--card2);
  color: var(--ink);
  font: inherit;
  font-size: .88rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s,transform .18s;
}

.pb-09__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.pb-09__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 7%,transparent);
}

.pb-09__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.pb-09__btn--primary {
  background: var(--accent);
  border-color: transparent;
  color: #fff;
}

.pb-09__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 86%,black);
}

.pb-09__srBox {
  margin: 0;
  display: grid;
  gap: .25rem;
  padding: .75rem .9rem;
  border-radius: .85rem;
  border: 1px dashed color-mix(in srgb,var(--accent) 40%,transparent);
  background: color-mix(in srgb,var(--accent) 6%,transparent);
}

.pb-09__srLabel {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.pb-09__srText {
  font-size: .86rem;
  line-height: 1.55;
  color: var(--ink);
}

.pb-09__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .8rem;
  font-weight: 600;
  color: var(--ok);
}

.pb-09__ann {
  display: grid;
  gap: .5rem;
  padding: clamp(.9rem,2.2vw,1.2rem);
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  background: var(--card2);
}

.pb-09__annHead {
  margin: 0;
  letter-spacing: .11em;
  text-transform: uppercase;
  font-size: .64rem;
}

.pb-09__annList {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0;
}

.pb-09__annList li {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: .2rem .6rem;
  padding-block: .6rem;
  border-block-start: 1px solid var(--line);
}

.pb-09__annList code {
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--ink);
}

.pb-09__annList .pb-09__why {
  grid-column: 1 / -1;
  font-size: .76rem;
  line-height: 1.5;
  color: var(--muted);
}

.pb-09__req,
.pb-09__rec,
.pb-09__opt {
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .09em;
  text-transform: uppercase;
  padding: .18rem .38rem;
  border-radius: .3rem;
  align-self: start;
}

.pb-09__req {
  color: #b91c1c;
  background: rgba(185,28,28,.1);
  border: 1px solid rgba(185,28,28,.3);
}

.pb-09__rec {
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 10%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 30%,transparent);
}

.pb-09__opt {
  color: var(--muted);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  border: 1px solid var(--line);
}

.pb-09[data-theme="dark"] {
  --bg: #0c0e11;
  --card: #13161b;
  --card2: #181c22;
  --ink: #eef1f5;
  --muted: rgba(238,241,245,.64);
  --line: rgba(238,241,245,.14);
  --track: rgba(238,241,245,.1);
  --accent: #7aa2ff;
  --focus: #a8c1ff;
  --ok: #4ade80;
}

.pb-09[data-theme="dark"] .pb-09__theme {
  background: rgba(255,255,255,.07);
}

.pb-09[data-theme="dark"] .pb-09__sun {
  display: none;
}

.pb-09[data-theme="dark"] .pb-09__moon {
  display: block;
}

.pb-09[data-theme="dark"] .pb-09__btn--primary {
  color: #0b1020;
}

.pb-09[data-theme="dark"] .pb-09__req {
  color: #fca5a5;
  background: rgba(252,165,165,.12);
  border-color: rgba(252,165,165,.32);
}

@media (prefers-color-scheme: dark) {
  .pb-09:not([data-theme="light"]) {
    --bg: #0c0e11;
    --card: #13161b;
    --card2: #181c22;
    --ink: #eef1f5;
    --muted: rgba(238,241,245,.64);
    --line: rgba(238,241,245,.14);
    --track: rgba(238,241,245,.1);
    --accent: #7aa2ff;
    --focus: #a8c1ff;
    --ok: #4ade80;
  }

  .pb-09:not([data-theme="light"]) .pb-09__theme {
    background: rgba(255,255,255,.07);
  }

  .pb-09:not([data-theme="light"]) .pb-09__sun {
    display: none;
  }

  .pb-09:not([data-theme="light"]) .pb-09__moon {
    display: block;
  }

  .pb-09:not([data-theme="light"]) .pb-09__btn--primary {
    color: #0b1020;
  }

  .pb-09:not([data-theme="light"]) .pb-09__req {
    color: #fca5a5;
    background: rgba(252,165,165,.12);
    border-color: rgba(252,165,165,.32);
  }
}

@media (max-width: 48rem) {
  .pb-09__main {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-09 *,
    .pb-09 *::before,
    .pb-09 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-09__card,
    .pb-09__bar,
    .pb-09__btn,
    .pb-09__ann,
    .pb-09__theme,
    .pb-09__srBox {
    border-color: CanvasText;
    box-shadow: none;
  }

  .pb-09__fill {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb09 = document.querySelector('.pb-09');
if (pb09) {
  const q = (s) => pb09.querySelector(s);
  const [bar, out, sr, live] = ['#pb-09-bar','#pb-09-out','#pb-09-sr','#pb-09-live'].map(q);
  const MAX = 100;
  let value = 45, announced = 45;
  const set = (v) => {
    value = Math.max(0, Math.min(MAX, v));
    const text = value + ' of ' + MAX + ' megabytes uploaded';
    bar.style.setProperty('--value', value);
    bar.setAttribute('aria-valuenow', value);
    bar.setAttribute('aria-valuetext', text);
    out.textContent = value;
    sr.textContent = 'Project archive upload, progress bar, ' + text;
    if (Math.abs(value - announced) >= 25 || value === MAX || value === 0) {
      announced = value;
      live.textContent = value === MAX ? 'Upload complete, 100 megabytes.' : value + ' percent uploaded.';
    }
  };
  q('#pb-09-plus').addEventListener('click', () => set(value + 15));
  q('#pb-09-minus').addEventListener('click', () => set(value - 15));
  bar.addEventListener('keydown', (e) => {
    const step = { ArrowRight: 5, ArrowUp: 5, ArrowLeft: -5, ArrowDown: -5 }[e.key];
    if (step) { e.preventDefault(); set(value + step); }
    else if (e.key === 'Home') { e.preventDefault(); set(0); }
    else if (e.key === 'End') { e.preventDefault(); set(MAX); }
  });
  q('.pb-09__theme').addEventListener('click', (e) => {
    const dark = pb09.dataset.theme !== 'dark';
    pb09.dataset.theme = dark ? 'dark' : 'light';
    e.currentTarget.setAttribute('aria-pressed', String(dark));
  });
  set(value);
}
```
