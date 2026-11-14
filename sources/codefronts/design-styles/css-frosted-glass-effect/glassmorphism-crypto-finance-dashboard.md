---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphism-crypto-finance-dashboard/"
title: "Glassmorphism Crypto Finance Dashboard"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A wide-format crypto portfolio dashboard with an animated SVG sparkline chart, count-up balance animation, four holdings rows with allocation bars,…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Crypto Finance Dashboard
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphism-crypto-finance-dashboard/

A wide-format crypto portfolio dashboard with an animated SVG sparkline chart, count-up balance animation, four holdings rows with allocation bars, period-tab switching, and three stat mini-cards — all on a deep dark background with teal ambient glow.
## HTML
```html
<div class="fg-11">
  <div class="fg-06__bg" aria-hidden="true">
    <div class="fg-06__glow fg-06__glow--1"></div>
    <div class="fg-06__glow fg-06__glow--2"></div>
    <div class="fg-06__dots"></div>
  </div>
  <div class="fg-06__card">
    <div class="fg-06__hd">
      <div>
        <p class="fg-06__hd-lbl">Portfolio Overview</p>
        <div class="fg-06__tabs" role="tablist" aria-label="Time period">
          <button class="fg-06__tab is-active" role="tab" aria-selected="true">1D</button>
          <button class="fg-06__tab" role="tab" aria-selected="false">1W</button>
          <button class="fg-06__tab" role="tab" aria-selected="false">1M</button>
          <button class="fg-06__tab" role="tab" aria-selected="false">1Y</button>
        </div>
      </div>
      <div class="fg-06__bal-wrap">
        <p class="fg-06__bal" id="fg-11-balance" aria-live="polite">$0.00</p>
        <p class="fg-06__chg">&#9650; $2,847.23 <span class="fg-06__pct">(+3.49%)</span></p>
      </div>
    </div>
    <div class="fg-06__chart-wrap" aria-hidden="true">
      <svg class="fg-06__chart" viewBox="0 0 600 120" preserveAspectRatio="none">
        <defs>
          <linearGradient id="fg-11-grad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="rgba(20,184,166,.38)"/>
            <stop offset="100%" stop-color="rgba(20,184,166,0)"/>
          </linearGradient>
        </defs>
        <path class="fg-06__chart-fill" d="M0,90 C30,85 60,70 100,65 C140,60 160,75 200,55 C240,35 260,45 300,30 C340,15 380,40 420,25 C460,10 500,35 540,20 C570,12 590,18 600,15 L600,120 L0,120 Z" fill="url(#fg-11-grad)"/>
        <path class="fg-06__chart-line" d="M0,90 C30,85 60,70 100,65 C140,60 160,75 200,55 C240,35 260,45 300,30 C340,15 380,40 420,25 C460,10 500,35 540,20 C570,12 590,18 600,15" fill="none" stroke="#14b8a6" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="fg-06__body">
      <div class="fg-06__holdings">
        <p class="fg-06__sec-ttl">Holdings</p>
        <div class="fg-06__holding">
          <div class="fg-06__coin" style="background:linear-gradient(135deg,#f59e0b,#d97706)"><svg width="14" height="14" viewBox="0 0 24 24" fill="white" aria-label="Bitcoin"><path d="M11.5 9.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5S13.83 11 13 11s-1.5-.67-1.5-1.5zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15v1h-2v-1H9v-2h4v-1h-3a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h1V7h2v1h2v2h-4v1h3a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-1z"/></svg></div>
          <div class="fg-06__hinfo"><span>Bitcoin</span><small>BTC</small></div>
          <div class="fg-06__hbar"><div class="fg-06__hbar-fill" style="width:53.6%;background:#f59e0b;animation-delay:.1s"></div></div>
          <div class="fg-06__hval"><span>$45,230</span><small class="fg-06__up">&#9650; 2.4%</small></div>
        </div>
        <div class="fg-06__holding">
          <div class="fg-06__coin" style="background:linear-gradient(135deg,#6366f1,#4338ca)"><svg width="14" height="14" viewBox="0 0 24 24" fill="white" aria-label="Ethereum"><path d="M11.944 17.97L4.58 13.62 11.943 24l7.37-10.38-7.372 4.35zM12.056 0L4.69 12.223l7.365 4.354 7.365-4.35L12.056 0z"/></svg></div>
          <div class="fg-06__hinfo"><span>Ethereum</span><small>ETH</small></div>
          <div class="fg-06__hbar"><div class="fg-06__hbar-fill" style="width:33.3%;background:#6366f1;animation-delay:.2s"></div></div>
          <div class="fg-06__hval"><span>$28,140</span><small class="fg-06__up">&#9650; 5.1%</small></div>
        </div>
        <div class="fg-06__holding">
          <div class="fg-06__coin" style="background:linear-gradient(135deg,#8b5cf6,#7c3aed)"><svg width="14" height="14" viewBox="0 0 24 24" fill="white" aria-label="Solana"><polygon points="12,2 22,8.5 22,15.5 12,22 2,15.5 2,8.5"/></svg></div>
          <div class="fg-06__hinfo"><span>Solana</span><small>SOL</small></div>
          <div class="fg-06__hbar"><div class="fg-06__hbar-fill" style="width:9.9%;background:#8b5cf6;animation-delay:.3s"></div></div>
          <div class="fg-06__hval"><span>$8,420</span><small class="fg-06__dn">&#9660; 1.2%</small></div>
        </div>
        <div class="fg-06__holding">
          <div class="fg-06__coin" style="background:linear-gradient(135deg,#10b981,#059669)"><svg width="14" height="14" viewBox="0 0 24 24" fill="white" aria-label="USD Coin"><circle cx="12" cy="12" r="10"/><path d="M12 6v12M8 8.5h5.5a2.5 2.5 0 0 1 0 5H10a2.5 2.5 0 0 0 0 5H16" stroke="#059669" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></div>
          <div class="fg-06__hinfo"><span>USD Coin</span><small>USDC</small></div>
          <div class="fg-06__hbar"><div class="fg-06__hbar-fill" style="width:3.2%;background:#10b981;animation-delay:.4s"></div></div>
          <div class="fg-06__hval"><span>$2,602</span><small class="fg-06__nt">&#8212; 0.0%</small></div>
        </div>
      </div>
      <div class="fg-06__stats">
        <div class="fg-06__stat-card">
          <p class="fg-06__stat-lbl">Today&rsquo;s P&amp;L</p>
          <p class="fg-06__stat-val fg-06__up">+$2,847</p>
          <p class="fg-06__stat-sub">+3.49% today</p>
        </div>
        <div class="fg-06__stat-card">
          <p class="fg-06__stat-lbl">Open Positions</p>
          <p class="fg-06__stat-val">4</p>
          <p class="fg-06__stat-sub">2 in profit</p>
        </div>
        <div class="fg-06__stat-card">
          <p class="fg-06__stat-lbl">Portfolio Score</p>
          <p class="fg-06__stat-val fg-06__grad-txt">A+</p>
          <p class="fg-06__stat-sub">Diversified</p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-11,
.fg-11 *,
.fg-11 *::before,
.fg-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-11 ::selection {
  background: rgba(20,184,166,.4);
  color: #fff;
}

.fg-11 {
  --c-bg: #030308;
  --c-a: #14b8a6;
  --c-glass: rgba(255,255,255,.05);
  --c-border: rgba(255,255,255,.09);
  --c-text: #e2e8f4;
  --c-muted: rgba(226,232,244,.5);
  --t: .25s ease;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-bg);
  position: relative;
  overflow: hidden;
  padding: 40px 16px;
}

.fg-06__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-06__glow {
  position: absolute;
  border-radius: 50%;
}

.fg-06__glow--1 {
  width: 480px;
  height: 480px;
  background: radial-gradient(circle,rgba(20,184,166,.18),transparent 70%);
  top: -120px;
  left: -100px;
  animation: fg-11-g1 24s ease-in-out infinite alternate;
}

.fg-06__glow--2 {
  width: 380px;
  height: 380px;
  background: radial-gradient(circle,rgba(99,102,241,.14),transparent 70%);
  bottom: -100px;
  right: -80px;
  animation: fg-11-g2 28s ease-in-out infinite alternate;
}

.fg-06__dots {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255,255,255,.04) 1px,transparent 1px);
  background-size: 22px 22px;
}

@keyframes fg-11-g1 {
  to {
    transform: translate(80px,100px) scale(1.2);
  }
}

@keyframes fg-11-g2 {
  to {
    transform: translate(-80px,-80px) scale(1.15);
  }
}

.fg-06__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 860px;
  background: var(--c-glass);
  backdrop-filter: blur(20px) saturate(150%);
  -webkit-backdrop-filter: blur(20px) saturate(150%);
  border: 1px solid var(--c-border);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 12px 60px rgba(0,0,0,.6),0 1px 0 rgba(255,255,255,.07) inset;
}

.fg-06__hd {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 24px 26px 0;
  flex-wrap: wrap;
  gap: 12px;
}

.fg-06__hd-lbl {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .5px;
  text-transform: uppercase;
  color: var(--c-muted);
  margin-bottom: 10px;
}

.fg-06__tabs {
  display: flex;
  gap: 4px;
}

.fg-06__tab {
  padding: 5px 13px;
  border: 1px solid var(--c-border);
  border-radius: 8px;
  background: transparent;
  color: var(--c-muted);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background var(--t),color var(--t),border-color var(--t);
}

.fg-06__tab.is-active {
  background: rgba(20,184,166,.14);
  border-color: rgba(20,184,166,.4);
  color: var(--c-a);
}

.fg-06__bal-wrap {
  text-align: right;
}

.fg-06__bal {
  font-size: 32px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.5px;
  margin-bottom: 4px;
}

.fg-06__chg {
  font-size: 14px;
  font-weight: 600;
  color: #22c55e;
}

.fg-06__pct {
  opacity: .8;
}

.fg-06__chart-wrap {
  padding: 12px 0 0;
  height: 130px;
}

.fg-06__chart {
  width: 100%;
  height: 100%;
  display: block;
}

.fg-06__chart-line {
  stroke-dasharray: 1200;
  stroke-dashoffset: 1200;
  animation: fg-11-draw 1.5s ease-out .2s forwards;
}

.fg-06__chart-fill {
  opacity: 0;
  animation: fg-11-fade .5s ease-out 1.3s forwards;
}

@keyframes fg-11-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes fg-11-fade {
  to {
    opacity: 1;
  }
}

.fg-06__body {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.fg-06__holdings {
  padding: 18px 26px;
  border-right: 1px solid var(--c-border);
}

.fg-06__sec-ttl {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .5px;
  text-transform: uppercase;
  color: var(--c-muted);
  margin-bottom: 12px;
}

.fg-06__holding {
  display: grid;
  grid-template-columns: 32px 1fr 80px 80px;
  gap: 10px;
  align-items: center;
  padding: 9px 0;
  border-bottom: 1px solid rgba(255,255,255,.05);
}

.fg-06__holding:last-child {
  border-bottom: none;
}

.fg-06__coin {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.fg-06__hinfo span {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: var(--c-text);
}

.fg-06__hinfo small {
  display: block;
  font-size: 11px;
  color: var(--c-muted);
}

.fg-06__hbar {
  height: 4px;
  border-radius: 2px;
  background: rgba(255,255,255,.08);
}

.fg-06__hbar-fill {
  height: 100%;
  border-radius: 2px;
  animation: fg-11-bar .9s ease-out both;
}

@keyframes fg-11-bar {
  from {
    width: 0!important;
  }
}

.fg-06__hval {
  text-align: right;
}

.fg-06__hval span {
  display: block;
  font-size: 13px;
  font-weight: 700;
  color: var(--c-text);
}

.fg-06__hval small {
  font-size: 11px;
  font-weight: 600;
}

.fg-06__up {
  color: #22c55e;
}

.fg-06__dn {
  color: #f87171;
}

.fg-06__nt {
  color: var(--c-muted);
}

.fg-06__stats {
  padding: 18px 22px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.fg-06__stat-card {
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
  padding: 14px 16px;
}

.fg-06__stat-lbl {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .3px;
  text-transform: uppercase;
  color: var(--c-muted);
  margin-bottom: 4px;
}

.fg-06__stat-val {
  font-size: 24px;
  font-weight: 800;
  color: var(--c-text);
  margin-bottom: 2px;
}

.fg-06__grad-txt {
  background: linear-gradient(90deg,#10b981,#14b8a6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fg-06__stat-sub {
  font-size: 11px;
  color: var(--c-muted);
}

@media (max-width: 640px) {
  .fg-06__body {
    grid-template-columns: 1fr;
  }

  .fg-06__holdings {
    border-right: none;
    border-bottom: 1px solid var(--c-border);
  }

  .fg-06__hd {
    flex-direction: column-reverse;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-06__glow,
    .fg-06__chart-line,
    .fg-06__chart-fill,
    .fg-06__hbar-fill {
    animation: none;
  }

  .fg-06__tab {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-11');
  if(!r)return;
  var balEl=r.querySelector('#fg-11-balance');
  if(balEl){
    var target=84392.18,start=Date.now(),dur=1200;
    function tick(){
      var p=Math.min((Date.now()-start)/dur,1);
      var e=1-Math.pow(1-p,3);
      balEl.textContent='$'+(e*target).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
      if(p<1)requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var tabs=r.querySelectorAll('.fg-06__tab');
  tabs.forEach(function(t){
    t.addEventListener('click',function(){
      tabs.forEach(function(x){x.classList.remove('is-active');x.setAttribute('aria-selected','false')});
      t.classList.add('is-active');t.setAttribute('aria-selected','true');
    });
  });
})();
```
