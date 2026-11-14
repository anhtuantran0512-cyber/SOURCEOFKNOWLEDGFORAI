---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/full-screen-analytics-dashboard-100vh-no-scroll-engine/"
title: "Full-Screen Analytics Dashboard (100vh No-Scroll Engine)"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The NOC-wall contract: every pixel of the viewport, zero scrollbars, ever."
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Screen Analytics Dashboard (100vh No-Scroll Engine)
Source: https://codefronts.com/layouts/css-dashboard-layouts/full-screen-analytics-dashboard-100vh-no-scroll-engine/

The NOC-wall contract: every pixel of the viewport, zero scrollbars, ever. A dark command center where all four zones — status bar, KPI strip, chart grid, incident ticker — are fractional grid tracks that scale with the screen, type rides clamp() so it grows on a TV and shrinks on a laptop, and every panel is armored with minmax(0,1fr) + overflow guards so no runaway feed can ever summon the browser scrollbar. Live pulses, sweeping gauges and an equalizer chart make it feel like mission control; the geometry makes it kiosk-safe.
## HTML
```html
<section class="cdl-16" aria-label="Full-screen command center demo">
  <div class="cdl-16__center">
    <header class="cdl-16__status">
      <strong><i class="cdl-16__beacon" aria-hidden="true"></i>ATLAS · Global Ops</strong>
      <span class="cdl-16__zone">All regions nominal</span>
      <time class="cdl-16__clock" datetime="2026-08-01T21:04">21:04:52 UTC</time>
    </header>
    <div class="cdl-16__kpis">
      <article><h3>Requests / s</h3><p>84,210</p><small class="cdl-16__ok">▲ steady</small></article>
      <article><h3>Error rate</h3><p>0.03%</p><small class="cdl-16__ok">within SLO</small></article>
      <article><h3>P99 latency</h3><p>412<small> ms</small></p><small class="cdl-16__warn">▲ 8% · eu-west</small></article>
      <article><h3>Active incidents</h3><p>1</p><small class="cdl-16__warn">sev-3 · queue lag</small></article>
    </div>
    <div class="cdl-16__charts">
      <article class="cdl-16__panel">
        <h3>Throughput · 60 min</h3>
        <div class="cdl-16__eq" aria-hidden="true"><i style="--s:.5;--d:0s"></i><i style="--s:.7;--d:.12s"></i><i style="--s:.6;--d:.24s"></i><i style="--s:.85;--d:.36s"></i><i style="--s:.65;--d:.48s"></i><i style="--s:.9;--d:.6s"></i><i style="--s:.75;--d:.72s"></i><i style="--s:.95;--d:.84s"></i><i style="--s:.7;--d:.96s"></i><i style="--s:.8;--d:1.08s"></i></div>
      </article>
      <article class="cdl-16__panel cdl-16__gauges">
        <h3>Saturation</h3>
        <div class="cdl-16__gaugerow">
          <div class="cdl-16__gauge" style="--val:68" role="img" aria-label="CPU 68 percent"><b>68<small>%</small></b><span>CPU</span></div>
          <div class="cdl-16__gauge cdl-16__g2" style="--val:41" role="img" aria-label="Memory 41 percent"><b>41<small>%</small></b><span>MEM</span></div>
          <div class="cdl-16__gauge cdl-16__g3" style="--val:83" role="img" aria-label="IO 83 percent"><b>83<small>%</small></b><span>I/O</span></div>
        </div>
      </article>
      <article class="cdl-16__panel">
        <h3>Regions</h3>
        <ul class="cdl-16__regions">
          <li><b>us-east</b><span class="cdl-16__meter"><i style="--w:62%"></i></span><em>62%</em></li>
          <li><b>us-west</b><span class="cdl-16__meter"><i style="--w:48%"></i></span><em>48%</em></li>
          <li><b>eu-west</b><span class="cdl-16__meter cdl-16__hotm"><i style="--w:87%"></i></span><em>87%</em></li>
          <li><b>ap-south</b><span class="cdl-16__meter"><i style="--w:35%"></i></span><em>35%</em></li>
        </ul>
      </article>
    </div>
    <footer class="cdl-16__tickerwrap" aria-label="Incident ticker">
      <div class="cdl-16__ticker"><span>⚠ sev-3 · queue lag eu-west · ETA 20m &nbsp;·&nbsp; ✓ deploy v3.02 healthy across 6 regions &nbsp;·&nbsp; ◇ maintenance window Sun 02:00 UTC &nbsp;·&nbsp; ✓ backup verified 21:00 &nbsp;·&nbsp;</span><span aria-hidden="true">⚠ sev-3 · queue lag eu-west · ETA 20m &nbsp;·&nbsp; ✓ deploy v3.02 healthy across 6 regions &nbsp;·&nbsp; ◇ maintenance window Sun 02:00 UTC &nbsp;·&nbsp; ✓ backup verified 21:00 &nbsp;·&nbsp;</span></div>
    </footer>
  </div>
</section>
```
## CSS
```css
.cdl-16,
.cdl-16 *,
.cdl-16 *::before,
.cdl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-16 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.14 0.02 230);
  --panel: oklch(0.19 0.025 230);
  --edge: oklch(0.29 0.03 230);
  --ink: oklch(0.93 0.01 210);
  --mut: oklch(0.62 0.03 220);
  --cyan: oklch(0.8 0.13 210);
  --ok: oklch(0.78 0.16 155);
  --warn: oklch(0.8 0.14 85);
  --hot: oklch(0.65 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

@property --cdl16-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.cdl-16__center {
  width: 100%;
  height: 100vh;
  overflow: hidden;
  display: grid;
  gap: 12px;
  grid-template-rows: 44px auto minmax(0,2.2fr) 36px;
  border: 1px solid var(--edge);
  padding: 12px;
  background: radial-gradient(140% 100% at 50% -20%,oklch(0.22 0.04 230/.9),transparent 55%),var(--bg);
}

.cdl-16__status {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0 6px;
  font-size: 13px;
}

.cdl-16__status strong {
  display: flex;
  align-items: center;
  gap: 10px;
  letter-spacing: .06em;
}

.cdl-16__beacon {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--ok);
  animation: cdl16-pulse 2.2s infinite;
}

@keyframes cdl16-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 color-mix(in oklch,var(--ok) 60%,transparent);
  }

  70% {
    box-shadow: 0 0 0 9px transparent;
  }
}

.cdl-16__zone {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--ok);
  border: 1px solid color-mix(in oklch,var(--ok) 35%,transparent);
  background: color-mix(in oklch,var(--ok) 10%,transparent);
  border-radius: 999px;
  padding: 4px 12px;
}

.cdl-16__clock {
  margin-left: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  color: var(--cyan);
  font-variant-numeric: tabular-nums;
}

.cdl-16__kpis {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
}

.cdl-16__kpis article {
  background: linear-gradient(160deg,color-mix(in oklch,var(--panel) 88%,white),var(--panel));
  border: 1px solid var(--edge);
  border-radius: 13px;
  padding: 11px 15px;
}

.cdl-16__kpis h3 {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-16__kpis p {
  font-size: clamp(20px,2.6cqi + 8px,34px);
  font-weight: 700;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
  line-height: 1.15;
  margin: 3px 0 1px;
}

.cdl-16__kpis p small {
  font-size: .5em;
  color: var(--mut);
}

.cdl-16__kpis>article>small {
  font-size: 10.5px;
  font-weight: 700;
}

.cdl-16__ok {
  color: var(--ok);
}

.cdl-16__warn {
  color: var(--warn);
}

.cdl-16__charts {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(3,minmax(0,1fr));
  min-height: 0;
}

.cdl-16__panel {
  min-height: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 10px;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 13px;
  padding: 13px 15px;
}

.cdl-16__panel h3 {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-16__eq {
  flex: 1;
  min-height: 0;
  display: flex;
  align-items: flex-end;
  gap: 6px;
}

.cdl-16__eq i {
  flex: 1;
  height: 92%;
  border-radius: 3px 3px 0 0;
  background: linear-gradient(to top,color-mix(in oklch,var(--cyan) 20%,transparent),var(--cyan));
  transform-origin: bottom;
  scale: 1 var(--s);
  animation: cdl16-eq 1.6s ease-in-out var(--d) infinite alternate;
}

@keyframes cdl16-eq {
  to {
    scale: 1 calc(var(--s)*.55);
  }
}

.cdl-16__gaugerow {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-around;
  gap: 8px;
  flex-wrap: wrap;
}

.cdl-16__gauge {
  --c: var(--cyan);
  position: relative;
  width: clamp(64px,7cqi,96px);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
}

.cdl-16__gauge::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(var(--c) var(--cdl16-a),oklch(0.27 0.03 230) 0);
  mask: radial-gradient(circle,transparent 58%,black 59%);
  animation: cdl16-sweep 1.2s cubic-bezier(.2,.7,.2,1) .3s both;
}

@keyframes cdl16-sweep {
  from {
    --cdl16-a: 0deg;
  }

  to {
    --cdl16-a: calc(var(--val)*3.6deg);
  }
}

.cdl-16__gauge b {
  position: relative;
  display: grid;
  place-content: center;
  font-size: clamp(14px,1.8cqi,20px);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cdl-16__gauge b small {
  font-size: .55em;
  color: var(--mut);
}

.cdl-16__gauge span {
  position: absolute;
  bottom: -4px;
  left: 50%;
  translate: -50% 100%;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: .14em;
  color: var(--mut);
}

.cdl-16__g2 {
  --c: var(--ok);
}

.cdl-16__g3 {
  --c: var(--warn);
}

.cdl-16__regions {
  list-style: none;
  flex: 1;
  display: grid;
  gap: 8px;
  align-content: space-evenly;
  min-height: 0;
}

.cdl-16__regions li {
  display: grid;
  grid-template-columns: 64px minmax(0,1fr) 40px;
  align-items: center;
  gap: 10px;
  font-size: 12px;
}

.cdl-16__regions b {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
}

.cdl-16__regions em {
  font-style: normal;
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-weight: 700;
}

.cdl-16__meter {
  height: 7px;
  border-radius: 999px;
  background: oklch(0.27 0.03 230);
  overflow: hidden;
}

.cdl-16__meter i {
  display: block;
  height: 100%;
  width: var(--w);
  border-radius: inherit;
  background: linear-gradient(90deg,color-mix(in oklch,var(--cyan) 60%,transparent),var(--cyan));
}

.cdl-16__hotm i {
  background: linear-gradient(90deg,var(--warn),var(--hot));
}

.cdl-16__tickerwrap {
  overflow: hidden;
  border: 1px solid var(--edge);
  border-radius: 10px;
  background: var(--panel);
  display: flex;
  align-items: center;
  mask: linear-gradient(90deg,transparent,black 4%,black 96%,transparent);
}

.cdl-16__ticker {
  display: flex;
  white-space: nowrap;
  animation: cdl16-tick 26s linear infinite;
}

.cdl-16__ticker span {
  padding: 0 12px;
  font-size: 12px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.cdl-16__tickerwrap:hover .cdl-16__ticker,
.cdl-16__tickerwrap:focus-within .cdl-16__ticker {
  animation-play-state: paused;
}

@keyframes cdl16-tick {
  to {
    translate: -50% 0;
  }
}

@container (max-width: 640px) {
  .cdl-16__center {
    height: auto;
    grid-template-rows: 44px auto auto 36px;
  }

  .cdl-16__charts {
    grid-template-columns: minmax(0,1fr);
    grid-auto-rows: 150px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-16 * {
    animation: none !important;
  }

  .cdl-16__gauge::before {
    background: conic-gradient(var(--c) calc(var(--val)*3.6deg),oklch(0.27 0.03 230) 0);
  }
}
```
