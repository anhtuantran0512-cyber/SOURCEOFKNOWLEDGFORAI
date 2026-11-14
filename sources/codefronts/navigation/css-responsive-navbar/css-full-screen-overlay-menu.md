---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-full-screen-overlay-menu/"
title: "CSS Full-Screen Overlay Menu"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Button-triggered full-viewport overlay menu with staggered link entrance animations and a blurred background."
has_js: "true"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Full-Screen Overlay Menu
Source: https://codefronts.com/navigation/css-responsive-navbar/css-full-screen-overlay-menu/

Button-triggered full-viewport overlay menu with staggered link entrance animations and a blurred background.
## HTML
```html
<div class="nav-14" id="nav14">
  <div class="nav-14__bar">
    <a href="#" class="nav-14__logo">Forma</a>
    <button class="nav-14__toggle" id="nav14Toggle" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="nav-14__overlay" aria-hidden="true">
    <ul class="nav-14__nav-links">
      <li>
        <a href="#"><span class="nav-14__nav-num">01</span><span class="nav-14__nav-title">Studio</span><span class="nav-14__nav-arrow">→</span></a>
      </li>
      <li>
        <a href="#"><span class="nav-14__nav-num">02</span><span class="nav-14__nav-title">Work</span><span class="nav-14__nav-arrow">→</span></a>
      </li>
      <li>
        <a href="#"><span class="nav-14__nav-num">03</span><span class="nav-14__nav-title">Services</span><span class="nav-14__nav-arrow">→</span></a>
      </li>
      <li>
        <a href="#"><span class="nav-14__nav-num">04</span><span class="nav-14__nav-title">Journal</span><span class="nav-14__nav-arrow">→</span></a>
      </li>
      <li>
        <a href="#"><span class="nav-14__nav-num">05</span><span class="nav-14__nav-title">Contact</span><span class="nav-14__nav-arrow">→</span></a>
      </li>
    </ul>
    <div class="nav-14__overlay-footer">
      <div class="nav-14__social">
        <a href="#">Instagram</a>
        <a href="#">Behance</a>
        <a href="#">LinkedIn</a>
      </div>
      <div class="nav-14__contact">hello@<a href="#">forma.studio</a></div>
    </div>
  </div>
</div>
<div class="nav-14__content">
  <h1 style="font-family:'Bebas Neue',sans-serif; font-size:clamp(3rem,8vw,7rem); letter-spacing:0.04em; line-height:0.9; margin-bottom:2rem;">Full-Screen<br>Overlay Menu</h1>
  <p style="color:#6b5f4a; font-size:1.05rem; line-height:1.75; max-width:600px;">Click the hamburger icon to see the full-screen overlay slide down. The overlay covers the entire viewport and displays large typographic navigation links. Hover each link to see it accent-colored and shift right.</p>
</div>
```
## CSS
```css
.nav-14,
.nav-14 *,
.nav-14 *::before,
.nav-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-14 {
  --bg: #f0ede8;
  --text: #1a1612;
  --overlay: #1a1612;
  --overlay-text: #f0ede8;
  --accent: #e85d26;
  font-family: 'DM Sans', sans-serif;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 500;
}

.nav-14__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 2rem;
  position: relative;
  z-index: 510;
  transition: color 0.4s;
}

.nav-14__logo {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.6rem;
  letter-spacing: 0.1em;
  text-decoration: none;
  color: var(--text);
  transition: color 0.4s;
}

.nav-14.is-open .nav-14__logo {
  color: var(--overlay-text);
}

.nav-14__toggle {
  display: flex;
  flex-direction: column;
  gap: 6px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
  width: 44px;
  height: 44px;
  justify-content: center;
  border-radius: 50%;
  transition: background 0.2s;
}

.nav-14__toggle:hover {
  background: rgba(0,0,0,0.06);
}

.nav-14.is-open .nav-14__toggle:hover {
  background: rgba(255,255,255,0.1);
}

.nav-14__toggle span {
  display: block;
  width: 28px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.4s cubic-bezier(.4,0,.2,1), opacity 0.3s, background 0.4s, width 0.3s;
}

.nav-14.is-open .nav-14__toggle span {
  background: var(--overlay-text);
}

.nav-14.is-open .nav-14__toggle span:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.nav-14.is-open .nav-14__toggle span:nth-child(2) {
  opacity: 0;
  width: 0;
}

.nav-14.is-open .nav-14__toggle span:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}
/* Overlay */

.nav-14__overlay {
  position: fixed;
  inset: 0;
  background: var(--overlay);
  z-index: 505;
  display: flex;
  flex-direction: column;
  transform: translateY(-100%);
  transition: transform 0.6s cubic-bezier(.4,0,.2,1);
  padding: 100px 2.5rem 2.5rem;
}

.nav-14.is-open .nav-14__overlay {
  transform: translateY(0);
}

.nav-14__nav-links {
  list-style: none;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.nav-14__nav-links li {
  overflow: hidden;
  border-bottom: 1px solid rgba(240,237,232,0.1);
}

.nav-14__nav-links li:first-child {
  border-top: 1px solid rgba(240,237,232,0.1);
}

.nav-14__nav-links a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-decoration: none;
  padding: 1.25rem 0;
  transition: padding-left 0.25s;
}

.nav-14__nav-links a:hover {
  padding-left: 1rem;
}

.nav-14__nav-num {
  font-size: 0.7rem;
  font-weight: 600;
  color: rgba(240,237,232,0.3);
  letter-spacing: 0.1em;
  align-self: flex-start;
  padding-top: 0.5rem;
}

.nav-14__nav-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(2.5rem, 6vw, 5rem);
  color: var(--overlay-text);
  letter-spacing: 0.04em;
  line-height: 1;
  flex: 1;
  padding: 0 1rem;
  transition: color 0.2s;
}

.nav-14__nav-links a:hover .nav-14__nav-title {
  color: var(--accent);
}

.nav-14__nav-arrow {
  color: rgba(240,237,232,0.3);
  font-size: 1.5rem;
  transition: color 0.2s, transform 0.2s;
}

.nav-14__nav-links a:hover .nav-14__nav-arrow {
  color: var(--accent);
  transform: translateX(4px);
}

.nav-14__overlay-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(240,237,232,0.1);
}

.nav-14__social {
  display: flex;
  gap: 1.5rem;
}

.nav-14__social a {
  color: rgba(240,237,232,0.4);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  transition: color 0.2s;
}

.nav-14__social a:hover {
  color: var(--overlay-text);
}

.nav-14__contact {
  color: rgba(240,237,232,0.4);
  font-size: 0.8rem;
  letter-spacing: 0.04em;
}

.nav-14__contact a {
  color: var(--accent);
  text-decoration: none;
}

.nav-14__content {
  padding-top: 80px;
  padding: 100px 2rem 2rem;
  color: #1a1612;
}

@media (prefers-reduced-motion: reduce) {
  .nav-14__overlay {
    transition: none;
  }

  .nav-14__toggle span {
    transition: none;
  }

  .nav-14__nav-links a,
    .nav-14__logo,
    .nav-14__toggle span {
    transition: none;
  }
}
```

## JavaScript
```js
const nav = document.getElementById('nav14');
  const btn = document.getElementById('nav14Toggle');
  btn.addEventListener('click', function() {
    const isOpen = nav.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });
```
