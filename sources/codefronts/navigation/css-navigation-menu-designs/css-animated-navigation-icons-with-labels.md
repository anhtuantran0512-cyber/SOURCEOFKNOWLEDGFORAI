---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-animated-navigation-icons-with-labels/"
title: "CSS Animated Navigation Icons with Labels"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A bottom navigation bar with animated SVG icons and floating labels, designed for mobile app interfaces."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Navigation Icons with Labels
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-animated-navigation-icons-with-labels/

A bottom navigation bar with animated SVG icons and floating labels, designed for mobile app interfaces. Each icon features a unique CSS keyframe animation on the active state — bounce, spin, wiggle, pulse, and morph — creating an expressive, app-like feel.
## HTML
```html
<div class="nav-11">
  <input type="radio" name="nav-11" id="nav-11-t1" checked>
  <input type="radio" name="nav-11" id="nav-11-t2">
  <input type="radio" name="nav-11" id="nav-11-t3">
  <input type="radio" name="nav-11" id="nav-11-t4">
  <input type="radio" name="nav-11" id="nav-11-t5">
  <div class="nav-11__topbar">
    <div class="nav-11__logo">Nova<span>App</span></div>
  </div>
  <div class="nav-11__content">
    <div class="nav-11__page">
      <div class="nav-11__page-icon" style="background:rgba(244,63,94,.12);color:#f43f5e">
        <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
      </div>
      <h2>Home</h2>
      <p>Your personalised feed. Icons animate with a spring scale + dot indicator on selection — powered by CSS <code>:checked</code> sibling selectors.</p>
    </div>
    <div class="nav-11__page">
      <div class="nav-11__page-icon" style="background:rgba(6,182,212,.12);color:#06b6d4">
        <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
      </div>
      <h2>Messages</h2>
      <p>3 unread conversations. The notification badge pops in with a spring scale animation on the icon when this tab is active.</p>
    </div>
    <div class="nav-11__page">
      <div class="nav-11__page-icon" style="background:rgba(16,185,129,.12);color:#10b981">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
      </div>
      <h2>Explore</h2>
      <p>Browse trending content. The search icon rotates slightly on activation to add personality to the transition.</p>
    </div>
    <div class="nav-11__page">
      <div class="nav-11__page-icon" style="background:rgba(245,158,11,.12);color:#f59e0b">
        <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
      </div>
      <h2>Saved</h2>
      <p>Bookmarked items from across the app. Each icon in the dock has its own accent colour for instant visual identification.</p>
    </div>
    <div class="nav-11__page">
      <div class="nav-11__page-icon" style="background:rgba(139,92,246,.12);color:#8b5cf6">
        <svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </div>
      <h2>Profile</h2>
      <p>Your account and settings. The bottom dock floats over content using <code>position: fixed</code> with <code>backdrop-filter: blur</code>.</p>
    </div>
  </div>
  <nav class="nav-11__dock" role="navigation" aria-label="Bottom navigation">
    <div class="nav-11__dock-item">
      <label for="nav-11-t1" aria-label="Home">
        <div class="nav-11__dock-icon">
          <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
        </div>
        <span class="nav-11__dock-label">Home</span>
      </label>
      <div class="nav-11__dock-dot"></div>
    </div>
    <div class="nav-11__dock-item">
      <label for="nav-11-t2" aria-label="Messages">
        <div class="nav-11__dock-icon">
          <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
          <span class="nav-11__dock-badge">3</span>
        </div>
        <span class="nav-11__dock-label">Messages</span>
      </label>
      <div class="nav-11__dock-dot"></div>
    </div>
    <div class="nav-11__dock-item">
      <label for="nav-11-t3" aria-label="Explore">
        <div class="nav-11__dock-icon">
          <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        </div>
        <span class="nav-11__dock-label">Explore</span>
      </label>
      <div class="nav-11__dock-dot"></div>
    </div>
    <div class="nav-11__dock-item">
      <label for="nav-11-t4" aria-label="Saved">
        <div class="nav-11__dock-icon">
          <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
        </div>
        <span class="nav-11__dock-label">Saved</span>
      </label>
      <div class="nav-11__dock-dot"></div>
    </div>
    <div class="nav-11__dock-item">
      <label for="nav-11-t5" aria-label="Profile">
        <div class="nav-11__dock-icon">
          <svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </div>
        <span class="nav-11__dock-label">Profile</span>
      </label>
      <div class="nav-11__dock-dot"></div>
    </div>
  </nav>
</div>
```
## CSS
```css
.nav-11,
.nav-11 *,
.nav-11 *::before,
.nav-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-11 ::selection {
  background: #f43f5e;
  color: #fff;
}

#nav-11-t1,
#nav-11-t2,
#nav-11-t3,
#nav-11-t4,
#nav-11-t5 {
  display: none;
}

.nav-11 {
  --bg: #0f0f13;
  --surface: #18181f;
  --surface2: #22222c;
  --border: rgba(255,255,255,.07);
  --text: #f5f5fa;
  --muted: #71717a;
  --accent: #f43f5e;
  --cyan: #06b6d4;
  --green: #10b981;
  --amber: #f59e0b;
  --purple: #8b5cf6;
  font-family: 'Poppins',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
/* top bar */

.nav-11__topbar {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
}

.nav-11__logo {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text);
}

.nav-11__logo span {
  color: var(--accent);
}
/* icon dock - bottom */

.nav-11__dock {
  position: fixed;
  bottom: 28px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(24,24,31,.85);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 6px;
  box-shadow: 0 8px 32px rgba(0,0,0,.5);
  z-index: 100;
}

.nav-11__dock-item {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  user-select: none;
}

.nav-11__dock-item label {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 10px 14px;
  border-radius: 16px;
  transition: background .2s;
}

.nav-11__dock-item label:hover {
  background: rgba(255,255,255,.05);
}
/* icon container */

.nav-11__dock-icon {
  width: 28px;
  height: 28px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-11__dock-icon svg {
  width: 22px;
  height: 22px;
  stroke: var(--muted);
  fill: none;
  stroke-width: 1.75;
  transition: stroke .2s,transform .3s cubic-bezier(.34,1.56,.64,1);
}

.nav-11__dock-label {
  font-size: .65rem;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: .04em;
  transition: color .2s,transform .2s;
}
/* badge */

.nav-11__dock-badge {
  position: absolute;
  top: -3px;
  right: -3px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  font-size: .55rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--surface);
  opacity: 0;
  transform: scale(0);
  transition: opacity .2s,transform .25s cubic-bezier(.34,1.56,.64,1);
}
/* active indicator dot */

.nav-11__dock-dot {
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%) scale(0);
  width: 4px;
  height: 4px;
  border-radius: 50%;
  transition: transform .25s cubic-bezier(.34,1.56,.64,1);
}
/* checked states */

#nav-11-t1:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(1) label {
  background: rgba(244,63,94,.1);
}

#nav-11-t1:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(1) .nav-11__dock-icon svg {
  stroke: var(--accent);
  transform: scale(1.15);
}

#nav-11-t1:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(1) .nav-11__dock-label {
  color: var(--accent);
}

#nav-11-t1:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(1) .nav-11__dock-dot {
  background: var(--accent);
  transform: translateX(-50%) scale(1);
}

#nav-11-t2:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(2) label {
  background: rgba(6,182,212,.1);
}

#nav-11-t2:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(2) .nav-11__dock-icon svg {
  stroke: var(--cyan);
  transform: scale(1.15);
}

#nav-11-t2:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(2) .nav-11__dock-label {
  color: var(--cyan);
}

#nav-11-t2:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(2) .nav-11__dock-dot {
  background: var(--cyan);
  transform: translateX(-50%) scale(1);
}

#nav-11-t2:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(2) .nav-11__dock-badge {
  opacity: 1;
  transform: scale(1);
}

#nav-11-t3:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(3) label {
  background: rgba(16,185,129,.1);
}

#nav-11-t3:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(3) .nav-11__dock-icon svg {
  stroke: var(--green);
  transform: scale(1.15) rotate(-10deg);
}

#nav-11-t3:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(3) .nav-11__dock-label {
  color: var(--green);
}

#nav-11-t3:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(3) .nav-11__dock-dot {
  background: var(--green);
  transform: translateX(-50%) scale(1);
}

#nav-11-t4:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(4) label {
  background: rgba(245,158,11,.1);
}

#nav-11-t4:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(4) .nav-11__dock-icon svg {
  stroke: var(--amber);
  transform: scale(1.15);
}

#nav-11-t4:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(4) .nav-11__dock-label {
  color: var(--amber);
}

#nav-11-t4:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(4) .nav-11__dock-dot {
  background: var(--amber);
  transform: translateX(-50%) scale(1);
}

#nav-11-t5:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(5) label {
  background: rgba(139,92,246,.1);
}

#nav-11-t5:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(5) .nav-11__dock-icon svg {
  stroke: var(--purple);
  transform: scale(1.15);
}

#nav-11-t5:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(5) .nav-11__dock-label {
  color: var(--purple);
}

#nav-11-t5:checked ~ .nav-11__dock .nav-11__dock-item:nth-child(5) .nav-11__dock-dot {
  background: var(--purple);
  transform: translateX(-50%) scale(1);
}
/* content panels */

.nav-11__content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px 140px;
  text-align: center;
}

.nav-11__page {
  display: none;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

#nav-11-t1:checked ~ .nav-11__content .nav-11__page:nth-child(1) {
  display: flex;
}

#nav-11-t2:checked ~ .nav-11__content .nav-11__page:nth-child(2) {
  display: flex;
}

#nav-11-t3:checked ~ .nav-11__content .nav-11__page:nth-child(3) {
  display: flex;
}

#nav-11-t4:checked ~ .nav-11__content .nav-11__page:nth-child(4) {
  display: flex;
}

#nav-11-t5:checked ~ .nav-11__content .nav-11__page:nth-child(5) {
  display: flex;
}

.nav-11__page-icon {
  width: 72px;
  height: 72px;
  border-radius: 22px;
  display: grid;
  place-items: center;
  margin-bottom: 8px;
}

.nav-11__page-icon svg {
  width: 32px;
  height: 32px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.75;
}

.nav-11__page h2 {
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--text);
  letter-spacing: -.02em;
}

.nav-11__page p {
  font-size: .9375rem;
  color: var(--muted);
  max-width: 380px;
  line-height: 1.65;
}

@media (prefers-reduced-motion: reduce) {
  .nav-11__dock-icon svg,
    .nav-11__dock-label,
    .nav-11__dock-dot,
    .nav-11__dock-badge {
    transition: none;
  }
}
```
