---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/glassmorphism-backdrop-blur-css-hamburger-navigation/"
title: "Glassmorphism Backdrop Blur CSS Hamburger Navigation"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Real frosted glass, not gray-with-opacity: the open menu is a translucent panel whose backdrop-filter stacks blur(18px) with saturate(170%), so the color…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Backdrop Blur CSS Hamburger Navigation
Source: https://codefronts.com/navigation/css-hamburger-menus/glassmorphism-backdrop-blur-css-hamburger-navigation/

Real frosted glass, not gray-with-opacity: the open menu is a translucent panel whose backdrop-filter stacks blur(18px) with saturate(170%), so the color field behind it glows through the frost the way iOS panels do. The stage ships animated gradient blobs precisely so you can see the glass working, plus the full recipe — 1px light-edge border, inner highlight, layered shadow — and an @supports fallback for engines without backdrop-filter.
## HTML
```html
<section class="chm-07" aria-label="Glassmorphism backdrop blur menu demo">
  <div class="chm-07__stage">
    <i class="chm-07__blob chm-07__blob--1" aria-hidden="true"></i>
    <i class="chm-07__blob chm-07__blob--2" aria-hidden="true"></i>
    <header class="chm-07__bar">
      <span class="chm-07__brand">lumen</span>
      <button class="chm-07__btn" type="button" aria-expanded="false" aria-controls="chm07-menu" aria-label="Open menu"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
    </header>
    <div class="chm-07__content" aria-hidden="true">
      <h2>Light, refracted.</h2>
      <p>Studio for luminous interfaces — glass, gradients and grain.</p>
      <div class="chm-07__chip">Scroll ↓</div>
    </div>
    <nav class="chm-07__menu" id="chm07-menu" aria-label="Site">
      <a href="#work" style="--i:0">Work</a>
      <a href="#services" style="--i:1">Services</a>
      <a href="#about" style="--i:2">About</a>
      <a href="#contact" style="--i:3">Contact</a>
      <footer style="--i:4"><span>© 2026 lumen</span><a href="#privacy" class="chm-07__tiny">Privacy</a></footer>
    </nav>
  </div>
</section>
```
## CSS
```css
.chm-07,
.chm-07 *,
.chm-07 *::before,
.chm-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-07 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.22 0.045 285);
  --ink: oklch(0.97 0.008 285);
  --mut: oklch(0.78 0.03 285);
  --acc: oklch(0.82 0.14 190);
  --blob1: oklch(0.62 0.23 310);
  --blob2: oklch(0.75 0.16 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-07__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid oklch(0.35 0.05 285);
  isolation: isolate;
}

.chm-07__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
  z-index: 0;
}

.chm-07__blob--1 {
  width: 300px;
  height: 300px;
  left: -80px;
  top: 60px;
  background: var(--blob1);
  animation: chm07-drift 11s ease-in-out infinite alternate;
}

.chm-07__blob--2 {
  width: 260px;
  height: 260px;
  right: -70px;
  bottom: -40px;
  background: var(--blob2);
  animation: chm07-drift 13s ease-in-out infinite alternate-reverse;
}

@keyframes chm07-drift {
  from {
    translate: 0 0;
    scale: 1;
  }

  to {
    translate: 40px -30px;
    scale: 1.15;
  }
}

.chm-07__bar {
  position: relative;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
  padding: 0 22px;
}

.chm-07__brand {
  font-size: 17px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
}

.chm-07__btn {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: 1px solid oklch(1 0 0/.28);
  border-radius: 14px;
  background: oklch(0.97 0.01 260/.1);
  -webkit-backdrop-filter: blur(12px) saturate(160%);
  backdrop-filter: blur(12px) saturate(160%);
  color: var(--ink);
  cursor: pointer;
  transition: background .25s,scale .2s;
}

.chm-07__btn:hover {
  background: oklch(0.97 0.01 260/.2);
  scale: 1.05;
}

.chm-07__btn:active {
  scale: .95;
}

.chm-07__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-07__btn span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-07__btn i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-07__btn i:nth-child(1) {
  top: 0;
}

.chm-07__btn i:nth-child(2) {
  top: 5px;
}

.chm-07__btn i:nth-child(3) {
  top: 10px;
}

[data-open] .chm-07__btn i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

[data-open] .chm-07__btn i:nth-child(2) {
  opacity: 0;
}

[data-open] .chm-07__btn i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-07__content {
  position: relative;
  z-index: 1;
  padding: 46px 26px;
  display: grid;
  gap: 14px;
  justify-items: start;
}

.chm-07__content h2 {
  font-size: 37px;
  line-height: 1.05;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.chm-07__content p {
  font-size: 14px;
  line-height: 1.55;
  color: var(--mut);
  max-width: 26ch;
  text-wrap: pretty;
}

.chm-07__chip {
  margin-top: 10px;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  border: 1px solid oklch(1 0 0/.25);
  border-radius: 99px;
  padding: 9px 16px;
  background: oklch(0.97 0.01 260/.08);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.chm-07__menu {
  position: absolute;
  z-index: 2;
  inset: 86px 16px 16px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 2px;
  padding: 0 26px;
  background: oklch(0.97 0.01 260/.12);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
  backdrop-filter: blur(18px) saturate(170%);
  border: 1px solid oklch(1 0 0/.28);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.25),0 24px 48px -20px oklch(0.2 0.05 280/.5);
  opacity: 0;
  translate: 0 -14px;
  scale: .98;
  visibility: hidden;
  transition: opacity .35s,translate .4s cubic-bezier(.2,.7,.2,1),scale .4s cubic-bezier(.2,.7,.2,1),visibility 0s .4s;
}

[data-open] .chm-07__menu {
  opacity: 1;
  translate: 0 0;
  scale: 1;
  visibility: visible;
  transition-delay: 0s;
}

@supports not (backdrop-filter: blur(1px)) {
  .chm-07__menu {
    background: oklch(0.25 0.04 280/.94);
  }

  .chm-07__btn {
    background: oklch(0.3 0.05 280/.85);
  }
}

.chm-07__menu a {
  padding: 15px 2px;
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: var(--ink);
  text-decoration: none;
  border-bottom: 1px solid oklch(1 0 0/.14);
  display: flex;
  justify-content: space-between;
  align-items: center;
  opacity: 0;
  translate: 0 12px;
  transition: color .2s,opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
}

.chm-07__menu a::after {
  content: "↗";
  font-size: 16px;
  opacity: 0;
  translate: -6px 4px;
  transition: opacity .2s,translate .25s;
}

.chm-07__menu a:hover,
.chm-07__menu a:focus-visible {
  color: var(--acc);
}

.chm-07__menu a:hover::after,
.chm-07__menu a:focus-visible::after {
  opacity: 1;
  translate: 0 0;
}

.chm-07__menu a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
  border-radius: 6px;
}

[data-open] .chm-07__menu a,
[data-open] .chm-07__menu footer {
  opacity: 1;
  translate: 0 0;
  transition-delay: 0s,calc(.1s + var(--i)*.055s),calc(.1s + var(--i)*.055s);
}

.chm-07__menu footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
  font-size: 12px;
  color: var(--mut);
  opacity: 0;
  translate: 0 12px;
  transition: opacity .3s,translate .35s;
}

.chm-07__tiny {
  font-size: 12px !important;
  padding: 0 !important;
  border: none !important;
  color: var(--mut) !important;
}

@media (prefers-reduced-motion: reduce) {
  .chm-07 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-07__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-07__btn');
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
