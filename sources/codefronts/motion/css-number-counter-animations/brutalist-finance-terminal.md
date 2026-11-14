---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/brutalist-finance-terminal/"
title: "Fintech Transaction & Revenue Counter Card"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A payments card in the language finance products actually use: settled balance counting in, a pending amount underneath, a transaction volume that ticks with…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fintech Transaction & Revenue Counter Card
Source: https://codefronts.com/motion/css-number-counter-animations/brutalist-finance-terminal/

A payments card in the language finance products actually use: settled balance counting in, a pending amount underneath, a transaction volume that ticks with each incoming payment, and a stacked 24-hour volume bar. Amounts are integers in minor units end to end — the only way a money counter stays exact.
## HTML
```html
<section class="cnc-20" aria-label="Fintech transaction and revenue counter card demo">
  <div class="cnc-20__stage">
    <article class="cnc-20__card">
      <div class="cnc-20__hero">
        <div class="cnc-20__row">
          <p class="cnc-20__label">Settled balance</p>
          <span class="cnc-20__acct">•••• 4419</span>
        </div>
        <p class="cnc-20__balance"><span class="cnc-20__num">$0.00</span></p>
        <p class="cnc-20__pending"><span class="cnc-20__pdot" aria-hidden="true"></span><b class="cnc-20__pend">$0.00</b> pending settlement</p>
        <div class="cnc-20__bars" aria-hidden="true">
          <span style="--cnc-20-v:32"></span><span style="--cnc-20-v:48"></span><span style="--cnc-20-v:41"></span><span style="--cnc-20-v:66"></span>
          <span style="--cnc-20-v:58"></span><span style="--cnc-20-v:79"></span><span style="--cnc-20-v:71"></span><span style="--cnc-20-v:92"></span>
          <span style="--cnc-20-v:84"></span><span style="--cnc-20-v:100"></span><span style="--cnc-20-v:88"></span><span style="--cnc-20-v:74"></span>
        </div>
        <p class="cnc-20__barslabel">Volume, last 12 hours</p>
      </div>
      <div class="cnc-20__body">
        <div class="cnc-20__kpis">
          <div><p class="cnc-20__k">Transactions</p><p class="cnc-20__v"><span class="cnc-20__txns">0</span></p></div>
          <div><p class="cnc-20__k">Avg. ticket</p><p class="cnc-20__v"><span class="cnc-20__avg">$0</span></p></div>
          <div><p class="cnc-20__k">Success rate</p><p class="cnc-20__v">99.4<small>%</small></p></div>
        </div>
        <ul class="cnc-20__feed" aria-label="Recent transactions"></ul>
      </div>
      <p class="cnc-20__sr" role="status" aria-live="polite"></p>
    </article>
    <p class="cnc-20__chip" aria-hidden="true">integer minor units · single Intl formatter · @starting-style ledger rows</p>
  </div>
</section>
```
## CSS
```css
.cnc-20,
.cnc-20 *,
.cnc-20 *::before,
.cnc-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-20-bg: oklch(0.95 0.008 265);
  --cnc-20-dark: oklch(0.24 0.05 265);
  --cnc-20-card: oklch(1 0 0);
  --cnc-20-ink: oklch(0.22 0.02 265);
  --cnc-20-mut: oklch(0.56 0.02 265);
  --cnc-20-acc: oklch(0.78 0.17 165);
  background: var(--cnc-20-bg);
  color: var(--cnc-20-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-20__card {
  width: min(100%,440px);
  border-radius: 24px;
  overflow: hidden;
  background: var(--cnc-20-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 28px 64px oklch(0.3 0.04 265/.2);
}

.cnc-20__hero {
  padding: clamp(20px,4vw,26px);
  background: var(--cnc-20-dark);
  color: oklch(0.98 0.004 265);
}

.cnc-20__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.cnc-20__label {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.72 0.03 265);
}

.cnc-20__acct {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(0.72 0.03 265);
}

.cnc-20__balance {
  margin-top: 12px;
  font-size: clamp(32px,6.4vw,44px);
  font-weight: 750;
  letter-spacing: -.05em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-20__num {
  display: inline-block;
  min-width: 10ch;
}

.cnc-20__pending {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
  font-size: 12.5px;
  color: oklch(0.74 0.03 265);
}

.cnc-20__pend {
  color: var(--cnc-20-acc);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cnc-20__pdot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--cnc-20-acc);
  animation: cnc-20-pulse 2s ease-in-out infinite;
}

@keyframes cnc-20-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .3;
  }
}

.cnc-20__bars {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  align-items: end;
  gap: 4px;
  height: 52px;
  margin-top: 20px;
}

.cnc-20__bars span {
  height: calc(var(--cnc-20-v) * 1%);
  border-radius: 3px;
  background: color-mix(in oklch,var(--cnc-20-acc) calc(var(--cnc-20-v) * 0.85%),oklch(1 0 0/.12));
  transform-origin: bottom;
  animation: cnc-20-grow .7s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--cnc-20-v) * 3ms);
}

@keyframes cnc-20-grow {
  from {
    transform: scaleY(0);
  }

  to {
    transform: scaleY(1);
  }
}

.cnc-20__barslabel {
  margin-top: 8px;
  font-size: 11px;
  color: oklch(0.68 0.03 265);
}

.cnc-20__body {
  padding: clamp(18px,3.4vw,24px);
}

.cnc-20__kpis {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 12px;
  padding-bottom: 16px;
  border-bottom: 1px solid oklch(0 0 0/.08);
}

.cnc-20__k {
  font-size: 11px;
  font-weight: 640;
  color: var(--cnc-20-mut);
}

.cnc-20__v {
  margin-top: 5px;
  font-size: 19px;
  font-weight: 730;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-20__v small {
  font-size: .6em;
  font-weight: 640;
  color: var(--cnc-20-mut);
}

.cnc-20__feed {
  list-style: none;
  display: grid;
  gap: 2px;
  margin-top: 14px;
}

.cnc-20__feed li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 10px;
  font-size: 12.5px;
  color: var(--cnc-20-mut);
  opacity: 1;
  translate: 0 0;
  transition: opacity .4s,translate .4s cubic-bezier(.16,1,.3,1),background .2s;
}

.cnc-20__feed li:hover {
  background: oklch(0 0 0/.04);
}

@starting-style {
  .cnc-20__feed li {
    opacity: 0;
    translate: 0 -8px;
  }
}

.cnc-20__feed b {
  color: var(--cnc-20-ink);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cnc-20__feed em {
  font-style: normal;
  color: var(--cnc-20-acc);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cnc-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-20-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,520px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-20 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
  const money0 = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  const nf = new Intl.NumberFormat('en-US');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const MERCHANTS = ['Northwind Studio', 'Kite & Co', 'Lumen Labs', 'Pier 9 Coffee', 'Fathom Media', 'Bright Harbor'];

  document.querySelectorAll('.cnc-20__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const numEl = card.querySelector('.cnc-20__num');
    const pendEl = card.querySelector('.cnc-20__pend');
    const txnEl = card.querySelector('.cnc-20__txns');
    const avgEl = card.querySelector('.cnc-20__avg');
    const feed = card.querySelector('.cnc-20__feed');
    let cents = 4829314, pending = 118450, txns = 1372, i = 0;      // integer minor units

    const roll = (el, from, to, fmt, ms = 1000) => {
      if (reduce) { el.textContent = fmt(to); return; }
      const t0 = performance.now();
      const frame = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        el.textContent = fmt(p === 1 ? to : Math.round(from + (to - from) * (1 - Math.pow(1 - p, 4))));
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };

    const render = () => {
      pendEl.textContent = money.format(pending / 100);
      txnEl.textContent = nf.format(txns);
      avgEl.textContent = money0.format(cents / 100 / txns);
    };
    const pushRow = (amt, name) => {
      const li = document.createElement('li');
      li.innerHTML = '<span>' + name + '</span><em>+' + money.format(amt / 100) + '</em>';
      feed.prepend(li);
      while (feed.children.length > 4) feed.lastElementChild.remove();
    };

    roll(numEl, 0, cents, (v) => money.format(v / 100), 1600); render();
    ['Northwind Studio', 'Kite & Co', 'Lumen Labs'].forEach((n, k) => pushRow([4280, 12900, 3450][k], n));

    const id = setInterval(() => {
      if (document.visibilityState !== 'visible') return;
      const amt = 1200 + Math.floor(Math.random() * 46000);
      const prev = cents; cents += amt; txns += 1; pending = Math.max(0, pending + amt - 9000);
      roll(numEl, prev, cents, (v) => money.format(v / 100), 650);
      pushRow(amt, MERCHANTS[i++ % MERCHANTS.length]);
      render();
    }, 3400);
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
