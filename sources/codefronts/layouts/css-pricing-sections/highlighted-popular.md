---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/highlighted-popular/"
title: "Highlighted Popular"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Three tiers with the middle \"Pro\" plan lifted, scaled, and ribboned with a \"Most Popular\" badge."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Highlighted Popular
Source: https://codefronts.com/layouts/css-pricing-sections/highlighted-popular/

Three tiers with the middle "Pro" plan lifted, scaled, and ribboned with a "Most Popular" badge. Sunset peach gradient on the highlight, neutral cream on the surrounding tiers — the lift pattern that drives 60–70% of mid-tier conversions.
## HTML
```html
<section class="ps-02" aria-label="Pricing">
  <header class="ps-02__head">
    <h2>Simple pricing, no surprises.</h2>
    <p>Three plans. Same product. Pick what you can grow into.</p>
  </header>
  <div class="ps-02__grid">
    <article class="ps-02__card">
      <h3>Basic</h3>
      <div class="ps-02__price">
        <span class="ps-02__cur">$</span><span class="ps-02__amt">12</span
        ><span class="ps-02__per">/mo</span>
      </div>
      <p class="ps-02__sub">Just the essentials.</p>
      <ul class="ps-02__feats">
        <li>3 projects</li>
        <li>5 GB storage</li>
        <li>Email-only support</li>
      </ul>
      <a class="ps-02__cta" href="#basic">Choose Basic</a>
    </article>
    <article class="ps-02__card ps-02__popular">
      <span class="ps-02__badge" aria-label="Most popular plan">Most popular</span>
      <h3>Pro</h3>
      <div class="ps-02__price">
        <span class="ps-02__cur">$</span><span class="ps-02__amt">36</span
        ><span class="ps-02__per">/mo</span>
      </div>
      <p class="ps-02__sub">Everything teams actually need.</p>
      <ul class="ps-02__feats">
        <li>Unlimited projects</li>
        <li>100 GB storage</li>
        <li>Priority support</li>
        <li>Custom domains</li>
        <li>Team roles</li>
      </ul>
      <a class="ps-02__cta ps-02__cta-pri" href="#pro">Choose Pro</a>
    </article>
    <article class="ps-02__card">
      <h3>Enterprise</h3>
      <div class="ps-02__price">
        <span class="ps-02__cur">$</span><span class="ps-02__amt">99</span
        ><span class="ps-02__per">/mo</span>
      </div>
      <p class="ps-02__sub">Compliance + dedicated success.</p>
      <ul class="ps-02__feats">
        <li>Everything in Pro</li>
        <li>SSO &amp; SAML</li>
        <li>SLA + dedicated CSM</li>
      </ul>
      <a class="ps-02__cta" href="#enterprise">Contact sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-02 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #1a1410;
  color: #fef2e6;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-02__head {
  text-align: center;
  margin-bottom: clamp(28px, 5vw, 48px);
}

.ps-02__head h2 {
  font-size: clamp(24px, 3.6vw, 36px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 10px;
  background: linear-gradient(90deg, #ff8b5a, #ffb37a);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ps-02__head p {
  color: #c9b3a3;
  margin: 0;
  font-size: 14px;
}

.ps-02__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  align-items: center;
  max-width: 980px;
  margin: 0 auto;
}

.ps-02__card {
  position: relative;
  background: #261c16;
  border: 1px solid rgba(255,179,122,0.12);
  border-radius: 16px;
  padding: 26px 22px 22px;
  display: flex;
  flex-direction: column;
}

.ps-02__popular {
  background: linear-gradient(180deg, #ff8b5a 0%, #f56a3a 100%);
  color: #1a1410;
  transform: scale(1.05);
  box-shadow: 0 14px 40px rgba(245,106,58,0.35);
  border: 0;
  z-index: 2;
}

.ps-02__badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: #1a1410;
  color: #ff8b5a;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 5px 12px;
  border-radius: 999px;
}

.ps-02__card h3 {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin: 0 0 14px;
  color: #ffb37a;
}

.ps-02__popular h3 {
  color: #1a1410;
}

.ps-02__price {
  display: flex;
  align-items: baseline;
  gap: 3px;
  margin-bottom: 6px;
}

.ps-02__cur {
  font-size: 18px;
  font-weight: 600;
  opacity: 0.7;
}

.ps-02__amt {
  font-size: 44px;
  font-weight: 800;
  letter-spacing: -0.03em;
}

.ps-02__per {
  font-size: 13px;
  opacity: 0.7;
  margin-left: 4px;
}

.ps-02__sub {
  font-size: 13px;
  opacity: 0.75;
  margin: 0 0 18px;
}

.ps-02__feats {
  list-style: none;
  padding: 0;
  margin: 0 0 22px;
  flex: 1;
  font-size: 13.5px;
  line-height: 1.9;
}

.ps-02__feats li::before {
  content: '✓';
  display: inline-block;
  width: 18px;
  font-weight: 800;
  opacity: 0.85;
}

.ps-02__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 8px;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid currentColor;
  color: #ffb37a;
  background: transparent;
  transition: background 0.18s, color 0.18s;
}

.ps-02__cta:hover {
  background: #ffb37a;
  color: #1a1410;
}

.ps-02__cta-pri {
  background: #1a1410;
  color: #ff8b5a;
  border-color: #1a1410;
}

.ps-02__cta-pri:hover {
  background: #fef2e6;
  color: #1a1410;
  border-color: #fef2e6;
}

.ps-02__cta:focus-visible {
  outline: 2px solid #ff8b5a;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-02__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
  }

  .ps-02__popular {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-02__cta {
    transition: none;
  }
}
```
