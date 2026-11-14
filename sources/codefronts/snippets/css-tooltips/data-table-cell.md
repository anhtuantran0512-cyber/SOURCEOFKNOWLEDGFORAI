---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/data-table-cell/"
title: "Data Table Cell"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A quarterly metrics table where each plain number is a hover target."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Table Cell
Source: https://codefronts.com/snippets/css-tooltips/data-table-cell/

A quarterly metrics table where each plain number is a hover target. The popover shows the metric name, large value, change-vs-prior quarter, a three-bar segment breakdown (e.g. SMB / Mid / Enterprise), and a two-piece footer with delta and aggregate context. For analytics dashboards, BI reports, KPI surfaces.
## HTML
```html
<div class="tp-11">
  <div class="tp-11__inner">
    <table class="tp-11__table">
      <thead>
        <tr>
          <th></th><th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="tp-11__row-label">Revenue</td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">$2.1M</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Revenue · Q1</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">$2.1M</span><span class="tp-11__change tp-11__up">↑ +18% vs Q4</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By segment</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">SMB</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:62%;background:#6366f1"></span></span><span class="tp-11__bar-pct">62%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Mid</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:28%;background:#8b5cf6"></span></span><span class="tp-11__bar-pct">28%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:10%;background:#a78bfa"></span></span><span class="tp-11__bar-pct">10%</span></span>
                </span>
                <span class="tp-11__foot"><span>vs prior: <strong>+$320K</strong></span><span>ARR: <strong>$8.4M</strong></span></span>
              </span>
            </span>
          </td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">$2.8M</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Revenue · Q2</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">$2.8M</span><span class="tp-11__change tp-11__up">↑ +33% vs Q1</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By segment</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">SMB</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:55%;background:#6366f1"></span></span><span class="tp-11__bar-pct">55%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Mid</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:33%;background:#8b5cf6"></span></span><span class="tp-11__bar-pct">33%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:12%;background:#a78bfa"></span></span><span class="tp-11__bar-pct">12%</span></span>
                </span>
                <span class="tp-11__foot"><span>vs Q1: <strong>+$700K</strong></span><span>ARR: <strong>$11.2M</strong></span></span>
              </span>
            </span>
          </td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">$3.4M</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Revenue · Q3</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">$3.4M</span><span class="tp-11__change tp-11__up">↑ +21% vs Q2</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By segment</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">SMB</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:48%;background:#6366f1"></span></span><span class="tp-11__bar-pct">48%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Mid</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:38%;background:#8b5cf6"></span></span><span class="tp-11__bar-pct">38%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:14%;background:#a78bfa"></span></span><span class="tp-11__bar-pct">14%</span></span>
                </span>
                <span class="tp-11__foot"><span>vs Q2: <strong>+$600K</strong></span><span>ARR: <strong>$13.6M</strong></span></span>
              </span>
            </span>
          </td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">$4.2M</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Revenue · Q4</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">$4.2M</span><span class="tp-11__change tp-11__up">↑ +24% vs Q3</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By segment</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">SMB</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:42%;background:#6366f1"></span></span><span class="tp-11__bar-pct">42%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Mid</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:38%;background:#8b5cf6"></span></span><span class="tp-11__bar-pct">38%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:20%;background:#a78bfa"></span></span><span class="tp-11__bar-pct">20%</span></span>
                </span>
                <span class="tp-11__foot"><span>vs Q3: <strong>+$800K</strong></span><span>Year: <strong>$12.5M</strong></span></span>
              </span>
            </span>
          </td>
        </tr>
        <tr>
          <td class="tp-11__row-label">Active Users</td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">12.4K</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Active Users · Q1</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">12.4K</span><span class="tp-11__change tp-11__up">↑ +22%</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By plan</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Free</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:58%;background:#22c55e"></span></span><span class="tp-11__bar-pct">58%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Pro</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:32%;background:#16a34a"></span></span><span class="tp-11__bar-pct">32%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:10%;background:#166534"></span></span><span class="tp-11__bar-pct">10%</span></span>
                </span>
                <span class="tp-11__foot"><span>New: <strong>+2,240</strong></span><span>DAU/MAU: <strong>41%</strong></span></span>
              </span>
            </span>
          </td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">18.9K</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Active Users · Q2</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">18.9K</span><span class="tp-11__change tp-11__up">↑ +52%</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By plan</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Free</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:54%;background:#22c55e"></span></span><span class="tp-11__bar-pct">54%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Pro</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:36%;background:#16a34a"></span></span><span class="tp-11__bar-pct">36%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:10%;background:#166534"></span></span><span class="tp-11__bar-pct">10%</span></span>
                </span>
                <span class="tp-11__foot"><span>New: <strong>+6,500</strong></span><span>DAU/MAU: <strong>44%</strong></span></span>
              </span>
            </span>
          </td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">24.1K</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Active Users · Q3</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">24.1K</span><span class="tp-11__change tp-11__up">↑ +28%</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By plan</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Free</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:50%;background:#22c55e"></span></span><span class="tp-11__bar-pct">50%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Pro</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:38%;background:#16a34a"></span></span><span class="tp-11__bar-pct">38%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:12%;background:#166534"></span></span><span class="tp-11__bar-pct">12%</span></span>
                </span>
                <span class="tp-11__foot"><span>New: <strong>+5,200</strong></span><span>DAU/MAU: <strong>47%</strong></span></span>
              </span>
            </span>
          </td>
          <td>
            <span class="tp-11__t">
              <span class="tp-11__val">31.8K</span>
              <span class="tp-11__tip">
                <span class="tp-11__head">
                  <span class="tp-11__metric">Active Users · Q4</span>
                  <span class="tp-11__big-row"><span class="tp-11__big">31.8K</span><span class="tp-11__change tp-11__up">↑ +32%</span></span>
                </span>
                <span class="tp-11__bars">
                  <span class="tp-11__bars-label">By plan</span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Free</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:44%;background:#22c55e"></span></span><span class="tp-11__bar-pct">44%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Pro</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:40%;background:#16a34a"></span></span><span class="tp-11__bar-pct">40%</span></span>
                  <span class="tp-11__bar-row"><span class="tp-11__bar-name">Ent.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:16%;background:#166534"></span></span><span class="tp-11__bar-pct">16%</span></span>
                </span>
                <span class="tp-11__foot"><span>New: <strong>+7,700</strong></span><span>YoY: <strong>+156%</strong></span></span>
              </span>
            </span>
          </td>
        </tr>
        <tr>
          <td class="tp-11__row-label">Churn</td>
          <td><span class="tp-11__t"><span class="tp-11__val">2.8%</span><span class="tp-11__tip"><span class="tp-11__head"><span class="tp-11__metric">Monthly Churn · Q1</span><span class="tp-11__big-row"><span class="tp-11__big">2.8%</span><span class="tp-11__change tp-11__dn">↓ +0.4pp worse</span></span></span><span class="tp-11__bars"><span class="tp-11__bars-label">Reason</span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Price</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:42%;background:#ef4444"></span></span><span class="tp-11__bar-pct">42%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Feat.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:31%;background:#f87171"></span></span><span class="tp-11__bar-pct">31%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Other</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:27%;background:#fca5a5"></span></span><span class="tp-11__bar-pct">27%</span></span></span><span class="tp-11__foot"><span>Net rev churn: <strong>1.1%</strong></span><span>Win-back: <strong>14%</strong></span></span></span></span></td>
          <td><span class="tp-11__t"><span class="tp-11__val">2.4%</span><span class="tp-11__tip"><span class="tp-11__head"><span class="tp-11__metric">Monthly Churn · Q2</span><span class="tp-11__big-row"><span class="tp-11__big">2.4%</span><span class="tp-11__change tp-11__up">↑ −0.4pp better</span></span></span><span class="tp-11__bars"><span class="tp-11__bars-label">Reason</span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Price</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:38%;background:#ef4444"></span></span><span class="tp-11__bar-pct">38%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Feat.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:34%;background:#f87171"></span></span><span class="tp-11__bar-pct">34%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Other</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:28%;background:#fca5a5"></span></span><span class="tp-11__bar-pct">28%</span></span></span><span class="tp-11__foot"><span>Net rev churn: <strong>0.8%</strong></span><span>Win-back: <strong>18%</strong></span></span></span></span></td>
          <td><span class="tp-11__t"><span class="tp-11__val">2.1%</span><span class="tp-11__tip"><span class="tp-11__head"><span class="tp-11__metric">Monthly Churn · Q3</span><span class="tp-11__big-row"><span class="tp-11__big">2.1%</span><span class="tp-11__change tp-11__up">↑ −0.3pp better</span></span></span><span class="tp-11__bars"><span class="tp-11__bars-label">Reason</span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Price</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:32%;background:#ef4444"></span></span><span class="tp-11__bar-pct">32%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Feat.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:38%;background:#f87171"></span></span><span class="tp-11__bar-pct">38%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Other</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:30%;background:#fca5a5"></span></span><span class="tp-11__bar-pct">30%</span></span></span><span class="tp-11__foot"><span>Net rev churn: <strong>0.6%</strong></span><span>Win-back: <strong>21%</strong></span></span></span></span></td>
          <td><span class="tp-11__t"><span class="tp-11__val">1.8%</span><span class="tp-11__tip"><span class="tp-11__head"><span class="tp-11__metric">Monthly Churn · Q4</span><span class="tp-11__big-row"><span class="tp-11__big">1.8%</span><span class="tp-11__change tp-11__up">↑ −0.3pp better</span></span></span><span class="tp-11__bars"><span class="tp-11__bars-label">Reason</span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Price</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:28%;background:#ef4444"></span></span><span class="tp-11__bar-pct">28%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Feat.</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:40%;background:#f87171"></span></span><span class="tp-11__bar-pct">40%</span></span><span class="tp-11__bar-row"><span class="tp-11__bar-name">Other</span><span class="tp-11__bar-track"><span class="tp-11__bar-fill" style="width:32%;background:#fca5a5"></span></span><span class="tp-11__bar-pct">32%</span></span></span><span class="tp-11__foot"><span>Net rev churn: <strong>0.4%</strong></span><span>Year: <strong>−1.0pp</strong></span></span></span></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```
