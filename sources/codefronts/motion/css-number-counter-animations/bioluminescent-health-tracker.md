---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/bioluminescent-health-tracker/"
title: "Health Metrics & Heart Rate Animated Display"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A vitals monitor where the animation itself carries the data: the heart glyph, the ECG sweep and the halo all beat at the patient's actual BPM because their…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Health Metrics & Heart Rate Animated Display
Source: https://codefronts.com/motion/css-number-counter-animations/bioluminescent-health-tracker/

A vitals monitor where the animation itself carries the data: the heart glyph, the ECG sweep and the halo all beat at the patient's actual BPM because their animation-duration is computed from a registered custom property. Change one number and every rhythm in the panel retimes — the classic mistake here is animating at a fixed 1s and letting the visual lie about the reading.
## HTML
```html
<section class="cnc-21" aria-label="Health metrics and heart rate animated display demo">
  <div class="cnc-21__stage">
    <article class="cnc-21__panel">
      <header class="cnc-21__head">
        <div>
          <p class="cnc-21__eyebrow">Live vitals · sample data</p>
          <h3 class="cnc-21__title">Morning zone 2 session</h3>
        </div>
        <span class="cnc-21__badge"><i aria-hidden="true"></i>Streaming</span>
      </header>
      <div class="cnc-21__hero">
        <span class="cnc-21__heart" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="34" height="34"><path d="M12 21s-8-4.9-8-10.6A4.8 4.8 0 0 1 12 7a4.8 4.8 0 0 1 8 3.4C20 16.1 12 21 12 21z" fill="currentColor"/></svg>
        </span>
        <p class="cnc-21__bpm"><span class="cnc-21__num" aria-hidden="true">64</span><small>bpm</small></p>
        <p class="cnc-21__zone">Zone <b class="cnc-21__zonen">2</b><span class="cnc-21__zonel">Fat burn</span></p>
      </div>
      <div class="cnc-21__ecg" aria-hidden="true">
        <svg viewBox="0 0 600 120" preserveAspectRatio="none">
          <defs><path id="cnc-21-beat" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" d="M0 60 H18 l5 -8 l5 16 l5 -8 H40 l4 -32 l5 58 l5 -32 H70 l7 -13 l7 13 H100" /></defs>
          <g class="cnc-21__trace">
            <use href="#cnc-21-beat" x="0"/><use href="#cnc-21-beat" x="100"/><use href="#cnc-21-beat" x="200"/>
            <use href="#cnc-21-beat" x="300"/><use href="#cnc-21-beat" x="400"/><use href="#cnc-21-beat" x="500"/>
          </g>
        </svg>
      </div>
      <div class="cnc-21__zones" aria-hidden="true">
        <span data-z="1"></span><span data-z="2"></span><span data-z="3"></span><span data-z="4"></span>
        <i class="cnc-21__marker"></i>
      </div>
      <dl class="cnc-21__grid">
        <div><dt>HRV</dt><dd><span class="cnc-21__hrv">48</span><small>ms</small></dd></div>
        <div><dt>SpO₂</dt><dd><span class="cnc-21__spo">98</span><small>%</small></dd></div>
        <div><dt>Resting</dt><dd><span>54</span><small>bpm</small></dd></div>
        <div><dt>Calories</dt><dd><span class="cnc-21__kcal">128</span><small>kcal</small></dd></div>
      </dl>
      <p class="cnc-21__sr" role="status" aria-live="polite"></p>
    </article>
    <p class="cnc-21__chip" aria-hidden="true">@property &lt;number&gt; · animation-duration: calc(60s / var(--bpm)) · debounced live region</p>
  </div>
</section>
```
## CSS
```css
.cnc-21,
.cnc-21 *,
.cnc-21 *::before,
.cnc-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --cnc-21-bpm {
  syntax: '<number>';
  inherits: true;
  initial-value: 64;
}

.cnc-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-21-bg: oklch(0.16 0.02 255);
  --cnc-21-card: oklch(0.21 0.026 258);
  --cnc-21-ink: oklch(0.97 0.005 250);
  --cnc-21-mut: oklch(0.68 0.02 258);
  --cnc-21-acc: oklch(0.70 0.20 18);
  --cnc-21-cool: oklch(0.80 0.14 195);
  background: var(--cnc-21-bg);
  color: var(--cnc-21-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-21__panel {
  --cnc-21-bpm: 64;
  --cnc-21-zp: 32;
  width: min(100%,460px);
  padding: clamp(18px,4vw,26px);
  border-radius: 26px;
  background: linear-gradient(180deg,color-mix(in oklch,var(--cnc-21-acc) 9%,var(--cnc-21-card)),var(--cnc-21-card));
  box-shadow: 0 0 0 1px oklch(1 0 0/.08),0 30px 70px oklch(0 0 0/.5);
  transition: --cnc-21-bpm 1.1s linear;
}

.cnc-21__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.cnc-21__eyebrow {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--cnc-21-mut);
}

.cnc-21__title {
  margin-top: 5px;
  font-size: 16px;
  font-weight: 660;
  letter-spacing: -.02em;
}

.cnc-21__badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 6px 11px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 640;
  color: var(--cnc-21-cool);
  background: color-mix(in oklch,var(--cnc-21-cool) 14%,transparent);
  white-space: nowrap;
}

.cnc-21__badge i {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  animation: cnc-21-blip calc(60s / var(--cnc-21-bpm)) ease-in-out infinite;
}

@keyframes cnc-21-blip {
  0%,
    70%,
    100% {
    opacity: .35;
  }

  12% {
    opacity: 1;
  }
}

.cnc-21__hero {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-top: 22px;
}

.cnc-21__heart {
  display: grid;
  place-items: center;
  width: 62px;
  height: 62px;
  border-radius: 50%;
  color: var(--cnc-21-acc);
  background: color-mix(in oklch,var(--cnc-21-acc) 16%,transparent);
  animation: cnc-21-beat calc(60s / var(--cnc-21-bpm)) cubic-bezier(.2,.8,.3,1) infinite;
}

@keyframes cnc-21-beat {
  0% {
    transform: scale(1);
    box-shadow: 0 0 0 0 color-mix(in oklch,var(--cnc-21-acc) 45%,transparent);
  }

  14% {
    transform: scale(1.14);
  }

  28% {
    transform: scale(1.02);
  }

  42% {
    transform: scale(1.08);
  }

  70%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 22px color-mix(in oklch,var(--cnc-21-acc) 0%,transparent);
  }
}

.cnc-21__bpm {
  display: flex;
  align-items: baseline;
  gap: 6px;
  font-size: clamp(44px,10vw,62px);
  font-weight: 750;
  letter-spacing: -.055em;
  line-height: .9;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-21__bpm small {
  font-size: 15px;
  font-weight: 640;
  letter-spacing: 0;
  color: var(--cnc-21-mut);
}

.cnc-21__num {
  display: inline-block;
  min-width: 3ch;
  text-align: right;
}

.cnc-21__zone {
  margin-left: auto;
  text-align: right;
  font-size: 12px;
  color: var(--cnc-21-mut);
  line-height: 1.5;
}

.cnc-21__zone b {
  display: block;
  font-size: 20px;
  color: var(--cnc-21-ink);
  font-weight: 730;
}

.cnc-21__zonel {
  display: block;
  font-size: 11.5px;
}

.cnc-21__ecg {
  position: relative;
  height: 96px;
  margin-top: 16px;
  border-radius: 14px;
  overflow: hidden;
  background: radial-gradient(120% 100% at 0% 50%,oklch(0.25 0.03 258),oklch(0.19 0.02 258));
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.06);
}

.cnc-21__ecg svg {
  width: 100%;
  height: 100%;
  display: block;
}

.cnc-21__trace {
  color: var(--cnc-21-acc);
  filter: drop-shadow(0 0 6px color-mix(in oklch,var(--cnc-21-acc) 60%,transparent));
}

.cnc-21__ecg::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 26%;
  background: linear-gradient(90deg,transparent,oklch(1 0 0/.16),transparent);
  animation: cnc-21-sweep calc(60s / var(--cnc-21-bpm) * 6) linear infinite;
}

@keyframes cnc-21-sweep {
  from {
    transform: translateX(-100%);
  }

  to {
    transform: translateX(400%);
  }
}

.cnc-21__zones {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 4px;
  margin-top: 16px;
  height: 10px;
}

.cnc-21__zones span {
  border-radius: 99px;
  background: oklch(1 0 0/.12);
}

.cnc-21__zones span[data-z="1"] {
  background: color-mix(in oklch,var(--cnc-21-cool) 45%,transparent);
}

.cnc-21__zones span[data-z="2"] {
  background: color-mix(in oklch,oklch(0.85 0.17 145) 55%,transparent);
}

.cnc-21__zones span[data-z="3"] {
  background: color-mix(in oklch,oklch(0.84 0.16 80) 50%,transparent);
}

.cnc-21__zones span[data-z="4"] {
  background: color-mix(in oklch,var(--cnc-21-acc) 55%,transparent);
}

.cnc-21__marker {
  position: absolute;
  top: -5px;
  left: calc(var(--cnc-21-zp) * 1%);
  width: 4px;
  height: 20px;
  border-radius: 99px;
  background: var(--cnc-21-ink);
  box-shadow: 0 0 12px oklch(1 0 0/.55);
  transition: left .9s cubic-bezier(.16,1,.3,1);
}

.cnc-21__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 10px;
  margin-top: 20px;
  padding-top: 18px;
  border-top: 1px solid oklch(1 0 0/.09);
}

.cnc-21__grid dt {
  font-size: 10.5px;
  font-weight: 660;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--cnc-21-mut);
}

.cnc-21__grid dd {
  margin-top: 5px;
  font-size: 19px;
  font-weight: 720;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-21__grid dd small {
  font-size: .58em;
  font-weight: 600;
  color: var(--cnc-21-mut);
  margin-left: 2px;
}

.cnc-21__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-21__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-21-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,560px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-21 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ZONES = [[0, 'Recovery'], [98, 'Fat burn'], [128, 'Cardio'], [158, 'Peak']];

  document.querySelectorAll('.cnc-21__panel').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const numEl = panel.querySelector('.cnc-21__num');
    const zoneN = panel.querySelector('.cnc-21__zonen');
    const zoneL = panel.querySelector('.cnc-21__zonel');
    const hrvEl = panel.querySelector('.cnc-21__hrv');
    const spoEl = panel.querySelector('.cnc-21__spo');
    const kcalEl = panel.querySelector('.cnc-21__kcal');
    const sr = panel.querySelector('.cnc-21__sr');
    let bpm = 64, kcal = 128, settle = 0;

    const roll = (el, from, to, ms) => {
      if (reduce || from === to) { el.textContent = to; return; }
      const t0 = performance.now();
      const frame = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        el.textContent = Math.round(from + (to - from) * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };

    const apply = (next) => {
      const prev = bpm; bpm = next;
      panel.style.setProperty('--cnc-21-bpm', bpm);          // one property retimes every rhythm
      panel.style.setProperty('--cnc-21-zp', Math.max(4, Math.min(96, ((bpm - 55) / 120) * 100)));
      roll(numEl, prev, bpm, 420);
      let zi = 0; ZONES.forEach((z, i) => { if (bpm >= z[0]) zi = i; });
      zoneN.textContent = zi + 1;
      zoneL.textContent = ZONES[zi][1];
      clearTimeout(settle);
      settle = setTimeout(() => { sr.textContent = 'Heart rate ' + bpm + ' beats per minute, zone ' + (zi + 1) + ', ' + ZONES[zi][1] + '.'; }, 1200);
    };

    apply(112);
    const id = setInterval(() => {
      if (document.visibilityState !== 'visible') return;
      apply(Math.max(96, Math.min(148, bpm + Math.round((Math.random() - 0.48) * 14))));
      hrvEl.textContent = 40 + Math.round(Math.random() * 18);
      spoEl.textContent = 96 + Math.round(Math.random() * 3);
      kcal += 2 + Math.round(Math.random() * 3);
      kcalEl.textContent = kcal;
    }, 2600);
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
