---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/vitals-timeline/"
title: "Patient Vitals Timeline — Medical Dashboard with CSS Sparklines"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A clinical monitoring strip: timestamped vitals readings (HR, SpO₂, BP) on a shared time axis, each with a pure-CSS sparkline drawn from custom properties…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Patient Vitals Timeline — Medical Dashboard with CSS Sparklines
Source: https://codefronts.com/layouts/css-timelines/vitals-timeline/

A clinical monitoring strip: timestamped vitals readings (HR, SpO₂, BP) on a shared time axis, each with a pure-CSS sparkline drawn from custom properties via clip-path — plus threshold flags that mark out-of-range readings with icon + text, in the restrained visual language of medical dashboards.
## HTML
```html
<section class="tls-11" aria-label="Patient vitals timeline demo">
  <div class="tls-11__monitor">
    <header class="tls-11__head">
      <p class="tls-11__pt">Bed 12 · J. Okafor</p>
      <p class="tls-11__range">Last 6 hours · <time datetime="2026-07-18T09:00">09:00</time>–<time datetime="2026-07-18T15:00">15:00</time></p>
    </header>
    <div class="tls-11__axis" aria-hidden="true"><span>09</span><span>10</span><span>11</span><span>12</span><span>13</span><span>14</span></div>
    <dl class="tls-11__rows">
      <div class="tls-11__row">
        <dt class="tls-11__metric">Heart rate <span class="tls-11__unit">bpm</span></dt>
        <dd class="tls-11__val">86</dd>
        <dd class="tls-11__spark" aria-hidden="true"><span class="tls-11__line" style="--c:#38bdf8;--p1:42;--p2:48;--p3:45;--p4:60;--p5:68;--p6:58"></span></dd>
        <dd class="tls-11__flag" data-flag="ok">In range</dd>
      </div>
      <div class="tls-11__row">
        <dt class="tls-11__metric">SpO₂ <span class="tls-11__unit">%</span></dt>
        <dd class="tls-11__val">93</dd>
        <dd class="tls-11__spark" aria-hidden="true"><span class="tls-11__line" style="--c:#a78bfa;--p1:80;--p2:76;--p3:70;--p4:62;--p5:55;--p6:48"></span></dd>
        <dd class="tls-11__flag" data-flag="low"><b aria-hidden="true">▼</b> Low</dd>
      </div>
      <div class="tls-11__row">
        <dt class="tls-11__metric">Systolic BP <span class="tls-11__unit">mmHg</span></dt>
        <dd class="tls-11__val">142</dd>
        <dd class="tls-11__spark" aria-hidden="true"><span class="tls-11__line" style="--c:#fbbf24;--p1:50;--p2:52;--p3:58;--p4:64;--p5:72;--p6:78"></span></dd>
        <dd class="tls-11__flag" data-flag="high"><b aria-hidden="true">▲</b> High</dd>
      </div>
      <div class="tls-11__row">
        <dt class="tls-11__metric">Temp <span class="tls-11__unit">°C</span></dt>
        <dd class="tls-11__val">37.1</dd>
        <dd class="tls-11__spark" aria-hidden="true"><span class="tls-11__line" style="--c:#34d399;--p1:48;--p2:50;--p3:49;--p4:52;--p5:51;--p6:50"></span></dd>
        <dd class="tls-11__flag" data-flag="ok">In range</dd>
      </div>
    </dl>
  </div>
</section>
```
## CSS
```css
.tls-11,
.tls-11 *,
.tls-11 *::before,
.tls-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-11 {
  min-height: 100vh;
  width: 100%;
  --tl-alert: #f59e0b;
  --tl-low: #60a5fa;
  --tl-line: #1e2733;
  --tl-ink: #e6edf5;
  --tl-mut: #7d8b9d;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0b1017;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-11__monitor {
  width: min(640px,100%);
  background: #0f1620;
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 20px 24px 24px;
}

.tls-11__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.tls-11__pt {
  font-size: 14px;
  font-weight: 700;
  color: var(--tl-ink);
}

.tls-11__range {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  color: var(--tl-mut);
}

.tls-11__axis {
  display: grid;
  grid-template-columns: 16ch 6ch 1fr 9ch;
  margin-bottom: 6px;
}

.tls-11__axis span {
  display: none;
}

.tls-11__axis::before {
  content: '';
  grid-column: 1 / 3;
}

.tls-11__axis {
  position: relative;
}

.tls-11__rows {
  display: grid;
  gap: 2px;
}

.tls-11__row {
  display: grid;
  grid-template-columns: 16ch 6ch 1fr 9ch;
  align-items: center;
  gap: 10px;
  padding: 10px 8px;
  border-radius: 8px;
}

.tls-11__row:hover {
  background: #131c28;
}

.tls-11__metric {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--tl-ink);
}

.tls-11__unit {
  font-size: 10px;
  color: var(--tl-mut);
  margin-left: 3px;
}

.tls-11__val {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 18px;
  font-weight: 700;
  color: var(--tl-ink);
  font-variant-numeric: tabular-nums;
  text-align: right;
}

.tls-11__spark {
  height: 34px;
  position: relative;
}

.tls-11__line {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,var(--c),transparent 130%);
  opacity: .9;
  clip-path: polygon(0 calc(100% - var(--p1) * 1%),20% calc(100% - var(--p2) * 1%),40% calc(100% - var(--p3) * 1%),60% calc(100% - var(--p4) * 1%),80% calc(100% - var(--p5) * 1%),100% calc(100% - var(--p6) * 1%),100% 100%,0 100%);
}

.tls-11__spark::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(90deg,#1a2430 0 1px,transparent 1px 20%);
}

.tls-11__flag {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .04em;
  text-transform: uppercase;
  text-align: right;
  color: var(--tl-mut);
}

.tls-11__flag[data-flag="high"] {
  color: var(--tl-alert);
}

.tls-11__flag[data-flag="low"] {
  color: var(--tl-low);
}

.tls-11__flag b {
  font-weight: 400;
  margin-right: 2px;
}

@media (max-width: 560px) {
  .tls-11__row,
    .tls-11__axis {
    grid-template-columns: 12ch 5ch 1fr 7ch;
  }
}
```

## JavaScript
```js
/* No JavaScript — each sparkline is a clip-path:polygon() whose vertex heights come from inline --p1…--p6 tokens; flags pair a glyph AND text with the color. */
```
