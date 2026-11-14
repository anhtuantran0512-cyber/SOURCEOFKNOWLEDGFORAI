---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/full-screen-overlay-mobile-navigation/"
title: "Full Screen Mobile Navigation Overlay CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The fashion-house takeover: the menu doesn't open a panel, it becomes the page — a near-black sheet where five oversized links reveal themselves line-by-line…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full Screen Mobile Navigation Overlay CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/full-screen-overlay-mobile-navigation/

The fashion-house takeover: the menu doesn't open a panel, it becomes the page — a near-black sheet where five oversized links reveal themselves line-by-line from under invisible masks, each with an index number and a hover state that slides in an em-dash and fills the outlined type. The mask reveal is the technique to steal: an overflow:hidden li with the link translating up from 110% below, staggered, so text appears to be printed onto the page.
## HTML
```html
<section class="chm-11" aria-label="Fullscreen overlay navigation demo">
  <div class="chm-11__stage">
    <div class="chm-11__page" aria-hidden="true">
      <div class="chm-11__hero"><span>AW·26</span><b>Silhouettes<br>in Static</b></div>
      <div class="chm-11__ln" style="--w:76%"></div>
      <div class="chm-11__ln" style="--w:58%"></div>
    </div>
    <nav class="chm-11__sheet" id="chm11-sheet" aria-label="Site">
      <ul>
        <li style="--i:0"><a href="#collections" data-n="01">Collections</a></li>
        <li style="--i:1"><a href="#runway" data-n="02">Runway</a></li>
        <li style="--i:2"><a href="#atelier" data-n="03">Atelier</a></li>
        <li style="--i:3"><a href="#stockists" data-n="04">Stockists</a></li>
        <li style="--i:4"><a href="#contact" data-n="05">Contact</a></li>
      </ul>
      <footer class="chm-11__foot">
        <a href="#instagram">Instagram</a><a href="#pinterest">Pinterest</a><span>Paris — Tokyo</span>
      </footer>
    </nav>
    <header class="chm-11__bar">
      <span class="chm-11__brand">VESTIGE</span>
      <button class="chm-11__btn" type="button" aria-expanded="false" aria-controls="chm11-sheet">
        <span class="chm-11__btnw"><i>Menu</i><i>Close</i></span>
        <span class="chm-11__ico" aria-hidden="true"><b></b><b></b></span>
      </button>
    </header>
  </div>
</section>
```
## CSS
```css
.chm-11,
.chm-11 *,
.chm-11 *::before,
.chm-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-11 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --paper: oklch(0.95 0.007 80);
  --sheet: oklch(0.16 0.012 70);
  --mut: oklch(0.6 0.015 70);
  --acc: oklch(0.78 0.15 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--sheet);
  display: grid;
  justify-content: center;
  container-type: inline-size;
}

.chm-11__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 560px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--paper);
  border: 1px solid oklch(0.86 0.01 80);
}

.chm-11__bar {
  position: absolute;
  inset: 0 0 auto 0;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
  padding: 0 22px;
  mix-blend-mode: difference;
  color: oklch(0.95 0.007 80);
}

.chm-11__brand {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .34em;
}

.chm-11__btn {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font: 600 12px 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.chm-11__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
  border-radius: 4px;
}

.chm-11__btnw {
  position: relative;
  height: 15px;
  overflow: hidden;
  display: block;
}

.chm-11__btnw i {
  display: block;
  height: 15px;
  line-height: 15px;
  font-style: normal;
  transition: translate .4s cubic-bezier(.65,0,.35,1);
}

[data-open] .chm-11__btnw i {
  translate: 0 -15px;
}

.chm-11__ico {
  position: relative;
  width: 26px;
  height: 10px;
  display: block;
}

.chm-11__ico b {
  position: absolute;
  left: 0;
  width: 26px;
  height: 1.5px;
  background: currentColor;
  transition: translate .35s cubic-bezier(.65,0,.35,1),rotate .35s cubic-bezier(.65,0,.35,1) .04s;
}

.chm-11__ico b:nth-child(1) {
  top: 0;
}

.chm-11__ico b:nth-child(2) {
  top: 8px;
}

[data-open] .chm-11__ico b:nth-child(1) {
  translate: 0 4px;
  rotate: 20deg;
}

[data-open] .chm-11__ico b:nth-child(2) {
  translate: 0 -4px;
  rotate: -20deg;
}

.chm-11__page {
  position: absolute;
  inset: 0;
  padding: 92px 26px;
  display: grid;
  gap: 16px;
  align-content: start;
}

.chm-11__hero {
  height: 250px;
  border-radius: 4px;
  background: linear-gradient(160deg,oklch(0.85 0.02 75),oklch(0.72 0.045 60));
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 18px;
}

.chm-11__hero span {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .3em;
}

.chm-11__hero b {
  font-size: 29px;
  line-height: 1.04;
  letter-spacing: -.02em;
  font-weight: 700;
}

.chm-11__ln {
  height: 10px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.87 0.012 80);
}

.chm-11__sheet {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: var(--sheet);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 30px;
  opacity: 0;
  scale: 1.03;
  visibility: hidden;
  transition: opacity .35s,scale .45s cubic-bezier(.2,.7,.2,1),visibility 0s .45s;
}

[data-open] .chm-11__sheet {
  opacity: 1;
  scale: 1;
  visibility: visible;
  transition-delay: 0s;
}

.chm-11__sheet ul {
  list-style: none;
}

.chm-11__sheet li {
  overflow: hidden;
}

.chm-11__sheet li a {
  display: block;
  padding: 7px 0;
  font-size: clamp(34px,9cqi,44px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.08;
  text-transform: uppercase;
  text-decoration: none;
  color: transparent;
  -webkit-text-stroke: 1.5px var(--paper);
  translate: 0 110%;
  transition: translate .6s cubic-bezier(.2,.75,.15,1),color .25s;
}

.chm-11__sheet li a::before {
  content: attr(data-n) " ";
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .2em;
  -webkit-text-stroke: 0;
  color: var(--acc);
  vertical-align: super;
  margin-right: 8px;
}

[data-open] .chm-11__sheet li a {
  translate: 0 0;
  transition-delay: calc(.25s + var(--i)*.07s),0s;
}

.chm-11__sheet li a:hover,
.chm-11__sheet li a:focus-visible {
  color: var(--paper);
}

.chm-11__sheet li a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
}

.chm-11__foot {
  display: flex;
  gap: 18px;
  align-items: baseline;
  margin-top: 34px;
  font-size: 12px;
  color: var(--mut);
  opacity: 0;
  transition: opacity .4s .5s;
}

[data-open] .chm-11__foot {
  opacity: 1;
}

.chm-11__foot a {
  color: var(--paper);
  text-decoration: none;
  border-bottom: 1px solid oklch(1 0 0/.25);
  padding-bottom: 2px;
}

.chm-11__foot a:hover,
.chm-11__foot a:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
}

.chm-11__foot span {
  margin-left: auto;
}

@media (prefers-reduced-motion: reduce) {
  .chm-11 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-11__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-11__btn');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```
