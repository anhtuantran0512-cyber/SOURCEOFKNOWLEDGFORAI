---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-horizontal-navigation-bar-with-hover-underline/"
title: "CSS Horizontal Navigation Bar with Hover Underline"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A clean, professional horizontal navigation bar featuring smooth animated underline indicators on hover."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Horizontal Navigation Bar with Hover Underline
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-horizontal-navigation-bar-with-hover-underline/

A clean, professional horizontal navigation bar featuring smooth animated underline indicators on hover. Built with CSS custom properties for easy theming, this pattern is the foundation of most website headers — links slide a colored underline in from the left on hover with a cubic-bezier transition.
## HTML
```html
<div class="nav-01">
  <nav class="nav-01__bar" role="navigation" aria-label="Main navigation">
    <div class="nav-01__logo">
      <span class="nav-01__logo-dot"></span>Clarity
    </div>
    <ul class="nav-01__links">
      <li><a href="#" class="nav-01__active" aria-current="page">Home</a></li>
      <li><a href="#">Products</a></li>
      <li><a href="#">Features</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Blog</a></li>
      <li><a href="#">About</a></li>
    </ul>
    <div class="nav-01__actions">
      <a href="#" class="nav-01__btn-ghost">Sign in</a>
      <a href="#" class="nav-01__btn-primary">Get started</a>
    </div>
  </nav>
  <div class="nav-01__hero">
    <span class="nav-01__badge">Pure CSS underline effect</span>
    <h1>Hover the nav links above</h1>
    <p>Each link reveals a smooth underline indicator using a CSS <code>::after</code> pseudo-element scaled from zero via <code>cubic-bezier</code> spring easing — no JavaScript.</p>
    <div class="nav-01__note">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
      The underline uses <code>transform: scaleX()</code> — a compositor-only property — so hover transitions run at 60 fps even on low-end devices.
    </div>
  </div>
</div>
```
## CSS
```css
.nav-01,
.nav-01 *,
.nav-01 *::before,
.nav-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-01 ::selection {
  background: #2563eb;
  color: #fff;
}

.nav-01 {
  --bg: #f8fafc;
  --surface: #ffffff;
  --border: #e2e8f0;
  --text: #1e293b;
  --muted: #64748b;
  --accent: #2563eb;
  --accent-light: #dbeafe;
  font-family: 'Inter',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.nav-01__bar {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 10;
  box-shadow: 0 1px 3px rgba(0,0,0,.04);
}

.nav-01__logo {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text);
  letter-spacing: -.02em;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-01__logo-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  display: inline-block;
}

.nav-01__links {
  display: flex;
  align-items: center;
  gap: 4px;
  list-style: none;
}

.nav-01__links a {
  display: flex;
  align-items: center;
  padding: 8px 14px;
  color: var(--muted);
  text-decoration: none;
  font-size: .875rem;
  font-weight: 500;
  border-radius: 6px;
  position: relative;
  transition: color .2s ease;
}

.nav-01__links a::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 14px;
  right: 14px;
  height: 2px;
  background: var(--accent);
  border-radius: 1px;
  transform: scaleX(0);
  transform-origin: center;
  transition: transform .25s cubic-bezier(.34,1.56,.64,1);
}

.nav-01__links a:hover {
  color: var(--text);
}

.nav-01__links a:hover::after,
.nav-01__links a.nav-01__active::after {
  transform: scaleX(1);
}

.nav-01__links a.nav-01__active {
  color: var(--text);
}

.nav-01__actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-01__btn-ghost {
  padding: 7px 16px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: transparent;
  color: var(--text);
  font-size: .875rem;
  font-weight: 500;
  cursor: pointer;
  transition: background .18s,border-color .18s;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
}

.nav-01__btn-ghost:hover {
  background: var(--bg);
  border-color: #cbd5e1;
}

.nav-01__btn-primary {
  padding: 7px 16px;
  border: 1px solid var(--accent);
  border-radius: 6px;
  background: var(--accent);
  color: #fff;
  font-size: .875rem;
  font-weight: 500;
  cursor: pointer;
  transition: opacity .18s;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
}

.nav-01__btn-primary:hover {
  opacity: .88;
}

.nav-01__hero {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 24px;
  text-align: center;
}

.nav-01__badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--accent-light);
  color: var(--accent);
  padding: 4px 12px;
  border-radius: 100px;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
  margin-bottom: 24px;
}

.nav-01__hero h1 {
  font-size: clamp(2rem,5vw,3.5rem);
  font-weight: 600;
  color: var(--text);
  letter-spacing: -.03em;
  line-height: 1.15;
  max-width: 640px;
  margin-bottom: 16px;
}

.nav-01__hero p {
  font-size: 1.0625rem;
  color: var(--muted);
  max-width: 480px;
  line-height: 1.65;
}

.nav-01__note {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 18px;
  margin-top: 40px;
  max-width: 480px;
  font-size: .8125rem;
  color: var(--muted);
  line-height: 1.5;
  text-align: left;
}

.nav-01__note svg {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  margin-top: 1px;
  color: var(--accent);
}

code {
  background: #f1f5f9;
  padding: 1px 5px;
  border-radius: 3px;
  font-family: monospace;
  font-size: .85em;
}

@media (max-width: 600px) {
  .nav-01__links,
    .nav-01__btn-ghost {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-01__links a::after,
    .nav-01__links a {
    transition: none;
  }
}
```
