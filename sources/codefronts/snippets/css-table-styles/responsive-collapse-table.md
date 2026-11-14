---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/responsive-collapse-table/"
title: "Responsive Collapse Table"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A multi-column team-member table that collapses into labelled card rows on mobile using CSS media queries and data-label attributes — no JavaScript required."
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Collapse Table
Source: https://codefronts.com/snippets/css-table-styles/responsive-collapse-table/

A multi-column team-member table that collapses into labelled card rows on mobile using CSS media queries and data-label attributes — no JavaScript required.
## HTML
```html
<div class="ct-01">
  <div class="ct-01__header">
    <div class="ct-01__icon">👥</div>
    <div>
      <div class="ct-01__title">Team Members</div>
      <div class="ct-01__sub">Resize the window to see the mobile card collapse</div>
    </div>
  </div>
  <div class="ct-01__table-wrap">
    <table>
      <thead>
        <tr>
          <th>User</th>
          <th>Role</th>
          <th>Status</th>
          <th>Joined</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td data-label="User">
            <div class="ct-01__avatar">
              <div class="ct-01__ava">AK</div>
              <div>
                <div class="ct-01__name">Arya Kapoor</div>
                <div class="ct-01__email">[email protected]</div>
              </div>
            </div>
          </td>
          <td data-label="Role"><span class="ct-01__role">Admin</span></td>
          <td data-label="Status"><span class="ct-01__badge ct-01__badge--active"><span class="ct-01__dot"></span>Active</span></td>
          <td data-label="Joined" style="color:var(--muted);font-size:13px">Jan 12, 2025</td>
          <td data-label="Actions">
            <div class="ct-01__action">
              <button class="ct-01__btn ct-01__btn--edit">Edit</button>
              <button class="ct-01__btn ct-01__btn--del">Del</button>
            </div>
          </td>
        </tr>
        <tr>
          <td data-label="User">
            <div class="ct-01__avatar">
              <div class="ct-01__ava" style="background:linear-gradient(135deg,#ff6b6b,#ffa07a)">MR</div>
              <div>
                <div class="ct-01__name">Marcus Reid</div>
                <div class="ct-01__email">[email protected]</div>
              </div>
            </div>
          </td>
          <td data-label="Role"><span class="ct-01__role">Developer</span></td>
          <td data-label="Status"><span class="ct-01__badge ct-01__badge--warn"><span class="ct-01__dot"></span>Pending</span></td>
          <td data-label="Joined" style="color:var(--muted);font-size:13px">Mar 4, 2025</td>
          <td data-label="Actions">
            <div class="ct-01__action">
              <button class="ct-01__btn ct-01__btn--edit">Edit</button>
              <button class="ct-01__btn ct-01__btn--del">Del</button>
            </div>
          </td>
        </tr>
        <tr>
          <td data-label="User">
            <div class="ct-01__avatar">
              <div class="ct-01__ava" style="background:linear-gradient(135deg,#00e676,#00b4d8)">SN</div>
              <div>
                <div class="ct-01__name">Selin Novak</div>
                <div class="ct-01__email">[email protected]</div>
              </div>
            </div>
          </td>
          <td data-label="Role"><span class="ct-01__role">Designer</span></td>
          <td data-label="Status"><span class="ct-01__badge ct-01__badge--active"><span class="ct-01__dot"></span>Active</span></td>
          <td data-label="Joined" style="color:var(--muted);font-size:13px">May 19, 2025</td>
          <td data-label="Actions">
            <div class="ct-01__action">
              <button class="ct-01__btn ct-01__btn--edit">Edit</button>
              <button class="ct-01__btn ct-01__btn--del">Del</button>
            </div>
          </td>
        </tr>
        <tr>
          <td data-label="User">
            <div class="ct-01__avatar">
              <div class="ct-01__ava" style="background:linear-gradient(135deg,#ff5252,#7c4dff)">TW</div>
              <div>
                <div class="ct-01__name">Theo Walsh</div>
                <div class="ct-01__email">[email protected]</div>
              </div>
            </div>
          </td>
          <td data-label="Role"><span class="ct-01__role">Manager</span></td>
          <td data-label="Status"><span class="ct-01__badge ct-01__badge--danger"><span class="ct-01__dot"></span>Inactive</span></td>
          <td data-label="Joined" style="color:var(--muted);font-size:13px">Nov 2, 2024</td>
          <td data-label="Actions">
            <div class="ct-01__action">
              <button class="ct-01__btn ct-01__btn--edit">Edit</button>
              <button class="ct-01__btn ct-01__btn--del">Del</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```
