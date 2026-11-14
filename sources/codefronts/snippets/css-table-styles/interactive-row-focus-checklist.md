---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/interactive-row-focus-checklist/"
title: "Interactive Row Focus Checklist"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A sprint task board where checking a row's checkbox triggers a full-row state change — background shift, strikethrough text, 4 px right slide, and a badge…"
has_js: "true"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Row Focus Checklist
Source: https://codefronts.com/snippets/css-table-styles/interactive-row-focus-checklist/

A sprint task board where checking a row's checkbox triggers a full-row state change — background shift, strikethrough text, 4 px right slide, and a badge swap — using the CSS :has() pseudo-class with a JS progress bar.
## HTML
```html
<div class="ct-09">
  <div class="ct-09__header">
    <div>
      <div class="ct-09__title">🚀 Sprint Task Board</div>
      <div class="ct-09__progress">0 of 5 completed</div>
      <div class="ct-09__progress-bar-wrap"><div class="ct-09__progress-bar" id="ct-09-bar"></div></div>
    </div>
  </div>
  <table>
    <thead>
      <tr>
        <th style="width:40px">Done</th>
        <th>Task</th>
        <th>Priority</th>
        <th>Assignee</th>
        <th>Due</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="ct-09__cb-wrap"><input class="ct-09__cb" type="checkbox" id="ct-09-t1"></td>
        <td><div class="ct-09__task"><div class="ct-09__task-name">Redesign onboarding flow UI</div><div class="ct-09__task-meta">Design → Engineering handoff</div></div></td>
        <td><span class="ct-09__priority ct-09__priority--high">High</span></td>
        <td><div class="ct-09__assignee" style="background:linear-gradient(135deg,#6366f1,#06b6d4)">AK</div></td>
        <td><div class="ct-09__due ct-09__due--overdue">Jun 18 ⚠</div></td>
        <td><span class="ct-09__status-badge">In Progress</span><span class="ct-09__done-badge">✓ Done</span></td>
      </tr>
      <tr>
        <td class="ct-09__cb-wrap"><input class="ct-09__cb" type="checkbox" id="ct-09-t2"></td>
        <td><div class="ct-09__task"><div class="ct-09__task-name">Set up CI/CD pipeline for staging</div><div class="ct-09__task-meta">DevOps → GitHub Actions</div></div></td>
        <td><span class="ct-09__priority ct-09__priority--high">High</span></td>
        <td><div class="ct-09__assignee" style="background:linear-gradient(135deg,#f59e0b,#ef4444)">MR</div></td>
        <td><div class="ct-09__due">Jun 22</div></td>
        <td><span class="ct-09__status-badge">Review</span><span class="ct-09__done-badge">✓ Done</span></td>
      </tr>
      <tr>
        <td class="ct-09__cb-wrap"><input class="ct-09__cb" type="checkbox" id="ct-09-t3"></td>
        <td><div class="ct-09__task"><div class="ct-09__task-name">Write unit tests for Auth module</div><div class="ct-09__task-meta">Backend coverage ≥ 80%</div></div></td>
        <td><span class="ct-09__priority ct-09__priority--med">Medium</span></td>
        <td><div class="ct-09__assignee" style="background:linear-gradient(135deg,#10b981,#0ea5e9)">SN</div></td>
        <td><div class="ct-09__due">Jun 25</div></td>
        <td><span class="ct-09__status-badge">Todo</span><span class="ct-09__done-badge">✓ Done</span></td>
      </tr>
      <tr>
        <td class="ct-09__cb-wrap"><input class="ct-09__cb" type="checkbox" id="ct-09-t4"></td>
        <td><div class="ct-09__task"><div class="ct-09__task-name">Update API documentation</div><div class="ct-09__task-meta">OpenAPI 3.1 spec + Postman collection</div></div></td>
        <td><span class="ct-09__priority ct-09__priority--low">Low</span></td>
        <td><div class="ct-09__assignee" style="background:linear-gradient(135deg,#8b5cf6,#ec4899)">TW</div></td>
        <td><div class="ct-09__due">Jun 28</div></td>
        <td><span class="ct-09__status-badge">Todo</span><span class="ct-09__done-badge">✓ Done</span></td>
      </tr>
      <tr>
        <td class="ct-09__cb-wrap"><input class="ct-09__cb" type="checkbox" id="ct-09-t5"></td>
        <td><div class="ct-09__task"><div class="ct-09__task-name">Performance audit — Lighthouse score</div><div class="ct-09__task-meta">Target: 95+ on all metrics</div></div></td>
        <td><span class="ct-09__priority ct-09__priority--med">Medium</span></td>
        <td><div class="ct-09__assignee" style="background:linear-gradient(135deg,#f43f5e,#fb923c)">JP</div></td>
        <td><div class="ct-09__due">Jul 1</div></td>
        <td><span class="ct-09__status-badge">Todo</span><span class="ct-09__done-badge">✓ Done</span></td>
      </tr>
    </tbody>
  </table>
</div>
```
## CSS
```css
.ct-09,
.ct-09 *,
.ct-09 *::before,
.ct-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-09 ::selection {
  background: #6366f1;
  color: #fff;
}

.ct-09 {
  --bg: #f8f7ff;
  --card: #ffffff;
  --border: #e0dff8;
  --text: #1e1b4b;
  --muted: #9794b8;
  --accent: #6366f1;
  --accent2: #818cf8;
  --done-bg: #f0fdf4;
  --done-border: #bbf7d0;
  --done-text: #166534;
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  padding: 36px 28px;
  min-height: 100vh;
  color: var(--text);
}

.ct-09__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.ct-09__title {
  font-size: 20px;
  font-weight: 800;
}

.ct-09__progress {
  font-size: 12px;
  color: var(--muted);
  font-weight: 600;
}

.ct-09__progress-bar-wrap {
  height: 4px;
  background: var(--border);
  border-radius: 2px;
  margin-top: 8px;
  overflow: hidden;
}

.ct-09__progress-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  border-radius: 2px;
  width: 0%;
  transition: width 0.4s ease;
}

.ct-09 table {
  width: 100%;
  border-collapse: collapse;
}

.ct-09 thead th {
  padding: 10px 16px;
  text-align: left;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  border-bottom: 2px solid var(--border);
}
/* ── THE :has() MAGIC ── */
/* Default state */

.ct-09 tbody tr {
  border-bottom: 1px solid var(--border);
  transition: background 0.3s, transform 0.3s, opacity 0.3s;
  cursor: pointer;
}
/* When a row's checkbox is checked: shift right + change background + strikethrough */

.ct-09 tbody tr:has(input[type="checkbox"]:checked) {
  background: var(--done-bg);
  border-left: 3px solid #22c55e;
  transform: translateX(4px);
}

.ct-09 tbody tr:has(input[type="checkbox"]:checked) .ct-09__task-name {
  text-decoration: line-through;
  color: var(--muted);
}

.ct-09 tbody tr:has(input[type="checkbox"]:checked) .ct-09__priority {
  opacity: 0.3;
}

.ct-09 tbody tr:has(input[type="checkbox"]:checked) .ct-09__done-badge {
  display: inline-flex;
}

.ct-09 tbody tr:has(input[type="checkbox"]:checked) .ct-09__status-badge {
  display: none;
}
/* Hover on unchecked rows */

.ct-09 tbody tr:not(:has(input[type="checkbox"]:checked)):hover {
  background: rgba(99,102,241,0.04);
}

.ct-09 tbody td {
  padding: 14px 16px;
  vertical-align: middle;
  font-size: 14px;
}

.ct-09 tbody tr:has(input[type="checkbox"]:checked) td {
  border-bottom-color: var(--done-border);
}
/* Custom checkbox */

.ct-09__cb-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
}

.ct-09__cb {
  width: 20px;
  height: 20px;
  appearance: none;
  -webkit-appearance: none;
  border: 2px solid var(--border);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
  position: relative;
  background: white;
}

.ct-09__cb:hover {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(99,102,241,0.15);
}

.ct-09__cb:checked {
  background: var(--accent);
  border-color: var(--accent);
  box-shadow: none;
}

.ct-09__cb:checked::after {
  content: '✓';
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 12px;
  font-weight: 800;
}

.ct-09__task {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  flex-direction: column;
}

.ct-09__task-name {
  font-weight: 600;
  font-size: 14px;
  transition: all 0.3s;
}

.ct-09__task-meta {
  font-size: 11px;
  color: var(--muted);
}

.ct-09__priority {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 20px;
  letter-spacing: 0.5px;
  transition: opacity 0.3s;
}

.ct-09__priority--high {
  background: rgba(239,68,68,0.1);
  color: #dc2626;
}

.ct-09__priority--med {
  background: rgba(245,158,11,0.1);
  color: #d97706;
}

.ct-09__priority--low {
  background: rgba(99,102,241,0.1);
  color: var(--accent);
}

.ct-09__status-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  font-weight: 600;
  padding: 3px 9px;
  border-radius: 20px;
  background: rgba(99,102,241,0.08);
  color: var(--accent);
  border: 1px solid rgba(99,102,241,0.2);
}

.ct-09__done-badge {
  display: none;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 20px;
  background: rgba(34,197,94,0.12);
  color: #16a34a;
  border: 1px solid rgba(34,197,94,0.25);
  animation: ct-09-popIn 0.3s cubic-bezier(0.34,1.56,0.64,1);
}

@keyframes ct-09-popIn {
  from {
    transform: scale(0.7);
    opacity: 0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

.ct-09__assignee {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  color: #fff;
}

.ct-09__due {
  font-size: 12px;
  color: var(--muted);
}

.ct-09__due--overdue {
  color: #dc2626;
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .ct-09 tbody tr,
    .ct-09__cb,
    .ct-09__progress-bar,
    .ct-09__done-badge {
    transition: none;
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const checkboxes = document.querySelectorAll('.ct-09__cb');
  const bar = document.getElementById('ct-09-bar');
  const progressLabel = document.querySelector('.ct-09__progress');
  function update() {
    const total = checkboxes.length;
    const done = [...checkboxes].filter(c => c.checked).length;
    if (bar) bar.style.width = (done / total * 100) + '%';
    if (progressLabel) progressLabel.textContent = done + ' of ' + total + ' completed';
  }
  checkboxes.forEach(cb => cb.addEventListener('change', update));
})();
```
