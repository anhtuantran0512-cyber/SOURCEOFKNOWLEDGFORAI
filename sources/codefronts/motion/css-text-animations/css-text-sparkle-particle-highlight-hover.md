---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-text-sparkle-particle-highlight-hover/"
title: "CSS Text Sparkle Particle Highlight Hover"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "The 'AI feature' shimmer, done properly: a gradient badge whose four-point sparkles pop in sequence around the label on hover (clip-path stars, no images),…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Sparkle Particle Highlight Hover
Source: https://codefronts.com/motion/css-text-animations/css-text-sparkle-particle-highlight-hover/

The 'AI feature' shimmer, done properly: a gradient badge whose four-point sparkles pop in sequence around the label on hover (clip-path stars, no images), and a display word wearing an always-on twinkle field with a hover-accelerated glitter sweep.
## HTML
```html
<div class="cat-01-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-01a" aria-label="AI badge with sparkle particles">
  <div class="cat-01a__stage">
    <button class="cat-01a__badge" type="button">
      <span class="cat-01a__spark" style="--i:0;top:-10px;left:12%" aria-hidden="true"></span>
      <span class="cat-01a__spark" style="--i:1;top:-14px;right:20%" aria-hidden="true"></span>
      <span class="cat-01a__spark cat-01a__spark--sm" style="--i:2;bottom:-10px;right:8%" aria-hidden="true"></span>
      <span class="cat-01a__spark cat-01a__spark--sm" style="--i:3;bottom:-12px;left:26%" aria-hidden="true"></span>
      <em class="cat-01a__glyph" aria-hidden="true">✦</em>Ask AI anything
    </button>
    <p class="cat-01a__sub" aria-hidden="true">hover / focus — clip-path stars pop in sequence</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="cat-01b" aria-label="Twinkling glitter text">
  <div class="cat-01b__stage">
    <h1 class="cat-01b__word" tabindex="0">shimmer<i class="cat-01b__stars" aria-hidden="true"></i></h1>
    <p class="cat-01b__sub" aria-hidden="true">always-on twinkle · hover speeds the sweep</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-01-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-01-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-01a,
.cat-01a *,
.cat-01a *::before,
.cat-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-01a {
  --a: oklch(0.75 0.19 300);
  --b: oklch(0.8 0.16 200);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 100% at 50% 0%,#171225,#0b0913 70%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-01a__stage {
  text-align: center;
  display: grid;
  gap: 26px;
  justify-items: center;
}

.cat-01a__badge {
  position: relative;
  isolation: isolate;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font: inherit;
  font-size: 17px;
  font-weight: 600;
  color: #fff;
  padding: 14px 26px;
  border: 1px solid color-mix(in oklab,var(--a) 55%,transparent);
  border-radius: 999px;
  cursor: pointer;
  background: linear-gradient(120deg,color-mix(in oklab,var(--a) 30%,#0b0913),color-mix(in oklab,var(--b) 24%,#0b0913));
  box-shadow: 0 0 0 0 transparent;
  transition: box-shadow .35s,border-color .35s;
}

.cat-01a__glyph {
  font-style: normal;
  background: linear-gradient(120deg,var(--b),var(--a));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-size: 1.15em;
}

.cat-01a__spark {
  position: absolute;
  width: 16px;
  height: 16px;
  background: linear-gradient(140deg,#fff,var(--b));
  clip-path: polygon(50% 0,62% 38%,100% 50%,62% 62%,50% 100%,38% 62%,0 50%,38% 38%);
  transform: scale(0);
  pointer-events: none;
  z-index: 1;
}

.cat-01a__spark--sm {
  width: 10px;
  height: 10px;
}

.cat-01a__badge:hover,
.cat-01a__badge:focus-visible {
  border-color: var(--a);
  box-shadow: 0 0 30px -6px color-mix(in oklab,var(--a) 60%,transparent),0 0 60px -18px var(--b);
}

.cat-01a__badge:hover .cat-01a__spark,
.cat-01a__badge:focus-visible .cat-01a__spark {
  animation: cat-01a-pop .75s cubic-bezier(.2,.9,.3,1.4) calc(var(--i)*90ms) both;
}

.cat-01a__badge:focus-visible {
  outline: 2px solid var(--b);
  outline-offset: 4px;
}

.cat-01a__sub {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(200,190,235,.4);
}

@keyframes cat-01a-pop {
  0% {
    transform: scale(0) rotate(0);
  }

  60% {
    transform: scale(1.25) rotate(40deg);
  }

  100% {
    transform: scale(1) rotate(45deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-01a__badge:hover .cat-01a__spark,
    .cat-01a__badge:focus-visible .cat-01a__spark {
    animation: none;
    transform: scale(1) rotate(45deg);
  }
}

.cat-01b,
.cat-01b *,
.cat-01b *::before,
.cat-01b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-01b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0d0a14;
}

.cat-01b__stage {
  text-align: center;
}

.cat-01b__word {
  position: relative;
  display: inline-block;
  font-family: 'Playfair Display',Georgia,serif;
  font-style: italic;
  font-weight: 700;
  font-size: clamp(56px,11vw,140px);
  line-height: 1.1;
  padding: 0 .15em;
  background: linear-gradient(115deg,#c9b8e8 20%,#fff 38%,#e8d5f5 46%,#a88fd0 60%,#c9b8e8 80%) 0 0/240% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: cat-01b-sweep 5.5s ease-in-out infinite;
  cursor: default;
}

.cat-01b__word:hover,
.cat-01b__word:focus-visible {
  animation-duration: 1.6s;
}

.cat-01b__word:focus-visible {
  outline: 2px solid #c9b8e8;
  outline-offset: 8px;
}

.cat-01b__stars {
  position: absolute;
  inset: -8% -4%;
  background: radial-gradient(2.5px 2.5px at 18% 30%,#fff 45%,transparent 55%),radial-gradient(2px 2px at 66% 18%,#fff 45%,transparent 55%),radial-gradient(3px 3px at 84% 62%,#fff 45%,transparent 55%),radial-gradient(2px 2px at 38% 74%,#fff 45%,transparent 55%),radial-gradient(2.5px 2.5px at 8% 66%,#fff 45%,transparent 55%);
  animation: cat-01b-twinkle 2.4s ease-in-out infinite;
  pointer-events: none;
}

.cat-01b__sub {
  margin-top: 18px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(200,185,230,.4);
}

@keyframes cat-01b-sweep {
  to {
    background-position: 240% 0;
  }
}

@keyframes cat-01b-twinkle {
  0%,
    100% {
    opacity: .25;
    transform: scale(1);
  }

  50% {
    opacity: 1;
    transform: scale(1.06);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-01b__word {
    animation: none;
  }

  .cat-01b__stars {
    animation: none;
    opacity: .5;
  }
}
```

## JavaScript
```js
/* No JavaScript — four clip-path star spans pop from scale(0) with staggered keyframes while the badge ring glows; all decoration is aria-hidden. */

/* No JavaScript — a light-band gradient sweeps the clipped glyphs on a slow loop (hover shortens the duration) while a radial-gradient star field twinkles above. */
```
