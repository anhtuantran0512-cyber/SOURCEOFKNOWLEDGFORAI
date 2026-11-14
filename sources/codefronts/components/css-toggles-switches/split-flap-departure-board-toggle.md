---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/split-flap-departure-board-toggle/"
title: "Split-Flap Departure Board Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "An airport departure-board cell that flips between OFF and ON: the top half of the card hinges down over the bottom in 3D, revealing the new state exactly…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split-Flap Departure Board Toggle
Source: https://codefronts.com/components/css-toggles-switches/split-flap-departure-board-toggle/

An airport departure-board cell that flips between OFF and ON: the top half of the card hinges down over the bottom in 3D, revealing the new state exactly like a mechanical split-flap display — hinge line, half-letters and all. Pure CSS.
## HTML
```html
<section class="tgl-12" aria-label="Split flap board toggle">
  <label class="tgl-12__wrap" for="tgl-12-sw">
    <input type="checkbox" id="tgl-12-sw" class="tgl-12__sw" role="switch">
    <span class="tgl-12__board" aria-hidden="true">
      <b class="tgl-12__half tgl-12__half--topnew"><i>ON</i></b>
      <b class="tgl-12__half tgl-12__half--botold"><i>OFF</i></b>
      <b class="tgl-12__flap"><span class="tgl-12__face tgl-12__face--front"><i>OFF</i></span><span class="tgl-12__face tgl-12__face--back"><i>ON</i></span></b>
      <em class="tgl-12__hinge"></em>
    </span>
    <span class="tgl-12__lbl">Departures feed</span>
  </label>
  <p class="tgl-12__cap">Mechanical split-flap · click to flip</p>
</section>
```
## CSS
```css
.tgl-12,
.tgl-12 *,
.tgl-12 *::before,
.tgl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-12 {
  font-family: ui-monospace,'SF Mono',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 26px;
  padding: 60px 20px;
  background: #14130f;
}

.tgl-12__wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  cursor: pointer;
}

.tgl-12__sw {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.tgl-12__board {
  position: relative;
  width: 150px;
  height: 96px;
  perspective: 500px;
  filter: drop-shadow(0 14px 24px rgba(0,0,0,.6));
}

.tgl-12__half,
.tgl-12__face {
  position: absolute;
  left: 0;
  width: 150px;
  height: 48px;
  overflow: hidden;
  background: #242220;
  color: #f5d97a;
  font-size: 44px;
  font-weight: 700;
  letter-spacing: .04em;
  text-align: center;
}

.tgl-12__half i,
.tgl-12__face i {
  font-style: normal;
  display: block;
  line-height: 96px;
}

.tgl-12__half--topnew {
  top: 0;
  border-radius: 8px 8px 0 0;
}

.tgl-12__half--botold {
  top: 48px;
  border-radius: 0 0 8px 8px;
  background: #1e1c1a;
}

.tgl-12__half--botold i,
.tgl-12__face--back i {
  transform: translateY(-48px);
}

.tgl-12__flap {
  position: absolute;
  top: 0;
  left: 0;
  width: 150px;
  height: 48px;
  transform-style: preserve-3d;
  transform-origin: bottom;
  transition: transform .6s cubic-bezier(.4,0,.6,1);
}

.tgl-12__sw:checked ~ .tgl-12__board .tgl-12__flap {
  transform: rotateX(-180deg);
}

.tgl-12__face {
  top: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border-radius: 8px 8px 0 0;
}

.tgl-12__face--back {
  transform: rotateX(180deg);
  background: #1e1c1a;
  border-radius: 0 0 8px 8px;
}

.tgl-12__hinge {
  position: absolute;
  top: 47px;
  left: 0;
  right: 0;
  height: 2px;
  background: #0d0c0a;
  z-index: 5;
}

.tgl-12__hinge::before,
.tgl-12__hinge::after {
  content: "";
  position: absolute;
  top: -4px;
  width: 5px;
  height: 10px;
  background: #0d0c0a;
  border-radius: 2px;
}

.tgl-12__hinge::before {
  left: -2px;
}

.tgl-12__hinge::after {
  right: -2px;
}

.tgl-12__lbl {
  font-size: 13px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #8d8672;
}

.tgl-12__sw:focus-visible ~ .tgl-12__board {
  outline: 3px solid #f5d97a;
  outline-offset: 5px;
  border-radius: 10px;
}

.tgl-12__cap {
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #57523f;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-12__flap {
    transition: transform .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hinged flap with front/back half-word faces rotates -180° inside a perspective parent, exactly like a mechanical split-flap cell. */
```
