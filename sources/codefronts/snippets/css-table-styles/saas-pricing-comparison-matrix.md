---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/saas-pricing-comparison-matrix/"
title: "SaaS Pricing Comparison Matrix"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A three-tier pricing comparison table with a glowing \"Most Popular\" Pro column badge, gradient column shading, and inline CTA buttons — entirely driven by…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Pricing Comparison Matrix
Source: https://codefronts.com/snippets/css-table-styles/saas-pricing-comparison-matrix/

A three-tier pricing comparison table with a glowing "Most Popular" Pro column badge, gradient column shading, and inline CTA buttons — entirely driven by CSS col groups and custom properties.
## HTML
```html
<div class="ct-02">
  <div class="ct-02__eyebrow">
    <div class="ct-02__label">⚡ Pricing Plans</div>
    <h2 class="ct-02__heading">Choose Your Power Level</h2>
    <p class="ct-02__sub">Scale from indie hacker to enterprise without friction</p>
  </div>
  <div class="ct-02__wrap">
    <table>
      <colgroup>
        <col style="width:38%">
        <col class="basic" style="width:20%">
        <col class="pro" style="width:22%">
        <col class="ent" style="width:20%">
      </colgroup>
      <thead>
        <tr>
          <th><div class="ct-02__plan-cell"></div></th>
          <th><div class="ct-02__plan-cell">
            <div class="ct-02__plan-name ct-02__plan-name--basic">Basic</div>
            <div class="ct-02__price">$9<span>/mo</span></div>
          </div></th>
          <th><div class="ct-02__plan-cell ct-02__plan-cell--pro">
            <div class="ct-02__badge">🔥 Most Popular</div>
            <div class="ct-02__plan-name ct-02__plan-name--pro">Pro</div>
            <div class="ct-02__price" style="color:#a855f7">$29<span>/mo</span></div>
          </div></th>
          <th><div class="ct-02__plan-cell">
            <div class="ct-02__plan-name ct-02__plan-name--ent">Enterprise</div>
            <div class="ct-02__price" style="font-size:20px;margin-top:4px">Custom</div>
          </div></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>AI Requests / month</td>
          <td><span class="ct-02__limit">500</span></td>
          <td><span class="ct-02__highlight">10,000</span></td>
          <td><span class="ct-02__limit">Unlimited</span></td>
        </tr>
        <tr>
          <td>Team Seats</td>
          <td><span class="ct-02__limit">1</span></td>
          <td><span class="ct-02__highlight">Up to 10</span></td>
          <td><span class="ct-02__limit">Unlimited</span></td>
        </tr>
        <tr>
          <td>Custom Integrations</td>
          <td><span class="ct-02__x">✕</span></td>
          <td><span class="ct-02__check">✓</span></td>
          <td><span class="ct-02__check">✓</span></td>
        </tr>
        <tr>
          <td>Priority Support</td>
          <td><span class="ct-02__x">✕</span></td>
          <td><span class="ct-02__check">✓</span></td>
          <td><span class="ct-02__check">✓</span></td>
        </tr>
        <tr>
          <td>SLA Guarantee</td>
          <td><span class="ct-02__x">✕</span></td>
          <td><span class="ct-02__x">✕</span></td>
          <td><span class="ct-02__check">✓ 99.99%</span></td>
        </tr>
        <tr>
          <td>Analytics Dashboard</td>
          <td><span class="ct-02__limit">Basic</span></td>
          <td><span class="ct-02__highlight">Advanced</span></td>
          <td><span class="ct-02__limit">Custom</span></td>
        </tr>
        <tr class="ct-02__cta-row">
          <td></td>
          <td><button class="ct-02__cta ct-02__cta--basic">Start Free</button></td>
          <td><button class="ct-02__cta ct-02__cta--pro">Get Pro →</button></td>
          <td><button class="ct-02__cta ct-02__cta--ent">Contact Us</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```
