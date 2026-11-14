---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/circular-counter/"
title: "Circular Counter Progress Ring with SVG Stroke Dashoffset"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The hero ring: an SVG circle with pathLength=\"100\" so the dash maths is just the percentage, a number that counts up on requestAnimationFrame, and a soft…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Counter Progress Ring with SVG Stroke Dashoffset
Source: https://codefronts.com/components/css-progress-bars/circular-counter/

The hero ring: an SVG circle with pathLength="100" so the dash maths is just the percentage, a number that counts up on requestAnimationFrame, and a soft accent glow. No circumference calculation anywhere — change the radius and nothing breaks.
## HTML
```html
<div class="pb-19">
  <button class="pb-19__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-19__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-19__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-19__stage">
    <div class="pb-19__card">
      <p class="pb-19__eyebrow"><span class="pb-19__badge">Today</span><span class="pb-19__mono">pathLength="100"</span></p>

      <div class="pb-19__ring" id="pb-19-ring" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-valuetext="0 of 1,600 calories" aria-label="Move goal">
        <svg viewBox="0 0 120 120" aria-hidden="true" focusable="false">
          <circle class="pb-19__trackArc" cx="60" cy="60" r="52" pathLength="100"></circle>
          <circle class="pb-19__arc" id="pb-19-arc" cx="60" cy="60" r="52" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"></circle>
        </svg>
        <p class="pb-19__center">
          <span class="pb-19__num pb-19__mono" id="pb-19-num">0</span>
          <span class="pb-19__unit">of 1,600 kcal</span>
        </p>
      </div>

      <div class="pb-19__meta">
        <p class="pb-19__stat"><span class="pb-19__statNum pb-19__mono" id="pb-19-pct">0%</span><span class="pb-19__statKey">of move goal</span></p>
        <p class="pb-19__stat"><span class="pb-19__statNum pb-19__mono">42</span><span class="pb-19__statKey">min exercise</span></p>
        <p class="pb-19__stat"><span class="pb-19__statNum pb-19__mono">9</span><span class="pb-19__statKey">stand hours</span></p>
      </div>

      <div class="pb-19__controls">
        <button class="pb-19__btn pb-19__btn--primary" type="button" id="pb-19-run">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.2v5.4M12 4.2 8.6 7.6M12 4.2l3.4 3.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.4 11.2a6.9 6.9 0 1 0 6.6-5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>Replay count-up
        </button>
        <button class="pb-19__btn" type="button" id="pb-19-add">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 6v12M6 12h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Log 120 kcal
        </button>
      </div>
      <p class="pb-19__live" id="pb-19-live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-19 {
  --bg: #050608;
  --card: #0b0d12;
  --ink: #eef2f7;
  --muted: rgba(238,242,247,.6);
  --line: rgba(238,242,247,.12);
  --track: rgba(238,242,247,.09);
  --accent: #a3e635;
  --accent-2: #22d3ee;
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

@supports (color: oklch(88% .2 125)) {
  .pb-19 {
    --accent: oklch(88% .2 128);
    --accent-2: oklch(82% .13 199);
  }
}

.pb-19 *,
.pb-19 *::before,
.pb-19 *::after {
  box-sizing: border-box;
}

.pb-19__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(70% 55% at 50% 12%,color-mix(in srgb,var(--accent) 16%,transparent),transparent 62%), radial-gradient(60% 50% at 85% 95%,color-mix(in srgb,var(--accent-2) 14%,transparent),transparent 60%);
}

.pb-19__theme {
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
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-19__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-19__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-19__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-19__sun {
  display: none;
}

.pb-19__moon {
  display: block;
}

.pb-19[data-theme="light"] .pb-19__sun {
  display: block;
}

.pb-19[data-theme="light"] .pb-19__moon {
  display: none;
}

.pb-19__card {
  inline-size: min(30rem,100%);
  display: grid;
  gap: clamp(1rem,2.6vw,1.5rem);
  justify-items: center;
  padding: clamp(1.5rem,4vw,2.5rem);
  border-radius: 1.8rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 90%,transparent);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 40px 90px -50px rgba(0,0,0,.95);
}

.pb-19__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .55rem;
  align-items: center;
  justify-content: center;
}

.pb-19__badge {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .26rem .5rem;
  border-radius: .4rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 14%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 30%,transparent);
}

.pb-19__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-19__ring {
  position: relative;
  inline-size: min(17rem,68vw);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
}

.pb-19__ring svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transform: rotate(-90deg);
  overflow: visible;
}

.pb-19__trackArc {
  fill: none;
  stroke: var(--track);
  stroke-width: 9;
}

.pb-19__arc {
  fill: none;
  stroke: var(--accent);
  stroke-width: 9;
  stroke-linecap: round;
  filter: drop-shadow(0 0 10px color-mix(in srgb,var(--accent) 55%,transparent));
  transition: stroke-dashoffset .85s cubic-bezier(.4,0,.2,1);
}

.pb-19__center {
  margin: 0;
  display: grid;
  gap: .15rem;
  justify-items: center;
  text-align: center;
}

.pb-19__num {
  font-size: clamp(2.6rem,11vw,3.9rem);
  font-weight: 600;
  letter-spacing: -.04em;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.pb-19__unit {
  font-size: .82rem;
  color: var(--muted);
}

.pb-19__meta {
  inline-size: 100%;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
}

.pb-19__stat {
  margin: 0;
  display: grid;
  gap: .1rem;
  justify-items: center;
  padding: .65rem .4rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  text-align: center;
}

.pb-19__statNum {
  font-size: 1.05rem;
  font-weight: 650;
  color: var(--ink);
}

.pb-19__statKey {
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--muted);
}

.pb-19__controls {
  display: flex;
  flex-wrap: wrap;
  gap: .55rem;
  justify-content: center;
}

.pb-19__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  padding: .65rem 1.1rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  font: inherit;
  font-size: .87rem;
  font-weight: 550;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-19__btn svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.pb-19__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 12%,transparent);
}

.pb-19__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-19__btn--primary {
  background: var(--accent);
  border-color: transparent;
  color: #0d1405;
  box-shadow: 0 14px 30px -18px var(--accent);
}

.pb-19__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 88%,white);
}

.pb-19__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .78rem;
  color: var(--accent);
}

.pb-19[data-theme="light"] {
  --bg: #f6f8f4;
  --card: #ffffff;
  --ink: #0d1208;
  --muted: rgba(13,18,8,.6);
  --line: rgba(13,18,8,.1);
  --track: rgba(13,18,8,.09);
  --accent: #4d7c0f;
  --accent-2: #0891b2;
}

.pb-19[data-theme="light"] .pb-19__theme {
  background: rgba(13,18,8,.05);
}

.pb-19[data-theme="light"] .pb-19__btn--primary {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .pb-19:not([data-theme="dark"]) {
    --bg: #f6f8f4;
    --card: #ffffff;
    --ink: #0d1208;
    --muted: rgba(13,18,8,.6);
    --line: rgba(13,18,8,.1);
    --track: rgba(13,18,8,.09);
    --accent: #4d7c0f;
    --accent-2: #0891b2;
  }

  .pb-19:not([data-theme="dark"]) .pb-19__theme {
    background: rgba(13,18,8,.05);
  }

  .pb-19:not([data-theme="dark"]) .pb-19__btn--primary {
    color: #fff;
  }

  .pb-19:not([data-theme="dark"]) .pb-19__sun {
    display: block;
  }

  .pb-19:not([data-theme="dark"]) .pb-19__moon {
    display: none;
  }

  .pb-19[data-theme="dark"] .pb-19__sun {
    display: none;
  }

  .pb-19[data-theme="dark"] .pb-19__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-19 *,
    .pb-19 *::before,
    .pb-19 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-19__card,
    .pb-19__btn,
    .pb-19__stat,
    .pb-19__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .pb-19__arc {
    stroke: Highlight;
    filter: none;
  }

  .pb-19__trackArc {
    stroke: GrayText;
  }
}
```

