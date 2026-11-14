---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/stagger-fill/"
title: "Stagger Fill"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A rhythmic CTA where several vertical bars rise one after another with staggered delays on hover — like an equaliser sweeping across the button."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stagger Fill
Source: https://codefronts.com/motion/css-button-hover-effects/stagger-fill/

A rhythmic CTA where several vertical bars rise one after another with staggered delays on hover — like an equaliser sweeping across the button.
## HTML
```html
<div class="bhe-33-group">
<section class="bhe-33a" aria-label="Stagger fill button">
  <button class="bhe-33a__btn" type="button"><span class="bhe-33a__bars" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span class="bhe-33a__label">Play set</span></button>
</section>
<section class="bhe-33b" aria-label="Horizontal blinds fill button">
  <button class="bhe-33b__btn" type="button"><span class="bhe-33b__bars" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span class="bhe-33b__label">Reveal</span></button>
</section>
</div>
```
## CSS
```css
.bhe-33-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-33-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-33a,
.bhe-33a *,
.bhe-33a *::before,
.bhe-33a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-33a {
  --bar: oklch(0.7 0.19 145);
  --on-bar: #04170d;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0a120c;
}

.bhe-33a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--bar);
  padding: 17px 44px;
  border: 2px solid var(--bar);
  border-radius: 10px;
  cursor: pointer;
  background: transparent;
  transition: color .25s .16s;
}

.bhe-33a__label {
  position: relative;
  z-index: 1;
}

.bhe-33a__bars {
  position: absolute;
  inset: 0;
  display: flex;
  z-index: 0;
}

.bhe-33a__bars i {
  flex: 1;
  background: var(--bar);
  transform: scaleY(0);
  transform-origin: bottom;
  transition: transform .3s ease;
}

.bhe-33a__bars i:nth-child(1) {
  transition-delay: 0s;
}

.bhe-33a__bars i:nth-child(2) {
  transition-delay: .05s;
}

.bhe-33a__bars i:nth-child(3) {
  transition-delay: .1s;
}

.bhe-33a__bars i:nth-child(4) {
  transition-delay: .15s;
}

.bhe-33a__btn:hover .bhe-33a__bars i,
.bhe-33a__btn:focus-visible .bhe-33a__bars i {
  transform: scaleY(1);
}

.bhe-33a__btn:hover,
.bhe-33a__btn:focus-visible {
  color: var(--on-bar);
}

.bhe-33a__btn:focus-visible {
  outline: 3px solid var(--bar);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-33a__bars i {
    transition: none;
  }
}

.bhe-33b,
.bhe-33b *,
.bhe-33b *::before,
.bhe-33b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-33b {
  --bar: oklch(0.62 0.17 280);
  --on-bar: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0d0a1a;
}

.bhe-33b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--bar);
  padding: 18px 46px;
  border: 2px solid var(--bar);
  border-radius: 10px;
  cursor: pointer;
  background: transparent;
  transition: color .25s .18s;
}

.bhe-33b__label {
  position: relative;
  z-index: 1;
}

.bhe-33b__bars {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  z-index: 0;
}

.bhe-33b__bars i {
  flex: 1;
  background: var(--bar);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .32s ease;
}

.bhe-33b__bars i:nth-child(1) {
  transition-delay: 0s;
}

.bhe-33b__bars i:nth-child(2) {
  transition-delay: .06s;
  transform-origin: right;
}

.bhe-33b__bars i:nth-child(3) {
  transition-delay: .12s;
}

.bhe-33b__bars i:nth-child(4) {
  transition-delay: .18s;
  transform-origin: right;
}

.bhe-33b__btn:hover .bhe-33b__bars i,
.bhe-33b__btn:focus-visible .bhe-33b__bars i {
  transform: scaleX(1);
}

.bhe-33b__btn:hover,
.bhe-33b__btn:focus-visible {
  color: var(--on-bar);
}

.bhe-33b__btn:focus-visible {
  outline: 3px solid var(--bar);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-33b__bars i {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
