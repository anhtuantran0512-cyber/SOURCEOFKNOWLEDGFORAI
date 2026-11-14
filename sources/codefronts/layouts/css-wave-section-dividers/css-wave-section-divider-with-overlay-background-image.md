---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/css-wave-section-divider-with-overlay-background-image/"
title: "CSS wave section divider with overlay background image"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "A crisp wave sitting over a full-bleed photo or video hero, with the contrast scrim, focal-point cropping and text legibility handled properly — the…"
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS wave section divider with overlay background image
Source: https://codefronts.com/layouts/css-wave-section-dividers/css-wave-section-divider-with-overlay-background-image/

A crisp wave sitting over a full-bleed photo or video hero, with the contrast scrim, focal-point cropping and text legibility handled properly — the combination that usually goes wrong when a divider is dropped on top of imagery.
## HTML
```html
<div class="wsd-13-group">
<section class="wsd-13a">
  <header class="wsd-13a__hero">
    <img class="wsd-13a__img" src="https://picsum.photos/seed/wsd13a/1600/900" width="1600" height="900" alt="" fetchpriority="high" decoding="async">
    <div class="wsd-13a__inner">
      <p class="wsd-13a__eyebrow">Full-bleed imagery</p>
      <h2 class="wsd-13a__title">Legible over any photo</h2>
      <p class="wsd-13a__copy">Gradient scrim below, wave on top, text in the safe zone.</p>
    </div>
    <svg class="wsd-13a__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,62 C280,118 560,10 840,54 C1080,92 1250,106 1440,74 L1440,120 L0,120 Z"></path>
    </svg>
  </header>
  <div class="wsd-13a__next"><p class="wsd-13a__copy">Wave fill matches this section exactly — no sticker effect.</p></div>
</section>
<section class="wsd-13b">
  <div class="wsd-13b__above"><p class="wsd-13b__copy">Text section</p></div>
  <div class="wsd-13b__band" role="img" aria-label="Coastline photograph shown inside a wave-shaped band"></div>
  <div class="wsd-13b__below"><p class="wsd-13b__copy">The photo itself is masked into a wave band — both edges curved.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-13-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-13-group > section {
  width: 100%;
}

.wsd-13a,
.wsd-13a *,
.wsd-13a *::before,
.wsd-13a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-13a {
  --next: oklch(0.97 0.01 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-13a__hero {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  color: #fff;
  padding: 82px 24px clamp(96px,13vw,150px);
  text-align: center;
}

.wsd-13a__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 35%;
  z-index: -2;
}

.wsd-13a__hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,oklch(0.15 0.03 260/.28),oklch(0.13 0.03 260/.8));
  z-index: -1;
}

.wsd-13a__inner {
  position: relative;
  max-width: 46ch;
  margin: 0 auto;
}

.wsd-13a__eyebrow {
  font-size: 12px;
  letter-spacing: .2em;
  text-transform: uppercase;
  opacity: .78;
  margin-bottom: 12px;
}

.wsd-13a__title {
  font-size: clamp(27px,4.6vw,46px);
  line-height: 1.06;
  margin-bottom: 10px;
  text-shadow: 0 2px 18px oklch(0.15 0.03 260/.55);
}

.wsd-13a__copy {
  font-size: 15px;
  opacity: .88;
}

.wsd-13a__wave {
  position: absolute;
  left: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(56px,9vw,116px);
  color: var(--next);
  pointer-events: none;
  z-index: 1;
}

.wsd-13a__wave path {
  fill: currentColor;
}

.wsd-13a__next {
  background: var(--next);
  color: oklch(0.3 0.03 250);
  padding: 22px 24px 58px;
  text-align: center;
}

.wsd-13a__next .wsd-13a__copy {
  opacity: .72;
}

.wsd-13b,
.wsd-13b *,
.wsd-13b *::before,
.wsd-13b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-13b {
  --paper: oklch(0.96 0.01 230);
  --mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 400' preserveAspectRatio='none'%3E%3Cpath d='M0,70 C360,-10 700,120 1000,70 C1180,40 1300,40 1440,66 L1440,330 C1200,410 900,270 620,326 C420,366 180,366 0,334 Z' fill='%23000'/%3E%3C/svg%3E");
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-13b__above,
.wsd-13b__below {
  background: var(--paper);
  color: oklch(0.32 0.03 230);
  padding: 40px 24px;
  text-align: center;
}

.wsd-13b__copy {
  font-size: 15px;
  opacity: .74;
  max-width: 52ch;
  margin: 0 auto;
}

.wsd-13b__band {
  height: clamp(220px,32vw,380px);
  background: url('https://picsum.photos/seed/wsd13b/1600/700') center/cover no-repeat,oklch(0.4 0.08 230);
  -webkit-mask: var(--mask) no-repeat center/100% 100%;
  mask: var(--mask) no-repeat center/100% 100%;
  margin: -24px 0;
}

@media (max-width: 640px) {
  .wsd-13b__band {
    margin: -12px 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — image, gradient scrim and wave are three stacked layers inside one isolated stacking context. */

/* No JavaScript — a single data-URI mask with a wave on both the top and bottom edge cuts the photo into a ribbon. */
```
