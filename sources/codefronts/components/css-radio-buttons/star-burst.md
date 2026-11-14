---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/star-burst/"
title: "Rating Star Radio Button Group"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "A five-star rating built the right way: five radio buttons, one per score, with cumulative fill — picking 4 lights stars 1-4 — plus hover preview and a…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rating Star Radio Button Group
Source: https://codefronts.com/components/css-radio-buttons/star-burst/

A five-star rating built the right way: five radio buttons, one per score, with cumulative fill — picking 4 lights stars 1-4 — plus hover preview and a staggered pop when the rating lands. No RTL row-reversal hacks, no JavaScript: the cumulative logic is a two-line :has() selector.
## HTML
```html
<div class="crb-11-group">
<section class="crb-11a" aria-label="Star rating radio group">
  <fieldset class="crb-11a__group">
    <legend class="crb-11a__legend">Rate your experience</legend>
    <div class="crb-11a__stars">
      <label class="crb-11a__star"><input class="crb-11a__input" type="radio" name="crb-11a" value="1"><svg class="crb-11a__glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="crb-11a__sr">1 of 5 stars</span></label>
      <label class="crb-11a__star"><input class="crb-11a__input" type="radio" name="crb-11a" value="2"><svg class="crb-11a__glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="crb-11a__sr">2 of 5 stars</span></label>
      <label class="crb-11a__star"><input class="crb-11a__input" type="radio" name="crb-11a" value="3"><svg class="crb-11a__glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="crb-11a__sr">3 of 5 stars</span></label>
      <label class="crb-11a__star"><input class="crb-11a__input" type="radio" name="crb-11a" value="4" checked><svg class="crb-11a__glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="crb-11a__sr">4 of 5 stars</span></label>
      <label class="crb-11a__star"><input class="crb-11a__input" type="radio" name="crb-11a" value="5"><svg class="crb-11a__glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="crb-11a__sr">5 of 5 stars</span></label>
    </div>
    <p class="crb-11a__hint">Hover to preview · click or use arrow keys to rate</p>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-11-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-11-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-11a,
.crb-11a *,
.crb-11a *::before,
.crb-11a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-11a {
  --star: oklch(0.8 0.16 80);
  --ink: #292317;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #fdf9f0;
}

.crb-11a__group {
  border: none;
  display: grid;
  justify-items: center;
  gap: 16px;
}

.crb-11a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 4px;
}

.crb-11a__stars {
  display: flex;
  gap: 6px;
}

.crb-11a__star {
  position: relative;
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 12px;
  cursor: pointer;
}

.crb-11a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-11a__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.crb-11a__glyph {
  width: 38px;
  height: 38px;
  fill: transparent;
  stroke: #d3c9ae;
  stroke-width: 1.6;
  transition: fill .25s,stroke .25s,transform .25s;
}

.crb-11a__star:has(.crb-11a__input:checked) .crb-11a__glyph,
.crb-11a__star:has(~ .crb-11a__star .crb-11a__input:checked) .crb-11a__glyph {
  fill: var(--star);
  stroke: var(--star);
}

.crb-11a__stars:has(.crb-11a__input:checked) .crb-11a__star:nth-child(1):has(.crb-11a__input:checked) .crb-11a__glyph,
.crb-11a__stars:has(.crb-11a__input:checked) .crb-11a__star:has(~ .crb-11a__star .crb-11a__input:checked):nth-child(1) .crb-11a__glyph {
  animation: crb-11a-pop .4s cubic-bezier(.34,1.56,.64,1) 0ms;
}

.crb-11a__star:nth-child(2):has(.crb-11a__input:checked) .crb-11a__glyph,
.crb-11a__star:has(~ .crb-11a__star .crb-11a__input:checked):nth-child(2) .crb-11a__glyph {
  animation: crb-11a-pop .4s cubic-bezier(.34,1.56,.64,1) 60ms;
}

.crb-11a__star:nth-child(3):has(.crb-11a__input:checked) .crb-11a__glyph,
.crb-11a__star:has(~ .crb-11a__star .crb-11a__input:checked):nth-child(3) .crb-11a__glyph {
  animation: crb-11a-pop .4s cubic-bezier(.34,1.56,.64,1) 120ms;
}

.crb-11a__star:nth-child(4):has(.crb-11a__input:checked) .crb-11a__glyph,
.crb-11a__star:has(~ .crb-11a__star .crb-11a__input:checked):nth-child(4) .crb-11a__glyph {
  animation: crb-11a-pop .4s cubic-bezier(.34,1.56,.64,1) 180ms;
}

.crb-11a__star:nth-child(5):has(.crb-11a__input:checked) .crb-11a__glyph {
  animation: crb-11a-pop .4s cubic-bezier(.34,1.56,.64,1) 240ms;
}

.crb-11a__stars:hover .crb-11a__star .crb-11a__glyph {
  fill: transparent;
  stroke: #d3c9ae;
}

.crb-11a__star:hover .crb-11a__glyph,
.crb-11a__star:has(~ .crb-11a__star:hover) .crb-11a__glyph {
  fill: color-mix(in oklab,var(--star) 55%,white)!important;
  stroke: var(--star)!important;
  transform: scale(1.08);
}

.crb-11a__star:has(.crb-11a__input:focus-visible) {
  outline: 3px solid var(--star);
  outline-offset: 2px;
}

.crb-11a__hint {
  font-size: 13px;
  color: #a49879;
}

@keyframes crb-11a-pop {
  0% {
    transform: scale(.6);
  }

  60% {
    transform: scale(1.25);
  }

  100% {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-11a__glyph {
    transition: fill .2s,stroke .2s;
    animation: none!important;
  }

  .crb-11a__star:hover .crb-11a__glyph {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — label:has(~ label input:checked) fills every star before the checked one (logical DOM order, no RTL hack); the hover trail uses the same pattern with :hover. */
```
