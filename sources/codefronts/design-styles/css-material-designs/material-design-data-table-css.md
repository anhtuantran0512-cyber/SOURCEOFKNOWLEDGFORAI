---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-data-table-css/"
title: "Material Design Data Table CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Sortable-look data table with row checkboxes, status badges, inline progress bars, avatar cells, pagination controls, and a dense display variant."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Data Table CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-data-table-css/

Sortable-look data table with row checkboxes, status badges, inline progress bars, avatar cells, pagination controls, and a dense display variant.
## HTML
```html
<div class="md-06">
  <div class="md-06__wrap">
    <div class="md-06__page-title">Material Design Data Tables</div>
    <div class="md-06__page-sub">Full-featured sortable data tables with checkboxes, status badges, progress bars and pagination — CSS</div>

    <!-- Main Table -->
    <div class="md-06__table-card">
      <div class="md-06__table-toolbar">
        <div class="md-06__table-title">Team Members</div>
        <input class="md-06__search" type="text" placeholder="🔍 Search members...">
        <div class="md-06__table-actions">
          <button class="md-06__tool-btn md-06__tool-btn--ghost">Export</button>
          <button class="md-06__tool-btn md-06__tool-btn--p">+ Invite</button>
        </div>
      </div>
      <div class="md-06__table-wrap">
        <table class="md-06__table">
          <thead>
            <tr>
              <th class="md-06__th" style="width:48px"><input class="md-06__check" type="checkbox"></th>
              <th class="md-06__th md-06__th--sorted">Name</th>
              <th class="md-06__th">Role</th>
              <th class="md-06__th">Status</th>
              <th class="md-06__th">Tasks</th>
              <th class="md-06__th md-06__th--num">Completed</th>
              <th class="md-06__th">Joined</th>
              <th class="md-06__th" style="width:100px">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr class="md-06__tr">
              <td class="md-06__td"><input class="md-06__check" type="checkbox" checked></td>
              <td class="md-06__td"><div class="md-06__cell-user"><div class="md-06__avatar" style="background:#0277bd">A</div><div><div style="font-weight:500">Alex Thompson</div><div style="font-size:.78rem;color:var(--ink3)">[email protected]</div></div></div></td>
              <td class="md-06__td">Lead Designer</td>
              <td class="md-06__td"><span class="md-06__badge md-06__badge--active">● Active</span></td>
              <td class="md-06__td"><div class="md-06__progress-wrap"><div class="md-06__progress-track"><div class="md-06__progress-fill" style="width:92%"></div></div><span class="md-06__progress-val">92%</span></div></td>
              <td class="md-06__td md-06__td--num">23/25</td>
              <td class="md-06__td" style="color:var(--ink2)">Jan 2023</td>
              <td class="md-06__td"><button class="md-06__row-action" title="Edit">✏</button><button class="md-06__row-action" title="View">👁</button><button class="md-06__row-action" title="More">⋮</button></td>
            </tr>
            <tr class="md-06__tr">
              <td class="md-06__td"><input class="md-06__check" type="checkbox"></td>
              <td class="md-06__td"><div class="md-06__cell-user"><div class="md-06__avatar" style="background:#e91e63">M</div><div><div style="font-weight:500">Maria Chen</div><div style="font-size:.78rem;color:var(--ink3)">[email protected]</div></div></div></td>
              <td class="md-06__td">UI Engineer</td>
              <td class="md-06__td"><span class="md-06__badge md-06__badge--active">● Active</span></td>
              <td class="md-06__td"><div class="md-06__progress-wrap"><div class="md-06__progress-track"><div class="md-06__progress-fill" style="width:78%"></div></div><span class="md-06__progress-val">78%</span></div></td>
              <td class="md-06__td md-06__td--num">14/18</td>
              <td class="md-06__td" style="color:var(--ink2)">Mar 2023</td>
              <td class="md-06__td"><button class="md-06__row-action">✏</button><button class="md-06__row-action">👁</button><button class="md-06__row-action">⋮</button></td>
            </tr>
            <tr class="md-06__tr">
              <td class="md-06__td"><input class="md-06__check" type="checkbox"></td>
              <td class="md-06__td"><div class="md-06__cell-user"><div class="md-06__avatar" style="background:#00897b">J</div><div><div style="font-weight:500">Jordan Kim</div><div style="font-size:.78rem;color:var(--ink3)">[email protected]</div></div></div></td>
              <td class="md-06__td">Product Manager</td>
              <td class="md-06__td"><span class="md-06__badge md-06__badge--review">◑ In Review</span></td>
              <td class="md-06__td"><div class="md-06__progress-wrap"><div class="md-06__progress-track"><div class="md-06__progress-fill" style="width:55%;background:#3949ab"></div></div><span class="md-06__progress-val">55%</span></div></td>
              <td class="md-06__td md-06__td--num">11/20</td>
              <td class="md-06__td" style="color:var(--ink2)">Jun 2023</td>
              <td class="md-06__td"><button class="md-06__row-action">✏</button><button class="md-06__row-action">👁</button><button class="md-06__row-action">⋮</button></td>
            </tr>
            <tr class="md-06__tr">
              <td class="md-06__td"><input class="md-06__check" type="checkbox"></td>
              <td class="md-06__td"><div class="md-06__cell-user"><div class="md-06__avatar" style="background:#7b1fa2">S</div><div><div style="font-weight:500">Sam Rivera</div><div style="font-size:.78rem;color:var(--ink3)">[email protected]</div></div></div></td>
              <td class="md-06__td">Dev Lead</td>
              <td class="md-06__td"><span class="md-06__badge md-06__badge--pending">◔ Pending</span></td>
              <td class="md-06__td"><div class="md-06__progress-wrap"><div class="md-06__progress-track"><div class="md-06__progress-fill" style="width:35%;background:#f57f17"></div></div><span class="md-06__progress-val">35%</span></div></td>
              <td class="md-06__td md-06__td--num">7/20</td>
              <td class="md-06__td" style="color:var(--ink2)">Sep 2023</td>
              <td class="md-06__td"><button class="md-06__row-action">✏</button><button class="md-06__row-action">👁</button><button class="md-06__row-action">⋮</button></td>
            </tr>
            <tr class="md-06__tr">
              <td class="md-06__td"><input class="md-06__check" type="checkbox"></td>
              <td class="md-06__td"><div class="md-06__cell-user"><div class="md-06__avatar" style="background:#f57c00">P</div><div><div style="font-weight:500">Priya Nair</div><div style="font-size:.78rem;color:var(--ink3)">[email protected]</div></div></div></td>
              <td class="md-06__td">QA Engineer</td>
              <td class="md-06__td"><span class="md-06__badge md-06__badge--inactive">○ Inactive</span></td>
              <td class="md-06__td"><div class="md-06__progress-wrap"><div class="md-06__progress-track"><div class="md-06__progress-fill" style="width:10%;background:#c62828"></div></div><span class="md-06__progress-val">10%</span></div></td>
              <td class="md-06__td md-06__td--num">2/20</td>
              <td class="md-06__td" style="color:var(--ink2)">Nov 2023</td>
              <td class="md-06__td"><button class="md-06__row-action">✏</button><button class="md-06__row-action">👁</button><button class="md-06__row-action">⋮</button></td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="md-06__pagination">
        <span class="md-06__pager-info">Rows per page: 10 &nbsp;·&nbsp; 1–5 of 42</span>
        <button class="md-06__page-btn">«</button>
        <button class="md-06__page-btn md-06__page-btn--active">1</button>
        <button class="md-06__page-btn">2</button>
        <button class="md-06__page-btn">3</button>
        <button class="md-06__page-btn">4</button>
        <button class="md-06__page-btn">5</button>
        <button class="md-06__page-btn">»</button>
      </div>
    </div>

    <!-- Dense Table -->
    <div class="md-06__table-card">
      <div class="md-06__table-toolbar">
        <div class="md-06__table-title">Recent Transactions</div>
        <div class="md-06__table-actions">
          <button class="md-06__tool-btn md-06__tool-btn--ghost">Filter</button>
          <button class="md-06__tool-btn md-06__tool-btn--ghost">Download</button>
        </div>
      </div>
      <div class="md-06__table-wrap">
        <table class="md-06__table md-06__table--dense">
          <thead>
            <tr>
              <th class="md-06__th">Date</th>
              <th class="md-06__th">Description</th>
              <th class="md-06__th">Category</th>
              <th class="md-06__th">Status</th>
              <th class="md-06__th md-06__th--num md-06__th--sorted">Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr class="md-06__tr"><td class="md-06__td" style="color:var(--ink2)">Jun 11, 2025</td><td class="md-06__td" style="font-weight:500">AWS Infrastructure</td><td class="md-06__td">Cloud</td><td class="md-06__td"><span class="md-06__badge md-06__badge--active">Paid</span></td><td class="md-06__td md-06__td--num" style="color:#c62828">-$1,240.00</td></tr>
            <tr class="md-06__tr"><td class="md-06__td" style="color:var(--ink2)">Jun 10, 2025</td><td class="md-06__td" style="font-weight:500">Client Invoice #0042</td><td class="md-06__td">Revenue</td><td class="md-06__td"><span class="md-06__badge md-06__badge--active">Settled</span></td><td class="md-06__td md-06__td--num" style="color:#2e7d32">+$8,500.00</td></tr>
            <tr class="md-06__tr"><td class="md-06__td" style="color:var(--ink2)">Jun 09, 2025</td><td class="md-06__td" style="font-weight:500">Figma Enterprise</td><td class="md-06__td">Tools</td><td class="md-06__td"><span class="md-06__badge md-06__badge--pending">Pending</span></td><td class="md-06__td md-06__td--num" style="color:#c62828">-$540.00</td></tr>
            <tr class="md-06__tr"><td class="md-06__td" style="color:var(--ink2)">Jun 08, 2025</td><td class="md-06__td" style="font-weight:500">Contractor Payment</td><td class="md-06__td">Payroll</td><td class="md-06__td"><span class="md-06__badge md-06__badge--active">Paid</span></td><td class="md-06__td md-06__td--num" style="color:#c62828">-$2,800.00</td></tr>
            <tr class="md-06__tr"><td class="md-06__td" style="color:var(--ink2)">Jun 07, 2025</td><td class="md-06__td" style="font-weight:500">Retainer Fee Q2</td><td class="md-06__td">Revenue</td><td class="md-06__td"><span class="md-06__badge md-06__badge--review">Processing</span></td><td class="md-06__td md-06__td--num" style="color:#2e7d32">+$12,000.00</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-06,
.md-06 *,
.md-06 *::before,
.md-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-06 ::selection {
  background: #0277bd;
  color: #fff;
}

.md-06 {
  --primary: #0277bd;
  --primary-l: #4fc3f7;
  --secondary: #ff6f00;
  --surface: #fff;
  --bg: #e1f5fe;
  --ink: #212121;
  --ink2: #546e7a;
  --ink3: #90a4ae;
  --divider: #b0bec5;
  --row-hover: #e3f2fd;
  --row-selected: #e8f4fd;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-06__wrap {
  max-width: 1100px;
  margin: 0 auto;
}

.md-06__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
}

.md-06__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  margin-bottom: 40px;
}
/* ── TABLE CONTAINER ── */

.md-06__table-card {
  background: var(--surface);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,.1),0 1px 3px rgba(0,0,0,.06);
  margin-bottom: 40px;
}

.md-06__table-toolbar {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 20px 16px;
  border-bottom: 1px solid var(--divider);
  flex-wrap: wrap;
}

.md-06__table-title {
  font-size: 1.1rem;
  font-weight: 700;
  flex: 1;
  min-width: 120px;
}

.md-06__table-actions {
  display: flex;
  gap: 8px;
}

.md-06__tool-btn {
  height: 36px;
  padding: 0 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: 'Roboto';
  font-size: .8rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  transition: background .15s;
}

.md-06__tool-btn--p {
  background: var(--primary);
  color: #fff;
}

.md-06__tool-btn--p:hover {
  background: #01579b;
}

.md-06__tool-btn--ghost {
  background: transparent;
  color: var(--primary);
  border: 1px solid rgba(2,119,189,.4);
}

.md-06__tool-btn--ghost:hover {
  background: rgba(2,119,189,.06);
}

.md-06__search {
  height: 36px;
  padding: 0 12px;
  border: 1px solid var(--divider);
  border-radius: 4px;
  font-family: 'Roboto';
  font-size: .875rem;
  color: var(--ink);
  outline: none;
  width: 200px;
  transition: border-color .15s;
}

.md-06__search:focus {
  border-color: var(--primary);
}
/* ── TABLE ── */

.md-06__table-wrap {
  overflow-x: auto;
}

.md-06__table {
  width: 100%;
  border-collapse: collapse;
  font-size: .875rem;
}

.md-06__table thead {
  background: #fafafa;
}

.md-06__th {
  padding: 14px 16px;
  text-align: left;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink2);
  white-space: nowrap;
  border-bottom: 2px solid var(--divider);
  cursor: pointer;
  user-select: none;
  position: relative;
}

.md-06__th:hover {
  color: var(--primary);
}

.md-06__th--sorted {
  color: var(--primary);
}

.md-06__th--sorted::after {
  content: ' ↑';
  font-size: .7rem;
}

.md-06__th--num {
  text-align: right;
}

.md-06__td {
  padding: 14px 16px;
  border-bottom: 1px solid #eceff1;
  vertical-align: middle;
  color: var(--ink);
}

.md-06__td--num {
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-weight: 500;
}

.md-06__tr {
  transition: background .12s;
}

.md-06__tr:hover .md-06__td {
  background: var(--row-hover);
}

.md-06__tr:last-child .md-06__td {
  border-bottom: none;
}
/* Checkbox column */

.md-06__check {
  appearance: none;
  width: 18px;
  height: 18px;
  border: 2px solid var(--ink3);
  border-radius: 3px;
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
  transition: background .12s,border-color .12s;
}

.md-06__check:checked {
  background: var(--primary);
  border-color: var(--primary);
}

.md-06__check:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  color: #fff;
  font-size: .7rem;
  font-weight: 700;
  line-height: 1;
}
/* Status badges */

.md-06__badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: .75rem;
  font-weight: 500;
  white-space: nowrap;
}

.md-06__badge--active {
  background: #e8f5e9;
  color: #2e7d32;
}

.md-06__badge--pending {
  background: #fff8e1;
  color: #f57f17;
}

.md-06__badge--inactive {
  background: #fce4ec;
  color: #c62828;
}

.md-06__badge--review {
  background: #e8eaf6;
  color: #3949ab;
}
/* Avatar cell */

.md-06__cell-user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.md-06__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .8rem;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}
/* Progress bar cell */

.md-06__progress-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.md-06__progress-track {
  height: 4px;
  background: #e0e0e0;
  border-radius: 2px;
  width: 80px;
  overflow: hidden;
  flex-shrink: 0;
}

.md-06__progress-fill {
  height: 100%;
  border-radius: 2px;
  background: var(--primary);
}

.md-06__progress-val {
  font-size: .8rem;
  color: var(--ink2);
  font-variant-numeric: tabular-nums;
  width: 32px;
}
/* Row actions */

.md-06__row-action {
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--ink3);
  padding: 4px 6px;
  border-radius: 4px;
  font-size: 1rem;
  transition: color .15s,background .15s;
}

.md-06__row-action:hover {
  color: var(--primary);
  background: rgba(2,119,189,.08);
}
/* ── PAGINATION ── */

.md-06__pagination {
  display: flex;
  align-items: center;
  gap: 4px;
  justify-content: flex-end;
  padding: 12px 16px;
  border-top: 1px solid var(--divider);
  flex-wrap: wrap;
}

.md-06__pager-info {
  font-size: .85rem;
  color: var(--ink2);
  margin-right: 16px;
}

.md-06__page-btn {
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 4px;
  background: transparent;
  font-family: 'Roboto';
  font-size: .85rem;
  font-weight: 500;
  color: var(--ink2);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background .12s,color .12s;
}

.md-06__page-btn:hover {
  background: rgba(2,119,189,.08);
  color: var(--primary);
}

.md-06__page-btn--active {
  background: var(--primary);
  color: #fff;
}

.md-06__page-btn--active:hover {
  background: #01579b;
  color: #fff;
}
/* ── DENSE TABLE ── */

.md-06__table--dense .md-06__th,
.md-06__table--dense .md-06__td {
  padding: 8px 12px;
}

.md-06__table--dense .md-06__badge {
  padding: 2px 8px;
  font-size: .72rem;
}

@media (prefers-reduced-motion: reduce) {
  .md-06 * {
    transition: none!important;
  }
}
```
