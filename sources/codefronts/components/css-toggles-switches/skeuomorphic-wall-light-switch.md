---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/skeuomorphic-wall-light-switch/"
title: "Skeuomorphic Wall Light Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A realistic wall-plate rocker switch — beveled plate, screw heads, a paddle that tips in 3D perspective — and when you flip it, the whole room warms up: the…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeuomorphic Wall Light Switch
Source: https://codefronts.com/components/css-toggles-switches/skeuomorphic-wall-light-switch/

A realistic wall-plate rocker switch — beveled plate, screw heads, a paddle that tips in 3D perspective — and when you flip it, the whole room warms up: the section's ambient light brightens via :has(). Skeuomorphism with a functional payoff.
## HTML
```html
<section class="tgl-15" aria-label="Skeuomorphic wall light switch">
  <span class="tgl-15__glow" aria-hidden="true"></span>
  <div class="tgl-15__plate">
    <span class="tgl-15__screw tgl-15__screw--top" aria-hidden="true"></span>
    <span class="tgl-15__well">
      <input type="checkbox" id="tgl-15-sw" class="tgl-15__sw" role="switch" aria-label="Room light">
      <label class="tgl-15__paddle" for="tgl-15-sw" aria-hidden="true"></label>
    </span>
    <span class="tgl-15__screw tgl-15__screw--bot" aria-hidden="true"></span>
  </div>
  <p class="tgl-15__cap">Flip it — the room lights up</p>
</section>
```
## CSS
```css
.tgl-15,
.tgl-15 *,
.tgl-15 *::before,
.tgl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-15 {
  --dusk: #2b2e38;
  --lamp: #f0e2c4;
  position: relative;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 30px;
  padding: 60px 20px;
  background: var(--dusk);
  transition: background-color .8s;
  overflow: hidden;
}

.tgl-15:has(.tgl-15__sw:checked) {
  background: var(--lamp);
}

.tgl-15__glow {
  position: absolute;
  top: 8%;
  left: 50%;
  width: 420px;
  height: 420px;
  transform: translateX(-50%);
  border-radius: 50%;
  background: radial-gradient(circle,rgba(255,214,130,.55),transparent 65%);
  opacity: 0;
  transition: opacity .8s;
  pointer-events: none;
}

.tgl-15:has(.tgl-15__sw:checked) .tgl-15__glow {
  opacity: 1;
}

.tgl-15__plate {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: 128px;
  padding: 22px 0;
  border-radius: 12px;
  background: linear-gradient(170deg,#f4f1ea,#d9d4c8);
  box-shadow: inset 0 2px 0 rgba(255,255,255,.9),inset 0 -3px 5px rgba(90,80,60,.35),0 18px 34px -14px rgba(0,0,0,.55);
}

.tgl-15__screw {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,#e8e4da,#a09a8c);
  box-shadow: inset 0 -1px 2px rgba(60,50,30,.5);
  position: relative;
}

.tgl-15__screw::before {
  content: "";
  position: absolute;
  top: 4.5px;
  left: 1.5px;
  right: 1.5px;
  height: 1.5px;
  background: #6e685c;
  border-radius: 1px;
  transform: rotate(-38deg);
}

.tgl-15__screw--bot::before {
  transform: rotate(24deg);
}

.tgl-15__well {
  display: block;
  width: 58px;
  height: 104px;
  border-radius: 8px;
  background: #c9c3b5;
  box-shadow: inset 0 3px 7px rgba(70,60,40,.55);
  padding: 5px;
  perspective: 300px;
  position: relative;
}

.tgl-15__sw {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.tgl-15__paddle {
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 6px;
  background: linear-gradient(180deg,#cfc9bb,#f6f3ec 55%,#efece3);
  box-shadow: 0 4px 8px rgba(60,50,30,.4),inset 0 1px 0 rgba(255,255,255,.8);
  cursor: pointer;
  transform: rotateX(14deg);
  transform-origin: center;
  transition: transform .22s cubic-bezier(.5,1.4,.6,1),background .22s;
}

.tgl-15__sw:checked ~ .tgl-15__paddle {
  transform: rotateX(-14deg);
  background: linear-gradient(0deg,#cfc9bb,#f6f3ec 55%,#efece3);
}

.tgl-15__sw:focus-visible ~ .tgl-15__paddle {
  outline: 3px solid oklch(0.65 0.16 250);
  outline-offset: 4px;
}

.tgl-15__cap {
  position: relative;
  z-index: 1;
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #8b8a94;
  transition: color .8s;
}

.tgl-15:has(.tgl-15__sw:checked) .tgl-15__cap {
  color: #8d7f5e;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-15,
    .tgl-15__glow,
    .tgl-15__paddle,
    .tgl-15__cap {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a perspective-tipped paddle rocks rotateX(14deg → -14deg), and :has(:checked) on the section relights the whole room. */
```
