---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/framer-motion-spring-menu/"
title: "Framer-Motion Spring Menu"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A glass navbar whose active indicator glides between links on a physics-based spring — the Framer Motion `layoutId` shared-element feel, reproduced with a…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Framer-Motion Spring Menu
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/framer-motion-spring-menu/

A glass navbar whose active indicator glides between links on a physics-based spring — the Framer Motion `layoutId` shared-element feel, reproduced with a single animated pill that measures each link and springs to it. Hovering previews the target; the active state commits it.
## HTML
```html
<section class="nb-10" aria-label="Framer Motion style spring menu demo">
  <nav class="nb-10__bar" id="nb-10-bar" aria-label="Primary">
    <span class="nb-10__pill" id="nb-10-pill" aria-hidden="true"></span>
    <a class="nb-10__link" href="#nb-10" aria-current="page">Overview</a>
    <a class="nb-10__link" href="#nb-10">Analytics</a>
    <a class="nb-10__link" href="#nb-10">Reports</a>
    <a class="nb-10__link" href="#nb-10">Settings</a>
  </nav>
</section>
```
## CSS
```css
.nb-10,
.nb-10 *,
.nb-10 *::before,
.nb-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-10 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 30deg at 40% 40%,#00dbde,#fc00ff,#00dbde);
  background-size: 200% 200%;
  animation: nb-10-bg 18s ease-in-out infinite;
}

@keyframes nb-10-bg {
  50% {
    background-position: 100% 100%;
  }
}

.nb-10__bar {
  position: relative;
  display: flex;
  gap: 4px;
  padding: 8px;
  border-radius: 9999px;
  isolation: isolate;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 20px 44px -22px rgba(0,0,0,.55);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.nb-10__pill {
  position: absolute;
  top: 8px;
  bottom: 8px;
  left: 8px;
  width: 96px;
  border-radius: 9999px;
  background: rgba(255,255,255,.24);
  border: 1px solid rgba(255,255,255,.5);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7);
  z-index: 0;
  transition: left .5s cubic-bezier(.34,1.56,.5,1),width .5s cubic-bezier(.34,1.56,.5,1);
}

.nb-10__link {
  position: relative;
  z-index: 1;
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 18px;
  border-radius: 9999px;
  text-decoration: none;
  color: #fff;
  font-size: 14.5px;
  font-weight: 600;
  transition: color .2s;
}

.nb-10__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-10,
    .nb-10__pill {
    animation: none;
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const bar = document.querySelector('#nb-10-bar');
  const pill = document.querySelector('#nb-10-pill');
  if (!bar || !pill) return;
  const links = [...bar.querySelectorAll('.nb-10__link')];
  let active = links.find(l => l.hasAttribute('aria-current')) || links[0];
  function move(el){
    const b = bar.getBoundingClientRect(), r = el.getBoundingClientRect();
    pill.style.left = (r.left - b.left) + 'px';
    pill.style.width = r.width + 'px';
  }
  links.forEach(l => {
    l.addEventListener('pointerenter', () => move(l));
    l.addEventListener('focus', () => move(l));
    l.addEventListener('click', e => { e.preventDefault(); links.forEach(x => x.removeAttribute('aria-current')); l.setAttribute('aria-current','page'); active = l; });
  });
  bar.addEventListener('pointerleave', () => move(active));
  requestAnimationFrame(() => move(active));
  addEventListener('resize', () => move(active));
})();
```
