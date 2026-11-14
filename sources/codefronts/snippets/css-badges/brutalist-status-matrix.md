---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/brutalist-status-matrix/"
title: "Brutalist Status Matrix"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Monospaced status grid — operational, degraded, outage, maintenance, deploying, queued."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Status Matrix
Source: https://codefronts.com/snippets/css-badges/brutalist-status-matrix/

Monospaced status grid — operational, degraded, outage, maintenance, deploying, queued. Inverts on hover. Live pulse on healthy systems, blink on outages, scanline on deploys.
## HTML
```html
<div class="bdg-29-grid">
  <div class="bdg-29-row">
    <span class="bdg-29-badge bdg-29-operational"><span class="bdg-29-dot"></span>Operational</span>
    <div class="bdg-29-service">api.gateway.production</div>
    <div class="bdg-29-meta">us-east-1 · 99.984% / 30d</div>
    <div class="bdg-29-time">↑ 47d 12h 04m · last incident: 2026-03-29</div>
  </div>
  <div class="bdg-29-row">
    <span class="bdg-29-badge bdg-29-degraded"><span class="bdg-29-dot"></span>Degraded</span>
    <div class="bdg-29-service">search.indexer.eu</div>
    <div class="bdg-29-meta">eu-west-2 · 96.412% / 24h</div>
    <div class="bdg-29-time">P95 latency 840ms · ETA recovery 18m</div>
  </div>
  <div class="bdg-29-row">
    <span class="bdg-29-badge bdg-29-outage"><span class="bdg-29-dot"></span>Outage</span>
    <div class="bdg-29-service">media.transcoder.bg</div>
    <div class="bdg-29-meta">ap-south-1 · 00.000% / 12m</div>
    <div class="bdg-29-time">incident #4119 · on-call: m.tanaka</div>
  </div>
  <div class="bdg-29-row">
    <span class="bdg-29-badge bdg-29-deploy"><span class="bdg-29-dot"></span>Deploying</span>
    <div class="bdg-29-service">auth.service.canary</div>
    <div class="bdg-29-meta">v4.18.2 · 38% traffic</div>
    <div class="bdg-29-time">commit a1f9c2e · rollback ready</div>
  </div>
</div>
```
## CSS
```css
.bdg-29-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  border: 2px solid #000;
  background: #f4f4f0;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.bdg-29-row {
  border-right: 2px solid #000;
  border-bottom: 2px solid #000;
  padding: 24px 20px;
  background: #fff;
  cursor: pointer;
  transition: background 0.2s;
}

.bdg-29-row:hover {
  background: #000;
  color: #fff;
}

.bdg-29-row:hover .bdg-29-time {
  color: #fff;
}

.bdg-29-row:hover .bdg-29-meta {
  color: rgba(255,255,255,0.6);
}

.bdg-29-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 6px 12px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  border: 2px solid currentColor;
  margin-bottom: 16px;
}

.bdg-29-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
}

.bdg-29-operational {
  color: #1d8f4a;
  background: #ddf5e3;
}

.bdg-29-operational .bdg-29-dot {
  animation: bdg-29-pulse 1.6s infinite;
}

.bdg-29-degraded {
  color: #b8761c;
  background: #fdf2d8;
}

.bdg-29-outage {
  color: #c0241c;
  background: #fde0dd;
}

.bdg-29-outage .bdg-29-dot {
  animation: bdg-29-blink 0.5s infinite;
}

.bdg-29-deploy {
  color: #1c4a9e;
  background: #dde6f7;
  position: relative;
  overflow: hidden;
}

.bdg-29-deploy::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(28,74,158,0.3), transparent);
  animation: bdg-29-scan 1.5s linear infinite;
}

@keyframes bdg-29-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.3;
  }
}

@keyframes bdg-29-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

@keyframes bdg-29-scan {
  0% {
    left: -100%;
  }

  100% {
    left: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-29-operational .bdg-29-dot,
    .bdg-29-outage .bdg-29-dot,
    .bdg-29-deploy::before {
    animation: none;
  }
}

.bdg-29-service {
  font-family: Georgia, "Fraunces", serif;
  font-size: 20px;
  font-weight: 500;
  margin-bottom: 4px;
  letter-spacing: -0.01em;
}

.bdg-29-meta {
  font-size: 10px;
  letter-spacing: 0.08em;
  color: #888;
  text-transform: uppercase;
  transition: color 0.2s;
}

.bdg-29-time {
  font-size: 10px;
  letter-spacing: 0.08em;
  color: #000;
  transition: color 0.2s;
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px dashed currentColor;
  opacity: 0.7;
}
```
