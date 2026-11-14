---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/adaptive-light-dark-mode-breadcrumb-bar-with-css-custom-properties/"
title: "Adaptive Light & Dark Mode Breadcrumb Bar with CSS Custom Properties"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb whose entire skin flips between light and dark from one set of custom properties — respecting the OS via prefers-color-scheme AND allowing a…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Adaptive Light & Dark Mode Breadcrumb Bar with CSS Custom Properties
Source: https://codefronts.com/navigation/css-breadcrumbs/adaptive-light-dark-mode-breadcrumb-bar-with-css-custom-properties/

A breadcrumb whose entire skin flips between light and dark from one set of custom properties — respecting the OS via prefers-color-scheme AND allowing a manual [data-theme] override. Frosted-glass bar background for modern SaaS dashboards, and every colour is a token, so re-theming is a five-line edit.
## HTML
```html
<div class="bc-03">
  <input type="checkbox" id="bc-03-theme" class="bc-03__check" aria-label="Toggle dark mode">
  <div class="bc-03__row">
    <nav class="bc-03__nav" aria-label="Breadcrumb">
      <ol>
        <li><a href="#">Dashboard</a></li>
        <li><a href="#">Projects</a></li>
        <li><a href="#">Aurora</a></li>
        <li><a href="#" aria-current="page">Settings</a></li>
      </ol>
    </nav>
    <label for="bc-03-theme" class="bc-03__toggle">
      <svg class="bc-03__sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="bc-03__moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
      <span class="bc-03__toggle-label">Theme</span>
    </label>
  </div>
</div>
```
## CSS
```css
.bc-03 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --bc-bg: oklch(1 0 0/.7);
  --bc-text: oklch(0.5 0.02 265);
  --bc-strong: oklch(0.25 0.02 265);
  --bc-accent: oklch(0.55 0.16 265);
  --bc-sep: oklch(0.75 0.02 265);
  --bc-hover: oklch(0.95 0.01 265);
  --bc-line: oklch(0.85 0.01 265/.7);
  color-scheme: light;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 28px;
  background: oklch(0.97 0.005 265);
  place-items: center;
  transition: background-color .3s ease;
}

.bc-03 * {
  box-sizing: border-box;
}

.bc-03:has(.bc-03__check:checked) {
  --bc-bg: oklch(0.2 0.02 265/.7);
  --bc-text: oklch(0.72 0.02 265);
  --bc-strong: oklch(0.96 0.01 265);
  --bc-accent: oklch(0.72 0.15 265);
  --bc-sep: oklch(0.5 0.02 265);
  --bc-hover: oklch(0.28 0.02 265);
  --bc-line: oklch(0.4 0.02 265/.5);
  color-scheme: dark;
  background: oklch(0.14 0.02 265);
}

.bc-03 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 8px 14px;
  border-radius: 12px;
  background: var(--bc-bg);
  border: 1px solid var(--bc-line);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .3s ease,border-color .3s ease;
}

.bc-03 li {
  display: flex;
  align-items: center;
}

.bc-03 li + li::before {
  content: "›";
  margin: 0 8px;
  color: var(--bc-sep);
}

.bc-03 a {
  padding: 5px 9px;
  border-radius: 7px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--bc-text);
  text-decoration: none;
  transition: background-color .18s ease,color .18s ease;
}

.bc-03 a:hover {
  color: var(--bc-strong);
  background: var(--bc-hover);
}

.bc-03 a:focus-visible {
  outline: 2px solid var(--bc-accent);
  outline-offset: 2px;
}

.bc-03 li[aria-current="page"] a {
  color: var(--bc-strong);
  font-weight: 600;
  background: color-mix(in oklab,var(--bc-accent) 18%,transparent);
}

@media (prefers-reduced-motion: reduce) {
  .bc-03 ol,
    .bc-03 a {
    transition: none;
  }
}

.bc-03 .bc-03__row {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
}

.bc-03 .bc-03__check {
  position: absolute;
  opacity: 0;
  pointer-events: none;
  width: 1px;
  height: 1px;
}

.bc-03 .bc-03__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border-radius: 999px;
  background: #fff;
  border: 1px solid oklch(0.85 0.02 260);
  color: oklch(0.3 0.03 260);
  font: 600 12.5px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: background .18s ease,border-color .18s ease,color .18s ease;
  user-select: none;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

.bc-03 .bc-03__toggle:hover {
  background: color-mix(in oklch,currentColor 14%,transparent);
}

.bc-03 .bc-03__check:focus-visible + .bc-03__toggle {
  outline: 2px solid var(--accent,oklch(0.62 0.18 255));
  outline-offset: 2px;
}

.bc-03 .bc-03__toggle svg {
  width: 14px;
  height: 14px;
}

.bc-03 .bc-03__moon {
  display: none;
}

.bc-03:has(.bc-03__check:checked) .bc-03__toggle {
  background: oklch(0.22 0.02 260);
  border-color: oklch(0.35 0.02 260);
  color: oklch(0.95 0.005 260);
  box-shadow: 0 1px 3px rgba(0,0,0,0.4);
}

.bc-03:has(.bc-03__check:checked) .bc-03__sun {
  display: none;
}

.bc-03:has(.bc-03__check:checked) .bc-03__moon {
  display: inline-block;
}
```

## JavaScript
```js
/* No JavaScript — five custom-property tokens skin the trail; prefers-color-scheme sets the OS default, [data-theme] overrides it manually. Add ~3 lines to persist the choice. */
```