## CSS
```css
.ct-01,
.ct-01 *,
.ct-01 *::before,
.ct-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-01 ::selection {
  background: #6c63ff;
  color: #fff;
}

.ct-01 {
  --accent: #6c63ff;
  --accent2: #00d4ff;
  --bg: #0f0f1a;
  --card: #1a1a2e;
  --border: #2a2a4a;
  --text: #e0e0f0;
  --muted: #888ab0;
  --success: #00e676;
  --warn: #ffab40;
  --danger: #ff5252;
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 32px 24px;
  color: var(--text);
}

.ct-01__header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
}

.ct-01__icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
}

.ct-01__title {
  font-size: 20px;
  font-weight: 700;
}

.ct-01__sub {
  font-size: 13px;
  color: var(--muted);
  margin-top: 2px;
}

.ct-01__table-wrap {
  overflow-x: auto;
  border-radius: 14px;
  border: 1px solid var(--border);
  background: var(--card);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}

.ct-01 table {
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;
}

.ct-01 thead tr {
  background: linear-gradient(90deg, rgba(108,99,255,0.15), rgba(0,212,255,0.08));
  border-bottom: 2px solid var(--border);
}

.ct-01 thead th {
  padding: 14px 20px;
  text-align: left;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--muted);
  white-space: nowrap;
}

.ct-01 thead th:first-child {
  color: var(--accent2);
}

.ct-01 tbody tr {
  border-bottom: 1px solid var(--border);
  transition: background 0.2s, transform 0.2s;
  cursor: pointer;
}

.ct-01 tbody tr:last-child {
  border-bottom: none;
}

.ct-01 tbody tr:hover {
  background: rgba(108,99,255,0.08);
  transform: translateX(3px);
}

.ct-01 tbody td {
  padding: 16px 20px;
  font-size: 14px;
  vertical-align: middle;
}

.ct-01__avatar {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ct-01__ava {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 13px;
  flex-shrink: 0;
  box-shadow: 0 0 12px rgba(108,99,255,0.4);
}

.ct-01__name {
  font-weight: 600;
}

.ct-01__email {
  font-size: 12px;
  color: var(--muted);
  margin-top: 1px;
}

.ct-01__badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
}

.ct-01__badge--active {
  background: rgba(0,230,118,0.15);
  color: var(--success);
}

.ct-01__badge--warn {
  background: rgba(255,171,64,0.15);
  color: var(--warn);
}

.ct-01__badge--danger {
  background: rgba(255,82,82,0.15);
  color: var(--danger);
}

.ct-01__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  animation: ct-01-pulse 2s infinite;
}

@keyframes ct-01-pulse {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.5;
    transform: scale(0.7);
  }
}

.ct-01__role {
  display: inline-block;
  padding: 3px 9px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
  background: rgba(108,99,255,0.12);
  color: var(--accent);
  border: 1px solid rgba(108,99,255,0.25);
}

.ct-01__action {
  display: flex;
  gap: 8px;
}

.ct-01__btn {
  padding: 5px 12px;
  border-radius: 7px;
  font-size: 12px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
}

.ct-01__btn--edit {
  background: rgba(108,99,255,0.2);
  color: var(--accent);
}

.ct-01__btn--edit:hover {
  background: var(--accent);
  color: #fff;
}

.ct-01__btn--del {
  background: rgba(255,82,82,0.1);
  color: var(--danger);
}

.ct-01__btn--del:hover {
  background: var(--danger);
  color: #fff;
}
/* ── RESPONSIVE COLLAPSE ── */

@media (max-width: 640px) {
  .ct-01 table,
    .ct-01 thead,
    .ct-01 tbody,
    .ct-01 th,
    .ct-01 td,
    .ct-01 tr {
    display: block;
  }

  .ct-01 thead {
    display: none;
  }

  .ct-01 tbody tr {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 12px;
    padding: 4px 0;
    transform: none !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
  }

  .ct-01 tbody td {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
    font-size: 13px;
  }

  .ct-01 tbody td:last-child {
    border-bottom: none;
  }

  .ct-01 tbody td::before {
    content: attr(data-label);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--muted);
    min-width: 80px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ct-01__dot,
    .ct-01 tbody tr {
    animation: none;
    transition: none;
  }
}
```
