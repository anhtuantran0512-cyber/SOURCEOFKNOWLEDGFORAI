---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/minimalist-border-outline-drawing-hover-effects/"
title: "Minimalist Border & Outline Drawing Hover Effects"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A refined understated CTA for editorial and luxury layouts: at rest it's just text, and on hover a hairline stroke draws itself continuously around the…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Border & Outline Drawing Hover Effects
Source: https://codefronts.com/motion/css-button-hover-effects/minimalist-border-outline-drawing-hover-effects/

A refined understated CTA for editorial and luxury layouts: at rest it's just text, and on hover a hairline stroke draws itself continuously around the rounded-rectangle perimeter.
## HTML
```html
<div class="bhe-09-group">
<section class="bhe-09a" aria-label="Outline drawing button">
  <button class="bhe-09a__btn" type="button"><svg class="bhe-09a__box" preserveAspectRatio="none" aria-hidden="true"><rect class="bhe-09a__rect" x="1" y="1" rx="12" ry="12"/></svg><span>Read the story</span></button>
</section>
<section class="bhe-09b" aria-label="Underline to box button">
  <button class="bhe-09b__btn" type="button"><span>Discover more</span></button>
</section>
</div>
```
## CSS
```css
.bhe-09-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-09-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-09a,
.bhe-09a *,
.bhe-09a *::before,
.bhe-09a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-09a {
  --line: oklch(0.45 0.03 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #f6f5f1;
}

.bhe-09a__btn {
  position: relative;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--line);
  padding: 20px 42px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.bhe-09a__btn > span {
  position: relative;
  z-index: 1;
}

.bhe-09a__box {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: visible;
}

.bhe-09a__rect {
  fill: none;
  stroke: var(--line);
  stroke-width: 2;
  width: calc(100% - 2px);
  height: calc(100% - 2px);
}

.bhe-09a__rect {
  stroke-dasharray: 0 1000;
  transition: stroke-dasharray .8s ease;
}

.bhe-09a__btn:hover .bhe-09a__rect,
.bhe-09a__btn:focus-visible .bhe-09a__rect {
  stroke-dasharray: 1000 0;
}

.bhe-09a__btn:focus-visible {
  outline: none;
}

.bhe-09a__btn:focus-visible > span {
  text-decoration: underline;
  text-underline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-09a__rect {
    transition: none;
    stroke-dasharray: 1000 0;
    opacity: .5;
  }
}

.bhe-09b,
.bhe-09b *,
.bhe-09b *::before,
.bhe-09b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-09b {
  --line: oklch(0.5 0.14 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #faf6f4;
}

.bhe-09b__btn {
  position: relative;
  font-size: 16px;
  font-weight: 700;
  color: var(--line);
  padding: 16px 32px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.bhe-09b__btn::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 2px;
  background: var(--line);
  transform: scaleX(1);
  transform-origin: left;
  transition: transform .3s ease;
}

.bhe-09b__btn::after {
  content: "";
  position: absolute;
  inset: 0;
  border: 2px solid var(--line);
  border-bottom: none;
  clip-path: inset(0 0 100% 0);
  transition: clip-path .35s ease .15s;
}

.bhe-09b__btn:hover::after,
.bhe-09b__btn:focus-visible::after {
  clip-path: inset(0 0 0 0);
}

.bhe-09b__btn:focus-visible {
  outline: none;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-09b__btn::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
