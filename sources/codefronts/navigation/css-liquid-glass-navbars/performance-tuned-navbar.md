---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/performance-tuned-navbar/"
title: "Performance-Tuned Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A liquid-glass navbar built for a rock-steady 60fps and clean Core Web Vitals."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Performance-Tuned Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/performance-tuned-navbar/

A liquid-glass navbar built for a rock-steady 60fps and clean Core Web Vitals. It isolates the expensive backdrop-filter paint with contain + isolation, hints the compositor with will-change on the animating layer only, animates transform/opacity exclusively, and reserves its box so CLS stays at 0 — the pattern senior engineers ship to production.
## HTML
```html
<section class="nb-22" aria-label="Performance tuned glass navbar demo">
  <nav class="nb-22__bar" aria-label="Primary">
    <span class="nb-22__sweep" aria-hidden="true"></span>
    <span class="nb-22__brand">⚡ Sixty</span>
    <div class="nb-22__links">
      <a class="nb-22__link" href="#nb-22" aria-current="page">Home</a>
      <a class="nb-22__link" href="#nb-22">Metrics</a>
      <a class="nb-22__link" href="#nb-22">Budget</a>
      <a class="nb-22__link" href="#nb-22">Docs</a>
    </div>
    <span class="nb-22__fps" aria-hidden="true">60 fps</span>
  </nav>
</section>
```
## CSS
```css
.nb-22,
.nb-22 *,
.nb-22 *::before,
.nb-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-22 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(120deg,#2c3e50,#4ca1af 70%,#c4e0e5);
}

.nb-22__bar {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  contain: layout paint style;
  display: flex;
  align-items: center;
  gap: 18px;
  width: min(740px,100%);
  padding: 14px 18px;
  border-radius: 16px;
  color: #fff;
  background: color-mix(in oklab,white 12%,transparent);
  border: 1px solid rgba(255,255,255,.34);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 16px 38px -22px rgba(0,0,0,.55);
  backdrop-filter: blur(18px) saturate(170%);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
}

.nb-22__sweep {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background: linear-gradient(105deg,transparent 40%,rgba(255,255,255,.35) 50%,transparent 60%);
  transform: translateX(-120%);
  will-change: transform;
  animation: nb-22-sweep 5s ease-in-out infinite;
}

@keyframes nb-22-sweep {
  0%,
    60% {
    transform: translateX(-120%);
  }

  100% {
    transform: translateX(120%);
  }
}

.nb-22__brand,
.nb-22__links,
.nb-22__fps {
  position: relative;
  z-index: 1;
}

.nb-22__brand {
  font-size: 16px;
  font-weight: 800;
}

.nb-22__links {
  display: flex;
  gap: 4px;
}

.nb-22__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 10px;
  text-decoration: none;
  color: #fff;
  opacity: .9;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,opacity .2s;
}

.nb-22__link:hover,
.nb-22__link[aria-current] {
  opacity: 1;
  background: rgba(255,255,255,.18);
}

.nb-22__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-22__fps {
  margin-inline-start: auto;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  font-variant-numeric: tabular-nums;
}

@media (prefers-reduced-motion: reduce) {
  .nb-22__sweep {
    animation: none;
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — contain:layout paint style + isolation:isolate scope the backdrop-filter paint, will-change promotes only the transform-animated sweep layer, and position:sticky (in a real page) reserves the box for zero CLS. */
```
