---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-liquid-fill-text-animation/"
title: "CSS Animated Liquid Fill Text Effect"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Letters as vessels: an SVG-masked word where real vector waves slosh horizontally while the waterline rises through the glyphs, and a no-SVG fallback that…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Liquid Fill Text Effect
Source: https://codefronts.com/motion/css-text-animations/css-liquid-fill-text-animation/

Letters as vessels: an SVG-masked word where real vector waves slosh horizontally while the waterline rises through the glyphs, and a no-SVG fallback that fakes the same physics with layered gradients and a repeating crest — both loop fill → hold → drain.
## HTML
```html
<div class="cat-22-group">
<section class="cat-22a" aria-label="Liquid fill text with SVG waves">
  <div class="cat-22a__stage">
    <svg class="cat-22a__svg" viewBox="0 0 640 190" role="img" aria-label="FLOW">
      <defs>
        <mask id="cat-22a-m"><text x="50%" y="50%" dominant-baseline="central" text-anchor="middle" class="cat-22a__mtext" fill="#fff">FLOW</text></mask>
        <linearGradient id="cat-22a-wg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6ee7ff"></stop><stop offset="1" stop-color="#0e7ac2"></stop></linearGradient>
      </defs>
      <text x="50%" y="50%" dominant-baseline="central" text-anchor="middle" class="cat-22a__mtext cat-22a__outline">FLOW</text>
      <g mask="url(#cat-22a-m)">
        <g class="cat-22a__water">
          <path class="cat-22a__wave cat-22a__wave--back" d="M-640 40 Q -560 24 -480 40 T -320 40 T -160 40 T 0 40 T 160 40 T 320 40 T 480 40 T 640 40 V 260 H -640 Z" fill="#1897d8" opacity=".55"></path>
          <path class="cat-22a__wave" d="M-640 44 Q -560 28 -480 44 T -320 44 T -160 44 T 0 44 T 160 44 T 320 44 T 480 44 T 640 44 V 260 H -640 Z" fill="url(#cat-22a-wg)"></path>
        </g>
      </g>
    </svg>
    <p class="cat-22a__sub" aria-hidden="true">an SVG mask confines the ocean to the letterforms</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-22b" aria-label="Gradient liquid fill text">
  <div class="cat-22b__stage">
    <h1 class="cat-22b__word">HYDRATE</h1>
    <p class="cat-22b__sub" aria-hidden="true">@property --fill animates the waterline · a repeating crest scrolls the surface</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-22-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-22-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-22a,
.cat-22a *,
.cat-22a *::before,
.cat-22a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-22a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 90% at 50% 10%,#0d1b2b,#071019 70%);
}

.cat-22a__stage {
  text-align: center;
  width: min(680px,100%);
}

.cat-22a__svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.cat-22a__mtext {
  font-family: 'Archivo Black','Arial Black','Segoe UI',sans-serif;
  font-weight: 900;
  font-size: 150px;
  letter-spacing: 6px;
}

.cat-22a__outline {
  fill: transparent;
  stroke: rgba(140,200,240,.35);
  stroke-width: 1.5;
}

.cat-22a__water {
  animation: cat-22a-rise 5.2s ease-in-out infinite alternate;
}

.cat-22a__wave {
  animation: cat-22a-slosh 3.2s linear infinite;
}

.cat-22a__wave--back {
  animation-duration: 4.6s;
  animation-direction: reverse;
}

.cat-22a__sub {
  margin-top: 14px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(150,200,235,.45);
}

@keyframes cat-22a-slosh {
  to {
    transform: translateX(320px);
  }
}

@keyframes cat-22a-rise {
  from {
    transform: translateY(150px);
  }

  to {
    transform: translateY(-18px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-22a__water {
    animation: none;
    transform: translateY(46px);
  }

  .cat-22a__wave {
    animation: none;
  }
}

@property --cat22b-fill {
  syntax: '<percentage>';
  initial-value: 12%;
  inherits: false;
}

.cat-22b,
.cat-22b *,
.cat-22b *::before,
.cat-22b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-22b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0a1418;
}

.cat-22b__stage {
  text-align: center;
}

.cat-22b__word {
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
  font-size: clamp(44px,9vw,116px);
  font-weight: 900;
  letter-spacing: .01em;
  color: rgba(150,220,235,.18);
  -webkit-text-stroke: 1.25px rgba(150,220,235,.4);
  background: radial-gradient(7px 5px at 8px 2px,rgba(190,240,255,.9) 46%,transparent 54%) repeat-x 0 calc(100% - var(--cat22b-fill)) / 16px 8px,linear-gradient(180deg,#54d4f0,#0f7fae) no-repeat 0 100% / 100% var(--cat22b-fill);
  -webkit-background-clip: text;
  background-clip: text;
  animation: cat-22b-fill 6.4s ease-in-out infinite alternate,cat-22b-crest 1.1s linear infinite;
}

.cat-22b__sub {
  margin-top: 20px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .14em;
  color: rgba(150,210,230,.4);
}

@keyframes cat-22b-fill {
  to {
    --cat22b-fill: 88%;
  }
}

@keyframes cat-22b-crest {
  to {
    background-position: 16px calc(100% - var(--cat22b-fill)),0 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-22b__word {
    animation: none;
    --cat22b-fill: 62%;
  }
}
```

## JavaScript
```js
/* No JavaScript — two wave paths slosh horizontally at different speeds while their group rises and drains; a white-text SVG mask keeps the water inside the glyphs. */

/* No JavaScript — a solid water gradient's height is the registered custom property --fill (animated 12%→88%), with a repeating radial crest strip riding the waterline. */
```
