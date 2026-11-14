---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/zebra-glassmorphism-table/"
title: "Zebra Glassmorphism Table"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A campaign-analytics table layered over animated gradient orbs, using backdrop-filter: blur() on alternating rows to create a frost-over-glass zebra stripe…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Zebra Glassmorphism Table
Source: https://codefronts.com/snippets/css-table-styles/zebra-glassmorphism-table/

A campaign-analytics table layered over animated gradient orbs, using backdrop-filter: blur() on alternating rows to create a frost-over-glass zebra stripe effect.
## HTML
```html
<div class="ct-06">
  <div class="ct-06__bg"></div>
  <div class="ct-06__orb ct-06__orb--a"></div>
  <div class="ct-06__orb ct-06__orb--b"></div>
  <div class="ct-06__content">
    <div class="ct-06__header">
      <div class="ct-06__eyebrow">✦ Glassmorphism</div>
      <div class="ct-06__title">Campaign Performance</div>
      <div class="ct-06__sub">Hover rows to see the frost effect intensify</div>
    </div>
    <div class="ct-06__glass">
      <table>
        <thead>
          <tr>
            <th>Campaign</th>
            <th>Owner</th>
            <th>Status</th>
            <th>Reach</th>
            <th>Conversion</th>
            <th>Progress</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:700">Q3 Product Launch</td>
            <td><div style="display:flex;align-items:center;gap:8px"><span class="ct-06__avatar" style="background:linear-gradient(135deg,#8b5cf6,#06b6d4)">AK</span><span style="color:var(--muted)">Arya K.</span></div></td>
            <td><span class="ct-06__status"><span class="ct-06__dot-g">●</span>Live</span></td>
            <td style="font-weight:600">248K</td>
            <td>4.2%</td>
            <td><div class="ct-06__bar-wrap"><div class="ct-06__bar-bg"><div class="ct-06__bar-fill" style="width:72%"></div></div><span class="ct-06__bar-val">72%</span></div></td>
          </tr>
          <tr>
            <td style="font-weight:700">Black Friday Promo</td>
            <td><div style="display:flex;align-items:center;gap:8px"><span class="ct-06__avatar" style="background:linear-gradient(135deg,#f59e0b,#ef4444)">MR</span><span style="color:var(--muted)">Marcus R.</span></div></td>
            <td><span class="ct-06__status"><span class="ct-06__dot-y">●</span>Scheduled</span></td>
            <td style="font-weight:600">1.1M</td>
            <td>—</td>
            <td><div class="ct-06__bar-wrap"><div class="ct-06__bar-bg"><div class="ct-06__bar-fill" style="width:18%"></div></div><span class="ct-06__bar-val">18%</span></div></td>
          </tr>
          <tr>
            <td style="font-weight:700">Creator Collab Series</td>
            <td><div style="display:flex;align-items:center;gap:8px"><span class="ct-06__avatar" style="background:linear-gradient(135deg,#10b981,#0ea5e9)">SN</span><span style="color:var(--muted)">Selin N.</span></div></td>
            <td><span class="ct-06__status"><span class="ct-06__dot-g">●</span>Live</span></td>
            <td style="font-weight:600">640K</td>
            <td>7.8%</td>
            <td><div class="ct-06__bar-wrap"><div class="ct-06__bar-bg"><div class="ct-06__bar-fill" style="width:91%;background:linear-gradient(90deg,#4ade80,#22d3ee)"></div></div><span class="ct-06__bar-val">91%</span></div></td>
          </tr>
          <tr>
            <td style="font-weight:700">Retargeting Wave</td>
            <td><div style="display:flex;align-items:center;gap:8px"><span class="ct-06__avatar" style="background:linear-gradient(135deg,#ec4899,#8b5cf6)">TW</span><span style="color:var(--muted)">Theo W.</span></div></td>
            <td><span class="ct-06__status"><span class="ct-06__dot-r">●</span>Paused</span></td>
            <td style="font-weight:600">82K</td>
            <td>1.1%</td>
            <td><div class="ct-06__bar-wrap"><div class="ct-06__bar-bg"><div class="ct-06__bar-fill" style="width:35%;background:linear-gradient(90deg,#f87171,#fb923c)"></div></div><span class="ct-06__bar-val">35%</span></div></td>
          </tr>
          <tr>
            <td style="font-weight:700">Brand Awareness APAC</td>
            <td><div style="display:flex;align-items:center;gap:8px"><span class="ct-06__avatar" style="background:linear-gradient(135deg,#0ea5e9,#6366f1)">JP</span><span style="color:var(--muted)">James P.</span></div></td>
            <td><span class="ct-06__status"><span class="ct-06__dot-g">●</span>Live</span></td>
            <td style="font-weight:600">2.4M</td>
            <td>2.9%</td>
            <td><div class="ct-06__bar-wrap"><div class="ct-06__bar-bg"><div class="ct-06__bar-fill" style="width:58%"></div></div><span class="ct-06__bar-val">58%</span></div></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
```
## CSS
```css
.ct-06,
.ct-06 *,
.ct-06 *::before,
.ct-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-06 ::selection {
  background: rgba(255,255,255,0.3);
  color: #fff;
}

.ct-06 {
  --text: #fff;
  --muted: rgba(255,255,255,0.5);
  --border: rgba(255,255,255,0.12);
  --row-a: rgba(255,255,255,0.06);
  --row-b: rgba(255,255,255,0.02);
  --accent: #a78bfa;
  font-family: 'Segoe UI', system-ui, sans-serif;
  padding: 40px 28px;
  min-height: 100vh;
  color: var(--text);
  position: relative;
  overflow: hidden;
}
/* Colourful animated background */

.ct-06__bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 25%, #4c1d95 50%, #7e22ce 75%, #0f172a 100%);
  background-size: 400% 400%;
  animation: ct-06-bgshift 10s ease infinite;
}

@keyframes ct-06-bgshift {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

.ct-06__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  animation: ct-06-orbdrift 8s ease-in-out infinite;
}

.ct-06__orb--a {
  width: 320px;
  height: 320px;
  background: rgba(139,92,246,0.4);
  top: -80px;
  left: -60px;
}

.ct-06__orb--b {
  width: 280px;
  height: 280px;
  background: rgba(6,182,212,0.3);
  bottom: -80px;
  right: -40px;
  animation-delay: -4s;
}

@keyframes ct-06-orbdrift {
  0%,
    100% {
    transform: translate(0, 0) scale(1);
  }

  50% {
    transform: translate(20px, 15px) scale(1.1);
  }
}

.ct-06__content {
  position: relative;
  z-index: 1;
}

.ct-06__header {
  margin-bottom: 24px;
}

.ct-06__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.ct-06__title {
  font-size: 22px;
  font-weight: 800;
}

.ct-06__sub {
  font-size: 13px;
  color: var(--muted);
  margin-top: 4px;
}
/* Glass table container */

.ct-06__glass {
  background: rgba(255,255,255,0.06);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid var(--border);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.15);
}

.ct-06 table {
  width: 100%;
  border-collapse: collapse;
}

.ct-06 thead tr {
  border-bottom: 1px solid var(--border);
  background: rgba(255,255,255,0.08);
}

.ct-06 thead th {
  padding: 14px 20px;
  text-align: left;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
}

.ct-06 thead th:last-child {
  text-align: right;
}
/* ZEBRA frost stripes */

.ct-06 tbody tr:nth-child(odd) {
  background: var(--row-a);
}

.ct-06 tbody tr:nth-child(even) {
  background: var(--row-b);
}

.ct-06 tbody tr {
  border-bottom: 1px solid rgba(255,255,255,0.05);
  transition: background 0.25s;
}

.ct-06 tbody tr:last-child {
  border-bottom: none;
}

.ct-06 tbody tr:hover {
  background: rgba(167,139,250,0.15) !important;
  backdrop-filter: blur(30px);
}

.ct-06 tbody td {
  padding: 15px 20px;
  font-size: 13px;
  vertical-align: middle;
}

.ct-06 tbody td:last-child {
  text-align: right;
}

.ct-06__avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  border: 1.5px solid rgba(255,255,255,0.2);
  display: inline-flex;
}

.ct-06__status {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
}

.ct-06__dot-g {
  color: #4ade80;
}

.ct-06__dot-y {
  color: #fbbf24;
}

.ct-06__dot-r {
  color: #f87171;
}

.ct-06__bar-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
  justify-content: flex-end;
}

.ct-06__bar-bg {
  width: 80px;
  height: 5px;
  background: rgba(255,255,255,0.1);
  border-radius: 3px;
  overflow: hidden;
}

.ct-06__bar-fill {
  height: 100%;
  border-radius: 3px;
  background: linear-gradient(90deg, var(--accent), #06b6d4);
  transition: width 1s ease;
}

.ct-06__bar-val {
  font-size: 12px;
  font-weight: 700;
  min-width: 32px;
}

@media (prefers-reduced-motion: reduce) {
  .ct-06__bg,
    .ct-06__orb,
    .ct-06 tbody tr {
    animation: none;
    transition: none;
  }
}
```
