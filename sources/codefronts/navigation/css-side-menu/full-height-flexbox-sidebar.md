---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/full-height-flexbox-sidebar/"
title: "Full-Height Flexbox Sidebar"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A sidebar that uses CSS Flexbox column direction to perfectly space a brand header, navigation links, an informational card, and a pinned user footer without…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Height Flexbox Sidebar
Source: https://codefronts.com/navigation/css-side-menu/full-height-flexbox-sidebar/

A sidebar that uses CSS Flexbox column direction to perfectly space a brand header, navigation links, an informational card, and a pinned user footer without absolute positioning.
## HTML
```html
<div class="sm-08">
  <nav class="sm-08__nav">
    <div class="sm-08__brand">
      <div class="sm-08__logo">A</div>
      <div class="sm-08__brand-name">Apex</div>
    </div>
    <div class="sm-08__links">
      <div class="sm-08__section-lbl">Workspace</div>
      <a class="sm-08__link sm-08__link--active" href="#"><span class="sm-08__link-icon">⬡</span> Dashboard</a>
      <a class="sm-08__link" href="#"><span class="sm-08__link-icon">◈</span> Projects</a>
      <a class="sm-08__link" href="#"><span class="sm-08__link-icon">▦</span> Tasks <span class="sm-08__badge">14</span></a>
      <a class="sm-08__link" href="#"><span class="sm-08__link-icon">◉</span> Inbox <span class="sm-08__badge">6</span></a>
      <div class="sm-08__section-lbl">Team</div>
      <a class="sm-08__link" href="#"><span class="sm-08__link-icon">◬</span> Members</a>
      <a class="sm-08__link" href="#"><span class="sm-08__link-icon">⬟</span> Roles</a>
    </div>
    <div class="sm-08__nav-card">
      <div class="sm-08__nav-card-title">Storage 68% full</div>
      <div class="sm-08__nav-card-sub">6.8 GB of 10 GB used. Upgrade for unlimited storage.</div>
    </div>
    <div class="sm-08__user">
      <div class="sm-08__user-avatar">TN</div>
      <div>
        <div class="sm-08__user-name">Tom N.</div>
        <div class="sm-08__user-plan">Pro Plan</div>
      </div>
      <div class="sm-08__logout">↗</div>
    </div>
  </nav>
  <div class="sm-08__main">
    <div class="sm-08__topbar">
      <div class="sm-08__page-title">Dashboard</div>
      <div class="sm-08__topbar-actions">
        <button class="sm-08__btn sm-08__btn--ghost">Export</button>
        <button class="sm-08__btn sm-08__btn--primary">+ New</button>
      </div>
    </div>
    <div class="sm-08__content">
      <p class="sm-08__desc">Sidebar uses <code>display:flex; flex-direction:column</code>. The links region has <code>flex:1</code> to grow and pin header/footer to top and bottom without <code>position:absolute</code>.</p>
      <div class="sm-08__grid">
        <div class="sm-08__card"><div class="sm-08__card-val">28</div><div class="sm-08__card-lbl">Active Projects</div></div>
        <div class="sm-08__card"><div class="sm-08__card-val">142</div><div class="sm-08__card-lbl">Open Tasks</div></div>
        <div class="sm-08__card"><div class="sm-08__card-val">7</div><div class="sm-08__card-lbl">Team Members</div></div>
        <div class="sm-08__card"><div class="sm-08__card-val">99%</div><div class="sm-08__card-lbl">SLA</div></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-08,
.sm-08 *,
.sm-08 *::before,
.sm-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-08 ::selection {
  background: #7c3aed;
  color: #fff;
}

.sm-08 {
  --bg: #fafaf9;
  --surface: #fff;
  --nav-bg: #1c1917;
  --accent: #7c3aed;
  --accent2: #a78bfa;
  --text: #fafaf9;
  --muted: #78716c;
  --text-dark: #1c1917;
  --border-nav: rgba(255,255,255,0.08);
  --border-main: #e7e5e4;
  --font: 'Outfit', system-ui, sans-serif;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text-dark);
  display: flex;
  min-height: 100vh;
  border-radius: 12px;
  overflow: hidden;
}
/* Sidebar nav using flexbox for perfect spacing */

.sm-08__nav {
  width: 240px;
  background: var(--nav-bg);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  padding: 0;
}
/* Top: brand */

.sm-08__brand {
  padding: 22px 18px;
  border-bottom: 1px solid var(--border-nav);
  display: flex;
  align-items: center;
  gap: 11px;
}

.sm-08__logo {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 16px;
  color: #fff;
}

.sm-08__brand-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
}
/* Middle: links — flex: 1 stretches this to fill available space */

.sm-08__links {
  flex: 1;
  padding: 14px 10px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sm-08__section-lbl {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #57534e;
  padding: 8px 10px 4px;
}

.sm-08__link {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 10px 12px;
  border-radius: 9px;
  color: #a8a29e;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
}

.sm-08__link:hover {
  color: var(--text);
  background: rgba(255,255,255,0.07);
}

.sm-08__link--active {
  color: var(--text);
  background: rgba(124,58,237,0.25);
}

.sm-08__link-icon {
  font-size: 15px;
}

.sm-08__badge {
  margin-left: auto;
  background: rgba(167,139,250,0.2);
  color: var(--accent2);
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
}
/* Spacer pushes bottom content down */

.sm-08__spacer {
  flex: 1;
}
/* Notification card in nav */

.sm-08__nav-card {
  margin: 0 10px 14px;
  padding: 14px;
  background: rgba(124,58,237,0.15);
  border: 1px solid rgba(124,58,237,0.25);
  border-radius: 10px;
}

.sm-08__nav-card-title {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.sm-08__nav-card-sub {
  font-size: 11px;
  color: #a8a29e;
  line-height: 1.5;
}
/* Bottom: user profile pinned to base */

.sm-08__user {
  padding: 16px 18px;
  border-top: 1px solid var(--border-nav);
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-08__user-avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f59e0b, #ef4444);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.sm-08__user-name {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}

.sm-08__user-plan {
  font-size: 10px;
  color: #a78bfa;
}

.sm-08__logout {
  margin-left: auto;
  width: 28px;
  height: 28px;
  background: rgba(255,255,255,0.07);
  border-radius: 7px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.sm-08__logout:hover {
  background: rgba(255,255,255,0.15);
}
/* Main */

.sm-08__main {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.sm-08__topbar {
  padding: 18px 22px;
  border-bottom: 1px solid var(--border-main);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sm-08__page-title {
  font-size: 18px;
  font-weight: 800;
}

.sm-08__topbar-actions {
  display: flex;
  gap: 8px;
}

.sm-08__btn {
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  font-family: var(--font);
}

.sm-08__btn--ghost {
  background: transparent;
  border: 1px solid var(--border-main);
  color: var(--text-dark);
}

.sm-08__btn--primary {
  background: var(--accent);
  border: none;
  color: #fff;
}

.sm-08__content {
  flex: 1;
  padding: 22px;
}

.sm-08__desc {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 20px;
}

.sm-08__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.sm-08__card {
  background: var(--surface);
  border: 1px solid var(--border-main);
  border-radius: 10px;
  padding: 16px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.sm-08__card-val {
  font-size: 24px;
  font-weight: 800;
  color: var(--accent);
}

.sm-08__card-lbl {
  font-size: 12px;
  color: var(--muted);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-08__link,
    .sm-08__logout {
    transition: none;
  }
}
```
