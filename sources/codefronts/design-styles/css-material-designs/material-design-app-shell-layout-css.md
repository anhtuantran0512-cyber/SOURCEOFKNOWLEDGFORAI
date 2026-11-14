---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-app-shell-layout-css/"
title: "Material Design App Shell Layout CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Full responsive app shell with sticky top app bar, persistent navigation drawer, breadcrumb toolbar, three-column stats grid, activity feed list, and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design App Shell Layout CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-app-shell-layout-css/

Full responsive app shell with sticky top app bar, persistent navigation drawer, breadcrumb toolbar, three-column stats grid, activity feed list, and a floating action button — production-ready layout, no JavaScript.
## HTML
```html
<div class="md-14">
  <input class="drawer-toggle" type="checkbox" id="md14-drawer">

  <div class="app-shell">

    <!-- Top App Bar -->
    <header class="topbar">
      <label class="topbar-menu-btn" for="md14-drawer">
        <svg viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
      </label>
      <span class="topbar-title">Dashboard</span>
      <div class="topbar-actions">
        <button class="topbar-action">
          <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
        </button>
        <button class="topbar-action">
          <svg viewBox="0 0 24 24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg>
        </button>
        <div class="topbar-avatar">K</div>
      </div>
    </header>

    <div class="app-body">

      <!-- Navigation Drawer -->
      <nav class="nav-drawer">
        <div class="nav-section">
          <div class="nav-item active">
            <svg class="nav-item-icon" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
            <span class="nav-item-text">Home</span>
          </div>
          <div class="nav-item">
            <svg class="nav-item-icon" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            <span class="nav-item-text">Reports</span>
            <span class="nav-badge">3</span>
          </div>
          <div class="nav-item">
            <svg class="nav-item-icon" viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
            <span class="nav-item-text">Users</span>
          </div>
          <div class="nav-item">
            <svg class="nav-item-icon" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
            <span class="nav-item-text">Tasks</span>
            <span class="nav-badge">7</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-subheader">Settings</div>
          <div class="nav-item">
            <svg class="nav-item-icon" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.07-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.74,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.07,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.47-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
            <span class="nav-item-text">General</span>
          </div>
          <div class="nav-item">
            <svg class="nav-item-icon" viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
            <span class="nav-item-text">Security</span>
          </div>
        </div>
      </nav>

      <!-- Main Content -->
      <main class="main-content">
        <div class="content-toolbar">
          <div class="breadcrumb">
            <span>App</span>
            <span class="breadcrumb-sep">›</span>
            <span>Dashboard</span>
          </div>
          <div class="toolbar-actions">
            <button class="tb-btn tb-btn--outline">Export</button>
            <button class="tb-btn tb-btn--filled">+ New</button>
          </div>
        </div>

        <div class="content-pad">

          <!-- Stats row -->
          <div class="card-grid">
            <div class="stat-card">
              <div class="stat-label">Total Users</div>
              <div class="stat-value">4,821</div>
              <div class="stat-sub">▲ 12% this month</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Revenue</div>
              <div class="stat-value">$28.4k</div>
              <div class="stat-sub">▲ 8.3% vs last month</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Open Tasks</div>
              <div class="stat-value">143</div>
              <div class="stat-sub">▼ 5 since yesterday</div>
            </div>
          </div>

          <!-- Recent activity -->
          <div class="content-card">
            <div class="content-card-header">
              <span class="content-card-title">Recent Activity</span>
            </div>
            <div class="list-row">
              <span class="list-row-dot dot-green"></span>
              <span class="list-row-text">User #4821 signed up via referral link</span>
              <span class="list-row-meta">2m ago</span>
            </div>
            <div class="list-row">
              <span class="list-row-dot dot-blue"></span>
              <span class="list-row-text">Report Q2 exported by Jordan Lee</span>
              <span class="list-row-meta">14m ago</span>
            </div>
            <div class="list-row">
              <span class="list-row-dot dot-orange"></span>
              <span class="list-row-text">Payment retry pending for order #7743</span>
              <span class="list-row-meta">1h ago</span>
            </div>
            <div class="list-row">
              <span class="list-row-dot dot-red"></span>
              <span class="list-row-text">Server CPU spike — auto-scaled resolved</span>
              <span class="list-row-meta">2h ago</span>
            </div>
            <div class="list-row">
              <span class="list-row-dot dot-green"></span>
              <span class="list-row-text">Deploy v2.4.1 completed successfully</span>
              <span class="list-row-meta">3h ago</span>
            </div>
          </div>

        </div><!-- /content-pad -->

        <!-- FAB -->
        <button class="fab">
          <svg viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
        </button>

      </main><!-- /main-content -->
    </div><!-- /app-body -->
  </div><!-- /app-shell -->
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

.md-14 {
  --primary: #1565c0;
  --primary-dark: #003c8f;
  --primary-light: #e3f2fd;
  --on-primary: #fff;
  --secondary: #00796b;
  --surface: #fffbfe;
  --surface-2: #f4f4f8;
  --on-surface: #1c1b1f;
  --outline: #79747e;
  --outline-variant: #dde1e7;
  --nav-width: 240px;
  --topbar-h: 56px;
  all: unset;
  display: block;
  font-family: 'Roboto', sans-serif;
  background: var(--surface-2);
  box-sizing: border-box;
  color: var(--on-surface);
}

.md-14 *,
.md-14 *::before,
.md-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
/* ── Hidden toggle for mobile drawer ── */

.md-14 .drawer-toggle {
  display: none;
}
/* ═══════════════════════════════════════
   APP SHELL
═══════════════════════════════════════ */

.md-14 .app-shell {
  display: flex;
  flex-direction: column;
  min-height: 480px;
  position: relative;
}
/* ── Top App Bar ── */

.md-14 .topbar {
  height: var(--topbar-h);
  background: var(--primary);
  color: var(--on-primary);
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 0 16px;
  position: sticky;
  top: 0;
  z-index: 10;
  box-shadow: 0 2px 6px rgba(0,0,0,.2);
}

.md-14 .topbar-menu-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 150ms;
}

.md-14 .topbar-menu-btn:hover {
  background: rgba(255,255,255,.12);
}

.md-14 .topbar-menu-btn svg {
  width: 20px;
  height: 20px;
  fill: currentColor;
}

.md-14 .topbar-title {
  font-size: 18px;
  font-weight: 500;
  flex: 1;
  letter-spacing: .2px;
}

.md-14 .topbar-actions {
  display: flex;
  gap: 4px;
}

.md-14 .topbar-action {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 150ms;
}

.md-14 .topbar-action:hover {
  background: rgba(255,255,255,.12);
}

.md-14 .topbar-action svg {
  width: 20px;
  height: 20px;
  fill: currentColor;
}

.md-14 .topbar-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--secondary);
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border: 2px solid rgba(255,255,255,.6);
}
/* ── Body: drawer + main ── */

.md-14 .app-body {
  display: flex;
  flex: 1;
  position: relative;
  min-height: 0;
}
/* ── Navigation Drawer ── */

.md-14 .nav-drawer {
  width: var(--nav-width);
  background: var(--surface);
  border-right: 1px solid var(--outline-variant);
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  transition: transform 300ms cubic-bezier(.4,0,.2,1), width 300ms;
}
/* ── Nav sections ── */

.md-14 .nav-section {
  padding: 8px 0;
}

.md-14 .nav-section + .nav-section {
  border-top: 1px solid var(--outline-variant);
}

.md-14 .nav-subheader {
  padding: 8px 28px 4px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--outline);
}

.md-14 .nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 12px;
  height: 48px;
  border-radius: 0 24px 24px 0;
  margin-right: 12px;
  cursor: pointer;
  transition: background 150ms;
  color: var(--on-surface);
  text-decoration: none;
  position: relative;
}

.md-14 .nav-item:hover {
  background: rgba(25,118,210,.06);
}

.md-14 .nav-item.active {
  background: var(--primary-light);
  color: var(--primary);
}

.md-14 .nav-item.active .nav-item-icon {
  fill: var(--primary);
}

.md-14 .nav-item.active .nav-item-text {
  font-weight: 700;
}

.md-14 .nav-item-icon {
  width: 20px;
  height: 20px;
  fill: var(--outline);
  flex-shrink: 0;
}

.md-14 .nav-item-text {
  font-size: 14px;
  font-weight: 500;
  flex: 1;
}

.md-14 .nav-badge {
  min-width: 20px;
  height: 18px;
  background: var(--primary);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 5px;
}
/* ── Main content area ── */

.md-14 .main-content {
  flex: 1;
  min-width: 0;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}
/* ── Toolbar strip (secondary) ── */

.md-14 .content-toolbar {
  background: var(--surface);
  border-bottom: 1px solid var(--outline-variant);
  padding: 0 16px;
  height: 44px;
  display: flex;
  align-items: center;
  gap: 16px;
  flex-shrink: 0;
}

.md-14 .breadcrumb {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: var(--outline);
}

.md-14 .breadcrumb-sep {
  font-size: 11px;
}

.md-14 .breadcrumb span:last-child {
  color: var(--on-surface);
  font-weight: 500;
}

.md-14 .toolbar-actions {
  margin-left: auto;
  display: flex;
  gap: 8px;
}

.md-14 .tb-btn {
  padding: 6px 14px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: background 150ms;
}

.md-14 .tb-btn--filled {
  background: var(--primary);
  color: #fff;
}

.md-14 .tb-btn--filled:hover {
  background: var(--primary-dark);
}

.md-14 .tb-btn--outline {
  background: transparent;
  color: var(--primary);
  border: 1px solid var(--primary);
}
/* ── Content padding ── */

.md-14 .content-pad {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
/* ── Card grid ── */

.md-14 .card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.md-14 .stat-card {
  background: var(--surface);
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 1px 3px rgba(0,0,0,.08);
}

.md-14 .stat-label {
  font-size: 11px;
  color: var(--outline);
  text-transform: uppercase;
  letter-spacing: .8px;
  font-weight: 500;
  margin-bottom: 6px;
}

.md-14 .stat-value {
  font-size: 22px;
  font-weight: 700;
  color: var(--on-surface);
}

.md-14 .stat-sub {
  font-size: 11px;
  color: var(--secondary);
  margin-top: 3px;
}
/* ── Content section card ── */

.md-14 .content-card {
  background: var(--surface);
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0,0,0,.08);
  overflow: hidden;
}

.md-14 .content-card-header {
  padding: 14px 16px;
  border-bottom: 1px solid var(--outline-variant);
  display: flex;
  align-items: center;
  gap: 8px;
}

.md-14 .content-card-title {
  font-size: 14px;
  font-weight: 600;
  flex: 1;
}

.md-14 .list-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--outline-variant);
  font-size: 13px;
  cursor: pointer;
  transition: background 120ms;
}

.md-14 .list-row:last-child {
  border-bottom: none;
}

.md-14 .list-row:hover {
  background: rgba(0,0,0,.03);
}

.md-14 .list-row-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.md-14 .dot-green {
  background: #43a047;
}

.md-14 .dot-orange {
  background: #f57c00;
}

.md-14 .dot-red {
  background: #e53935;
}

.md-14 .dot-blue {
  background: var(--primary);
}

.md-14 .list-row-text {
  flex: 1;
}

.md-14 .list-row-meta {
  font-size: 11px;
  color: var(--outline);
}
/* ── FAB ── */

.md-14 .fab {
  position: absolute;
  bottom: 20px;
  right: 20px;
  width: 52px;
  height: 52px;
  border-radius: 16px;
  background: var(--primary);
  color: #fff;
  border: none;
  font-size: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(21,101,192,.4);
  transition: box-shadow 150ms, transform 150ms;
  z-index: 5;
}

.md-14 .fab:hover {
  box-shadow: 0 6px 18px rgba(21,101,192,.5);
  transform: translateY(-1px);
}

.md-14 .fab svg {
  width: 22px;
  height: 22px;
  fill: currentColor;
}

@media (prefers-reduced-motion: reduce) {
  .md-14 .nav-drawer,
    .md-14 .topbar-menu-btn,
    .md-14 .topbar-action,
    .md-14 .nav-item,
    .md-14 .tb-btn,
    .md-14 .fab,
    .md-14 .list-row {
    transition: none !important;
  }
}
```
