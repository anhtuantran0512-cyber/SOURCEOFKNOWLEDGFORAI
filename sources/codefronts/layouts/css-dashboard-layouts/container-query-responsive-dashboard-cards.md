---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/container-query-responsive-dashboard-cards/"
title: "Container Query Responsive Dashboard Cards"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The same widget markup pasted into three panels — 260px, 420px, and one you resize yourself — renders three different layouts: stacked, side-by-side, and…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Container Query Responsive Dashboard Cards
Source: https://codefronts.com/layouts/css-dashboard-layouts/container-query-responsive-dashboard-cards/

The same widget markup pasted into three panels — 260px, 420px, and one you resize yourself — renders three different layouts: stacked, side-by-side, and full analytics with a legend rail. Media queries can't do this: they ask “how wide is the screen?” when a dashboard widget needs “how wide is MY slot?”. Container queries flip responsive design from page-level to component-level, and this demo makes the difference draggable.
## HTML
```html
<section class="cdl-08" aria-label="Container query widget demo">
  <div class="cdl-08__stage">
    <div class="cdl-08__row">
      <div class="cdl-08__slot" style="flex:0 0 250px"><p class="cdl-08__cap">260px slot → stacked</p>
        <div class="cdl-08__widget">
          <div class="cdl-08__kpi"><h3>Bandwidth</h3><p class="cdl-08__big">4.6<small>TB</small></p><span class="cdl-08__delta">▲ 18% this week</span></div>
          <div class="cdl-08__chart" aria-hidden="true"><i style="--h:35%"></i><i style="--h:55%"></i><i style="--h:42%"></i><i style="--h:68%"></i><i style="--h:58%"></i><i style="--h:80%"></i><i style="--h:72%"></i><i style="--h:95%"></i></div>
          <ul class="cdl-08__legend"><li><i class="cdl-08__c1" aria-hidden="true"></i>CDN 62%</li><li><i class="cdl-08__c2" aria-hidden="true"></i>API 27%</li><li><i class="cdl-08__c3" aria-hidden="true"></i>Media 11%</li></ul>
        </div>
      </div>
      <div class="cdl-08__slot" style="flex:1 1 300px"><p class="cdl-08__cap">≥ 340px → value beside chart</p>
        <div class="cdl-08__widget">
          <div class="cdl-08__kpi"><h3>Bandwidth</h3><p class="cdl-08__big">4.6<small>TB</small></p><span class="cdl-08__delta">▲ 18% this week</span></div>
          <div class="cdl-08__chart" aria-hidden="true"><i style="--h:35%"></i><i style="--h:55%"></i><i style="--h:42%"></i><i style="--h:68%"></i><i style="--h:58%"></i><i style="--h:80%"></i><i style="--h:72%"></i><i style="--h:95%"></i></div>
          <ul class="cdl-08__legend"><li><i class="cdl-08__c1" aria-hidden="true"></i>CDN 62%</li><li><i class="cdl-08__c2" aria-hidden="true"></i>API 27%</li><li><i class="cdl-08__c3" aria-hidden="true"></i>Media 11%</li></ul>
        </div>
      </div>
    </div>
    <div class="cdl-08__slot cdl-08__slot--free"><p class="cdl-08__cap">⤡ drag my corner — breakpoints at 340px and 520px</p>
      <div class="cdl-08__widget">
        <div class="cdl-08__kpi"><h3>Bandwidth</h3><p class="cdl-08__big">4.6<small>TB</small></p><span class="cdl-08__delta">▲ 18% this week</span></div>
        <div class="cdl-08__chart" aria-hidden="true"><i style="--h:35%"></i><i style="--h:55%"></i><i style="--h:42%"></i><i style="--h:68%"></i><i style="--h:58%"></i><i style="--h:80%"></i><i style="--h:72%"></i><i style="--h:95%"></i></div>
        <ul class="cdl-08__legend"><li><i class="cdl-08__c1" aria-hidden="true"></i>CDN 62%</li><li><i class="cdl-08__c2" aria-hidden="true"></i>API 27%</li><li><i class="cdl-08__c3" aria-hidden="true"></i>Media 11%</li></ul>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-08,
.cdl-08 *,
.cdl-08 *::before,
.cdl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-08 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.975 0.005 285);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.012 285);
  --ink: oklch(0.27 0.02 285);
  --mut: oklch(0.55 0.02 285);
  --acc: oklch(0.58 0.18 290);
  --c2: oklch(0.7 0.14 220);
  --c3: oklch(0.8 0.12 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cdl-08__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  gap: 16px;
  border: 1px solid var(--edge);
  background: linear-gradient(175deg,var(--bg),oklch(0.955 0.008 285));
  padding: 18px;
}

.cdl-08__row {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.cdl-08__slot {
  container-type: inline-size;
  container-name: cdl08w;
  min-width: 0;
  display: grid;
  gap: 9px;
  align-content: start;
}

.cdl-08__slot--free {
  resize: horizontal;
  overflow: auto;
  min-width: 240px;
  max-width: 100%;
  padding-bottom: 6px;
  border-right: 2px dashed color-mix(in oklch,var(--acc) 40%,transparent);
  padding-right: 14px;
}

.cdl-08__cap {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-08__slot--free .cdl-08__cap {
  color: var(--acc);
}

.cdl-08__widget {
  display: grid;
  gap: 14px;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 16px;
  padding: 18px;
  box-shadow: 0 10px 26px -20px oklch(0.4 0.06 290 / .5);
}

.cdl-08__kpi h3 {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-08__big {
  font-size: clamp(24px,10cqi,40px);
  font-weight: 700;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
  line-height: 1.1;
  margin: 4px 0 2px;
}

.cdl-08__big small {
  font-size: .5em;
  color: var(--mut);
  font-weight: 600;
  margin-left: 2px;
}

.cdl-08__delta {
  font-size: 11.5px;
  font-weight: 700;
  color: oklch(0.55 0.14 155);
}

.cdl-08__chart {
  display: flex;
  align-items: flex-end;
  gap: 6px;
  height: 64px;
  min-width: 0;
}

.cdl-08__chart i {
  flex: 1;
  height: var(--h);
  border-radius: 4px 4px 0 0;
  background: linear-gradient(to top,color-mix(in oklch,var(--acc) 30%,transparent),var(--acc));
}

.cdl-08__legend {
  list-style: none;
  display: none;
  gap: 8px;
  align-content: center;
}

.cdl-08__legend li {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 600;
  color: var(--mut);
  white-space: nowrap;
}

.cdl-08__legend i {
  width: 10px;
  height: 10px;
  border-radius: 3px;
}

.cdl-08__c1 {
  background: var(--acc);
}

.cdl-08__c2 {
  background: var(--c2);
}

.cdl-08__c3 {
  background: var(--c3);
}

@container cdl08w (min-width: 340px) {
  .cdl-08__widget {
    grid-template-columns: auto minmax(0,1fr);
    align-items: end;
  }

  .cdl-08__kpi {
    align-self: center;
    padding-right: 8px;
  }
}

@container cdl08w (min-width: 520px) {
  .cdl-08__widget {
    grid-template-columns: auto minmax(0,1fr) 132px;
  }

  .cdl-08__legend {
    display: grid;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-08 * {
    transition: none !important;
  }
}
```
