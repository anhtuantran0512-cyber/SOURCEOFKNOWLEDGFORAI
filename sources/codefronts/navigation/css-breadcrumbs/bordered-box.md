---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/bordered-box/"
title: "Clean Line-Separator Minimalist CSS Breadcrumbs"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The most restrained trail in the set: crumbs divided by thin vertical hairline rules with generous whitespace, low-profile muted type, and a single hairline…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clean Line-Separator Minimalist CSS Breadcrumbs
Source: https://codefronts.com/navigation/css-breadcrumbs/bordered-box/

The most restrained trail in the set: crumbs divided by thin vertical hairline rules with generous whitespace, low-profile muted type, and a single hairline that brightens under the active crumb. Editorial, calm, and perfect for content-heavy sites where the breadcrumb should whisper, not shout.
## HTML
```html
<nav class="bc-30" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Magazine</a></li>
    <li><a href="#">Essays</a></li>
    <li><a href="#" aria-current="page">On Slow Design</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-30 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 32px;
  background: oklch(0.99 0.002 90);
  place-items: center;
}

.bc-30 * {
  box-sizing: border-box;
}

.bc-30 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-30 li {
  display: flex;
  align-items: center;
}

.bc-30 li:not(:last-child)::after {
  content: "";
  height: 14px;
  margin-inline: 16px;
  border-inline-end: 1px solid oklch(0.82 0.005 90);
}

.bc-30 a {
  font: 400 13.5px/1 system-ui,sans-serif;
  letter-spacing: .015em;
  color: oklch(0.52 0.006 90);
  text-decoration: none;
  padding: 2px 1px;
  transition: color .15s ease;
}

.bc-30 a:hover {
  color: oklch(0.3 0.01 90);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
}

.bc-30 a:focus-visible {
  outline: 2px solid oklch(0.45 0.03 90);
  outline-offset: 3px;
}

.bc-30 li[aria-current="page"] a {
  color: oklch(0.2 0.008 90);
  font-weight: 500;
}

@media (prefers-reduced-motion: reduce) {
  .bc-30 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — separators are 1px logical border hairlines (border-inline-end) with generous margin-inline; quiet muted type keeps the trail subordinate to page content. */
```
