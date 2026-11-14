---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/sidebar-bottom-fixed-toggle/"
title: "Sidebar Bottom Fixed Toggle"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A collapsible vertical navigation bar with the theme switch anchored at the bottom — the sidebar collapses from 240px to 70px with labels fading out while…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sidebar Bottom Fixed Toggle
Source: https://codefronts.com/snippets/css-dark-mode-toggle/sidebar-bottom-fixed-toggle/

A collapsible vertical navigation bar with the theme switch anchored at the bottom — the sidebar collapses from 240px to 70px with labels fading out while the toggle remains reachable as an icon-only button.
## HTML
```html
<div class="dm-10" data-theme="light" id="dm-10-root">
  <aside class="dm-10__sidebar">
    <div class="dm-10__logo">
      <div class="dm-10__logo-icon">◈</div>
      <span class="dm-10__logo-name">Frontspace</span>
    </div>
    <nav class="dm-10__nav">
      <button class="dm-10__nav-item active"><span class="dm-10__nav-icon">◉</span><span class="dm-10__nav-label">Dashboard</span></button>
      <button class="dm-10__nav-item"><span class="dm-10__nav-icon">📈</span><span class="dm-10__nav-label">Analytics</span></button>
      <button class="dm-10__nav-item"><span class="dm-10__nav-icon">🗂️</span><span class="dm-10__nav-label">Projects</span></button>
      <button class="dm-10__nav-item"><span class="dm-10__nav-icon">👤</span><span class="dm-10__nav-label">Contacts</span></button>
      <button class="dm-10__nav-item"><span class="dm-10__nav-icon">📨</span><span class="dm-10__nav-label">Messages</span></button>
      <button class="dm-10__nav-item"><span class="dm-10__nav-icon">📁</span><span class="dm-10__nav-label">Files</span></button>
    </nav>
    <button class="dm-10__collapse-btn" id="dm-10-collapse">
      <span class="dm-10__collapse-icon">◀</span>
      <span class="dm-10__nav-label">Collapse</span>
    </button>
    <div class="dm-10__footer">
      <div class="dm-10__user">
        <div class="dm-10__avatar">JD</div>
        <div class="dm-10__user-info">
          <div class="dm-10__user-name">Jane Doe</div>
          <div class="dm-10__user-role">Product Designer</div>
        </div>
      </div>
      <button class="dm-10__theme-btn" id="dm-10-theme" aria-label="Toggle theme">
        <span class="dm-10__theme-btn-icon" id="dm-10-theme-icon">🌙</span>
        <div class="dm-10__theme-btn-track"><div class="dm-10__theme-btn-knob"></div></div>
        <span class="dm-10__theme-btn-label" id="dm-10-theme-label">Dark Mode</span>
      </button>
    </div>
  </aside>
  <main class="dm-10__main">
    <div class="dm-10__page-head">
      <h1 class="dm-10__page-title">Good morning, Jane ✦</h1>
      <span class="dm-10__page-badge" id="dm-10-theme-badge">Light Mode</span>
    </div>
    <div class="dm-10__cards">
      <div class="dm-10__card"><span class="dm-10__card-emoji">🚀</span><div class="dm-10__card-name">Launches</div><div class="dm-10__card-val">12</div></div>
      <div class="dm-10__card"><span class="dm-10__card-emoji">⭐</span><div class="dm-10__card-name">Reviews</div><div class="dm-10__card-val">4.9</div></div>
      <div class="dm-10__card"><span class="dm-10__card-emoji">💬</span><div class="dm-10__card-name">Messages</div><div class="dm-10__card-val">84</div></div>
      <div class="dm-10__card"><span class="dm-10__card-emoji">📦</span><div class="dm-10__card-name">Deliveries</div><div class="dm-10__card-val">37</div></div>
    </div>
    <div class="dm-10__feed">
      <div class="dm-10__feed-title">Recent Activity</div>
      <div class="dm-10__feed-item"><div class="dm-10__feed-dot"></div><div class="dm-10__feed-text"><strong>Alex Kim</strong> approved your design sprint</div><span class="dm-10__feed-time">2m ago</span></div>
      <div class="dm-10__feed-item"><div class="dm-10__feed-dot"></div><div class="dm-10__feed-text"><strong>Project Atlas</strong> moved to review stage</div><span class="dm-10__feed-time">18m ago</span></div>
      <div class="dm-10__feed-item"><div class="dm-10__feed-dot"></div><div class="dm-10__feed-text"><strong>Maria Santos</strong> left a comment on your file</div><span class="dm-10__feed-time">1h ago</span></div>
      <div class="dm-10__feed-item"><div class="dm-10__feed-dot"></div><div class="dm-10__feed-text">System deployed <strong>v2.4.1</strong> to production</div><span class="dm-10__feed-time">3h ago</span></div>
    </div>
  </main>
</div>
```
## CSS
```css
.dm-10,
.dm-10 *,
.dm-10 *::before,
.dm-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-10 ::selection {
  background: #f43f5e;
  color: #fff;
}

.dm-10[data-theme="light"] {
  --bg: #fff1f4;
  --sidebar: #ffffff;
  --surface: #ffffff;
  --surface2: #fff5f7;
  --border: #fecdd3;
  --text: #1f0a0d;
  --muted: #9f7880;
  --accent: #f43f5e;
  --accent2: #fb7185;
  --nav-active: rgba(244,63,94,0.1);
  --toggle-bg: #fecdd3;
  --shadow: 2px 0 24px rgba(244,63,94,0.08);
}

.dm-10[data-theme="dark"] {
  --bg: #0a0406;
  --sidebar: #150406;
  --surface: #160508;
  --surface2: #1e060a;
  --border: #3d0d14;
  --text: #ffe0e5;
  --muted: #7a3a42;
  --accent: #fb7185;
  --accent2: #fda4af;
  --nav-active: rgba(251,113,133,0.12);
  --toggle-bg: #2a080e;
  --shadow: 2px 0 24px rgba(244,63,94,0.2);
}

.dm-10 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  color: var(--text);
  transition: background 0.45s ease,color 0.45s ease;
}
/* ── Sidebar ── */

.dm-10__sidebar {
  width: var(--sw,240px);
  min-height: 100vh;
  background: var(--sidebar);
  border-right: 1px solid var(--border);
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
  transition: width 0.4s cubic-bezier(0.34,1.2,0.64,1), background 0.45s ease,border-color 0.45s ease,box-shadow 0.45s ease;
}

.dm-10.is-collapsed .dm-10__sidebar {
  width: 70px;
}
/* Logo area */

.dm-10__logo {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 22px 18px 16px;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
  overflow: hidden;
  transition: border-color 0.45s ease;
}

.dm-10__logo-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  box-shadow: 0 3px 10px rgba(244,63,94,0.3);
  transition: box-shadow 0.45s ease;
}

.dm-10__logo-name {
  font-size: 0.95rem;
  font-weight: 800;
  letter-spacing: -0.01em;
  white-space: nowrap;
  overflow: hidden;
  transition: opacity 0.3s ease,transform 0.3s ease,color 0.45s ease;
  color: var(--text);
}

.dm-10.is-collapsed .dm-10__logo-name {
  opacity: 0;
  transform: translateX(-10px);
}
/* Nav list */

.dm-10__nav {
  flex: 1;
  padding: 16px 10px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  overflow-y: auto;
  overflow-x: hidden;
}

.dm-10__nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 10px;
  border-radius: 12px;
  border: none;
  background: transparent;
  cursor: pointer;
  width: 100%;
  color: var(--muted);
  transition: background 0.2s ease,color 0.2s ease;
  overflow: hidden;
  white-space: nowrap;
  text-align: left;
}

.dm-10__nav-item:hover {
  background: var(--nav-active);
  color: var(--accent);
}

.dm-10__nav-item.active {
  background: var(--nav-active);
  color: var(--accent);
  font-weight: 700;
}

.dm-10__nav-icon {
  font-size: 18px;
  flex-shrink: 0;
  width: 22px;
  text-align: center;
}

.dm-10__nav-label {
  font-size: 0.82rem;
  font-weight: 600;
  transition: opacity 0.3s ease,transform 0.3s ease;
}

.dm-10.is-collapsed .dm-10__nav-label {
  opacity: 0;
  transform: translateX(-8px);
}
/* Collapse button */

.dm-10__collapse-btn {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 10px;
  border: none;
  background: transparent;
  cursor: pointer;
  color: var(--muted);
  width: 100%;
  border-top: 1px solid var(--border);
  transition: color 0.2s ease,border-color 0.45s ease;
  overflow: hidden;
  white-space: nowrap;
}

.dm-10__collapse-btn:hover {
  color: var(--accent);
}

.dm-10__collapse-icon {
  font-size: 18px;
  flex-shrink: 0;
  width: 22px;
  text-align: center;
  transition: transform 0.4s ease;
  display: inline-block;
}

.dm-10.is-collapsed .dm-10__collapse-icon {
  transform: rotate(180deg);
}
/* Bottom user + toggle section */

.dm-10__footer {
  padding: 12px 10px 16px;
  border-top: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex-shrink: 0;
  transition: border-color 0.45s ease;
  overflow: hidden;
}
/* User row */

.dm-10__user {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px;
  border-radius: 12px;
  overflow: hidden;
  white-space: nowrap;
}

.dm-10__avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 800;
  color: #fff;
  box-shadow: 0 2px 8px rgba(244,63,94,0.25);
}

.dm-10__user-info {
  overflow: hidden;
  transition: opacity 0.3s ease;
}

.dm-10.is-collapsed .dm-10__user-info {
  opacity: 0;
}

.dm-10__user-name {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text);
  transition: color 0.45s ease;
}

.dm-10__user-role {
  font-size: 0.65rem;
  color: var(--muted);
  transition: color 0.45s ease;
}
/* Theme toggle in footer */

.dm-10__theme-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: var(--toggle-bg);
  cursor: pointer;
  overflow: hidden;
  white-space: nowrap;
  transition: background 0.45s ease,border-color 0.45s ease;
  width: 100%;
}

.dm-10__theme-btn:hover {
  background: var(--nav-active);
}

.dm-10__theme-btn-icon {
  flex-shrink: 0;
  width: 22px;
  text-align: center;
  font-size: 16px;
  transition: transform 0.4s ease;
}

.dm-10[data-theme="dark"] .dm-10__theme-btn-icon {
  transform: rotate(20deg);
}

.dm-10__theme-btn-track {
  width: 32px;
  height: 18px;
  border-radius: 9px;
  background: var(--border);
  position: relative;
  flex-shrink: 0;
  transition: background 0.4s ease;
}

.dm-10[data-theme="dark"] .dm-10__theme-btn-track {
  background: linear-gradient(135deg,var(--accent),var(--accent2));
}

.dm-10__theme-btn-knob {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,0.15);
  transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
}

.dm-10[data-theme="dark"] .dm-10__theme-btn-knob {
  transform: translateX(14px);
}

.dm-10__theme-btn-label {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--accent);
  transition: opacity 0.3s ease,color 0.45s ease;
}

.dm-10.is-collapsed .dm-10__theme-btn-label,
.dm-10.is-collapsed .dm-10__theme-btn-track {
  opacity: 0;
}
/* ── Main content ── */

.dm-10__main {
  flex: 1;
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  overflow: hidden;
  min-width: 0;
}

.dm-10__page-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.dm-10__page-title {
  font-size: clamp(1.1rem,2.5vw,1.5rem);
  font-weight: 900;
  letter-spacing: -0.03em;
  color: var(--text);
  transition: color 0.45s ease;
}

.dm-10__page-badge {
  padding: 4px 12px;
  border-radius: 99px;
  background: var(--nav-active);
  border: 1px solid var(--border);
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--accent);
  white-space: nowrap;
  transition: background 0.45s ease,border-color 0.45s ease,color 0.45s ease;
}
/* Content cards */

.dm-10__cards {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(160px,1fr));
  gap: 14px;
}

.dm-10__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 20px 16px;
  transition: background 0.45s ease,border-color 0.45s ease,box-shadow 0.3s ease;
  cursor: default;
}

.dm-10__card:hover {
  box-shadow: 0 4px 16px rgba(244,63,94,0.1);
  border-color: var(--accent2);
}

.dm-10__card-emoji {
  font-size: 24px;
  margin-bottom: 10px;
  display: block;
}

.dm-10__card-name {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
  transition: color 0.45s ease;
}

.dm-10__card-val {
  font-size: 1.3rem;
  font-weight: 900;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
/* Activity feed */

.dm-10__feed {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 18px;
  flex: 1;
  transition: background 0.45s ease,border-color 0.45s ease;
}

.dm-10__feed-title {
  font-size: 0.78rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 12px;
  transition: color 0.45s ease;
}

.dm-10__feed-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
  transition: border-color 0.45s ease;
}

.dm-10__feed-item:last-child {
  border-bottom: none;
}

.dm-10__feed-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  flex-shrink: 0;
  margin-top: 5px;
}

.dm-10__feed-text {
  font-size: 0.78rem;
  color: var(--muted);
  line-height: 1.5;
  transition: color 0.45s ease;
}

.dm-10__feed-text strong {
  color: var(--text);
  font-weight: 700;
  transition: color 0.45s ease;
}

.dm-10__feed-time {
  font-size: 0.65rem;
  color: var(--muted);
  margin-left: auto;
  white-space: nowrap;
  transition: color 0.45s ease;
}

@media (prefers-reduced-motion: reduce) {
  .dm-10,
    .dm-10 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(()=>{
  const root=document.getElementById('dm-10-root');
  const themeBtn=document.getElementById('dm-10-theme');
  const themeIcon=document.getElementById('dm-10-theme-icon');
  const themeLabel=document.getElementById('dm-10-theme-label');
  const themeBadge=document.getElementById('dm-10-theme-badge');
  const collapseBtn=document.getElementById('dm-10-collapse');
  themeBtn.addEventListener('click',()=>{
    const isDark=root.getAttribute('data-theme')==='dark';
    root.setAttribute('data-theme',isDark?'light':'dark');
    themeIcon.textContent=isDark?'🌙':'☀️';
    themeLabel.textContent=isDark?'Dark Mode':'Light Mode';
    themeBadge.textContent=isDark?'Light Mode':'Dark Mode';
  });
  collapseBtn.addEventListener('click',()=>{
    root.classList.toggle('is-collapsed');
  });
})();
```
