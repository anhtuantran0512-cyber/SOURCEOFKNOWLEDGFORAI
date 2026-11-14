---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/live-stock-crypto-price-ticker/"
title: "Live Stock / Crypto Price Ticker with Green-Red Deltas"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "A Bloomberg-style terminal strip for fintech and crypto sites: tickers, prices and percentage deltas glide by in tabular-figure monospace while a tiny JS…"
has_js: "true"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Stock / Crypto Price Ticker with Green-Red Deltas
Source: https://codefronts.com/motion/css-infinite-marquee/live-stock-crypto-price-ticker/

A Bloomberg-style terminal strip for fintech and crypto sites: tickers, prices and percentage deltas glide by in tabular-figure monospace while a tiny JS loop nudges the numbers every 2 seconds — the marquee itself stays 100% CSS, so updates never stutter the scroll, and green/red states are announced with real +/− characters, not color alone.
## HTML
```html
<section class="mqs-05" aria-label="Stock price ticker marquee demo">
  <div class="mqs-05__terminal">
    <div class="mqs-05__bar"><span class="mqs-05__live"></span>Markets · simulated feed</div>
    <div class="mqs-05__viewport">
      <div class="mqs-05__group" data-mqs05-group>
        <span class="mqs-05__quote" data-sym="NVTX"><b class="mqs-05__sym">NVTX</b><span class="mqs-05__px" data-px>842.15</span><span class="mqs-05__dl" data-dl>+1.24%</span></span>
        <span class="mqs-05__quote" data-sym="ACRN"><b class="mqs-05__sym">ACRN</b><span class="mqs-05__px" data-px>198.40</span><span class="mqs-05__dl" data-dl>−0.87%</span></span>
        <span class="mqs-05__quote" data-sym="SLTC"><b class="mqs-05__sym">SLTC</b><span class="mqs-05__px" data-px>64.02</span><span class="mqs-05__dl" data-dl>+0.31%</span></span>
        <span class="mqs-05__quote" data-sym="BTC"><b class="mqs-05__sym">BTC</b><span class="mqs-05__px" data-px>67,412</span><span class="mqs-05__dl" data-dl>+2.10%</span></span>
        <span class="mqs-05__quote" data-sym="ETH"><b class="mqs-05__sym">ETH</b><span class="mqs-05__px" data-px>3,528</span><span class="mqs-05__dl" data-dl>−1.44%</span></span>
        <span class="mqs-05__quote" data-sym="MERI"><b class="mqs-05__sym">MERI</b><span class="mqs-05__px" data-px>412.77</span><span class="mqs-05__dl" data-dl>+0.05%</span></span>
      </div>
      <div class="mqs-05__group" data-mqs05-group aria-hidden="true">
        <span class="mqs-05__quote" data-sym="NVTX"><b class="mqs-05__sym">NVTX</b><span class="mqs-05__px" data-px>842.15</span><span class="mqs-05__dl" data-dl>+1.24%</span></span>
        <span class="mqs-05__quote" data-sym="ACRN"><b class="mqs-05__sym">ACRN</b><span class="mqs-05__px" data-px>198.40</span><span class="mqs-05__dl" data-dl>−0.87%</span></span>
        <span class="mqs-05__quote" data-sym="SLTC"><b class="mqs-05__sym">SLTC</b><span class="mqs-05__px" data-px>64.02</span><span class="mqs-05__dl" data-dl>+0.31%</span></span>
        <span class="mqs-05__quote" data-sym="BTC"><b class="mqs-05__sym">BTC</b><span class="mqs-05__px" data-px>67,412</span><span class="mqs-05__dl" data-dl>+2.10%</span></span>
        <span class="mqs-05__quote" data-sym="ETH"><b class="mqs-05__sym">ETH</b><span class="mqs-05__px" data-px>3,528</span><span class="mqs-05__dl" data-dl>−1.44%</span></span>
        <span class="mqs-05__quote" data-sym="MERI"><b class="mqs-05__sym">MERI</b><span class="mqs-05__px" data-px>412.77</span><span class="mqs-05__dl" data-dl>+0.05%</span></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-05,
.mqs-05 *,
.mqs-05 *::before,
.mqs-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-05 {
  min-height: 100vh;
  width: 100%;
  --gap: 40px;
  --speed: 32s;
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
  background: #08090c;
  padding: 72px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.mqs-05__terminal {
  width: 100%;
  border-block: 1px solid #1c2027;
}

.mqs-05__bar {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 10px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #5b6472;
  padding: 8px 20px;
  border-bottom: 1px solid #14171d;
}

.mqs-05__live {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 8px #22c55e88;
  animation: mqs-05-pulse 1.6s ease-in-out infinite;
}

@keyframes mqs-05-pulse {
  50% {
    opacity: .35;
  }
}

.mqs-05__viewport {
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  padding-block: 14px;
}

.mqs-05__group {
  flex: none;
  display: flex;
  align-items: center;
  gap: var(--gap);
  animation: mqs-05-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-05-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-05__viewport:hover .mqs-05__group {
  animation-play-state: paused;
}

.mqs-05__quote {
  flex: none;
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-variant-numeric: tabular-nums;
}

.mqs-05__sym {
  font-size: 13px;
  font-weight: 700;
  color: #e5e9f0;
  letter-spacing: .06em;
}

.mqs-05__px {
  font-size: 13px;
  color: #8b94a5;
  min-width: 7ch;
  text-align: right;
}

.mqs-05__dl {
  font-size: 12px;
  font-weight: 700;
  min-width: 7ch;
}

.mqs-05__quote[data-dir="up"] .mqs-05__dl {
  color: #34d399;
}

.mqs-05__quote[data-dir="down"] .mqs-05__dl {
  color: #f87171;
}

@media (prefers-reduced-motion: reduce) {
  .mqs-05__group {
    animation: none;
  }

  .mqs-05__viewport {
    overflow-x: auto;
  }

  .mqs-05__live {
    animation: none;
  }
}
```

## JavaScript
```js
// JS owns the DATA only — the scroll is pure CSS, so these text updates never stutter the loop.
const state = {};
document.querySelectorAll('.mqs-05__group:not([aria-hidden]) .mqs-05__quote').forEach(q => {
  state[q.dataset.sym] = parseFloat(q.querySelector('[data-px]').textContent.replace(/,/g, ''));
});
function renderQuote(sym, price, deltaPct) {
  // CRITICAL: update the quote in BOTH groups so the loop seam never shows stale numbers.
  document.querySelectorAll('.mqs-05__quote[data-sym="' + sym + '"]').forEach(q => {
    q.querySelector('[data-px]').textContent = price >= 1000
      ? Math.round(price).toLocaleString('en-US') : price.toFixed(2);
    // Signed characters (not color alone) carry direction; U+2212 minus reads better than hyphen.
    q.querySelector('[data-dl]').textContent = (deltaPct >= 0 ? '+' : '\u2212') + Math.abs(deltaPct).toFixed(2) + '%';
    q.dataset.dir = deltaPct >= 0 ? 'up' : 'down';
  });
}
function randomWalk() {
  for (const sym in state) {
    const deltaPct = (Math.random() - 0.48) * 1.2;       // gentle ±0.6% drift
    state[sym] = Math.max(1, state[sym] * (1 + deltaPct / 100));
    renderQuote(sym, state[sym], deltaPct);
  }
}
randomWalk();
setInterval(randomWalk, 2000); // replace randomWalk with your WebSocket handler for real feeds
```
