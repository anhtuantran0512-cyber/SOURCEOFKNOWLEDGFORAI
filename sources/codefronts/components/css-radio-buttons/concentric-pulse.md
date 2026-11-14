---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/concentric-pulse/"
title: "Concentric Ripple Animation Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "An animated radio button with real physicality: on check, two concentric rings burst outward from the dot like a droplet hitting water — a crisp inner ring…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Concentric Ripple Animation Radio
Source: https://codefronts.com/components/css-radio-buttons/concentric-pulse/

An animated radio button with real physicality: on check, two concentric rings burst outward from the dot like a droplet hitting water — a crisp inner ring chased by a softer outer one — while the dot itself springs in. A pure CSS micro-interaction that makes forms feel alive.
## HTML
```html
<div class="crb-07-group">
<section class="crb-07a" aria-label="Concentric ripple radio buttons">
  <fieldset class="crb-07a__group">
    <legend class="crb-07a__legend">Meeting length</legend>
    <div class="crb-07a__list">
      <label class="crb-07a__row"><span class="crb-07a__well"><input class="crb-07a__input" type="radio" name="crb-07a" value="15"><span class="crb-07a__ring" aria-hidden="true"></span></span><span class="crb-07a__text">15 minutes</span></label>
      <label class="crb-07a__row"><span class="crb-07a__well"><input class="crb-07a__input" type="radio" name="crb-07a" value="30" checked><span class="crb-07a__ring" aria-hidden="true"></span></span><span class="crb-07a__text">30 minutes</span></label>
      <label class="crb-07a__row"><span class="crb-07a__well"><input class="crb-07a__input" type="radio" name="crb-07a" value="60"><span class="crb-07a__ring" aria-hidden="true"></span></span><span class="crb-07a__text">1 hour</span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-07-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-07-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-07a,
.crb-07a *,
.crb-07a *::before,
.crb-07a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-07a {
  --accent: oklch(0.6 0.17 220);
  --ink: #1d2530;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f2f7fa;
}

.crb-07a__group {
  border: none;
  width: min(340px,100%);
}

.crb-07a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
}

.crb-07a__list {
  display: grid;
  margin-top: 14px;
}

.crb-07a__row {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 52px;
  padding: 0 8px;
  border-radius: 12px;
  cursor: pointer;
  transition: background .2s;
}

.crb-07a__row:hover {
  background: rgba(255,255,255,.85);
}

.crb-07a__well {
  position: relative;
  width: 24px;
  height: 24px;
  flex: none;
}

.crb-07a__input {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  z-index: 2;
  width: 24px;
  height: 24px;
  border: 2px solid #a9b6c4;
  border-radius: 50%;
  display: grid;
  place-items: center;
  cursor: pointer;
  background: #fff;
  transition: border-color .25s;
}

.crb-07a__input::before {
  content: "";
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--accent);
  transform: scale(0);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.crb-07a__input::after {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: 50%;
  border: 2px solid var(--accent);
  opacity: 0;
  pointer-events: none;
}

.crb-07a__ring {
  position: absolute;
  inset: 0;
  z-index: 1;
  border-radius: 50%;
  border: 2px solid color-mix(in oklab,var(--accent) 70%,transparent);
  opacity: 0;
  pointer-events: none;
}

.crb-07a__input:checked {
  border-color: var(--accent);
}

.crb-07a__input:checked::before {
  transform: scale(1);
}

.crb-07a__input:checked::after {
  animation: crb-07a-burst .7s cubic-bezier(.22,1,.36,1);
}

.crb-07a__input:checked + .crb-07a__ring {
  animation: crb-07a-burst .8s cubic-bezier(.22,1,.36,1) .12s;
}

.crb-07a__input:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.crb-07a__text {
  font-size: 15.5px;
  color: var(--ink);
}

@keyframes crb-07a-burst {
  0% {
    transform: scale(.4);
    opacity: .9;
  }

  100% {
    transform: scale(2.6);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-07a__input:checked::after,
    .crb-07a__input:checked + .crb-07a__ring {
    animation: none;
  }

  .crb-07a__input::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two ring layers (::after + a sibling span) run a one-shot scale/fade keyframe on :checked, the second delayed 120ms for the concentric water-drop effect. */
```
