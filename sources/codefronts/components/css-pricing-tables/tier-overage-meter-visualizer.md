---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/tier-overage-meter-visualizer/"
title: "Tier Overage Meter Visualizer"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Show, don't tell, what each tier covers: capacity meters for projects, storage and seats fill to each plan's limit as the cards scroll into view, with the…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tier Overage Meter Visualizer
Source: https://codefronts.com/components/css-pricing-tables/tier-overage-meter-visualizer/

Show, don't tell, what each tier covers: capacity meters for projects, storage and seats fill to each plan's limit as the cards scroll into view, with the near-full bars shifting amber — an instant visual answer to "which plan fits my usage?"
## HTML
```html
<section class="prc-13" aria-label="Pricing with capacity meters">
  <h2 class="prc-13__title">See exactly what fits</h2>
  <div class="prc-13__grid">
    <article class="prc-13__card">
      <h3>Free</h3><p class="prc-13__price">$0</p>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Projects <b>3 of 100</b></span><span class="prc-13__track"><span class="prc-13__fill" style="--fill:.03"></span></span></div>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Storage <b>2 GB</b></span><span class="prc-13__track"><span class="prc-13__fill" style="--fill:.08"></span></span></div>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Seats <b>1</b></span><span class="prc-13__track"><span class="prc-13__fill" style="--fill:.05"></span></span></div>
      <a href="#" class="prc-13__cta">Start free</a>
    </article>
    <article class="prc-13__card prc-13__card--hot">
      <h3>Pro</h3><p class="prc-13__price">$24<small>/mo</small></p>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Projects <b>60 of 100</b></span><span class="prc-13__track"><span class="prc-13__fill" style="--fill:.6"></span></span></div>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Storage <b>250 GB</b></span><span class="prc-13__track"><span class="prc-13__fill" style="--fill:.55"></span></span></div>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Seats <b>10</b></span><span class="prc-13__track"><span class="prc-13__fill" style="--fill:.5"></span></span></div>
      <a href="#" class="prc-13__cta prc-13__cta--hot">Go Pro</a>
    </article>
    <article class="prc-13__card">
      <h3>Max</h3><p class="prc-13__price">$59<small>/mo</small></p>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Projects <b>Unlimited</b></span><span class="prc-13__track"><span class="prc-13__fill prc-13__fill--warn" style="--fill:.97"></span></span></div>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Storage <b>2 TB</b></span><span class="prc-13__track"><span class="prc-13__fill prc-13__fill--warn" style="--fill:.9"></span></span></div>
      <div class="prc-13__meter"><span class="prc-13__mlabel">Seats <b>Unlimited</b></span><span class="prc-13__track"><span class="prc-13__fill prc-13__fill--warn" style="--fill:.97"></span></span></div>
      <a href="#" class="prc-13__cta">Go Max</a>
    </article>
  </div>
</section>
```
## CSS
```css
.prc-13,
.prc-13 *,
.prc-13 *::before,
.prc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-13 {
  --accent: oklch(0.6 0.16 235);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f4f7fa;
  color: #141c24;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-13__title {
  text-align: center;
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 38px;
}

.prc-13__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: 20px;
  width: min(900px,100%);
  margin: 0 auto;
}

.prc-13__card {
  background: #fff;
  border: 1px solid #dfe6ee;
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.prc-13__card--hot {
  border-color: var(--accent);
  box-shadow: 0 16px 40px -26px oklch(0.6 0.16 235/.5);
}

.prc-13__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #65758a;
}

.prc-13__price {
  font-size: 40px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-13__price small {
  font-size: 15px;
  font-weight: 600;
  color: #8494a8;
}

.prc-13__meter {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.prc-13__mlabel {
  display: flex;
  justify-content: space-between;
  font-size: 12.5px;
  font-weight: 600;
  color: #65758a;
}

.prc-13__mlabel b {
  color: #141c24;
  font-variant-numeric: tabular-nums;
}

.prc-13__track {
  display: block;
  height: 8px;
  border-radius: 99px;
  background: #e8edf4;
  overflow: hidden;
}

.prc-13__fill {
  display: block;
  height: 100%;
  border-radius: 99px;
  background: linear-gradient(90deg,oklch(0.7 0.13 235),var(--accent));
  transform: scaleX(var(--fill));
  transform-origin: left;
  animation: prc-13-sweep 1s cubic-bezier(.3,0,.2,1) both;
  animation-timeline: view();
  animation-range: entry 0% entry 60%;
}

.prc-13__fill--warn {
  background: linear-gradient(90deg,oklch(0.75 0.14 85),oklch(0.68 0.17 55));
}

@keyframes prc-13-sweep {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(var(--fill));
  }
}

.prc-13__cta {
  margin-top: 6px;
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1.5px solid #dfe6ee;
  color: #141c24;
  transition: border-color .2s;
}

.prc-13__cta:hover {
  border-color: var(--accent);
}

.prc-13__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-13__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-13__fill {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each fill bar scales from 0 to its --fill fraction with a scroll-driven view() timeline entrance; browsers without scroll timelines paint the bars at final value instantly. */
```
