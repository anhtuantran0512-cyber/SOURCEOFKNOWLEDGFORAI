---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/iris-aperture/"
title: "Camera Iris Aperture Expand Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A lens that opens onto a menu: eight aperture blades — each one skewed element — rotate apart exactly like a real iris diaphragm, revealing six options…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Camera Iris Aperture Expand Menu
Source: https://codefronts.com/navigation/css-circular-menus/iris-aperture/

A lens that opens onto a menu: eight aperture blades — each one skewed element — rotate apart exactly like a real iris diaphragm, revealing six options arranged inside the barrel. The blade mechanics mirror physical apertures: every blade pivots around a point on the barrel's rim, not its own center. Made for photography portfolios and camera products.
## HTML
```html
<section class="ccm-23" aria-label="Camera iris aperture menu demo">
  <div class="ccm-23__stage">
    <div class="ccm-23__barrel" style="--n:8">
      <div class="ccm-23__inner" id="ccm23-menu" style="--m:6">
        <ul class="ccm-23__opts">
          <li style="--i:0"><a href="#portraits">Portraits</a></li>
          <li style="--i:1"><a href="#street">Street</a></li>
          <li style="--i:2"><a href="#nature">Nature</a></li>
          <li style="--i:3"><a href="#studio">Studio</a></li>
          <li style="--i:4"><a href="#film">Film</a></li>
          <li style="--i:5"><a href="#prints">Prints</a></li>
        </ul>
        <span class="ccm-23__fstop" aria-hidden="true">f/1.8</span>
      </div>
      <div class="ccm-23__iris" aria-hidden="true">
        <span class="ccm-23__blade" style="--i:0"><i></i></span>
        <span class="ccm-23__blade" style="--i:1"><i></i></span>
        <span class="ccm-23__blade" style="--i:2"><i></i></span>
        <span class="ccm-23__blade" style="--i:3"><i></i></span>
        <span class="ccm-23__blade" style="--i:4"><i></i></span>
        <span class="ccm-23__blade" style="--i:5"><i></i></span>
        <span class="ccm-23__blade" style="--i:6"><i></i></span>
        <span class="ccm-23__blade" style="--i:7"><i></i></span>
      </div>
      <button type="button" class="ccm-23__shutter" aria-expanded="false" aria-controls="ccm23-menu">Open<br>lens</button>
    </div>
  </div>
</section>
```
## CSS
```css
.ccm-23,
.ccm-23 *,
.ccm-23 *::before,
.ccm-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-23 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 42%,oklch(0.24 0.01 260),oklch(0.15 0.008 260) 75%);
  --t: .7s;
  --brand: oklch(0.78 0.13 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.9 0.005 75);
}

.ccm-23__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 42%,oklch(0.24 0.01 260),oklch(0.15 0.008 260) 75%);
  overflow: hidden;
}

.ccm-23__barrel {
  position: relative;
  width: 380px;
  height: 380px;
  border-radius: 50%;
  background: radial-gradient(circle at 40% 32%,oklch(0.3 0.01 260),oklch(0.18 0.008 260) 70%);
  box-shadow: 0 0 0 10px oklch(0.28 0.01 260),0 0 0 12px oklch(0.4 0.02 75 / .5),0 40px 90px -40px oklch(0 0 0 / .9),inset 0 0 40px oklch(0 0 0 / .6);
  display: grid;
  place-items: center;
  overflow: hidden;
}

.ccm-23__inner {
  position: absolute;
  inset: 26px;
  border-radius: 50%;
  background: radial-gradient(circle at 45% 38%,oklch(0.26 0.02 280),oklch(0.16 0.015 280) 75%);
  clip-path: circle(9% at 50% 50%);
  transition: clip-path var(--t) cubic-bezier(.4,0,.25,1);
  display: grid;
  place-items: center;
}

.ccm-23__barrel.is-open .ccm-23__inner {
  clip-path: circle(50% at 50% 50%);
}

.ccm-23__opts {
  position: absolute;
  inset: 0;
  list-style: none;
}

.ccm-23__opts li {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --a: calc((360deg / var(--m)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * 112px) calc(sin(var(--a)) * 112px);
  opacity: 0;
  scale: .6;
  transition: opacity .3s,scale .4s cubic-bezier(.34,1.3,.4,1);
  transition-delay: 0s;
}

.ccm-23__barrel.is-open .ccm-23__opts li {
  opacity: 1;
  scale: 1;
  transition-delay: calc(var(--t) * .55 + var(--i) * 40ms);
}

.ccm-23__opts a {
  pointer-events: auto;
  display: grid;
  place-items: center;
  min-width: 78px;
  padding: 11px 14px;
  border-radius: 999px;
  background: oklch(1 0 0 / .08);
  border: 1px solid oklch(0.8 0.1 75 / .35);
  color: oklch(0.93 0.02 75);
  text-decoration: none;
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: .04em;
  transition: background .2s,color .2s;
}

.ccm-23__opts a:hover,
.ccm-23__opts a:focus-visible {
  background: var(--brand);
  color: oklch(0.22 0.02 75);
  outline: none;
}

.ccm-23__opts a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.ccm-23__barrel:not(.is-open) .ccm-23__opts a {
  pointer-events: none;
}

.ccm-23__fstop {
  font: 600 13px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .12em;
  color: oklch(0.65 0.08 75);
}

.ccm-23__iris {
  position: absolute;
  inset: 26px;
  border-radius: 50%;
  pointer-events: none;
  overflow: hidden;
  z-index: 1;
}

.ccm-23__inner {
  z-index: 2;
}

.ccm-23__blade {
  position: absolute;
  inset: 0;
  rotate: calc((360deg / var(--n)) * var(--i));
  transition: rotate var(--t) cubic-bezier(.4,0,.25,1);
}

.ccm-23__barrel.is-open .ccm-23__blade {
  rotate: calc((360deg / var(--n)) * var(--i) + 108deg);
}

.ccm-23__blade i {
  position: absolute;
  left: 50%;
  top: -14%;
  width: 58%;
  height: 58%;
  transform-origin: 0% 0%;
  rotate: 24deg;
  border-radius: 0 62% 42% 46%;
  background: linear-gradient(130deg,oklch(0.32 0.01 260),oklch(0.2 0.008 260) 55%,oklch(0.26 0.012 260));
  box-shadow: inset 1px -1px 0 oklch(0.45 0.02 75 / .4),0 4px 10px oklch(0 0 0 / .5);
}

.ccm-23__shutter {
  position: absolute;
  left: 50%;
  bottom: -12px;
  translate: -50% 0;
  z-index: 3;
  width: 86px;
  height: 86px;
  border-radius: 50%;
  border: 3px solid oklch(0.4 0.02 75);
  background: radial-gradient(circle at 38% 30%,oklch(0.34 0.02 75),oklch(0.22 0.015 75));
  color: oklch(0.9 0.06 75);
  font: 700 12.5px/1.25 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .08em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 14px 30px -10px oklch(0 0 0 / .8);
  transition: color .3s,border-color .3s;
}

.ccm-23__shutter:hover {
  border-color: var(--brand);
}

.ccm-23__shutter:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .ccm-23 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const barrel = document.querySelector('.ccm-23__barrel');
  const btn = barrel.querySelector('.ccm-23__shutter');
  const fstop = barrel.querySelector('.ccm-23__fstop');
  const stops = ['f/1.8', 'f/2.8', 'f/4', 'f/5.6', 'f/8'];
  let timer = null;
  btn.addEventListener('click', () => {
    const open = barrel.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', String(open));
    btn.innerHTML = open ? 'Close<br>lens' : 'Open<br>lens';
    clearInterval(timer);
    let k = open ? 0 : stops.length - 1;
    timer = setInterval(() => {
      fstop.textContent = stops[k];
      k += open ? 1 : -1;
      if (k < 0 || k >= stops.length) clearInterval(timer);
    }, 120);
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && barrel.classList.contains('is-open')) btn.click();
  });
})();
```
