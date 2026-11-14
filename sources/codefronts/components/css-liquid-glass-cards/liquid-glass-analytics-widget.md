---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/liquid-glass-analytics-widget/"
title: "Liquid Glass Analytics Widget"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A dashboard KPI card whose frosted glass panel floats over a live SVG line chart, subtly warping the grid lines and area fill beneath it."
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Analytics Widget
Source: https://codefronts.com/components/css-liquid-glass-cards/liquid-glass-analytics-widget/

A dashboard KPI card whose frosted glass panel floats over a live SVG line chart, subtly warping the grid lines and area fill beneath it. High-contrast numbers stay razor-sharp on a solid tint while the chart behind is lensed by a real SVG displacement filter — the readability trade-off that Liquid Glass dashboards must nail.
## HTML
```html
<section class="lg-01" aria-label="Liquid glass analytics widget demo">
  <svg class="lg-01__defs" aria-hidden="true" width="0" height="0"><filter id="lg-01-warp"><feTurbulence type="fractalNoise" baseFrequency="0.008 0.02" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="18" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <article class="lg-01__card">
    <svg class="lg-01__chart" viewBox="0 0 320 150" preserveAspectRatio="none" aria-hidden="true">
      <g class="lg-01__grid" filter="url(#lg-01-warp)">
        <line x1="0" y1="30" x2="320" y2="30"/><line x1="0" y1="70" x2="320" y2="70"/><line x1="0" y1="110" x2="320" y2="110"/>
        <path class="lg-01__area" d="M0 120 L40 96 L80 104 L120 60 L160 74 L200 40 L240 52 L280 24 L320 34 L320 150 L0 150 Z"/>
      </g>
      <path class="lg-01__line" d="M0 120 L40 96 L80 104 L120 60 L160 74 L200 40 L240 52 L280 24 L320 34"/>
    </svg>
    <div class="lg-01__panel">
      <p class="lg-01__eyebrow">Monthly Revenue</p>
      <div class="lg-01__kpi"><strong>$248.6k</strong><span class="lg-01__delta" aria-label="up 12.4 percent">▲ 12.4%</span></div>
      <p class="lg-01__sub">vs. $221.2k last month</p>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-01,
.lg-01 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-01 {
  --accent: oklch(0.72 0.17 155);
  --series: oklch(0.82 0.16 150);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 140deg at 70% 30%,#0d2b2b,#134e4a,#0f766e,#0d2b2b);
  background-size: 200% 200%;
  animation: lg-01-bg 20s ease-in-out infinite;
}

@keyframes lg-01-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-01__card {
  position: relative;
  width: min(360px,100%);
  border-radius: 24px;
  overflow: hidden;
  isolation: isolate;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 28px 60px -30px rgba(0,0,0,.7);
  backdrop-filter: blur(14px) saturate(180%);
  -webkit-backdrop-filter: blur(14px) saturate(180%);
}

.lg-01__chart {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: .9;
}

.lg-01__grid line {
  stroke: rgba(255,255,255,.22);
  stroke-width: 1;
}

.lg-01__area {
  fill: color-mix(in oklab,var(--series) 30%,transparent);
}

.lg-01__line {
  fill: none;
  stroke: var(--series);
  stroke-width: 2.5;
  filter: drop-shadow(0 0 6px color-mix(in oklab,var(--series) 60%,transparent));
}

.lg-01__panel {
  position: relative;
  padding: 22px 24px;
}

.lg-01__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(255,255,255,.75);
}

.lg-01__kpi {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-top: 8px;
}

.lg-01__kpi strong {
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: #fff;
  text-shadow: 0 2px 10px rgba(0,0,0,.35);
}

.lg-01__delta {
  font-size: 13px;
  font-weight: 700;
  color: #effef6;
  padding: 3px 8px;
  border-radius: 999px;
  background: color-mix(in oklab,var(--accent) 55%,transparent);
}

.lg-01__sub {
  margin-top: 6px;
  font-size: 13px;
  color: rgba(255,255,255,.7);
}

@media (prefers-reduced-motion: reduce) {
  .lg-01 {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the refraction is a pure SVG feTurbulence + feDisplacementMap filter on the chart grid. Drop your own data into the path 'd' attributes and the glass lenses it automatically. */
```
