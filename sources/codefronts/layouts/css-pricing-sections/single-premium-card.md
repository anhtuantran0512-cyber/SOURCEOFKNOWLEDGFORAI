---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/single-premium-card/"
title: "Single Premium Card"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A single-tier pricing layout for one-product brands — premium gold / brass treatment over deep navy, oversized price block, six feature checkmarks in two…"
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Single Premium Card
Source: https://codefronts.com/layouts/css-pricing-sections/single-premium-card/

A single-tier pricing layout for one-product brands — premium gold / brass treatment over deep navy, oversized price block, six feature checkmarks in two columns, anchor testimonial below. The pattern Basecamp / Hover use when there is only one thing to sell.
## HTML
```html
<section class="ps-06" aria-label="Pricing">
  <article class="ps-06__card">
    <span class="ps-06__eye">One plan · everything included</span>
    <h2>The whole product, <em>flat fee.</em></h2>
    <p class="ps-06__lead">
      Stop comparing tiers. One price. Every feature. Every team member. As long as you need it.
    </p>
    <div class="ps-06__price">
      <span class="ps-06__amt"><em>$</em>249</span>
      <span class="ps-06__per">per month, billed annually</span>
    </div>
    <ul class="ps-06__feats">
      <li>Unlimited team members</li>
      <li>Unlimited projects &amp; storage</li>
      <li>SSO &amp; SAML included</li>
      <li>SOC 2 &amp; HIPAA ready</li>
      <li>Priority email + chat support</li>
      <li>30-day money-back guarantee</li>
    </ul>
    <a class="ps-06__cta" href="#buy">Buy now — instant access</a>
    <p class="ps-06__foot">No demo required. Cancel any time, refund any time within 30 days.</p>
    <blockquote class="ps-06__quote">
      <p>“It paid for itself in the first week. We never looked at the tier ladder again.”</p>
      <cite>— Maya R., Head of Ops at Northwood</cite>
    </blockquote>
  </article>
</section>
```
## CSS
```css
.ps-06 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(60% 60% at 30% 0%, rgba(212,175,55,0.12), transparent 60%), radial-gradient(50% 50% at 90% 100%, rgba(212,175,55,0.10), transparent 60%), #0b0b1a;
  color: #f4ecd8;
  font-family: 'Inter', system-ui, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ps-06__card {
  position: relative;
  width: 100%;
  max-width: 540px;
  background: linear-gradient(180deg, #14142a 0%, #0b0b1a 100%);
  border: 1px solid #d4af37;
  border-radius: 22px;
  padding: clamp(28px, 5vw, 44px);
  text-align: center;
  box-shadow: 0 20px 60px rgba(212,175,55,0.15), inset 0 0 0 1px rgba(212,175,55,0.15);
}

.ps-06__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 22px;
  background: linear-gradient(135deg, transparent 40%, rgba(255,212,121,0.06) 50%, transparent 60%);
  pointer-events: none;
}

.ps-06__eye {
  display: inline-block;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #d4af37;
  padding: 5px 14px;
  border: 1px solid rgba(212,175,55,0.4);
  border-radius: 999px;
  margin-bottom: 18px;
}

.ps-06__card h2 {
  font-family: 'Playfair Display', 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(28px, 4.5vw, 44px);
  font-weight: 700;
  letter-spacing: -0.01em;
  margin: 0 0 14px;
  color: #fff;
}

.ps-06__card h2 em {
  color: #d4af37;
  font-style: italic;
}

.ps-06__lead {
  color: #b8a888;
  font-size: 14.5px;
  line-height: 1.6;
  margin: 0 auto 28px;
  max-width: 380px;
}

.ps-06__price {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  margin-bottom: 28px;
  padding: 22px 0;
  border-top: 1px solid rgba(212,175,55,0.18);
  border-bottom: 1px solid rgba(212,175,55,0.18);
}

.ps-06__amt {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(56px, 9vw, 88px);
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 1;
  background: linear-gradient(180deg, #ffd479, #d4af37);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ps-06__amt em {
  font-size: 0.5em;
  font-style: normal;
  vertical-align: top;
  padding-right: 2px;
  opacity: 0.85;
}

.ps-06__per {
  font-size: 13px;
  color: #b8a888;
}

.ps-06__feats {
  list-style: none;
  padding: 0;
  margin: 0 0 28px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px 22px;
  text-align: left;
  font-size: 13.5px;
  color: #f4ecd8;
}

.ps-06__feats li::before {
  content: '✓';
  color: #d4af37;
  font-weight: 700;
  display: inline-block;
  width: 20px;
}

.ps-06__cta {
  display: block;
  padding: 14px 20px;
  border-radius: 10px;
  background: linear-gradient(180deg, #ffd479, #d4af37);
  color: #0b0b1a;
  text-decoration: none;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.01em;
  box-shadow: 0 10px 24px rgba(212,175,55,0.3);
  transition: transform 0.18s;
}

.ps-06__cta:hover {
  transform: translateY(-1px);
}

.ps-06__cta:focus-visible {
  outline: 2px solid #ffd479;
  outline-offset: 3px;
}

.ps-06__foot {
  font-size: 12px;
  color: #8a8068;
  margin: 12px 0 26px;
}

.ps-06__quote {
  margin: 0;
  padding-top: 22px;
  border-top: 1px dashed rgba(212,175,55,0.2);
}

.ps-06__quote p {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 16px;
  font-style: italic;
  color: #f4ecd8;
  margin: 0 0 8px;
  line-height: 1.5;
}

.ps-06__quote cite {
  font-style: normal;
  font-size: 12px;
  color: #8a8068;
  letter-spacing: 0.05em;
}

@media (max-width: 540px) {
  .ps-06__feats {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-06__cta {
    transition: none;
  }
}
```
