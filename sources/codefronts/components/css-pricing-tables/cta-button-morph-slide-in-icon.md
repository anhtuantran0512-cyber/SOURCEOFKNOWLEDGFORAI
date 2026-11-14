---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/cta-button-morph-slide-in-icon/"
title: "CTA Button Morph & Slide-In Icon"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Conversion-grade call-to-action choreography: hover any plan's button and it fills with color from the left, widens its padding, and an arrow slides in from…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CTA Button Morph & Slide-In Icon
Source: https://codefronts.com/components/css-pricing-tables/cta-button-morph-slide-in-icon/

Conversion-grade call-to-action choreography: hover any plan's button and it fills with color from the left, widens its padding, and an arrow slides in from the edge — three coordinated micro-transitions that make "Choose plan" feel irresistible to click.
## HTML
```html
<section class="prc-08" aria-label="Pricing with animated call-to-action buttons">
  <div class="prc-08__grid">
    <article class="prc-08__card"><h3>Seed</h3><p class="prc-08__price">$19</p><span class="prc-08__per">per month</span><ul><li>5k contacts</li><li>Email campaigns</li></ul><a href="#" class="prc-08__cta" style="--fill:oklch(0.62 0.15 165)"><span class="prc-08__label">Choose Seed</span><span class="prc-08__arrow" aria-hidden="true">→</span></a></article>
    <article class="prc-08__card prc-08__card--hot"><h3>Bloom</h3><p class="prc-08__price">$49</p><span class="prc-08__per">per month</span><ul><li>50k contacts</li><li>Automations</li><li>A/B testing</li></ul><a href="#" class="prc-08__cta" style="--fill:oklch(0.55 0.18 285)"><span class="prc-08__label">Choose Bloom</span><span class="prc-08__arrow" aria-hidden="true">→</span></a></article>
    <article class="prc-08__card"><h3>Forest</h3><p class="prc-08__price">$129</p><span class="prc-08__per">per month</span><ul><li>Unlimited contacts</li><li>Multivariate testing</li><li>Dedicated IP</li></ul><a href="#" class="prc-08__cta" style="--fill:oklch(0.5 0.14 250)"><span class="prc-08__label">Choose Forest</span><span class="prc-08__arrow" aria-hidden="true">→</span></a></article>
  </div>
</section>
```
## CSS
```css
.prc-08,
.prc-08 *,
.prc-08 *::before,
.prc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-08 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f7f8f7;
  color: #181c19;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
}

.prc-08__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 20px;
  width: min(880px,100%);
}

.prc-08__card {
  background: #fff;
  border: 1px solid #e4e7e4;
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.prc-08__card--hot {
  border-color: oklch(0.55 0.18 285);
  box-shadow: 0 16px 40px -26px oklch(0.55 0.18 285/.5);
}

.prc-08__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #6f766f;
}

.prc-08__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-08__per {
  font-size: 12.5px;
  color: #8b918b;
  margin-bottom: 16px;
}

.prc-08__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 14px;
  color: #4a504a;
  flex: 1;
  margin-bottom: 20px;
}

.prc-08__card li::before {
  content: "✓";
  color: var(--fill,oklch(0.55 0.18 285));
  font-weight: 700;
  margin-right: 8px;
}

.prc-08__cta {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  overflow: hidden;
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  padding: 13px 18px;
  border-radius: 12px;
  border: 1.5px solid #d9ded9;
  color: #181c19;
  transition: color .3s,border-color .3s,padding .3s;
}

.prc-08__cta::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--fill);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .35s cubic-bezier(.6,0,.2,1);
}

.prc-08__cta:hover,
.prc-08__cta:focus-visible {
  color: #fff;
  border-color: var(--fill);
  padding: 13px 22px;
}

.prc-08__cta:hover::before,
.prc-08__cta:focus-visible::before {
  transform: scaleX(1);
}

.prc-08__label {
  position: relative;
  transition: transform .3s;
}

.prc-08__arrow {
  position: relative;
  display: inline-block;
  width: 0;
  opacity: 0;
  transform: translateX(8px);
  transition: transform .3s .05s,opacity .3s .05s,width .3s;
}

.prc-08__cta:hover .prc-08__arrow,
.prc-08__cta:focus-visible .prc-08__arrow {
  width: 20px;
  opacity: 1;
  transform: translateX(6px);
}

.prc-08__cta:focus-visible {
  outline: 3px solid var(--fill);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-08__cta,
    .prc-08__cta::before,
    .prc-08__label,
    .prc-08__arrow {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the color fill is a scaleX(0→1) pseudo-element, the arrow slides in via transform/opacity, and each button's --fill custom property recolors the whole morph from one ruleset. */
```
