---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/classic-three-tier/"
title: "Classic Three Tier"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "The canonical SaaS pricing layout — three equal tier cards (Starter / Team / Business) with emerald accent."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Classic Three Tier
Source: https://codefronts.com/layouts/css-pricing-sections/classic-three-tier/

The canonical SaaS pricing layout — three equal tier cards (Starter / Team / Business) with emerald accent. Real <ul> feature lists, dashed dividers, and full-width CTAs at the bottom. The conversion-tested baseline every team starts from.
## HTML
```html
<section class="ps-01" aria-label="Pricing">
  <header class="ps-01__head">
    <span class="ps-01__eye">Pricing</span>
    <h2>Pick the plan that fits today.</h2>
    <p>Upgrade, downgrade, or cancel any time. No fine print.</p>
  </header>
  <div class="ps-01__grid">
    <article class="ps-01__card">
      <h3>Starter</h3>
      <p class="ps-01__sub">For solo builders shipping their first thing.</p>
      <div class="ps-01__price">
        <span class="ps-01__amt">$9</span><span class="ps-01__per">/ month</span>
      </div>
      <ul class="ps-01__feats">
        <li>1 project</li>
        <li>2 GB storage</li>
        <li>Community support</li>
        <li>Basic analytics</li>
      </ul>
      <a class="ps-01__cta" href="#starter">Start free →</a>
    </article>
    <article class="ps-01__card">
      <h3>Team</h3>
      <p class="ps-01__sub">For small teams who need to ship together.</p>
      <div class="ps-01__price">
        <span class="ps-01__amt">$29</span><span class="ps-01__per">/ month</span>
      </div>
      <ul class="ps-01__feats">
        <li>10 projects</li>
        <li>50 GB storage</li>
        <li>Email support</li>
        <li>Team analytics</li>
        <li>Role-based access</li>
      </ul>
      <a class="ps-01__cta" href="#team">Start 14-day trial →</a>
    </article>
    <article class="ps-01__card">
      <h3>Business</h3>
      <p class="ps-01__sub">For growing companies that need governance.</p>
      <div class="ps-01__price">
        <span class="ps-01__amt">$79</span><span class="ps-01__per">/ month</span>
      </div>
      <ul class="ps-01__feats">
        <li>Unlimited projects</li>
        <li>500 GB storage</li>
        <li>Priority support</li>
        <li>Advanced analytics</li>
        <li>SSO + audit logs</li>
        <li>SOC 2 ready</li>
      </ul>
      <a class="ps-01__cta" href="#business">Talk to sales →</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-01 {
  display: block;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #07120e;
  color: #e7f5ee;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

.ps-01__head {
  text-align: center;
  margin-bottom: clamp(20px, 4vw, 40px);
}

.ps-01__eye {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #34d399;
  margin-bottom: 12px;
}

.ps-01__head h2 {
  font-size: clamp(22px, 3.4vw, 34px);
  font-weight: 700;
  letter-spacing: -0.01em;
  margin: 0 0 8px;
}

.ps-01__head p {
  color: #9bb5a8;
  margin: 0;
  font-size: 14px;
}

.ps-01__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  max-width: 980px;
  margin: 0 auto;
}

.ps-01__card {
  background: #0d1f18;
  border: 1px solid rgba(52,211,153,0.2);
  border-radius: 14px;
  padding: 22px 20px 20px;
  display: flex;
  flex-direction: column;
  transition: border-color 0.2s, transform 0.2s;
}

.ps-01__card:hover {
  border-color: #34d399;
  transform: translateY(-2px);
}

.ps-01__card h3 {
  font-size: 15px;
  font-weight: 700;
  margin: 0 0 4px;
  color: #34d399;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.ps-01__sub {
  font-size: 13px;
  color: #9bb5a8;
  margin: 0 0 18px;
  line-height: 1.5;
  min-height: 38px;
}

.ps-01__price {
  display: flex;
  align-items: baseline;
  gap: 6px;
  margin-bottom: 18px;
  padding-bottom: 18px;
  border-bottom: 1px dashed rgba(52,211,153,0.25);
}

.ps-01__amt {
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #f0fff7;
}

.ps-01__per {
  font-size: 13px;
  color: #9bb5a8;
}

.ps-01__feats {
  list-style: none;
  padding: 0;
  margin: 0 0 22px;
  flex: 1;
}

.ps-01__feats li {
  position: relative;
  padding: 6px 0 6px 22px;
  font-size: 13.5px;
  color: #d2e9dc;
}

.ps-01__feats li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 14px;
  height: 14px;
  transform: translateY(-50%);
  background: linear-gradient(135deg, transparent 50%, #34d399 50%) center/100% 100% no-repeat;
  -webkit-mask: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path fill='black' d='M6.5 11.5 3 8l1-1 2.5 2.5L12 4l1 1z'/></svg>") center/contain no-repeat;
  mask: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path fill='black' d='M6.5 11.5 3 8l1-1 2.5 2.5L12 4l1 1z'/></svg>") center/contain no-repeat;
  background: #34d399;
}

.ps-01__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 8px;
  background: rgba(52,211,153,0.12);
  color: #34d399;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid rgba(52,211,153,0.28);
  transition: background 0.18s, color 0.18s;
}

.ps-01__cta:hover {
  background: #34d399;
  color: #07120e;
}

.ps-01__cta:focus-visible {
  outline: 2px solid #34d399;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-01__grid {
    grid-template-columns: 1fr;
    max-width: 460px;
  }

  .ps-01__sub {
    min-height: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-01__card {
    transition: none;
  }

  .ps-01__card:hover {
    transform: none;
  }
}
```
