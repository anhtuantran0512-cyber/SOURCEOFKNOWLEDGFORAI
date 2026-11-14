---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/isometric-tactile-3d-depress/"
title: "Isometric Tactile 3D Depress"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A chunky game-UI button in isometric perspective with a thick extruded side, so it looks like a real key. On hover it rotates flat and sinks as if pressed."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Isometric Tactile 3D Depress
Source: https://codefronts.com/motion/css-button-hover-effects/isometric-tactile-3d-depress/

A chunky game-UI button in isometric perspective with a thick extruded side, so it looks like a real key. On hover it rotates flat and sinks as if pressed.
## HTML
```html
<div class="bhe-06-group">
<section class="bhe-06a" aria-label="Isometric 3D button">
  <button class="bhe-06a__btn" type="button">Press me</button>
</section>
<section class="bhe-06b" aria-label="Pushable 3D pill button">
  <button class="bhe-06b__btn" type="button"><span class="bhe-06b__edge" aria-hidden="true"></span><span class="bhe-06b__front">Buy now</span></button>
</section>
</div>
```
## CSS
```css
.bhe-06-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-06-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-06a,
.bhe-06a *,
.bhe-06a *::before,
.bhe-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-06a {
  --cap: oklch(0.72 0.16 155);
  --side: oklch(0.5 0.13 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 70px 24px;
  perspective: 700px;
}

.bhe-06a__btn {
  font-size: 18px;
  font-weight: 800;
  color: #08351f;
  padding: 18px 40px;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  background: var(--cap);
  transform: rotateX(15deg) translateY(-6px);
  box-shadow: 0 1px 0 var(--side),0 2px 0 var(--side),0 3px 0 var(--side),0 4px 0 var(--side),0 5px 0 var(--side),0 6px 0 var(--side),0 7px 0 var(--side),0 8px 0 var(--side),0 20px 24px -8px rgba(0,0,0,.45);
  transition: transform .22s cubic-bezier(.3,.7,.4,1),box-shadow .22s;
}

.bhe-06a__btn:hover {
  transform: rotateX(4deg) translateY(-1px);
  box-shadow: 0 1px 0 var(--side),0 2px 0 var(--side),0 3px 0 var(--side),0 4px 0 var(--side),0 12px 16px -8px rgba(0,0,0,.4);
}

.bhe-06a__btn:active {
  transform: rotateX(0deg) translateY(2px);
  box-shadow: 0 1px 0 var(--side),0 2px 0 var(--side),0 6px 10px -6px rgba(0,0,0,.4);
}

.bhe-06a__btn:focus-visible {
  outline: 3px solid #08351f;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-06a__btn {
    transition: box-shadow .15s;
  }
}

.bhe-06b,
.bhe-06b *,
.bhe-06b *::before,
.bhe-06b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-06b {
  --front: oklch(0.68 0.18 40);
  --edge: oklch(0.42 0.14 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #1a120c;
}

.bhe-06b__btn {
  position: relative;
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  border: none;
  background: transparent;
  cursor: pointer;
  padding: 0;
  border-radius: 14px;
}

.bhe-06b__edge {
  position: absolute;
  inset: 0;
  background: var(--edge);
  border-radius: 14px;
}

.bhe-06b__front {
  display: block;
  position: relative;
  padding: 16px 40px;
  border-radius: 14px;
  background: var(--front);
  transform: translateY(-6px);
  transition: transform .12s cubic-bezier(.3,.7,.4,1);
}

.bhe-06b__btn:hover .bhe-06b__front {
  transform: translateY(-8px);
}

.bhe-06b__btn:active .bhe-06b__front {
  transform: translateY(-1px);
}

.bhe-06b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-06b__front {
    transition: transform .1s;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
