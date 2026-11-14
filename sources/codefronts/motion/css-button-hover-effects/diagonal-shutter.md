---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/diagonal-shutter/"
title: "Diagonal Shutter"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A dynamic CTA where a skewed colour panel sweeps across on hover like a diagonal shutter closing over the surface, with the label swapping colour as it passes."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Shutter
Source: https://codefronts.com/motion/css-button-hover-effects/diagonal-shutter/

A dynamic CTA where a skewed colour panel sweeps across on hover like a diagonal shutter closing over the surface, with the label swapping colour as it passes.
## HTML
```html
<div class="bhe-20-group">
<section class="bhe-20a" aria-label="Diagonal shutter button">
  <button class="bhe-20a__btn" type="button"><span>View gallery</span></button>
</section>
<section class="bhe-20b" aria-label="Twin shutter button">
  <button class="bhe-20b__btn" type="button"><span>Book demo</span></button>
</section>
</div>
```
## CSS
```css
.bhe-20-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-20-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-20a,
.bhe-20a *,
.bhe-20a *::before,
.bhe-20a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-20a {
  --blade: #111;
  --on-blade: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #e9e6dd;
}

.bhe-20a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .03em;
  color: #111;
  padding: 17px 40px;
  border: 2px solid #111;
  border-radius: 8px;
  cursor: pointer;
  background: #f7f5f0;
  transition: color .3s .12s;
}

.bhe-20a__btn span {
  position: relative;
  z-index: 1;
}

.bhe-20a__btn::before {
  content: "";
  position: absolute;
  top: -20%;
  left: -20%;
  width: 140%;
  height: 140%;
  background: var(--blade);
  transform: skewX(-20deg) scaleX(0);
  transform-origin: center;
  transition: transform .45s cubic-bezier(.5,0,.2,1);
  z-index: 0;
}

.bhe-20a__btn:hover,
.bhe-20a__btn:focus-visible {
  color: var(--on-blade);
}

.bhe-20a__btn:hover::before,
.bhe-20a__btn:focus-visible::before {
  transform: skewX(-20deg) scaleX(1);
}

.bhe-20a__btn:focus-visible {
  outline: 3px solid #111;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-20a__btn,
    .bhe-20a__btn::before {
    transition: color .2s;
  }

  .bhe-20a__btn:hover::before,
    .bhe-20a__btn:focus-visible::before {
    transform: skewX(-20deg) scaleX(1);
  }
}

.bhe-20b,
.bhe-20b *,
.bhe-20b *::before,
.bhe-20b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-20b {
  --blade: oklch(0.55 0.17 255);
  --on-blade: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0b1220;
}

.bhe-20b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--blade);
  padding: 17px 42px;
  border: 2px solid var(--blade);
  border-radius: 8px;
  cursor: pointer;
  background: transparent;
  transition: color .3s .14s;
}

.bhe-20b__btn span {
  position: relative;
  z-index: 1;
}

.bhe-20b__btn::before,
.bhe-20b__btn::after {
  content: "";
  position: absolute;
  top: -30%;
  height: 160%;
  width: 70%;
  background: var(--blade);
  transform: skewX(-18deg) scaleX(0);
  transition: transform .4s cubic-bezier(.5,0,.2,1);
  z-index: 0;
}

.bhe-20b__btn::before {
  left: -20%;
  transform-origin: left;
}

.bhe-20b__btn::after {
  right: -20%;
  transform-origin: right;
}

.bhe-20b__btn:hover,
.bhe-20b__btn:focus-visible {
  color: var(--on-blade);
}

.bhe-20b__btn:hover::before,
.bhe-20b__btn:focus-visible::before,
.bhe-20b__btn:hover::after,
.bhe-20b__btn:focus-visible::after {
  transform: skewX(-18deg) scaleX(1);
}

.bhe-20b__btn:focus-visible {
  outline: 3px solid var(--blade);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-20b__btn,
    .bhe-20b__btn::before,
    .bhe-20b__btn::after {
    transition: color .2s;
  }

  .bhe-20b__btn:hover::before,
    .bhe-20b__btn:focus-visible::before,
    .bhe-20b__btn:hover::after,
    .bhe-20b__btn:focus-visible::after {
    transform: skewX(-18deg) scaleX(1);
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
