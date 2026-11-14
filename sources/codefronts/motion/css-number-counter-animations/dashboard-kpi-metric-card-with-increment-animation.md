---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/dashboard-kpi-metric-card-with-increment-animation/"
title: "Dashboard KPI Metric Card with Increment Animation"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "The workhorse tile of every admin panel: a headline metric that counts to its new value, a delta chip that flips green or red with a rotating arrow, a…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dashboard KPI Metric Card with Increment Animation
Source: https://codefronts.com/motion/css-number-counter-animations/dashboard-kpi-metric-card-with-increment-animation/

The workhorse tile of every admin panel: a headline metric that counts to its new value, a delta chip that flips green or red with a rotating arrow, a CSS-only sparkline, and a live-region announcement when the figure settles. Hover reveals the comparison period. It re-runs on demand so you can watch the increment behaviour that dashboards trigger on every poll.
## HTML
```html
<section class="cnc-04" aria-label="Dashboard KPI metric card demo">
  <div class="cnc-04__stage">
    <div class="cnc-04__grid">
      <article class="cnc-04__card" data-dir="up">
        <header class="cnc-04__top">
          <h3 class="cnc-04__label">Monthly recurring revenue</h3>
          <span class="cnc-04__dot" aria-hidden="true"></span>
        </header>
        <p class="cnc-04__value"><span class="cnc-04__cur">$</span><span class="cnc-04__num" data-to="284920">0</span></p>
        <div class="cnc-04__foot">
          <span class="cnc-04__delta">
            <svg class="cnc-04__arrow" viewBox="0 0 12 12" width="11" height="11" aria-hidden="true"><path d="M6 1.5 10.5 8H1.5z" fill="currentColor"/></svg>
            <b class="cnc-04__pct">12.4</b>%
          </span>
          <span class="cnc-04__vs">vs. last month</span>
        </div>
        <svg class="cnc-04__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true">
          <polyline class="cnc-04__line" points="0,28 12,25 24,27 36,20 48,22 60,15 72,17 84,10 96,12 108,5 120,3"/>
        </svg>
      </article>
      <article class="cnc-04__card" data-dir="down">
        <header class="cnc-04__top">
          <h3 class="cnc-04__label">Churn rate</h3>
          <span class="cnc-04__dot" aria-hidden="true"></span>
        </header>
        <p class="cnc-04__value"><span class="cnc-04__num" data-to="18" data-dec="1">0</span><span class="cnc-04__unit">%</span></p>
        <div class="cnc-04__foot">
          <span class="cnc-04__delta">
            <svg class="cnc-04__arrow" viewBox="0 0 12 12" width="11" height="11" aria-hidden="true"><path d="M6 1.5 10.5 8H1.5z" fill="currentColor"/></svg>
            <b class="cnc-04__pct">3.1</b>%
          </span>
          <span class="cnc-04__vs">vs. last month</span>
        </div>
        <svg class="cnc-04__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true">
          <polyline class="cnc-04__line" points="0,6 12,9 24,7 36,14 48,12 60,18 72,16 84,23 96,21 108,28 120,30"/>
        </svg>
      </article>
    </div>
    <button class="cnc-04__replay" type="button">Simulate data refresh</button>
    <p class="cnc-04__sr" role="status" aria-live="polite"></p>
    <p class="cnc-04__chip" aria-hidden="true">rAF tween from previous value · hoisted Intl.NumberFormat · :has() direction theming</p>
  </div>
</section>
```
## CSS
```css
.cnc-04,
.cnc-04 *,
.cnc-04 *::before,
.cnc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-04-bg: oklch(0.15 0.015 265);
  --cnc-04-card: oklch(0.21 0.02 265);
  --cnc-04-ink: oklch(0.98 0.004 260);
  --cnc-04-mut: oklch(0.66 0.02 265);
  --cnc-04-up: oklch(0.78 0.17 158);
  --cnc-04-down: oklch(0.7 0.19 25);
  background: var(--cnc-04-bg);
  color: var(--cnc-04-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(18px,4vw,48px);
  background: radial-gradient(70% 50% at 50% 0%,oklch(0.3 0.06 265/.5),transparent 70%);
}

.cnc-04__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(258px,1fr));
  gap: 16px;
  width: min(100%,640px);
}

.cnc-04__card {
  --cnc-04-acc: var(--cnc-04-up);
  position: relative;
  padding: 20px 20px 0;
  border-radius: 18px;
  overflow: hidden;
  background: var(--cnc-04-card);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.07),0 20px 48px oklch(0 0 0/.4);
  transition: box-shadow .35s,transform .35s cubic-bezier(.16,1,.3,1);
}

.cnc-04__card:has([data-dir="down"]),
.cnc-04__card[data-dir="down"] {
  --cnc-04-acc: var(--cnc-04-down);
}

.cnc-04__card:hover {
  transform: translateY(-3px);
  box-shadow: inset 0 0 0 1px color-mix(in oklch,var(--cnc-04-acc) 35%,transparent),0 24px 56px oklch(0 0 0/.5);
}

.cnc-04__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.cnc-04__label {
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: .01em;
  color: var(--cnc-04-mut);
}

.cnc-04__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--cnc-04-acc);
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--cnc-04-acc) 20%,transparent);
}

.cnc-04__value {
  display: flex;
  align-items: baseline;
  margin-top: 14px;
  font-size: clamp(30px,4.4vw,40px);
  font-weight: 730;
  letter-spacing: -.045em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-04__cur {
  font-size: .62em;
  font-weight: 620;
  color: var(--cnc-04-mut);
  margin-right: 2px;
}

.cnc-04__unit {
  font-size: .55em;
  font-weight: 640;
  color: var(--cnc-04-mut);
  margin-left: 2px;
}

.cnc-04__foot {
  display: flex;
  align-items: center;
  gap: 9px;
  margin-top: 12px;
  padding-bottom: 16px;
  font-size: 12.5px;
  color: var(--cnc-04-mut);
}

.cnc-04__delta {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 9px;
  border-radius: 8px;
  font-weight: 680;
  font-variant-numeric: tabular-nums;
  color: var(--cnc-04-acc);
  background: color-mix(in oklch,var(--cnc-04-acc) 15%,transparent);
}

.cnc-04__card[data-dir="down"] .cnc-04__arrow {
  rotate: 180deg;
}

.cnc-04__vs {
  opacity: .75;
  transition: opacity .3s;
}

.cnc-04__card:hover .cnc-04__vs {
  opacity: 1;
}

.cnc-04__spark {
  display: block;
  width: calc(100% + 40px);
  height: 40px;
  margin: 0 -20px -1px;
}

.cnc-04__line {
  fill: none;
  stroke: var(--cnc-04-acc);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  vector-effect: non-scaling-stroke;
  stroke-dasharray: 260;
  stroke-dashoffset: 260;
  animation: cnc-04-draw 1.4s cubic-bezier(.16,1,.3,1) .25s forwards;
}

@keyframes cnc-04-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.cnc-04__replay {
  min-height: 44px;
  padding: 0 20px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
  background: oklch(1 0 0/.06);
  color: var(--cnc-04-ink);
  font: inherit;
  font-size: 13.5px;
  font-weight: 620;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.cnc-04__replay:hover {
  background: oklch(1 0 0/.13);
  transform: translateY(-1px);
}

.cnc-04__replay:focus-visible {
  outline: 3px solid var(--cnc-04-up);
  outline-offset: 3px;
}

.cnc-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-04-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .cnc-04__line {
    animation: none;
    stroke-dashoffset: 0;
  }

  .cnc-04__card {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');                        // hoisted: built once
  const nf1 = new Intl.NumberFormat('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ease = (p) => 1 - Math.pow(1 - p, 4);

  const roll = (el, from, to, dec, ms = 1100) => {
    const f = dec ? nf1 : nf;
    const show = (v) => { el.textContent = f.format(dec ? v / 10 : Math.round(v)); };
    if (reduce) { show(to); return; }
    const t0 = performance.now();
    const frame = (t) => {
      const p = Math.min(1, (t - t0) / ms);
      show(p === 1 ? to : from + (to - from) * ease(p));
      if (p < 1) requestAnimationFrame(frame);
    };
    requestAnimationFrame(frame);
  };

  document.querySelectorAll('.cnc-04').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const nums = [...root.querySelectorAll('.cnc-04__num')];
    const say = root.querySelector('.cnc-04__sr');
    const run = (fromZero) => {
      nums.forEach((el) => {
        const to = +el.dataset.to, dec = +el.dataset.dec || 0;
        const from = fromZero ? 0 : +(el.dataset.cur || 0);
        el.dataset.cur = to;
        roll(el, from, to, dec);
      });
      setTimeout(() => {
        say.textContent = 'Metrics updated. Monthly recurring revenue ' + nf.format(+nums[0].dataset.to) + ' dollars, up 12.4 percent. Churn rate 1.8 percent, down 3.1 percent.';
      }, 1200);
    };
    run(true);
    root.querySelector('.cnc-04__replay').addEventListener('click', () => {
      nums.forEach((el) => { el.dataset.cur = el.dataset.to; el.dataset.to = Math.max(1, Math.round(+el.dataset.to * (0.86 + Math.random() * 0.3))); });
      run(false);
      root.querySelectorAll('.cnc-04__line').forEach((l) => { l.style.animation = 'none'; void l.getBBox(); l.style.animation = ''; });
    });
  });
})();
```
