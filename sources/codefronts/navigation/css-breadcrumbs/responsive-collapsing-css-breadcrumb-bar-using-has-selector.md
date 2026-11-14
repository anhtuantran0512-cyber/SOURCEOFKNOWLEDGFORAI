---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/responsive-collapsing-css-breadcrumb-bar-using-has-selector/"
title: "Responsive Collapsing CSS Breadcrumb Bar using :has() Selector"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb that truncates itself on narrow screens with ZERO JavaScript: intermediate crumbs collapse behind an ellipsis, and hovering or focusing the…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Collapsing CSS Breadcrumb Bar using :has() Selector
Source: https://codefronts.com/navigation/css-breadcrumbs/responsive-collapsing-css-breadcrumb-bar-using-has-selector/

A breadcrumb that truncates itself on narrow screens with ZERO JavaScript: intermediate crumbs collapse behind an ellipsis, and hovering or focusing the ellipsis expands them back with a smooth max-width tween. Container queries make it respond to its own column width, so it collapses in a narrow sidebar even on a wide screen.
## HTML
```html
<div class="bc-02">
  <nav aria-label="Breadcrumb">
    <ol>
      <li><a href="#">Home</a></li>
      <li class="bc-02__ellipsis"><button type="button" aria-label="Show collapsed breadcrumbs">&hellip;</button></li>
      <li><a href="#">Store</a></li>
      <li><a href="#">Women</a></li>
      <li><a href="#">Outerwear</a></li>
      <li><a href="#" aria-current="page">Wool Coat</a></li>
    </ol>
  </nav>
</div>
```
## CSS
```css
.bc-02 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  container-type: inline-size;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 28px;
  background: oklch(0.14 0.02 265);
  color: oklch(0.9 0.01 265);
  place-items: center;
}

.bc-02 * {
  box-sizing: border-box;
}

.bc-02 ol {
  display: flex;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-02 li {
  display: flex;
  align-items: center;
}

.bc-02 li + li::before {
  content: "›";
  margin: 0 8px;
  color: oklch(0.55 0.02 265);
}

.bc-02 a {
  white-space: nowrap;
  overflow: hidden;
  max-width: 14ch;
  text-overflow: ellipsis;
  padding: 5px 4px;
  border-radius: 6px;
  color: oklch(0.78 0.03 265);
  text-decoration: none;
  transition: max-width .3s ease,opacity .25s ease,color .15s ease;
}

.bc-02 a:hover {
  color: #fff;
}

.bc-02 a:focus-visible {
  outline: 2px solid oklch(0.72 0.15 265);
  outline-offset: 2px;
}

.bc-02 li[aria-current="page"] a {
  color: #fff;
  font-weight: 600;
}

.bc-02__ellipsis {
  display: none;
}

.bc-02__ellipsis button {
  display: grid;
  place-items: center;
  min-width: 34px;
  height: 30px;
  padding: 0 8px;
  border: none;
  border-radius: 8px;
  background: oklch(0.24 0.02 265);
  color: oklch(0.8 0.02 265);
  font: 700 15px/1 system-ui,sans-serif;
  cursor: pointer;
}

.bc-02__ellipsis button:focus-visible {
  outline: 2px solid oklch(0.72 0.15 265);
  outline-offset: 2px;
}

@container (max-width: 480px) {
  .bc-02 ol:has(.bc-02__ellipsis) li:not(:first-child):not(:last-child):not(.bc-02__ellipsis) a {
    max-width: 0;
    opacity: 0;
    padding-inline: 0;
  }

  .bc-02 ol:has(.bc-02__ellipsis) li:not(:first-child):not(:last-child):not(.bc-02__ellipsis)::before {
    display: none;
  }

  .bc-02__ellipsis {
    display: flex;
  }

  .bc-02 ol:hover li a,
    .bc-02 ol:focus-within li a {
    max-width: 14ch;
    opacity: 1;
    padding-inline: 4px;
  }

  .bc-02 ol:hover li::before,
    .bc-02 ol:focus-within li::before {
    display: flex;
  }

  .bc-02 ol:hover .bc-02__ellipsis,
    .bc-02 ol:focus-within .bc-02__ellipsis {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-02 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — container queries collapse intermediate crumbs to max-width:0 behind an ellipsis; ol:hover/:focus-within tweens them back. */
```
