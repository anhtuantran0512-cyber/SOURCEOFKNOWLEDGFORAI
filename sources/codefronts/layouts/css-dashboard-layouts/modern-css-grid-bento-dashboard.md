---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/modern-css-grid-bento-dashboard/"
title: "Modern CSS Grid Bento Dashboard"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The Vercel-generation board: a 4-column bento where the hero KPI spans 2×2, the traffic chart runs 2×1 wide and the activity feed drops 1×2 down the rail —…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern CSS Grid Bento Dashboard
Source: https://codefronts.com/layouts/css-dashboard-layouts/modern-css-grid-bento-dashboard/

The Vercel-generation board: a 4-column bento where the hero KPI spans 2×2, the traffic chart runs 2×1 wide and the activity feed drops 1×2 down the rail — every size decision is two CSS properties. Hover any tile and a single :has() rule gently dims and shrinks its neighbours; on load the whole board staggers in through @starting-style. Non-uniform, rhythmic, and it reflows to 2 columns on narrow panels via a container query.
## HTML
```html
<section class="cdl-01" aria-label="Bento grid dashboard demo">
  <div class="cdl-01__stage">
    <header class="cdl-01__top">
      <span class="cdl-01__mark" aria-hidden="true"></span>
      <strong>Pulse · Overview</strong>
      <span class="cdl-01__live"><i aria-hidden="true"></i>Live</span>
    </header>
    <div class="cdl-01__board">
      <article class="cdl-01__tile cdl-01__hero" style="--i:0">
        <h3>Monthly recurring revenue</h3>
        <p class="cdl-01__big">$482,910<span class="cdl-01__delta cdl-01__up">▲ 12.4%</span></p>
        <p class="cdl-01__sub">vs. $429,644 last month</p>
        <div class="cdl-01__area" aria-hidden="true"><i></i></div>
      </article>
      <article class="cdl-01__tile" style="--i:1">
        <h3>Active users</h3>
        <p class="cdl-01__num">18,442</p>
        <div class="cdl-01__spark" aria-hidden="true"><i style="--h:42%"></i><i style="--h:58%"></i><i style="--h:50%"></i><i style="--h:72%"></i><i style="--h:64%"></i><i style="--h:88%"></i><i style="--h:100%"></i></div>
      </article>
      <article class="cdl-01__tile" style="--i:2">
        <h3>Uptime</h3>
        <div class="cdl-01__ringwrap"><div class="cdl-01__ring" role="img" aria-label="Uptime 99.98 percent"><b>99.98<small>%</small></b></div></div>
      </article>
      <article class="cdl-01__tile cdl-01__wide" style="--i:3">
        <h3>Traffic · last 12 weeks</h3>
        <div class="cdl-01__bars" aria-hidden="true"><i style="--h:34%"></i><i style="--h:48%"></i><i style="--h:41%"></i><i style="--h:56%"></i><i style="--h:52%"></i><i style="--h:63%"></i><i style="--h:58%"></i><i style="--h:74%"></i><i style="--h:69%"></i><i style="--h:82%"></i><i style="--h:78%"></i><i style="--h:96%"></i></div>
      </article>
      <article class="cdl-01__tile cdl-01__tall" style="--i:4">
        <h3>Activity</h3>
        <ul class="cdl-01__feed">
          <li><i class="cdl-01__dot" aria-hidden="true"></i><div><b>Deploy shipped</b><span>prod · 2m ago</span></div></li>
          <li><i class="cdl-01__dot cdl-01__d2" aria-hidden="true"></i><div><b>Invoice #2291 paid</b><span>$1,900 · 14m ago</span></div></li>
          <li><i class="cdl-01__dot cdl-01__d3" aria-hidden="true"></i><div><b>New teammate joined</b><span>ana@ · 1h ago</span></div></li>
          <li><i class="cdl-01__dot" aria-hidden="true"></i><div><b>Alert resolved</b><span>api-eu · 3h ago</span></div></li>
          <li><i class="cdl-01__dot cdl-01__d2" aria-hidden="true"></i><div><b>Backup completed</b><span>db-01 · 5h ago</span></div></li>
        </ul>
      </article>
      <article class="cdl-01__tile" style="--i:5">
        <h3>Top region</h3>
        <p class="cdl-01__num">🇺🇸 41%</p>
        <div class="cdl-01__meter" aria-hidden="true"><i style="--w:41%"></i></div>
        <p class="cdl-01__sub">UK 22% · CA 12% · AU 9%</p>
      </article>
      <article class="cdl-01__tile" style="--i:6">
        <h3>P95 latency</h3>
        <p class="cdl-01__num">184<small> ms</small></p>
        <p class="cdl-01__delta cdl-01__down">▼ 23 ms this week</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-01,
.cdl-01 *,
.cdl-01 *::before,
.cdl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-01 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.16 0.028 288);
  --card: oklch(0.215 0.03 288);
  --edge: oklch(0.31 0.035 288);
  --ink: oklch(0.95 0.01 288);
  --mut: oklch(0.68 0.03 288);
  --acc: oklch(0.72 0.17 295);
  --acc2: oklch(0.78 0.14 195);
  --good: oklch(0.78 0.16 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cdl-01__stage {
  width: 100%;
  height: 100vh;
  padding: 22px;
  background: radial-gradient(120% 90% at 85% -10%,oklch(0.28 0.07 295 / .55),transparent 60%),radial-gradient(90% 80% at -10% 110%,oklch(0.24 0.06 200 / .45),transparent 55%),var(--bg);
  border: 1px solid var(--edge);
}

.cdl-01__top {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13.5px;
  letter-spacing: .02em;
  margin-bottom: 16px;
}

.cdl-01__mark {
  width: 20px;
  height: 20px;
  border-radius: 6px;
  background: conic-gradient(from 220deg,var(--acc),var(--acc2));
}

.cdl-01__live {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--good);
  padding: 5px 11px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklch,var(--good) 35%,transparent);
  background: color-mix(in oklch,var(--good) 12%,transparent);
}

.cdl-01__live i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--good);
  animation: cdl01-pulse 2s infinite;
}

@keyframes cdl01-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 color-mix(in oklch,var(--good) 55%,transparent);
  }

  70% {
    box-shadow: 0 0 0 7px transparent;
  }
}

.cdl-01__board {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(4,minmax(0,1fr));
  grid-auto-rows: 122px;
}

.cdl-01__tile {
  position: relative;
  overflow: hidden;
  border-radius: 16px;
  padding: 16px 18px;
  background: linear-gradient(160deg,color-mix(in oklch,var(--card) 92%,white) 0%,var(--card) 55%);
  border: 1px solid var(--edge);
  display: flex;
  flex-direction: column;
  gap: 8px;
  opacity: 1;
  translate: 0 0;
  transition: opacity .5s ease,translate .5s cubic-bezier(.2,.7,.2,1),scale .3s ease,filter .3s ease,border-color .3s ease;
  transition-delay: calc(var(--i)*55ms),calc(var(--i)*55ms),0s,0s,0s;
}

@starting-style {
  .cdl-01__tile {
    opacity: 0;
    translate: 0 14px;
  }
}

.cdl-01__tile:hover {
  border-color: color-mix(in oklch,var(--acc) 55%,var(--edge));
}

.cdl-01__board:has(.cdl-01__tile:hover) .cdl-01__tile:not(:hover) {
  opacity: .55;
  scale: .985;
  filter: saturate(.8);
}

.cdl-01__hero {
  grid-column: span 2;
  grid-row: span 2;
}

.cdl-01__wide {
  grid-column: span 2;
}

.cdl-01__tall {
  grid-row: span 2;
}

.cdl-01__tile h3 {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-01__big {
  font-size: clamp(30px,5cqi,44px);
  font-weight: 700;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
  display: flex;
  align-items: baseline;
  gap: 12px;
  flex-wrap: wrap;
}

.cdl-01__num {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
}

.cdl-01__num small {
  font-size: 14px;
  color: var(--mut);
  font-weight: 600;
}

.cdl-01__sub {
  font-size: 12px;
  color: var(--mut);
}

.cdl-01__delta {
  font-size: 12.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cdl-01__up {
  color: var(--good);
}

.cdl-01__down {
  color: var(--acc2);
}

.cdl-01__area {
  margin-top: auto;
  height: 78px;
  position: relative;
}

.cdl-01__area i {
  position: absolute;
  inset: 0;
  clip-path: polygon(0 78%,9% 66%,18% 71%,28% 52%,38% 58%,48% 40%,58% 47%,68% 30%,78% 36%,88% 16%,100% 22%,100% 100%,0 100%);
  background: linear-gradient(to top,color-mix(in oklch,var(--acc) 8%,transparent),color-mix(in oklch,var(--acc) 55%,transparent));
}

.cdl-01__spark {
  margin-top: auto;
  display: flex;
  align-items: flex-end;
  gap: 5px;
  height: 44px;
}

.cdl-01__spark i {
  flex: 1;
  height: var(--h);
  border-radius: 3px 3px 0 0;
  background: color-mix(in oklch,var(--acc) 60%,transparent);
  transform-origin: bottom;
  animation: cdl01-rise .7s cubic-bezier(.2,.7,.2,1) backwards;
}

.cdl-01__spark i:last-child {
  background: var(--acc);
}

.cdl-01__bars {
  margin-top: auto;
  display: flex;
  align-items: flex-end;
  gap: 7px;
  height: 56px;
}

.cdl-01__bars i {
  flex: 1;
  height: var(--h);
  border-radius: 4px 4px 0 0;
  background: linear-gradient(to top,color-mix(in oklch,var(--acc2) 35%,transparent),var(--acc2));
  transform-origin: bottom;
  animation: cdl01-rise .7s cubic-bezier(.2,.7,.2,1) backwards;
  animation-delay: calc(var(--i,0)*1ms + .25s);
}

@keyframes cdl01-rise {
  from {
    scale: 1 0;
  }
}

.cdl-01__ringwrap {
  display: grid;
  place-items: center;
  flex: 1;
}

.cdl-01__ring {
  position: relative;
  width: 84px;
  aspect-ratio: 1;
  display: grid;
  place-items: center;
}

.cdl-01__ring::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(var(--good) 0 99.98%,oklch(0.3 0.03 288) 0);
  mask: radial-gradient(circle at 50% 50%,transparent 54%,black 55%);
}

.cdl-01__ring b {
  position: relative;
  font-size: 15px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cdl-01__ring b small {
  font-size: 10px;
  color: var(--mut);
}

.cdl-01__feed {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 13px;
  overflow: hidden;
}

.cdl-01__feed li {
  display: flex;
  gap: 10px;
  align-items: flex-start;
}

.cdl-01__feed b {
  display: block;
  font-size: 12.5px;
  font-weight: 600;
}

.cdl-01__feed span {
  font-size: 11px;
  color: var(--mut);
}

.cdl-01__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--good);
  margin-top: 4px;
  flex: none;
}

.cdl-01__d2 {
  background: var(--acc);
}

.cdl-01__d3 {
  background: var(--acc2);
}

.cdl-01__meter {
  height: 6px;
  border-radius: 999px;
  background: oklch(0.29 0.03 288);
  overflow: hidden;
}

.cdl-01__meter i {
  display: block;
  height: 100%;
  width: var(--w);
  border-radius: inherit;
  background: linear-gradient(90deg,var(--acc),var(--acc2));
}

@container (max-width: 680px) {
  .cdl-01__board {
    grid-template-columns: repeat(2,minmax(0,1fr));
  }

  .cdl-01__wide,
    .cdl-01__hero {
    grid-column: span 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-01 * {
    animation: none !important;
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
