---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-scroll-aware-shrink-navbar/"
title: "CSS Scroll-Aware Shrink Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Full-height hero navbar that compresses to a compact strip on scroll with JS class-toggle and CSS transition."
has_js: "true"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scroll-Aware Shrink Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-scroll-aware-shrink-navbar/

Full-height hero navbar that compresses to a compact strip on scroll with JS class-toggle and CSS transition.
## HTML
```html
<div class="nav-06" id="navbar06">
  <input type="checkbox" id="nav-06-toggle">
  <div class="nav-06__inner">
    <a href="#" class="nav-06__logo">Kol<em>or</em></a>
    <ul class="nav-06__links">
      <li><a href="#" class="is-active">Home</a></li>
      <li><a href="#">Work</a></li>
      <li><a href="#">Services</a></li>
      <li><a href="#">Studio</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
    <button class="nav-06__btn">Hire us</button>
    <label for="nav-06-toggle" class="nav-06__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-06__mobile">
    <a href="#">Home</a><a href="#">Work</a><a href="#">Services</a><a href="#">Studio</a><a href="#">Contact</a>
    <a href="#" style="color:#e8a838; font-weight:600;">Hire us →</a>
  </div>
</div>
<div class="nav-06__hero">
  <h1>Scroll to see the navbar transform</h1>
  <p>As you scroll down, the navbar shrinks in height, gains a frosted white background, and switches from ghost to solid button style.</p>
  <div class="nav-06__scroll-hint">↓ scroll down ↓</div>
</div>
<div style="padding:4rem 2rem; max-width:700px; margin:0 auto;">
  <h2 style="font-size:2rem; font-weight:700; letter-spacing:-0.03em; margin-bottom:1rem;">Page content area</h2>
  <p style="color:#6b5f4a; font-size:1.05rem; line-height:1.75;">The navbar listens to the <code>scroll</code> event and adds an <code>.is-scrolled</code> class when the page scrolls past 60px. All style changes are CSS transitions on that class toggle.</p>
</div>
```
## CSS
```css
.nav-06,
.nav-06 *,
.nav-06 *::before,
.nav-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-06 {
  --bg: transparent;
  --scrolled-bg: rgba(255,255,255,0.95);
  --text: #faf5ee;
  --scrolled-text: #1a1206;
  --accent: #e8a838;
  --border: rgba(255,255,255,0.15);
  --scrolled-border: rgba(0,0,0,0.08);
  font-family: 'Outfit', sans-serif;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 200;
  transition: background 0.4s, box-shadow 0.4s, height 0.4s;
  height: 80px;
}

.nav-06.is-scrolled {
  background: var(--scrolled-bg);
  backdrop-filter: blur(16px);
  box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 4px 16px rgba(0,0,0,0.06);
  height: 60px;
}

.nav-06__inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  height: 100%;
  gap: 2rem;
}

.nav-06__logo {
  font-weight: 800;
  font-size: 1.3rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.03em;
  transition: color 0.4s;
  flex-shrink: 0;
}

.nav-06.is-scrolled .nav-06__logo {
  color: var(--scrolled-text);
}

.nav-06__logo em {
  color: var(--accent);
  font-style: normal;
}

.nav-06__links {
  display: flex;
  list-style: none;
  gap: 0.25rem;
  flex: 1;
}

.nav-06__links a {
  color: rgba(250,245,238,0.85);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.45rem 0.9rem;
  border-radius: 8px;
  transition: color 0.4s, background 0.2s;
}

.nav-06.is-scrolled .nav-06__links a {
  color: rgba(26,18,6,0.7);
}

.nav-06__links a:hover {
  background: rgba(255,255,255,0.12);
  color: var(--text) !important;
}

.nav-06.is-scrolled .nav-06__links a:hover {
  background: rgba(232,168,56,0.1);
  color: var(--accent) !important;
}

.nav-06__links a.is-active {
  color: var(--accent) !important;
  font-weight: 600;
}

.nav-06__btn {
  padding: 0.5rem 1.3rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  border: 2px solid rgba(255,255,255,0.35);
  font-family: inherit;
  color: var(--text);
  background: transparent;
  transition: all 0.4s;
  flex-shrink: 0;
}

.nav-06.is-scrolled .nav-06__btn {
  border-color: transparent;
  background: var(--accent);
  color: #1a1206;
}

.nav-06__btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(232,168,56,0.35);
}
/* Hero */

.nav-06__hero {
  height: 100vh;
  background: linear-gradient(135deg, #1a1206 0%, #3d2b00 50%, #1a1206 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  color: #faf5ee;
  text-align: center;
  padding: 2rem;
  position: relative;
}

.nav-06__hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at center, rgba(232,168,56,0.15) 0%, transparent 70%);
  pointer-events: none;
}

.nav-06__hero h1 {
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 800;
  letter-spacing: -0.04em;
  margin-bottom: 1rem;
}

.nav-06__hero p {
  color: rgba(250,245,238,0.65);
  font-size: 1.1rem;
  max-width: 500px;
  line-height: 1.7;
}

.nav-06__scroll-hint {
  margin-top: 3rem;
  color: rgba(250,245,238,0.4);
  font-size: 0.875rem;
  animation: nav-06-bob 2s ease-in-out infinite;
}

@keyframes nav-06-bob {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(6px);
  }
}
/* Mobile */

#nav-06-toggle {
  display: none;
}

.nav-06__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
  margin-left: auto;
}

.nav-06__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s, background 0.4s;
}

.nav-06.is-scrolled .nav-06__hamburger span {
  background: var(--scrolled-text);
}

#nav-06-toggle:checked ~ .nav-06__inner .nav-06__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-06-toggle:checked ~ .nav-06__inner .nav-06__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-06-toggle:checked ~ .nav-06__inner .nav-06__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-06__mobile {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  background: rgba(255,255,255,0.97);
  backdrop-filter: blur(16px);
  padding: 0.75rem 1.5rem 1rem;
  border-bottom: 1px solid rgba(0,0,0,0.08);
}

.nav-06__mobile a {
  display: block;
  color: rgba(26,18,6,0.8);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  padding: 0.65rem 0.5rem;
  border-radius: 8px;
  transition: background 0.15s;
}

.nav-06__mobile a:hover {
  background: rgba(232,168,56,0.1);
  color: #e8a838;
  padding-left: 1rem;
}

#nav-06-toggle:checked ~ .nav-06__mobile {
  display: flex;
}

@media (max-width: 768px) {
  .nav-06__links,
    .nav-06__btn {
    display: none;
  }

  .nav-06__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-06,
    .nav-06__logo,
    .nav-06__links a,
    .nav-06__btn,
    .nav-06__hamburger span {
    transition: none;
  }

  .nav-06__scroll-hint {
    animation: none;
  }
}
```

## JavaScript
```js
const nav = document.getElementById('navbar06');
  function onScroll() {
    if (window.scrollY > 60) {
      nav.classList.add('is-scrolled');
    } else {
      nav.classList.remove('is-scrolled');
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
```
