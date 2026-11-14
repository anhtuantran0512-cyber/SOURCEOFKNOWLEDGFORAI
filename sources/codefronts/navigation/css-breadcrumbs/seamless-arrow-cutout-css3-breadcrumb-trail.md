---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/seamless-arrow-cutout-css3-breadcrumb-trail/"
title: "Seamless Arrow-Cutout CSS3 Breadcrumb Trail"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The interlocking-chevron breadcrumb built the classic CSS3 way — with ::before/::after triangles made from transparent-border tricks rather than clip-path."
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Seamless Arrow-Cutout CSS3 Breadcrumb Trail
Source: https://codefronts.com/navigation/css-breadcrumbs/seamless-arrow-cutout-css3-breadcrumb-trail/

The interlocking-chevron breadcrumb built the classic CSS3 way — with ::before/::after triangles made from transparent-border tricks rather than clip-path. Each crumb's arrow is two rotated border-triangles that seamlessly notch into the next, the technique taught in every 'CSS arrow' tutorial, modernised.
## HTML
```html
<nav class="bc-13" aria-label="Breadcrumb">
  <ol class="bc-13__list">
    <li class="bc-13__item"><a class="bc-13__link" href="#">Home</a></li>
    <li class="bc-13__item"><a class="bc-13__link" href="#">Catalog</a></li>
    <li class="bc-13__item"><a class="bc-13__link" href="#">Tools</a></li>
    <li class="bc-13__item"><a class="bc-13__link" aria-current="page" href="#">Power Drills</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-13 {
  width: 100%;
  min-height: 100vh;
  --h: 44px;
  --depth: 14px;
  --page: oklch(0.96 0.01 90);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: var(--page);
  display: flex;
  align-items: center;
  justify-content: center;
}

.bc-13 * {
  box-sizing: border-box;
}

.bc-13__list {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-13__item {
  display: flex;
  position: relative;
}

.bc-13__item + .bc-13__item {
  margin-inline-start: calc(var(--depth) * -1);
}

.bc-13__link {
  position: relative;
  display: flex;
  align-items: center;
  height: var(--h);
  padding: 0 calc(var(--depth) + 12px) 0 calc(var(--depth) + 12px);
  font: 600 13px/1 system-ui,sans-serif;
  color: #fff;
  text-decoration: none;
  background: oklch(0.58 0.03 90);
  clip-path: polygon(0 0,calc(100% - var(--depth)) 0,100% 50%,calc(100% - var(--depth)) 100%,0 100%,var(--depth) 50%);
  transition: filter .18s ease;
}

.bc-13__item:first-child .bc-13__link {
  clip-path: polygon(0 0,calc(100% - var(--depth)) 0,100% 50%,calc(100% - var(--depth)) 100%,0 100%);
  padding-left: 16px;
}

.bc-13__item:last-child .bc-13__link {
  clip-path: polygon(0 0,100% 0,100% 100%,0 100%,var(--depth) 50%);
  padding-right: 16px;
  background: oklch(0.6 0.18 25);
}

.bc-13__item:first-child:last-child .bc-13__link {
  clip-path: none;
}

.bc-13__item:nth-child(2) .bc-13__link {
  background: oklch(0.52 0.05 60);
}

.bc-13__item:nth-child(3) .bc-13__link {
  background: oklch(0.5 0.07 40);
}

.bc-13__link:hover {
  filter: brightness(1.12);
}

.bc-13__link:focus-visible {
  outline: 3px solid oklch(0.3 0.05 40);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bc-13__link {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — arrows are transparent-border triangles (::after in the crumb colour, ::before in the page colour) that notch together seamlessly; the widest-support arrow technique. */
```
