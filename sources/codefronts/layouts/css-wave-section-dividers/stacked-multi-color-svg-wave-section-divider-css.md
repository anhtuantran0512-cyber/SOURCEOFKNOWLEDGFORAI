---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/stacked-multi-color-svg-wave-section-divider-css/"
title: "Stacked multi color SVG wave section divider CSS"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "Two to three offset waves in tinted layers, so the transition between background colours reads as depth rather than a line."
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked multi color SVG wave section divider CSS
Source: https://codefronts.com/layouts/css-wave-section-dividers/stacked-multi-color-svg-wave-section-divider-css/

Two to three offset waves in tinted layers, so the transition between background colours reads as depth rather than a line. The staple move for SaaS pricing pages and agency sites that need a rich section change without an image.
## HTML
```html
<div class="wsd-04-group">
<section class="wsd-04a">
  <div class="wsd-04a__top">
    <h2 class="wsd-04a__title">Layered depth, one hue</h2>
    <div class="wsd-04a__stack" aria-hidden="true">
      <svg class="wsd-04a__layer wsd-04a__layer--1" viewBox="0 0 1440 130" preserveAspectRatio="none" focusable="false"><path d="M0,70 C260,20 520,120 780,74 C1040,28 1240,60 1440,40 L1440,130 L0,130 Z"></path></svg>
      <svg class="wsd-04a__layer wsd-04a__layer--2" viewBox="0 0 1440 130" preserveAspectRatio="none" focusable="false"><path d="M0,86 C240,44 500,126 760,88 C1020,50 1250,96 1440,66 L1440,130 L0,130 Z"></path></svg>
      <svg class="wsd-04a__layer wsd-04a__layer--3" viewBox="0 0 1440 130" preserveAspectRatio="none" focusable="false"><path d="M0,100 C220,70 480,132 740,102 C1000,72 1250,120 1440,92 L1440,130 L0,130 Z"></path></svg>
    </div>
  </div>
  <div class="wsd-04a__bottom"><p class="wsd-04a__copy">Back layers are transparent tints; only the front layer is opaque.</p></div>
</section>
<section class="wsd-04b">
  <div class="wsd-04b__top">
    <h2 class="wsd-04b__title">Two-colour ribbon seam</h2>
    <div class="wsd-04b__stack" aria-hidden="true">
      <svg class="wsd-04b__layer wsd-04b__layer--accent" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,54 C300,110 620,6 940,52 C1160,84 1300,92 1440,62 L1440,120 L0,120 Z"></path></svg>
      <svg class="wsd-04b__layer wsd-04b__layer--solid" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,74 C300,126 620,22 940,70 C1160,102 1300,110 1440,80 L1440,120 L0,120 Z"></path></svg>
    </div>
  </div>
  <div class="wsd-04b__bottom"><p class="wsd-04b__copy">An accent ribbon peeks out from under the opaque edge — brand colour, no extra markup weight.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-04-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-04-group > section {
  width: 100%;
}

.wsd-04a,
.wsd-04a *,
.wsd-04a *::before,
.wsd-04a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-04a {
  --from: oklch(0.34 0.12 285);
  --to: oklch(0.95 0.03 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-04a__top {
  position: relative;
  overflow: hidden;
  background: var(--from);
  color: #fff;
  padding: 70px 24px 128px;
  text-align: center;
}

.wsd-04a__title {
  font-size: clamp(25px,4vw,38px);
}

.wsd-04a__stack {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: clamp(70px,11vw,130px);
  pointer-events: none;
}

.wsd-04a__layer {
  position: absolute;
  left: 0;
  bottom: 0;
  display: block;
  width: 100%;
  height: 100%;
}

.wsd-04a__layer--1 path {
  fill: color-mix(in oklab,var(--to) 30%,transparent);
}

.wsd-04a__layer--2 path {
  fill: color-mix(in oklab,var(--to) 62%,transparent);
}

.wsd-04a__layer--3 path {
  fill: var(--to);
}

.wsd-04a__bottom {
  background: var(--to);
  color: oklch(0.32 0.08 285);
  padding: 32px 24px 62px;
  text-align: center;
}

.wsd-04a__copy {
  font-size: 15px;
  opacity: .75;
}

.wsd-04b,
.wsd-04b *,
.wsd-04b *::before,
.wsd-04b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-04b {
  --from: oklch(0.24 0.04 200);
  --to: oklch(0.97 0.01 200);
  --accent: oklch(0.75 0.17 88);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-04b__top {
  position: relative;
  overflow: hidden;
  background: var(--from);
  color: #fff;
  padding: 68px 24px 116px;
  text-align: center;
}

.wsd-04b__title {
  font-size: clamp(25px,4vw,38px);
}

.wsd-04b__stack {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: clamp(64px,10vw,120px);
  pointer-events: none;
}

.wsd-04b__layer {
  position: absolute;
  left: 0;
  bottom: 0;
  display: block;
  width: 100%;
  height: 100%;
}

.wsd-04b__layer--accent path {
  fill: var(--accent);
}

.wsd-04b__layer--solid path {
  fill: var(--to);
}

.wsd-04b__bottom {
  background: var(--to);
  color: oklch(0.28 0.04 200);
  padding: 30px 24px 60px;
  text-align: center;
}

.wsd-04b__copy {
  font-size: 15px;
  opacity: .75;
  max-width: 52ch;
  margin: 0 auto;
}
```

## JavaScript
```js
/* No JavaScript — three absolutely positioned SVG layers filled with color-mix() steps of one destination hue; only the last is opaque. */

/* No JavaScript — an accent-filled wave sits 20px above an identical opaque wave, so only a sliver of brand colour shows. */
```
