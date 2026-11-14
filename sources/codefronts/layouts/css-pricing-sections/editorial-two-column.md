---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/editorial-two-column/"
title: "Editorial Two Column"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A dense editorial pricing layout — left column carries the value-prop copy, right column stacks two compact tier rows like a printed price list."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Two Column
Source: https://codefronts.com/layouts/css-pricing-sections/editorial-two-column/

A dense editorial pricing layout — left column carries the value-prop copy, right column stacks two compact tier rows like a printed price list. Neutral charcoal on cream, the Stripe / Basecamp documentation aesthetic.
## HTML
```html
<section class="ps-13" aria-label="Pricing">
  <div class="ps-13__grid">
    <div class="ps-13__copy">
      <span class="ps-13__eye">— Pricing</span>
      <h2>Two plans. <em>Pick one,</em> change later.</h2>
      <p>
        We don’t play games with feature gating, seat limits, or upsell pop-ups. Pick a plan, get
        the whole product, and move on with your work.
      </p>
      <p class="ps-13__fine">
        All plans include unlimited projects, every integration, and email support. Cancel any time,
        money back inside 30 days.
      </p>
      <a class="ps-13__link" href="#compare">See the full feature list →</a>
    </div>
    <div class="ps-13__tiers">
      <article class="ps-13__row">
        <header>
          <h3>Solo</h3>
          <span class="ps-13__pri">$15<em>/ month</em></span>
        </header>
        <p>For freelancers and indie builders shipping client work.</p>
        <ul>
          <li>Single workspace</li>
          <li>10 GB storage</li>
          <li>Email support</li>
        </ul>
        <a class="ps-13__cta" href="#solo">Choose Solo →</a>
      </article>
      <article class="ps-13__row ps-13__rec">
        <header>
          <h3>Studio <span class="ps-13__tag">Recommended</span></h3>
          <span class="ps-13__pri">$48<em>/ month</em></span>
        </header>
        <p>For small teams who run multiple client engagements.</p>
        <ul>
          <li>Unlimited workspaces</li>
          <li>250 GB storage</li>
          <li>Priority support &amp; onboarding</li>
          <li>Client billing &amp; white-label</li>
        </ul>
        <a class="ps-13__cta ps-13__cta-pri" href="#studio">Choose Studio →</a>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.ps-13 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #f5f1ea;
  color: #1c1c1e;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-13__grid {
  max-width: 1040px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 56px;
  align-items: start;
}

.ps-13__copy {
  padding-top: 6px;
}

.ps-13__eye {
  display: block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.1em;
  color: #6b6b6e;
  margin-bottom: 14px;
}

.ps-13__copy h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(28px, 4.4vw, 44px);
  font-weight: 700;
  letter-spacing: -0.015em;
  line-height: 1.1;
  margin: 0 0 18px;
}

.ps-13__copy h2 em {
  font-style: italic;
  color: #6b6b6e;
}

.ps-13__copy p {
  font-size: 15px;
  line-height: 1.65;
  color: #3d3d40;
  margin: 0 0 12px;
  max-width: 380px;
}

.ps-13__fine {
  font-size: 13px !important;
  color: #6b6b6e !important;
  padding-top: 12px;
  border-top: 1px solid #d8d2c5;
}

.ps-13__link {
  display: inline-block;
  margin-top: 12px;
  font-size: 13px;
  font-weight: 600;
  color: #1c1c1e;
  text-decoration: underline;
  text-underline-offset: 4px;
  text-decoration-thickness: 1.5px;
}

.ps-13__link:hover {
  color: #6b6b6e;
}

.ps-13__tiers {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ps-13__row {
  background: #fff;
  border: 1px solid #d8d2c5;
  border-radius: 6px;
  padding: 22px 22px 18px;
  transition: border-color 0.18s, box-shadow 0.18s;
}

.ps-13__row:hover {
  border-color: #1c1c1e;
  box-shadow: 4px 4px 0 0 #1c1c1e;
}

.ps-13__rec {
  border-color: #1c1c1e;
  box-shadow: 4px 4px 0 0 #1c1c1e;
}

.ps-13__row header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 12px;
  margin-bottom: 12px;
  border-bottom: 1px dashed #d8d2c5;
}

.ps-13__row h3 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 22px;
  font-weight: 700;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.ps-13__tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  background: #1c1c1e;
  color: #f5f1ea;
  padding: 3px 8px;
  border-radius: 2px;
}

.ps-13__pri {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.ps-13__pri em {
  font-size: 11px;
  font-style: normal;
  color: #6b6b6e;
  font-weight: 500;
  margin-left: 4px;
  letter-spacing: 0;
}

.ps-13__row p {
  font-size: 13.5px;
  color: #3d3d40;
  margin: 0 0 10px;
  line-height: 1.5;
}

.ps-13__row ul {
  list-style: none;
  padding: 0;
  margin: 0 0 16px;
  font-size: 13px;
  line-height: 1.85;
  color: #3d3d40;
}

.ps-13__row ul li::before {
  content: '·';
  color: #1c1c1e;
  font-weight: 800;
  display: inline-block;
  width: 18px;
  font-size: 18px;
  line-height: 0.5;
  vertical-align: middle;
}

.ps-13__cta {
  display: inline-block;
  padding: 9px 16px;
  border-radius: 4px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  border: 1.5px solid #1c1c1e;
  color: #1c1c1e;
  background: transparent;
  transition: background 0.18s, color 0.18s;
}

.ps-13__cta-pri {
  background: #1c1c1e;
  color: #f5f1ea;
}

.ps-13__cta:hover {
  background: #1c1c1e;
  color: #f5f1ea;
}

.ps-13__cta-pri:hover {
  background: #f5f1ea;
  color: #1c1c1e;
}

.ps-13__cta:focus-visible {
  outline: 2px solid #1c1c1e;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-13__grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-13__row {
    transition: none;
  }

  .ps-13__row:hover {
    transform: none;
  }
}
```
