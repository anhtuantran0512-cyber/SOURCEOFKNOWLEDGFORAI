---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/scale-up-focused-plan-hover/"
title: "Scale-Up Focused Plan Hover"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "The classic conversion micro-interaction: hover (or keyboard-focus) any tier and it lifts, scales up and deepens its shadow while sibling cards ease back and…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scale-Up Focused Plan Hover
Source: https://codefronts.com/components/css-pricing-tables/scale-up-focused-plan-hover/

The classic conversion micro-interaction: hover (or keyboard-focus) any tier and it lifts, scales up and deepens its shadow while sibling cards ease back and dim — pulling the eye to exactly one plan at a time using :has() sibling logic.
## HTML
```html
<section class="prc-05" aria-label="Pricing cards with focus hover">
  <h2 class="prc-05__title">Pick your pace</h2>
  <div class="prc-05__grid">
    <article class="prc-05__card"><h3>Lite</h3><p class="prc-05__price">$15</p><span class="prc-05__per">/ month</span><ul><li>2 seats</li><li>Weekly reports</li><li>Email support</li></ul><a href="#" class="prc-05__cta">Select Lite</a></article>
    <article class="prc-05__card"><h3>Growth</h3><p class="prc-05__price">$39</p><span class="prc-05__per">/ month</span><ul><li>10 seats</li><li>Daily reports</li><li>Integrations</li><li>Chat support</li></ul><a href="#" class="prc-05__cta">Select Growth</a></article>
    <article class="prc-05__card"><h3>Scale</h3><p class="prc-05__price">$99</p><span class="prc-05__per">/ month</span><ul><li>Unlimited seats</li><li>Real-time analytics</li><li>Dedicated manager</li></ul><a href="#" class="prc-05__cta">Select Scale</a></article>
  </div>
</section>
```
## CSS
```css
.prc-05,
.prc-05 *,
.prc-05 *::before,
.prc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-05 {
  --accent: oklch(0.6 0.2 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f2f0f7;
  color: #1d1a26;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-05__title {
  text-align: center;
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 38px;
}

.prc-05__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 22px;
  width: min(880px,100%);
  margin: 0 auto;
}

.prc-05__card {
  position: relative;
  background: #fff;
  border: 1px solid #e2dfeb;
  border-radius: 20px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: transform .35s cubic-bezier(.3,1.2,.3,1),filter .35s;
  will-change: transform;
}

.prc-05__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 20px;
  box-shadow: 0 30px 60px -22px oklch(0.6 0.2 300/.45);
  opacity: 0;
  transition: opacity .35s;
  pointer-events: none;
}

.prc-05__card:hover,
.prc-05__card:focus-within {
  transform: translateY(-10px) scale(1.05);
  z-index: 1;
}

.prc-05__card:hover::after,
.prc-05__card:focus-within::after {
  opacity: 1;
}

.prc-05__grid:has(.prc-05__card:hover) .prc-05__card:not(:hover),
.prc-05__grid:has(.prc-05__card:focus-within) .prc-05__card:not(:focus-within) {
  transform: scale(.96);
  filter: saturate(.6) opacity(.75);
}

.prc-05__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #726c85;
}

.prc-05__price {
  font-size: 44px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-05__per {
  font-size: 12.5px;
  color: #8d87a0;
  margin-bottom: 16px;
}

.prc-05__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 14px;
  color: #4d4761;
  flex: 1;
  margin-bottom: 20px;
}

.prc-05__card li::before {
  content: "✓";
  color: var(--accent);
  font-weight: 700;
  margin-right: 9px;
}

.prc-05__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  background: #1d1a26;
  color: #fff;
  transition: background .25s;
}

.prc-05__card:hover .prc-05__cta,
.prc-05__cta:focus-visible {
  background: var(--accent);
}

.prc-05__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-05__card,
    .prc-05__card::after {
    transition-duration: .01s;
  }

  .prc-05__card:hover,
    .prc-05__card:focus-within {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hover/focus-within scales the active card while a grid-level :has() rule eases the siblings back; the deep shadow is a pre-rendered pseudo-element fading in, so nothing repaints per frame. */
```
