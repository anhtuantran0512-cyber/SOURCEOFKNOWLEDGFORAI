---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/scroll-snap-slider/"
title: "Scroll-Snap Slider"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A native-feeling carousel with zero carousel library: a column-flow grid inside a snap container, slides centered by scroll-snap-align, momentum and touch…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Snap Slider
Source: https://codefronts.com/layouts/css-grid-layouts/scroll-snap-slider/

A native-feeling carousel with zero carousel library: a column-flow grid inside a snap container, slides centered by scroll-snap-align, momentum and touch physics free from the browser. Edge peeking shows there's more to scroll — the affordance JS sliders fake with padding math.
## HTML
```html
<section class="cgl-27" aria-label="Scroll snap slider demo">
  <div class="cgl-27__rail" role="group" aria-label="Featured slides">
    <article class="cgl-27__slide" tabindex="0" style="--g:linear-gradient(130deg,oklch(0.55 0.16 330),oklch(0.3 0.1 300))"><h4>Native physics</h4><p>Momentum, rubber-band, touch — all free.</p></article>
    <article class="cgl-27__slide" tabindex="0" style="--g:linear-gradient(130deg,oklch(0.5 0.15 260),oklch(0.28 0.09 290))"><h4>snap-align: center</h4><p>The browser settles each slide mid-view.</p></article>
    <article class="cgl-27__slide" tabindex="0" style="--g:linear-gradient(130deg,oklch(0.55 0.14 200),oklch(0.3 0.08 240))"><h4>78% columns</h4><p>Neighbours peek — the honest 'more here' cue.</p></article>
    <article class="cgl-27__slide" tabindex="0" style="--g:linear-gradient(130deg,oklch(0.6 0.13 150),oklch(0.32 0.08 180))"><h4>Zero libraries</h4><p>Delete the carousel dependency.</p></article>
  </div>
</section>
```
## CSS
```css
.cgl-27,
.cgl-27 *,
.cgl-27 *::before,
.cgl-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-27 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.14 0.02 310);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.6rem 0;
}

.cgl-27 .cgl-27__rail {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 78%;
  gap: 14px;
  overflow-x: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  padding-inline: 11%;
  padding-block-end: 10px;
  scrollbar-width: thin;
  scrollbar-color: oklch(0.5 0.1 310) transparent;
}

.cgl-27 .cgl-27__slide {
  scroll-snap-align: center;
  aspect-ratio: 16/8;
  border-radius: 18px;
  background: var(--g);
  padding: 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: .4rem;
  border: 1px solid oklch(1 0 0/.14);
}

.cgl-27 h4 {
  font-size: 1.1rem;
  color: white;
}

.cgl-27 .cgl-27__slide p {
  font-size: .8rem;
  color: oklch(0.85 0.03 310);
}

.cgl-27 .cgl-27__slide:focus-visible {
  outline: 3px solid oklch(0.8 0.14 330);
  outline-offset: 3px;
}
```

## JavaScript
```js
/* No JavaScript — a column-flow grid in a snap container; the browser supplies all carousel physics. */
```
