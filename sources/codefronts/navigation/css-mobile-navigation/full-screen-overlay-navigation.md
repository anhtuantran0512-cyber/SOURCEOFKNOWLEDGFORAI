---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/full-screen-overlay-navigation/"
title: "Full-Screen Overlay Navigation"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "An editorial full-screen nav that expands via a circular clip-path reveal from the top-right corner."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Screen Overlay Navigation
Source: https://codefronts.com/navigation/css-mobile-navigation/full-screen-overlay-navigation/

An editorial full-screen nav that expands via a circular clip-path reveal from the top-right corner. Menu links stagger in with a slide-up entrance driven entirely by CSS sibling selectors.
## HTML
```html
<div class="mn-02">
  <input type="checkbox" id="mn-02-toggle">
  <label class="mn-02__btn" for="mn-02-toggle">
    <div class="mn-02__btn-lines">
      <span></span><span></span><span></span>
    </div>
  </label>
  <div class="mn-02__overlay">
    <span class="mn-02__overlay-label">Navigation</span>
    <ul class="mn-02__overlay-links">
      <li><a href="#"><span class="num">01</span> Work</a></li>
      <li><a href="#"><span class="num">02</span> About</a></li>
      <li><a href="#"><span class="num">03</span> Services</a></li>
      <li><a href="#"><span class="num">04</span> Journal</a></li>
      <li><a href="#"><span class="num">05</span> Contact</a></li>
    </ul>
    <div class="mn-02__overlay-footer">
      <a href="#">Twitter</a>
      <a href="#">Instagram</a>
      <a href="#">Dribbble</a>
    </div>
  </div>
  <div class="mn-02__page">
    <div class="mn-02__header">
      <div class="mn-02__logo">Studio<span>.</span></div>
    </div>
    <div class="mn-02__hero">
      <div class="mn-02__eyebrow">Creative Agency</div>
      <h1>We craft digital experiences</h1>
      <p>Award-winning design studio specializing in brand identity and digital products.</p>
      <a href="#" class="mn-02__cta">View Our Work →</a>
    </div>
  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: 'Segoe UI', sans-serif;
}

.mn-02 {
  --bg: #f7f3ee;
  --overlay-bg: #1c1917;
  --accent: #d97706;
  --text-dark: #1c1917;
  --text-light: #f7f3ee;
  --muted: #78716c;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.6);
}

.mn-02 #mn-02-toggle {
  display: none;
}
/* Overlay panel */

.mn-02__overlay {
  position: absolute;
  inset: 0;
  background: var(--overlay-bg);
  z-index: 20;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 40px 36px;
  clip-path: circle(0% at calc(100% - 36px) 36px);
  transition: clip-path 0.6s cubic-bezier(0.77, 0, 0.175, 1);
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__overlay {
  clip-path: circle(150% at calc(100% - 36px) 36px);
}

.mn-02__overlay-links {
  list-style: none;
  margin-top: 40px;
}

.mn-02__overlay-links li {
  overflow: hidden;
  margin-bottom: 4px;
}

.mn-02__overlay-links a {
  display: flex;
  align-items: baseline;
  gap: 16px;
  color: var(--text-light);
  text-decoration: none;
  font-size: 38px;
  font-weight: 700;
  letter-spacing: -1px;
  line-height: 1.2;
  padding: 8px 0;
  transition: color 0.2s;
  transform: translateY(100%);
  opacity: 0;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s, color 0.2s;
}

.mn-02__overlay-links a:hover {
  color: var(--accent);
}

.mn-02__overlay-links a .num {
  font-size: 13px;
  font-weight: 400;
  color: var(--muted);
  letter-spacing: 0;
  min-width: 28px;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__overlay .mn-02__overlay-links a {
  transform: translateY(0);
  opacity: 1;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__overlay .mn-02__overlay-links li:nth-child(1) a {
  transition-delay: 0.15s;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__overlay .mn-02__overlay-links li:nth-child(2) a {
  transition-delay: 0.22s;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__overlay .mn-02__overlay-links li:nth-child(3) a {
  transition-delay: 0.29s;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__overlay .mn-02__overlay-links li:nth-child(4) a {
  transition-delay: 0.36s;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__overlay .mn-02__overlay-links li:nth-child(5) a {
  transition-delay: 0.43s;
}

.mn-02__overlay-footer {
  margin-top: 48px;
  display: flex;
  gap: 24px;
}

.mn-02__overlay-footer a {
  color: var(--muted);
  text-decoration: none;
  font-size: 13px;
  transition: color 0.2s;
}

.mn-02__overlay-footer a:hover {
  color: var(--text-light);
}
/* Close / hamburger button */

.mn-02__btn {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 30;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--overlay-bg);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__btn {
  background: rgba(255,255,255,0.1);
}

.mn-02__btn-lines {
  width: 22px;
  height: 14px;
  position: relative;
}

.mn-02__btn-lines span {
  position: absolute;
  left: 0;
  width: 100%;
  height: 2px;
  background: #fff;
  border-radius: 2px;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: center;
}

.mn-02__btn-lines span:nth-child(1) {
  top: 0;
}

.mn-02__btn-lines span:nth-child(2) {
  top: 50%;
  transform: translateY(-50%);
}

.mn-02__btn-lines span:nth-child(3) {
  bottom: 0;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__btn .mn-02__btn-lines span:nth-child(1) {
  top: 50%;
  transform: translateY(-50%) rotate(45deg);
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__btn .mn-02__btn-lines span:nth-child(2) {
  opacity: 0;
}

.mn-02 #mn-02-toggle:checked ~ .mn-02__btn .mn-02__btn-lines span:nth-child(3) {
  bottom: 50%;
  transform: translateY(50%) rotate(-45deg);
}

.mn-02__overlay-label {
  color: rgba(255,255,255,0.3);
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
}
/* Page */

.mn-02__page {
  padding: 0;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.mn-02__header {
  padding: 24px 20px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mn-02__logo {
  font-size: 20px;
  font-weight: 800;
  color: var(--text-dark);
  letter-spacing: -0.5px;
}

.mn-02__logo span {
  color: var(--accent);
}

.mn-02__hero {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 32px 24px;
}

.mn-02__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 12px;
}

.mn-02__hero h1 {
  font-size: 38px;
  font-weight: 800;
  color: var(--text-dark);
  letter-spacing: -1.5px;
  line-height: 1.1;
  margin-bottom: 16px;
}

.mn-02__hero p {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.7;
  max-width: 280px;
}

.mn-02__cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 24px;
  background: var(--text-dark);
  color: var(--text-light);
  font-size: 14px;
  font-weight: 600;
  padding: 12px 24px;
  border-radius: 100px;
  text-decoration: none;
  width: fit-content;
}

@media (prefers-reduced-motion: reduce) {
  .mn-02__overlay,
    .mn-02__overlay-links a,
    .mn-02__btn-lines span {
    transition: none;
  }
}
```
