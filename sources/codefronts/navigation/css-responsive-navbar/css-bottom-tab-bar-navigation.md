---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-bottom-tab-bar-navigation/"
title: "CSS Bottom Tab Bar Navigation"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Mobile-first fixed bottom tab bar with icon + label layout, active fill highlight, and animated indicator dot."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Bottom Tab Bar Navigation
Source: https://codefronts.com/navigation/css-responsive-navbar/css-bottom-tab-bar-navigation/

Mobile-first fixed bottom tab bar with icon + label layout, active fill highlight, and animated indicator dot.
## HTML
```html
<div class="nav-10">
  <div class="nav-10__desktop">
    <a href="#" class="nav-10__logo">Pulse<span>.</span></a>
    <ul class="nav-10__desktop-links">
      <li><a href="#" class="is-active">🏠 Home</a></li>
      <li><a href="#">📊 Analytics</a></li>
      <li><a href="#">💬 Messages</a></li>
      <li><a href="#">📁 Files</a></li>
      <li><a href="#">👤 Profile</a></li>
    </ul>
    <div class="nav-10__desktop-actions">
      <button class="nav-10__desktop-btn">Upgrade plan</button>
    </div>
  </div>
  <div class="nav-10__tab-bar">
    <ul class="nav-10__tabs">
      <li>
        <a href="#" class="nav-10__tab is-active">
          <div class="nav-10__tab-icon">🏠</div>
          Home
        </a>
      </li>
      <li>
        <a href="#" class="nav-10__tab">
          <div class="nav-10__tab-icon">📊</div>
          <span class="nav-10__tab-badge">2</span>
          Stats
        </a>
      </li>
      <li>
        <a href="#" class="nav-10__tab nav-10__tab--fab">
          <div class="nav-10__tab-icon">＋</div>
          New
        </a>
      </li>
      <li>
        <a href="#" class="nav-10__tab">
          <div class="nav-10__tab-icon">💬</div>
          <span class="nav-10__tab-badge">5</span>
          Chat
        </a>
      </li>
      <li>
        <a href="#" class="nav-10__tab">
          <div class="nav-10__tab-icon">👤</div>
          Profile
        </a>
      </li>
    </ul>
  </div>
  <div class="nav-10__content">
    <h1 style="font-size:2.5rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:1rem; color:#1e1b4b;">Bottom Tab Bar Navigation</h1>
    <p style="color:#6b7280; font-size:1.1rem; line-height:1.7; max-width:600px;">On desktop you see a standard horizontal navbar. Resize below 768px to see the iOS-style bottom tab bar with a floating action button in the center. The FAB uses a negative <code>translateY</code> to lift above the bar.</p>
  </div>
</div>
```
## CSS
```css
.nav-10,
.nav-10 *,
.nav-10 *::before,
.nav-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-10 {
  --bg: #fff;
  --text: #1e1b4b;
  --muted: #9ca3af;
  --accent: #6366f1;
  --accent-light: #eef2ff;
  font-family: 'Nunito', sans-serif;
}
/* Top desktop nav */

.nav-10__desktop {
  background: var(--bg);
  border-bottom: 1px solid #e5e7eb;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  height: 64px;
  gap: 2rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.nav-10__logo {
  font-weight: 800;
  font-size: 1.2rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.nav-10__logo span {
  color: var(--accent);
}

.nav-10__desktop-links {
  display: flex;
  list-style: none;
  gap: 0;
  flex: 1;
}

.nav-10__desktop-links a {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.5rem 0.9rem;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}

.nav-10__desktop-links a:hover {
  background: var(--accent-light);
  color: var(--accent);
}

.nav-10__desktop-links a.is-active {
  color: var(--accent);
  background: var(--accent-light);
}

.nav-10__desktop-actions {
  margin-left: auto;
  display: flex;
  gap: 0.75rem;
}

.nav-10__desktop-btn {
  padding: 0.45rem 1.1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  font-family: inherit;
  background: var(--accent);
  color: #fff;
  transition: background 0.2s, transform 0.15s;
}

.nav-10__desktop-btn:hover {
  background: #4f46e5;
  transform: translateY(-1px);
}
/* Bottom tab bar */

.nav-10__tab-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--bg);
  border-top: 1px solid #e5e7eb;
  display: none;
  padding: 0 0.5rem;
  padding-bottom: env(safe-area-inset-bottom, 0);
  z-index: 200;
  box-shadow: 0 -4px 20px rgba(0,0,0,0.07);
}

.nav-10__tabs {
  display: flex;
  list-style: none;
  height: 60px;
}

.nav-10__tabs li {
  flex: 1;
}

.nav-10__tab {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  height: 100%;
  text-decoration: none;
  color: var(--muted);
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  border-radius: 8px;
  transition: color 0.2s;
  position: relative;
}

.nav-10__tab-icon {
  font-size: 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 28px;
  border-radius: 999px;
  transition: background 0.2s, transform 0.2s;
}

.nav-10__tab:hover {
  color: var(--text);
}

.nav-10__tab:hover .nav-10__tab-icon {
  background: #f3f4f6;
}

.nav-10__tab.is-active {
  color: var(--accent);
}

.nav-10__tab.is-active .nav-10__tab-icon {
  background: var(--accent-light);
  transform: translateY(-2px);
}

.nav-10__tab-badge {
  position: absolute;
  top: 8px;
  right: calc(50% - 22px);
  background: #ef4444;
  color: #fff;
  font-size: 0.55rem;
  font-weight: 800;
  padding: 1px 5px;
  border-radius: 999px;
  min-width: 16px;
  text-align: center;
  border: 2px solid var(--bg);
}
/* Center FAB tab */

.nav-10__tab--fab .nav-10__tab-icon {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  font-size: 1.4rem;
  width: 44px;
  height: 40px;
  border-radius: 14px;
  box-shadow: 0 4px 12px rgba(99,102,241,0.45);
  transform: translateY(-8px);
}

.nav-10__tab--fab {
  color: var(--accent);
}

.nav-10__tab--fab:hover .nav-10__tab-icon {
  transform: translateY(-10px) scale(1.05);
}

.nav-10__content {
  padding: 2rem;
}

@media (max-width: 768px) {
  .nav-10__desktop {
    display: none;
  }

  .nav-10__tab-bar {
    display: block;
  }

  .nav-10__content {
    padding-bottom: 80px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-10__tab-icon,
    .nav-10__tab {
    transition: none;
  }

  .nav-10__desktop-btn {
    transition: none;
  }
}
```
