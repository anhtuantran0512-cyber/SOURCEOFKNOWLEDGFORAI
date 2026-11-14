---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/neumorphic-inset-side-menu/"
title: "Neumorphic Inset Side Menu"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A dark-mode dashboard sidebar using soft extruded box-shadows and recessed inset-shadow interactive states to simulate a tactile raised and pressed surface…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Inset Side Menu
Source: https://codefronts.com/navigation/css-side-menu/neumorphic-inset-side-menu/

A dark-mode dashboard sidebar using soft extruded box-shadows and recessed inset-shadow interactive states to simulate a tactile raised and pressed surface aesthetic.
## HTML
```html
<div class="sm-09">
  <nav class="sm-09__nav">
    <div class="sm-09__brand">
      <div class="sm-09__logo">N</div>
      <div class="sm-09__brand-name">Neura</div>
    </div>
    <div class="sm-09__links">
      <a class="sm-09__link sm-09__link--active" href="#"><span class="sm-09__link-icon">⬡</span><span class="sm-09__link-text">Dashboard</span><span class="sm-09__dot"></span></a>
      <a class="sm-09__link" href="#"><span class="sm-09__link-icon">◈</span><span class="sm-09__link-text">Analytics</span><span class="sm-09__dot"></span></a>
      <a class="sm-09__link" href="#"><span class="sm-09__link-icon">▦</span><span class="sm-09__link-text">Calendar</span><span class="sm-09__dot"></span></a>
      <a class="sm-09__link" href="#"><span class="sm-09__link-icon">◉</span><span class="sm-09__link-text">Messages</span><span class="sm-09__dot"></span></a>
      <div class="sm-09__divider"></div>
      <a class="sm-09__link" href="#"><span class="sm-09__link-icon">⬙</span><span class="sm-09__link-text">Settings</span><span class="sm-09__dot"></span></a>
    </div>
    <div class="sm-09__user-card">
      <div class="sm-09__avatar">PB</div>
      <div>
        <div class="sm-09__uname">P. Blake</div>
        <div class="sm-09__urole">Designer</div>
      </div>
    </div>
  </nav>
  <div class="sm-09__main">
    <div class="sm-09__heading">Dashboard</div>
    <div class="sm-09__sub">Neumorphic UI using layered <code>box-shadow</code> — extruded hover, inset active state, all driven by CSS transitions alone.</div>
    <div class="sm-09__cards">
      <div class="sm-09__card"><div class="sm-09__card-val">3,091</div><div class="sm-09__card-lbl">Sessions</div></div>
      <div class="sm-09__card"><div class="sm-09__card-val">71%</div><div class="sm-09__card-lbl">Engagement</div></div>
      <div class="sm-09__card"><div class="sm-09__card-val">$6.3k</div><div class="sm-09__card-lbl">Revenue</div></div>
      <div class="sm-09__card"><div class="sm-09__card-val">521</div><div class="sm-09__card-lbl">Sign-ups</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-09,
.sm-09 *,
.sm-09 *::before,
.sm-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-09 ::selection {
  background: #6366f1;
  color: #fff;
}

.sm-09 {
  --bg: #1a1a2e;
  --bg-neu: #1e1e35;
  --bg-dark: #16162a;
  --accent: #818cf8;
  --accent2: #c084fc;
  --text: #e2e8f0;
  --muted: #64748b;
  --font: 'Poppins', system-ui, sans-serif;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  border-radius: 12px;
  overflow: hidden;
}
/* Neumorphic sidebar */

.sm-09__nav {
  width: 220px;
  background: var(--bg-neu);
  /* Neu shadow — extruded outward */
  box-shadow: inset 2px 2px 6px rgba(255,255,255,0.04), inset -2px -2px 8px rgba(0,0,0,0.4);
  display: flex;
  flex-direction: column;
  padding: 22px 0;
  flex-shrink: 0;
}

.sm-09__brand {
  padding: 0 18px 18px;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  gap: 12px;
}
/* Neumorphic logo */

.sm-09__logo {
  width: 38px;
  height: 38px;
  background: var(--bg-neu);
  border-radius: 11px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 16px;
  background: linear-gradient(145deg, #24243e, #181828);
  box-shadow: 4px 4px 10px rgba(0,0,0,0.5), -2px -2px 8px rgba(255,255,255,0.05);
  color: var(--accent);
}

.sm-09__brand-name {
  font-size: 14px;
  font-weight: 700;
}

.sm-09__links {
  flex: 1;
  padding: 0 10px;
}

.sm-09__link {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 11px 14px;
  border-radius: 12px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  margin-bottom: 6px;
  transition: color 0.2s, box-shadow 0.2s, background 0.2s;
  background: transparent;
  /* resting state — flat */
  box-shadow: none;
}
/* Hover: extruded */

.sm-09__link:hover {
  color: var(--text);
  background: var(--bg-neu);
  box-shadow: 3px 3px 8px rgba(0,0,0,0.5), -2px -2px 6px rgba(255,255,255,0.04);
}
/* Active: pressed/inset */

.sm-09__link--active {
  color: var(--accent);
  background: var(--bg-dark);
  box-shadow: inset 3px 3px 8px rgba(0,0,0,0.6), inset -2px -2px 6px rgba(255,255,255,0.04);
}

.sm-09__link-icon {
  font-size: 16px;
}

.sm-09__link-text {
  flex: 1;
}

.sm-09__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 8px var(--accent);
  opacity: 0;
  transition: opacity 0.2s;
}

.sm-09__link--active .sm-09__dot {
  opacity: 1;
}
/* Neu divider */

.sm-09__divider {
  height: 1px;
  margin: 8px 10px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.06), transparent);
}
/* User card at bottom — neu inset card */

.sm-09__user-card {
  margin: 8px 10px 0;
  padding: 14px;
  border-radius: 14px;
  background: var(--bg-dark);
  box-shadow: inset 3px 3px 8px rgba(0,0,0,0.5), inset -2px -2px 6px rgba(255,255,255,0.04);
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-09__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  box-shadow: 3px 3px 8px rgba(0,0,0,0.5);
  flex-shrink: 0;
}

.sm-09__uname {
  font-size: 12px;
  font-weight: 700;
}

.sm-09__urole {
  font-size: 10px;
  color: var(--muted);
}
/* Main */

.sm-09__main {
  flex: 1;
  padding: 22px;
}

.sm-09__heading {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 6px;
}

.sm-09__sub {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 20px;
}
/* Neu stat cards */

.sm-09__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.sm-09__card {
  padding: 16px;
  border-radius: 14px;
  background: var(--bg-neu);
  box-shadow: 4px 4px 12px rgba(0,0,0,0.5), -2px -2px 8px rgba(255,255,255,0.04);
}

.sm-09__card-val {
  font-size: 22px;
  font-weight: 700;
  color: var(--accent);
}

.sm-09__card-lbl {
  font-size: 11px;
  color: var(--muted);
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-09__link {
    transition: none;
  }
}
```
