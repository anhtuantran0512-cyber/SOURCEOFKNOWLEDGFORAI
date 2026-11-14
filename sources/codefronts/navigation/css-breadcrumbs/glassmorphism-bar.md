---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/glassmorphism-bar/"
title: "Truncated Ellipsis Compact CSS Mobile Breadcrumb"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A single-line breadcrumb engineered for tight mobile widths: each crumb caps its width and truncates long titles with an ellipsis, the trail never wraps or…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Truncated Ellipsis Compact CSS Mobile Breadcrumb
Source: https://codefronts.com/navigation/css-breadcrumbs/glassmorphism-bar/

A single-line breadcrumb engineered for tight mobile widths: each crumb caps its width and truncates long titles with an ellipsis, the trail never wraps or overflows, and the current page always stays fully visible while ancestors shrink first. Pure CSS overflow management for constrained viewports.
## HTML
```html
<nav class="bc-33" aria-label="Breadcrumb">
  <ol>
    <li><a href="#" title="Home">Home</a></li>
    <li><a href="#" title="Electronics &amp; Accessories">Electronics &amp; Accessories</a></li>
    <li><a href="#" title="Headphones and Earbuds">Headphones and Earbuds</a></li>
    <li><a href="#" aria-current="page" title="Wireless Over-Ear Noise-Cancelling">Wireless Over-Ear Noise-Cancelling</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-33 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 26px;
  background: oklch(0.98 0.004 240);
  place-items: center;
}

.bc-33 * {
  box-sizing: border-box;
}

.bc-33 ol {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  list-style: none;
  margin: 0 auto;
  padding: 10px 12px;
  max-width: 340px;
  overflow: hidden;
  border-radius: 10px;
  background: #fff;
  border: 1px solid oklch(0.9 0.008 240);
}

.bc-33 li {
  display: flex;
  align-items: center;
  min-width: 0;
}

.bc-33 li + li::before {
  content: "›";
  flex: none;
  margin: 0 6px;
  color: oklch(0.7 0.02 240);
}

.bc-33 a {
  min-width: 0;
  max-width: 12ch;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font: 500 13px/1 system-ui,sans-serif;
  color: oklch(0.5 0.09 250);
  text-decoration: none;
  padding: 2px 3px;
  border-radius: 5px;
}

.bc-33 li:not(:last-child) a {
  flex-shrink: 1;
}

.bc-33 a:hover {
  color: oklch(0.4 0.13 250);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.bc-33 a:focus-visible {
  outline: 2px solid oklch(0.5 0.14 250);
  outline-offset: 1px;
}

.bc-33 li:first-child a,
.bc-33 li[aria-current="page"] a {
  flex-shrink: 0;
}

.bc-33 li[aria-current="page"] a {
  max-width: none;
  color: oklch(0.3 0.02 240);
  font-weight: 600;
}
```

## JavaScript
```js
/* No JavaScript — flex-shrink priorities + min-width:0 + text-overflow:ellipsis truncate ancestors first while the current page (flex-shrink:0) stays fully visible; nothing ever overflows. */
```
