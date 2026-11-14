---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/inverted-curve-svg-wave-divider-css/"
title: "Inverted curve SVG wave divider CSS"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "Concave dips that pull the eye downward into a CTA."
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inverted curve SVG wave divider CSS
Source: https://codefronts.com/layouts/css-wave-section-dividers/inverted-curve-svg-wave-divider-css/

Concave dips that pull the eye downward into a CTA. Instead of the wave bulging outward, the edge scoops inward — a shape that visually funnels attention toward whatever sits at the pinch point, which is why conversion-focused pages use it around signup banners.
## HTML
```html
<div class="wsd-07-group">
<section class="wsd-07a">
  <div class="wsd-07a__above"><p class="wsd-07a__copy">Features, proof, screenshots…</p></div>
  <div class="wsd-07a__band">
    <svg class="wsd-07a__wave wsd-07a__wave--top" viewBox="0 0 1440 110" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0,0 C360,0 420,110 720,110 C1020,110 1080,0 1440,0 L1440,0 L0,0 Z"></path></svg>
    <h2 class="wsd-07a__title">Start your free trial</h2>
    <p class="wsd-07a__copy">The curve funnels the eye to the centre — put the button there.</p>
    <a class="wsd-07a__cta" href="#0">Create account</a>
  </div>
  <div class="wsd-07a__below"><p class="wsd-07a__copy">…and the page continues.</p></div>
</section>
<section class="wsd-07b">
  <div class="wsd-07b__above"><p class="wsd-07b__copy">Section above</p></div>
  <div class="wsd-07b__band">
    <svg class="wsd-07b__wave wsd-07b__wave--top" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0,0 C420,0 480,90 720,90 C960,90 1020,0 1440,0 Z"></path></svg>
    <h2 class="wsd-07b__title">A lens for one idea</h2>
    <p class="wsd-07b__copy">Curved on both edges, the band floats away from the grid.</p>
    <svg class="wsd-07b__wave wsd-07b__wave--bottom" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0,90 C420,90 480,0 720,0 C960,0 1020,90 1440,90 Z"></path></svg>
  </div>
  <div class="wsd-07b__below"><p class="wsd-07b__copy">Section below</p></div>
</section>
</div>
```
## CSS
```css
.wsd-07-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-07-group > section {
  width: 100%;
}

.wsd-07a,
.wsd-07a *,
.wsd-07a *::before,
.wsd-07a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-07a {
  --page: oklch(0.96 0.01 240);
  --band: oklch(0.28 0.1 262);
  --accent: oklch(0.8 0.16 92);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-07a__above,
.wsd-07a__below {
  background: var(--page);
  color: oklch(0.36 0.03 240);
  padding: 46px 24px;
  text-align: center;
}

.wsd-07a__copy {
  font-size: 15px;
  opacity: .75;
}

.wsd-07a__band {
  position: relative;
  overflow: hidden;
  background: var(--band);
  color: #fff;
  padding: clamp(88px,12vw,140px) 24px 60px;
  text-align: center;
}

.wsd-07a__wave {
  position: absolute;
  left: 0;
  display: block;
  width: 100%;
  height: clamp(56px,8vw,104px);
  color: var(--page);
  pointer-events: none;
}

.wsd-07a__wave--top {
  top: -1px;
}

.wsd-07a__wave path {
  fill: currentColor;
}

.wsd-07a__title {
  font-size: clamp(25px,4vw,40px);
  margin-bottom: 10px;
}

.wsd-07a__band .wsd-07a__copy {
  opacity: .8;
  max-width: 44ch;
  margin: 0 auto;
}

.wsd-07a__cta {
  display: inline-block;
  margin-top: 20px;
  font-size: 14.5px;
  font-weight: 800;
  color: oklch(0.24 0.08 262);
  background: var(--accent);
  padding: 13px 28px;
  border-radius: 9999px;
  text-decoration: none;
  transition: transform .2s;
}

.wsd-07a__cta:hover {
  transform: translateY(-2px);
}

.wsd-07a__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.wsd-07b,
.wsd-07b *,
.wsd-07b *::before,
.wsd-07b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-07b {
  --page: oklch(0.95 0.02 100);
  --band: oklch(0.33 0.09 178);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-07b__above,
.wsd-07b__below {
  background: var(--page);
  color: oklch(0.36 0.04 120);
  padding: 42px 24px;
  text-align: center;
}

.wsd-07b__copy {
  font-size: 15px;
  opacity: .75;
}

.wsd-07b__band {
  position: relative;
  overflow: hidden;
  background: var(--band);
  color: #fff;
  padding: clamp(80px,11vw,120px) 24px clamp(80px,11vw,120px);
  text-align: center;
}

.wsd-07b__wave {
  position: absolute;
  left: 0;
  display: block;
  width: 100%;
  height: clamp(48px,7vw,86px);
  color: var(--page);
  pointer-events: none;
}

.wsd-07b__wave--top {
  top: -1px;
}

.wsd-07b__wave--bottom {
  bottom: -1px;
}

.wsd-07b__wave path {
  fill: currentColor;
}

.wsd-07b__title {
  font-size: clamp(24px,3.8vw,36px);
  margin-bottom: 8px;
}

.wsd-07b__band .wsd-07b__copy {
  opacity: .82;
  max-width: 44ch;
  margin: 0 auto;
}
```

## JavaScript
```js
/* No JavaScript — a page-coloured concave path on the band's top edge scoops inward, funnelling attention to the centred CTA. */

/* No JavaScript — mirrored concave paths on both edges pinch the band into a lens shape. */
```
