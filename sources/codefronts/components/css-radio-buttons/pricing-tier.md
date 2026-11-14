---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/pricing-tier/"
title: "Subscription Pricing Plan Cards"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "A complete pricing-table selector: three plan cards with price, feature list and a highlighted \"Recommended\" tier — each card a radio button, so the whole…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subscription Pricing Plan Cards
Source: https://codefronts.com/components/css-radio-buttons/pricing-tier/

A complete pricing-table selector: three plan cards with price, feature list and a highlighted "Recommended" tier — each card a radio button, so the whole table is one submittable form control. Checked card lifts with an accent crown bar; a live summary line below confirms the choice, pure CSS.
## HTML
```html
<div class="crb-17-group">
<section class="crb-17a" aria-label="Subscription pricing plan cards">
  <fieldset class="crb-17a__group">
    <legend class="crb-17a__legend">Pick your plan</legend>
    <div class="crb-17a__cards">
      <label class="crb-17a__card">
        <input class="crb-17a__input" type="radio" name="crb-17a" value="starter">
        <span class="crb-17a__name">Starter</span>
        <span class="crb-17a__price">$0<small>/mo</small></span>
        <ul class="crb-17a__feats"><li>3 projects</li><li>Community support</li><li>1 GB storage</li></ul>
        <span class="crb-17a__pill"><span class="crb-17a__pill-idle">Select</span><span class="crb-17a__pill-on">Selected ✓</span></span>
      </label>
      <label class="crb-17a__card crb-17a__card--reco">
        <input class="crb-17a__input" type="radio" name="crb-17a" value="pro" checked>
        <span class="crb-17a__crown">Recommended</span>
        <span class="crb-17a__name">Pro</span>
        <span class="crb-17a__price">$19<small>/mo</small></span>
        <ul class="crb-17a__feats"><li>Unlimited projects</li><li>Priority support</li><li>100 GB storage</li></ul>
        <span class="crb-17a__pill"><span class="crb-17a__pill-idle">Select</span><span class="crb-17a__pill-on">Selected ✓</span></span>
      </label>
      <label class="crb-17a__card">
        <input class="crb-17a__input" type="radio" name="crb-17a" value="team">
        <span class="crb-17a__name">Team</span>
        <span class="crb-17a__price">$49<small>/mo</small></span>
        <ul class="crb-17a__feats"><li>Everything in Pro</li><li>SSO &amp; audit log</li><li>Unlimited storage</li></ul>
        <span class="crb-17a__pill"><span class="crb-17a__pill-idle">Select</span><span class="crb-17a__pill-on">Selected ✓</span></span>
      </label>
    </div>
    <p class="crb-17a__sum"><span data-sum="starter">Starter — free forever, upgrade anytime.</span><span data-sum="pro">Pro — 14-day free trial, cancel anytime.</span><span data-sum="team">Team — includes onboarding for your whole org.</span></p>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-17-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-17-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-17a,
.crb-17a *,
.crb-17a *::before,
.crb-17a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-17a {
  --accent: oklch(0.55 0.2 262);
  --ink: #1c2130;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f4f5f9;
}

.crb-17a__group {
  border: none;
  display: grid;
  justify-items: center;
}

.crb-17a__legend {
  font-size: 26px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
  text-align: center;
}

.crb-17a__cards {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  justify-content: center;
  margin-top: 30px;
}

.crb-17a__card {
  position: relative;
  display: grid;
  align-content: start;
  gap: 6px;
  width: 230px;
  padding: 28px 22px 22px;
  background: #fff;
  border: 2px solid #e5e7f0;
  border-radius: 18px;
  cursor: pointer;
  box-shadow: 0 0 0 transparent;
  transition: border-color .25s,transform .25s,box-shadow .25s;
}

.crb-17a__card--reco {
  border-color: color-mix(in oklab,var(--accent) 35%,#e5e7f0);
}

.crb-17a__crown {
  position: absolute;
  top: -11px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .04em;
  padding: 3px 12px;
  border-radius: 9999px;
  background: var(--accent);
  color: #fff;
  white-space: nowrap;
}

.crb-17a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-17a__name {
  font-size: 15px;
  font-weight: 750;
  color: #6b7189;
  text-transform: uppercase;
  letter-spacing: .08em;
}

.crb-17a__price {
  font-size: 34px;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.03em;
}

.crb-17a__price small {
  font-size: 14px;
  font-weight: 600;
  color: #8a8fa3;
  letter-spacing: 0;
}

.crb-17a__feats {
  list-style: none;
  display: grid;
  gap: 7px;
  margin-top: 10px;
}

.crb-17a__feats li {
  font-size: 13.5px;
  color: #5d6378;
  padding-left: 20px;
  position: relative;
}

.crb-17a__feats li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 5px;
  width: 10px;
  height: 6px;
  border-left: 2px solid var(--accent);
  border-bottom: 2px solid var(--accent);
  transform: rotate(-45deg);
}

.crb-17a__pill {
  position: relative;
  display: grid;
  place-items: center;
  margin-top: 18px;
  min-height: 42px;
  border-radius: 10px;
  border: 1.5px solid #d7dae6;
  font-size: 14px;
  font-weight: 700;
  color: #555b70;
  overflow: hidden;
  transition: border-color .25s,background .25s,color .25s;
}

.crb-17a__pill-idle,
.crb-17a__pill-on {
  grid-area: 1/1;
  transition: opacity .25s,transform .25s;
}

.crb-17a__pill-on {
  opacity: 0;
  transform: translateY(6px);
  color: #fff;
}

.crb-17a__card:hover {
  border-color: color-mix(in oklab,var(--accent) 45%,#e5e7f0);
  transform: translateY(-2px);
}

.crb-17a__card:has(.crb-17a__input:checked) {
  border-color: var(--accent);
  transform: translateY(-4px);
  box-shadow: 0 22px 44px -20px color-mix(in oklab,var(--accent) 55%,transparent);
}

.crb-17a__card:has(.crb-17a__input:checked) .crb-17a__pill {
  background: var(--accent);
  border-color: var(--accent);
}

.crb-17a__card:has(.crb-17a__input:checked) .crb-17a__pill-idle {
  opacity: 0;
  transform: translateY(-6px);
}

.crb-17a__card:has(.crb-17a__input:checked) .crb-17a__pill-on {
  opacity: 1;
  transform: translateY(0);
}

.crb-17a__card:has(.crb-17a__input:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.crb-17a__sum {
  margin-top: 22px;
  font-size: 14px;
  color: #6b7189;
  min-height: 20px;
  text-align: center;
}

.crb-17a__sum span {
  display: none;
}

.crb-17a__group:has(.crb-17a__input[value="starter"]:checked) .crb-17a__sum [data-sum="starter"] {
  display: inline;
}

.crb-17a__group:has(.crb-17a__input[value="pro"]:checked) .crb-17a__sum [data-sum="pro"] {
  display: inline;
}

.crb-17a__group:has(.crb-17a__input[value="team"]:checked) .crb-17a__sum [data-sum="team"] {
  display: inline;
}

@media (prefers-reduced-motion: reduce) {
  .crb-17a__card,
    .crb-17a__pill,
    .crb-17a__pill-idle,
    .crb-17a__pill-on {
    transition: none;
  }

  .crb-17a__card:hover,
    .crb-17a__card:has(.crb-17a__input:checked) {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each pricing card is a radio label; :has() lifts the checked card, cross-fades the Select/Selected pill and switches the live summary sentence below the table. */
```
