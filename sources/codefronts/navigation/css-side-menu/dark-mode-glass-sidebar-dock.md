---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/dark-mode-glass-sidebar-dock/"
title: "Dark Mode Glass Sidebar Dock"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A floating vertical dock modelled after macOS Tahoe: a dark frosted glass rail of icons that fluidly expands to reveal labels on hover, with a sliding…"
has_js: "true"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Glass Sidebar Dock
Source: https://codefronts.com/navigation/css-side-menu/dark-mode-glass-sidebar-dock/

A floating vertical dock modelled after macOS Tahoe: a dark frosted glass rail of icons that fluidly expands to reveal labels on hover, with a sliding specular highlight tracking the active item. The collapse/expand is spring-eased so it feels physical, not mechanical.
## HTML
```html
<section class="sm-17" aria-label="Dark mode liquid glass sidebar dock demo">
  <nav class="sm-17__dock" id="sm-17-dock" aria-label="Primary">
    <span class="sm-17__hl" aria-hidden="true"></span>
    <a class="sm-17__item" href="#sm-17" aria-current="page"><span class="sm-17__ic" aria-hidden="true">⌂</span><span class="sm-17__lb">Dashboard</span></a>
    <a class="sm-17__item" href="#sm-17"><span class="sm-17__ic" aria-hidden="true">◔</span><span class="sm-17__lb">Analytics</span></a>
    <a class="sm-17__item" href="#sm-17"><span class="sm-17__ic" aria-hidden="true">▤</span><span class="sm-17__lb">Projects</span></a>
    <a class="sm-17__item" href="#sm-17"><span class="sm-17__ic" aria-hidden="true">✉</span><span class="sm-17__lb">Messages</span></a>
    <a class="sm-17__item" href="#sm-17"><span class="sm-17__ic" aria-hidden="true">⚙</span><span class="sm-17__lb">Settings</span></a>
  </nav>
  <p class="sm-17__hint">Hover the dock →</p>
</section>
```
## CSS
```css
.sm-17,
.sm-17 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-17 {
  --accent: oklch(0.66 0.2 275);
  --w-min: 66px;
  --w-max: 210px;
  position: relative;
  display: flex;
  align-items: center;
  gap: 24px;
  width: 100%;
  min-height: 100vh;
  padding: 26px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 10% 10%,#1e1b3a,#0b0a17 70%);
}

.sm-17__dock {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: var(--w-min);
  padding: 12px;
  border-radius: 22px;
  overflow: hidden;
  isolation: isolate;
  background: color-mix(in oklab,white 8%,rgba(10,10,20,.35));
  border: 1px solid rgba(255,255,255,.16);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.28),0 30px 60px -28px rgba(0,0,0,.8);
  backdrop-filter: blur(22px) saturate(160%);
  -webkit-backdrop-filter: blur(22px) saturate(160%);
  transition: width .5s cubic-bezier(.34,1.35,.5,1);
}

.sm-17__dock:hover,
.sm-17__dock:focus-within {
  width: var(--w-max);
}

.sm-17__hl {
  position: absolute;
  left: 12px;
  right: 12px;
  height: 44px;
  border-radius: 12px;
  background: color-mix(in oklab,var(--accent) 70%,transparent);
  box-shadow: 0 6px 18px -6px var(--accent);
  transform: translateY(var(--y,0));
  transition: transform .4s cubic-bezier(.34,1.35,.5,1);
  pointer-events: none;
}

.sm-17__item {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 44px;
  padding: 0 12px;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255,255,255,.82);
  font-size: 14.5px;
  font-weight: 600;
  white-space: nowrap;
}

.sm-17__item[aria-current] {
  color: #fff;
}

.sm-17__ic {
  font-size: 20px;
  width: 20px;
  text-align: center;
  flex: none;
}

.sm-17__lb {
  max-width: 0;
  opacity: 0;
  overflow: hidden;
  transition: max-width .5s cubic-bezier(.34,1.35,.5,1),opacity .35s;
}

.sm-17__dock:hover .sm-17__lb,
.sm-17__dock:focus-within .sm-17__lb {
  max-width: 130px;
  opacity: 1;
}

.sm-17__item:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.sm-17__hint {
  color: rgba(255,255,255,.5);
  font-size: 14px;
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .sm-17__dock,
    .sm-17__hl,
    .sm-17__lb {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const dock = document.querySelector('#sm-17-dock');
  if (!dock) return;
  const hl = dock.querySelector('.sm-17__hl');
  const items = [...dock.querySelectorAll('.sm-17__item')];
  const move = (el) => { hl.style.setProperty('--y', (el.offsetTop - 12) + 'px'); };
  const active = dock.querySelector('[aria-current]') || items[0];
  requestAnimationFrame(() => move(active));
  items.forEach((it) => {
    it.addEventListener('pointerenter', () => move(it));
    it.addEventListener('focus', () => move(it));
  });
  dock.addEventListener('pointerleave', () => move(dock.querySelector('[aria-current]') || items[0]));
})();
```
