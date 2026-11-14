---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/modern-saas-dashboard-sidebar-menu-with-native-dark-mode-switch/"
title: "Modern SaaS Dashboard Sidebar Menu with Native Dark Mode Switch"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The 2027 SaaS shell in one file: a full dashboard sidebar — brand, nav, user badge — with a real light/dark theme switch that re-skins the ENTIRE app via a…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern SaaS Dashboard Sidebar Menu with Native Dark Mode Switch
Source: https://codefronts.com/layouts/css-sidebar-layouts/modern-saas-dashboard-sidebar-menu-with-native-dark-mode-switch/

The 2027 SaaS shell in one file: a full dashboard sidebar — brand, nav, user badge — with a real light/dark theme switch that re-skins the ENTIRE app via a single checkbox and the :has() relational selector. Every color on the page is a custom property, so the theme flip is one selector and zero JavaScript.
## HTML
```html
<section class="sbl-01">
  <aside class="sbl-01__sidebar">
    <div class="sbl-01__brand"><span class="sbl-01__logo" aria-hidden="true"></span>Nimbus</div>
    <nav class="sbl-01__nav" aria-label="Main">
      <a class="sbl-01__link" href="#" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg>Overview</a>
      <a class="sbl-01__link" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10m6 10V4m6 16v-7"/></svg>Analytics</a>
      <a class="sbl-01__link" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg>Customers</a>
      <a class="sbl-01__link" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>Billing</a>
      <a class="sbl-01__link" href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg>Settings</a>
    </nav>
    <label class="sbl-01__switch"><input type="checkbox"><span class="sbl-01__track" aria-hidden="true"><span class="sbl-01__thumb"></span></span>Light mode</label>
    <div class="sbl-01__user"><span class="sbl-01__avatar" aria-hidden="true">AK</span><span><strong>Ada Kim</strong><small>[email protected]</small></span></div>
  </aside>
  <main class="sbl-01__main">
    <h1>Good morning, Ada</h1>
    <div class="sbl-01__cards"><article class="sbl-01__card"><small>MRR</small><strong>$48,210</strong></article><article class="sbl-01__card"><small>Active users</small><strong>12,904</strong></article><article class="sbl-01__card"><small>Churn</small><strong>1.8%</strong></article></div>
  </main>
</section>
```
## CSS
```css
.sbl-01,
.sbl-01 *,
.sbl-01 *::before,
.sbl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-01 {
  --bg: oklch(0.14 0.015 265);
  --panel: oklch(0.17 0.018 265);
  --ink: oklch(0.93 0.005 265);
  --mut: oklch(0.65 0.01 265);
  --line: oklch(0.28 0.015 265);
  --accent: oklch(0.7 0.15 165);
  color-scheme: dark;
  display: grid;
  grid-template-columns: 250px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  transition: background-color .35s ease,color .35s ease;
}

.sbl-01:has(.sbl-01__switch input:checked) {
  --bg: oklch(0.97 0.004 100);
  --panel: oklch(1 0 0);
  --ink: oklch(0.25 0.02 265);
  --mut: oklch(0.52 0.015 265);
  --line: oklch(0.9 0.006 265);
  color-scheme: light;
}

.sbl-01__sidebar {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 20px 14px;
  background: var(--panel);
  border-right: 1px solid var(--line);
  transition: background-color .35s ease,border-color .35s ease;
}

.sbl-01__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 16px/1 system-ui,sans-serif;
  padding: 4px 10px 18px;
}

.sbl-01__logo {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  background: conic-gradient(from 210deg,var(--accent),oklch(0.6 0.18 220));
}

.sbl-01__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-01__link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-01__link svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-01__link:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-01__link[aria-current="page"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 16%,transparent);
  box-shadow: inset 2px 0 0 var(--accent);
}

.sbl-01__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-01__switch {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  font: 500 13px/1 system-ui,sans-serif;
  color: var(--mut);
  cursor: pointer;
  border-radius: 10px;
}

.sbl-01__switch:hover {
  color: var(--ink);
}

.sbl-01__switch input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.sbl-01__track {
  width: 36px;
  height: 20px;
  border-radius: 999px;
  background: var(--line);
  padding: 2px;
  transition: background-color .25s ease;
}

.sbl-01__thumb {
  display: block;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--ink);
  translate: 0 0;
  transition: translate .25s ease,background-color .25s ease;
}

.sbl-01__switch input:checked + .sbl-01__track {
  background: var(--accent);
}

.sbl-01__switch input:checked + .sbl-01__track .sbl-01__thumb {
  translate: 16px 0;
  background: #fff;
}

.sbl-01__switch:has(input:focus-visible) .sbl-01__track {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-01__user {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 10px;
  border-top: 1px solid var(--line);
  font: 500 13px/1.35 system-ui,sans-serif;
}

.sbl-01__user small {
  display: block;
  color: var(--mut);
  font-size: 11.5px;
}

.sbl-01__avatar {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font: 700 11px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(135deg,var(--accent),oklch(0.6 0.18 220));
}

.sbl-01__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-01__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 20px;
}

.sbl-01__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(150px,1fr));
  gap: 14px;
}

.sbl-01__card {
  display: grid;
  gap: 8px;
  padding: 18px;
  border-radius: 14px;
  background: var(--panel);
  border: 1px solid var(--line);
  transition: background-color .35s ease,border-color .35s ease;
}

.sbl-01__card small {
  font: 500 11px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .07em;
  color: var(--mut);
}

.sbl-01__card strong {
  font: 600 22px/1 system-ui,sans-serif;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-01,
    .sbl-01 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — body-wide theming via .sbl-01:has(input:checked) swapping one set of custom properties; every component reads the variables. */
```
