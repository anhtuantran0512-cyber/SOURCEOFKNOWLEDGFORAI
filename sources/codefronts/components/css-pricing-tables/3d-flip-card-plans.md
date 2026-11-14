---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/3d-flip-card-plans/"
title: "3D Flip Card Plans"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Click \"View details\" and the entire pricing card rotates 180° in 3D space, revealing full specs and fine print on its back face — the flip runs on a hidden…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Card Plans
Source: https://codefronts.com/components/css-pricing-tables/3d-flip-card-plans/

Click "View details" and the entire pricing card rotates 180° in 3D space, revealing full specs and fine print on its back face — the flip runs on a hidden checkbox, so it's tappable, keyboard-toggleable and needs zero JavaScript.
## HTML
```html
<section class="prc-10" aria-label="Pricing cards that flip to show details">
  <div class="prc-10__grid">
    <div class="prc-10__scene">
      <input type="checkbox" id="prc-10-a" class="prc-10__sr">
      <div class="prc-10__inner">
        <article class="prc-10__face prc-10__front"><h3>Launch</h3><p class="prc-10__price">$25<small>/mo</small></p><p class="prc-10__blurb">For new stores finding their footing.</p><a href="#" class="prc-10__cta">Choose Launch</a><label for="prc-10-a" class="prc-10__flipbtn">View details ⟲</label></article>
        <article class="prc-10__face prc-10__back"><h4>Launch — details</h4><ul><li>1 staff account</li><li>2.9% + 30¢ per sale</li><li>Basic reports</li><li>14-day trial, cancel anytime</li></ul><label for="prc-10-a" class="prc-10__flipbtn">Back ⟲</label></article>
      </div>
    </div>
    <div class="prc-10__scene">
      <input type="checkbox" id="prc-10-b" class="prc-10__sr">
      <div class="prc-10__inner">
        <article class="prc-10__face prc-10__front prc-10__front--hot"><h3>Grow</h3><p class="prc-10__price">$65<small>/mo</small></p><p class="prc-10__blurb">For stores scaling past six figures.</p><a href="#" class="prc-10__cta prc-10__cta--hot">Choose Grow</a><label for="prc-10-b" class="prc-10__flipbtn">View details ⟲</label></article>
        <article class="prc-10__face prc-10__back"><h4>Grow — details</h4><ul><li>5 staff accounts</li><li>2.4% + 30¢ per sale</li><li>Advanced reports &amp; forecasts</li><li>Abandoned-cart recovery</li></ul><label for="prc-10-b" class="prc-10__flipbtn">Back ⟲</label></article>
      </div>
    </div>
    <div class="prc-10__scene">
      <input type="checkbox" id="prc-10-c" class="prc-10__sr">
      <div class="prc-10__inner">
        <article class="prc-10__face prc-10__front"><h3>Advanced</h3><p class="prc-10__price">$199<small>/mo</small></p><p class="prc-10__blurb">For high-volume, multi-region brands.</p><a href="#" class="prc-10__cta">Choose Advanced</a><label for="prc-10-c" class="prc-10__flipbtn">View details ⟲</label></article>
        <article class="prc-10__face prc-10__back"><h4>Advanced — details</h4><ul><li>15 staff accounts</li><li>1.9% + 30¢ per sale</li><li>Custom report builder</li><li>Duty &amp; tax calculators</li></ul><label for="prc-10-c" class="prc-10__flipbtn">Back ⟲</label></article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.prc-10,
.prc-10 *,
.prc-10 *::before,
.prc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-10 {
  --accent: oklch(0.6 0.17 230);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #eef2f6;
  color: #15202c;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
}

.prc-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-10__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: 20px;
  width: min(900px,100%);
}

.prc-10__scene {
  perspective: 1400px;
}

.prc-10__inner {
  display: grid;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.5,0,.2,1);
  height: 100%;
}

.prc-10__scene:has(.prc-10__sr:checked) .prc-10__inner {
  transform: rotateY(180deg);
}

.prc-10__face {
  grid-area: 1/1;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  background: #fff;
  border: 1px solid #dde4ec;
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  transition: visibility 0s .35s;
}

.prc-10__back {
  transform: rotateY(180deg);
  visibility: hidden;
  background: #15202c;
  color: #e8eef5;
  border-color: #15202c;
}

.prc-10__scene:has(.prc-10__sr:checked) .prc-10__front {
  visibility: hidden;
}

.prc-10__scene:has(.prc-10__sr:checked) .prc-10__back {
  visibility: visible;
}

.prc-10__front--hot {
  border-color: var(--accent);
  box-shadow: 0 16px 40px -24px oklch(0.6 0.17 230/.55);
}

.prc-10__face h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #67788c;
}

.prc-10__face h4 {
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 4px;
}

.prc-10__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-10__price small {
  font-size: 15px;
  font-weight: 600;
  color: #8795a8;
}

.prc-10__blurb {
  font-size: 13.5px;
  color: #5d6d80;
  line-height: 1.5;
  flex: 1;
}

.prc-10__back ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 13.5px;
  flex: 1;
}

.prc-10__back li::before {
  content: "•";
  color: var(--accent);
  margin-right: 9px;
}

.prc-10__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1.5px solid #dde4ec;
  color: #15202c;
  transition: border-color .2s;
}

.prc-10__cta:hover {
  border-color: var(--accent);
}

.prc-10__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-10__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-10__flipbtn {
  margin-top: 8px;
  text-align: center;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--accent);
  cursor: pointer;
  padding: 6px;
  border-radius: 8px;
}

.prc-10__flipbtn:hover {
  background: oklch(0.6 0.17 230/.1);
}

.prc-10__back .prc-10__flipbtn {
  color: oklch(0.75 0.12 230);
}

.prc-10__sr:focus-visible ~ .prc-10__inner {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
  border-radius: 18px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-10__inner {
    transition-duration: .01s;
  }

  .prc-10__face {
    transition-delay: 0s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hidden checkbox per card drives rotateY(180deg) on a preserve-3d wrapper via :has(); visibility swaps after the flip so keyboard focus can never land on the hidden face. */
```
