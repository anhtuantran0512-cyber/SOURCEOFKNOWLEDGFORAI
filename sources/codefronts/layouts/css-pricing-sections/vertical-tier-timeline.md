---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/vertical-tier-timeline/"
title: "Vertical Tier Timeline"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Tiers presented as a vertical roadmap — Free → Pro → Enterprise — connected by a glowing lime spine."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tier Timeline
Source: https://codefronts.com/layouts/css-pricing-sections/vertical-tier-timeline/

Tiers presented as a vertical roadmap — Free → Pro → Enterprise — connected by a glowing lime spine. Each station is a real <ol>/<li> with a numbered milestone, price, and feature list. Reads as a growth path, not a column comparison.
## HTML
```html
<section class="ps-08" aria-label="Pricing">
  <header class="ps-08__head">
    <h2>Grow into the next plan, not out of one.</h2>
    <p>Three stops on the same road. Switch up or down with one click.</p>
  </header>
  <ol class="ps-08__line">
    <li class="ps-08__stop">
      <span class="ps-08__num" aria-hidden="true">01</span>
      <article class="ps-08__pane">
        <header>
          <h3>Free</h3>
          <span class="ps-08__pri">$0</span>
        </header>
        <p>
          Open-source projects, side experiments, anything you want to ship without a credit card.
        </p>
        <ul>
          <li>1 project</li>
          <li>500 MB storage</li>
          <li>Public repos only</li>
        </ul>
        <a class="ps-08__cta" href="#free">Start free →</a>
      </article>
    </li>
    <li class="ps-08__stop ps-08__current">
      <span class="ps-08__num" aria-hidden="true">02</span>
      <article class="ps-08__pane">
        <header>
          <h3>Pro</h3>
          <span class="ps-08__pri">$24<em>/mo</em></span>
        </header>
        <p>
          Where most teams settle. Private projects, real support, and the integrations you actually
          use.
        </p>
        <ul>
          <li>Unlimited projects</li>
          <li>50 GB storage</li>
          <li>Email + chat support</li>
          <li>Slack, GitHub, Linear sync</li>
        </ul>
        <a class="ps-08__cta ps-08__cta-pri" href="#pro">Choose Pro →</a>
      </article>
    </li>
    <li class="ps-08__stop">
      <span class="ps-08__num" aria-hidden="true">03</span>
      <article class="ps-08__pane">
        <header>
          <h3>Enterprise</h3>
          <span class="ps-08__pri">Custom</span>
        </header>
        <p>
          For teams with procurement processes, security reviews, and quarterly business reviews.
        </p>
        <ul>
          <li>SSO + SAML + audit logs</li>
          <li>SLA, dedicated CSM</li>
          <li>Custom DPA &amp; invoicing</li>
        </ul>
        <a class="ps-08__cta" href="#ent">Talk to sales →</a>
      </article>
    </li>
  </ol>
</section>
```
## CSS
```css
.ps-08 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #0a1408;
  color: #ecfccb;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-08__head {
  text-align: center;
  margin-bottom: clamp(28px, 5vw, 44px);
}

.ps-08__head h2 {
  font-size: clamp(22px, 3.4vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #f7feec;
}

.ps-08__head p {
  color: #93a87f;
  margin: 0;
  font-size: 14px;
}

.ps-08__line {
  position: relative;
  list-style: none;
  padding: 0;
  margin: 0 auto;
  max-width: 580px;
}

.ps-08__line::before {
  content: '';
  position: absolute;
  left: 28px;
  top: 18px;
  bottom: 18px;
  width: 2px;
  background: linear-gradient(180deg, #84cc16, rgba(132,204,22,0.2));
  border-radius: 2px;
}

.ps-08__stop {
  position: relative;
  padding: 0 0 24px 70px;
  min-height: 56px;
}

.ps-08__stop:last-child {
  padding-bottom: 0;
}

.ps-08__num {
  position: absolute;
  left: 6px;
  top: 0;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: #0a1408;
  border: 2px solid #84cc16;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 700;
  color: #84cc16;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.ps-08__current .ps-08__num {
  background: #84cc16;
  color: #0a1408;
  box-shadow: 0 0 0 6px rgba(132,204,22,0.18);
}

.ps-08__pane {
  background: #14210e;
  border: 1px solid rgba(132,204,22,0.18);
  border-radius: 12px;
  padding: 18px 18px 16px;
}

.ps-08__current .ps-08__pane {
  border-color: #84cc16;
  background: linear-gradient(180deg, #1a3010, #14210e);
  box-shadow: 0 8px 24px rgba(132,204,22,0.12);
}

.ps-08__pane header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 8px;
  border-bottom: 1px dashed rgba(132,204,22,0.18);
  padding-bottom: 10px;
}

.ps-08__pane h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin: 0;
  color: #84cc16;
}

.ps-08__pri {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #f7feec;
}

.ps-08__pri em {
  font-size: 12px;
  font-style: normal;
  color: #93a87f;
  font-weight: 500;
  margin-left: 2px;
}

.ps-08__pane p {
  font-size: 13px;
  color: #c8d8b0;
  margin: 10px 0;
  line-height: 1.55;
}

.ps-08__pane ul {
  list-style: none;
  padding: 0;
  margin: 0 0 14px;
  font-size: 13px;
  line-height: 1.85;
  color: #c8d8b0;
}

.ps-08__pane ul li::before {
  content: '→';
  color: #84cc16;
  display: inline-block;
  width: 20px;
  font-weight: 700;
}

.ps-08__cta {
  display: inline-block;
  padding: 9px 14px;
  border-radius: 7px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  border: 1px solid rgba(132,204,22,0.4);
  color: #84cc16;
  background: transparent;
  transition: background 0.18s, color 0.18s;
}

.ps-08__cta:hover {
  background: rgba(132,204,22,0.15);
  color: #ecfccb;
}

.ps-08__cta-pri {
  background: #84cc16;
  color: #0a1408;
  border-color: #84cc16;
}

.ps-08__cta-pri:hover {
  background: #a3e635;
  color: #0a1408;
  border-color: #a3e635;
}

.ps-08__cta:focus-visible {
  outline: 2px solid #a3e635;
  outline-offset: 3px;
}
```
