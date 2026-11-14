---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/tilt-card/"
title: "3D Tilt Card Option Selector"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Premium selectable cards that tilt in 3D toward your cursor like they're mounted on gimbals, with a glare sheen that sweeps across the surface as they rotate."
has_js: "true"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Tilt Card Option Selector
Source: https://codefronts.com/components/css-radio-buttons/tilt-card/

Premium selectable cards that tilt in 3D toward your cursor like they're mounted on gimbals, with a glare sheen that sweeps across the surface as they rotate. Checking a card locks in an accent edge-light. The selector pattern for GPU tiers, game difficulty and portfolio picks.
## HTML
```html
<div class="crb-12-group">
<section class="crb-12a" aria-label="3D tilt card option selector">
  <fieldset class="crb-12a__group" id="crb-12a-group">
    <legend class="crb-12a__legend">Render tier</legend>
    <div class="crb-12a__row">
      <label class="crb-12a__opt">
        <input class="crb-12a__input" type="radio" name="crb-12a" value="swift">
        <span class="crb-12a__card">
          <span class="crb-12a__tier">Swift</span>
          <span class="crb-12a__spec">8 GB VRAM</span>
          <span class="crb-12a__spec">1080p · 60 fps</span>
          <span class="crb-12a__price">$0.14/hr</span>
        </span>
      </label>
      <label class="crb-12a__opt">
        <input class="crb-12a__input" type="radio" name="crb-12a" value="surge" checked>
        <span class="crb-12a__card">
          <span class="crb-12a__tier">Surge</span>
          <span class="crb-12a__spec">24 GB VRAM</span>
          <span class="crb-12a__spec">1440p · 144 fps</span>
          <span class="crb-12a__price">$0.38/hr</span>
        </span>
      </label>
      <label class="crb-12a__opt">
        <input class="crb-12a__input" type="radio" name="crb-12a" value="titan">
        <span class="crb-12a__card">
          <span class="crb-12a__tier">Titan</span>
          <span class="crb-12a__spec">80 GB VRAM</span>
          <span class="crb-12a__spec">4K · 240 fps</span>
          <span class="crb-12a__price">$1.20/hr</span>
        </span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-12-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-12-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-12a,
.crb-12a *,
.crb-12a *::before,
.crb-12a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-12a {
  --accent: oklch(0.75 0.14 190);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(160deg,#12151f,#0a0c12);
}

.crb-12a__group {
  border: none;
}

.crb-12a__legend {
  font-size: 24px;
  font-weight: 750;
  color: #eef1fa;
  letter-spacing: -.02em;
  text-align: center;
}

.crb-12a__row {
  display: flex;
  flex-wrap: wrap;
  gap: 22px;
  justify-content: center;
  margin-top: 28px;
  perspective: 900px;
}

.crb-12a__opt {
  position: relative;
  cursor: pointer;
}

.crb-12a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-12a__card {
  position: relative;
  overflow: hidden;
  display: grid;
  gap: 5px;
  width: 190px;
  padding: 24px 20px;
  background: linear-gradient(165deg,#1c2130,#141826);
  border: 1.5px solid rgba(255,255,255,.1);
  border-radius: 16px;
  transform: rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .18s ease-out,border-color .3s,box-shadow .3s;
}

.crb-12a__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(115deg,transparent 30%,rgba(255,255,255,.16) 48%,transparent 62%);
  transform: translateX(var(--gx,0px));
  opacity: var(--go,0);
  transition: opacity .3s;
  pointer-events: none;
}

.crb-12a__tier {
  font-size: 19px;
  font-weight: 800;
  color: #fff;
  letter-spacing: -.01em;
  margin-bottom: 6px;
}

.crb-12a__spec {
  font-size: 13px;
  color: #8f98b5;
}

.crb-12a__price {
  margin-top: 12px;
  font-size: 15px;
  font-weight: 750;
  color: var(--accent);
}

.crb-12a__opt:has(.crb-12a__input:checked) .crb-12a__card {
  border-color: var(--accent);
  box-shadow: 0 0 0 1px color-mix(in oklab,var(--accent) 60%,transparent),0 24px 48px -20px color-mix(in oklab,var(--accent) 45%,transparent);
}

.crb-12a__opt:has(.crb-12a__input:focus-visible) .crb-12a__card {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-12a__card {
    transition: border-color .2s;
    transform: none!important;
  }
}
```

## JavaScript
```js
(() => {
  const init = () => {
    const group = document.querySelector('#crb-12a-group'); if (!group) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX_TILT = 10, GLARE_SWEEP = 90;
    group.querySelectorAll('.crb-12a__opt').forEach((opt) => {
      const card = opt.querySelector('.crb-12a__card');
      opt.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width - .5, py = (e.clientY - r.top) / r.height - .5;
        card.style.setProperty('--ry', (px * MAX_TILT * 2).toFixed(2) + 'deg');
        card.style.setProperty('--rx', (-py * MAX_TILT * 2).toFixed(2) + 'deg');
        card.style.setProperty('--gx', (px * GLARE_SWEEP).toFixed(1) + 'px');
        card.style.setProperty('--go', '1');
      }, { passive: true });
      opt.addEventListener('pointerleave', () => {
        card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg');
        card.style.setProperty('--gx', '0px'); card.style.setProperty('--go', '0');
      });
    });
  };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', init) : init();
})();
```
