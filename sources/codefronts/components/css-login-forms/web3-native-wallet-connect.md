---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/web3-native-wallet-connect/"
title: "Web3 Native Wallet Connect"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The non-traditional auth flow for crypto / AI toolkits: a tidy grid of third-party connection tiles — MetaMask, WalletConnect, Coinbase, Ledger — with…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Web3 Native Wallet Connect
Source: https://codefronts.com/components/css-login-forms/web3-native-wallet-connect/

The non-traditional auth flow for crypto / AI toolkits: a tidy grid of third-party connection tiles — MetaMask, WalletConnect, Coinbase, Ledger — with strict, uniform bounding boxes and a crisp hardware-accelerated lift on hover.
## HTML
```html
<section class="lf-04">
  <div class="lf-04__card">
    <h1 class="lf-04__h">Connect a wallet</h1>
    <p class="lf-04__sub">Choose how you'd like to sign in to the app.</p>
    <div class="lf-04__grid">
      <button class="lf-04__tile" style="--tint:45" type="button"><span class="lf-04__ic" aria-hidden="true">🦊</span><span class="lf-04__nm">MetaMask</span><span class="lf-04__meta">Popular</span></button>
      <button class="lf-04__tile" style="--tint:250" type="button"><span class="lf-04__ic" aria-hidden="true">◈</span><span class="lf-04__nm">WalletConnect</span><span class="lf-04__meta">Mobile</span></button>
      <button class="lf-04__tile" style="--tint:255" type="button"><span class="lf-04__ic" aria-hidden="true">◉</span><span class="lf-04__nm">Coinbase</span><span class="lf-04__meta">Custodial</span></button>
      <button class="lf-04__tile" style="--tint:200" type="button"><span class="lf-04__ic" aria-hidden="true">▦</span><span class="lf-04__nm">Ledger</span><span class="lf-04__meta">Hardware</span></button>
    </div>
    <p class="lf-04__foot">By connecting you agree to the <a href="#">Terms</a>.</p>
  </div>
</section>
```
## CSS
```css
.lf-04,
.lf-04 *,
.lf-04 *::before,
.lf-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-04 {
  --radius: 14px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0b0d12;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  color: #e8ebf3;
}

.lf-04__card {
  width: min(420px,100%);
  background: #14171f;
  border: 1px solid #232734;
  border-radius: 20px;
  padding: 30px 26px;
  box-shadow: 0 30px 70px -44px #000;
}

.lf-04__h {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.lf-04__sub {
  font-size: 13.5px;
  color: #8b92a6;
  margin: 5px 0 20px;
}

.lf-04__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 12px;
}

.lf-04__tile {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
  padding: 16px 15px;
  cursor: pointer;
  background: #1b1f2a;
  border: 1.5px solid #2a2f3d;
  border-radius: var(--radius);
  color: #e8ebf3;
  text-align: left;
  transition: transform .16s,box-shadow .2s,border-color .2s;
}

.lf-04__tile:hover {
  transform: translateY(-3px);
  border-color: oklch(0.62 0.16 var(--tint));
  box-shadow: 0 12px 26px -14px oklch(0.62 0.18 var(--tint)/.6);
}

.lf-04__tile:focus-visible {
  outline: 3px solid oklch(0.62 0.18 var(--tint)/.6);
  outline-offset: 2px;
}

.lf-04__ic {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 10px;
  font-size: 18px;
  background: color-mix(in oklch,oklch(0.62 0.16 var(--tint)) 22%,#14171f);
}

.lf-04__nm {
  font-size: 14.5px;
  font-weight: 600;
}

.lf-04__meta {
  font-size: 11.5px;
  color: #7c8398;
}

.lf-04__foot {
  font-size: 12px;
  color: #7c8398;
  margin-top: 18px;
  text-align: center;
}

.lf-04__foot a {
  color: oklch(0.7 0.14 250);
  text-decoration: none;
}

.lf-04__foot a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .lf-04__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-04__tile {
    transition: box-shadow .2s,border-color .2s;
  }

  .lf-04__tile:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a responsive CSS Grid of uniform connector buttons with GPU translateY hover. */
```
