---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/macos-tahoe-menu-bar/"
title: "macOS Tahoe Menu Bar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "The translucent top menu bar from macOS Tahoe: a razor-thin glass strip that blends into the desktop wallpaper, with a leading brand glyph, classic pull-down…"
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: macOS Tahoe Menu Bar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/macos-tahoe-menu-bar/

The translucent top menu bar from macOS Tahoe: a razor-thin glass strip that blends into the desktop wallpaper, with a leading brand glyph, classic pull-down menu titles, and a trailing cluster of status icons and a clock. Pure CSS — the frosted blur is real backdrop-filter.
## HTML
```html
<section class="nb-02" aria-label="macOS Tahoe menu bar demo">
  <header class="nb-02__bar">
    <span class="nb-02__logo" aria-hidden="true">◐</span>
    <nav class="nb-02__menus" aria-label="Menu bar">
      <button class="nb-02__menu nb-02__menu--app" type="button">Lumen</button>
      <button class="nb-02__menu" type="button">File</button>
      <button class="nb-02__menu" type="button">Edit</button>
      <button class="nb-02__menu" type="button">View</button>
      <button class="nb-02__menu" type="button">Window</button>
      <button class="nb-02__menu" type="button">Help</button>
    </nav>
    <div class="nb-02__status">
      <span class="nb-02__ico" title="Wi-Fi" aria-label="Wi-Fi">▲</span>
      <span class="nb-02__ico" title="Battery" aria-label="Battery">▮</span>
      <span class="nb-02__ico" title="Search" aria-label="Search">⌕</span>
      <span class="nb-02__clock">Wed 9:41 AM</span>
    </div>
  </header>
  <div class="nb-02__desk"><span class="nb-02__wm">Tahoe</span></div>
</section>
```
## CSS
```css
.nb-02,
.nb-02 *,
.nb-02 *::before,
.nb-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-02 {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: -apple-system,'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 90% at 20% 0%,#ff9d6c,#c14bd6 45%,#3b2a86 100%);
}

.nb-02__bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 4px;
  height: 34px;
  padding: 0 12px;
  color: #fff;
  background: color-mix(in oklab,white 14%,transparent);
  border-bottom: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4);
  backdrop-filter: blur(30px) saturate(180%);
  -webkit-backdrop-filter: blur(30px) saturate(180%);
  text-shadow: 0 1px 3px rgba(0,0,0,.25);
}

.nb-02__logo {
  font-size: 17px;
  margin-right: 4px;
}

.nb-02__menus {
  display: flex;
  align-items: center;
}

.nb-02__menu {
  font: inherit;
  font-size: 13.5px;
  color: #fff;
  background: none;
  border: 0;
  padding: 5px 11px;
  border-radius: 7px;
  cursor: pointer;
  min-height: 26px;
  transition: background .15s;
}

.nb-02__menu--app {
  font-weight: 700;
}

.nb-02__menu:hover,
.nb-02__menu:focus-within {
  background: rgba(255,255,255,.22);
}

.nb-02__menu:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 1px;
}

.nb-02__status {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 13px;
}

.nb-02__ico {
  font-size: 13px;
  opacity: .95;
  cursor: default;
}

.nb-02__clock {
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.nb-02__desk {
  height: calc(100% - 34px);
  display: grid;
  place-items: center;
}

.nb-02__wm {
  font-size: 96px;
  font-weight: 800;
  letter-spacing: -.04em;
  color: rgba(255,255,255,.14);
}
```

## JavaScript
```js
/* No JavaScript — sticky bar + backdrop-filter frost the wallpaper; menu titles are focusable buttons with hover/focus capsules and a flex margin-inline-start:auto status cluster. */
```
