---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-navigation-css/"
title: "Material Design Navigation CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Top app bar, navigation drawer, navigation rail, bottom navigation bar, scrollable tab bar, and breadcrumb trail — all built with CSS custom properties and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Navigation CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-navigation-css/

Top app bar, navigation drawer, navigation rail, bottom navigation bar, scrollable tab bar, and breadcrumb trail — all built with CSS custom properties and zero JavaScript.
## HTML
```html
<div class="md-03">
  <!-- Top App Bar -->
  <div class="md-03__appbar">
    <button class="md-03__appbar-menu">☰</button>
    <span class="md-03__appbar-title">Material Navigation</span>
    <div class="md-03__appbar-actions">
      <button class="md-03__appbar-action">🔍</button>
      <button class="md-03__appbar-action">🔔</button>
      <button class="md-03__appbar-action">⋮</button>
    </div>
  </div>

  <div class="md-03__body">
    <!-- Navigation Drawer -->
    <nav class="md-03__drawer">
      <div class="md-03__drawer-section">
        <div class="md-03__drawer-section-title">Main</div>
        <div class="md-03__nav-item md-03__nav-item--active">
          <span class="md-03__nav-icon">🏠</span>Home
        </div>
        <div class="md-03__nav-item">
          <span class="md-03__nav-icon">📊</span>Dashboard
          <span class="md-03__nav-badge">3</span>
        </div>
        <div class="md-03__nav-item">
          <span class="md-03__nav-icon">📁</span>Projects
        </div>
        <div class="md-03__nav-item">
          <span class="md-03__nav-icon">📅</span>Calendar
        </div>
      </div>
      <div class="md-03__divider"></div>
      <div class="md-03__drawer-section">
        <div class="md-03__drawer-section-title">Settings</div>
        <div class="md-03__nav-item">
          <span class="md-03__nav-icon">👤</span>Profile
        </div>
        <div class="md-03__nav-item">
          <span class="md-03__nav-icon">🔔</span>Notifications
          <span class="md-03__nav-badge">12</span>
        </div>
        <div class="md-03__nav-item">
          <span class="md-03__nav-icon">⚙</span>Settings
        </div>
        <div class="md-03__nav-item">
          <span class="md-03__nav-icon">❓</span>Help
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="md-03__main">
      <!-- Breadcrumbs -->
      <div class="md-03__breadcrumbs">
        <span class="md-03__breadcrumb-link">Home</span>
        <span class="md-03__breadcrumb-sep">›</span>
        <span class="md-03__breadcrumb-link">Projects</span>
        <span class="md-03__breadcrumb-sep">›</span>
        <span>Material Navigation Demo</span>
      </div>

      <!-- Tab Bar -->
      <div class="md-03__tabs">
        <input class="md-03__tab-input" type="radio" name="md03tab" id="md03t1" checked>
        <label class="md-03__tab-label" for="md03t1">Overview</label>
        <input class="md-03__tab-input" type="radio" name="md03tab" id="md03t2">
        <label class="md-03__tab-label" for="md03t2">Components</label>
        <input class="md-03__tab-input" type="radio" name="md03tab" id="md03t3">
        <label class="md-03__tab-label" for="md03t3">Guidelines</label>
        <input class="md-03__tab-input" type="radio" name="md03tab" id="md03t4">
        <label class="md-03__tab-label" for="md03t4">Resources</label>
      </div>

      <div class="md-03__content-card">
        <div class="md-03__section-head">Navigation Patterns</div>
        <p style="color:var(--ink2);line-height:1.6;font-size:.9rem">Material Design 3 provides multiple navigation components: the <strong>Navigation Drawer</strong> (left sidebar) for complex apps, the <strong>Navigation Rail</strong> (compact vertical) for tablets, the <strong>Bottom Navigation Bar</strong> for mobile, and the <strong>Top Tab Bar</strong> for content switching. Each adapts to screen size and app complexity.</p>
      </div>

      <!-- Bottom Navigation Bar -->
      <div class="md-03__section-head" style="margin-top:8px">Bottom Navigation Bar</div>
      <div class="md-03__bottomnav">
        <input class="md-03__bn-input" type="radio" name="md03bn" id="md03bn1" checked>
        <label class="md-03__bn-label" for="md03bn1">
          <span class="md-03__bn-icon">🏠</span>Home
        </label>
        <input class="md-03__bn-input" type="radio" name="md03bn" id="md03bn2">
        <label class="md-03__bn-label" for="md03bn2">
          <span class="md-03__bn-icon">🔍</span>Search
        </label>
        <input class="md-03__bn-input" type="radio" name="md03bn" id="md03bn3">
        <label class="md-03__bn-label" for="md03bn3">
          <span class="md-03__bn-icon">🔔<span class="md-03__bn-badge">5</span></span>Alerts
        </label>
        <input class="md-03__bn-input" type="radio" name="md03bn" id="md03bn4">
        <label class="md-03__bn-label" for="md03bn4">
          <span class="md-03__bn-icon">👤</span>Profile
        </label>
      </div>
    </main>

    <!-- Navigation Rail -->
    <nav class="md-03__rail">
      <button class="md-03__rail-fab">+</button>
      <div class="md-03__rail-item md-03__rail-item--active">
        <div class="md-03__rail-icon-wrap">🏠</div>
        <span>Home</span>
      </div>
      <div class="md-03__rail-item">
        <div class="md-03__rail-icon-wrap">📊</div>
        <span>Stats</span>
      </div>
      <div class="md-03__rail-item">
        <div class="md-03__rail-icon-wrap">📁</div>
        <span>Files</span>
      </div>
      <div class="md-03__rail-item">
        <div class="md-03__rail-icon-wrap">⚙</div>
        <span>Settings</span>
      </div>
    </nav>
  </div>
</div>
```
## CSS
```css
.md-03,
.md-03 *,
.md-03 *::before,
.md-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-03 ::selection {
  background: #c62828;
  color: #fff;
}

.md-03 {
  --primary: #c62828;
  --primary-light: #ef5350;
  --primary-dark: #8d1c1c;
  --secondary: #ff8a65;
  --surface: #fff;
  --bg: #fafafa;
  --ink: #212121;
  --ink2: #757575;
  --ink3: #bdbdbd;
  --divider: #e0e0e0;
  --nav-h: 64px;
  --rail-w: 80px;
  --sidebar-w: 256px;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  color: var(--ink);
  min-height: 100vh;
}
/* ── TOP APP BAR ── */

.md-03__appbar {
  width: 100%;
  height: var(--nav-h);
  background: var(--primary);
  color: #fff;
  display: flex;
  align-items: center;
  padding: 0 16px;
  gap: 12px;
  box-shadow: 0 2px 4px rgba(0,0,0,.25);
  position: sticky;
  top: 0;
  z-index: 10;
}

.md-03__appbar-menu {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: none;
  background: transparent;
  color: #fff;
  cursor: pointer;
  font-size: 1.3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background .2s;
}

.md-03__appbar-menu:hover {
  background: rgba(255,255,255,.12);
}

.md-03__appbar-title {
  font-size: 1.25rem;
  font-weight: 500;
  letter-spacing: .0125em;
  flex: 1;
}

.md-03__appbar-actions {
  display: flex;
  gap: 4px;
}

.md-03__appbar-action {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: none;
  background: transparent;
  color: #fff;
  cursor: pointer;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background .2s;
}

.md-03__appbar-action:hover {
  background: rgba(255,255,255,.12);
}
/* ── LAYOUT BODY ── */

.md-03__body {
  display: flex;
  min-height: calc(100vh - var(--nav-h));
}
/* ── NAVIGATION DRAWER ── */

.md-03__drawer {
  width: var(--sidebar-w);
  flex-shrink: 0;
  background: var(--surface);
  border-right: 1px solid var(--divider);
  padding: 12px 0;
  overflow-y: auto;
}

.md-03__drawer-section {
  padding: 4px 0;
  margin-bottom: 4px;
}

.md-03__drawer-section-title {
  font-size: .75rem;
  font-weight: 500;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--ink2);
  padding: 8px 16px 4px;
}

.md-03__nav-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0 16px;
  height: 48px;
  border-radius: 0 24px 24px 0;
  margin-right: 16px;
  cursor: pointer;
  font-size: .9rem;
  font-weight: 400;
  color: var(--ink2);
  transition: background .15s,color .15s;
  position: relative;
  overflow: hidden;
  user-select: none;
}

.md-03__nav-item:hover {
  background: rgba(0,0,0,.04);
}

.md-03__nav-item--active {
  background: rgba(198,40,40,.12);
  color: var(--primary);
  font-weight: 500;
}

.md-03__nav-item--active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 25%;
  bottom: 25%;
  width: 3px;
  border-radius: 0 2px 2px 0;
  background: var(--primary);
}

.md-03__nav-icon {
  font-size: 1.3rem;
  width: 24px;
  text-align: center;
}

.md-03__nav-badge {
  margin-left: auto;
  background: var(--primary);
  color: #fff;
  font-size: .7rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 10px;
}

.md-03__divider {
  height: 1px;
  background: var(--divider);
  margin: 8px 16px;
}
/* ── NAVIGATION RAIL (shown on right in demo) ── */

.md-03__rail {
  width: var(--rail-w);
  background: var(--surface);
  border-left: 1px solid var(--divider);
  padding: 16px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.md-03__rail-fab {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  border: none;
  background: var(--secondary);
  color: #fff;
  font-size: 1.4rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(255,138,101,.4);
  margin-bottom: 8px;
  transition: box-shadow .2s,transform .2s;
}

.md-03__rail-fab:hover {
  box-shadow: 0 4px 16px rgba(255,138,101,.5);
  transform: translateY(-2px);
}

.md-03__rail-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  width: 72px;
  padding: 12px 0;
  border-radius: 16px;
  cursor: pointer;
  font-size: .7rem;
  font-weight: 500;
  color: var(--ink2);
  transition: background .15s,color .15s;
}

.md-03__rail-item:hover {
  background: rgba(0,0,0,.04);
}

.md-03__rail-item--active {
  color: var(--primary);
}

.md-03__rail-item--active .md-03__rail-icon-wrap {
  background: rgba(198,40,40,.12);
}

.md-03__rail-icon-wrap {
  width: 56px;
  height: 32px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
}
/* ── MAIN CONTENT ── */

.md-03__main {
  flex: 1;
  padding: 32px;
  overflow: auto;
}

.md-03__section-head {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--ink);
}
/* ── TAB BAR ── */

.md-03__tabs {
  background: var(--primary);
  display: flex;
  border-bottom: none;
  margin-bottom: 28px;
  border-radius: 0;
}

.md-03__tab-input {
  display: none;
}

.md-03__tab-label {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 48px;
  gap: 4px;
  padding: 0 16px;
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  cursor: pointer;
  position: relative;
  transition: color .2s;
  user-select: none;
}

.md-03__tab-label::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: #fff;
  transform: scaleX(0);
  transition: transform .2s;
}

.md-03__tab-input:checked + .md-03__tab-label {
  color: #fff;
}

.md-03__tab-input:checked + .md-03__tab-label::after {
  transform: scaleX(1);
}
/* ── BREADCRUMBS ── */

.md-03__breadcrumbs {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .85rem;
  color: var(--ink2);
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.md-03__breadcrumb-link {
  color: var(--primary);
  text-decoration: none;
  cursor: pointer;
}

.md-03__breadcrumb-link:hover {
  text-decoration: underline;
}

.md-03__breadcrumb-sep {
  color: var(--ink3);
}
/* ── BOTTOM NAV BAR ── */

.md-03__bottomnav {
  background: var(--surface);
  border-top: 1px solid var(--divider);
  display: flex;
  box-shadow: 0 -2px 4px rgba(0,0,0,.08);
  margin-top: 24px;
  border-radius: 8px;
  overflow: hidden;
}

.md-03__bn-input {
  display: none;
}

.md-03__bn-label {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 8px 0 10px;
  gap: 4px;
  cursor: pointer;
  font-size: .7rem;
  font-weight: 500;
  letter-spacing: .04em;
  color: var(--ink2);
  transition: color .15s;
  position: relative;
}

.md-03__bn-icon {
  font-size: 1.4rem;
  position: relative;
}

.md-03__bn-input:checked + .md-03__bn-label {
  color: var(--primary);
}

.md-03__bn-badge {
  position: absolute;
  top: -4px;
  right: -8px;
  background: var(--primary);
  color: #fff;
  font-size: .6rem;
  font-weight: 700;
  padding: 1px 5px;
  border-radius: 8px;
}
/* Content card in main */

.md-03__content-card {
  background: var(--surface);
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 16px;
  box-shadow: 0 1px 3px rgba(0,0,0,.1);
}

@media (prefers-reduced-motion: reduce) {
  .md-03 * {
    transition: none!important;
  }
}
```
