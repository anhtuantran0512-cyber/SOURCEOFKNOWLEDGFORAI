---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/feature-comparison-table/"
title: "Feature Comparison Table"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A real <table> with proper <th scope>, sticky header row, and check / dash cells comparing four plans across nine features."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Comparison Table
Source: https://codefronts.com/layouts/css-pricing-sections/feature-comparison-table/

A real <table> with proper <th scope>, sticky header row, and check / dash cells comparing four plans across nine features. Cyan accent on the recommended column. Mobile fallback collapses to a stacked card list under 720px.
## HTML
```html
<section class="ps-03" aria-label="Plan comparison">
  <header class="ps-03__head">
    <h2>Compare every feature.</h2>
    <p>Pick the column that matches what you ship today.</p>
  </header>
  <div class="ps-03__scroll">
    <table class="ps-03__tbl">
      <thead>
        <tr>
          <th scope="col" class="ps-03__fc">Feature</th>
          <th scope="col">Free<br /><span>$0</span></th>
          <th scope="col" class="ps-03__rec">
            <span class="ps-03__pill">Recommended</span>Pro<br /><span>$24</span>
          </th>
          <th scope="col">Team<br /><span>$48</span></th>
          <th scope="col">Enterprise<br /><span>Contact</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Projects</th>
          <td>1</td>
          <td class="ps-03__rec">10</td>
          <td>50</td>
          <td>Unlimited</td>
        </tr>
        <tr>
          <th scope="row">Storage</th>
          <td>500 MB</td>
          <td class="ps-03__rec">10 GB</td>
          <td>50 GB</td>
          <td>500 GB</td>
        </tr>
        <tr>
          <th scope="row">Custom domain</th>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td class="ps-03__rec"><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
        </tr>
        <tr>
          <th scope="row">Team roles</th>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td class="ps-03__rec"><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
        </tr>
        <tr>
          <th scope="row">Priority support</th>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td class="ps-03__rec"><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
        </tr>
        <tr>
          <th scope="row">SSO &amp; SAML</th>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td class="ps-03__rec"><span class="ps-03__no" aria-label="not included">—</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
        </tr>
        <tr>
          <th scope="row">Audit logs</th>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td class="ps-03__rec"><span class="ps-03__no" aria-label="not included">—</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
        </tr>
        <tr>
          <th scope="row">99.99% SLA</th>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td class="ps-03__rec"><span class="ps-03__no" aria-label="not included">—</span></td>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
        </tr>
        <tr>
          <th scope="row">Dedicated CSM</th>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td class="ps-03__rec"><span class="ps-03__no" aria-label="not included">—</span></td>
          <td><span class="ps-03__no" aria-label="not included">—</span></td>
          <td><span class="ps-03__yes" aria-label="included">✓</span></td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th scope="row" class="ps-03__fc"></th>
          <td><a class="ps-03__cta" href="#free">Get started</a></td>
          <td class="ps-03__rec">
            <a class="ps-03__cta ps-03__cta-pri" href="#pro">Choose Pro →</a>
          </td>
          <td><a class="ps-03__cta" href="#team">Choose Team</a></td>
          <td><a class="ps-03__cta" href="#ent">Talk to sales</a></td>
        </tr>
      </tfoot>
    </table>
  </div>
</section>
```
## CSS
```css
.ps-03 {
  padding: clamp(28px, 5vw, 56px) clamp(16px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #06141a;
  color: #e0f2f7;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-03__head {
  text-align: center;
  margin-bottom: clamp(20px, 4vw, 36px);
}

.ps-03__head h2 {
  font-size: clamp(22px, 3.2vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #f1fbff;
}

.ps-03__head p {
  color: #88a8b3;
  margin: 0;
  font-size: 14px;
}

.ps-03__scroll {
  overflow-x: auto;
  overflow-y: visible;
  -webkit-overflow-scrolling: touch;
  max-width: 980px;
  margin: 0 auto;
  padding-top: 14px;
}

.ps-03__tbl {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13.5px;
  min-width: 720px;
}

.ps-03__tbl th,
.ps-03__tbl td {
  text-align: center;
  padding: 14px 12px;
  border-bottom: 1px solid rgba(34,211,238,0.1);
}

.ps-03__tbl thead th {
  font-size: 14px;
  font-weight: 700;
  color: #cfeaf2;
  background: #0c1f27;
  position: relative;
}

.ps-03__tbl thead th span:not(.ps-03__pill) {
  display: block;
  font-size: 13px;
  font-weight: 500;
  color: #88a8b3;
  margin-top: 4px;
}

.ps-03__fc {
  text-align: left !important;
  color: #88a8b3 !important;
  font-weight: 500 !important;
  background: transparent !important;
}

.ps-03__tbl tbody th {
  text-align: left;
  font-weight: 500;
  color: #cfeaf2;
}

.ps-03__rec {
  background: rgba(34,211,238,0.06);
  color: #22d3ee;
  position: relative;
}

.ps-03__tbl thead th.ps-03__rec {
  background: linear-gradient(180deg, rgba(34,211,238,0.18), rgba(34,211,238,0.04));
  color: #5eead4;
}

.ps-03__pill {
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  background: #22d3ee;
  color: #06141a;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 999px;
}

.ps-03__yes {
  display: inline-block;
  width: 22px;
  height: 22px;
  line-height: 22px;
  border-radius: 50%;
  background: rgba(34,211,238,0.15);
  color: #22d3ee;
  font-weight: 700;
}

.ps-03__no {
  color: #4a606a;
  font-weight: 500;
}

.ps-03__tbl tfoot td {
  padding-top: 18px;
  padding-bottom: 4px;
  border: 0;
}

.ps-03__cta {
  display: inline-block;
  padding: 9px 16px;
  border-radius: 7px;
  font-size: 12.5px;
  font-weight: 600;
  text-decoration: none;
  border: 1px solid rgba(34,211,238,0.3);
  color: #5eead4;
  transition: background 0.18s, color 0.18s;
}

.ps-03__cta:hover {
  background: rgba(34,211,238,0.18);
  color: #f1fbff;
}

.ps-03__cta-pri {
  background: #22d3ee;
  color: #06141a;
  border-color: #22d3ee;
}

.ps-03__cta-pri:hover {
  background: #5eead4;
  color: #06141a;
}

.ps-03__cta:focus-visible {
  outline: 2px solid #22d3ee;
  outline-offset: 3px;
}

@media (max-width: 720px) {
  .ps-03__scroll {
    padding-bottom: 8px;
  }

  .ps-03__tbl thead th,
    .ps-03__tbl tbody th,
    .ps-03__tbl td {
    padding: 10px 8px;
    font-size: 12px;
  }

  .ps-03__pill {
    font-size: 9px;
    padding: 2px 6px;
  }
}
```
