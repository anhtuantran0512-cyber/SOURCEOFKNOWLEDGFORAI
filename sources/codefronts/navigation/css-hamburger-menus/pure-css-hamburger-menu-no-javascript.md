---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/pure-css-hamburger-menu-no-javascript/"
title: "Pure CSS Hamburger Menu Without JavaScript"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The checkbox hack, rebuilt for the :has() era: the input still holds the state, but :has(:checked) reads it from the ROOT, so the burger, the header, the…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Hamburger Menu Without JavaScript
Source: https://codefronts.com/navigation/css-hamburger-menus/pure-css-hamburger-menu-no-javascript/

The checkbox hack, rebuilt for the :has() era: the input still holds the state, but :has(:checked) reads it from the ROOT, so the burger, the header, the fullscreen panel and even the page content can all react — no sibling-order gymnastics, no restructured markup. Compare demo 05 (the ~ combinator version) side by side: same zero-JS guarantee, but here the menu tints the header, scales the page and swaps the burger, all from one selector.
## HTML
```html
<section class="chm-09" aria-label="Pure CSS :has() hamburger menu demo">
  <div class="chm-09__stage">
    <input type="checkbox" id="chm09-t" class="chm-09__state">
    <div class="chm-09__page" aria-hidden="true">
      <div class="chm-09__hero"><b>:has()</b><span>state, readable anywhere</span></div>
      <div class="chm-09__ln" style="--w:82%"></div>
      <div class="chm-09__ln" style="--w:60%"></div>
      <div class="chm-09__ln" style="--w:73%"></div>
    </div>
    <nav class="chm-09__panel" aria-label="Site">
      <a href="#index" style="--i:0">Index</a>
      <a href="#essays" style="--i:1">Essays</a>
      <a href="#library" style="--i:2">Library</a>
      <a href="#colophon" style="--i:3">Colophon</a>
    </nav>
    <header class="chm-09__bar">
      <span class="chm-09__brand">marginalia</span>
      <label for="chm09-t" class="chm-09__burger"><span aria-hidden="true"><i></i><i></i><i></i></span></label>
    </header>
  </div>
</section>
```
## CSS
```css
.chm-09,
.chm-09 *,
.chm-09 *::before,
.chm-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-09 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.965 0.008 85);
  --ink: oklch(0.24 0.02 60);
  --mut: oklch(0.52 0.02 60);
  --acc: oklch(0.58 0.16 45);
  --panel: oklch(0.24 0.03 55);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-09__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid oklch(0.87 0.015 80);
}

.chm-09__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-09__bar {
  position: absolute;
  inset: 0 0 auto 0;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
  padding: 0 16px 0 24px;
}

.chm-09__brand {
  font-size: 16px;
  font-weight: 700;
  font-style: italic;
  letter-spacing: -.01em;
  transition: color .35s;
}

.chm-09:has(#chm09-t:checked) .chm-09__brand {
  color: oklch(0.95 0.015 80);
}

.chm-09__burger {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--ink);
  color: oklch(0.96 0.01 80);
  cursor: pointer;
  transition: background .3s,scale .2s;
}

.chm-09__burger:hover {
  scale: 1.06;
}

.chm-09__state:focus-visible ~ .chm-09__bar .chm-09__burger {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-09:has(#chm09-t:checked) .chm-09__burger {
  background: oklch(0.96 0.01 80);
  color: var(--panel);
}

.chm-09__burger span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-09__burger i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-09__burger i:nth-child(1) {
  top: 0;
}

.chm-09__burger i:nth-child(2) {
  top: 5px;
}

.chm-09__burger i:nth-child(3) {
  top: 10px;
}

.chm-09:has(#chm09-t:checked) .chm-09__burger i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

.chm-09:has(#chm09-t:checked) .chm-09__burger i:nth-child(2) {
  opacity: 0;
}

.chm-09:has(#chm09-t:checked) .chm-09__burger i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-09__page {
  position: absolute;
  inset: 0;
  padding: 86px 24px 24px;
  display: grid;
  gap: 14px;
  align-content: start;
  transition: scale .5s cubic-bezier(.2,.7,.2,1),filter .5s,opacity .5s;
}

.chm-09:has(#chm09-t:checked) .chm-09__page {
  scale: .96;
  filter: blur(2px);
  opacity: .55;
}

.chm-09__hero {
  height: 190px;
  border-radius: 16px;
  background: linear-gradient(150deg,oklch(0.9 0.035 70),oklch(0.84 0.06 45));
  display: flex;
  flex-direction: column;
  justify-content: end;
  padding: 18px;
  margin-bottom: 6px;
}

.chm-09__hero b {
  font-size: 30px;
  letter-spacing: -.02em;
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.chm-09__hero span {
  font-size: 12.5px;
  color: var(--mut);
}

.chm-09__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.89 0.012 80);
}

.chm-09__panel {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: linear-gradient(170deg,color-mix(in oklch,var(--panel) 92%,white),var(--panel) 60%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 32px;
  opacity: 0;
  scale: 1.04;
  visibility: hidden;
  transition: opacity .4s,scale .5s cubic-bezier(.2,.7,.2,1),visibility 0s .5s;
}

.chm-09:has(#chm09-t:checked) .chm-09__panel {
  opacity: 1;
  scale: 1;
  visibility: visible;
  transition: opacity .4s,scale .5s cubic-bezier(.2,.7,.2,1),visibility 0s 0s;
}

.chm-09__panel a {
  padding: 16px 2px;
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: oklch(0.95 0.015 80);
  text-decoration: none;
  border-bottom: 1px solid oklch(1 0 0/.12);
  display: flex;
  align-items: center;
  justify-content: space-between;
  opacity: 0;
  translate: 0 14px;
  transition: color .2s,opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
}

.chm-09__panel a::after {
  content: "→";
  font-size: 18px;
  color: var(--acc);
  opacity: 0;
  translate: -8px 0;
  transition: opacity .2s,translate .25s;
}

.chm-09__panel a:hover::after,
.chm-09__panel a:focus-visible::after {
  opacity: 1;
  translate: 0 0;
}

.chm-09__panel a:hover,
.chm-09__panel a:focus-visible {
  color: oklch(0.85 0.09 60);
}

.chm-09__panel a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
  border-radius: 4px;
}

.chm-09:has(#chm09-t:checked) .chm-09__panel a {
  opacity: 1;
  translate: 0 0;
  transition-delay: 0s,calc(.14s + var(--i)*.06s),calc(.14s + var(--i)*.06s);
}

@media (prefers-reduced-motion: reduce) {
  .chm-09 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
