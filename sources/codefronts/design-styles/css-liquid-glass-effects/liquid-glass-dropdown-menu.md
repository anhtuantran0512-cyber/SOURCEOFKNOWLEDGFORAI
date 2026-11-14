---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-dropdown-menu/"
title: "Liquid Glass Dropdown Menu"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A floating dropdown that glassifies the page beneath it when it opens, dropping in like a liquid bubble that snaps into place."
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Dropdown Menu
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-dropdown-menu/

A floating dropdown that glassifies the page beneath it when it opens, dropping in like a liquid bubble that snaps into place. Replaces the blocky native select with a sleek frosted panel — pure CSS via a focusable details/summary, so it's keyboard-operable with zero JS.
## HTML
```html
<section class="lg-09" aria-label="Liquid glass dropdown menu">
  <div class="lg-09__bg" aria-hidden="true"></div>
  <details class="lg-09__dd">
    <summary class="lg-09__trigger">Workspace <span class="lg-09__chev" aria-hidden="true">▾</span></summary>
    <div class="lg-09__panel" role="menu">
      <a class="lg-09__item" role="menuitem" href="#lg-09">🗂  Projects</a>
      <a class="lg-09__item" role="menuitem" href="#lg-09">👥  Team</a>
      <a class="lg-09__item" role="menuitem" href="#lg-09">⚙️  Settings</a>
      <hr class="lg-09__sep">
      <a class="lg-09__item" role="menuitem" href="#lg-09">↪  Sign out</a>
    </div>
  </details>
</section>
```
## CSS
```css
.lg-09,
.lg-09 *,
.lg-09 *::before,
.lg-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-09 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 120px 20px;
  overflow: hidden;
  background: radial-gradient(circle at 20% 30%,#4a2f8a,transparent 55%),radial-gradient(circle at 80% 20%,#1e5aa8,transparent 50%),radial-gradient(circle at 50% 90%,#a83d7a,transparent 50%),#0a0620;
}

.lg-09__bg {
  position: absolute;
  inset: -40px;
  background: radial-gradient(circle at 30% 40%,#7c3aed,transparent 45%),radial-gradient(circle at 70% 60%,#0891b2,transparent 45%),radial-gradient(circle at 50% 80%,#db2777,transparent 40%);
  filter: blur(60px);
  opacity: .7;
  pointer-events: none;
}

.lg-09__dd {
  position: relative;
  z-index: 2;
  width: min(240px,80vw);
}

.lg-09__trigger {
  list-style: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  padding: 13px 18px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.35);
  background: color-mix(in oklab,white 14%,transparent);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 12px 26px -16px rgba(0,0,0,.6);
  backdrop-filter: blur(16px) saturate(170%);
  -webkit-backdrop-filter: blur(16px) saturate(170%);
  transition: background .2s;
}

.lg-09__trigger::-webkit-details-marker {
  display: none;
}

.lg-09__trigger:hover {
  background: color-mix(in oklab,white 20%,transparent);
}

.lg-09__dd[open] .lg-09__trigger:focus-visible,
.lg-09__trigger:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-09__chev {
  transition: transform .3s;
}

.lg-09__dd[open] .lg-09__chev {
  transform: rotate(180deg);
}

.lg-09__panel {
  position: absolute;
  left: 0;
  right: 0;
  margin-top: 10px;
  padding: 8px;
  border-radius: 16px;
  transform-origin: top center;
  background: color-mix(in oklab,white 12%,transparent);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 26px 50px -24px rgba(0,0,0,.7);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.lg-09__dd[open] .lg-09__panel {
  animation: lg-09-drop .4s cubic-bezier(.3,1.3,.5,1);
}

.lg-09__item {
  display: block;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  padding: 11px 14px;
  border-radius: 10px;
  transition: background .18s;
}

.lg-09__item:hover {
  background: rgba(255,255,255,.18);
}

.lg-09__item:focus-visible {
  outline: 2px solid #fff;
  outline-offset: -2px;
}

.lg-09__sep {
  border: none;
  border-top: 1px solid rgba(255,255,255,.18);
  margin: 6px 8px;
}

@keyframes lg-09-drop {
  0% {
    opacity: 0;
    transform: translateY(-10px) scaleY(.6);
  }

  60% {
    opacity: 1;
    transform: translateY(2px) scaleY(1.05);
  }

  100% {
    opacity: 1;
    transform: translateY(0) scaleY(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-09__dd[open] .lg-09__panel {
    animation: none;
  }

  .lg-09__chev {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a native details/summary handles open/close + keyboard, and the panel animates in with a springy keyframe (scaleY overshoot) for the liquid-drop snap. */
```
