---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/crypto-wallet-balance-widget/"
title: "Crypto Wallet Balance Widget"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A clean crypto wallet balance card in Liquid Glass, wrapped in an animated neon gradient border that runs light around its curved edges — showing off the…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Crypto Wallet Balance Widget
Source: https://codefronts.com/components/css-liquid-glass-cards/crypto-wallet-balance-widget/

A clean crypto wallet balance card in Liquid Glass, wrapped in an animated neon gradient border that runs light around its curved edges — showing off the refraction along the glass rim. Balance, 24h change and a mini token list sit on the frosted face with tabular, high-contrast numbers.
## HTML
```html
<section class="lg-12" aria-label="Crypto wallet balance widget demo">
  <section class="lg-12__card" aria-label="Wallet balance">
    <header class="lg-12__head"><span class="lg-12__wallet">Main Wallet</span><span class="lg-12__addr" aria-label="Address 0x7a…3f9">0x7a…3f9</span></header>
    <p class="lg-12__cap">Total balance</p>
    <div class="lg-12__bal"><strong>$18,204.57</strong><span class="lg-12__chg" aria-label="up 3.2 percent in 24 hours">▲ 3.2%</span></div>
    <ul class="lg-12__tokens">
      <li><span class="lg-12__tk">◆ ETH</span><span class="lg-12__amt">4.21</span><span class="lg-12__usd">$14,088</span></li>
      <li><span class="lg-12__tk">● BTC</span><span class="lg-12__amt">0.052</span><span class="lg-12__usd">$3,410</span></li>
      <li><span class="lg-12__tk">▲ SOL</span><span class="lg-12__amt">18.0</span><span class="lg-12__usd">$706</span></li>
    </ul>
    <div class="lg-12__acts"><button class="lg-12__act" type="button">Send</button><button class="lg-12__act lg-12__act--alt" type="button">Receive</button></div>
  </section>
</section>
```
## CSS
```css
.lg-12,
.lg-12 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --ring {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.lg-12 {
  --n1: oklch(0.72 0.2 200);
  --n2: oklch(0.7 0.22 320);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 30% 10%,#0b1120,#020617 70%);
}

.lg-12__card {
  position: relative;
  width: min(320px,100%);
  padding: 22px;
  border-radius: 24px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 9%,rgba(8,12,24,.5));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.28),0 34px 70px -30px rgba(0,0,0,.9);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.lg-12__card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 24px;
  padding: 1.6px;
  background: conic-gradient(from var(--ring),var(--n1),var(--n2),var(--n1));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: lg-12-ring 5s linear infinite;
  pointer-events: none;
  filter: drop-shadow(0 0 6px var(--n1));
}

@keyframes lg-12-ring {
  to {
    --ring: 360deg;
  }
}

.lg-12__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.lg-12__wallet {
  font-size: 14px;
  font-weight: 800;
}

.lg-12__addr {
  font-size: 12px;
  color: rgba(255,255,255,.6);
  font-variant-numeric: tabular-nums;
}

.lg-12__cap {
  font-size: 11px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,255,255,.6);
  margin-top: 16px;
}

.lg-12__bal {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-top: 5px;
}

.lg-12__bal strong {
  font-size: 30px;
  font-weight: 800;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.lg-12__chg {
  font-size: 12px;
  font-weight: 700;
  color: #bbf7d0;
  padding: 3px 8px;
  border-radius: 999px;
  background: color-mix(in oklab,oklch(0.72 0.17 155) 45%,transparent);
}

.lg-12__tokens {
  list-style: none;
  display: grid;
  gap: 6px;
  margin: 18px 0;
}

.lg-12__tokens li {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 10px;
  align-items: center;
  padding: 10px 12px;
  border-radius: 12px;
  background: rgba(255,255,255,.06);
  font-size: 13px;
}

.lg-12__tk {
  font-weight: 700;
}

.lg-12__amt {
  color: rgba(255,255,255,.8);
  font-variant-numeric: tabular-nums;
}

.lg-12__usd {
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.lg-12__acts {
  display: flex;
  gap: 10px;
}

.lg-12__act {
  flex: 1;
  min-height: 44px;
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  color: #020617;
  background: linear-gradient(120deg,var(--n1),var(--n2));
  box-shadow: 0 10px 24px -12px var(--n1);
}

.lg-12__act--alt {
  color: #fff;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.28);
}

.lg-12__act:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-12__card::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a conic-gradient masked to the border-box (mask-composite:exclude) with an @property --ring angle animation runs neon light around the curved glass rim, refracting along the edge. */
```
