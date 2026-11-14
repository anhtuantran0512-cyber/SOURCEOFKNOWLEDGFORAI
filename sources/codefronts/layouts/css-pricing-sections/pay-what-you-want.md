---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/pay-what-you-want/"
title: "Pay What You Want"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A pay-what-you-want layout with five preset chips ($5 / $10 / $25 / $50 / Custom) — selecting one updates the active state and the highlighted CTA via radio…"
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pay What You Want
Source: https://codefronts.com/layouts/css-pricing-sections/pay-what-you-want/

A pay-what-you-want layout with five preset chips ($5 / $10 / $25 / $50 / Custom) — selecting one updates the active state and the highlighted CTA via radio + :has(). Mint palette, the indie-product / crowdfunding pattern.
## HTML
```html
<section class="ps-16" aria-label="Pay what you want">
  <div class="ps-16__card">
    <header class="ps-16__head">
      <span class="ps-16__eye">Pay what you want</span>
      <h2>Support the project — <em>name your price.</em></h2>
      <p>
        The full product is yours regardless of the amount. Pay more if it helps, pay less if it’s
        tight. We trust you.
      </p>
    </header>
    <fieldset class="ps-16__amounts">
      <legend class="ps-16__sr">Choose an amount</legend>
      <input type="radio" name="ps-16" id="ps-16-5" />
      <label for="ps-16-5"><strong>$5</strong><span>Coffee</span></label>
      <input type="radio" name="ps-16" id="ps-16-10" checked />
      <label for="ps-16-10"><strong>$10</strong><span>Average</span></label>
      <input type="radio" name="ps-16" id="ps-16-25" />
      <label for="ps-16-25"><strong>$25</strong><span>Generous</span></label>
      <input type="radio" name="ps-16" id="ps-16-50" />
      <label for="ps-16-50"><strong>$50</strong><span>Sponsor</span></label>
      <input type="radio" name="ps-16" id="ps-16__x" />
      <label for="ps-16__x"><strong>Custom</strong><span>You decide</span></label>
    </fieldset>
    <ul class="ps-16__feats">
      <li>Lifetime access to the full product</li>
      <li>All future updates included</li>
      <li>Source files + commercial use rights</li>
    </ul>
    <a class="ps-16__cta" href="#pay">
      <span class="ps-16__cta-default">Pay $10 — get it now</span>
      <span class="ps-16__cta-5">Pay $5 — get it now</span>
      <span class="ps-16__cta-25">Pay $25 — get it now</span>
      <span class="ps-16__cta-50">Pay $50 — get it now</span>
      <span class="ps-16__cta-x">Enter custom amount →</span>
    </a>
    <p class="ps-16__foot">No questions asked refund inside 14 days. Powered by Stripe.</p>
  </div>
</section>
```
## CSS
```css
.ps-16 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(50% 50% at 50% 0%, rgba(45,212,191,0.16), transparent 60%), #06181a;
  color: #d4f5ee;
  font-family: 'Inter', system-ui, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ps-16__card {
  width: 100%;
  max-width: 560px;
  background: linear-gradient(180deg, #0d2326, #06181a);
  border: 1px solid rgba(45,212,191,0.3);
  border-radius: 18px;
  padding: clamp(26px, 4vw, 38px);
  box-shadow: 0 24px 60px rgba(45,212,191,0.12);
}

.ps-16__head {
  text-align: center;
  margin-bottom: 24px;
}

.ps-16__eye {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #5eead4;
  padding: 4px 12px;
  background: rgba(94,234,212,0.12);
  border-radius: 999px;
  margin-bottom: 14px;
}

.ps-16__head h2 {
  font-size: clamp(22px, 3.6vw, 30px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 10px;
  color: #fff;
}

.ps-16__head h2 em {
  color: #5eead4;
  font-style: italic;
}

.ps-16__head p {
  color: #92b8b1;
  font-size: 14px;
  line-height: 1.6;
  margin: 0 auto;
  max-width: 420px;
}

.ps-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  border: 0;
}

.ps-16__amounts {
  border: 0;
  padding: 0;
  margin: 0 0 20px;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
}

.ps-16__amounts input[type="radio"] {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ps-16__amounts label {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 14px 6px;
  background: rgba(94,234,212,0.06);
  border: 1.5px solid rgba(94,234,212,0.18);
  border-radius: 10px;
  cursor: pointer;
  transition: border-color 0.18s, background 0.18s, transform 0.18s;
  text-align: center;
  min-height: 64px;
}

.ps-16__amounts label strong {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -0.01em;
  color: #fff;
}

.ps-16__amounts label span {
  display: block;
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #5eead4;
  margin-top: 2px;
}

.ps-16__amounts label:hover {
  border-color: rgba(94,234,212,0.5);
  background: rgba(94,234,212,0.1);
}

.ps-16__amounts input:checked + label {
  background: linear-gradient(135deg, #2dd4bf, #5eead4);
  border-color: #5eead4;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(45,212,191,0.4);
}

.ps-16__amounts input:checked + label strong {
  color: #06181a;
}

.ps-16__amounts input:checked + label span {
  color: rgba(6,24,26,0.7);
}

.ps-16__amounts input:focus-visible + label {
  outline: 2px solid #5eead4;
  outline-offset: 3px;
}

.ps-16__feats {
  list-style: none;
  padding: 0;
  margin: 0 0 20px;
  font-size: 13px;
  line-height: 1.95;
  color: #b8d6cf;
}

.ps-16__feats li::before {
  content: '✓';
  color: #5eead4;
  display: inline-block;
  width: 22px;
  font-weight: 700;
}

.ps-16__cta {
  display: block;
  position: relative;
  text-align: center;
  padding: 14px 18px;
  border-radius: 10px;
  background: linear-gradient(135deg, #2dd4bf, #5eead4);
  color: #06181a;
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.01em;
  box-shadow: 0 10px 24px rgba(45,212,191,0.3);
  transition: transform 0.18s;
  margin-bottom: 12px;
}

.ps-16__cta:hover {
  transform: translateY(-1px);
}

.ps-16__cta:focus-visible {
  outline: 2px solid #5eead4;
  outline-offset: 3px;
}

.ps-16__cta span {
  display: none;
}

.ps-16__cta .ps-16__cta-default {
  display: block;
}

.ps-16:has(#ps-16-5:checked) .ps-16__cta-default,
.ps-16:has(#ps-16-25:checked) .ps-16__cta-default,
.ps-16:has(#ps-16-50:checked) .ps-16__cta-default,
.ps-16:has(#ps-16__x:checked) .ps-16__cta-default {
  display: none;
}

.ps-16:has(#ps-16-5:checked) .ps-16__cta-5 {
  display: block;
}

.ps-16:has(#ps-16-25:checked) .ps-16__cta-25 {
  display: block;
}

.ps-16:has(#ps-16-50:checked) .ps-16__cta-50 {
  display: block;
}

.ps-16:has(#ps-16__x:checked) .ps-16__cta-x {
  display: block;
}

.ps-16__foot {
  font-size: 11.5px;
  color: #6e8a85;
  text-align: center;
  margin: 0;
}

@media (max-width: 540px) {
  .ps-16__amounts {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-16__amounts label,
    .ps-16__cta {
    transition: none;
  }
}
```
