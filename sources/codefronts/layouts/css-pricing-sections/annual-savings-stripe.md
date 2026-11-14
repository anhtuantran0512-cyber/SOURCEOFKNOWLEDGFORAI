---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/annual-savings-stripe/"
title: "Annual Savings Stripe"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A pricing layout that makes the annual discount visible — monthly price struck through next to the discounted annual price, with a \"Save $X/yr\" pill underneath."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Annual Savings Stripe
Source: https://codefronts.com/layouts/css-pricing-sections/annual-savings-stripe/

A pricing layout that makes the annual discount visible — monthly price struck through next to the discounted annual price, with a "Save $X/yr" pill underneath. Forest green base with warm orange savings accents — the conversion-tested "anchor and discount" pattern.
## HTML
```html
<section class="ps-21" aria-label="Pricing">
  <header class="ps-21__head">
    <h2>Pay yearly, save real money.</h2>
    <p>Same product, two months free when you commit to a year.</p>
  </header>
  <div class="ps-21__grid">
    <article class="ps-21__card">
      <h3>Seedling</h3>
      <div class="ps-21__prices">
        <span class="ps-21__was" aria-label="Monthly price, was">$15<em>/mo</em></span>
        <span class="ps-21__now"><strong>$12</strong><em>/mo billed yearly</em></span>
      </div>
      <span class="ps-21__bag" aria-label="Yearly savings">Save $36/yr</span>
      <ul>
        <li>1 garden</li>
        <li>30 plant slots</li>
        <li>Care reminders</li>
      </ul>
      <a class="ps-21__cta" href="#seedling">Choose Seedling</a>
    </article>
    <article class="ps-21__card ps-21__rec">
      <span class="ps-21__pill">Recommended</span>
      <h3>Greenhouse</h3>
      <div class="ps-21__prices">
        <span class="ps-21__was" aria-label="Monthly price, was">$36<em>/mo</em></span>
        <span class="ps-21__now"><strong>$29</strong><em>/mo billed yearly</em></span>
      </div>
      <span class="ps-21__bag" aria-label="Yearly savings">Save $84/yr</span>
      <ul>
        <li>10 gardens</li>
        <li>Unlimited slots</li>
        <li>Disease alerts</li>
        <li>Soil data sync</li>
      </ul>
      <a class="ps-21__cta ps-21__cta-pri" href="#greenhouse">Choose Greenhouse</a>
    </article>
    <article class="ps-21__card">
      <h3>Estate</h3>
      <div class="ps-21__prices">
        <span class="ps-21__was" aria-label="Monthly price, was">$96<em>/mo</em></span>
        <span class="ps-21__now"><strong>$79</strong><em>/mo billed yearly</em></span>
      </div>
      <span class="ps-21__bag" aria-label="Yearly savings">Save $204/yr</span>
      <ul>
        <li>Multi-property</li>
        <li>Pro APIs</li>
        <li>Phone support</li>
      </ul>
      <a class="ps-21__cta" href="#estate">Choose Estate</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-21 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(60% 60% at 50% 0%, rgba(34,107,72,0.2), transparent 60%), #07140e;
  color: #e7f5ee;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-21__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 36px);
}

.ps-21__head h2 {
  font-size: clamp(24px, 3.6vw, 36px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #fff;
}

.ps-21__head p {
  color: #94b5a3;
  margin: 0;
  font-size: 14px;
}

.ps-21__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  max-width: 980px;
  margin: 0 auto;
  align-items: center;
}

.ps-21__card {
  position: relative;
  background: #0d2018;
  border: 1px solid rgba(52,153,108,0.22);
  border-radius: 14px;
  padding: 24px 22px 20px;
  display: flex;
  flex-direction: column;
}

.ps-21__rec {
  background: linear-gradient(180deg, #14301f, #0d2018);
  border-color: #34996c;
  box-shadow: 0 0 0 1px #34996c inset, 0 14px 36px rgba(52,153,108,0.2);
  transform: scale(1.04);
}

.ps-21__pill {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: #34996c;
  color: #07140e;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 11px;
  border-radius: 999px;
}

.ps-21__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 0 0 14px;
  color: #6ee7b7;
}

.ps-21__prices {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 8px;
}

.ps-21__was {
  font-size: 14px;
  color: #94b5a3;
  text-decoration: line-through;
  text-decoration-color: #f97316;
  text-decoration-thickness: 2px;
}

.ps-21__was em {
  font-style: normal;
  font-size: 12px;
  opacity: 0.8;
}

.ps-21__now {
  display: flex;
  align-items: baseline;
  gap: 6px;
}

.ps-21__now strong {
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #fff;
}

.ps-21__now em {
  font-style: normal;
  font-size: 12px;
  color: #94b5a3;
}

.ps-21__bag {
  display: inline-block;
  align-self: flex-start;
  background: #f97316;
  color: #07140e;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.04em;
  padding: 3px 10px;
  border-radius: 4px;
  margin-bottom: 18px;
}

.ps-21__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 20px;
  flex: 1;
  font-size: 13.5px;
  line-height: 1.95;
  color: #c8e0d3;
}

.ps-21__card ul li::before {
  content: '✓';
  color: #34d399;
  display: inline-block;
  width: 20px;
  font-weight: 700;
}

.ps-21__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 8px;
  background: rgba(52,153,108,0.14);
  color: #6ee7b7;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid rgba(52,153,108,0.32);
  transition: background 0.18s, color 0.18s;
}

.ps-21__cta-pri {
  background: #34996c;
  color: #07140e;
  border-color: #34996c;
}

.ps-21__cta:hover {
  background: #34996c;
  color: #07140e;
}

.ps-21__cta:focus-visible {
  outline: 2px solid #34996c;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-21__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
  }

  .ps-21__rec {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-21__cta {
    transition: none;
  }
}
```
