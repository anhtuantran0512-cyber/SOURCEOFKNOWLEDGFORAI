---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-mega-menu-dropdown-navbar/"
title: "CSS Mega Menu Dropdown Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Full-width mega menu with multi-column layout, icon cards, and a featured highlight panel triggered by CSS focus-within."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Mega Menu Dropdown Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-mega-menu-dropdown-navbar/

Full-width mega menu with multi-column layout, icon cards, and a featured highlight panel triggered by CSS focus-within.
## HTML
```html
<div class="nav-02">
  <input type="checkbox" id="nav-02-toggle">
  <div class="nav-02__inner">
    <a href="#" class="nav-02__logo">Nova<span>.</span></a>
    <ul class="nav-02__menu">
      <li class="nav-02__item">
        <a href="#">Products</a>
        <div class="nav-02__mega nav-02__mega--grid nav-02__mega--wide">
          <div>
            <div class="nav-02__mega-col-title">Core tools</div>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">🎨</div><div><div class="nav-02__mega-title">Design Studio</div><div class="nav-02__mega-desc">Create pixel-perfect interfaces</div></div></a>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">⚡</div><div><div class="nav-02__mega-title">Prototyping</div><div class="nav-02__mega-desc">Interactive mockups in minutes</div></div></a>
          </div>
          <div>
            <div class="nav-02__mega-col-title">Collaboration</div>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">👥</div><div><div class="nav-02__mega-title">Teams</div><div class="nav-02__mega-desc">Real-time multiplayer editing</div></div></a>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">💬</div><div><div class="nav-02__mega-title">Comments</div><div class="nav-02__mega-desc">Contextual feedback flows</div></div></a>
          </div>
          <div>
            <div class="nav-02__mega-col-title">Integrations</div>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">🔌</div><div><div class="nav-02__mega-title">Plugins</div><div class="nav-02__mega-desc">500+ community extensions</div></div></a>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">🔗</div><div><div class="nav-02__mega-title">API</div><div class="nav-02__mega-desc">Build on top of Nova</div></div></a>
          </div>
        </div>
      </li>
      <li class="nav-02__item">
        <a href="#">Solutions</a>
        <div class="nav-02__mega nav-02__mega--grid">
          <div>
            <div class="nav-02__mega-col-title">By team</div>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">🏢</div><div><div class="nav-02__mega-title">Enterprise</div><div class="nav-02__mega-desc">Advanced security & compliance</div></div></a>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">🚀</div><div><div class="nav-02__mega-title">Startups</div><div class="nav-02__mega-desc">Move fast, ship beautiful</div></div></a>
          </div>
          <div>
            <div class="nav-02__mega-col-title">By role</div>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">✏️</div><div><div class="nav-02__mega-title">Designers</div><div class="nav-02__mega-desc">Your complete design OS</div></div></a>
            <a href="#" class="nav-02__mega-link"><div class="nav-02__mega-icon">💻</div><div><div class="nav-02__mega-title">Developers</div><div class="nav-02__mega-desc">Inspect & export production code</div></div></a>
          </div>
        </div>
      </li>
      <li class="nav-02__item nav-02__item--plain"><a href="#">Pricing</a></li>
      <li class="nav-02__item nav-02__item--plain"><a href="#">Blog</a></li>
    </ul>
    <div class="nav-02__cta">
      <button class="nav-02__btn nav-02__btn--ghost">Log in</button>
      <button class="nav-02__btn nav-02__btn--pink">Try for free</button>
    </div>
    <label for="nav-02-toggle" class="nav-02__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-02__drawer">
    <a href="#">Products</a>
    <a href="#">Solutions</a>
    <a href="#">Pricing</a>
    <a href="#">Blog</a>
    <a href="#">Log in</a>
    <a href="#" style="color:#e84393;">Try for free →</a>
  </div>
</div>
<div style="padding:4rem 2rem; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:700; letter-spacing:-0.03em; margin-bottom:1rem; color:#1a1a2e;">Mega Menu Dropdown Navbar</h1>
  <p style="color:#6b7280; font-size:1.1rem; line-height:1.7;">Hover over Products or Solutions to see the mega menu panels. Pure CSS :hover-driven with grid layout. Resize to see mobile drawer.</p>
</div>
```
## CSS
```css
.nav-02,
.nav-02 *,
.nav-02 *::before,
.nav-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-02 {
  --bg: #ffffff;
  --text: #1a1a2e;
  --muted: #6b7280;
  --accent: #e84393;
  --border: #e5e7eb;
  --mega-bg: #ffffff;
  --icon-bg: #fdf2f8;
  font-family: 'DM Sans', sans-serif;
  position: sticky;
  top: 0;
  z-index: 200;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}

.nav-02__inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  height: 68px;
  gap: 2rem;
}

.nav-02__logo {
  font-weight: 700;
  font-size: 1.3rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.03em;
  flex-shrink: 0;
}

.nav-02__logo span {
  color: var(--accent);
}

.nav-02__menu {
  display: flex;
  list-style: none;
  gap: 0;
  flex: 1;
}

.nav-02__item {
  position: relative;
}

.nav-02__item > a {
  display: flex;
  align-items: center;
  gap: 4px;
  color: var(--text);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
  white-space: nowrap;
}

.nav-02__item > a::after {
  content: '▾';
  font-size: 0.7rem;
  color: var(--muted);
  transition: transform 0.2s;
}

.nav-02__item--plain > a::after {
  display: none;
}

.nav-02__item:hover > a {
  background: #fdf2f8;
  color: var(--accent);
}

.nav-02__item:hover > a::after {
  transform: rotate(180deg);
}
/* Mega menu panel */

.nav-02__mega {
  position: absolute;
  top: calc(100% + 8px);
  left: -1rem;
  background: var(--mega-bg);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 20px 60px rgba(0,0,0,0.12), 0 4px 16px rgba(0,0,0,0.06);
  display: none;
  min-width: 560px;
  gap: 1.5rem;
}

.nav-02__mega--grid {
  display: none;
  grid-template-columns: repeat(2, 1fr);
}

.nav-02__mega--wide {
  min-width: 700px;
  grid-template-columns: repeat(3, 1fr);
}

.nav-02__item:hover .nav-02__mega--grid {
  display: grid;
}

.nav-02__mega-col-title {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 0.75rem;
}

.nav-02__mega-link {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  text-decoration: none;
  padding: 0.6rem 0.75rem;
  border-radius: 10px;
  transition: background 0.15s;
  margin-bottom: 0.25rem;
}

.nav-02__mega-link:hover {
  background: #fdf2f8;
}

.nav-02__mega-icon {
  width: 36px;
  height: 36px;
  background: var(--icon-bg);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
}

.nav-02__mega-link:hover .nav-02__mega-icon {
  background: #fce7f3;
}

.nav-02__mega-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 2px;
}

.nav-02__mega-desc {
  font-size: 0.775rem;
  color: var(--muted);
  line-height: 1.4;
}

.nav-02__spacer {
  flex: 1;
}

.nav-02__cta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
}

.nav-02__btn {
  padding: 0.45rem 1.1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  font-family: inherit;
  transition: all 0.2s;
}

.nav-02__btn--ghost {
  background: transparent;
  color: var(--text);
}

.nav-02__btn--ghost:hover {
  background: #f3f4f6;
}

.nav-02__btn--pink {
  background: var(--accent);
  color: #fff;
}

.nav-02__btn--pink:hover {
  background: #d1236a;
  transform: translateY(-1px);
}
/* Mobile */

#nav-02-toggle {
  display: none;
}

.nav-02__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
  margin-left: auto;
}

.nav-02__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-02-toggle:checked ~ .nav-02__inner .nav-02__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-02-toggle:checked ~ .nav-02__inner .nav-02__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-02-toggle:checked ~ .nav-02__inner .nav-02__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-02__drawer {
  display: none;
  padding: 1rem 1.5rem;
  border-top: 1px solid var(--border);
  flex-direction: column;
  gap: 0.25rem;
}

.nav-02__drawer a {
  display: block;
  padding: 0.65rem 0.5rem;
  color: var(--text);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  border-radius: 8px;
}

.nav-02__drawer a:hover {
  background: #fdf2f8;
  color: var(--accent);
  padding-left: 1rem;
}

#nav-02-toggle:checked ~ .nav-02__drawer {
  display: flex;
}

@media (max-width: 768px) {
  .nav-02__menu,
    .nav-02__cta {
    display: none;
  }

  .nav-02__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-02__btn {
    transition: none;
  }

  .nav-02__hamburger span {
    transition: none;
  }

  .nav-02__drawer a {
    transition: none;
  }
}
```
