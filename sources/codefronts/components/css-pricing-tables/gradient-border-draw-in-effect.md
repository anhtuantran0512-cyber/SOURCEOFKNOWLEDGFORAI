---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/gradient-border-draw-in-effect/"
title: "Gradient Border Draw-In Effect"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Hover a clean minimal card and a colorful gradient border draws itself around the perimeter from 0 to 100% — a registered @property percentage sweeping a…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Border Draw-In Effect
Source: https://codefronts.com/components/css-pricing-tables/gradient-border-draw-in-effect/

Hover a clean minimal card and a colorful gradient border draws itself around the perimeter from 0 to 100% — a registered @property percentage sweeping a masked conic-gradient — then un-draws in reverse when you leave.
## HTML
```html
<section class="prc-16" aria-label="Pricing cards with gradient border draw effect">
  <div class="prc-16__grid">
    <article class="prc-16__card"><h3>Sketch</h3><p class="prc-16__price">$11<small>/mo</small></p><ul><li>3 boards</li><li>PNG export</li></ul><a href="#" class="prc-16__cta">Start Sketch</a></article>
    <article class="prc-16__card"><h3>Draft</h3><p class="prc-16__price">$27<small>/mo</small></p><ul><li>Unlimited boards</li><li>SVG + PDF export</li><li>Comments</li></ul><a href="#" class="prc-16__cta">Start Draft</a></article>
    <article class="prc-16__card"><h3>Studio</h3><p class="prc-16__price">$68<small>/mo</small></p><ul><li>Everything in Draft</li><li>Team libraries</li><li>SSO</li></ul><a href="#" class="prc-16__cta">Start Studio</a></article>
  </div>
</section>
```
## CSS
```css
@property --prc16-p {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}

.prc-16,
.prc-16 *,
.prc-16 *::before,
.prc-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-16 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fafafa;
  color: #191919;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
}

.prc-16__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 22px;
  width: min(880px,100%);
}

.prc-16__card {
  position: relative;
  background: #fff;
  border: 1px solid #ebebeb;
  border-radius: 18px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  transition: box-shadow .35s;
}

.prc-16__card::before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: 19px;
  padding: 2px;
  background: conic-gradient(from -90deg,oklch(0.65 0.25 350),oklch(0.6 0.22 280) calc(var(--prc16-p)*.5),oklch(0.7 0.18 200) var(--prc16-p),transparent 0);
  mask: linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask: linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  transition: --prc16-p .8s cubic-bezier(.5,0,.2,1);
  pointer-events: none;
}

.prc-16__card:hover,
.prc-16__card:focus-within {
  box-shadow: 0 20px 44px -28px rgba(120,60,200,.35);
}

.prc-16__card:hover::before,
.prc-16__card:focus-within::before {
  --prc16-p: 100%;
}

.prc-16__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #8a8a8a;
}

.prc-16__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-16__price small {
  font-size: 15px;
  font-weight: 600;
  color: #9a9a9a;
}

.prc-16__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 14px;
  color: #4c4c4c;
  flex: 1;
  margin: 12px 0 20px;
}

.prc-16__card li::before {
  content: "→";
  color: oklch(0.6 0.22 280);
  margin-right: 9px;
}

.prc-16__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  background: #191919;
  color: #fff;
  transition: background .25s;
}

.prc-16__cta:hover {
  background: oklch(0.45 0.2 280);
}

.prc-16__cta:focus-visible {
  outline: 3px solid oklch(0.6 0.22 280);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-16__card::before {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a registered @property <percentage> transitions 0%→100% on hover; the conic-gradient goes transparent past that percentage, so the masked 2px ring appears to draw itself around the card. */
```
