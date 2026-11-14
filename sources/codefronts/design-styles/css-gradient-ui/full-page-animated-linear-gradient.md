---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/full-page-animated-linear-gradient/"
title: "Full-Page Animated Linear Gradient"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "The classic full-page moving gradient, done right: a 400%-oversized four-stop linear gradient panned with background-position on an ease-in-out loop, with a…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Page Animated Linear Gradient
Source: https://codefronts.com/design-styles/css-gradient-ui/full-page-animated-linear-gradient/

The classic full-page moving gradient, done right: a 400%-oversized four-stop linear gradient panned with background-position on an ease-in-out loop, with a launch-page layout on top — plus the oklch stop choices that stop it looking muddy midway.
## HTML
```html
<div class="cgu-09-group">
<section class="cgu-09" aria-label="Full page animated linear gradient demo">
  <div class="cgu-09__content">
    <p class="cgu-09__eyebrow">09 · Animated linear gradient</p>
    <h2 class="cgu-09__title">The background is breathing</h2>
    <p class="cgu-09__sub">A 400%-oversized gradient panned edge to edge over 18 seconds. The loop point is invisible because the last stop repeats the first.</p>
    <div class="cgu-09__row">
      <button class="cgu-09__btn" type="button">Get early access</button>
      <span class="cgu-09__hint">No credit card · 2-minute setup</span>
    </div>
    <ul class="cgu-09__ticks">
      <li>Last stop = first stop, so the cycle never snaps</li>
      <li>400% background-size — you only ever see a soft slice</li>
      <li>ease-in-out makes it dwell, breathe, return</li>
    </ul>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-09-group {
  display: block;
  width: 100%;
}

.cgu-09,
.cgu-09 *,
.cgu-09 *::before,
.cgu-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-09 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f4f2ff;
  background: linear-gradient(115deg,#0f0c29,#302b63,#24243e,#6d28d9,#0f0c29);
  background-size: 400% 400%;
  animation: cgu09-pan 18s ease-in-out infinite;
}

.cgu-09__content {
  width: min(640px,100%);
  text-align: center;
  display: grid;
  gap: 20px;
  justify-items: center;
}

.cgu-09__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: rgba(244,242,255,.7);
}

.cgu-09__title {
  font-size: clamp(36px,6vw,72px);
  font-weight: 850;
  letter-spacing: -.03em;
  line-height: 1.02;
  text-wrap: balance;
  text-shadow: 0 2px 34px rgba(0,0,0,.35);
}

.cgu-09__sub {
  max-width: 50ch;
  font-size: 16px;
  line-height: 1.65;
  color: rgba(244,242,255,.85);
  text-wrap: pretty;
}

.cgu-09__row {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 8px;
}

.cgu-09__btn {
  font: inherit;
  font-size: 15.5px;
  font-weight: 750;
  color: #1c1140;
  padding: 15px 34px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: linear-gradient(180deg,#ffffff,#e4dcff);
  box-shadow: 0 16px 36px -16px rgba(0,0,0,.5);
  transition: transform .3s,box-shadow .3s;
}

.cgu-09__btn:hover,
.cgu-09__btn:focus-visible {
  transform: translateY(-2px);
  box-shadow: 0 22px 44px -16px rgba(0,0,0,.6);
}

.cgu-09__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.cgu-09__hint {
  font-size: 13px;
  color: rgba(244,242,255,.7);
}

.cgu-09__ticks {
  list-style: none;
  display: grid;
  gap: 10px;
  margin-top: 26px;
  text-align: left;
}

.cgu-09__ticks li {
  position: relative;
  padding-left: 26px;
  font-size: 14px;
  line-height: 1.5;
  color: rgba(244,242,255,.82);
}

.cgu-09__ticks li::before {
  content: "✓";
  position: absolute;
  left: 0;
  top: 0;
  font-weight: 800;
  color: #c4b5fd;
}

@keyframes cgu09-pan {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-09 {
    animation: none;
    background-position: 0% 50%;
  }
}
```

## JavaScript
```js
/* No JavaScript — one oversized linear-gradient panned with background-position keyframes; the loop closes because the last stop repeats the first. */
```
