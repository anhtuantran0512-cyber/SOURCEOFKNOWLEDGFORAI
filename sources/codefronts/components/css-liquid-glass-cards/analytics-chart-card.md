---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/analytics-chart-card/"
title: "Analytics Chart Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A card containing an SVG line chart where a Liquid Glass refraction layer floats over the plot and subtly warps the ruled grid lines underneath — the grid…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Analytics Chart Card
Source: https://codefronts.com/components/css-liquid-glass-cards/analytics-chart-card/

A card containing an SVG line chart where a Liquid Glass refraction layer floats over the plot and subtly warps the ruled grid lines underneath — the grid bends as if seen through a curved lens while the series line and KPI stay sharp. The dashboard-glass readability trade-off, done right.
## HTML
```html
<section class="lg-14" aria-label="Liquid glass analytics chart card demo">
  <svg class="lg-14__defs" aria-hidden="true" width="0" height="0"><filter id="lg-14-warp"><feTurbulence type="fractalNoise" baseFrequency="0.009 0.02" numOctaves="2" seed="4" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="16" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <article class="lg-14__card">
    <div class="lg-14__head"><p class="lg-14__eyebrow">Active users</p><span class="lg-14__delta" aria-label="up 9.1 percent">▲ 9.1%</span></div>
    <svg class="lg-14__chart" viewBox="0 0 320 160" preserveAspectRatio="none" aria-hidden="true">
      <g class="lg-14__grid" filter="url(#lg-14-warp)">
        <line x1="0" y1="40" x2="320" y2="40"/><line x1="0" y1="80" x2="320" y2="80"/><line x1="0" y1="120" x2="320" y2="120"/>
        <line x1="64" y1="0" x2="64" y2="160"/><line x1="128" y1="0" x2="128" y2="160"/><line x1="192" y1="0" x2="192" y2="160"/><line x1="256" y1="0" x2="256" y2="160"/>
        <path class="lg-14__area" d="M0 128 L46 104 L92 116 L138 66 L184 84 L230 44 L276 58 L320 30 L320 160 L0 160 Z"/>
      </g>
      <path class="lg-14__line" d="M0 128 L46 104 L92 116 L138 66 L184 84 L230 44 L276 58 L320 30"/>
    </svg>
    <div class="lg-14__panel"><strong class="lg-14__kpi">42,910</strong><span class="lg-14__sub">last 30 days · warped grid under glass</span></div>
  </article>
</section>
```
## CSS
```css
.lg-14,
.lg-14 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-14 {
  width: 100%;
  --accent: oklch(0.72 0.17 250);
  --series: oklch(0.82 0.14 255);
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 140deg at 70% 30%,#1e1b4b,#1e3a8a,#0e7490,#1e1b4b);
  background-size: 200% 200%;
  animation: lg-14-bg 20s ease-in-out infinite;
}

@keyframes lg-14-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-14__card {
  position: relative;
  width: min(370px,100%);
  border-radius: 24px;
  overflow: hidden;
  isolation: isolate;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 28px 60px -30px rgba(0,0,0,.7);
  backdrop-filter: blur(14px) saturate(180%);
  -webkit-backdrop-filter: blur(14px) saturate(180%);
}

.lg-14__head {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 20px 0;
}

.lg-14__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(255,255,255,.78);
}

.lg-14__delta {
  font-size: 12px;
  font-weight: 700;
  color: #eef6ff;
  padding: 3px 9px;
  border-radius: 999px;
  background: color-mix(in oklab,var(--accent) 55%,transparent);
}

.lg-14__chart {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 70px;
  width: 100%;
  height: 150px;
  opacity: .9;
}

.lg-14__grid line {
  stroke: rgba(255,255,255,.22);
  stroke-width: 1;
}

.lg-14__area {
  fill: color-mix(in oklab,var(--series) 26%,transparent);
}

.lg-14__line {
  fill: none;
  stroke: var(--series);
  stroke-width: 2.5;
  filter: drop-shadow(0 0 6px color-mix(in oklab,var(--series) 60%,transparent));
}

.lg-14__panel {
  position: relative;
  z-index: 2;
  padding: 0 20px 22px;
  margin-top: 150px;
}

.lg-14__kpi {
  display: block;
  font-size: 40px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: #fff;
  text-shadow: 0 2px 10px rgba(0,0,0,.35);
}

.lg-14__sub {
  font-size: 12.5px;
  color: rgba(255,255,255,.72);
}

@media (prefers-reduced-motion: reduce) {
  .lg-14 {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the refraction is a pure SVG feTurbulence + feDisplacementMap filter applied to the chart's grid group, so the ruled lines bend under the frosted overlay. Drop your own data into the path 'd' attributes and the glass lenses it automatically. */
```
