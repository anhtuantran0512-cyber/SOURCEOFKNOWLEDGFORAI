---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/indeterminate-progress-bar-with-aria-busy-state/"
title: "Indeterminate Progress Bar with aria-busy State"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The bar for work whose length you cannot know yet: a sliding fill sweeping a track on a 1.8s linear loop while aria-busy=\"true\" sits on the container and a…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Indeterminate Progress Bar with aria-busy State
Source: https://codefronts.com/components/css-progress-bars/indeterminate-progress-bar-with-aria-busy-state/

The bar for work whose length you cannot know yet: a sliding fill sweeping a track on a 1.8s linear loop while aria-busy="true" sits on the container and a polite live region announces the state once. Hit Complete and it snaps into a determinate 100% bar — the exact transition production loaders get wrong.
## HTML
```html
<div class="pb-02">
  <button class="pb-02__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-02__stage">
    <div class="pb-02__card">
      <header class="pb-02__head">
        <p class="pb-02__eyebrow"><span class="pb-02__badge">Indeterminate</span><span class="pb-02__mono">duration unknown</span></p>
        <h2 class="pb-02__title">Building preview deployment</h2>
        <p class="pb-02__lead">No total, no percentage, no lying about it. The bar sweeps while <code>aria-busy</code> is true and becomes a real 100% bar the moment the work resolves.</p>
      </header>

      <div class="pb-02__panel" id="pb-02-region" aria-busy="true">
        <p class="pb-02__meta">
          <span class="pb-02__dot" data-state="busy" aria-hidden="true"></span>
          <span class="pb-02__state" id="pb-02-state">Bundling routes</span>
          <span class="pb-02__mono pb-02__elapsed" id="pb-02-elapsed">00:04</span>
        </p>
        <div class="pb-02__track" id="pb-02-track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-labelledby="pb-02-state">
          <span class="pb-02__sweep" id="pb-02-sweep"></span>
          <span class="pb-02__fill" id="pb-02-fill" style="--value:0"></span>
        </div>
        <p class="pb-02__legend">
          <span class="pb-02__pill pb-02__mono" id="pb-02-pill">aria-busy="true"</span>
          <span class="pb-02__pill pb-02__mono" id="pb-02-pill2">aria-valuenow=&lt;absent&gt;</span>
        </p>
      </div>

      <div class="pb-02__controls">
        <button class="pb-02__btn pb-02__btn--primary" type="button" id="pb-02-run">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 3.5v4M12 16.5v4M4.6 12h4M15.4 12h4M6.7 6.7l2.8 2.8M14.5 14.5l2.8 2.8M17.3 6.7l-2.8 2.8M9.5 14.5l-2.8 2.8" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Simulate load
        </button>
        <button class="pb-02__btn" type="button" id="pb-02-done">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5.5 12.8l4.2 4.2L18.6 8" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Complete
        </button>
      </div>

      <p class="pb-02__note">Indeterminate means the <code>value</code> attribute is <strong>absent</strong> — not zero. <code>value="0"</code> is a determinate bar announcing 0%.</p>
      <p class="pb-02__live" id="pb-02-live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-02 {
  --bg: #070a12;
  --card: #0c1120;
  --card2: #111830;
  --ink: #eaf0ff;
  --muted: rgba(234,240,255,.6);
  --line: rgba(234,240,255,.12);
  --track: rgba(234,240,255,.08);
  --accent: #3b82f6;
  --accent-2: #60a5fa;
  --ok: #10b981;
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

@supports (color: oklch(70% .18 260)) {
  .pb-02 {
    --accent: oklch(64% .17 258);
    --accent-2: oklch(74% .14 254);
    --ok: oklch(74% .16 162);
  }
}

.pb-02 *,
.pb-02 *::before,
.pb-02 *::after {
  box-sizing: border-box;
}

.pb-02__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(110% 70% at 50% -10%,color-mix(in srgb,var(--accent) 20%,transparent),transparent 60%), linear-gradient(180deg,transparent,color-mix(in srgb,var(--accent) 6%,transparent));
}

.pb-02__theme {
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

.pb-02__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.11);
}

.pb-02__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-02__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-02__sun {
  display: none;
}

.pb-02__moon {
  display: block;
}

.pb-02[data-theme="light"] .pb-02__sun {
  display: block;
}

.pb-02[data-theme="light"] .pb-02__moon {
  display: none;
}

.pb-02__card {
  inline-size: min(46rem,100%);
  display: grid;
  gap: clamp(1rem,2.4vw,1.6rem);
  padding: clamp(1.3rem,3.4vw,2.4rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 32px 80px -44px rgba(0,0,0,.95);
}

.pb-02__head {
  display: grid;
  gap: .5rem;
}

.pb-02__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .6rem;
  margin: 0;
}

.pb-02__badge {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .28rem .55rem;
  border-radius: .45rem;
  color: var(--accent-2);
  background: color-mix(in srgb,var(--accent) 18%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 34%,transparent);
}

.pb-02__mono {
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-02__title {
  margin: 0;
  font-size: clamp(1.45rem,3.6vw,2.2rem);
  line-height: 1.1;
  letter-spacing: -.022em;
  font-weight: 650;
}

.pb-02__lead {
  margin: 0;
  max-inline-size: 48ch;
  font-size: clamp(.92rem,1.5vw,1.02rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-02__lead code,
.pb-02__note code {
  font-family: var(--mono);
  font-size: .84em;
  color: var(--accent-2);
}

.pb-02__panel {
  display: grid;
  gap: .85rem;
  padding: clamp(1rem,2.4vw,1.4rem);
  border-radius: 1.15rem;
  border: 1px solid var(--line);
  background: var(--card2);
}

.pb-02__meta {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
}

.pb-02__state {
  font-size: .92rem;
  font-weight: 550;
}

.pb-02__elapsed {
  margin-inline-start: auto;
}

.pb-02__dot {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 99px;
  background: var(--accent-2);
  flex: none;
  box-shadow: 0 0 0 0 color-mix(in srgb,var(--accent) 60%,transparent);
  animation: pb-02-ping 1.6s ease-out infinite;
}

.pb-02__dot[data-state="done"] {
  background: var(--ok);
  animation: none;
  box-shadow: 0 0 0 3px color-mix(in srgb,var(--ok) 22%,transparent);
}

@keyframes pb-02-ping {
  0% {
    box-shadow: 0 0 0 0 color-mix(in srgb,var(--accent) 55%,transparent);
  }

  100% {
    box-shadow: 0 0 0 .65rem transparent;
  }
}

.pb-02__track {
  position: relative;
  inline-size: 100%;
  block-size: .65rem;
  border-radius: 99px;
  overflow: hidden;
  background: var(--track);
  border: 1px solid var(--line);
  box-shadow: 0 1px 2px rgba(0,0,0,.4) inset;
}

.pb-02__sweep {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 100%;
  border-radius: 99px;
  transform-origin: left center;
  will-change: transform;
  background: linear-gradient(90deg,transparent,var(--accent) 22%,var(--accent-2) 72%,transparent);
  animation: pb-02-sweep 1.8s cubic-bezier(.65,.05,.36,1) infinite;
}

@keyframes pb-02-sweep {
  0% {
    transform: translateX(-100%) scaleX(.35);
  }

  50% {
    transform: translateX(30%) scaleX(.75);
  }

  100% {
    transform: translateX(240%) scaleX(.4);
  }
}

.pb-02__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent),var(--ok));
  transition: inline-size .35s cubic-bezier(.4,0,.2,1);
  opacity: 0;
}

.pb-02__track[aria-busy="false"] .pb-02__sweep {
  animation: none;
  opacity: 0;
}

.pb-02__track[aria-busy="false"] .pb-02__fill,
.pb-02__panel[aria-busy="false"] .pb-02__fill {
  opacity: 1;
}

.pb-02__legend {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.pb-02__pill {
  padding: .3rem .55rem;
  border-radius: .5rem;
  font-size: .72rem;
  color: var(--ink);
  background: color-mix(in srgb,var(--ink) 7%,transparent);
  border: 1px solid var(--line);
}

.pb-02__controls {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.pb-02__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  padding: .65rem 1.05rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  font: inherit;
  font-size: .88rem;
  font-weight: 550;
  cursor: pointer;
  transition: transform .18s,background .18s,border-color .18s;
}

.pb-02__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.pb-02__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 12%,transparent);
}

.pb-02__btn:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-02__btn--primary {
  background: var(--accent);
  border-color: transparent;
  color: #fff;
  box-shadow: 0 10px 24px -14px var(--accent);
}

.pb-02__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 88%,white);
}

.pb-02__note {
  margin: 0;
  font-size: .82rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-02__live {
  margin: 0;
  font-size: .8rem;
  min-block-size: 1.2rem;
  color: var(--ok);
  font-weight: 550;
}

.pb-02[data-theme="light"] {
  --bg: #f4f6fb;
  --card: #ffffff;
  --card2: #f7f9fd;
  --ink: #0a1024;
  --muted: rgba(10,16,36,.62);
  --line: rgba(10,16,36,.1);
  --track: rgba(10,16,36,.08);
  --accent: #2563eb;
  --accent-2: #1d4ed8;
  --ok: #059669;
}

.pb-02[data-theme="light"] .pb-02__theme {
  background: rgba(10,16,36,.05);
}

@media (prefers-color-scheme: light) {
  .pb-02:not([data-theme="dark"]) {
    --bg: #f4f6fb;
    --card: #ffffff;
    --card2: #f7f9fd;
    --ink: #0a1024;
    --muted: rgba(10,16,36,.62);
    --line: rgba(10,16,36,.1);
    --track: rgba(10,16,36,.08);
    --accent: #2563eb;
    --accent-2: #1d4ed8;
    --ok: #059669;
  }

  .pb-02:not([data-theme="dark"]) .pb-02__theme {
    background: rgba(10,16,36,.05);
  }

  .pb-02:not([data-theme="dark"]) .pb-02__sun {
    display: block;
  }

  .pb-02:not([data-theme="dark"]) .pb-02__moon {
    display: none;
  }

  .pb-02[data-theme="dark"] .pb-02__sun {
    display: none;
  }

  .pb-02[data-theme="dark"] .pb-02__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-02 *,
    .pb-02 *::before,
    .pb-02 *::after {
    animation: none !important;
    transition: none !important;
  }

  .pb-02__sweep {
    background: repeating-linear-gradient(45deg,var(--accent) 0 .5rem,var(--accent-2) .5rem 1rem);
    opacity: .9;
  }
}

@media (forced-colors: active) {
  .pb-02__card,
    .pb-02__panel,
    .pb-02__track,
    .pb-02__btn,
    .pb-02__theme,
    .pb-02__pill {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-02__sweep,
    .pb-02__fill {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb02 = document.querySelector('.pb-02');
if (pb02) {
  const q = (s) => pb02.querySelector(s);
  const [region, track, fill, dot, state, pill, pill2, live, elapsed] =
    ['#pb-02-region','#pb-02-track','#pb-02-fill','.pb-02__dot','#pb-02-state','#pb-02-pill','#pb-02-pill2','#pb-02-live','#pb-02-elapsed'].map(q);
  let timer, t = 4;
  const paint = (busy) => {
    region.setAttribute('aria-busy', String(busy));
    track.setAttribute('aria-busy', String(busy));
    pill.textContent = 'aria-busy="' + busy + '"';
    if (busy) { track.removeAttribute('aria-valuenow'); pill2.textContent = 'aria-valuenow=<absent>'; }
    else { track.setAttribute('aria-valuenow', '100'); pill2.textContent = 'aria-valuenow="100"'; }
  };
  const busy = () => {
    clearInterval(timer); t = 0; fill.style.setProperty('--value', 0);
    dot.dataset.state = 'busy'; state.textContent = 'Bundling routes'; live.textContent = '';
    paint(true);
    timer = setInterval(() => { t += 1; elapsed.textContent = '00:' + String(t).padStart(2, '0'); }, 1000);
  };
  const done = () => {
    clearInterval(timer); paint(false); fill.style.setProperty('--value', 100);
    dot.dataset.state = 'done'; state.textContent = 'Deployment ready';
    live.textContent = 'Deployment ready. Build finished in ' + elapsed.textContent + '.';
  };
  q('#pb-02-run').addEventListener('click', busy);
  q('#pb-02-done').addEventListener('click', done);
  q('.pb-02__theme').addEventListener('click', (e) => {
    const light = pb02.dataset.theme !== 'light';
    pb02.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  busy();
}
```
