---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/count-up-kpi-metrics-card/"
title: "Count-Up KPI Metrics Card"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Dashboard KPI tiles whose numbers genuinely interpolate — no JavaScript, no requestAnimationFrame loop."
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Count-Up KPI Metrics Card
Source: https://codefronts.com/components/css-animated-cards/count-up-kpi-metrics-card/

Dashboard KPI tiles whose numbers genuinely interpolate — no JavaScript, no requestAnimationFrame loop. A registered @property integer is animated by the style engine and printed through counter(), the delta chips slide in behind it, and the whole row cascades. This is the pure-CSS counter every analytics card should be using in 2026.
## HTML
```html
<section class="ac-12" aria-label="Count up KPI metrics card demo">
  <div class="ac-12__stage">
    <header class="ac-12__head">
      <p class="ac-12__eyebrow">Analytics</p>
      <h2 class="ac-12__title">Revenue overview · last 30 days</h2>
    </header>
    <div class="ac-12__grid">
      <article class="ac-12__card">
        <div class="ac-12__top"><p class="ac-12__key">Monthly recurring revenue</p><span class="ac-12__pill ac-12__pill--up">+12.4%</span></div>
        <p class="ac-12__val"><span class="ac-12__cur">$</span><span class="ac-12__n ac-12__n--a" aria-hidden="true"></span><span class="ac-12__unit">k</span><span class="ac-12__sr">482 thousand dollars</span></p>
        <svg class="ac-12__spark" viewBox="0 0 120 34" preserveAspectRatio="none" aria-hidden="true"><path class="ac-12__line" d="M0 28 L15 24 L30 26 L45 18 L60 20 L75 12 L90 14 L105 6 L120 3"/></svg>
        <p class="ac-12__foot">vs $429k previous period</p>
      </article>
      <article class="ac-12__card">
        <div class="ac-12__top"><p class="ac-12__key">Active workspaces</p><span class="ac-12__pill ac-12__pill--up">+318</span></div>
        <p class="ac-12__val"><span class="ac-12__n ac-12__n--b" aria-hidden="true"></span><span class="ac-12__sr">9,140 workspaces</span></p>
        <div class="ac-12__bars" aria-hidden="true"><i style="--ac-12-h:38%"></i><i style="--ac-12-h:52%"></i><i style="--ac-12-h:44%"></i><i style="--ac-12-h:70%"></i><i style="--ac-12-h:61%"></i><i style="--ac-12-h:86%"></i><i style="--ac-12-h:100%"></i></div>
        <p class="ac-12__foot">8,822 at start of period</p>
      </article>
      <article class="ac-12__card">
        <div class="ac-12__top"><p class="ac-12__key">Net revenue retention</p><span class="ac-12__pill ac-12__pill--flat">stable</span></div>
        <p class="ac-12__val"><span class="ac-12__n ac-12__n--c" aria-hidden="true"></span><span class="ac-12__dot">.</span><span class="ac-12__n ac-12__n--d" aria-hidden="true"></span><span class="ac-12__unit">%</span><span class="ac-12__sr">118.6 percent</span></p>
        <div class="ac-12__meter" role="meter" aria-valuenow="118.6" aria-valuemin="0" aria-valuemax="150" aria-label="Net revenue retention"><span></span></div>
        <p class="ac-12__foot">Target 115% · 12-month cohort</p>
      </article>
    </div>
    <p class="ac-12__chip" aria-hidden="true">@property &lt;integer&gt; · counter-reset var() · content:counter() · tabular-nums · zero JavaScript</p>
  </div>
</section>
```
## CSS
```css
@property --ac-12-a {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --ac-12-b {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --ac-12-c {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --ac-12-d {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.ac-12,
.ac-12 *,
.ac-12 *::before,
.ac-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-12-bg: oklch(0.16 0.016 268);
  --ac-12-card: oklch(0.21 0.019 268);
  --ac-12-ink: oklch(0.97 0.004 260);
  --ac-12-mut: oklch(0.69 0.02 268);
  --ac-12-acc: oklch(0.80 0.16 158);
  --ac-12-line: oklch(1 0 0/.11);
  background: var(--ac-12-bg);
  color: var(--ac-12-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,28px);
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(100% 70% at 50% 0%,color-mix(in oklch,var(--ac-12-acc) 11%,transparent),transparent 62%);
}

.ac-12__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.ac-12__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-12-acc);
}

.ac-12__title {
  font-size: clamp(22px,3.2vw,34px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-12__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(238px,1fr));
  gap: 14px;
  width: min(100%,940px);
}

.ac-12__card {
  display: grid;
  gap: 12px;
  padding: 18px;
  border: 1px solid var(--ac-12-line);
  border-radius: 20px;
  background: var(--ac-12-card);
  animation: ac-12-rise .8s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--ac-12-i,0) * 110ms);
}

.ac-12__card:nth-child(2) {
  --ac-12-i: 1;
}

.ac-12__card:nth-child(3) {
  --ac-12-i: 2;
}

@keyframes ac-12-rise {
  from {
    opacity: 0;
    transform: translateY(16px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ac-12__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 10px;
}

.ac-12__key {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--ac-12-mut);
  line-height: 1.35;
  text-wrap: pretty;
}

.ac-12__pill {
  flex: none;
  padding: 4px 9px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  animation: ac-12-slide .7s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(.4s + var(--ac-12-i,0) * 110ms);
}

.ac-12__pill--up {
  background: color-mix(in oklch,var(--ac-12-acc) 18%,transparent);
  color: var(--ac-12-acc);
}

.ac-12__pill--flat {
  background: oklch(1 0 0/.08);
  color: var(--ac-12-mut);
}

@keyframes ac-12-slide {
  from {
    opacity: 0;
    transform: translateX(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ac-12__val {
  display: flex;
  align-items: baseline;
  font-size: clamp(34px,4.4vw,46px);
  font-weight: 700;
  letter-spacing: -.045em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.ac-12__cur,
.ac-12__unit {
  color: var(--ac-12-acc);
  font-size: .52em;
  font-weight: 640;
}

.ac-12__cur {
  margin-right: 2px;
}

.ac-12__unit {
  margin-left: 2px;
}

.ac-12__dot {
  margin: 0 1px;
}

.ac-12__n {
  animation: var(--ac-12-kf) 2.1s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(.1s + var(--ac-12-i,0) * 110ms);
}

.ac-12__n--a {
  counter-reset: ac-12-a var(--ac-12-a);
  --ac-12-kf: ac-12-ka;
}

.ac-12__n--a::after {
  content: counter(ac-12-a);
}

.ac-12__n--b {
  counter-reset: ac-12-b var(--ac-12-b);
  --ac-12-kf: ac-12-kb;
}

.ac-12__n--b::after {
  content: counter(ac-12-b);
}

.ac-12__n--c {
  counter-reset: ac-12-c var(--ac-12-c);
  --ac-12-kf: ac-12-kc;
}

.ac-12__n--c::after {
  content: counter(ac-12-c);
}

.ac-12__n--d {
  counter-reset: ac-12-d var(--ac-12-d);
  --ac-12-kf: ac-12-kd;
}

.ac-12__n--d::after {
  content: counter(ac-12-d);
}

@keyframes ac-12-ka {
  from {
    --ac-12-a: 0;
  }

  to {
    --ac-12-a: 482;
  }
}

@keyframes ac-12-kb {
  from {
    --ac-12-b: 0;
  }

  to {
    --ac-12-b: 9140;
  }
}

@keyframes ac-12-kc {
  from {
    --ac-12-c: 0;
  }

  to {
    --ac-12-c: 118;
  }
}

@keyframes ac-12-kd {
  from {
    --ac-12-d: 0;
  }

  to {
    --ac-12-d: 6;
  }
}

.ac-12__spark {
  width: 100%;
  height: 34px;
  overflow: visible;
}

.ac-12__line {
  fill: none;
  stroke: var(--ac-12-acc);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 200;
  stroke-dashoffset: 200;
  animation: ac-12-draw 1.6s cubic-bezier(.5,0,.2,1) .3s forwards;
}

@keyframes ac-12-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ac-12__bars {
  display: flex;
  align-items: flex-end;
  gap: 5px;
  height: 34px;
}

.ac-12__bars i {
  flex: 1;
  height: var(--ac-12-h);
  border-radius: 3px;
  background: color-mix(in oklch,var(--ac-12-acc) 55%,transparent);
  transform-origin: 50% 100%;
  animation: ac-12-grow .7s cubic-bezier(.16,1,.3,1) both;
}

.ac-12__bars i:nth-child(1) {
  animation-delay: .3s;
}

.ac-12__bars i:nth-child(2) {
  animation-delay: .36s;
}

.ac-12__bars i:nth-child(3) {
  animation-delay: .42s;
}

.ac-12__bars i:nth-child(4) {
  animation-delay: .48s;
}

.ac-12__bars i:nth-child(5) {
  animation-delay: .54s;
}

.ac-12__bars i:nth-child(6) {
  animation-delay: .6s;
}

.ac-12__bars i:nth-child(7) {
  animation-delay: .66s;
  background: var(--ac-12-acc);
}

@keyframes ac-12-grow {
  from {
    transform: scaleY(0);
  }

  to {
    transform: scaleY(1);
  }
}

.ac-12__meter {
  height: 7px;
  border-radius: 99px;
  background: oklch(1 0 0/.09);
  overflow: hidden;
}

.ac-12__meter span {
  display: block;
  height: 100%;
  width: 79%;
  border-radius: 99px;
  background: linear-gradient(90deg,color-mix(in oklch,var(--ac-12-acc) 55%,transparent),var(--ac-12-acc));
  transform-origin: 0 50%;
  animation: ac-12-fill 1.5s cubic-bezier(.16,1,.3,1) .35s both;
}

@keyframes ac-12-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.ac-12__foot {
  font-size: 11.5px;
  color: var(--ac-12-mut);
  font-variant-numeric: tabular-nums;
}

.ac-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ac-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-12-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-12-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-12__n {
    animation-duration: 1ms;
  }

  .ac-12__card,
    .ac-12__pill,
    .ac-12__bars i,
    .ac-12__meter span {
    animation-duration: 1ms;
  }

  .ac-12__line {
    animation: none;
    stroke-dashoffset: 0;
  }
}
```
