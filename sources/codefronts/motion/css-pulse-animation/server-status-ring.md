---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/server-status-ring/"
title: "Server Status Ring"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A DevOps operations-center dashboard with server-status rings — 4 tiles each showing a service, its uptime, and a concentric pulsing ring indicating health…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Server Status Ring
Source: https://codefronts.com/motion/css-pulse-animation/server-status-ring/

A DevOps operations-center dashboard with server-status rings — 4 tiles each showing a service, its uptime, and a concentric pulsing ring indicating health status. Terminal-green healthy state (#22c55e) with amber warning (#f59e0b) tile mixed in for realism. Datadog / PagerDuty / Grafana ops-center aesthetic with all-uppercase JetBrains Mono labels, deep-forest surface (#0a3a1f), and hostname / region metadata.
## HTML
```html
<div class="pl-08">
  <header class="pl-08__head">
    <div class="pl-08__brand">
      <span class="pl-08__logo" aria-hidden="true">◆</span>
      <span>opswatch</span>
    </div>
    <div class="pl-08__region-strip">
      <span class="pl-08__region-item">us-east-1</span>
      <span class="pl-08__region-item pl-08__region-item--sel">eu-west-2</span>
      <span class="pl-08__region-item">ap-south-1</span>
    </div>
    <div class="pl-08__meta">
      <span class="pl-08__meta-dot" aria-label="Live"></span>
      <span>Live · 14:22 UTC</span>
    </div>
  </header>
  <main class="pl-08__grid">
    <article class="pl-08__tile" role="group" aria-label="api-gateway, uptime 99.98%, healthy">
      <div class="pl-08__ring pl-08__ring--ok">
        <div class="pl-08__ring-inner">
          <span class="pl-08__uptime">99.98<em>%</em></span>
          <span class="pl-08__ring-label">UPTIME</span>
        </div>
      </div>
      <div class="pl-08__tile-name">api-gateway</div>
      <div class="pl-08__tile-meta">
        <span class="pl-08__tag pl-08__tag--ok">HEALTHY</span>
        <span>p95 · 142ms</span>
      </div>
    </article>
    <article class="pl-08__tile" role="group" aria-label="auth-service, uptime 99.99%, healthy">
      <div class="pl-08__ring pl-08__ring--ok">
        <div class="pl-08__ring-inner">
          <span class="pl-08__uptime">99.99<em>%</em></span>
          <span class="pl-08__ring-label">UPTIME</span>
        </div>
      </div>
      <div class="pl-08__tile-name">auth-service</div>
      <div class="pl-08__tile-meta">
        <span class="pl-08__tag pl-08__tag--ok">HEALTHY</span>
        <span>p95 · 38ms</span>
      </div>
    </article>
    <article class="pl-08__tile" role="group" aria-label="billing-svc, uptime 98.42%, degraded">
      <div class="pl-08__ring pl-08__ring--warn">
        <div class="pl-08__ring-inner">
          <span class="pl-08__uptime">98.42<em>%</em></span>
          <span class="pl-08__ring-label">UPTIME</span>
        </div>
      </div>
      <div class="pl-08__tile-name">billing-svc</div>
      <div class="pl-08__tile-meta">
        <span class="pl-08__tag pl-08__tag--warn">DEGRADED</span>
        <span>p95 · 890ms ↑</span>
      </div>
    </article>
    <article class="pl-08__tile" role="group" aria-label="search-index, uptime 99.94%, healthy">
      <div class="pl-08__ring pl-08__ring--ok">
        <div class="pl-08__ring-inner">
          <span class="pl-08__uptime">99.94<em>%</em></span>
          <span class="pl-08__ring-label">UPTIME</span>
        </div>
      </div>
      <div class="pl-08__tile-name">search-index</div>
      <div class="pl-08__tile-meta">
        <span class="pl-08__tag pl-08__tag--ok">HEALTHY</span>
        <span>p95 · 76ms</span>
      </div>
    </article>
  </main>
</div>
```
## CSS
```css
.pl-08 {
  --bg: #0a3a1f;
  --card: #08301a;
  --card-hover: #0c4025;
  --ink: #d1fae5;
  --sub: #6ee7b7;
  --ok: #22c55e;
  --ok-dim: rgba(34,197,94,.35);
  --warn: #f59e0b;
  --warn-dim: rgba(245,158,11,.4);
  --line: rgba(34,197,94,.14);
  font-family: 'JetBrains Mono',ui-monospace,'Menlo','Consolas',monospace;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 16px;
  padding: 24px;
  background: radial-gradient(60% 100% at 20% 10%, rgba(34,197,94,.06) 0%, transparent 60%), var(--bg);
  color: var(--ink);
}

.pl-08 *,
.pl-08 *::before,
.pl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-08 ::selection {
  background: var(--ok);
  color: var(--bg);
}

.pl-08__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 12px 18px;
  border-radius: 9px;
  background: var(--card);
  border: 1px solid var(--line);
}

.pl-08__brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.pl-08__logo {
  color: var(--ok);
  font-size: .9rem;
}

.pl-08__region-strip {
  display: flex;
  gap: 4px;
}

.pl-08__region-item {
  padding: 5px 10px;
  border-radius: 5px;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .04em;
  color: var(--sub);
  cursor: pointer;
  transition: background .15s ease;
}

.pl-08__region-item:hover {
  background: var(--card-hover);
}

.pl-08__region-item--sel {
  background: var(--card-hover);
  color: var(--ink);
}

.pl-08__meta {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .74rem;
  color: var(--sub);
  font-variant-numeric: tabular-nums;
}

.pl-08__meta-dot {
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--ok);
  animation: pl-08-blink 1.4s ease-in-out infinite;
}

@keyframes pl-08-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .4;
  }
}

.pl-08__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 12px;
}

@media (max-width: 820px) {
  .pl-08__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

.pl-08__tile {
  padding: 18px 14px;
  border-radius: 10px;
  background: var(--card);
  border: 1px solid var(--line);
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: background .18s ease,border-color .18s ease;
}

.pl-08__tile:hover {
  background: var(--card-hover);
}
/* Status ring with pulsing pseudo-elements */

.pl-08__ring {
  position: relative;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 2px solid var(--ok);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
}

.pl-08__ring::before,
.pl-08__ring::after {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid currentColor;
  color: var(--ok-dim);
  pointer-events: none;
  animation: pl-08-ring 2s ease-out infinite;
}

.pl-08__ring::after {
  animation-delay: 1s;
}

.pl-08__ring--warn {
  border-color: var(--warn);
}

.pl-08__ring--warn::before,
.pl-08__ring--warn::after {
  color: var(--warn-dim);
  animation-duration: 1.2s;
}

.pl-08__ring--warn::after {
  animation-delay: .6s;
}

@keyframes pl-08-ring {
  0% {
    transform: scale(1);
    opacity: .7;
  }

  70% {
    transform: scale(1.35);
    opacity: 0;
  }

  100% {
    transform: scale(1.4);
    opacity: 0;
  }
}

.pl-08__ring-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  line-height: 1;
}

.pl-08__uptime {
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
}

.pl-08__uptime em {
  font-size: .65rem;
  font-style: normal;
  color: var(--sub);
  margin-left: 1px;
}

.pl-08__ring-label {
  font-size: .55rem;
  font-weight: 700;
  letter-spacing: .14em;
  color: var(--sub);
  margin-top: 3px;
}

.pl-08__tile-name {
  font-size: .85rem;
  font-weight: 700;
  letter-spacing: -.005em;
  color: var(--ink);
  margin-bottom: 8px;
}

.pl-08__tile-meta {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  font-size: .68rem;
  color: var(--sub);
  font-variant-numeric: tabular-nums;
}

.pl-08__tag {
  padding: 2px 7px;
  border-radius: 3px;
  font-size: .6rem;
  font-weight: 800;
  letter-spacing: .1em;
}

.pl-08__tag--ok {
  background: rgba(34,197,94,.15);
  color: var(--ok);
}

.pl-08__tag--warn {
  background: rgba(245,158,11,.15);
  color: var(--warn);
}

@media (prefers-reduced-motion: reduce) {
  .pl-08__ring::before,
    .pl-08__ring::after,
    .pl-08__meta-dot {
    animation: none!important;
  }

  .pl-08__ring::before,
    .pl-08__ring::after {
    opacity: 0!important;
  }
}
```
