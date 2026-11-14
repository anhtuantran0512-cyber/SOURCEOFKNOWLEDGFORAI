---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/dual-line-intersection-border-draw/"
title: "Dual-Line Intersection Border Draw"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A crisp architectural outline CTA for editorial and agency sites: on hover two lines draw from opposite corners and meet to close a rectangular border around…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dual-Line Intersection Border Draw
Source: https://codefronts.com/motion/css-button-hover-effects/dual-line-intersection-border-draw/

A crisp architectural outline CTA for editorial and agency sites: on hover two lines draw from opposite corners and meet to close a rectangular border around the label.
## HTML
```html
<div class="bhe-05-group">
<section class="bhe-05a" aria-label="Dual-line border draw button">
  <button class="bhe-05a__btn" type="button"><span>Explore work</span></button>
</section>
<section class="bhe-05b" aria-label="Corner bracket button">
  <button class="bhe-05b__btn" type="button"><span>View case study</span></button>
</section>
</div>
```
## CSS
```css
.bhe-05-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-05-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-05a,
.bhe-05a *,
.bhe-05a *::before,
.bhe-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-05a {
  --line: oklch(0.55 0.02 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #f4f3ef;
}

.bhe-05a__btn {
  position: relative;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--line);
  padding: 18px 40px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.bhe-05a__btn::before,
.bhe-05a__btn::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.bhe-05a__btn::before {
  border-top: 2px solid var(--line);
  border-right: 2px solid var(--line);
  transform: scale(0);
  transform-origin: top left;
  transition: transform .3s ease;
}

.bhe-05a__btn::after {
  border-bottom: 2px solid var(--line);
  border-left: 2px solid var(--line);
  transform: scale(0);
  transform-origin: bottom right;
  transition: transform .3s ease;
}

.bhe-05a__btn:hover::before,
.bhe-05a__btn:focus-visible::before {
  transform: scale(1);
  transition-delay: 0s;
}

.bhe-05a__btn:hover::after,
.bhe-05a__btn:focus-visible::after {
  transform: scale(1);
  transition-delay: .3s;
}

.bhe-05a__btn:focus-visible {
  outline: 2px dashed var(--line);
  outline-offset: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-05a__btn::before,
    .bhe-05a__btn::after {
    transition: none;
  }
}

.bhe-05b,
.bhe-05b *,
.bhe-05b *::before,
.bhe-05b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-05b {
  --line: oklch(0.72 0.16 190);
  font-family: ui-monospace,'Segoe UI',monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0a1416;
}

.bhe-05b__btn {
  position: relative;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--line);
  padding: 20px 46px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.bhe-05b__btn::before,
.bhe-05b__btn::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border: 2px solid var(--line);
  transition: width .3s ease,height .3s ease;
}

.bhe-05b__btn::before {
  top: 0;
  left: 0;
  border-right: none;
  border-bottom: none;
}

.bhe-05b__btn::after {
  bottom: 0;
  right: 0;
  border-left: none;
  border-top: none;
}

.bhe-05b__btn:hover::before,
.bhe-05b__btn:focus-visible::before,
.bhe-05b__btn:hover::after,
.bhe-05b__btn:focus-visible::after {
  width: 100%;
  height: 100%;
}

.bhe-05b__btn:focus-visible {
  outline: none;
  text-decoration: underline;
  text-underline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-05b__btn::before,
    .bhe-05b__btn::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
