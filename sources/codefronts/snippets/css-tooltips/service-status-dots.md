---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/service-status-dots/"
title: "Service Status Dots"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A status-page list where each colored dot pulses with its service state — hovering any row reveals an uptime bar history (30 days, color-coded), live metrics…"
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Service Status Dots
Source: https://codefronts.com/snippets/css-tooltips/service-status-dots/

A status-page list where each colored dot pulses with its service state — hovering any row reveals an uptime bar history (30 days, color-coded), live metrics (uptime, latency, throughput), and the most recent incident summary. Built for SaaS status pages, infrastructure dashboards, on-call surfaces.
## HTML
```html
<div class="tp-08">
  <div class="tp-08__inner">
    <div class="tp-08__row-wrap">
      <div class="tp-08__row">
        <span class="tp-08__dot tp-08__ok tp-08__pulse"></span>
        <span class="tp-08__name">API Gateway</span>
        <span class="tp-08__pct">99.98%</span>
      </div>
      <span class="tp-08__tip">
        <span class="tp-08__tip-head">
          <span class="tp-08__tip-dot" style="background:#3fb950"></span>
          <span class="tp-08__tip-name">API Gateway</span>
          <span class="tp-08__badge tp-08__badge-ok">Operational</span>
        </span>
        <span class="tp-08__bars-label">30-day uptime</span>
        <span class="tp-08__bars">
          <span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:80%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#d29922;height:60%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span>
        </span>
        <span class="tp-08__metrics">
          <span class="tp-08__met"><span class="tp-08__met-label">Uptime</span><span class="tp-08__met-val tp-08__met-ok">99.98%</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">p95 latency</span><span class="tp-08__met-val">38ms</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">Req/min</span><span class="tp-08__met-val">12.4k</span></span>
        </span>
        <span class="tp-08__incident">Last incident: <strong>Feb 14 · 18 min partial degradation</strong> — elevated error rates on /auth endpoints. Resolved.</span>
      </span>
    </div>

    <div class="tp-08__row-wrap">
      <div class="tp-08__row">
        <span class="tp-08__dot tp-08__ok tp-08__pulse"></span>
        <span class="tp-08__name">Auth Service</span>
        <span class="tp-08__pct">100.00%</span>
      </div>
      <span class="tp-08__tip">
        <span class="tp-08__tip-head">
          <span class="tp-08__tip-dot" style="background:#3fb950"></span>
          <span class="tp-08__tip-name">Auth Service</span>
          <span class="tp-08__badge tp-08__badge-ok">Operational</span>
        </span>
        <span class="tp-08__bars-label">30-day uptime</span>
        <span class="tp-08__bars">
          <span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span>
        </span>
        <span class="tp-08__metrics">
          <span class="tp-08__met"><span class="tp-08__met-label">Uptime</span><span class="tp-08__met-val tp-08__met-ok">100%</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">p95 latency</span><span class="tp-08__met-val">18ms</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">Token/min</span><span class="tp-08__met-val">84k</span></span>
        </span>
        <span class="tp-08__incident">No incidents in the last 90 days.</span>
      </span>
    </div>

    <div class="tp-08__row-wrap">
      <div class="tp-08__row">
        <span class="tp-08__dot tp-08__ok tp-08__pulse"></span>
        <span class="tp-08__name">PostgreSQL Primary</span>
        <span class="tp-08__pct">99.94%</span>
      </div>
      <span class="tp-08__tip">
        <span class="tp-08__tip-head">
          <span class="tp-08__tip-dot" style="background:#3fb950"></span>
          <span class="tp-08__tip-name">PostgreSQL Primary</span>
          <span class="tp-08__badge tp-08__badge-ok">Operational</span>
        </span>
        <span class="tp-08__bars-label">30-day uptime</span>
        <span class="tp-08__bars">
          <span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#f85149;height:40%"></span><span class="tp-08__bar" style="background:#d29922;height:70%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span>
        </span>
        <span class="tp-08__metrics">
          <span class="tp-08__met"><span class="tp-08__met-label">Uptime</span><span class="tp-08__met-val tp-08__met-ok">99.94%</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">p95 latency</span><span class="tp-08__met-val">6ms</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">Conns</span><span class="tp-08__met-val">142/500</span></span>
        </span>
        <span class="tp-08__incident">Last incident: <strong>Mar 2 · 34 min outage</strong> — connection pool exhaustion during traffic spike. Failover to replica triggered.</span>
      </span>
    </div>

    <div class="tp-08__row-wrap">
      <div class="tp-08__row">
        <span class="tp-08__dot tp-08__warn"></span>
        <span class="tp-08__name">Email Delivery</span>
        <span class="tp-08__pct">98.42%</span>
      </div>
      <span class="tp-08__tip">
        <span class="tp-08__tip-head">
          <span class="tp-08__tip-dot" style="background:#d29922"></span>
          <span class="tp-08__tip-name">Email Delivery</span>
          <span class="tp-08__badge tp-08__badge-warn">Degraded</span>
        </span>
        <span class="tp-08__bars-label">30-day uptime</span>
        <span class="tp-08__bars">
          <span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#d29922;height:55%"></span><span class="tp-08__bar" style="background:#d29922;height:50%"></span><span class="tp-08__bar" style="background:#f85149;height:30%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#3fb950;height:100%"></span><span class="tp-08__bar" style="background:#d29922;height:60%"></span><span class="tp-08__bar" style="background:#d29922;height:55%"></span><span class="tp-08__bar" style="background:#d29922;height:65%"></span><span class="tp-08__bar" style="background:#d29922;height:58%"></span><span class="tp-08__bar" style="background:#d29922;height:62%"></span><span class="tp-08__bar" style="background:#d29922;height:60%"></span><span class="tp-08__bar" style="background:#d29922;height:57%"></span>
        </span>
        <span class="tp-08__metrics">
          <span class="tp-08__met"><span class="tp-08__met-label">Uptime</span><span class="tp-08__met-val tp-08__met-warn">98.42%</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">Delivery</span><span class="tp-08__met-val tp-08__met-warn">91.3%</span></span>
          <span class="tp-08__met"><span class="tp-08__met-label">Avg delay</span><span class="tp-08__met-val tp-08__met-warn">340ms</span></span>
        </span>
        <span class="tp-08__incident">Active: <strong>Elevated bounce rates on Gmail / Yahoo</strong> — IP reputation issue with third-party relay. Investigation ongoing since May 11.</span>
      </span>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-08 {
  width: 100%;
  min-height: 100vh;
  background: #0d1117;
  /* Right room — status detail tooltip pops to the RIGHT of each row,
       ~280px wide. Without big right padding the tip would be cut off
       by .cf-stage's overflow:hidden on the gallery card. */
  padding: 36px 320px 36px 28px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

.tp-08__inner {
  max-width: 440px;
  margin: 0 auto;
}

.tp-08__row-wrap {
  position: relative;
}

.tp-08__row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  cursor: help;
}

.tp-08__row-wrap:last-child .tp-08__row {
  border-bottom: none;
}

.tp-08__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  flex-shrink: 0;
}

.tp-08__ok {
  background: #3fb950;
  box-shadow: 0 0 6px rgba(63, 185, 80, 0.5);
}

.tp-08__warn {
  background: #d29922;
  box-shadow: 0 0 6px rgba(210, 153, 34, 0.5);
}

.tp-08__down {
  background: #f85149;
  box-shadow: 0 0 6px rgba(248, 81, 73, 0.5);
}

.tp-08__pulse {
  animation: tp-08-pulse-anim 2.5s ease-in-out infinite;
}

@keyframes tp-08-pulse-anim {
  0%,
    100% {
    box-shadow: 0 0 6px rgba(63, 185, 80, 0.5);
  }

  50% {
    box-shadow: 0 0 14px rgba(63, 185, 80, 0.8);
  }
}

.tp-08__name {
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.7);
  flex: 1;
  letter-spacing: 0.02em;
}

.tp-08__pct {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.25);
}

.tp-08__tip {
  position: absolute;
  left: calc(100% + 14px);
  top: 50%;
  transform: translateY(-50%) translateX(6px);
  width: 280px;
  background: #161b22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 9px;
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.8);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  z-index: 30;
  overflow: hidden;
  display: block;
  text-align: left;
}

.tp-08__row-wrap:hover .tp-08__tip {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(0);
  transition-delay: 0s;
}

.tp-08__tip-head {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px 10px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.tp-08__tip-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.tp-08__tip-name {
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.85);
  flex: 1;
}

.tp-08__badge {
  font-size: 9px;
  padding: 2px 7px;
  border-radius: 20px;
  letter-spacing: 0.06em;
  font-weight: 500;
}

.tp-08__badge-ok {
  background: rgba(63, 185, 80, 0.15);
  color: #3fb950;
  border: 1px solid rgba(63, 185, 80, 0.25);
}

.tp-08__badge-warn {
  background: rgba(210, 153, 34, 0.15);
  color: #d29922;
  border: 1px solid rgba(210, 153, 34, 0.25);
}

.tp-08__badge-down {
  background: rgba(248, 81, 73, 0.15);
  color: #f85149;
  border: 1px solid rgba(248, 81, 73, 0.25);
}

.tp-08__bars-label {
  display: block;
  padding: 10px 14px 5px;
  font-size: 8px;
  color: rgba(255, 255, 255, 0.2);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.tp-08__bars {
  display: flex;
  gap: 2px;
  align-items: flex-end;
  height: 34px;
  padding: 0 14px 10px;
}

.tp-08__bar {
  flex: 1;
  border-radius: 1px;
  min-height: 4px;
  display: block;
}

.tp-08__metrics {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.tp-08__met {
  display: block;
  padding: 10px 13px;
  border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.tp-08__met:last-child {
  border-right: none;
}

.tp-08__met-label {
  display: block;
  font-size: 7px;
  color: rgba(255, 255, 255, 0.2);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.tp-08__met-val {
  display: block;
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.7);
}

.tp-08__met-ok {
  color: #3fb950;
}

.tp-08__met-warn {
  color: #d29922;
}

.tp-08__met-down {
  color: #f85149;
}

.tp-08__incident {
  display: block;
  padding: 9px 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  font-size: 10px;
  color: rgba(255, 255, 255, 0.25);
  line-height: 1.5;
  font-family: 'Inter', system-ui, sans-serif;
}

.tp-08__incident strong {
  color: rgba(255, 255, 255, 0.55);
  font-weight: 500;
}
```
