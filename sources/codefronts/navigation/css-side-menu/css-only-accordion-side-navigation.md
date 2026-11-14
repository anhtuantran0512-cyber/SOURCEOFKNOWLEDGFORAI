---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/css-only-accordion-side-navigation/"
title: "CSS-Only Accordion Side Navigation"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A documentation-style sidebar where multiple independent accordion sections can be expanded or collapsed simultaneously using hidden checkboxes and…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS-Only Accordion Side Navigation
Source: https://codefronts.com/navigation/css-side-menu/css-only-accordion-side-navigation/

A documentation-style sidebar where multiple independent accordion sections can be expanded or collapsed simultaneously using hidden checkboxes and max-height transitions.
## HTML
```html
<div class="sm-16">
  <nav class="sm-16__nav">
    <div class="sm-16__brand">
      <div class="sm-16__logo">D</div>
      <div>
        <span class="sm-16__brand-name">DocBase</span>
        <span class="sm-16__brand-version">v3.2</span>
      </div>
    </div>
    <div class="sm-16__search">
      <input type="text" class="sm-16__search-input" placeholder="Search docs…">
    </div>
    <a class="sm-16__flat" href="#"><span class="sm-16__flat-icon">⬡</span> Overview</a>
    <!-- Accordion 1 -->
    <div class="sm-16__section">
      <input type="checkbox" class="sm-16__acc-toggle" id="sm-16-a1" checked>
      <label class="sm-16__section-header" for="sm-16-a1">
        <span><span class="sm-16__section-header-icon">◈</span> Getting Started</span>
        <span class="sm-16__chevron">›</span>
      </label>
      <div class="sm-16__items">
        <a class="sm-16__item sm-16__item--active" href="#">Installation</a>
        <a class="sm-16__item" href="#">Configuration</a>
        <a class="sm-16__item" href="#">Quick Start</a>
        <a class="sm-16__item" href="#">Examples</a>
      </div>
    </div>
    <!-- Accordion 2 -->
    <div class="sm-16__section">
      <input type="checkbox" class="sm-16__acc-toggle" id="sm-16-a2">
      <label class="sm-16__section-header" for="sm-16-a2">
        <span><span class="sm-16__section-header-icon">▦</span> Core Concepts</span>
        <span class="sm-16__chevron">›</span>
      </label>
      <div class="sm-16__items">
        <a class="sm-16__item" href="#">Architecture</a>
        <a class="sm-16__item" href="#">Data Flow</a>
        <a class="sm-16__item" href="#">State Management</a>
        <a class="sm-16__item" href="#">Routing</a>
      </div>
    </div>
    <!-- Accordion 3 -->
    <div class="sm-16__section">
      <input type="checkbox" class="sm-16__acc-toggle" id="sm-16-a3">
      <label class="sm-16__section-header" for="sm-16-a3">
        <span><span class="sm-16__section-header-icon">◉</span> API Reference</span>
        <span class="sm-16__chevron">›</span>
      </label>
      <div class="sm-16__items">
        <a class="sm-16__item" href="#">Endpoints <span class="sm-16__item-badge">48</span></a>
        <a class="sm-16__item" href="#">Authentication</a>
        <a class="sm-16__item" href="#">Webhooks</a>
        <a class="sm-16__item" href="#">Rate Limits</a>
      </div>
    </div>
    <!-- Accordion 4 -->
    <div class="sm-16__section">
      <input type="checkbox" class="sm-16__acc-toggle" id="sm-16-a4">
      <label class="sm-16__section-header" for="sm-16-a4">
        <span><span class="sm-16__section-header-icon">◬</span> Guides</span>
        <span class="sm-16__chevron">›</span>
      </label>
      <div class="sm-16__items">
        <a class="sm-16__item" href="#">Deployment</a>
        <a class="sm-16__item" href="#">Performance</a>
        <a class="sm-16__item" href="#">Security</a>
      </div>
    </div>
    <a class="sm-16__flat" href="#"><span class="sm-16__flat-icon">⬙</span> Changelog</a>
  </nav>
  <div class="sm-16__main">
    <div class="sm-16__heading">Documentation</div>
    <div class="sm-16__sub">CSS-only accordion sidebar: each section uses a hidden <code>checkbox</code> and <code>max-height</code> transition. Clicking a header expands/collapses its items independently.</div>
    <div class="sm-16__docs">
      <div class="sm-16__doc-card">
        <div class="sm-16__doc-icon">📦</div>
        <div>
          <div class="sm-16__doc-title">Installation Guide</div>
          <div class="sm-16__doc-sub">Set up your environment in under 5 minutes</div>
        </div>
      </div>
      <div class="sm-16__doc-card">
        <div class="sm-16__doc-icon">⚙️</div>
        <div>
          <div class="sm-16__doc-title">Configuration Reference</div>
          <div class="sm-16__doc-sub">All available options with examples</div>
        </div>
      </div>
      <div class="sm-16__doc-card">
        <div class="sm-16__doc-icon">🚀</div>
        <div>
          <div class="sm-16__doc-title">Quick Start Tutorial</div>
          <div class="sm-16__doc-sub">Build your first integration in 10 steps</div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-16,
.sm-16 *,
.sm-16 *::before,
.sm-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-16 ::selection {
  background: #2563eb;
  color: #fff;
}

.sm-16 {
  --bg: #f0f4ff;
  --surface: #fff;
  --nav-bg: #fff;
  --accent: #2563eb;
  --accent2: #60a5fa;
  --text: #0f172a;
  --muted: #94a3b8;
  --muted2: #64748b;
  --border: #e2e8f0;
  --border-active: rgba(37,99,235,0.15);
  --font: 'Plus Jakarta Sans', system-ui, sans-serif;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  border-radius: 12px;
  overflow: hidden;
}
/* Accordion hidden radio/checkboxes */

.sm-16__acc-toggle {
  display: none;
}
/* Sidebar */

.sm-16__nav {
  width: 240px;
  background: var(--nav-bg);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  overflow-y: auto;
}

.sm-16__nav::-webkit-scrollbar {
  width: 3px;
}

.sm-16__nav::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

.sm-16__brand {
  padding: 18px 16px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

.sm-16__logo {
  width: 32px;
  height: 32px;
  background: var(--accent);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  color: #fff;
  font-size: 14px;
}

.sm-16__brand-name {
  font-size: 14px;
  font-weight: 800;
}

.sm-16__brand-version {
  font-size: 10px;
  color: var(--muted);
  margin-left: 4px;
  font-weight: 500;
}
/* Search bar */

.sm-16__search {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}

.sm-16__search-input {
  width: 100%;
  padding: 7px 12px;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 7px;
  font-size: 12px;
  font-family: var(--font);
  color: var(--text);
  outline: none;
}

.sm-16__search-input:focus {
  border-color: var(--accent2);
}
/* Accordion section */

.sm-16__section {
  border-bottom: 1px solid var(--border);
}
/* Section header — label acts as click target */

.sm-16__section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  cursor: pointer;
  user-select: none;
  transition: background 0.15s;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted2);
}

.sm-16__section-header:hover {
  background: rgba(37,99,235,0.04);
}

.sm-16__section-header-icon {
  font-size: 14px;
}
/* Chevron */

.sm-16__chevron {
  font-size: 12px;
  color: var(--muted);
  transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
  display: inline-block;
}

.sm-16__acc-toggle:checked + .sm-16__section-header .sm-16__chevron {
  transform: rotate(90deg);
}

.sm-16__acc-toggle:checked + .sm-16__section-header {
  color: var(--accent);
}
/* Collapsible sub-items */

.sm-16__items {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.38s cubic-bezier(0.4,0,0.2,1);
}

.sm-16__acc-toggle:checked + .sm-16__section-header + .sm-16__items {
  max-height: 400px;
}
/* Individual link items */

.sm-16__item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 16px 9px 36px;
  color: var(--muted2);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.15s;
  position: relative;
}

.sm-16__item::before {
  content: '';
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--muted);
  transition: background 0.15s, transform 0.15s;
}

.sm-16__item:hover {
  color: var(--accent);
  background: rgba(37,99,235,0.05);
}

.sm-16__item:hover::before {
  background: var(--accent);
  transform: translateY(-50%) scale(1.4);
}

.sm-16__item--active {
  color: var(--accent);
  background: rgba(37,99,235,0.07);
}

.sm-16__item--active::before {
  background: var(--accent);
}

.sm-16__item-badge {
  margin-left: auto;
  background: rgba(37,99,235,0.12);
  color: var(--accent);
  font-size: 10px;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 99px;
}
/* Flat link */

.sm-16__flat {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 16px;
  color: var(--muted2);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.15s;
  border-bottom: 1px solid var(--border);
}

.sm-16__flat:hover {
  color: var(--accent);
  background: rgba(37,99,235,0.04);
}

.sm-16__flat-icon {
  font-size: 14px;
}
/* Main */

.sm-16__main {
  flex: 1;
  padding: 24px;
}

.sm-16__heading {
  font-size: 20px;
  font-weight: 800;
  margin-bottom: 6px;
}

.sm-16__sub {
  font-size: 13px;
  color: var(--muted2);
  line-height: 1.7;
  margin-bottom: 22px;
}

.sm-16__docs {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.sm-16__doc-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.sm-16__doc-card:hover {
  border-color: var(--accent2);
  box-shadow: 0 2px 12px rgba(37,99,235,0.08);
}

.sm-16__doc-icon {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  background: rgba(37,99,235,0.08);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
}

.sm-16__doc-title {
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 2px;
}

.sm-16__doc-sub {
  font-size: 12px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .sm-16__items,
    .sm-16__chevron {
    transition: none;
  }
}
```
