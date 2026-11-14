---
source: "codefronts"
url: "https://codefronts.com/layouts/css-bento-grid-layouts/saas-feature-value-prop-matrix/"
title: "SaaS Feature Value-Prop Matrix"
section: "layouts"
category: "css-bento-grid-layouts"
category_name: "CSS Bento Grid Layouts"
description: "The bento grid layout for SaaS landing pages that over 60% of modern startups use to break down complex features without walls of text: one large…"
has_js: "true"
---

Here's a working CSS Bento Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Feature Value-Prop Matrix
Source: https://codefronts.com/layouts/css-bento-grid-layouts/saas-feature-value-prop-matrix/

The bento grid layout for SaaS landing pages that over 60% of modern startups use to break down complex features without walls of text: one large core-feature block with an in-card UI mock, a real-time activity block, and smaller cells for integrations, a testimonial and pricing. Variant A adds the Linear-style cursor-tracked spotlight border; variant B is a pure-CSS version with a living animated bar chart and scrolling activity feed.
## HTML
```html
<div class="bgl-02-group">
<section class="bgl-02a" aria-labelledby="bgl-02a-h">
  <div class="bgl-02a__grid" id="bgl-02a-grid">
    <article class="bgl-02a__card bgl-02a__core">
      <h2 class="bgl-02a__h" id="bgl-02a-h">One inbox for every deploy</h2>
      <p class="bgl-02a__p">Approvals, rollbacks and incident threads, unified across every environment your team ships to.</p>
      <div class="bgl-02a__mock" aria-hidden="true">
        <div class="bgl-02a__row"><span class="bgl-02a__dot" style="background:#4ade80"></span>production &mdash; deploy #4812 live<em>2m</em></div>
        <div class="bgl-02a__row"><span class="bgl-02a__dot" style="background:#facc15"></span>staging &mdash; awaiting approval<em>9m</em></div>
        <div class="bgl-02a__row"><span class="bgl-02a__dot" style="background:#818cf8"></span>preview &mdash; PR #229 built<em>21m</em></div>
      </div>
    </article>
    <article class="bgl-02a__card"><h3 class="bgl-02a__t"><span class="bgl-02a__live" aria-hidden="true"></span>Real-time activity</h3><p class="bgl-02a__p">1,284 events streamed in the last hour across 12 services.</p></article>
    <article class="bgl-02a__card"><h3 class="bgl-02a__t">40+ integrations</h3><div class="bgl-02a__tiles" aria-hidden="true"><span>Sl</span><span>Gh</span><span>Ln</span><span>Dd</span><span>Pg</span><span>+35</span></div></article>
    <article class="bgl-02a__card"><blockquote class="bgl-02a__q">&ldquo;We cut incident response time by 60% in the first month.&rdquo;</blockquote><p class="bgl-02a__by">&mdash; Maya R., Platform Lead</p></article>
    <article class="bgl-02a__card"><h3 class="bgl-02a__t">Free for 10 seats</h3><p class="bgl-02a__p">Then $12 per seat. No usage caps, ever.</p><a class="bgl-02a__cta" href="#">Start free</a></article>
  </div>
</section>
<section class="bgl-02b" aria-labelledby="bgl-02b-h">
  <div class="bgl-02b__grid">
    <article class="bgl-02b__card bgl-02b__core">
      <h2 class="bgl-02b__h" id="bgl-02b-h">Revenue you can watch grow</h2>
      <p class="bgl-02b__p">Live MRR, churn and expansion in one board &mdash; refreshed every 30 seconds.</p>
      <div class="bgl-02b__chart" role="img" aria-label="Bar chart: monthly recurring revenue rising across seven months">
        <span style="--h:.35"></span><span style="--h:.48"></span><span style="--h:.42"></span><span style="--h:.6"></span><span style="--h:.72"></span><span style="--h:.66"></span><span style="--h:.92"></span>
      </div>
    </article>
    <article class="bgl-02b__card bgl-02b__feed" aria-label="Recent activity feed">
      <h3 class="bgl-02b__t">Activity</h3>
      <div class="bgl-02b__scroller">
        <ul class="bgl-02b__list">
          <li>Acme upgraded to Scale &mdash; +$490</li><li>New signup from Berlin</li><li>Invoice #2291 paid</li><li>Nova added 12 seats</li><li>Trial converted &mdash; +$99</li>
        </ul>
        <ul class="bgl-02b__list" aria-hidden="true">
          <li>Acme upgraded to Scale &mdash; +$490</li><li>New signup from Berlin</li><li>Invoice #2291 paid</li><li>Nova added 12 seats</li><li>Trial converted &mdash; +$99</li>
        </ul>
      </div>
    </article>
    <article class="bgl-02b__card"><p class="bgl-02b__big">99.99%</p><p class="bgl-02b__p">Uptime SLA on every plan</p></article>
    <article class="bgl-02b__card"><p class="bgl-02b__big">2 min</p><p class="bgl-02b__p">Median time to first dashboard</p></article>
  </div>
</section>
</div>
```
## CSS
```css
.bgl-02-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.bgl-02-group > section {
  flex: 1 1 480px;
  min-width: 320px;
}

.bgl-02a,
.bgl-02a *,
.bgl-02a *::before,
.bgl-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-02a {
  width: 100%;
  min-height: 100vh;
  --glow: oklch(0.7 0.17 285);
  --gap: 16px;
  --radius: 18px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #0b0b12;
  color: #ecebf3;
}

.bgl-02a__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(150px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-02a__card {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  padding: 26px;
  border-radius: var(--radius);
  background: #12121c;
  border: 1px solid rgba(255,255,255,.07);
  transition: transform .3s;
}

.bgl-02a__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(320px circle at var(--mx,50%) var(--my,50%),color-mix(in oklab,var(--glow) 16%,transparent),transparent 70%);
  opacity: 0;
  transition: opacity .35s;
  pointer-events: none;
  z-index: 0;
}

.bgl-02a__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: radial-gradient(280px circle at var(--mx,50%) var(--my,50%),var(--glow),transparent 70%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity .35s;
  pointer-events: none;
  z-index: 0;
}

.bgl-02a__card:hover {
  transform: translateY(-2px);
}

.bgl-02a__card:hover::before,
.bgl-02a__card:hover::after {
  opacity: 1;
}

.bgl-02a__card>* {
  position: relative;
  z-index: 1;
}

.bgl-02a__core {
  grid-column: span 8;
  grid-row: span 2;
  justify-content: flex-start;
  gap: 14px;
  padding: 34px;
}

.bgl-02a__h {
  font-size: clamp(26px,3.4cqw,38px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  text-wrap: pretty;
}

.bgl-02a__p {
  font-size: 14.5px;
  line-height: 1.6;
  color: rgba(236,235,243,.6);
  max-width: 52ch;
  text-wrap: pretty;
}

.bgl-02a__mock {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 16px;
  border-radius: 12px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.06);
  font-size: 13.5px;
}

.bgl-02a__row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 8px;
  background: rgba(255,255,255,.04);
}

.bgl-02a__row em {
  margin-left: auto;
  font-style: normal;
  color: rgba(236,235,243,.4);
}

.bgl-02a__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex: none;
}

.bgl-02a__t {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16.5px;
  font-weight: 700;
}

.bgl-02a__live {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4ade80;
  box-shadow: 0 0 0 0 rgba(74,222,128,.6);
  animation: bgl-02a-pulse 2s infinite;
}

.bgl-02a__tiles {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.bgl-02a__tiles span {
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 10px;
  font-size: 12.5px;
  font-weight: 700;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.08);
}

.bgl-02a__q {
  font-size: 15.5px;
  line-height: 1.55;
  font-weight: 600;
  text-wrap: pretty;
}

.bgl-02a__by {
  font-size: 13px;
  color: rgba(236,235,243,.5);
}

.bgl-02a__cta {
  align-self: flex-start;
  font-size: 14px;
  font-weight: 700;
  color: #0b0b12;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 9999px;
  background: var(--glow);
  transition: transform .25s;
}

.bgl-02a__cta:hover {
  transform: translateY(-2px);
}

.bgl-02a__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@keyframes bgl-02a-pulse {
  70% {
    box-shadow: 0 0 0 9px rgba(74,222,128,0);
  }

  100% {
    box-shadow: 0 0 0 0 rgba(74,222,128,0);
  }
}

@container (max-width: 880px) {
  .bgl-02a__core {
    grid-column: span 12;
  }

  .bgl-02a__card {
    grid-column: span 6;
  }

  .bgl-02a__core {
    grid-column: span 12;
  }
}

@container (max-width: 560px) {
  .bgl-02a__card,
    .bgl-02a__core {
    grid-column: span 12;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-02a__card,
    .bgl-02a__cta {
    transition: none;
  }

  .bgl-02a__live {
    animation: none;
  }

  .bgl-02a__card:hover {
    transform: none;
  }
}

.bgl-02b,
.bgl-02b *,
.bgl-02b *::before,
.bgl-02b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-02b {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.65 0.15 165);
  --gap: 16px;
  --radius: 18px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #f6f8f7;
  color: #15201b;
}

.bgl-02b__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(150px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-02b__card {
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 8px;
  padding: 26px;
  border-radius: var(--radius);
  background: #fff;
  border: 1px solid rgba(21,32,27,.08);
  transition: transform .3s,box-shadow .3s;
}

.bgl-02b__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 16px 30px -20px rgba(21,32,27,.3);
}

.bgl-02b__core {
  grid-column: span 8;
  grid-row: span 2;
  justify-content: flex-start;
  gap: 12px;
  padding: 32px;
}

.bgl-02b__h {
  font-size: clamp(24px,3cqw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
  text-wrap: pretty;
}

.bgl-02b__p {
  font-size: 14.5px;
  line-height: 1.6;
  color: rgba(21,32,27,.6);
  text-wrap: pretty;
}

.bgl-02b__chart {
  margin-top: auto;
  display: flex;
  align-items: flex-end;
  gap: 10px;
  height: 170px;
  padding: 16px;
  border-radius: 12px;
  background: color-mix(in oklab,var(--accent) 7%,white);
}

.bgl-02b__chart span {
  flex: 1;
  height: 100%;
  border-radius: 6px 6px 3px 3px;
  background: linear-gradient(180deg,var(--accent),color-mix(in oklab,var(--accent) 60%,#0f5132));
  transform: scaleY(var(--h));
  transform-origin: bottom;
  animation: bgl-02b-grow .9s cubic-bezier(.2,.9,.2,1) backwards;
}

.bgl-02b__chart span:nth-child(2) {
  animation-delay: .08s;
}

.bgl-02b__chart span:nth-child(3) {
  animation-delay: .16s;
}

.bgl-02b__chart span:nth-child(4) {
  animation-delay: .24s;
}

.bgl-02b__chart span:nth-child(5) {
  animation-delay: .32s;
}

.bgl-02b__chart span:nth-child(6) {
  animation-delay: .4s;
}

.bgl-02b__chart span:nth-child(7) {
  animation-delay: .48s;
}

.bgl-02b__feed {
  grid-row: span 2;
  justify-content: flex-start;
}

.bgl-02b__t {
  font-size: 16px;
  font-weight: 700;
}

.bgl-02b__scroller {
  flex: 1;
  overflow: hidden;
  -webkit-mask: linear-gradient(transparent,#000 15%,#000 85%,transparent);
  mask: linear-gradient(transparent,#000 15%,#000 85%,transparent);
}

.bgl-02b__list {
  list-style: none;
  animation: bgl-02b-roll 12s linear infinite;
}

.bgl-02b__list li {
  padding: 11px 0;
  font-size: 13.5px;
  color: rgba(21,32,27,.7);
  border-bottom: 1px dashed rgba(21,32,27,.1);
}

.bgl-02b__feed:hover .bgl-02b__list {
  animation-play-state: paused;
}

.bgl-02b__big {
  font-size: clamp(30px,3.6cqw,40px);
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}

@keyframes bgl-02b-grow {
  from {
    transform: scaleY(0);
  }
}

@keyframes bgl-02b-roll {
  to {
    transform: translateY(-50%);
  }
}

@container (max-width: 880px) {
  .bgl-02b__core,
    .bgl-02b__feed {
    grid-column: span 12;
  }

  .bgl-02b__card {
    grid-column: span 6;
  }

  .bgl-02b__core,
    .bgl-02b__feed {
    grid-column: span 12;
  }

  .bgl-02b__feed {
    min-height: 260px;
  }
}

@container (max-width: 560px) {
  .bgl-02b__card,
    .bgl-02b__core,
    .bgl-02b__feed {
    grid-column: span 12;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-02b__card {
    transition: none;
  }

  .bgl-02b__chart span {
    animation: none;
  }

  .bgl-02b__list {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const grid = document.querySelector('#bgl-02a-grid'); if (!grid) return;
  const cards = grid.querySelectorAll('.bgl-02a__card');
  grid.addEventListener('pointermove', e => {
    for (const card of cards) {
      const r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      card.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }
  });
})();

/* No JavaScript — bars grow via staggered scaleY keyframes (transform-origin:bottom), and the activity feed is a duplicated list on a -50% translateY marquee, masked with a soft fade and paused on hover. */
```
