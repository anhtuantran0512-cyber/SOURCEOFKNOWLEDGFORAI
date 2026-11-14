---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/swiss-saas-analytics/"
title: "B2B SaaS Analytics Summary Grid"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "The summary strip at the top of every B2B analytics product: six metric tiles that re-count whenever the date range changes, each with a delta chip and a…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: B2B SaaS Analytics Summary Grid
Source: https://codefronts.com/motion/css-number-counter-animations/swiss-saas-analytics/

The summary strip at the top of every B2B analytics product: six metric tiles that re-count whenever the date range changes, each with a delta chip and a sparkline that redraws. One dataset, one render function, one cached formatter per metric — the architecture that stops a dashboard turning into six copies of the same counter code.
## HTML
```html
<section class="cnc-24" aria-label="B2B SaaS analytics summary grid demo">
  <div class="cnc-24__stage">
    <div class="cnc-24__panel">
      <header class="cnc-24__head">
        <div>
          <h3 class="cnc-24__title">Workspace analytics</h3>
          <p class="cnc-24__sub" id="cnc-24-base">Compared with the previous period · sample data</p>
        </div>
        <div class="cnc-24__seg" role="group" aria-label="Date range">
          <button class="cnc-24__segb" type="button" data-range="7" aria-pressed="false">7d</button>
          <button class="cnc-24__segb" type="button" data-range="30" aria-pressed="true">30d</button>
          <button class="cnc-24__segb" type="button" data-range="90" aria-pressed="false">90d</button>
        </div>
      </header>
      <div class="cnc-24__grid">
        <article class="cnc-24__tile" data-key="mrr"><p class="cnc-24__k">Net MRR</p><p class="cnc-24__v" aria-hidden="true">—</p><p class="cnc-24__d"><span></span></p><svg class="cnc-24__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true"><polyline points=""/></svg></article>
        <article class="cnc-24__tile" data-key="workspaces"><p class="cnc-24__k">Active workspaces</p><p class="cnc-24__v" aria-hidden="true">—</p><p class="cnc-24__d"><span></span></p><svg class="cnc-24__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true"><polyline points=""/></svg></article>
        <article class="cnc-24__tile" data-key="seats"><p class="cnc-24__k">Paid seats</p><p class="cnc-24__v" aria-hidden="true">—</p><p class="cnc-24__d"><span></span></p><svg class="cnc-24__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true"><polyline points=""/></svg></article>
        <article class="cnc-24__tile" data-key="nrr"><p class="cnc-24__k">Net revenue retention</p><p class="cnc-24__v" aria-hidden="true">—</p><p class="cnc-24__d"><span></span></p><svg class="cnc-24__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true"><polyline points=""/></svg></article>
        <article class="cnc-24__tile" data-key="trial"><p class="cnc-24__k">Trial → paid</p><p class="cnc-24__v" aria-hidden="true">—</p><p class="cnc-24__d"><span></span></p><svg class="cnc-24__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true"><polyline points=""/></svg></article>
        <article class="cnc-24__tile" data-key="latency"><p class="cnc-24__k">p95 API latency</p><p class="cnc-24__v" aria-hidden="true">—</p><p class="cnc-24__d"><span></span></p><svg class="cnc-24__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true"><polyline points=""/></svg></article>
      </div>
      <p class="cnc-24__status" role="status" aria-live="polite"></p>
    </div>
    <p class="cnc-24__chip" aria-hidden="true">cached Intl formatters · tween from displayed value · container-query grid · sparkline redraw</p>
  </div>
</section>
```
## CSS
```css
.cnc-24,
.cnc-24 *,
.cnc-24 *::before,
.cnc-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-24-bg: oklch(0.97 0.006 265);
  --cnc-24-card: oklch(1 0 0);
  --cnc-24-ink: oklch(0.24 0.02 265);
  --cnc-24-mut: oklch(0.57 0.02 265);
  --cnc-24-acc: oklch(0.55 0.19 275);
  --cnc-24-up: oklch(0.55 0.14 158);
  --cnc-24-down: oklch(0.58 0.19 25);
  --cnc-24-line: oklch(0 0 0/.08);
  background: var(--cnc-24-bg);
  color: var(--cnc-24-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-24__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-24__panel {
  container-type: inline-size;
  width: min(100%,980px);
  padding: clamp(18px,3vw,26px);
  border-radius: 24px;
  background: var(--cnc-24-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 64px oklch(0.3 0.03 265/.14);
}

.cnc-24__head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

.cnc-24__title {
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.cnc-24__sub {
  margin-top: 4px;
  font-size: 12px;
  color: var(--cnc-24-mut);
}

.cnc-24__seg {
  display: flex;
  gap: 2px;
  padding: 3px;
  border-radius: 12px;
  background: oklch(0 0 0/.05);
}

.cnc-24__segb {
  min-height: 34px;
  padding: 7px 15px;
  border: 0;
  border-radius: 9px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 660;
  color: var(--cnc-24-mut);
  background: transparent;
  cursor: pointer;
  transition: background .18s,color .18s,box-shadow .18s;
}

.cnc-24__segb:hover {
  color: var(--cnc-24-ink);
}

.cnc-24__segb:focus-visible {
  outline: 2px solid var(--cnc-24-acc);
  outline-offset: 2px;
}

.cnc-24__segb[aria-pressed="true"] {
  color: var(--cnc-24-ink);
  background: var(--cnc-24-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.12);
}

.cnc-24__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
  margin-top: 20px;
}

@container (min-width: 480px) {
  .cnc-24__grid {
    grid-template-columns: 1fr 1fr;
  }
}

@container (min-width: 780px) {
  .cnc-24__grid {
    grid-template-columns: repeat(3,1fr);
  }
}

.cnc-24__tile {
  position: relative;
  padding: 16px 16px 14px;
  border-radius: 16px;
  border: 1px solid var(--cnc-24-line);
  background: var(--cnc-24-card);
  overflow: hidden;
  transition: border-color .2s,box-shadow .2s,translate .2s;
}

.cnc-24__tile:hover {
  border-color: color-mix(in oklch,var(--cnc-24-acc) 45%,var(--cnc-24-line));
  box-shadow: 0 10px 26px oklch(0.3 0.04 275/.12);
  translate: 0 -2px;
}

.cnc-24__k {
  font-size: 11.5px;
  font-weight: 640;
  color: var(--cnc-24-mut);
}

.cnc-24__v {
  margin-top: 8px;
  font-size: clamp(24px,3.4vw,30px);
  font-weight: 750;
  letter-spacing: -.045em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-24__d {
  margin-top: 8px;
  font-size: 11.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cnc-24__d span {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 8px;
  border-radius: 99px;
  color: var(--cnc-24-up);
  background: color-mix(in oklch,var(--cnc-24-up) 12%,transparent);
}

.cnc-24__tile[data-dir="down"] .cnc-24__d span {
  color: var(--cnc-24-down);
  background: color-mix(in oklch,var(--cnc-24-down) 12%,transparent);
}

.cnc-24__spark {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 58%;
  height: 44px;
  opacity: .9;
}

.cnc-24__spark polyline {
  fill: none;
  stroke: var(--cnc-24-acc);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 260;
  stroke-dashoffset: 0;
  animation: cnc-24-draw .9s cubic-bezier(.16,1,.3,1);
}

.cnc-24__tile[data-dir="down"] .cnc-24__spark polyline {
  stroke: var(--cnc-24-down);
}

@keyframes cnc-24-draw {
  from {
    stroke-dashoffset: 260;
  }

  to {
    stroke-dashoffset: 0;
  }
}

.cnc-24__status {
  margin-top: 16px;
  font-size: 12px;
  color: var(--cnc-24-mut);
}

.cnc-24__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-24-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,640px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-24 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const FMT = {
    usd: new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', notation: 'compact', maximumFractionDigits: 1 }),
    num: new Intl.NumberFormat('en-US'),
    publishDate: '2026-05-19T10:00:00.000Z',
    updatedDate: '2026-08-07T16:16:00.000Z',
    pct: new Intl.NumberFormat('en-US', { style: 'percent', maximumFractionDigits: 1 }),
    ms: new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 }),
  };
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const META = {
    mrr: { fmt: 'usd', scale: 1 }, workspaces: { fmt: 'num', scale: 1 }, seats: { fmt: 'num', scale: 1 },
    nrr: { fmt: 'pct', scale: 0.0001 }, trial: { fmt: 'pct', scale: 0.0001 }, latency: { fmt: 'ms', scale: 1, suffix: ' ms', invert: true },
  };
  const DATA = {
    7:  { mrr:[412800,3.1,[18,20,19,24,22,27,30]], workspaces:[1284,1.8,[11,13,12,15,17,16,19]], seats:[9642,2.4,[14,15,17,16,19,21,23]], nrr:[11240,0.6,[20,19,21,22,21,23,24]], trial:[3180,-0.4,[16,18,15,17,14,16,15]], latency:[186,-4.2,[26,24,22,25,21,19,18]] },
    30: { mrr:[398400,8.6,[10,12,15,14,18,17,21,24,23,27,29,32]], workspaces:[1216,6.2,[8,9,11,10,13,15,14,17,18,20,22,24]], seats:[9180,7.4,[9,11,10,14,16,15,18,20,19,23,25,27]], nrr:[11080,1.9,[16,17,16,18,19,18,20,21,20,22,23,24]], trial:[3320,2.1,[12,14,13,16,15,18,17,19,18,20,21,22]], latency:[203,-11.5,[30,29,27,28,25,24,22,23,20,19,18,17]] },
    90: { mrr:[344900,24.3,[6,8,7,11,13,12,16,19,18,23,26,25,29,31,34]], workspaces:[1044,19.8,[5,7,6,9,11,10,13,15,14,18,20,19,23,25,27]], seats:[7960,26.1,[4,6,8,7,11,13,12,16,18,17,21,24,23,27,30]], nrr:[10740,4.4,[13,14,16,15,17,18,17,19,20,19,21,22,21,23,25]], trial:[2960,6.8,[9,11,10,13,12,15,14,17,16,19,18,21,20,22,24]], latency:[241,-18.9,[33,32,30,31,28,27,25,26,23,22,20,21,18,17,16]] },
  };

  document.querySelectorAll('.cnc-24__panel').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const status = panel.querySelector('.cnc-24__status');
    const tiles = [...panel.querySelectorAll('.cnc-24__tile')].map((el) => ({
      el, key: el.dataset.key, v: el.querySelector('.cnc-24__v'),
      d: el.querySelector('.cnc-24__d span'), poly: el.querySelector('polyline'), current: 0,
    }));

    const show = (t, raw) => {
      const m = META[t.key];
      t.v.textContent = FMT[m.fmt].format(raw * m.scale) + (m.suffix || '');
    };
    const tween = (t, to, ms) => {
      const from = t.current;
      if (reduce || from === to) { t.current = to; show(t, to); return; }
      const t0 = performance.now();
      const step = (now) => {
        const p = Math.min(1, (now - t0) / ms), e = 1 - Math.pow(1 - p, 4);
        show(t, Math.round(from + (to - from) * e));
        if (p < 1) requestAnimationFrame(step);
      };
      t.current = to;
      requestAnimationFrame(step);
    };
    const redraw = (poly, arr) => {
      const max = Math.max(...arr), min = Math.min(...arr), span = max - min || 1;
      poly.setAttribute('points', arr.map((v, i) =>
        (i / (arr.length - 1) * 116 + 2).toFixed(1) + ',' + (30 - (v - min) / span * 26).toFixed(1)).join(' '));
      poly.style.animation = 'none'; void poly.getBoundingClientRect(); poly.style.animation = '';
    };
    const render = (range) => {
      tiles.forEach((t) => {
        const [val, delta, spark] = DATA[range][t.key];
        const good = META[t.key].invert ? delta < 0 : delta > 0;
        t.el.dataset.dir = good ? 'up' : 'down';
        t.d.textContent = (delta > 0 ? '▲ +' : '▼ ') + delta.toFixed(1) + '%';
        tween(t, val, 900);
        redraw(t.poly, spark);
      });
      status.textContent = 'Showing the last ' + range + ' days. Net MRR ' +
        FMT.usd.format(DATA[range].mrr[0]) + ', ' + DATA[range].mrr[1].toFixed(1) + '% versus the previous period.';
    };

    panel.querySelectorAll('[data-range]').forEach((btn) => {
      btn.addEventListener('click', () => {
        panel.querySelectorAll('[data-range]').forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
        const go = () => render(btn.dataset.range);
        document.startViewTransition && !reduce ? document.startViewTransition(go) : go();
      });
    });
    render('30');
  });
})();
```
