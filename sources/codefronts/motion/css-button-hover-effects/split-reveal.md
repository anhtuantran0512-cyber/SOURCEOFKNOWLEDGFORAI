---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/split-reveal/"
title: "Split Reveal"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A theatrical CTA: on hover the surface splits into top and bottom halves that slide apart, revealing a contrasting label behind — an outward curtain…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Reveal
Source: https://codefronts.com/motion/css-button-hover-effects/split-reveal/

A theatrical CTA: on hover the surface splits into top and bottom halves that slide apart, revealing a contrasting label behind — an outward curtain (distinct from topic 25's inward doors).
## HTML
```html
<div class="bhe-19-group">
<section class="bhe-19a" aria-label="Split reveal button">
  <button class="bhe-19a__btn" type="button" data-front="Hover me"><span class="bhe-19a__back">Let's go →</span></button>
</section>
<section class="bhe-19b" aria-label="Vertical split reveal button">
  <button class="bhe-19b__btn" type="button" data-front="Reveal"><span class="bhe-19b__back">Unlock ✦</span></button>
</section>
</div>
```
## CSS
```css
.bhe-19-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-19-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-19a,
.bhe-19a *,
.bhe-19a *::before,
.bhe-19a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-19a {
  --front: oklch(0.5 0.16 285);
  --back: oklch(0.72 0.17 145);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0d0b1a;
}

.bhe-19a__btn {
  position: relative;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #04140b;
  padding: 18px 44px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--back);
}

.bhe-19a__back {
  position: relative;
  z-index: 0;
}

.bhe-19a__btn::before,
.bhe-19a__btn::after {
  content: attr(data-front);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  background: var(--front);
  z-index: 1;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.bhe-19a__btn::before {
  clip-path: inset(0 0 calc(50% - 1px) 0);
}

.bhe-19a__btn::after {
  clip-path: inset(calc(50% - 1px) 0 0 0);
}

.bhe-19a__btn:hover::before,
.bhe-19a__btn:focus-visible::before {
  transform: translateY(-100%);
}

.bhe-19a__btn:hover::after,
.bhe-19a__btn:focus-visible::after {
  transform: translateY(100%);
}

.bhe-19a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-19a__btn::before,
    .bhe-19a__btn::after {
    transition: none;
  }
}

.bhe-19b,
.bhe-19b *,
.bhe-19b *::before,
.bhe-19b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-19b {
  --front: oklch(0.52 0.16 25);
  --back: oklch(0.72 0.16 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #160b0a;
}

.bhe-19b__btn {
  position: relative;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #1a1206;
  padding: 18px 46px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--back);
}

.bhe-19b__back {
  position: relative;
  z-index: 0;
}

.bhe-19b__btn::before,
.bhe-19b__btn::after {
  content: attr(data-front);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  background: var(--front);
  z-index: 1;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.bhe-19b__btn::before {
  clip-path: inset(0 calc(50% - 1px) 0 0);
}

.bhe-19b__btn::after {
  clip-path: inset(0 0 0 calc(50% - 1px));
}

.bhe-19b__btn:hover::before,
.bhe-19b__btn:focus-visible::before {
  transform: translateX(-100%);
}

.bhe-19b__btn:hover::after,
.bhe-19b__btn:focus-visible::after {
  transform: translateX(100%);
}

.bhe-19b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-19b__btn::before,
    .bhe-19b__btn::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
