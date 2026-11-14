---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-pill-highlight-navigation-bar/"
title: "CSS Pill Highlight Navigation Bar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Compact pill-shaped nav links that highlight on hover with a soft background fill and subtle scale animation."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pill Highlight Navigation Bar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-pill-highlight-navigation-bar/

Compact pill-shaped nav links that highlight on hover with a soft background fill and subtle scale animation.
## HTML
```html
<div class="nav-05">
  <div class="nav-05__bar">
    <a href="#" class="nav-05__logo">⬡ Helix</a>
    <div class="nav-05__sep"></div>
    <ul class="nav-05__links">
      <li><a href="#" class="is-active">Home</a></li>
      <li><a href="#">Features</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Blog</a></li>
      <li><a href="#">About</a></li>
    </ul>
    <div class="nav-05__sep"></div>
    <button class="nav-05__cta">Get access</button>
  </div>
</div>
<input type="checkbox" id="nav-05-toggle">
<div class="nav-05__mobile-bar">
  <a href="#" class="nav-05__mobile-logo">⬡ Helix</a>
  <label for="nav-05-toggle" class="nav-05__hamburger" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </label>
</div>
<div class="nav-05__mobile-links">
  <a href="#">Home</a>
  <a href="#">Features</a>
  <a href="#">Pricing</a>
  <a href="#">Blog</a>
  <a href="#">About</a>
  <a href="#" style="color:#818cf8; font-weight:600;">Get access →</a>
</div>
<div style="padding:4rem 2rem; color:#f9fafb; max-width:700px; margin:0 auto; text-align:center;">
  <h1 style="font-size:3rem; font-weight:700; letter-spacing:-0.04em; margin-bottom:1rem;">Pill Highlight <br>Navigation Bar</h1>
  <p style="color:#9ca3af; font-size:1.1rem; line-height:1.7;">A floating pill-style navbar centered on the page. Active state uses a solid white pill with dark text. Hover shows a translucent pill preview.</p>
</div>
```
## CSS
```css
.nav-05,
.nav-05 *,
.nav-05 *::before,
.nav-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-05 {
  --text: #f9fafb;
  --muted: #9ca3af;
  --pill: rgba(255,255,255,0.1);
  --active-pill: #ffffff;
  --active-text: #111827;
  font-family: 'Inter', sans-serif;
  display: flex;
  justify-content: center;
  padding: 1.5rem 1rem;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-05__bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 999px;
  padding: 0.35rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.08);
}

.nav-05__logo {
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--text);
  text-decoration: none;
  padding: 0.4rem 1rem;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.nav-05__sep {
  width: 1px;
  height: 20px;
  background: rgba(255,255,255,0.15);
  flex-shrink: 0;
}

.nav-05__links {
  display: flex;
  list-style: none;
  gap: 0.25rem;
}

.nav-05__links a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  padding: 0.4rem 0.9rem;
  border-radius: 999px;
  transition: color 0.2s, background 0.2s;
  white-space: nowrap;
}

.nav-05__links a:hover {
  color: var(--text);
  background: var(--pill);
}

.nav-05__links a.is-active {
  background: var(--active-pill);
  color: var(--active-text);
  font-weight: 600;
  box-shadow: 0 1px 4px rgba(0,0,0,0.25);
}

.nav-05__cta {
  padding: 0.4rem 1.1rem;
  border-radius: 999px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  font-family: inherit;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  transition: opacity 0.2s, transform 0.15s;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(99,102,241,0.4);
}

.nav-05__cta:hover {
  opacity: 0.85;
  transform: scale(0.97);
}
/* Mobile — stack center-aligned */

#nav-05-toggle {
  display: none;
}

.nav-05__mobile-bar {
  display: none;
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(10,10,10,0.9);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding: 0.75rem 1.25rem;
  align-items: center;
  justify-content: space-between;
}

.nav-05__mobile-logo {
  font-weight: 700;
  font-size: 1rem;
  color: #f9fafb;
  text-decoration: none;
}

.nav-05__hamburger {
  display: flex;
  flex-direction: column;
  gap: 4px;
  cursor: pointer;
  border: none;
  background: transparent;
  padding: 6px;
}

.nav-05__hamburger span {
  display: block;
  width: 20px;
  height: 1.5px;
  background: #f9fafb;
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-05-toggle:checked ~ .nav-05__mobile-bar .nav-05__hamburger span:nth-child(1) {
  transform: translateY(5.5px) rotate(45deg);
}

#nav-05-toggle:checked ~ .nav-05__mobile-bar .nav-05__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-05-toggle:checked ~ .nav-05__mobile-bar .nav-05__hamburger span:nth-child(3) {
  transform: translateY(-5.5px) rotate(-45deg);
}

.nav-05__mobile-links {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  background: rgba(10,10,10,0.95);
  backdrop-filter: blur(12px);
  padding: 1rem 1.25rem;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  position: sticky;
  top: 56px;
  z-index: 99;
}

.nav-05__mobile-links a {
  display: block;
  color: #9ca3af;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  padding: 0.6rem 0.75rem;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}

.nav-05__mobile-links a:hover {
  background: rgba(255,255,255,0.06);
  color: #f9fafb;
}

#nav-05-toggle:checked ~ .nav-05__mobile-links {
  display: flex;
}

@media (max-width: 640px) {
  .nav-05 {
    display: none;
  }

  .nav-05__mobile-bar {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-05__links a,
    .nav-05__cta {
    transition: none;
  }

  .nav-05__hamburger span {
    transition: none;
  }

  .nav-05__mobile-links a {
    transition: none;
  }
}
```
