---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/animated-css-wave-section-divider-for-landing-page/"
title: "Animated CSS wave section divider for landing page"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "Continuous liquid motion for SaaS and agency hero sections: two identical wave tiles slide sideways forever so the crest never appears to end, creating a…"
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated CSS wave section divider for landing page
Source: https://codefronts.com/layouts/css-wave-section-dividers/animated-css-wave-section-divider-for-landing-page/

Continuous liquid motion for SaaS and agency hero sections: two identical wave tiles slide sideways forever so the crest never appears to end, creating a calm ocean-drift that keeps a landing page alive without a canvas, a library or a single frame of JavaScript.
## HTML
```html
<div class="wsd-02-group">
<section class="wsd-02a">
  <div class="wsd-02a__hero">
    <p class="wsd-02a__eyebrow">Landing page hero</p>
    <h2 class="wsd-02a__title">Ship faster with fluid sections</h2>
    <div class="wsd-02a__waves" aria-hidden="true">
      <div class="wsd-02a__track">
        <svg viewBox="0 0 1440 110" preserveAspectRatio="none" focusable="false"><path d="M0,60 C180,100 360,20 720,60 C1080,100 1260,20 1440,60 L1440,110 L0,110 Z"></path></svg>
        <svg viewBox="0 0 1440 110" preserveAspectRatio="none" focusable="false"><path d="M0,60 C180,100 360,20 720,60 C1080,100 1260,20 1440,60 L1440,110 L0,110 Z"></path></svg>
      </div>
    </div>
  </div>
  <div class="wsd-02a__next"><p class="wsd-02a__copy">Transform-only loop — 0 layout, 0 paint, 0 CLS.</p></div>
</section>
<section class="wsd-02b">
  <div class="wsd-02b__hero">
    <h2 class="wsd-02b__title">Layered liquid depth</h2>
    <div class="wsd-02b__waves" aria-hidden="true">
      <div class="wsd-02b__track wsd-02b__track--back">
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C240,110 480,30 720,70 C960,110 1200,30 1440,70 L1440,120 L0,120 Z"></path></svg>
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C240,110 480,30 720,70 C960,110 1200,30 1440,70 L1440,120 L0,120 Z"></path></svg>
      </div>
      <div class="wsd-02b__track wsd-02b__track--mid">
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,84 C200,44 420,120 720,84 C1020,48 1240,120 1440,84 L1440,120 L0,120 Z"></path></svg>
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,84 C200,44 420,120 720,84 C1020,48 1240,120 1440,84 L1440,120 L0,120 Z"></path></svg>
      </div>
      <div class="wsd-02b__track wsd-02b__track--front">
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,96 C260,120 460,64 720,96 C980,124 1180,64 1440,96 L1440,120 L0,120 Z"></path></svg>
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,96 C260,120 460,64 720,96 C980,124 1180,64 1440,96 L1440,120 L0,120 Z"></path></svg>
      </div>
    </div>
  </div>
  <div class="wsd-02b__next"><p class="wsd-02b__copy">Different speeds per layer = parallax without scroll listeners.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-02-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-02-group > section {
  width: 100%;
}

.wsd-02a,
.wsd-02a *,
.wsd-02a *::before,
.wsd-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-02a {
  --deep: oklch(0.32 0.11 255);
  --pale: oklch(0.96 0.02 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-02a__hero {
  position: relative;
  overflow: hidden;
  background: linear-gradient(160deg,oklch(0.38 0.13 262),var(--deep));
  color: #fff;
  padding: 74px 24px 116px;
  text-align: center;
}

.wsd-02a__eyebrow {
  font-size: 12px;
  letter-spacing: .2em;
  text-transform: uppercase;
  opacity: .6;
  margin-bottom: 12px;
}

.wsd-02a__title {
  font-size: clamp(26px,4.2vw,42px);
  line-height: 1.1;
}

.wsd-02a__waves {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: clamp(60px,9vw,110px);
  pointer-events: none;
}

.wsd-02a__track {
  display: flex;
  width: 200%;
  height: 100%;
  animation: wsd-02a-drift 14s linear infinite;
}

.wsd-02a__track svg {
  display: block;
  width: 50%;
  height: 100%;
}

.wsd-02a__track path {
  fill: var(--pale);
}

.wsd-02a__next {
  background: var(--pale);
  color: var(--deep);
  padding: 36px 24px 62px;
  text-align: center;
}

.wsd-02a__copy {
  font-size: 15px;
  opacity: .75;
}

@keyframes wsd-02a-drift {
  from {
    transform: translate3d(0,0,0);
  }

  to {
    transform: translate3d(-50%,0,0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .wsd-02a__track {
    animation: none;
  }
}

.wsd-02b,
.wsd-02b *,
.wsd-02b *::before,
.wsd-02b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-02b {
  --sea: oklch(0.52 0.14 215);
  --foam: oklch(0.97 0.02 215);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-02b__hero {
  position: relative;
  overflow: hidden;
  background: linear-gradient(180deg,oklch(0.42 0.13 235),var(--sea));
  color: #fff;
  padding: 72px 24px 124px;
  text-align: center;
}

.wsd-02b__title {
  font-size: clamp(25px,4vw,38px);
}

.wsd-02b__waves {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: clamp(66px,10vw,120px);
  pointer-events: none;
}

.wsd-02b__track {
  position: absolute;
  inset: 0;
  display: flex;
  width: 200%;
}

.wsd-02b__track svg {
  display: block;
  width: 50%;
  height: 100%;
}

.wsd-02b__track--back {
  animation: wsd-02b-drift 22s linear infinite;
}

.wsd-02b__track--back path {
  fill: color-mix(in oklab,var(--foam) 32%,transparent);
}

.wsd-02b__track--mid {
  animation: wsd-02b-drift 15s linear infinite reverse;
}

.wsd-02b__track--mid path {
  fill: color-mix(in oklab,var(--foam) 58%,transparent);
}

.wsd-02b__track--front {
  animation: wsd-02b-drift 9s linear infinite;
}

.wsd-02b__track--front path {
  fill: var(--foam);
}

.wsd-02b__next {
  background: var(--foam);
  color: oklch(0.32 0.08 225);
  padding: 34px 24px 60px;
  text-align: center;
}

.wsd-02b__copy {
  font-size: 15px;
  opacity: .78;
}

@keyframes wsd-02b-drift {
  from {
    transform: translate3d(0,0,0);
  }

  to {
    transform: translate3d(-50%,0,0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .wsd-02b__track {
    animation: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — two seamless SVG copies inside a 200%-wide track translated -50% on an infinite linear keyframe. */

/* No JavaScript — three stacked seamless tracks drift at different durations (one reversed) to fake depth with zero scroll listeners. */
```
