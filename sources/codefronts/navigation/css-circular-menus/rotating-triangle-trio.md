---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/rotating-triangle-trio/"
title: "Triangular Rotary Navigation Switcher"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A three-mode switcher built on a rotating triangle: the softly-rounded triangular plate spins 120° per selection so the active vertex always points at 12…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Triangular Rotary Navigation Switcher
Source: https://codefronts.com/navigation/css-circular-menus/rotating-triangle-trio/

A three-mode switcher built on a rotating triangle: the softly-rounded triangular plate spins 120° per selection so the active vertex always points at 12 o'clock, while the three mode buttons hold still around it. Perfect for exactly-three-state UIs — Work / Rest / Play, Low / Mid / High, Past / Now / Next.
## HTML
```html
<section class="ccm-20" aria-label="Triangular rotary switcher demo">
  <div class="ccm-20__stage">
    <fieldset class="ccm-20__rig"><legend class="ccm-20__sr">Focus mode</legend>
      <svg class="ccm-20__plate" viewBox="0 0 200 200" aria-hidden="true">
        <path d="M100 22 L169 141 Q175 152 163 152 L37 152 Q25 152 31 141 Z" fill="url(#ccm20-g)" stroke="oklch(0.85 0.02 250 / .25)" stroke-width="1"/>
        <circle cx="100" cy="46" r="5" class="ccm-20__dot"/>
        <defs><linearGradient id="ccm20-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="oklch(0.42 0.06 255)"/><stop offset="1" stop-color="oklch(0.3 0.05 265)"/></linearGradient></defs>
      </svg>
      <div class="ccm-20__station" style="--i:0"><input type="radio" name="ccm20" id="ccm20-a" value="Work" checked><label for="ccm20-a">Work</label></div>
      <div class="ccm-20__station" style="--i:1"><input type="radio" name="ccm20" id="ccm20-b" value="Rest"><label for="ccm20-b">Rest</label></div>
      <div class="ccm-20__station" style="--i:2"><input type="radio" name="ccm20" id="ccm20-c" value="Play"><label for="ccm20-c">Play</label></div>
      <p class="ccm-20__mode" aria-live="polite">Work mode</p>
    </fieldset>
  </div>
</section>
```
## CSS
```css
.ccm-20,
.ccm-20 *,
.ccm-20 *::before,
.ccm-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-20 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,oklch(0.24 0.025 260),oklch(0.17 0.02 270));
  --brand: oklch(0.75 0.16 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.92 0.008 255);
}

.ccm-20__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(180deg,oklch(0.24 0.025 260),oklch(0.17 0.02 270));
  overflow: hidden;
}

.ccm-20__rig {
  position: relative;
  border: none;
  width: 320px;
  height: 320px;
  display: grid;
  place-items: center;
}

.ccm-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-20__plate {
  width: 210px;
  height: 210px;
  rotate: var(--rot,0deg);
  transition: rotate .65s cubic-bezier(.3,1.4,.35,1);
  filter: drop-shadow(0 18px 34px oklch(0 0 0 / .55));
}

.ccm-20__dot {
  fill: var(--brand);
  filter: drop-shadow(0 0 6px var(--brand));
}

.ccm-20__station {
  position: absolute;
  left: 50%;
  top: 50%;
  --a: calc(120deg * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * 138px - 50%) calc(sin(var(--a)) * 138px - 50%);
}

.ccm-20__station input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.ccm-20__station label {
  display: grid;
  place-items: center;
  min-width: 74px;
  height: 44px;
  padding: 0 16px;
  border-radius: 999px;
  background: oklch(0.29 0.03 260);
  border: 1px solid oklch(0.6 0.05 255 / .4);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: .04em;
  cursor: pointer;
  transition: background .25s,color .25s,border-color .25s,scale .25s;
}

.ccm-20__station label:hover {
  border-color: var(--brand);
}

.ccm-20__station :checked + label {
  background: var(--brand);
  border-color: var(--brand);
  color: oklch(0.24 0.04 60);
  scale: 1.1;
  box-shadow: 0 0 26px -4px oklch(0.75 0.16 60 / .6);
}

.ccm-20__station :focus-visible + label {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.ccm-20__mode {
  position: absolute;
  bottom: -8px;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.65 0.05 255);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-20 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const rig = document.querySelector('.ccm-20__rig');
  const plate = rig.querySelector('.ccm-20__plate');
  const mode = rig.querySelector('.ccm-20__mode');
  const values = ['Work', 'Rest', 'Play'];
  let rot = 0, cur = 0;
  rig.addEventListener('change', (e) => {
    if (e.target.name !== 'ccm20') return;
    const idx = values.indexOf(e.target.value);
    let delta = ((idx - cur) * 120 % 360 + 540) % 360 - 180; // shortest spin, ±120°
    rot += delta; cur = idx;
    plate.style.setProperty('--rot', rot + 'deg');
    mode.textContent = e.target.value + ' mode';
  });
})();
```
