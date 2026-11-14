---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/live-status-pulse-card/"
title: "Live Status Pulse Card"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The online dot, engineered: concentric rings expanding on a staggered 2.4-second loop, a core that brightens on the same clock, and status colour driven…"
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Status Pulse Card
Source: https://codefronts.com/components/css-animated-cards/live-status-pulse-card/

The online dot, engineered: concentric rings expanding on a staggered 2.4-second loop, a core that brightens on the same clock, and status colour driven entirely by one data attribute so operational/degraded/down are a single-token swap. Includes the uptime bar with per-day tooltips that every status page needs.
## HTML
```html
<section class="ac-20" aria-label="Live status pulse card demo">
  <div class="ac-20__stage">
    <article class="ac-20__card">
      <header class="ac-20__top" data-status="ok">
        <span class="ac-20__dot" aria-hidden="true"></span>
        <div>
          <h2 class="ac-20__title">All systems operational</h2>
          <p class="ac-20__sub" role="status">Updated 14 seconds ago · 99.982% 90-day uptime</p>
        </div>
        <span class="ac-20__live" aria-hidden="true">Live</span>
      </header>
      <ul class="ac-20__list" role="list">
        <li class="ac-20__row" data-status="ok">
          <span class="ac-20__pip" aria-hidden="true"></span>
          <span class="ac-20__name">API · edge gateway</span>
          <span class="ac-20__ms">38 ms</span>
          <span class="ac-20__state">Operational</span>
        </li>
        <li class="ac-20__row" data-status="ok">
          <span class="ac-20__pip" aria-hidden="true"></span>
          <span class="ac-20__name">Dashboard · web app</span>
          <span class="ac-20__ms">112 ms</span>
          <span class="ac-20__state">Operational</span>
        </li>
        <li class="ac-20__row" data-status="warn">
          <span class="ac-20__pip" aria-hidden="true"></span>
          <span class="ac-20__name">Webhooks · delivery queue</span>
          <span class="ac-20__ms">1.9 s</span>
          <span class="ac-20__state">Degraded</span>
        </li>
        <li class="ac-20__row" data-status="ok">
          <span class="ac-20__pip" aria-hidden="true"></span>
          <span class="ac-20__name">Object storage · eu-west-1</span>
          <span class="ac-20__ms">64 ms</span>
          <span class="ac-20__state">Operational</span>
        </li>
      </ul>
      <div class="ac-20__uptime">
        <p class="ac-20__ulabel">Last 60 days</p>
        <div class="ac-20__bars" role="img" aria-label="Uptime for the last 60 days: two partial outages, otherwise fully operational">
          <i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="warn"><b>Jul 2 · 41 min degraded</b></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="down"><b>Jul 17 · 6 min outage</b></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i><i data-d="ok"></i>
        </div>
        <div class="ac-20__uscale"><span>60 days ago</span><span>Today</span></div>
      </div>
    </article>
    <p class="ac-20__chip" aria-hidden="true">two delay-offset ping rings · fade at 70% · status token via data attribute · shape + label, never colour alone</p>
  </div>
</section>
```
## CSS
```css
.ac-20,
.ac-20 *,
.ac-20 *::before,
.ac-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-20-bg: oklch(0.15 0.014 250);
  --ac-20-card: oklch(0.20 0.017 250);
  --ac-20-ink: oklch(0.97 0.004 260);
  --ac-20-mut: oklch(0.68 0.02 252);
  --ac-20-line: oklch(1 0 0/.10);
  --ac-20-ok: oklch(0.78 0.17 152);
  --ac-20-warn: oklch(0.82 0.16 78);
  --ac-20-down: oklch(0.68 0.21 25);
  background: var(--ac-20-bg);
  color: var(--ac-20-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 16px;
  padding: clamp(20px,5vw,56px);
}

.ac-20__card {
  width: min(100%,560px);
  display: grid;
  gap: 18px;
  padding: 22px;
  border: 1px solid var(--ac-20-line);
  border-radius: 22px;
  background: var(--ac-20-card);
  box-shadow: 0 36px 70px -46px oklch(0 0 0/.9);
}

.ac-20 [data-status="ok"] {
  --ac-20-c: var(--ac-20-ok);
}

.ac-20 [data-status="warn"] {
  --ac-20-c: var(--ac-20-warn);
}

.ac-20 [data-status="down"] {
  --ac-20-c: var(--ac-20-down);
}

.ac-20__top {
  display: flex;
  align-items: center;
  gap: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--ac-20-line);
}

.ac-20__dot {
  position: relative;
  flex: none;
  width: 13px;
  height: 13px;
  border-radius: 50%;
  background: var(--ac-20-c);
  box-shadow: 0 0 12px color-mix(in oklch,var(--ac-20-c) 70%,transparent);
  animation: ac-20-core 2.4s ease-in-out infinite;
}

.ac-20__dot::before,
.ac-20__dot::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1.5px solid var(--ac-20-c);
  animation: ac-20-ping 2.4s cubic-bezier(.2,.6,.4,1) infinite;
}

.ac-20__dot::after {
  animation-delay: 1.2s;
}

@keyframes ac-20-ping {
  0% {
    scale: 1;
    opacity: .85;
  }

  70% {
    opacity: 0;
  }

  100% {
    scale: 3.6;
    opacity: 0;
  }
}

@keyframes ac-20-core {
  0%,
    100% {
    opacity: .82;
  }

  50% {
    opacity: 1;
  }
}

.ac-20__top div {
  flex: 1;
  min-width: 0;
}

.ac-20__title {
  font-size: 17.5px;
  font-weight: 660;
  letter-spacing: -.025em;
}

.ac-20__sub {
  margin-top: 4px;
  font-size: 12.5px;
  color: var(--ac-20-mut);
  font-variant-numeric: tabular-nums;
}

.ac-20__live {
  flex: none;
  padding: 5px 11px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ac-20-c) 16%,transparent);
  color: var(--ac-20-c);
  font-size: 10.5px;
  font-weight: 750;
  letter-spacing: .13em;
  text-transform: uppercase;
}

.ac-20__list {
  display: grid;
  gap: 2px;
  list-style: none;
}

.ac-20__row {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  padding: 0 8px;
  border-radius: 11px;
  transition: background .2s;
}

.ac-20__row:hover {
  background: oklch(1 0 0/.04);
}

.ac-20__pip {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--ac-20-c);
}

.ac-20__row[data-status="warn"] .ac-20__pip {
  border-radius: 2px;
  rotate: 45deg;
  animation: ac-20-blink 1.6s ease-in-out infinite;
}

.ac-20__row[data-status="down"] .ac-20__pip {
  clip-path: polygon(50% 0,100% 100%,0 100%);
  border-radius: 0;
}

@keyframes ac-20-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.ac-20__name {
  font-size: 13.5px;
  font-weight: 560;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.ac-20__ms {
  font-size: 12px;
  color: var(--ac-20-mut);
  font-variant-numeric: tabular-nums;
}

.ac-20__state {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--ac-20-c);
  min-width: 88px;
  text-align: right;
}

.ac-20__uptime {
  display: grid;
  gap: 8px;
  padding-top: 16px;
  border-top: 1px solid var(--ac-20-line);
}

.ac-20__ulabel {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ac-20-mut);
}

.ac-20__bars {
  display: flex;
  gap: 2px;
  height: 30px;
}

.ac-20__bars i {
  position: relative;
  flex: 1;
  border-radius: 2px;
  background: color-mix(in oklch,var(--ac-20-ok) 55%,transparent);
  transition: background .2s,scale .2s;
  transform-origin: 50% 100%;
}

.ac-20__bars i[data-d="warn"] {
  background: var(--ac-20-warn);
}

.ac-20__bars i[data-d="down"] {
  background: var(--ac-20-down);
}

.ac-20__bars i:hover {
  scale: 1.35 1.06;
  background: var(--ac-20-ok);
}

.ac-20__bars i[data-d="warn"]:hover {
  background: var(--ac-20-warn);
}

.ac-20__bars i[data-d="down"]:hover {
  background: var(--ac-20-down);
}

.ac-20__bars b {
  position: absolute;
  left: 50%;
  bottom: calc(100% + 8px);
  translate: -50% 4px;
  padding: 6px 10px;
  border-radius: 8px;
  background: oklch(0.97 0 0);
  color: oklch(0.18 0.02 250);
  font-size: 11px;
  font-weight: 650;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity .18s,translate .18s;
  z-index: 2;
}

.ac-20__bars i:hover b {
  opacity: 1;
  translate: -50% 0;
}

.ac-20__uscale {
  display: flex;
  justify-content: space-between;
  font-size: 10.5px;
  color: var(--ac-20-mut);
  letter-spacing: .06em;
}

.ac-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-20-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-20-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,760px);
}

@media (max-width: 480px) {
  .ac-20__row {
    grid-template-columns: auto 1fr auto;
  }

  .ac-20__ms {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-20__dot,
    .ac-20__dot::before,
    .ac-20__dot::after,
    .ac-20__row[data-status="warn"] .ac-20__pip {
    animation: none;
  }

  .ac-20__dot::before,
    .ac-20__dot::after {
    opacity: .35;
  }
}
```
