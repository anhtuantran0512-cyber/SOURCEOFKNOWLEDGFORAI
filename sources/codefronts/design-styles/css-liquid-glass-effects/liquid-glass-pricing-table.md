---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-pricing-table/"
title: "Liquid Glass Pricing Table"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A three-tier pricing grid where the 'Pro' plan is a live Liquid Glass card: a gradient border slowly rotates around it, a glowing 'Most popular' badge sits…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Pricing Table
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-pricing-table/

A three-tier pricing grid where the 'Pro' plan is a live Liquid Glass card: a gradient border slowly rotates around it, a glowing 'Most popular' badge sits on the rim, and it lifts above the flatter free tiers. High-end SaaS pricing energy, pure CSS.
## HTML
```html
<section class="lg-10" aria-label="Liquid glass pricing table">
  <div class="lg-10__grid">
    <article class="lg-10__card"><h3 class="lg-10__name">Starter</h3><p class="lg-10__price"><span>$0</span>/mo</p><ul class="lg-10__feats"><li>3 projects</li><li>Community support</li><li>1 GB storage</li></ul><button class="lg-10__cta" type="button">Choose Starter</button></article>
    <article class="lg-10__card lg-10__card--pro"><span class="lg-10__badge">Most popular</span><h3 class="lg-10__name">Pro</h3><p class="lg-10__price"><span>$24</span>/mo</p><ul class="lg-10__feats"><li>Unlimited projects</li><li>Priority support</li><li>100 GB storage</li><li>Advanced analytics</li></ul><button class="lg-10__cta lg-10__cta--pro" type="button">Choose Pro</button></article>
    <article class="lg-10__card"><h3 class="lg-10__name">Team</h3><p class="lg-10__price"><span>$69</span>/mo</p><ul class="lg-10__feats"><li>Everything in Pro</li><li>SSO & roles</li><li>1 TB storage</li></ul><button class="lg-10__cta" type="button">Choose Team</button></article>
  </div>
</section>
```
## CSS
```css
.lg-10,
.lg-10 *,
.lg-10 *::before,
.lg-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --lg-10-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.lg-10 {
  --pro: oklch(0.66 0.2 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(circle at 20% 20%,#3a1f5a,#160f2c 60%),radial-gradient(circle at 80% 80%,#1f3a5a,#160f2c 60%);
}

.lg-10__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(240px,100%),1fr));
  gap: 22px;
  width: min(920px,100%);
  align-items: center;
}

.lg-10__card {
  position: relative;
  padding: 30px 26px;
  border-radius: 22px;
  color: #fff;
  background: color-mix(in oklab,white 8%,transparent);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3),0 20px 44px -26px rgba(0,0,0,.6);
  backdrop-filter: blur(18px) saturate(160%);
  -webkit-backdrop-filter: blur(18px) saturate(160%);
}

.lg-10__card--pro {
  background: color-mix(in oklab,white 15%,transparent);
  transform: translateY(-14px);
  z-index: 2;
}

.lg-10__card--pro::before {
  content: "";
  position: absolute;
  inset: -1.5px;
  border-radius: inherit;
  padding: 1.5px;
  background: conic-gradient(from var(--lg-10-angle),var(--pro),oklch(0.72 0.17 200),oklch(0.75 0.18 340),var(--pro));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  animation: lg-10-spin 5s linear infinite;
  pointer-events: none;
}

.lg-10__badge {
  position: absolute;
  top: -13px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 999px;
  color: #fff;
  background: var(--pro);
  box-shadow: 0 0 0 1px rgba(255,255,255,.3),0 0 24px 2px color-mix(in oklab,var(--pro) 70%,transparent);
  animation: lg-10-glow 2.4s ease-in-out infinite;
}

.lg-10__name {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: rgba(255,255,255,.8);
  margin-bottom: 10px;
}

.lg-10__price {
  font-size: 15px;
  color: rgba(255,255,255,.7);
  margin-bottom: 20px;
}

.lg-10__price span {
  font-size: 40px;
  font-weight: 900;
  color: #fff;
  letter-spacing: -.02em;
}

.lg-10__feats {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 11px;
  margin-bottom: 24px;
}

.lg-10__feats li {
  font-size: 14px;
  color: rgba(255,255,255,.9);
  padding-left: 24px;
  position: relative;
}

.lg-10__feats li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: oklch(0.78 0.16 160);
  font-weight: 800;
}

.lg-10__cta {
  width: 100%;
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  padding: 13px;
  border-radius: 12px;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.3);
  background: rgba(255,255,255,.12);
  transition: background .2s,transform .15s;
}

.lg-10__cta--pro {
  background: linear-gradient(180deg,color-mix(in oklab,var(--pro) 85%,white),var(--pro));
  border-color: color-mix(in oklab,var(--pro) 40%,white);
}

.lg-10__cta:hover {
  transform: translateY(-2px);
  background: rgba(255,255,255,.2);
}

.lg-10__cta--pro:hover {
  background: linear-gradient(180deg,color-mix(in oklab,var(--pro) 75%,white),var(--pro));
}

.lg-10__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@keyframes lg-10-spin {
  to {
    --lg-10-angle: 360deg;
  }
}

@keyframes lg-10-glow {
  0%,
    100% {
    box-shadow: 0 0 0 1px rgba(255,255,255,.3),0 0 16px 1px color-mix(in oklab,var(--pro) 60%,transparent);
  }

  50% {
    box-shadow: 0 0 0 1px rgba(255,255,255,.4),0 0 30px 4px color-mix(in oklab,var(--pro) 80%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-10__card--pro::before,
    .lg-10__badge {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the free tiers are static frosted cards; the Pro card's rotating border is an @property-driven conic-gradient masked to a rim, and the badge glow is a CSS box-shadow pulse. */
```
