---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/speed-test-gauge/"
title: "Speed Test Gauge Progress with Needle and Ticks"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "A 240&deg; speedometer with a logarithmic scale (10 to 1000 Mbps), tick labels on the arc, and a needle that sweeps to the measured value."
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Speed Test Gauge Progress with Needle and Ticks
Source: https://codefronts.com/components/css-progress-bars/speed-test-gauge/

A 240&deg; speedometer with a logarithmic scale (10 to 1000 Mbps), tick labels on the arc, and a needle that sweeps to the measured value. Log scale because the difference between 10 and 50 matters far more to a user than the difference between 900 and 950.
## HTML
```html
<div class="pb-21">
  <button class="pb-21__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-21__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-21__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-21__stage">
    <div class="pb-21__card">
      <header class="pb-21__head">
        <p class="pb-21__eyebrow"><span class="pb-21__badge">Speed test</span><span class="pb-21__mono">London &middot; 3 ms to edge</span></p>
      </header>

      <div class="pb-21__gauge" id="pb-21-gauge" role="progressbar" aria-valuemin="10" aria-valuemax="1000" aria-valuenow="487" aria-valuetext="487 megabits per second download" aria-label="Connection speed">
        <svg viewBox="0 0 200 160" aria-hidden="true" focusable="false">
          <path class="pb-21__arcTrack" d="M32.45 144 A 78 78 0 1 1 167.55 144" pathLength="100"></path>
          <path class="pb-21__arcFill" id="pb-21-arc" d="M32.45 144 A 78 78 0 1 1 167.55 144" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"></path>
          <g id="pb-21-ticks"></g>
        </svg>
        <div class="pb-21__needleWrap" aria-hidden="true"><span class="pb-21__needle" id="pb-21-needle" style="--angle:0"></span><span class="pb-21__hub"></span></div>
        <p class="pb-21__readout">
          <span class="pb-21__val pb-21__mono" id="pb-21-val">487</span>
          <span class="pb-21__unit">Mbps <span id="pb-21-dir">download</span></span>
        </p>
      </div>

      <div class="pb-21__dirs" role="group" aria-label="Direction">
        <button class="pb-21__dirBtn" type="button" id="pb-21-down" aria-pressed="true">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13M6.8 12.2 12 17.4l5.2-5.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Download
        </button>
        <button class="pb-21__dirBtn" type="button" id="pb-21-up" aria-pressed="false">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 19.5v-13M6.8 11.8 12 6.6l5.2 5.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Upload
        </button>
      </div>

      <div class="pb-21__sub">
        <p class="pb-21__subItem"><span class="pb-21__subKey">Ping</span><span class="pb-21__subVal pb-21__mono">8 ms</span></p>
        <p class="pb-21__subItem"><span class="pb-21__subKey">Jitter</span><span class="pb-21__subVal pb-21__mono">1.4 ms</span></p>
        <p class="pb-21__subItem"><span class="pb-21__subKey">Loss</span><span class="pb-21__subVal pb-21__mono">0.0%</span></p>
      </div>

      <button class="pb-21__btn" type="button" id="pb-21-retest">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.2v5.4M12 4.2 8.6 7.6M12 4.2l3.4 3.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.4 11.2a6.9 6.9 0 1 0 6.6-5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>Test again
      </button>
      <p class="pb-21__live" id="pb-21-live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-21 {
  --bg: #04060a;
  --card: #0a0e15;
  --ink: #e8f0fb;
  --muted: rgba(232,240,251,.58);
  --line: rgba(232,240,251,.12);
  --track: rgba(232,240,251,.1);
  --accent: #38bdf8;
  --accent-2: #a78bfa;
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

@supports (color: oklch(78% .13 220)) {
  .pb-21 {
    --accent: oklch(78% .13 220);
    --accent-2: oklch(76% .16 295);
  }
}

.pb-21 *,
.pb-21 *::before,
.pb-21 *::after {
  box-sizing: border-box;
}

.pb-21__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(75% 55% at 50% 5%,color-mix(in srgb,var(--accent) 18%,transparent),transparent 62%);
}

.pb-21__theme {
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

.pb-21__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-21__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-21__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-21__sun {
  display: none;
}

.pb-21__moon {
  display: block;
}

.pb-21[data-theme="light"] .pb-21__sun {
  display: block;
}

.pb-21[data-theme="light"] .pb-21__moon {
  display: none;
}

.pb-21__card {
  inline-size: min(32rem,100%);
  display: grid;
  gap: clamp(.9rem,2.4vw,1.3rem);
  justify-items: center;
  padding: clamp(1.4rem,3.6vw,2.3rem);
  border-radius: 1.7rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 90%,transparent);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 38px 90px -48px rgba(0,0,0,.95);
}

.pb-21__head {
  display: grid;
  gap: .3rem;
  justify-items: center;
}

.pb-21__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: center;
  justify-content: center;
}

.pb-21__badge {
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

.pb-21__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-21__gauge {
  position: relative;
  inline-size: min(22rem,82vw);
  aspect-ratio: 200 / 160;
}

.pb-21__gauge svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.pb-21__arcTrack {
  fill: none;
  stroke: var(--track);
  stroke-width: 9;
  stroke-linecap: round;
}

.pb-21__arcFill {
  fill: none;
  stroke: var(--accent);
  stroke-width: 9;
  stroke-linecap: round;
  filter: drop-shadow(0 0 10px color-mix(in srgb,var(--accent) 50%,transparent));
  transition: stroke-dashoffset .9s cubic-bezier(.34,1.2,.64,1);
}

.pb-21__tick {
  fill: var(--muted);
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 600;
  text-anchor: middle;
  font-variant-numeric: tabular-nums;
  transition: fill .3s;
}

.pb-21__tick--on {
  fill: var(--accent);
}

.pb-21__tickMark {
  stroke: var(--track);
  stroke-width: 2.4;
  stroke-linecap: round;
  transition: stroke .3s;
}

.pb-21__tickMark--on {
  stroke: color-mix(in srgb,var(--accent) 70%,transparent);
}

.pb-21__needleWrap {
  position: absolute;
  inset-inline-start: 50%;
  inset-block-start: 0;
  block-size: 65.6%;
  inline-size: 0;
}

.pb-21__needle {
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: 50%;
  inline-size: .22rem;
  block-size: 56%;
  border-radius: .15rem;
  background: linear-gradient(180deg,var(--ink),color-mix(in srgb,var(--ink) 30%,transparent));
  transform-origin: 50% 100%;
  transform: translateX(-50%) rotate(calc(var(--angle,0) * 1deg));
  transition: transform .9s cubic-bezier(.34,1.35,.64,1);
}

.pb-21__hub {
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: 50%;
  translate: -50% 50%;
  inline-size: .85rem;
  block-size: .85rem;
  border-radius: 99px;
  background: var(--ink);
  box-shadow: 0 0 0 4px color-mix(in srgb,var(--accent) 25%,transparent);
}

.pb-21__readout {
  position: absolute;
  inset-block-end: 0;
  inset-inline: 0;
  margin: 0;
  display: grid;
  gap: .05rem;
  justify-items: center;
  pointer-events: none;
}

.pb-21__val {
  font-size: clamp(2.2rem,9vw,3.2rem);
  font-weight: 600;
  letter-spacing: -.04em;
  color: var(--ink);
}

.pb-21__unit {
  font-size: .8rem;
  color: var(--muted);
}

.pb-21__dirs {
  display: flex;
  gap: .4rem;
  padding: .25rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 5%,transparent);
}

.pb-21__dirBtn {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.5rem;
  padding: .5rem .9rem;
  border-radius: .65rem;
  border: 1px solid transparent;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: .84rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s,color .18s;
}

.pb-21__dirBtn svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.pb-21__dirBtn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.pb-21__dirBtn[aria-pressed="true"] {
  background: color-mix(in srgb,var(--accent) 18%,transparent);
  color: var(--ink);
  border-color: color-mix(in srgb,var(--accent) 40%,transparent);
}

.pb-21__sub {
  inline-size: 100%;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
}

.pb-21__subItem {
  margin: 0;
  display: grid;
  gap: .1rem;
  justify-items: center;
  padding: .6rem .4rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.pb-21__subKey {
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.pb-21__subVal {
  font-size: .95rem;
  font-weight: 650;
  color: var(--ink);
}

.pb-21__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  padding: .65rem 1.2rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  font: inherit;
  font-size: .88rem;
  font-weight: 550;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-21__btn svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.pb-21__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 12%,transparent);
}

.pb-21__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-21__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .78rem;
  color: var(--accent);
}

.pb-21[data-theme="light"] {
  --bg: #f4f7fb;
  --card: #ffffff;
  --ink: #08101c;
  --muted: rgba(8,16,28,.6);
  --line: rgba(8,16,28,.1);
  --track: rgba(8,16,28,.09);
  --accent: #0284c7;
  --accent-2: #7c3aed;
}

.pb-21[data-theme="light"] .pb-21__theme {
  background: rgba(8,16,28,.05);
}

@media (prefers-color-scheme: light) {
  .pb-21:not([data-theme="dark"]) {
    --bg: #f4f7fb;
    --card: #ffffff;
    --ink: #08101c;
    --muted: rgba(8,16,28,.6);
    --line: rgba(8,16,28,.1);
    --track: rgba(8,16,28,.09);
    --accent: #0284c7;
    --accent-2: #7c3aed;
  }

  .pb-21:not([data-theme="dark"]) .pb-21__theme {
    background: rgba(8,16,28,.05);
  }

  .pb-21:not([data-theme="dark"]) .pb-21__sun {
    display: block;
  }

  .pb-21:not([data-theme="dark"]) .pb-21__moon {
    display: none;
  }

  .pb-21[data-theme="dark"] .pb-21__sun {
    display: none;
  }

  .pb-21[data-theme="dark"] .pb-21__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-21 *,
    .pb-21 *::before,
    .pb-21 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-21__card,
    .pb-21__btn,
    .pb-21__subItem,
    .pb-21__theme,
    .pb-21__dirs {
    border-color: CanvasText;
    box-shadow: none;
  }

  .pb-21__arcFill {
    stroke: Highlight;
    filter: none;
  }

  .pb-21__arcTrack {
    stroke: GrayText;
  }

  .pb-21__needle,
    .pb-21__hub {
    background: CanvasText;
    box-shadow: none;
  }
}
```

