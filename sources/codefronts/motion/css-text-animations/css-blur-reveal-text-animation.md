---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-blur-reveal-text-animation/"
title: "CSS Smoky Text Dissipate Blur Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Typography that exhales: a checkbox-driven toggle where letters blur, drift on their own vectors and vanish like smoke (then reform on untoggle), and an…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Smoky Text Dissipate Blur Animation
Source: https://codefronts.com/motion/css-text-animations/css-blur-reveal-text-animation/

Typography that exhales: a checkbox-driven toggle where letters blur, drift on their own vectors and vanish like smoke (then reform on untoggle), and an SVG-filter loop where feTurbulence displacement genuinely shreds the word into vapor before it recondenses.
## HTML
```html
<div class="cat-28-group">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="cat-28a" aria-label="Toggle text into smoke">
  <div class="cat-28a__stage">
    <input class="cat-28a__check" type="checkbox" id="cat-28a-t">
    <h1 class="cat-28a__word" aria-label="VANISH">
      <span aria-hidden="true"><i style="--i:0;--x:-30px;--y:-58px;--r:-18deg">V</i><i style="--i:1;--x:14px;--y:-70px;--r:10deg">A</i><i style="--i:2;--x:-10px;--y:-52px;--r:-6deg">N</i><i style="--i:3;--x:26px;--y:-66px;--r:14deg">I</i><i style="--i:4;--x:-22px;--y:-74px;--r:-12deg">S</i><i style="--i:5;--x:18px;--y:-56px;--r:8deg">H</i></span>
    </h1>
    <label class="cat-28a__switch" for="cat-28a-t"><span class="cat-28a__knob" aria-hidden="true"></span>dissolve</label>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-28b" aria-label="Text shredding into vapor">
  <div class="cat-28b__stage">
    <svg class="cat-28b__svg" viewBox="0 0 640 200">
      <defs>
        <filter id="cat-28b-f" x="-40%" y="-80%" width="180%" height="260%">
          <feTurbulence type="fractalNoise" baseFrequency="0.012 0.05" numOctaves="2" seed="7" result="n">
            <animate attributeName="baseFrequency" values="0.012 0.05;0.02 0.09;0.012 0.05" dur="7s" repeatCount="indefinite"></animate>
          </feTurbulence>
          <feDisplacementMap in="SourceGraphic" in2="n" scale="0" xChannelSelector="R" yChannelSelector="G">
            <animate attributeName="scale" values="0;0;90;0;0" keyTimes="0;.3;.55;.8;1" dur="7s" repeatCount="indefinite"></animate>
          </feDisplacementMap>
        </filter>
      </defs>
      <text x="50%" y="52%" dominant-baseline="central" text-anchor="middle" class="cat-28b__word" filter="url(#cat-28b-f)">VAPOR</text>
    </svg>
    <p class="cat-28b__sub" aria-hidden="true">feTurbulence displacement shreds the edges — blur alone can't do this</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-28-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-28-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-28a,
.cat-28a *,
.cat-28a *::before,
.cat-28a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-28a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#15171c,#0d0e12);
  font-family: 'Playfair Display',Georgia,serif;
}

.cat-28a__stage {
  display: grid;
  gap: 38px;
  justify-items: center;
  text-align: center;
}

.cat-28a__check {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.cat-28a__word {
  font-size: clamp(54px,10vw,130px);
  font-weight: 700;
  letter-spacing: .1em;
  margin-right: -.1em;
  color: #e9e4d8;
}

.cat-28a__word i {
  display: inline-block;
  font-style: normal;
  transition: transform 1.1s cubic-bezier(.3,.6,.4,1),opacity 1s ease,filter 1s ease;
  transition-delay: calc(var(--i)*55ms);
}

.cat-28a__check:checked ~ .cat-28a__word i {
  opacity: 0;
  filter: blur(14px);
  transform: translate(var(--x),var(--y)) rotate(var(--r)) scale(1.35);
}

.cat-28a__switch {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: rgba(233,228,216,.6);
  cursor: pointer;
  user-select: none;
}

.cat-28a__knob {
  width: 42px;
  height: 24px;
  border-radius: 999px;
  background: rgba(233,228,216,.14);
  border: 1px solid rgba(233,228,216,.25);
  position: relative;
  transition: background .3s;
}

.cat-28a__knob::after {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #e9e4d8;
  transition: transform .3s cubic-bezier(.2,.8,.3,1);
}

.cat-28a__check:checked ~ .cat-28a__switch .cat-28a__knob {
  background: rgba(233,228,216,.35);
}

.cat-28a__check:checked ~ .cat-28a__switch .cat-28a__knob::after {
  transform: translateX(18px);
}

.cat-28a__check:focus-visible ~ .cat-28a__switch .cat-28a__knob {
  outline: 2px solid #e9e4d8;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cat-28a__word i {
    transition: opacity .4s ease;
    transition-delay: 0s;
  }

  .cat-28a__check:checked ~ .cat-28a__word i {
    transform: none;
    filter: none;
  }
}

.cat-28b,
.cat-28b *,
.cat-28b *::before,
.cat-28b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-28b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0e1116;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-28b__stage {
  text-align: center;
  width: min(680px,100%);
}

.cat-28b__svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.cat-28b__word {
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
  font-size: 120px;
  font-weight: 700;
  letter-spacing: 8px;
  fill: #dfe7f2;
  animation: cat-28b-haze 7s ease-in-out infinite;
}

.cat-28b__sub {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  color: rgba(180,200,230,.4);
}

@keyframes cat-28b-haze {
  0%,
    30% {
    opacity: 1;
    filter: blur(0);
  }

  55% {
    opacity: .06;
    filter: blur(9px);
  }

  80%,
    100% {
    opacity: 1;
    filter: blur(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-28b__word {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a visually-hidden checkbox drives :checked ~ sibling selectors; each letter blurs and drifts along its own inline vector with a staggered delay, and untoggling reverses it. */

/* No JavaScript — SMIL animates feTurbulence frequency and the displacement scale (0→90→0) while a synchronized CSS keyframe handles blur and opacity; the word shreds, vanishes, recondenses. */
```
