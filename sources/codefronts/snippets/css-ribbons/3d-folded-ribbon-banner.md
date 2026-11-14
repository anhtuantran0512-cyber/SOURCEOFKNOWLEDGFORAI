---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/3d-folded-ribbon-banner/"
title: "3D Folded Ribbon Banner"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "Paper physics, built rather than drawn."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Folded Ribbon Banner
Source: https://codefronts.com/snippets/css-ribbons/3d-folded-ribbon-banner/

Paper physics, built rather than drawn. The ribbon is five real facets in one preserve-3d space — a flat face, two wings creased back on the Y axis, and two tails folded down on the X axis — so the ends genuinely turn away from the camera instead of being triangles pointing at it. Each facet is lit by the same light source, its value derived from the accent with color-mix(), and a blurred contact shadow plants the whole strip on the card. It unfolds on load from a hinge at its pinned edge and settles at three degrees, never quite flat.
## HTML
```html
<section class="rib-14" aria-label="3D folded ribbon header banner demo">
  <div class="rib-14__stage">
    <div class="rib-14__card">
      <div class="rib-14__bannerwrap">
        <div class="rib-14__banner">
          <span class="rib-14__wing rib-14__wing--l" aria-hidden="true"><span class="rib-14__tail"></span></span>
          <div class="rib-14__face">
            <h2 class="rib-14__title">Workshop Series 2026</h2>
            <p class="rib-14__sub">Six Saturdays · Berlin &amp; remote</p>
          </div>
          <span class="rib-14__wing rib-14__wing--r" aria-hidden="true"><span class="rib-14__tail"></span></span>
        </div>
      </div>
      <div class="rib-14__body">
        <p class="rib-14__lede">A hands-on programme for engineers who want to stop fighting their stylesheets. Small cohorts, real codebases, no slides after lunch.</p>
        <ul class="rib-14__list">
          <li><span class="rib-14__no">01</span><span><strong>Cascade layers in anger</strong> — untangling a ten-year-old theme without a rewrite.</span></li>
          <li><span class="rib-14__no">02</span><span><strong>Container-first components</strong> — building once, placing anywhere.</span></li>
          <li><span class="rib-14__no">03</span><span><strong>Motion that respects people</strong> — reduced-motion as a design constraint.</span></li>
        </ul>
        <div class="rib-14__foot">
          <button class="rib-14__cta" type="button">Reserve a seat</button>
          <p class="rib-14__seats">14 of 60 seats left · €480 incl. VAT</p>
        </div>
      </div>
    </div>
    <p class="rib-14__chip" aria-hidden="true">preserve-3d facets · rotateY creases · composed double fold · color-mix facet shading</p>
  </div>
</section>
```
## CSS
```css
.rib-14,
.rib-14 *,
.rib-14 *::before,
.rib-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-14-bg: #e9e5dc;
  --rib-14-bg: oklch(0.93 0.012 85);
  --rib-14-card: #fffdf8;
  --rib-14-card: oklch(0.99 0.008 88);
  --rib-14-ink: #241f18;
  --rib-14-ink: oklch(0.25 0.016 70);
  --rib-14-mut: #6d6357;
  --rib-14-mut: oklch(0.54 0.018 74);
  --rib-14-acc: #1f5f52;
  --rib-14-acc: oklch(0.45 0.09 175);
  --rib-14-wing: clamp(40px,7.5vw,86px);
  --rib-14-tail: clamp(20px,3.4vw,34px);
  --rib-14-turn: 58deg;
  --rib-14-depth: 38px;
  --rib-14-crease: oklch(0.20 0.04 175/.55);
  background: var(--rib-14-bg);
  color: var(--rib-14-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,3vw,26px);
  padding: clamp(24px,5vw,56px);
}

.rib-14__card {
  position: relative;
  width: min(100%,700px);
  border-radius: 22px;
  background: var(--rib-14-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 60px -30px oklch(0.3 0.03 70/.55);
}

.rib-14__bannerwrap {
  position: relative;
  padding-block-start: clamp(34px,5.4vw,52px);
  padding-inline: clamp(10px,2.4vw,26px);
  padding-block-end: calc(var(--rib-14-tail) + clamp(18px,2.8vw,30px));
  perspective: 760px;
  perspective-origin: 50% 34%;
}

.rib-14__banner {
  position: relative;
  display: flex;
  align-items: stretch;
  justify-content: center;
  transform-style: preserve-3d;
  transform-origin: 50% 0;
  transform: rotateX(9deg);
  animation: rib-14-unfold 1.05s cubic-bezier(.16,1,.3,1) both;
}

@keyframes rib-14-unfold {
  from {
    transform: rotateX(-86deg);
    opacity: 0;
  }

  to {
    transform: rotateX(9deg);
    opacity: 1;
  }
}

.rib-14__face {
  position: relative;
  z-index: 2;
  flex: 0 1 auto;
  min-inline-size: min(70%,430px);
  display: grid;
  gap: 5px;
  align-content: center;
  padding: clamp(18px,3.4vw,26px) clamp(24px,4.6vw,44px);
  text-align: center;
  color: oklch(0.98 0.01 175);
  transform: translateZ(var(--rib-14-depth));
  background: #1f5f52;
  background: linear-gradient(168deg,color-mix(in oklch,var(--rib-14-acc) 100%,white 26%) 0%,color-mix(in oklch,var(--rib-14-acc) 100%,white 8%) 34%,var(--rib-14-acc) 68%,color-mix(in oklch,var(--rib-14-acc) 90%,black 10%) 100%);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.34),inset 0 -1px 0 oklch(0 0 0/.18),0 22px 28px -20px oklch(0.28 0.05 175/.55),6px 0 14px -6px oklch(0.16 0.04 175/.7),-6px 0 14px -6px oklch(0.16 0.04 175/.7);
}

.rib-14__title {
  font-size: clamp(20px,4vw,30px);
  font-weight: 700;
  letter-spacing: -.028em;
  line-height: 1.1;
  text-wrap: balance;
  backface-visibility: hidden;
}

.rib-14__sub {
  font-size: 13px;
  letter-spacing: .06em;
  opacity: .85;
}

.rib-14__wing {
  position: relative;
  flex: 0 0 var(--rib-14-wing);
  margin-block-start: clamp(9px,1.8vw,15px);
  margin-block-end: calc(var(--rib-14-tail) * -0.55);
  transform-style: preserve-3d;
  background: #1a5148;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-14-acc) 58%,black) 0%,color-mix(in oklch,var(--rib-14-acc) 34%,black) 100%);
}

.rib-14__wing--l {
  transform-origin: 100% 50%;
  transform: rotateY(var(--rib-14-turn));
}

.rib-14__wing--l::before {
  content: '';
  position: absolute;
  inset-block: 0;
  inset-inline-end: 0;
  inline-size: 2px;
  background: linear-gradient(180deg,oklch(1 0 0/.30),oklch(1 0 0/.06));
  z-index: 3;
}

.rib-14__wing--r {
  transform-origin: 0 50%;
  transform: rotateY(calc(var(--rib-14-turn) * -1));
}

.rib-14__wing--r::before {
  content: '';
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 2px;
  background: linear-gradient(180deg,oklch(1 0 0/.30),oklch(1 0 0/.06));
  z-index: 3;
}

.rib-14__tail {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  block-size: var(--rib-14-tail);
  transform-origin: 50% 0;
  transform: rotateX(62deg);
  background: #164740;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-14-acc) 70%,black) 0%,color-mix(in oklch,var(--rib-14-acc) 54%,black) 100%);
  clip-path: polygon(0 0,100% 0,100% 100%,50% 40%,0 100%);
}

.rib-14__bannerwrap::after {
  content: '';
  position: absolute;
  z-index: 0;
  inset-inline: clamp(58px,13vw,130px);
  inset-block-end: clamp(6px,1.4vw,14px);
  block-size: 18px;
  border-radius: 50%;
  background: oklch(0.26 0.05 175/.46);
  filter: blur(12px);
}

.rib-14__body {
  display: grid;
  gap: clamp(14px,2.6vw,20px);
  padding: clamp(24px,4.4vw,36px);
}

.rib-14__lede {
  font-size: clamp(14.5px,2.5vw,16.5px);
  line-height: 1.62;
  color: var(--rib-14-mut);
  text-wrap: pretty;
}

.rib-14__list {
  display: grid;
  gap: 12px;
  list-style: none;
  padding: 0;
}

.rib-14__list li {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  font-size: 14px;
  line-height: 1.5;
  padding-block-end: 12px;
  border-block-end: 1px solid oklch(0 0 0/.07);
}

.rib-14__list li:last-child {
  border-block-end: 0;
  padding-block-end: 0;
}

.rib-14__no {
  flex: none;
  inline-size: 30px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--rib-14-acc);
  padding-block-start: 2px;
}

.rib-14__list strong {
  font-weight: 680;
}

.rib-14__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px;
}

.rib-14__cta {
  min-height: 48px;
  padding-inline: 24px;
  border: 0;
  border-radius: 12px;
  background: var(--rib-14-acc);
  color: oklch(0.99 0.01 175);
  font: inherit;
  font-size: 15px;
  font-weight: 660;
  cursor: pointer;
  transition: filter .25s,translate .2s;
}

.rib-14__cta:hover {
  filter: brightness(1.1);
  translate: 0 -1px;
}

.rib-14__cta:focus-visible {
  outline: 3px solid var(--rib-14-ink);
  outline-offset: 3px;
}

.rib-14__seats {
  font-size: 12.5px;
  color: var(--rib-14-mut);
  font-variant-numeric: tabular-nums;
}

.rib-14__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-14-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-14__banner {
    animation: none;
  }

  .rib-14 * {
    transition-duration: .01ms !important;
  }
}
```
