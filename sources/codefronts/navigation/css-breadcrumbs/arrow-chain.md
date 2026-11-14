---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/arrow-chain/"
title: "Modern Pure CSS Arrow Breadcrumb Bar using clip-path Polygons"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The classic interlocking-arrow breadcrumb — no images, no background sprites, no border hacks."
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern Pure CSS Arrow Breadcrumb Bar using clip-path Polygons
Source: https://codefronts.com/navigation/css-breadcrumbs/arrow-chain/

The classic interlocking-arrow breadcrumb — no images, no background sprites, no border hacks. Each crumb is a single anchor sliced into a chevron with one clip-path: polygon(), and a --arrow-depth custom property tunes the point angle across the whole trail from one line. First and last crumbs get clean flat outer edges.
## HTML
```html
<nav class="bc-23" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Electronics</a></li>
    <li><a href="#">Audio</a></li>
    <li><a href="#">Headphones</a></li>
    <li><a href="#" aria-current="page">Wireless Over-Ear</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-23 {
  width: 100%;
  min-height: 100vh;
  --arrow-depth: 16px;
  --h: 40px;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 28px;
  background: oklch(0.96 0.005 260);
  display: flex;
  align-items: center;
  justify-content: center;
}

.bc-23 * {
  box-sizing: border-box;
}

.bc-23 ol {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  filter: drop-shadow(0 2px 4px oklch(0 0 0/.12));
}

.bc-23 li {
  display: flex;
}

.bc-23 a {
  display: flex;
  align-items: center;
  height: var(--h);
  padding: 0 18px 0 26px;
  margin-inline-start: calc(var(--arrow-depth) * -1);
  text-decoration: none;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: #fff;
  background: oklch(0.6 0.02 260);
  clip-path: polygon(0 0,calc(100% - var(--arrow-depth)) 0,100% 50%,calc(100% - var(--arrow-depth)) 100%,0 100%,var(--arrow-depth) 50%);
  transition: filter .18s ease,background-color .18s ease;
}

.bc-23 li:nth-child(2) a {
  background: oklch(0.56 0.03 260);
}

.bc-23 li:nth-child(3) a {
  background: oklch(0.52 0.04 260);
}

.bc-23 li:nth-child(4) a {
  background: oklch(0.48 0.05 260);
}

.bc-23 li:first-child a {
  padding-left: 20px;
  margin-inline-start: 0;
  clip-path: polygon(0 0,calc(100% - var(--arrow-depth)) 0,100% 50%,calc(100% - var(--arrow-depth)) 100%,0 100%);
}

.bc-23 li:last-child a {
  padding-right: 22px;
  background: oklch(0.62 0.17 265);
  color: #fff;
  clip-path: polygon(0 0,100% 0,100% 100%,0 100%,var(--arrow-depth) 50%);
}

.bc-23 a:hover {
  filter: brightness(1.12);
}

.bc-23 a:focus-visible {
  outline: none;
  box-shadow: inset 0 0 0 2.5px #fff,inset 0 0 0 4px oklch(0.62 0.17 265);
}

.bc-23 li:last-child a[aria-current="page"] {
  cursor: default;
}

@media (prefers-reduced-motion: reduce) {
  .bc-23 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each crumb is one <a> sliced by clip-path: polygon(); --arrow-depth drives both the chevron math and the overlap margin. */
```
