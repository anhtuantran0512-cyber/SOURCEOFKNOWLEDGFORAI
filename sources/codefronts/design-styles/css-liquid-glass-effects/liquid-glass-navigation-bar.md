---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-navigation-bar/"
title: "Liquid Glass Navigation Bar"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A sticky top navbar that turns into a frosted lens as content scrolls beneath it: photos and headings blur and desaturate as they pass under the bar, with a…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Navigation Bar
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-navigation-bar/

A sticky top navbar that turns into a frosted lens as content scrolls beneath it: photos and headings blur and desaturate as they pass under the bar, with a razor-thin translucent bottom border catching the light. The exact 'floating chrome' look of a modern OS, in pure CSS.
## HTML
```html
<section class="lg-03" aria-label="Liquid glass navigation bar">
  <header class="lg-03__bar">
    <span class="lg-03__brand">Lumen</span>
    <nav class="lg-03__nav" aria-label="Primary">
      <a class="lg-03__link" href="#lg-03" aria-current="page">Home</a>
      <a class="lg-03__link" href="#lg-03">Work</a>
      <a class="lg-03__link" href="#lg-03">Studio</a>
      <a class="lg-03__link" href="#lg-03">Contact</a>
    </nav>
  </header>
  <div class="lg-03__scroll" id="lg-03">
    <img src="https://picsum.photos/seed/lgnav-a/900/500" width="900" height="500" alt="Coastline at dawn">
    <h3>Scroll — watch content frost under the bar</h3>
    <img src="https://picsum.photos/seed/lgnav-b/900/500" width="900" height="500" alt="City at night">
    <p>The sticky bar samples and blurs whatever slides beneath it, in real time, on the compositor.</p>
    <img src="https://picsum.photos/seed/lgnav-c/900/500" width="900" height="500" alt="Mountain range">
  </div>
</section>
```
## CSS
```css
.lg-03,
.lg-03 *,
.lg-03 *::before,
.lg-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-03 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  height: 100vh;
  overflow-y: auto;
  background: #0e0b1a;
}

.lg-03__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 14px clamp(16px,4vw,32px);
  background: color-mix(in oklab,white 10%,transparent);
  border-bottom: 1px solid rgba(255,255,255,.25);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 10px 30px -20px rgba(0,0,0,.8);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
}

.lg-03__brand {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: #fff;
}

.lg-03__nav {
  display: flex;
  gap: 6px;
}

.lg-03__link {
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,.85);
  text-decoration: none;
  padding: 8px 14px;
  border-radius: 999px;
  transition: background .2s,color .2s;
}

.lg-03__link:hover {
  background: rgba(255,255,255,.16);
  color: #fff;
}

.lg-03__link[aria-current=page] {
  background: rgba(255,255,255,.9);
  color: #0e0b1a;
}

.lg-03__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.lg-03__scroll {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 28px;
  padding: 28px clamp(16px,4vw,40px) 120px;
  max-width: 940px;
  margin: 0 auto;
}

.lg-03__scroll img {
  width: 100%;
  height: auto;
  border-radius: 18px;
  display: block;
  box-shadow: 0 20px 44px -24px rgba(0,0,0,.7);
}

.lg-03__scroll h3 {
  color: #fff;
  font-size: 26px;
  font-weight: 800;
  text-align: center;
}

.lg-03__scroll p {
  color: rgba(255,255,255,.75);
  font-size: 16px;
  line-height: 1.6;
  text-align: center;
  max-width: 52ch;
}

@media (prefers-reduced-motion: reduce) {
  .lg-03__scroll {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — position:sticky keeps the bar pinned and backdrop-filter blurs + saturates whatever scrolls beneath it. */
```
