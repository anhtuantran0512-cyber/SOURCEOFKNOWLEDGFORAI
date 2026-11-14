---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-dropdown-navigation-menu/"
title: "CSS Dropdown Navigation Menu"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A multi-level dropdown navigation built entirely with CSS using the checkbox hack and `:focus-within` for accessibility."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dropdown Navigation Menu
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-dropdown-navigation-menu/

A multi-level dropdown navigation built entirely with CSS using the checkbox hack and `:focus-within` for accessibility. Submenus fade and slide down on hover, with smooth opacity and transform transitions — no JavaScript required.
## HTML
```html
<div class="nav-02">
  <nav class="nav-02__bar" role="navigation">
    <div class="nav-02__logo">
      <span class="nav-02__logo-mark">
        <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      </span>
      Vertex
    </div>
    <ul class="nav-02__links">
      <li>
        <a href="#">Products
          <svg class="nav-02__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </a>
        <ul class="nav-02__dropdown nav-02__dropdown--wide">
          <li>
            <a href="#">
              <span class="nav-02__dropdown-icon"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg></span>
              <span class="nav-02__dropdown-text">Dashboard<span>Analytics & insights</span></span>
            </a>
          </li>
          <li>
            <a href="#">
              <span class="nav-02__dropdown-icon"><svg viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></span>
              <span class="nav-02__dropdown-text">Monitoring<span>Real-time metrics</span></span>
            </a>
          </li>
          <li>
            <a href="#">
              <span class="nav-02__dropdown-icon"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></span>
              <span class="nav-02__dropdown-text">Teams<span>Collaboration tools</span></span>
            </a>
          </li>
          <li>
            <a href="#">
              <span class="nav-02__dropdown-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93l-1.41 1.41M5.34 18.66l-1.41 1.41M20 12h2M2 12H0M19.07 19.07l-1.41-1.41M5.34 5.34L3.93 3.93M12 20v2M12 2v2"/></svg></span>
              <span class="nav-02__dropdown-text">Automation<span>Workflow builder</span></span>
            </a>
          </li>
          <li class="nav-02__dropdown-cta-wrap" style="grid-column:1/-1">
            <a href="#" class="nav-02__dropdown-cta">
              Explore all products →
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </li>
        </ul>
      </li>
      <li>
        <a href="#">Solutions
          <svg class="nav-02__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </a>
        <ul class="nav-02__dropdown">
          <li><a href="#"><span class="nav-02__dropdown-text">Enterprise</span></a></li>
          <li><a href="#"><span class="nav-02__dropdown-text">Startups</span></a></li>
          <li><a href="#"><span class="nav-02__dropdown-text">Agencies</span></a></li>
          <div class="nav-02__dropdown-divider"></div>
          <li><a href="#"><span class="nav-02__dropdown-text">Case Studies</span></a></li>
        </ul>
      </li>
      <li><a href="#">Pricing</a></li>
      <li>
        <a href="#">Resources
          <svg class="nav-02__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </a>
        <ul class="nav-02__dropdown">
          <li><a href="#"><span class="nav-02__dropdown-text">Documentation</span></a></li>
          <li><a href="#"><span class="nav-02__dropdown-text">Blog</span></a></li>
          <li><a href="#"><span class="nav-02__dropdown-text">Community</span></a></li>
        </ul>
      </li>
    </ul>
    <div class="nav-02__actions">
      <a href="#" class="nav-02__btn nav-02__btn--ghost">Log in</a>
      <a href="#" class="nav-02__btn nav-02__btn--fill">Start free</a>
    </div>
  </nav>
  <div class="nav-02__hero">
    <span class="nav-02__pill"><span class="nav-02__pill-dot"></span>Hover any nav item with an arrow</span>
    <h1>CSS Dropdown Navigation Menu</h1>
    <p>Dropdowns appear on <code>:hover</code> using <code>opacity</code> + <code>translateY</code> transitions. Wide panels use CSS Grid. Zero JavaScript required.</p>
  </div>
</div>
```
## CSS
```css
.nav-02,
.nav-02 *,
.nav-02 *::before,
.nav-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-02 ::selection {
  background: #7c3aed;
  color: #fff;
}

.nav-02 {
  --bg: #faf5ff;
  --surface: #ffffff;
  --border: #ede9fe;
  --text: #1e1b4b;
  --muted: #6b7280;
  --accent: #7c3aed;
  --accent2: #a78bfa;
  --shadow: rgba(124,58,237,.12);
  font-family: 'Plus Jakarta Sans',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
}

.nav-02__bar {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 68px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 16px var(--shadow);
}

.nav-02__logo {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text);
  letter-spacing: -.03em;
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-02__logo-mark {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  display: grid;
  place-items: center;
}

.nav-02__logo-mark svg {
  width: 18px;
  height: 18px;
  fill: #fff;
}

.nav-02__links {
  display: flex;
  align-items: center;
  gap: 2px;
  list-style: none;
}
/* top-level item */

.nav-02__links > li {
  position: relative;
}

.nav-02__links > li > a {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 10px 14px;
  color: var(--muted);
  text-decoration: none;
  font-size: .875rem;
  font-weight: 500;
  border-radius: 7px;
  transition: color .18s,background .18s;
  white-space: nowrap;
}

.nav-02__links > li > a:hover,
.nav-02__links > li:hover > a {
  color: var(--text);
  background: var(--bg);
}

.nav-02__links > li > a .nav-02__caret {
  width: 14px;
  height: 14px;
  opacity: .5;
  transition: transform .22s ease;
}

.nav-02__links > li:hover > a .nav-02__caret {
  transform: rotate(180deg);
}
/* dropdown panel */

.nav-02__dropdown {
  position: absolute;
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(-6px);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 12px 40px var(--shadow);
  padding: 8px;
  min-width: 200px;
  list-style: none;
  opacity: 0;
  pointer-events: none;
  transition: opacity .18s ease,transform .2s ease;
  z-index: 200;
}

.nav-02__links > li:hover .nav-02__dropdown,
.nav-02__links > li:focus-within .nav-02__dropdown {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}

.nav-02__dropdown li a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  color: var(--muted);
  text-decoration: none;
  font-size: .875rem;
  font-weight: 500;
  border-radius: 7px;
  transition: background .15s,color .15s;
}

.nav-02__dropdown li a:hover {
  background: var(--bg);
  color: var(--text);
}

.nav-02__dropdown-icon {
  width: 32px;
  height: 32px;
  border-radius: 7px;
  background: var(--bg);
  display: grid;
  place-items: center;
  flex-shrink: 0;
}

.nav-02__dropdown-icon svg {
  width: 16px;
  height: 16px;
  stroke: var(--accent);
  fill: none;
  stroke-width: 2;
}

.nav-02__dropdown-text {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.nav-02__dropdown-text span {
  font-size: .75rem;
  color: var(--accent2);
  font-weight: 400;
}

.nav-02__dropdown-divider {
  height: 1px;
  background: var(--border);
  margin: 6px 8px;
}
/* wide dropdown */

.nav-02__dropdown--wide {
  min-width: 480px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
}
/* cta row */

.nav-02__dropdown-cta {
  grid-column: 1/-1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(135deg,#f5f3ff,#ede9fe);
  border-radius: 8px;
  padding: 12px 14px;
  margin-top: 4px;
  font-size: .8125rem;
  color: var(--accent);
  font-weight: 600;
  text-decoration: none;
}

.nav-02__dropdown-cta:hover {
  background: linear-gradient(135deg,#ede9fe,#ddd6fe);
}

.nav-02__dropdown-cta svg {
  width: 16px;
  height: 16px;
  stroke: var(--accent);
  fill: none;
  stroke-width: 2;
}

.nav-02__actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-02__btn {
  padding: 8px 18px;
  border-radius: 7px;
  font-size: .875rem;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  transition: all .18s;
  border: 1.5px solid;
}

.nav-02__btn--ghost {
  color: var(--accent);
  border-color: var(--border);
  background: transparent;
}

.nav-02__btn--ghost:hover {
  border-color: var(--accent2);
  background: var(--bg);
}

.nav-02__btn--fill {
  color: #fff;
  border-color: var(--accent);
  background: var(--accent);
}

.nav-02__btn--fill:hover {
  opacity: .88;
}
/* hero */

.nav-02__hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 100px 24px;
  text-align: center;
}

.nav-02__hero h1 {
  font-size: clamp(2rem,5vw,3.25rem);
  font-weight: 600;
  color: var(--text);
  letter-spacing: -.03em;
  max-width: 600px;
  margin-bottom: 14px;
  line-height: 1.2;
}

.nav-02__hero p {
  font-size: 1rem;
  color: var(--muted);
  max-width: 440px;
  line-height: 1.65;
}

.nav-02__pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--accent);
  color: #fff;
  border-radius: 100px;
  padding: 4px 12px 4px 6px;
  font-size: .75rem;
  font-weight: 600;
  margin-bottom: 22px;
}

.nav-02__pill-dot {
  width: 18px;
  height: 18px;
  background: rgba(255,255,255,.25);
  border-radius: 50%;
  display: grid;
  place-items: center;
}

.nav-02__pill-dot::after {
  content: '';
  width: 6px;
  height: 6px;
  background: #fff;
  border-radius: 50%;
  display: block;
}

@media (max-width: 700px) {
  .nav-02__links,
    .nav-02__btn--ghost {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-02__dropdown,
    .nav-02__links > li > a .nav-02__caret {
    transition: none;
  }
}
```
