---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/clip-mask/"
title: "Image Clip Mask Option Selector"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "A destination picker where photography is the control: each option is a real photo clipped into a tall arch; unselected images rest desaturated and dim, and…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image Clip Mask Option Selector
Source: https://codefronts.com/components/css-radio-buttons/clip-mask/

A destination picker where photography is the control: each option is a real photo clipped into a tall arch; unselected images rest desaturated and dim, and picking one blooms it to full colour while the arch relaxes into a softer, wider mask and the caption slides up. Editorial, gallery-grade selection.
## HTML
```html
<div class="crb-19-group">
<section class="crb-19a" aria-label="Image clip mask option selector">
  <fieldset class="crb-19a__group">
    <legend class="crb-19a__legend">Where to next?</legend>
    <div class="crb-19a__row">
      <label class="crb-19a__opt">
        <input class="crb-19a__input" type="radio" name="crb-19a" value="alps" checked>
        <span class="crb-19a__arch"><img class="crb-19a__img" src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=480&q=80&auto=format&fit=crop" alt="Snow-capped alpine peaks at dawn" loading="lazy"><span class="crb-19a__cap">The Alps</span></span>
      </label>
      <label class="crb-19a__opt">
        <input class="crb-19a__input" type="radio" name="crb-19a" value="coast">
        <span class="crb-19a__arch"><img class="crb-19a__img" src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=480&q=80&auto=format&fit=crop" alt="Turquoise water on a white sand beach" loading="lazy"><span class="crb-19a__cap">The Coast</span></span>
      </label>
      <label class="crb-19a__opt">
        <input class="crb-19a__input" type="radio" name="crb-19a" value="forest">
        <span class="crb-19a__arch"><img class="crb-19a__img" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=480&q=80&auto=format&fit=crop" alt="Sunlight through a tall green forest" loading="lazy"><span class="crb-19a__cap">The Forest</span></span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-19-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-19-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-19a,
.crb-19a *,
.crb-19a *::before,
.crb-19a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-19a {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #141210;
}

.crb-19a__group {
  border: none;
}

.crb-19a__legend {
  font-size: 26px;
  font-weight: 750;
  color: #f4efe8;
  letter-spacing: -.02em;
  text-align: center;
}

.crb-19a__row {
  display: flex;
  flex-wrap: wrap;
  gap: 22px;
  justify-content: center;
  margin-top: 30px;
}

.crb-19a__opt {
  position: relative;
  cursor: pointer;
}

.crb-19a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-19a__arch {
  position: relative;
  overflow: hidden;
  display: block;
  width: 170px;
  height: 250px;
  border-radius: 85px 85px 18px 18px;
  transition: border-radius .5s cubic-bezier(.22,1,.36,1),transform .4s,box-shadow .4s;
}

.crb-19a__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: grayscale(1) brightness(.65);
  transform: scale(1.08);
  transition: filter .55s ease,transform .8s cubic-bezier(.22,1,.36,1);
}

.crb-19a__cap {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 26px 14px 12px;
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: .02em;
  color: #fff;
  text-align: center;
  background: linear-gradient(180deg,transparent,rgba(10,8,5,.75));
  transform: translateY(10px);
  opacity: .75;
  transition: transform .4s,opacity .4s;
}

.crb-19a__opt:hover .crb-19a__img {
  filter: grayscale(.4) brightness(.85);
}

.crb-19a__opt:has(.crb-19a__input:checked) .crb-19a__arch {
  border-radius: 26px;
  transform: translateY(-6px);
  box-shadow: 0 26px 50px -22px rgba(0,0,0,.85);
}

.crb-19a__opt:has(.crb-19a__input:checked) .crb-19a__img {
  filter: none;
  transform: scale(1);
}

.crb-19a__opt:has(.crb-19a__input:checked) .crb-19a__cap {
  transform: translateY(0);
  opacity: 1;
}

.crb-19a__opt:has(.crb-19a__input:focus-visible) .crb-19a__arch {
  outline: 3px solid #f4efe8;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-19a__arch,
    .crb-19a__img,
    .crb-19a__cap {
    transition: filter .3s,opacity .3s;
  }

  .crb-19a__opt:has(.crb-19a__input:checked) .crb-19a__arch {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — border-radius morphs the arch mask (50%→26px interpolates natively, no clip-path needed) while the photo blooms from grayscale via :has(input:checked). */
```
