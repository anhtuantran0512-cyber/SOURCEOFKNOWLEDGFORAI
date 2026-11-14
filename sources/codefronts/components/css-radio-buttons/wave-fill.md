---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/wave-fill/"
title: "Liquid Wave Fill Radio Button"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Circular options that fill with liquid when selected: an aqua wave rises inside the checked circle, its surface rolling with two counter-rotating crests…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Wave Fill Radio Button
Source: https://codefronts.com/components/css-radio-buttons/wave-fill/

Circular options that fill with liquid when selected: an aqua wave rises inside the checked circle, its surface rolling with two counter-rotating crests before settling near the brim. A tactile, playful selector for sizes, intensities or hydration-style apps — pure CSS fluid dynamics.
## HTML
```html
<div class="crb-18-group">
<section class="crb-18a" aria-label="Liquid wave fill radio buttons">
  <fieldset class="crb-18a__group">
    <legend class="crb-18a__legend">Roast strength</legend>
    <div class="crb-18a__row">
      <label class="crb-18a__opt"><input class="crb-18a__input" type="radio" name="crb-18a" value="mild"><span class="crb-18a__cup" aria-hidden="true"><span class="crb-18a__wave"></span><span class="crb-18a__wave crb-18a__wave--back"></span><span class="crb-18a__letter">S</span></span><span class="crb-18a__name">Smooth</span></label>
      <label class="crb-18a__opt"><input class="crb-18a__input" type="radio" name="crb-18a" value="medium" checked><span class="crb-18a__cup" aria-hidden="true"><span class="crb-18a__wave"></span><span class="crb-18a__wave crb-18a__wave--back"></span><span class="crb-18a__letter">M</span></span><span class="crb-18a__name">Medium</span></label>
      <label class="crb-18a__opt"><input class="crb-18a__input" type="radio" name="crb-18a" value="bold"><span class="crb-18a__cup" aria-hidden="true"><span class="crb-18a__wave"></span><span class="crb-18a__wave crb-18a__wave--back"></span><span class="crb-18a__letter">B</span></span><span class="crb-18a__name">Bold</span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-18-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-18-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-18a,
.crb-18a *,
.crb-18a *::before,
.crb-18a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-18a {
  --aqua: oklch(0.68 0.13 210);
  --ink: #173039;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #eef6f8;
}

.crb-18a__group {
  border: none;
}

.crb-18a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
  text-align: center;
}

.crb-18a__row {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
  margin-top: 28px;
}

.crb-18a__opt {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 12px;
  cursor: pointer;
}

.crb-18a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-18a__cup {
  position: relative;
  overflow: hidden;
  width: 84px;
  height: 84px;
  border-radius: 50%;
  background: #fff;
  border: 2.5px solid #cfe0e6;
  display: grid;
  place-items: center;
  transition: border-color .3s,box-shadow .3s;
}

.crb-18a__wave {
  position: absolute;
  left: 50%;
  top: 100%;
  width: 220%;
  aspect-ratio: 1;
  margin-left: -110%;
  border-radius: 42%;
  background: var(--aqua);
  transform: translateY(4%) rotate(0deg);
  transition: transform 1s cubic-bezier(.22,1,.36,1);
  pointer-events: none;
}

.crb-18a__wave--back {
  border-radius: 44%;
  background: color-mix(in oklab,var(--aqua) 65%,#0b3a4a);
  opacity: .5;
}

.crb-18a__letter {
  position: relative;
  z-index: 1;
  font-size: 26px;
  font-weight: 800;
  color: #b9cdd5;
  transition: color .4s .2s;
}

.crb-18a__name {
  font-size: 14px;
  font-weight: 650;
  color: #6d8791;
  transition: color .25s;
}

.crb-18a__opt:hover .crb-18a__cup {
  border-color: var(--aqua);
}

.crb-18a__opt:has(.crb-18a__input:checked) .crb-18a__cup {
  border-color: var(--aqua);
  box-shadow: 0 12px 26px -12px color-mix(in oklab,var(--aqua) 60%,transparent);
}

.crb-18a__opt:has(.crb-18a__input:checked) .crb-18a__wave {
  transform: translateY(-64%) rotate(0deg);
  animation: crb-18a-roll 5s linear infinite;
}

.crb-18a__opt:has(.crb-18a__input:checked) .crb-18a__wave--back {
  animation: crb-18a-rollr 7s linear infinite;
}

.crb-18a__opt:has(.crb-18a__input:checked) .crb-18a__letter {
  color: #fff;
}

.crb-18a__opt:has(.crb-18a__input:checked) .crb-18a__name {
  color: var(--ink);
}

.crb-18a__opt:has(.crb-18a__input:focus-visible) .crb-18a__cup {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

@keyframes crb-18a-roll {
  from {
    transform: translateY(-64%) rotate(0deg);
  }

  to {
    transform: translateY(-64%) rotate(360deg);
  }
}

@keyframes crb-18a-rollr {
  from {
    transform: translateY(-64%) rotate(360deg);
  }

  to {
    transform: translateY(-64%) rotate(0deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-18a__wave {
    transition: transform .3s;
  }

  .crb-18a__opt:has(.crb-18a__input:checked) .crb-18a__wave,
    .crb-18a__opt:has(.crb-18a__input:checked) .crb-18a__wave--back {
    animation: none;
    border-radius: 50%;
  }
}
```

## JavaScript
```js
/* No JavaScript — a rounded-square water body rotates inside the clipped circle (its non-circular rim reads as a rolling wave); :checked translates it up to fill 64%. */
```
