---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/analytics-dashboard-stat-card/"
title: "Analytics Dashboard Stat Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Dark KPI card: metric label, big currency value, up-arrow trend delta with muted comparator, static SVG sparkline, and 7D/30D/90D tabs."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Analytics Dashboard Stat Card
Source: https://codefronts.com/components/css-cards/analytics-dashboard-stat-card/

Dark KPI card: metric label, big currency value, up-arrow trend delta with muted comparator, static SVG sparkline, and 7D/30D/90D tabs.
## HTML
```html
<section class="card-15">
  <article class="card-15__card">
    <div class="card-15__glow" aria-hidden="true"></div>
    <header class="card-15__head">
      <div class="card-15__title-row">
        <span class="card-15__pulse" aria-hidden="true"></span>
        <h3 class="card-15__label">Monthly recurring revenue</h3>
      </div>
      <button type="button" class="card-15__more" aria-label="More options">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg>
      </button>
    </header>
    <div class="card-15__value-row">
      <p class="card-15__value"><data value="284712">$284,712</data></p>
      <div class="card-15__trend">
        <span class="card-15__delta">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 15 12 9 18 15"/></svg>
          12.4%
        </span>
        <span class="card-15__vs">vs prev · $253,120</span>
      </div>
    </div>
    <div class="card-15__chart">
      <svg class="card-15__spark" viewBox="0 0 300 80" preserveAspectRatio="none" role="img" aria-label="Monthly recurring revenue up-trend, twelve data points">
        <defs>
          <linearGradient id="c15-fill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stop-color="#34d399" stop-opacity="0.35"/>
            <stop offset="1" stop-color="#34d399" stop-opacity="0"/>
          </linearGradient>
          <linearGradient id="c15-line" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0" stop-color="#34d399"/>
            <stop offset="1" stop-color="#22d3ee"/>
          </linearGradient>
        </defs>
        <line x1="0" y1="42" x2="300" y2="42" stroke="rgba(255,255,255,0.08)" stroke-width="1" stroke-dasharray="3 4"/>
        <path d="M 0 60 L 25 55 L 50 58 L 75 48 L 100 52 L 125 42 L 150 38 L 175 30 L 200 26 L 225 20 L 250 14 L 275 10 L 300 6 L 300 80 L 0 80 Z" fill="url(#c15-fill)"/>
        <path d="M 0 60 L 25 55 L 50 58 L 75 48 L 100 52 L 125 42 L 150 38 L 175 30 L 200 26 L 225 20 L 250 14 L 275 10 L 300 6" fill="none" stroke="url(#c15-line)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="300" cy="6" r="4" fill="#34d399"/>
        <circle cx="300" cy="6" r="7" fill="#34d399" opacity="0.25"/>
      </svg>
    </div>
    <dl class="card-15__stats">
      <div class="card-15__stat">
        <dt>Active users</dt>
        <dd><data value="12847">12.8k</data></dd>
      </div>
      <div class="card-15__stat">
        <dt>ARPU</dt>
        <dd><data value="22.14">$22.14</data></dd>
      </div>
      <div class="card-15__stat">
        <dt>Churn</dt>
        <dd class="card-15__stat--warn"><data value="2.1">2.1%</data></dd>
      </div>
    </dl>
    <div class="card-15__tabs" role="tablist" aria-label="Timeframe">
      <button type="button" class="card-15__tab" role="tab" aria-selected="false">7D</button>
      <button type="button" class="card-15__tab card-15__tab--active" role="tab" aria-selected="true">30D</button>
      <button type="button" class="card-15__tab" role="tab" aria-selected="false">90D</button>
      <button type="button" class="card-15__tab" role="tab" aria-selected="false">1Y</button>
    </div>
    <footer class="card-15__foot">
      <span class="card-15__updated">Updated 2m ago</span>
      <a href="#report" class="card-15__link">View full report
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </footer>
  </article>
</section>
```
## CSS
```css
.card-15 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 0%, rgba(52, 211, 153, 0.10) 0%, transparent 50%), radial-gradient(ellipse at 80% 100%, rgba(34, 211, 238, 0.08) 0%, transparent 50%), #06070c;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #34d399;
  --accent: #34d399;
  --accent-2: #22d3ee;
}

.card-15 *,
.card-15 *::before,
.card-15 *::after {
  box-sizing: border-box;
}

.card-15__card {
  position: relative;
  width: 100%;
  max-width: 360px;
  background: linear-gradient(180deg, rgba(52, 211, 153, 0.03) 0%, transparent 40%), linear-gradient(160deg, #14151d 0%, #0d0e15 100%);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 20px;
  padding: 22px 22px 18px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 255, 0.02) inset, 0 1px 0 rgba(255, 255, 255, 0.04) inset;
}

.card-15__glow {
  position: absolute;
  top: -60px;
  right: -40px;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(52, 211, 153, 0.14) 0%, transparent 60%);
  filter: blur(20px);
  pointer-events: none;
}

.card-15__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.card-15__title-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.card-15__pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 3px rgba(52, 211, 153, 0.18), 0 0 12px rgba(52, 211, 153, 0.6);
  animation: card-15-pulse 2.4s ease-in-out infinite;
}

.card-15__label {
  font-size: 12px;
  font-weight: 500;
  color: #a1a1aa;
  margin: 0;
  letter-spacing: -0.005em;
}

.card-15__more {
  width: 28px;
  height: 28px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 0;
  border-radius: 8px;
  color: #71717a;
  cursor: pointer;
  transition: background 0.18s, color 0.18s;
}

.card-15__more:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #d4d4d8;
}

.card-15__more:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-15__value-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 6px;
}

.card-15__value {
  font-size: 36px;
  font-weight: 700;
  letter-spacing: -0.035em;
  margin: 0;
  color: #fafafa;
  font-variant-numeric: tabular-nums;
  line-height: 1.05;
  background: linear-gradient(180deg, #ffffff 0%, #b4b4be 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-15__value data {
  color: inherit;
}

.card-15__trend {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
  padding-bottom: 4px;
}

.card-15__delta {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 12px;
  font-weight: 700;
  color: var(--accent);
  padding: 3px 8px;
  background: rgba(52, 211, 153, 0.14);
  border: 1px solid rgba(52, 211, 153, 0.24);
  border-radius: 999px;
  font-variant-numeric: tabular-nums;
}

.card-15__vs {
  font-size: 10.5px;
  color: #71717a;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.01em;
}

.card-15__chart {
  height: 80px;
  margin: 6px -22px 12px;
  padding: 0 22px;
  position: relative;
}

.card-15__spark {
  width: 100%;
  height: 100%;
  display: block;
  overflow: visible;
}

.card-15__stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  margin: 0 0 14px;
  padding: 12px 0;
  background: rgba(255, 255, 255, 0.04);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.04);
}

.card-15__stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: 0 8px;
  position: relative;
}

.card-15__stat + .card-15__stat::before {
  content: '';
  position: absolute;
  left: 0;
  top: 20%;
  bottom: 20%;
  width: 1px;
  background: rgba(255, 255, 255, 0.06);
}

.card-15__stat dt {
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: #71717a;
  margin: 0;
}

.card-15__stat dd {
  font-size: 14px;
  font-weight: 700;
  color: #f4f4f5;
  margin: 0;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
}

.card-15__stat--warn {
  color: #fbbf24 !important;
}

.card-15__tabs {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2px;
  padding: 3px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.04);
  border-radius: 10px;
  margin-bottom: 12px;
}

.card-15__tab {
  min-height: 32px;
  padding: 6px 8px;
  background: transparent;
  border: 0;
  border-radius: 7px;
  color: #71717a;
  font: 600 11.5px 'Inter', sans-serif;
  letter-spacing: 0.02em;
  cursor: pointer;
  transition: background 0.18s, color 0.18s, box-shadow 0.18s;
}

.card-15__tab:hover {
  color: #d4d4d8;
  background: rgba(255, 255, 255, 0.03);
}

.card-15__tab--active {
  color: #06070c;
  background: linear-gradient(180deg, #ecfdf5 0%, #a7f3d0 100%);
  box-shadow: 0 2px 8px rgba(52, 211, 153, 0.25), 0 0 0 1px rgba(52, 211, 153, 0.4);
}

.card-15__tab--active:hover {
  color: #06070c;
  background: linear-gradient(180deg, #ecfdf5 0%, #a7f3d0 100%);
}

.card-15__tab:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-15__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  font-size: 10.5px;
}

.card-15__updated {
  color: #71717a;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.card-15__updated::before {
  content: '';
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: #52525b;
}

.card-15__link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-weight: 600;
  color: #a1a1aa;
  text-decoration: none;
  padding: 4px 6px;
  border-radius: 6px;
  transition: color 0.18s, background 0.18s;
}

.card-15__link:hover {
  color: var(--accent);
  background: rgba(52, 211, 153, 0.06);
}

.card-15__link:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@keyframes card-15-pulse {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 3px rgba(52, 211, 153, 0.18), 0 0 12px rgba(52, 211, 153, 0.6);
  }

  50% {
    transform: scale(1.15);
    box-shadow: 0 0 0 5px rgba(52, 211, 153, 0.10), 0 0 16px rgba(52, 211, 153, 0.9);
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-15__pulse {
    animation: none;
  }

  .card-15__more,
    .card-15__tab,
    .card-15__link {
    transition: none;
  }
}
```
