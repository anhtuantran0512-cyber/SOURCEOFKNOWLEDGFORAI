---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/multi-level-accordion-side-menu/"
title: "Multi-Level Accordion Side Menu"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A hierarchical documentation sidebar where each top-level section expands independently using hidden checkboxes and max-height transitions, supporting deep…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Level Accordion Side Menu
Source: https://codefronts.com/navigation/css-side-menu/multi-level-accordion-side-menu/

A hierarchical documentation sidebar where each top-level section expands independently using hidden checkboxes and max-height transitions, supporting deep nested navigation trees.
## HTML
```html
<div class="sm-07">
  <nav class="sm-07__nav">
    <div class="sm-07__brand">
      <div class="sm-07__logo">D</div>
      <div class="sm-07__brand-name">DevDocs</div>
    </div>
    <a class="sm-07__flat sm-07__flat--active" href="#"><span class="sm-07__flat-icon">⬡</span> Overview</a>
    <!-- Accordion 1 -->
    <div class="sm-07__group">
      <input type="checkbox" class="sm-07__acc-toggle" id="sm-07-acc1" checked>
      <label class="sm-07__group-label" for="sm-07-acc1">
        <span class="sm-07__flat-icon">◈</span> Components
      </label>
      <div class="sm-07__sub">
        <a class="sm-07__sub-link sm-07__sub-link--active" href="#">Buttons</a>
        <a class="sm-07__sub-link" href="#">Modals</a>
        <a class="sm-07__sub-link" href="#">Forms</a>
        <a class="sm-07__sub-link" href="#">Tables</a>
        <a class="sm-07__sub-link" href="#">Toasts</a>
      </div>
    </div>
    <!-- Accordion 2 -->
    <div class="sm-07__group">
      <input type="checkbox" class="sm-07__acc-toggle" id="sm-07-acc2">
      <label class="sm-07__group-label" for="sm-07-acc2">
        <span class="sm-07__flat-icon">▦</span> Foundations
      </label>
      <div class="sm-07__sub">
        <a class="sm-07__sub-link" href="#">Typography</a>
        <a class="sm-07__sub-link" href="#">Color System</a>
        <a class="sm-07__sub-link" href="#">Spacing Scale</a>
        <a class="sm-07__sub-link" href="#">Iconography</a>
      </div>
    </div>
    <!-- Accordion 3 -->
    <div class="sm-07__group">
      <input type="checkbox" class="sm-07__acc-toggle" id="sm-07-acc3">
      <label class="sm-07__group-label" for="sm-07-acc3">
        <span class="sm-07__flat-icon">◉</span> Patterns
      </label>
      <div class="sm-07__sub">
        <a class="sm-07__sub-link" href="#">Navigation</a>
        <a class="sm-07__sub-link" href="#">Data Display</a>
        <a class="sm-07__sub-link" href="#">Authentication</a>
      </div>
    </div>
    <a class="sm-07__flat" href="#"><span class="sm-07__flat-icon">⬙</span> Settings</a>
  </nav>
  <div class="sm-07__main">
    <div class="sm-07__page-title">Components</div>
    <div class="sm-07__page-sub">Multi-level accordion sidebar using only <code>:checked</code> state on hidden inputs and <code>max-height</code> transitions. No JavaScript.</div>
    <div class="sm-07__panel">
      <div class="sm-07__panel-title">Buttons</div>
      <div class="sm-07__panel-body">Primary, secondary, ghost, destructive, and icon-only button variants with loading states and accessible focus rings.</div>
    </div>
    <div class="sm-07__panel">
      <div class="sm-07__panel-title">Modals</div>
      <div class="sm-07__panel-body">Layered dialog system with focus trap, ARIA role management, and backdrop dismiss behaviour.</div>
    </div>
    <div class="sm-07__panel">
      <div class="sm-07__panel-title">Forms</div>
      <div class="sm-07__panel-body">Input, select, textarea, checkbox, radio, and date picker components with unified error state styling.</div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-07,
.sm-07 *,
.sm-07 *::before,
.sm-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-07 ::selection {
  background: #0891b2;
  color: #fff;
}

.sm-07 {
  --bg: #0a1628;
  --surface: #102040;
  --nav-bg: #0c1e38;
  --accent: #0891b2;
  --accent2: #22d3ee;
  --text: #e2e8f0;
  --muted: #64748b;
  --border: rgba(8,145,178,0.18);
  --font: 'IBM Plex Sans', system-ui, sans-serif;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  border-radius: 12px;
  overflow: hidden;
}
/* Accordion uses :checked on hidden inputs */

.sm-07__acc-toggle {
  display: none;
}

.sm-07__nav {
  width: 240px;
  background: var(--nav-bg);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  overflow-y: auto;
  overflow-x: hidden;
}

.sm-07__nav::-webkit-scrollbar {
  width: 3px;
}

.sm-07__nav::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

.sm-07__brand {
  padding: 18px 16px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-07__logo {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 7px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 13px;
  color: #fff;
}

.sm-07__brand-name {
  font-weight: 700;
  font-size: 14px;
}
/* Flat link */

.sm-07__flat {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 16px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.18s;
  border-left: 2px solid transparent;
}

.sm-07__flat:hover,
.sm-07__flat--active {
  color: var(--text);
  background: rgba(8,145,178,0.1);
  border-left-color: var(--accent);
}

.sm-07__flat-icon {
  font-size: 14px;
}
/* Accordion group */

.sm-07__group {
  border-bottom: 1px solid var(--border);
}

.sm-07__group-label {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 16px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.18s;
  user-select: none;
  position: relative;
}

.sm-07__group-label:hover {
  color: var(--text);
  background: rgba(8,145,178,0.07);
}

.sm-07__group-label::after {
  content: '›';
  position: absolute;
  right: 14px;
  font-size: 16px;
  transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
  color: var(--muted);
}

.sm-07__acc-toggle:checked + .sm-07__group-label {
  color: var(--accent2);
}

.sm-07__acc-toggle:checked + .sm-07__group-label::after {
  transform: rotate(90deg);
  color: var(--accent2);
}
/* Sub-links expand */

.sm-07__sub {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s cubic-bezier(0.4,0,0.2,1);
}

.sm-07__acc-toggle:checked + .sm-07__group-label + .sm-07__sub {
  max-height: 300px;
}

.sm-07__sub-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 9px 16px 9px 38px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.18s;
  position: relative;
}

.sm-07__sub-link::before {
  content: '';
  position: absolute;
  left: 22px;
  top: 50%;
  transform: translateY(-50%);
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--muted);
  transition: background 0.18s;
}

.sm-07__sub-link:hover {
  color: var(--text);
  background: rgba(8,145,178,0.1);
}

.sm-07__sub-link:hover::before {
  background: var(--accent2);
}

.sm-07__sub-link--active {
  color: var(--accent2);
}

.sm-07__sub-link--active::before {
  background: var(--accent2);
  box-shadow: 0 0 6px var(--accent);
}
/* Main */

.sm-07__main {
  flex: 1;
  padding: 24px;
}

.sm-07__page-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
}

.sm-07__page-sub {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 20px;
}

.sm-07__panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 18px;
  margin-bottom: 12px;
}

.sm-07__panel-title {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 4px;
}

.sm-07__panel-body {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.6;
}

@media (prefers-reduced-motion: reduce) {
  .sm-07__sub,
    .sm-07__group-label::after {
    transition: none;
  }
}
```
