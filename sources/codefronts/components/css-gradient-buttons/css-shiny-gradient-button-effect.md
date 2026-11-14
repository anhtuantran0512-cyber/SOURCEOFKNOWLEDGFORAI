---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-shiny-gradient-button-effect/"
title: "CSS Shiny Gradient Button Effect"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A discount-coupon CTA on a royal purple-to-blue gradient with a skewed white sheen streaking across every few seconds — the classic landing-page shine, tuned…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shiny Gradient Button Effect
Source: https://codefronts.com/components/css-gradient-buttons/css-shiny-gradient-button-effect/

A discount-coupon CTA on a royal purple-to-blue gradient with a skewed white sheen streaking across every few seconds — the classic landing-page shine, tuned not to strobe.
## HTML
```html
<div class="gb-09">
  <div class="gb-09__coupon">
    <p class="gb-09__pct">-30%</p>
    <p class="gb-09__label">Summer drop · 48h only</p>
    <button class="gb-09__btn" type="button">Claim your offer</button>
    <p class="gb-09__code">Use code <b>SOLSTICE30</b> at checkout</p>
  </div>
</div>
```
## CSS
```css
.gb-09,
.gb-09 *,
.gb-09 *::before,
.gb-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-09 ::selection {
  background: #facc15;
  color: #2e1065;
}

.gb-09 {
  --royal: #4c1d95;
  --iris: #6d28d9;
  --blue: #2563eb;
  --gold: #facc15;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: linear-gradient(170deg,#f4f1ff 0%,#eef4ff 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-09__coupon {
  position: relative;
  width: 100%;
  max-width: 400px;
  background: #fff;
  border-radius: 22px;
  padding: 38px 34px 34px;
  text-align: center;
  box-shadow: 0 26px 60px -30px rgba(76,29,149,.35);
  overflow: hidden;
}

.gb-09__coupon::before {
  content: "";
  position: absolute;
  inset: 0 0 auto;
  height: 6px;
  background: linear-gradient(90deg,var(--royal),var(--blue),var(--gold));
}

.gb-09__pct {
  font-size: 52px;
  font-weight: 900;
  letter-spacing: -2px;
  background: linear-gradient(120deg,var(--royal),var(--blue));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  line-height: 1;
  margin-bottom: 6px;
}

.gb-09__label {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: #8f86b8;
  margin-bottom: 26px;
}

.gb-09__btn {
  position: relative;
  width: 100%;
  padding: 17px 30px;
  border: none;
  border-radius: 14px;
  font-family: inherit;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .3px;
  color: #fff;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  background: linear-gradient(120deg,var(--royal) 0%,var(--iris) 45%,var(--blue) 100%);
  box-shadow: 0 12px 30px -10px rgba(109,40,217,.55);
  transition: transform .25s ease,box-shadow .35s ease;
  -webkit-tap-highlight-color: transparent;
}
/* The sheen: a skewed translucent streak parked off-canvas, swept
   across on an infinite keyframe with a long idle gap so it flashes
   every few seconds instead of strobing. */

.gb-09__btn::after {
  content: "";
  position: absolute;
  top: -20%;
  bottom: -20%;
  left: 0;
  width: 28%;
  background: linear-gradient(105deg,
      transparent 0%,
      rgba(255,255,255,.05) 30%,
      rgba(255,255,255,.55) 50%,
      rgba(255,255,255,.05) 70%,
      transparent 100%);
  transform: translateX(-220%) skewX(-20deg);
  animation: gb-09-sheen 4.2s cubic-bezier(.4,0,.2,1) infinite;
  pointer-events: none;
}

@keyframes gb-09-sheen {
  0% {
    transform: translateX(-220%) skewX(-20deg);
  }

  28% {
    transform: translateX(520%) skewX(-20deg);
  }

  100% {
    transform: translateX(520%) skewX(-20deg);
  }
}

.gb-09__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 18px 40px -12px rgba(37,99,235,.6);
}

.gb-09__btn:hover::after {
  animation-duration: 1.6s;
}

.gb-09__btn:active {
  transform: translateY(0) scale(.985);
}

.gb-09__btn:focus-visible {
  outline: 3px solid var(--blue);
  outline-offset: 3px;
}

.gb-09__code {
  margin-top: 18px;
  font-size: 13px;
  color: #8f86b8;
}

.gb-09__code b {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  color: var(--royal);
  background: #f4f1ff;
  padding: 3px 10px;
  border-radius: 6px;
  border: 1px dashed #cfc4f5;
}

@media (prefers-reduced-motion: reduce) {
  .gb-09__btn {
    transition: none;
  }

  .gb-09__btn::after {
    animation: none;
    transform: translateX(-220%) skewX(-20deg);
  }

  .gb-09__btn:hover {
    transform: none;
  }
}
```
