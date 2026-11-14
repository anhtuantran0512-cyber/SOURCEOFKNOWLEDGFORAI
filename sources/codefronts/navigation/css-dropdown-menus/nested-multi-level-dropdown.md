---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/nested-multi-level-dropdown/"
title: "Nested Multi-Level Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A three-level deep nested dropdown where each submenu flies out to the right of its parent item, triggered purely by CSS hover on sibling selectors."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nested Multi-Level Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/nested-multi-level-dropdown/

A three-level deep nested dropdown where each submenu flies out to the right of its parent item, triggered purely by CSS hover on sibling selectors.
## HTML
```html
<div class="dd-11">
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <nav class="dd-11__nav">
    <ul class="dd-11__list dd-11__list--root">
      <li class="dd-11__item">
        <a href="#" class="dd-11__link">Home</a>
      </li>
      <li class="dd-11__item dd-11__item--has-sub">
        <a href="#" class="dd-11__link">Products</a>
        <ul class="dd-11__sub">
          <li class="dd-11__item dd-11__item--has-sub">
            <a href="#" class="dd-11__link">Software</a>
            <ul class="dd-11__sub">
              <li class="dd-11__item"><a href="#" class="dd-11__link">Web App</a></li>
              <li class="dd-11__item"><a href="#" class="dd-11__link">Desktop</a></li>
              <li class="dd-11__item"><a href="#" class="dd-11__link">Mobile</a></li>
            </ul>
          </li>
          <li class="dd-11__item dd-11__item--has-sub">
            <a href="#" class="dd-11__link">Hardware</a>
            <ul class="dd-11__sub">
              <li class="dd-11__item"><a href="#" class="dd-11__link">Devices</a></li>
              <li class="dd-11__item"><a href="#" class="dd-11__link">Accessories</a></li>
            </ul>
          </li>
          <li class="dd-11__item"><a href="#" class="dd-11__link">Services</a></li>
        </ul>
      </li>
      <li class="dd-11__item dd-11__item--has-sub">
        <a href="#" class="dd-11__link">Company</a>
        <ul class="dd-11__sub">
          <li class="dd-11__item"><a href="#" class="dd-11__link">About</a></li>
          <li class="dd-11__item"><a href="#" class="dd-11__link">Careers</a></li>
          <li class="dd-11__item dd-11__item--has-sub">
            <a href="#" class="dd-11__link">Press</a>
            <ul class="dd-11__sub">
              <li class="dd-11__item"><a href="#" class="dd-11__link">News</a></li>
              <li class="dd-11__item"><a href="#" class="dd-11__link">Media Kit</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li class="dd-11__item"><a href="#" class="dd-11__link">Contact</a></li>
    </ul>
  </nav>
</div>
```
## CSS
```css
.dd-11,
.dd-11 *,
.dd-11 *::before,
.dd-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-11 ::selection {
  background: #1d4ed8;
  color: #eff6ff;
}

.dd-11 {
  --brand: #1d4ed8;
  --surface: #fff;
  --text: #1e293b;
  --muted: #64748b;
  --border: #e2e8f0;
  --hover: #eff6ff;
  font-family: 'Manrope', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 20px;
  background: linear-gradient(135deg, #eff6ff 0%, #e0e7ff 100%);
}

.dd-11__nav {
  position: relative;
  z-index: 100;
}

.dd-11__list {
  list-style: none;
  display: flex;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 6px;
  gap: 2px;
  box-shadow: 0 4px 20px rgba(0,0,0,.07);
}

.dd-11__list--root > .dd-11__item {
  position: relative;
}
/* submenus */

.dd-11__sub {
  list-style: none;
  position: absolute;
  top: 0;
  left: 100%;
  min-width: 170px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  box-shadow: 0 8px 32px rgba(0,0,0,.12);
  padding: 5px;
  display: flex;
  flex-direction: column;
  gap: 1px;
  opacity: 0;
  pointer-events: none;
  transform: translateX(4px);
  transition: opacity 0.2s ease, transform 0.2s ease;
  z-index: 10;
}
/* Hover bridges — must be on the .dd-11__item (the :hover target),
   NOT on .dd-11__sub because the sub has pointer-events:none at rest
   so its ::before is unreachable. Nested items extend their right
   edge by an invisible strip covering the gap to the submenu. */

.dd-11__item {
  position: relative;
}

.dd-11__item:not(.dd-11__list--root > .dd-11__item)::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 100%;
  width: 10px;
}
/* Root-level items drop submenus DOWNWARD, so bridge goes BELOW. */

.dd-11__list--root > .dd-11__item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 8px;
}
/* first level drops down */

.dd-11__list--root > .dd-11__item > .dd-11__sub {
  top: calc(100% + 8px);
  left: 0;
  transform: translateY(-4px);
}

.dd-11__list--root > .dd-11__item:hover > .dd-11__sub {
  transform: translateY(0);
}

.dd-11__item:hover > .dd-11__sub {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(0);
}

.dd-11__list--root > .dd-11__item:hover > .dd-11__sub {
  opacity: 1;
  pointer-events: auto;
}

.dd-11__link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 14px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 500;
  white-space: nowrap;
  transition: background 0.15s, color 0.15s;
  gap: 8px;
}

.dd-11__link:hover {
  background: var(--hover);
  color: var(--brand);
}
/* nested indicator arrow */

.dd-11__item--has-sub > .dd-11__link::after {
  content: '›';
  font-size: 14px;
  font-weight: 400;
  color: var(--muted);
  margin-left: auto;
}
/* root level items use down arrow */

.dd-11__list--root > .dd-11__item--has-sub > .dd-11__link::after {
  content: '⌄';
  font-size: 11px;
}

.dd-11__list--root .dd-11__link {
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .dd-11__sub {
    transition: none;
  }
}
```
