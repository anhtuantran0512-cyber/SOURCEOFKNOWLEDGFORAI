---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/isometric-3d-layered-css-breadcrumb-navigation/"
title: "Isometric 3D Layered CSS Breadcrumb Navigation"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb tilted into isometric 3D: the whole trail sits on an angled plane via a rotateX/rotateZ transform, each crumb extruded with a stacked box-shadow…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Isometric 3D Layered CSS Breadcrumb Navigation
Source: https://codefronts.com/navigation/css-breadcrumbs/isometric-3d-layered-css-breadcrumb-navigation/

A breadcrumb tilted into isometric 3D: the whole trail sits on an angled plane via a rotateX/rotateZ transform, each crumb extruded with a stacked box-shadow 'side', so the path looks like physical tiles laid on a surface. A hover raises the tile toward the viewer — a striking showpiece built with pure CSS 3D transforms.
## HTML
```html
<nav class="bc-09" aria-label="Breadcrumb">
  <div class="bc-09__plane">
    <ol>
      <li><a href="#">Home</a></li>
      <li><a href="#">World</a></li>
      <li><a href="#">Levels</a></li>
      <li><a href="#" aria-current="page">Stage 4</a></li>
    </ol>
  </div>
</nav>
```
## CSS
```css
.bc-09 {
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 56px 40px 70px;
  background: oklch(0.94 0.02 265);
  display: flex;
  justify-content: center;
  perspective: 900px;
  align-items: center;
  justify-content: center;
}

.bc-09 * {
  box-sizing: border-box;
}

.bc-09__plane {
  transform-style: preserve-3d;
  transform: rotateX(52deg) rotateZ(-42deg);
}

.bc-09 ol {
  display: flex;
  gap: 16px;
  list-style: none;
  margin: 0;
  padding: 0;
  transform-style: preserve-3d;
}

.bc-09 a {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 74px;
  height: 42px;
  padding: 0 14px;
  border-radius: 8px;
  font: 700 13px/1 system-ui,sans-serif;
  color: #fff;
  text-decoration: none;
  background: oklch(0.62 0.13 265);
  box-shadow: 0 1px oklch(0.42 0.1 265),0 2px oklch(0.42 0.1 265),0 3px oklch(0.42 0.1 265),0 4px oklch(0.42 0.1 265),0 5px oklch(0.42 0.1 265),0 6px oklch(0.4 0.09 265),0 8px 12px rgba(0,0,0,.3);
  transition: transform .2s ease,box-shadow .2s ease;
}

.bc-09 a:hover,
.bc-09 a:focus-visible {
  transform: translateZ(16px);
  box-shadow: 0 2px oklch(0.42 0.1 265),0 4px oklch(0.42 0.1 265),0 6px oklch(0.42 0.1 265),0 8px oklch(0.42 0.1 265),0 10px oklch(0.42 0.1 265),0 12px oklch(0.4 0.09 265),0 20px 22px rgba(0,0,0,.32);
  outline: none;
}

.bc-09 a:focus-visible {
  box-shadow: 0 2px oklch(0.42 0.1 265),0 4px oklch(0.42 0.1 265),0 6px oklch(0.42 0.1 265),0 8px oklch(0.42 0.1 265),0 10px oklch(0.42 0.1 265),0 12px oklch(0.4 0.09 265),0 0 0 3px #fff,0 20px 22px rgba(0,0,0,.32);
}

.bc-09 li[aria-current="page"] a {
  background: oklch(0.68 0.19 30);
  box-shadow: 0 1px oklch(0.5 0.14 30),0 2px oklch(0.5 0.14 30),0 3px oklch(0.5 0.14 30),0 4px oklch(0.5 0.14 30),0 5px oklch(0.5 0.14 30),0 6px oklch(0.48 0.13 30),0 8px 12px rgba(0,0,0,.3);
  transform: translateZ(8px);
}

@media (prefers-reduced-motion: reduce) {
  .bc-09__plane {
    transform: none;
  }

  .bc-09 a {
    box-shadow: 0 2px 6px rgba(0,0,0,.2);
    transition: none;
  }

  .bc-09 a:hover,
    .bc-09 a:focus-visible {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — perspective + rotateX/rotateZ tilt the trail onto an isometric plane; a stacked box-shadow fakes tile extrusion, translateZ lifts on hover. Reduced-motion flattens to 2D. */
```
