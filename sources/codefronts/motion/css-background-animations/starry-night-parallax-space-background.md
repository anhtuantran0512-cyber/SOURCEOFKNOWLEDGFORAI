---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/starry-night-parallax-space-background/"
title: "Starry Night Sky & Falling Starfall"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Hundreds of stars and a meteor shower, with four DOM nodes."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Starry Night Sky & Falling Starfall
Source: https://codefronts.com/motion/css-background-animations/starry-night-parallax-space-background/

Hundreds of stars and a meteor shower, with four DOM nodes. The field is three tiled radial-gradient layers at different densities and parallax speeds, twinkling by opacity; the meteors are five elements with a bright head, a tapered tail drawn by a gradient, and staggered delays on a long cycle so they arrive irregularly — never in a metronomic loop.
## HTML
```html
<section class="bga-22" aria-label="Starry night sky and falling stars background demo">
  <div class="bga-22__void" aria-hidden="true"></div>
  <div class="bga-22__nebula" aria-hidden="true"></div>
  <div class="bga-22__stars bga-22__stars--far" aria-hidden="true"></div>
  <div class="bga-22__stars bga-22__stars--mid" aria-hidden="true"></div>
  <div class="bga-22__stars bga-22__stars--near" aria-hidden="true"></div>

  <div class="bga-22__shower" aria-hidden="true">
    <span class="bga-22__meteor" style="--bga-22-d:0s;--bga-22-top:-6%;--bga-22-left:-8%;--bga-22-len:210px"></span>
    <span class="bga-22__meteor" style="--bga-22-d:4.3s;--bga-22-top:8%;--bga-22-left:16%;--bga-22-len:150px"></span>
    <span class="bga-22__meteor" style="--bga-22-d:9.1s;--bga-22-top:-12%;--bga-22-left:42%;--bga-22-len:260px"></span>
    <span class="bga-22__meteor" style="--bga-22-d:14.7s;--bga-22-top:2%;--bga-22-left:64%;--bga-22-len:170px"></span>
    <span class="bga-22__meteor" style="--bga-22-d:21.2s;--bga-22-top:-4%;--bga-22-left:28%;--bga-22-len:300px"></span>
  </div>

  <div class="bga-22__stage">
    <div class="bga-22__copy">
      <p class="bga-22__eyebrow">Four nodes, hundreds of stars · 22</p>
      <h1 class="bga-22__title">Perseids,<br>in three paint layers.</h1>
      <p class="bga-22__sub">Coprime tile sizes so the field never visibly repeats, opacity-only twinkling, and meteor delays chosen so arrivals stay irregular for the whole 26-second cycle.</p>
      <div class="bga-22__legend">
        <span>140px · 83px · 61px tiles</span>
        <span>5 meteors · 26s cycle</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-22,
.bga-22 *,
.bga-22 *::before,
.bga-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-22-bg: oklch(0.11 0.03 268);
  --bga-22-star: oklch(0.99 0.005 250);
  --bga-22-acc: oklch(0.82 0.13 250);
  background: var(--bga-22-bg);
  color: oklch(0.97 0.008 250);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-22__void {
  position: absolute;
  inset: 0;
  background: radial-gradient(130% 100% at 50% 108%,oklch(0.2 0.05 262),oklch(0.08 0.025 272) 68%);
}

.bga-22__nebula {
  position: absolute;
  inset: 0;
  opacity: .5;
  mix-blend-mode: screen;
  filter: blur(46px);
  background: radial-gradient(34% 30% at 22% 30%,oklch(0.5 0.18 300/.5),transparent 70%), radial-gradient(30% 26% at 74% 22%,oklch(0.48 0.16 220/.45),transparent 72%), radial-gradient(40% 30% at 58% 78%,oklch(0.44 0.14 340/.4),transparent 74%);
  animation: bga-22-neb 70s ease-in-out infinite alternate;
}

@keyframes bga-22-neb {
  to {
    translate: 2% -2%;
    scale: 1.12;
  }
}

.bga-22__stars {
  position: absolute;
  inset: -6%;
  background-repeat: repeat;
}

.bga-22__stars--far {
  opacity: .5;
  background-image: radial-gradient(var(--bga-22-star) .6px,transparent .8px);
  background-size: 61px 61px;
  background-position: 14px 22px;
  animation: bga-22-tw 7.5s ease-in-out infinite alternate,bga-22-drift 220s linear infinite;
}

.bga-22__stars--mid {
  opacity: .72;
  background-image: radial-gradient(var(--bga-22-star) .85px,transparent 1.05px),radial-gradient(oklch(0.86 0.09 240/.8) .7px,transparent .95px);
  background-size: 83px 83px,127px 127px;
  background-position: 0 0,47px 61px;
  animation: bga-22-tw 5s ease-in-out infinite alternate-reverse,bga-22-drift 150s linear infinite;
}

.bga-22__stars--near {
  background-image: radial-gradient(var(--bga-22-star) 1.2px,transparent 1.45px);
  background-size: 140px 140px;
  background-position: 66px 31px;
  filter: drop-shadow(0 0 4px oklch(0.9 0.06 240/.7));
  animation: bga-22-tw 3.6s ease-in-out infinite alternate,bga-22-drift 95s linear infinite;
}

@keyframes bga-22-tw {
  from {
    opacity: .4;
  }

  to {
    opacity: 1;
  }
}

@keyframes bga-22-drift {
  to {
    background-position-x: -140px;
  }
}

.bga-22__shower {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

.bga-22__meteor {
  position: absolute;
  top: var(--bga-22-top);
  left: var(--bga-22-left);
  width: var(--bga-22-len,200px);
  height: 2px;
  border-radius: 99px;
  rotate: 32deg;
  transform-origin: 0 50%;
  opacity: 0;
  background: linear-gradient(270deg,oklch(1 0 0) 0 2%,color-mix(in oklab,var(--bga-22-acc) 72%,transparent) 18%,transparent 100%);
  filter: drop-shadow(0 0 6px oklch(0.9 0.08 240/.9));
  animation: bga-22-fall 26s cubic-bezier(.5,0,.85,.45) infinite;
  animation-delay: var(--bga-22-d,0s);
}

@keyframes bga-22-fall {
  0% {
    translate: 0 0;
    opacity: 0;
    scale: .35 1;
  }

  1.2% {
    opacity: 1;
  }

  9% {
    translate: 78vw 62vh;
    opacity: 0;
    scale: 1.5 1;
  }

  100% {
    translate: 78vw 62vh;
    opacity: 0;
    scale: 1.5 1;
  }
}

.bga-22__stage {
  position: relative;
  z-index: 5;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-22__copy {
  width: min(100%,660px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
}

.bga-22__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--bga-22-acc);
}

.bga-22__title {
  font-size: clamp(29px,6vw,62px);
  font-weight: 600;
  line-height: 1.01;
  letter-spacing: -.05em;
  text-wrap: balance;
  text-shadow: 0 0 50px oklch(0.7 0.12 250/.4),0 3px 24px oklch(0.08 0.02 270/.9);
}

.bga-22__sub {
  max-width: 52ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.93 0.01 250/.78);
  text-wrap: pretty;
  text-shadow: 0 1px 14px oklch(0.08 0.02 270/.9);
}

.bga-22__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 8px;
}

.bga-22__legend span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 7px 13px;
  border-radius: 99px;
  color: oklch(1 0 0/.68);
  background: oklch(1 0 0/.06);
  border: 1px solid oklch(1 0 0/.14);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

@media (prefers-reduced-motion: reduce) {
  .bga-22__stars,
    .bga-22__meteor,
    .bga-22__nebula {
    animation: none;
  }

  .bga-22__meteor {
    opacity: .55;
  }
}
```
