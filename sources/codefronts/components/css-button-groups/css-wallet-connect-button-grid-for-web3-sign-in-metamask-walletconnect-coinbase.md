---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-wallet-connect-button-grid-for-web3-sign-in-metamask-walletconnect-coinbase/"
title: "CSS Wallet Connect Button Grid for Web3 Sign-In (MetaMask, WalletConnect, Coinbase)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "The Web3 connect-wallet modal, styled properly: a responsive grid of wallet sign-in buttons — MetaMask, WalletConnect, Coinbase, Ledger — each with a logo…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Wallet Connect Button Grid for Web3 Sign-In (MetaMask, WalletConnect, Coinbase)
Source: https://codefronts.com/components/css-button-groups/css-wallet-connect-button-grid-for-web3-sign-in-metamask-walletconnect-coinbase/

The Web3 connect-wallet modal, styled properly: a responsive grid of wallet sign-in buttons — MetaMask, WalletConnect, Coinbase, Ledger — each with a logo tile, name, status hint and a recommended badge. The most-wanted 'CSS wallet connect button grid Web3 sign-in' layout for dApps and crypto onboarding, dark-mode native and fully keyboard-operable.
## HTML
```html
<section class="btn-10" aria-label="Web3 wallet connect grid demo">
  <div class="btn-10__modal">
    <p class="btn-10__eyebrow">Connect</p>
    <h3 class="btn-10__title">Choose a wallet</h3>
    <p class="btn-10__sub">Sign in to continue. We never store your keys.</p>
    <div class="btn-10__grid">
      <button type="button" class="btn-10__tile btn-10__tile--rec">
        <span class="btn-10__flag">Recommended</span>
        <span class="btn-10__logo" style="--l:linear-gradient(135deg,#f6851b,#e2761b)">M</span>
        <span class="btn-10__name">MetaMask</span>
        <span class="btn-10__hint">Detected in browser</span>
      </button>
      <button type="button" class="btn-10__tile">
        <span class="btn-10__logo" style="--l:linear-gradient(135deg,#3b99fc,#1f6fe5)">W</span>
        <span class="btn-10__name">WalletConnect</span>
        <span class="btn-10__hint">Scan with app</span>
      </button>
      <button type="button" class="btn-10__tile">
        <span class="btn-10__logo" style="--l:linear-gradient(135deg,#2c5ff6,#0a3ecb)">C</span>
        <span class="btn-10__name">Coinbase</span>
        <span class="btn-10__hint">Popular</span>
      </button>
      <button type="button" class="btn-10__tile">
        <span class="btn-10__logo" style="--l:linear-gradient(135deg,#3a3a3a,#141414)">L</span>
        <span class="btn-10__name">Ledger</span>
        <span class="btn-10__hint">Hardware</span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-10,
.btn-10 *,
.btn-10 *::before,
.btn-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-10 {
  --a1: oklch(0.6 0.22 300);
  --a2: oklch(0.75 0.15 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 100% at 50% -10%,#1b1533,#0a0713);
  padding: 44px 20px;
}

.btn-10__modal {
  width: min(460px,100%);
  background: linear-gradient(180deg,rgba(40,30,70,.55),rgba(18,12,34,.85));
  border: 1px solid rgba(150,120,255,.2);
  border-radius: 22px;
  padding: 30px 28px 32px;
  box-shadow: 0 40px 90px -40px rgba(90,40,220,.6);
  backdrop-filter: blur(12px);
}

.btn-10__eyebrow {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .18em;
  text-transform: uppercase;
  background: linear-gradient(90deg,var(--a1),var(--a2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.btn-10__title {
  font-size: 26px;
  font-weight: 800;
  color: #f2eeff;
  letter-spacing: -.02em;
  margin: 5px 0 6px;
}

.btn-10__sub {
  font-size: 14px;
  color: rgba(220,210,255,.6);
  margin-bottom: 22px;
}

.btn-10__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(150px,1fr));
  gap: 12px;
}

.btn-10__tile {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 9px;
  padding: 18px 16px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 16px;
  cursor: pointer;
  text-align: left;
  transition: translate .2s,border-color .2s,background .2s;
}

.btn-10__tile:hover {
  translate: 0 -3px;
  border-color: var(--a2);
  background: rgba(255,255,255,.07);
}

.btn-10__tile--rec {
  border-color: transparent;
  background: linear-gradient(rgba(18,12,34,.9),rgba(18,12,34,.9)) padding-box,linear-gradient(135deg,var(--a1),var(--a2)) border-box;
  border: 1.5px solid transparent;
}

.btn-10__flag {
  position: absolute;
  top: -9px;
  right: 12px;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: #160a2c;
  background: linear-gradient(90deg,var(--a1),var(--a2));
  padding: 4px 9px;
  border-radius: 999px;
}

.btn-10__logo {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: var(--l);
  color: #fff;
  font-size: 20px;
  font-weight: 800;
}

.btn-10__name {
  font-size: 15.5px;
  font-weight: 750;
  color: #f2eeff;
}

.btn-10__hint {
  font-size: 12px;
  color: rgba(200,190,240,.55);
}

.btn-10__tile:focus-visible {
  outline: 3px solid var(--a2);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-10__tile {
    transition: none;
  }
}
```
