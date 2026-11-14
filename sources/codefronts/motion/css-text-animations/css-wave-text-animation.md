---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-wave-text-animation/"
title: "CSS Wavy Text Animation Keyframes"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "A continuous sine wave rolling through letters two ways: a soft ocean bob for friendly onboarding headers, and a candy-colored jelly squash where each letter…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Wavy Text Animation Keyframes
Source: https://codefronts.com/motion/css-text-animations/css-wave-text-animation/

A continuous sine wave rolling through letters two ways: a soft ocean bob for friendly onboarding headers, and a candy-colored jelly squash where each letter compresses as it lands.
## HTML
```html
<div class="cat-11-group">
<link href="https://fonts.googleapis.com/css2?family=Fredoka:[email protected]&display=swap" rel="stylesheet">
<section class="cat-11a" aria-label="Ocean wave text animation">
  <div class="cat-11a__stage">
    <h1 class="cat-11a__word" aria-label="make waves">
      <span aria-hidden="true"><i style="--i:0">m</i><i style="--i:1">a</i><i style="--i:2">k</i><i style="--i:3">e</i><i class="cat-11a__sp" style="--i:4">&nbsp;</i><i style="--i:5">w</i><i style="--i:6">a</i><i style="--i:7">v</i><i style="--i:8">e</i><i style="--i:9">s</i></span>
    </h1>
    <p class="cat-11a__sub">negative delays phase-shift one shared keyframe</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:[email protected]&display=swap" rel="stylesheet">
<section class="cat-11b" aria-label="Jelly squash text animation">
  <div class="cat-11b__stage">
    <h1 class="cat-11b__word" aria-label="squishy!">
      <span aria-hidden="true"><i style="--i:0">s</i><i style="--i:1">q</i><i style="--i:2">u</i><i style="--i:3">i</i><i style="--i:4">s</i><i style="--i:5">h</i><i style="--i:6">y</i><i style="--i:7">!</i></span>
    </h1>
    <p class="cat-11b__sub">squash &amp; stretch + per-letter oklch hue</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-11-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-11-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-11a,
.cat-11a *,
.cat-11a *::before,
.cat-11a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-11a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#e8f6f8,#cdeef2);
  font-family: 'Fredoka','Segoe UI',system-ui,sans-serif;
}

.cat-11a__stage {
  text-align: center;
}

.cat-11a__word {
  font-size: clamp(48px,9vw,110px);
  font-weight: 600;
  color: oklch(0.52 0.12 220);
  letter-spacing: .01em;
}

.cat-11a__word i {
  display: inline-block;
  font-style: normal;
  animation: cat-11a-wave 1.6s ease-in-out infinite;
  animation-delay: calc(var(--i)*-.12s);
}

.cat-11a__sub {
  margin-top: 18px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  color: rgba(40,90,110,.5);
}

@keyframes cat-11a-wave {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-16px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-11a__word i {
    animation: none;
  }
}

.cat-11b,
.cat-11b *,
.cat-11b *::before,
.cat-11b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-11b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #1b1224;
  font-family: 'Fredoka','Segoe UI',system-ui,sans-serif;
}

.cat-11b__stage {
  text-align: center;
}

.cat-11b__word {
  font-size: clamp(52px,9.6vw,116px);
  font-weight: 700;
  letter-spacing: .02em;
}

.cat-11b__word i {
  display: inline-block;
  font-style: normal;
  color: oklch(0.8 0.19 calc(var(--i)*42));
  transform-origin: center bottom;
  animation: cat-11b-jelly 1.5s ease-in-out infinite;
  animation-delay: calc(var(--i)*-.13s);
  text-shadow: 0 6px 24px rgb(0 0 0/.35);
}

.cat-11b__sub {
  margin-top: 18px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  color: rgba(220,200,240,.4);
}

@keyframes cat-11b-jelly {
  0%,
    100% {
    transform: translateY(0) scale(1.04,.92);
  }

  35% {
    transform: translateY(-20px) scale(.94,1.08);
  }

  70% {
    transform: translateY(0) scale(1.1,.86);
  }

  85% {
    transform: translateY(-3px) scale(.98,1.02);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-11b__word i {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one ease-in-out bounce keyframe; calc(var(--i) * -0.12s) negative delays phase-shift letters into a travelling sine wave. */

/* No JavaScript — the wave keyframe gains squash-and-stretch scale() pairs (origin bottom) and each letter tints via oklch(0.8 0.19 calc(var(--i)*42)). */
```
