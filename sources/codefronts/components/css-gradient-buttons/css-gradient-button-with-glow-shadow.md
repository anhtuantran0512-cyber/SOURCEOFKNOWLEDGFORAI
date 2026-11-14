---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-button-with-glow-shadow/"
title: "CSS Gradient Button With Glow Shadow"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A pricing-card CTA whose coral-to-violet gradient is echoed by a blurred pseudo-element underneath, producing a hue-matched ambient glow instead of a flat…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Button With Glow Shadow
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-button-with-glow-shadow/

A pricing-card CTA whose coral-to-violet gradient is echoed by a blurred pseudo-element underneath, producing a hue-matched ambient glow instead of a flat black drop shadow.
## HTML
```html
<div class="gb-01">
  <div class="gb-01__card">
    <span class="gb-01__badge">Most Popular</span>
    <h3 class="gb-01__title">Pro Workspace</h3>
    <p class="gb-01__price"><strong>$24</strong> / month · billed yearly</p>
    <button class="gb-01__btn" type="button">Upgrade to Pro</button>
    <p class="gb-01__note">Cancel anytime · 14-day free trial</p>
  </div>
</div>
```
## CSS
```css
.gb-01,
.gb-01 *,
.gb-01 *::before,
.gb-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-01 ::selection {
  background: #ff6b9d;
  color: #fff;
}

.gb-01 {
  --grad-a: #ff6b6b;
  --grad-b: #c44dff;
  --grad-c: #7c5cff;
  --glow: rgba(196,77,255,.45);
  --ink: #2b2440;
  --card: #fffaf5;
  --dur: .45s;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: linear-gradient(160deg,#fdf3ec 0%,#f5ecfd 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-01__card {
  background: var(--card);
  border-radius: 24px;
  padding: 44px 40px 40px;
  max-width: 360px;
  width: 100%;
  text-align: center;
  box-shadow: 0 24px 60px -24px rgba(124,92,255,.18),0 2px 8px rgba(43,36,64,.05);
}

.gb-01__badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  color: #c44dff;
  background: rgba(196,77,255,.1);
  padding: 6px 14px;
  border-radius: 999px;
  margin-bottom: 18px;
}

.gb-01__title {
  font-size: 26px;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.5px;
  margin-bottom: 8px;
}

.gb-01__price {
  font-size: 15px;
  color: #8a819e;
  margin-bottom: 28px;
}

.gb-01__price strong {
  color: var(--ink);
  font-size: 20px;
}

.gb-01__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 17px 32px;
  border: none;
  border-radius: 16px;
  font-family: inherit;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .2px;
  color: #fff;
  cursor: pointer;
  background: linear-gradient(120deg,var(--grad-a) 0%,var(--grad-b) 55%,var(--grad-c) 100%);
  box-shadow: 0 10px 28px -6px var(--glow),0 4px 10px -4px rgba(255,107,107,.4);
  transition: transform var(--dur) cubic-bezier(.34,1.56,.64,1),box-shadow var(--dur) ease;
  -webkit-tap-highlight-color: transparent;
}
/* Duplicate gradient blurred underneath = hue-matched ambient glow */

.gb-01__btn::before {
  content: "";
  position: absolute;
  inset: 8px -4px -10px;
  border-radius: inherit;
  background: linear-gradient(120deg,var(--grad-a),var(--grad-b),var(--grad-c));
  filter: blur(22px);
  opacity: .55;
  z-index: -1;
  transition: opacity var(--dur) ease,transform var(--dur) ease;
}

.gb-01__btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 40px -8px var(--glow),0 8px 16px -6px rgba(255,107,107,.5);
}

.gb-01__btn:hover::before {
  opacity: .85;
  transform: scaleX(1.04);
}

.gb-01__btn:active {
  transform: translateY(-1px) scale(.985);
}

.gb-01__btn:focus-visible {
  outline: 3px solid #c44dff;
  outline-offset: 3px;
}

.gb-01__note {
  margin-top: 16px;
  font-size: 12.5px;
  color: #a89fbc;
}

@media (prefers-reduced-motion: reduce) {
  .gb-01__btn,
    .gb-01__btn::before {
    transition: none;
  }

  .gb-01__btn:hover {
    transform: none;
  }
}
```
