---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/3d-flip/"
title: "3D Flip"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A CTA that flips like a physical card: on hover it rotates 180° in 3D to reveal a styled back face with a different label and colour."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip
Source: https://codefronts.com/motion/css-button-hover-effects/3d-flip/

A CTA that flips like a physical card: on hover it rotates 180° in 3D to reveal a styled back face with a different label and colour.
## HTML
```html
<div class="bhe-23-group">
<section class="bhe-23a" aria-label="3D flip button">
  <button class="bhe-23a__btn" type="button" aria-label="Follow"><span class="bhe-23a__inner"><span class="bhe-23a__face bhe-23a__face--a">Follow</span><span class="bhe-23a__face bhe-23a__face--b" aria-hidden="true">Following ✓</span></span></button>
</section>
<section class="bhe-23b" aria-label="3D roll button">
  <button class="bhe-23b__btn" type="button" aria-label="Download"><span class="bhe-23b__inner"><span class="bhe-23b__face bhe-23b__face--a">Download</span><span class="bhe-23b__face bhe-23b__face--b" aria-hidden="true">Saved ↓</span></span></button>
</section>
</div>
```
## CSS
```css
.bhe-23-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-23-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-23a,
.bhe-23a *,
.bhe-23a *::before,
.bhe-23a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-23a {
  --face-a: oklch(0.55 0.16 265);
  --face-b: oklch(0.6 0.15 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #101018;
  perspective: 900px;
}

.bhe-23a__btn {
  width: 200px;
  height: 58px;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: transparent;
  padding: 0;
}

.bhe-23a__inner {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .5s cubic-bezier(.4,0,.2,1);
}

.bhe-23a__face {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border-radius: 12px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.bhe-23a__face--a {
  background: var(--face-a);
}

.bhe-23a__face--b {
  background: var(--face-b);
  transform: rotateY(180deg);
}

.bhe-23a__btn:hover .bhe-23a__inner,
.bhe-23a__btn:focus-visible .bhe-23a__inner {
  transform: rotateY(180deg);
}

.bhe-23a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
  border-radius: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-23a__inner {
    transition: none;
  }
}

.bhe-23b,
.bhe-23b *,
.bhe-23b *::before,
.bhe-23b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-23b {
  --face-a: oklch(0.56 0.16 210);
  --face-b: oklch(0.62 0.15 145);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0a1418;
  perspective: 700px;
}

.bhe-23b__btn {
  width: 190px;
  height: 58px;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: transparent;
  padding: 0;
}

.bhe-23b__inner {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .5s cubic-bezier(.4,0,.2,1);
}

.bhe-23b__face {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border-radius: 12px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.bhe-23b__face--a {
  background: var(--face-a);
}

.bhe-23b__face--b {
  background: var(--face-b);
  transform: rotateX(180deg);
}

.bhe-23b__btn:hover .bhe-23b__inner,
.bhe-23b__btn:focus-visible .bhe-23b__inner {
  transform: rotateX(180deg);
}

.bhe-23b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
  border-radius: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-23b__inner {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
