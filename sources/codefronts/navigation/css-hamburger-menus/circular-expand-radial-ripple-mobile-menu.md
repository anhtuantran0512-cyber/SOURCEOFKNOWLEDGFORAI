---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/circular-expand-radial-ripple-mobile-menu/"
title: "Radial Ripple Expand Mobile Hamburger Menu CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Five action buttons fan out along a perfect quarter-circle arc from the corner toggle, their positions computed by the browser itself — CSS sin() and cos()…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radial Ripple Expand Mobile Hamburger Menu CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/circular-expand-radial-ripple-mobile-menu/

Five action buttons fan out along a perfect quarter-circle arc from the corner toggle, their positions computed by the browser itself — CSS sin() and cos() turn an index and a radius into coordinates, no JS math, no hand-tuned magic offsets. Three ripple rings pulse outward behind the fan as it opens. Fully checkbox-driven: the entire radial system, ripples included, runs on :has() and custom-property trigonometry.
## HTML
```html
<section class="chm-24" aria-label="Radial ripple fan menu demo">
  <div class="chm-24__stage">
    <input type="checkbox" id="chm24-t" class="chm-24__state">
    <div class="chm-24__page" aria-hidden="true">
      <div class="chm-24__map"></div>
      <div class="chm-24__pin" style="--x:24%;--y:30%"></div>
      <div class="chm-24__pin" style="--x:62%;--y:22%"></div>
      <div class="chm-24__pin" style="--x:45%;--y:56%"></div>
    </div>
    <div class="chm-24__ripples" aria-hidden="true"><i></i><i></i><i></i></div>
    <nav class="chm-24__fan" aria-label="Quick actions">
      <a href="#route" class="chm-24__item" style="--i:0"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H14a3 3 0 0 0 0-6h-4a3 3 0 0 1 0-6h5.5"/></svg><span>Route</span></a>
      <a href="#layers" class="chm-24__item" style="--i:1"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5Z"/><path d="m5.5 11.5-2.5 1.5 9 5 9-5-2.5-1.5"/></svg><span>Layers</span></a>
      <a href="#pin" class="chm-24__item" style="--i:2"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-6.5-5.5-6.5-11a6.5 6.5 0 0 1 13 0C18.5 15.5 12 21 12 21Z"/><circle cx="12" cy="10" r="2.2"/></svg><span>Drop pin</span></a>
      <a href="#measure" class="chm-24__item" style="--i:3"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m4 17 13-13 3 3-13 13H4Z"/><path d="m9.5 8.5 1.5 1.5M12.5 5.5 14 7"/></svg><span>Measure</span></a>
      <a href="#share" class="chm-24__item" style="--i:4"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="m8.3 10.8 7.4-3.6M8.3 13.2l7.4 3.6"/></svg><span>Share</span></a>
    </nav>
    <label for="chm24-t" class="chm-24__toggle"><span aria-hidden="true"><i></i><i></i><i></i></span></label>
  </div>
</section>
```
## CSS
```css
.chm-24,
.chm-24 *,
.chm-24 *::before,
.chm-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-24 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.23 0.03 250);
  --ink: oklch(0.95 0.008 250);
  --acc: oklch(0.8 0.15 150);
  --acc2: oklch(0.7 0.14 210);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-24__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 520px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid oklch(0.33 0.03 250);
}

.chm-24__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-24__page {
  position: absolute;
  inset: 0;
}

.chm-24__map {
  position: absolute;
  inset: 0;
  background: radial-gradient(120% 90% at 70% 20%,oklch(0.3 0.05 230/.8),transparent 55%),repeating-linear-gradient(0deg,transparent 0 46px,oklch(1 0 0/.045) 46px 47px),repeating-linear-gradient(90deg,transparent 0 46px,oklch(1 0 0/.045) 46px 47px),var(--bg);
}

.chm-24__map::after {
  content: "";
  position: absolute;
  left: -10%;
  top: 30%;
  width: 120%;
  height: 90px;
  background: oklch(0.45 0.07 230/.35);
  rotate: -14deg;
  border-radius: 99px;
  filter: blur(2px);
}

.chm-24__pin {
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: 11px;
  height: 11px;
  border-radius: 50% 50% 50% 0;
  rotate: -45deg;
  background: var(--acc2);
  box-shadow: 0 0 0 3px oklch(0.7 0.14 210/.25);
}

.chm-24__ripples {
  position: absolute;
  right: 44px;
  bottom: 44px;
  width: 0;
  height: 0;
  pointer-events: none;
}

.chm-24__ripples i {
  position: absolute;
  left: -54px;
  top: -54px;
  width: 108px;
  height: 108px;
  border-radius: 50%;
  border: 1.5px solid color-mix(in oklch,var(--acc) 60%,transparent);
  scale: .3;
  opacity: 0;
}

.chm-24:has(#chm24-t:checked) .chm-24__ripples i {
  animation: chm24-ripple 1s cubic-bezier(.2,.7,.3,1) forwards;
}

.chm-24:has(#chm24-t:checked) .chm-24__ripples i:nth-child(2) {
  animation-delay: .12s;
}

.chm-24:has(#chm24-t:checked) .chm-24__ripples i:nth-child(3) {
  animation-delay: .24s;
}

@keyframes chm24-ripple {
  0% {
    scale: .3;
    opacity: .9;
  }

  100% {
    scale: 2.6;
    opacity: 0;
  }
}

.chm-24__fan {
  position: absolute;
  right: 44px;
  bottom: 44px;
  width: 0;
  height: 0;
}

.chm-24__item {
  --n: 5;
  --arc: 90deg;
  --a: calc(90deg + (var(--i) / (var(--n) - 1)) * var(--arc));
  --r: 108px;
  position: absolute;
  left: -24px;
  top: -24px;
  width: 48px;
  height: 48px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: oklch(0.3 0.035 250);
  border: 1px solid oklch(0.42 0.04 250);
  color: var(--ink);
  text-decoration: none;
  translate: 0 0;
  scale: .4;
  opacity: 0;
  pointer-events: none;
  transition: translate .5s cubic-bezier(.25,1.3,.35,1),scale .4s cubic-bezier(.25,1.3,.35,1),opacity .25s,background .2s,border-color .2s;
}

.chm-24__item svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.chm-24__item span {
  position: absolute;
  right: calc(100% + 10px);
  top: 50%;
  translate: 0 -50%;
  font-size: 11.5px;
  font-weight: 700;
  white-space: nowrap;
  background: oklch(0.95 0.008 250);
  color: oklch(0.22 0.02 250);
  border-radius: 7px;
  padding: 5px 10px;
  opacity: 0;
  scale: .9;
  transition: opacity .15s,scale .15s;
  pointer-events: none;
}

.chm-24__item:hover span,
.chm-24__item:focus-visible span {
  opacity: 1;
  scale: 1;
}

.chm-24:has(#chm24-t:checked) .chm-24__item {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r) * -1);
  scale: 1;
  opacity: 1;
  pointer-events: auto;
  transition-delay: calc(var(--i)*45ms),calc(var(--i)*45ms),calc(var(--i)*45ms),0s,0s;
}

.chm-24__item:hover,
.chm-24__item:focus-visible {
  background: oklch(0.36 0.05 250);
  border-color: var(--acc);
}

.chm-24__item:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-24__toggle {
  position: absolute;
  right: 16px;
  bottom: 16px;
  width: 56px;
  height: 56px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: linear-gradient(150deg,var(--acc),oklch(0.62 0.14 190));
  color: oklch(0.15 0.03 250);
  cursor: pointer;
  box-shadow: 0 16px 32px -12px color-mix(in oklch,var(--acc) 55%,transparent);
  transition: rotate .4s cubic-bezier(.25,1.3,.35,1),scale .2s;
}

.chm-24__toggle:hover {
  scale: 1.06;
}

.chm-24__toggle:active {
  scale: .94;
}

.chm-24__state:focus-visible ~ .chm-24__toggle {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-24:has(#chm24-t:checked) .chm-24__toggle {
  rotate: 135deg;
}

.chm-24__toggle span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-24__toggle i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2.2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-24__toggle i:nth-child(1) {
  top: 0;
}

.chm-24__toggle i:nth-child(2) {
  top: 5px;
}

.chm-24__toggle i:nth-child(3) {
  top: 10px;
}

.chm-24:has(#chm24-t:checked) .chm-24__toggle i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

.chm-24:has(#chm24-t:checked) .chm-24__toggle i:nth-child(2) {
  opacity: 0;
}

.chm-24:has(#chm24-t:checked) .chm-24__toggle i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

@media (prefers-reduced-motion: reduce) {
  .chm-24 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
    animation: none !important;
  }
}
```
