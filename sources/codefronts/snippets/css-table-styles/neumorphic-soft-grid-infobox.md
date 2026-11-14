---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/neumorphic-soft-grid-infobox/"
title: "Neumorphic Soft Grid Infobox"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A product analytics dashboard table where every element — the outer card, inner container, metric chips, and circular quota arcs — is sculpted from the same…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft Grid Infobox
Source: https://codefronts.com/snippets/css-table-styles/neumorphic-soft-grid-infobox/

A product analytics dashboard table where every element — the outer card, inner container, metric chips, and circular quota arcs — is sculpted from the same background colour using dual box-shadow neumorphic depth.
## HTML
```html
<div class="ct-12">
  <div class="ct-12__header">
    <div class="ct-12__title">🧊 Product Analytics</div>
    <div class="ct-12__sub">Neumorphic soft grid — every element carved in or raised from the same surface</div>
  </div>
  <div class="ct-12__card">
    <div class="ct-12__inner">
      <table>
        <thead>
          <tr>
            <th>Module</th>
            <th>Active Users</th>
            <th>Revenue</th>
            <th>Trend</th>
            <th>Quota</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="ct-12__row-icon" style="background:linear-gradient(135deg,rgba(108,99,255,0.12),rgba(108,99,255,0.06))">🚀</span>
              <span class="ct-12__row-name">Core Platform<span class="ct-12__row-sub">SaaS · Enterprise</span></span>
            </td>
            <td><span class="ct-12__metric-chip" style="color:var(--accent)">18,440</span></td>
            <td><span class="ct-12__metric-chip" style="color:var(--green)">$142K</span></td>
            <td><span class="ct-12__trend" style="color:var(--green)">▲ 12.4%</span></td>
            <td>
              <div class="ct-12__arc-wrap">
                <div class="ct-12__arc" style="--pct:82%"><span class="ct-12__arc-val">82%</span></div>
              </div>
            </td>
          </tr>
          <tr>
            <td>
              <span class="ct-12__row-icon" style="background:linear-gradient(135deg,rgba(240,98,146,0.12),rgba(240,98,146,0.06))">🤖</span>
              <span class="ct-12__row-name">AI Copilot<span class="ct-12__row-sub">ML · Inference</span></span>
            </td>
            <td><span class="ct-12__metric-chip" style="color:var(--accent2)">9,280</span></td>
            <td><span class="ct-12__metric-chip" style="color:var(--green)">$87K</span></td>
            <td><span class="ct-12__trend" style="color:var(--green)">▲ 34.1%</span></td>
            <td>
              <div class="ct-12__arc-wrap">
                <div class="ct-12__arc" style="--pct:67%;background: conic-gradient(var(--accent2) 67%, transparent 0%),var(--surface)"><span class="ct-12__arc-val">67%</span></div>
              </div>
            </td>
          </tr>
          <tr>
            <td>
              <span class="ct-12__row-icon" style="background:linear-gradient(135deg,rgba(38,166,154,0.12),rgba(38,166,154,0.06))">📊</span>
              <span class="ct-12__row-name">Analytics Hub<span class="ct-12__row-sub">BI · Reporting</span></span>
            </td>
            <td><span class="ct-12__metric-chip" style="color:var(--green)">5,190</span></td>
            <td><span class="ct-12__metric-chip" style="color:var(--orange)">$31K</span></td>
            <td><span class="ct-12__trend" style="color:var(--orange)">▼ 3.2%</span></td>
            <td>
              <div class="ct-12__arc-wrap">
                <div class="ct-12__arc" style="--pct:41%;background: conic-gradient(var(--orange) 41%, transparent 0%),var(--surface)"><span class="ct-12__arc-val">41%</span></div>
              </div>
            </td>
          </tr>
          <tr>
            <td>
              <span class="ct-12__row-icon" style="background:linear-gradient(135deg,rgba(255,112,67,0.12),rgba(255,112,67,0.06))">🔐</span>
              <span class="ct-12__row-name">Auth Shield<span class="ct-12__row-sub">Security · IAM</span></span>
            </td>
            <td><span class="ct-12__metric-chip" style="color:var(--orange)">22,100</span></td>
            <td><span class="ct-12__metric-chip" style="color:var(--green)">$58K</span></td>
            <td><span class="ct-12__trend" style="color:var(--green)">▲ 8.7%</span></td>
            <td>
              <div class="ct-12__arc-wrap">
                <div class="ct-12__arc" style="--pct:95%;background: conic-gradient(var(--green) 95%, transparent 0%),var(--surface)"><span class="ct-12__arc-val">95%</span></div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
```
## CSS
```css
.ct-12,
.ct-12 *,
.ct-12 *::before,
.ct-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-12 ::selection {
  background: #6c63ff;
  color: #fff;
}

.ct-12 {
  --bg: #e8eaf0;
  --surface: #e8eaf0;
  --shadow-light: #ffffff;
  --shadow-dark: rgba(163,170,190,0.7);
  --text: #2d3250;
  --muted: #8890b0;
  --accent: #6c63ff;
  --accent2: #f06292;
  --green: #26a69a;
  --orange: #ff7043;
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  padding: 44px 32px;
  min-height: 100vh;
  color: var(--text);
}
/* Neumorphic mixins */

.ct-12__raised {
  box-shadow: 6px 6px 14px var(--shadow-dark), -6px -6px 14px var(--shadow-light);
}

.ct-12__pressed {
  box-shadow: inset 4px 4px 10px var(--shadow-dark), inset -4px -4px 10px var(--shadow-light);
}

.ct-12__header {
  margin-bottom: 32px;
}

.ct-12__title {
  font-size: 22px;
  font-weight: 800;
  color: var(--text);
}

.ct-12__sub {
  font-size: 13px;
  color: var(--muted);
  margin-top: 4px;
}
/* OUTER CARD — raised neumorphic */

.ct-12__card {
  background: var(--surface);
  border-radius: 24px;
  padding: 6px;
  box-shadow: 10px 10px 24px var(--shadow-dark), -10px -10px 24px var(--shadow-light);
}
/* INNER sunken container */

.ct-12__inner {
  background: var(--surface);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: inset 3px 3px 8px var(--shadow-dark), inset -3px -3px 8px var(--shadow-light);
}

.ct-12 table {
  width: 100%;
  border-collapse: collapse;
}

.ct-12 thead th {
  padding: 16px 20px;
  text-align: left;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  background: var(--surface);
  border-bottom: 1px solid rgba(163,170,190,0.3);
}

.ct-12 thead th:not(:first-child) {
  text-align: center;
}

.ct-12 tbody tr {
  border-bottom: 1px solid rgba(163,170,190,0.2);
  transition: background 0.2s;
}

.ct-12 tbody tr:last-child {
  border-bottom: none;
}
/* On hover: each row gets a subtle inset press effect via the ::before overlay */

.ct-12 tbody tr:hover {
  background: rgba(108,99,255,0.03);
}

.ct-12 tbody tr:hover .ct-12__metric-chip {
  box-shadow: inset 3px 3px 8px rgba(163,170,190,0.6), inset -3px -3px 8px #ffffff;
}

.ct-12 tbody td {
  padding: 16px 20px;
  font-size: 14px;
  vertical-align: middle;
}

.ct-12 tbody td:not(:first-child) {
  text-align: center;
}

.ct-12__row-icon {
  width: 38px;
  height: 38px;
  border-radius: 12px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  box-shadow: 4px 4px 10px var(--shadow-dark), -4px -4px 10px var(--shadow-light);
  margin-right: 12px;
  vertical-align: middle;
}

.ct-12__row-name {
  font-weight: 700;
  font-size: 14px;
}

.ct-12__row-sub {
  font-size: 11px;
  color: var(--muted);
  display: block;
  margin-top: 1px;
}
/* Metric chips — raised pill neumorphic */

.ct-12__metric-chip {
  display: inline-block;
  padding: 7px 16px;
  border-radius: 20px;
  font-weight: 800;
  font-size: 13px;
  background: var(--surface);
  box-shadow: 4px 4px 10px var(--shadow-dark), -4px -4px 10px var(--shadow-light);
  transition: box-shadow 0.2s;
}

.ct-12__trend {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 700;
  padding: 5px 12px;
  border-radius: 20px;
  box-shadow: 3px 3px 8px var(--shadow-dark), -3px -3px 8px var(--shadow-light);
}
/* Progress arc (CSS only, linear fill) */

.ct-12__arc-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
}

.ct-12__arc {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 4px 4px 10px var(--shadow-dark), -4px -4px 10px var(--shadow-light);
  font-size: 11px;
  font-weight: 800;
  position: relative;
  background: conic-gradient(var(--accent) var(--pct, 0%), transparent 0%), var(--surface);
}

.ct-12__arc::after {
  content: '';
  position: absolute;
  inset: 8px;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: inset 2px 2px 5px var(--shadow-dark), inset -2px -2px 5px var(--shadow-light);
}

.ct-12__arc-val {
  position: relative;
  z-index: 1;
  font-size: 11px;
  font-weight: 800;
  color: var(--text);
}

@media (prefers-reduced-motion: reduce) {
  .ct-12 tbody tr,
    .ct-12__metric-chip {
    transition: none;
  }
}
```
