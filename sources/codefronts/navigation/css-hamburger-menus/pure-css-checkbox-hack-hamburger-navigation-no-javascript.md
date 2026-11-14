---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/pure-css-checkbox-hack-hamburger-navigation-no-javascript/"
title: "Pure CSS Checkbox Hack Hamburger Navigation (No JavaScript)"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The classic zero-dependency pattern, done the honest way: a hidden-but-focusable checkbox holds the open/closed state, the burger is its <label>, and the…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Checkbox Hack Hamburger Navigation (No JavaScript)
Source: https://codefronts.com/navigation/css-hamburger-menus/pure-css-checkbox-hack-hamburger-navigation-no-javascript/

The classic zero-dependency pattern, done the honest way: a hidden-but-focusable checkbox holds the open/closed state, the burger is its <label>, and the :checked ~ sibling combinator drives the panel — no JavaScript anywhere in the chain. This version fixes the two mistakes in 90% of checkbox-hack tutorials: the input stays keyboard-reachable (clip, not display:none), and its focus ring is re-projected onto the visible burger.
## HTML
```html
<section class="chm-05" aria-label="Pure CSS checkbox hack hamburger menu demo">
  <div class="chm-05__stage">
    <input type="checkbox" id="chm05-t" class="chm-05__state">
    <header class="chm-05__bar">
      <span class="chm-05__brand"><i aria-hidden="true"></i>papertrail</span>
      <label for="chm05-t" class="chm-05__burger">
        <span class="chm-05__ico" aria-hidden="true"><i></i><i></i><i></i></span>
        <span class="chm-05__word chm-05__word--open" aria-hidden="true">Menu</span>
        <span class="chm-05__word chm-05__word--close" aria-hidden="true">Close</span>
      </label>
    </header>
    <nav class="chm-05__panel" aria-label="Primary">
      <a href="#features" style="--i:0">Features</a>
      <a href="#pricing" style="--i:1">Pricing</a>
      <a href="#changelog" style="--i:2">Changelog</a>
      <a href="#docs" style="--i:3">Docs</a>
      <a href="#signin" style="--i:4" class="chm-05__cta">Sign in →</a>
    </nav>
    <div class="chm-05__content" aria-hidden="true">
      <div class="chm-05__hero"><b>0 bytes</b><span>of JavaScript in this menu</span></div>
      <div class="chm-05__ln" style="--w:84%"></div>
      <div class="chm-05__ln" style="--w:66%"></div>
      <div class="chm-05__ln" style="--w:75%"></div>
    </div>
  </div>
</section>
```
## CSS
```css
.chm-05,
.chm-05 *,
.chm-05 *::before,
.chm-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-05 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.96 0.012 100);
  --panel: oklch(0.27 0.04 145);
  --edge: oklch(0.87 0.02 100);
  --ink: oklch(0.26 0.02 130);
  --mut: oklch(0.52 0.02 130);
  --acc: oklch(0.55 0.13 145);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-05__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.chm-05__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-05__bar {
  position: relative;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
  padding: 0 16px 0 24px;
}

.chm-05__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-weight: 700;
  font-size: 15px;
  letter-spacing: -.01em;
}

.chm-05__brand i {
  width: 19px;
  height: 19px;
  border-radius: 50%;
  background: conic-gradient(from 160deg,var(--acc),oklch(0.75 0.13 110));
}

.chm-05__burger {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 99px;
  border: 1.5px solid var(--ink);
  cursor: pointer;
  font-weight: 700;
  font-size: 12.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  user-select: none;
  transition: background .25s,color .25s,border-color .25s;
}

.chm-05__burger:hover {
  background: var(--ink);
  color: var(--bg);
}

.chm-05__state:focus-visible ~ .chm-05__bar .chm-05__burger {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-05__state:checked ~ .chm-05__bar .chm-05__burger {
  border-color: oklch(0.9 0.02 145);
  color: oklch(0.95 0.02 145);
}

.chm-05__state:checked ~ .chm-05__bar .chm-05__burger:hover {
  background: oklch(0.95 0.02 145);
  color: var(--panel);
}

.chm-05__ico {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-05__ico i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-05__ico i:nth-child(1) {
  top: 0;
}

.chm-05__ico i:nth-child(2) {
  top: 5px;
}

.chm-05__ico i:nth-child(3) {
  top: 10px;
}

.chm-05__state:checked ~ .chm-05__bar .chm-05__ico i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

.chm-05__state:checked ~ .chm-05__bar .chm-05__ico i:nth-child(2) {
  opacity: 0;
}

.chm-05__state:checked ~ .chm-05__bar .chm-05__ico i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-05__word {
  display: block;
}

.chm-05__word--close {
  display: none;
}

.chm-05__state:checked ~ .chm-05__bar .chm-05__word--open {
  display: none;
}

.chm-05__state:checked ~ .chm-05__bar .chm-05__word--close {
  display: block;
}

.chm-05__panel {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: var(--panel);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 4px;
  padding: 0 32px;
  translate: 0 -105%;
  visibility: hidden;
  transition: translate .5s cubic-bezier(.7,0,.25,1),visibility 0s .5s;
}

.chm-05__state:checked ~ .chm-05__panel {
  translate: 0 0;
  visibility: visible;
  transition: translate .5s cubic-bezier(.7,0,.25,1),visibility 0s 0s;
}

.chm-05__panel a {
  padding: 13px 2px;
  font-size: 27px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: oklch(0.95 0.02 130);
  text-decoration: none;
  border-bottom: 1px solid oklch(0.36 0.04 145);
  opacity: 0;
  translate: 0 -14px;
  transition: color .2s,opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
}

.chm-05__state:checked ~ .chm-05__panel a {
  opacity: 1;
  translate: 0 0;
  transition-delay: 0s,calc(.16s + var(--i)*.05s),calc(.16s + var(--i)*.05s);
}

.chm-05__panel a:hover,
.chm-05__panel a:focus-visible {
  color: oklch(0.85 0.14 110);
}

.chm-05__panel a:focus-visible {
  outline: 2px solid oklch(0.85 0.14 110);
  outline-offset: 4px;
  border-radius: 4px;
}

.chm-05__cta {
  border-bottom: none !important;
  font-size: 16px !important;
  margin-top: 18px;
  color: oklch(0.85 0.14 110) !important;
}

.chm-05__content {
  padding: 16px 24px;
  display: grid;
  gap: 13px;
}

.chm-05__hero {
  height: 170px;
  border-radius: 16px;
  background: linear-gradient(150deg,oklch(0.9 0.04 120),oklch(0.84 0.06 145));
  display: flex;
  flex-direction: column;
  justify-content: end;
  padding: 18px;
  margin-bottom: 6px;
}

.chm-05__hero b {
  font-size: 26px;
  letter-spacing: -.02em;
}

.chm-05__hero span {
  font-size: 12.5px;
  color: var(--mut);
}

.chm-05__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.89 0.012 100);
}

@media (prefers-reduced-motion: reduce) {
  .chm-05 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
