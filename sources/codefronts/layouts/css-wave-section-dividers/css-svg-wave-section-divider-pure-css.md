---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/css-svg-wave-section-divider-pure-css/"
title: "CSS SVG wave section divider pure CSS"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "The baseline everyone actually needs: a smooth, dependency-free wave that breaks the straight line between two coloured sections."
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS SVG wave section divider pure CSS
Source: https://codefronts.com/layouts/css-wave-section-dividers/css-svg-wave-section-divider-pure-css/

The baseline everyone actually needs: a smooth, dependency-free wave that breaks the straight line between two coloured sections. One inline SVG path, one CSS rule, no plugin, no JavaScript, no layout shift — the drop-in replacement for a page-builder shape divider.
## HTML
```html
<div class="wsd-01-group">
<section class="wsd-01a">
  <div class="wsd-01a__top">
    <p class="wsd-01a__eyebrow">Pure CSS + inline SVG</p>
    <h2 class="wsd-01a__title">Break the boxy grid</h2>
    <p class="wsd-01a__copy">One path, one rule, zero dependencies.</p>
    <svg class="wsd-01a__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,64 C240,120 480,8 720,40 C960,72 1200,120 1440,72 L1440,120 L0,120 Z"></path>
    </svg>
  </div>
  <div class="wsd-01a__bottom"><p class="wsd-01a__copy">Next section starts here — the wave is this block's own edge.</p></div>
</section>
<section class="wsd-01b">
  <div class="wsd-01b__a"><h2 class="wsd-01b__title">Reusable divider utility</h2><p class="wsd-01b__copy">The wave lives in CSS, so the HTML stays clean.</p></div>
  <div class="wsd-01b__divider" role="presentation"></div>
  <div class="wsd-01b__b"><p class="wsd-01b__copy">Drop <code>.wave-divider</code> between any two blocks.</p></div>
</section>
<section class="wsd-01c">
  <div class="wsd-01c__top">
    <h2 class="wsd-01c__title">Gentle, editorial seam</h2>
    <svg class="wsd-01c__wave" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,52 C180,4 360,4 540,44 C740,88 900,88 1080,50 C1220,20 1330,20 1440,42 L1440,90 L0,90 Z"></path>
    </svg>
  </div>
  <div class="wsd-01c__bottom"><p class="wsd-01c__copy">Low-amplitude curves read as premium; tall waves read as playful.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-01-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-01-group > section {
  width: 100%;
}

.wsd-01a,
.wsd-01a *,
.wsd-01a *::before,
.wsd-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-01a {
  --ink: oklch(0.28 0.06 264);
  --next: oklch(0.97 0.01 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-01a__top {
  position: relative;
  background: var(--ink);
  color: #fff;
  padding: 72px 24px 108px;
  text-align: center;
}

.wsd-01a__eyebrow {
  font-size: 12px;
  letter-spacing: .18em;
  text-transform: uppercase;
  opacity: .62;
  margin-bottom: 14px;
}

.wsd-01a__title {
  font-size: clamp(26px,4vw,40px);
  line-height: 1.1;
  margin-bottom: 10px;
}

.wsd-01a__copy {
  font-size: 15px;
  opacity: .78;
}

.wsd-01a__wave {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(56px,9vw,110px);
  color: var(--next);
  pointer-events: none;
}

.wsd-01a__wave path {
  fill: currentColor;
}

.wsd-01a__bottom {
  background: var(--next);
  color: var(--ink);
  padding: 44px 24px 64px;
  text-align: center;
}

.wsd-01a__bottom .wsd-01a__copy {
  opacity: .72;
}

.wsd-01b,
.wsd-01b *,
.wsd-01b *::before,
.wsd-01b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-01b {
  --a: oklch(0.55 0.16 205);
  --b: oklch(0.98 0.01 205);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-01b__a {
  background: var(--a);
  color: #fff;
  padding: 64px 24px 40px;
  text-align: center;
}

.wsd-01b__title {
  font-size: clamp(24px,3.6vw,34px);
  margin-bottom: 8px;
}

.wsd-01b__copy {
  font-size: 15px;
  opacity: .82;
}

.wsd-01b__divider {
  height: clamp(48px,7vw,88px);
  background: var(--b);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 100' preserveAspectRatio='none'%3E%3Cpath d='M0,40 C300,110 640,-10 960,34 C1200,68 1320,74 1440,44 L1440,100 L0,100 Z' fill='%23000'/%3E%3C/svg%3E") no-repeat center/100% 100%;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 100' preserveAspectRatio='none'%3E%3Cpath d='M0,40 C300,110 640,-10 960,34 C1200,68 1320,74 1440,44 L1440,100 L0,100 Z' fill='%23000'/%3E%3C/svg%3E") no-repeat center/100% 100%;
  margin-top: -1px;
}

.wsd-01b__b {
  background: var(--b);
  color: oklch(0.3 0.05 205);
  padding: 28px 24px 60px;
  text-align: center;
}

.wsd-01b__b code {
  font-family: ui-monospace,monospace;
  background: oklch(0.92 0.03 205);
  padding: 2px 6px;
  border-radius: 4px;
}

.wsd-01c,
.wsd-01c *,
.wsd-01c *::before,
.wsd-01c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-01c {
  --warm: oklch(0.93 0.05 78);
  --deep: oklch(0.35 0.07 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-01c__top {
  position: relative;
  background: var(--warm);
  color: var(--deep);
  padding: 66px 24px 96px;
  text-align: center;
}

.wsd-01c__title {
  font-size: clamp(24px,3.6vw,34px);
}

.wsd-01c__wave {
  position: absolute;
  left: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(44px,6vw,80px);
  color: var(--deep);
  pointer-events: none;
}

.wsd-01c__wave path {
  fill: currentColor;
}

.wsd-01c__bottom {
  background: var(--deep);
  color: var(--warm);
  padding: 34px 24px 62px;
  text-align: center;
}

.wsd-01c__copy {
  font-size: 15px;
  opacity: .85;
}
```

## JavaScript
```js
/* No JavaScript — a single inline SVG path filled with the next section's colour, stretched with preserveAspectRatio="none". */

/* No JavaScript — the wave is an inline data-URI SVG used as a CSS mask, so the shape is a reusable utility class instead of markup. */

/* No JavaScript — two mirrored cubic curves in one path give a calm, low-amplitude seam suited to editorial layouts. */
```
