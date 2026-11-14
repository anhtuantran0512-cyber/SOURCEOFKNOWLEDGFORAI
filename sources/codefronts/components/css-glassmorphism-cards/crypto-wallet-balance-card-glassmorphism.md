---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/crypto-wallet-balance-card-glassmorphism/"
title: "Crypto Wallet Balance Card Glassmorphism"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two wallet heroes: a deep-space balance card with an animated SVG sparkline drawing itself in and per-asset micro bars, and a neon allocation card whose…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Crypto Wallet Balance Card Glassmorphism
Source: https://codefronts.com/components/css-glassmorphism-cards/crypto-wallet-balance-card-glassmorphism/

Two wallet heroes: a deep-space balance card with an animated SVG sparkline drawing itself in and per-asset micro bars, and a neon allocation card whose conic-gradient portfolio ring rotates slowly behind a masked donut. Both are pure CSS + inline SVG — no chart library.
## HTML
```html
<div class="glz-05-group">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:[email protected]&family=Chivo+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-05a" aria-label="Crypto wallet balance card demo">
  <article class="glz-05a__card">
    <header class="glz-05a__head"><span class="glz-05a__label">Total balance</span><span class="glz-05a__net">◈ Mainnet</span></header>
    <p class="glz-05a__bal">$48,290<small>.16</small></p>
    <p class="glz-05a__delta"><b>▲ +12.4%</b> past 30 days</p>
    <svg class="glz-05a__spark" viewBox="0 0 120 40" aria-hidden="true" preserveAspectRatio="none">
      <defs><linearGradient id="glz05aG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="oklch(0.8 0.16 170)" stop-opacity=".4"/><stop offset="1" stop-color="oklch(0.8 0.16 170)" stop-opacity="0"/></linearGradient></defs>
      <path class="glz-05a__area" d="M0 34 L11 30 L22 31 L33 25 L44 27 L55 20 L66 23 L77 15 L88 17 L99 10 L110 12 L120 6 V40 H0 Z" fill="url(#glz05aG)"/>
      <path class="glz-05a__line" d="M0 34 L11 30 L22 31 L33 25 L44 27 L55 20 L66 23 L77 15 L88 17 L99 10 L110 12 L120 6" fill="none" stroke="oklch(0.8 0.16 170)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
    </svg>
    <ul class="glz-05a__assets">
      <li><i class="glz-05a__coin" style="--c:#f7931a">₿</i><span>BTC<em>0.412</em></span><div class="glz-05a__bar" style="--w:72%"><i></i></div><b class="glz-05a__up">+3.2%</b></li>
      <li><i class="glz-05a__coin" style="--c:#627eea">Ξ</i><span>ETH<em>4.86</em></span><div class="glz-05a__bar" style="--w:54%"><i></i></div><b class="glz-05a__up">+6.1%</b></li>
      <li><i class="glz-05a__coin" style="--c:#14f195">◎</i><span>SOL<em>118.4</em></span><div class="glz-05a__bar" style="--w:38%"><i></i></div><b class="glz-05a__dn">−1.8%</b></li>
    </ul>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:[email protected]&family=Chivo+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-05b" aria-label="Crypto portfolio allocation ring card">
  <article class="glz-05b__card">
    <div class="glz-05b__ringwrap">
      <div class="glz-05b__ring" role="img" aria-label="Portfolio allocation: Bitcoin 55%, Ethereum 30%, Solana 15%"></div>
      <div class="glz-05b__center"><em>Portfolio</em><b>$48.2k</b></div>
    </div>
    <ul class="glz-05b__legend">
      <li><i style="--c:oklch(0.75 0.16 60)"></i>BTC<b>55%</b></li>
      <li><i style="--c:oklch(0.65 0.19 285)"></i>ETH<b>30%</b></li>
      <li><i style="--c:oklch(0.85 0.17 165)"></i>SOL<b>15%</b></li>
    </ul>
    <div class="glz-05b__row"><button type="button">↑ Send</button><button type="button">↓ Receive</button><button type="button">⇄ Swap</button></div>
  </article>
</section>
</div>
```
## CSS
```css
.glz-05-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-05-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-05a,
.glz-05a *,
.glz-05a *::before,
.glz-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-05a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: #070812 linear-gradient(rgba(120,140,255,.05) 1px,transparent 1px) 0 0/100% 44px,linear-gradient(90deg,rgba(120,140,255,.05) 1px,transparent 1px) 0 0/44px 100%;
  font-family: 'Chivo Mono',ui-monospace,monospace;
}

.glz-05a::before {
  content: "";
  position: absolute;
  width: 64vmin;
  height: 64vmin;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.5 0.2 290/.55),transparent 70%);
  top: -18%;
  right: -10%;
  filter: blur(40px);
}

.glz-05a::after {
  content: "";
  position: absolute;
  width: 50vmin;
  height: 50vmin;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.6 0.16 170/.4),transparent 70%);
  bottom: -14%;
  left: -8%;
  filter: blur(50px);
}

.glz-05a__card {
  position: relative;
  z-index: 1;
  width: min(370px,100%);
  padding: 26px 26px 22px;
  border-radius: 24px;
  color: #e9edff;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.03));
  backdrop-filter: blur(24px) saturate(170%);
  -webkit-backdrop-filter: blur(24px) saturate(170%);
  border: 1px solid rgba(160,175,255,.22);
  box-shadow: 0 30px 70px -24px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.2);
}

.glz-05a__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 10.5px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(233,237,255,.5);
}

.glz-05a__net {
  padding: 5px 10px;
  border-radius: 99px;
  border: 1px solid oklch(0.8 0.16 170/.4);
  color: oklch(0.85 0.14 170);
  letter-spacing: .1em;
}

.glz-05a__bal {
  margin-top: 16px;
  font-family: 'Unbounded',sans-serif;
  font-size: clamp(30px,7vw,38px);
  font-weight: 600;
  letter-spacing: -.01em;
  color: #fff;
  font-variant-numeric: tabular-nums;
}

.glz-05a__bal small {
  font-size: .55em;
  color: rgba(233,237,255,.55);
}

.glz-05a__delta {
  margin-top: 8px;
  font-size: 12px;
  color: rgba(233,237,255,.55);
}

.glz-05a__delta b {
  color: oklch(0.85 0.16 165);
  animation: glz-05a-pulse 1.2s ease .4s 2;
}

.glz-05a__spark {
  width: 100%;
  height: 64px;
  margin-top: 18px;
}

.glz-05a__line {
  stroke-dasharray: 340;
  stroke-dashoffset: 340;
  animation: glz-05a-draw 1.6s cubic-bezier(.4,0,.2,1) .3s forwards;
}

.glz-05a__area {
  opacity: 0;
  animation: glz-05a-fade .8s ease 1.4s forwards;
}

.glz-05a__assets {
  list-style: none;
  margin-top: 16px;
  display: grid;
  gap: 12px;
  border-top: 1px solid rgba(160,175,255,.16);
  padding-top: 16px;
}

.glz-05a__assets li {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: 12.5px;
}

.glz-05a__coin {
  width: 32px;
  height: 32px;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-style: normal;
  font-size: 14px;
  color: #0a0a14;
  background: var(--c);
  box-shadow: 0 0 14px color-mix(in oklab,var(--c) 60%,transparent);
}

.glz-05a__assets span {
  width: 52px;
  font-weight: 600;
}

.glz-05a__assets em {
  display: block;
  font-style: normal;
  font-size: 10.5px;
  color: rgba(233,237,255,.45);
}

.glz-05a__bar {
  flex: 1;
  height: 5px;
  border-radius: 99px;
  background: rgba(160,175,255,.14);
  overflow: hidden;
}

.glz-05a__bar i {
  display: block;
  height: 100%;
  width: var(--w);
  border-radius: inherit;
  background: linear-gradient(90deg,oklch(0.65 0.18 290),oklch(0.8 0.16 170));
  transform: scaleX(0);
  transform-origin: left;
  animation: glz-05a-grow 1s cubic-bezier(.3,0,.2,1) .8s forwards;
}

.glz-05a__up {
  color: oklch(0.85 0.16 165);
}

.glz-05a__dn {
  color: oklch(0.75 0.19 20);
}

@keyframes glz-05a-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes glz-05a-fade {
  to {
    opacity: 1;
  }
}

@keyframes glz-05a-grow {
  to {
    transform: scaleX(1);
  }
}

@keyframes glz-05a-pulse {
  50% {
    text-shadow: 0 0 18px oklch(0.85 0.16 165/.9);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-05a__card {
    background: rgba(14,16,32,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-05a__line {
    animation: none;
    stroke-dashoffset: 0;
  }

  .glz-05a__area {
    animation: none;
    opacity: 1;
  }

  .glz-05a__bar i {
    animation: none;
    transform: none;
  }

  .glz-05a__delta b {
    animation: none;
  }
}

.glz-05b,
.glz-05b *,
.glz-05b *::before,
.glz-05b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --glz-05b-spin {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.glz-05b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: radial-gradient(90% 80% at 50% 110%,#1b1038,#0a0716 60%);
}

.glz-05b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(40% 34% at 78% 18%,oklch(0.6 0.24 320/.35),transparent 70%),radial-gradient(36% 30% at 18% 30%,oklch(0.7 0.17 165/.3),transparent 70%);
}

.glz-05b__card {
  position: relative;
  z-index: 1;
  width: min(340px,100%);
  padding: 30px 26px 24px;
  border-radius: 26px;
  text-align: center;
  color: #efeaff;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.03));
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(200,180,255,.24);
  box-shadow: 0 34px 70px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.22);
  font-family: 'Chivo Mono',ui-monospace,monospace;
}

.glz-05b__ringwrap {
  position: relative;
  width: 172px;
  height: 172px;
  margin: 0 auto;
}

.glz-05b__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(from var(--glz-05b-spin),oklch(0.75 0.16 60) 0 55%,oklch(0.65 0.19 285) 55% 85%,oklch(0.85 0.17 165) 85% 100%);
  -webkit-mask: radial-gradient(closest-side,transparent 62%,#000 63%);
  mask: radial-gradient(closest-side,transparent 62%,#000 63%);
  animation: glz-05b-spin 22s linear infinite;
  filter: drop-shadow(0 0 18px oklch(0.65 0.19 285/.55));
}

.glz-05b__center {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  gap: 4px;
}

.glz-05b__center em {
  font-style: normal;
  font-size: 10px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: rgba(239,234,255,.5);
}

.glz-05b__center b {
  font-family: 'Unbounded',sans-serif;
  font-size: 26px;
  font-weight: 600;
  color: #fff;
}

.glz-05b__legend {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-top: 22px;
  font-size: 11.5px;
  letter-spacing: .04em;
}

.glz-05b__legend i {
  display: inline-block;
  width: 9px;
  height: 9px;
  border-radius: 3px;
  background: var(--c);
  margin-right: 6px;
  box-shadow: 0 0 10px color-mix(in oklab,var(--c) 70%,transparent);
}

.glz-05b__legend b {
  margin-left: 6px;
  color: rgba(239,234,255,.6);
  font-weight: 500;
}

.glz-05b__row {
  display: flex;
  gap: 9px;
  margin-top: 22px;
}

.glz-05b__row button {
  flex: 1;
  padding: 12px 6px;
  border-radius: 13px;
  border: 1px solid rgba(200,180,255,.25);
  background: rgba(255,255,255,.06);
  color: #efeaff;
  font: 600 12px 'Chivo Mono',monospace;
  cursor: pointer;
  transition: background .25s ease,transform .2s ease;
}

.glz-05b__row button:hover {
  background: rgba(255,255,255,.14);
  transform: translateY(-2px);
}

.glz-05b__row button:focus-visible {
  outline: 2px solid oklch(0.85 0.17 165);
  outline-offset: 2px;
}

@keyframes glz-05b-spin {
  to {
    --glz-05b-spin: 360deg;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-05b__card {
    background: rgba(20,14,38,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-05b__ring {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the sparkline draws in via stroke-dasharray/offset, asset bars scaleX from 0, and the +12.4% chip pulses exactly twice. */

/* No JavaScript — the donut is a conic-gradient masked to a ring; @property makes its from-angle animatable so the whole allocation slowly rotates. */
```
