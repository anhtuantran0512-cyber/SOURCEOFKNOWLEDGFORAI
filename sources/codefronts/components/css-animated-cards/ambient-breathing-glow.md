---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/ambient-breathing-glow/"
title: "Ambient Breathing Glow"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The featured-plan card that genuinely breathes."
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ambient Breathing Glow
Source: https://codefronts.com/components/css-animated-cards/ambient-breathing-glow/

The featured-plan card that genuinely breathes. Two counter-phased auras swell and fade on different periods so the light never looks like a single lamp switching on and off; a conic halo travels around the panel edge; a registered hue property sweeps the whole palette 46 degrees, violet through magenta and back; the rim, the crown, the badge and the feature pips all pulse on the same 6-second clock at staggered phases. Everything animated is composited &mdash; opacity, scale and one custom property &mdash; and a veil layer keeps the copy at full contrast on the brightest frame.
## HTML
```html
<section class="ac-15" aria-label="Ambient breathing glow card demo">
  <div class="ac-15__stage">
    <div class="ac-15__row">
      <article class="ac-15__card">
        <p class="ac-15__plan">Starter</p>
        <p class="ac-15__price">$0<span>/mo</span></p>
        <ul class="ac-15__list" role="list"><li>3 projects</li><li>Community support</li><li>1 GB storage</li></ul>
        <button class="ac-15__cta" type="button">Choose Starter</button>
      </article>
      <article class="ac-15__card ac-15__card--hero">
        <span class="ac-15__halo" aria-hidden="true"></span>
        <span class="ac-15__aura ac-15__aura--a" aria-hidden="true"></span>
        <span class="ac-15__aura ac-15__aura--b" aria-hidden="true"></span>
        <span class="ac-15__crown" aria-hidden="true"></span>
        <span class="ac-15__veil" aria-hidden="true"></span>
        <span class="ac-15__sheen" aria-hidden="true"></span>
        <span class="ac-15__flag">Most popular</span>
        <div class="ac-15__inner">
          <p class="ac-15__plan">Studio</p>
          <p class="ac-15__price">$24<span>/mo</span></p>
          <ul class="ac-15__list ac-15__list--lit" role="list"><li>Unlimited projects</li><li>Priority support &middot; 4 hr SLA</li><li>250 GB storage</li><li>Custom domains</li></ul>
          <button class="ac-15__cta ac-15__cta--go" type="button">Choose Studio<span class="ac-15__ctaglow" aria-hidden="true"></span></button>
        </div>
      </article>
      <article class="ac-15__card">
        <p class="ac-15__plan">Scale</p>
        <p class="ac-15__price">$96<span>/mo</span></p>
        <ul class="ac-15__list" role="list"><li>Everything in Studio</li><li>SSO &amp; audit log</li><li>2 TB storage</li></ul>
        <button class="ac-15__cta" type="button">Choose Scale</button>
      </article>
    </div>
    <p class="ac-15__chip" aria-hidden="true">counter-phase auras &middot; @property hue drift &middot; rotating conic halo &middot; phase-lagged rim &middot; 6 s &asymp; resting breath</p>
  </div>
</section>
```
## CSS
```css
@property --ac-15-h {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

@property --ac-15-spin {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.ac-15,
.ac-15 *,
.ac-15 *::before,
.ac-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-15-bg: oklch(0.13 0.018 288);
  --ac-15-card: oklch(0.185 0.02 288);
  --ac-15-ink: oklch(0.97 0.004 280);
  --ac-15-mut: oklch(0.70 0.02 288);
  --ac-15-acc: oklch(0.76 0.19 308);
  --ac-15-acc2: oklch(0.82 0.15 214);
  --ac-15-line: oklch(1 0 0/.10);
  --ac-15-live: var(--ac-15-acc);
  --ac-15-live2: var(--ac-15-acc2);
  background: var(--ac-15-bg);
  color: var(--ac-15-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(120% 80% at 50% 42%,color-mix(in oklch,var(--ac-15-acc) 9%,transparent),transparent 68%);
}

.ac-15__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 16px;
  align-items: center;
  width: min(100%,900px);
}

.ac-15__card {
  position: relative;
  display: grid;
  gap: 13px;
  padding: 24px 22px;
  border: 1px solid var(--ac-15-line);
  border-radius: 22px;
  background: var(--ac-15-card);
}

.ac-15__card--hero {
  padding: 0;
  border-color: color-mix(in oklch,var(--ac-15-live) 46%,transparent);
  background: linear-gradient(180deg,color-mix(in oklch,var(--ac-15-live) 13%,var(--ac-15-card)),var(--ac-15-card) 62%);
  isolation: isolate;
  --ac-15-live: oklch(0.76 0.19 calc(308 + var(--ac-15-h)));
  --ac-15-live2: oklch(0.82 0.15 calc(214 + var(--ac-15-h)));
  animation: ac-15-hue 12s ease-in-out infinite;
}

.ac-15__inner {
  display: grid;
  gap: 13px;
  padding: 30px 24px;
  position: relative;
  z-index: 2;
}

@keyframes ac-15-hue {
  0%,
    100% {
    --ac-15-h: -16;
  }

  50% {
    --ac-15-h: 30;
  }
}

.ac-15__halo {
  position: absolute;
  inset: -16px;
  z-index: -3;
  border-radius: 32px;
  pointer-events: none;
  background: conic-gradient(from var(--ac-15-spin),transparent 0 48%,color-mix(in oklch,var(--ac-15-live) 90%,transparent) 68%,var(--ac-15-live2) 82%,transparent 96%);
  filter: blur(13px);
  opacity: .85;
  animation: ac-15-spin 13s linear infinite,ac-15-halo 6s ease-in-out infinite;
}

@keyframes ac-15-spin {
  to {
    --ac-15-spin: 360deg;
  }
}

@keyframes ac-15-halo {
  0%,
    100% {
    opacity: .45;
  }

  50% {
    opacity: 1;
  }
}

.ac-15__aura {
  position: absolute;
  z-index: -2;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(34px);
  will-change: transform,opacity;
}

.ac-15__aura--a {
  inset: -42% -30%;
  background: radial-gradient(closest-side,color-mix(in oklch,var(--ac-15-live) 78%,transparent),transparent 74%);
  animation: ac-15-breathe 6s ease-in-out infinite;
}

.ac-15__aura--b {
  inset: -24% -46% -50% -20%;
  background: radial-gradient(closest-side,color-mix(in oklch,var(--ac-15-live2) 62%,transparent),transparent 76%);
  animation: ac-15-breathe-b 8.5s ease-in-out infinite;
}

@keyframes ac-15-breathe {
  0%,
    100% {
    opacity: .34;
    scale: .9;
  }

  50% {
    opacity: .92;
    scale: 1.1;
  }
}

@keyframes ac-15-breathe-b {
  0%,
    100% {
    opacity: .62;
    scale: 1.08;
    translate: 0 0;
  }

  50% {
    opacity: .22;
    scale: .88;
    translate: 0 -6%;
  }
}

.ac-15__crown {
  position: absolute;
  inset: 1px 1px auto;
  height: 56%;
  z-index: -1;
  border-radius: 21px 21px 0 0;
  pointer-events: none;
  background: radial-gradient(120% 100% at 50% 0%,color-mix(in oklch,var(--ac-15-live) 46%,transparent),transparent 70%);
  animation: ac-15-crown 6s ease-in-out infinite;
}

@keyframes ac-15-crown {
  0%,
    100% {
    opacity: .28;
  }

  50% {
    opacity: .8;
  }
}

.ac-15__veil {
  position: absolute;
  inset: 1px;
  z-index: 1;
  border-radius: 21px;
  pointer-events: none;
  background: linear-gradient(180deg,color-mix(in oklch,var(--ac-15-card) 62%,transparent),color-mix(in oklch,var(--ac-15-card) 88%,transparent) 58%);
}

.ac-15__sheen {
  position: absolute;
  inset: 1px;
  z-index: 3;
  border-radius: 21px;
  overflow: hidden;
  pointer-events: none;
}

.ac-15__sheen::before {
  content: '';
  position: absolute;
  inset: -40% -60%;
  background: linear-gradient(104deg,transparent 42%,oklch(1 0 0/.16) 50%,transparent 58%);
  translate: -120% 0;
  animation: ac-15-sheen 9s cubic-bezier(.4,0,.3,1) infinite;
}

@keyframes ac-15-sheen {
  0% {
    translate: -120% 0;
  }

  26% {
    translate: 120% 0;
  }

  100% {
    translate: 120% 0;
  }
}

.ac-15__card--hero::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 4;
  pointer-events: none;
  border-radius: 22px;
  box-shadow: inset 0 0 0 1px color-mix(in oklch,var(--ac-15-live) 85%,transparent),inset 0 1px 0 0 oklch(1 0 0/.22);
  opacity: .3;
  animation: ac-15-rim 6s ease-in-out .9s infinite;
}

@keyframes ac-15-rim {
  0%,
    100% {
    opacity: .22;
  }

  50% {
    opacity: .85;
  }
}

.ac-15__flag {
  position: absolute;
  top: -11px;
  left: 50%;
  translate: -50% 0;
  z-index: 5;
  padding: 5px 13px;
  border-radius: 99px;
  background: var(--ac-15-live);
  color: oklch(0.14 0.02 300);
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .09em;
  text-transform: uppercase;
  white-space: nowrap;
  box-shadow: 0 6px 20px -6px color-mix(in oklch,var(--ac-15-live) 90%,transparent);
  animation: ac-15-flag 6s ease-in-out infinite;
}

@keyframes ac-15-flag {
  0%,
    100% {
    translate: -50% 0;
    box-shadow: 0 6px 20px -8px color-mix(in oklch,var(--ac-15-live) 70%,transparent);
  }

  50% {
    translate: -50% -2px;
    box-shadow: 0 10px 28px -6px color-mix(in oklch,var(--ac-15-live) 100%,transparent);
  }
}

.ac-15__plan {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--ac-15-mut);
}

.ac-15__card--hero .ac-15__plan {
  color: var(--ac-15-live);
}

.ac-15__price {
  font-size: clamp(32px,4vw,42px);
  font-weight: 700;
  letter-spacing: -.045em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.ac-15__price span {
  font-size: .36em;
  font-weight: 600;
  color: var(--ac-15-mut);
  letter-spacing: 0;
}

.ac-15__list {
  display: grid;
  gap: 9px;
  list-style: none;
  font-size: 13.5px;
  color: var(--ac-15-mut);
  line-height: 1.4;
}

.ac-15__list li {
  display: flex;
  gap: 9px;
  align-items: flex-start;
}

.ac-15__list li::before {
  content: '';
  flex: none;
  width: 15px;
  height: 15px;
  margin-top: 1px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--ac-15-acc) 22%,transparent);
  box-shadow: inset 0 0 0 1.5px color-mix(in oklch,var(--ac-15-acc) 55%,transparent);
}

.ac-15__list--lit li::before {
  background: color-mix(in oklch,var(--ac-15-live) 30%,transparent);
  box-shadow: inset 0 0 0 1.5px color-mix(in oklch,var(--ac-15-live) 75%,transparent);
  animation: ac-15-pip 6s ease-in-out infinite;
  animation-delay: calc(var(--ac-15-p,0) * .5s);
}

.ac-15__list--lit li:nth-child(2)::before {
  --ac-15-p: 1;
}

.ac-15__list--lit li:nth-child(3)::before {
  --ac-15-p: 2;
}

.ac-15__list--lit li:nth-child(4)::before {
  --ac-15-p: 3;
}

@keyframes ac-15-pip {
  0%,
    100% {
    opacity: .55;
    box-shadow: inset 0 0 0 1.5px color-mix(in oklch,var(--ac-15-live) 55%,transparent);
  }

  50% {
    opacity: 1;
    box-shadow: inset 0 0 0 1.5px color-mix(in oklch,var(--ac-15-live) 95%,transparent),0 0 12px -2px color-mix(in oklch,var(--ac-15-live) 80%,transparent);
  }
}

.ac-15__cta {
  min-height: 46px;
  margin-top: 6px;
  padding: 0 18px;
  border: 1px solid var(--ac-15-line);
  border-radius: 13px;
  background: oklch(1 0 0/.05);
  color: var(--ac-15-ink);
  font-size: 14px;
  font-weight: 640;
  font-family: inherit;
  cursor: pointer;
  transition: background .22s,transform .22s,border-color .22s;
}

.ac-15__cta:hover {
  background: oklch(1 0 0/.1);
  transform: translateY(-1px);
}

.ac-15__cta:focus-visible {
  outline: 2px solid var(--ac-15-live);
  outline-offset: 3px;
}

.ac-15__cta--go {
  position: relative;
  overflow: hidden;
  background: var(--ac-15-live);
  border-color: transparent;
  color: oklch(0.14 0.02 300);
}

.ac-15__cta--go:hover {
  background: color-mix(in oklch,var(--ac-15-live) 88%,oklch(1 0 0));
}

.ac-15__ctaglow {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(60% 140% at 50% 120%,oklch(1 0 0/.55),transparent 70%);
  opacity: .3;
  animation: ac-15-ctaglow 6s ease-in-out infinite;
}

@keyframes ac-15-ctaglow {
  0%,
    100% {
    opacity: .18;
  }

  50% {
    opacity: .6;
  }
}

.ac-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-15-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-15-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,760px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-15 *,
    .ac-15 *::before,
    .ac-15 *::after {
    animation: none !important;
  }

  .ac-15__halo {
    opacity: .7;
  }

  .ac-15__aura--a {
    opacity: .7;
  }

  .ac-15__aura--b {
    opacity: .45;
  }

  .ac-15__crown {
    opacity: .55;
  }

  .ac-15__card--hero::after {
    opacity: .6;
  }

  .ac-15__ctaglow {
    opacity: .4;
  }

  .ac-15__sheen {
    display: none;
  }

  .ac-15__cta {
    transition: none;
  }
}
```
