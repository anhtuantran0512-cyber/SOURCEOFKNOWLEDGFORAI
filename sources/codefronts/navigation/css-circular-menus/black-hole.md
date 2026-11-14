---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/black-hole/"
title: "Vortex / Particle Expand Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "Menu items that arrive by spiral: each option swings in along a decaying orbit — rotation and radius animated together — while a cloud of particles swirls…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vortex / Particle Expand Menu
Source: https://codefronts.com/navigation/css-circular-menus/black-hole/

Menu items that arrive by spiral: each option swings in along a decaying orbit — rotation and radius animated together — while a cloud of particles swirls around the vortex core. The spiral trajectory is two nested elements, each animating one axis; the composition does the math for you. Maximum drama for launch screens, games and creative sites.
## HTML
```html
<section class="ccm-24" aria-label="Vortex particle menu demo">
  <div class="ccm-24__stage">
    <div class="ccm-24__field" aria-hidden="true"></div>
    <nav class="ccm-24__vortex" style="--n:5" aria-label="Galaxy menu">
      <ul class="ccm-24__arms" id="ccm24-menu">
        <li class="ccm-24__arm" style="--i:0"><a class="ccm-24__rider" href="#worlds">Worlds</a></li>
        <li class="ccm-24__arm" style="--i:1"><a class="ccm-24__rider" href="#fleet">Fleet</a></li>
        <li class="ccm-24__arm" style="--i:2"><a class="ccm-24__rider" href="#crew">Crew</a></li>
        <li class="ccm-24__arm" style="--i:3"><a class="ccm-24__rider" href="#codex">Codex</a></li>
        <li class="ccm-24__arm" style="--i:4"><a class="ccm-24__rider" href="#signal">Signal</a></li>
      </ul>
      <button type="button" class="ccm-24__core" aria-expanded="false" aria-controls="ccm24-menu"><span></span><b>Enter</b></button>
    </nav>
  </div>
</section>
```
## CSS
```css
.ccm-24,
.ccm-24 *,
.ccm-24 *::before,
.ccm-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-24 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 45%,oklch(0.28 0.09 305),oklch(0.15 0.05 290) 72%);
  --brand: oklch(0.75 0.17 310);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #fff;
}

.ccm-24__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 45%,oklch(0.28 0.09 305),oklch(0.15 0.05 290) 72%);
  overflow: hidden;
}

.ccm-24__field {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.ccm-24__field span {
  position: absolute;
  left: 50%;
  top: 50%;
  width: var(--s);
  height: var(--s);
  border-radius: 50%;
  background: var(--c);
  opacity: .55;
  filter: blur(.5px);
  animation: ccm24-orbit var(--dur) linear infinite;
  animation-delay: var(--del);
}

.ccm-24__vortex {
  position: relative;
  width: 120px;
  height: 120px;
  display: grid;
  place-items: center;
}

.ccm-24__arms {
  position: absolute;
  inset: 0;
  list-style: none;
}

.ccm-24__arm {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --slot: calc((360deg / var(--n)) * var(--i) - 90deg);
  rotate: calc(var(--slot) - 220deg);
  transition: rotate .9s cubic-bezier(.3,1.15,.35,1);
  transition-delay: calc(var(--i) * 55ms);
}

.ccm-24__vortex.is-open .ccm-24__arm {
  rotate: var(--slot);
}

.ccm-24__rider {
  pointer-events: auto;
  position: absolute;
  display: grid;
  place-items: center;
  min-width: 74px;
  padding: 12px 16px;
  border-radius: 999px;
  background: oklch(1 0 0 / .08);
  border: 1px solid oklch(0.8 0.14 310 / .45);
  backdrop-filter: blur(4px);
  color: #fff;
  text-decoration: none;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .05em;
  translate: 0 0;
  rotate: calc(220deg - var(--slot));
  opacity: 0;
  visibility: hidden;
  transition: translate .9s cubic-bezier(.25,.9,.3,1),rotate .9s cubic-bezier(.3,1.15,.35,1),opacity .45s,visibility 0s .9s;
  transition-delay: calc(var(--i) * 55ms);
}

.ccm-24__vortex.is-open .ccm-24__rider {
  translate: 158px 0;
  rotate: calc(0deg - var(--slot));
  opacity: 1;
  visibility: visible;
  transition: translate .9s cubic-bezier(.25,.9,.3,1),rotate .9s cubic-bezier(.3,1.15,.35,1),opacity .45s,visibility 0s;
  transition-delay: calc(var(--i) * 55ms);
}

.ccm-24__vortex:not(.is-open) .ccm-24__arm,
.ccm-24__vortex:not(.is-open) .ccm-24__rider {
  transition-duration: .35s;
  transition-delay: 0s;
}

.ccm-24__rider:hover,
.ccm-24__rider:focus-visible {
  background: var(--brand);
  color: oklch(0.2 0.05 300);
  outline: none;
}

.ccm-24__rider:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.ccm-24__core {
  position: relative;
  z-index: 2;
  display: grid;
  place-items: center;
  width: 112px;
  height: 112px;
  border: none;
  border-radius: 50%;
  background: radial-gradient(circle at 40% 32%,oklch(0.5 0.16 310),oklch(0.3 0.12 295) 70%);
  color: #fff;
  cursor: pointer;
  box-shadow: 0 0 70px -8px oklch(0.7 0.18 310 / .65),inset 0 1px 0 oklch(1 0 0 / .25);
}

.ccm-24__core b {
  position: relative;
  font-size: 14px;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.ccm-24__core span {
  position: absolute;
  inset: -9px;
  border-radius: 50%;
  border: 1px dashed oklch(0.8 0.14 310 / .5);
  animation: ccm24-spin 14s linear infinite;
}

.ccm-24__core:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 5px;
}

@keyframes ccm24-spin {
  to {
    rotate: 360deg;
  }
}

@keyframes ccm24-orbit {
  from {
    transform: rotate(var(--a0)) translateX(var(--r));
  }

  to {
    transform: rotate(calc(var(--a0) + 360deg)) translateX(var(--r));
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccm-24 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
    animation: none !important;
  }

  .ccm-24__field {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.querySelector('.ccm-24__stage');
  const field = stage.querySelector('.ccm-24__field');
  const vortex = stage.querySelector('.ccm-24__vortex');
  const core = vortex.querySelector('.ccm-24__core');
  const hues = [310, 280, 200, 340];
  for (let i = 0; i < 22; i++) {
    const p = document.createElement('span');
    p.style.setProperty('--s', (2 + Math.random() * 4).toFixed(1) + 'px');
    p.style.setProperty('--r', (60 + Math.random() * 190).toFixed(0) + 'px');
    p.style.setProperty('--a0', (Math.random() * 360).toFixed(0) + 'deg');
    p.style.setProperty('--dur', (9 + Math.random() * 22).toFixed(1) + 's');
    p.style.setProperty('--del', (-Math.random() * 20).toFixed(1) + 's');
    p.style.setProperty('--c', 'oklch(0.8 0.14 ' + hues[i % hues.length] + ')');
    field.append(p);
  }
  core.addEventListener('click', () => {
    const open = vortex.classList.toggle('is-open');
    core.setAttribute('aria-expanded', String(open));
    core.querySelector('b').textContent = open ? 'Close' : 'Enter';
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && vortex.classList.contains('is-open')) { core.click(); core.focus(); }
  });
})();
```
