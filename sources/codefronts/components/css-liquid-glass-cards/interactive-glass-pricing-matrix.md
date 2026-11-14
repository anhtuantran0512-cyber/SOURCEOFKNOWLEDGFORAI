---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/interactive-glass-pricing-matrix/"
title: "Interactive Glass Pricing Matrix"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A three-tier pricing table in Liquid Glass with a Monthly/Yearly billing toggle."
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Glass Pricing Matrix
Source: https://codefronts.com/components/css-liquid-glass-cards/interactive-glass-pricing-matrix/

A three-tier pricing table in Liquid Glass with a Monthly/Yearly billing toggle. Prices swap with a spring count, and the 'Popular' plan wears a stronger specular rim-light and a slow colour-refraction sweep so it visibly out-shines its neighbours — the conversion pattern SaaS teams ask for.
## HTML
```html
<section class="lg-04" aria-label="Interactive liquid glass pricing matrix demo">
  <div class="lg-04__head">
    <button class="lg-04__switch" id="lg-04-switch" role="switch" aria-checked="false" type="button"><span class="lg-04__track"><span class="lg-04__thumb"></span></span><span class="lg-04__slabels">Monthly · <b>Yearly −20%</b></span></button>
  </div>
  <div class="lg-04__grid" id="lg-04-grid" data-cycle="month">
    <section class="lg-04__plan"><h3>Starter</h3><p class="lg-04__price"><span class="m">$12</span><span class="y">$115</span><small>/<span class="lg-04__per">mo</span></small></p><ul class="lg-04__feat"><li>3 projects</li><li>Community support</li></ul><a class="lg-04__cta" href="#lg-04">Choose Starter</a></section>
    <section class="lg-04__plan lg-04__plan--pop"><span class="lg-04__badge">Popular</span><h3>Pro</h3><p class="lg-04__price"><span class="m">$29</span><span class="y">$278</span><small>/<span class="lg-04__per">mo</span></small></p><ul class="lg-04__feat"><li>Unlimited projects</li><li>Priority support</li><li>Advanced analytics</li></ul><a class="lg-04__cta lg-04__cta--pop" href="#lg-04">Choose Pro</a></section>
    <section class="lg-04__plan"><h3>Scale</h3><p class="lg-04__price"><span class="m">$79</span><span class="y">$758</span><small>/<span class="lg-04__per">mo</span></small></p><ul class="lg-04__feat"><li>SSO + audit log</li><li>Dedicated CSM</li></ul><a class="lg-04__cta" href="#lg-04">Choose Scale</a></section>
  </div>
  <p class="lg-04__live" aria-live="polite">Billing: monthly</p>
</section>
```
## CSS
```css
.lg-04,
.lg-04 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --spin {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.lg-04 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.68 0.19 285);
  padding: 26px 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 100% at 50% -10%,#4338ca,#1e1b4b 70%);
}

.lg-04__head {
  display: flex;
  justify-content: center;
  margin-bottom: 22px;
}

.lg-04__switch {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: none;
  border: 0;
  cursor: pointer;
  color: #fff;
  font: 600 14px 'Segoe UI',system-ui,sans-serif;
}

.lg-04__track {
  width: 46px;
  height: 26px;
  border-radius: 999px;
  background: rgba(255,255,255,.2);
  border: 1px solid rgba(255,255,255,.4);
  position: relative;
  transition: background .3s;
}

.lg-04__thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #fff;
  transition: transform .35s cubic-bezier(.34,1.4,.5,1);
}

.lg-04__switch[aria-checked=true] .lg-04__thumb {
  transform: translateX(20px);
}

.lg-04__switch[aria-checked=true] .lg-04__track {
  background: color-mix(in oklab,var(--accent) 70%,transparent);
}

.lg-04__switch:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
  border-radius: 8px;
}

.lg-04__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 14px;
  max-width: 720px;
  margin: 0 auto;
}

.lg-04__plan {
  position: relative;
  padding: 22px 20px;
  border-radius: 20px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 24px 50px -30px rgba(0,0,0,.7);
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
}

.lg-04__plan--pop {
  border: 0;
}

.lg-04__plan--pop::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 20px;
  padding: 1.5px;
  background: conic-gradient(from var(--spin),var(--accent),#fff,var(--accent));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: lg-04-spin 6s linear infinite;
  pointer-events: none;
}

@keyframes lg-04-spin {
  to {
    --spin: 360deg;
  }
}

.lg-04__badge {
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--accent);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: 999px;
  letter-spacing: .04em;
}

.lg-04__plan h3 {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 8px;
}

.lg-04__price {
  display: flex;
  align-items: baseline;
  gap: 2px;
  font-weight: 800;
  margin-bottom: 14px;
}

.lg-04__price .m,
.lg-04__price .y {
  font-size: 34px;
  letter-spacing: -.02em;
}

.lg-04__price .y {
  display: none;
}

.lg-04__price small {
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,.7);
}

.lg-04__grid[data-cycle=year] .m {
  display: none;
}

.lg-04__grid[data-cycle=year] .y {
  display: inline;
}

.lg-04__feat {
  list-style: none;
  display: grid;
  gap: 7px;
  margin-bottom: 18px;
  font-size: 13.5px;
  color: rgba(255,255,255,.85);
}

.lg-04__feat li::before {
  content: "✓ ";
  color: #a5f3d0;
}

.lg-04__cta {
  display: block;
  text-align: center;
  min-height: 44px;
  line-height: 44px;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 700;
  color: #fff;
  background: rgba(255,255,255,.16);
  border: 1px solid rgba(255,255,255,.34);
}

.lg-04__cta--pop {
  background: var(--accent);
  border-color: transparent;
}

.lg-04__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

.lg-04__live {
  text-align: center;
  color: rgba(255,255,255,.7);
  font-size: 12px;
  margin-top: 14px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-04__plan--pop::before {
    animation: none;
  }
}

@media (max-width: 640px) {
  .lg-04__grid {
    grid-template-columns: 1fr;
  }
}
```

## JavaScript
```js
(() => {
  const sw = document.querySelector('#lg-04-switch');
  const grid = document.querySelector('#lg-04-grid');
  const live = document.querySelector('.lg-04__live');
  if (!sw || !grid) return;
  sw.addEventListener('click', () => {
    const yearly = sw.getAttribute('aria-checked') !== 'true';
    sw.setAttribute('aria-checked', String(yearly));
    grid.dataset.cycle = yearly ? 'year' : 'month';
    grid.querySelectorAll('.lg-04__per').forEach(el => el.textContent = yearly ? 'yr' : 'mo');
    live.textContent = 'Billing: ' + (yearly ? 'yearly (20% off)' : 'monthly');
  });
})();
```
