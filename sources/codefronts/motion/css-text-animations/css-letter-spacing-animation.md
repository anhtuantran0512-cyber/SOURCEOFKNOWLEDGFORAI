---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-letter-spacing-animation/"
title: "CSS Split Text Reveal Animation Overflow Hidden"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "The agency-site classic: multi-line headlines where each line climbs out of an invisible overflow:hidden mask — shown as a warm editorial three-liner and a…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Split Text Reveal Animation Overflow Hidden
Source: https://codefronts.com/motion/css-text-animations/css-letter-spacing-animation/

The agency-site classic: multi-line headlines where each line climbs out of an invisible overflow:hidden mask — shown as a warm editorial three-liner and a brutalist skew-rise where lines shear upright as they land.
## HTML
```html
<div class="cat-10-group">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="cat-10a" aria-label="Editorial line mask reveal">
  <h1 class="cat-10a__title">
    <span class="cat-10a__mask"><span class="cat-10a__line" style="--i:0">We craft</span></span>
    <span class="cat-10a__mask"><span class="cat-10a__line" style="--i:1">interfaces that</span></span>
    <span class="cat-10a__mask"><span class="cat-10a__line cat-10a__line--em" style="--i:2">feel inevitable.</span></span>
  </h1>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-10b" aria-label="Skewed line mask reveal">
  <h1 class="cat-10b__title">
    <span class="cat-10b__mask"><span class="cat-10b__line" style="--i:0">BOLD</span></span>
    <span class="cat-10b__mask"><span class="cat-10b__line cat-10b__line--ghost" style="--i:1">MOVES</span></span>
    <span class="cat-10b__mask"><span class="cat-10b__line cat-10b__line--acid" style="--i:2">ONLY.</span></span>
  </h1>
</section>
</div>
```
## CSS
```css
.cat-10-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-10-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-10a,
.cat-10a *,
.cat-10a *::before,
.cat-10a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-10a {
  --ink: #26201a;
  --accent: oklch(0.6 0.13 60);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f7f2e9,#efe6d6);
  font-family: 'Playfair Display',Georgia,serif;
}

.cat-10a__title {
  font-size: clamp(36px,6vw,76px);
  font-weight: 600;
  line-height: 1.12;
  color: var(--ink);
  letter-spacing: -.015em;
}

.cat-10a__mask {
  display: block;
  overflow: hidden;
  padding-bottom: .1em;
  margin-bottom: -.1em;
}

.cat-10a__line {
  display: block;
  transform: translateY(112%);
  animation: cat-10a-rise .85s cubic-bezier(.16,.84,.3,1) calc(var(--i)*140ms + .25s) both;
}

.cat-10a__line--em {
  font-style: italic;
  color: var(--accent);
}

@keyframes cat-10a-rise {
  to {
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-10a__line {
    animation: none;
    transform: none;
  }
}

.cat-10b,
.cat-10b *,
.cat-10b *::before,
.cat-10b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-10b {
  --acid: oklch(0.9 0.21 125);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101010;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.cat-10b__title {
  font-size: clamp(52px,9.4vw,128px);
  font-weight: 900;
  line-height: .96;
  letter-spacing: -.03em;
  color: #f4f4f0;
  text-transform: uppercase;
}

.cat-10b__mask {
  display: block;
  overflow: hidden;
  padding-bottom: .06em;
  margin-bottom: -.06em;
}

.cat-10b__line {
  display: block;
  transform-origin: left bottom;
  transform: translateY(115%) skewY(7deg);
  animation: cat-10b-rise .8s cubic-bezier(.2,.85,.25,1) calc(var(--i)*120ms + .2s) both;
}

.cat-10b__line--ghost {
  color: transparent;
  -webkit-text-stroke: 2px #f4f4f0;
}

.cat-10b__line--acid {
  color: var(--acid);
}

@keyframes cat-10b-rise {
  to {
    transform: translateY(0) skewY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-10b__line {
    animation: none;
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each line lives in its own overflow:hidden mask and climbs from translateY(112%) with a 140ms stagger. */

/* No JavaScript — lines rise while unskewing from skewY(7deg), transform-origin left-bottom, so each lands with a whip of momentum. */
```
