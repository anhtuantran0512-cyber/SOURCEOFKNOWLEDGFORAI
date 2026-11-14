---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/sliding-pill-with-traveling-label/"
title: "Sliding Pill with Traveling Label"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The label rides IN the thumb: a wide pill where the sliding handle itself says 'Draft' or 'Live', crossfading its word mid-journey while ghost labels in the…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Pill with Traveling Label
Source: https://codefronts.com/components/css-toggles-switches/sliding-pill-with-traveling-label/

The label rides IN the thumb: a wide pill where the sliding handle itself says 'Draft' or 'Live', crossfading its word mid-journey while ghost labels in the track show the destination. Ideal for publish switches where the state word must move with the control.
## HTML
```html
<section class="tgl-20" aria-label="Sliding pill with traveling label">
  <div class="tgl-20__row">
    <span class="tgl-20__lbl" id="tgl-20-l">Article status</span>
    <input type="checkbox" id="tgl-20-sw" class="tgl-20__sw" role="switch" aria-labelledby="tgl-20-l">
    <label class="tgl-20__track" for="tgl-20-sw" aria-hidden="true">
      <span class="tgl-20__ghost tgl-20__ghost--l">Draft</span>
      <span class="tgl-20__ghost tgl-20__ghost--r">Live</span>
      <span class="tgl-20__thumb"><i class="tgl-20__w tgl-20__w--draft">Draft</i><i class="tgl-20__w tgl-20__w--live">Live</i></span>
    </label>
  </div>
  <p class="tgl-20__cap">The word travels with the thumb</p>
</section>
```
## CSS
```css
.tgl-20,
.tgl-20 *,
.tgl-20 *::before,
.tgl-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-20 {
  --live: oklch(0.65 0.16 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 60px 20px;
  background: #f7f7f4;
}

.tgl-20__row {
  display: flex;
  align-items: center;
  gap: 26px;
  background: #fff;
  border: 1px solid #e8e7e0;
  border-radius: 16px;
  padding: 18px 24px;
  box-shadow: 0 10px 28px -22px rgba(40,40,20,.5);
}

.tgl-20__lbl {
  font-size: 15px;
  font-weight: 600;
  color: #3a3d33;
}

.tgl-20__sw {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.tgl-20__track {
  position: relative;
  flex: none;
  width: 164px;
  height: 44px;
  border-radius: 24px;
  background: #ecebe4;
  box-shadow: inset 0 2px 5px rgba(60,60,30,.15);
  cursor: pointer;
}

.tgl-20__ghost {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  color: #b4b2a4;
  transition: opacity .35s;
}

.tgl-20__ghost--l {
  left: 0;
}

.tgl-20__ghost--r {
  right: 0;
}

.tgl-20__sw:not(:checked) ~ .tgl-20__track .tgl-20__ghost--l,
.tgl-20__sw:checked ~ .tgl-20__track .tgl-20__ghost--r {
  opacity: 0;
}

.tgl-20__thumb {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 78px;
  height: 36px;
  border-radius: 20px;
  background: #5c6270;
  box-shadow: 0 3px 8px rgba(30,35,50,.35);
  transition: transform .35s cubic-bezier(.3,1,.35,1.05),background-color .35s;
  display: block;
}

.tgl-20__sw:checked ~ .tgl-20__track .tgl-20__thumb {
  transform: translateX(78px);
  background: var(--live);
}

.tgl-20__w {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13.5px;
  font-weight: 800;
  letter-spacing: .04em;
  color: #fff;
  font-style: normal;
  transition: opacity .35s;
}

.tgl-20__w--live {
  opacity: 0;
}

.tgl-20__sw:checked ~ .tgl-20__track .tgl-20__w--draft {
  opacity: 0;
}

.tgl-20__sw:checked ~ .tgl-20__track .tgl-20__w--live {
  opacity: 1;
}

.tgl-20__sw:focus-visible ~ .tgl-20__track {
  outline: 3px solid oklch(0.6 0.17 250);
  outline-offset: 3px;
}

.tgl-20__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #a8a698;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-20__thumb,
    .tgl-20__w,
    .tgl-20__ghost {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the wide thumb carries both state words stacked; one translateX slides it while the words crossfade on the same curve. */
```
