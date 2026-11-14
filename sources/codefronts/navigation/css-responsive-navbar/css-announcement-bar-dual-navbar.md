---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-announcement-bar-dual-navbar/"
title: "CSS Announcement Bar Dual Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Three-layer header: a dismissible announcement strip, a secondary utility bar, and the primary navigation row."
has_js: "true"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Announcement Bar Dual Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-announcement-bar-dual-navbar/

Three-layer header: a dismissible announcement strip, a secondary utility bar, and the primary navigation row.
## HTML
```html
<div class="nav-19">
  <div class="nav-19__announce">
    <span class="nav-19__announce-emoji">🎉</span>
    <span>Summer sale — up to 40% off everything. <a href="#">Shop now →</a></span>
    <button class="nav-19__announce-close" id="announceDismiss" aria-label="Dismiss">×</button>
  </div>
  <div class="nav-19__utility">
    <div class="nav-19__utility-left">
      <span>📍 Free shipping on orders over $50</span>
      <span>🔒 Secure checkout</span>
    </div>
    <div class="nav-19__utility-right">
      <a href="#">Help</a>
      <a href="#">Track order</a>
      <a href="#">English ▾</a>
    </div>
  </div>
  <input type="checkbox" id="nav-19-toggle">
  <div class="nav-19__main">
    <a href="#" class="nav-19__logo">Shop<span>ify</span></a>
    <ul class="nav-19__links">
      <li><a href="#" class="is-active">Home</a></li>
      <li><a href="#">New arrivals</a></li>
      <li><a href="#">Collections</a></li>
      <li><a href="#">Sale</a></li>
      <li><a href="#">About</a></li>
    </ul>
    <div class="nav-19__actions">
      <button class="nav-19__cart">
        🛒 Cart
        <span class="nav-19__cart-badge">3</span>
      </button>
      <button class="nav-19__btn">Sign in</button>
    </div>
    <label for="nav-19-toggle" class="nav-19__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-19__mobile">
    <a href="#">Home</a><a href="#">New arrivals</a><a href="#">Collections</a>
    <a href="#">Sale</a><a href="#">About</a>
    <a href="#" style="color:#7c3aed; font-weight:700;">Sign in →</a>
  </div>
</div>
<div style="padding:3rem 2rem; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:1rem; color:#111;">Announcement Bar + Dual Navbar</h1>
  <p style="color:#6b7280; font-size:1.05rem; line-height:1.75;">Three stacked bars: a dismissible announcement strip, a utility info row, and the main navigation. The dismiss button uses JavaScript to hide the announcement bar. Common e-commerce pattern.</p>
</div>
```
## CSS
```css
.nav-19,
.nav-19 *,
.nav-19 *::before,
.nav-19 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-19 {
  --bg: #fff;
  --text: #111;
  --muted: #6b7280;
  --accent: #7c3aed;
  --announce-bg: #7c3aed;
  --announce-text: #fff;
  --border: #f0f0f0;
  font-family: 'Rubik', sans-serif;
  position: sticky;
  top: 0;
  z-index: 100;
}
/* Announcement bar */

.nav-19__announce {
  background: var(--announce-bg);
  color: var(--announce-text);
  text-align: center;
  padding: 0.5rem 2.5rem;
  font-size: 0.8rem;
  font-weight: 500;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  line-height: 1.4;
}

.nav-19__announce a {
  color: #fff;
  font-weight: 700;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.nav-19__announce a:hover {
  opacity: 0.8;
}

.nav-19__announce-close {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  border: none;
  cursor: pointer;
  color: #fff;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s;
}

.nav-19__announce-close:hover {
  background: rgba(255,255,255,0.35);
}

.nav-19__announce-emoji {
  font-size: 1rem;
}
/* Utility bar */

.nav-19__utility {
  background: #f9f9fa;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.3rem 2rem;
  font-size: 0.75rem;
  color: var(--muted);
  font-weight: 500;
}

.nav-19__utility-left {
  display: flex;
  gap: 1.25rem;
}

.nav-19__utility-left span {
  display: flex;
  align-items: center;
  gap: 4px;
}

.nav-19__utility-right {
  display: flex;
  gap: 1.25rem;
  align-items: center;
}

.nav-19__utility-right a {
  color: var(--muted);
  text-decoration: none;
  transition: color 0.15s;
}

.nav-19__utility-right a:hover {
  color: var(--text);
}
/* Main nav */

.nav-19__main {
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  padding: 0 2rem;
  height: 64px;
  gap: 2rem;
}

.nav-19__logo {
  font-weight: 800;
  font-size: 1.3rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.03em;
  flex-shrink: 0;
}

.nav-19__logo span {
  color: var(--accent);
}

.nav-19__links {
  display: flex;
  list-style: none;
  gap: 0;
  flex: 1;
}

.nav-19__links a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0.5rem 0.9rem;
  border-radius: 6px;
  transition: color 0.15s, background 0.15s;
}

.nav-19__links a:hover {
  color: var(--text);
  background: #f4f4f8;
}

.nav-19__links a.is-active {
  color: var(--accent);
  font-weight: 600;
}

.nav-19__actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav-19__cart {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--muted);
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  background: transparent;
  font-family: inherit;
  padding: 0.45rem 0.75rem;
  border-radius: 8px;
  transition: color 0.15s, background 0.15s;
  position: relative;
}

.nav-19__cart:hover {
  color: var(--text);
  background: #f4f4f8;
}

.nav-19__cart-badge {
  position: absolute;
  top: 2px;
  right: 4px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  font-size: 0.6rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-19__btn {
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

.nav-19__btn:hover {
  background: #6d28d9;
  transform: translateY(-1px);
}
/* Mobile */

#nav-19-toggle {
  display: none;
}

.nav-19__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
  margin-left: auto;
}

.nav-19__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-19-toggle:checked ~ .nav-19__main .nav-19__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-19-toggle:checked ~ .nav-19__main .nav-19__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-19-toggle:checked ~ .nav-19__main .nav-19__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-19__mobile {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  padding: 0.75rem 1.5rem 1rem;
  border-top: 1px solid var(--border);
  background: var(--bg);
}

.nav-19__mobile a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.6rem 0.5rem;
  border-radius: 6px;
  transition: background 0.15s, color 0.15s;
}

.nav-19__mobile a:hover {
  background: #f4f4f8;
  color: var(--text);
}

#nav-19-toggle:checked ~ .nav-19__mobile {
  display: flex;
}

@media (max-width: 768px) {
  .nav-19__links,
    .nav-19__actions,
    .nav-19__utility {
    display: none;
  }

  .nav-19__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-19__btn,
    .nav-19__links a,
    .nav-19__hamburger span {
    transition: none;
  }
}
```

## JavaScript
```js
document.getElementById('announceDismiss').addEventListener('click', function() {
  this.closest('.nav-19__announce').style.display = 'none';
});
```
