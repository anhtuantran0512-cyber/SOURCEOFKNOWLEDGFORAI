---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/responsive-css-svg-wave-divider-bottom-of-hero-section/"
title: "Responsive CSS SVG wave divider bottom of hero section"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "A dark-mode hero whose wave sits perfectly on its bottom edge and scales fluidly from a 320px phone to a 2560px display — with the wave height driven by…"
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive CSS SVG wave divider bottom of hero section
Source: https://codefronts.com/layouts/css-wave-section-dividers/responsive-css-svg-wave-divider-bottom-of-hero-section/

A dark-mode hero whose wave sits perfectly on its bottom edge and scales fluidly from a 320px phone to a 2560px display — with the wave height driven by clamp() so the curve never flattens into a smear on desktop or eat half the screen on mobile.
## HTML
```html
<div class="wsd-03-group">
<section class="wsd-03a">
  <header class="wsd-03a__hero">
    <p class="wsd-03a__eyebrow">Responsive hero</p>
    <h2 class="wsd-03a__title">Scales from 320px to 4K</h2>
    <p class="wsd-03a__copy">Wave height is clamped, so the curve keeps its shape at every width.</p>
    <a class="wsd-03a__cta" href="#0">Read the guide</a>
    <svg class="wsd-03a__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,48 C220,112 420,8 720,48 C1020,88 1240,112 1440,64 L1440,120 L0,120 Z"></path>
    </svg>
  </header>
  <div class="wsd-03a__body"><p class="wsd-03a__copy">Content section — never overlapped, because the hero reserves padding.</p></div>
</section>
<section class="wsd-03b">
  <header class="wsd-03b__hero">
    <h2 class="wsd-03b__title">Ratio-locked curve</h2>
    <p class="wsd-03b__copy">aspect-ratio keeps the wave mathematically identical at every width.</p>
    <svg class="wsd-03b__wave" viewBox="0 0 1440 160" aria-hidden="true" focusable="false">
      <path d="M0,80 C300,160 560,0 880,64 C1120,112 1280,132 1440,96 L1440,160 L0,160 Z"></path>
    </svg>
  </header>
  <div class="wsd-03b__body"><p class="wsd-03b__copy">No preserveAspectRatio override needed — the box matches the viewBox ratio.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-03-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-03-group > section {
  width: 100%;
}

.wsd-03a,
.wsd-03a *,
.wsd-03a *::before,
.wsd-03a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-03a {
  --night: oklch(0.19 0.03 265);
  --paper: oklch(0.96 0.01 265);
  --accent: oklch(0.72 0.16 168);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-03a__hero {
  position: relative;
  overflow: hidden;
  background: radial-gradient(120% 130% at 20% 0%,oklch(0.28 0.07 272),var(--night));
  color: #fff;
  padding: 76px 24px clamp(104px,15vw,180px);
  text-align: center;
}

.wsd-03a__eyebrow {
  font-size: 12px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 12px;
}

.wsd-03a__title {
  font-size: clamp(26px,4.4vw,44px);
  line-height: 1.08;
  margin-bottom: 10px;
}

.wsd-03a__copy {
  font-size: 15px;
  opacity: .76;
  max-width: 46ch;
  margin: 0 auto;
}

.wsd-03a__cta {
  display: inline-block;
  margin-top: 20px;
  font-size: 14px;
  font-weight: 700;
  color: var(--night);
  background: var(--accent);
  padding: 12px 26px;
  border-radius: 9999px;
  text-decoration: none;
  transition: transform .2s;
}

.wsd-03a__cta:hover {
  transform: translateY(-2px);
}

.wsd-03a__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.wsd-03a__wave {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(52px,8vw,120px);
  color: var(--paper);
  pointer-events: none;
}

.wsd-03a__wave path {
  fill: currentColor;
}

.wsd-03a__body {
  background: var(--paper);
  color: oklch(0.3 0.03 265);
  padding: 32px 24px 62px;
  text-align: center;
}

.wsd-03a__body .wsd-03a__copy {
  opacity: .72;
}

.wsd-03b,
.wsd-03b *,
.wsd-03b *::before,
.wsd-03b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-03b {
  --plum: oklch(0.3 0.09 320);
  --mist: oklch(0.95 0.02 320);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-03b__hero {
  position: relative;
  background: linear-gradient(150deg,oklch(0.36 0.12 328),var(--plum));
  color: #fff;
  padding: 70px 24px 0;
  text-align: center;
}

.wsd-03b__title {
  font-size: clamp(25px,4vw,38px);
  margin-bottom: 10px;
}

.wsd-03b__copy {
  font-size: 15px;
  opacity: .78;
  max-width: 48ch;
  margin: 0 auto;
}

.wsd-03b__wave {
  display: block;
  width: 100%;
  aspect-ratio: 1440/160;
  height: auto;
  margin-bottom: -1px;
  color: var(--mist);
}

.wsd-03b__wave path {
  fill: currentColor;
}

.wsd-03b__body {
  background: var(--mist);
  color: oklch(0.32 0.06 320);
  padding: 30px 24px 60px;
  text-align: center;
}

.wsd-03b__body .wsd-03b__copy {
  opacity: .72;
}
```

## JavaScript
```js
/* No JavaScript — clamp()ed wave height plus bottom:-1px overlap keeps the seam pixel-clean at any DPR. */

/* No JavaScript — the SVG is in normal flow with aspect-ratio matching its viewBox, so it reserves its own space and cannot overlap content. */
```
