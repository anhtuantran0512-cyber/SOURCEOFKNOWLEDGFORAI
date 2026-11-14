---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/accordion-card/"
title: "Accordion Card"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A single standalone card holding several nested layers of content."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accordion Card
Source: https://codefronts.com/components/css-stacked-cards/accordion-card/

A single standalone card holding several nested layers of content. Click a layer's header and it expands while its neighbours smoothly compress within the card's fixed boundary — an all-in-one accordion that never grows the surrounding layout.
## HTML
```html
<section class="scd-21" aria-label="Single accordion card">
  <div class="scd-21__card">
    <div class="scd-21__sec">
      <input type="radio" name="scd-21" id="scd-21-1" class="scd-21__r" checked>
      <label class="scd-21__h" for="scd-21-1" style="--c:oklch(0.66 0.16 20)">Overview</label>
      <div class="scd-21__b"><p>A pocket knife of a component — three panels, one fixed card, zero layout shift.</p></div>
    </div>
    <div class="scd-21__sec">
      <input type="radio" name="scd-21" id="scd-21-2" class="scd-21__r">
      <label class="scd-21__h" for="scd-21-2" style="--c:oklch(0.68 0.15 150)">Features</label>
      <div class="scd-21__b"><p>Keyboard-navigable, reduced-motion aware, and copy-paste ready with scoped styles.</p></div>
    </div>
    <div class="scd-21__sec">
      <input type="radio" name="scd-21" id="scd-21-3" class="scd-21__r">
      <label class="scd-21__h" for="scd-21-3" style="--c:oklch(0.66 0.16 265)">Usage</label>
      <div class="scd-21__b"><p>Drop the markup in, keep the <code>.scd-21</code> scope, and swap the copy. Done.</p></div>
    </div>
  </div>
</section>
```
## CSS
```css
.scd-21,
.scd-21 *,
.scd-21 *::before,
.scd-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-21 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #101219;
}

.scd-21__card {
  width: min(360px,100%);
  height: 320px;
  display: flex;
  flex-direction: column;
  background: #1b1e28;
  border: 1px solid #2a2e3a;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 26px 54px -30px rgba(0,0,0,.8);
}

.scd-21__sec {
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  min-height: 0;
  transition: flex-grow .45s cubic-bezier(.3,.9,.3,1);
}

.scd-21__sec:has(.scd-21__r:checked) {
  flex: 1 1 auto;
}

.scd-21__r {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.scd-21__h {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 18px 22px;
  font-weight: 800;
  font-size: 16px;
  color: #c9cde0;
  cursor: pointer;
  border-top: 1px solid #262a36;
}

.scd-21__sec:first-child .scd-21__h {
  border-top: none;
}

.scd-21__h::before {
  content: "";
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #3a4050;
  transition: background .3s;
}

.scd-21__r:checked ~ .scd-21__h {
  color: #fff;
}

.scd-21__r:checked ~ .scd-21__h::before {
  background: var(--c);
}

.scd-21__b {
  overflow: hidden;
  opacity: 0;
  max-height: 0;
  transition: opacity .4s,max-height .45s;
}

.scd-21__r:checked ~ .scd-21__b {
  opacity: 1;
  max-height: 200px;
}

.scd-21__b p {
  padding: 0 22px 22px;
  color: #aab0c2;
  font-size: 14px;
  line-height: 1.6;
}

.scd-21__b code {
  background: #0f1117;
  padding: 2px 5px;
  border-radius: 5px;
  font-size: 12px;
}

.scd-21__r:focus-visible ~ .scd-21__h {
  outline: 3px solid var(--c);
  outline-offset: -3px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-21__sec,
    .scd-21__b {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — inside one fixed-size card, the checked section's flex-grow fills while siblings shrink to their headers, so the card box never changes height. */
```
