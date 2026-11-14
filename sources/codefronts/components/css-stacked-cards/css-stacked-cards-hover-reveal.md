---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/css-stacked-cards-hover-reveal/"
title: "CSS Stacked Cards Hover Reveal"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "An editorial-style deck of portfolio cards sitting in a slightly rotated pile on a warm paper backdrop."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stacked Cards Hover Reveal
Source: https://codefronts.com/components/css-stacked-cards/css-stacked-cards-hover-reveal/

An editorial-style deck of portfolio cards sitting in a slightly rotated pile on a warm paper backdrop. On hover the four cards fan outward into an arc, and hovering any single card lifts it forward. Built for creative portfolios, team profiles, and service offerings where a tactile micro-interaction matters more than chrome. Pure CSS, no JavaScript.
## HTML
```html
<div class="scd-28">
  <div class="scd-28__stage" data-scd-28="scene">
    <div class="scd-28__deck" data-scd-28="deck">
      <div class="scd-28__card scd-28__card--c4">
        <div class="scd-28__surface"><div class="scd-28__grad"></div><div class="scd-28__glow"></div><div class="scd-28__sheen"></div></div>
        <div class="scd-28__content"><div class="scd-28__meta"><span class="scd-28__chip">Type</span><span class="scd-28__idx">04</span></div>
        <div class="scd-28__title">Letter<br><em>forms</em></div>
        <div class="scd-28__row"><p class="scd-28__desc">An editorial typography system built for screens.</p></div>
        <span class="scd-28__cta">View case <span class="scd-28__arrow">&rarr;</span></span></div>
      </div>
      <div class="scd-28__card scd-28__card--c3">
        <div class="scd-28__surface"><div class="scd-28__grad"></div><div class="scd-28__glow"></div><div class="scd-28__sheen"></div></div>
        <div class="scd-28__content"><div class="scd-28__meta"><span class="scd-28__chip">Motion</span><span class="scd-28__idx">03</span></div>
        <div class="scd-28__title">In<br><em>motion</em></div>
        <div class="scd-28__row"><p class="scd-28__desc">Kinetic brand identity that moves with intent.</p></div>
        <span class="scd-28__cta">View case <span class="scd-28__arrow">&rarr;</span></span></div>
      </div>
      <div class="scd-28__card scd-28__card--c2">
        <div class="scd-28__surface"><div class="scd-28__grad"></div><div class="scd-28__glow"></div><div class="scd-28__sheen"></div></div>
        <div class="scd-28__content"><div class="scd-28__meta"><span class="scd-28__chip">Color</span><span class="scd-28__idx">02</span></div>
        <div class="scd-28__title">Warm<br><em>tones</em></div>
        <div class="scd-28__row"><p class="scd-28__desc">Palette &amp; art direction with a human warmth.</p></div>
        <span class="scd-28__cta">View case <span class="scd-28__arrow">&rarr;</span></span></div>
      </div>
      <div class="scd-28__card scd-28__card--c1">
        <div class="scd-28__surface"><div class="scd-28__grad"></div><div class="scd-28__glow"></div><div class="scd-28__sheen"></div></div>
        <div class="scd-28__content"><div class="scd-28__meta"><span class="scd-28__chip">Index</span><span class="scd-28__idx">01</span></div>
        <div class="scd-28__title">Selected<br><em>works</em></div>
        <div class="scd-28__row"><p class="scd-28__desc">Hover to open the deck. Move to explore.</p></div>
        <span class="scd-28__cta">Begin <span class="scd-28__arrow">&rarr;</span></span></div>
      </div>
    </div>
    <div class="scd-28__floor"></div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@300;400;500;600&display=swap');

.scd-28,
.scd-28 *,
.scd-28 *::before,
.scd-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-28 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #05060a;
  font-family: 'Geist', sans-serif;
}

.scd-28::before {
  content: '';
  position: absolute;
  inset: -30%;
  background: radial-gradient(40% 40% at 20% 30%, rgba(99,102,241,.35), transparent 70%), radial-gradient(45% 45% at 80% 25%, rgba(236,72,153,.3), transparent 70%), radial-gradient(50% 50% at 50% 85%, rgba(45,212,191,.28), transparent 70%);
  filter: blur(20px);
  animation: scd-28-drift 18s ease-in-out infinite alternate;
  pointer-events: none;
}

@keyframes scd-28-drift {
  0% {
    transform: translate(-3%,-2%) scale(1);
  }

  100% {
    transform: translate(4%,3%) scale(1.12);
  }
}

.scd-28::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, rgba(255,255,255,.022) 0 1px, transparent 1px 3px);
  mix-blend-mode: overlay;
  pointer-events: none;
}

.scd-28__stage {
  position: relative;
  width: 300px;
  height: 400px;
  perspective: 1300px;
  z-index: 1;
}

.scd-28__deck {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .25s ease-out;
}

.scd-28__card {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  transform-style: preserve-3d;
  transition: transform .8s cubic-bezier(.16,1,.3,1), box-shadow .6s, filter .6s;
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(0,0,0,.55), 0 0 0 1px rgba(255,255,255,.08) inset;
}

.scd-28__surface {
  position: absolute;
  inset: 0;
  backdrop-filter: blur(8px);
}

.scd-28__grad {
  position: absolute;
  inset: 0;
  opacity: .9;
  background-size: 200% 200%;
  animation: scd-28-flow 8s ease infinite;
}

@keyframes scd-28-flow {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.scd-28__glow {
  position: absolute;
  inset: 0;
  background: radial-gradient(280px circle at var(--mx,50%) var(--my,40%), rgba(255,255,255,.4), transparent 60%);
  mix-blend-mode: soft-light;
  opacity: 0;
  transition: opacity .5s;
}

.scd-28__card:hover .scd-28__glow {
  opacity: 1;
}

.scd-28__sheen {
  position: absolute;
  top: -60%;
  left: -30%;
  width: 60%;
  height: 220%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.5), transparent);
  transform: rotate(18deg) translateX(-220px);
  transition: transform .9s cubic-bezier(.16,1,.3,1);
}

.scd-28__card:hover .scd-28__sheen {
  transform: rotate(18deg) translateX(560px);
}

.scd-28__content {
  position: absolute;
  inset: 0;
  padding: 28px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transform: translateZ(50px);
}

.scd-28__meta {
  display: flex;
  align-items: center;
  gap: 10px;
}

.scd-28__chip {
  font-size: .62rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,.16);
  backdrop-filter: blur(6px);
  color: #fff;
  font-weight: 500;
  border: 1px solid rgba(255,255,255,.22);
}

.scd-28__idx {
  margin-left: auto;
  font-family: 'Instrument Serif', serif;
  font-style: italic;
  font-size: 1.3rem;
  color: rgba(255,255,255,.7);
}

.scd-28__title {
  font-family: 'Instrument Serif', serif;
  font-size: 3rem;
  line-height: .92;
  color: #fff;
  letter-spacing: -.01em;
  text-shadow: 0 2px 20px rgba(0,0,0,.3);
}

.scd-28__title em {
  font-style: italic;
}

.scd-28__desc {
  font-size: .8rem;
  color: rgba(255,255,255,.78);
  line-height: 1.5;
  max-width: 24ch;
}

.scd-28__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.scd-28__cta {
  font-size: .78rem;
  color: #fff;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity .5s .1s, transform .5s .1s;
}

.scd-28__card:hover .scd-28__cta {
  opacity: 1;
  transform: translateY(0);
}

.scd-28__arrow {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(255,255,255,.2);
  display: grid;
  place-items: center;
  font-size: .8rem;
}

.scd-28__card--c1 .scd-28__grad {
  background: linear-gradient(135deg,#1e1b4b,#4338ca 40%,#6d28d9);
}

.scd-28__card--c2 .scd-28__grad {
  background: linear-gradient(135deg,#831843,#be185d 45%,#f43f5e);
}

.scd-28__card--c3 .scd-28__grad {
  background: linear-gradient(135deg,#064e3b,#0d9488 50%,#2dd4bf);
}

.scd-28__card--c4 .scd-28__grad {
  background: linear-gradient(135deg,#7c2d12,#ea580c 45%,#f59e0b);
}

.scd-28__card--c1 {
  transform: translateZ(0) translateY(0) rotate(-3deg);
  z-index: 4;
}

.scd-28__card--c2 {
  transform: translateZ(-40px) translateY(10px) rotate(2deg);
  z-index: 3;
  filter: brightness(.85);
}

.scd-28__card--c3 {
  transform: translateZ(-80px) translateY(20px) rotate(-2deg);
  z-index: 2;
  filter: brightness(.72);
}

.scd-28__card--c4 {
  transform: translateZ(-120px) translateY(30px) rotate(3deg);
  z-index: 1;
  filter: brightness(.6);
}
/* Stage-spread fan — only when no individual card is being hovered.
   Without the :not(:has(...:hover)) guard, hovering any single card
   fires BOTH this stage spread AND the per-card lift below. The two
   transforms fight on the same .8s cubic-bezier transition, sliding
   the card out from under the cursor mid-animation → cursor leaves
   the card → spread snaps back → cursor re-enters → infinite flicker.
   Restricting the spread to "stage hover AND nothing inside being
   hovered" lets the spread fan cleanly when you first enter the
   stage area, then freezes at the moment your cursor lands on a card. */

.scd-28__stage:hover:not(:has(.scd-28__card:hover)) .scd-28__card--c1 {
  transform: translate(-165px,-30px) translateZ(40px) rotate(-12deg);
  filter: brightness(1);
}

.scd-28__stage:hover:not(:has(.scd-28__card:hover)) .scd-28__card--c2 {
  transform: translate(-55px,18px) translateZ(20px) rotate(-4deg);
  filter: brightness(1);
}

.scd-28__stage:hover:not(:has(.scd-28__card:hover)) .scd-28__card--c3 {
  transform: translate(55px,18px) translateZ(20px) rotate(4deg);
  filter: brightness(1);
}

.scd-28__stage:hover:not(:has(.scd-28__card:hover)) .scd-28__card--c4 {
  transform: translate(165px,-30px) translateZ(40px) rotate(12deg);
  filter: brightness(1);
}
/* When a card IS being hovered, write each card's hovered transform
   explicitly — keeping its fanned x/y position AND adding the lift
   (translateZ + scale). This way the transform doesn't snap the card
   back to (0,0) which is what caused the flicker. */

.scd-28__stage:hover .scd-28__card--c1:hover {
  transform: translate(-165px,-56px) translateZ(90px) rotate(-12deg) scale(1.06);
  filter: brightness(1.05);
  z-index: 9;
}

.scd-28__stage:hover .scd-28__card--c2:hover {
  transform: translate(-55px,-8px) translateZ(90px) rotate(-4deg) scale(1.06);
  filter: brightness(1.05);
  z-index: 9;
}

.scd-28__stage:hover .scd-28__card--c3:hover {
  transform: translate(55px,-8px) translateZ(90px) rotate(4deg) scale(1.06);
  filter: brightness(1.05);
  z-index: 9;
}

.scd-28__stage:hover .scd-28__card--c4:hover {
  transform: translate(165px,-56px) translateZ(90px) rotate(12deg) scale(1.06);
  filter: brightness(1.05);
  z-index: 9;
}

.scd-28__card:hover {
  box-shadow: 0 50px 90px rgba(0,0,0,.65), 0 0 0 1px rgba(255,255,255,.18) inset, 0 0 40px rgba(255,255,255,.12);
}

.scd-28__floor {
  position: absolute;
  bottom: -70px;
  left: 50%;
  width: 240px;
  height: 40px;
  background: radial-gradient(ellipse, rgba(0,0,0,.6), transparent 70%);
  transform: translateX(-50%);
  filter: blur(8px);
}

@media (prefers-reduced-motion: reduce) {
  .scd-28::before,
    .scd-28__grad,
    .scd-28__sheen,
    .scd-28__deck,
    .scd-28__card,
    .scd-28__cta {
    animation: none !important;
    transition: none !important;
  }
}
```
