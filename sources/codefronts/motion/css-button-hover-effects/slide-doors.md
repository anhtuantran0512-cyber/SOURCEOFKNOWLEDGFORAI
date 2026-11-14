---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/slide-doors/"
title: "Slide Doors"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A CTA where two coloured panels slide in from the left and right to meet in the exact centre on hover — like closing doors — restyling the surface as they…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide Doors
Source: https://codefronts.com/motion/css-button-hover-effects/slide-doors/

A CTA where two coloured panels slide in from the left and right to meet in the exact centre on hover — like closing doors — restyling the surface as they seal (the inward counterpart to topic 19's outward split).
## HTML
```html
<div class="bhe-25-group">
<section class="bhe-25a" aria-label="Slide doors button">
  <button class="bhe-25a__btn" type="button"><span>Open account</span></button>
</section>
<section class="bhe-25b" aria-label="Vertical shutter doors button">
  <button class="bhe-25b__btn" type="button"><span>Reveal offer</span></button>
</section>
</div>
```
## CSS
```css
.bhe-25-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-25-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-25a,
.bhe-25a *,
.bhe-25a *::before,
.bhe-25a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-25a {
  --door: oklch(0.55 0.15 300);
  --on-door: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #f2eef8;
}

.bhe-25a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--door);
  padding: 17px 42px;
  border: 2px solid var(--door);
  border-radius: 10px;
  cursor: pointer;
  background: #fff;
  transition: color .25s .18s;
}

.bhe-25a__btn span {
  position: relative;
  z-index: 1;
}

.bhe-25a__btn::before,
.bhe-25a__btn::after {
  content: "";
  position: absolute;
  top: 0;
  width: 50%;
  height: 100%;
  background: var(--door);
  transition: transform .35s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.bhe-25a__btn::before {
  left: 0;
  transform: translateX(-101%);
}

.bhe-25a__btn::after {
  right: 0;
  transform: translateX(101%);
}

.bhe-25a__btn:hover,
.bhe-25a__btn:focus-visible {
  color: var(--on-door);
}

.bhe-25a__btn:hover::before,
.bhe-25a__btn:focus-visible::before,
.bhe-25a__btn:hover::after,
.bhe-25a__btn:focus-visible::after {
  transform: translateX(0);
}

.bhe-25a__btn:focus-visible {
  outline: 3px solid var(--door);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-25a__btn,
    .bhe-25a__btn::before,
    .bhe-25a__btn::after {
    transition: color .2s;
  }

  .bhe-25a__btn:hover::before,
    .bhe-25a__btn:focus-visible::before,
    .bhe-25a__btn:hover::after,
    .bhe-25a__btn:focus-visible::after {
    transform: translateX(0);
  }
}

.bhe-25b,
.bhe-25b *,
.bhe-25b *::before,
.bhe-25b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-25b {
  --door: oklch(0.58 0.16 200);
  --on-door: #03181c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #e6f2f4;
}

.bhe-25b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--door);
  padding: 18px 44px;
  border: 2px solid var(--door);
  border-radius: 10px;
  cursor: pointer;
  background: #fff;
  transition: color .25s .18s;
}

.bhe-25b__btn span {
  position: relative;
  z-index: 1;
}

.bhe-25b__btn::before,
.bhe-25b__btn::after {
  content: "";
  position: absolute;
  left: 0;
  width: 100%;
  height: 50%;
  background: var(--door);
  transition: transform .35s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.bhe-25b__btn::before {
  top: 0;
  transform: translateY(-101%);
}

.bhe-25b__btn::after {
  bottom: 0;
  transform: translateY(101%);
}

.bhe-25b__btn:hover,
.bhe-25b__btn:focus-visible {
  color: var(--on-door);
}

.bhe-25b__btn:hover::before,
.bhe-25b__btn:focus-visible::before,
.bhe-25b__btn:hover::after,
.bhe-25b__btn:focus-visible::after {
  transform: translateY(0);
}

.bhe-25b__btn:focus-visible {
  outline: 3px solid var(--door);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-25b__btn,
    .bhe-25b__btn::before,
    .bhe-25b__btn::after {
    transition: color .2s;
  }

  .bhe-25b__btn:hover::before,
    .bhe-25b__btn:focus-visible::before,
    .bhe-25b__btn:hover::after,
    .bhe-25b__btn:focus-visible::after {
    transform: translateY(0);
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
