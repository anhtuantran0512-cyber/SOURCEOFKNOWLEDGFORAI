---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/animated-3-line-to-x-hamburger-icon-toggle-css/"
title: "Animated 3-Line to X Hamburger Icon Toggle CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Four production-grade line-to-X morphs on one stage — Spin, Squeeze, Arrow and Drop — each a 3-span icon whose entire animation is translate/rotate/opacity…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated 3-Line to X Hamburger Icon Toggle CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/animated-3-line-to-x-hamburger-icon-toggle-css/

Four production-grade line-to-X morphs on one stage — Spin, Squeeze, Arrow and Drop — each a 3-span icon whose entire animation is translate/rotate/opacity with tuned delays, so every variant runs on the compositor at 60fps. Click any tile (they're real aria-pressed toggle buttons), read the timing recipe printed under it, and lift the one that matches your brand's temperament.
## HTML
```html
<section class="chm-03" aria-label="Animated hamburger to X icon variants demo">
  <div class="chm-03__stage">
    <header class="chm-03__head"><h2>Line → X morphs</h2><span>click a tile · real aria-pressed buttons</span></header>
    <div class="chm-03__grid">
      <figure class="chm-03__cell">
        <button class="chm-03__tile chm-03__spin" type="button" aria-pressed="false" aria-label="Toggle spin morph demo"><span class="chm-03__ico" aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Spin</b><code>rotate 180° · fold 45°</code></figcaption>
      </figure>
      <figure class="chm-03__cell">
        <button class="chm-03__tile chm-03__squeeze" type="button" aria-pressed="false" aria-label="Toggle squeeze morph demo"><span class="chm-03__ico" aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Squeeze</b><code>converge → rotate, 2 beats</code></figcaption>
      </figure>
      <figure class="chm-03__cell">
        <button class="chm-03__tile chm-03__arrow" type="button" aria-pressed="false" aria-label="Toggle arrow morph demo"><span class="chm-03__ico" aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Arrow</b><code>scale .62 · origin left</code></figcaption>
      </figure>
      <figure class="chm-03__cell">
        <button class="chm-03__tile chm-03__drop" type="button" aria-pressed="false" aria-label="Toggle drop morph demo"><span class="chm-03__ico" aria-hidden="true"><i></i><i></i><i></i></span></button>
        <figcaption><b>Drop</b><code>mid falls · outers cross late</code></figcaption>
      </figure>
    </div>
  </div>
</section>
```
## CSS
```css
.chm-03,
.chm-03 *,
.chm-03 *::before,
.chm-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-03 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.17 0.02 275);
  --card: oklch(0.22 0.025 275);
  --edge: oklch(0.3 0.03 275);
  --ink: oklch(0.95 0.008 275);
  --mut: oklch(0.65 0.02 275);
  --acc: oklch(0.75 0.15 165);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-03__stage {
  border-radius: 20px;
  padding: 24px;
  background: radial-gradient(100% 90% at 50% -20%,oklch(0.26 0.05 285/.7),transparent 60%),var(--bg);
  border: 1px solid var(--edge);
}

.chm-03__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.chm-03__head h2 {
  font-size: 16px;
  letter-spacing: -.01em;
}

.chm-03__head span {
  font-size: 11.5px;
  color: var(--mut);
}

.chm-03__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
  gap: 14px;
}

.chm-03__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.chm-03__cell figcaption {
  display: grid;
  justify-items: center;
  gap: 4px;
  text-align: center;
}

.chm-03__cell b {
  font-size: 13px;
}

.chm-03__cell code {
  font: 10.5px ui-monospace,Menlo,Consolas,monospace;
  color: var(--mut);
}

.chm-03__tile {
  width: 100%;
  aspect-ratio: 1.25;
  display: grid;
  place-items: center;
  border: 1px solid var(--edge);
  border-radius: 16px;
  background: linear-gradient(165deg,color-mix(in oklch,var(--card) 88%,white),var(--card) 60%);
  color: var(--ink);
  cursor: pointer;
  transition: border-color .25s,translate .2s;
}

.chm-03__tile:hover {
  border-color: color-mix(in oklch,var(--acc) 55%,var(--edge));
  translate: 0 -2px;
}

.chm-03__tile:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-03__tile[aria-pressed="true"] {
  border-color: var(--acc);
  color: var(--acc);
}

.chm-03__ico {
  position: relative;
  width: 22px;
  height: 16px;
  display: block;
  transition: rotate .45s cubic-bezier(.3,.9,.35,1);
}

.chm-03__ico i {
  position: absolute;
  left: 0;
  width: 22px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s cubic-bezier(.2,.7,.2,1),rotate .3s cubic-bezier(.2,.7,.2,1),opacity .2s,scale .3s cubic-bezier(.2,.7,.2,1);
}

.chm-03__ico i:nth-child(1) {
  top: 0;
}

.chm-03__ico i:nth-child(2) {
  top: 7px;
}

.chm-03__ico i:nth-child(3) {
  top: 14px;
}

.chm-03__spin[aria-pressed="true"] .chm-03__ico {
  rotate: 180deg;
}

.chm-03__spin[aria-pressed="true"] i:nth-child(1) {
  translate: 0 7px;
  rotate: 45deg;
}

.chm-03__spin[aria-pressed="true"] i:nth-child(2) {
  opacity: 0;
  scale: 0 1;
}

.chm-03__spin[aria-pressed="true"] i:nth-child(3) {
  translate: 0 -7px;
  rotate: -45deg;
}

.chm-03__squeeze i {
  transition: translate .2s cubic-bezier(.55,0,.55,1),rotate .25s cubic-bezier(.2,.7,.2,1) .18s,opacity .15s .08s;
}

.chm-03__squeeze[aria-pressed="true"] i:nth-child(1) {
  translate: 0 7px;
  rotate: 45deg;
}

.chm-03__squeeze[aria-pressed="true"] i:nth-child(2) {
  opacity: 0;
}

.chm-03__squeeze[aria-pressed="true"] i:nth-child(3) {
  translate: 0 -7px;
  rotate: -45deg;
}

.chm-03__arrow i {
  transform-origin: left center;
}

.chm-03__arrow[aria-pressed="true"] i:nth-child(1) {
  scale: .62 1;
  rotate: -40deg;
  translate: 0 1px;
}

.chm-03__arrow[aria-pressed="true"] i:nth-child(3) {
  scale: .62 1;
  rotate: 40deg;
  translate: 0 -1px;
}

.chm-03__drop i {
  transition: translate .32s cubic-bezier(.5,0,.9,.6),rotate .3s cubic-bezier(.2,.7,.2,1) .16s,opacity .26s ease-in;
}

.chm-03__drop[aria-pressed="true"] i:nth-child(2) {
  translate: 3px 16px;
  rotate: 14deg;
  opacity: 0;
}

.chm-03__drop[aria-pressed="true"] i:nth-child(1) {
  translate: 0 7px;
  rotate: 45deg;
}

.chm-03__drop[aria-pressed="true"] i:nth-child(3) {
  translate: 0 -7px;
  rotate: -45deg;
}

@media (prefers-reduced-motion: reduce) {
  .chm-03 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-03__tile').forEach(function (btn) {
    if (btn.dataset.bound) return; btn.dataset.bound = '1';
    btn.addEventListener('click', function () {
      btn.setAttribute('aria-pressed', String(btn.getAttribute('aria-pressed') !== 'true'));
    });
  });
})();
```
