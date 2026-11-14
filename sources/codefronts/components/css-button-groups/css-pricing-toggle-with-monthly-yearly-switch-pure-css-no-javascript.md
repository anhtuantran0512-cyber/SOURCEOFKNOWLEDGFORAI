---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-pricing-toggle-with-monthly-yearly-switch-pure-css-no-javascript/"
title: "CSS Pricing Toggle with Monthly / Yearly Switch (Pure CSS, No JavaScript)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "The SaaS pricing-page staple: a two-option billing switch where flipping between Monthly and Yearly slides a thumb across the track AND swaps every price on…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pricing Toggle with Monthly / Yearly Switch (Pure CSS, No JavaScript)
Source: https://codefronts.com/components/css-button-groups/css-pricing-toggle-with-monthly-yearly-switch-pure-css-no-javascript/

The SaaS pricing-page staple: a two-option billing switch where flipping between Monthly and Yearly slides a thumb across the track AND swaps every price on the card — the exact 'CSS pricing toggle monthly yearly switch without JavaScript' pattern product teams in the US, UK, Canada and Australia ship on landing pages. Real radio inputs, keyboard-operable, screen-reader friendly.
## HTML
```html
<section class="btn-04" aria-label="Monthly yearly pricing toggle demo">
  <div class="btn-04__card">
    <div class="btn-04__toggle" role="group" aria-label="Billing period">
      <div class="btn-04__track">
        <input type="radio" name="btn-04" id="btn-04-m" class="btn-04__in" checked>
        <label for="btn-04-m" class="btn-04__opt">Monthly</label>
        <input type="radio" name="btn-04" id="btn-04-y" class="btn-04__in">
        <label for="btn-04-y" class="btn-04__opt">Yearly <span class="btn-04__save">Save 20%</span></label>
        <span class="btn-04__thumb" aria-hidden="true"></span>
      </div>
    </div>
    <div class="btn-04__plans">
      <div class="btn-04__plan">
        <p class="btn-04__name">Starter</p>
        <p class="btn-04__price" aria-live="polite"><span class="btn-04__mo"><b>$12</b>/mo</span><span class="btn-04__yr"><b>$115</b>/yr</span></p>
        <p class="btn-04__note">Billed per seat, cancel anytime.</p>
      </div>
      <div class="btn-04__plan btn-04__plan--hot">
        <p class="btn-04__name">Studio</p>
        <p class="btn-04__price" aria-live="polite"><span class="btn-04__mo"><b>$29</b>/mo</span><span class="btn-04__yr"><b>$278</b>/yr</span></p>
        <p class="btn-04__note">Everything in Starter, unlimited projects.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-04,
.btn-04 *,
.btn-04 *::before,
.btn-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-04 {
  --accent: oklch(0.66 0.15 195);
  --ink: #0d2b2e;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 0%,#eafaf6,#d6efe9);
  padding: 44px 20px;
}

.btn-04__card {
  width: min(560px,100%);
  background: #fff;
  border-radius: 24px;
  padding: 32px 30px 34px;
  box-shadow: 0 30px 70px -40px rgba(6,60,58,.5);
}

.btn-04__toggle {
  display: flex;
  justify-content: center;
  margin-bottom: 26px;
}

.btn-04__track {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px;
  padding: 5px;
  background: #e4f1ee;
  border-radius: 999px;
}

.btn-04__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-04__opt {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 22px;
  border-radius: 999px;
  font-size: 15px;
  font-weight: 650;
  color: #4a6b68;
  cursor: pointer;
  transition: color .25s;
  white-space: nowrap;
}

.btn-04__save {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .02em;
  color: var(--accent);
  background: #fff;
  padding: 3px 8px;
  border-radius: 999px;
}

.btn-04__thumb {
  position: absolute;
  z-index: 0;
  top: 5px;
  left: 5px;
  width: calc(50% - 7px);
  height: calc(100% - 10px);
  background: var(--ink);
  border-radius: 999px;
  transition: translate .35s cubic-bezier(.4,0,.2,1);
  box-shadow: 0 6px 16px -6px rgba(6,60,58,.7);
}

.btn-04__track:has(#btn-04-y:checked) .btn-04__thumb {
  translate: calc(100% + 2px) 0;
}

.btn-04__track:has(#btn-04-m:checked) label[for=btn-04-m],
.btn-04__track:has(#btn-04-y:checked) label[for=btn-04-y] {
  color: #fff;
}

.btn-04__track:has(#btn-04-y:checked) label[for=btn-04-y] .btn-04__save {
  color: var(--ink);
}

.btn-04__in:focus-visible + .btn-04__opt {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.btn-04__plans {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.btn-04__plan {
  border: 1.5px solid #e2eeeb;
  border-radius: 16px;
  padding: 20px 18px;
}

.btn-04__plan--hot {
  border-color: var(--accent);
  background: linear-gradient(180deg,#f3fbf9,#fff);
}

.btn-04__name {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
}

.btn-04__price {
  position: relative;
  height: 44px;
  margin: 8px 0 4px;
  color: var(--ink);
}

.btn-04__price span {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: baseline;
  font-size: 15px;
  color: #5b7a77;
  transition: opacity .3s;
}

.btn-04__price b {
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--ink);
  margin-right: 2px;
}

.btn-04__yr {
  opacity: 0;
}

.btn-04__card:has(#btn-04-y:checked) .btn-04__mo {
  opacity: 0;
}

.btn-04__card:has(#btn-04-y:checked) .btn-04__yr {
  opacity: 1;
}

.btn-04__note {
  font-size: 13px;
  line-height: 1.5;
  color: #7a938f;
}

@media (max-width: 520px) {
  .btn-04__plans {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .btn-04__thumb,
    .btn-04__price span,
    .btn-04__opt {
    transition: none;
  }
}
```
