---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/collapsible-sidebar-admin-shell/"
title: "Collapsible Sidebar Admin Shell"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The canonical SaaS shell: fixed top bar, a sidebar that folds from 236px (icon + label) to 68px (icon only, labels tooltip on hover), and a fluid main region…"
has_js: "true"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Collapsible Sidebar Admin Shell
Source: https://codefronts.com/layouts/css-dashboard-layouts/collapsible-sidebar-admin-shell/

The canonical SaaS shell: fixed top bar, a sidebar that folds from 236px (icon + label) to 68px (icon only, labels tooltip on hover), and a fluid main region that absorbs every pixel the sidebar gives up. Flexbox does the layout, a flex-basis transition does the fold, and 8 lines of JS exist for exactly one reason — a real <button aria-expanded> is the accessible way to build a disclosure control. Everything else is CSS.
## HTML
```html
<section class="cdl-02" aria-label="Collapsible sidebar admin shell demo">
  <div class="cdl-02__shell">
    <header class="cdl-02__bar">
      <button class="cdl-02__toggle" type="button" aria-expanded="true" aria-label="Collapse navigation">
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
      <strong class="cdl-02__brand"><span class="cdl-02__logo" aria-hidden="true"></span>Ledgerly</strong>
      <span class="cdl-02__search" role="search"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>Search…<kbd>⌘K</kbd></span>
      <span class="cdl-02__avatar" aria-hidden="true">JD</span>
    </header>
    <div class="cdl-02__body">
      <nav class="cdl-02__side" aria-label="Primary">
        <a href="#overview" class="cdl-02__on" data-label="Overview" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12 12 4l9 8"/><path d="M5 10v10h14V10"/></svg><span class="cdl-02__label">Overview</span></a>
        <a href="#orders" data-label="Orders"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16l-1.5 12h-13Z"/><path d="M8 7a4 4 0 0 1 8 0"/></svg><span class="cdl-02__label">Orders</span><b class="cdl-02__pill">12</b></a>
        <a href="#customers" data-label="Customers"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M17.5 13.6a6.5 6.5 0 0 1 4 6.4"/></svg><span class="cdl-02__label">Customers</span></a>
        <a href="#reports" data-label="Reports"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 20V10M12 20V4M19 20v-7"/></svg><span class="cdl-02__label">Reports</span></a>
        <a href="#billing" data-label="Billing"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/></svg><span class="cdl-02__label">Billing</span></a>
        <span class="cdl-02__gap" aria-hidden="true"></span>
        <a href="#settings" data-label="Settings"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/></svg><span class="cdl-02__label">Settings</span></a>
      </nav>
      <main class="cdl-02__main">
        <div class="cdl-02__head"><h2>Overview</h2><button class="cdl-02__cta" type="button">New order</button></div>
        <div class="cdl-02__cards">
          <article class="cdl-02__card"><h3>Revenue</h3><p>$128,430</p><small>▲ 8.2% vs last week</small></article>
          <article class="cdl-02__card"><h3>Orders</h3><p>1,203</p><small>▲ 3.1% vs last week</small></article>
          <article class="cdl-02__card"><h3>Refunds</h3><p>0.8%</p><small>▼ 0.2 pts vs last week</small></article>
        </div>
        <div class="cdl-02__panel"><h3>Sales this quarter</h3><div class="cdl-02__chart" aria-hidden="true"><i style="--h:35%"></i><i style="--h:52%"></i><i style="--h:44%"></i><i style="--h:61%"></i><i style="--h:57%"></i><i style="--h:73%"></i><i style="--h:66%"></i><i style="--h:84%"></i><i style="--h:92%"></i></div></div>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-02,
.cdl-02 *,
.cdl-02 *::before,
.cdl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-02 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --w-open: 236px;
  --w-rail: 68px;
  --bg: oklch(0.975 0.005 265);
  --panel: oklch(1 0 0);
  --edge: oklch(0.91 0.01 265);
  --ink: oklch(0.26 0.02 265);
  --mut: oklch(0.55 0.02 265);
  --acc: oklch(0.55 0.19 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cdl-02__shell {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid var(--edge);
  background: var(--bg);
  box-shadow: 0 24px 50px -30px oklch(0.4 0.05 265 / .35);
}

.cdl-02__bar {
  flex: none;
  display: flex;
  align-items: center;
  gap: 14px;
  height: 56px;
  padding: 0 16px;
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
}

.cdl-02__toggle {
  width: 40px;
  height: 40px;
  display: grid;
  place-items: center;
  border: none;
  border-radius: 10px;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
  transition: background .2s;
}

.cdl-02__toggle:hover {
  background: oklch(0.94 0.01 265);
}

.cdl-02__toggle:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cdl-02__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  letter-spacing: -.01em;
}

.cdl-02__logo {
  width: 20px;
  height: 20px;
  border-radius: 6px;
  background: conic-gradient(from 200deg,var(--acc),oklch(0.7 0.14 210));
}

.cdl-02__search {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  color: var(--mut);
  border: 1px solid var(--edge);
  border-radius: 999px;
  padding: 7px 8px 7px 12px;
  background: var(--bg);
}

.cdl-02__search kbd {
  font: 600 10px 'Segoe UI',system-ui,sans-serif;
  border: 1px solid var(--edge);
  border-radius: 5px;
  padding: 2px 6px;
  background: var(--panel);
  color: var(--mut);
}

.cdl-02__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 11px;
  font-weight: 700;
  color: oklch(1 0 0);
  background: linear-gradient(140deg,var(--acc),oklch(0.65 0.16 300));
}

.cdl-02__body {
  flex: 1;
  display: flex;
  min-height: 0;
}

.cdl-02__side {
  flex: 0 0 var(--w-open);
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px 10px;
  background: var(--panel);
  border-right: 1px solid var(--edge);
  overflow: hidden;
  transition: flex-basis .3s cubic-bezier(.2,.7,.2,1);
}

[data-collapsed] .cdl-02__side {
  flex-basis: var(--w-rail);
}

@container (max-width: 720px) {
  .cdl-02__side {
    flex-basis: var(--w-rail);
  }

  .cdl-02__label,
    .cdl-02__pill {
    opacity: 0;
    translate: -8px 0;
    pointer-events: none;
  }

  .cdl-02__search {
    display: none;
  }
}

.cdl-02__side a {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  height: 44px;
  padding: 0 13px;
  border-radius: 11px;
  text-decoration: none;
  color: var(--mut);
  font-size: 13.5px;
  font-weight: 600;
  white-space: nowrap;
  transition: background .2s,color .2s;
}

.cdl-02__side a svg {
  flex: none;
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cdl-02__side a:hover {
  background: oklch(0.955 0.008 265);
  color: var(--ink);
}

.cdl-02__side a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-02__side a.cdl-02__on {
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  color: var(--acc);
}

.cdl-02__label {
  transition: opacity .18s ease,translate .25s ease;
}

[data-collapsed] .cdl-02__label {
  opacity: 0;
  translate: -8px 0;
  pointer-events: none;
}

.cdl-02__pill {
  margin-left: auto;
  font-size: 10.5px;
  font-weight: 700;
  color: oklch(1 0 0);
  background: var(--acc);
  border-radius: 999px;
  padding: 2px 7px;
  transition: opacity .18s;
}

[data-collapsed] .cdl-02__pill {
  opacity: 0;
}

.cdl-02__gap {
  flex: 1;
}

[data-collapsed] .cdl-02__side a::after {
  content: attr(data-label);
  position: absolute;
  left: calc(100% + 10px);
  top: 50%;
  translate: 0 -50%;
  background: oklch(0.24 0.02 265);
  color: oklch(0.97 0 0);
  font-size: 12px;
  font-weight: 600;
  padding: 6px 11px;
  border-radius: 8px;
  white-space: nowrap;
  opacity: 0;
  scale: .92;
  pointer-events: none;
  transition: opacity .15s,scale .15s;
  z-index: 5;
}

[data-collapsed] .cdl-02__side a:hover::after,
[data-collapsed] .cdl-02__side a:focus-visible::after {
  opacity: 1;
  scale: 1;
}

.cdl-02__main {
  flex: 1 1 auto;
  min-width: 0;
  padding: 22px;
  overflow: auto;
  overscroll-behavior: contain;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.cdl-02__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cdl-02__head h2 {
  font-size: 19px;
  letter-spacing: -.01em;
}

.cdl-02__cta {
  border: none;
  border-radius: 10px;
  padding: 10px 16px;
  font: 600 13px 'Segoe UI',system-ui,sans-serif;
  color: oklch(1 0 0);
  background: var(--acc);
  cursor: pointer;
  transition: background .2s,translate .15s;
}

.cdl-02__cta:hover {
  background: color-mix(in oklch,var(--acc) 88%,black);
}

.cdl-02__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cdl-02__cta:active {
  translate: 0 1px;
}

.cdl-02__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
  gap: 14px;
}

.cdl-02__card {
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 14px;
  padding: 16px 18px;
}

.cdl-02__card h3 {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-02__card p {
  font-size: clamp(19px,2.2cqi + 12px,24px);
  font-weight: 700;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
  margin: 6px 0 2px;
}

.cdl-02__card small {
  font-size: 11.5px;
  color: oklch(0.55 0.14 155);
  font-weight: 600;
}

.cdl-02__panel {
  flex: 1;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 14px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-height: 170px;
}

.cdl-02__panel h3 {
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
}

.cdl-02__chart {
  flex: 1;
  display: flex;
  align-items: flex-end;
  gap: 10px;
}

.cdl-02__chart i {
  flex: 1;
  height: var(--h);
  border-radius: 6px 6px 0 0;
  background: linear-gradient(to top,color-mix(in oklch,var(--acc) 30%,transparent),var(--acc));
}

@media (prefers-reduced-motion: reduce) {
  .cdl-02 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.cdl-02__shell').forEach(function (shell) {
    if (shell.dataset.bound) return; shell.dataset.bound = '1';
    var btn = shell.querySelector('.cdl-02__toggle');
    btn.addEventListener('click', function () {
      var collapsed = shell.toggleAttribute('data-collapsed');
      btn.setAttribute('aria-expanded', String(!collapsed));
      btn.setAttribute('aria-label', collapsed ? 'Expand navigation' : 'Collapse navigation');
    });
  });
})();
```
