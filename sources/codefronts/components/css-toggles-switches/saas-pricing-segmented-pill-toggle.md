---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/saas-pricing-segmented-pill-toggle/"
title: "SaaS Pricing Segmented Pill Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The Monthly / Annually switcher every pricing page needs: hidden radio buttons inside a single track, a background pill that glides behind the active label,…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Pricing Segmented Pill Toggle
Source: https://codefronts.com/components/css-toggles-switches/saas-pricing-segmented-pill-toggle/

The Monthly / Annually switcher every pricing page needs: hidden radio buttons inside a single track, a background pill that glides behind the active label, a 'save 20%' badge — and the price below live-swaps, all without a line of JavaScript.
## HTML
```html
<section class="tgl-07" aria-label="Pricing period toggle">
  <div class="tgl-07__card">
    <div class="tgl-07__seg" role="radiogroup" aria-label="Billing period">
      <input type="radio" name="tgl-07" id="tgl-07-m" class="tgl-07__r" checked>
      <input type="radio" name="tgl-07" id="tgl-07-y" class="tgl-07__r">
      <span class="tgl-07__pill" aria-hidden="true"></span>
      <label class="tgl-07__opt" for="tgl-07-m">Monthly</label>
      <label class="tgl-07__opt" for="tgl-07-y">Annually <em class="tgl-07__save">−20%</em></label>
    </div>
    <div class="tgl-07__price">
      <p class="tgl-07__p tgl-07__p--m"><b>$24</b><span>/mo · billed monthly</span></p>
      <p class="tgl-07__p tgl-07__p--y"><b>$19</b><span>/mo · billed yearly</span></p>
    </div>
    <p class="tgl-07__plan">Pro plan · unlimited projects</p>
  </div>
</section>
```
## CSS
```css
.tgl-07,
.tgl-07 *,
.tgl-07 *::before,
.tgl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-07 {
  --accent: oklch(0.55 0.18 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #f6f5fb;
}

.tgl-07__card {
  width: min(340px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 28px;
  box-shadow: 0 20px 50px -30px rgba(50,40,120,.45);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
}

.tgl-07__seg {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  background: #eeecf6;
  border-radius: 999px;
  padding: 4px;
}

.tgl-07__r {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.tgl-07__pill {
  position: absolute;
  top: 4px;
  left: 4px;
  width: calc(50% - 4px);
  height: calc(100% - 8px);
  border-radius: 999px;
  background: var(--accent);
  box-shadow: 0 4px 12px -4px color-mix(in oklab,var(--accent) 70%,transparent);
  transition: transform .35s cubic-bezier(.3,1,.35,1.05);
  z-index: 0;
}

.tgl-07__r:nth-of-type(2):checked ~ .tgl-07__pill {
  transform: translateX(100%);
}

.tgl-07__opt {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 10px 0;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 700;
  color: #6b6683;
  cursor: pointer;
  transition: color .25s;
}

.tgl-07__r:nth-of-type(1):checked ~ .tgl-07__opt:nth-of-type(1),
.tgl-07__r:nth-of-type(2):checked ~ .tgl-07__opt:nth-of-type(2) {
  color: #fff;
}

.tgl-07__save {
  font-style: normal;
  font-size: 11px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 999px;
  background: oklch(0.9 0.09 150);
  color: oklch(0.42 0.12 150);
}

.tgl-07__r:nth-of-type(2):checked ~ .tgl-07__opt:nth-of-type(2) .tgl-07__save {
  background: rgba(255,255,255,.25);
  color: #fff;
}

.tgl-07__price {
  position: relative;
  height: 56px;
  width: 100%;
}

.tgl-07__p {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 8px;
  transition: opacity .3s,transform .3s;
}

.tgl-07__p b {
  font-size: 40px;
  font-weight: 800;
  color: #221d3a;
  letter-spacing: -.02em;
}

.tgl-07__p span {
  font-size: 13px;
  color: #8a86a0;
}

.tgl-07__p--y {
  opacity: 0;
  transform: translateY(8px);
}

.tgl-07__card:has(.tgl-07__r:nth-of-type(2):checked) .tgl-07__p--m {
  opacity: 0;
  transform: translateY(-8px);
}

.tgl-07__card:has(.tgl-07__r:nth-of-type(2):checked) .tgl-07__p--y {
  opacity: 1;
  transform: translateY(0);
}

.tgl-07__r:nth-of-type(1):focus-visible ~ .tgl-07__opt:nth-of-type(1),
.tgl-07__r:nth-of-type(2):focus-visible ~ .tgl-07__opt:nth-of-type(2) {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.tgl-07__plan {
  font-size: 12.5px;
  color: #8a86a0;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-07__pill,
    .tgl-07__p {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hidden radios give native single-choice + arrow keys; a highlight pill slides behind the checked label and :has() swaps the live price. */
```
