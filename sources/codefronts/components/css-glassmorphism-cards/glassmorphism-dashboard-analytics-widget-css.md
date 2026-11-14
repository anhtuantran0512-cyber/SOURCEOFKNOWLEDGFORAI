---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-dashboard-analytics-widget-css/"
title: "Glassmorphism Dashboard Analytics Widget CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two dashboard staples: a revenue widget whose SVG area chart draws itself in with a moving “live” dot and CSS-only timeframe pills, and a KPI strip where the…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Dashboard Analytics Widget CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-dashboard-analytics-widget-css/

Two dashboard staples: a revenue widget whose SVG area chart draws itself in with a moving “live” dot and CSS-only timeframe pills, and a KPI strip where the numbers literally count up using the @property + counter() trick — animated integers with zero JavaScript.
## HTML
```html
<div class="glz-11-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-11a" aria-label="Glassmorphism analytics widget demo">
  <article class="glz-11a__card">
    <header class="glz-11a__head">
      <div><h3>Net revenue</h3><p class="glz-11a__big">$128,430<span class="glz-11a__chip">▲ 18.2%</span></p></div>
      <div class="glz-11a__pills" role="radiogroup" aria-label="Timeframe">
        <label><input type="radio" name="glz-11a-t"><span>7D</span></label>
        <label><input type="radio" name="glz-11a-t" checked><span>30D</span></label>
        <label><input type="radio" name="glz-11a-t"><span>90D</span></label>
      </div>
    </header>
    <div class="glz-11a__chart">
      <svg viewBox="0 0 120 44" preserveAspectRatio="none" aria-hidden="true">
        <defs><linearGradient id="glz11aG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="oklch(0.75 0.15 210)" stop-opacity=".45"/><stop offset="1" stop-color="oklch(0.75 0.15 210)" stop-opacity="0"/></linearGradient></defs>
        <path class="glz-11a__area" d="M0 36 L12 32 L24 34 L36 26 L48 29 L60 21 L72 24 L84 14 L96 18 L108 9 L120 12 V44 H0 Z" fill="url(#glz11aG)"/>
        <path class="glz-11a__line" d="M0 36 L12 32 L24 34 L36 26 L48 29 L60 21 L72 24 L84 14 L96 18 L108 9 L120 12" fill="none" stroke="oklch(0.75 0.15 210)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <i class="glz-11a__dot" aria-hidden="true"></i>
    </div>
    <footer class="glz-11a__foot"><span>MRR <b>$42.8k</b></span><span>New customers <b>312</b></span><span>Churn <b class="glz-11a__dn">1.9%</b></span></footer>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-11b" aria-label="KPI cards with CSS count-up animation">
  <div class="glz-11b__grid">
    <article class="glz-11b__kpi" style="--target:1284;--d:0s"><span class="glz-11b__ic" aria-hidden="true">◉</span><h3>Active users</h3><b aria-label="1284"></b><em class="glz-11b__up">▲ 12% this week</em></article>
    <article class="glz-11b__kpi" style="--target:96;--d:.15s"><span class="glz-11b__ic" aria-hidden="true">▦</span><h3>Reports built</h3><b aria-label="96"></b><em class="glz-11b__up">▲ 8 today</em></article>
    <article class="glz-11b__kpi" style="--target:42;--d:.3s"><span class="glz-11b__ic" aria-hidden="true">⚡</span><h3>Avg. load (ms)</h3><b aria-label="42"></b><em class="glz-11b__dn">▼ 6ms faster</em></article>
  </div>
</section>
</div>
```
## CSS
```css
.glz-11-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-11-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-11a,
.glz-11a *,
.glz-11a *::before,
.glz-11a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-11a {
  --blu: oklch(0.75 0.15 210);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0a0f1e;
  font-family: 'Manrope',system-ui,sans-serif;
}

.glz-11a::before {
  content: "";
  position: absolute;
  width: 58vmin;
  height: 58vmin;
  border-radius: 50%;
  background: oklch(0.55 0.17 250);
  filter: blur(95px);
  opacity: .5;
  top: -14%;
  left: -6%;
}

.glz-11a::after {
  content: "";
  position: absolute;
  width: 46vmin;
  height: 46vmin;
  border-radius: 50%;
  background: oklch(0.6 0.15 180);
  filter: blur(95px);
  opacity: .4;
  bottom: -12%;
  right: -6%;
}

.glz-11a__card {
  position: relative;
  z-index: 1;
  width: min(440px,100%);
  padding: 26px 26px 20px;
  border-radius: 24px;
  color: #e9eefb;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: 0 32px 66px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-11a__head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 14px;
  flex-wrap: wrap;
}

.glz-11a__head h3 {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(233,238,251,.55);
}

.glz-11a__big {
  margin-top: 8px;
  font-size: clamp(24px,4.4vw,30px);
  font-weight: 800;
  letter-spacing: -.02em;
  color: #fff;
  font-variant-numeric: tabular-nums;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.glz-11a__chip {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .04em;
  padding: 5px 9px;
  border-radius: 99px;
  color: oklch(0.87 0.15 160);
  background: oklch(0.87 0.15 160/.14);
  border: 1px solid oklch(0.87 0.15 160/.35);
}

.glz-11a__pills {
  display: flex;
  gap: 4px;
  padding: 4px;
  border-radius: 12px;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.14);
}

.glz-11a__pills label {
  position: relative;
}

.glz-11a__pills input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}

.glz-11a__pills span {
  display: block;
  padding: 6px 11px;
  border-radius: 9px;
  font: 700 11px 'JetBrains Mono',monospace;
  color: rgba(233,238,251,.55);
  transition: background .2s ease,color .2s ease;
}

.glz-11a__pills label:has(input:checked) span {
  background: rgba(255,255,255,.16);
  color: #fff;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.25);
}

.glz-11a__pills label:has(input:focus-visible) span {
  outline: 2px solid var(--blu);
  outline-offset: 2px;
}

.glz-11a__chart {
  position: relative;
  margin-top: 20px;
}

.glz-11a__chart svg {
  width: 100%;
  height: 120px;
  display: block;
}

.glz-11a__line {
  stroke-dasharray: 300;
  stroke-dashoffset: 300;
  animation: glz-11a-draw 1.5s cubic-bezier(.4,0,.2,1) .2s forwards;
}

.glz-11a__area {
  opacity: 0;
  animation: glz-11a-fade .7s ease 1.3s forwards;
}

.glz-11a__dot {
  position: absolute;
  right: 0;
  top: 27%;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--blu);
  box-shadow: 0 0 0 0 oklch(0.75 0.15 210/.6);
  animation: glz-11a-ping 2s ease-out 1.7s infinite;
}

.glz-11a__foot {
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,.12);
  font-size: 12px;
  color: rgba(233,238,251,.55);
}

.glz-11a__foot b {
  color: #fff;
  font-variant-numeric: tabular-nums;
  margin-left: 6px;
}

.glz-11a__dn {
  color: oklch(0.75 0.17 20)!important;
}

@keyframes glz-11a-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes glz-11a-fade {
  to {
    opacity: 1;
  }
}

@keyframes glz-11a-ping {
  0% {
    box-shadow: 0 0 0 0 oklch(0.75 0.15 210/.6);
  }

  70%,
    100% {
    box-shadow: 0 0 0 12px transparent;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-11a__card {
    background: rgba(15,21,38,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-11a__line {
    animation: none;
    stroke-dashoffset: 0;
  }

  .glz-11a__area {
    animation: none;
    opacity: 1;
  }

  .glz-11a__dot {
    animation: none;
  }
}

.glz-11b,
.glz-11b *,
.glz-11b *::before,
.glz-11b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --glz-11b-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.glz-11b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: linear-gradient(190deg,#101426,#0b1c1e);
}

.glz-11b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(44% 38% at 78% 20%,oklch(0.6 0.16 180/.35),transparent 70%),radial-gradient(40% 34% at 16% 82%,oklch(0.58 0.2 280/.35),transparent 70%);
}

.glz-11b__grid {
  position: relative;
  z-index: 1;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 18px;
  width: min(860px,100%);
}

.glz-11b__kpi {
  flex: 1 1 220px;
  max-width: 280px;
  padding: 24px 24px 20px;
  border-radius: 22px;
  color: #e9f4f2;
  font-family: 'Manrope',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: 0 26px 54px -24px rgba(0,0,0,.75),inset 0 1px 0 rgba(255,255,255,.22);
  transition: transform .3s ease;
}

.glz-11b__kpi:hover {
  transform: translateY(-5px);
}

.glz-11b__ic {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  font-size: 15px;
  color: oklch(0.85 0.14 180);
  background: oklch(0.85 0.14 180/.12);
  border: 1px solid oklch(0.85 0.14 180/.3);
}

.glz-11b__kpi h3 {
  margin-top: 14px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(233,244,242,.55);
}

.glz-11b__kpi b {
  display: block;
  margin-top: 6px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 38px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: #fff;
  --glz-11b-n: 0;
  animation: glz-11b-count 1.8s cubic-bezier(.2,.6,.2,1) var(--d) forwards;
}

.glz-11b__kpi b::after {
  counter-reset: glz11b calc(var(--glz-11b-n));
  content: counter(glz11b);
}

.glz-11b__kpi em {
  display: block;
  margin-top: 8px;
  font-style: normal;
  font-size: 12px;
  font-weight: 700;
}

.glz-11b__up {
  color: oklch(0.85 0.15 160);
}

.glz-11b__dn {
  color: oklch(0.85 0.14 180);
}

@keyframes glz-11b-count {
  to {
    --glz-11b-n: var(--target);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-11b__kpi {
    background: rgba(16,24,30,.94);
  }
}

@supports not (animation-timeline: scroll()) {
}

@media (prefers-reduced-motion: reduce) {
  .glz-11b__kpi b {
    animation-duration: .001s;
    animation-delay: 0s;
  }

  .glz-11b__kpi {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the line draws via dash-offset, the area fades in after it, the live dot pings with an expanding transparent box-shadow, and timeframe pills are real radios. */

/* No JavaScript — each number is an @property-registered integer animated to --target and printed via counter(); reduced-motion snaps straight to the final value. */
```
