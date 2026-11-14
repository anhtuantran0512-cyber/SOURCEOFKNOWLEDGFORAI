---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/fitness-step-counter/"
title: "Fitness Tracker & Daily Step Goal Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "Three concentric activity rings, a step count that rolls as you add movement, and a goal celebration that fires exactly once when the ring closes."
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fitness Tracker & Daily Step Goal Counter
Source: https://codefronts.com/motion/css-number-counter-animations/fitness-step-counter/

Three concentric activity rings, a step count that rolls as you add movement, and a goal celebration that fires exactly once when the ring closes. The rings are stroked SVG circles sharing one animation clock, so they sweep together like the hardware trackers they reference — and each carries its own accessible progress semantics.
## HTML
```html
<section class="cnc-19" aria-label="Fitness tracker and daily step goal counter demo">
  <div class="cnc-19__stage">
    <article class="cnc-19__card">
      <header class="cnc-19__top">
        <div><p class="cnc-19__day">Thursday</p><p class="cnc-19__date">7 August</p></div>
        <span class="cnc-19__streak">12-day streak</span>
      </header>
      <div class="cnc-19__rings">
        <svg viewBox="0 0 120 120" aria-hidden="true">
          <circle class="cnc-19__track" cx="60" cy="60" r="52"/><circle class="cnc-19__arc cnc-19__arc--1" cx="60" cy="60" r="52" pathLength="100"/>
          <circle class="cnc-19__track" cx="60" cy="60" r="39"/><circle class="cnc-19__arc cnc-19__arc--2" cx="60" cy="60" r="39" pathLength="100"/>
          <circle class="cnc-19__track" cx="60" cy="60" r="26"/><circle class="cnc-19__arc cnc-19__arc--3" cx="60" cy="60" r="26" pathLength="100"/>
        </svg>
        <svg class="cnc-19__check" viewBox="0 0 40 40" aria-hidden="true"><path d="M12 20.5 17.5 26 28 14.5"/></svg>
      </div>
      <p class="cnc-19__steps"><span class="cnc-19__num">0</span><span class="cnc-19__unit">steps</span></p>
      <p class="cnc-19__goal"><b class="cnc-19__pct">0%</b> of 10,000 step goal</p>
      <ul class="cnc-19__legend">
        <li style="--cnc-19-c:1"><span></span>Move <b class="cnc-19__kcal">0</b> kcal</li>
        <li style="--cnc-19-c:2"><span></span>Exercise <b>38</b> min</li>
        <li style="--cnc-19-c:3"><span></span>Stand <b>9</b> hr</li>
      </ul>
      <div class="cnc-19__acts">
        <button class="cnc-19__btn" type="button" data-add="850">Log a walk +850</button>
        <button class="cnc-19__btn cnc-19__btn--solid" type="button" data-add="2600">Log a run +2,600</button>
      </div>
      <p class="cnc-19__sr" role="status" aria-live="polite"></p>
    </article>
    <p class="cnc-19__chip" aria-hidden="true">pathLength=100 rings · min() clamp · one-shot goal flag · drawn checkmark</p>
  </div>
</section>
```
## CSS
```css
.cnc-19,
.cnc-19 *,
.cnc-19 *::before,
.cnc-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-19-bg: oklch(0.14 0.02 300);
  --cnc-19-card: oklch(0.2 0.025 300);
  --cnc-19-ink: oklch(0.98 0.004 300);
  --cnc-19-mut: oklch(0.66 0.02 300);
  --cnc-19-c1: oklch(0.72 0.2 15);
  --cnc-19-c2: oklch(0.82 0.19 145);
  --cnc-19-c3: oklch(0.78 0.15 210);
  background: var(--cnc-19-bg);
  color: var(--cnc-19-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-19__card {
  position: relative;
  width: min(100%,400px);
  padding: clamp(20px,4vw,28px);
  border-radius: 26px;
  text-align: center;
  background: var(--cnc-19-card);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.07),0 26px 60px oklch(0 0 0/.45);
}

.cnc-19__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  text-align: left;
}

.cnc-19__day {
  font-size: 15px;
  font-weight: 680;
}

.cnc-19__date {
  font-size: 12px;
  color: var(--cnc-19-mut);
  margin-top: 2px;
}

.cnc-19__streak {
  padding: 6px 11px;
  border-radius: 99px;
  background: oklch(1 0 0/.08);
  font-size: 11.5px;
  font-weight: 640;
}

.cnc-19__rings {
  position: relative;
  display: grid;
  place-items: center;
  width: min(60vw,180px);
  aspect-ratio: 1;
  margin: 14px auto 0;
}

.cnc-19__rings svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
  overflow: visible;
}

.cnc-19__track {
  fill: none;
  stroke: oklch(1 0 0/.09);
  stroke-width: 11;
}

.cnc-19__arc {
  fill: none;
  stroke-width: 11;
  stroke-linecap: round;
  stroke-dasharray: 100;
  stroke-dashoffset: calc(100 - 100 * min(1,var(--cnc-19-p,0)));
  transition: stroke-dashoffset 1.1s cubic-bezier(.16,1,.3,1);
}

.cnc-19__arc--1 {
  stroke: var(--cnc-19-c1);
  filter: drop-shadow(0 0 8px color-mix(in oklch,var(--cnc-19-c1) 50%,transparent));
}

.cnc-19__arc--2 {
  stroke: var(--cnc-19-c2);
}

.cnc-19__arc--3 {
  stroke: var(--cnc-19-c3);
}

.cnc-19__check {
  position: absolute;
  width: 46px;
  height: 46px;
  opacity: 0;
  scale: .6;
  transition: opacity .4s,scale .5s cubic-bezier(.16,1,.3,1);
}

.cnc-19__check path {
  fill: none;
  stroke: var(--cnc-19-c2);
  stroke-width: 3.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 30;
  stroke-dashoffset: 30;
}

.cnc-19__card[data-done] .cnc-19__check {
  opacity: 1;
  scale: 1;
}

.cnc-19__card[data-done] .cnc-19__check path {
  animation: cnc-19-draw .5s .15s cubic-bezier(.16,1,.3,1) forwards;
}

@keyframes cnc-19-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.cnc-19__steps {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 7px;
  margin-top: 18px;
  font-size: clamp(36px,7vw,48px);
  font-weight: 760;
  letter-spacing: -.05em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-19__unit {
  font-size: .3em;
  font-weight: 660;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--cnc-19-mut);
}

.cnc-19__goal {
  margin-top: 8px;
  font-size: 12.5px;
  color: var(--cnc-19-mut);
}

.cnc-19__goal b {
  color: var(--cnc-19-c1);
  font-weight: 720;
  font-variant-numeric: tabular-nums;
}

.cnc-19__legend {
  list-style: none;
  display: grid;
  gap: 7px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid oklch(1 0 0/.08);
  text-align: left;
  font-size: 12.5px;
  color: var(--cnc-19-mut);
}

.cnc-19__legend li {
  display: flex;
  align-items: center;
  gap: 9px;
}

.cnc-19__legend span {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--cnc-19-c1);
}

.cnc-19__legend li:nth-child(2) span {
  background: var(--cnc-19-c2);
}

.cnc-19__legend li:nth-child(3) span {
  background: var(--cnc-19-c3);
}

.cnc-19__legend b {
  color: var(--cnc-19-ink);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  margin-left: auto;
}

.cnc-19__acts {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  margin-top: 18px;
}

.cnc-19__btn {
  flex: 1;
  min-width: 130px;
  min-height: 46px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 12px;
  background: oklch(1 0 0/.05);
  color: var(--cnc-19-ink);
  font: inherit;
  font-size: 13px;
  font-weight: 660;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.cnc-19__btn--solid {
  background: var(--cnc-19-c1);
  border-color: transparent;
  color: oklch(0.16 0.03 15);
}

.cnc-19__btn:hover {
  transform: translateY(-2px);
  filter: brightness(1.08);
}

.cnc-19__btn:focus-visible {
  outline: 3px solid var(--cnc-19-c2);
  outline-offset: 3px;
}

.cnc-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-19-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,520px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-19 * {
    transition-duration: .01ms !important;
    animation-duration: 1ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.cnc-19__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const GOAL = 10000;
    const numEl = card.querySelector('.cnc-19__num');
    const pctEl = card.querySelector('.cnc-19__pct');
    const kcalEl = card.querySelector('.cnc-19__kcal');
    const say = card.querySelector('.cnc-19__sr');
    const arcs = [1, 2, 3].map((i) => card.querySelector('.cnc-19__arc--' + i));
    let steps = 6420;

    const roll = (from, to, ms = 900) => {
      if (reduce) { numEl.textContent = nf.format(to); return; }
      const t0 = performance.now();
      const frame = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        numEl.textContent = nf.format(p === 1 ? to : Math.round(from + (to - from) * (1 - Math.pow(1 - p, 4))));
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };

    const render = () => {
      const p = steps / GOAL;
      arcs[0].style.setProperty('--cnc-19-p', p.toFixed(4));
      arcs[1].style.setProperty('--cnc-19-p', Math.min(1.2, p * 0.78).toFixed(4));
      arcs[2].style.setProperty('--cnc-19-p', Math.min(1.2, p * 1.05).toFixed(4));
      pctEl.textContent = Math.round(p * 100) + '%';
      kcalEl.textContent = nf.format(Math.round(steps * 0.043));
      if (steps >= GOAL && !card.dataset.done) {              // one-shot celebration
        card.dataset.done = '1';
        say.textContent = 'Daily step goal reached: ' + nf.format(steps) + ' steps';
      }
    };

    roll(0, steps, 1400); render();
    card.querySelectorAll('.cnc-19__btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const prev = steps; steps += +btn.dataset.add;
        roll(prev, steps, 700); render();
        if (steps < GOAL) say.textContent = nf.format(GOAL - steps) + ' steps to goal';
      });
    });
  });
})();
```
