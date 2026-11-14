---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/hard-shadow-shift/"
title: "Hard Shadow Shift"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A graphic flat-design CTA with a solid blur-free offset shadow."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hard Shadow Shift
Source: https://codefronts.com/motion/css-button-hover-effects/hard-shadow-shift/

A graphic flat-design CTA with a solid blur-free offset shadow. On hover the button slides onto its shadow, flattening against the page as if pressed (monochrome and graphic, distinct from topic 11's neon).
## HTML
```html
<div class="bhe-27-group">
<section class="bhe-27a" aria-label="Hard shadow shift button">
  <button class="bhe-27a__btn" type="button">Get the kit</button>
</section>
<section class="bhe-27b" aria-label="Lift hard shadow button">
  <button class="bhe-27b__btn" type="button">Download deck</button>
</section>
</div>
```
## CSS
```css
.bhe-27-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-27-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-27a,
.bhe-27a *,
.bhe-27a *::before,
.bhe-27a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-27a {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #f0ede4;
}

.bhe-27a__btn {
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 38px;
  border: 2px solid #16130f;
  border-radius: 8px;
  cursor: pointer;
  background: oklch(0.55 0.17 255);
  box-shadow: 6px 6px 0 #16130f;
  transform: translate(0,0);
  transition: transform .16s ease,box-shadow .16s ease;
}

.bhe-27a__btn:hover {
  transform: translate(6px,6px);
  box-shadow: 0 0 0 #16130f;
}

.bhe-27a__btn:active {
  transform: translate(6px,6px) scale(.98);
}

.bhe-27a__btn:focus-visible {
  outline: 3px solid #16130f;
  outline-offset: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-27a__btn {
    transition: box-shadow .12s;
  }

  .bhe-27a__btn:hover {
    transform: translate(6px,6px);
  }
}

.bhe-27b,
.bhe-27b *,
.bhe-27b *::before,
.bhe-27b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-27b {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #faf4e8;
}

.bhe-27b__btn {
  font-size: 16px;
  font-weight: 800;
  color: #1a1206;
  padding: 16px 40px;
  border: 2px solid #1a1206;
  border-radius: 8px;
  cursor: pointer;
  background: #ffcf4d;
  box-shadow: 0 0 0 #1a1206;
  transform: translate(0,0);
  transition: transform .16s ease,box-shadow .16s ease;
}

.bhe-27b__btn:hover {
  transform: translate(-5px,-5px);
  box-shadow: 5px 5px 0 #1a1206;
}

.bhe-27b__btn:active {
  transform: translate(-2px,-2px);
  box-shadow: 2px 2px 0 #1a1206;
}

.bhe-27b__btn:focus-visible {
  outline: 3px solid #1a1206;
  outline-offset: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-27b__btn {
    transition: box-shadow .12s;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
