---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-stats-dashboard-kpi-grid/"
title: "CSS Stats Dashboard KPI Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A 6-card SaaS dashboard KPI grid with real metrics — MRR, active users, churn, NPS, deploys, uptime — each card showing the number, the delta vs last period,…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stats Dashboard KPI Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-stats-dashboard-kpi-grid/

A 6-card SaaS dashboard KPI grid with real metrics — MRR, active users, churn, NPS, deploys, uptime — each card showing the number, the delta vs last period, and a CSS-drawn sparkline. Zero JavaScript, zero chart library, drop-in for any admin dashboard or marketing stats section.
## HTML
```html
<div class="cg-13">
  <div class="cg-13__head">
    <div>
      <h2 class="cg-13__title">Dashboard</h2>
      <span class="cg-13__sub">Last 30 days · Updated 2 min ago</span>
    </div>
    <div class="cg-13__rangepill">
      <span class="cg-13__rangeitem">7D</span>
      <span class="cg-13__rangeitem cg-13__rangeitem--on">30D</span>
      <span class="cg-13__rangeitem">90D</span>
      <span class="cg-13__rangeitem">1Y</span>
    </div>
  </div>

  <div class="cg-13__grid">

    <article class="cg-13__card cg-13__card--hero" style="--accent:#7c3aed">
      <span class="cg-13__kicker">Monthly Recurring Revenue</span>
      <div class="cg-13__row">
        <span class="cg-13__metric">$847.2K</span>
        <span class="cg-13__delta cg-13__delta--up">▲ 12.4%</span>
      </div>
      <p class="cg-13__hint">+$93.4K vs last 30 days. On track for $1M MRR by Q4.</p>
      <div class="cg-13__spark">
        <i style="height:32%"></i><i style="height:48%"></i><i style="height:42%"></i><i style="height:58%"></i>
        <i style="height:52%"></i><i style="height:68%"></i><i style="height:76%"></i><i style="height:90%"></i>
      </div>
    </article>

    <article class="cg-13__card" style="--accent:#0ea5e9">
      <span class="cg-13__kicker">Active Users</span>
      <span class="cg-13__metric">12,418</span>
      <span class="cg-13__delta cg-13__delta--up">▲ 8.1%</span>
      <div class="cg-13__spark">
        <i style="height:48%"></i><i style="height:52%"></i><i style="height:46%"></i><i style="height:62%"></i>
        <i style="height:58%"></i><i style="height:72%"></i><i style="height:68%"></i><i style="height:84%"></i>
      </div>
    </article>

    <article class="cg-13__card" style="--accent:#ef4444">
      <span class="cg-13__kicker">Churn Rate</span>
      <span class="cg-13__metric">2.1%</span>
      <span class="cg-13__delta cg-13__delta--down">▼ 0.4%</span>
      <div class="cg-13__spark">
        <i style="height:64%"></i><i style="height:58%"></i><i style="height:62%"></i><i style="height:48%"></i>
        <i style="height:42%"></i><i style="height:38%"></i><i style="height:34%"></i><i style="height:28%"></i>
      </div>
    </article>

    <article class="cg-13__card" style="--accent:#10b981">
      <span class="cg-13__kicker">NPS Score</span>
      <span class="cg-13__metric">+72</span>
      <span class="cg-13__delta cg-13__delta--up">▲ 4 pts</span>
      <div class="cg-13__spark">
        <i style="height:58%"></i><i style="height:60%"></i><i style="height:55%"></i><i style="height:65%"></i>
        <i style="height:62%"></i><i style="height:72%"></i><i style="height:68%"></i><i style="height:78%"></i>
      </div>
    </article>

    <article class="cg-13__card" style="--accent:#f59e0b">
      <span class="cg-13__kicker">Deploys / week</span>
      <span class="cg-13__metric">147</span>
      <span class="cg-13__delta cg-13__delta--up">▲ 22</span>
      <div class="cg-13__spark">
        <i style="height:42%"></i><i style="height:52%"></i><i style="height:48%"></i><i style="height:64%"></i>
        <i style="height:58%"></i><i style="height:72%"></i><i style="height:78%"></i><i style="height:88%"></i>
      </div>
    </article>

    <article class="cg-13__card" style="--accent:#06b6d4">
      <span class="cg-13__kicker">Uptime</span>
      <span class="cg-13__metric">99.98%</span>
      <span class="cg-13__delta cg-13__delta--flat">— flat</span>
      <div class="cg-13__spark">
        <i style="height:88%"></i><i style="height:90%"></i><i style="height:86%"></i><i style="height:92%"></i>
        <i style="height:88%"></i><i style="height:94%"></i><i style="height:90%"></i><i style="height:92%"></i>
      </div>
    </article>

  </div>
</div>
```
## CSS
```css
.cg-13,
.cg-13 *,
.cg-13 *::before,
.cg-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-13 ::selection {
  background: #0f172a;
  color: #fff;
}

.cg-13 {
  --bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --up: #10b981;
  --down: #ef4444;
  min-height: 100vh;
  background: var(--bg);
  padding: clamp(28px,3.4vw,48px) clamp(20px,3vw,40px);
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;
  color: var(--ink);
}

.cg-13__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: clamp(20px,2.5vw,32px);
  gap: 14px;
  flex-wrap: wrap;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.cg-13__title {
  font-size: clamp(1.5rem,2.6vw,2rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
}

.cg-13__sub {
  display: block;
  font-size: .84rem;
  color: var(--muted);
  font-weight: 500;
  margin-top: 6px;
}

.cg-13__rangepill {
  display: flex;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 4px;
  gap: 2px;
}

.cg-13__rangeitem {
  padding: 6px 12px;
  border-radius: 7px;
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .04em;
  color: var(--muted);
  cursor: pointer;
  transition: background .2s,color .2s;
}

.cg-13__rangeitem--on {
  background: var(--ink);
  color: #fff;
}

.cg-13__rangeitem:hover:not(.cg-13__rangeitem--on) {
  color: var(--ink);
}

.cg-13__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: clamp(12px,1.4vw,18px);
  max-width: 1200px;
  margin: 0 auto;
}

.cg-13__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: clamp(18px,2vw,22px);
  display: flex;
  flex-direction: column;
  gap: 6px;
  position: relative;
  overflow: hidden;
  transition: transform .25s,box-shadow .25s,border-color .25s;
}

.cg-13__card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--accent);
  opacity: 0;
  transition: opacity .25s;
}

.cg-13__card:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 28px -16px rgba(15,23,42,.12);
  border-color: var(--accent);
}

.cg-13__card:hover::before {
  opacity: 1;
}

.cg-13__card--hero {
  grid-column: span 2;
}

.cg-13__kicker {
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cg-13__row {
  display: flex;
  align-items: baseline;
  gap: 14px;
  flex-wrap: wrap;
}

.cg-13__metric {
  font-size: clamp(1.8rem,3vw,2.6rem);
  font-weight: 900;
  letter-spacing: -.025em;
  line-height: 1.05;
  font-feature-settings: "tnum";
}

.cg-13__card--hero .cg-13__metric {
  font-size: clamp(2.4rem,4.2vw,3.4rem);
}

.cg-13__delta {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: .86rem;
  font-weight: 700;
  font-feature-settings: "tnum";
}

.cg-13__delta--up {
  color: var(--up);
}

.cg-13__delta--down {
  color: var(--down);
}

.cg-13__delta--flat {
  color: var(--muted);
}

.cg-13__hint {
  font-size: .86rem;
  color: var(--muted);
  line-height: 1.45;
  margin-top: 4px;
}

.cg-13__spark {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 48px;
  margin-top: auto;
  padding-top: 14px;
}

.cg-13__card--hero .cg-13__spark {
  height: 72px;
}

.cg-13__spark i {
  flex: 1;
  display: block;
  background: linear-gradient(180deg,var(--accent),transparent 130%);
  border-radius: 2px 2px 0 0;
  min-height: 6px;
}

@media (max-width: 760px) {
  .cg-13__card--hero {
    grid-column: span 1;
  }

  .cg-13__head {
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-13__card,
    .cg-13__rangeitem {
    transition: none;
  }
}
```
