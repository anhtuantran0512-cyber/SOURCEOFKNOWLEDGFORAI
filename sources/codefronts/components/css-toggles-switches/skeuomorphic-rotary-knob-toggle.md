---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/skeuomorphic-rotary-knob-toggle/"
title: "Skeuomorphic Rotary Knob Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A machined aluminum knob that rotates between OFF and ON detents: brushed-metal conic sheen, a milled indicator line, tick marks on the bezel, and a pilot…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeuomorphic Rotary Knob Toggle
Source: https://codefronts.com/components/css-toggles-switches/skeuomorphic-rotary-knob-toggle/

A machined aluminum knob that rotates between OFF and ON detents: brushed-metal conic sheen, a milled indicator line, tick marks on the bezel, and a pilot LED that ignites at the ON detent. The checkbox IS the knob — click or Space twists it.
## HTML
```html
<section class="tgl-22" aria-label="Rotary knob toggle">
  <div class="tgl-22__unit">
    <span class="tgl-22__legend tgl-22__legend--off" aria-hidden="true">OFF</span>
    <span class="tgl-22__bezel">
      <input type="checkbox" id="tgl-22-sw" class="tgl-22__sw" role="switch" aria-label="Amplifier power">
    </span>
    <span class="tgl-22__legend tgl-22__legend--on" aria-hidden="true">ON</span>
    <span class="tgl-22__led" aria-hidden="true"></span>
  </div>
  <p class="tgl-22__cap">Machined detent · click to twist</p>
</section>
```
## CSS
```css
.tgl-22,
.tgl-22 *,
.tgl-22 *::before,
.tgl-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-22 {
  --led: oklch(0.75 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
  padding: 60px 20px;
  background: #26282c;
}

.tgl-22__unit {
  position: relative;
  display: flex;
  align-items: flex-end;
  gap: 14px;
  padding: 26px 22px 20px;
  border-radius: 18px;
  background: linear-gradient(170deg,#33363c,#2a2c31);
  box-shadow: 0 20px 44px -22px #000,inset 0 1px 0 rgba(255,255,255,.07);
}

.tgl-22__legend {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  color: #7d828c;
  padding-bottom: 34px;
}

.tgl-22__bezel {
  position: relative;
  display: grid;
  place-items: center;
  width: 104px;
  height: 104px;
  border-radius: 50%;
  background: radial-gradient(circle,#1d1f23 58%,#3a3d44 60%,#22242a 100%);
  box-shadow: inset 0 2px 6px rgba(0,0,0,.7);
}

.tgl-22__bezel::before,
.tgl-22__bezel::after {
  content: "";
  position: absolute;
  bottom: 6px;
  width: 2px;
  height: 7px;
  background: #6a6f7a;
  border-radius: 1px;
}

.tgl-22__bezel::before {
  left: 14px;
  transform: rotate(38deg);
}

.tgl-22__bezel::after {
  right: 14px;
  transform: rotate(-38deg);
}

.tgl-22__sw {
  appearance: none;
  -webkit-appearance: none;
  width: 88px;
  height: 88px;
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  background: radial-gradient(circle at 32% 26%,rgba(255,255,255,.35),transparent 46%),conic-gradient(#b9bec8 0 8%,#8d939e 8% 16%,#b3b8c2 16% 24%,#878d98 24% 32%,#b9bec8 32% 40%,#8d939e 40% 48%,#b3b8c2 48% 56%,#878d98 56% 64%,#b9bec8 64% 72%,#8d939e 72% 80%,#b3b8c2 80% 88%,#878d98 88% 96%,#b9bec8 96% 100%);
  box-shadow: 0 6px 14px rgba(0,0,0,.6),inset 0 -3px 6px rgba(0,0,0,.35),inset 0 2px 3px rgba(255,255,255,.5);
  transform: rotate(-32deg);
  transition: transform .35s cubic-bezier(.3,1.4,.4,1);
}

.tgl-22__sw:checked {
  transform: rotate(32deg);
}

.tgl-22__sw:active {
  transform: rotate(-32deg) scale(.97);
}

.tgl-22__sw:checked:active {
  transform: rotate(32deg) scale(.97);
}

.tgl-22__sw::before {
  content: "";
  position: absolute;
  top: 7px;
  left: 50%;
  width: 5px;
  height: 22px;
  margin-left: -2.5px;
  border-radius: 3px;
  background: #22242a;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.8),0 1px 0 rgba(255,255,255,.3);
}

.tgl-22__led {
  position: absolute;
  top: 14px;
  right: 16px;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #3a3026;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.7);
  transition: background-color .25s,box-shadow .25s;
}

.tgl-22__unit:has(.tgl-22__sw:checked) .tgl-22__led {
  background: var(--led);
  box-shadow: 0 0 7px var(--led),0 0 16px color-mix(in oklab,var(--led) 55%,transparent);
}

.tgl-22__sw:focus-visible {
  outline: 3px solid oklch(0.7 0.15 220);
  outline-offset: 5px;
}

.tgl-22__cap {
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #5b6068;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-22__sw {
    transition: transform .12s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the round checkbox rotates -32°→32° with a detent bezier; conic-gradient machining turns with it while ticks, legends and the LED stay fixed. */
```
