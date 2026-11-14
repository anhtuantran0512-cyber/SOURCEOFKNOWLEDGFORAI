---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/responsive-sidebar-to-bottom-tabs/"
title: "Responsive Sidebar to Bottom Tabs"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "One glass navigation that adapts to its container: a floating vertical sidebar on desktop, seamlessly re-flowing into a bottom-anchored tab bar on narrow…"
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Sidebar to Bottom Tabs
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/responsive-sidebar-to-bottom-tabs/

One glass navigation that adapts to its container: a floating vertical sidebar on desktop, seamlessly re-flowing into a bottom-anchored tab bar on narrow screens. Same links, same frosted material, layout driven purely by a container query — no duplicate markup, no JS.
## HTML
```html
<section class="nb-24" aria-label="Responsive glass sidebar to bottom tabs demo">
  <div class="nb-24__app">
    <nav class="nb-24__nav" aria-label="Primary">
      <span class="nb-24__logo" aria-hidden="true">◆</span>
      <a class="nb-24__item" href="#nb-24" aria-current="page"><span class="nb-24__ic" aria-hidden="true">⌂</span><span class="nb-24__lb">Home</span></a>
      <a class="nb-24__item" href="#nb-24"><span class="nb-24__ic" aria-hidden="true">⌕</span><span class="nb-24__lb">Search</span></a>
      <a class="nb-24__item" href="#nb-24"><span class="nb-24__ic" aria-hidden="true">▤</span><span class="nb-24__lb">Library</span></a>
      <a class="nb-24__item" href="#nb-24"><span class="nb-24__ic" aria-hidden="true">◔</span><span class="nb-24__lb">Activity</span></a>
      <a class="nb-24__item" href="#nb-24"><span class="nb-24__ic" aria-hidden="true">◉</span><span class="nb-24__lb">Profile</span></a>
    </nav>
    <div class="nb-24__main"><p class="nb-24__hint">Resize the preview: the glass sidebar re-flows into a bottom tab bar on narrow widths — one nav, one material, zero duplicate markup.</p></div>
  </div>
</section>
```
## CSS
```css
.nb-24,
.nb-24 *,
.nb-24 *::before,
.nb-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-24 {
  width: 100%;
  min-height: 100vh;
  padding: 14px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(130deg,#654ea3,#4776e6 60%,#8e54e9);
}

.nb-24__app {
  position: relative;
  container-type: inline-size;
  min-height: calc(100vh - 28px);
  border-radius: 20px;
  overflow: hidden;
  background: radial-gradient(circle at 30% 20%,rgba(255,255,255,.14),transparent 60%),url('https://picsum.photos/seed/nb24/1000/700') center/cover;
}

.nb-24__nav {
  position: absolute;
  z-index: 5;
  top: 16px;
  left: 16px;
  bottom: 16px;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 6px;
  width: 150px;
  padding: 14px 10px;
  border-radius: 18px;
  color: #fff;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 20px 44px -24px rgba(0,0,0,.6);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
}

.nb-24__logo {
  font-size: 22px;
  text-align: center;
  padding: 6px 0 10px;
}

.nb-24__item {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255,255,255,.85);
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,color .2s;
}

.nb-24__ic {
  font-size: 19px;
  line-height: 1;
  width: 22px;
  text-align: center;
}

.nb-24__item:hover {
  color: #fff;
  background: rgba(255,255,255,.16);
}

.nb-24__item[aria-current] {
  color: #fff;
  background: rgba(255,255,255,.24);
}

.nb-24__item:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-24__main {
  min-height: calc(100vh - 28px);
  display: grid;
  place-items: center;
  padding: 24px 24px 24px 190px;
}

.nb-24__hint {
  max-width: 34ch;
  text-align: center;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  line-height: 1.6;
  text-shadow: 0 2px 14px rgba(0,0,0,.35);
}

@container (max-width: 560px) {
  .nb-24__nav {
    flex-direction: row;
    top: auto;
    left: 16px;
    right: 16px;
    bottom: 16px;
    width: auto;
    justify-content: space-around;
    padding: 8px;
  }

  .nb-24__logo {
    display: none;
  }

  .nb-24__item {
    flex-direction: column;
    gap: 3px;
    min-width: 56px;
    justify-content: center;
    padding: 6px;
  }

  .nb-24__lb {
    font-size: 11px;
  }

  .nb-24__ic {
    width: auto;
  }

  .nb-24__main {
    padding: 24px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nb-24__item {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one flex nav is a vertical sidebar by default and, via @container (max-width:560px), re-flows into a horizontal bottom tab bar. Only flex-direction/position/radius change; the glass recipe is shared. */
```
