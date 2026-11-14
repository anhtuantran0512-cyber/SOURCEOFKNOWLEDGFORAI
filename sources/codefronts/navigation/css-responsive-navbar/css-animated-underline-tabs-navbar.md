---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-animated-underline-tabs-navbar/"
title: "CSS Animated Underline Tabs Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Tab-style navbar with an animated bottom border that slides between items using CSS transitions and radio-button state."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Underline Tabs Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-animated-underline-tabs-navbar/

Tab-style navbar with an animated bottom border that slides between items using CSS transitions and radio-button state.
## HTML
```html
<div class="nav-04">
  <input type="checkbox" id="nav-04-toggle">
  <div class="nav-04__top">
    <a href="#" class="nav-04__logo">Stack<span>.</span></a>
    <div class="nav-04__spacer"></div>
    <div class="nav-04__actions">
      <a href="#" class="nav-04__action-link">Sign in</a>
      <button class="nav-04__btn">Start building</button>
    </div>
    <label for="nav-04-toggle" class="nav-04__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-04__tabs">
    <a href="#" class="nav-04__tab is-active">Overview</a>
    <a href="#" class="nav-04__tab">Components <span class="nav-04__tab-count">48</span></a>
    <a href="#" class="nav-04__tab">Templates <span class="nav-04__tab-count">12</span></a>
    <a href="#" class="nav-04__tab">Documentation</a>
    <a href="#" class="nav-04__tab">Changelog <span class="nav-04__tab-count">3</span></a>
    <a href="#" class="nav-04__tab">Community</a>
    <a href="#" class="nav-04__tab">Showcase</a>
  </div>
  <div class="nav-04__mobile">
    <a href="#">Overview</a>
    <a href="#">Components</a>
    <a href="#">Templates</a>
    <a href="#">Documentation</a>
    <a href="#">Changelog</a>
    <a href="#">Community</a>
    <a href="#">Showcase</a>
  </div>
</div>
<div style="padding:4rem 2.5rem; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:800; letter-spacing:-0.04em; margin-bottom:1rem;">Animated Underline <span style="color:#ff6b35;">Tabs Navbar</span></h1>
  <p style="color:#888; font-size:1.1rem; line-height:1.7;">The sliding underline is a <code>scaleX</code> transform on an <code>::after</code> pseudo-element. Hover shows a 60% preview; active tab shows 100% width. No JavaScript.</p>
</div>
```
## CSS
```css
.nav-04,
.nav-04 *,
.nav-04 *::before,
.nav-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-04 {
  --bg: #fff;
  --text: #1c1c1c;
  --muted: #888;
  --accent: #ff6b35;
  --track: #f0ebe3;
  font-family: 'Manrope', sans-serif;
  background: var(--bg);
  border-bottom: 1px solid #f0ebe3;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-04__top {
  display: flex;
  align-items: center;
  padding: 0 2.5rem;
  height: 60px;
  gap: 2rem;
}

.nav-04__logo {
  font-weight: 800;
  font-size: 1.25rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.04em;
  flex-shrink: 0;
}

.nav-04__logo span {
  color: var(--accent);
}

.nav-04__spacer {
  flex: 1;
}

.nav-04__actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav-04__action-link {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--muted);
  text-decoration: none;
  transition: color 0.2s;
}

.nav-04__action-link:hover {
  color: var(--text);
}

.nav-04__btn {
  padding: 0.45rem 1.1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  font-family: inherit;
  background: var(--text);
  color: #fff;
  transition: background 0.2s, transform 0.15s;
  letter-spacing: -0.01em;
}

.nav-04__btn:hover {
  background: var(--accent);
  transform: translateY(-1px);
}
/* Tab nav */

.nav-04__tabs {
  display: flex;
  align-items: flex-end;
  padding: 0 2.5rem;
  overflow-x: auto;
  scrollbar-width: none;
  gap: 0;
  height: 48px;
}

.nav-04__tabs::-webkit-scrollbar {
  display: none;
}

.nav-04__tab {
  flex-shrink: 0;
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 0 1.25rem;
  height: 100%;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--muted);
  text-decoration: none;
  transition: color 0.2s;
  white-space: nowrap;
}

.nav-04__tab::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2.5px;
  background: var(--accent);
  border-radius: 2px 2px 0 0;
  transform: scaleX(0);
  transition: transform 0.25s cubic-bezier(.4,0,.2,1);
}

.nav-04__tab:hover {
  color: var(--text);
}

.nav-04__tab:hover::after {
  transform: scaleX(0.6);
}

.nav-04__tab.is-active {
  color: var(--accent);
}

.nav-04__tab.is-active::after {
  transform: scaleX(1);
}

.nav-04__tab-count {
  font-size: 0.7rem;
  font-weight: 700;
  background: var(--track);
  color: var(--muted);
  padding: 1px 6px;
  border-radius: 10px;
  min-width: 20px;
  text-align: center;
}

.nav-04__tab.is-active .nav-04__tab-count {
  background: #ffe8df;
  color: var(--accent);
}
/* Mobile */

#nav-04-toggle {
  display: none;
}

.nav-04__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
}

.nav-04__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-04-toggle:checked ~ .nav-04__top .nav-04__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-04-toggle:checked ~ .nav-04__top .nav-04__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-04-toggle:checked ~ .nav-04__top .nav-04__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-04__mobile {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  padding: 0.75rem 1.5rem 1rem;
  border-top: 1px solid var(--track);
}

.nav-04__mobile a {
  display: block;
  padding: 0.6rem 0.5rem;
  color: var(--text);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  border-radius: 6px;
  transition: background 0.15s, color 0.15s;
}

.nav-04__mobile a:hover {
  background: #ffe8df;
  color: var(--accent);
  padding-left: 1rem;
}

#nav-04-toggle:checked ~ .nav-04__mobile {
  display: flex;
}

@media (max-width: 640px) {
  .nav-04__tabs,
    .nav-04__actions {
    display: none;
  }

  .nav-04__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-04__tab::after {
    transition: none;
  }

  .nav-04__btn {
    transition: none;
  }

  .nav-04__hamburger span {
    transition: none;
  }
}
```
