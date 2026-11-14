---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/css-gradient-progress-loading-bar/"
title: "CSS Gradient Progress & Loading Bar"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A download-manager screen with every progress pattern that matters: determinate gradient bars with animated shimmer, a barber-pole indeterminate loader, and…"
has_js: "true"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Progress & Loading Bar
Source: https://codefronts.com/design-styles/css-gradient-ui/css-gradient-progress-loading-bar/

A download-manager screen with every progress pattern that matters: determinate gradient bars with animated shimmer, a barber-pole indeterminate loader, and conic-gradient progress rings — plus 8 lines of optional JS that animate the demo values.
## HTML
```html
<div class="cgu-06-group">
<section class="cgu-06" aria-label="CSS gradient progress and loading bar demos">
  <div class="cgu-06__inner">
    <header class="cgu-06__head">
      <p class="cgu-06__eyebrow">06 · Progress &amp; loading</p>
      <h2 class="cgu-06__title">Every progress pattern, one screen</h2>
      <p class="cgu-06__sub">Determinate bars, an indeterminate barber-pole, and conic donut rings — all driven by one <code>--p</code> custom property.</p>
    </header>
    <div class="cgu-06__panel">
      <div class="cgu-06__bars">
        <div class="cgu-06__job" id="cgu-06-job1" style="--p:72">
          <div class="cgu-06__jobrow"><span class="cgu-06__file">design-tokens.zip</span><span class="cgu-06__pct" data-pct>72%</span></div>
          <div class="cgu-06__track" role="progressbar" aria-label="design-tokens.zip download" aria-valuemin="0" aria-valuemax="100" aria-valuenow="72"><div class="cgu-06__fill cgu-06__fill--aurora"></div></div>
        </div>
        <div class="cgu-06__job" id="cgu-06-job2" style="--p:38">
          <div class="cgu-06__jobrow"><span class="cgu-06__file">component-library.fig</span><span class="cgu-06__pct" data-pct>38%</span></div>
          <div class="cgu-06__track" role="progressbar" aria-label="component-library.fig download" aria-valuemin="0" aria-valuemax="100" aria-valuenow="38"><div class="cgu-06__fill cgu-06__fill--sunset"></div></div>
        </div>
        <div class="cgu-06__job">
          <div class="cgu-06__jobrow"><span class="cgu-06__file">Indexing assets…</span><span class="cgu-06__pct">—</span></div>
          <div class="cgu-06__track" role="progressbar" aria-label="Indexing assets"><div class="cgu-06__pole"></div></div>
        </div>
      </div>
      <div class="cgu-06__rings">
        <figure class="cgu-06__ringbox" id="cgu-06-ring1" style="--p:64">
          <div class="cgu-06__ring cgu-06__ring--cyan" role="progressbar" aria-label="Storage used" aria-valuemin="0" aria-valuemax="100" aria-valuenow="64"><span class="cgu-06__ringpct" data-pct>64%</span></div>
          <figcaption class="cgu-06__ringcap">Storage</figcaption>
        </figure>
        <figure class="cgu-06__ringbox" id="cgu-06-ring2" style="--p:89">
          <div class="cgu-06__ring cgu-06__ring--pink" role="progressbar" aria-label="Sync complete" aria-valuemin="0" aria-valuemax="100" aria-valuenow="89"><span class="cgu-06__ringpct" data-pct>89%</span></div>
          <figcaption class="cgu-06__ringcap">Sync</figcaption>
        </figure>
      </div>
    </div>
    <p class="cgu-06__foot">The JS below only animates the demo numbers — in production, set <code>--p</code> and <code>aria-valuenow</code> from real events.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-06-group {
  display: block;
  width: 100%;
}

.cgu-06,
.cgu-06 *,
.cgu-06 *::before,
.cgu-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-06 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: linear-gradient(200deg,#0d1020 0%,#0a0c14 70%);
}

.cgu-06__inner {
  width: min(880px,100%);
  display: grid;
  gap: 36px;
}

.cgu-06__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-06__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #38bdf8;
}

.cgu-06__title {
  font-size: clamp(27px,4vw,44px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  text-wrap: balance;
}

.cgu-06__sub {
  max-width: 56ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
}

.cgu-06__sub code,
.cgu-06__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12.5px;
  color: #7dd3fc;
  background: rgba(56,189,248,.1);
  padding: 1px 5px;
  border-radius: 5px;
}

.cgu-06__panel {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 26px;
  padding: 30px;
  border-radius: 22px;
  border: 1px solid rgba(255,255,255,.07);
  background: rgba(255,255,255,.028);
}

.cgu-06__bars {
  display: grid;
  gap: 24px;
  align-content: center;
}

.cgu-06__job {
  display: grid;
  gap: 9px;
}

.cgu-06__jobrow {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.cgu-06__file {
  font-size: 14px;
  font-weight: 650;
}

.cgu-06__pct {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12.5px;
  color: #8b90b0;
  font-variant-numeric: tabular-nums;
}

.cgu-06__track {
  height: 10px;
  border-radius: 9999px;
  background: #1a1e33;
  overflow: hidden;
}

.cgu-06__fill {
  position: relative;
  height: 100%;
  width: calc(var(--p) * 1%);
  border-radius: inherit;
  transition: width .5s cubic-bezier(.3,.8,.3,1);
}

.cgu-06__fill--aurora {
  background: linear-gradient(90deg,#22d3ee,#818cf8,#e879f9);
}

.cgu-06__fill--sunset {
  background: linear-gradient(90deg,#fbbf24,#fb7185);
}

.cgu-06__fill::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg,transparent 20%,rgba(255,255,255,.45) 50%,transparent 80%);
  background-size: 200% 100%;
  animation: cgu06-shimmer 1.6s linear infinite;
}

.cgu-06__pole {
  height: 100%;
  width: 100%;
  border-radius: inherit;
  background: repeating-linear-gradient(-55deg,#818cf8 0 14px,#4547a9 14px 28px);
  background-size: 200% 100%;
  animation: cgu06-pole 1.1s linear infinite;
}

.cgu-06__rings {
  display: flex;
  gap: 22px;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  border-left: 1px solid rgba(255,255,255,.06);
  padding-left: 26px;
}

.cgu-06__ringbox {
  display: grid;
  gap: 10px;
  justify-items: center;
}

.cgu-06__ring {
  --c1: #22d3ee;
  --c2: #818cf8;
  position: relative;
  width: 112px;
  aspect-ratio: 1;
  border-radius: 50%;
  display: grid;
  place-items: center;
}

.cgu-06__ring::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(var(--c1) 0,var(--c2) calc(var(--p) * 1%),#1e2338 0);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 10px),#000 calc(100% - 9px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 10px),#000 calc(100% - 9px));
}

.cgu-06__ring--pink {
  --c1: #fbbf24;
  --c2: #fb7185;
}

.cgu-06__ringpct {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 19px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cgu-06__ringcap {
  font-size: 12.5px;
  color: #8b90b0;
}

.cgu-06__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
}

@keyframes cgu06-shimmer {
  to {
    background-position: -200% 0;
  }
}

@keyframes cgu06-pole {
  to {
    background-position: -56px 0;
  }
}

@media (max-width: 640px) {
  .cgu-06__panel {
    grid-template-columns: 1fr;
  }

  .cgu-06__rings {
    border-left: none;
    padding-left: 0;
    padding-top: 22px;
    border-top: 1px solid rgba(255,255,255,.06);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-06__fill::after,
    .cgu-06__pole {
    animation: none;
  }

  .cgu-06__fill {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  // Demo ticker only: eases each --p toward a new random target every few seconds.
  const items = ['cgu-06-job1','cgu-06-job2','cgu-06-ring1','cgu-06-ring2'].map(id => document.getElementById(id)).filter(Boolean);
  if (!items.length || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const state = items.map(el => ({ el, p: parseFloat(getComputedStyle(el).getPropertyValue('--p')) || 50, t: 0 }));
  const retarget = s => { s.t = 20 + Math.random() * 78; };
  state.forEach(retarget);
  setInterval(() => { state.forEach(retarget); }, 3800);
  (function tick(){
    state.forEach(s => {
      s.p += (s.t - s.p) * 0.04;
      const v = Math.round(s.p);
      s.el.style.setProperty('--p', s.p.toFixed(1));
      const label = s.el.querySelector('[data-pct]'); if (label) label.textContent = v + '%';
      const bar = s.el.querySelector('[role="progressbar"]') || s.el; bar.setAttribute('aria-valuenow', v);
    });
    requestAnimationFrame(tick);
  })();
})();
```
