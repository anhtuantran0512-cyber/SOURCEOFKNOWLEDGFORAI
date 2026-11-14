---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/pure-css-radial-submenu-sin-and-cos/"
title: "Pure CSS Radial Submenu (sin() & cos())"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "Zero JavaScript."
has_js: "false"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Radial Submenu (sin() & cos())
Source: https://codefronts.com/navigation/css-circular-menus/pure-css-radial-submenu-sin-and-cos/

Zero JavaScript. A hidden checkbox drives the open state, and CSS trigonometric functions — sin() and cos(), shipped in every 2023+ browser — place six links on a perfect ring. This is the reference implementation to learn radial math from: one angle formula, one radius token, and the whole menu is generative.
## HTML
```html
<section class="ccm-02" aria-label="Pure CSS radial submenu demo">
  <div class="ccm-02__stage">
    <div class="ccm-02__hub" style="--n:6">
      <input type="checkbox" id="ccm02-t" class="ccm-02__state">
      <ul class="ccm-02__orbit">
        <li class="ccm-02__item" style="--i:0"><a href="#home" aria-label="Home"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 11l8-7 8 7v9h-5v-6h-6v6H4z"/></svg></a></li>
        <li class="ccm-02__item" style="--i:1"><a href="#search" aria-label="Search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/></svg></a></li>
        <li class="ccm-02__item" style="--i:2"><a href="#stats" aria-label="Analytics"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 20V10M12 20V4M19 20v-7"/></svg></a></li>
        <li class="ccm-02__item" style="--i:3"><a href="#chat" aria-label="Messages"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg></a></li>
        <li class="ccm-02__item" style="--i:4"><a href="#saved" aria-label="Saved"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h12v17l-6-4-6 4z"/></svg></a></li>
        <li class="ccm-02__item" style="--i:5"><a href="#settings" aria-label="Settings"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg></a></li>
      </ul>
      <label for="ccm02-t" class="ccm-02__toggle"><span class="ccm-02__bar"></span><span class="ccm-02__sr">Toggle menu</span></label>
    </div>
    <p class="ccm-02__note">No JavaScript on this one — inspect it.</p>
  </div>
</section>
```
## CSS
```css
.ccm-02,
.ccm-02 *,
.ccm-02 *::before,
.ccm-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-02 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 40%,oklch(0.35 0.06 175),oklch(0.22 0.04 190));
  --brand: oklch(0.7 0.16 160);
  --deep: oklch(0.28 0.05 170);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-02__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 40%,oklch(0.35 0.06 175),oklch(0.22 0.04 190));
  overflow: hidden;
}

.ccm-02__hub {
  position: relative;
  width: 64px;
  height: 64px;
}

.ccm-02__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-02__toggle {
  position: absolute;
  inset: 0;
  z-index: 2;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--brand);
  color: var(--deep);
  cursor: pointer;
  box-shadow: 0 10px 30px -8px oklch(0.7 0.16 160 / .6);
  transition: rotate .4s cubic-bezier(.34,1.3,.4,1);
}

.ccm-02__bar {
  position: relative;
  width: 22px;
  height: 2.5px;
  border-radius: 2px;
  background: currentColor;
  transition: rotate .35s;
}

.ccm-02__bar::before,
.ccm-02__bar::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 2px;
  background: currentColor;
  transition: translate .35s,rotate .35s;
}

.ccm-02__bar::before {
  translate: 0 -7px;
}

.ccm-02__bar::after {
  translate: 0 7px;
}

.ccm-02__hub:has(:checked) .ccm-02__toggle {
  rotate: 90deg;
}

.ccm-02__hub:has(:checked) .ccm-02__bar {
  rotate: 45deg;
}

.ccm-02__hub:has(:checked) .ccm-02__bar::before {
  translate: 0 0;
  rotate: -90deg;
}

.ccm-02__hub:has(:checked) .ccm-02__bar::after {
  translate: 0 0;
  opacity: 0;
}

.ccm-02__hub:has(.ccm-02__state:focus-visible) .ccm-02__toggle {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.ccm-02__orbit {
  position: absolute;
  inset: 0;
  list-style: none;
  --r: 0px;
  transition: --r .5s;
}

.ccm-02__item {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
  opacity: 0;
  scale: .4;
  visibility: hidden;
  transition: translate .5s cubic-bezier(.34,1.35,.45,1),opacity .3s,scale .5s cubic-bezier(.34,1.35,.45,1),visibility 0s .5s;
  transition-delay: calc(var(--i) * 35ms);
}

.ccm-02__hub:has(:checked) .ccm-02__item {
  --r: 120px;
  opacity: 1;
  scale: 1;
  visibility: visible;
  transition: translate .5s cubic-bezier(.34,1.35,.45,1),opacity .3s,scale .5s cubic-bezier(.34,1.35,.45,1),visibility 0s;
  transition-delay: calc(var(--i) * 45ms);
}

.ccm-02__item a {
  pointer-events: auto;
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: oklch(0.98 0.01 160 / .1);
  border: 1px solid oklch(0.9 0.05 160 / .25);
  backdrop-filter: blur(6px);
  color: oklch(0.92 0.04 160);
  transition: background .25s,color .25s,scale .25s;
}

.ccm-02__item a:hover,
.ccm-02__item a:focus-visible {
  background: var(--brand);
  color: var(--deep);
  scale: 1.12;
  outline: none;
}

.ccm-02__item svg {
  width: 21px;
  height: 21px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.ccm-02__note {
  position: absolute;
  bottom: 20px;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 12.5px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: oklch(0.75 0.04 165 / .6);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-02 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
