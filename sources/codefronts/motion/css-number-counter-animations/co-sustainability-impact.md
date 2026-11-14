---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/co-sustainability-impact/"
title: "ESG Impact & Carbon Footprint Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "An impact panel for sustainability reports: tonnes of CO₂ avoided, litres of water saved, trees planted — each counting up in pure CSS, each with its own…"
has_js: "false"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: ESG Impact & Carbon Footprint Counter
Source: https://codefronts.com/motion/css-number-counter-animations/co-sustainability-impact/

An impact panel for sustainability reports: tonnes of CO₂ avoided, litres of water saved, trees planted — each counting up in pure CSS, each with its own hand-drawn-feel progress arc, on a calm paper-and-moss palette that deliberately avoids the neon-dashboard look these numbers are usually trapped in.
## HTML
```html
<section class="cnc-15" aria-label="ESG impact and carbon footprint counter demo">
  <div class="cnc-15__stage">
    <header class="cnc-15__head">
      <p class="cnc-15__eyebrow">Impact report · FY2026</p>
      <h2 class="cnc-15__title">Measured, verified, reduced</h2>
    </header>
    <div class="cnc-15__grid">
      <article class="cnc-15__tile" style="--cnc-15-hue:150">
        <div class="cnc-15__dial" aria-hidden="true"><span class="cnc-15__arc cnc-15__arc--a"></span></div>
        <p class="cnc-15__val"><span class="cnc-15__n cnc-15__n--a" aria-hidden="true"></span><span class="cnc-15__unit">t</span></p>
        <h3 class="cnc-15__key">CO₂e avoided</h3>
        <p class="cnc-15__note">vs. 2019 baseline, Scope 1 + 2, third-party assured</p>
        <p class="cnc-15__sr">1,284 tonnes of CO2 equivalent avoided</p>
      </article>
      <article class="cnc-15__tile" style="--cnc-15-hue:220">
        <div class="cnc-15__dial" aria-hidden="true"><span class="cnc-15__arc cnc-15__arc--b"></span></div>
        <p class="cnc-15__val"><span class="cnc-15__n cnc-15__n--b" aria-hidden="true"></span><span class="cnc-15__unit">ML</span></p>
        <h3 class="cnc-15__key">Water returned</h3>
        <p class="cnc-15__note">Megalitres replenished across 6 watersheds</p>
        <p class="cnc-15__sr">96 megalitres of water returned</p>
      </article>
      <article class="cnc-15__tile" style="--cnc-15-hue:95">
        <div class="cnc-15__dial" aria-hidden="true"><span class="cnc-15__arc cnc-15__arc--c"></span></div>
        <p class="cnc-15__val"><span class="cnc-15__n cnc-15__n--c" aria-hidden="true"></span><span class="cnc-15__unit">k</span></p>
        <h3 class="cnc-15__key">Native trees planted</h3>
        <p class="cnc-15__note">Survival-audited at 24 months, 91% rate</p>
        <p class="cnc-15__sr">48 thousand native trees planted</p>
      </article>
    </div>
    <p class="cnc-15__chip" aria-hidden="true">3 registered properties · counter() text · masked conic arcs · zero JavaScript</p>
  </div>
</section>
```
## CSS
```css
@property --cnc-15-a {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --cnc-15-b {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --cnc-15-c {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --cnc-15-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.cnc-15,
.cnc-15 *,
.cnc-15 *::before,
.cnc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-15-bg: oklch(0.95 0.02 110);
  --cnc-15-card: oklch(0.99 0.008 105);
  --cnc-15-ink: oklch(0.28 0.04 140);
  --cnc-15-mut: oklch(0.55 0.03 140);
  background: var(--cnc-15-bg);
  color: var(--cnc-15-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(18px,4vw,52px);
  background: radial-gradient(80% 60% at 50% 0%,oklch(0.92 0.05 130/.9),transparent 70%);
}

.cnc-15__head {
  text-align: center;
}

.cnc-15__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: oklch(0.55 0.12 145);
}

.cnc-15__title {
  margin-top: 8px;
  font-size: clamp(24px,4vw,36px);
  font-weight: 640;
  letter-spacing: -.03em;
}

.cnc-15__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(216px,1fr));
  gap: 16px;
  width: min(100%,880px);
}

.cnc-15__tile {
  --cnc-15-acc: oklch(0.6 0.14 var(--cnc-15-hue,150));
  display: grid;
  justify-items: center;
  gap: 6px;
  padding: 26px 20px 22px;
  border-radius: 20px;
  text-align: center;
  background: var(--cnc-15-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.04),0 18px 40px oklch(0.4 0.06 140/.12);
}

.cnc-15__dial {
  position: relative;
  width: 92px;
  height: 56px;
  margin-bottom: 6px;
  overflow: hidden;
}

.cnc-15__dial::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 92px;
  height: 92px;
  border-radius: 50%;
  border: 9px solid color-mix(in oklch,var(--cnc-15-acc) 14%,transparent);
  rotate: -120deg;
  clip-path: polygon(0 0,100% 0,100% 62%,0 62%);
}

.cnc-15__arc {
  position: absolute;
  left: 0;
  top: 0;
  width: 92px;
  height: 92px;
  border-radius: 50%;
  border: 9px solid var(--cnc-15-acc);
  rotate: -120deg;
  -webkit-mask: conic-gradient(#000 calc(var(--cnc-15-p) * 240deg),transparent 0);
  mask: conic-gradient(#000 calc(var(--cnc-15-p) * 240deg),transparent 0);
}

.cnc-15__val {
  display: flex;
  align-items: baseline;
  gap: 3px;
  margin-top: 4px;
  font-size: clamp(32px,5vw,42px);
  font-weight: 730;
  letter-spacing: -.045em;
  line-height: 1;
  color: var(--cnc-15-acc);
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-15__unit {
  font-size: .42em;
  font-weight: 660;
  letter-spacing: 0;
}

.cnc-15__key {
  font-size: 14.5px;
  font-weight: 640;
  letter-spacing: -.01em;
  margin-top: 8px;
}

.cnc-15__note {
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--cnc-15-mut);
  text-wrap: pretty;
  max-width: 26ch;
}

.cnc-15__n--a {
  counter-reset: cnc-15-a var(--cnc-15-a);
  animation: cnc-15-ka 2.4s cubic-bezier(.16,1,.3,1) both;
}

.cnc-15__n--a::after {
  content: counter(cnc-15-a);
}

.cnc-15__n--b {
  counter-reset: cnc-15-b var(--cnc-15-b);
  animation: cnc-15-kb 2.4s cubic-bezier(.16,1,.3,1) .12s both;
}

.cnc-15__n--b::after {
  content: counter(cnc-15-b);
}

.cnc-15__n--c {
  counter-reset: cnc-15-c var(--cnc-15-c);
  animation: cnc-15-kc 2.4s cubic-bezier(.16,1,.3,1) .24s both;
}

.cnc-15__n--c::after {
  content: counter(cnc-15-c);
}

@keyframes cnc-15-ka {
  to {
    --cnc-15-a: 1284;
  }
}

@keyframes cnc-15-kb {
  to {
    --cnc-15-b: 96;
  }
}

@keyframes cnc-15-kc {
  to {
    --cnc-15-c: 48;
  }
}

.cnc-15__arc--a {
  animation: cnc-15-pa 2.4s cubic-bezier(.16,1,.3,1) both;
}

.cnc-15__arc--b {
  animation: cnc-15-pb 2.4s cubic-bezier(.16,1,.3,1) .12s both;
}

.cnc-15__arc--c {
  animation: cnc-15-pc 2.4s cubic-bezier(.16,1,.3,1) .24s both;
}

@keyframes cnc-15-pa {
  to {
    --cnc-15-p: .82;
  }
}

@keyframes cnc-15-pb {
  to {
    --cnc-15-p: .64;
  }
}

@keyframes cnc-15-pc {
  to {
    --cnc-15-p: .91;
  }
}

.cnc-15__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-15-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,560px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-15__n--a,
    .cnc-15__n--b,
    .cnc-15__n--c,
    .cnc-15__arc {
    animation-duration: 1ms !important;
  }
}
```
