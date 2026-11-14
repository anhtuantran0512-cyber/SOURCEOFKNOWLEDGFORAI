---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/feature-section-with-live-metric-counter-chips/"
title: "Feature Section with Live Metric Counter Chips"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Three proof-of-scale cards, each headed by a number that ramps from zero the first time the card enters the viewport — 99.99% uptime, 47ms P50, 2.4M events…"
has_js: "true"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with Live Metric Counter Chips
Source: https://codefronts.com/layouts/css-feature-sections/feature-section-with-live-metric-counter-chips/

Three proof-of-scale cards, each headed by a number that ramps from zero the first time the card enters the viewport — 99.99% uptime, 47ms P50, 2.4M events per minute — with stat chips underneath giving the supporting detail. The ramp is a registered custom property animated on a view() timeline where supported, with a 20-line IntersectionObserver ramp as the fallback for engines without scroll-driven animations.
## HTML
```html
<section class="fs-03" aria-labelledby="fs-03-heading">
  <div class="fs-03__hero" aria-hidden="true">
    <span class="fs-03__wordmark">SABLE//telemetry</span>
    <span class="fs-03__status"><i></i>all systems nominal</span>
  </div>

  <div class="fs-03__stage">
    <div class="fs-03__head">
      <p class="fs-03__eyebrow">[ why teams switch ]</p>
      <h2 class="fs-03__heading" id="fs-03-heading">Numbers we publish because we watch them</h2>
    </div>

    <ul class="fs-03__cards">
      <li class="fs-03__card" style="--target: 99">
        <p class="fs-03__label">Ingest availability</p>
        <p class="fs-03__metric" aria-hidden="true"><span class="fs-03__num"></span><span class="fs-03__unit">.99%</span></p>
        <p class="fs-03__sr">99.99 percent ingest availability over the last twelve months.</p>
        <h3 class="fs-03__ctitle">Writes never wait on a rebalance</h3>
        <p class="fs-03__prose">Three regions accept writes at once and reconcile behind the read path, so a node loss shows up in our incident log and nowhere else.</p>
        <ul class="fs-03__chips">
          <li>12mo trailing</li><li>Multi-region</li><li>No maintenance windows</li>
        </ul>
      </li>

      <li class="fs-03__card" style="--target: 47">
        <p class="fs-03__label">Query latency, P50</p>
        <p class="fs-03__metric" aria-hidden="true"><span class="fs-03__num"></span><span class="fs-03__unit">ms</span></p>
        <p class="fs-03__sr">Median query latency of 47 milliseconds.</p>
        <h3 class="fs-03__ctitle">Dashboards that answer while you look</h3>
        <p class="fs-03__prose">Columnar storage with per-tenant caches keeps the median under 50ms across a 30-day window, P99 under 380ms, measured from the client.</p>
        <ul class="fs-03__chips">
          <li>P99 380ms</li><li>30d window</li><li>Client-measured</li>
        </ul>
      </li>

      <li class="fs-03__card" style="--target: 2">
        <p class="fs-03__label">Sustained throughput</p>
        <p class="fs-03__metric" aria-hidden="true"><span class="fs-03__num"></span><span class="fs-03__unit">.4M events/min</span></p>
        <p class="fs-03__sr">2.4 million events per minute sustained.</p>
        <h3 class="fs-03__ctitle">Peak traffic is just Tuesday</h3>
        <p class="fs-03__prose">Ingest scales horizontally on the write path, so a product launch spike is absorbed without a queue backlog or a support ticket from us.</p>
        <ul class="fs-03__chips">
          <li>2.4M events/min</li><li>Auto-shard</li><li>Backpressure-free</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="fs-03__below" aria-hidden="true">status.sable.dev · methodology · sla</div>
</section>
```
## CSS
```css
@property --fs-03-n {
  syntax: "<integer>";
  inherits: true;
  initial-value: 0;
}

.fs-03 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #000000;
  --card: #0a0a0b;
  --card: oklch(0.16 0.004 285);
  --ink: #f4f4f6;
  --muted: #8b8b95;
  --muted: oklch(0.65 0.008 285);
  --rule: #232327;
  --rule: oklch(0.27 0.005 285);
  --accent: #ff3ec8;
  --accent: oklch(0.72 0.27 340);
  --font-display: "JetBrains Mono", "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-03 *,
.fs-03 *::before,
.fs-03 *::after {
  box-sizing: border-box;
}

.fs-03__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 16px;
  justify-content: space-between;
  align-items: center;
  padding: 14px 18px;
  border-block-end: 1px solid var(--rule);
  font: 500 11.5px/1 var(--font-display);
  letter-spacing: 0.06em;
  color: var(--muted);
}

.fs-03__wordmark {
  color: var(--ink);
}

.fs-03__status {
  display: inline-flex;
  align-items: center;
  gap: 7px;
}

.fs-03__status i {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: #35e08a;
  box-shadow: 0 0 8px #35e08a;
}

.fs-03__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 5vw, 56px) 14px;
}

.fs-03__head {
  inline-size: 100%;
  max-inline-size: 72rem;
  min-inline-size: 0;
  margin: 0 0 24px;
}

.fs-03__eyebrow {
  margin: 0 0 10px;
  font: 500 11px/1 var(--font-display);
  letter-spacing: 0.16em;
  color: var(--accent);
}

.fs-03__heading {
  margin: 0;
  font: 500 clamp(23px, 4vw, 34px)/1.15 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-03__cards {
  inline-size: 100%;
  max-inline-size: 72rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: 12px;
}

.fs-03__card {
  min-inline-size: 0;
  padding: 14px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 6px;
  position: relative;
  overflow: hidden;
}

.fs-03__card::before {
  content: "";
  position: absolute;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 1px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
}

.fs-03__card::after {
  content: "";
  position: absolute;
  inset-block-start: -60px;
  inset-inline-start: -40px;
  inline-size: 180px;
  block-size: 180px;
  border-radius: 50%;
  background: radial-gradient(circle, color-mix(in oklab, var(--accent) 22%, transparent), transparent 70%);
  pointer-events: none;
}

.fs-03__label {
  position: relative;
  margin: 0 0 8px;
  font: 500 10.5px/1 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.fs-03__metric {
  position: relative;
  display: flex;
  align-items: baseline;
  gap: 4px;
  margin: 0 0 12px;
  font-family: var(--font-display);
  font-variant-numeric: tabular-nums;
}

.fs-03__num {
  font-size: clamp(38px, 7vw, 56px);
  font-weight: 600;
  line-height: 0.95;
  letter-spacing: -0.04em;
  color: var(--accent);
  text-shadow: 0 0 22px color-mix(in oklab, var(--accent) 45%, transparent);
}

.fs-03__num {
  counter-reset: fs03n var(--fs-03-n);
}

.fs-03__num::after {
  content: counter(fs03n);
}

.fs-03__unit {
  font-size: 14px;
  font-weight: 500;
  color: var(--muted);
}

.fs-03__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  margin: 0;
}

.fs-03__ctitle {
  position: relative;
  margin: 0 0 8px;
  font: 600 15px/1.3 system-ui, sans-serif;
  letter-spacing: -0.01em;
}

.fs-03__prose {
  position: relative;
  margin: 0 0 14px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-03__chips {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.fs-03__chips li {
  padding: 5px 9px;
  font: 500 10.5px/1.3 var(--font-display);
  letter-spacing: 0.04em;
  color: color-mix(in oklab, var(--accent) 65%, var(--ink));
  border: 1px solid color-mix(in oklab, var(--accent) 35%, var(--rule));
  border-radius: 4px;
  background: color-mix(in oklab, var(--accent) 7%, transparent);
}

.fs-03__below {
  padding: 14px 18px;
  border-block-start: 1px solid var(--rule);
  font: 500 11px/1 var(--font-display);
  letter-spacing: 0.08em;
  color: var(--muted);
}

@supports (animation-timeline: view()) {
  .fs-03__card {
    animation: fs-03-ramp 1s linear both;
    animation-timeline: view();
    animation-range: entry 20% cover 45%;
  }

  .fs-03__card {
    --fs-03-n: 0;
  }

  @keyframes fs-03-ramp {
    from {
      --fs-03-n: 0;
    }

    to {
      --fs-03-n: var(--target);
    }
  }
}

@supports not (animation-timeline: view()) {
  .fs-03__card {
    --fs-03-n: var(--target);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-03__card {
    animation: none;
    --fs-03-n: var(--target);
  }
}

@media (prefers-color-scheme: light) {
  .fs-03 {
    --bg: #f7f7f8;
    --card: #ffffff;
    --ink: #101013;
    --muted: #5c5c66;
    --rule: #e2e2e6;
    --accent: #b60a86;
  }

  .fs-03__num {
    text-shadow: none;
  }
}

[data-theme="dark"] .fs-03 {
  --bg: #000000;
  --card: #0a0a0b;
  --ink: #f4f4f6;
  --muted: #8b8b95;
  --rule: #232327;
  --accent: #ff3ec8;
}
```

## JavaScript
```js
const cards = document.querySelectorAll('.fs-03__card');
const canCSS = CSS.supports('animation-timeline', 'view()');
if (cards.length && !canCSS && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const ramp = (card) => {
    const target = Number(getComputedStyle(card).getPropertyValue('--target')) || 0;
    const start = performance.now();
    const step = (now) => {
      const p = Math.min(1, (now - start) / 900);
      card.style.setProperty('--fs-03-n', String(Math.round(target * (1 - Math.pow(1 - p, 3)))));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { ramp(e.target); io.unobserve(e.target); } });
  }, { threshold: 0.35 });
  cards.forEach((c) => { c.style.setProperty('--fs-03-n', '0'); io.observe(c); });
}
```
