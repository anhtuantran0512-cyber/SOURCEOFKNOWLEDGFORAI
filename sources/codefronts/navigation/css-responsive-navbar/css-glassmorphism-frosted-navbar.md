---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-glassmorphism-frosted-navbar/"
title: "CSS Glassmorphism Frosted Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Dark frosted-glass sticky navbar with backdrop-filter blur, smooth hover pills, and a pure CSS hamburger toggle."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glassmorphism Frosted Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-glassmorphism-frosted-navbar/

Dark frosted-glass sticky navbar with backdrop-filter blur, smooth hover pills, and a pure CSS hamburger toggle.
## HTML
```html
<div class="nav-01">
  <input type="checkbox" id="nav-01-toggle">
  <div class="nav-01__bar">
    <a href="#" class="nav-01__logo">
      <div class="nav-01__logo-icon">✦</div>
      Prisma
    </a>
    <ul class="nav-01__links">
      <li><a href="#" class="is-active">Home</a></li>
      <li><a href="#">Products</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Blog</a></li>
      <li><a href="#">About</a></li>
    </ul>
    <div class="nav-01__actions">
      <button class="nav-01__btn nav-01__btn--ghost">Sign in</button>
      <button class="nav-01__btn nav-01__btn--primary">Get started</button>
    </div>
    <label for="nav-01-toggle" class="nav-01__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-01__mobile">
    <a href="#">Home</a>
    <a href="#">Products</a>
    <a href="#">Pricing</a>
    <a href="#">Blog</a>
    <a href="#">About</a>
    <div class="nav-01__mobile-actions">
      <button class="nav-01__btn nav-01__btn--ghost">Sign in</button>
      <button class="nav-01__btn nav-01__btn--primary">Get started</button>
    </div>
  </div>
</div>
<div style="padding:4rem 2rem; color:#f0eeff; max-width:700px; margin:0 auto;">
  <h1 style="font-size:3rem; font-weight:700; letter-spacing:-0.03em; margin-bottom:1rem; background:linear-gradient(135deg,#a78bfa,#60a5fa); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Glassmorphism Navbar</h1>
  <p style="color:rgba(240,238,255,0.65); font-size:1.1rem; line-height:1.7;">Resize the window to see the hamburger menu appear. The nav uses <code>backdrop-filter: blur()</code> for the frosted glass effect.</p>
</div>
```
## CSS
```css
.nav-01,
.nav-01 *,
.nav-01 *::before,
.nav-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-01 {
  --glass-bg: rgba(255,255,255,0.08);
  --glass-border: rgba(255,255,255,0.15);
  --text: #f0eeff;
  --accent: #a78bfa;
  --hover-bg: rgba(167,139,250,0.15);
  font-family: 'Plus Jakarta Sans', sans-serif;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-01__bar {
  background: var(--glass-bg);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid var(--glass-border);
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  position: relative;
}

.nav-01__logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--text);
  font-weight: 700;
  font-size: 1.2rem;
  letter-spacing: -0.02em;
}

.nav-01__logo-icon {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #a78bfa, #60a5fa);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}

.nav-01__links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  list-style: none;
}

.nav-01__links a {
  color: rgba(240,238,255,0.75);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.5rem 0.9rem;
  border-radius: 8px;
  transition: background 0.2s, color 0.2s;
  position: relative;
}

.nav-01__links a:hover,
.nav-01__links a.is-active {
  background: var(--hover-bg);
  color: var(--accent);
}

.nav-01__links a.is-active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 50%;
  transform: translateX(-50%);
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--accent);
}

.nav-01__actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav-01__btn {
  padding: 0.45rem 1.1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  font-family: inherit;
  transition: all 0.2s;
}

.nav-01__btn--ghost {
  background: transparent;
  color: var(--text);
  border: 1px solid var(--glass-border);
}

.nav-01__btn--ghost:hover {
  background: var(--hover-bg);
}

.nav-01__btn--primary {
  background: linear-gradient(135deg, #a78bfa, #60a5fa);
  color: #fff;
}

.nav-01__btn--primary:hover {
  opacity: 0.85;
  transform: translateY(-1px);
}

.nav-01__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
}

.nav-01__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-01-toggle {
  display: none;
}

#nav-01-toggle:checked ~ .nav-01__bar .nav-01__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-01-toggle:checked ~ .nav-01__bar .nav-01__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-01-toggle:checked ~ .nav-01__bar .nav-01__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-01__mobile {
  display: none;
  background: rgba(15,12,41,0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--glass-border);
  padding: 1rem 1.5rem;
  flex-direction: column;
  gap: 0.25rem;
}

.nav-01__mobile a {
  color: rgba(240,238,255,0.8);
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  padding: 0.65rem 0.75rem;
  border-radius: 8px;
  transition: background 0.2s, color 0.2s;
}

.nav-01__mobile a:hover {
  background: var(--hover-bg);
  color: var(--accent);
}

.nav-01__mobile-actions {
  display: flex;
  gap: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--glass-border);
  margin-top: 0.5rem;
}

.nav-01__mobile-actions .nav-01__btn {
  flex: 1;
  text-align: center;
}

#nav-01-toggle:checked ~ .nav-01__mobile {
  display: flex;
}

@media (max-width: 768px) {
  .nav-01__links,
    .nav-01__actions {
    display: none;
  }

  .nav-01__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-01__btn--primary {
    transition: none;
  }

  .nav-01__hamburger span {
    transition: none;
  }
}
```
