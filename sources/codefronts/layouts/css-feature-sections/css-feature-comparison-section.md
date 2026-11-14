---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-feature-comparison-section/"
title: "Feature Comparison Section Included Matrix"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "A real table doing what a table is for: feature rows down the left, three tiers across the top, a ✓ or an em dash in every cell."
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Comparison Section Included Matrix
Source: https://codefronts.com/layouts/css-feature-sections/css-feature-comparison-section/

A real table doing what a table is for: feature rows down the left, three tiers across the top, a ✓ or an em dash in every cell. Row groups keep forty features readable, the header row sticks while you scroll the body, and the highlighted tier column is detected with :has() rather than a class on every cell — so moving the highlight is a one-attribute change.
## HTML
```html
<section class="fs-18" aria-labelledby="fs-18-heading">
  <div class="fs-18__hero" aria-hidden="true">
    <span class="fs-18__wordmark">MERIDIAN CLOUD</span>
    <span class="fs-18__heronav">Platform · Solutions · Partners · Support</span>
  </div>

  <div class="fs-18__stage">
    <div class="fs-18__head">
      <p class="fs-18__eyebrow">Included in every plan</p>
      <h2 class="fs-18__heading" id="fs-18-heading">Feature availability by tier</h2>
      <p class="fs-18__sub">Capabilities only — pricing and commitment terms are in the section below.</p>
    </div>

    <div class="fs-18__scroller">
      <table class="fs-18__table">
        <caption class="fs-18__caption">Feature availability across the Basic, Professional and Enterprise tiers.</caption>
        <thead>
          <tr>
            <th class="fs-18__rowhead" scope="col">Capability</th>
            <th scope="col">Basic</th>
            <th scope="col" data-featured><span class="fs-18__ribbon">Recommended</span>Professional</th>
            <th scope="col">Enterprise</th>
          </tr>
        </thead>
        <tbody>
          <tr class="fs-18__grouprow"><th scope="colgroup" colspan="4">Core platform</th></tr>
          <tr><th class="fs-18__rowhead" scope="row">Projects and environments</th><td>Up to 3</td><td>Unlimited</td><td>Unlimited</td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Managed Postgres</th><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Point-in-time recovery</th><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td>7 days</td><td>35 days</td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Custom domains with managed TLS</th><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td></tr>

          <tr class="fs-18__grouprow"><th scope="colgroup" colspan="4">Collaboration</th></tr>
          <tr><th class="fs-18__rowhead" scope="row">Seats</th><td>3</td><td>25</td><td>Unlimited</td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Role-based access control</th><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Preview environments per branch</th><td>1</td><td>10</td><td>Unlimited</td></tr>

          <tr class="fs-18__grouprow"><th scope="colgroup" colspan="4">Security and compliance</th></tr>
          <tr><th class="fs-18__rowhead" scope="row">SSO with SAML and OIDC</th><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td></tr>
          <tr><th class="fs-18__rowhead" scope="row">SCIM provisioning</th><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Audit log export</th><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td>30 days</td><td>7 years</td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Customer-managed encryption keys</th><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td></tr>

          <tr class="fs-18__grouprow"><th scope="colgroup" colspan="4">Support</th></tr>
          <tr><th class="fs-18__rowhead" scope="row">Response target</th><td>Community</td><td>4 business hours</td><td>15 minutes, 24/7</td></tr>
          <tr><th class="fs-18__rowhead" scope="row">Named technical contact</th><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span class="fs-18__no" aria-hidden="true">—</span><span class="fs-18__sr">Not included</span></td><td><span aria-hidden="true">✓</span><span class="fs-18__sr">Included</span></td></tr>
        </tbody>
      </table>
    </div>
    <p class="fs-18__foot">Need a capability that is not listed? <a class="fs-18__link" href="#fs-18-heading">Ask the solutions team</a></p>
  </div>

  <div class="fs-18__below" aria-hidden="true">Pricing and terms · Service level agreement</div>
</section>
```
## CSS
```css
.fs-18 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f2f5fa;
  --page: oklch(0.965 0.008 250);
  --card: #ffffff;
  --ink: #0f1c33;
  --ink: oklch(0.23 0.038 258);
  --muted: #56637c;
  --muted: oklch(0.49 0.03 262);
  --rule: #d3dbe8;
  --rule: oklch(0.87 0.014 255);
  --accent: #1450c8;
  --accent: oklch(0.47 0.19 262);
  --cellpad: 11px;
  --font-display: "Avenir Next Condensed", "Arial Narrow", "Roboto Condensed", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-18 *,
.fs-18 *::before,
.fs-18 *::after {
  box-sizing: border-box;
}

.fs-18__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 14px 20px;
  background: var(--card);
  border-block-end: 3px solid var(--accent);
}

.fs-18__wordmark {
  font: 700 13px/1 var(--font-display);
  letter-spacing: 0.16em;
}

.fs-18__heronav {
  font-size: 11.5px;
  color: var(--muted);
}

.fs-18__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 4.5vw, 52px) 14px;
}

.fs-18__head {
  inline-size: 100%;
  max-inline-size: 70rem;
  min-inline-size: 0;
  margin: 0 0 20px;
}

.fs-18__eyebrow {
  margin: 0 0 10px;
  font: 700 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-18__heading {
  margin: 0 0 8px;
  font: 700 clamp(24px, 4.4vw, 37px)/1.1 var(--font-display);
  letter-spacing: 0.005em;
  text-wrap: balance;
}

.fs-18__sub {
  margin: 0;
  max-inline-size: 58ch;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-18__scroller {
  inline-size: 100%;
  max-inline-size: 70rem;
  min-inline-size: 0;
  overflow-x: auto;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 6px;
  mask-image: linear-gradient(90deg, #000 0, #000 calc(100% - 22px), transparent 100%);
}

.fs-18__table {
  inline-size: 100%;
  min-inline-size: 620px;
  border-collapse: collapse;
  font-size: 13px;
}

.fs-18__caption {
  padding: 12px 14px;
  text-align: start;
  font-size: 11.5px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--muted);
  border-block-end: 1px solid var(--rule);
}

.fs-18__table thead th {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  padding: 14px var(--cellpad);
  text-align: center;
  vertical-align: bottom;
  font: 700 12.5px/1.3 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  background: var(--card);
  border-block-end: 2px solid var(--ink);
}

.fs-18__table thead th[data-featured] {
  position: sticky;
  color: var(--accent);
}

.fs-18__ribbon {
  display: block;
  margin: 0 auto 6px;
  inline-size: fit-content;
  padding: 3px 8px;
  font: 700 9px/1.3 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #fff;
  background: var(--accent);
  border-radius: 2px;
}

.fs-18__rowhead {
  text-align: start !important;
  font-weight: 600;
  min-inline-size: 0;
}

.fs-18__table tbody th,
.fs-18__table tbody td {
  padding: var(--cellpad);
  border-block-end: 1px solid color-mix(in oklab, var(--rule) 65%, transparent);
}

.fs-18__table tbody td {
  text-align: center;
  color: var(--muted);
}

.fs-18__table tbody tr:hover td,
.fs-18__table tbody tr:hover th {
  background: color-mix(in oklab, var(--accent) 5%, var(--card));
}

.fs-18__grouprow th {
  padding: 10px var(--cellpad);
  text-align: start;
  font: 700 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ink);
  background: color-mix(in oklab, var(--ink) 6%, var(--card));
  border-block-end: 1px solid var(--rule);
}

.fs-18__table:has(thead th:nth-child(3)[data-featured]) tbody td:nth-child(3) {
  background: color-mix(in oklab, var(--accent) 7%, var(--card));
  color: var(--ink);
  font-weight: 600;
}

.fs-18__table:has(thead th:nth-child(3)[data-featured]) tbody tr:hover td:nth-child(3) {
  background: color-mix(in oklab, var(--accent) 12%, var(--card));
}

.fs-18__no {
  color: var(--muted);
  opacity: 0.55;
}

.fs-18__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.fs-18__foot {
  inline-size: 100%;
  max-inline-size: 70rem;
  margin: 14px 0 0;
  font-size: 13px;
  color: var(--muted);
}

.fs-18__link {
  color: var(--accent);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.fs-18__link:hover {
  color: var(--ink);
}

.fs-18__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fs-18__below {
  padding: 14px 20px;
  background: var(--card);
  border-block-start: 1px solid var(--rule);
  font-size: 11.5px;
  color: var(--muted);
}

@media (prefers-color-scheme: dark) {
  .fs-18 {
    --page: #0b1220;
    --card: #121a2a;
    --ink: #e9eef8;
    --muted: #93a1bb;
    --rule: #222d42;
    --accent: #5b91ff;
  }

  .fs-18__ribbon {
    color: #0b1220;
  }
}

[data-theme="dark"] .fs-18 {
  --page: #0b1220;
  --card: #121a2a;
  --ink: #e9eef8;
  --muted: #93a1bb;
  --rule: #222d42;
  --accent: #5b91ff;
}

[data-theme="dark"] .fs-18 .fs-18__ribbon {
  color: #0b1220;
}
```
