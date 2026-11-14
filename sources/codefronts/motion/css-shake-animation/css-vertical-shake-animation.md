---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-vertical-shake-animation/"
title: "CSS Vertical Shake Animation"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The vertical axis has different physics: a jackhammer specimen that hammers downward with asymmetric frames (fast down, slow up — impacts are one-sided), and…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vertical Shake Animation
Source: https://codefronts.com/motion/css-shake-animation/css-vertical-shake-animation/

The vertical axis has different physics: a jackhammer specimen that hammers downward with asymmetric frames (fast down, slow up — impacts are one-sided), and a landing thud where a dropped card hits, compresses, and rings out a decaying vertical shudder with a dust-line flash.
## HTML
```html
<div class="shk-23-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-23a" aria-label="Jackhammer vertical shake specimen">
  <div class="shk-23a__site">
    <p class="shk-23a__permit">PERMIT NO. 23-Y · VERTICAL WORKS</p>
    <div class="shk-23a__stage">
      <div class="shk-23a__hammer" tabindex="0" aria-label="Hammering block — hover to pause">UNDER<br>CONSTRUCTION</div>
      <div class="shk-23a__ground" aria-hidden="true"></div>
    </div>
    <p class="shk-23a__note">down-strokes 6px & fast · up-strokes 1px & lazy — impacts are one-sided</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-23b" aria-label="Card that drops, thuds and shudders">
  <div class="shk-23b__stage">
    <div class="shk-23b__card" tabindex="0">
      <p class="shk-23b__big">17,4 kg</p>
      <p class="shk-23b__small">delivered · signature not required</p>
    </div>
    <div class="shk-23b__shadow" aria-hidden="true"></div>
    <p class="shk-23b__hint" aria-hidden="true">replays every 3.5s (hover to pause) — drop → squash → decaying vertical shudder, one timeline</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-23-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-23-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-23a,
.shk-23a *,
.shk-23a *::before,
.shk-23a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-23a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: repeating-linear-gradient(45deg,#f4c81d 0 26px,#191713 26px 52px);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-23a__site {
  width: min(440px,100%);
  padding: 30px 32px 26px;
  background: #f7f4ea;
  border: 3px solid #191713;
  border-radius: 6px;
  box-shadow: 10px 10px 0 rgba(25,23,19,.85);
}

.shk-23a__permit {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  color: #191713;
  border-bottom: 2px dashed rgba(25,23,19,.3);
  padding-bottom: 10px;
}

.shk-23a__stage {
  margin-top: 26px;
  display: grid;
  justify-items: center;
}

.shk-23a__hammer {
  padding: 22px 30px;
  text-align: center;
  font-size: 21px;
  line-height: 1.15;
  font-weight: 900;
  letter-spacing: .04em;
  color: #f7f4ea;
  background: #191713;
  border-radius: 4px;
  transform-origin: 50% 100%;
  animation: shk-23a-hammer .5s linear infinite;
  outline: none;
}

.shk-23a__hammer:hover,
.shk-23a__hammer:focus-visible {
  animation-play-state: paused;
}

.shk-23a__ground {
  width: 78%;
  height: 5px;
  margin-top: 6px;
  background: rgba(25,23,19,.85);
  border-radius: 999px;
  animation: shk-23a-dust .5s linear infinite;
}

.shk-23a__note {
  margin-top: 22px;
  font-size: 12px;
  font-weight: 600;
  color: rgba(25,23,19,.6);
  text-align: center;
  text-wrap: pretty;
}

@keyframes shk-23a-hammer {
  0%,
    100% {
    translate: 0 0;
    scale: 1 1;
  }

  15% {
    translate: 0 6px;
    scale: 1.05 .94;
  }

  35% {
    translate: 0 -1px;
    scale: 1 1;
  }

  50% {
    translate: 0 5px;
    scale: 1.04 .95;
  }

  70% {
    translate: 0 -.5px;
    scale: 1 1;
  }

  85% {
    translate: 0 4px;
    scale: 1.03 .96;
  }
}

@keyframes shk-23a-dust {
  0%,
    100% {
    scale: 1 1;
    opacity: .85;
  }

  15% {
    scale: 1.06 1;
    opacity: 1;
  }

  50% {
    scale: 1.05 1;
  }

  85% {
    scale: 1.04 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-23a__hammer,
    .shk-23a__ground {
    animation: none;
  }
}

.shk-23b,
.shk-23b *,
.shk-23b *::before,
.shk-23b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-23b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 100% at 50% 0%,#1b1e26,#101218 65%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-23b__stage {
  display: grid;
  justify-items: center;
}

.shk-23b__card {
  padding: 30px 44px;
  text-align: center;
  background: linear-gradient(180deg,#f2e8d8,#e2d2b8);
  border-radius: 14px;
  box-shadow: 0 24px 45px -20px rgba(0,0,0,.75);
  transform-origin: 50% 100%;
  animation: shk-23b-thud 3.5s cubic-bezier(.5,0,.7,.3) infinite;
  outline: none;
}

.shk-23b__card:hover,
.shk-23b__card:focus-visible {
  animation-play-state: paused;
}

.shk-23b__big {
  font-size: 34px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: #2c2416;
}

.shk-23b__small {
  margin-top: 6px;
  font-size: 12.5px;
  color: rgba(44,36,22,.55);
}

.shk-23b__shadow {
  width: 200px;
  height: 12px;
  margin-top: 14px;
  border-radius: 50%;
  background: rgba(0,0,0,.55);
  filter: blur(5px);
  animation: shk-23b-shadow 3.5s cubic-bezier(.5,0,.7,.3) infinite;
}

.shk-23b__hint {
  margin-top: 26px;
  font-size: 12px;
  color: rgba(230,235,248,.4);
  max-width: 420px;
  text-align: center;
}

@keyframes shk-23b-thud {
  0% {
    translate: 0 -120px;
    scale: 1 1;
    opacity: 0;
  }

  6% {
    opacity: 1;
  }

  12% {
    translate: 0 0;
    scale: 1 1;
  }

  15% {
    scale: 1.12 .84;
  }

  20% {
    scale: .96 1.05;
  }

  25% {
    translate: 0 3px;
    scale: 1.03 .97;
  }

  31% {
    translate: 0 -1.5px;
    scale: 1 1;
  }

  37% {
    translate: 0 1.5px;
  }

  43% {
    translate: 0 -.5px;
  }

  48%,
    86% {
    translate: 0 0;
    scale: 1 1;
  }

  100% {
    translate: 0 -120px;
    opacity: 0;
  }
}

@keyframes shk-23b-shadow {
  0% {
    scale: .45 1;
    opacity: .25;
  }

  12% {
    scale: 1 1;
    opacity: .8;
  }

  15% {
    scale: 1.15 1;
  }

  25% {
    scale: 1.04 1;
  }

  48%,
    86% {
    scale: 1 1;
    opacity: .8;
  }

  100% {
    scale: .45 1;
    opacity: .25;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-23b__card,
    .shk-23b__shadow {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — down-frames are large/fast, up-frames small/slow (gravity is asymmetric), each contact squashes via scale with transform-origin at the bottom edge, and the ground line stretches in sympathy on the same clock. */

/* No JavaScript — fall, squash, and shudder are segments of ONE keyframe timeline, with the ground shadow scaling on a matching clock so light and mass agree. Faking physics = choreographing consequences. */
```
