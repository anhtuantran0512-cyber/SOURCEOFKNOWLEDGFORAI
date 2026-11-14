---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/minimalist-3-line-css-menu-icon-with-hover-effects/"
title: "Simple 3-Line CSS Hamburger Icon Hover Effect"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Five hover treatments for the resting burger — the micro-interaction users see a hundred times before they ever click: Slide-through (lines exit right and…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Simple 3-Line CSS Hamburger Icon Hover Effect
Source: https://codefronts.com/navigation/css-hamburger-menus/minimalist-3-line-css-menu-icon-with-hover-effects/

Five hover treatments for the resting burger — the micro-interaction users see a hundred times before they ever click: Slide-through (lines exit right and re-enter from the left through an overflow mask), Stretch (the short middle line extends to full width), Wave (staggered dip), Spread (lines breathe apart), and Tilt (the icon cocks 90° with overshoot). All pure CSS, all firing on :focus-visible too, each labeled with its one-line recipe.
## HTML
```html
<section class="chm-19" aria-label="Hamburger icon hover effects demo">
  <div class="chm-19__stage">
    <header class="chm-19__head"><h2>Hover states</h2><span>hover or Tab through — resting-state micro-interactions</span></header>
    <div class="chm-19__grid">
      <figure class="chm-19__cell">
        <button class="chm-19__btn chm-19__slide" type="button" aria-label="Slide-through hover demo"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Slide-through</b><code>mask + ::after twin</code></figcaption>
      </figure>
      <figure class="chm-19__cell">
        <button class="chm-19__btn chm-19__stretch" type="button" aria-label="Stretch hover demo"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Stretch</b><code>middle 60% → 100%</code></figcaption>
      </figure>
      <figure class="chm-19__cell">
        <button class="chm-19__btn chm-19__wave" type="button" aria-label="Wave hover demo"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Wave</b><code>staggered dip + bounce</code></figcaption>
      </figure>
      <figure class="chm-19__cell">
        <button class="chm-19__btn chm-19__spread" type="button" aria-label="Spread hover demo"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Spread</b><code>outer lines ±3px</code></figcaption>
      </figure>
      <figure class="chm-19__cell">
        <button class="chm-19__btn chm-19__tilt" type="button" aria-label="Tilt hover demo"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Tilt</b><code>rotate 90° overshoot</code></figcaption>
      </figure>
    </div>
  </div>
</section>
```
## CSS
```css
.chm-19,
.chm-19 *,
.chm-19 *::before,
.chm-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-19 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.965 0.005 250);
  --card: oklch(1 0 0);
  --edge: oklch(0.89 0.008 250);
  --ink: oklch(0.24 0.015 255);
  --mut: oklch(0.54 0.012 255);
  --acc: oklch(0.6 0.17 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-19__stage {
  border-radius: 20px;
  padding: 24px;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.chm-19__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.chm-19__head h2 {
  font-size: 16px;
  letter-spacing: -.01em;
}

.chm-19__head span {
  font-size: 11.5px;
  color: var(--mut);
}

.chm-19__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(118px,100%),1fr));
  gap: 13px;
}

.chm-19__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 11px;
}

.chm-19__cell figcaption {
  display: grid;
  justify-items: center;
  gap: 4px;
  text-align: center;
}

.chm-19__cell b {
  font-size: 12.5px;
}

.chm-19__cell code {
  font: 10px ui-monospace,Menlo,Consolas,monospace;
  color: var(--mut);
}

.chm-19__btn {
  width: 100%;
  aspect-ratio: 1.15;
  display: grid;
  place-items: center;
  border: 1px solid var(--edge);
  border-radius: 15px;
  background: var(--card);
  color: var(--ink);
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 10px 24px -20px oklch(0.3 0.03 255/.7);
  transition: border-color .25s,translate .2s;
}

.chm-19__btn:hover {
  border-color: color-mix(in oklch,var(--acc) 45%,var(--edge));
  translate: 0 -2px;
}

.chm-19__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-19__btn>span {
  position: relative;
  width: 28px;
  height: 20px;
  display: block;
}

.chm-19__btn i {
  position: absolute;
  left: 0;
  width: 28px;
  height: 2.5px;
  border-radius: 2px;
  background: currentColor;
}

.chm-19__btn i:nth-child(1) {
  top: 0;
}

.chm-19__btn i:nth-child(2) {
  top: 8.75px;
}

.chm-19__btn i:nth-child(3) {
  top: 17.5px;
}

.chm-19__slide>span {
  overflow: hidden;
  width: 28px;
}

.chm-19__slide i {
  transition: translate .35s cubic-bezier(.65,0,.35,1);
}

.chm-19__slide i::after {
  content: "";
  position: absolute;
  inset: 0;
  translate: -34px 0;
  border-radius: inherit;
  background: inherit;
}

.chm-19__slide i:nth-child(2) {
  transition-delay: .045s;
}

.chm-19__slide i:nth-child(3) {
  transition-delay: .09s;
}

.chm-19__slide:hover i,
.chm-19__slide:focus-visible i {
  translate: 34px 0;
}

.chm-19__stretch i {
  transition: width .3s cubic-bezier(.2,.7,.2,1);
}

.chm-19__stretch i:nth-child(2) {
  width: 17px;
}

.chm-19__stretch:hover i:nth-child(2),
.chm-19__stretch:focus-visible i:nth-child(2) {
  width: 28px;
}

.chm-19__wave i {
  transition: translate .3s cubic-bezier(.3,1.6,.4,1);
}

.chm-19__wave i:nth-child(2) {
  transition-delay: .05s;
}

.chm-19__wave i:nth-child(3) {
  transition-delay: .1s;
}

.chm-19__wave:hover i,
.chm-19__wave:focus-visible i {
  translate: 0 3px;
}

.chm-19__spread i {
  transition: translate .3s cubic-bezier(.2,.7,.2,1);
}

.chm-19__spread:hover i:nth-child(1),
.chm-19__spread:focus-visible i:nth-child(1) {
  translate: 0 -3px;
}

.chm-19__spread:hover i:nth-child(3),
.chm-19__spread:focus-visible i:nth-child(3) {
  translate: 0 3px;
}

.chm-19__tilt>span {
  transition: rotate .45s cubic-bezier(.3,1.5,.4,1);
}

.chm-19__tilt:hover>span,
.chm-19__tilt:focus-visible>span {
  rotate: 90deg;
}

@media (prefers-reduced-motion: reduce) {
  .chm-19 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
