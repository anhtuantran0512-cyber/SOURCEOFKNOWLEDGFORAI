---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/feature-usp-text-ticker/"
title: "Feature / USP Text Ticker — E-commerce Benefit Marquee"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The workhorse of e-commerce headers: an uppercase benefits ticker ('Free worldwide shipping • 30-day returns • 24/7 support') that loops seamlessly, slows to…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature / USP Text Ticker — E-commerce Benefit Marquee
Source: https://codefronts.com/motion/css-infinite-marquee/feature-usp-text-ticker/

The workhorse of e-commerce headers: an uppercase benefits ticker ('Free worldwide shipping • 30-day returns • 24/7 support') that loops seamlessly, slows to half speed on hover so it stays readable, and collapses to a static wrapped list for reduced-motion users — nothing is ever lost, only the motion.
## HTML
```html
<section class="mqs-04" aria-label="USP text ticker marquee demo">
  <div class="mqs-04__wrap">
    <div class="mqs-04__band">
      <div class="mqs-04__group">
        <span class="mqs-04__item">Free worldwide shipping</span><span class="mqs-04__sep" aria-hidden="true">◆</span>
        <span class="mqs-04__item">30-day no-questions returns</span><span class="mqs-04__sep" aria-hidden="true">◆</span>
        <span class="mqs-04__item">24/7 human support</span><span class="mqs-04__sep" aria-hidden="true">◆</span>
        <span class="mqs-04__item">Carbon-neutral delivery</span><span class="mqs-04__sep" aria-hidden="true">◆</span>
      </div>
      <div class="mqs-04__group" aria-hidden="true">
        <span class="mqs-04__item">Free worldwide shipping</span><span class="mqs-04__sep">◆</span>
        <span class="mqs-04__item">30-day no-questions returns</span><span class="mqs-04__sep">◆</span>
        <span class="mqs-04__item">24/7 human support</span><span class="mqs-04__sep">◆</span>
        <span class="mqs-04__item">Carbon-neutral delivery</span><span class="mqs-04__sep">◆</span>
      </div>
    </div>
    <div class="mqs-04__ctrl">
      <input class="mqs-04__pauseBox" type="checkbox" id="mqs-04-pause">
      <label class="mqs-04__pauseBtn" for="mqs-04-pause">Pause ticker</label>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-04,
.mqs-04 *,
.mqs-04 *::before,
.mqs-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-04 {
  min-height: 100vh;
  width: 100%;
  --gap: 28px;
  --speed: 20s;
  --band: #14532d;
  --ink: #ecfdf5;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f6f8f6;
  padding: 72px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.mqs-04__wrap {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.mqs-04__band {
  width: 100%;
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  background: var(--band);
  padding-block: 13px;
}

.mqs-04__group {
  flex: none;
  display: flex;
  align-items: center;
  gap: var(--gap);
  animation: mqs-04-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-04-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-04__band:hover .mqs-04__group {
  animation-duration: calc(var(--speed) * 2);
}

.mqs-04:has(.mqs-04__pauseBox:checked) .mqs-04__group {
  animation-play-state: paused;
}

.mqs-04__item {
  flex: none;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink);
  line-height: 1;
}

.mqs-04__sep {
  flex: none;
  font-size: 8px;
  color: #86efac;
}

.mqs-04__ctrl {
  display: flex;
}

.mqs-04__pauseBox {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.mqs-04__pauseBtn {
  font-size: 12px;
  font-weight: 600;
  color: #4b5563;
  border: 1px solid #d1d5db;
  border-radius: 999px;
  padding: 6px 14px;
  cursor: pointer;
  user-select: none;
}

.mqs-04__pauseBtn:hover {
  color: #14532d;
  border-color: #14532d;
}

.mqs-04__pauseBox:focus-visible + .mqs-04__pauseBtn {
  outline: 2px solid #14532d;
  outline-offset: 2px;
}

.mqs-04:has(.mqs-04__pauseBox:checked) .mqs-04__pauseBtn::after {
  content: ' — paused';
}

@media (prefers-reduced-motion: reduce) {
  .mqs-04__group {
    animation: none;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
  }

  .mqs-04__group[aria-hidden="true"] {
    display: none;
  }

  .mqs-04__ctrl {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hover legibility comes from doubling animation-duration (modern engines recalc position proportionally, so it relaxes instead of snapping). */
```
