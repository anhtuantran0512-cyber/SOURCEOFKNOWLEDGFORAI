---
source: "codefronts"
url: "https://codefronts.com/layouts/css-bento-grid-layouts/analytics-dashboard-overview/"
title: "Analytics Dashboard Overview"
section: "layouts"
category: "css-bento-grid-layouts"
category_name: "CSS Bento Grid Layouts"
description: "The application-dashboard bento grid layout developers search for when building admin panels: a wide line graph across the top, a square single-number KPI…"
has_js: "true"
---

Here's a working CSS Bento Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Analytics Dashboard Overview
Source: https://codefronts.com/layouts/css-bento-grid-layouts/analytics-dashboard-overview/

The application-dashboard bento grid layout developers search for when building admin panels: a wide line graph across the top, a square single-number KPI widget with an animated count-up, a vertical recent-activity list and a quick-actions block — multiple distinct data types visible at once without mental fatigue. Variant B is a dark ops-console with a pure-CSS conic-gradient gauge and sparkline bars.
## HTML
```html
<div class="bgl-03-group">
<section class="bgl-03a" aria-labelledby="bgl-03a-h">
  <div class="bgl-03a__grid">
    <article class="bgl-03a__card bgl-03a__chart">
      <header class="bgl-03a__head"><h2 id="bgl-03a-h">Weekly active users</h2><span class="bgl-03a__delta">&#9650; 12.4%</span></header>
      <svg class="bgl-03a__svg" viewBox="0 0 400 120" preserveAspectRatio="none" role="img" aria-label="Line chart: weekly active users trending upward">
        <defs><linearGradient id="bgl-03a-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="oklch(0.62 0.19 262)" stop-opacity=".25"/><stop offset="1" stop-color="oklch(0.62 0.19 262)" stop-opacity="0"/></linearGradient></defs>
        <path d="M0,95 L50,80 L100,86 L150,60 L200,68 L250,42 L300,50 L350,26 L400,18 L400,120 L0,120 Z" fill="url(#bgl-03a-fill)"/>
        <polyline class="bgl-03a__line" points="0,95 50,80 100,86 150,60 200,68 250,42 300,50 350,26 400,18" fill="none" stroke="oklch(0.62 0.19 262)" stroke-width="2.5" stroke-linecap="round"/>
      </svg>
    </article>
    <article class="bgl-03a__card">
      <h3 class="bgl-03a__t">Revenue this month</h3>
      <p class="bgl-03a__kpi"><span id="bgl-03a-kpi" data-target="48250" data-duration="1400" aria-label="$48,250">$48,250</span></p>
      <p class="bgl-03a__sub">of $60,000 goal &mdash; 80%</p>
    </article>
    <article class="bgl-03a__card bgl-03a__list" aria-label="Recent activity">
      <h3 class="bgl-03a__t">Recent activity</h3>
      <ul class="bgl-03a__ul">
        <li><span class="bgl-03a__av" style="background:oklch(0.75 0.12 262)">JS</span><div><strong>Jonah S.</strong> exported Q3 report<em>4 min ago</em></div></li>
        <li><span class="bgl-03a__av" style="background:oklch(0.75 0.12 165)">AK</span><div><strong>Ana K.</strong> invited 3 teammates<em>18 min ago</em></div></li>
        <li><span class="bgl-03a__av" style="background:oklch(0.75 0.12 25)">RB</span><div><strong>Rui B.</strong> changed billing plan<em>1 h ago</em></div></li>
        <li><span class="bgl-03a__av" style="background:oklch(0.75 0.12 320)">TW</span><div><strong>Tess W.</strong> created dashboard &ldquo;Growth&rdquo;<em>2 h ago</em></div></li>
      </ul>
    </article>
    <article class="bgl-03a__card">
      <h3 class="bgl-03a__t">Quick actions</h3>
      <div class="bgl-03a__actions">
        <button type="button">+ New report</button><button type="button">Invite</button><button type="button">Export CSV</button>
      </div>
    </article>
  </div>
</section>
<section class="bgl-03b" aria-labelledby="bgl-03b-h">
  <div class="bgl-03b__grid">
    <article class="bgl-03b__card bgl-03b__gaugecard">
      <h2 class="bgl-03b__t" id="bgl-03b-h">API health</h2>
      <div class="bgl-03b__gauge" role="img" aria-label="Gauge: 98 percent healthy"><span>98%</span></div>
      <p class="bgl-03b__sub">3,412 checks in the last 5 min</p>
    </article>
    <article class="bgl-03b__card bgl-03b__wide">
      <h3 class="bgl-03b__t">Request volume <em>req/s per region</em></h3>
      <div class="bgl-03b__spark" aria-hidden="true">
        <i style="--h:.4"></i><i style="--h:.55"></i><i style="--h:.5"></i><i style="--h:.7"></i><i style="--h:.62"></i><i style="--h:.8"></i><i style="--h:.75"></i><i style="--h:.9"></i><i style="--h:.68"></i><i style="--h:.82"></i><i style="--h:.95"></i><i style="--h:.88"></i>
      </div>
    </article>
    <article class="bgl-03b__card"><h3 class="bgl-03b__t">p99 latency</h3><p class="bgl-03b__num">142<small>ms</small></p></article>
    <article class="bgl-03b__card"><h3 class="bgl-03b__t">Error rate</h3><p class="bgl-03b__num bgl-03b__ok">0.02<small>%</small></p></article>
    <article class="bgl-03b__card bgl-03b__uptime">
      <h3 class="bgl-03b__t">90-day uptime</h3>
      <div class="bgl-03b__dots" role="img" aria-label="Uptime history: 89 of 90 days fully operational">
        <b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="bgl-03b__down"></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b>
      </div>
    </article>
  </div>
</section>
</div>
```
## CSS
```css
.bgl-03-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.bgl-03-group > section {
  flex: 1 1 480px;
  min-width: 320px;
}

.bgl-03a,
.bgl-03a *,
.bgl-03a *::before,
.bgl-03a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-03a {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.62 0.19 262);
  --gap: 16px;
  --radius: 16px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #eef0f4;
  color: #1a2030;
}

.bgl-03a__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(150px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-03a__card {
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 24px;
  border-radius: var(--radius);
  background: #fff;
  border: 1px solid rgba(26,32,48,.07);
  box-shadow: 0 1px 2px rgba(26,32,48,.05);
  transition: transform .3s,box-shadow .3s;
}

.bgl-03a__card:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 28px -18px rgba(26,32,48,.3);
}

.bgl-03a__chart {
  grid-column: span 8;
  grid-row: span 2;
}

.bgl-03a__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
}

.bgl-03a__head h2 {
  font-size: 17px;
  font-weight: 700;
}

.bgl-03a__delta {
  font-size: 13px;
  font-weight: 700;
  color: oklch(0.55 0.15 155);
  background: oklch(0.95 0.04 155);
  padding: 4px 10px;
  border-radius: 9999px;
}

.bgl-03a__svg {
  flex: 1;
  width: 100%;
  min-height: 160px;
}

.bgl-03a__line {
  stroke-dasharray: 900;
  stroke-dashoffset: 900;
  animation: bgl-03a-draw 1.6s cubic-bezier(.4,0,.2,1) .2s forwards;
}

.bgl-03a__t {
  font-size: 14px;
  font-weight: 700;
  color: rgba(26,32,48,.55);
  text-transform: uppercase;
  letter-spacing: .06em;
}

.bgl-03a__kpi {
  font-size: clamp(32px,3.8cqw,42px);
  font-weight: 800;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.bgl-03a__sub {
  font-size: 13.5px;
  color: rgba(26,32,48,.55);
}

.bgl-03a__list {
  grid-row: span 2;
}

.bgl-03a__ul {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.bgl-03a__ul li {
  display: flex;
  gap: 12px;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid rgba(26,32,48,.07);
  font-size: 13.5px;
  line-height: 1.45;
}

.bgl-03a__ul li:last-child {
  border-bottom: none;
}

.bgl-03a__ul em {
  display: block;
  font-style: normal;
  font-size: 12px;
  color: rgba(26,32,48,.45);
}

.bgl-03a__av {
  flex: none;
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
}

.bgl-03a__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.bgl-03a__actions button {
  font-size: 13.5px;
  font-weight: 700;
  font-family: inherit;
  color: var(--accent);
  padding: 10px 16px;
  border: 1px solid color-mix(in oklab,var(--accent) 35%,transparent);
  border-radius: 10px;
  background: color-mix(in oklab,var(--accent) 6%,white);
  cursor: pointer;
  transition: transform .2s,background .2s;
}

.bgl-03a__actions button:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--accent) 12%,white);
}

.bgl-03a__actions button:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@keyframes bgl-03a-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@container (max-width: 880px) {
  .bgl-03a__chart,
    .bgl-03a__list {
    grid-column: span 12;
  }

  .bgl-03a__card {
    grid-column: span 6;
  }

  .bgl-03a__chart,
    .bgl-03a__list {
    grid-column: span 12;
  }
}

@container (max-width: 560px) {
  .bgl-03a__card,
    .bgl-03a__chart,
    .bgl-03a__list {
    grid-column: span 12;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-03a__card,
    .bgl-03a__actions button {
    transition: none;
  }

  .bgl-03a__line {
    animation: none;
    stroke-dashoffset: 0;
  }
}

.bgl-03b,
.bgl-03b *,
.bgl-03b *::before,
.bgl-03b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --bgl03b-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.bgl-03b {
  width: 100%;
  min-height: 100vh;
  --grn: oklch(0.75 0.16 155);
  --gap: 14px;
  --radius: 14px;
  container-type: inline-size;
  font-family: ui-monospace,'Segoe UI',monospace;
  padding: 48px 24px;
  background: #0c1210;
  color: #d9efe4;
}

.bgl-03b__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(140px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-03b__card {
  grid-column: span 3;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  padding: 22px;
  border-radius: var(--radius);
  background: #101a16;
  border: 1px solid rgba(217,239,228,.09);
  transition: border-color .3s;
}

.bgl-03b__card:hover {
  border-color: color-mix(in oklab,var(--grn) 45%,transparent);
}

.bgl-03b__gaugecard {
  grid-column: span 4;
  grid-row: span 2;
  align-items: center;
  text-align: center;
  gap: 14px;
}

.bgl-03b__gauge {
  --bgl03b-p: 98%;
  position: relative;
  display: grid;
  place-items: center;
  width: 150px;
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(var(--grn) var(--bgl03b-p),rgba(217,239,228,.1) 0);
  transition: --bgl03b-p 1.4s cubic-bezier(.4,0,.2,1);
  animation: bgl-03b-fill 1.4s cubic-bezier(.4,0,.2,1) backwards;
}

.bgl-03b__gauge::before {
  content: "";
  position: absolute;
  inset: 10px;
  border-radius: 50%;
  background: #101a16;
}

.bgl-03b__gauge span {
  position: relative;
  font-size: 30px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.bgl-03b__wide {
  grid-column: span 8;
}

.bgl-03b__t {
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(217,239,228,.55);
}

.bgl-03b__t em {
  font-style: normal;
  text-transform: none;
  letter-spacing: 0;
  color: rgba(217,239,228,.35);
  margin-left: 8px;
}

.bgl-03b__spark {
  display: flex;
  align-items: flex-end;
  gap: 6px;
  height: 90px;
}

.bgl-03b__spark i {
  flex: 1;
  height: 100%;
  border-radius: 3px;
  background: linear-gradient(180deg,var(--grn),color-mix(in oklab,var(--grn) 45%,#0c1210));
  transform: scaleY(var(--h));
  transform-origin: bottom;
  animation: bgl-03b-grow .8s cubic-bezier(.2,.9,.2,1) backwards;
}

.bgl-03b__spark i:nth-child(odd) {
  animation-delay: .1s;
}

.bgl-03b__spark i:nth-child(3n) {
  animation-delay: .2s;
}

.bgl-03b__num {
  font-size: clamp(28px,3.4cqw,38px);
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.bgl-03b__num small {
  font-size: .45em;
  color: rgba(217,239,228,.45);
  margin-left: 2px;
}

.bgl-03b__ok {
  color: var(--grn);
}

.bgl-03b__sub {
  font-size: 12.5px;
  color: rgba(217,239,228,.45);
}

.bgl-03b__uptime {
  grid-column: span 6;
}

.bgl-03b__dots {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.bgl-03b__dots b {
  width: 14px;
  height: 26px;
  border-radius: 3px;
  background: var(--grn);
  opacity: .85;
}

.bgl-03b__down {
  background: oklch(0.65 0.2 25)!important;
}

@keyframes bgl-03b-fill {
  from {
    --bgl03b-p: 0%;
  }
}

@keyframes bgl-03b-grow {
  from {
    transform: scaleY(0);
  }
}

@container (max-width: 880px) {
  .bgl-03b__gaugecard,
    .bgl-03b__wide,
    .bgl-03b__uptime {
    grid-column: span 12;
  }

  .bgl-03b__card {
    grid-column: span 6;
  }

  .bgl-03b__gaugecard,
    .bgl-03b__wide,
    .bgl-03b__uptime {
    grid-column: span 12;
  }
}

@container (max-width: 560px) {
  .bgl-03b__card,
    .bgl-03b__gaugecard,
    .bgl-03b__wide,
    .bgl-03b__uptime {
    grid-column: span 12;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-03b__gauge,
    .bgl-03b__spark i {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const el = document.querySelector('#bgl-03a-kpi'); if (!el) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return; // real value already in markup
  const target = +el.dataset.target, dur = +el.dataset.duration;
  const fmt = n => '$' + Math.round(n).toLocaleString('en-US');
  const io = new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) return;
    io.disconnect();
    const t0 = performance.now();
    const tick = now => {
      const p = Math.min((now - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(target * eased);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }, { threshold: .4 });
  io.observe(el);
})();

/* No JavaScript — the gauge is a conic-gradient whose registered @property percentage animates 0→98% on load; sparkline bars grow with staggered scaleY keyframes. */
```
