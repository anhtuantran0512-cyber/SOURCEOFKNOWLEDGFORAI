---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/cyberpunk-crypto-tracker/"
title: "Cyberpunk Crypto Tracker"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A neon-on-charcoal financial data table where hovering the <tbody> dims all rows to 40% opacity and the hovered row glows back to full brightness with a cyan…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Crypto Tracker
Source: https://codefronts.com/snippets/css-table-styles/cyberpunk-crypto-tracker/

A neon-on-charcoal financial data table where hovering the <tbody> dims all rows to 40% opacity and the hovered row glows back to full brightness with a cyan left-border laser line.
## HTML
```html
<div class="ct-04">
  <div class="ct-04__header">
    <div class="ct-04__logo">CYPTO.NEXUS</div>
    <div class="ct-04__live"><span class="ct-04__live-dot"></span>LIVE</div>
  </div>
  <table>
    <thead>
      <tr>
        <th>#&nbsp;&nbsp;Asset</th>
        <th>Price</th>
        <th>24h %</th>
        <th>Market Cap</th>
        <th>Volume</th>
        <th>7d Chart</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><div class="ct-04__coin"><div class="ct-04__icon" style="color:#f7931a;border-color:rgba(247,147,26,0.3);background:rgba(247,147,26,0.06)">₿</div><div><div class="ct-04__ticker">BTC</div><div class="ct-04__cname">Bitcoin</div></div></div></td>
        <td><div class="ct-04__price">$67,420</div></td>
        <td><span class="ct-04__chg ct-04__chg--bull">▲ 3.14%</span></td>
        <td><div class="ct-04__mkt">$1.31T</div></td>
        <td><div class="ct-04__vol">$42.8B</div></td>
        <td><div class="ct-04__spark">
          <div class="ct-04__bar" style="height:40%;background:var(--bull);animation-delay:.05s"></div>
          <div class="ct-04__bar" style="height:55%;background:var(--bull);animation-delay:.1s"></div>
          <div class="ct-04__bar" style="height:45%;background:var(--bull);animation-delay:.15s"></div>
          <div class="ct-04__bar" style="height:70%;background:var(--bull);animation-delay:.2s"></div>
          <div class="ct-04__bar" style="height:60%;background:var(--bull);animation-delay:.25s"></div>
          <div class="ct-04__bar" style="height:85%;background:var(--bull);animation-delay:.3s"></div>
          <div class="ct-04__bar" style="height:100%;background:var(--bull);animation-delay:.35s"></div>
        </div></td>
      </tr>
      <tr>
        <td><div class="ct-04__coin"><div class="ct-04__icon" style="color:#627eea;border-color:rgba(98,126,234,0.3);background:rgba(98,126,234,0.06)">Ξ</div><div><div class="ct-04__ticker">ETH</div><div class="ct-04__cname">Ethereum</div></div></div></td>
        <td><div class="ct-04__price">$3,890</div></td>
        <td><span class="ct-04__chg ct-04__chg--bear">▼ 1.22%</span></td>
        <td><div class="ct-04__mkt">$468B</div></td>
        <td><div class="ct-04__vol">$18.1B</div></td>
        <td><div class="ct-04__spark">
          <div class="ct-04__bar" style="height:90%;background:var(--bear);animation-delay:.05s"></div>
          <div class="ct-04__bar" style="height:75%;background:var(--bear);animation-delay:.1s"></div>
          <div class="ct-04__bar" style="height:80%;background:var(--bear);animation-delay:.15s"></div>
          <div class="ct-04__bar" style="height:60%;background:var(--bear);animation-delay:.2s"></div>
          <div class="ct-04__bar" style="height:55%;background:var(--bear);animation-delay:.25s"></div>
          <div class="ct-04__bar" style="height:45%;background:var(--bear);animation-delay:.3s"></div>
          <div class="ct-04__bar" style="height:35%;background:var(--bear);animation-delay:.35s"></div>
        </div></td>
      </tr>
      <tr>
        <td><div class="ct-04__coin"><div class="ct-04__icon" style="color:#00ffa3;border-color:rgba(0,255,163,0.3);background:rgba(0,255,163,0.06)">◎</div><div><div class="ct-04__ticker">SOL</div><div class="ct-04__cname">Solana</div></div></div></td>
        <td><div class="ct-04__price">$183.50</div></td>
        <td><span class="ct-04__chg ct-04__chg--bull">▲ 8.77%</span></td>
        <td><div class="ct-04__mkt">$84B</div></td>
        <td><div class="ct-04__vol">$6.4B</div></td>
        <td><div class="ct-04__spark">
          <div class="ct-04__bar" style="height:30%;background:var(--bull);animation-delay:.05s"></div>
          <div class="ct-04__bar" style="height:35%;background:var(--bull);animation-delay:.1s"></div>
          <div class="ct-04__bar" style="height:50%;background:var(--bull);animation-delay:.15s"></div>
          <div class="ct-04__bar" style="height:60%;background:var(--bull);animation-delay:.2s"></div>
          <div class="ct-04__bar" style="height:75%;background:var(--bull);animation-delay:.25s"></div>
          <div class="ct-04__bar" style="height:90%;background:var(--bull);animation-delay:.3s"></div>
          <div class="ct-04__bar" style="height:100%;background:var(--bull);animation-delay:.35s"></div>
        </div></td>
      </tr>
      <tr>
        <td><div class="ct-04__coin"><div class="ct-04__icon" style="color:#7b2fff;border-color:rgba(123,47,255,0.3);background:rgba(123,47,255,0.06)">⬡</div><div><div class="ct-04__ticker">AVAX</div><div class="ct-04__cname">Avalanche</div></div></div></td>
        <td><div class="ct-04__price">$41.20</div></td>
        <td><span class="ct-04__chg ct-04__chg--bear">▼ 0.55%</span></td>
        <td><div class="ct-04__mkt">$17B</div></td>
        <td><div class="ct-04__vol">$820M</div></td>
        <td><div class="ct-04__spark">
          <div class="ct-04__bar" style="height:60%;background:var(--warn);animation-delay:.05s"></div>
          <div class="ct-04__bar" style="height:65%;background:var(--warn);animation-delay:.1s"></div>
          <div class="ct-04__bar" style="height:50%;background:var(--warn);animation-delay:.15s"></div>
          <div class="ct-04__bar" style="height:70%;background:var(--warn);animation-delay:.2s"></div>
          <div class="ct-04__bar" style="height:55%;background:var(--warn);animation-delay:.25s"></div>
          <div class="ct-04__bar" style="height:48%;background:var(--warn);animation-delay:.3s"></div>
          <div class="ct-04__bar" style="height:42%;background:var(--warn);animation-delay:.35s"></div>
        </div></td>
      </tr>
    </tbody>
  </table>
</div>
```
## CSS
```css
.ct-04,
.ct-04 *,
.ct-04 *::before,
.ct-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-04 ::selection {
  background: #0ff;
  color: #000;
}

.ct-04 {
  --bg: #080810;
  --panel: #0d0d1a;
  --border: rgba(0,255,255,0.12);
  --text: #d0d8f0;
  --muted: #4a5280;
  --neon: #00ffff;
  --neon2: #7b2fff;
  --bull: #39ff14;
  --bear: #ff003c;
  --warn: #ffae00;
  font-family: 'Courier New', 'Segoe UI', monospace;
  background: var(--bg);
  padding: 28px 20px;
  min-height: 100vh;
  color: var(--text);
}

.ct-04__header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.ct-04__logo {
  font-size: 22px;
  font-weight: 900;
  letter-spacing: 3px;
  background: linear-gradient(90deg, var(--neon), var(--neon2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: none;
  animation: ct-04-logoflicker 4s ease-in-out infinite;
}

@keyframes ct-04-logoflicker {
  0%,
    95%,
    100% {
    opacity: 1;
  }

  96% {
    opacity: 0.6;
  }

  97% {
    opacity: 1;
  }

  98% {
    opacity: 0.7;
  }
}

.ct-04__live {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  color: var(--bull);
}

.ct-04__live-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--bull);
  animation: ct-04-livepulse 1.2s ease-in-out infinite;
}

@keyframes ct-04-livepulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(57,255,20,0.8);
  }

  70% {
    box-shadow: 0 0 0 6px rgba(57,255,20,0);
  }
}

.ct-04 table {
  width: 100%;
  border-collapse: collapse;
}

.ct-04 thead th {
  padding: 10px 16px;
  text-align: left;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  border-bottom: 1px solid var(--border);
}

.ct-04 thead th:not(:first-child) {
  text-align: right;
}

.ct-04 tbody tr {
  border-bottom: 1px solid rgba(255,255,255,0.04);
  transition: all 0.3s;
  cursor: pointer;
  position: relative;
}
/* The glow-row-hover: dim others on table hover, illuminate hovered row */

.ct-04 tbody:hover tr {
  opacity: 0.4;
}

.ct-04 tbody tr:hover {
  opacity: 1 !important;
  background: rgba(0,255,255,0.04);
  box-shadow: inset 0 0 30px rgba(0,255,255,0.05);
}

.ct-04 tbody tr:hover td:first-child::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 2px;
  background: var(--neon);
  box-shadow: 0 0 10px var(--neon);
}

.ct-04 tbody td {
  padding: 14px 16px;
  font-size: 13px;
  vertical-align: middle;
  position: relative;
}

.ct-04 tbody td:not(:first-child) {
  text-align: right;
  font-family: monospace;
}

.ct-04__coin {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ct-04__icon {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 900;
  border: 1px solid var(--border);
  background: rgba(255,255,255,0.04);
}

.ct-04__ticker {
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 1px;
  color: var(--neon);
}

.ct-04__cname {
  font-size: 11px;
  color: var(--muted);
}

.ct-04__price {
  font-weight: 700;
  font-size: 14px;
  color: var(--text);
}

.ct-04__mkt {
  font-size: 12px;
  color: var(--muted);
}

.ct-04__vol {
  font-size: 12px;
  color: var(--muted);
}

.ct-04__chg {
  font-weight: 700;
  font-size: 13px;
  padding: 3px 8px;
  border-radius: 5px;
  display: inline-block;
}

.ct-04__chg--bull {
  color: var(--bull);
  background: rgba(57,255,20,0.08);
}

.ct-04__chg--bear {
  color: var(--bear);
  background: rgba(255,0,60,0.08);
}
/* Sparkline bar */

.ct-04__spark {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 28px;
  justify-content: flex-end;
}

.ct-04__bar {
  width: 4px;
  border-radius: 2px 2px 0 0;
  animation: ct-04-barrise 0.6s ease-out backwards;
}

@keyframes ct-04-barrise {
  from {
    transform: scaleY(0);
    transform-origin: bottom;
  }

  to {
    transform: scaleY(1);
    transform-origin: bottom;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ct-04 tbody tr,
    .ct-04__logo,
    .ct-04__live-dot,
    .ct-04__bar {
    animation: none;
    transition: none;
  }
}
```
