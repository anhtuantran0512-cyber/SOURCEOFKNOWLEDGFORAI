---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/pure-css-clip-path-wave-divider-without-svg/"
title: "Pure CSS clip path wave divider without SVG"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "For engineers who refuse to ship inline SVG in their markup: three CSS-only ways to cut a wave — modern clip-path: path(), a repeating radial-gradient mask,…"
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS clip path wave divider without SVG
Source: https://codefronts.com/layouts/css-wave-section-dividers/pure-css-clip-path-wave-divider-without-svg/

For engineers who refuse to ship inline SVG in their markup: three CSS-only ways to cut a wave — modern clip-path: path(), a repeating radial-gradient mask, and an ellipse curve — all with no extra DOM node and nothing for the HTML payload to carry.
## HTML
```html
<div class="wsd-06-group">
<section class="wsd-06a">
  <div class="wsd-06a__a"><h2 class="wsd-06a__title">No SVG in the DOM</h2><p class="wsd-06a__copy">The curve is one CSS declaration.</p></div>
  <div class="wsd-06a__divider" role="presentation"></div>
  <div class="wsd-06a__b"><p class="wsd-06a__copy">clip-path: path() takes SVG path syntax straight in CSS.</p></div>
</section>
<section class="wsd-06b">
  <div class="wsd-06b__a"><h2 class="wsd-06b__title">Fluid without stretching</h2><p class="wsd-06b__copy">The wave tiles instead of squashing.</p></div>
  <div class="wsd-06b__divider" role="presentation"></div>
  <div class="wsd-06b__b"><p class="wsd-06b__copy">A repeating radial-gradient mask keeps every crest the same size at any viewport.</p></div>
</section>
<section class="wsd-06c">
  <div class="wsd-06c__a"><h2 class="wsd-06c__title">One-line dome curve</h2></div>
  <div class="wsd-06c__b"><p class="wsd-06c__copy">border-radius: 50% 50% 0 0 / 100% 100% 0 0 — the cheapest curve in CSS.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-06-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-06-group > section {
  width: 100%;
}

.wsd-06a,
.wsd-06a *,
.wsd-06a *::before,
.wsd-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-06a {
  --a: oklch(0.3 0.08 150);
  --b: oklch(0.96 0.02 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-06a__a {
  background: var(--a);
  color: #fff;
  padding: 64px 24px 34px;
  text-align: center;
}

.wsd-06a__title {
  font-size: clamp(24px,3.8vw,36px);
  margin-bottom: 8px;
}

.wsd-06a__copy {
  font-size: 15px;
  opacity: .8;
}

.wsd-06a__divider {
  height: 100px;
  background: var(--b);
  clip-path: path('M0,44 C240,110 480,-6 720,38 C960,82 1200,110 1440,58 L1440,100 L0,100 Z');
  margin-top: -1px;
}

.wsd-06a__b {
  background: var(--b);
  color: oklch(0.3 0.06 150);
  padding: 14px 24px 60px;
  text-align: center;
}

.wsd-06a__b .wsd-06a__copy {
  opacity: .74;
}

.wsd-06b,
.wsd-06b *,
.wsd-06b *::before,
.wsd-06b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-06b {
  --a: oklch(0.35 0.13 268);
  --b: oklch(0.97 0.01 268);
  --pitch: 74px;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-06b__a {
  background: var(--a);
  color: #fff;
  padding: 62px 24px 32px;
  text-align: center;
}

.wsd-06b__title {
  font-size: clamp(24px,3.8vw,36px);
  margin-bottom: 8px;
}

.wsd-06b__copy {
  font-size: 15px;
  opacity: .8;
}

.wsd-06b__divider {
  height: 42px;
  background: var(--b);
  -webkit-mask: radial-gradient(calc(var(--pitch)/2) at 50% 100%,transparent 98%,#000) repeat-x 0 0/var(--pitch) 42px;
  mask: radial-gradient(calc(var(--pitch)/2) at 50% 100%,transparent 98%,#000) repeat-x 0 0/var(--pitch) 42px;
  margin-top: -1px;
}

.wsd-06b__b {
  background: var(--b);
  color: oklch(0.32 0.08 268);
  padding: 12px 24px 58px;
  text-align: center;
}

.wsd-06b__b .wsd-06b__copy {
  opacity: .74;
  max-width: 52ch;
  margin: 0 auto;
}

.wsd-06c,
.wsd-06c *,
.wsd-06c *::before,
.wsd-06c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-06c {
  --a: oklch(0.42 0.15 25);
  --b: oklch(0.97 0.02 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  overflow: hidden;
}

.wsd-06c__a {
  background: var(--a);
  color: #fff;
  padding: 62px 24px 52px;
  text-align: center;
}

.wsd-06c__title {
  font-size: clamp(24px,3.8vw,36px);
}

.wsd-06c__b {
  position: relative;
  background: var(--b);
  color: oklch(0.34 0.09 25);
  padding: 46px 24px 58px;
  text-align: center;
  border-radius: 50% 50% 0 0/72px 72px 0 0;
  margin-top: -40px;
  width: 112%;
  margin-left: -6%;
}

.wsd-06c__copy {
  font-size: 15px;
  opacity: .76;
  max-width: 52ch;
  margin: 0 auto;
}
```

## JavaScript
```js
/* No JavaScript — a fixed-height strip clipped with clip-path:path(). Note path() units are px, so this variant is intentionally fixed-height. */

/* No JavaScript — a tiled radial-gradient mask carves identical scallops; wider screens get more crests instead of wider ones. */

/* No JavaScript — an over-wide block with an elliptical border-radius pulled up over the previous section makes a dome with zero masking. */
```
