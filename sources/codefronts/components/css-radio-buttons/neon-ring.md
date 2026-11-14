---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/neon-ring/"
title: "Cyberpunk Neon Ring Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "A sci-fi loadout selector: hexagon-cornered chips with neon ring indicators that ignite on selection — a conic energy arc spins around the checked ring while…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Ring Radio
Source: https://codefronts.com/components/css-radio-buttons/neon-ring/

A sci-fi loadout selector: hexagon-cornered chips with neon ring indicators that ignite on selection — a conic energy arc spins around the checked ring while cyan/magenta scanlines flicker across the chip. Built for gaming UIs, web3 dashboards and dev-tool dark themes. Pure CSS, registered-property animated.
## HTML
```html
<div class="crb-16-group">
<section class="crb-16a" aria-label="Cyberpunk neon ring radio buttons">
  <fieldset class="crb-16a__group">
    <legend class="crb-16a__legend">Select loadout</legend>
    <div class="crb-16a__row">
      <label class="crb-16a__chip"><input class="crb-16a__input" type="radio" name="crb-16a" value="ghost" checked><span class="crb-16a__scan" aria-hidden="true"></span><span class="crb-16a__ring" aria-hidden="true"></span><span class="crb-16a__name">GHOST</span><span class="crb-16a__role">Stealth</span></label>
      <label class="crb-16a__chip"><input class="crb-16a__input" type="radio" name="crb-16a" value="viper"><span class="crb-16a__scan" aria-hidden="true"></span><span class="crb-16a__ring" aria-hidden="true"></span><span class="crb-16a__name">VIPER</span><span class="crb-16a__role">Assault</span></label>
      <label class="crb-16a__chip"><input class="crb-16a__input" type="radio" name="crb-16a" value="atlas"><span class="crb-16a__scan" aria-hidden="true"></span><span class="crb-16a__ring" aria-hidden="true"></span><span class="crb-16a__name">ATLAS</span><span class="crb-16a__role">Tank</span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-16-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-16-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

@property --crb16a-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.crb-16a,
.crb-16a *,
.crb-16a *::before,
.crb-16a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-16a {
  --neon: #22e3ff;
  --neon2: #ff2bd6;
  font-family: ui-monospace,'Cascadia Code','Segoe UI',monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 110% at 50% 0%,#0d1022,#06070f);
}

.crb-16a__group {
  border: none;
}

.crb-16a__legend {
  font-size: 20px;
  font-weight: 750;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: #e8fbff;
  text-align: center;
  text-shadow: 0 0 18px color-mix(in oklab,var(--neon) 60%,transparent);
}

.crb-16a__row {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  justify-content: center;
  margin-top: 30px;
}

.crb-16a__chip {
  position: relative;
  isolation: isolate;
  display: grid;
  justify-items: center;
  gap: 3px;
  width: 158px;
  padding: 26px 16px 20px;
  background: linear-gradient(170deg,#12172e,#0a0d1c);
  clip-path: polygon(10px 0,100% 0,100% calc(100% - 10px),calc(100% - 10px) 100%,0 100%,0 10px);
  border: 1px solid rgba(34,227,255,.25);
  cursor: pointer;
  transition: border-color .3s,background .3s;
}

.crb-16a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-16a__scan {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,rgba(34,227,255,.05) 0 1px,transparent 1px 3px);
  opacity: .6;
  pointer-events: none;
  z-index: 0;
}

.crb-16a__ring {
  position: relative;
  z-index: 1;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-bottom: 10px;
  border: 2px solid #33405f;
  transition: border-color .3s;
}

.crb-16a__ring::before {
  content: "";
  position: absolute;
  inset: -7px;
  border-radius: 50%;
  background: conic-gradient(from var(--crb16a-a),transparent 0%,var(--neon) 12%,var(--neon2) 22%,transparent 32%);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px));
  opacity: 0;
  transition: opacity .3s;
}

.crb-16a__ring::after {
  content: "";
  position: absolute;
  inset: 8px;
  border-radius: 50%;
  background: var(--neon);
  box-shadow: 0 0 10px var(--neon),0 0 26px color-mix(in oklab,var(--neon) 55%,transparent);
  transform: scale(0);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.crb-16a__name {
  position: relative;
  z-index: 1;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .2em;
  color: #dfe9ff;
}

.crb-16a__role {
  position: relative;
  z-index: 1;
  font-size: 11px;
  letter-spacing: .14em;
  color: #5f6c94;
}

.crb-16a__chip:hover {
  border-color: color-mix(in oklab,var(--neon) 55%,transparent);
}

.crb-16a__chip:has(.crb-16a__input:checked) {
  border-color: var(--neon);
  background: linear-gradient(170deg,#16204a,#0b1024);
}

.crb-16a__chip:has(.crb-16a__input:checked) .crb-16a__ring {
  border-color: color-mix(in oklab,var(--neon) 60%,#33405f);
}

.crb-16a__chip:has(.crb-16a__input:checked) .crb-16a__ring::before {
  opacity: 1;
  animation: crb-16a-spin 1.6s linear infinite;
}

.crb-16a__chip:has(.crb-16a__input:checked) .crb-16a__ring::after {
  transform: scale(1);
}

.crb-16a__chip:has(.crb-16a__input:checked) .crb-16a__name {
  color: #fff;
  text-shadow: 0 0 12px color-mix(in oklab,var(--neon) 70%,transparent);
}

.crb-16a__chip:has(.crb-16a__input:focus-visible) {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

@keyframes crb-16a-spin {
  to {
    --crb16a-a: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-16a__chip:has(.crb-16a__input:checked) .crb-16a__ring::before {
    animation: none;
    background: conic-gradient(var(--neon) 0 100%);
    opacity: .5;
  }

  .crb-16a__ring::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — @property registers --crb16a-a as a real <angle>, so the conic energy arc's start angle animates natively; a radial-gradient mask cuts it into a ring. */
```
