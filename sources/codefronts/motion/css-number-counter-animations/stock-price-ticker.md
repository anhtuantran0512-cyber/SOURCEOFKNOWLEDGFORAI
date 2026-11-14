---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/stock-price-ticker/"
title: "Real-Time Financial Stock Ticker"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A trading-desk price list with the two conventions that market UIs live by: a directional flash (green up, red down) that decays in under half a second, and…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real-Time Financial Stock Ticker
Source: https://codefronts.com/motion/css-number-counter-animations/stock-price-ticker/

A trading-desk price list with the two conventions that market UIs live by: a directional flash (green up, red down) that decays in under half a second, and monospaced tabular figures that never shift as prices tick. Includes a scrolling tape marquee, a sparkline per row, and a reduced-motion mode that swaps flashes for static arrows.
## HTML
```html
<section class="cnc-18" aria-label="Real-time financial stock ticker demo">
  <div class="cnc-18__stage">
    <div class="cnc-18__panel">
      <header class="cnc-18__head">
        <h3 class="cnc-18__title">Watchlist</h3>
        <span class="cnc-18__clock"><span class="cnc-18__live" aria-hidden="true"></span>Market open</span>
      </header>
      <ul class="cnc-18__rows" aria-hidden="true">
        <li class="cnc-18__row" data-sym="NVDA" data-price="14210" data-dir="up">
          <span class="cnc-18__sym">NVDA<small>NVIDIA Corp</small></span>
          <svg class="cnc-18__spark" viewBox="0 0 60 22" preserveAspectRatio="none"><polyline points="0,16 10,14 20,15 30,9 40,11 50,6 60,4"/></svg>
          <span class="cnc-18__price">142.10</span>
          <span class="cnc-18__chg">+1.82%</span>
        </li>
        <li class="cnc-18__row" data-sym="AAPL" data-price="22845" data-dir="down">
          <span class="cnc-18__sym">AAPL<small>Apple Inc</small></span>
          <svg class="cnc-18__spark" viewBox="0 0 60 22" preserveAspectRatio="none"><polyline points="0,6 10,8 20,7 30,12 40,10 50,15 60,17"/></svg>
          <span class="cnc-18__price">228.45</span>
          <span class="cnc-18__chg">−0.64%</span>
        </li>
        <li class="cnc-18__row" data-sym="TSLA" data-price="31088" data-dir="up">
          <span class="cnc-18__sym">TSLA<small>Tesla Inc</small></span>
          <svg class="cnc-18__spark" viewBox="0 0 60 22" preserveAspectRatio="none"><polyline points="0,18 10,13 20,16 30,10 40,12 50,8 60,5"/></svg>
          <span class="cnc-18__price">310.88</span>
          <span class="cnc-18__chg">+3.21%</span>
        </li>
        <li class="cnc-18__row" data-sym="BTC" data-price="9421400" data-dir="up">
          <span class="cnc-18__sym">BTC<small>Bitcoin</small></span>
          <svg class="cnc-18__spark" viewBox="0 0 60 22" preserveAspectRatio="none"><polyline points="0,14 10,15 20,10 30,12 40,7 50,9 60,3"/></svg>
          <span class="cnc-18__price">94,214.00</span>
          <span class="cnc-18__chg">+0.94%</span>
        </li>
      </ul>
      <div class="cnc-18__tape" aria-hidden="true">
        <div class="cnc-18__track"></div>
      </div>
      <p class="cnc-18__note">Simulated data · prices stored as integer cents · hover the tape to pause</p>
    </div>
    <p class="cnc-18__chip" aria-hidden="true">reflow-restarted flash · integer minor units · WCAG 2.2.2 pausable marquee</p>
  </div>
</section>
```
## CSS
```css
.cnc-18,
.cnc-18 *,
.cnc-18 *::before,
.cnc-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-18-bg: oklch(0.13 0.012 250);
  --cnc-18-card: oklch(0.18 0.015 250);
  --cnc-18-ink: oklch(0.97 0.004 250);
  --cnc-18-mut: oklch(0.62 0.02 250);
  --cnc-18-up: oklch(0.78 0.17 152);
  --cnc-18-down: oklch(0.7 0.19 22);
  background: var(--cnc-18-bg);
  color: var(--cnc-18-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-18__panel {
  width: min(100%,560px);
  border-radius: 20px;
  overflow: hidden;
  background: var(--cnc-18-card);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.07),0 24px 56px oklch(0 0 0/.5);
}

.cnc-18__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 16px 18px;
  border-bottom: 1px solid oklch(1 0 0/.08);
}

.cnc-18__title {
  font-size: 15px;
  font-weight: 680;
  letter-spacing: -.01em;
}

.cnc-18__clock {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 11.5px;
  color: var(--cnc-18-mut);
}

.cnc-18__live {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--cnc-18-up);
  animation: cnc-18-blink 2.2s ease-in-out infinite;
}

@keyframes cnc-18-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .3;
  }
}

.cnc-18__rows {
  list-style: none;
}

.cnc-18__row {
  --cnc-18-dir: var(--cnc-18-up);
  display: grid;
  grid-template-columns: 1fr 60px auto auto;
  align-items: center;
  gap: 14px;
  padding: 12px 18px;
  border-bottom: 1px solid oklch(1 0 0/.05);
}

.cnc-18__row[data-dir="down"] {
  --cnc-18-dir: var(--cnc-18-down);
}

.cnc-18__row.is-flash {
  animation: cnc-18-flash .45s ease-out;
}

@keyframes cnc-18-flash {
  from {
    background: color-mix(in oklch,var(--cnc-18-dir) 24%,transparent);
  }

  to {
    background: transparent;
  }
}

.cnc-18__sym {
  display: grid;
  font-size: 13.5px;
  font-weight: 720;
  letter-spacing: .02em;
}

.cnc-18__sym small {
  font-size: 11px;
  font-weight: 400;
  color: var(--cnc-18-mut);
  letter-spacing: 0;
  margin-top: 2px;
}

.cnc-18__spark {
  width: 60px;
  height: 22px;
  overflow: visible;
}

.cnc-18__spark polyline {
  fill: none;
  stroke: var(--cnc-18-dir);
  stroke-width: 1.6;
  stroke-linecap: round;
  stroke-linejoin: round;
  vector-effect: non-scaling-stroke;
  opacity: .85;
}

.cnc-18__price {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 14.5px;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
  min-width: 9ch;
  text-align: right;
}

.cnc-18__chg {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  min-width: 7.5ch;
  justify-content: flex-end;
  font-size: 12.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: var(--cnc-18-dir);
}

.cnc-18__chg::before {
  content: "▲";
  font-size: 9px;
}

.cnc-18__row[data-dir="down"] .cnc-18__chg::before {
  content: "▼";
}

.cnc-18__tape {
  overflow: hidden;
  padding: 10px 0;
  border-top: 1px solid oklch(1 0 0/.08);
  background: oklch(0 0 0/.25);
  -webkit-mask: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
  mask: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
}

.cnc-18__track {
  display: flex;
  gap: 26px;
  width: max-content;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  font-variant-numeric: tabular-nums;
  animation: cnc-18-tape 26s linear infinite;
}

.cnc-18__tape:hover .cnc-18__track,
.cnc-18__tape:focus-within .cnc-18__track {
  animation-play-state: paused;
}

@keyframes cnc-18-tape {
  to {
    transform: translateX(-50%);
  }
}

.cnc-18__track b {
  font-weight: 700;
  margin-right: 6px;
}

.cnc-18__track i {
  font-style: normal;
}

.cnc-18__track .up {
  color: var(--cnc-18-up);
}

.cnc-18__track .down {
  color: var(--cnc-18-down);
}

.cnc-18__note {
  padding: 12px 18px;
  font-size: 11px;
  color: var(--cnc-18-mut);
}

.cnc-18__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-18-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,560px);
}

@media (max-width: 460px) {
  .cnc-18__spark {
    display: none;
  }

  .cnc-18__row {
    grid-template-columns: 1fr auto auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnc-18__row.is-flash {
    animation: none;
  }

  .cnc-18__track,
    .cnc-18__live {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const fmt = new Intl.NumberFormat('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const pct = new Intl.NumberFormat('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2, signDisplay: 'always' });
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.querySelectorAll('.cnc-18__panel').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const rows = [...panel.querySelectorAll('.cnc-18__row')];
    const track = panel.querySelector('.cnc-18__track');

    const tapeHTML = () => rows.map((r) => {
      const dir = r.dataset.dir;
      return '<span><b>' + r.dataset.sym + '</b><i class="' + dir + '">' + fmt.format(r.dataset.price / 100) + ' ' + (dir === 'up' ? '▲' : '▼') + '</i></span>';
    }).join('');
    const paintTape = () => { track.innerHTML = tapeHTML() + tapeHTML(); };   // duplicated for seamless loop
    paintTape();

    const update = (row) => {
      const prev = +row.dataset.price;                       // integer cents, no float drift
      const drift = Math.round(prev * (Math.random() - 0.48) * 0.004);
      const next = Math.max(1, prev + drift);
      row.dataset.price = next;
      row.dataset.dir = next >= prev ? 'up' : 'down';
      row.querySelector('.cnc-18__price').textContent = fmt.format(next / 100);
      const change = ((next - prev) / prev) * 100;
      row.querySelector('.cnc-18__chg').textContent = pct.format(change) + '%';
      if (!reduce) { row.classList.remove('is-flash'); void row.offsetWidth; row.classList.add('is-flash'); }
    };

    const id = setInterval(() => {
      if (document.visibilityState !== 'visible') return;
      update(rows[Math.floor(Math.random() * rows.length)]);
      paintTape();
    }, 1400);                                                // ≤ 3 flashes/sec (WCAG 2.3.1)
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
