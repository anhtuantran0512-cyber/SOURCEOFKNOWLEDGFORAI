---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-moving-gradient-cta-button/"
title: "CSS Moving Gradient CTA Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "An eye-catching call-to-action button with an infinite colour-cycling gradient background that shifts through violet, cyan, and rose — no JavaScript, no images."
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Moving Gradient CTA Button
Source: https://codefronts.com/motion/css-animated-buttons/css-moving-gradient-cta-button/

An eye-catching call-to-action button with an infinite colour-cycling gradient background that shifts through violet, cyan, and rose — no JavaScript, no images.
## HTML
```html
<div class="ab-07">
  <div class="ab-07__card">
    <p class="ab-07__eyebrow">Limited Time Offer</p>
    <h2 class="ab-07__heading">Start Your Free Trial</h2>
    <p class="ab-07__body">14 days free, no credit card required. Cancel anytime with one click.</p>
    <button class="ab-07__btn">Claim Your Free Trial →</button>
  </div>
</div>
```
## CSS
```css
.ab-07,
.ab-07 *,
.ab-07 *::before,
.ab-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-07 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ab-07 {
  font-family: system-ui,sans-serif;
  background: #0a0a14;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.ab-07__card {
  background: #13131f;
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 16px;
  padding: 2.5rem 2rem;
  max-width: 440px;
  text-align: center;
}

.ab-07__eyebrow {
  font-size: .72rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #a78bfa;
  margin-bottom: .75rem;
}

.ab-07__heading {
  font-size: 1.8rem;
  font-weight: 800;
  color: #f1f5f9;
  margin-bottom: .75rem;
}

.ab-07__body {
  font-size: .9rem;
  color: #94a3b8;
  margin-bottom: 1.75rem;
  line-height: 1.6;
}

.ab-07__btn {
  display: inline-block;
  padding: .9rem 2.4rem;
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
  background: linear-gradient(90deg,#7c3aed,#06b6d4,#f43f5e,#7c3aed);
  background-size: 300% 300%;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  outline: none;
  letter-spacing: .03em;
  animation: ab-07-shift 4s ease infinite;
  will-change: background-position;
  box-shadow: 0 4px 20px rgba(124,58,237,.4);
  transition: filter .2s,box-shadow .2s,transform .15s;
}

.ab-07__btn:hover {
  filter: brightness(1.12);
  box-shadow: 0 6px 32px rgba(124,58,237,.6);
  transform: translateY(-2px);
}

.ab-07__btn:active {
  transform: translateY(0);
  filter: brightness(.95);
}

@keyframes ab-07-shift {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-07__btn {
    animation: none;
    background: linear-gradient(90deg,#7c3aed,#06b6d4);
  }
}
```
