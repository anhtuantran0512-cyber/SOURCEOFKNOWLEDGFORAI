---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/feature-accordion-tiers/"
title: "Feature Accordion Tiers"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Three tier cards with native <details>/<summary> dropdowns that reveal the full feature list on click — keeps the page short and lets curious buyers dig in."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Accordion Tiers
Source: https://codefronts.com/layouts/css-pricing-sections/feature-accordion-tiers/

Three tier cards with native <details>/<summary> dropdowns that reveal the full feature list on click — keeps the page short and lets curious buyers dig in. Deep purple palette, no JS, fully keyboard-accessible.
## HTML
```html
<section class="ps-19" aria-label="Pricing">
  <header class="ps-19__head">
    <h2>Pricing without the wall of checkmarks.</h2>
    <p>Open any tier to read the full feature list. Tap to collapse.</p>
  </header>
  <div class="ps-19__grid">
    <article class="ps-19__card">
      <h3>Indie</h3>
      <div class="ps-19__price"><em>$</em>11<span>/mo</span></div>
      <p class="ps-19__sub">For solo developers shipping side projects.</p>
      <details class="ps-19__det">
        <summary>See all features <span aria-hidden="true">⌄</span></summary>
        <ul>
          <li>1 project workspace</li>
          <li>10 GB storage</li>
          <li>Community forum support</li>
          <li>Public deploys with auto-SSL</li>
          <li>50K monthly visitor cap</li>
          <li>1-year version history</li>
        </ul>
      </details>
      <a class="ps-19__cta" href="#indie">Choose Indie →</a>
    </article>
    <article class="ps-19__card ps-19__pri">
      <span class="ps-19__pill">Recommended</span>
      <h3>Studio</h3>
      <div class="ps-19__price"><em>$</em>34<span>/mo</span></div>
      <p class="ps-19__sub">For small teams shipping to real users.</p>
      <details class="ps-19__det" open>
        <summary>See all features <span aria-hidden="true">⌄</span></summary>
        <ul>
          <li>Unlimited project workspaces</li>
          <li>100 GB storage</li>
          <li>Priority email + chat support</li>
          <li>Custom domains with auto-SSL</li>
          <li>500K monthly visitor cap</li>
          <li>3-year version history</li>
          <li>Team roles &amp; permissions</li>
          <li>Slack, GitHub, Linear sync</li>
        </ul>
      </details>
      <a class="ps-19__cta ps-19__cta-pri" href="#studio">Choose Studio →</a>
    </article>
    <article class="ps-19__card">
      <h3>Org</h3>
      <div class="ps-19__price"><em>$</em>96<span>/mo</span></div>
      <p class="ps-19__sub">For organisations with compliance requirements.</p>
      <details class="ps-19__det">
        <summary>See all features <span aria-hidden="true">⌄</span></summary>
        <ul>
          <li>Everything in Studio</li>
          <li>SAML SSO &amp; SCIM provisioning</li>
          <li>Audit logs (90-day retention)</li>
          <li>Unlimited monthly visitors</li>
          <li>Forever version history</li>
          <li>SOC 2 + DPA on file</li>
          <li>SLA 99.99% with credits</li>
          <li>Dedicated CSM &amp; quarterly review</li>
        </ul>
      </details>
      <a class="ps-19__cta" href="#org">Talk to sales →</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-19 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(60% 60% at 50% 0%, rgba(168,85,247,0.16), transparent 60%), #15071f;
  color: #f3e8ff;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-19__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 36px);
}

.ps-19__head h2 {
  font-size: clamp(22px, 3.4vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #fff;
}

.ps-19__head p {
  color: #c4a8d6;
  margin: 0;
  font-size: 14px;
}

.ps-19__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  max-width: 980px;
  margin: 0 auto;
  align-items: start;
}

.ps-19__card {
  position: relative;
  background: #281033;
  border: 1px solid rgba(168,85,247,0.2);
  border-radius: 14px;
  padding: 24px 22px 20px;
  display: flex;
  flex-direction: column;
}

.ps-19__pri {
  background: linear-gradient(180deg, #3b1554, #281033);
  border-color: #a855f7;
  box-shadow: 0 0 0 1px #a855f7 inset, 0 16px 40px rgba(168,85,247,0.22);
}

.ps-19__pill {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #a855f7, #d946ef);
  color: #15071f;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 11px;
  border-radius: 999px;
}

.ps-19__card h3 {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin: 0 0 6px;
  color: #d8b4fe;
}

.ps-19__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  font-size: 36px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 6px;
  color: #fff;
}

.ps-19__price em {
  font-size: 0.5em;
  font-style: normal;
  padding-right: 2px;
  opacity: 0.7;
}

.ps-19__price span {
  font-size: 0.32em;
  font-weight: 500;
  opacity: 0.65;
  margin-left: 6px;
}

.ps-19__sub {
  font-size: 13px;
  color: #c4a8d6;
  margin: 0 0 16px;
  line-height: 1.5;
  min-height: 36px;
}

.ps-19__det {
  border: 1px solid rgba(168,85,247,0.18);
  border-radius: 8px;
  padding: 0 14px;
  margin-bottom: 16px;
  background: rgba(168,85,247,0.05);
}

.ps-19__det[open] {
  padding-bottom: 4px;
}

.ps-19__det summary {
  cursor: pointer;
  padding: 11px 0;
  font-size: 13px;
  font-weight: 600;
  color: #d8b4fe;
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  outline: 0;
}

.ps-19__det summary::-webkit-details-marker {
  display: none;
}

.ps-19__det summary span {
  display: inline-block;
  font-size: 14px;
  transition: transform 0.25s;
}

.ps-19__det[open] summary span {
  transform: rotate(180deg);
}

.ps-19__det summary:focus-visible {
  outline: 2px solid #a855f7;
  outline-offset: 3px;
  border-radius: 4px;
}

.ps-19__det ul {
  list-style: none;
  padding: 0;
  margin: 0 0 8px;
  font-size: 12.5px;
  line-height: 1.95;
  color: #d8c8e8;
  border-top: 1px dashed rgba(168,85,247,0.18);
  padding-top: 10px;
}

.ps-19__det ul li::before {
  content: '✓';
  color: #d946ef;
  display: inline-block;
  width: 18px;
  font-weight: 700;
}

.ps-19__cta {
  display: block;
  text-align: center;
  margin-top: auto;
  padding: 11px 16px;
  border-radius: 8px;
  background: rgba(168,85,247,0.12);
  color: #d8b4fe;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid rgba(168,85,247,0.3);
  transition: background 0.18s, color 0.18s;
}

.ps-19__cta-pri {
  background: linear-gradient(135deg, #a855f7, #d946ef);
  color: #15071f;
  border-color: transparent;
}

.ps-19__cta:hover {
  background: rgba(168,85,247,0.28);
  color: #fff;
}

.ps-19__cta:focus-visible {
  outline: 2px solid #d946ef;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-19__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
  }

  .ps-19__sub {
    min-height: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-19__det summary span {
    transition: none;
  }

  .ps-19__cta {
    transition: none;
  }
}
```
