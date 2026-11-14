---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/animated-gradient-blobs-navbar/"
title: "Animated Gradient Blobs Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "The showcase setup for any glass navbar: slow, colourful gradient blobs drift behind the bar so the frost has something rich to refract — because liquid…"
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Blobs Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/animated-gradient-blobs-navbar/

The showcase setup for any glass navbar: slow, colourful gradient blobs drift behind the bar so the frost has something rich to refract — because liquid glass disappears over flat backgrounds. Three blurred blobs orbit on keyframes while the navbar samples and warps them. Pure CSS.
## HTML
```html
<section class="nb-16" aria-label="Animated gradient blobs glass navbar demo">
  <div class="nb-16__blobs" aria-hidden="true"><span class="nb-16__blob nb-16__blob--a"></span><span class="nb-16__blob nb-16__blob--b"></span><span class="nb-16__blob nb-16__blob--c"></span></div>
  <nav class="nb-16__bar" aria-label="Primary">
    <span class="nb-16__brand">◐ Prism</span>
    <div class="nb-16__links">
      <a class="nb-16__link" href="#nb-16" aria-current="page">Gallery</a>
      <a class="nb-16__link" href="#nb-16">Artists</a>
      <a class="nb-16__link" href="#nb-16">Shop</a>
      <a class="nb-16__link" href="#nb-16">Journal</a>
    </div>
  </nav>
</section>
```
## CSS
```css
.nb-16,
.nb-16 *,
.nb-16 *::before,
.nb-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-16 {
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0a0616;
}

.nb-16__blobs {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.nb-16__blob {
  position: absolute;
  width: 340px;
  height: 340px;
  border-radius: 50%;
  filter: blur(60px);
  opacity: .85;
  will-change: transform;
}

.nb-16__blob--a {
  background: radial-gradient(circle,#5b8cff,transparent 70%);
  top: -80px;
  left: -40px;
  animation: nb-16-a 16s ease-in-out infinite;
}

.nb-16__blob--b {
  background: radial-gradient(circle,#ff5ea8,transparent 70%);
  bottom: -100px;
  right: -30px;
  animation: nb-16-b 20s ease-in-out infinite;
}

.nb-16__blob--c {
  background: radial-gradient(circle,#38e8c6,transparent 70%);
  top: 40%;
  left: 45%;
  animation: nb-16-c 24s ease-in-out infinite;
}

@keyframes nb-16-a {
  50% {
    transform: translate(120px,80px) scale(1.2);
  }
}

@keyframes nb-16-b {
  50% {
    transform: translate(-120px,-60px) scale(1.15);
  }
}

@keyframes nb-16-c {
  50% {
    transform: translate(-80px,60px) scale(.85);
  }
}

.nb-16__bar {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 14px 20px;
  border-radius: 20px;
  color: #fff;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45),0 24px 50px -26px rgba(0,0,0,.7);
  backdrop-filter: blur(24px) saturate(190%);
  -webkit-backdrop-filter: blur(24px) saturate(190%);
}

.nb-16__brand {
  font-size: 16px;
  font-weight: 800;
}

.nb-16__links {
  display: flex;
  gap: 6px;
}

.nb-16__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 16px;
  border-radius: 12px;
  text-decoration: none;
  color: #fff;
  opacity: .9;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,opacity .2s;
}

.nb-16__link:hover,
.nb-16__link[aria-current] {
  opacity: 1;
  background: rgba(255,255,255,.18);
}

.nb-16__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-16__blob {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — three blurred radial-gradient blobs orbit on long transform-only @keyframes behind the bar, giving the backdrop-filter rich moving colour to refract. Reduced-motion freezes them. */
```
