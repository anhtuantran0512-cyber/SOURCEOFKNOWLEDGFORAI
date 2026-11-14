---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-text-stroke-draw-animation/"
title: "CSS Animated Stroke Text Drawing Effect"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Self-writing typography via the dash trick: a script word that hand-draws itself then floods with ink, and a technical neon tracer where a lit dash segment…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Stroke Text Drawing Effect
Source: https://codefronts.com/motion/css-text-animations/css-text-stroke-draw-animation/

Self-writing typography via the dash trick: a script word that hand-draws itself then floods with ink, and a technical neon tracer where a lit dash segment chases endlessly around the letterforms with a glow filter.
## HTML
```html
<div class="cat-24-group">
<link href="https://fonts.googleapis.com/css2?family=Caveat:[email protected]&display=swap" rel="stylesheet">
<section class="cat-24a" aria-label="Script text draws itself then fills">
  <div class="cat-24a__stage">
    <svg class="cat-24a__svg" viewBox="0 0 640 220">
      <text x="50%" y="54%" dominant-baseline="central" text-anchor="middle" class="cat-24a__word">Merci</text>
    </svg>
    <p class="cat-24a__sub" aria-hidden="true">stroke-dashoffset 640 → 0, then the fill floods in</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-24b" aria-label="Neon segment tracing letter outlines">
  <div class="cat-24b__stage">
    <svg class="cat-24b__svg" viewBox="0 0 640 190">
      <text x="50%" y="52%" dominant-baseline="central" text-anchor="middle" class="cat-24b__base">TRACE</text>
      <text x="50%" y="52%" dominant-baseline="central" text-anchor="middle" class="cat-24b__lit" aria-hidden="true">TRACE</text>
    </svg>
    <p class="cat-24b__sub" aria-hidden="true">a 70-unit lit dash chases a 560-unit gap forever</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-24-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-24-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-24a,
.cat-24a *,
.cat-24a *::before,
.cat-24a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-24a {
  --ink: #1d2440;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f4efe6;
  background-image: radial-gradient(rgba(29,36,64,.06) 1px,transparent 1px);
  background-size: 26px 26px;
}

.cat-24a__stage {
  text-align: center;
  width: min(660px,100%);
}

.cat-24a__svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.cat-24a__word {
  font-family: 'Caveat',cursive;
  font-size: 170px;
  font-weight: 600;
  fill: transparent;
  stroke: var(--ink);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 640;
  stroke-dashoffset: 640;
  animation: cat-24a-draw 3s ease-in-out .4s forwards,cat-24a-ink .7s ease 3.1s forwards;
}

.cat-24a__sub {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  color: rgba(29,36,64,.45);
}

@keyframes cat-24a-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes cat-24a-ink {
  to {
    fill: var(--ink);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-24a__word {
    animation: none;
    stroke-dashoffset: 0;
    fill: var(--ink);
  }
}

.cat-24b,
.cat-24b *,
.cat-24b *::before,
.cat-24b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-24b {
  --glow: oklch(0.85 0.18 190);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0a0f14;
}

.cat-24b__stage {
  text-align: center;
  width: min(660px,100%);
}

.cat-24b__svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.cat-24b__base,
.cat-24b__lit {
  font-family: 'Archivo','Arial Black',sans-serif;
  font-size: 130px;
  font-weight: 900;
  letter-spacing: 4px;
  fill: transparent;
}

.cat-24b__base {
  stroke: rgba(140,200,230,.18);
  stroke-width: 1.5;
}

.cat-24b__lit {
  stroke: var(--glow);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-dasharray: 70 560;
  stroke-dashoffset: 0;
  filter: drop-shadow(0 0 6px var(--glow)) drop-shadow(0 0 18px color-mix(in oklab,var(--glow) 60%,transparent));
  animation: cat-24b-chase 3.2s linear infinite;
}

.cat-24b__sub {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  color: rgba(150,200,230,.4);
}

@keyframes cat-24b-chase {
  to {
    stroke-dashoffset: -630;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-24b__lit {
    animation: none;
    stroke-dasharray: none;
    opacity: .7;
    filter: drop-shadow(0 0 6px var(--glow));
  }
}
```

## JavaScript
```js
/* No JavaScript — the outline's dash equals its length, offset to invisible, then animated to 0; a second keyframe floods the fill once the pen finishes. */

/* No JavaScript — a dim full outline sits under a lit copy whose dasharray is 70 lit / 560 gap; offsetting one full period per loop chases the segment around the glyphs. */
```
