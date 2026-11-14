---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/staircase-bricks/"
title: "Staircase Bricks"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "Cards staggered by fixed, repeating horizontal and vertical offsets into a strict stair-step cascade, so a uniform edge of every card stays visible."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staircase Bricks
Source: https://codefronts.com/components/css-stacked-cards/staircase-bricks/

Cards staggered by fixed, repeating horizontal and vertical offsets into a strict stair-step cascade, so a uniform edge of every card stays visible. Hover any step to slide it out and read its full face.
## HTML
```html
<section class="scd-13" aria-label="Staircase cascade of cards">
  <div class="scd-13__stair">
    <a class="scd-13__card" href="#" style="--i:0;--c:oklch(0.64 0.16 265)"><b>Plan</b><span>Scope &amp; milestones</span></a>
    <a class="scd-13__card" href="#" style="--i:1;--c:oklch(0.64 0.15 210)"><b>Design</b><span>Flows &amp; system</span></a>
    <a class="scd-13__card" href="#" style="--i:2;--c:oklch(0.66 0.15 160)"><b>Build</b><span>Ship in slices</span></a>
    <a class="scd-13__card" href="#" style="--i:3;--c:oklch(0.68 0.16 90)"><b>Launch</b><span>Measure &amp; iterate</span></a>
  </div>
</section>
```
## CSS
```css
.scd-13,
.scd-13 *,
.scd-13 *::before,
.scd-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-13 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #12141c;
}

.scd-13__stair {
  position: relative;
  width: 260px;
  height: 280px;
}

.scd-13__card {
  position: absolute;
  left: 0;
  top: 0;
  width: 190px;
  height: 120px;
  padding: 20px;
  border-radius: 16px;
  color: #fff;
  text-decoration: none;
  background: var(--c);
  box-shadow: 0 18px 34px -20px rgba(0,0,0,.8);
  transform: translate(calc(var(--i) * 24px),calc(var(--i) * 46px));
  z-index: calc(var(--i) + 1);
  transition: transform .35s cubic-bezier(.3,.9,.3,1),box-shadow .3s;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.scd-13__card b {
  font-size: 19px;
  font-weight: 800;
}

.scd-13__card span {
  font-size: 13px;
  opacity: .9;
}

.scd-13__card:hover,
.scd-13__card:focus-visible {
  transform: translate(calc(var(--i) * 24px + 40px),calc(var(--i) * 46px - 8px));
  box-shadow: 0 28px 48px -20px rgba(0,0,0,.9);
  z-index: 20;
  outline: none;
}

.scd-13__card:focus-visible {
  box-shadow: 0 0 0 3px #fff,0 28px 48px -20px rgba(0,0,0,.9);
}

@media (prefers-reduced-motion: reduce) {
  .scd-13__card {
    transition: box-shadow .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — an index-driven constant translate builds the staircase; :hover slides the target step out along the diagonal. */
```
