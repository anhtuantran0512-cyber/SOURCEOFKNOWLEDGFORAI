---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/brutalist-css-bordered-hamburger-menu/"
title: "Brutalist Design Bordered CSS Hamburger Menu"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Neo-brutalism with its rules intact: 3px black borders on everything, hard offset shadows that don't blur (box-shadow: 6px 6px 0), one shrieking yellow,…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Design Bordered CSS Hamburger Menu
Source: https://codefronts.com/navigation/css-hamburger-menus/brutalist-css-bordered-hamburger-menu/

Neo-brutalism with its rules intact: 3px black borders on everything, hard offset shadows that don't blur (box-shadow: 6px 6px 0), one shrieking yellow, Space-Mono-style uppercase type — and motion that CUTS instead of eases, because in this dialect a transition curve is a lie. The burger is a bordered plate that slams down onto its shadow when pressed; the menu is a stack of full-bleed rows that invert to black on hover, numbered like a manifest. Checkbox hack, naturally — raw HTML for a raw style.
## HTML
```html
<section class="chm-27" aria-label="Brutalist bordered menu demo">
  <div class="chm-27__stage">
    <input type="checkbox" id="chm27-t" class="chm-27__state">
    <header class="chm-27__bar">
      <span class="chm-27__brand">RAW—GOODS<i class="chm-27__reg" aria-hidden="true">®</i></span>
      <label for="chm27-t" class="chm-27__plate">
        <span class="chm-27__ico" aria-hidden="true"><i></i><i></i><i></i></span>
        <span class="chm-27__lbl chm-27__lbl--m" aria-hidden="true">MENU</span>
        <span class="chm-27__lbl chm-27__lbl--c" aria-hidden="true">CLOSE</span>
      </label>
    </header>
    <nav class="chm-27__menu" aria-label="Site">
      <div class="chm-27__row"><a href="#shop"><b>01</b>SHOP ALL<span aria-hidden="true">→</span></a></div>
      <div class="chm-27__row"><a href="#drops"><b>02</b>DROPS<span aria-hidden="true">→</span></a></div>
      <div class="chm-27__row"><a href="#manifesto"><b>03</b>MANIFESTO<span aria-hidden="true">→</span></a></div>
      <div class="chm-27__row"><a href="#faq"><b>04</b>FAQ<span aria-hidden="true">→</span></a></div>
    </nav>
    <div class="chm-27__page" aria-hidden="true">
      <div class="chm-27__badge">EST. 2026<br>NO COOKIES<br>NO TRACKING</div>
      <div class="chm-27__box"></div>
    </div>
    <div class="chm-27__ticker" aria-hidden="true"><div class="chm-27__tape"><span>FREE SHIPPING OVER $80 ★ PRESS THE PLATE ★ EVERYTHING HAS A BORDER ★&nbsp;</span><span>FREE SHIPPING OVER $80 ★ PRESS THE PLATE ★ EVERYTHING HAS A BORDER ★&nbsp;</span></div></div>
  </div>
</section>
```
## CSS
```css
.chm-27,
.chm-27 *,
.chm-27 *::before,
.chm-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-27 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --paper: oklch(0.96 0.01 95);
  --ink: oklch(0.18 0.01 90);
  --acc: oklch(0.86 0.17 95);
  font-family: ui-monospace,'Cascadia Mono',Menlo,Consolas,monospace;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-27__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 560px;
  border: 3px solid var(--ink);
  background: radial-gradient(oklch(0.18 0.01 90/.14) 1.2px,transparent 1.3px) 0 0/18px 18px,var(--paper);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 8px 8px 0 var(--ink);
}

.chm-27__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-27__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px;
  border-bottom: 3px solid var(--ink);
  background: var(--paper);
  position: relative;
  z-index: 2;
}

.chm-27__brand {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .04em;
}

.chm-27__reg {
  font-style: normal;
  font-size: 10px;
  vertical-align: super;
}

.chm-27__plate {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 46px;
  padding: 0 14px;
  border: 3px solid var(--ink);
  background: var(--acc);
  cursor: pointer;
  user-select: none;
  box-shadow: 6px 6px 0 var(--ink);
  transition: translate .06s linear,box-shadow .06s linear;
}

.chm-27__plate:hover {
  background: oklch(0.9 0.19 95);
}

.chm-27__state:focus-visible ~ .chm-27__bar .chm-27__plate {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.chm-27__state:checked ~ .chm-27__bar .chm-27__plate {
  translate: 6px 6px;
  box-shadow: 0 0 0 var(--ink);
}

.chm-27__ico {
  position: relative;
  width: 20px;
  height: 14px;
  display: block;
}

.chm-27__ico i {
  position: absolute;
  left: 0;
  width: 20px;
  height: 3px;
  background: var(--ink);
  transition: translate .06s linear,rotate .06s linear,opacity .06s linear;
}

.chm-27__ico i:nth-child(1) {
  top: 0;
}

.chm-27__ico i:nth-child(2) {
  top: 5.5px;
}

.chm-27__ico i:nth-child(3) {
  top: 11px;
}

.chm-27__state:checked ~ .chm-27__bar .chm-27__ico i:nth-child(1) {
  translate: 0 5.5px;
  rotate: 45deg;
}

.chm-27__state:checked ~ .chm-27__bar .chm-27__ico i:nth-child(2) {
  opacity: 0;
}

.chm-27__state:checked ~ .chm-27__bar .chm-27__ico i:nth-child(3) {
  translate: 0 -5.5px;
  rotate: -45deg;
}

.chm-27__lbl {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
}

.chm-27__lbl--c {
  display: none;
}

.chm-27__state:checked ~ .chm-27__bar .chm-27__lbl--m {
  display: none;
}

.chm-27__state:checked ~ .chm-27__bar .chm-27__lbl--c {
  display: block;
}

.chm-27__menu {
  position: absolute;
  inset: 79px 0 40px;
  z-index: 1;
  background: var(--paper);
  border-bottom: 3px solid var(--ink);
  display: none;
  flex-direction: column;
}

.chm-27__state:checked ~ .chm-27__menu {
  display: flex;
}

.chm-27__row {
  border-bottom: 3px solid var(--ink);
}

.chm-27__row a {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 0 18px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--ink);
  text-decoration: none;
  transition: none;
}

.chm-27__row b {
  font-size: 11px;
  border: 2px solid var(--ink);
  padding: 2px 6px;
}

.chm-27__row span {
  margin-left: auto;
  font-size: 18px;
}

.chm-27__row a:hover,
.chm-27__row a:focus-visible {
  background: var(--ink);
  color: var(--paper);
}

.chm-27__row a:hover b,
.chm-27__row a:focus-visible b {
  border-color: var(--paper);
}

.chm-27__row a:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: -6px;
}

.chm-27__page {
  flex: 1;
  padding: 22px;
  display: grid;
  gap: 18px;
  align-content: start;
}

.chm-27__badge {
  width: max-content;
  border: 3px solid var(--ink);
  background: var(--acc);
  padding: 12px 16px;
  font-size: 12px;
  font-weight: 700;
  line-height: 1.7;
  letter-spacing: .06em;
  rotate: -1.5deg;
  box-shadow: 6px 6px 0 var(--ink);
}

.chm-27__box {
  height: 150px;
  border: 3px solid var(--ink);
  background: repeating-linear-gradient(-45deg,var(--paper) 0 12px,oklch(0.18 0.01 90/.12) 12px 24px);
}

.chm-27__ticker {
  margin-top: auto;
  border-top: 3px solid var(--ink);
  background: var(--ink);
  color: var(--paper);
  overflow: hidden;
  padding: 9px 0;
}

.chm-27__tape {
  display: flex;
  width: max-content;
  animation: chm27-tape 14s linear infinite;
}

.chm-27__tape span {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  white-space: nowrap;
}

@keyframes chm27-tape {
  to {
    translate: -50% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .chm-27__tape {
    animation: none;
  }

  .chm-27 * {
    transition: none !important;
  }
}
```
