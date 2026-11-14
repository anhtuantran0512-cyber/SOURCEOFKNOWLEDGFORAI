---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/interactive-wheel-menu-pie-slice-dropdown/"
title: "Interactive Wheel Menu (Pie Slice Dropdown)"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A game-style selection wheel: six real pie slices cut with conic-gradient hit zones, a live center readout, and radio-group semantics underneath so the whole…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Wheel Menu (Pie Slice Dropdown)
Source: https://codefronts.com/navigation/css-circular-menus/interactive-wheel-menu-pie-slice-dropdown/

A game-style selection wheel: six real pie slices cut with conic-gradient hit zones, a live center readout, and radio-group semantics underneath so the whole wheel works with arrow keys exactly like a native control. The pattern behind weapon wheels, emoji reactions and quick-tool pickers.
## HTML
```html
<section class="ccm-03" aria-label="Pie slice wheel menu demo">
  <div class="ccm-03__stage">
    <fieldset class="ccm-03__wheelbox"><legend class="ccm-03__sr">Choose a tool</legend>
      <div class="ccm-03__wheel">
        <div class="ccm-03__slice" style="--i:0"><input type="radio" name="ccm03" id="ccm03-a" value="Brush" checked><label for="ccm03-a"><span class="ccm-03__lab"><b>🖌</b>Brush</span></label></div>
        <div class="ccm-03__slice" style="--i:1"><input type="radio" name="ccm03" id="ccm03-b" value="Eraser"><label for="ccm03-b"><span class="ccm-03__lab"><b>◻</b>Eraser</span></label></div>
        <div class="ccm-03__slice" style="--i:2"><input type="radio" name="ccm03" id="ccm03-c" value="Fill"><label for="ccm03-c"><span class="ccm-03__lab"><b>◉</b>Fill</span></label></div>
        <div class="ccm-03__slice" style="--i:3"><input type="radio" name="ccm03" id="ccm03-d" value="Text"><label for="ccm03-d"><span class="ccm-03__lab"><b>T</b>Text</span></label></div>
        <div class="ccm-03__slice" style="--i:4"><input type="radio" name="ccm03" id="ccm03-e" value="Shapes"><label for="ccm03-e"><span class="ccm-03__lab"><b>△</b>Shapes</span></label></div>
        <div class="ccm-03__slice" style="--i:5"><input type="radio" name="ccm03" id="ccm03-f" value="Crop"><label for="ccm03-f"><span class="ccm-03__lab"><b>⌗</b>Crop</span></label></div>
        <div class="ccm-03__center"><em>Tool</em><output class="ccm-03__pick" for="ccm03-a ccm03-b ccm03-c ccm03-d ccm03-e ccm03-f">Brush</output></div>
      </div>
    </fieldset>
    <p class="ccm-03__hint">Click a slice — or focus the wheel and use ← → arrow keys.</p>
  </div>
</section>
```
## CSS
```css
.ccm-03,
.ccm-03 *,
.ccm-03 *::before,
.ccm-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-03 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(170deg,oklch(0.97 0.008 60),oklch(0.93 0.02 40));
  --brand: oklch(0.68 0.19 35);
  --ink: oklch(0.25 0.02 35);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.ccm-03__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  border-radius: 20px;
  background: linear-gradient(170deg,oklch(0.97 0.008 60),oklch(0.93 0.02 40));
  border: 1px solid oklch(0.9 0.015 40);
}

.ccm-03__wheelbox {
  border: none;
}

.ccm-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-03__wheel {
  position: relative;
  width: 300px;
  height: 300px;
}

.ccm-03__slice {
  position: absolute;
  inset: 0;
  rotate: calc(var(--i) * 60deg);
  pointer-events: none;
  transition: translate .25s cubic-bezier(.34,1.3,.4,1);
}

.ccm-03__slice input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.ccm-03__slice label {
  position: absolute;
  inset: 0;
  pointer-events: auto;
  border-radius: 50%;
  clip-path: polygon(50% 50%,50% 0%,75% 6.7%,93.3% 25%);
  cursor: pointer;
  background: #fff;
  border: 1px solid oklch(0.88 0.02 40);
  transition: background .2s;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .02em;
  color: var(--ink);
}

.ccm-03__slice label:hover {
  background: oklch(0.95 0.03 40);
}

.ccm-03__slice :checked + label {
  background: linear-gradient(150deg,var(--brand),oklch(0.6 0.21 25));
  color: #fff;
  border-color: transparent;
}

.ccm-03__slice:has(:checked) {
  scale: 1.04;
  z-index: 1;
  filter: drop-shadow(0 6px 14px oklch(0.55 0.2 30 / .35));
}

.ccm-03__slice:has(:focus-visible) label {
  outline: 3px solid var(--brand);
  outline-offset: -6px;
}

.ccm-03__lab {
  position: absolute;
  left: 50%;
  top: 50%;
  translate: calc(cos(-60deg) * 100px - 50%) calc(sin(-60deg) * 100px - 50%);
  rotate: calc(var(--i) * -60deg);
  display: grid;
  justify-items: center;
  gap: 1px;
  pointer-events: none;
}

.ccm-03__lab b {
  font-size: 19px;
  font-weight: 400;
  line-height: 1.1;
}

.ccm-03__center {
  position: absolute;
  inset: 50%;
  translate: -50% -50%;
  width: 118px;
  height: 118px;
  border-radius: 50%;
  background: #fff;
  border: 1px solid oklch(0.88 0.02 40);
  box-shadow: 0 10px 26px -12px oklch(0.4 0.08 35 / .5);
  display: grid;
  place-content: center;
  text-align: center;
  gap: 2px;
  z-index: 2;
}

.ccm-03__center em {
  font-style: normal;
  font-size: 10.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 35);
}

.ccm-03__pick {
  font-size: 18px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--brand);
}

.ccm-03__hint {
  font-size: 13px;
  color: oklch(0.5 0.02 35);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-03 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ccm-03');
  const out = root.querySelector('.ccm-03__pick');
  root.addEventListener('change', (e) => {
    if (e.target.name === 'ccm03') out.textContent = e.target.value;
  });
})();
```