## CSS
```css
.tp-11 {
  width: 100%;
  min-height: 100vh;
  background: #f8f9fa;
  /* Top room — table cell tips pop UP from each value (~220px tall). */
  padding: 240px 28px 36px;
  font-family: 'Inter', system-ui, sans-serif;
}

.tp-11__inner {
  max-width: 520px;
  margin: 0 auto;
}

.tp-11__table {
  width: 100%;
  border-collapse: collapse;
}

.tp-11__table thead th {
  font-size: 9.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
  font-weight: 500;
  padding: 0 14px 11px;
  text-align: right;
}

.tp-11__table thead th:first-child {
  text-align: left;
}

.tp-11__table tbody tr {
  border-top: 1px solid #eee;
}

.tp-11__table tbody tr:hover {
  background: rgba(0, 0, 0, 0.015);
}

.tp-11__table tbody td {
  padding: 12px 14px;
  font-size: 12.5px;
  color: #333;
  text-align: right;
  white-space: nowrap;
}

.tp-11__row-label {
  color: #777 !important;
  font-size: 11px !important;
  text-align: left !important;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.tp-11__t {
  position: relative;
  display: inline-block;
  cursor: help;
}

.tp-11__val {
  border-bottom: 1px dashed transparent;
  transition: border-color .15s, color .15s;
}

.tp-11__t:hover .tp-11__val {
  border-bottom-color: #aaa;
  color: #111;
}

.tp-11__tip {
  position: absolute;
  bottom: calc(100% + 9px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  width: 240px;
  background: #fff;
  border-radius: 9px;
  border: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.11), 0 2px 8px rgba(0, 0, 0, 0.05);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  z-index: 30;
  overflow: hidden;
  display: block;
  text-align: left;
  white-space: normal;
}

.tp-11__t:hover .tp-11__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-11__head {
  display: block;
  padding: 12px 13px 9px;
  border-bottom: 1px solid #f0f0f0;
}

.tp-11__metric {
  display: block;
  font-size: 9.5px;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  margin-bottom: 5px;
}

.tp-11__big-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.tp-11__big {
  font-size: 22px;
  font-weight: 700;
  color: #111;
}

.tp-11__change {
  font-size: 11px;
  font-weight: 600;
}

.tp-11__up {
  color: #16a34a;
}

.tp-11__dn {
  color: #dc2626;
}

.tp-11__bars {
  display: block;
  padding: 11px 13px 7px;
  border-bottom: 1px solid #f0f0f0;
}

.tp-11__bars-label {
  display: block;
  font-size: 7.5px;
  color: #bbb;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 7px;
}

.tp-11__bar-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 5px;
}

.tp-11__bar-name {
  font-size: 9.5px;
  color: #999;
  width: 32px;
  text-align: right;
  flex-shrink: 0;
}

.tp-11__bar-track {
  flex: 1;
  height: 5px;
  background: #f0f0f0;
  border-radius: 3px;
  overflow: hidden;
  display: block;
}

.tp-11__bar-fill {
  height: 100%;
  border-radius: 3px;
  display: block;
}

.tp-11__bar-pct {
  font-size: 9.5px;
  color: #bbb;
  width: 28px;
  flex-shrink: 0;
  text-align: right;
}

.tp-11__foot {
  display: flex;
  justify-content: space-between;
  padding: 10px 13px;
  font-size: 10.5px;
  color: #bbb;
}

.tp-11__foot strong {
  color: #555;
  font-weight: 600;
}
```
