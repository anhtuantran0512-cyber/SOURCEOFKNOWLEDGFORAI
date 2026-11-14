---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/breadcrumb-bar-with-built-in-dropdown-sibling-menus/"
title: "Breadcrumb Bar with Built-In Dropdown Sibling Menus"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A power-navigation breadcrumb where intermediate crumbs reveal a dropdown of sibling pages on hover AND focus — jump sideways to any peer section without…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Breadcrumb Bar with Built-In Dropdown Sibling Menus
Source: https://codefronts.com/navigation/css-breadcrumbs/breadcrumb-bar-with-built-in-dropdown-sibling-menus/

A power-navigation breadcrumb where intermediate crumbs reveal a dropdown of sibling pages on hover AND focus — jump sideways to any peer section without going back up the tree. Built with the native <details>/<summary> disclosure so it's keyboard-accessible and JS-free, with a modern popover-style panel.
## HTML
```html
<nav class="bc-10" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li class="bc-10__has">
      <details open>
        <summary>Guides<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></summary>
        <div class="bc-10__menu" role="group" aria-label="Sibling sections">
          <a href="#">Tutorials</a><a href="#">References</a><a href="#">Recipes</a><a href="#">Changelog</a>
        </div>
      </details>
    </li>
    <li class="bc-10__has">
      <details>
        <summary>CSS<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></summary>
        <div class="bc-10__menu" role="group" aria-label="Sibling sections">
          <a href="#">HTML</a><a href="#">JavaScript</a><a href="#">Accessibility</a>
        </div>
      </details>
    </li>
    <li><a href="#" aria-current="page">Dropdown Breadcrumbs</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-10 {
  display: grid;
  width: 100%;
  --accent: oklch(0.55 0.15 265);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.98 0.004 265);
  min-height: 100vh;
  place-items: center;
}

.bc-10 * {
  box-sizing: border-box;
}

.bc-10 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-10 li {
  display: flex;
  align-items: center;
  position: relative;
}

.bc-10 li + li::before {
  content: "›";
  margin: 0 6px;
  color: oklch(0.72 0.02 265);
}

.bc-10 a {
  padding: 6px 8px;
  border-radius: 7px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.48 0.08 265);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.bc-10 a:hover {
  color: oklch(0.36 0.13 265);
  background: oklch(0.94 0.02 265);
}

.bc-10 a:focus-visible,
.bc-10 summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-10 li[aria-current="page"] a {
  color: oklch(0.28 0.02 265);
  font-weight: 700;
}

.bc-10 summary {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 6px 8px;
  border-radius: 7px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.48 0.08 265);
  cursor: pointer;
  list-style: none;
  transition: background-color .15s ease,color .15s ease;
}

.bc-10 summary::-webkit-details-marker {
  display: none;
}

.bc-10 summary:hover {
  color: oklch(0.36 0.13 265);
  background: oklch(0.94 0.02 265);
}

.bc-10 summary svg {
  width: 13px;
  height: 13px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: rotate .2s ease;
}

.bc-10 details[open] summary svg {
  rotate: 180deg;
}

.bc-10__menu {
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  z-index: 20;
  display: flex;
  flex-direction: column;
  min-width: 170px;
  padding: 6px;
  border-radius: 11px;
  background: #fff;
  border: 1px solid oklch(0.9 0.008 265);
  box-shadow: 0 10px 30px rgba(20,25,60,.14);
}

.bc-10__menu a {
  padding: 8px 11px;
  border-radius: 7px;
  font-weight: 500;
  color: oklch(0.4 0.02 265);
}

.bc-10__menu a:hover {
  background: color-mix(in oklab,var(--accent) 12%,transparent);
  color: var(--accent);
}

.bc-10 details::details-content {
  height: 0;
  overflow: hidden;
  transition: height .2s ease,content-visibility .2s ease allow-discrete;
  interpolate-size: allow-keywords;
}

.bc-10 details[open]::details-content {
  height: auto;
}

@media (hover: hover) {
  .bc-10 .bc-10__has:hover details:not([open]) .bc-10__menu {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-10 summary svg,
    .bc-10 details::details-content {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — sibling menus are native <details>/<summary> disclosures (keyboard + screen-reader ready); ::details-content + interpolate-size animate the open height where supported. */
```
