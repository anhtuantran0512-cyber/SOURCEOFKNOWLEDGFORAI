---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/sliding-background-color-wipe-button-effects/"
title: "Sliding Background Color Wipe Button Effects"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A dependable CTA where a solid colour wipes in and the label colour swaps to stay readable — the most robust, most requested hover for professional product UIs."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Background Color Wipe Button Effects
Source: https://codefronts.com/motion/css-button-hover-effects/sliding-background-color-wipe-button-effects/

A dependable CTA where a solid colour wipes in and the label colour swaps to stay readable — the most robust, most requested hover for professional product UIs.
## HTML
```html
<div class="bhe-12-group">
<section class="bhe-12a" aria-label="Colour wipe button">
  <button class="bhe-12a__btn" type="button"><span>Contact sales</span></button>
</section>
<section class="bhe-12b" aria-label="Bottom-up fill button">
  <button class="bhe-12b__btn" type="button"><span>Get the app</span></button>
</section>
<section class="bhe-12c" aria-label="Center-out fill button">
  <button class="bhe-12c__btn" type="button"><span>Start trial</span></button>
</section>
</div>
```
## CSS
```css
.bhe-12-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-12-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-12a,
.bhe-12a *,
.bhe-12a *::before,
.bhe-12a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-12a {
  --fill: oklch(0.55 0.17 255);
  --on-fill: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #eef1f6;
}

.bhe-12a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 700;
  color: var(--fill);
  padding: 16px 38px;
  border: 2px solid var(--fill);
  border-radius: 10px;
  cursor: pointer;
  background: transparent;
  transition: color .25s .12s;
}

.bhe-12a__btn span {
  position: relative;
  z-index: 1;
}

.bhe-12a__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--fill);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.bhe-12a__btn:hover,
.bhe-12a__btn:focus-visible {
  color: var(--on-fill);
}

.bhe-12a__btn:hover::before,
.bhe-12a__btn:focus-visible::before {
  transform: scaleX(1);
}

.bhe-12a__btn:focus-visible {
  outline: 3px solid var(--fill);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-12a__btn,
    .bhe-12a__btn::before {
    transition: none;
  }

  .bhe-12a__btn:hover::before,
    .bhe-12a__btn:focus-visible::before {
    transform: scaleX(1);
  }
}

.bhe-12b,
.bhe-12b *,
.bhe-12b *::before,
.bhe-12b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-12b {
  --fill: oklch(0.6 0.16 150);
  --on-fill: #04180d;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0d160f;
}

.bhe-12b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--fill);
  padding: 17px 42px;
  border: 2px solid var(--fill);
  border-radius: 10px;
  cursor: pointer;
  background: transparent;
  transition: color .25s .14s;
}

.bhe-12b__btn span {
  position: relative;
  z-index: 1;
}

.bhe-12b__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--fill);
  transform: scaleY(0);
  transform-origin: bottom;
  transition: transform .38s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.bhe-12b__btn:hover,
.bhe-12b__btn:focus-visible {
  color: var(--on-fill);
}

.bhe-12b__btn:hover::before,
.bhe-12b__btn:focus-visible::before {
  transform: scaleY(1);
}

.bhe-12b__btn:focus-visible {
  outline: 3px solid var(--fill);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-12b__btn,
    .bhe-12b__btn::before {
    transition: none;
  }

  .bhe-12b__btn:hover::before,
    .bhe-12b__btn:focus-visible::before {
    transform: scaleY(1);
  }
}

.bhe-12c,
.bhe-12c *,
.bhe-12c *::before,
.bhe-12c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-12c {
  --fill: oklch(0.58 0.18 20);
  --on-fill: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #1a0f10;
}

.bhe-12c__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--fill);
  padding: 17px 42px;
  border: 2px solid var(--fill);
  border-radius: 9999px;
  cursor: pointer;
  background: transparent;
  transition: color .25s .12s;
}

.bhe-12c__btn span {
  position: relative;
  z-index: 1;
}

.bhe-12c__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--fill);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.bhe-12c__btn:hover,
.bhe-12c__btn:focus-visible {
  color: var(--on-fill);
}

.bhe-12c__btn:hover::before,
.bhe-12c__btn:focus-visible::before {
  transform: scaleX(1);
}

.bhe-12c__btn:focus-visible {
  outline: 3px solid var(--fill);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-12c__btn,
    .bhe-12c__btn::before {
    transition: none;
  }

  .bhe-12c__btn:hover::before,
    .bhe-12c__btn:focus-visible::before {
    transform: scaleX(1);
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
