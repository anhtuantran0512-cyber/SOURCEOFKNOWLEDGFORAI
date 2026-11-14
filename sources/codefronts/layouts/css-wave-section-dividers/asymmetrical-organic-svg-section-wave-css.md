---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/asymmetrical-organic-svg-section-wave-css/"
title: "Asymmetrical organic SVG section wave CSS"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "Non-repeating, hand-drawn-feeling curves for editorial and brand-showcase sites."
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Asymmetrical organic SVG section wave CSS
Source: https://codefronts.com/layouts/css-wave-section-dividers/asymmetrical-organic-svg-section-wave-css/

Non-repeating, hand-drawn-feeling curves for editorial and brand-showcase sites. Symmetry reads as template; asymmetry reads as art direction — these paths deliberately break the mirror so each section edge looks authored rather than generated.
## HTML
```html
<div class="wsd-10-group">
<section class="wsd-10a">
  <div class="wsd-10a__top">
    <p class="wsd-10a__num">01 / Studio</p>
    <h2 class="wsd-10a__title">Curves with<br>a point of view</h2>
    <svg class="wsd-10a__wave" viewBox="0 0 1440 130" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,96 C280,-8 520,104 760,78 C920,60 1120,86 1440,22 L1440,130 L0,130 Z"></path>
    </svg>
  </div>
  <div class="wsd-10a__bottom"><p class="wsd-10a__copy">One dominant crest on the left, a long quiet run-out to the right.</p></div>
</section>
<section class="wsd-10b">
  <div class="wsd-10b__top">
    <h2 class="wsd-10b__title">A fragment of something bigger</h2>
    <svg class="wsd-10b__blob" viewBox="0 0 1200 220" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M-40,150 C120,60 280,206 470,168 C640,134 700,44 880,62 C1030,77 1090,150 1240,120 L1240,240 L-40,240 Z"></path>
    </svg>
  </div>
  <div class="wsd-10b__bottom"><p class="wsd-10b__copy">The path overflows on both sides, so the curve never looks boxed by the viewport.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-10-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-10-group > section {
  width: 100%;
}

.wsd-10a,
.wsd-10a *,
.wsd-10a *::before,
.wsd-10a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-10a {
  --ink: oklch(0.2 0.02 60);
  --cream: oklch(0.94 0.04 82);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-10a__top {
  position: relative;
  overflow: hidden;
  background: var(--ink);
  color: var(--cream);
  padding: 70px 8% 130px;
  text-align: left;
}

.wsd-10a__num {
  font-family: ui-monospace,monospace;
  font-size: 12px;
  letter-spacing: .16em;
  opacity: .6;
  margin-bottom: 14px;
}

.wsd-10a__title {
  font-size: clamp(28px,5.4vw,54px);
  line-height: 1.02;
  letter-spacing: -.02em;
  max-width: 16ch;
}

.wsd-10a__wave {
  position: absolute;
  left: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(66px,10vw,130px);
  color: var(--cream);
  pointer-events: none;
}

.wsd-10a__wave path {
  fill: currentColor;
}

.wsd-10a__bottom {
  background: var(--cream);
  color: var(--ink);
  padding: 14px 8% 58px;
}

.wsd-10a__copy {
  font-size: 15px;
  opacity: .72;
  max-width: 52ch;
}

.wsd-10b,
.wsd-10b *,
.wsd-10b *::before,
.wsd-10b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-10b {
  --deep: oklch(0.32 0.11 195);
  --sand: oklch(0.95 0.04 96);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-10b__top {
  position: relative;
  overflow: hidden;
  background: var(--deep);
  color: #fff;
  padding: 72px 24px 140px;
  text-align: center;
}

.wsd-10b__title {
  font-size: clamp(25px,4.2vw,40px);
  line-height: 1.06;
  max-width: 22ch;
  margin: 0 auto;
}

.wsd-10b__blob {
  position: absolute;
  left: -4%;
  bottom: -1px;
  display: block;
  width: 108%;
  height: clamp(90px,14vw,180px);
  color: var(--sand);
  pointer-events: none;
}

.wsd-10b__blob path {
  fill: currentColor;
}

.wsd-10b__bottom {
  background: var(--sand);
  color: oklch(0.3 0.06 190);
  padding: 12px 24px 58px;
  text-align: center;
}

.wsd-10b__copy {
  font-size: 15px;
  opacity: .74;
  max-width: 52ch;
  margin: 0 auto;
}
```

## JavaScript
```js
/* No JavaScript — deliberately unequal control points give one dominant crest and a long quiet run-out. */

/* No JavaScript — the path is authored wider than its box and positioned to overflow both edges, so the shape reads as a fragment. */
```
