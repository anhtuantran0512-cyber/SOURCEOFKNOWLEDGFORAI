---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/bottom-accessory-mini-player-bar/"
title: "Bottom Accessory / Mini-Player Bar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "The iOS 26 'bottom accessory' pattern: a persistent liquid-glass mini-player that floats just above the main tab bar."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bottom Accessory / Mini-Player Bar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/bottom-accessory-mini-player-bar/

The iOS 26 'bottom accessory' pattern: a persistent liquid-glass mini-player that floats just above the main tab bar. Two stacked glass surfaces — a now-playing accessory with artwork, title and transport controls, and the tab bar beneath — sharing one refractive language. Pure CSS.
## HTML
```html
<section class="nb-05" aria-label="Liquid glass bottom accessory bar demo">
  <div class="nb-05__content"><p class="nb-05__hint">Now-playing accessory floats above the tab bar — two glass surfaces, one material.</p></div>
  <div class="nb-05__stack">
    <div class="nb-05__player" role="group" aria-label="Now playing">
      <span class="nb-05__art" aria-hidden="true"></span>
      <span class="nb-05__meta"><span class="nb-05__song">Solar Fields</span><span class="nb-05__artist">Nova — Aurora EP</span></span>
      <span class="nb-05__bar05" aria-hidden="true"><span class="nb-05__fill"></span></span>
      <span class="nb-05__transport">
        <button class="nb-05__t" type="button" aria-label="Previous">⏮</button>
        <button class="nb-05__t nb-05__t--play" type="button" aria-label="Play">⏵</button>
        <button class="nb-05__t" type="button" aria-label="Next">⏭</button>
      </span>
    </div>
    <nav class="nb-05__tabs" aria-label="Primary">
      <a class="nb-05__tab" href="#nb-05" aria-current="page"><span aria-hidden="true">⌂</span>Home</a>
      <a class="nb-05__tab" href="#nb-05"><span aria-hidden="true">◎</span>Radio</a>
      <a class="nb-05__tab" href="#nb-05"><span aria-hidden="true">♪</span>Library</a>
      <a class="nb-05__tab" href="#nb-05"><span aria-hidden="true">⌕</span>Search</a>
    </nav>
  </div>
</section>
```
## CSS
```css
.nb-05,
.nb-05 *,
.nb-05 *::before,
.nb-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-05 {
  --accent: oklch(0.66 0.2 20);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 120deg at 70% 30%,#ff6a3d,#ff2d78,#7a2bff,#ff6a3d);
  background-size: 200% 200%;
  animation: nb-05-bg 20s ease-in-out infinite;
}

@keyframes nb-05-bg {
  50% {
    background-position: 100% 100%;
  }
}

.nb-05__content {
  height: 100%;
  display: grid;
  place-items: center;
  padding: 24px;
}

.nb-05__hint {
  max-width: 34ch;
  text-align: center;
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  line-height: 1.6;
  text-shadow: 0 2px 12px rgba(0,0,0,.3);
}

.nb-05__stack {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nb-05__player,
.nb-05__tabs {
  isolation: isolate;
  background: color-mix(in oklab,white 16%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 20px 40px -22px rgba(0,0,0,.6);
  backdrop-filter: blur(26px) saturate(180%);
  -webkit-backdrop-filter: blur(26px) saturate(180%);
}

.nb-05__player {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 20px;
  color: #fff;
}

.nb-05__art {
  width: 46px;
  height: 46px;
  border-radius: 12px;
  flex: none;
  background: linear-gradient(135deg,#ffd36b,#ff5ea8);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6);
}

.nb-05__meta {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.nb-05__song {
  font-size: 14.5px;
  font-weight: 700;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nb-05__artist {
  font-size: 12.5px;
  color: rgba(255,255,255,.8);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nb-05__bar05 {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 4px;
  height: 3px;
  border-radius: 3px;
  background: rgba(255,255,255,.28);
}

.nb-05__fill {
  display: block;
  width: 42%;
  height: 100%;
  border-radius: 3px;
  background: #fff;
}

.nb-05__transport {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 4px;
}

.nb-05__t {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  border: 0;
  background: none;
  color: #fff;
  font-size: 17px;
  cursor: pointer;
  transition: background .18s;
}

.nb-05__t:hover {
  background: rgba(255,255,255,.18);
}

.nb-05__t--play {
  background: var(--accent);
  font-size: 16px;
}

.nb-05__t--play:hover {
  background: color-mix(in oklab,var(--accent) 85%,white);
}

.nb-05__t:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-05__tabs {
  display: flex;
  justify-content: space-around;
  padding: 8px;
  border-radius: 22px;
}

.nb-05__tab {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  min-width: 56px;
  min-height: 44px;
  justify-content: center;
  border-radius: 14px;
  text-decoration: none;
  color: rgba(255,255,255,.82);
  font-size: 11px;
  font-weight: 600;
  transition: background .2s,color .2s;
}

.nb-05__tab span {
  font-size: 19px;
}

.nb-05__tab[aria-current] {
  color: #fff;
  background: rgba(255,255,255,.2);
}

.nb-05__tab:hover {
  color: #fff;
  background: rgba(255,255,255,.12);
}

.nb-05__tab:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-05 {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two stacked backdrop-filter glass surfaces (accessory + tab bar) pinned to the bottom in a flex column, sharing one frost recipe so they read as a single material at two elevations. */
```
