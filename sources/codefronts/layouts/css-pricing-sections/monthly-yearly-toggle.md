---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/monthly-yearly-toggle/"
title: "Monthly Yearly Toggle"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A pure-CSS billing-cycle switch using two hidden radios + :has()."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Monthly Yearly Toggle
Source: https://codefronts.com/layouts/css-pricing-sections/monthly-yearly-toggle/

A pure-CSS billing-cycle switch using two hidden radios + :has(). No JavaScript — selecting Yearly swaps every visible price across all three tiers via sibling state. Teal gradient, save-20%-pill on the yearly option.
## HTML
```html
<section class="ps-04" aria-label="Pricing">
  <header class="ps-04__head">
    <h2>Pay how it suits you.</h2>
    <p>Switch billing — no contracts, no negotiation.</p>
    <fieldset class="ps-04__switch">
      <legend class="ps-04__sr">Billing cycle</legend>
      <input type="radio" name="ps-04__cycle" id="ps-04__m" checked />
      <label for="ps-04__m">Monthly</label>
      <input type="radio" name="ps-04__cycle" id="ps-04__y" />
      <label for="ps-04__y">Yearly <span class="ps-04__save">−20%</span></label>
      <span class="ps-04__thumb" aria-hidden="true"></span>
    </fieldset>
  </header>
  <div class="ps-04__grid">
    <article class="ps-04__card">
      <h3>Hobby</h3>
      <div class="ps-04__price">
        <span class="ps-04__m-amt">$0</span><span class="ps-04__y-amt">$0</span
        ><span class="ps-04__per">forever</span>
      </div>
      <ul>
        <li>1 site</li>
        <li>Public projects</li>
        <li>Community</li>
      </ul>
      <a class="ps-04__cta" href="#hobby">Start free</a>
    </article>
    <article class="ps-04__card ps-04__best">
      <span class="ps-04__badge">Best value</span>
      <h3>Studio</h3>
      <div class="ps-04__price">
        <span class="ps-04__m-amt">$19</span><span class="ps-04__y-amt">$15</span
        ><span class="ps-04__per">/ month</span>
      </div>
      <ul>
        <li>Unlimited sites</li>
        <li>Custom domains</li>
        <li>Email support</li>
        <li>Form submissions</li>
      </ul>
      <a class="ps-04__cta ps-04__cta-pri" href="#studio">Start trial</a>
    </article>
    <article class="ps-04__card">
      <h3>Agency</h3>
      <div class="ps-04__price">
        <span class="ps-04__m-amt">$59</span><span class="ps-04__y-amt">$47</span
        ><span class="ps-04__per">/ month</span>
      </div>
      <ul>
        <li>Everything in Studio</li>
        <li>Client billing</li>
        <li>Workspace switcher</li>
        <li>Priority support</li>
      </ul>
      <a class="ps-04__cta" href="#agency">Choose Agency</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-04 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #062021;
  color: #e0fafa;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-04__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 40px);
}

.ps-04__head h2 {
  font-size: clamp(22px, 3.4vw, 34px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  background: linear-gradient(90deg, #14b8a6, #5eead4);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ps-04__head p {
  color: #7ea7a4;
  margin: 0 0 22px;
  font-size: 14px;
}

.ps-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.ps-04__switch {
  position: relative;
  display: inline-grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  padding: 4px;
  background: #0d2f30;
  border: 1px solid rgba(94,234,212,0.18);
  border-radius: 999px;
  margin: 0;
}

.ps-04__switch input[type="radio"] {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ps-04__switch input:focus-visible + label {
  outline: 2px solid #5eead4;
  outline-offset: 3px;
}

.ps-04__switch label {
  position: relative;
  z-index: 1;
  padding: 8px 22px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  color: #7ea7a4;
  border-radius: 999px;
  transition: color 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}

.ps-04__save {
  font-size: 10px;
  font-weight: 700;
  background: rgba(94,234,212,0.18);
  color: #5eead4;
  padding: 2px 6px;
  border-radius: 6px;
}

.ps-04__thumb {
  position: absolute;
  top: 4px;
  left: 4px;
  width: calc(50% - 4px);
  height: calc(100% - 8px);
  background: linear-gradient(135deg, #14b8a6, #5eead4);
  border-radius: 999px;
  transition: transform 0.28s cubic-bezier(.4,0,.2,1);
  z-index: 0;
  box-shadow: 0 4px 14px rgba(20,184,166,0.3);
}

.ps-04__switch:has(#ps-04__y:checked) .ps-04__thumb {
  transform: translateX(100%);
}

.ps-04__switch:has(#ps-04__m:checked) label[for="ps-04__m"],
.ps-04__switch:has(#ps-04__y:checked) label[for="ps-04__y"] {
  color: #062021;
}

.ps-04__switch:has(#ps-04__y:checked) .ps-04__save {
  background: rgba(6,32,33,0.25);
  color: #062021;
}

.ps-04__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  max-width: 980px;
  margin: 0 auto;
}

.ps-04__card {
  position: relative;
  background: #0d2f30;
  border: 1px solid rgba(94,234,212,0.15);
  border-radius: 14px;
  padding: 24px 22px 22px;
  display: flex;
  flex-direction: column;
}

.ps-04__best {
  border-color: #5eead4;
  box-shadow: 0 0 0 1px #5eead4 inset;
}

.ps-04__badge {
  position: absolute;
  top: -10px;
  right: 16px;
  background: #5eead4;
  color: #062021;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 6px;
}

.ps-04__card h3 {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin: 0 0 14px;
  color: #5eead4;
}

.ps-04__price {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin-bottom: 18px;
}

.ps-04__m-amt,
.ps-04__y-amt {
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #f0fff7;
}

.ps-04__per {
  font-size: 13px;
  color: #7ea7a4;
}

.ps-04:has(#ps-04__m:checked) .ps-04__y-amt {
  display: none;
}

.ps-04:has(#ps-04__y:checked) .ps-04__m-amt {
  display: none;
}

.ps-04__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 22px;
  flex: 1;
  font-size: 13.5px;
  line-height: 2;
  color: #c8eaea;
}

.ps-04__card ul li::before {
  content: '✓';
  color: #5eead4;
  font-weight: 700;
  display: inline-block;
  width: 20px;
}

.ps-04__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 8px;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  background: rgba(94,234,212,0.12);
  color: #5eead4;
  border: 1px solid rgba(94,234,212,0.25);
  transition: background 0.18s, color 0.18s;
}

.ps-04__cta-pri {
  background: #5eead4;
  color: #062021;
  border-color: #5eead4;
}

.ps-04__cta:hover {
  background: #5eead4;
  color: #062021;
}

.ps-04__cta:focus-visible {
  outline: 2px solid #5eead4;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-04__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-04__thumb {
    transition: none;
  }

  .ps-04__cta {
    transition: none;
  }

  .ps-04__switch label {
    transition: none;
  }
}
```
