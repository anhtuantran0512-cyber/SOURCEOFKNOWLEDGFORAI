---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-icon-dot-indicator-navbar/"
title: "CSS Icon Dot Indicator Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Clean minimal navbar where the active link is marked by an animated accent dot appearing below the text."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Icon Dot Indicator Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-icon-dot-indicator-navbar/

Clean minimal navbar where the active link is marked by an animated accent dot appearing below the text.
## HTML
```html
<div class="nav-13">
  <div class="nav-13__bar">
    <a href="#" class="nav-13__logo">
      <div class="nav-13__logo-dot"></div>
      Orbit
    </a>
    <div class="nav-13__sep"></div>
    <ul class="nav-13__links">
      <li>
        <a href="#" class="is-active">
          <span class="nav-13__icon">🏠</span>
          <span class="nav-13__label">Home</span>
        </a>
        <div class="nav-13__dot-ind"></div>
      </li>
      <li>
        <a href="#">
          <span class="nav-13__icon">🔍</span>
          <span class="nav-13__label">Explore</span>
        </a>
        <div class="nav-13__dot-ind"></div>
      </li>
      <li style="position:relative">
        <a href="#">
          <span class="nav-13__icon">🔔</span>
          <span class="nav-13__label">Alerts</span>
        </a>
        <div class="nav-13__badge"></div>
        <div class="nav-13__dot-ind"></div>
      </li>
      <li>
        <a href="#">
          <span class="nav-13__icon">💎</span>
          <span class="nav-13__label">Premium</span>
        </a>
        <div class="nav-13__dot-ind"></div>
      </li>
      <li>
        <a href="#">
          <span class="nav-13__icon">👤</span>
          <span class="nav-13__label">Profile</span>
        </a>
        <div class="nav-13__dot-ind"></div>
      </li>
    </ul>
    <div class="nav-13__sep"></div>
    <button class="nav-13__action">Upgrade</button>
  </div>
</div>
<input type="checkbox" id="nav-13-toggle">
<div class="nav-13__mobile-bar">
  <a href="#" class="nav-13__mobile-logo">
    <div class="nav-13__logo-dot"></div>
    Orbit
  </a>
  <label for="nav-13-toggle" class="nav-13__hamburger" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </label>
</div>
<div class="nav-13__mobile-menu">
  <a href="#">🏠 Home</a>
  <a href="#">🔍 Explore</a>
  <a href="#">🔔 Alerts</a>
  <a href="#">💎 Premium</a>
  <a href="#">👤 Profile</a>
</div>
<div style="padding:4rem 2rem; color:#f0e6ff; max-width:700px; margin:0 auto; text-align:center;">
  <h1 style="font-size:2.5rem; font-weight:700; letter-spacing:-0.03em; margin-bottom:1rem;">Icon + Dot Indicator Navbar</h1>
  <p style="color:rgba(240,230,255,0.5); font-size:1rem; line-height:1.7; font-family:'Poppins',sans-serif;">Each icon tab shows a label below it. The active indicator is a small glowing dot beneath the active item, controlled by <code>:has(a.is-active)</code>. Notification badge uses a positioned dot.</p>
</div>
```
## CSS
```css
.nav-13,
.nav-13 *,
.nav-13 *::before,
.nav-13 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-13 {
  --bg: rgba(20,8,40,0.85);
  --border: rgba(255,255,255,0.08);
  --text: #f0e6ff;
  --muted: rgba(240,230,255,0.4);
  --accent: #d946ef;
  --accent-glow: rgba(217,70,239,0.35);
  font-family: 'Poppins', sans-serif;
  display: flex;
  justify-content: center;
  padding: 1.5rem 1rem;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-13__bar {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 0.75rem 1.25rem;
  backdrop-filter: blur(20px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
}

.nav-13__logo {
  font-weight: 700;
  font-size: 1rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.01em;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-13__logo-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 8px var(--accent-glow);
}

.nav-13__sep {
  width: 1px;
  height: 24px;
  background: var(--border);
}

.nav-13__links {
  display: flex;
  list-style: none;
  gap: 0.25rem;
}

.nav-13__links li {
  position: relative;
}

.nav-13__links a {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  text-decoration: none;
  padding: 0.4rem 0.85rem;
  border-radius: 12px;
  transition: background 0.2s;
  min-width: 56px;
}

.nav-13__links a:hover {
  background: rgba(255,255,255,0.05);
}

.nav-13__icon {
  font-size: 1.1rem;
  line-height: 1;
}

.nav-13__label {
  font-size: 0.6rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--muted);
  transition: color 0.2s;
}

.nav-13__links a:hover .nav-13__label {
  color: var(--text);
}

.nav-13__links a.is-active {
  background: rgba(217,70,239,0.12);
}

.nav-13__links a.is-active .nav-13__label {
  color: var(--accent);
}

.nav-13__dot-ind {
  position: absolute;
  bottom: 2px;
  left: 50%;
  transform: translateX(-50%);
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 6px var(--accent-glow);
  opacity: 0;
  transition: opacity 0.2s;
}

.nav-13__links a.is-active + .nav-13__dot-ind,
.nav-13__links li:has(a.is-active) .nav-13__dot-ind {
  opacity: 1;
}
/* notif badge */

.nav-13__badge {
  position: absolute;
  top: 4px;
  right: 8px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #f43f5e;
  border: 2px solid #14082808;
}

.nav-13__action {
  padding: 0.5rem 1.1rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  font-family: inherit;
  background: linear-gradient(135deg, #d946ef, #9333ea);
  color: #fff;
  box-shadow: 0 2px 12px var(--accent-glow);
  transition: opacity 0.2s, transform 0.15s;
  white-space: nowrap;
}

.nav-13__action:hover {
  opacity: 0.85;
  transform: scale(0.97);
}
/* Mobile */

#nav-13-toggle {
  display: none;
}

.nav-13__mobile-bar {
  display: none;
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(20,8,40,0.9);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 0 1.5rem;
  height: 60px;
  align-items: center;
  justify-content: space-between;
}

.nav-13__mobile-logo {
  font-weight: 700;
  font-size: 1rem;
  color: var(--text);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-13__hamburger {
  display: flex;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  border: none;
  background: transparent;
  padding: 8px;
}

.nav-13__hamburger span {
  display: block;
  width: 20px;
  height: 1.5px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-13-toggle:checked ~ .nav-13__mobile-bar .nav-13__hamburger span:nth-child(1) {
  transform: translateY(6.5px) rotate(45deg);
}

#nav-13-toggle:checked ~ .nav-13__mobile-bar .nav-13__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-13-toggle:checked ~ .nav-13__mobile-bar .nav-13__hamburger span:nth-child(3) {
  transform: translateY(-6.5px) rotate(-45deg);
}

.nav-13__mobile-menu {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  background: rgba(20,8,40,0.97);
  backdrop-filter: blur(20px);
  padding: 0.75rem 1.25rem 1rem;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 60px;
  z-index: 99;
}

.nav-13__mobile-menu a {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.65rem 0.75rem;
  border-radius: 10px;
  transition: background 0.15s, color 0.15s;
}

.nav-13__mobile-menu a:hover {
  background: rgba(255,255,255,0.05);
  color: var(--text);
}

#nav-13-toggle:checked ~ .nav-13__mobile-menu {
  display: flex;
}

@media (max-width: 640px) {
  .nav-13 {
    display: none;
  }

  .nav-13__mobile-bar {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-13__links a,
    .nav-13__action,
    .nav-13__dot-ind {
    transition: none;
  }

  .nav-13__hamburger span {
    transition: none;
  }
}
```