## JavaScript
```js
const pb21 = document.querySelector('.pb-21');
if (pb21) {
  const q = (s) => pb21.querySelector(s);
  const MIN = 10, MAX = 1000, SPAN = 240, TICKS = [10, 25, 50, 100, 250, 500, 1000];
  const [gauge, arc, needle, val, dir, live] = ['#pb-21-gauge','#pb-21-arc','#pb-21-needle','#pb-21-val','#pb-21-dir','#pb-21-live'].map(q);
  const frac = (v) => (Math.log(v) - Math.log(MIN)) / (Math.log(MAX) - Math.log(MIN));
  const angle = (v) => -SPAN / 2 + frac(v) * SPAN;
  let speed = { download: 487, upload: 112 }, mode = 'download';
const CX = 100, CY = 105;
  const at = (v, r) => { const a = (angle(v) - 90) * Math.PI / 180; return [CX + Math.cos(a) * r, CY + Math.sin(a) * r]; };
  q('#pb-21-ticks').innerHTML = TICKS.map((v) => {
    const [x1, y1] = at(v, 70), [x2, y2] = at(v, 63), [tx, ty] = at(v, 52);
    return '<line class="pb-21__tickMark" data-v="' + v + '" x1="' + x1.toFixed(1) + '" y1="' + y1.toFixed(1) + '" x2="' + x2.toFixed(1) + '" y2="' + y2.toFixed(1) + '"></line>' +
      '<text class="pb-21__tick" data-v="' + v + '" x="' + tx.toFixed(1) + '" y="' + (ty + 3.2).toFixed(1) + '">' + v + '</text>';
  }).join('');
  const paint = () => {
    const v = speed[mode], f = frac(v);
    needle.style.setProperty('--angle', angle(v).toFixed(2));
    arc.style.strokeDashoffset = (100 - f * 100).toFixed(2);
    val.textContent = v; dir.textContent = mode;
    gauge.setAttribute('aria-valuenow', v);
    gauge.setAttribute('aria-valuetext', v + ' megabits per second ' + mode);
    pb21.querySelectorAll('.pb-21__tick').forEach((t) => t.classList.toggle('pb-21__tick--on', Number(t.dataset.v) <= v));
    pb21.querySelectorAll('.pb-21__tickMark').forEach((t) => t.classList.toggle('pb-21__tickMark--on', Number(t.dataset.v) <= v));
  };
  const setMode = (m) => {
    mode = m;
    q('#pb-21-down').setAttribute('aria-pressed', String(m === 'download'));
    q('#pb-21-up').setAttribute('aria-pressed', String(m === 'upload'));
    paint(); live.textContent = speed[m] + ' Mbps ' + m + '.';
  };
  q('#pb-21-down').addEventListener('click', () => setMode('download'));
  q('#pb-21-up').addEventListener('click', () => setMode('upload'));
  q('#pb-21-retest').addEventListener('click', () => {
    speed = { download: 180 + Math.round(Math.random() * 760), upload: 40 + Math.round(Math.random() * 260) };
    needle.style.setProperty('--angle', angle(MIN).toFixed(2)); arc.style.strokeDashoffset = 100;
    setTimeout(paint, 220); live.textContent = 'Retesting connection.';
  });
  q('.pb-21__theme').addEventListener('click', (e) => {
    const light = pb21.dataset.theme !== 'light';
    pb21.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  paint();
}
```
