---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/safari-toolbar-svg-refraction/"
title: "Safari Toolbar (SVG Refraction)"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A Safari-style top toolbar that goes beyond blur into true optical refraction."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Safari Toolbar (SVG Refraction)
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/safari-toolbar-svg-refraction/

A Safari-style top toolbar that goes beyond blur into true optical refraction. An inline SVG feTurbulence + feDisplacementMap filter warps the frosted layer so the background bends through the glass like a real lens — the effect Apple ships and plain glassmorphism can't fake. Back / forward controls, a pill address field and a share button complete the chrome.
## HTML
```html
<section class="nb-03" aria-label="Safari liquid glass toolbar demo">
  <svg class="nb-03__filter" aria-hidden="true" focusable="false"><filter id="nb-03-refract"><feTurbulence type="fractalNoise" baseFrequency="0.008 0.012" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="16" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <header class="nb-03__bar">
    <span class="nb-03__glass" aria-hidden="true"></span>
    <div class="nb-03__ctrls">
      <button class="nb-03__nav" type="button" aria-label="Back">‹</button>
      <button class="nb-03__nav" type="button" aria-label="Forward">›</button>
    </div>
    <label class="nb-03__field">
      <span class="nb-03__lock" aria-hidden="true">🔒</span>
      <input class="nb-03__url" type="text" value="codefronts.com/liquid-glass" aria-label="Address" spellcheck="false">
    </label>
    <button class="nb-03__nav" type="button" aria-label="Share">⤴</button>
  </header>
  <div class="nb-03__page"><p class="nb-03__txt">Watch the background bend through the toolbar — that warp is a live SVG displacement map, not a blur.</p></div>
</section>
```
## CSS
```css
.nb-03,
.nb-03 *,
.nb-03 *::before,
.nb-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-03 {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: -apple-system,'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(125deg,#00c6fb,#7b5bff 45%,#ff5ea8),url('https://picsum.photos/seed/nb03/1000/700') center/cover;
  background-blend-mode: overlay;
}

.nb-03__filter {
  position: absolute;
  width: 0;
  height: 0;
}

.nb-03__bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 10px;
  height: 52px;
  padding: 0 14px;
  isolation: isolate;
  background: color-mix(in oklab,white 12%,transparent);
  border-bottom: 1px solid rgba(255,255,255,.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45),0 10px 30px -18px rgba(0,0,0,.5);
  backdrop-filter: blur(14px) saturate(170%);
  -webkit-backdrop-filter: blur(14px) saturate(170%);
}

.nb-03__glass {
  position: absolute;
  inset: -40px 0 -40px 0;
  z-index: 0;
  pointer-events: none;
  background: inherit;
  filter: url(#nb-03-refract);
  opacity: .6;
}

.nb-03__ctrls {
  position: relative;
  z-index: 2;
  display: flex;
  gap: 4px;
}

.nb-03__nav {
  position: relative;
  z-index: 2;
  width: 34px;
  height: 34px;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,.35);
  background: rgba(255,255,255,.16);
  color: #fff;
  font-size: 18px;
  line-height: 1;
  cursor: pointer;
  transition: background .18s;
}

.nb-03__nav:hover {
  background: rgba(255,255,255,.3);
}

.nb-03__nav:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-03__field {
  position: relative;
  z-index: 2;
  flex: 1;
  display: flex;
  align-items: center;
  gap: 8px;
  height: 34px;
  padding: 0 14px;
  border-radius: 10px;
  background: rgba(255,255,255,.9);
  box-shadow: inset 0 1px 3px rgba(0,0,0,.15);
}

.nb-03__lock {
  font-size: 12px;
}

.nb-03__url {
  flex: 1;
  border: 0;
  background: none;
  outline: none;
  font: inherit;
  font-size: 14px;
  color: #111;
}

.nb-03__field:focus-within {
  box-shadow: 0 0 0 3px rgba(255,255,255,.7),inset 0 1px 3px rgba(0,0,0,.15);
}

.nb-03__page {
  padding: 40px 24px;
  color: #fff;
}

.nb-03__txt {
  font-size: 18px;
  line-height: 1.6;
  max-width: 40ch;
  font-weight: 600;
  text-shadow: 0 2px 12px rgba(0,0,0,.35);
}

@supports not (filter: url(#nb-03-refract)) {
  .nb-03__glass {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nb-03__glass {
    filter: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — refraction is a live SVG feTurbulence + feDisplacementMap filter applied to a decorative ::glass layer; toolbar controls sit above it on a higher z-index so text stays sharp. */
```
