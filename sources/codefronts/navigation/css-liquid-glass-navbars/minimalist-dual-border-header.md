---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/minimalist-dual-border-header/"
title: "Minimalist Dual-Border Header"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "The most restrained take: an ultra-clean glass header defined almost entirely by light."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Dual-Border Header
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/minimalist-dual-border-header/

The most restrained take: an ultra-clean glass header defined almost entirely by light. A 1px semi-transparent outer border pairs with a 1px inner highlight to simulate the two edges of a physical glass pane, over a whisper of frost. No fills, no shadows shouting — just a precise, expensive-looking sliver of glass.
## HTML
```html
<section class="nb-23" aria-label="Minimalist dual border glass header demo">
  <header class="nb-23__bar">
    <span class="nb-23__brand">— clear</span>
    <nav class="nb-23__nav" aria-label="Primary">
      <a class="nb-23__link" href="#nb-23" aria-current="page">Index</a>
      <a class="nb-23__link" href="#nb-23">Work</a>
      <a class="nb-23__link" href="#nb-23">Info</a>
    </nav>
    <a class="nb-23__link nb-23__link--ghost" href="#nb-23">Contact →</a>
  </header>
</section>
```
## CSS
```css
.nb-23,
.nb-23 *,
.nb-23 *::before,
.nb-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-23 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(120deg,#485563,#29323c 60%,#7b6b8f);
}

.nb-23__bar {
  display: flex;
  align-items: center;
  gap: 24px;
  width: min(720px,100%);
  padding: 15px 20px;
  border-radius: 14px;
  color: #fff;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.55);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.75),inset 0 -1px 0 rgba(255,255,255,.3),0 18px 36px -22px rgba(0,0,0,.55);
  backdrop-filter: blur(14px) saturate(150%);
  -webkit-backdrop-filter: blur(14px) saturate(150%);
}

.nb-23__brand {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .02em;
  color: rgba(255,255,255,.95);
}

.nb-23__nav {
  display: flex;
  gap: 2px;
  margin-inline-start: auto;
}

.nb-23__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 13px;
  border-radius: 8px;
  text-decoration: none;
  color: rgba(255,255,255,.66);
  font-size: 14px;
  font-weight: 500;
  letter-spacing: .01em;
  transition: color .2s,background .2s;
}

.nb-23__link:hover {
  color: #fff;
  background: rgba(255,255,255,.08);
}

.nb-23__link[aria-current] {
  color: #fff;
}

.nb-23__link--ghost {
  color: rgba(255,255,255,.9);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4);
}

.nb-23__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-23__link {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the 'dual border' is one 1px outer border plus an inset 0 1px 0 top-highlight shadow, together reading as the two faces of a glass pane over a light backdrop-filter frost. */
```
