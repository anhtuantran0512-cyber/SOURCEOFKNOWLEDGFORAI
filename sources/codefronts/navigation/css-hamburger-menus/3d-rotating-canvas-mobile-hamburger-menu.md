---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/3d-rotating-canvas-mobile-hamburger-menu/"
title: "3D Flip Canvas Mobile Hamburger Navigation CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The theatrical finale: open the menu and the entire page tilts back in 3D — rotateY around its right edge with real perspective — swinging aside like a door…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Canvas Mobile Hamburger Navigation CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/3d-rotating-canvas-mobile-hamburger-menu/

The theatrical finale: open the menu and the entire page tilts back in 3D — rotateY around its right edge with real perspective — swinging aside like a door to reveal the nav standing behind it, whose links counter-rotate into place from the opposite angle. Three properties (perspective, transform-origin, preserve-3d) produce the drama; the layering discipline of demo 08 keeps it usable. The push menu's flamboyant sibling, for portfolios that want an entrance.
## HTML
```html
<section class="chm-28" aria-label="3D flip canvas navigation demo">
  <div class="chm-28__viewport">
    <nav class="chm-28__menu" id="chm28-menu" aria-label="Site">
      <b class="chm-28__title" style="--i:0">Menu</b>
      <a href="#work" style="--i:1">Selected work</a>
      <a href="#reel" style="--i:2">Show reel</a>
      <a href="#process" style="--i:3">Process</a>
      <a href="#studio" style="--i:4">Studio</a>
      <a href="#contact" style="--i:5">Contact</a>
      <span class="chm-28__foot" style="--i:6">© 2026 — Antwerp</span>
    </nav>
    <div class="chm-28__canvas" id="chm28-canvas">
      <header class="chm-28__bar">
        <span class="chm-28__brand">DEPTH.WORKS</span>
        <button class="chm-28__btn" type="button" aria-expanded="false" aria-controls="chm28-menu" aria-label="Open menu"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
      </header>
      <div class="chm-28__content" aria-hidden="true">
        <div class="chm-28__poster"><span>MOTION<br>&amp; SPACE</span></div>
        <div class="chm-28__ln" style="--w:74%"></div>
        <div class="chm-28__ln" style="--w:58%"></div>
      </div>
    </div>
    <button class="chm-28__catch" type="button" tabindex="-1" aria-hidden="true"></button>
  </div>
</section>
```
## CSS
```css
.chm-28,
.chm-28 *,
.chm-28 *::before,
.chm-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-28 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.17 0.03 310);
  --page: oklch(0.96 0.006 310);
  --ink: oklch(0.24 0.02 310);
  --mut: oklch(0.55 0.015 310);
  --acc: oklch(0.75 0.17 340);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-28__viewport {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: radial-gradient(130% 100% at 90% 50%,oklch(0.25 0.06 320/.85),transparent 60%),var(--bg);
  border: 1px solid oklch(0.3 0.04 310);
  perspective: 1400px;
}

.chm-28__menu {
  position: absolute;
  inset: 0 0 0 44%;
  padding: 34px 26px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  color: oklch(0.94 0.01 320);
  transform: rotateY(18deg) translateX(40px);
  opacity: .35;
  transition: transform .6s cubic-bezier(.4,0,.2,1),opacity .5s;
}

[data-open] .chm-28__menu {
  transform: rotateY(0) translateX(0);
  opacity: 1;
}

.chm-28__title {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 16px;
}

.chm-28__menu a {
  padding: 12px 0;
  font-size: 21px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: oklch(0.94 0.01 320);
  text-decoration: none;
  border-bottom: 1px solid oklch(1 0 0/.1);
  opacity: 0;
  translate: 18px 0;
  transition: opacity .35s,translate .45s cubic-bezier(.2,.7,.2,1),color .2s;
}

[data-open] .chm-28__menu a {
  opacity: 1;
  translate: 0 0;
  transition-delay: calc(.15s + var(--i)*.05s),calc(.15s + var(--i)*.05s),0s;
}

.chm-28__menu a:hover,
.chm-28__menu a:focus-visible {
  color: var(--acc);
}

.chm-28__menu a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
  border-radius: 4px;
}

.chm-28__foot {
  margin-top: auto;
  font-size: 11.5px;
  color: oklch(0.62 0.03 320);
  opacity: 0;
  transition: opacity .4s .45s;
}

[data-open] .chm-28__foot {
  opacity: 1;
}

.chm-28__canvas {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: var(--page);
  display: flex;
  flex-direction: column;
  transform-origin: 88% 50%;
  transform: none;
  transition: transform .6s cubic-bezier(.4,0,.2,1),box-shadow .6s,border-radius .6s;
}

[data-open] .chm-28__canvas {
  transform: translateX(-58%) rotateY(34deg) scale(.92);
  box-shadow: 40px 30px 80px -30px oklch(0.08 0.03 310/.8);
  border-radius: 18px;
}

.chm-28__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 68px;
  padding: 0 18px 0 24px;
  border-bottom: 1px solid oklch(0.88 0.01 310);
}

.chm-28__brand {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .24em;
}

.chm-28__btn {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: none;
  border-radius: 12px;
  background: var(--ink);
  color: var(--page);
  cursor: pointer;
  transition: background .25s,scale .2s;
}

.chm-28__btn:hover {
  scale: 1.05;
}

.chm-28__btn:active {
  scale: .93;
}

.chm-28__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-28__btn span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-28__btn i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-28__btn i:nth-child(1) {
  top: 0;
}

.chm-28__btn i:nth-child(2) {
  top: 5px;
}

.chm-28__btn i:nth-child(3) {
  top: 10px;
}

[data-open] .chm-28__btn i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

[data-open] .chm-28__btn i:nth-child(2) {
  opacity: 0;
}

[data-open] .chm-28__btn i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-28__content {
  flex: 1;
  padding: 22px;
  display: grid;
  gap: 14px;
  align-content: start;
}

.chm-28__poster {
  height: 250px;
  border-radius: 16px;
  background: linear-gradient(155deg,oklch(0.85 0.06 330),oklch(0.62 0.16 320));
  display: grid;
  align-content: end;
  padding: 20px;
}

.chm-28__poster span {
  font-size: 30px;
  font-weight: 800;
  line-height: 1.02;
  letter-spacing: -.02em;
  color: oklch(0.2 0.05 320);
}

.chm-28__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.89 0.008 310);
}

.chm-28__catch {
  position: absolute;
  inset: 0 56% 0 0;
  z-index: 5;
  display: none;
  border: none;
  background: transparent;
  cursor: e-resize;
}

[data-open] .chm-28__catch {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .chm-28 [data-open] .chm-28__canvas {
    transform: translateX(-58%);
  }

  .chm-28 .chm-28__menu {
    transform: none;
  }

  .chm-28 * {
    transition-duration: .15s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-28__viewport').forEach(function (vp) {
    if (vp.dataset.bound) return; vp.dataset.bound = '1';
    var btn = vp.querySelector('.chm-28__btn'), canvas = vp.querySelector('.chm-28__canvas');
    function set(open) {
      vp.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) { canvas.setAttribute('inert', ''); vp.querySelector('.chm-28__menu a').focus(); }
      else { canvas.removeAttribute('inert'); btn.focus(); }
    }
    btn.addEventListener('click', function () { set(true); });
    vp.querySelector('.chm-28__catch').addEventListener('click', function () { set(false); });
    vp.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && vp.hasAttribute('data-open')) set(false);
    });
  });
})();
```
