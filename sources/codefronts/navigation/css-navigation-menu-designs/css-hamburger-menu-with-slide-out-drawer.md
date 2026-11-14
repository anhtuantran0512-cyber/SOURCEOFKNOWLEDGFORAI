---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-hamburger-menu-with-slide-out-drawer/"
title: "CSS Hamburger Menu with Slide-Out Drawer"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A mobile-first hamburger menu that reveals a full-height slide-out navigation drawer using only a hidden checkbox."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hamburger Menu with Slide-Out Drawer
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-hamburger-menu-with-slide-out-drawer/

A mobile-first hamburger menu that reveals a full-height slide-out navigation drawer using only a hidden checkbox. The three-bar icon morphs into an X when active, and a backdrop overlay fades in behind the open drawer.
## HTML
```html
<div class="nav-04">
  <input type="checkbox" id="nav-04-toggle">
  <nav class="nav-04__bar">
    <div class="nav-04__logo">Mo<span>ve</span></div>
    <label for="nav-04-toggle" class="nav-04__ham" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </nav>
  <label for="nav-04-toggle" class="nav-04__overlay"></label>
  <div class="nav-04__drawer" role="dialog" aria-label="Navigation drawer">
    <div class="nav-04__drawer-head">
      <div class="nav-04__drawer-logo">Mo<span>ve</span></div>
      <label for="nav-04-toggle" class="nav-04__close" aria-label="Close menu">
        <svg viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg>
      </label>
    </div>
    <ul class="nav-04__drawer-links">
      <li class="nav-04__active">
        <a href="#">
          <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          Home
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
          Products
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>
          Pricing
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg>
          Docs
        </a>
      </li>
      <div class="nav-04__drawer-divider"></div>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
          Community
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
          Support
        </a>
      </li>
    </ul>
    <div class="nav-04__drawer-footer">
      <a href="#" class="nav-04__drawer-cta">Get started free →</a>
    </div>
  </div>
  <div class="nav-04__hero">
    <h1>CSS Hamburger Menu with Slide-Out Drawer</h1>
    <p>A hidden <code>&lt;input type="checkbox"&gt;</code> toggled by the hamburger label. The drawer uses <code>translateX</code> and the overlay uses <code>opacity</code> transitions — zero JavaScript.</p>
    <span class="nav-04__instruction">
      <svg viewBox="0 0 24 24"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      Tap the hamburger icon top-right
    </span>
  </div>
</div>
```
## CSS
```css
.nav-04,
.nav-04 *,
.nav-04 *::before,
.nav-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-04 ::selection {
  background: #f97316;
  color: #fff;
}

.nav-04 {
  --bg: #fffbf7;
  --surface: #ffffff;
  --drawer: #1c1917;
  --border: #fde8d8;
  --text: #1c1917;
  --muted: #78716c;
  --accent: #f97316;
  --accent2: #fb923c;
  font-family: 'Outfit',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
}
/* hidden checkbox toggle */

#nav-04-toggle {
  display: none;
}

.nav-04__bar {
  background: var(--surface);
  border-bottom: 2px solid var(--border);
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 200;
}

.nav-04__logo {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.03em;
}

.nav-04__logo span {
  color: var(--accent);
}
/* hamburger button */

.nav-04__ham {
  width: 44px;
  height: 44px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  border-radius: 10px;
  transition: background .18s;
  user-select: none;
}

.nav-04__ham:hover {
  background: var(--border);
}

.nav-04__ham span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform .3s cubic-bezier(.23,1,.32,1),opacity .2s,width .3s;
  transform-origin: center;
}
/* open state — morph to X */

#nav-04-toggle:checked ~ .nav-04__bar .nav-04__ham span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-04-toggle:checked ~ .nav-04__bar .nav-04__ham span:nth-child(2) {
  opacity: 0;
  width: 0;
}

#nav-04-toggle:checked ~ .nav-04__bar .nav-04__ham span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
/* overlay */

.nav-04__overlay {
  position: fixed;
  inset: 0;
  z-index: 150;
  background: rgba(0,0,0,0);
  pointer-events: none;
  transition: background .35s ease;
}

#nav-04-toggle:checked ~ .nav-04__overlay {
  background: rgba(0,0,0,.45);
  pointer-events: auto;
}
/* drawer */

.nav-04__drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 300px;
  z-index: 160;
  background: var(--drawer);
  transform: translateX(100%);
  transition: transform .35s cubic-bezier(.23,1,.32,1);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

#nav-04-toggle:checked ~ .nav-04__overlay ~ .nav-04__drawer {
  transform: translateX(0);
}

.nav-04__drawer-head {
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255,255,255,.07);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-04__drawer-logo {
  font-size: 1.2rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: -.02em;
}

.nav-04__drawer-logo span {
  color: var(--accent);
}

.nav-04__close {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  cursor: pointer;
  display: grid;
  place-items: center;
  background: rgba(255,255,255,.07);
  transition: background .18s;
}

.nav-04__close:hover {
  background: rgba(255,255,255,.14);
}

.nav-04__close svg {
  width: 18px;
  height: 18px;
  stroke: #fff;
  fill: none;
  stroke-width: 2;
}

.nav-04__drawer-links {
  padding: 16px;
  flex: 1;
  list-style: none;
}

.nav-04__drawer-links li a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 14px;
  color: rgba(255,255,255,.7);
  text-decoration: none;
  font-size: .9375rem;
  font-weight: 500;
  border-radius: 10px;
  transition: background .18s,color .18s;
}

.nav-04__drawer-links li a:hover {
  background: rgba(255,255,255,.06);
  color: #fff;
}

.nav-04__drawer-links li a svg {
  width: 18px;
  height: 18px;
  stroke: currentColor;
  fill: none;
  stroke-width: 1.75;
  flex-shrink: 0;
  opacity: .6;
}

.nav-04__drawer-links .nav-04__active a {
  color: #fff;
  background: rgba(249,115,22,.12);
}

.nav-04__drawer-links .nav-04__active a svg {
  color: var(--accent);
  opacity: 1;
}

.nav-04__drawer-divider {
  height: 1px;
  background: rgba(255,255,255,.06);
  margin: 8px 14px;
}

.nav-04__drawer-footer {
  padding: 20px 16px;
  border-top: 1px solid rgba(255,255,255,.07);
}

.nav-04__drawer-cta {
  display: block;
  width: 100%;
  padding: 12px;
  background: var(--accent);
  color: #fff;
  border-radius: 10px;
  text-align: center;
  text-decoration: none;
  font-weight: 600;
  font-size: .9rem;
  transition: opacity .18s;
}

.nav-04__drawer-cta:hover {
  opacity: .88;
}
/* hero */

.nav-04__hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 100px 24px;
  text-align: center;
}

.nav-04__hero h1 {
  font-size: clamp(2rem,5vw,3.25rem);
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.03em;
  max-width: 560px;
  margin-bottom: 14px;
  line-height: 1.2;
}

.nav-04__hero p {
  font-size: 1rem;
  color: var(--muted);
  max-width: 420px;
  line-height: 1.7;
}

.nav-04__instruction {
  margin-top: 32px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--surface);
  border: 2px solid var(--border);
  padding: 10px 18px;
  border-radius: 100px;
  font-size: .875rem;
  font-weight: 600;
  color: var(--accent);
}

.nav-04__instruction svg {
  width: 18px;
  height: 18px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}

@media (prefers-reduced-motion: reduce) {
  .nav-04__ham span,
    .nav-04__drawer,
    .nav-04__overlay {
    transition: none;
  }
}
```
