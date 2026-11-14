---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/3d-push/"
title: "Tactile 3D Push Button Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Radio options as chunky mechanical keys: each sits proud on a hard shadow base, and the selected key stays physically pressed down — travel, shadow and a…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tactile 3D Push Button Radio
Source: https://codefronts.com/components/css-radio-buttons/3d-push/

Radio options as chunky mechanical keys: each sits proud on a hard shadow base, and the selected key stays physically pressed down — travel, shadow and a darkened cap all agree that it's IN. The checked state IS the pressed state, which makes selection instantly readable. Deeply satisfying, pure CSS.
## HTML
```html
<div class="crb-23-group">
<section class="crb-23a" aria-label="Tactile 3D push button radio">
  <fieldset class="crb-23a__group">
    <legend class="crb-23a__legend">Drive mode</legend>
    <div class="crb-23a__deck">
      <label class="crb-23a__opt"><input class="crb-23a__input" type="radio" name="crb-23a" value="eco"><span class="crb-23a__key"><span class="crb-23a__led" aria-hidden="true"></span>Eco</span></label>
      <label class="crb-23a__opt"><input class="crb-23a__input" type="radio" name="crb-23a" value="comfort" checked><span class="crb-23a__key"><span class="crb-23a__led" aria-hidden="true"></span>Comfort</span></label>
      <label class="crb-23a__opt"><input class="crb-23a__input" type="radio" name="crb-23a" value="sport"><span class="crb-23a__key"><span class="crb-23a__led" aria-hidden="true"></span>Sport</span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-23-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-23-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-23a,
.crb-23a *,
.crb-23a *::before,
.crb-23a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-23a {
  --cap: #f2ede4;
  --led: oklch(0.72 0.19 145);
  --ink: #3a3428;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #dcd5c8;
}

.crb-23a__group {
  border: none;
}

.crb-23a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
  text-align: center;
}

.crb-23a__deck {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  justify-content: center;
  margin-top: 30px;
  padding: 22px 26px;
  background: #cfc7b7;
  border-radius: 20px;
  box-shadow: inset 0 2px 6px rgba(70,60,40,.25);
}

.crb-23a__opt {
  position: relative;
  cursor: pointer;
}

.crb-23a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-23a__key {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 118px;
  justify-content: center;
  padding: 15px 24px;
  font-size: 15px;
  font-weight: 750;
  color: var(--ink);
  background: linear-gradient(180deg,#fff,var(--cap));
  border-radius: 12px;
  transform: translateY(-6px);
  box-shadow: 0 6px 0 #b3a88f,0 10px 14px -4px rgba(70,60,40,.35),inset 0 1px 0 #fff;
  transition: transform .12s ease,box-shadow .12s ease,background .2s;
}

.crb-23a__led {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #b8b0a0;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.25);
  transition: background .15s,box-shadow .15s;
}

.crb-23a__opt:hover .crb-23a__key {
  transform: translateY(-7px);
  box-shadow: 0 7px 0 #b3a88f,0 12px 16px -4px rgba(70,60,40,.35),inset 0 1px 0 #fff;
}

.crb-23a__opt:active .crb-23a__key {
  transform: translateY(-1px);
  box-shadow: 0 1px 0 #b3a88f,0 3px 6px -2px rgba(70,60,40,.3),inset 0 1px 0 #fff;
}

.crb-23a__opt:has(.crb-23a__input:checked) .crb-23a__key {
  transform: translateY(-1px);
  background: linear-gradient(180deg,#f4efe6,#e6dfd0);
  box-shadow: 0 1px 0 #b3a88f,0 2px 4px -2px rgba(70,60,40,.3),inset 0 2px 4px rgba(70,60,40,.18);
}

.crb-23a__opt:has(.crb-23a__input:checked) .crb-23a__led {
  background: var(--led);
  box-shadow: 0 0 6px var(--led),0 0 14px color-mix(in oklab,var(--led) 55%,transparent);
}

.crb-23a__opt:has(.crb-23a__input:focus-visible) .crb-23a__key {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-23a__key {
    transition: background .1s,box-shadow .1s;
  }
}
```

## JavaScript
```js
/* No JavaScript — checked = pressed: :has(input:checked) drives the cap down 5px while the hard base shadow collapses in lockstep; the browser's radio exclusivity pops the old key back up. */
```
