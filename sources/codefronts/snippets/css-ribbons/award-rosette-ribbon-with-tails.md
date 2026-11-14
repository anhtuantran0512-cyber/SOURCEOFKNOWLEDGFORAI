---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/award-rosette-ribbon-with-tails/"
title: "Award Rosette Ribbon with Tails"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "A proper rosette: a pleated scalloped disc built from a 24-point clip-path and a repeating-conic-gradient, with two ribbon tails dangling beneath and a slow…"
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Award Rosette Ribbon with Tails
Source: https://codefronts.com/snippets/css-ribbons/award-rosette-ribbon-with-tails/

A proper rosette: a pleated scalloped disc built from a 24-point clip-path and a repeating-conic-gradient, with two ribbon tails dangling beneath and a slow specular sweep across the metal. Every value is derived — the scallop polygon comes from trigonometry, the pleats from one repeating gradient — so it stays sharp at any size and weighs nothing.
## HTML
```html
<section class="rib-12" aria-label="Editors choice award rosette demo">
  <div class="rib-12__stage">
    <div class="rib-12__panel">
      <div class="rib-12__rosette" role="img" aria-label="Editor's Choice award, 2026, awarded by The Frontend Digest">
        <span class="rib-12__tail rib-12__tail--l"></span>
        <span class="rib-12__tail rib-12__tail--r"></span>
        <span class="rib-12__disc">
          <span class="rib-12__inner">
            <svg class="rib-12__star" viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" focusable="false"><path fill="currentColor" d="m12 2 2.9 6.26 6.85.74-5.1 4.6 1.42 6.72L12 17.02 5.93 20.3l1.42-6.71-5.1-4.6 6.85-.75L12 2Z"/></svg>
            <span class="rib-12__label">Editor's<br>Choice</span>
            <span class="rib-12__year">2026</span>
          </span>
        </span>
      </div>
      <div class="rib-12__copy">
        <p class="rib-12__eyebrow">Annual tooling awards</p>
        <h2 class="rib-12__title">Best developer experience, 2026</h2>
        <p class="rib-12__body">Judged across 240 submissions by a panel of nine engineers on setup time, documentation quality, escape hatches and long-term maintenance cost.</p>
        <p class="rib-12__quote">“The only entry where every reviewer shipped something real inside an hour.”</p>
        <div class="rib-12__by"><span class="rib-12__dot"></span>The Frontend Digest · November 2026</div>
      </div>
    </div>
    <p class="rib-12__chip" aria-hidden="true">24-point trig polygon · repeating-conic-gradient pleats · mirrored tails · drop-shadow</p>
  </div>
</section>
```
## CSS
```css
.rib-12,
.rib-12 *,
.rib-12 *::before,
.rib-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-12-bg: #10100e;
  --rib-12-bg: oklch(0.18 0.008 90);
  --rib-12-panel: #1a1a16;
  --rib-12-panel: oklch(0.23 0.01 90);
  --rib-12-ink: #f6f3ea;
  --rib-12-ink: oklch(0.97 0.012 90);
  --rib-12-mut: #a49d90;
  --rib-12-mut: oklch(0.71 0.018 88);
  --rib-12-hue: 86;
  --rib-12-hi: #f0cf7a;
  --rib-12-hi: oklch(0.88 0.13 var(--rib-12-hue));
  --rib-12-lo: #b48a34;
  --rib-12-lo: oklch(0.68 0.13 var(--rib-12-hue));
  --rib-12-deep: #7a5a19;
  --rib-12-deep: oklch(0.5 0.11 var(--rib-12-hue));
  --rib-12-size: clamp(150px,26vw,208px);
  --rib-12-tail: clamp(86px,15vw,116px);
  background: var(--rib-12-bg);
  color: var(--rib-12-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,28px);
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 30% 30%,color-mix(in oklch,var(--rib-12-hi) 12%,transparent),transparent 70%);
}

.rib-12__panel {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: clamp(24px,5vw,48px);
  width: min(100%,860px);
  padding: clamp(26px,5vw,46px);
  border-radius: 26px;
  background: var(--rib-12-panel);
  border: 1px solid oklch(1 0 0/.08);
  box-shadow: 0 40px 90px -44px oklch(0 0 0/.9);
}

.rib-12__rosette {
  position: relative;
  flex: none;
  inline-size: var(--rib-12-size);
  display: grid;
  place-items: center;
  padding-block-end: calc(var(--rib-12-tail) * .62);
  filter: drop-shadow(0 18px 26px oklch(0 0 0/.6));
}

.rib-12__tail {
  position: absolute;
  inset-block-start: 52%;
  inline-size: calc(var(--rib-12-size) * .3);
  block-size: var(--rib-12-tail);
  background: #b48a34;
  background: linear-gradient(100deg,var(--rib-12-deep),var(--rib-12-lo) 45%,var(--rib-12-deep));
  clip-path: polygon(0 0,100% 0,100% 100%,50% 74%,0 100%);
  z-index: 0;
}

.rib-12__tail--l {
  inset-inline-start: calc(50% - var(--rib-12-size) * .3);
  rotate: 11deg;
  transform-origin: top center;
}

.rib-12__tail--r {
  inset-inline-start: calc(50%);
  rotate: -11deg;
  transform-origin: top center;
}

.rib-12__disc {
  position: relative;
  z-index: 1;
  inline-size: var(--rib-12-size);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  background: #b48a34;
  background: repeating-conic-gradient(from -7.5deg,var(--rib-12-hi) 0deg 15deg,var(--rib-12-lo) 15deg 30deg);
  clip-path: polygon(50% 0%,61.4% 7.5%,75% 6.7%,81.1% 18.9%,93.3% 25%,92.5% 38.6%,100% 50%,92.5% 61.4%,93.3% 75%,81.1% 81.1%,75% 93.3%,61.4% 92.5%,50% 100%,38.6% 92.5%,25% 93.3%,18.9% 81.1%,6.7% 75%,7.5% 61.4%,0% 50%,7.5% 38.6%,6.7% 25%,18.9% 18.9%,25% 6.7%,38.6% 7.5%);
}

.rib-12__inner {
  inline-size: 72%;
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 3px;
  border-radius: 50%;
  background: radial-gradient(circle at 34% 28%,color-mix(in oklch,var(--rib-12-hi) 100%,white 24%),var(--rib-12-lo) 62%,var(--rib-12-deep));
  box-shadow: inset 0 2px 4px oklch(1 0 0/.5),inset 0 -3px 8px oklch(0 0 0/.35),0 0 0 3px color-mix(in oklch,var(--rib-12-deep) 70%,transparent);
  color: oklch(0.28 0.06 var(--rib-12-hue));
  text-align: center;
  overflow: hidden;
}

.rib-12__inner::after {
  content: '';
  position: absolute;
  inline-size: 200%;
  block-size: 36%;
  background: linear-gradient(100deg,transparent 20%,oklch(1 0 0/.55) 50%,transparent 78%);
  rotate: -24deg;
  animation: rib-12-sweep 5.5s cubic-bezier(.5,0,.5,1) infinite;
}

@keyframes rib-12-sweep {
  0%,
    72% {
    translate: -70% 0;
    opacity: 0;
  }

  80% {
    opacity: .9;
  }

  100% {
    translate: 70% 0;
    opacity: 0;
  }
}

.rib-12__star {
  color: oklch(0.32 0.08 var(--rib-12-hue));
  filter: drop-shadow(0 1px 0 oklch(1 0 0/.4));
}

.rib-12__label {
  font-size: clamp(13px,2.6vw,16px);
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: .02em;
  text-transform: uppercase;
  text-shadow: 0 1px 0 oklch(1 0 0/.35);
}

.rib-12__year {
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .2em;
  opacity: .78;
  font-variant-numeric: tabular-nums;
}

.rib-12__copy {
  flex: 1 1 300px;
  display: grid;
  gap: 11px;
}

.rib-12__eyebrow {
  font-size: 11.5px;
  font-weight: 750;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--rib-12-hi);
}

.rib-12__title {
  font-size: clamp(24px,4.2vw,34px);
  font-weight: 660;
  letter-spacing: -.032em;
  line-height: 1.14;
  text-wrap: balance;
}

.rib-12__body {
  font-size: 14.5px;
  line-height: 1.62;
  color: var(--rib-12-mut);
  text-wrap: pretty;
}

.rib-12__quote {
  margin-block-start: 4px;
  padding-inline-start: 14px;
  border-inline-start: 2px solid color-mix(in oklch,var(--rib-12-hi) 55%,transparent);
  font-size: 15px;
  line-height: 1.5;
  font-style: italic;
  color: var(--rib-12-ink);
}

.rib-12__by {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 12.5px;
  color: var(--rib-12-mut);
}

.rib-12__dot {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: var(--rib-12-hi);
}

.rib-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-12-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-12 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```
