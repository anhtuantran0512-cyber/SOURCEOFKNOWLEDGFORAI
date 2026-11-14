---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/hexagonal-honeycomb/"
title: "Hexagonal Grid Radial Selector"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A honeycomb selector: six hexagonal cells lock around a central hex like real comb, each cut with one clip-path and placed with the same ring trig as every…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hexagonal Grid Radial Selector
Source: https://codefronts.com/navigation/css-circular-menus/hexagonal-honeycomb/

A honeycomb selector: six hexagonal cells lock around a central hex like real comb, each cut with one clip-path and placed with the same ring trig as every circle menu — hexagons ARE a radial layout with a 60° step. Radio-group semantics underneath; the picked cell fills with the accent and pops forward. No JavaScript.
## HTML
```html
<section class="ccm-19" aria-label="Hexagonal grid selector demo">
  <div class="ccm-19__stage">
    <fieldset class="ccm-19__comb" style="--n:6"><legend class="ccm-19__sr">Choose a class</legend>
      <div class="ccm-19__center"><span class="ccm-19__hexface"><em>PICK</em><output class="ccm-19__out">Ranger</output></span></div>
      <div class="ccm-19__cell" style="--i:0"><input type="radio" name="ccm19" id="ccm19-a" value="Ranger" checked><label for="ccm19-a"><b>🏹</b>Ranger</label></div>
      <div class="ccm-19__cell" style="--i:1"><input type="radio" name="ccm19" id="ccm19-b" value="Mage"><label for="ccm19-b"><b>✦</b>Mage</label></div>
      <div class="ccm-19__cell" style="--i:2"><input type="radio" name="ccm19" id="ccm19-c" value="Knight"><label for="ccm19-c"><b>🛡</b>Knight</label></div>
      <div class="ccm-19__cell" style="--i:3"><input type="radio" name="ccm19" id="ccm19-d" value="Rogue"><label for="ccm19-d"><b>🗡</b>Rogue</label></div>
      <div class="ccm-19__cell" style="--i:4"><input type="radio" name="ccm19" id="ccm19-e" value="Cleric"><label for="ccm19-e"><b>☥</b>Cleric</label></div>
      <div class="ccm-19__cell" style="--i:5"><input type="radio" name="ccm19" id="ccm19-f" value="Bard"><label for="ccm19-f"><b>♪</b>Bard</label></div>
    </fieldset>
    <p class="ccm-19__note">Pure CSS · arrow keys cycle the comb</p>
  </div>
</section>
```
## CSS
```css
.ccm-19,
.ccm-19 *,
.ccm-19 *::before,
.ccm-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-19 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,oklch(0.25 0.02 60),oklch(0.18 0.018 50));
  --brand: oklch(0.78 0.15 80);
  --hex: polygon(25% 3.35%,75% 3.35%,100% 50%,75% 96.65%,25% 96.65%,0% 50%);
  --cell: 104px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.9 0.01 80);
}

.ccm-19__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(180deg,oklch(0.25 0.02 60),oklch(0.18 0.018 50));
  overflow: hidden;
}

.ccm-19__comb {
  position: relative;
  border: none;
  width: calc(var(--cell) * 3.1);
  height: calc(var(--cell) * 3.1);
  display: grid;
  place-items: center;
}

.ccm-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-19__center,
.ccm-19__cell {
  position: absolute;
  left: 50%;
  top: 50%;
  width: var(--cell);
  height: calc(var(--cell) * 1.1547);
}

.ccm-19__center {
  translate: -50% -50%;
  display: grid;
}

.ccm-19__hexface {
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 2px;
  clip-path: var(--hex);
  background: radial-gradient(circle at 40% 30%,oklch(0.34 0.03 65),oklch(0.24 0.02 55));
  text-align: center;
}

.ccm-19__hexface em {
  font-style: normal;
  font-size: 9.5px;
  letter-spacing: .3em;
  color: oklch(0.62 0.06 75);
}

.ccm-19__out {
  font-size: 16.5px;
  font-weight: 800;
  color: var(--brand);
}

.ccm-19__cell {
  --a: calc(60deg * var(--i) - 90deg);
  --d: calc(var(--cell) * 1.08);
  translate: calc(cos(var(--a)) * var(--d) - 50%) calc(sin(var(--a)) * var(--d) - 50%);
  transition: scale .25s cubic-bezier(.34,1.35,.4,1),filter .25s;
  /* second ring: 12 cells alternating --d of 2.16 and 1.87 × cell */
}

.ccm-19__cell:has(:checked) {
  scale: 1.08;
  z-index: 1;
  filter: drop-shadow(0 8px 18px oklch(0.7 0.15 80 / .45));
}

.ccm-19__cell input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.ccm-19__cell label {
  position: absolute;
  inset: 0;
  clip-path: var(--hex);
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 5px;
  background: oklch(0.3 0.025 60);
  border: none;
  cursor: pointer;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .03em;
  transition: background .25s,color .25s;
}

.ccm-19__cell label b {
  font-size: 21px;
  font-weight: 400;
  line-height: 1;
}

.ccm-19__cell label:hover {
  background: oklch(0.36 0.035 65);
}

.ccm-19__cell :checked + label {
  background: linear-gradient(150deg,var(--brand),oklch(0.68 0.16 60));
  color: oklch(0.25 0.04 60);
}

.ccm-19__cell label::after {
  content: "";
  position: absolute;
  inset: 5px;
  clip-path: var(--hex);
  background: transparent;
  border: 0 solid transparent;
  pointer-events: none;
}

.ccm-19__cell:has(:focus-visible) label::after {
  background: oklch(1 0 0 / .0);
  box-shadow: inset 0 0 0 3px #fff;
}

.ccm-19__cell:has(:focus-visible) label {
  filter: brightness(1.15);
}

.ccm-19__note {
  position: absolute;
  bottom: 20px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.6 0.05 70 / .6);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-19 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  // Optional 3-line enhancement: mirror the picked class into the center hex.
  const root = document.querySelector('.ccm-19');
  const out = root.querySelector('.ccm-19__out');
  root.addEventListener('change', (e) => { if (e.target.name === 'ccm19') out.textContent = e.target.value; });
})();
```
