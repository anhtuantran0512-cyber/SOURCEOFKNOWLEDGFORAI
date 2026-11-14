---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/3d-flip-card-toggle/"
title: "3D Flip Card Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A toggle that flips like a card on a table: the whole control rotates 180° in 3D to reveal its other face — muted gray 'Paused' on the front, vivid 'Active'…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Card Toggle
Source: https://codefronts.com/components/css-toggles-switches/3d-flip-card-toggle/

A toggle that flips like a card on a table: the whole control rotates 180° in 3D to reveal its other face — muted gray 'Paused' on the front, vivid 'Active' on the back — turning a boolean into a satisfying physical object.
## HTML
```html
<section class="tgl-19" aria-label="3D flip card toggle">
  <input type="checkbox" id="tgl-19-sw" class="tgl-19__sw" role="switch" aria-label="Campaign active">
  <label class="tgl-19__persp" for="tgl-19-sw" aria-hidden="true">
    <span class="tgl-19__card">
      <span class="tgl-19__face tgl-19__face--front"><b>PAUSED</b><small>Campaign is not spending</small></span>
      <span class="tgl-19__face tgl-19__face--back"><b>ACTIVE</b><small>Ads are live · $184/day</small></span>
    </span>
  </label>
  <p class="tgl-19__cap">Click the card to flip state</p>
</section>
```
## CSS
```css
.tgl-19,
.tgl-19 *,
.tgl-19 *::before,
.tgl-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-19 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 26px;
  padding: 60px 20px;
  background: #f1f2f6;
}

.tgl-19__sw {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.tgl-19__persp {
  perspective: 900px;
  cursor: pointer;
  display: block;
}

.tgl-19__card {
  position: relative;
  display: block;
  width: 230px;
  height: 130px;
  transform-style: preserve-3d;
  transition: transform .65s cubic-bezier(.4,.2,.2,1.15);
}

.tgl-19__sw:checked ~ .tgl-19__persp .tgl-19__card {
  transform: rotateY(180deg);
}

.tgl-19__face {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  border-radius: 16px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  box-shadow: 0 18px 36px -20px rgba(30,35,60,.55);
}

.tgl-19__face b {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: .12em;
}

.tgl-19__face small {
  font-size: 12.5px;
  opacity: .75;
}

.tgl-19__face--front {
  background: linear-gradient(150deg,#fdfdfe,#e7e9ef);
  color: #5a6172;
}

.tgl-19__face--back {
  background: linear-gradient(150deg,oklch(0.62 0.17 155),oklch(0.5 0.14 170));
  color: #fff;
  transform: rotateY(180deg);
}

.tgl-19__sw:focus-visible ~ .tgl-19__persp {
  outline: 3px solid oklch(0.6 0.17 250);
  outline-offset: 5px;
  border-radius: 18px;
}

.tgl-19__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #9aa0af;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-19__card {
    transition: transform .15s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a preserve-3d card rotates rotateY(180deg) on :checked, with backface-hidden faces so each side lands upright. */
```
