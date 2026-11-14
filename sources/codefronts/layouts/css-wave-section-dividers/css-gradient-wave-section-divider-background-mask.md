---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/css-gradient-wave-section-divider-background-mask/"
title: "CSS gradient wave section divider background mask"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "A mesh-gradient section whose edge is cut into a wave by a mask, so the gradient itself is the divider."
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS gradient wave section divider background mask
Source: https://codefronts.com/layouts/css-wave-section-dividers/css-gradient-wave-section-divider-background-mask/

A mesh-gradient section whose edge is cut into a wave by a mask, so the gradient itself is the divider. This is the 2027 look: no flat fills, no visible seam, just a coloured field that ends in a curve — and it works with animated gradients too.
## HTML
```html
<div class="wsd-09-group">
<section class="wsd-09a">
  <div class="wsd-09a__mesh">
    <p class="wsd-09a__eyebrow">Gradient mask</p>
    <h2 class="wsd-09a__title">The gradient is the divider</h2>
    <p class="wsd-09a__copy">One mask-image, any background underneath.</p>
  </div>
  <div class="wsd-09a__next"><p class="wsd-09a__copy">Section below stays a plain block — no wave markup needed.</p></div>
</section>
<section class="wsd-09b">
  <div class="wsd-09b__top">
    <h2 class="wsd-09b__title">Gradient inside the path</h2>
    <svg class="wsd-09b__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <defs>
        <linearGradient id="wsd-09b-grad" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="oklch(0.7 0.19 30)"></stop>
          <stop offset="0.5" stop-color="oklch(0.72 0.17 340)"></stop>
          <stop offset="1" stop-color="oklch(0.68 0.17 285)"></stop>
        </linearGradient>
      </defs>
      <path d="M0,58 C280,116 560,8 840,52 C1080,90 1250,104 1440,74 L1440,120 L0,120 Z" fill="url(#wsd-09b-grad)"></path>
    </svg>
  </div>
  <div class="wsd-09b__bottom"><p class="wsd-09b__copy">A gradient-filled path is safer over unpredictable content than masking a whole block.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-09-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-09-group > section {
  width: 100%;
}

.wsd-09a,
.wsd-09a *,
.wsd-09a *::before,
.wsd-09a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-09a {
  --wave: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 400' preserveAspectRatio='none'%3E%3Cpath d='M0,0 L1440,0 L1440,340 C1180,392 900,292 660,336 C420,380 200,392 0,356 Z' fill='%23000'/%3E%3C/svg%3E");
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-09a__mesh {
  background: radial-gradient(70% 80% at 12% 18%,oklch(0.62 0.22 300),transparent 70%),radial-gradient(60% 70% at 88% 26%,oklch(0.72 0.17 200),transparent 68%),radial-gradient(80% 90% at 50% 100%,oklch(0.55 0.2 340),transparent 72%),oklch(0.16 0.04 280);
  color: #fff;
  padding: 76px 24px clamp(96px,13vw,150px);
  text-align: center;
  -webkit-mask: var(--wave) no-repeat center/100% 100%;
  mask: var(--wave) no-repeat center/100% 100%;
}

.wsd-09a__eyebrow {
  font-size: 12px;
  letter-spacing: .2em;
  text-transform: uppercase;
  opacity: .66;
  margin-bottom: 12px;
}

.wsd-09a__title {
  font-size: clamp(26px,4.2vw,42px);
  line-height: 1.1;
  margin-bottom: 10px;
}

.wsd-09a__copy {
  font-size: 15px;
  opacity: .82;
}

.wsd-09a__next {
  background: oklch(0.97 0.01 280);
  color: oklch(0.3 0.05 280);
  padding: 24px 24px 58px;
  text-align: center;
  margin-top: -2px;
}

.wsd-09a__next .wsd-09a__copy {
  opacity: .72;
}

.wsd-09b,
.wsd-09b *,
.wsd-09b *::before,
.wsd-09b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-09b {
  --dark: oklch(0.18 0.03 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-09b__top {
  position: relative;
  background: var(--dark);
  color: #fff;
  padding: 68px 24px 116px;
  text-align: center;
}

.wsd-09b__title {
  font-size: clamp(24px,3.8vw,36px);
}

.wsd-09b__wave {
  position: absolute;
  left: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(58px,9vw,120px);
  pointer-events: none;
}

.wsd-09b__bottom {
  background: linear-gradient(90deg,oklch(0.7 0.19 30),oklch(0.72 0.17 340),oklch(0.68 0.17 285));
  color: oklch(0.2 0.04 320);
  padding: 26px 24px 56px;
  text-align: center;
}

.wsd-09b__copy {
  font-size: 15px;
  font-weight: 600;
  max-width: 52ch;
  margin: 0 auto;
}
```

## JavaScript
```js
/* No JavaScript — the whole mesh-gradient section is clipped by an SVG data-URI mask, so the gradient's own edge becomes the wave. */

/* No JavaScript — a <linearGradient> in <defs> fills the path, matched to the next section's CSS gradient so the seam is invisible. */
```
