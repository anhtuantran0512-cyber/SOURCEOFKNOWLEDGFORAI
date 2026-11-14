---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/accessible-breadcrumb-navigation-with-schema-org-microdata-aria/"
title: "Accessible Breadcrumb Navigation with Schema.org Microdata & ARIA"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The reference-grade accessible, SEO-complete breadcrumb: full schema.org BreadcrumbList Microdata inline in the HTML so Google can render breadcrumb rich…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Breadcrumb Navigation with Schema.org Microdata & ARIA
Source: https://codefronts.com/navigation/css-breadcrumbs/accessible-breadcrumb-navigation-with-schema-org-microdata-aria/

The reference-grade accessible, SEO-complete breadcrumb: full schema.org BreadcrumbList Microdata inline in the HTML so Google can render breadcrumb rich results, ARIA done correctly, aria-hidden pseudo-element separators screen readers skip, and a WCAG-AAA :focus-visible treatment. This is the one to ship on a real content site.
## HTML
```html
<nav class="bc-01" aria-label="Breadcrumb">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/"><span itemprop="name">Home</span></a>
      <meta itemprop="position" content="1">
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/guides"><span itemprop="name">Guides</span></a>
      <meta itemprop="position" content="2">
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/guides/css"><span itemprop="name">CSS</span></a>
      <meta itemprop="position" content="3">
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" aria-current="page">
      <span itemprop="name">Accessible Breadcrumbs</span>
      <meta itemprop="position" content="4">
    </li>
  </ol>
</nav>
```
## CSS
```css
.bc-01 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 28px;
  background: oklch(0.99 0.003 250);
  place-items: center;
}

.bc-01 * {
  box-sizing: border-box;
}

.bc-01 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 2px 0;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-01 li {
  display: flex;
  align-items: center;
  font: 500 14px/1.4 system-ui,sans-serif;
}

.bc-01 li + li::before {
  content: "/";
  margin: 0 12px;
  color: oklch(0.72 0.02 250);
  font-weight: 400;
}

.bc-01 a {
  display: inline-block;
  padding: 4px 6px;
  border-radius: 6px;
  color: oklch(0.5 0.13 255);
  text-decoration: none;
  transition: background-color .15s ease,color .15s ease;
}

.bc-01 a:hover {
  color: oklch(0.42 0.16 255);
  background: oklch(0.95 0.02 255);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.bc-01 a:focus-visible {
  outline: 3px solid oklch(0.45 0.18 255);
  outline-offset: 2px;
}

.bc-01 li[aria-current="page"] span {
  color: oklch(0.35 0.01 250);
  font-weight: 600;
  padding: 4px 6px;
}
```

## JavaScript
```js
/* No JavaScript — the value here is semantic: schema.org BreadcrumbList Microdata for rich results, ARIA landmark + aria-current, and non-semantic separators kept out of the a11y tree. */
```