## JavaScript
```js
const pb19 = document.querySelector('.pb-19');
if (pb19) {
  const q = (s) => pb19.querySelector(s);
  const [ring, arc, num, pct, live] = ['#pb-19-ring','#pb-19-arc','#pb-19-num','#pb-19-pct','#pb-19-live'].map(q);
  const GOAL = 1600;
  let kcal = 1284, raf;
  const ease = (t) => 1 - Math.pow(1 - t, 3);
  const commit = (v) => {
    const p = Math.min(100, Math.round(v / GOAL * 100));
    arc.style.strokeDashoffset = 100 - p;
    ring.setAttribute('aria-valuenow', p);
    ring.setAttribute('aria-valuetext', v.toLocaleString('en-US') + ' of ' + GOAL.toLocaleString('en-US') + ' calories');
    pct.textContent = p + '%';
  };
  const run = () => {
    cancelAnimationFrame(raf);
    commit(kcal);
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) { num.textContent = kcal.toLocaleString('en-US'); return; }
    const start = performance.now();
    const step = (now) => {
      const t = Math.min(1, (now - start) / 900);
      num.textContent = Math.round(ease(t) * kcal).toLocaleString('en-US');
      if (t < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
  };
  q('#pb-19-run').addEventListener('click', run);
  q('#pb-19-add').addEventListener('click', () => {
    kcal = Math.min(GOAL, kcal + 120); run();
    live.textContent = kcal >= GOAL ? 'Move goal reached.' : kcal.toLocaleString('en-US') + ' of 1,600 calories.';
  });
  q('.pb-19__theme').addEventListener('click', (e) => {
    const light = pb19.dataset.theme !== 'light';
    pb19.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  run();
}
```
