---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-tabs-css/"
title: "Material Design Tabs CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Primary, scrollable, icon-plus-label, and vertical tab bars — all driven by the CSS checkbox-hack with an animated active ink bar, no JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Tabs CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-tabs-css/

Primary, scrollable, icon-plus-label, and vertical tab bars — all driven by the CSS checkbox-hack with an animated active ink bar, no JavaScript.
## HTML
```html
<div class="md-07">
  <div class="md-07__wrap">
    <div class="md-07__page-title">Material Design Tabs CSS</div>
    <div class="md-07__page-sub">Primary, scrollable, icon and vertical tab components — all CSS checkbox-hack, no JavaScript</div>

    <!-- Primary Tabs -->
    <div class="md-07__section">
      <div class="md-07__section-label" style="padding-bottom:0;background:var(--primary);color:rgba(255,255,255,.6)">Primary Tabs</div>
      <input class="md-07__tab-in" type="radio" name="md07p" id="md07p1" checked>
      <input class="md-07__tab-in" type="radio" name="md07p" id="md07p2">
      <input class="md-07__tab-in" type="radio" name="md07p" id="md07p3">
      <input class="md-07__tab-in" type="radio" name="md07p" id="md07p4">
      <div class="md-07__tabs">
        <label class="md-07__tab-lbl" for="md07p1">Overview</label>
        <label class="md-07__tab-lbl" for="md07p2">Analytics <span class="md-07__tab-badge">3</span></label>
        <label class="md-07__tab-lbl" for="md07p3">Settings</label>
        <label class="md-07__tab-lbl" for="md07p4">History</label>
      </div>
      <div class="md-07__panels">
        <div class="md-07__panel md-07__panel--1">
          <div class="md-07__panel-title">Project Overview</div>
          <div class="md-07__panel-text">Aurora Design System is a comprehensive Material Design 3 component library. It provides 240+ components, 12 themes and full accessibility compliance out of the box.</div>
          <div class="md-07__stat-row">
            <div class="md-07__stat"><div class="md-07__stat-val">240+</div><div class="md-07__stat-lbl">Components</div></div>
            <div class="md-07__stat"><div class="md-07__stat-val">12</div><div class="md-07__stat-lbl">Themes</div></div>
            <div class="md-07__stat"><div class="md-07__stat-val">98%</div><div class="md-07__stat-lbl">Coverage</div></div>
            <div class="md-07__stat"><div class="md-07__stat-val">4.9★</div><div class="md-07__stat-lbl">Rating</div></div>
          </div>
        </div>
        <div class="md-07__panel md-07__panel--2">
          <div class="md-07__panel-title">Analytics Dashboard</div>
          <div class="md-07__panel-text">Page views, session durations and conversion rates from the past 30 days. All metrics trending upward.</div>
          <div class="md-07__stat-row">
            <div class="md-07__stat"><div class="md-07__stat-val">84.2k</div><div class="md-07__stat-lbl">Page Views</div></div>
            <div class="md-07__stat"><div class="md-07__stat-val">3m 42s</div><div class="md-07__stat-lbl">Avg. Session</div></div>
            <div class="md-07__stat"><div class="md-07__stat-val">6.8%</div><div class="md-07__stat-lbl">Conversion</div></div>
          </div>
        </div>
        <div class="md-07__panel md-07__panel--3">
          <div class="md-07__panel-title">Project Settings</div>
          <div class="md-07__panel-text">Manage project configuration, API keys, webhooks and team permissions from this panel.</div>
          <ul class="md-07__list">
            <li>Enable dark mode by default</li>
            <li>Set custom domain: aurora.design</li>
            <li>Configure Figma plugin sync</li>
            <li>Manage webhook endpoints</li>
            <li>Export tokens as CSS variables</li>
          </ul>
        </div>
        <div class="md-07__panel md-07__panel--4">
          <div class="md-07__panel-title">Version History</div>
          <div class="md-07__panel-text">Track all changes, releases and rollbacks for your design system.</div>
          <ul class="md-07__list">
            <li>v3.4.0 — New icon set (340 icons)</li>
            <li>v3.3.2 — Dialog animation fixes</li>
            <li>v3.3.0 — Tabs & nav rail components</li>
            <li>v3.2.0 — M3 color scheme support</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Scrollable Tabs -->
    <div class="md-07__section">
      <div class="md-07__section-label">Scrollable Tabs</div>
      <input class="md-07__tab-in" type="radio" name="md07s" id="md07s1" checked>
      <input class="md-07__tab-in" type="radio" name="md07s" id="md07s2">
      <input class="md-07__tab-in" type="radio" name="md07s" id="md07s3">
      <input class="md-07__tab-in" type="radio" name="md07s" id="md07s4">
      <input class="md-07__tab-in" type="radio" name="md07s" id="md07s5">
      <input class="md-07__tab-in" type="radio" name="md07s" id="md07s6">
      <div class="md-07__tabs md-07__tabs--scroll">
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07s1">All Items</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07s2">Typography</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07s3">Color</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07s4">Spacing</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07s5">Motion</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07s6">Elevation</label>
      </div>
      <div class="md-07__panels">
        <div class="md-07__panel md-07__panel--s1"><div class="md-07__panel-title">All Design Tokens</div><div class="md-07__panel-text">Comprehensive list of all design tokens across typography, color, spacing, motion and elevation systems.</div></div>
        <div class="md-07__panel md-07__panel--s2"><div class="md-07__panel-title">Typography Scale</div><div class="md-07__panel-text">Headline Display — 57sp · Large · Weight 400<br>Headline Large — 32sp · Weight 400<br>Title Medium — 16sp · Weight 500<br>Body Large — 16sp · Weight 400<br>Label Small — 11sp · Weight 500</div></div>
        <div class="md-07__panel md-07__panel--s3"><div class="md-07__panel-title">Color System</div><div class="md-07__panel-text">Primary, Secondary, Tertiary, Error and Neutral palettes generated from seed color using HCT color space. Each role has Light and Dark mode values.</div></div>
        <div class="md-07__panel md-07__panel--s4"><div class="md-07__panel-title">Spacing System</div><div class="md-07__panel-text">4dp base grid. Common spacings: 4, 8, 12, 16, 24, 32, 48, 64dp. Component padding follows 16dp horizontal and 8/12dp vertical conventions.</div></div>
        <div class="md-07__panel md-07__panel--s5"><div class="md-07__panel-title">Motion System</div><div class="md-07__panel-text">Standard: 300ms · Emphasized: 500ms cubic-bezier(.2,0,0,1) · Decelerate: cubic-bezier(0,0,0,1) · Accelerate: cubic-bezier(.3,0,1,1)</div></div>
        <div class="md-07__panel md-07__panel--s6"><div class="md-07__panel-title">Elevation Levels</div><div class="md-07__panel-text">0: Flat · 1: Filled · 2: Outlined · 3: Raised (cards) · 4: FAB · 5: Nav drawer · 6: Modal dialogs</div></div>
      </div>
    </div>

    <!-- Icon Tabs -->
    <div class="md-07__section">
      <div class="md-07__section-label">Icon + Label Tabs</div>
      <input class="md-07__tab-in" type="radio" name="md07i" id="md07i1" checked>
      <input class="md-07__tab-in" type="radio" name="md07i" id="md07i2">
      <input class="md-07__tab-in" type="radio" name="md07i" id="md07i3">
      <input class="md-07__tab-in" type="radio" name="md07i" id="md07i4">
      <div class="md-07__tabs md-07__tabs--icon md-07__tabs--scroll" style="background:var(--surface);border-bottom:1px solid var(--divider)">
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07i1"><span class="md-07__tab-icon">🏠</span>Home</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07i2"><span class="md-07__tab-icon">🔔</span>Alerts</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07i3"><span class="md-07__tab-icon">📁</span>Files</label>
        <label class="md-07__tab-lbl md-07__tab-lbl--scroll" for="md07i4"><span class="md-07__tab-icon">👤</span>Profile</label>
      </div>
      <div class="md-07__panels">
        <div class="md-07__panel md-07__panel--s1" style="display:none" id="md07icon1">Home tab content</div>
      </div>
      <div class="md-07__panels" style="padding-top:0">
        <div class="md-07__panel md-07__panel--i1" id="md07-i-panel">
          <div class="md-07__panel-title" id="md07-icon-title">Home</div>
          <div class="md-07__panel-text">Tab panels with icon + label, following Material Design 3 icon tab guidelines for improved visual hierarchy and tap target accessibility.</div>
        </div>
      </div>
    </div>

    <!-- Vertical Tabs -->
    <div class="md-07__section">
      <div class="md-07__section-label" style="padding-bottom:16px">Vertical Tabs</div>
      <div class="md-07__vert-wrap">
        <input class="md-07__tab-in" type="radio" name="md07v" id="md07v1" checked>
        <input class="md-07__tab-in" type="radio" name="md07v" id="md07v2">
        <input class="md-07__tab-in" type="radio" name="md07v" id="md07v3">
        <input class="md-07__tab-in" type="radio" name="md07v" id="md07v4">
        <div class="md-07__tabs md-07__tabs--vert">
          <label class="md-07__tab-lbl md-07__tab-lbl--vert" for="md07v1"><span>🎨</span>Design</label>
          <label class="md-07__tab-lbl md-07__tab-lbl--vert" for="md07v2"><span>⚡</span>Develop</label>
          <label class="md-07__tab-lbl md-07__tab-lbl--vert" for="md07v3"><span>🧪</span>Test</label>
          <label class="md-07__tab-lbl md-07__tab-lbl--vert" for="md07v4"><span>🚀</span>Deploy</label>
        </div>
        <div class="md-07__vert-panels">
          <div class="md-07__panel md-07__panel--v1"><div class="md-07__panel-title">Design Phase</div><div class="md-07__panel-text">Create wireframes and high-fidelity designs using the Aurora component library in Figma. Use design tokens for consistency across all breakpoints.</div></div>
          <div class="md-07__panel md-07__panel--v2"><div class="md-07__panel-title">Development Phase</div><div class="md-07__panel-text">Implement components using React and CSS custom properties. Leverage the Aurora npm package for pre-built accessible Material Design 3 components.</div></div>
          <div class="md-07__panel md-07__panel--v3"><div class="md-07__panel-title">Testing Phase</div><div class="md-07__panel-text">Run Playwright visual regression tests, axe accessibility audits and cross-browser compatibility checks. Target &gt;94% code coverage.</div></div>
          <div class="md-07__panel md-07__panel--v4"><div class="md-07__panel-title">Deployment Phase</div><div class="md-07__panel-text">Publish to npm registry, update Figma plugin, generate changelog and notify subscribers. CI/CD pipeline handles versioning automatically.</div></div>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.md-07,
.md-07 *,
.md-07 *::before,
.md-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-07 ::selection {
  background: #2e7d32;
  color: #fff;
}

.md-07 {
  --primary: #2e7d32;
  --primary-l: #66bb6a;
  --secondary: #ff8f00;
  --bg: #f1f8e9;
  --surface: #fff;
  --ink: #212121;
  --ink2: #546e7a;
  --ink3: #90a4ae;
  --divider: #c5e1a5;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-07__wrap {
  max-width: 860px;
  margin: 0 auto;
}

.md-07__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
}

.md-07__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  margin-bottom: 40px;
}
/* ── TAB SECTION WRAPPER ── */

.md-07__section {
  background: var(--surface);
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 32px;
  box-shadow: 0 1px 4px rgba(0,0,0,.1);
}

.md-07__section-label {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink2);
  padding: 20px 20px 0;
}
/* ── PRIMARY TABS ── */

.md-07__tabs {
  display: flex;
  background: var(--primary);
  position: relative;
}

.md-07__tab-in {
  display: none;
}

.md-07__tab-lbl {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  height: 48px;
  padding: 0 16px;
  cursor: pointer;
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  position: relative;
  user-select: none;
  transition: color .2s;
  white-space: nowrap;
}

.md-07__tab-lbl::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: #fff;
  border-radius: 2px 2px 0 0;
  transform: scaleX(0);
  transition: transform .25s cubic-bezier(.4,0,.2,1);
}

.md-07__tab-in:checked + .md-07__tab-lbl {
  color: #fff;
}

.md-07__tab-in:checked + .md-07__tab-lbl::after {
  transform: scaleX(1);
}

.md-07__tab-badge {
  background: var(--secondary);
  color: #fff;
  font-size: .65rem;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 8px;
  line-height: 1.6;
}
/* ── TAB PANELS ── */

.md-07__panels {
  padding: 28px;
}

.md-07__panel {
  display: none;
}

#md07p1:checked ~ .md-07__panels .md-07__panel--1,
#md07p2:checked ~ .md-07__panels .md-07__panel--2,
#md07p3:checked ~ .md-07__panels .md-07__panel--3,
#md07p4:checked ~ .md-07__panels .md-07__panel--4 {
  display: block;
}
/* ── SCROLLABLE TABS ── */

.md-07__tabs--scroll {
  overflow-x: auto;
  scrollbar-width: none;
  background: var(--surface);
  border-bottom: 1px solid var(--divider);
}

.md-07__tabs--scroll::-webkit-scrollbar {
  display: none;
}

.md-07__tab-lbl--scroll {
  flex: none;
  color: var(--ink2);
  height: 48px;
}

.md-07__tab-lbl--scroll::after {
  background: var(--primary);
  height: 3px;
}

.md-07__tab-in:checked + .md-07__tab-lbl--scroll {
  color: var(--primary);
}

#md07s1:checked ~ .md-07__panels .md-07__panel--s1,
#md07s2:checked ~ .md-07__panels .md-07__panel--s2,
#md07s3:checked ~ .md-07__panels .md-07__panel--s3,
#md07s4:checked ~ .md-07__panels .md-07__panel--s4,
#md07s5:checked ~ .md-07__panels .md-07__panel--s5,
#md07s6:checked ~ .md-07__panels .md-07__panel--s6 {
  display: block;
}
/* ── SECONDARY/ICON TABS ── */

.md-07__tabs--icon .md-07__tab-lbl {
  flex-direction: column;
  height: 64px;
  gap: 4px;
  font-size: .7rem;
}

.md-07__tab-icon {
  font-size: 1.3rem;
  display: block;
}
/* ── VERTICAL TABS ── */

.md-07__vert-wrap {
  display: flex;
  gap: 0;
  min-height: 240px;
}

.md-07__tabs--vert {
  flex-direction: column;
  background: var(--surface);
  border-right: 1px solid var(--divider);
  width: 180px;
  flex-shrink: 0;
}

.md-07__tab-lbl--vert {
  flex: none;
  height: 48px;
  justify-content: flex-start;
  padding: 0 20px;
  color: var(--ink2);
  font-size: .875rem;
  gap: 12px;
}

.md-07__tab-lbl--vert::after {
  left: auto;
  right: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  height: auto;
  background: var(--primary);
  border-radius: 2px 0 0 2px;
}

.md-07__tab-in:checked + .md-07__tab-lbl--vert {
  color: var(--primary);
  background: rgba(46,125,50,.06);
}

.md-07__vert-panels {
  flex: 1;
  padding: 24px;
}

#md07v1:checked ~ .md-07__vert-panels .md-07__panel--v1,
#md07v2:checked ~ .md-07__vert-panels .md-07__panel--v2,
#md07v3:checked ~ .md-07__vert-panels .md-07__panel--v3,
#md07v4:checked ~ .md-07__vert-panels .md-07__panel--v4 {
  display: block;
}
/* Panel content styles */

.md-07__panel-title {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 10px;
  color: var(--ink);
}

.md-07__panel-text {
  font-size: .9rem;
  line-height: 1.7;
  color: var(--ink2);
}

.md-07__stat-row {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin-top: 16px;
}

.md-07__stat {
  background: var(--bg);
  border-radius: 10px;
  padding: 16px 20px;
  flex: 1;
  min-width: 100px;
}

.md-07__stat-val {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary);
}

.md-07__stat-lbl {
  font-size: .75rem;
  color: var(--ink2);
  margin-top: 2px;
}

.md-07__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 8px;
}

.md-07__list li {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .88rem;
  color: var(--ink2);
}

.md-07__list li::before {
  content: '✓';
  color: var(--primary);
  font-weight: 700;
  flex-shrink: 0;
}

@media (prefers-reduced-motion: reduce) {
  .md-07 * {
    transition: none!important;
  }
}
```
