---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/css-hamburger-menu-with-clip-path-circle-expansion/"
title: "CSS Hamburger Menu with Clip-Path Circle Expansion"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The reveal every design-award site uses: tap the burger and the menu doesn't slide or fade — it grows out of the button as a perfect circle, because the…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hamburger Menu with Clip-Path Circle Expansion
Source: https://codefronts.com/navigation/css-hamburger-menus/css-hamburger-menu-with-clip-path-circle-expansion/

The reveal every design-award site uses: tap the burger and the menu doesn't slide or fade — it grows out of the button as a perfect circle, because the whole panel is clipped by clip-path: circle() anchored at the button's coordinates. One transitioned property on the compositor, zero layout work, zero libraries. Links stagger in behind the wavefront and an Escape key or the × collapses the circle back into the corner.
## HTML
```html
<section class="chm-01" aria-label="Clip-path circle expansion hamburger menu demo">
  <div class="chm-01__stage">
    <header class="chm-01__bar">
      <span class="chm-01__brand"><i class="chm-01__logo" aria-hidden="true"></i>orbit.studio</span>
    </header>
    <div class="chm-01__content" aria-hidden="true">
      <div class="chm-01__hero"></div>
      <div class="chm-01__ln" style="--w:82%"></div>
      <div class="chm-01__ln" style="--w:64%"></div>
      <div class="chm-01__ln" style="--w:74%"></div>
      <div class="chm-01__ln" style="--w:46%"></div>
    </div>
    <nav class="chm-01__menu" id="chm01-menu" aria-label="Site">
      <a href="#work" style="--i:0"><small>01</small>Work</a>
      <a href="#studio" style="--i:1"><small>02</small>Studio</a>
      <a href="#journal" style="--i:2"><small>03</small>Journal</a>
      <a href="#contact" style="--i:3"><small>04</small>Contact</a>
      <p class="chm-01__meta" style="--i:4">[email protected] · NYC — LDN</p>
    </nav>
    <button class="chm-01__btn" type="button" aria-expanded="false" aria-controls="chm01-menu" aria-label="Open menu">
      <span aria-hidden="true"><i></i><i></i><i></i></span>
    </button>
  </div>
</section>
```
## CSS
```css
.chm-01,
.chm-01 *,
.chm-01 *::before,
.chm-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-01 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.97 0.005 250);
  --ink: oklch(0.22 0.02 260);
  --mut: oklch(0.6 0.015 260);
  --menu: oklch(0.23 0.06 285);
  --acc: oklch(0.8 0.16 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-01__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid oklch(0.88 0.01 260);
  box-shadow: 0 30px 60px -35px oklch(0.3 0.05 285/.45);
}

.chm-01__bar {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  height: 76px;
  padding: 0 24px;
}

.chm-01__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  font-size: 15px;
  letter-spacing: -.01em;
}

.chm-01__logo {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: conic-gradient(from 210deg,var(--acc),oklch(0.55 0.2 300),var(--acc));
}

.chm-01__content {
  padding: 8px 24px;
  display: grid;
  gap: 14px;
}

.chm-01__hero {
  height: 190px;
  border-radius: 16px;
  background: linear-gradient(140deg,oklch(0.9 0.03 265),oklch(0.84 0.05 300));
  margin-bottom: 8px;
}

.chm-01__ln {
  height: 12px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.9 0.008 260);
}

.chm-01__menu {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: radial-gradient(120% 100% at 100% 0%,oklch(0.3 0.08 295),var(--menu) 55%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  padding: 0 34px;
  clip-path: circle(0px at calc(100% - 46px) 46px);
  visibility: hidden;
  transition: clip-path .65s cubic-bezier(.65,0,.35,1),visibility 0s .65s;
}

[data-open] .chm-01__menu {
  clip-path: circle(150% at calc(100% - 46px) 46px);
  visibility: visible;
  transition: clip-path .65s cubic-bezier(.65,0,.35,1),visibility 0s 0s;
}

.chm-01__menu a {
  display: flex;
  align-items: baseline;
  gap: 14px;
  padding: 12px 2px;
  font-size: 31px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: oklch(0.96 0.01 90);
  text-decoration: none;
  opacity: 0;
  translate: 0 18px;
  transition: opacity .3s,translate .4s cubic-bezier(.2,.7,.2,1),color .2s;
}

.chm-01__menu a small {
  font-size: 11px;
  font-weight: 600;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
}

.chm-01__menu a:hover,
.chm-01__menu a:focus-visible {
  color: var(--acc);
}

.chm-01__menu a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
  border-radius: 6px;
}

.chm-01__meta {
  margin-top: 26px;
  font-size: 12px;
  color: oklch(0.68 0.03 290);
  opacity: 0;
  translate: 0 18px;
  transition: opacity .3s,translate .4s cubic-bezier(.2,.7,.2,1);
}

[data-open] .chm-01__menu a,
[data-open] .chm-01__meta {
  opacity: 1;
  translate: 0 0;
  transition-delay: calc(.18s + var(--i)*.06s);
}

.chm-01__btn {
  position: absolute;
  z-index: 3;
  top: 22px;
  right: 22px;
  width: 48px;
  height: 48px;
  border: none;
  border-radius: 50%;
  background: var(--ink);
  cursor: pointer;
  display: grid;
  place-items: center;
  transition: background .3s,scale .2s;
}

.chm-01__btn:hover {
  scale: 1.06;
}

.chm-01__btn:active {
  scale: .94;
}

.chm-01__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

[data-open] .chm-01__btn {
  background: oklch(0.32 0.07 295);
}

.chm-01__btn span {
  position: relative;
  width: 20px;
  height: 14px;
  display: block;
}

.chm-01__btn i {
  position: absolute;
  left: 0;
  width: 20px;
  height: 2px;
  border-radius: 2px;
  background: oklch(0.97 0.005 250);
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-01__btn i:nth-child(1) {
  top: 0;
}

.chm-01__btn i:nth-child(2) {
  top: 6px;
}

.chm-01__btn i:nth-child(3) {
  top: 12px;
}

[data-open] .chm-01__btn i:nth-child(1) {
  translate: 0 6px;
  rotate: 45deg;
}

[data-open] .chm-01__btn i:nth-child(2) {
  opacity: 0;
  translate: -6px 0;
}

[data-open] .chm-01__btn i:nth-child(3) {
  translate: 0 -6px;
  rotate: -45deg;
}

@media (prefers-reduced-motion: reduce) {
  .chm-01 .chm-01__menu {
    transition: opacity .15s,visibility 0s .15s;
    clip-path: none;
    opacity: 0;
  }

  .chm-01 [data-open] .chm-01__menu {
    opacity: 1;
    transition-delay: 0s;
  }

  .chm-01 .chm-01__menu a,
    .chm-01 .chm-01__meta {
    transition: opacity .15s;
    translate: 0 0;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-01__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-01__btn');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```
