---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-pricing-table-layout/"
title: "CSS Flexbox Pricing Table Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A three-tier pricing table with equal-height columns, a scaled featured plan, and flex-driven feature lists — all columns stretch to identical height without…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Pricing Table Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-pricing-table-layout/

A three-tier pricing table with equal-height columns, a scaled featured plan, and flex-driven feature lists — all columns stretch to identical height without JavaScript.
## HTML
```html
<div class="fl-07">
  <div class="fl-07__head">
    <div class="fl-07__eyebrow">Pricing</div>
    <h2 class="fl-07__title">Simple, Transparent Plans</h2>
    <div class="fl-07__toggle">
      <span>Monthly</span>
      <div class="fl-07__toggle-pill">Annual</div>
      <span class="fl-07__save-badge">Save 20%</span>
    </div>
  </div>

  <div class="fl-07__plans">

    <!-- Starter -->
    <div class="fl-07__plan">
      <div class="fl-07__plan-tag">Starter</div>
      <div class="fl-07__plan-name">Free</div>
      <div class="fl-07__plan-desc">Perfect for side projects and learning CSS flexbox layouts.</div>
      <div class="fl-07__price-row">
        <div class="fl-07__price-currency">$</div>
        <div class="fl-07__price-value">0</div>
        <div class="fl-07__price-period">/mo</div>
      </div>
      <div class="fl-07__price-annual">No credit card needed</div>
      <button class="fl-07__cta fl-07__cta--outline">Get started free</button>
      <div class="fl-07__divider"></div>
      <div class="fl-07__features">
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>3 projects
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Basic flex layouts
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Community support
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check fl-07__feature-check--muted">–</div><span style="opacity:0.4">Team collaboration</span>
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check fl-07__feature-check--muted">–</div><span style="opacity:0.4">Priority export</span>
        </div>
      </div>
    </div>

    <!-- Pro (featured) -->
    <div class="fl-07__plan fl-07__plan--featured">
      <div class="fl-07__plan-tag">Most Popular</div>
      <div class="fl-07__plan-name">Pro</div>
      <div class="fl-07__plan-desc">For professionals who need advanced layouts and team features.</div>
      <div class="fl-07__price-row">
        <div class="fl-07__price-currency">$</div>
        <div class="fl-07__price-value">29</div>
        <div class="fl-07__price-period">/mo</div>
      </div>
      <div class="fl-07__price-annual">Billed $279/yr — save $69</div>
      <button class="fl-07__cta fl-07__cta--primary">Start Pro trial</button>
      <div class="fl-07__divider"></div>
      <div class="fl-07__features">
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Unlimited projects
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>All flex layout patterns
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Priority support
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Team collaboration (5 seats)
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check fl-07__feature-check--muted">–</div><span style="opacity:0.4">White-label export</span>
        </div>
      </div>
    </div>

    <!-- Enterprise -->
    <div class="fl-07__plan">
      <div class="fl-07__plan-tag">Enterprise</div>
      <div class="fl-07__plan-name">Scale</div>
      <div class="fl-07__plan-desc">For large teams building complex flexbox design systems at scale.</div>
      <div class="fl-07__price-row">
        <div class="fl-07__price-currency">$</div>
        <div class="fl-07__price-value">99</div>
        <div class="fl-07__price-period">/mo</div>
      </div>
      <div class="fl-07__price-annual">Billed $950/yr — save $238</div>
      <button class="fl-07__cta fl-07__cta--outline">Contact sales</button>
      <div class="fl-07__divider"></div>
      <div class="fl-07__features">
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Unlimited everything
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Custom flex components
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Dedicated support
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>Unlimited team seats
        </div>
        <div class="fl-07__feature">
          <div class="fl-07__feature-check">✓</div>White-label export
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.fl-07,
.fl-07 *,
.fl-07 *::before,
.fl-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-07 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.fl-07 {
  --bg: #f0f9ff;
  --surface: #fff;
  --ink: #0c1a2e;
  --muted: #64748b;
  --accent: #0ea5e9;
  --accent-dark: #0284c7;
  --featured: #0f172a;
  --border: rgba(14,165,233,0.15);
  --check: #22c55e;
  font-family: 'Nunito', sans-serif;
  background: var(--bg);
  padding: 28px 20px;
  border-radius: 16px;
  min-height: 500px;
}

.fl-07__head {
  text-align: center;
  margin-bottom: 24px;
}

.fl-07__eyebrow {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.fl-07__title {
  font-size: 1.4rem;
  font-weight: 900;
  color: var(--ink);
  margin-bottom: 6px;
}

.fl-07__toggle {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(14,165,233,0.08);
  border-radius: 20px;
  padding: 4px 8px;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--muted);
  cursor: pointer;
}

.fl-07__toggle-pill {
  background: var(--accent);
  color: #fff;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.72rem;
}

.fl-07__save-badge {
  background: #dcfce7;
  color: #16a34a;
  font-size: 0.65rem;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 6px;
}
/* Pricing row: flex with stretch alignment so cards equal height */

.fl-07__plans {
  display: flex;
  gap: 16px;
  align-items: stretch;
}

.fl-07__plan {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  gap: 0;
  transition: box-shadow 0.2s;
}

.fl-07__plan:hover {
  box-shadow: 0 10px 40px rgba(14,165,233,0.1);
}

.fl-07__plan--featured {
  background: var(--featured);
  border-color: var(--accent);
  box-shadow: 0 0 0 2px var(--accent), 0 20px 60px rgba(14,165,233,0.2);
  position: relative;
  transform: scale(1.03);
  z-index: 1;
}

.fl-07__plan-tag {
  display: inline-block;
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  margin-bottom: 12px;
  align-self: flex-start;
}

.fl-07__plan--featured .fl-07__plan-tag {
  background: var(--accent);
  color: #fff;
}

.fl-07__plan:not(.fl-07__plan--featured) .fl-07__plan-tag {
  background: rgba(14,165,233,0.1);
  color: var(--accent);
}

.fl-07__plan-name {
  font-size: 1rem;
  font-weight: 900;
  color: var(--ink);
  margin-bottom: 4px;
}

.fl-07__plan--featured .fl-07__plan-name {
  color: #fff;
}

.fl-07__plan-desc {
  font-size: 0.75rem;
  color: var(--muted);
  margin-bottom: 16px;
  line-height: 1.5;
}

.fl-07__plan--featured .fl-07__plan-desc {
  color: rgba(255,255,255,0.55);
}

.fl-07__price-row {
  display: flex;
  align-items: baseline;
  gap: 2px;
  margin-bottom: 4px;
}

.fl-07__price-currency {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--ink);
  align-self: flex-start;
  padding-top: 4px;
}

.fl-07__plan--featured .fl-07__price-currency {
  color: #fff;
}

.fl-07__price-value {
  font-size: 2.4rem;
  font-weight: 900;
  color: var(--ink);
  line-height: 1;
}

.fl-07__plan--featured .fl-07__price-value {
  color: #fff;
}

.fl-07__price-period {
  font-size: 0.78rem;
  color: var(--muted);
  padding-bottom: 4px;
}

.fl-07__plan--featured .fl-07__price-period {
  color: rgba(255,255,255,0.45);
}

.fl-07__price-annual {
  font-size: 0.7rem;
  color: var(--muted);
  margin-bottom: 20px;
}

.fl-07__plan--featured .fl-07__price-annual {
  color: rgba(255,255,255,0.4);
}

.fl-07__cta {
  padding: 10px;
  border-radius: 10px;
  font-family: 'Nunito', sans-serif;
  font-size: 0.85rem;
  font-weight: 800;
  cursor: pointer;
  text-align: center;
  margin-bottom: 20px;
  transition: all 0.2s;
  border: none;
}

.fl-07__cta--outline {
  background: transparent;
  border: 2px solid var(--border);
  color: var(--ink);
}

.fl-07__cta--outline:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.fl-07__cta--primary {
  background: var(--accent);
  color: #fff;
}

.fl-07__cta--primary:hover {
  background: var(--accent-dark);
}

.fl-07__divider {
  height: 1px;
  background: var(--border);
  margin-bottom: 16px;
}

.fl-07__plan--featured .fl-07__divider {
  background: rgba(255,255,255,0.1);
}

.fl-07__features {
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.fl-07__feature {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.78rem;
  color: var(--muted);
  line-height: 1.4;
}

.fl-07__plan--featured .fl-07__feature {
  color: rgba(255,255,255,0.65);
}

.fl-07__feature-check {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: rgba(34,197,94,0.15);
  color: var(--check);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.6rem;
  font-weight: 800;
  flex-shrink: 0;
  margin-top: 1px;
}

.fl-07__feature-check--muted {
  background: rgba(100,116,139,0.1);
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fl-07__plan,
    .fl-07__cta {
    transition: none;
  }
}
```
