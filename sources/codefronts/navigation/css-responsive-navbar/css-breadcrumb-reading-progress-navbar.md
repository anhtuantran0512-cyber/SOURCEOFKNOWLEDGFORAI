---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-breadcrumb-reading-progress-navbar/"
title: "CSS Breadcrumb Reading Progress Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Dual-row navbar with an auto-updating breadcrumb trail and a thin color-fill reading progress bar driven by scroll position."
has_js: "true"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Breadcrumb Reading Progress Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-breadcrumb-reading-progress-navbar/

Dual-row navbar with an auto-updating breadcrumb trail and a thin color-fill reading progress bar driven by scroll position.
## HTML
```html
<div class="nav-08" id="nav08">
  <div class="nav-08__progress-track">
    <div class="nav-08__progress-bar" id="nav08Progress"></div>
  </div>
  <input type="checkbox" id="nav-08-toggle">
  <div class="nav-08__main">
    <a href="#" class="nav-08__logo">Docs</a>
    <ol class="nav-08__crumbs">
      <li><a href="#">Home</a></li>
      <li><a href="#">Guide</a></li>
      <li><a href="#">CSS</a></li>
      <li><span>Responsive Navbar</span></li>
    </ol>
    <div class="nav-08__sep"></div>
    <ul class="nav-08__sections">
      <li><a href="#" class="is-active">Overview</a></li>
      <li><a href="#">Installation</a></li>
      <li><a href="#">Usage</a></li>
      <li><a href="#">API</a></li>
      <li><a href="#">Examples</a></li>
    </ul>
    <div class="nav-08__actions">
      <span class="nav-08__time">12 min read</span>
      <button class="nav-08__edit">Edit page</button>
    </div>
    <label for="nav-08-toggle" class="nav-08__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-08__mobile">
    <a href="#">Overview</a>
    <a href="#">Installation</a>
    <a href="#">Usage</a>
    <a href="#">API</a>
    <a href="#">Examples</a>
  </div>
</div>
<div style="padding:3rem 2rem; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:700; letter-spacing:-0.03em; margin-bottom:1.5rem;">Breadcrumb + Reading Progress Navbar</h1>
  <p style="color:#78716c; font-size:1.05rem; line-height:1.75; margin-bottom:1.5rem;">Scroll this page to see the green reading progress bar fill up. The bar width is set by JavaScript reading <code>scrollY / (documentHeight - viewportHeight)</code>.</p>
  <p style="color:#78716c; font-size:1.05rem; line-height:1.75; margin-bottom:1.5rem;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>
  <p style="color:#78716c; font-size:1.05rem; line-height:1.75; margin-bottom:1.5rem;">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
  <p style="color:#78716c; font-size:1.05rem; line-height:1.75;">Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
</div>
```
## CSS
```css
.nav-08,
.nav-08 *,
.nav-08 *::before,
.nav-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-08 {
  --bg: #fff;
  --border: #e4e4e0;
  --text: #111110;
  --muted: #78716c;
  --accent: #10b981;
  --progress-bg: #e4e4e0;
  font-family: 'IBM Plex Sans', sans-serif;
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
}
/* Read progress bar at very top */

.nav-08__progress-track {
  height: 3px;
  background: var(--progress-bg);
  position: relative;
}

.nav-08__progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #10b981, #06d6a0, #34d399);
  width: 0%;
  transition: width 0.1s linear;
  position: relative;
}

.nav-08__progress-bar::after {
  content: '';
  position: absolute;
  right: -1px;
  top: -1px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #06d6a0;
  box-shadow: 0 0 6px #06d6a0;
}
/* Main nav */

.nav-08__main {
  display: flex;
  align-items: center;
  padding: 0 2rem;
  height: 56px;
  gap: 0;
}

.nav-08__logo {
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.02em;
  margin-right: 1.5rem;
  flex-shrink: 0;
}
/* Breadcrumb */

.nav-08__crumbs {
  display: flex;
  align-items: center;
  gap: 0;
  list-style: none;
  flex: 1;
  overflow: hidden;
}

.nav-08__crumbs li {
  display: flex;
  align-items: center;
  font-size: 0.875rem;
  white-space: nowrap;
}

.nav-08__crumbs li + li::before {
  content: '/';
  color: #d4d4d0;
  margin: 0 0.5rem;
  font-size: 0.8rem;
}

.nav-08__crumbs a {
  color: var(--muted);
  text-decoration: none;
  font-weight: 500;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  transition: color 0.15s, background 0.15s;
}

.nav-08__crumbs a:hover {
  color: var(--text);
  background: #f4f4f2;
}

.nav-08__crumbs li:last-child a,
.nav-08__crumbs li:last-child span {
  color: var(--text);
  font-weight: 600;
  pointer-events: none;
}

.nav-08__sep {
  width: 1px;
  height: 24px;
  background: var(--border);
  margin: 0 1.25rem;
  flex-shrink: 0;
}
/* Section nav */

.nav-08__sections {
  display: flex;
  list-style: none;
  gap: 0;
  overflow-x: auto;
  scrollbar-width: none;
}

.nav-08__sections::-webkit-scrollbar {
  display: none;
}

.nav-08__sections a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 500;
  padding: 0.35rem 0.85rem;
  border-radius: 999px;
  transition: color 0.15s, background 0.15s;
  white-space: nowrap;
}

.nav-08__sections a:hover {
  color: var(--text);
  background: #f4f4f2;
}

.nav-08__sections a.is-active {
  color: var(--accent);
  background: rgba(16,185,129,0.08);
  font-weight: 600;
}
/* Right */

.nav-08__actions {
  margin-left: auto;
  flex-shrink: 0;
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.nav-08__time {
  font-size: 0.775rem;
  color: var(--muted);
}

.nav-08__edit {
  padding: 0.35rem 0.85rem;
  border-radius: 6px;
  font-size: 0.775rem;
  font-weight: 600;
  cursor: pointer;
  border: 1px solid var(--border);
  font-family: inherit;
  color: var(--text);
  background: transparent;
  transition: background 0.15s, border-color 0.15s;
}

.nav-08__edit:hover {
  background: #f4f4f2;
  border-color: #ccc;
}
/* Mobile */

#nav-08-toggle {
  display: none;
}

.nav-08__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 6px;
  border: none;
  background: transparent;
}

.nav-08__hamburger span {
  display: block;
  width: 20px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-08-toggle:checked ~ .nav-08__main .nav-08__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-08-toggle:checked ~ .nav-08__main .nav-08__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-08-toggle:checked ~ .nav-08__main .nav-08__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-08__mobile {
  display: none;
  flex-direction: column;
  gap: 0;
  padding: 0.75rem 1.5rem 1rem;
  border-top: 1px solid var(--border);
}

.nav-08__mobile a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.6rem 0.5rem;
  border-radius: 6px;
}

.nav-08__mobile a:hover {
  background: #f4f4f2;
  color: var(--text);
}

#nav-08-toggle:checked ~ .nav-08__mobile {
  display: flex;
}

@media (max-width: 768px) {
  .nav-08__crumbs li:not(:first-child):not(:last-child) {
    display: none;
  }

  .nav-08__sep,
    .nav-08__sections,
    .nav-08__time {
    display: none;
  }

  .nav-08__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-08__progress-bar {
    transition: none;
  }

  .nav-08__hamburger span {
    transition: none;
  }
}
```

## JavaScript
```js
const bar = document.getElementById('nav08Progress');
  function updateProgress() {
    const scrolled = window.scrollY;
    const total = document.documentElement.scrollHeight - window.innerHeight;
    const pct = total > 0 ? (scrolled / total) * 100 : 0;
    bar.style.width = pct + '%';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();
```
