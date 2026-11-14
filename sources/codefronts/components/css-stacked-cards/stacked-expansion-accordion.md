---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/stacked-expansion-accordion/"
title: "Stacked Expansion Accordion"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A compact pile of cards resting on their bottom edges."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Expansion Accordion
Source: https://codefronts.com/components/css-stacked-cards/stacked-expansion-accordion/

A compact pile of cards resting on their bottom edges. Click any card and its body expands with a smooth grid animation, pushing the surrounding cards down to reveal product specs or technical detail — no JS, driven by hidden radios and CSS grid rows.
## HTML
```html
<section class="scd-04" aria-label="Stacked expansion accordion">
  <div class="scd-04__stack">
    <div class="scd-04__panel">
      <input type="radio" name="scd-04" id="scd-04-1" class="scd-04__radio" checked>
      <label class="scd-04__head" for="scd-04-1"><span class="scd-04__dot"></span>Dimensions &amp; weight<span class="scd-04__chev">›</span></label>
      <div class="scd-04__wrap"><div class="scd-04__body"><p>142 × 68 × 7.4 mm · 168 g. Aerospace-grade aluminium frame with a matte bead-blast finish.</p></div></div>
    </div>
    <div class="scd-04__panel">
      <input type="radio" name="scd-04" id="scd-04-2" class="scd-04__radio">
      <label class="scd-04__head" for="scd-04-2"><span class="scd-04__dot"></span>Display<span class="scd-04__chev">›</span></label>
      <div class="scd-04__wrap"><div class="scd-04__body"><p>6.3″ LTPO OLED, 1–120 Hz adaptive, 2600 nits peak, Dolby Vision, hardened glass.</p></div></div>
    </div>
    <div class="scd-04__panel">
      <input type="radio" name="scd-04" id="scd-04-3" class="scd-04__radio">
      <label class="scd-04__head" for="scd-04-3"><span class="scd-04__dot"></span>Battery &amp; charging<span class="scd-04__chev">›</span></label>
      <div class="scd-04__wrap"><div class="scd-04__body"><p>4,800 mAh · 80 W wired to 50% in 12 min · 30 W wireless · USB-C 3.2.</p></div></div>
    </div>
    <div class="scd-04__panel">
      <input type="radio" name="scd-04" id="scd-04-4" class="scd-04__radio">
      <label class="scd-04__head" for="scd-04-4"><span class="scd-04__dot"></span>In the box<span class="scd-04__chev">›</span></label>
      <div class="scd-04__wrap"><div class="scd-04__body"><p>Device, braided USB-C cable, SIM tool, quick-start guide. Adapter sold separately.</p></div></div>
    </div>
  </div>
</section>
```
## CSS
```css
.scd-04,
.scd-04 *,
.scd-04 *::before,
.scd-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-04 {
  --accent: oklch(0.6 0.16 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 50px 20px;
  background: #111319;
}

.scd-04__stack {
  width: min(440px,100%);
}

.scd-04__panel {
  background: #1c1f28;
  border: 1px solid #2a2e3a;
  border-radius: 16px;
  margin-top: -12px;
  box-shadow: 0 14px 30px -22px rgba(0,0,0,.8);
  transition: margin .35s,box-shadow .35s,border-color .35s;
  position: relative;
}

.scd-04__panel:first-child {
  margin-top: 0;
}

.scd-04__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.scd-04__head {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 18px 20px;
  cursor: pointer;
  color: #eef0f6;
  font-weight: 700;
  font-size: 15px;
}

.scd-04__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #3a4050;
  transition: background .3s;
}

.scd-04__chev {
  margin-left: auto;
  color: #5a6070;
  font-size: 22px;
  line-height: 1;
  transition: transform .3s,color .3s;
}

.scd-04__wrap {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .4s cubic-bezier(.3,.9,.3,1);
}

.scd-04__body {
  overflow: hidden;
}

.scd-04__body p {
  padding: 0 20px 20px;
  color: #aab0c0;
  font-size: 14px;
  line-height: 1.6;
}

.scd-04__radio:checked ~ .scd-04__wrap {
  grid-template-rows: 1fr;
}

.scd-04__radio:checked ~ .scd-04__head {
  color: #fff;
}

.scd-04__radio:checked ~ .scd-04__head .scd-04__dot {
  background: var(--accent);
}

.scd-04__radio:checked ~ .scd-04__head .scd-04__chev {
  transform: rotate(90deg);
  color: var(--accent);
}

.scd-04__panel:has(.scd-04__radio:checked) {
  margin-top: 14px;
  border-color: var(--accent);
  box-shadow: 0 22px 46px -26px rgba(60,80,220,.6);
  z-index: 2;
}

.scd-04__panel:first-child:has(.scd-04__radio:checked) {
  margin-top: 0;
}

.scd-04__radio:focus-visible ~ .scd-04__head {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
  border-radius: 16px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-04__panel,
    .scd-04__wrap,
    .scd-04__chev {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — radios drive a grid-template-rows 0fr→1fr reveal, and :has() lifts the open card clear of the stack. */
```
