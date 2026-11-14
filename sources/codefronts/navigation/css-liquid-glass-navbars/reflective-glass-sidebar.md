---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/reflective-glass-sidebar/"
title: "Reflective Glass Sidebar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A vertical glass sidebar that dynamically reflects the colour of whatever section is in view — scroll the content and the sidebar's tint, glow and active…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reflective Glass Sidebar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/reflective-glass-sidebar/

A vertical glass sidebar that dynamically reflects the colour of whatever section is in view — scroll the content and the sidebar's tint, glow and active accent shift to match the adjacent panel, as if the glass were picking up the light of the room behind it.
## HTML
```html
<section class="nb-18" aria-label="Reflective glass sidebar demo">
  <nav class="nb-18__side" id="nb-18-side" aria-label="Primary" style="--reflect:#5b8cff">
    <span class="nb-18__glow" aria-hidden="true"></span>
    <span class="nb-18__logo" aria-hidden="true">◈</span>
    <a class="nb-18__item" href="#nb-18" aria-current="page" aria-label="Home">⌂</a>
    <a class="nb-18__item" href="#nb-18" aria-label="Discover">◎</a>
    <a class="nb-18__item" href="#nb-18" aria-label="Media">▤</a>
    <a class="nb-18__item" href="#nb-18" aria-label="Settings">⚙</a>
  </nav>
  <div class="nb-18__scroll" id="nb-18-scroll">
    <div class="nb-18__panel" data-color="#5b8cff" style="--c:#5b8cff"><h3>Ocean</h3></div>
    <div class="nb-18__panel" data-color="#ff5ea8" style="--c:#ff5ea8"><h3>Bloom</h3></div>
    <div class="nb-18__panel" data-color="#38e8c6" style="--c:#38e8c6"><h3>Mint</h3></div>
    <div class="nb-18__panel" data-color="#ffb03a" style="--c:#ffb03a"><h3>Amber</h3></div>
  </div>
</section>
```
## CSS
```css
.nb-18,
.nb-18 *,
.nb-18 *::before,
.nb-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-18 {
  position: relative;
  display: flex;
  width: 100%;
  min-height: 100vh;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0a0c14;
  overflow: hidden;
}

.nb-18__side {
  position: relative;
  z-index: 5;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 74px;
  padding: 18px 0;
  overflow: hidden;
  color: #fff;
  background: color-mix(in oklab,var(--reflect) 16%,rgba(255,255,255,.06));
  border-right: 1px solid color-mix(in oklab,var(--reflect) 40%,rgba(255,255,255,.14));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  transition: background .5s,border-color .5s;
}

.nb-18__glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: radial-gradient(60px 120px at 50% 0,color-mix(in oklab,var(--reflect) 80%,transparent),transparent 70%);
  opacity: .6;
  transition: background .5s;
  pointer-events: none;
}

.nb-18__logo {
  position: relative;
  z-index: 1;
  font-size: 22px;
  margin-bottom: 8px;
  color: color-mix(in oklab,var(--reflect) 60%,white);
}

.nb-18__item {
  position: relative;
  z-index: 1;
  width: 46px;
  height: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 14px;
  text-decoration: none;
  color: rgba(255,255,255,.8);
  font-size: 19px;
  transition: background .3s,color .3s;
}

.nb-18__item:hover {
  color: #fff;
  background: rgba(255,255,255,.12);
}

.nb-18__item[aria-current] {
  color: #fff;
  background: color-mix(in oklab,var(--reflect) 55%,transparent);
  box-shadow: 0 0 18px -2px color-mix(in oklab,var(--reflect) 70%,transparent);
}

.nb-18__item:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-18__scroll {
  flex: 1;
  height: 100vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
}

.nb-18__panel {
  height: 100vh;
  min-height: 520px;
  scroll-snap-align: start;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 40%,color-mix(in oklab,var(--c) 55%,#0a0c14),#0a0c14 75%);
}

.nb-18__panel h3 {
  color: #fff;
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -.02em;
  text-shadow: 0 2px 20px rgba(0,0,0,.4);
}

@media (prefers-reduced-motion: reduce) {
  .nb-18__side,
    .nb-18__glow {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const side = document.querySelector('#nb-18-side');
  const scroll = document.querySelector('#nb-18-scroll');
  if (!side || !scroll) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) side.style.setProperty('--reflect', e.target.dataset.color); });
  }, { root: scroll, threshold: .6 });
  scroll.querySelectorAll('.nb-18__panel').forEach(p => io.observe(p));
})();
```
