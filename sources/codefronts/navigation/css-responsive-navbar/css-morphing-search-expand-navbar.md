---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-morphing-search-expand-navbar/"
title: "CSS Morphing Search Expand Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Navbar with a search icon that morphs into a full-width input field using JS and CSS max-width transition."
has_js: "true"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Morphing Search Expand Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-morphing-search-expand-navbar/

Navbar with a search icon that morphs into a full-width input field using JS and CSS max-width transition.
## HTML
```html
<div class="nav-15" id="nav15">
  <input type="checkbox" id="nav-15-toggle">
  <div class="nav-15__inner">
    <a href="#" class="nav-15__logo">Synapse<span>.</span></a>
    <ul class="nav-15__links">
      <li><a href="#" class="is-active">Home</a></li>
      <li><a href="#">Features</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Docs</a></li>
      <li><a href="#">Blog</a></li>
    </ul>
    <div class="nav-15__search-wrap">
      <div class="nav-15__search" id="nav15Search">
        <button class="nav-15__search-btn" id="nav15SearchBtn" aria-label="Search">🔍</button>
        <input type="text" class="nav-15__search-input" id="nav15SearchInput" placeholder="Search docs, features...">
      </div>
    </div>
    <button class="nav-15__btn">Sign up</button>
    <label for="nav-15-toggle" class="nav-15__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-15__mobile">
    <a href="#">Home</a><a href="#">Features</a><a href="#">Pricing</a><a href="#">Docs</a><a href="#">Blog</a>
    <a href="#" style="color:#3b82f6; font-weight:700;">Sign up →</a>
  </div>
</div>
<div style="padding:4rem 2rem; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:800; letter-spacing:-0.04em; margin-bottom:1rem; color:#0f172a;">Morphing Search Expand Navbar</h1>
  <p style="color:#64748b; font-size:1.05rem; line-height:1.75;">Click the 🔍 icon to expand the search bar. It grows from 40px to 280px with a smooth <code>width</code> transition, the nav links fade out to give it room, and clicking outside collapses it.</p>
</div>
```
## CSS
```css
.nav-15,
.nav-15 *,
.nav-15 *::before,
.nav-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-15 {
  --bg: #fff;
  --text: #0f172a;
  --muted: #64748b;
  --accent: #3b82f6;
  --accent-light: #eff6ff;
  --border: #e2e8f0;
  font-family: 'Figtree', sans-serif;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.nav-15__inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  height: 64px;
  gap: 1.5rem;
  position: relative;
}

.nav-15__logo {
  font-weight: 800;
  font-size: 1.2rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.03em;
  flex-shrink: 0;
}

.nav-15__logo span {
  color: var(--accent);
}

.nav-15__links {
  display: flex;
  list-style: none;
  gap: 0.25rem;
  flex: 1;
  transition: opacity 0.3s, visibility 0.3s;
}

.nav-15__links a {
  color: var(--muted);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.45rem 0.9rem;
  border-radius: 8px;
  transition: color 0.15s, background 0.15s;
}

.nav-15__links a:hover {
  color: var(--text);
  background: var(--accent-light);
}

.nav-15__links a.is-active {
  color: var(--accent);
}
/* Search */

.nav-15__search-wrap {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-left: auto;
}

.nav-15__search {
  display: flex;
  align-items: center;
  background: var(--accent-light);
  border: 1.5px solid transparent;
  border-radius: 10px;
  overflow: hidden;
  width: 40px;
  transition: width 0.4s cubic-bezier(.4,0,.2,1), border-color 0.3s, background 0.3s;
}

.nav-15__search.is-expanded {
  width: 280px;
  border-color: var(--accent);
  background: #fff;
}

.nav-15__search-btn {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--accent);
  font-size: 1rem;
  border-radius: 10px;
  transition: color 0.2s;
}

.nav-15__search-input {
  flex: 1;
  border: none;
  outline: none;
  background: transparent;
  font-family: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text);
  padding-right: 0.75rem;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
}

.nav-15__search.is-expanded .nav-15__search-input {
  opacity: 1;
  pointer-events: all;
}

.nav-15__search-input::placeholder {
  color: var(--muted);
}
/* When expanded, hide links */

.nav-15.is-searching .nav-15__links {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.nav-15__btn {
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
  flex-shrink: 0;
}

.nav-15__btn:hover {
  background: #2563eb;
  transform: translateY(-1px);
}
/* Mobile */

#nav-15-toggle {
  display: none;
}

.nav-15__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
}

.nav-15__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-15-toggle:checked ~ .nav-15__inner .nav-15__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-15-toggle:checked ~ .nav-15__inner .nav-15__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-15-toggle:checked ~ .nav-15__inner .nav-15__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-15__mobile {
  display: none;
  flex-direction: column;
  padding: 0.75rem 1.5rem 1rem;
  border-top: 1px solid var(--border);
  gap: 0.25rem;
}

.nav-15__mobile a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.6rem 0.5rem;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}

.nav-15__mobile a:hover {
  background: var(--accent-light);
  color: var(--accent);
}

#nav-15-toggle:checked ~ .nav-15__mobile {
  display: flex;
}

@media (max-width: 768px) {
  .nav-15__links,
    .nav-15__btn {
    display: none;
  }

  .nav-15__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-15__search,
    .nav-15__links,
    .nav-15__search-input {
    transition: none;
  }

  .nav-15__btn,
    .nav-15__hamburger span {
    transition: none;
  }
}
```

## JavaScript
```js
const nav = document.getElementById('nav15');
  const search = document.getElementById('nav15Search');
  const btn = document.getElementById('nav15SearchBtn');
  const input = document.getElementById('nav15SearchInput');
  let open = false;
  function openSearch() {
    open = true;
    search.classList.add('is-expanded');
    nav.classList.add('is-searching');
    setTimeout(() => input.focus(), 350);
  }
  function closeSearch() {
    open = false;
    search.classList.remove('is-expanded');
    nav.classList.remove('is-searching');
    input.value = '';
  }
  btn.addEventListener('click', function(e) {
    e.stopPropagation();
    open ? closeSearch() : openSearch();
  });
  document.addEventListener('click', function(e) {
    if (open && !search.contains(e.target)) closeSearch();
  });
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeSearch();
  });
```
