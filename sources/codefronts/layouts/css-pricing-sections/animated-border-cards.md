---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/animated-border-cards/"
title: "Animated Border Cards"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Three pricing cards with a conic-gradient border that rotates continuously using @property animatable angle."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Border Cards
Source: https://codefronts.com/layouts/css-pricing-sections/animated-border-cards/

Three pricing cards with a conic-gradient border that rotates continuously using @property animatable angle. Slate base, violet/cyan highlight on the recommended tier — the modern AI-product launch treatment.
## HTML
```html
<section class="ps-12" aria-label="Pricing">
  <header class="ps-12__head">
    <span class="ps-12__eye">Plans</span>
    <h2>Built for builders. Priced for shipping.</h2>
  </header>
  <div class="ps-12__grid">
    <article class="ps-12__card">
      <span class="ps-12__edge" aria-hidden="true"></span>
      <div class="ps-12__body">
        <h3>Starter</h3>
        <div class="ps-12__price"><em>$</em>14<span>/mo</span></div>
        <ul>
          <li>3 projects</li>
          <li>10 GB storage</li>
          <li>Community support</li>
        </ul>
        <a class="ps-12__cta" href="#starter">Choose Starter</a>
      </div>
    </article>
    <article class="ps-12__card ps-12__pri">
      <span class="ps-12__edge" aria-hidden="true"></span>
      <div class="ps-12__body">
        <span class="ps-12__pill">Recommended</span>
        <h3>Builder</h3>
        <div class="ps-12__price"><em>$</em>32<span>/mo</span></div>
        <ul>
          <li>Unlimited projects</li>
          <li>100 GB storage</li>
          <li>Priority support</li>
          <li>API + webhooks</li>
        </ul>
        <a class="ps-12__cta ps-12__cta-pri" href="#builder">Choose Builder</a>
      </div>
    </article>
    <article class="ps-12__card">
      <span class="ps-12__edge" aria-hidden="true"></span>
      <div class="ps-12__body">
        <h3>Scale</h3>
        <div class="ps-12__price"><em>$</em>89<span>/mo</span></div>
        <ul>
          <li>Everything in Builder</li>
          <li>SSO + audit logs</li>
          <li>SLA + CSM</li>
        </ul>
        <a class="ps-12__cta" href="#scale">Talk to sales</a>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@property --ps-12-ang {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.ps-12 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #0a0d1a;
  color: #e6e7f0;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-12__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 40px);
}

.ps-12__eye {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #a5b4fc;
  padding: 5px 12px;
  background: rgba(165,180,252,0.1);
  border: 1px solid rgba(165,180,252,0.25);
  border-radius: 999px;
  margin-bottom: 14px;
}

.ps-12__head h2 {
  font-size: clamp(22px, 3.4vw, 34px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0;
  color: #fff;
}

.ps-12__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  max-width: 980px;
  margin: 0 auto;
}

.ps-12__card {
  position: relative;
  border-radius: 16px;
  padding: 1.5px;
  background: rgba(255,255,255,0.04);
}

.ps-12__edge {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  padding: 1.5px;
  background: conic-gradient(from var(--ps-12-ang), #1e293b, #475569, #1e293b);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: ps-12-spin 6s linear infinite;
}

.ps-12__pri .ps-12__edge {
  background: conic-gradient(from var(--ps-12-ang), #6366f1, #22d3ee, #a855f7, #6366f1);
}

@keyframes ps-12-spin {
  to {
    --ps-12-ang: 360deg;
  }
}

.ps-12__body {
  position: relative;
  background: #0f1224;
  border-radius: 14.5px;
  padding: 22px 20px 20px;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.ps-12__pill {
  display: inline-block;
  align-self: flex-start;
  background: linear-gradient(135deg, #6366f1, #22d3ee);
  color: #0a0d1a;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 999px;
  margin-bottom: 10px;
}

.ps-12__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 0 0 12px;
  color: #c7d2fe;
}

.ps-12__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 18px;
  color: #fff;
}

.ps-12__price em {
  font-size: 0.5em;
  font-style: normal;
  padding-right: 2px;
  opacity: 0.7;
}

.ps-12__price span {
  font-size: 0.34em;
  font-weight: 500;
  opacity: 0.65;
  margin-left: 6px;
}

.ps-12__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 22px;
  flex: 1;
  font-size: 13.5px;
  line-height: 1.95;
  color: #b8bfd8;
}

.ps-12__card ul li::before {
  content: '✓';
  color: #a5b4fc;
  display: inline-block;
  width: 20px;
  font-weight: 700;
}

.ps-12__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 9px;
  background: rgba(165,180,252,0.08);
  color: #c7d2fe;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid rgba(165,180,252,0.25);
  transition: background 0.18s, color 0.18s;
}

.ps-12__cta-pri {
  background: linear-gradient(135deg, #6366f1, #22d3ee);
  color: #0a0d1a;
  border-color: transparent;
}

.ps-12__cta:hover {
  background: rgba(165,180,252,0.18);
  color: #fff;
}

.ps-12__cta-pri:hover {
  filter: brightness(1.1);
}

.ps-12__cta:focus-visible {
  outline: 2px solid #a5b4fc;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-12__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-12__edge {
    animation: none;
    background: linear-gradient(135deg, #475569, #1e293b);
  }

  .ps-12__pri .ps-12__edge {
    background: linear-gradient(135deg, #6366f1, #22d3ee);
  }
}
```