## CSS
```css
.ct-02,
.ct-02 *,
.ct-02 *::before,
.ct-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-02 ::selection {
  background: #a855f7;
  color: #fff;
}

.ct-02 {
  --bg: #06060f;
  --card: #10101e;
  --border: #1e1e3a;
  --text: #e8e8f8;
  --muted: #6b6b8e;
  --pro-glow: #a855f7;
  --pro2: #06b6d4;
  --basic: #3b82f6;
  --ent: #f59e0b;
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  padding: 36px 24px;
  min-height: 100vh;
  color: var(--text);
}

.ct-02__eyebrow {
  text-align: center;
  margin-bottom: 32px;
}

.ct-02__label {
  display: inline-block;
  background: linear-gradient(90deg, rgba(168,85,247,0.2), rgba(6,182,212,0.2));
  border: 1px solid rgba(168,85,247,0.3);
  border-radius: 20px;
  padding: 4px 16px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--pro-glow);
  margin-bottom: 10px;
}

.ct-02__heading {
  font-size: 24px;
  font-weight: 800;
}

.ct-02__sub {
  font-size: 14px;
  color: var(--muted);
  margin-top: 4px;
}

.ct-02__wrap {
  overflow-x: auto;
  border-radius: 16px;
}

.ct-02 table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  min-width: 540px;
}
/* COLUMN GROUPS */

.ct-02 col.basic {
  background: transparent;
}

.ct-02 col.pro {
  background: rgba(168,85,247,0.06);
}

.ct-02 col.ent {
  background: transparent;
}
/* HEADER ROW */

.ct-02 thead tr {
  border: none;
}

.ct-02 thead th {
  padding: 0;
  vertical-align: top;
}

.ct-02 thead th:first-child {
  width: 38%;
}
/* Hide the border-bottom on the empty top-left corner cell — it has
   no plan content, so the divider line below it reads as a stray
   horizontal mark above "AI Requests / month". Stripe / Linear /
   Vercel pricing tables all leave the top-left corner borderless. */

.ct-02 thead th:first-child .ct-02__plan-cell {
  border-bottom: none;
}

.ct-02__plan-cell {
  padding: 24px 20px;
  border-radius: 0;
  border-bottom: 2px solid var(--border);
  position: relative;
}

.ct-02__plan-cell--pro {
  background: linear-gradient(180deg, rgba(168,85,247,0.15), rgba(6,182,212,0.08));
  border-bottom: 2px solid var(--pro-glow);
  border-top: 3px solid var(--pro-glow);
  border-left: 1px solid rgba(168,85,247,0.3);
  border-right: 1px solid rgba(168,85,247,0.3);
}

.ct-02__badge {
  display: inline-block;
  background: linear-gradient(90deg, var(--pro-glow), var(--pro2));
  color: #fff;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 3px 9px;
  border-radius: 20px;
  margin-bottom: 8px;
  animation: ct-02-shimmer 3s ease-in-out infinite;
}

@keyframes ct-02-shimmer {
  0%,
    100% {
    box-shadow: 0 0 8px rgba(168,85,247,0.5);
  }

  50% {
    box-shadow: 0 0 20px rgba(168,85,247,0.9), 0 0 40px rgba(6,182,212,0.4);
  }
}

.ct-02__plan-name {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 6px;
}

.ct-02__price {
  font-size: 28px;
  font-weight: 900;
}

.ct-02__price span {
  font-size: 13px;
  font-weight: 400;
  color: var(--muted);
}

.ct-02__per {
  font-size: 12px;
  color: var(--muted);
}

.ct-02__plan-name--basic {
  color: var(--basic);
}

.ct-02__plan-name--pro {
  color: var(--pro-glow);
}

.ct-02__plan-name--ent {
  color: var(--ent);
}
/* FEATURE ROWS */

.ct-02 tbody tr {
  border: none;
}

.ct-02 tbody tr:hover td {
  background: rgba(255,255,255,0.02) !important;
}

.ct-02 tbody td {
  padding: 14px 20px;
  border-bottom: 1px solid var(--border);
  font-size: 13px;
  vertical-align: middle;
  transition: background 0.2s;
}

.ct-02 tbody td:first-child {
  color: var(--muted);
  font-size: 13px;
  font-weight: 500;
}

.ct-02 tbody td:nth-child(3) {
  border-left: 1px solid rgba(168,85,247,0.2);
  border-right: 1px solid rgba(168,85,247,0.2);
  background: rgba(168,85,247,0.04);
}

.ct-02 tbody tr:last-child td {
  border-bottom: none;
  padding-bottom: 24px;
}

.ct-02__check {
  color: #22c55e;
  font-size: 16px;
  font-weight: 700;
}

.ct-02__x {
  color: #374151;
  font-size: 16px;
  font-weight: 700;
}

.ct-02__limit {
  font-size: 12px;
  color: var(--muted);
  font-weight: 500;
}

.ct-02__highlight {
  font-weight: 700;
  color: var(--pro-glow);
  font-size: 13px;
}
/* CTA BUTTONS inside table */

.ct-02__cta-row td {
  padding-top: 20px !important;
  padding-bottom: 28px !important;
  border-bottom: none !important;
  background: transparent !important;
}

.ct-02__cta {
  display: inline-block;
  padding: 10px 22px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
}

.ct-02__cta--basic {
  background: rgba(59,130,246,0.12);
  color: var(--basic);
  border: 1px solid rgba(59,130,246,0.3);
}

.ct-02__cta--basic:hover {
  background: var(--basic);
  color: #fff;
}

.ct-02__cta--pro {
  background: linear-gradient(90deg, var(--pro-glow), var(--pro2));
  color: #fff;
  box-shadow: 0 4px 20px rgba(168,85,247,0.4);
}

.ct-02__cta--pro:hover {
  box-shadow: 0 6px 28px rgba(168,85,247,0.7);
  transform: translateY(-1px);
}

.ct-02__cta--ent {
  background: rgba(245,158,11,0.12);
  color: var(--ent);
  border: 1px solid rgba(245,158,11,0.3);
}

.ct-02__cta--ent:hover {
  background: var(--ent);
  color: #000;
}

@media (prefers-reduced-motion: reduce) {
  .ct-02__badge,
    .ct-02__cta {
    animation: none;
    transition: none;
  }
}
```
