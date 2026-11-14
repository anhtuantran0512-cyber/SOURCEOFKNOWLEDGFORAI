---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-sidebar-dashboard-layout/"
title: "CSS Flexbox Sidebar Dashboard Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A full app-shell dashboard with a fixed-width flex sidebar, collapsible nav groups, top header bar, stat cards row, and a main content area — all wired with…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Sidebar Dashboard Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-sidebar-dashboard-layout/

A full app-shell dashboard with a fixed-width flex sidebar, collapsible nav groups, top header bar, stat cards row, and a main content area — all wired with flexbox.
## HTML
```html
<div class="fl-05">
  <div class="fl-05__shell">

    <!-- Sidebar -->
    <aside class="fl-05__sidebar">
      <div class="fl-05__sidebar-top">
        <div class="fl-05__workspace-icon">F</div>
        <div>
          <div class="fl-05__workspace-name">FlexBoard</div>
          <div class="fl-05__workspace-plan">Pro Plan</div>
        </div>
      </div>
      <nav class="fl-05__sidebar-nav">
        <div class="fl-05__nav-section">Main</div>
        <div class="fl-05__nav-item is-active">
          <div class="fl-05__nav-dot" style="background:#3b82f6"></div>
          Dashboard
        </div>
        <div class="fl-05__nav-item">
          <div class="fl-05__nav-dot" style="background:#8b5cf6"></div>
          Analytics
          <span class="fl-05__nav-count">12</span>
        </div>
        <div class="fl-05__nav-item">
          <div class="fl-05__nav-dot" style="background:#22c55e"></div>
          Projects
        </div>
        <div class="fl-05__nav-item">
          <div class="fl-05__nav-dot" style="background:#f97316"></div>
          Tasks
          <span class="fl-05__nav-count is-hot">3</span>
        </div>
        <div class="fl-05__nav-section">Settings</div>
        <div class="fl-05__nav-item">
          <div class="fl-05__nav-dot" style="background:#7d8590"></div>
          Members
        </div>
        <div class="fl-05__nav-item">
          <div class="fl-05__nav-dot" style="background:#7d8590"></div>
          Billing
        </div>
      </nav>
      <div class="fl-05__sidebar-bottom">
        <div class="fl-05__user-row">
          <div class="fl-05__user-avatar">JD</div>
          <div>
            <div class="fl-05__user-name">Jane Doe</div>
            <div class="fl-05__user-role">Admin</div>
          </div>
        </div>
      </div>
    </aside>

    <!-- Main -->
    <main class="fl-05__main">
      <div class="fl-05__topbar">
        <div class="fl-05__topbar-title">Dashboard Overview</div>
        <div class="fl-05__topbar-action fl-05__topbar-action--ghost">⬇ Export</div>
        <div class="fl-05__topbar-action fl-05__topbar-action--primary">+ New Project</div>
      </div>
      <div class="fl-05__content">
        <div class="fl-05__stats">
          <div class="fl-05__stat">
            <div class="fl-05__stat-label">Total Revenue</div>
            <div class="fl-05__stat-value">$48.2k</div>
            <div class="fl-05__stat-delta up">↑ 12.5% this month</div>
          </div>
          <div class="fl-05__stat">
            <div class="fl-05__stat-label">Active Users</div>
            <div class="fl-05__stat-value">2,841</div>
            <div class="fl-05__stat-delta up">↑ 8.1% this week</div>
          </div>
          <div class="fl-05__stat">
            <div class="fl-05__stat-label">Open Tasks</div>
            <div class="fl-05__stat-value">34</div>
            <div class="fl-05__stat-delta down">↓ 3 from yesterday</div>
          </div>
        </div>

        <div class="fl-05__activity">
          <div class="fl-05__activity-head">
            Recent Activity
            <span class="fl-05__activity-view">View all</span>
          </div>
          <div class="fl-05__activity-row">
            <div class="fl-05__activity-dot" style="background:#22c55e"></div>
            <div class="fl-05__activity-text">Deployment to production succeeded</div>
            <div class="fl-05__activity-time">2m ago</div>
          </div>
          <div class="fl-05__activity-row">
            <div class="fl-05__activity-dot" style="background:#3b82f6"></div>
            <div class="fl-05__activity-text">New member <strong style="color:#e6edf3">@alex</strong> joined the workspace</div>
            <div class="fl-05__activity-time">14m ago</div>
          </div>
          <div class="fl-05__activity-row">
            <div class="fl-05__activity-dot" style="background:#f97316"></div>
            <div class="fl-05__activity-text">Task "CSS Flexbox docs" moved to Review</div>
            <div class="fl-05__activity-time">1h ago</div>
          </div>
          <div class="fl-05__activity-row">
            <div class="fl-05__activity-dot" style="background:#ef4444"></div>
            <div class="fl-05__activity-text">Build #142 failed — check logs</div>
            <div class="fl-05__activity-time">3h ago</div>
          </div>
        </div>
      </div>
    </main>

  </div>
</div>
```
## CSS
```css
.fl-05,
.fl-05 *,
.fl-05 *::before,
.fl-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-05 ::selection {
  background: #3b82f6;
  color: #fff;
}

.fl-05 {
  --bg: #0d1117;
  --sidebar: #161b22;
  --surface: #1c2128;
  --border: #30363d;
  --accent: #3b82f6;
  --accent2: #8b5cf6;
  --green: #22c55e;
  --orange: #f97316;
  --red: #ef4444;
  --text: #e6edf3;
  --muted: #7d8590;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: var(--bg);
  border-radius: 16px;
  overflow: hidden;
  min-height: 500px;
}
/* Outer flex row: sidebar + main */

.fl-05__shell {
  display: flex;
  height: 500px;
}
/* ── Sidebar ── */

.fl-05__sidebar {
  width: 220px;
  flex-shrink: 0;
  background: var(--sidebar);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  padding: 0;
}

.fl-05__sidebar-top {
  padding: 20px 16px 12px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}

.fl-05__workspace-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: 800;
  color: #fff;
  flex-shrink: 0;
}

.fl-05__workspace-name {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text);
}

.fl-05__workspace-plan {
  font-size: 0.65rem;
  color: var(--accent);
  font-weight: 600;
}

.fl-05__sidebar-nav {
  flex: 1;
  padding: 12px 8px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  overflow-y: auto;
}

.fl-05__nav-section {
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 10px 8px 4px;
}

.fl-05__nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 10px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--muted);
  transition: all 0.15s;
  position: relative;
}

.fl-05__nav-item:hover {
  background: rgba(255,255,255,0.06);
  color: var(--text);
}

.fl-05__nav-item.is-active {
  background: rgba(59,130,246,0.15);
  color: var(--accent);
  font-weight: 600;
}

.fl-05__nav-item.is-active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 60%;
  background: var(--accent);
  border-radius: 0 2px 2px 0;
}

.fl-05__nav-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.fl-05__nav-count {
  margin-left: auto;
  font-size: 0.65rem;
  font-weight: 700;
  background: rgba(255,255,255,0.08);
  padding: 1px 6px;
  border-radius: 10px;
  color: var(--muted);
}

.fl-05__nav-count.is-hot {
  background: var(--red);
  color: #fff;
}

.fl-05__sidebar-bottom {
  padding: 12px 8px;
  border-top: 1px solid var(--border);
}

.fl-05__user-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.15s;
}

.fl-05__user-row:hover {
  background: rgba(255,255,255,0.06);
}

.fl-05__user-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f97316, #ef4444);
  font-size: 0.7rem;
  font-weight: 800;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.fl-05__user-name {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text);
}

.fl-05__user-role {
  font-size: 0.65rem;
  color: var(--muted);
}
/* ── Main panel ── */

.fl-05__main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.fl-05__topbar {
  height: 52px;
  background: var(--sidebar);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  padding: 0 20px;
  gap: 12px;
  flex-shrink: 0;
}

.fl-05__topbar-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text);
  flex: 1;
}

.fl-05__topbar-action {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
}

.fl-05__topbar-action--primary {
  background: var(--accent);
  color: #fff;
}

.fl-05__topbar-action--ghost {
  background: rgba(255,255,255,0.06);
  color: var(--muted);
  border: 1px solid var(--border);
}

.fl-05__content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
/* Stats row */

.fl-05__stats {
  display: flex;
  gap: 12px;
}

.fl-05__stat {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
}

.fl-05__stat-label {
  font-size: 0.68rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 8px;
}

.fl-05__stat-value {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--text);
}

.fl-05__stat-delta {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 0.72rem;
  font-weight: 600;
  margin-top: 4px;
}

.fl-05__stat-delta.up {
  color: var(--green);
}

.fl-05__stat-delta.down {
  color: var(--red);
}
/* Activity list */

.fl-05__activity {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
}

.fl-05__activity-head {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.fl-05__activity-view {
  font-size: 0.7rem;
  color: var(--accent);
  font-weight: 600;
  cursor: pointer;
}

.fl-05__activity-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  border-bottom: 1px solid rgba(48,54,61,0.5);
}

.fl-05__activity-row:last-child {
  border-bottom: none;
}

.fl-05__activity-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.fl-05__activity-text {
  flex: 1;
  font-size: 0.78rem;
  color: var(--text);
}

.fl-05__activity-time {
  font-size: 0.68rem;
  color: var(--muted);
  flex-shrink: 0;
}

@media (prefers-reduced-motion: reduce) {
  .fl-05__nav-item,
    .fl-05__user-row {
    transition: none;
  }
}
```
