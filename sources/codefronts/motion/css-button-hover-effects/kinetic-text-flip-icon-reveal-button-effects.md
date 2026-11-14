---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/kinetic-text-flip-icon-reveal-button-effects/"
title: "Kinetic Text Flip & Icon Reveal Button Effects"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A snappy micro-interaction: on hover the label slides up and out while a second line or icon slides up to replace it, inside a clipped window."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Kinetic Text Flip & Icon Reveal Button Effects
Source: https://codefronts.com/motion/css-button-hover-effects/kinetic-text-flip-icon-reveal-button-effects/

A snappy micro-interaction: on hover the label slides up and out while a second line or icon slides up to replace it, inside a clipped window. Perfect for 'Add to cart → Added ✓'.
## HTML
```html
<div class="bhe-14-group">
<section class="bhe-14a" aria-label="Text flip reveal button">
  <button class="bhe-14a__btn" type="button"><span class="bhe-14a__col"><span class="bhe-14a__row">Add to cart</span><span class="bhe-14a__row bhe-14a__row--alt" aria-hidden="true">Added&nbsp;✓</span></span></button>
</section>
<section class="bhe-14b" aria-label="Label to icon button">
  <button class="bhe-14b__btn" type="button" aria-label="Next step"><span class="bhe-14b__col"><span class="bhe-14b__row">Next step</span><span class="bhe-14b__row" aria-hidden="true">→</span></span></button>
</section>
</div>
```
## CSS
```css
.bhe-14-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-14-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-14a,
.bhe-14a *,
.bhe-14a *::before,
.bhe-14a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-14a {
  --accent: oklch(0.58 0.15 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0f1512;
}

.bhe-14a__btn {
  overflow: hidden;
  height: 56px;
  min-width: 180px;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 0;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-14a__col {
  display: flex;
  flex-direction: column;
  width: 100%;
  transform: translateY(0);
  transition: transform .4s cubic-bezier(.2,.9,.2,1);
}

.bhe-14a__row {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  padding: 0 40px;
  width: 100%;
}

.bhe-14a__row--alt {
  background: oklch(0.5 0.15 155);
}

.bhe-14a__btn:hover .bhe-14a__col,
.bhe-14a__btn:focus-visible .bhe-14a__col {
  transform: translateY(-50%);
}

.bhe-14a__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-14a__col {
    transition: none;
  }
}

.bhe-14b,
.bhe-14b *,
.bhe-14b *::before,
.bhe-14b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-14b {
  --accent: oklch(0.56 0.17 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0d0b1a;
}

.bhe-14b__btn {
  overflow: hidden;
  height: 56px;
  width: 180px;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-14b__col {
  display: flex;
  flex-direction: column;
  transition: transform .38s cubic-bezier(.2,.9,.2,1);
}

.bhe-14b__row {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  font-size: 20px;
}

.bhe-14b__row:first-child {
  font-size: 16px;
}

.bhe-14b__btn:hover .bhe-14b__col,
.bhe-14b__btn:focus-visible .bhe-14b__col {
  transform: translateY(-56px);
}

.bhe-14b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-14b__col {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
