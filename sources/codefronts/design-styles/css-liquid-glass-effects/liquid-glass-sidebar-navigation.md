---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-sidebar-navigation/"
title: "Liquid Glass Sidebar Navigation"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A collapsible vertical dashboard sidebar that stays crisp over colourful abstract background shapes: frosted glass panel, capsule active states, and a…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Sidebar Navigation
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-sidebar-navigation/

A collapsible vertical dashboard sidebar that stays crisp over colourful abstract background shapes: frosted glass panel, capsule active states, and a dark-mode switch that uses the CSS :has() selector to re-tint the whole shell from a single checkbox — no JS.
## HTML
```html
<section class="lg-15" aria-label="Liquid glass sidebar navigation">
  <div class="lg-15__blobs" aria-hidden="true"><span></span><span></span><span></span></div>
  <input class="lg-15__sr" type="checkbox" id="lg-15-collapse">
  <input class="lg-15__sr" type="checkbox" id="lg-15-theme">
  <aside class="lg-15__side">
    <div class="lg-15__top"><span class="lg-15__logo">◆</span><span class="lg-15__brand">Nimbus</span></div>
    <nav class="lg-15__nav" aria-label="Dashboard">
      <a class="lg-15__link" href="#lg-15" aria-current="page"><span class="lg-15__i">▤</span><span class="lg-15__t">Overview</span></a>
      <a class="lg-15__link" href="#lg-15"><span class="lg-15__i">◫</span><span class="lg-15__t">Projects</span></a>
      <a class="lg-15__link" href="#lg-15"><span class="lg-15__i">☰</span><span class="lg-15__t">Tasks</span></a>
      <a class="lg-15__link" href="#lg-15"><span class="lg-15__i">◍</span><span class="lg-15__t">Reports</span></a>
    </nav>
    <div class="lg-15__foot">
      <label class="lg-15__toggle" for="lg-15-theme"><span class="lg-15__i">◐</span><span class="lg-15__t">Dark mode</span></label>
      <label class="lg-15__toggle" for="lg-15-collapse"><span class="lg-15__i">⇔</span><span class="lg-15__t">Collapse</span></label>
    </div>
  </aside>
  <div class="lg-15__stage"><h3>Dashboard</h3><p>Toggle dark mode or collapse — the shell re-tints via CSS :has(), no JavaScript.</p></div>
</section>
```
## CSS
```css
.lg-15,
.lg-15 *,
.lg-15 *::before,
.lg-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-15 {
  --w: 230px;
  --surface: color-mix(in oklab,white 55%,transparent);
  --fg: #1a1730;
  --muted: rgba(26,23,48,.66);
  --rim: rgba(255,255,255,.8);
  --active: oklch(0.66 0.18 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  overflow: hidden;
  background: #dfe6f5;
}

.lg-15:has(#lg-15-theme:checked) {
  --surface: color-mix(in oklab,white 10%,transparent);
  --fg: #f2f0fa;
  --muted: rgba(255,255,255,.7);
  --rim: rgba(255,255,255,.3);
  background: #0e0b1a;
}

.lg-15:has(#lg-15-collapse:checked) {
  --w: 78px;
}

.lg-15__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.lg-15__blobs span {
  position: absolute;
  border-radius: 50%;
  filter: blur(40px);
  opacity: .7;
  animation: lg-15-float 14s ease-in-out infinite;
}

.lg-15__blobs span:nth-child(1) {
  width: 280px;
  height: 280px;
  background: oklch(0.7 0.2 300);
  top: -40px;
  left: 120px;
}

.lg-15__blobs span:nth-child(2) {
  width: 240px;
  height: 240px;
  background: oklch(0.72 0.18 200);
  bottom: -30px;
  left: 40px;
  animation-delay: -4s;
}

.lg-15__blobs span:nth-child(3) {
  width: 300px;
  height: 300px;
  background: oklch(0.72 0.17 40);
  top: 40%;
  right: -40px;
  animation-delay: -8s;
}

.lg-15__side {
  position: relative;
  z-index: 2;
  width: var(--w);
  flex: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 18px 14px;
  margin: 16px;
  border-radius: 22px;
  background: var(--surface);
  border: 1px solid var(--rim);
  box-shadow: inset 0 1px 0 var(--rim),0 30px 60px -30px rgba(0,0,0,.4);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  transition: width .35s cubic-bezier(.4,0,.2,1);
}

.lg-15__top {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 10px 14px;
  color: var(--fg);
}

.lg-15__logo {
  font-size: 22px;
  color: var(--active);
  flex: none;
}

.lg-15__brand,
.lg-15__t {
  font-weight: 700;
  white-space: nowrap;
  overflow: hidden;
  transition: opacity .2s;
}

.lg-15__brand {
  font-size: 19px;
}

.lg-15:has(#lg-15-collapse:checked) .lg-15__brand,
.lg-15:has(#lg-15-collapse:checked) .lg-15__t {
  opacity: 0;
}

.lg-15__nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.lg-15__link,
.lg-15__toggle {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  color: var(--muted);
  padding: 11px 12px;
  border-radius: 12px;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.lg-15__i {
  font-size: 17px;
  flex: none;
  width: 20px;
  text-align: center;
}

.lg-15__link:hover,
.lg-15__toggle:hover {
  background: color-mix(in oklab,var(--fg) 10%,transparent);
  color: var(--fg);
}

.lg-15__link[aria-current=page] {
  background: var(--active);
  color: #fff;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 6px 16px -8px var(--active);
}

.lg-15__link:focus-visible,
.lg-15__toggle:focus-within {
  outline: 3px solid var(--active);
  outline-offset: 2px;
}

.lg-15__foot {
  display: flex;
  flex-direction: column;
  gap: 4px;
  border-top: 1px solid var(--rim);
  padding-top: 10px;
}

.lg-15__stage {
  position: relative;
  z-index: 2;
  flex: 1;
  padding: 60px 40px;
  color: var(--fg);
}

.lg-15__stage h3 {
  font-size: 30px;
  font-weight: 800;
  margin-bottom: 10px;
}

.lg-15__stage p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--muted);
  max-width: 44ch;
}

@keyframes lg-15-float {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(24px,-20px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-15__side {
    transition: none;
  }

  .lg-15__blobs span {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two hidden checkboxes plus the CSS :has() selector re-tint the whole shell (dark mode) and shrink the sidebar (collapse) from the parent, with capsule aria-current active states. */
```
