---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/brutalist-print/"
title: "Brutalist Print"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Print-zine pricing — black on cream, hard offset shadows, mono type, intentionally raw."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Print
Source: https://codefronts.com/layouts/css-pricing-sections/brutalist-print/

Print-zine pricing — black on cream, hard offset shadows, mono type, intentionally raw. Each plan card sits askew on a yellow grid; CTAs are big inverted blocks. The brutalist aesthetic that signals "no marketing fluff" — popular with indie hackers and OSS.
## HTML
```html
<section class="ps-09" aria-label="Pricing">
  <header class="ps-09__head">
    <span class="ps-09__eye">issue №07 · pricing</span>
    <h2>Three sizes. One product. Pick.</h2>
  </header>
  <div class="ps-09__grid">
    <article class="ps-09__card ps-09__r1">
      <div class="ps-09__row"><span>Plan</span><strong>Solo</strong></div>
      <div class="ps-09__row"><span>Cost</span><strong class="ps-09__pri">$8/mo</strong></div>
      <div class="ps-09__row"><span>Built for</span><strong>Indie devs</strong></div>
      <hr />
      <ul>
        <li>1 site, 1 admin</li>
        <li>5 GB storage</li>
        <li>Forum support</li>
      </ul>
      <a class="ps-09__cta" href="#solo">[ Buy Solo ]</a>
    </article>
    <article class="ps-09__card ps-09__r2 ps-09__pop">
      <span class="ps-09__stamp">★ POPULAR</span>
      <div class="ps-09__row"><span>Plan</span><strong>Studio</strong></div>
      <div class="ps-09__row"><span>Cost</span><strong class="ps-09__pri">$24/mo</strong></div>
      <div class="ps-09__row"><span>Built for</span><strong>Small studios</strong></div>
      <hr />
      <ul>
        <li>10 sites, 5 admins</li>
        <li>50 GB storage</li>
        <li>Email support</li>
        <li>Custom domain</li>
      </ul>
      <a class="ps-09__cta ps-09__cta-pri" href="#studio">[ Buy Studio ]</a>
    </article>
    <article class="ps-09__card ps-09__r3">
      <div class="ps-09__row"><span>Plan</span><strong>Shop</strong></div>
      <div class="ps-09__row"><span>Cost</span><strong class="ps-09__pri">$60/mo</strong></div>
      <div class="ps-09__row"><span>Built for</span><strong>Agencies</strong></div>
      <hr />
      <ul>
        <li>Unlimited sites</li>
        <li>500 GB storage</li>
        <li>Priority support</li>
        <li>White-label</li>
      </ul>
      <a class="ps-09__cta" href="#shop">[ Buy Shop ]</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-09 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: repeating-linear-gradient(0deg, transparent 0, transparent 23px, rgba(0,0,0,0.04) 23px, rgba(0,0,0,0.04) 24px), repeating-linear-gradient(90deg, transparent 0, transparent 23px, rgba(0,0,0,0.04) 23px, rgba(0,0,0,0.04) 24px), #f4eccc;
  color: #0e0e0e;
  font-family: 'JetBrains Mono', 'Courier New', monospace;
}

.ps-09__head {
  margin-bottom: clamp(24px, 4vw, 36px);
}

.ps-09__eye {
  display: inline-block;
  font-size: 11px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  padding: 4px 10px;
  background: #0e0e0e;
  color: #f4eccc;
  margin-bottom: 12px;
}

.ps-09__head h2 {
  font-size: clamp(28px, 5vw, 44px);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.1;
  margin: 0;
  text-transform: uppercase;
}

.ps-09__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
  max-width: 980px;
  margin: 0 auto;
}

.ps-09__card {
  position: relative;
  background: #f4eccc;
  border: 2px solid #0e0e0e;
  padding: 22px 20px 20px;
  box-shadow: 8px 8px 0 0 #0e0e0e;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.ps-09__card:hover {
  transform: translate(2px, 2px);
  box-shadow: 6px 6px 0 0 #0e0e0e;
}

.ps-09__r1 {
  transform: rotate(-1.2deg);
}

.ps-09__r2 {
  transform: rotate(0.8deg);
}

.ps-09__r3 {
  transform: rotate(-0.6deg);
}

.ps-09__pop {
  background: #facc15;
  border-color: #0e0e0e;
  box-shadow: 8px 8px 0 0 #0e0e0e;
}

.ps-09__stamp {
  position: absolute;
  top: -14px;
  right: -10px;
  background: #0e0e0e;
  color: #facc15;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  padding: 5px 12px;
  transform: rotate(4deg);
  text-transform: uppercase;
}

.ps-09__row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 12px;
  padding: 4px 0;
  border-bottom: 1px dotted rgba(0,0,0,0.25);
}

.ps-09__row span {
  text-transform: uppercase;
  opacity: 0.7;
  letter-spacing: 0.06em;
}

.ps-09__row strong {
  font-size: 14px;
  font-weight: 700;
}

.ps-09__pri {
  font-size: 22px !important;
  font-weight: 800 !important;
}

.ps-09__card hr {
  border: 0;
  border-top: 2px solid #0e0e0e;
  margin: 14px 0 12px;
}

.ps-09__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 18px;
  font-size: 12.5px;
  line-height: 1.7;
}

.ps-09__card ul li::before {
  content: '▸ ';
}

.ps-09__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  background: #f4eccc;
  color: #0e0e0e;
  border: 2px solid #0e0e0e;
  text-decoration: none;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transition: background 0.15s, color 0.15s;
}

.ps-09__cta-pri {
  background: #0e0e0e;
  color: #facc15;
}

.ps-09__cta:hover {
  background: #0e0e0e;
  color: #facc15;
}

.ps-09__cta-pri:hover {
  background: #facc15;
  color: #0e0e0e;
}

.ps-09__cta:focus-visible {
  outline: 3px solid #ff5e5e;
  outline-offset: 2px;
}

@media (max-width: 820px) {
  .ps-09__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
    gap: 32px;
  }

  .ps-09__r1,
    .ps-09__r2,
    .ps-09__r3 {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-09__card {
    transition: none;
  }

  .ps-09__card:hover {
    transform: none;
    box-shadow: 8px 8px 0 0 #0e0e0e;
  }

  .ps-09__r1,
    .ps-09__r2,
    .ps-09__r3 {
    transform: none;
  }
}
```
