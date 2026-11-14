---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/interactive-gift-card-coupon-reveal/"
title: "Interactive Gift Card Coupon Reveal"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front displays a festive holiday gift card graphic with animated snowflakes; back reveals a copyable coupon code via the Clipboard API."
has_js: "true"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Gift Card Coupon Reveal
Source: https://codefronts.com/components/css-flip-cards/interactive-gift-card-coupon-reveal/

Front displays a festive holiday gift card graphic with animated snowflakes; back reveals a copyable coupon code via the Clipboard API.
## HTML
```html
<div class="fc-03">
  <div class="fc-03__scene">
    <div class="fc-03__card">
      <div class="fc-03__front">
        <span class="fc-03__flake">❄</span>
        <span class="fc-03__flake">✦</span>
        <span class="fc-03__flake">❄</span>
        <span class="fc-03__flake">✦</span>
        <div class="fc-03__logo">Nova Store</div>
        <div class="fc-03__gift-title">Holiday Gift Card</div>
        <div class="fc-03__amount">$50</div>
        <div class="fc-03__front-hint">Hover to reveal →</div>
      </div>
      <div class="fc-03__back">
        <div class="fc-03__back-label">Your Exclusive Coupon Code</div>
        <div class="fc-03__code-box" title="Click to copy">NOVA-XMAS-2025</div>
        <div class="fc-03__copy-tip">Click code to copy</div>
        <div class="fc-03__expiry">Expires <span>December 31, 2025</span></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-03,
.fc-03 *,
.fc-03 *::before,
.fc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-03 ::selection {
  background: #ec4899;
  color: #fff;
}

.fc-03 {
  --bg: #0c0510;
  --pink: #ec4899;
  --gold: #f59e0b;
  --rose: #fb7185;
  --white: #fff1f5;
  --card-w: 380px;
  --card-h: 240px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 30% 50%,#1a0520,#0c0510 70%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-03__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-03__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .8s cubic-bezier(.4,0,.2,1);
}

.fc-03__scene:hover .fc-03__card {
  transform: rotateY(180deg);
}

.fc-03__front,
.fc-03__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT — holiday gift card */

.fc-03__front {
  background: linear-gradient(135deg,#3b0764,#831843,#7c2d12);
  border: 1px solid rgba(236,72,153,.3);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.fc-03__front::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 70% 30%,rgba(245,158,11,.15),transparent 60%), radial-gradient(ellipse at 30% 80%,rgba(236,72,153,.2),transparent 50%);
}
/* snowflake decorations */

.fc-03__flake {
  position: absolute;
  font-size: 20px;
  opacity: .25;
  animation: fc-03-drift 4s ease-in-out infinite;
}

.fc-03__flake:nth-child(1) {
  top: 10%;
  left: 8%;
  animation-delay: 0s;
}

.fc-03__flake:nth-child(2) {
  top: 20%;
  right: 10%;
  font-size: 14px;
  animation-delay: .8s;
}

.fc-03__flake:nth-child(3) {
  bottom: 15%;
  left: 12%;
  font-size: 16px;
  animation-delay: 1.6s;
}

.fc-03__flake:nth-child(4) {
  bottom: 10%;
  right: 8%;
  animation-delay: 2.4s;
}

@keyframes fc-03-drift {
  0%,
    100% {
    transform: translateY(0) rotate(0);
  }

  50% {
    transform: translateY(-8px) rotate(15deg);
  }
}

.fc-03__logo {
  position: relative;
  z-index: 1;
  font-size: 12px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(255,241,245,.5);
  margin-bottom: 8px;
  font-weight: 600;
}

.fc-03__gift-title {
  position: relative;
  z-index: 1;
  font-size: 28px;
  font-weight: 900;
  text-align: center;
  line-height: 1.1;
  background: linear-gradient(135deg,#fbbf24,#f472b6,#c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fc-03__amount {
  position: relative;
  z-index: 1;
  margin-top: 10px;
  font-size: 42px;
  font-weight: 900;
  color: var(--gold);
  text-shadow: 0 0 30px rgba(245,158,11,.5);
}

.fc-03__front-hint {
  position: absolute;
  bottom: 16px;
  right: 16px;
  z-index: 1;
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,241,245,.3);
}
/* BACK — coupon code */

.fc-03__back {
  background: linear-gradient(135deg,#0a1628,#1e0833);
  border: 1px solid rgba(245,158,11,.25);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 32px;
  gap: 20px;
}

.fc-03__back::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 50%,rgba(245,158,11,.06),transparent 70%);
}

.fc-03__back-label {
  position: relative;
  z-index: 1;
  font-size: 10px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(255,241,245,.4);
  font-weight: 600;
}

.fc-03__code-box {
  position: relative;
  z-index: 1;
  background: rgba(245,158,11,.07);
  border: 2px dashed rgba(245,158,11,.4);
  border-radius: 12px;
  padding: 14px 28px;
  font-size: 22px;
  font-weight: 900;
  letter-spacing: .2em;
  color: var(--gold);
  text-align: center;
  font-family: 'Courier New',monospace;
  text-shadow: 0 0 20px rgba(245,158,11,.4);
  cursor: pointer;
  transition: background .2s;
  width: 100%;
}

.fc-03__code-box:hover {
  background: rgba(245,158,11,.14);
}

.fc-03__copy-tip {
  position: relative;
  z-index: 1;
  font-size: 10px;
  color: rgba(255,241,245,.3);
  letter-spacing: .08em;
}

.fc-03__expiry {
  position: relative;
  z-index: 1;
  font-size: 11px;
  color: rgba(255,241,245,.4);
}

.fc-03__expiry span {
  color: var(--rose);
}

@media (prefers-reduced-motion: reduce) {
  .fc-03__card {
    transition: none;
  }

  .fc-03__flake {
    animation: none;
  }
}
```

## JavaScript
```js
document.querySelector('.fc-03__code-box')?.addEventListener('click',function(){
  navigator.clipboard?.writeText('NOVA-XMAS-2025');
  const orig=this.textContent;this.textContent='✓ Copied!';
  setTimeout(()=>this.textContent=orig,2000);
});
```
