---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/checkbox-hack-mobile-nav-dropdown/"
title: "Checkbox Hack Mobile Nav Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A pure CSS hamburger-to-X mobile nav using the checkbox hack — an invisible input toggled by a label drives the entire menu open/close state."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Checkbox Hack Mobile Nav Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/checkbox-hack-mobile-nav-dropdown/

A pure CSS hamburger-to-X mobile nav using the checkbox hack — an invisible input toggled by a label drives the entire menu open/close state.
## HTML
```html
<div class="dd-10">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <input type="checkbox" id="dd-10-toggle" class="dd-10__input">
  <header class="dd-10__header">
    <a href="#" class="dd-10__brand">Forge</a>
    <label for="dd-10-toggle" class="dd-10__hamburger" aria-label="Toggle menu">
      <span></span>
      <span></span>
      <span></span>
    </label>
  </header>
  <nav class="dd-10__menu" role="navigation" aria-label="Main navigation">
    <a href="#" class="dd-10__link">Work</a>
    <a href="#" class="dd-10__link">Services</a>
    <a href="#" class="dd-10__link">About</a>
    <a href="#" class="dd-10__link">Journal</a>
    <a href="#" class="dd-10__link dd-10__link--cta">Start a Project</a>
  </nav>
</div>
```
## CSS
```css
.dd-10,
.dd-10 *,
.dd-10 *::before,
.dd-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-10 ::selection {
  background: #111827;
  color: #f9fafb;
}

.dd-10 {
  --ink: #111827;
  --surface: #fff;
  --accent: #f59e0b;
  --border: #f3f4f6;
  font-family: 'Space Grotesk', sans-serif;
  min-height: 380px;
  display: flex;
  flex-direction: column;
  background: linear-gradient(160deg, #fff 0%, #f9fafb 100%);
  max-width: 440px;
  margin: 0 auto;
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0,0,0,.08);
}
/* hidden checkbox */

.dd-10__input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
  pointer-events: none;
}

.dd-10__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 20px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
  position: relative;
  z-index: 10;
}

.dd-10__brand {
  font-size: 20px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  letter-spacing: -0.5px;
}

.dd-10__hamburger {
  width: 40px;
  height: 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  border-radius: 8px;
  transition: background 0.15s;
  padding: 8px;
}

.dd-10__hamburger:hover {
  background: #f9fafb;
}

.dd-10__hamburger span {
  display: block;
  width: 20px;
  height: 2px;
  background: var(--ink);
  border-radius: 2px;
  transition: transform 0.3s ease, opacity 0.2s ease;
  transform-origin: center;
}
/* checked: hamburger → X */

.dd-10__input:checked ~ .dd-10__header .dd-10__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.dd-10__input:checked ~ .dd-10__header .dd-10__hamburger span:nth-child(2) {
  opacity: 0;
  transform: scaleX(0);
}

.dd-10__input:checked ~ .dd-10__header .dd-10__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
/* menu panel */

.dd-10__menu {
  display: flex;
  flex-direction: column;
  background: var(--surface);
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.38s ease, opacity 0.25s ease;
}

.dd-10__input:checked ~ .dd-10__menu {
  max-height: 400px;
  opacity: 1;
}

.dd-10__link {
  display: block;
  padding: 18px 24px;
  color: var(--ink);
  text-decoration: none;
  font-size: 22px;
  font-weight: 700;
  border-bottom: 1px solid var(--border);
  letter-spacing: -0.5px;
  transition: color 0.15s, padding-left 0.2s ease;
}

.dd-10__link:hover {
  color: var(--accent);
  padding-left: 32px;
}

.dd-10__link--cta {
  color: var(--accent);
  font-size: 15px;
  letter-spacing: 0;
  font-weight: 600;
  border-bottom: none;
  padding: 20px 24px;
}

.dd-10__link--cta:hover {
  color: #d97706;
  padding-left: 32px;
}

@media (prefers-reduced-motion: reduce) {
  .dd-10__menu,
    .dd-10__hamburger span,
    .dd-10__link {
    transition: none;
  }
}
```
