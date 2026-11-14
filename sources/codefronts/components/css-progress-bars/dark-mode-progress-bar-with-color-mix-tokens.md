---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/dark-mode-progress-bar-with-color-mix-tokens/"
title: "Dark Mode Progress Bar with color-mix Tokens"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "One bar, two themes, no duplicated rules: the track is color-mix(in oklab, currentColor 15%, transparent) and the fill is the accent mixed with a touch of…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Progress Bar with color-mix Tokens
Source: https://codefronts.com/components/css-progress-bars/dark-mode-progress-bar-with-color-mix-tokens/

One bar, two themes, no duplicated rules: the track is color-mix(in oklab, currentColor 15%, transparent) and the fill is the accent mixed with a touch of white, so both re-derive themselves from whatever colour the surface inherits. Light and dark cards render side by side to prove it.
## HTML
```html
<div class="pb-08">
  <button class="pb-08__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-08__stage">
    <header class="pb-08__intro">
      <p class="pb-08__eyebrow"><span class="pb-08__badge">Tokens</span><span class="pb-08__mono">color-mix(in oklab, …)</span></p>
      <h2 class="pb-08__title">One bar. Both themes. No duplicate rules.</h2>
      <p class="pb-08__lead">Both cards below use the same three declarations. The track is derived from <code>currentColor</code>, the fill from <code>--accent</code> — so the surface decides how the bar looks, not a second stylesheet.</p>
    </header>

    <div class="pb-08__pair">
      <section class="pb-08__surface pb-08__surface--light" aria-labelledby="pb-08-h-l">
        <p class="pb-08__surfaceHead"><span id="pb-08-h-l">Light surface</span><span class="pb-08__mono">color:#0c1020</span></p>
        <p class="pb-08__metric"><span class="pb-08__num" id="pb-08-num-l">64</span><span class="pb-08__unit">% of 20 GB used</span></p>
        <div class="pb-08__bar" role="progressbar" aria-valuenow="64" aria-valuemin="0" aria-valuemax="100" aria-valuetext="12.8 of 20 gigabytes used" aria-label="Storage used, light surface" style="--value:64"><span class="pb-08__fill"></span></div>
        <p class="pb-08__legend pb-08__mono">track = currentColor 15%</p>
      </section>

      <section class="pb-08__surface pb-08__surface--dark" aria-labelledby="pb-08-h-d">
        <p class="pb-08__surfaceHead"><span id="pb-08-h-d">Dark surface</span><span class="pb-08__mono">color:#e8eaf2</span></p>
        <p class="pb-08__metric"><span class="pb-08__num" id="pb-08-num-d">64</span><span class="pb-08__unit">% of 20 GB used</span></p>
        <div class="pb-08__bar" role="progressbar" aria-valuenow="64" aria-valuemin="0" aria-valuemax="100" aria-valuetext="12.8 of 20 gigabytes used" aria-label="Storage used, dark surface" style="--value:64"><span class="pb-08__fill"></span></div>
        <p class="pb-08__legend pb-08__mono">track = currentColor 15%</p>
      </section>
    </div>

    <div class="pb-08__controls">
      <label class="pb-08__sliderLabel" for="pb-08-range">Value<input class="pb-08__range" id="pb-08-range" type="range" min="0" max="100" value="64" step="1"></label>
      <p class="pb-08__support pb-08__mono" id="pb-08-support">checking color-mix support…</p>
    </div>

    <div class="pb-08__code">
      <p class="pb-08__codeHead"><span class="pb-08__mono">tokens.css</span><span class="pb-08__tagline">fallback first, mix second</span></p>
      <pre><code>.track{
  background:rgba(128,128,128,.15);                              /* fallback */
  background:color-mix(in oklab, currentColor 15%, transparent);
}
.fill{
  background:var(--accent);
  background:color-mix(in oklab, var(--accent) 90%, white 10%);
}</code></pre>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-08 {
  --bg: #080a10;
  --card: #0d1118;
  --ink: #e8eaf2;
  --muted: rgba(232,234,242,.6);
  --line: rgba(232,234,242,.12);
  --accent: #a78bfa;
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

@supports (color: oklch(76% .16 295)) {
  .pb-08 {
    --accent: oklch(76% .16 295);
  }
}

.pb-08 *,
.pb-08 *::before,
.pb-08 *::after {
  box-sizing: border-box;
}

.pb-08__stage {
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(1rem,2.4vw,1.6rem);
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(100% 60% at 50% 0%,color-mix(in srgb,var(--accent) 16%,transparent),transparent 62%);
}

.pb-08__theme {
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

.pb-08__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.11);
}

.pb-08__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-08__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-08__sun {
  display: none;
}

.pb-08__moon {
  display: block;
}

.pb-08[data-theme="light"] .pb-08__sun {
  display: block;
}

.pb-08[data-theme="light"] .pb-08__moon {
  display: none;
}

.pb-08__intro {
  inline-size: min(46rem,100%);
  display: grid;
  gap: .55rem;
}

.pb-08__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  align-items: center;
}

.pb-08__badge {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .28rem .55rem;
  border-radius: .45rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 16%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 32%,transparent);
}

.pb-08__mono {
  font-family: var(--mono);
  font-size: .74rem;
  color: inherit;
  opacity: .75;
  font-variant-numeric: tabular-nums;
}

.pb-08__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,2.15rem);
  line-height: 1.12;
  letter-spacing: -.024em;
  font-weight: 650;
  text-wrap: balance;
}

.pb-08__lead {
  margin: 0;
  max-inline-size: 56ch;
  font-size: clamp(.9rem,1.5vw,1rem);
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-08__lead code {
  font-family: var(--mono);
  font-size: .85em;
  color: var(--accent);
}

.pb-08__pair {
  inline-size: min(46rem,100%);
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
  gap: clamp(.8rem,2vw,1.2rem);
}

.pb-08__surface {
  display: grid;
  gap: .7rem;
  padding: clamp(1.1rem,2.6vw,1.5rem);
  border-radius: 1.25rem;
  border: 1px solid color-mix(in oklab,currentColor 12%,transparent);
  box-shadow: 0 20px 50px -34px rgba(0,0,0,.6);
}

.pb-08__surface--light {
  background: #f7f8fc;
  color: #0c1020;
}

.pb-08__surface--dark {
  background: #0b0e15;
  color: #e8eaf2;
}

.pb-08__surfaceHead {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: space-between;
  align-items: baseline;
  font-size: .82rem;
  font-weight: 600;
}

.pb-08__metric {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .4rem;
}

.pb-08__num {
  font-family: var(--mono);
  font-size: clamp(1.7rem,4vw,2.4rem);
  font-weight: 600;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.pb-08__unit {
  font-size: .8rem;
  opacity: .65;
}

.pb-08__bar {
  position: relative;
  inline-size: 100%;
  block-size: .8rem;
  border-radius: 99px;
  overflow: hidden;
  background: rgba(128,128,128,.15);
  border: 1px solid rgba(128,128,128,.22);
  box-shadow: 0 1px 2px rgba(0,0,0,.18) inset;
}

.pb-08__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: var(--accent);
  transition: inline-size .35s cubic-bezier(.4,0,.2,1);
}

@supports (color: color-mix(in oklab,white 10%,transparent)) {
  .pb-08__bar {
    background: color-mix(in oklab,currentColor 15%,transparent);
    border-color: color-mix(in oklab,currentColor 20%,transparent);
  }

  .pb-08__fill {
    background: color-mix(in oklab,var(--accent) 90%,white 10%);
  }
}

.pb-08__legend {
  margin: 0;
  font-size: .7rem;
  opacity: .6;
}

.pb-08__controls {
  inline-size: min(46rem,100%);
  display: flex;
  flex-wrap: wrap;
  gap: .9rem;
  align-items: center;
  justify-content: space-between;
}

.pb-08__sliderLabel {
  display: flex;
  align-items: center;
  gap: .7rem;
  font-size: .82rem;
  font-weight: 550;
  color: var(--muted);
}

.pb-08__range {
  inline-size: min(18rem,55vw);
  accent-color: var(--accent);
  block-size: 1.6rem;
  cursor: pointer;
}

.pb-08__range:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
  border-radius: 99px;
}

.pb-08__support {
  margin: 0;
  padding: .3rem .55rem;
  border-radius: .45rem;
  border: 1px solid var(--line);
  color: var(--muted);
}

.pb-08__code {
  inline-size: min(46rem,100%);
  border-radius: 1.15rem;
  border: 1px solid var(--line);
  background: #05070c;
  overflow: hidden;
}

.pb-08__codeHead {
  margin: 0;
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  padding: .6rem .9rem;
  border-block-end: 1px solid var(--line);
  color: rgba(232,234,242,.72);
}

.pb-08__tagline {
  font-size: .72rem;
  opacity: .7;
}

.pb-08__code pre {
  margin: 0;
  padding: .95rem .9rem;
  overflow-x: auto;
}

.pb-08__code code {
  font-family: var(--mono);
  font-size: clamp(.68rem,1vw,.8rem);
  line-height: 1.75;
  color: rgba(232,234,242,.8);
  white-space: pre;
}

.pb-08[data-theme="light"] {
  --bg: #f5f6fb;
  --card: #ffffff;
  --ink: #0c1020;
  --muted: rgba(12,16,32,.62);
  --line: rgba(12,16,32,.1);
  --accent: #7c3aed;
}

.pb-08[data-theme="light"] .pb-08__theme {
  background: rgba(12,16,32,.05);
}

@media (prefers-color-scheme: light) {
  .pb-08:not([data-theme="dark"]) {
    --bg: #f5f6fb;
    --card: #ffffff;
    --ink: #0c1020;
    --muted: rgba(12,16,32,.62);
    --line: rgba(12,16,32,.1);
    --accent: #7c3aed;
  }

  .pb-08:not([data-theme="dark"]) .pb-08__theme {
    background: rgba(12,16,32,.05);
  }

  .pb-08:not([data-theme="dark"]) .pb-08__sun {
    display: block;
  }

  .pb-08:not([data-theme="dark"]) .pb-08__moon {
    display: none;
  }

  .pb-08[data-theme="dark"] .pb-08__sun {
    display: none;
  }

  .pb-08[data-theme="dark"] .pb-08__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-08 *,
    .pb-08 *::before,
    .pb-08 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-08__surface,
    .pb-08__bar,
    .pb-08__code,
    .pb-08__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .pb-08__fill {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb08 = document.querySelector('.pb-08');
if (pb08) {
  const range = pb08.querySelector('#pb-08-range');
  const bars = [...pb08.querySelectorAll('.pb-08__bar')];
  const nums = [...pb08.querySelectorAll('.pb-08__num')];
  const GB = 20;
  const paint = (v) => {
    bars.forEach((bar) => {
      bar.style.setProperty('--value', v);
      bar.setAttribute('aria-valuenow', v);
      bar.setAttribute('aria-valuetext', (GB * v / 100).toFixed(1) + ' of ' + GB + ' gigabytes used');
    });
    nums.forEach((n) => { n.textContent = v; });
  };
  range.addEventListener('input', (e) => paint(Number(e.target.value)));
  const ok = CSS.supports('color', 'color-mix(in oklab, white 10%, transparent)');
  pb08.querySelector('#pb-08-support').textContent = ok ? 'color-mix(in oklab) supported \u2713' : 'color-mix unsupported \u2014 rgba fallback active';
  pb08.querySelector('.pb-08__theme').addEventListener('click', (e) => {
    const light = pb08.dataset.theme !== 'light';
    pb08.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  paint(Number(range.value));
}
```
