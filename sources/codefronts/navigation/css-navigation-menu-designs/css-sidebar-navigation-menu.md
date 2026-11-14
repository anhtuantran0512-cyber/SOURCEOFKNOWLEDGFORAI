---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-sidebar-navigation-menu/"
title: "CSS Sidebar Navigation Menu"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A collapsible vertical sidebar navigation with nested sub-menus, icon support, and a mini-mode that collapses to icon-only width."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sidebar Navigation Menu
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-sidebar-navigation-menu/

A collapsible vertical sidebar navigation with nested sub-menus, icon support, and a mini-mode that collapses to icon-only width. The sidebar uses CSS Grid for layout and supports multiple levels of navigation hierarchy, ideal for admin dashboards and web apps.
## HTML
```html
<div class="nav-07">
  <input type="checkbox" id="nav-07-collapse">
  <aside class="nav-07__sidebar" role="navigation" aria-label="Sidebar">
    <div class="nav-07__sidebar-top">
      <div class="nav-07__brand">
        <div class="nav-07__brand-icon">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <span class="nav-07__brand-name">Quantum</span>
      </div>
      <label for="nav-07-collapse" class="nav-07__collapse-btn" aria-label="Collapse sidebar">
        <svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
      </label>
    </div>
    <nav class="nav-07__nav">
      <div class="nav-07__nav-label">Main</div>
      <ul>
        <li class="nav-07__active">
          <a href="#">
            <svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
            <span>Dashboard</span>
          </a>
        </li>
        <li>
          <a href="#">
            <svg viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            <span>Analytics</span>
            <span class="nav-07__badge">5</span>
          </a>
        </li>
        <li>
          <a href="#">
            <svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
            <span>Users</span>
          </a>
        </li>
        <li>
          <a href="#">
            <svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 01-8 0"/></svg>
            <span>Orders</span>
            <span class="nav-07__badge">12</span>
          </a>
        </li>
      </ul>
      <div class="nav-07__nav-label">System</div>
      <ul>
        <li>
          <a href="#">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93l-1.41 1.41M5.34 18.66l-1.41 1.41M20 12h2M2 12H0M19.07 19.07l-1.41-1.41M5.34 5.34L3.93 3.93M12 20v2M12 2v2"/></svg>
            <span>Settings</span>
          </a>
        </li>
        <li>
          <a href="#">
            <svg viewBox="0 0 24 24"><path d="M18 8h1a4 4 0 010 8h-1M2 8h16v9a4 4 0 01-4 4H6a4 4 0 01-4-4V8zM6 1v3M10 1v3M14 1v3"/></svg>
            <span>Integrations</span>
          </a>
        </li>
      </ul>
    </nav>
    <div class="nav-07__user">
      <div class="nav-07__avatar">JD</div>
      <div class="nav-07__user-info">
        <b>Jane Doe</b>
        <span>Admin</span>
      </div>
    </div>
  </aside>
  <main class="nav-07__main">
    <div class="nav-07__topbar">
      <h2>Dashboard Overview</h2>
      <div class="nav-07__topbar-right">
        <button class="nav-07__chip">This month</button>
        <button class="nav-07__chip">Export</button>
      </div>
    </div>
    <div class="nav-07__grid">
      <div class="nav-07__stat"><div class="nav-07__stat-label">Revenue</div><div class="nav-07__stat-val">$84.2k</div><div class="nav-07__stat-sub">↑ 12.4% vs last month</div></div>
      <div class="nav-07__stat"><div class="nav-07__stat-label">Users</div><div class="nav-07__stat-val">4,218</div><div class="nav-07__stat-sub">↑ 8.1% vs last month</div></div>
      <div class="nav-07__stat"><div class="nav-07__stat-label">Orders</div><div class="nav-07__stat-val">1,093</div><div class="nav-07__stat-sub">↑ 5.2% vs last month</div></div>
    </div>
    <div class="nav-07__table">
      <div class="nav-07__table-head"><span>Order</span><span>Amount</span><span>Date</span><span>Status</span></div>
      <div class="nav-07__table-row"><span>#1082 – Acme Corp</span><span>$2,400</span><span>Jun 11</span><span class="nav-07__dot nav-07__dot--green">Paid</span></div>
      <div class="nav-07__table-row"><span>#1081 – Globex Inc</span><span>$980</span><span>Jun 10</span><span class="nav-07__dot nav-07__dot--yellow">Pending</span></div>
      <div class="nav-07__table-row"><span>#1080 – Initech</span><span>$3,150</span><span>Jun 9</span><span class="nav-07__dot nav-07__dot--green">Paid</span></div>
      <div class="nav-07__table-row"><span>#1079 – Umbrella</span><span>$640</span><span>Jun 8</span><span class="nav-07__dot nav-07__dot--red">Failed</span></div>
    </div>
  </main>
</div>
```
## CSS
```css
.nav-07,
.nav-07 *,
.nav-07 *::before,
.nav-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-07 ::selection {
  background: #4f46e5;
  color: #fff;
}

#nav-07-collapse {
  display: none;
}

.nav-07 {
  --bg: #f5f5f4;
  --sidebar: #1e1e2e;
  --sidebar-hover: #2a2a3e;
  --surface: #ffffff;
  --border: #e7e5e4;
  --text: #1c1917;
  --muted: #78716c;
  --sidebar-text: rgba(255,255,255,.65);
  --sidebar-active: #fff;
  --accent: #818cf8;
  --accent-bg: rgba(129,140,248,.15);
  font-family: 'IBM Plex Sans',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
}
/* sidebar */

.nav-07__sidebar {
  width: 240px;
  min-height: 100vh;
  background: var(--sidebar);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  transition: width .28s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
}

#nav-07-collapse:checked ~ .nav-07__sidebar {
  width: 64px;
}

.nav-07__sidebar-top {
  padding: 20px 16px;
  border-bottom: 1px solid rgba(255,255,255,.06);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

.nav-07__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  overflow: hidden;
  white-space: nowrap;
}

.nav-07__brand-icon {
  width: 32px;
  height: 32px;
  flex-shrink: 0;
  border-radius: 8px;
  background: linear-gradient(135deg,var(--accent),#6366f1);
  display: grid;
  place-items: center;
}

.nav-07__brand-icon svg {
  width: 16px;
  height: 16px;
  fill: #fff;
}

.nav-07__brand-name {
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
  letter-spacing: -.02em;
  transition: opacity .2s,width .28s;
}

#nav-07-collapse:checked ~ .nav-07__sidebar .nav-07__brand-name {
  opacity: 0;
  width: 0;
}

.nav-07__collapse-btn {
  width: 28px;
  height: 28px;
  flex-shrink: 0;
  cursor: pointer;
  background: rgba(255,255,255,.06);
  border-radius: 6px;
  display: grid;
  place-items: center;
  transition: background .18s;
}

.nav-07__collapse-btn:hover {
  background: rgba(255,255,255,.1);
}

.nav-07__collapse-btn svg {
  width: 14px;
  height: 14px;
  stroke: #fff;
  fill: none;
  stroke-width: 2;
  transition: transform .28s;
}

#nav-07-collapse:checked ~ .nav-07__sidebar .nav-07__collapse-btn svg {
  transform: rotate(180deg);
}
/* nav sections */

.nav-07__nav {
  flex: 1;
  padding: 12px 8px;
  overflow-y: auto;
  overflow-x: hidden;
}

.nav-07__nav-label {
  font-size: .65rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(255,255,255,.25);
  padding: 4px 8px 6px;
  margin-top: 8px;
  white-space: nowrap;
  overflow: hidden;
  transition: opacity .2s;
}

#nav-07-collapse:checked ~ .nav-07__sidebar .nav-07__nav-label {
  opacity: 0;
}

.nav-07__nav ul {
  list-style: none;
}

.nav-07__nav li a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 8px;
  color: var(--sidebar-text);
  text-decoration: none;
  font-size: .875rem;
  font-weight: 500;
  border-radius: 8px;
  transition: background .18s,color .18s;
  white-space: nowrap;
  overflow: hidden;
}

.nav-07__nav li a:hover {
  background: var(--sidebar-hover);
  color: var(--sidebar-active);
}

.nav-07__nav li.nav-07__active a {
  background: var(--accent-bg);
  color: var(--accent);
}

.nav-07__nav li a svg {
  width: 18px;
  height: 18px;
  stroke: currentColor;
  fill: none;
  stroke-width: 1.75;
  flex-shrink: 0;
}

.nav-07__nav li a span {
  transition: opacity .2s,width .28s;
}

#nav-07-collapse:checked ~ .nav-07__sidebar .nav-07__nav li a span {
  opacity: 0;
  width: 0;
  overflow: hidden;
  display: inline-block;
}

.nav-07__badge {
  margin-left: auto;
  padding: 2px 7px;
  border-radius: 100px;
  font-size: .65rem;
  font-weight: 700;
  background: var(--accent);
  color: #fff;
  flex-shrink: 0;
  transition: opacity .2s;
}

#nav-07-collapse:checked ~ .nav-07__sidebar .nav-07__badge {
  opacity: 0;
}
/* user row */

.nav-07__user {
  padding: 12px 10px;
  border-top: 1px solid rgba(255,255,255,.06);
  display: flex;
  align-items: center;
  gap: 10px;
  overflow: hidden;
}

.nav-07__avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  flex-shrink: 0;
  background: linear-gradient(135deg,#818cf8,#6366f1);
  display: grid;
  place-items: center;
  font-size: .8rem;
  font-weight: 700;
  color: #fff;
}

.nav-07__user-info {
  overflow: hidden;
  white-space: nowrap;
  transition: opacity .2s;
}

.nav-07__user-info b {
  display: block;
  font-size: .8125rem;
  font-weight: 600;
  color: #fff;
}

.nav-07__user-info span {
  font-size: .7rem;
  color: rgba(255,255,255,.35);
}

#nav-07-collapse:checked ~ .nav-07__sidebar .nav-07__user-info {
  opacity: 0;
  width: 0;
}
/* main */

.nav-07__main {
  flex: 1;
  padding: 32px;
  overflow-y: auto;
}

.nav-07__topbar {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 24px;
  margin-bottom: 28px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-07__topbar h2 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
}

.nav-07__topbar-right {
  margin-left: auto;
  display: flex;
  gap: 10px;
}

.nav-07__chip {
  padding: 5px 12px;
  border-radius: 6px;
  font-size: .8rem;
  font-weight: 500;
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--muted);
  cursor: pointer;
  transition: background .18s;
}

.nav-07__chip:hover {
  background: var(--border);
}

.nav-07__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.nav-07__stat {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 22px;
}

.nav-07__stat-label {
  font-size: .75rem;
  color: var(--muted);
  font-weight: 500;
  margin-bottom: 8px;
  letter-spacing: .03em;
  text-transform: uppercase;
}

.nav-07__stat-val {
  font-size: 1.875rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.03em;
}

.nav-07__stat-sub {
  font-size: .75rem;
  color: #10b981;
  font-weight: 600;
  margin-top: 4px;
}

.nav-07__table {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}

.nav-07__table-head {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  padding: 12px 20px;
  border-bottom: 1px solid var(--border);
  font-size: .75rem;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: .04em;
  text-transform: uppercase;
}

.nav-07__table-row {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  padding: 14px 20px;
  border-bottom: 1px solid var(--border);
  font-size: .875rem;
  color: var(--text);
  transition: background .15s;
}

.nav-07__table-row:last-child {
  border-bottom: none;
}

.nav-07__table-row:hover {
  background: var(--bg);
}

.nav-07__dot {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.nav-07__dot::before {
  content: '';
  width: 7px;
  height: 7px;
  border-radius: 50%;
  display: inline-block;
}

.nav-07__dot--green::before {
  background: #10b981;
}

.nav-07__dot--yellow::before {
  background: #f59e0b;
}

.nav-07__dot--red::before {
  background: #ef4444;
}

@media (max-width: 768px) {
  .nav-07__sidebar {
    width: 64px;
  }

  .nav-07__brand-name,
    .nav-07__nav li a span,
    .nav-07__badge,
    .nav-07__user-info,
    .nav-07__nav-label {
    opacity: 0;
    width: 0;
    overflow: hidden;
  }

  .nav-07__main {
    padding: 16px;
  }

  .nav-07__grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-07__sidebar,
    .nav-07__brand-name,
    .nav-07__nav li a span,
    .nav-07__badge,
    .nav-07__user-info {
    transition: none;
  }
}
```
