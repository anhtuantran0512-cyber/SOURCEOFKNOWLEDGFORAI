---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/currency-switcher/"
title: "Currency Switcher"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A pure-CSS currency switcher (USD / EUR / GBP) using hidden radios + :has() to swap every visible price across all three tiers."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Currency Switcher
Source: https://codefronts.com/layouts/css-pricing-sections/currency-switcher/

A pure-CSS currency switcher (USD / EUR / GBP) using hidden radios + :has() to swap every visible price across all three tiers. Burgundy on cream — the wine-merchant / boutique-software aesthetic.
## HTML
```html
<section class="ps-17" aria-label="Pricing">
  <header class="ps-17__head">
    <h2>Pricing in your currency.</h2>
    <p>Pay where you live, with the rate fixed at billing time.</p>
    <fieldset class="ps-17__tabs">
      <legend class="ps-17__sr">Currency</legend>
      <input type="radio" name="ps-17__c" id="ps-17__usd" checked />
      <label for="ps-17__usd">USD</label>
      <input type="radio" name="ps-17__c" id="ps-17__eur" />
      <label for="ps-17__eur">EUR</label>
      <input type="radio" name="ps-17__c" id="ps-17__gbp" />
      <label for="ps-17__gbp">GBP</label>
    </fieldset>
  </header>
  <div class="ps-17__grid">
    <article class="ps-17__card">
      <h3>Petit</h3>
      <div class="ps-17__price">
        <span class="ps-17__usd">$12</span><span class="ps-17__eur">€11</span
        ><span class="ps-17__gbp">£10</span>
        <em>/month</em>
      </div>
      <ul>
        <li>Solo cellar</li>
        <li>3 bottles tracked</li>
        <li>Email reminders</li>
      </ul>
      <a class="ps-17__cta" href="#petit">Choose Petit</a>
    </article>
    <article class="ps-17__card ps-17__best">
      <span class="ps-17__pill">Sommelier’s pick</span>
      <h3>Reserve</h3>
      <div class="ps-17__price">
        <span class="ps-17__usd">$36</span><span class="ps-17__eur">€33</span
        ><span class="ps-17__gbp">£28</span>
        <em>/month</em>
      </div>
      <ul>
        <li>Full cellar</li>
        <li>Unlimited bottles</li>
        <li>Tasting notes</li>
        <li>Pairing engine</li>
      </ul>
      <a class="ps-17__cta ps-17__cta-pri" href="#reserve">Choose Reserve</a>
    </article>
    <article class="ps-17__card">
      <h3>Grand Cru</h3>
      <div class="ps-17__price">
        <span class="ps-17__usd">$96</span><span class="ps-17__eur">€88</span
        ><span class="ps-17__gbp">£76</span>
        <em>/month</em>
      </div>
      <ul>
        <li>Multi-cellar</li>
        <li>Insurance valuation</li>
        <li>White-glove setup</li>
      </ul>
      <a class="ps-17__cta" href="#grand">Talk to us</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-17 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #faf6ee;
  color: #2a0a14;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-17__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 36px);
}

.ps-17__head h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(26px, 4vw, 38px);
  font-weight: 700;
  letter-spacing: -0.015em;
  margin: 0 0 8px;
  color: #6b1224;
}

.ps-17__head p {
  color: #8a4555;
  margin: 0 0 20px;
  font-size: 14px;
}

.ps-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  border: 0;
}

.ps-17__tabs {
  position: relative;
  display: inline-grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0;
  border: 1.5px solid #6b1224;
  border-radius: 999px;
  padding: 3px;
  background: #fff;
  margin: 0;
}

.ps-17__tabs input[type="radio"] {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ps-17__tabs label {
  padding: 7px 22px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #8a4555;
  cursor: pointer;
  border-radius: 999px;
  transition: color 0.18s, background 0.18s;
}

.ps-17__tabs input:checked + label {
  background: #6b1224;
  color: #faf6ee;
}

.ps-17__tabs input:focus-visible + label {
  outline: 2px solid #6b1224;
  outline-offset: 3px;
}

.ps-17__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  max-width: 1000px;
  margin: 0 auto;
  align-items: center;
}

.ps-17__card {
  position: relative;
  background: #fff;
  border: 1px solid #e7d8c8;
  border-radius: 8px;
  padding: 26px 22px 22px;
  display: flex;
  flex-direction: column;
}

.ps-17__best {
  background: #6b1224;
  color: #faf6ee;
  border: 0;
  transform: scale(1.04);
  box-shadow: 0 18px 44px rgba(107,18,36,0.3);
}

.ps-17__pill {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: #faf6ee;
  color: #6b1224;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 4px 11px;
  border: 1.5px solid #6b1224;
  border-radius: 999px;
}

.ps-17__card h3 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 22px;
  font-weight: 700;
  margin: 0 0 12px;
  color: #6b1224;
  font-style: italic;
}

.ps-17__best h3 {
  color: #faf6ee;
}

.ps-17__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  margin-bottom: 18px;
  padding-bottom: 18px;
  border-bottom: 1px dashed #e7d8c8;
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.03em;
}

.ps-17__best .ps-17__price {
  border-bottom-color: rgba(250,246,238,0.25);
}

.ps-17__price em {
  font-size: 13px;
  font-weight: 500;
  color: #8a4555;
  font-style: normal;
  margin-left: 6px;
}

.ps-17__best .ps-17__price em {
  color: rgba(250,246,238,0.7);
}

.ps-17__price > span {
  display: none;
}

.ps-17:has(#ps-17__usd:checked) .ps-17__usd,
.ps-17:has(#ps-17__eur:checked) .ps-17__eur,
.ps-17:has(#ps-17__gbp:checked) .ps-17__gbp {
  display: inline;
}

.ps-17__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 20px;
  flex: 1;
  font-size: 13.5px;
  line-height: 1.95;
  color: #4a2030;
}

.ps-17__best ul {
  color: rgba(250,246,238,0.85);
}

.ps-17__card ul li::before {
  content: '◆';
  color: #6b1224;
  display: inline-block;
  width: 20px;
  font-size: 9px;
}

.ps-17__best ul li::before {
  color: #faf6ee;
}

.ps-17__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 6px;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  border: 1.5px solid currentColor;
  color: #6b1224;
  background: transparent;
  transition: background 0.18s, color 0.18s;
}

.ps-17__best .ps-17__cta {
  color: #faf6ee;
}

.ps-17__cta-pri {
  background: #faf6ee;
  color: #6b1224 !important;
  border-color: #faf6ee;
}

.ps-17__cta:hover {
  background: #6b1224;
  color: #faf6ee;
  border-color: #6b1224;
}

.ps-17__cta-pri:hover {
  background: transparent;
  color: #faf6ee !important;
  border-color: #faf6ee;
}

.ps-17__cta:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-17__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
  }

  .ps-17__best {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-17__tabs label,
    .ps-17__cta {
    transition: none;
  }
}
```
