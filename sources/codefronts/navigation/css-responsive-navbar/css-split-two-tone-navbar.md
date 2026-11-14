---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-split-two-tone-navbar/"
title: "CSS Split Two-Tone Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Split-color navbar with dark left branding panel and light right links panel — bold editorial contrast layout."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Split Two-Tone Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-split-two-tone-navbar/

Split-color navbar with dark left branding panel and light right links panel — bold editorial contrast layout.
## HTML
```html
<div class="nav-09">
  <div class="nav-09__left">
    <a href="#" class="nav-09__logo">Geo<span>metric</span></a>
  </div>
  <div class="nav-09__center">
    <ul class="nav-09__links">
      <li><a href="#" class="is-active">Studio</a></li>
      <li><a href="#">Work</a></li>
      <li><a href="#">Process</a></li>
      <li><a href="#">Journal</a></li>
    </ul>
  </div>
  <div class="nav-09__right">
    <button class="nav-09__btn nav-09__btn--ghost">Log in</button>
    <button class="nav-09__btn nav-09__btn--dark">Start project</button>
  </div>
</div>
<input type="checkbox" id="nav-09-toggle">
<div class="nav-09__mobile-bar">
  <a href="#" class="nav-09__mobile-logo">Geo<span>metric</span></a>
  <label for="nav-09-toggle" class="nav-09__hamburger" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </label>
</div>
<div class="nav-09__mobile-menu">
  <a href="#">Studio</a>
  <a href="#">Work</a>
  <a href="#">Process</a>
  <a href="#">Journal</a>
  <a href="#">Start project →</a>
</div>
<div style="padding:4rem 2rem; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:700; letter-spacing:-0.03em; margin-bottom:1rem;">Split Two-Tone Navbar</h1>
  <p style="color:#6b7280; font-size:1.1rem; line-height:1.7;">The angled divider between the dark and yellow sections is achieved with <code>clip-path: polygon()</code> — no pseudo-elements, no borders. The skew angle is 24px offset on the left and right panels.</p>
</div>
```
## CSS
```css
.nav-09,
.nav-09 *,
.nav-09 *::before,
.nav-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-09 {
  --left-bg: #1a1a2e;
  --right-bg: #f7c948;
  --left-text: #f0eeff;
  --right-text: #1a1a2e;
  --accent: #f7c948;
  font-family: 'Space Grotesk', sans-serif;
  display: grid;
  grid-template-columns: auto 1fr auto;
  height: 68px;
  position: sticky;
  top: 0;
  z-index: 100;
  overflow: hidden;
}

.nav-09__left {
  background: var(--left-bg);
  display: flex;
  align-items: center;
  padding: 0 2.5rem;
  clip-path: polygon(0 0, 100% 0, calc(100% - 24px) 100%, 0 100%);
  min-width: 220px;
}

.nav-09__logo {
  font-weight: 700;
  font-size: 1.2rem;
  color: var(--left-text);
  text-decoration: none;
  letter-spacing: -0.02em;
  white-space: nowrap;
}

.nav-09__logo span {
  color: var(--accent);
}

.nav-09__center {
  background: var(--left-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
}

.nav-09__links {
  display: flex;
  list-style: none;
  gap: 0;
}

.nav-09__links a {
  display: block;
  color: rgba(240,238,255,0.6);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0.5rem 1.1rem;
  border-radius: 6px;
  transition: color 0.2s, background 0.2s;
}

.nav-09__links a:hover {
  color: var(--left-text);
  background: rgba(255,255,255,0.08);
}

.nav-09__links a.is-active {
  color: var(--accent);
  font-weight: 600;
}

.nav-09__right {
  background: var(--right-bg);
  display: flex;
  align-items: center;
  padding: 0 2rem 0 2.5rem;
  gap: 0.75rem;
  clip-path: polygon(24px 0, 100% 0, 100% 100%, 0 100%);
}

.nav-09__btn {
  padding: 0.45rem 1.2rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  font-family: inherit;
  transition: all 0.2s;
}

.nav-09__btn--ghost {
  background: rgba(26,26,46,0.1);
  color: var(--right-text);
  border: 1.5px solid rgba(26,26,46,0.2);
}

.nav-09__btn--ghost:hover {
  background: rgba(26,26,46,0.18);
}

.nav-09__btn--dark {
  background: var(--left-bg);
  color: var(--left-text);
}

.nav-09__btn--dark:hover {
  background: #2a2a4e;
  transform: translateY(-1px);
}
/* Mobile */

#nav-09-toggle {
  display: none;
}

.nav-09__mobile-bar {
  display: none;
  position: sticky;
  top: 0;
  z-index: 100;
  background: #1a1a2e;
  height: 60px;
  padding: 0 1.5rem;
  align-items: center;
  justify-content: space-between;
}

.nav-09__mobile-logo {
  font-weight: 700;
  font-size: 1.1rem;
  color: #f0eeff;
  text-decoration: none;
  letter-spacing: -0.02em;
}

.nav-09__mobile-logo span {
  color: #f7c948;
}

.nav-09__hamburger {
  display: flex;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  border: none;
  background: transparent;
  padding: 8px;
}

.nav-09__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: #f0eeff;
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-09-toggle:checked ~ .nav-09__mobile-bar .nav-09__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

#nav-09-toggle:checked ~ .nav-09__mobile-bar .nav-09__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-09-toggle:checked ~ .nav-09__mobile-bar .nav-09__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-09__mobile-menu {
  display: none;
  flex-direction: column;
  background: #1a1a2e;
  padding: 0.75rem 1.5rem 1.25rem;
  position: sticky;
  top: 60px;
  z-index: 99;
  border-bottom: 3px solid #f7c948;
}

.nav-09__mobile-menu a {
  display: block;
  color: rgba(240,238,255,0.7);
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  padding: 0.65rem 0.5rem;
  border-radius: 6px;
  transition: color 0.2s, background 0.2s;
}

.nav-09__mobile-menu a:hover {
  color: #f7c948;
  background: rgba(247,201,72,0.08);
  padding-left: 1rem;
}

.nav-09__mobile-menu a:last-child {
  color: #f7c948;
  font-weight: 700;
  margin-top: 0.5rem;
}

#nav-09-toggle:checked ~ .nav-09__mobile-menu {
  display: flex;
}

@media (max-width: 768px) {
  .nav-09 {
    display: none;
  }

  .nav-09__mobile-bar {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-09__btn,
    .nav-09__links a {
    transition: none;
  }

  .nav-09__hamburger span {
    transition: none;
  }

  .nav-09__mobile-menu a {
    transition: none;
  }
}
```
