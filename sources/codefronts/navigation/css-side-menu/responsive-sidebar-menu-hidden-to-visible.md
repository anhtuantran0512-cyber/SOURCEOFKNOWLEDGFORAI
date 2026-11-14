---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/responsive-sidebar-menu-hidden-to-visible/"
title: "Responsive Sidebar Menu (Hidden-to-Visible)"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A sidebar permanently visible as a fixed column on desktop that hides off-screen on mobile and is revealed by a burger toggle, all handled by CSS media…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Sidebar Menu (Hidden-to-Visible)
Source: https://codefronts.com/navigation/css-side-menu/responsive-sidebar-menu-hidden-to-visible/

A sidebar permanently visible as a fixed column on desktop that hides off-screen on mobile and is revealed by a burger toggle, all handled by CSS media queries alone.
## HTML
```html
<div class="sm-05">
  <input type="checkbox" class="sm-05__toggle" id="sm-05-toggle">
  <nav class="sm-05__nav">
    <div class="sm-05__brand">
      <div class="sm-05__logo">P</div>
      <div class="sm-05__brand-name">Prism UI</div>
    </div>
    <div class="sm-05__section-title">Main Menu</div>
    <div class="sm-05__links">
      <a class="sm-05__link sm-05__link--active" href="#"><span class="sm-05__link-icon">⬡</span> Home</a>
      <a class="sm-05__link" href="#"><span class="sm-05__link-icon">◈</span> Reports <span class="sm-05__badge">4</span></a>
      <a class="sm-05__link" href="#"><span class="sm-05__link-icon">▦</span> Campaigns</a>
      <a class="sm-05__link" href="#"><span class="sm-05__link-icon">◬</span> Audience</a>
    </div>
    <div class="sm-05__divider"></div>
    <div class="sm-05__section-title">Account</div>
    <div class="sm-05__links">
      <a class="sm-05__link" href="#"><span class="sm-05__link-icon">◉</span> Profile</a>
      <a class="sm-05__link" href="#"><span class="sm-05__link-icon">⬙</span> Settings</a>
    </div>
    <div class="sm-05__footer">
      <div class="sm-05__avatar">SR</div>
      <div>
        <div class="sm-05__uname">Sam R.</div>
        <div class="sm-05__urole">Editor</div>
      </div>
    </div>
  </nav>
  <div class="sm-05__main">
    <div class="sm-05__topbar">
      <label class="sm-05__burger" for="sm-05-toggle">
        <span></span><span></span><span></span>
      </label>
      <div class="sm-05__topbar-title">Home</div>
      <div class="sm-05__topbar-breadcrumb">Prism / Home</div>
    </div>
    <div class="sm-05__content">
      <div class="sm-05__welcome">Good morning, Sam 🌤</div>
      <div class="sm-05__sub">Sidebar is always visible on wide screens. Resize to mobile to see it hide off-screen with a burger toggle — no JS.</div>
      <div class="sm-05__grid">
        <div class="sm-05__card"><div class="sm-05__card-val">5,382</div><div class="sm-05__card-lbl">Sessions</div></div>
        <div class="sm-05__card"><div class="sm-05__card-val">63%</div><div class="sm-05__card-lbl">Conversion</div></div>
        <div class="sm-05__card"><div class="sm-05__card-val">228</div><div class="sm-05__card-lbl">Subscribers</div></div>
        <div class="sm-05__card"><div class="sm-05__card-val">$4.8k</div><div class="sm-05__card-lbl">Revenue</div></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-05,
.sm-05 *,
.sm-05 *::before,
.sm-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-05 ::selection {
  background: #6366f1;
  color: #fff;
}

.sm-05 {
  --bg: #f8fafc;
  --surface: #fff;
  --nav-bg: #fff;
  --accent: #6366f1;
  --accent2: #818cf8;
  --text: #1e293b;
  --muted: #94a3b8;
  --border: #e2e8f0;
  --font: 'Nunito', system-ui, sans-serif;
  --w: 240px;
  --dur: 0.35s;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  display: flex;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}
/* Mobile toggle */

.sm-05__toggle {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
/* Nav */

.sm-05__nav {
  width: var(--w);
  min-height: 460px;
  background: var(--nav-bg);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  padding: 20px 0;
  flex-shrink: 0;
  position: relative;
  box-shadow: 2px 0 12px rgba(99,102,241,0.06);
}
/* Desktop: always visible — simulated here by having the wrapper at full width */
/* On mobile the sidebar is off-canvas */

@media (max-width: 600px) {
  .sm-05__nav {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    transform: translateX(-100%);
    transition: transform var(--dur) cubic-bezier(0.4,0,0.2,1);
    z-index: 20;
  }

  .sm-05__toggle:checked ~ .sm-05__nav {
    transform: translateX(0);
  }
}

.sm-05__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0 20px 18px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 12px;
}

.sm-05__logo {
  width: 34px;
  height: 34px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 15px;
  color: #fff;
}

.sm-05__brand-name {
  font-size: 15px;
  font-weight: 800;
}

.sm-05__section-title {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 8px 20px 4px;
}

.sm-05__links {
  flex: 1;
  padding: 0 10px;
}

.sm-05__link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  border-radius: 9px;
  color: #64748b;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
  margin-bottom: 2px;
}

.sm-05__link:hover {
  color: var(--accent);
  background: rgba(99,102,241,0.07);
}

.sm-05__link--active {
  color: var(--accent);
  background: rgba(99,102,241,0.1);
}

.sm-05__link-icon {
  font-size: 16px;
}

.sm-05__badge {
  margin-left: auto;
  background: var(--accent);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
}

.sm-05__divider {
  height: 1px;
  background: var(--border);
  margin: 10px 20px;
}
/* User bottom */

.sm-05__footer {
  padding: 14px 16px 0;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-05__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
}

.sm-05__uname {
  font-size: 13px;
  font-weight: 700;
}

.sm-05__urole {
  font-size: 11px;
  color: var(--muted);
}
/* Main */

.sm-05__main {
  flex: 1;
  min-width: 0;
}

.sm-05__topbar {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 20px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}

.sm-05__burger {
  display: none;
  width: 36px;
  height: 36px;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  cursor: pointer;
  transition: background 0.2s;
}

@media (max-width: 600px) {
  .sm-05__burger {
    display: flex;
  }
}

.sm-05__burger span {
  width: 14px;
  height: 2px;
  background: #64748b;
  border-radius: 2px;
}

.sm-05__topbar-title {
  font-size: 16px;
  font-weight: 800;
}

.sm-05__topbar-breadcrumb {
  font-size: 12px;
  color: var(--muted);
  margin-left: auto;
}

.sm-05__content {
  padding: 22px 20px;
}

.sm-05__welcome {
  font-size: 19px;
  font-weight: 800;
  margin-bottom: 6px;
}

.sm-05__sub {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 20px;
}

.sm-05__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sm-05__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}

.sm-05__card-val {
  font-size: 22px;
  font-weight: 800;
  color: var(--accent);
}

.sm-05__card-lbl {
  font-size: 12px;
  color: var(--muted);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-05__nav {
    transition: none;
  }
}
```
