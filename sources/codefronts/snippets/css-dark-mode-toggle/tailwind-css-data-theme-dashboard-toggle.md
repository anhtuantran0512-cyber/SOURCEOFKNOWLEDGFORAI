---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/tailwind-css-data-theme-dashboard-toggle/"
title: "Tailwind CSS data-theme Dashboard Toggle"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A full SaaS admin dashboard — sidebar, KPI cards, bar chart — where toggling sets data-theme=dark on the root element, flipping every component via…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS data-theme Dashboard Toggle
Source: https://codefronts.com/snippets/css-dark-mode-toggle/tailwind-css-data-theme-dashboard-toggle/

A full SaaS admin dashboard — sidebar, KPI cards, bar chart — where toggling sets data-theme=dark on the root element, flipping every component via attribute-scoped CSS custom properties.
## HTML
```html
<div class="dm-06" data-theme="light" id="dm-06-root">
  <aside class="dm-06__sidebar">
    <div class="dm-06__logo">
      <div class="dm-06__logo-mark">◈</div>
      <span class="dm-06__logo-name">Dashboard</span>
    </div>
    <button class="dm-06__nav-item active"><span class="dm-06__nav-icon">◉</span><span>Overview</span></button>
    <button class="dm-06__nav-item"><span class="dm-06__nav-icon">📊</span><span>Analytics</span></button>
    <button class="dm-06__nav-item"><span class="dm-06__nav-icon">👥</span><span>Users</span></button>
    <button class="dm-06__nav-item"><span class="dm-06__nav-icon">💳</span><span>Billing</span></button>
    <div class="dm-06__nav-divider"></div>
    <button class="dm-06__nav-item"><span class="dm-06__nav-icon">⚙️</span><span>Settings</span></button>
    <div class="dm-06__sidebar-footer">
      <button class="dm-06__theme-toggle" id="dm-06-btn" aria-label="Toggle theme">
        <div class="dm-06__toggle-pill"><div class="dm-06__toggle-knob"></div></div>
        <span class="dm-06__toggle-text" id="dm-06-label">Dark Mode</span>
      </button>
    </div>
  </aside>
  <main class="dm-06__main">
    <div class="dm-06__topbar">
      <h1 class="dm-06__page-title">Overview</h1>
      <div class="dm-06__user">
        <div class="dm-06__avatar">JD</div>
      </div>
    </div>
    <div class="dm-06__kpi-row">
      <div class="dm-06__kpi">
        <div class="dm-06__kpi-label">Revenue</div>
        <div class="dm-06__kpi-value">$84k</div>
        <div class="dm-06__kpi-delta up">↑ 12.4%</div>
      </div>
      <div class="dm-06__kpi">
        <div class="dm-06__kpi-label">Users</div>
        <div class="dm-06__kpi-value">12.3k</div>
        <div class="dm-06__kpi-delta up">↑ 8.1%</div>
      </div>
      <div class="dm-06__kpi">
        <div class="dm-06__kpi-label">Churn</div>
        <div class="dm-06__kpi-value">2.1%</div>
        <div class="dm-06__kpi-delta dn">↑ 0.3%</div>
      </div>
      <div class="dm-06__kpi">
        <div class="dm-06__kpi-label">NPS</div>
        <div class="dm-06__kpi-value">74</div>
        <div class="dm-06__kpi-delta up">↑ 6 pts</div>
      </div>
    </div>
    <div class="dm-06__chart-card">
      <div class="dm-06__chart-head">
        <div>
          <div class="dm-06__chart-title">Monthly Revenue</div>
          <div class="dm-06__chart-sub">Last 8 months</div>
        </div>
      </div>
      <div class="dm-06__bars" id="dm-06-bars">
        <!-- bars injected by JS -->
      </div>
    </div>
  </main>
</div>
```
## CSS
```css
.dm-06,
.dm-06 *,
.dm-06 *::before,
.dm-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-06 ::selection {
  background: #8b5cf6;
  color: #fff;
}
/* ── Data-theme attribute drives all tokens ── */

.dm-06[data-theme="light"] {
  --bg: #f5f3ff;
  --sidebar: #fff;
  --surface: #ffffff;
  --surface2: #faf9ff;
  --border: #ede9fe;
  --text: #1e1b4b;
  --muted: #7c7aa8;
  --accent: #7c3aed;
  --accent2: #c026d3;
  --positive: #059669;
  --warn: #d97706;
  --tag-bg: rgba(124,58,237,0.1);
  --bar1: linear-gradient(to top,#7c3aed,#a855f7);
  --bar2: linear-gradient(to top,#c026d3,#e879f9);
  --bar3: linear-gradient(to top,#059669,#34d399);
  --bar4: linear-gradient(to top,#d97706,#fbbf24);
  --card-shadow: 0 2px 12px rgba(124,58,237,0.08),0 1px 3px rgba(0,0,0,0.05);
  --sidebar-shadow: 2px 0 20px rgba(0,0,0,0.05);
}

.dm-06[data-theme="dark"] {
  --bg: #06030f;
  --sidebar: #0d0920;
  --surface: #100d22;
  --surface2: #160f2e;
  --border: #1e1640;
  --text: #e8e3ff;
  --muted: #5e5a82;
  --accent: #a78bfa;
  --accent2: #e879f9;
  --positive: #34d399;
  --warn: #fbbf24;
  --tag-bg: rgba(167,139,250,0.15);
  --bar1: linear-gradient(to top,#7c3aed,#a78bfa);
  --bar2: linear-gradient(to top,#9333ea,#e879f9);
  --bar3: linear-gradient(to top,#059669,#6ee7b7);
  --bar4: linear-gradient(to top,#b45309,#fbbf24);
  --card-shadow: 0 2px 20px rgba(167,139,250,0.1),0 1px 3px rgba(0,0,0,0.4);
  --sidebar-shadow: 2px 0 20px rgba(0,0,0,0.4);
}

.dm-06 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  color: var(--text);
  transition: background 0.4s ease,color 0.4s ease;
}
/* Sidebar */

.dm-06__sidebar {
  width: 220px;
  min-height: 100vh;
  background: var(--sidebar);
  border-right: 1px solid var(--border);
  box-shadow: var(--sidebar-shadow);
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  gap: 8px;
  flex-shrink: 0;
  transition: background 0.4s ease,border-color 0.4s ease;
}

.dm-06__logo {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px 20px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 8px;
  transition: border-color 0.4s ease;
}

.dm-06__logo-mark {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: #fff;
  font-weight: 800;
}

.dm-06__logo-name {
  font-size: 0.88rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -0.01em;
  transition: color 0.4s ease;
}

.dm-06__nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 10px;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: background 0.2s ease,color 0.2s ease;
  border: none;
  background: transparent;
  text-align: left;
  width: 100%;
}

.dm-06__nav-item:hover,
.dm-06__nav-item.active {
  background: var(--tag-bg);
  color: var(--accent);
}

.dm-06__nav-item.active {
  font-weight: 700;
}

.dm-06__nav-icon {
  font-size: 16px;
  width: 20px;
  text-align: center;
}

.dm-06__nav-divider {
  height: 1px;
  background: var(--border);
  margin: 8px 0;
  transition: background 0.4s ease;
}
/* Bottom toggle area */

.dm-06__sidebar-footer {
  margin-top: auto;
  border-top: 1px solid var(--border);
  padding-top: 16px;
  transition: border-color 0.4s ease;
}

.dm-06__theme-toggle {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 10px;
  background: var(--tag-bg);
  border: 1px solid var(--border);
  cursor: pointer;
  transition: background 0.3s ease,border-color 0.3s ease;
  width: 100%;
}

.dm-06__theme-toggle:hover {
  background: var(--surface2);
}

.dm-06__toggle-pill {
  width: 36px;
  height: 20px;
  border-radius: 10px;
  background: var(--border);
  position: relative;
  transition: background 0.4s ease;
  flex-shrink: 0;
}

.dm-06[data-theme="dark"] .dm-06__toggle-pill {
  background: linear-gradient(135deg,var(--accent),var(--accent2));
}

.dm-06__toggle-knob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,0.2);
  transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
}

.dm-06[data-theme="dark"] .dm-06__toggle-knob {
  transform: translateX(16px);
}

.dm-06__toggle-text {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--accent);
  flex: 1;
  transition: color 0.4s ease;
}
/* Main content */

.dm-06__main {
  flex: 1;
  padding: 28px;
  overflow: hidden;
}

.dm-06__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.dm-06__page-title {
  font-size: 1.3rem;
  font-weight: 900;
  letter-spacing: -0.03em;
  color: var(--text);
  transition: color 0.4s ease;
}

.dm-06__user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.dm-06__avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 800;
  color: #fff;
  box-shadow: 0 2px 8px var(--tag-bg);
}
/* KPI Cards */

.dm-06__kpi-row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(140px,1fr));
  gap: 14px;
  margin-bottom: 20px;
}

.dm-06__kpi {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 18px 16px;
  box-shadow: var(--card-shadow);
  transition: background 0.4s ease,border-color 0.4s ease,box-shadow 0.4s ease;
}

.dm-06__kpi-label {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
  transition: color 0.4s ease;
}

.dm-06__kpi-value {
  font-size: 1.6rem;
  font-weight: 900;
  letter-spacing: -0.04em;
  color: var(--text);
  transition: color 0.4s ease;
}

.dm-06__kpi-delta {
  font-size: 0.7rem;
  font-weight: 700;
  margin-top: 3px;
}

.dm-06__kpi-delta.up {
  color: var(--positive);
}

.dm-06__kpi-delta.dn {
  color: var(--warn);
}
/* Chart area */

.dm-06__chart-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 20px;
  box-shadow: var(--card-shadow);
  transition: background 0.4s ease,border-color 0.4s ease;
}

.dm-06__chart-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}

.dm-06__chart-title {
  font-size: 0.88rem;
  font-weight: 800;
  color: var(--text);
  transition: color 0.4s ease;
}

.dm-06__chart-sub {
  font-size: 0.7rem;
  color: var(--muted);
  transition: color 0.4s ease;
}

.dm-06__bars {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  height: 120px;
  padding-bottom: 4px;
}

.dm-06__bar-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.dm-06__bar {
  width: 100%;
  border-radius: 6px 6px 0 0;
  transition: height 0.6s cubic-bezier(0.34,1.2,0.64,1),background 0.4s ease;
  min-height: 8px;
}

.dm-06__bar:nth-child(1) {
  background: var(--bar1);
}

.dm-06__bar:nth-child(1) ~ .dm-06__bar {
  background: var(--bar2);
}

.dm-06__bar-lbl {
  font-size: 0.62rem;
  color: var(--muted);
  font-weight: 600;
  transition: color 0.4s ease;
}

@media (max-width: 500px) {
  .dm-06__sidebar {
    width: 60px;
  }

  .dm-06__logo-name,
    .dm-06__nav-item span:not(.dm-06__nav-icon),
    .dm-06__toggle-text {
    display: none;
  }

  .dm-06__logo {
    justify-content: center;
  }

  .dm-06__nav-item {
    justify-content: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .dm-06,
    .dm-06 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(()=>{
  const root=document.getElementById('dm-06-root');
  const btn=document.getElementById('dm-06-btn');
  const label=document.getElementById('dm-06-label');
  const barsEl=document.getElementById('dm-06-bars');
  const data=[45,62,38,75,58,82,70,91];
  const months=['May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const grads=['var(--bar1)','var(--bar2)','var(--bar3)','var(--bar4)'];
  const max=Math.max(...data);
  data.forEach((v,i)=>{
    const col=document.createElement('div');
    col.className='dm-06__bar-col';
    const bar=document.createElement('div');
    bar.className='dm-06__bar';
    bar.style.height=Math.round((v/max)*110)+'px';
    bar.style.background=grads[i%4];
    const lbl=document.createElement('div');
    lbl.className='dm-06__bar-lbl';
    lbl.textContent=months[i];
    col.append(bar,lbl);
    barsEl.append(col);
  });
  btn.addEventListener('click',()=>{
    const isDark=root.getAttribute('data-theme')==='dark';
    root.setAttribute('data-theme',isDark?'light':'dark');
    label.textContent=isDark?'Dark Mode':'Light Mode';
  });
})();
```
