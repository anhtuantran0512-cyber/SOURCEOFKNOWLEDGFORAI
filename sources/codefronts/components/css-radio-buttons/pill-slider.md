---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/pill-slider/"
title: "Sliding Pill Toggle Switch"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "A three-way pill slider where the thumb glides between options AND changes colour as it lands — Pickup is amber, Delivery is green, Dine-in is violet."
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Pill Toggle Switch
Source: https://codefronts.com/components/css-radio-buttons/pill-slider/

A three-way pill slider where the thumb glides between options AND changes colour as it lands — Pickup is amber, Delivery is green, Dine-in is violet. The thumb position and hue are both pure CSS, computed from which radio is checked via :has() and nth-child.
## HTML
```html
<div class="crb-08-group">
<section class="crb-08a" aria-label="Sliding pill toggle switch">
  <fieldset class="crb-08a__group">
    <legend class="crb-08a__legend">How do you want it?</legend>
    <div class="crb-08a__track">
      <label class="crb-08a__seg"><input class="crb-08a__input" type="radio" name="crb-08a" value="pickup" checked><span class="crb-08a__text">Pickup</span></label>
      <label class="crb-08a__seg"><input class="crb-08a__input" type="radio" name="crb-08a" value="delivery"><span class="crb-08a__text">Delivery</span></label>
      <label class="crb-08a__seg"><input class="crb-08a__input" type="radio" name="crb-08a" value="dinein"><span class="crb-08a__text">Dine-in</span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-08-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-08-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-08a,
.crb-08a *,
.crb-08a *::before,
.crb-08a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-08a {
  --ink: #221d16;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #faf7f2;
}

.crb-08a__group {
  border: none;
  display: grid;
  justify-items: center;
  gap: 20px;
}

.crb-08a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 2px;
}

.crb-08a__track {
  --thumb: oklch(0.75 0.15 75);
  position: relative;
  isolation: isolate;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  padding: 5px;
  background: #efe9df;
  border-radius: 9999px;
  box-shadow: inset 0 1px 3px rgba(60,45,20,.12);
}

.crb-08a__track::before {
  content: "";
  position: absolute;
  z-index: 0;
  top: 5px;
  left: 5px;
  width: calc(33.333% - 3.33px);
  height: calc(100% - 10px);
  border-radius: 9999px;
  background: var(--thumb);
  box-shadow: 0 3px 10px color-mix(in oklab,var(--thumb) 45%,transparent);
  transition: transform .4s cubic-bezier(.22,1,.36,1),background .4s;
}

.crb-08a__track:has(.crb-08a__seg:nth-child(2) .crb-08a__input:checked) {
  --thumb: oklch(0.62 0.17 155);
}

.crb-08a__track:has(.crb-08a__seg:nth-child(2) .crb-08a__input:checked)::before {
  transform: translateX(100%);
}

.crb-08a__track:has(.crb-08a__seg:nth-child(3) .crb-08a__input:checked) {
  --thumb: oklch(0.55 0.2 300);
}

.crb-08a__track:has(.crb-08a__seg:nth-child(3) .crb-08a__input:checked)::before {
  transform: translateX(200%);
}

.crb-08a__seg {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  min-width: 110px;
  min-height: 46px;
  padding: 0 18px;
  border-radius: 9999px;
  cursor: pointer;
}

.crb-08a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-08a__text {
  font-size: 15px;
  font-weight: 700;
  color: #8c8271;
  transition: color .3s;
}

.crb-08a__seg:has(.crb-08a__input:checked) .crb-08a__text {
  color: #fff;
}

.crb-08a__seg:has(.crb-08a__input:focus-visible) {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-08a__track::before {
    transition: background .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — three :has(nth-child) rules move the ::before thumb 0/100%/200% and swap the --thumb colour in the same transition. */
```
