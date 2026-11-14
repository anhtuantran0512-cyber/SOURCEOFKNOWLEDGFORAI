---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-centered-logo-navbar/"
title: "CSS Centered Logo Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Classic agency-style navbar with centered logo, symmetrical link groups left and right, and outlined CTA button."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Centered Logo Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-centered-logo-navbar/

Classic agency-style navbar with centered logo, symmetrical link groups left and right, and outlined CTA button.
## HTML
```html
<div class="nav-12">
  <div class="nav-12__bar">
    <ul class="nav-12__left">
      <li><a href="#" class="is-active">Collections</a></li>
      <li><a href="#">Lookbook</a></li>
      <li><a href="#">Stores</a></li>
    </ul>
    <div class="nav-12__logo-wrap">
      <a href="#" class="nav-12__logo">AURORE</a>
      <span class="nav-12__logo-sub">Paris — since 1924</span>
    </div>
    <ul class="nav-12__right">
      <li><a href="#">About</a></li>
      <li><a href="#">Atelier</a></li>
      <li><a href="#" class="is-cta">Reserve</a></li>
    </ul>
  </div>
  <input type="checkbox" id="nav-12-toggle">
  <div class="nav-12__mobile-bar">
    <a href="#" class="nav-12__mobile-logo">AURORE</a>
    <label for="nav-12-toggle" class="nav-12__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-12__mobile-menu">
    <a href="#">Collections</a>
    <a href="#">Lookbook</a>
    <a href="#">Stores</a>
    <a href="#">About</a>
    <a href="#">Atelier</a>
    <a href="#" style="color:#c4a55a;">Reserve</a>
  </div>
</div>
<div style="padding:4rem 2.5rem; max-width:700px; margin:0 auto; text-align:center;">
  <h1 style="font-family:'Cormorant Garamond',serif; font-size:3rem; font-weight:600; letter-spacing:0.05em; margin-bottom:1rem; color:#1a1612;">Centered Logo Navbar</h1>
  <p style="color:#8c8070; font-size:1.05rem; line-height:1.8;">A luxury brand–style navbar using CSS Grid with <code>1fr auto 1fr</code> columns to perfectly center the logo while allowing left and right link groups to fill equal space.</p>
</div>
```
## CSS
```css
.nav-12,
.nav-12 *,
.nav-12 *::before,
.nav-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-12 {
  --bg: #faf8f5;
  --text: #1a1612;
  --muted: #8c8070;
  --accent: #c4a55a;
  --border: #e8e0d4;
  font-family: 'Jost', sans-serif;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-12__bar {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 0 2.5rem;
  height: 72px;
}

.nav-12__left {
  display: flex;
  align-items: center;
  gap: 0;
  list-style: none;
}

.nav-12__left a {
  color: var(--muted);
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: color 0.2s;
  white-space: nowrap;
}

.nav-12__left a:hover {
  color: var(--text);
}

.nav-12__left a.is-active {
  color: var(--text);
}

.nav-12__logo-wrap {
  text-align: center;
  padding: 0 1.5rem;
}

.nav-12__logo {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 600;
  font-size: 1.5rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: 0.08em;
  display: block;
  white-space: nowrap;
}

.nav-12__logo-sub {
  font-size: 0.6rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
  font-family: 'Jost', sans-serif;
  font-weight: 500;
  display: block;
  margin-top: -2px;
}

.nav-12__right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 0;
  list-style: none;
}

.nav-12__right a {
  color: var(--muted);
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: color 0.2s;
  white-space: nowrap;
}

.nav-12__right a:hover {
  color: var(--text);
}

.nav-12__right a.is-cta {
  color: var(--accent);
  border: 1px solid var(--accent);
  border-radius: 4px;
  padding: 0.4rem 0.9rem;
  transition: background 0.2s, color 0.2s;
}

.nav-12__right a.is-cta:hover {
  background: var(--accent);
  color: var(--bg);
}
/* Mobile */

#nav-12-toggle {
  display: none;
}

.nav-12__mobile-bar {
  display: none;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.5rem;
  height: 60px;
}

.nav-12__mobile-logo {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 600;
  font-size: 1.3rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: 0.08em;
}

.nav-12__hamburger {
  display: flex;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  border: none;
  background: transparent;
  padding: 6px;
}

.nav-12__hamburger span {
  display: block;
  width: 20px;
  height: 1px;
  background: var(--text);
  border-radius: 1px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-12-toggle:checked ~ .nav-12__mobile-bar .nav-12__hamburger span:nth-child(1) {
  transform: translateY(6px) rotate(45deg);
}

#nav-12-toggle:checked ~ .nav-12__mobile-bar .nav-12__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-12-toggle:checked ~ .nav-12__mobile-bar .nav-12__hamburger span:nth-child(3) {
  transform: translateY(-6px) rotate(-45deg);
}

.nav-12__mobile-menu {
  display: none;
  flex-direction: column;
  gap: 0;
  padding: 0.75rem 1.5rem 1.25rem;
  border-top: 1px solid var(--border);
}

.nav-12__mobile-menu a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.7rem 0.5rem;
  border-bottom: 1px solid rgba(232,224,212,0.5);
  transition: color 0.2s;
}

.nav-12__mobile-menu a:last-child {
  border-bottom: none;
}

.nav-12__mobile-menu a:hover {
  color: var(--text);
}

#nav-12-toggle:checked ~ .nav-12__mobile-menu {
  display: flex;
}

@media (max-width: 768px) {
  .nav-12__bar {
    display: none;
  }

  .nav-12__mobile-bar {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-12__hamburger span {
    transition: none;
  }
}
```
