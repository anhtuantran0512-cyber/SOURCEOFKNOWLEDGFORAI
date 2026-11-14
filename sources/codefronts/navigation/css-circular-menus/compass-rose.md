---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/compass-rose/"
title: "Compass Rose Directional Navigation"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A brass-and-ink compass whose needle swings to whichever cardinal you choose: four destinations sit at N/E/S/W, the needle takes the shortest rotation to…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compass Rose Directional Navigation
Source: https://codefronts.com/navigation/css-circular-menus/compass-rose/

A brass-and-ink compass whose needle swings to whichever cardinal you choose: four destinations sit at N/E/S/W, the needle takes the shortest rotation to point at the active one, and a degree readout ticks along like a real bearing. A natural fit for travel products, maps, story sites and portfolio 'explore' screens.
## HTML
```html
<section class="ccm-22" aria-label="Compass rose navigation demo">
  <div class="ccm-22__stage">
    <fieldset class="ccm-22__rose"><legend class="ccm-22__sr">Choose a destination</legend>
      <div class="ccm-22__dial" aria-hidden="true">
        <span class="ccm-22__ticks"></span>
        <span class="ccm-22__letter ccm-22__letter--n" style="--x:0;--y:-1">N</span>
        <span class="ccm-22__letter" style="--x:1;--y:0">E</span>
        <span class="ccm-22__letter" style="--x:0;--y:1">S</span>
        <span class="ccm-22__letter" style="--x:-1;--y:0">W</span>
        <span class="ccm-22__needle"><i></i></span>
        <span class="ccm-22__cap"></span>
      </div>
      <div class="ccm-22__station ccm-22__station--n"><input type="radio" name="ccm22" id="ccm22-n" value="0" data-place="Highlands" checked><label for="ccm22-n">Highlands</label></div>
      <div class="ccm-22__station ccm-22__station--e"><input type="radio" name="ccm22" id="ccm22-e" value="90" data-place="Coast"><label for="ccm22-e">Coast</label></div>
      <div class="ccm-22__station ccm-22__station--s"><input type="radio" name="ccm22" id="ccm22-s" value="180" data-place="Old Town"><label for="ccm22-s">Old Town</label></div>
      <div class="ccm-22__station ccm-22__station--w"><input type="radio" name="ccm22" id="ccm22-w" value="270" data-place="Vineyards"><label for="ccm22-w">Vineyards</label></div>
      <p class="ccm-22__bearing"><output class="ccm-22__deg">000</output>° · <span class="ccm-22__place">Highlands</span></p>
    </fieldset>
  </div>
</section>
```
## CSS
```css
.ccm-22,
.ccm-22 *,
.ccm-22 *::before,
.ccm-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-22 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(170deg,oklch(0.93 0.02 85),oklch(0.87 0.03 80));
  --brass: oklch(0.72 0.1 85);
  --ink: oklch(0.3 0.03 60);
  --paper: oklch(0.95 0.015 85);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.ccm-22__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(170deg,oklch(0.93 0.02 85),oklch(0.87 0.03 80));
  border: 1px solid oklch(0.85 0.03 82);
}

.ccm-22__rose {
  position: relative;
  border: none;
  width: 360px;
  height: 360px;
  display: grid;
  place-items: center;
}

.ccm-22__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-22__dial {
  position: relative;
  width: 250px;
  height: 250px;
  border-radius: 50%;
  background: radial-gradient(circle at 38% 30%,var(--paper),oklch(0.88 0.025 85));
  box-shadow: 0 0 0 8px oklch(0.72 0.1 85),0 0 0 9px oklch(0.55 0.08 80),0 24px 50px -20px oklch(0.4 0.06 70 / .7),inset 0 2px 6px oklch(1 0 0 / .8);
  display: grid;
  place-items: center;
}

.ccm-22__ticks {
  position: absolute;
  inset: 8px;
  border-radius: 50%;
  background: repeating-conic-gradient(from -0.5deg,var(--ink) 0 1deg,transparent 1deg 5deg),repeating-conic-gradient(from -1deg,oklch(0.3 0.03 60 / .9) 0 2deg,transparent 2deg 45deg);
  -webkit-mask: radial-gradient(circle,transparent 75%,#000 75.5%);
  mask: radial-gradient(circle,transparent 75%,#000 75.5%);
}

.ccm-22__letter {
  position: absolute;
  left: 50%;
  top: 50%;
  translate: calc(var(--x) * 88px - 50%) calc(var(--y) * 88px - 50%);
  font-size: 21px;
  font-weight: 700;
  letter-spacing: .05em;
}

.ccm-22__letter--n {
  color: oklch(0.55 0.19 25);
}

.ccm-22__needle {
  position: absolute;
  width: 12px;
  height: 172px;
  rotate: var(--rot,0deg);
  transition: rotate .9s cubic-bezier(.3,1.2,.35,1);
}

.ccm-22__needle i {
  position: absolute;
  left: 50%;
  top: 0;
  translate: -50% 0;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-bottom: 86px solid oklch(0.55 0.19 25);
  filter: drop-shadow(0 2px 3px oklch(0.3 0.05 25 / .4));
}

.ccm-22__needle::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: 0;
  translate: -50% 0;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-top: 86px solid oklch(0.45 0.04 60);
}

.ccm-22__cap {
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,oklch(0.85 0.08 85),var(--brass));
  box-shadow: 0 1px 3px oklch(0 0 0 / .4);
}

.ccm-22__station {
  position: absolute;
}

.ccm-22__station--n {
  top: -2px;
  left: 50%;
  translate: -50% 0;
}

.ccm-22__station--e {
  right: -16px;
  top: 50%;
  translate: 0 -50%;
}

.ccm-22__station--s {
  bottom: -2px;
  left: 50%;
  translate: -50% 0;
}

.ccm-22__station--w {
  left: -16px;
  top: 50%;
  translate: 0 -50%;
}

.ccm-22__station input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.ccm-22__station label {
  display: inline-block;
  padding: 9px 15px;
  border-radius: 999px;
  background: oklch(1 0 0 / .6);
  border: 1px solid oklch(0.7 0.06 80);
  font-size: 13.5px;
  font-style: italic;
  cursor: pointer;
  white-space: nowrap;
  transition: background .25s,color .25s,border-color .25s;
  box-shadow: 0 4px 12px -6px oklch(0.4 0.06 70 / .5);
}

.ccm-22__station label:hover {
  border-color: var(--ink);
}

.ccm-22__station :checked + label {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
  font-style: normal;
}

.ccm-22__station :focus-visible + label {
  outline: 3px solid oklch(0.55 0.19 25);
  outline-offset: 2px;
}

.ccm-22__bearing {
  position: absolute;
  bottom: -34px;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 15px;
  letter-spacing: .08em;
  font-variant-numeric: tabular-nums;
}

.ccm-22__deg {
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .ccm-22 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const rose = document.querySelector('.ccm-22__rose');
  const needle = rose.querySelector('.ccm-22__needle');
  const degOut = rose.querySelector('.ccm-22__deg');
  const place = rose.querySelector('.ccm-22__place');
  let rot = 0, shown = 0, raf = null;
  const tween = (target) => {
    cancelAnimationFrame(raf);
    const from = shown, delta = ((target - from) % 360 + 540) % 360 - 180, t0 = performance.now();
    const step = (t) => {
      const k = Math.min(1, (t - t0) / 850), e = 1 - Math.pow(1 - k, 3);
      shown = (from + delta * e + 360) % 360;
      degOut.textContent = String(Math.round(shown) % 360).padStart(3, '0');
      if (k < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
  };
  rose.addEventListener('change', (e) => {
    if (e.target.name !== 'ccm22') return;
    const target = Number(e.target.value);
    let delta = ((target - ((rot % 360) + 360) % 360) % 360 + 540) % 360 - 180;
    rot += delta;
    needle.style.setProperty('--rot', rot + 'deg');
    place.textContent = e.target.dataset.place;
    tween(target);
  });
})();
```
