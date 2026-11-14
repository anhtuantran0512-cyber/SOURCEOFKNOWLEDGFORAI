---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-full-screen-overlay-navigation/"
title: "CSS Full-Screen Overlay Navigation"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A dramatic full-screen navigation overlay that covers the entire viewport with a dark semi-transparent background."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Full-Screen Overlay Navigation
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-full-screen-overlay-navigation/

A dramatic full-screen navigation overlay that covers the entire viewport with a dark semi-transparent background. Menu links animate in with a staggered slide-up entrance, creating a cinematic reveal effect perfect for portfolio and creative agency sites.
## HTML
```html
<div class="nav-05">
  <input type="checkbox" id="nav-05-toggle">
  <nav class="nav-05__bar">
    <a href="#" class="nav-05__logo">Vol<em>ta</em></a>
    <label for="nav-05-toggle" class="nav-05__btn" aria-label="Open menu">
      <span></span><span></span><span></span>
    </label>
  </nav>
  <div class="nav-05__overlay" role="dialog" aria-label="Full screen navigation">
    <ul class="nav-05__nav-list">
      <li><a href="#"><span class="nav-05__num">01</span>Work</a></li>
      <li><a href="#"><span class="nav-05__num">02</span>Studio</a></li>
      <li><a href="#"><span class="nav-05__num">03</span>Services</a></li>
      <li><a href="#"><span class="nav-05__num">04</span>Journal</a></li>
      <li><a href="#"><span class="nav-05__num">05</span>Contact</a></li>
    </ul>
    <div class="nav-05__overlay-footer">
      <div class="nav-05__overlay-social">
        <a href="#">Twitter</a>
        <a href="#">Dribbble</a>
        <a href="#">Instagram</a>
        <a href="#">LinkedIn</a>
      </div>
      <a href="#" class="nav-05__overlay-cta">Start a project →</a>
    </div>
  </div>
  <div class="nav-05__hero">
    <h1>Design <span>beyond</span><br>the ordinary</h1>
    <p>Open the menu top-right. The overlay slides in using <code>translateY(-100%)</code> — no JavaScript, just a checkbox toggle and CSS transitions.</p>
  </div>
</div>
```
## CSS
```css
.nav-05,
.nav-05 *,
.nav-05 *::before,
.nav-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-05 ::selection {
  background: #d946ef;
  color: #fff;
}

#nav-05-toggle {
  display: none;
}

.nav-05 {
  --bg: #09090b;
  --surface: #18181b;
  --text: #fafafa;
  --muted: #a1a1aa;
  --accent: #d946ef;
  --accent2: #e879f9;
  font-family: 'Syne',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
}

.nav-05__bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 300;
  padding: 24px 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-05__logo {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.04em;
  text-decoration: none;
  z-index: 310;
  position: relative;
}

.nav-05__logo em {
  color: var(--accent);
  font-style: normal;
}
/* open btn */

.nav-05__btn {
  z-index: 310;
  position: relative;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 10px;
  transition: background .18s;
  user-select: none;
}

.nav-05__btn:hover {
  background: rgba(255,255,255,.1);
}

.nav-05__btn span {
  display: block;
  border-radius: 2px;
  background: var(--text);
  transition: transform .35s cubic-bezier(.23,1,.32,1),opacity .25s,width .35s;
}

.nav-05__btn span:nth-child(1) {
  width: 24px;
  height: 2px;
}

.nav-05__btn span:nth-child(2) {
  width: 16px;
  height: 2px;
}

.nav-05__btn span:nth-child(3) {
  width: 20px;
  height: 2px;
}

#nav-05-toggle:checked ~ .nav-05__bar .nav-05__btn span:nth-child(1) {
  transform: translateY(6px) rotate(45deg);
  width: 24px;
}

#nav-05-toggle:checked ~ .nav-05__bar .nav-05__btn span:nth-child(2) {
  opacity: 0;
  width: 0;
}

#nav-05-toggle:checked ~ .nav-05__bar .nav-05__btn span:nth-child(3) {
  transform: translateY(-6px) rotate(-45deg);
  width: 24px;
}
/* full-screen overlay */

.nav-05__overlay {
  position: fixed;
  inset: 0;
  z-index: 200;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px 60px;
  transform: translateY(-100%);
  transition: transform .5s cubic-bezier(.77,0,.175,1);
  overflow: hidden;
}

#nav-05-toggle:checked ~ .nav-05__overlay {
  transform: translateY(0);
}

.nav-05__overlay::before {
  content: '';
  position: absolute;
  bottom: -200px;
  right: -200px;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(217,70,239,.12) 0%,transparent 70%);
  pointer-events: none;
}

.nav-05__nav-list {
  list-style: none;
  margin-bottom: 48px;
}

.nav-05__nav-list li {
  overflow: hidden;
}

.nav-05__nav-list li a {
  display: inline-flex;
  align-items: center;
  gap: 16px;
  font-size: clamp(2.5rem,7vw,5rem);
  font-weight: 800;
  color: rgba(255,255,255,.15);
  text-decoration: none;
  letter-spacing: -.04em;
  line-height: 1.15;
  transition: color .2s ease;
  padding: 4px 0;
}

.nav-05__nav-list li a:hover {
  color: var(--text);
}

.nav-05__nav-list li a .nav-05__num {
  font-size: .875rem;
  font-weight: 600;
  color: var(--accent);
  letter-spacing: .06em;
  margin-top: 4px;
  opacity: 0;
  transition: opacity .2s;
}

.nav-05__nav-list li a:hover .nav-05__num {
  opacity: 1;
}

.nav-05__overlay-footer {
  display: flex;
  align-items: center;
  gap: 48px;
  flex-wrap: wrap;
}

.nav-05__overlay-social {
  display: flex;
  gap: 16px;
}

.nav-05__overlay-social a {
  font-size: .875rem;
  color: var(--muted);
  text-decoration: none;
  font-weight: 600;
  transition: color .18s;
}

.nav-05__overlay-social a:hover {
  color: var(--text);
}

.nav-05__overlay-cta {
  padding: 12px 28px;
  background: var(--accent);
  color: #fff;
  border-radius: 100px;
  text-decoration: none;
  font-weight: 700;
  font-size: .9375rem;
  transition: opacity .18s;
}

.nav-05__overlay-cta:hover {
  opacity: .85;
}
/* page content */

.nav-05__hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 100px 24px;
}

.nav-05__hero h1 {
  font-size: clamp(2.5rem,8vw,6rem);
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.05em;
  line-height: 1;
  margin-bottom: 20px;
}

.nav-05__hero h1 span {
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.nav-05__hero p {
  font-size: 1.0625rem;
  color: var(--muted);
  max-width: 440px;
  line-height: 1.65;
}

@media (prefers-reduced-motion: reduce) {
  .nav-05__overlay,
    .nav-05__btn span {
    transition: none;
  }
}
```
