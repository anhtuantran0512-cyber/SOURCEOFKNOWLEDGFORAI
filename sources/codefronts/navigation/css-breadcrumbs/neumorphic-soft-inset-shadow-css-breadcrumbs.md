---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/neumorphic-soft-inset-shadow-css-breadcrumbs/"
title: "Neumorphic Soft Inset-Shadow CSS Breadcrumbs"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A neumorphic breadcrumb where the whole trail sits in a soft pressed 'channel' carved into the surface, and each crumb is a subtle inset well — the tactile…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft Inset-Shadow CSS Breadcrumbs
Source: https://codefronts.com/navigation/css-breadcrumbs/neumorphic-soft-inset-shadow-css-breadcrumbs/

A neumorphic breadcrumb where the whole trail sits in a soft pressed 'channel' carved into the surface, and each crumb is a subtle inset well — the tactile soft-UI treatment focused on inset shadows (the counterpart to demo 10's extruded nodes). The current crumb rises as the one raised node in the groove.
## HTML
```html
<nav class="bc-16" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Devices</a></li>
    <li><a href="#">Thermostat</a></li>
    <li><a href="#" aria-current="page">Schedule</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-16 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --surface: oklch(0.9 0.008 250);
  --dark: oklch(0.78 0.015 250);
  --light: oklch(0.99 0.004 250);
  --accent: oklch(0.5 0.15 260);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 38px 30px;
  background: var(--surface);
  place-items: center;
}

.bc-16 * {
  box-sizing: border-box;
}

.bc-16 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  list-style: none;
  margin: 0;
  padding: 10px 14px;
  border-radius: 16px;
  background: var(--surface);
  box-shadow: inset 5px 5px 10px var(--dark),inset -5px -5px 10px var(--light);
}

.bc-16 li {
  display: flex;
  align-items: center;
}

.bc-16 li:not(:last-child)::after {
  content: "›";
  margin: 0 6px;
  color: oklch(0.62 0.01 250);
}

.bc-16 a {
  display: inline-block;
  padding: 8px 14px;
  border-radius: 11px;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--accent);
  text-decoration: none;
  transition: box-shadow .2s ease,color .2s ease;
}

.bc-16 a:hover {
  box-shadow: inset 2px 2px 5px var(--dark),inset -2px -2px 5px var(--light);
}

.bc-16 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-16 li[aria-current="page"] a {
  color: oklch(0.38 0.03 250);
  box-shadow: 5px 5px 10px var(--dark),-5px -5px 10px var(--light);
}

@media (prefers-reduced-motion: reduce) {
  .bc-16 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the trail sits in an inset soft-UI channel; hover gives a crumb its own well and the current page is the one raised node popping out of the groove. */
```
