---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/dotted-separator/"
title: "Inline Bullet-Point Dot Separator CSS Breadcrumb"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The classic blog / editorial trail: text links separated by subtle centred bullet dots generated with ::after{content:'•'}."
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Bullet-Point Dot Separator CSS Breadcrumb
Source: https://codefronts.com/navigation/css-breadcrumbs/dotted-separator/

The classic blog / editorial trail: text links separated by subtle centred bullet dots generated with ::after{content:'•'}. Understated, inline, and instantly familiar — with a refined hover and an accent current page. The go-to for article headers, category lists, and post meta rows.
## HTML
```html
<nav class="bc-34" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Blog</a></li>
    <li><a href="#">Frontend</a></li>
    <li><a href="#" aria-current="page">Modern CSS in 2027</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-34 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  font-family: Georgia,'Times New Roman',serif;
  padding: 32px;
  background: oklch(0.99 0.003 60);
  place-items: center;
}

.bc-34 * {
  box-sizing: border-box;
}

.bc-34 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-34 li {
  display: flex;
  align-items: center;
}

.bc-34 li:not(:last-child)::after {
  content: "•";
  margin: 0 12px;
  font-size: 11px;
  color: oklch(0.75 0.02 60);
}

.bc-34 a {
  font: 400 14.5px/1 Georgia,serif;
  color: oklch(0.45 0.05 40);
  text-decoration: none;
  padding: 2px 1px;
  transition: color .15s ease;
}

.bc-34 a:hover {
  color: oklch(0.36 0.11 35);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.bc-34 a:focus-visible {
  outline: 2px solid oklch(0.45 0.12 35);
  outline-offset: 3px;
}

.bc-34 li[aria-current="page"] a {
  color: oklch(0.25 0.02 40);
  font-style: italic;
}

@media (prefers-reduced-motion: reduce) {
  .bc-34 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — decorative bullet separators via li::after{content:"•"}, kept out of the accessible name; swap the glyph for ·, |, or / in one line. */
```
