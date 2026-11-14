---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/industrial-rocker-i-o-switch/"
title: "Industrial Rocker I/O Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The power switch off the back of real hardware: a rectangular rocker with engraved I and O halves seesawing inside a riveted steel panel, plus a red pilot…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Industrial Rocker I/O Switch
Source: https://codefronts.com/components/css-toggles-switches/industrial-rocker-i-o-switch/

The power switch off the back of real hardware: a rectangular rocker with engraved I and O halves seesawing inside a riveted steel panel, plus a red pilot lamp that ignites on power. Perspective, gradients and text-shadow do all the machining.
## HTML
```html
<section class="tgl-26" aria-label="Industrial rocker power switch">
  <div class="tgl-26__panel">
    <span class="tgl-26__rivet" style="top:8px;left:8px" aria-hidden="true"></span><span class="tgl-26__rivet" style="top:8px;right:8px" aria-hidden="true"></span><span class="tgl-26__rivet" style="bottom:8px;left:8px" aria-hidden="true"></span><span class="tgl-26__rivet" style="bottom:8px;right:8px" aria-hidden="true"></span>
    <span class="tgl-26__lamp" aria-hidden="true"></span>
    <span class="tgl-26__well">
      <input type="checkbox" id="tgl-26-sw" class="tgl-26__sw" role="switch" aria-label="Main power">
      <label class="tgl-26__rocker" for="tgl-26-sw" aria-hidden="true"><i>I</i><i>O</i></label>
    </span>
    <span class="tgl-26__tag">MAIN PWR</span>
  </div>
  <p class="tgl-26__cap">IEC rocker · I = on, O = off</p>
</section>
```
## CSS
```css
.tgl-26,
.tgl-26 *,
.tgl-26 *::before,
.tgl-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-26 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
  padding: 60px 20px;
  background: #1f2126;
}

.tgl-26__panel {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding: 34px 44px 22px;
  border-radius: 10px;
  background: repeating-linear-gradient(92deg,#585d66 0 2px,#4e535c 2px 4px);
  box-shadow: 0 22px 46px -20px #000,inset 0 1px 0 rgba(255,255,255,.18),inset 0 -2px 4px rgba(0,0,0,.4);
}

.tgl-26__rivet {
  position: absolute;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,#9aa0aa,#4a4f58);
  box-shadow: inset 0 -1px 2px rgba(0,0,0,.6);
}

.tgl-26__lamp {
  position: absolute;
  top: 14px;
  right: 22px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #3d2426;
  box-shadow: inset 0 1px 3px rgba(0,0,0,.8);
  transition: background-color .2s,box-shadow .2s;
}

.tgl-26__panel:has(.tgl-26__sw:checked) .tgl-26__lamp {
  background: oklch(0.62 0.22 25);
  box-shadow: 0 0 8px oklch(0.62 0.22 25),0 0 20px oklch(0.62 0.22 25 / .5);
}

.tgl-26__well {
  display: block;
  width: 60px;
  height: 112px;
  border-radius: 7px;
  background: #191b1f;
  box-shadow: inset 0 3px 8px rgba(0,0,0,.85),inset 0 0 0 2px #101114;
  padding: 5px;
  perspective: 280px;
  position: relative;
}

.tgl-26__sw {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.tgl-26__rocker {
  display: grid;
  grid-template-rows: 1fr 1fr;
  width: 100%;
  height: 100%;
  border-radius: 5px;
  background: linear-gradient(180deg,#2c2f35,#3a3e46 50%,#22252a);
  cursor: pointer;
  transform: rotateX(-16deg);
  transform-origin: center;
  transition: transform .16s cubic-bezier(.5,1.5,.6,1),background .16s;
}

.tgl-26__sw:checked ~ .tgl-26__rocker {
  transform: rotateX(16deg);
  background: linear-gradient(0deg,#2c2f35,#3a3e46 50%,#22252a);
}

.tgl-26__rocker i {
  display: grid;
  place-items: center;
  font-style: normal;
  font-size: 17px;
  font-weight: 800;
  color: #878d99;
  text-shadow: 0 -1px 1px rgba(0,0,0,.8),0 1px 1px rgba(255,255,255,.15);
}

.tgl-26__sw:checked ~ .tgl-26__rocker i:first-child {
  color: #cdd3dd;
}

.tgl-26__sw:not(:checked) ~ .tgl-26__rocker i:last-child {
  color: #cdd3dd;
}

.tgl-26__sw:focus-visible ~ .tgl-26__rocker {
  outline: 3px solid oklch(0.7 0.15 220);
  outline-offset: 5px;
}

.tgl-26__tag {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .24em;
  color: #20232a;
  background: #b8bdc6;
  padding: 3px 10px;
  border-radius: 3px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6);
}

.tgl-26__cap {
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #5a5f68;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-26__rocker {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the rocker seesaws rotateX(-16°→16°) in a perspective well while gradient shading flips; :has() ignites the pilot lamp. */
```
