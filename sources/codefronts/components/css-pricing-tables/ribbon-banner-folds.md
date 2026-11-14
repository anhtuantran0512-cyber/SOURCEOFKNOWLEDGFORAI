---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/ribbon-banner-folds/"
title: "Ribbon & Banner Folds"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Classic e-commerce trust styling: a corner ribbon with true 3D fold-backs, and a drop-down bookmark banner that unfurls on page load — both drawn entirely…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ribbon & Banner Folds
Source: https://codefronts.com/components/css-pricing-tables/ribbon-banner-folds/

Classic e-commerce trust styling: a corner ribbon with true 3D fold-backs, and a drop-down bookmark banner that unfurls on page load — both drawn entirely with borders and clip-path, no images, and both slide into place with a springy entrance.
## HTML
```html
<section class="prc-17" aria-label="Pricing cards with ribbon and banner accents">
  <div class="prc-17__grid">
    <article class="prc-17__card">
      <span class="prc-17__bookmark" aria-hidden="true">Deal</span>
      <h3>Basic</h3><p class="prc-17__price">$14<small>/mo</small></p>
      <p class="prc-17__note">Launch-week deal pricing, locked for life.</p>
      <a href="#" class="prc-17__cta">Get Basic</a>
    </article>
    <article class="prc-17__card prc-17__card--hot">
      <span class="prc-17__corner" aria-hidden="true"><span class="prc-17__ribbon">−30%</span></span>
      <h3>Plus</h3><p class="prc-17__price">$34<small>/mo</small></p>
      <p class="prc-17__note">30% off annual — offer shown in the ribbon.</p>
      <a href="#" class="prc-17__cta prc-17__cta--hot">Get Plus</a>
    </article>
    <article class="prc-17__card">
      <h3>Max</h3><p class="prc-17__price">$74<small>/mo</small></p>
      <p class="prc-17__note">Full suite, priority everything.</p>
      <a href="#" class="prc-17__cta">Get Max</a>
    </article>
  </div>
</section>
```
## CSS
```css
.prc-17,
.prc-17 *,
.prc-17 *::before,
.prc-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-17 {
  --rib: oklch(0.58 0.21 15);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f6f4f1;
  color: #1e1a17;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 64px 24px;
}

.prc-17__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 22px;
  width: min(880px,100%);
}

.prc-17__card {
  position: relative;
  background: #fff;
  border: 1px solid #e7e2db;
  border-radius: 16px;
  padding: 30px 26px 26px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  overflow: visible;
}

.prc-17__card--hot {
  border-color: var(--rib);
  box-shadow: 0 18px 40px -26px oklch(0.58 0.21 15/.5);
}

.prc-17__corner {
  position: absolute;
  top: -6px;
  right: -6px;
  width: 110px;
  height: 110px;
  overflow: hidden;
  pointer-events: none;
}

.prc-17__corner::before,
.prc-17__corner::after {
  content: "";
  position: absolute;
  background: color-mix(in oklch,var(--rib),black 35%);
  width: 6px;
  height: 6px;
}

.prc-17__corner::before {
  top: 0;
  left: 14px;
  clip-path: polygon(0 100%,100% 100%,100% 0);
}

.prc-17__corner::after {
  right: 0;
  bottom: 14px;
  clip-path: polygon(0 0,0 100%,100% 0);
}

.prc-17__ribbon {
  position: absolute;
  top: 26px;
  right: -34px;
  width: 150px;
  transform: rotate(45deg);
  background: var(--rib);
  color: #fff;
  text-align: center;
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .1em;
  padding: 7px 0;
  box-shadow: 0 4px 10px rgba(0,0,0,.18);
  animation: prc-17-slide .7s cubic-bezier(.3,1.4,.4,1) .3s both;
}

@keyframes prc-17-slide {
  from {
    transform: rotate(45deg) translateX(160px);
  }

  to {
    transform: rotate(45deg) translateX(0);
  }
}

.prc-17__bookmark {
  position: absolute;
  top: -4px;
  left: 24px;
  background: #1e1a17;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: 12px 10px 16px;
  clip-path: polygon(0 0,100% 0,100% 100%,50% calc(100% - 8px),0 100%);
  animation: prc-17-drop .6s cubic-bezier(.3,1.5,.4,1) .5s both;
}

@keyframes prc-17-drop {
  from {
    transform: translateY(-110%);
  }

  to {
    transform: translateY(0);
  }
}

.prc-17__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #857b70;
}

.prc-17__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-17__price small {
  font-size: 15px;
  font-weight: 600;
  color: #9a9088;
}

.prc-17__note {
  font-size: 13.5px;
  color: #6e645a;
  line-height: 1.5;
  flex: 1;
  margin: 8px 0 18px;
}

.prc-17__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1.5px solid #e7e2db;
  color: #1e1a17;
  transition: border-color .2s;
}

.prc-17__cta:hover {
  border-color: var(--rib);
}

.prc-17__cta--hot {
  background: var(--rib);
  border-color: var(--rib);
  color: #fff;
}

.prc-17__cta:focus-visible {
  outline: 3px solid var(--rib);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-17__ribbon,
    .prc-17__bookmark {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the corner ribbon is a rotated strip clipped by an overflow:hidden square with border-triangle fold-backs; the bookmark is a clip-path notch. Both unfurl once on load with overshoot easing. */
```
