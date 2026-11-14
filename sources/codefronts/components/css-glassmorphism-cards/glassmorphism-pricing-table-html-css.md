---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-pricing-table-html-css/"
title: "Glassmorphism Pricing Table HTML CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two production pricing patterns: a three-tier dark table where the featured plan gets a gradient ring, a lift and a glow, and a light single-plan card with a…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Pricing Table HTML CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-pricing-table-html-css/

Two production pricing patterns: a three-tier dark table where the featured plan gets a gradient ring, a lift and a glow, and a light single-plan card with a pure-CSS monthly / yearly billing toggle driven by :has() — no JavaScript anywhere.
## HTML
```html
<div class="glz-02-group">
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="glz-02a" aria-label="Glassmorphism pricing table demo">
  <div class="glz-02a__wrap">
    <h2 class="glz-02a__title">Simple, honest pricing</h2>
    <div class="glz-02a__grid">
      <article class="glz-02a__tier"><h3>Starter</h3><p class="glz-02a__price">$19<span>/mo</span></p><ul><li>3 projects</li><li>10 GB storage</li><li>Community support</li></ul><button type="button">Choose Starter</button></article>
      <article class="glz-02a__tier glz-02a__tier--pro"><span class="glz-02a__chip">Most popular</span><h3>Pro</h3><p class="glz-02a__price">$49<span>/mo</span></p><ul><li>Unlimited projects</li><li>1 TB storage</li><li>Priority support</li><li>Custom domains</li></ul><button type="button">Choose Pro</button></article>
      <article class="glz-02a__tier"><h3>Scale</h3><p class="glz-02a__price">$129<span>/mo</span></p><ul><li>Everything in Pro</li><li>SSO &amp; audit logs</li><li>Dedicated manager</li></ul><button type="button">Choose Scale</button></article>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="glz-02b" aria-label="Pricing card with CSS-only billing toggle">
  <article class="glz-02b__plan">
    <input type="checkbox" id="glz-02b-yr" class="glz-02b__check">
    <div class="glz-02b__head">
      <h3>Studio Plan</h3>
      <label class="glz-02b__toggle" for="glz-02b-yr"><span>Monthly</span><i aria-hidden="true"></i><span>Yearly</span></label>
    </div>
    <div class="glz-02b__prices" aria-live="polite">
      <p class="glz-02b__mo">$24<span>/month</span></p>
      <p class="glz-02b__yr">$19<span>/month, billed yearly</span></p>
    </div>
    <p class="glz-02b__save">2 months free on yearly</p>
    <ul class="glz-02b__list"><li>Unlimited boards</li><li>Version history</li><li>Guest reviewers</li><li>Export to PDF &amp; PNG</li></ul>
    <button type="button" class="glz-02b__cta">Start 14-day trial</button>
  </article>
</section>
</div>
```
## CSS
```css
.glz-02-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.glz-02-group > section {
  width: 100%;
}

.glz-02a,
.glz-02a *,
.glz-02a *::before,
.glz-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-02a {
  --vio: oklch(0.66 0.21 292);
  --teal: oklch(0.8 0.15 180);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  background: #0b0f1c;
  font-family: 'Sora',system-ui,sans-serif;
}

.glz-02a::before,
.glz-02a::after {
  content: "";
  position: absolute;
  width: 52vmin;
  height: 52vmin;
  border-radius: 50%;
  filter: blur(80px);
  opacity: .55;
}

.glz-02a::before {
  background: var(--vio);
  top: -10%;
  left: 6%;
}

.glz-02a::after {
  background: var(--teal);
  bottom: -14%;
  right: 4%;
}

.glz-02a__wrap {
  position: relative;
  z-index: 1;
  width: min(980px,100%);
}

.glz-02a__title {
  text-align: center;
  color: #eef1fb;
  font-size: clamp(24px,3.4vw,36px);
  font-weight: 700;
  letter-spacing: -.02em;
  margin-bottom: 38px;
}

.glz-02a__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(240px,1fr));
  gap: 20px;
  align-items: stretch;
}

.glz-02a__tier {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 30px 26px;
  border-radius: 22px;
  color: #dfe5f5;
  background: linear-gradient(160deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  border: 1px solid rgba(255,255,255,.16);
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.18);
  transition: transform .35s ease,box-shadow .35s ease;
}

.glz-02a__tier:hover {
  transform: translateY(-6px);
}

.glz-02a__tier--pro {
  border: 1.5px solid transparent;
  background: linear-gradient(rgba(17,22,40,.9),rgba(17,22,40,.9)) padding-box,linear-gradient(135deg,var(--vio),var(--teal)) border-box;
  transform: scale(1.04);
  box-shadow: 0 30px 70px -24px oklch(0.66 0.21 292/.55),inset 0 1px 0 rgba(255,255,255,.2);
}

.glz-02a__tier--pro:hover {
  transform: scale(1.04) translateY(-6px);
}

.glz-02a__chip {
  position: absolute;
  top: -13px;
  left: 50%;
  transform: translateX(-50%);
  white-space: nowrap;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #0b0f1c;
  padding: 6px 14px;
  border-radius: 99px;
  background: linear-gradient(90deg,oklch(0.82 0.14 292),var(--teal));
}

.glz-02a__tier h3 {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(223,229,245,.7);
}

.glz-02a__price {
  font-size: 44px;
  font-weight: 800;
  letter-spacing: -.03em;
  color: #fff;
}

.glz-02a__price span {
  font-size: 14px;
  font-weight: 400;
  color: rgba(223,229,245,.55);
  letter-spacing: 0;
}

.glz-02a__tier ul {
  list-style: none;
  display: grid;
  gap: 10px;
  font-size: 13.5px;
  color: rgba(223,229,245,.85);
}

.glz-02a__tier li::before {
  content: "";
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  margin-right: 10px;
  background: linear-gradient(135deg,var(--vio),var(--teal));
  vertical-align: 2px;
}

.glz-02a__tier button {
  margin-top: auto;
  padding: 13px 18px;
  border-radius: 13px;
  border: 1px solid rgba(255,255,255,.25);
  background: rgba(255,255,255,.08);
  color: #fff;
  font: 600 14px 'Sora',sans-serif;
  cursor: pointer;
  transition: background .25s ease,transform .2s ease;
}

.glz-02a__tier button:hover {
  background: rgba(255,255,255,.16);
  transform: translateY(-2px);
}

.glz-02a__tier--pro button {
  border: none;
  background: linear-gradient(90deg,var(--vio),var(--teal));
  color: #08101c;
}

.glz-02a__tier button:focus-visible {
  outline: 2px solid var(--teal);
  outline-offset: 3px;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-02a__tier {
    background: rgba(19,25,44,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-02a__tier,
    .glz-02a__tier button {
    transition: none;
  }
}

.glz-02b,
.glz-02b *,
.glz-02b *::before,
.glz-02b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-02b {
  --ink: #231c35;
  --acc: oklch(0.6 0.22 310);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 90% at 12% 8%,oklch(0.88 0.09 320),transparent 55%),radial-gradient(110% 90% at 90% 90%,oklch(0.87 0.1 200),transparent 55%),#f3f1f7;
  font-family: 'Sora',system-ui,sans-serif;
}

.glz-02b__plan {
  width: min(400px,100%);
  padding: 30px 30px 32px;
  border-radius: 26px;
  color: var(--ink);
  background: linear-gradient(150deg,rgba(255,255,255,.62),rgba(255,255,255,.3));
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid rgba(255,255,255,.8);
  box-shadow: 0 30px 60px -26px rgba(80,60,140,.45),inset 0 1px 0 rgba(255,255,255,.9);
}

.glz-02b__check {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.glz-02b__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.glz-02b__head h3 {
  font-size: 19px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.glz-02b__toggle {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 11.5px;
  font-weight: 600;
  color: rgba(35,28,53,.6);
  cursor: pointer;
  user-select: none;
}

.glz-02b__toggle i {
  width: 42px;
  height: 24px;
  border-radius: 99px;
  background: rgba(35,28,53,.15);
  position: relative;
  transition: background .3s ease;
}

.glz-02b__toggle i::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,.25);
  transition: translate .3s cubic-bezier(.3,1.4,.4,1);
}

.glz-02b__plan:has(.glz-02b__check:checked) .glz-02b__toggle i {
  background: var(--acc);
}

.glz-02b__plan:has(.glz-02b__check:checked) .glz-02b__toggle i::after {
  translate: 18px 0;
}

.glz-02b__plan:has(.glz-02b__check:focus-visible) .glz-02b__toggle i {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.glz-02b__prices {
  display: grid;
  margin-top: 22px;
}

.glz-02b__prices p {
  grid-area: 1/1;
  font-size: 46px;
  font-weight: 800;
  letter-spacing: -.035em;
  transition: opacity .35s ease,transform .35s ease;
}

.glz-02b__prices span {
  display: block;
  font-size: 13px;
  font-weight: 400;
  letter-spacing: 0;
  color: rgba(35,28,53,.55);
  margin-top: 2px;
}

.glz-02b__yr {
  opacity: 0;
  transform: translateY(10px);
}

.glz-02b__plan:has(.glz-02b__check:checked) .glz-02b__mo {
  opacity: 0;
  transform: translateY(-10px);
}

.glz-02b__plan:has(.glz-02b__check:checked) .glz-02b__yr {
  opacity: 1;
  transform: none;
}

.glz-02b__save {
  margin-top: 14px;
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: oklch(0.42 0.18 310);
  padding: 6px 12px;
  border-radius: 99px;
  background: oklch(0.9 0.08 310/.7);
  border: 1px solid oklch(0.8 0.1 310/.6);
  opacity: .45;
  transition: opacity .3s ease;
}

.glz-02b__plan:has(.glz-02b__check:checked) .glz-02b__save {
  opacity: 1;
}

.glz-02b__list {
  list-style: none;
  display: grid;
  gap: 10px;
  margin-top: 22px;
  font-size: 14px;
}

.glz-02b__list li::before {
  content: "✓";
  margin-right: 10px;
  font-weight: 800;
  color: var(--acc);
}

.glz-02b__cta {
  width: 100%;
  margin-top: 26px;
  padding: 15px;
  border: none;
  border-radius: 14px;
  background: linear-gradient(120deg,oklch(0.55 0.24 310),oklch(0.62 0.2 260));
  color: #fff;
  font: 700 15px 'Sora',sans-serif;
  cursor: pointer;
  box-shadow: 0 14px 30px -12px oklch(0.55 0.24 310/.7);
  transition: transform .2s ease,box-shadow .2s ease;
}

.glz-02b__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 36px -12px oklch(0.55 0.24 310/.8);
}

.glz-02b__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-02b__plan {
    background: rgba(255,255,255,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-02b__plan * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — the featured ring is a transparent border filled by a border-box gradient behind an opaque padding-box fill; hover lift is a transform. */

/* No JavaScript — a hidden checkbox + :has() flips the knob, cross-fades the two grid-stacked price blocks and lights the “2 months free” badge. */
```
