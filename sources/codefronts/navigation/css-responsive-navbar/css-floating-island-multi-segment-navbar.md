---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-floating-island-multi-segment-navbar/"
title: "CSS Floating Island Multi-Segment Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Detached floating pill navbar with three independently styled segments for branding, links, and actions."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Island Multi-Segment Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-floating-island-multi-segment-navbar/

Detached floating pill navbar with three independently styled segments for branding, links, and actions.
## HTML
```html
<div class="nav-16">
  <div class="nav-16__island">
    <a href="#" class="nav-16__logo">
      <div class="nav-16__logo-badge"></div>
      Canopy
    </a>
  </div>
  <div class="nav-16__island">
    <ul class="nav-16__links">
      <li><a href="#" class="is-active">Explore</a></li>
      <li><a href="#">Products</a></li>
      <li><a href="#">Sustainability</a></li>
      <li><a href="#">Journal</a></li>
      <li><a href="#">About</a></li>
    </ul>
  </div>
  <div class="nav-16__island nav-16__cta-island">
    <span class="nav-16__cta-text">Join 12k+ members</span>
    <button class="nav-16__cta-btn">Get started</button>
  </div>
</div>
<input type="checkbox" id="nav-16-toggle">
<div class="nav-16__mobile-bar">
  <a href="#" class="nav-16__mobile-logo">
    <div style="width:8px;height:8px;border-radius:50%;background:#6abf40;"></div>
    Canopy
  </a>
  <label for="nav-16-toggle" class="nav-16__hamburger" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </label>
</div>
<div class="nav-16__mobile-menu">
  <a href="#">Explore</a>
  <a href="#">Products</a>
  <a href="#">Sustainability</a>
  <a href="#">Journal</a>
  <a href="#">About</a>
  <a href="#" style="color:#4a8c2a; font-weight:700; margin-top:0.25rem;">Get started →</a>
</div>
<div style="padding:4rem 2rem; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:800; letter-spacing:-0.04em; margin-bottom:1rem; color:#1c2b0e;">Floating Island Multi-Segment Navbar</h1>
  <p style="color:#5a7040; font-size:1.05rem; line-height:1.75;">Three separate floating pill-shaped islands: logo, nav links, and CTA. Each uses <code>backdrop-filter</code> glass effect independently. The islands sit inside a flex row with <code>justify-content: space-between</code>.</p>
</div>
```
## CSS
```css
.nav-16,
.nav-16 *,
.nav-16 *::before,
.nav-16 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-16 {
  --text: #1c2b0e;
  --muted: rgba(28,43,14,0.45);
  --accent: #4a8c2a;
  --bg: rgba(255,255,255,0.85);
  --border: rgba(28,43,14,0.1);
  font-family: 'Plus Jakarta Sans', sans-serif;
  padding: 1.25rem 1.5rem;
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
/* Each section is its own floating island */

.nav-16__island {
  background: var(--bg);
  backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid var(--border);
  border-radius: 999px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.08), 0 1px 0 rgba(255,255,255,0.6) inset;
  display: flex;
  align-items: center;
}

.nav-16__logo {
  font-weight: 800;
  font-size: 1rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.02em;
  padding: 0.6rem 1.3rem;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-16__logo-badge {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #6abf40;
  box-shadow: 0 0 0 3px rgba(106,191,64,0.2);
}

.nav-16__links {
  display: flex;
  list-style: none;
  gap: 0;
  padding: 0.35rem;
}

.nav-16__links a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.45rem 0.9rem;
  border-radius: 999px;
  transition: color 0.2s, background 0.2s;
  white-space: nowrap;
}

.nav-16__links a:hover {
  color: var(--text);
  background: rgba(74,140,42,0.08);
}

.nav-16__links a.is-active {
  color: var(--accent);
  background: rgba(74,140,42,0.12);
}

.nav-16__cta-island {
  gap: 0.5rem;
  padding: 0.35rem 0.35rem 0.35rem 1rem;
}

.nav-16__cta-text {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--muted);
  white-space: nowrap;
}

.nav-16__cta-btn {
  padding: 0.5rem 1.1rem;
  border-radius: 999px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  font-family: inherit;
  background: var(--accent);
  color: #fff;
  transition: background 0.2s, transform 0.15s;
  box-shadow: 0 2px 8px rgba(74,140,42,0.35);
}

.nav-16__cta-btn:hover {
  background: #3a6e20;
  transform: scale(0.97);
}
/* Mobile */

#nav-16-toggle {
  display: none;
}

.nav-16__mobile-bar {
  display: none;
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 1rem 1.25rem;
  align-items: center;
  justify-content: space-between;
}

.nav-16__mobile-logo {
  font-weight: 800;
  font-size: 1rem;
  color: #1c2b0e;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-16__hamburger {
  display: flex;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 0.5rem 0.75rem;
  border: none;
  background: rgba(255,255,255,0.85);
  border-radius: 999px;
  border: 1px solid rgba(28,43,14,0.1);
  backdrop-filter: blur(12px);
}

.nav-16__hamburger span {
  display: block;
  width: 18px;
  height: 1.5px;
  background: #1c2b0e;
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-16-toggle:checked ~ .nav-16__mobile-bar .nav-16__hamburger span:nth-child(1) {
  transform: translateY(6.5px) rotate(45deg);
}

#nav-16-toggle:checked ~ .nav-16__mobile-bar .nav-16__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-16-toggle:checked ~ .nav-16__mobile-bar .nav-16__hamburger span:nth-child(3) {
  transform: translateY(-6.5px) rotate(-45deg);
}

.nav-16__mobile-menu {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(20px);
  margin: 0 1.25rem;
  border-radius: 16px;
  padding: 0.75rem 0.75rem 1rem;
  border: 1px solid rgba(28,43,14,0.1);
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
  position: sticky;
  top: 70px;
  z-index: 99;
}

.nav-16__mobile-menu a {
  display: block;
  color: rgba(28,43,14,0.6);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.6rem 0.75rem;
  border-radius: 10px;
  transition: background 0.15s, color 0.15s;
}

.nav-16__mobile-menu a:hover {
  background: rgba(74,140,42,0.08);
  color: #4a8c2a;
}

#nav-16-toggle:checked ~ .nav-16__mobile-menu {
  display: flex;
}

@media (max-width: 768px) {
  .nav-16 {
    display: none;
  }

  .nav-16__mobile-bar {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-16__links a,
    .nav-16__cta-btn {
    transition: none;
  }

  .nav-16__hamburger span {
    transition: none;
  }
}
```
