---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/css-frosted-glass-sidebar-navigation-menu/"
title: "CSS Frosted Glass Sidebar Navigation Menu"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "An admin dashboard with a frosted glass sidebar navigation on a colorful stage."
has_js: "false"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Frosted Glass Sidebar Navigation Menu
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/css-frosted-glass-sidebar-navigation-menu/

An admin dashboard with a frosted glass sidebar navigation on a colorful stage. Sidebar contains logo, 6 nav items with icons and badges, and a user profile card at the bottom. Main content area shows placeholder dashboard cards (revenue KPI, active users chart, recent activity list) so the frosted sidebar has real UI content to blur behind it. Zero JS — pure CSS Grid + backdrop-filter.
## HTML
```html
<div class="fg-04">
  <div class="fg-04__stage">

    <!-- Frosted glass sidebar -->
    <aside class="fg-04__sidebar" aria-label="Main navigation">
      <div class="fg-04__brand">
        <span class="fg-04__logo" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2l2.09 6.26L20 9.27l-4.55 4.44L16.54 20 12 16.77 7.46 20l1.09-6.29L4 9.27l5.91-1.01L12 2z"/>
          </svg>
        </span>
        <span>Aurora</span>
        <span class="fg-04__brand-badge">Pro</span>
      </div>

      <nav class="fg-04__nav" aria-label="Primary">
        <a href="#" class="fg-04__nav-item fg-04__nav-item--active">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/>
          </svg>
          Dashboard
        </a>
        <a href="#" class="fg-04__nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/>
          </svg>
          Projects
          <span class="fg-04__nav-badge">12</span>
        </a>
        <a href="#" class="fg-04__nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/>
            <circle cx="9" cy="7" r="4"/>
          </svg>
          Team
        </a>
        <a href="#" class="fg-04__nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>
          </svg>
          Analytics
          <span class="fg-04__nav-badge fg-04__nav-badge--dot"></span>
        </a>
        <a href="#" class="fg-04__nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
            <polyline points="22,6 12,13 2,6"/>
          </svg>
          Inbox
          <span class="fg-04__nav-badge">3</span>
        </a>
        <a href="#" class="fg-04__nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="12" cy="12" r="3"/>
            <path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 01-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/>
          </svg>
          Settings
        </a>
      </nav>

      <div class="fg-04__profile">
        <div class="fg-04__avatar" aria-hidden="true">MC</div>
        <div class="fg-04__profile-body">
          <span class="fg-04__profile-name">Maya Chen</span>
          <span class="fg-04__profile-role">Admin · Aurora</span>
        </div>
        <button type="button" class="fg-04__profile-btn" aria-label="Account menu">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <polyline points="6 9 12 15 18 9"/>
          </svg>
        </button>
      </div>
    </aside>

    <!-- Main content — real dashboard so the sidebar has UI to blur over -->
    <main class="fg-04__main">
      <header class="fg-04__main-head">
        <div>
          <h1>Dashboard</h1>
          <p>Welcome back, Maya. Here's what's happening today.</p>
        </div>
        <button type="button" class="fg-04__main-cta">New project +</button>
      </header>

      <div class="fg-04__cards">
        <article class="fg-04__card">
          <span class="fg-04__card-kicker">Monthly revenue</span>
          <span class="fg-04__card-metric">$847.2K</span>
          <span class="fg-04__card-delta fg-04__card-delta--up">▲ 12.4% vs last month</span>
          <div class="fg-04__spark">
            <i style="height:32%"></i><i style="height:48%"></i><i style="height:42%"></i><i style="height:58%"></i>
            <i style="height:52%"></i><i style="height:68%"></i><i style="height:76%"></i><i style="height:90%"></i>
          </div>
        </article>

        <article class="fg-04__card">
          <span class="fg-04__card-kicker">Active users</span>
          <span class="fg-04__card-metric">12,418</span>
          <span class="fg-04__card-delta fg-04__card-delta--up">▲ 8.1% this week</span>
          <div class="fg-04__spark">
            <i style="height:48%"></i><i style="height:52%"></i><i style="height:46%"></i><i style="height:62%"></i>
            <i style="height:58%"></i><i style="height:72%"></i><i style="height:68%"></i><i style="height:84%"></i>
          </div>
        </article>

        <article class="fg-04__card fg-04__card--wide">
          <span class="fg-04__card-kicker">Recent activity</span>
          <ul class="fg-04__activity">
            <li><b>Maya</b> shipped design review to production · <em>2m ago</em></li>
            <li><b>Liam</b> merged 3 pull requests · <em>18m ago</em></li>
            <li><b>Aria</b> commented on brand refresh · <em>1h ago</em></li>
            <li><b>Noah</b> deployed staging environment · <em>3h ago</em></li>
          </ul>
        </article>
      </div>
    </main>

  </div>
</div>
```
## CSS
```css
.fg-04,
.fg-04 *,
.fg-04 *::before,
.fg-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-04 ::selection {
  background: rgba(255,255,255,.28);
  color: #fff;
}

.fg-04 {
  --accent: #7c6cff;
  --paper: #0b0d15;
  --ink: #f1f5f9;
  --muted: #94a3b8;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,sans-serif;
  color: var(--ink);
  padding: 24px;
  display: flex;
}

.fg-04__stage {
  position: relative;
  flex: 1;
  border-radius: 20px;
  overflow: hidden;
  background: radial-gradient(circle at 20% 15%, rgba(124,108,255,0.36) 0%, transparent 42%), radial-gradient(circle at 85% 30%, rgba(236,72,153,0.28) 0%, transparent 40%), radial-gradient(circle at 70% 85%, rgba(34,211,238,0.22) 0%, transparent 45%), linear-gradient(135deg,#0b0d15 0%,#1a1d2d 100%);
  display: grid;
  grid-template-columns: 260px 1fr;
  min-height: calc(100vh - 48px);
}
/* Sidebar — the frosted glass panel */

.fg-04__sidebar {
  position: relative;
  padding: 22px 16px;
  background: rgba(255,255,255,0.10);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  backdrop-filter: blur(28px) saturate(180%);
  border-right: 1px solid rgba(255,255,255,0.14);
  display: flex;
  flex-direction: column;
  gap: 20px;
  color: #fff;
}

@supports not (backdrop-filter: blur(1px)) {
  .fg-04__sidebar {
    background: rgba(15,20,25,0.9);
  }
}

.fg-04__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0 6px;
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: -.01em;
}

.fg-04__logo {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: rgba(255,255,255,0.16);
  border: 1px solid rgba(255,255,255,0.24);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.fg-04__brand > span:nth-child(2) {
  flex: 1;
  min-width: 0;
}

.fg-04__brand-badge {
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .1em;
  padding: 3px 7px;
  border-radius: 5px;
  background: var(--accent);
  color: #fff;
  text-transform: uppercase;
}

.fg-04__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
  flex: 1;
}

.fg-04__nav-item {
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 10px;
  border-radius: 8px;
  color: rgba(255,255,255,0.78);
  text-decoration: none;
  font-size: .88rem;
  font-weight: 500;
  transition: background .2s,color .2s;
}

.fg-04__nav-item:hover {
  background: rgba(255,255,255,0.08);
  color: #fff;
}

.fg-04__nav-item--active {
  background: rgba(255,255,255,0.14);
  color: #fff;
  font-weight: 600;
}

.fg-04__nav-item--active::before {
  content: "";
  position: absolute;
  left: -16px;
  top: 14%;
  bottom: 14%;
  width: 3px;
  background: var(--accent);
  border-radius: 0 3px 3px 0;
}

.fg-04__nav-item svg {
  flex-shrink: 0;
  opacity: .85;
}

.fg-04__nav-item > span:not(.fg-04__nav-badge) {
  flex: 1;
  min-width: 0;
}

.fg-04__nav-badge {
  margin-left: auto;
  font-size: .66rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 999px;
  background: rgba(124,108,255,0.28);
  color: #c4b5fd;
}

.fg-04__nav-badge--dot {
  padding: 0;
  width: 7px;
  height: 7px;
  background: #ef4444;
}
/* User profile card */

.fg-04__profile {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-radius: 10px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
}

.fg-04__avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg,#f9c1cf,#d97a99);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .78rem;
  font-weight: 800;
  color: #fff;
  flex-shrink: 0;
}

.fg-04__profile-body {
  display: flex;
  flex-direction: column;
  gap: 1px;
  flex: 1;
  min-width: 0;
}

.fg-04__profile-name {
  font-size: .86rem;
  font-weight: 700;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fg-04__profile-role {
  font-size: .7rem;
  color: rgba(255,255,255,0.65);
  font-weight: 500;
}

.fg-04__profile-btn {
  background: transparent;
  border: 0;
  color: rgba(255,255,255,0.65);
  cursor: pointer;
  padding: 4px;
  border-radius: 5px;
}

.fg-04__profile-btn:hover {
  color: #fff;
  background: rgba(255,255,255,0.10);
}
/* Main content */

.fg-04__main {
  padding: clamp(22px,3vw,36px);
  display: flex;
  flex-direction: column;
  gap: 22px;
  min-width: 0;
}

.fg-04__main-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.fg-04__main-head h1 {
  font-size: clamp(1.4rem,2.4vw,1.75rem);
  font-weight: 800;
  letter-spacing: -.02em;
}

.fg-04__main-head p {
  font-size: .9rem;
  color: var(--muted);
  margin-top: 4px;
}

.fg-04__main-cta {
  padding: 9px 16px;
  background: var(--accent);
  color: #fff;
  border: 0;
  border-radius: 9px;
  font-family: inherit;
  font-size: .88rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .2s,transform .1s;
}

.fg-04__main-cta:hover {
  background: #6d5cf0;
  transform: translateY(-1px);
}

.fg-04__cards {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 14px;
}

.fg-04__card {
  padding: 20px;
  border-radius: 14px;
  background: rgba(15,20,30,0.75);
  border: 1px solid rgba(255,255,255,0.08);
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.fg-04__card--wide {
  grid-column: 1 / -1;
}

.fg-04__card-kicker {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.fg-04__card-metric {
  font-size: 1.75rem;
  font-weight: 900;
  letter-spacing: -.02em;
  font-feature-settings: "tnum";
}

.fg-04__card-delta {
  font-size: .8rem;
  font-weight: 700;
}

.fg-04__card-delta--up {
  color: #10b981;
}

.fg-04__spark {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 38px;
  margin-top: 12px;
}

.fg-04__spark i {
  flex: 1;
  background: linear-gradient(180deg,var(--accent),transparent 130%);
  border-radius: 2px 2px 0 0;
  min-height: 6px;
}

.fg-04__activity {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 10px;
}

.fg-04__activity li {
  font-size: .84rem;
  color: rgba(255,255,255,0.78);
  padding: 6px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.fg-04__activity li:last-child {
  border-bottom: 0;
}

.fg-04__activity b {
  color: #fff;
  font-weight: 700;
}

.fg-04__activity em {
  color: var(--muted);
  font-style: normal;
  font-size: .76rem;
  margin-left: 4px;
}

@media (max-width: 900px) {
  .fg-04__stage {
    grid-template-columns: 1fr;
  }

  .fg-04__sidebar {
    display: none;
  }

  .fg-04__cards {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-04__nav-item,
    .fg-04__main-cta,
    .fg-04__profile-btn {
    transition: none;
  }
}
```
